"""Mechanical author check: compare every knowledge record's author list with Crossref
(for a DOI) or the arXiv API (arXiv-only records). Standard library only; read-only on
knowledge/. Flags a recorded author whose family name is absent from the source, or
whose given name disagrees with the source's (first-initial or first-token mismatch).

    python3 research/redteam/cross-model-pilot/author_sweep.py [glob ...]
"""
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

UA = {"User-Agent": "eternalism-author-sweep/1 (research audit)"}
SKIP = re.compile(r"et al|collaboration|consortium|team|group", re.I)


def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z ]", " ", s).split()


def split_name(name):
    if "," in name:
        family, given = [p.strip() for p in name.split(",", 1)]
    else:
        parts = name.strip().split()
        family, given = (parts[-1], " ".join(parts[:-1])) if parts else ("", "")
        # Particles such as "Di", "de", "van" belong to the family name.
        while parts[:-1] and given.split() and given.split()[-1].lower() in {"di", "de", "van", "von", "da", "del", "der", "le", "la"}:
            p = given.split()
            family, given = p[-1] + " " + family, " ".join(p[:-1])
    return " ".join(norm(family)), norm(given)


def get(url):
    for attempt in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                time.sleep(0.4)  # stay well under Crossref's public rate limit
                return r.read()
        except urllib.error.HTTPError as exc:
            if exc.code != 429 or attempt == 4:
                raise
            time.sleep(5 * 2 ** attempt)


def crossref_authors(doi):
    m = json.loads(get("https://api.crossref.org/works/" + urllib.parse.quote(doi)))["message"]
    return [(" ".join(norm(a.get("family", ""))), norm(a.get("given", ""))) for a in m.get("author", [])]


def arxiv_authors(ids):
    ns = {"a": "http://www.w3.org/2005/Atom"}

    def fetch(chunk):
        try:
            return [get("https://export.arxiv.org/api/query?max_results=100&id_list=" + ",".join(chunk))]
        except urllib.error.HTTPError:  # one bad ID fails the batch; retry singly and skip it
            if len(chunk) == 1:
                print(f"SKIP  arXiv {chunk[0]}: lookup failed")
                return []
            return [x for one in chunk for x in fetch([one])]

    out = {}
    for i in range(0, len(ids), 50):
        for xml in fetch(ids[i:i + 50]):
            for e in ET.fromstring(xml).findall("a:entry", ns):
                aid = re.sub(r"v\d+$", "", e.find("a:id", ns).text.rsplit("/abs/", 1)[-1])
                out[aid] = [split_name(a.find("a:name", ns).text) for a in e.findall("a:author", ns)]
        time.sleep(3)
    return out


def compare(recorded, source):
    problems = []
    fams = {f: g for f, g in source}
    for name in recorded:
        if SKIP.search(name):
            continue
        fam, giv = split_name(name)
        match = fams.get(fam) or next((g for f, g in source if f.split()[-1:] == fam.split()[-1:]), None)
        if match is None and fam not in fams:
            problems.append(f"{name!r}: family name not in source")
            continue
        if giv and match:
            if giv[0][0] != match[0][0] or (len(giv[0]) > 1 and len(match[0]) > 1 and giv[0] != match[0]):
                problems.append(f"{name!r}: source given name {' '.join(match)!r}")
    return problems


def main():
    paths = sys.argv[1:] or ["knowledge/**/*.jsonl"]
    recs = []
    for pattern in paths:
        for f in sorted(glob.glob(pattern, recursive=True)):
            for n, line in enumerate(open(f), 1):
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if isinstance(r, dict) and r.get("authors"):
                    recs.append((f, n, r))
    arx = {}
    for f, n, r in recs:
        blob = " ".join(str(r.get(k, "")) for k in ("url", "version", "doi"))
        doi = re.search(r"10\.\d{4,9}/[^\s;,)\"']+", blob)
        aid = re.search(r"(\d{4}\.\d{4,5}|[a-z\-]+(?:\.[A-Z]{2})?/\d{7})", blob)
        r["_doi"] = doi.group(0).rstrip(".") if doi and not doi.group(0).startswith("10.48550") else None
        r["_arxiv"] = aid.group(1) if aid and not r["_doi"] else None
    arx = arxiv_authors(sorted({r["_arxiv"] for _, _, r in recs if r["_arxiv"]}))
    flagged = checked = 0
    for f, n, r in recs:
        try:
            source = crossref_authors(r["_doi"]) if r["_doi"] else arx.get(r["_arxiv"]) if r["_arxiv"] else None
        except Exception as exc:  # report and continue
            print(f"SKIP  {r['id']} [{f}:{n}] lookup failed: {exc}")
            continue
        if not source:
            continue
        checked += 1
        authors = r["authors"] if isinstance(r["authors"], list) else re.split(r";| and ", r["authors"])
        problems = compare([a for a in authors if isinstance(a, str)], source)
        if problems:
            flagged += 1
            print(f"FLAG  {r['id']} [{f}:{n}] via {'doi ' + r['_doi'] if r['_doi'] else 'arXiv ' + r['_arxiv']}")
            for p in problems:
                print("      " + p)
    print(f"\n{len(recs)} records with authors; {checked} checked against a source; {flagged} flagged")


if __name__ == "__main__":
    main()
