#!/usr/bin/env python3
"""Check knowledge-base source records against the contract and, optionally,
against arXiv and Crossref. Standard library only.

    python3 scripts/check_sources.py                      # offline, knowledge/
    python3 scripts/check_sources.py --online             # plus identifier checks
    python3 scripts/check_sources.py --online .worktrees/kb-causal-sets/knowledge

Offline: JSON validity, required fields, read_depth vocabulary, full-text extra
fields, ID collisions within and across files. Online: every arXiv ID must
resolve (via its DataCite DOI) and match the recorded title, a stated arXiv
version must exist; every DOI must resolve in Crossref and
match the title, and recorded pages/year must agree when both sides state them.

A pass means the identifiers point at the recorded titles. It does not show that
a source was read, that a locator is right, or that any extracted claim is true.
"""

import argparse
import difflib
import html
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".agent-runtime" / "source-check-cache.json"
UA = "eternalism-source-check/0.1 (research bibliography audit)"

REQUIRED = ["id", "title", "url", "checked_on", "read_depth", "kind", "relevance", "limits"]
DEPTHS = {"discovery", "abstract", "full-text", "reproduced", "code-audited"}
FULL_TEXT_EXTRA = ["authors", "version", "assumptions", "conclusion", "proof_status",
                   "dependencies", "related_source_ids", "open_questions"]
LOCATOR_KEYS = ["locator", "section_locator", "locators"]

ARXIV_RE = re.compile(
    r"arxiv\.org/(?:abs|html|pdf)/((?:\d{4}\.\d{4,5}|[a-z\-]+(?:\.[A-Z]{2})?/\d{7})(?:v\d+)?)",
    re.I)
DOI_RE = re.compile(r"\b(10\.\d{4,9}/[^\s\"'<>;,]+)", re.I)
PAGES_RE = re.compile(r"pp?\.\s*(\d+)\s*[-–]\s*(\d+)")
TITLE_MIN = 0.85


def norm_title(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"<[^>]+>", "", s)  # Crossref titles may carry MathML/JATS markup
    s = re.sub(r"\$[^$]*\$|\\[a-zA-Z]+|[{}]", " ", s)
    s = re.sub(r"[^a-z0-9 ]+", " ", s.lower())
    return " ".join(s.split())


def title_score(a, b):
    a, b = norm_title(a), norm_title(b)
    if not a or not b:
        return 0.0
    # Records often drop or add a subtitle; accept a clean prefix match.
    if a.startswith(b) or b.startswith(a):
        if min(len(a), len(b)) >= 15:
            return 1.0
    return difflib.SequenceMatcher(None, a, b).ratio()


def clean_doi(d):
    d = urllib.parse.unquote(d).rstrip(".)]")
    return d.lower()


class Report:
    def __init__(self):
        self.items = []

    def add(self, level, where, rid, msg):
        self.items.append((level, where, rid, msg))

    def count(self, level):
        return sum(1 for i in self.items if i[0] == level)


def find_files(paths):
    out = []
    for p in paths:
        p = Path(p)
        if p.is_file():
            out.append(p)
        elif p.is_dir():
            out.extend(sorted(p.rglob("*sources.jsonl")))
    seen, uniq = set(), []
    for f in out:
        r = f.resolve()
        if r not in seen:
            seen.add(r)
            uniq.append(f)
    return uniq


def rel(f):
    try:
        return str(f.resolve().relative_to(ROOT))
    except ValueError:
        return str(f)


def load(files, rep):
    records = []
    for f in files:
        where = rel(f)
        ids = set()
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                r = json.loads(line)
            except json.JSONDecodeError as e:
                rep.add("ERROR", f"{where}:{n}", "-", f"invalid JSON: {e.msg}")
                continue
            if not isinstance(r, dict):
                rep.add("ERROR", f"{where}:{n}", "-", "record is not an object")
                continue
            rid = r.get("id", "-")
            if rid in ids:
                rep.add("ERROR", f"{where}:{n}", rid, "duplicate id within file")
            ids.add(rid)
            records.append((where, n, r))
    return records


