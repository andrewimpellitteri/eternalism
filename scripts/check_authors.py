#!/usr/bin/env python3
"""Compare knowledge-record author lists with Crossref (for a DOI) or the arXiv API
(arXiv-only records). Standard library only; read-only. Catches the failure mode the
identifier check cannot: plausible but wrong names.

    python3 scripts/check_authors.py [paths ...] [--strict]

FLAG  a recorded author whose family name is not in the source, or whose given name
      disagrees with the source's.
WARN  an authors entry holding several names in one string (cannot be compared).
Exit status is 1 with --strict when anything is flagged. Default paths: knowledge/**/*.jsonl.
"""
import argparse
import glob
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

UA = {"User-Agent": "eternalism-check-authors/1 (research audit)"}
SKIP = re.compile(r"\bet al\b|collaboration|consortium|\bteam\b|\bgroup\b", re.I)
SUFFIX = re.compile(r",?\s+(jr\.?|sr\.?|ii|iii|iv)$", re.I)
PARTICLES = {"di", "de", "van", "von", "da", "del", "der", "le", "la", "du", "dos"}
TRANSLIT = (("ae", "a"), ("oe", "o"), ("ue", "u"))
NS = {"a": "http://www.w3.org/2005/Atom"}


def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z ]", " ", s).split()


def fold(family):
    """Family-name key that treats Höhn/Hoehn and Müller/Mueller as equal."""
    key = family.replace(" ", "")
    for a, b in TRANSLIT:
        key = key.replace(a, b)
    return key


def split_name(name):
    name = SUFFIX.sub("", re.sub(r"\(.*?\)", "", name)).strip()
    if "," in name:
        family, given = [p.strip() for p in name.split(",", 1)]
        return " ".join(norm(family)), norm(given)
    parts = name.split()
    if not parts:
        return "", []
    family, given = [parts[-1]], parts[:-1]
    while given and given[-1].lower() in PARTICLES:
        family.insert(0, given.pop())
    return " ".join(norm(" ".join(family))), norm(" ".join(given))


def packed(name):
    """True when one authors entry holds several people."""
    return name.count(",") >= 2 or bool(re.search(r",\s*\S+\s+\S+,", name)) or " and " in name


def given_ok(mine, theirs):
    """Compare first full given names when both sides have one; otherwise initials."""
    if not mine or not theirs:
        return True
    mine_full = [t for t in mine if len(t) > 1]
    theirs_full = [t for t in theirs if len(t) > 1]
    if mine_full and theirs_full:
        return mine_full[0] in theirs_full or theirs_full[0] in mine_full
    return bool({t[0] for t in mine} & {t[0] for t in theirs})


def compare(recorded, source):
    """Problems with a recorded author list against [(family, [given tokens])]."""
    problems = []
    by_key = {fold(f): g for f, g in source}
    for name in recorded:
        if not isinstance(name, str) or SKIP.search(name):
            continue
        if packed(name):
            problems.append(("WARN", f"{name!r}: several names in one entry"))
            continue
        fam, giv = split_name(name)
        if not fam:
            continue
        theirs = by_key.get(fold(fam))
        if theirs is None:
            last = fold(fam.split()[-1])
            theirs = next((g for fam2, g in source if fam2 and fold(fam2.split()[-1]) == last), None)
        if theirs is None:
            problems.append(("FLAG", f"{name!r}: family name not in source"))
        elif not given_ok(giv, theirs):
            problems.append(("FLAG", f"{name!r}: source given name {' '.join(theirs)!r}"))
    return problems



def get(url):
    for attempt in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                time.sleep(0.4)
                return r.read()
        except urllib.error.HTTPError as exc:
            if exc.code != 429 or attempt == 4:
                raise
            time.sleep(5 * 2 ** attempt)


def crossref(doi):
    m = json.loads(get("https://api.crossref.org/works/" + urllib.parse.quote(doi)))["message"]
    return [(" ".join(norm(a.get("family", ""))), norm(a.get("given", ""))) for a in m.get("author", [])]


def arxiv(ids):
    def fetch(chunk):
        try:
            return [get("https://export.arxiv.org/api/query?max_results=100&id_list=" + ",".join(chunk))]
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
            return [] if len(chunk) == 1 else [x for one in chunk for x in fetch([one])]
    out = {}
    for i in range(0, len(ids), 50):
        for xml in fetch(ids[i:i + 50]):
            for e in ET.fromstring(xml).findall("a:entry", NS):
                aid = re.sub(r"v\d+$", "", e.find("a:id", NS).text.rsplit("/abs/", 1)[-1])
                out[aid] = [split_name(a.find("a:name", NS).text) for a in e.findall("a:author", NS)]
        time.sleep(3)
    return out


def identifiers(r):
    blob = " ".join(str(r.get(k, "")) for k in ("url", "version", "doi"))
    doi = re.search(r"10\.\d{4,9}/[^\s;,)\"']+", blob)
    doi = doi.group(0).rstrip(".") if doi and not doi.group(0).startswith("10.48550") else None
    aid = re.search(r"arxiv\.org/(?:abs|html|pdf)/([\w.\-/]+?)(?:v\d+)?(?:[\s\"']|$)|arXiv:([\w.\-/]+?)(?:v\d+)?\b", blob)
    aid = (aid.group(1) or aid.group(2)) if aid and not doi else None
    return doi, aid


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("paths", nargs="*", default=["knowledge/**/*.jsonl"])
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()
    recs = []
    for pattern in a.paths:
        for path in sorted(glob.glob(pattern, recursive=True)):
            for n, line in enumerate(open(path), 1):
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if isinstance(r, dict) and isinstance(r.get("authors"), list) and r["authors"]:
                    recs.append((path, n, r, *identifiers(r)))
    names = arxiv(sorted({aid for *_, aid in recs if aid}))
    flagged = checked = 0
    for path, n, r, doi, aid in recs:
        try:
            source = crossref(doi) if doi else names.get(aid) if aid else None
        except (urllib.error.URLError, TimeoutError, KeyError, ValueError) as exc:
            print(f"SKIP  {r.get('id')} [{path}:{n}] lookup failed: {exc}")
            continue
        if not source:
            continue
        checked += 1
        problems = compare(r["authors"], source)
        if problems:
            flagged += any(level == "FLAG" for level, _ in problems)
            via = f"doi {doi}" if doi else f"arXiv {aid}"
            print(f"{'FLAG' if any(l == 'FLAG' for l, _ in problems) else 'WARN'}  {r.get('id')} [{path}:{n}] via {via}")
            for _, text in problems:
                print("      " + text)
    print(f"\n{len(recs)} records with authors; {checked} checked against a source; {flagged} flagged")
    return 1 if a.strict and flagged else 0


if __name__ == "__main__":
    sys.exit(main())