def check_offline(records, rep):
    by_id = {}
    for where, n, r in records:
        rid = r.get("id", "-")
        loc = f"{where}:{n}"
        missing = [k for k in REQUIRED if not r.get(k)]
        if missing:
            rep.add("ERROR", loc, rid, "missing required: " + ", ".join(missing))
        depth = r.get("read_depth")
        if depth and depth not in DEPTHS:
            rep.add("ERROR", loc, rid, f"read_depth {depth!r} not in contract")
        if depth == "full-text":
            gaps = [k for k in FULL_TEXT_EXTRA if not r.get(k)]
            if not any(r.get(k) for k in LOCATOR_KEYS):
                gaps.append("locator")
            if gaps:
                rep.add("WARN", loc, rid, "full-text record lacks: " + ", ".join(gaps))
        if r.get("checked_on") and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(r["checked_on"])):
            rep.add("WARN", loc, rid, f"checked_on not ISO date: {r['checked_on']!r}")
        url = str(r.get("url", ""))
        if url and not url.startswith(("http://", "https://")):
            rep.add("WARN", loc, rid, f"url is not http(s): {url!r}")
        if depth in ("full-text", "reproduced") and arxiv_ids(r):
            if not any(re.search(r"v\d+$", a) for a in arxiv_ids(r)) and not re.search(
                    r"\bv\d+\b", str(r.get("version", ""))):
                rep.add("WARN", loc, rid, "arXiv full-text record has no exact version")
        by_id.setdefault(rid, []).append((loc, r))
    for rid, hits in by_id.items():
        files = {h[0].rsplit(":", 1)[0] for h in hits}
        if len(files) < 2:
            continue
        titles = {norm_title(h[1].get("title", "")) for h in hits}
        depths = {h[1].get("read_depth") for h in hits}
        where = ", ".join(sorted(h[0] for h in hits))
        if len(titles) > 1:
            rep.add("ERROR", where, rid, "same id names different titles across files")
        elif len(depths) > 1:
            rep.add("WARN", where, rid,
                    "copied record diverges in read_depth: " + ", ".join(sorted(map(str, depths))))
        else:
            rep.add("INFO", where, rid, "record copied across files; reference the id instead")


def arxiv_ids(r):
    found = []
    for k in ("url", "text_url"):
        for m in ARXIV_RE.finditer(str(r.get(k, ""))):
            found.append(m.group(1).removesuffix(".pdf"))
    return sorted(set(found))


def dois(r):
    # Only url and version: limits often quote superseded, wrong DOIs on purpose.
    found = []
    for k in ("url", "version", "doi"):
        for m in DOI_RE.finditer(str(r.get(k, ""))):
            found.append(clean_doi(m.group(1)))
    return sorted(set(found))


class Net:
    def __init__(self, refresh):
        self.cache = {}
        if CACHE.exists() and not refresh:
            try:
                self.cache = json.loads(CACHE.read_text())
            except (OSError, json.JSONDecodeError):
                self.cache = {}
        self.last = {}

    def save(self):
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        CACHE.write_text(json.dumps(self.cache, indent=1, sort_keys=True))

    def get(self, url, host, gap, tries=3):
        status = "unreachable"
        for attempt in range(tries):
            wait = self.last.get(host, 0) + gap * (attempt + 1) - time.time()
            if wait > 0:
                time.sleep(wait)
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    return resp.status, resp.read()
            except urllib.error.HTTPError as e:
                if e.code not in (429, 500, 502, 503, 504):
                    return e.code, b""
                status = e.code
            except (urllib.error.URLError, TimeoutError, OSError):
                status = "unreachable"
            finally:
                self.last[host] = time.time()
        return status, b""

    def arxiv(self, ids):
        # Titles come from arXiv's DataCite DOIs (10.48550/arXiv.ID); export.arxiv.org
        # is often slow or unreachable. A stated version is checked on arxiv.org/abs.
        for i in ids:
            key = f"arxiv:{i}"
            if not self.cache.get(key, {"transient": True}).get("transient"):
                continue
            base = re.sub(r"v\d+$", "", i)
            status, body = self.get("https://api.datacite.org/dois/10.48550/arxiv." + base,
                                    "datacite", 0.3)
            if status == 404:
                self.cache[key] = {"status": "not found"}
                continue
            if status != 200:
                self.cache[key] = {"status": f"datacite {status}", "transient": True}
                continue
            attrs = json.loads(body)["data"]["attributes"]
            hit = {"status": "ok", "title": " ".join(t.get("title", "") for t in attrs["titles"][:1]),
                   "year": attrs.get("publicationYear")}
            if base != i:
                vstatus, vbody = self.get(f"https://arxiv.org/abs/{i}", "arxiv", 1.0)
                m = re.search(rb'<meta name="citation_title" content="([^"]+)"', vbody or b"")
                if m:  # Papers are retitled between versions; keep the cited one.
                    hit["version_title"] = html.unescape(m.group(1).decode(errors="replace"))
                if vstatus == 404:
                    hit = {"status": f"version {i[len(base):]} does not exist"}
                elif vstatus != 200:
                    hit = {"status": f"version check http {vstatus}", "transient": True,
                           "title": hit["title"]}
            self.cache[key] = hit
        return {i: self.cache[f"arxiv:{i}"] for i in ids}

    def crossref(self, doi):
        key = f"doi:{doi}"
        if key not in self.cache or self.cache[key].get("transient"):
            url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/")
            status, body = self.get(url, "crossref", 1.0)
            if status == 200:
                m = json.loads(body)["message"]
                issued = (m.get("issued", {}).get("date-parts") or [[None]])[0][0]
                self.cache[key] = {"status": "ok", "title": " ".join(m.get("title") or [""]),
                                   "page": m.get("page"), "year": issued,
                                   "container": " ".join(m.get("container-title") or [""])}
            elif status == 404:
                self.cache[key] = {"status": "not found"}
            else:
                self.cache[key] = {"status": f"http {status}", "transient": True}
        return self.cache[key]


def check_online(records, rep, refresh):
    net = Net(refresh)
    all_arxiv = sorted({a for _, _, r in records for a in arxiv_ids(r)})
    try:
        ax = net.arxiv(all_arxiv)
        n_doi = 0
        for where, n, r in records:
            rid, loc, title = r.get("id", "-"), f"{where}:{n}", r.get("title", "")
            # Each identifier's own titles; a mismatch is an error only when no other
            # identifier in the record matches the recorded title either.
            own, problems = {}, []
            for a in arxiv_ids(r):
                hit = ax[a]
                if hit["status"] != "ok":
                    rep.add("WARN" if hit.get("transient") else "ERROR", loc, rid,
                            f"arXiv {a}: {hit['status']}")
                    continue
                own[f"arXiv {a}"] = [t for t in (hit.get("version_title"), hit["title"]) if t]
            ds = dois(r)
            if len(ds) > 1:
                rep.add("WARN", loc, rid, "several DOIs in url/version: " + ", ".join(ds))
            doi_hits = {}
            for d in ds:
                n_doi += 1
                hit = net.crossref(d)
                if hit["status"] != "ok":
                    rep.add("ERROR" if hit["status"] == "not found" else "WARN", loc, rid,
                            f"DOI {d}: {hit['status']}")
                    continue
                doi_hits[d] = hit
                own[f"DOI {d}"] = [hit["title"]]
            matched = {k for k, ts in own.items() if any(title_score(title, t) >= TITLE_MIN for t in ts)}
            for k, ts in own.items():
                if k in matched:
                    continue
                generic = len(norm_title(ts[0]).split()) <= 3 or re.search(r"\brepl(y|ies)\b", ts[0], re.I)
                if matched or generic:
                    why = f"matches {', '.join(sorted(matched))}" if matched else "Crossref title is generic"
                    rep.add("WARN", loc, rid, f"{k} title is {ts[0]!r}; record title {why}")
                else:
                    rep.add("ERROR", loc, rid, f"{k} title is {ts[0]!r}")
            for d, hit in doi_hits.items():
                ver = str(r.get("version", ""))
                pm = PAGES_RE.search(ver)
                if pm and hit.get("page"):
                    cp = re.findall(r"\d+", hit["page"])
                    if len(cp) >= 2 and [pm.group(1), pm.group(2)] != cp[:2] or (
                            len(cp) == 1 and pm.group(1) != cp[0]):
                        rep.add("ERROR", loc, rid, f"pages {pm.group(1)}-{pm.group(2)} "
                                f"but Crossref has {hit['page']}")
                years = {int(y) for y in re.findall(r"\b(1[89]\d\d|20\d\d)\b", ver)}
                if r.get("year"):
                    years.add(int(str(r["year"])[:4]))
                if years and hit.get("year") and all(abs(y - hit["year"]) > 1 for y in years):
                    rep.add("WARN", loc, rid, f"year {sorted(years)} but Crossref issued {hit['year']}")
            if not arxiv_ids(r) and not dois(r):
                rep.add("INFO", loc, rid, "no arXiv ID or DOI; identifier not machine-checked")
    finally:
        net.save()
    return len(all_arxiv), n_doi


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("paths", nargs="*", default=[str(ROOT / "knowledge")])
    ap.add_argument("--online", action="store_true", help="resolve arXiv IDs and DOIs")
    ap.add_argument("--refresh", action="store_true", help="ignore the lookup cache")
    ap.add_argument("--info", action="store_true", help="also print INFO lines")
    ap.add_argument("--strict", action="store_true", help="exit nonzero on warnings")
    a = ap.parse_args()

    rep = Report()
    files = find_files(a.paths)
    if not files:
        print("no sources.jsonl files found", file=sys.stderr)
        return 2
    records = load(files, rep)
    check_offline(records, rep)
    checked = ""
    if a.online:
        n_ax, n_doi = check_online(records, rep, a.refresh)
        checked = f"; {n_ax} arXiv IDs and {n_doi} DOI lookups checked"

    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    for level, where, rid, msg in sorted(rep.items, key=lambda i: (order[i[0]], i[1])):
        if level == "INFO" and not a.info:
            continue
        print(f"{level:5} {rid}  [{where}]\n      {msg}")
    print(f"\n{len(files)} files, {len(records)} records{checked}: "
          f"{rep.count('ERROR')} errors, {rep.count('WARN')} warnings, {rep.count('INFO')} info")
    if rep.count("ERROR") or (a.strict and rep.count("WARN")):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
