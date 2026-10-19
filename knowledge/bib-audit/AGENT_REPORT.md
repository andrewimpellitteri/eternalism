# AGENT_REPORT — kb-bib-repair

Status: worker submission for independent review, 2026-10-19. Not an accepted
completion. No lane `sources.jsonl` file was edited; all changes are proposals.

## Done / files

- Audited all **37 records** across `knowledge/*/sources.jsonl` and
  `knowledge/seed-sources.jsonl` that are not arXiv- or DOI-identified
  (books, JSTOR items, publisher pages, catalog scans, code repos, SEP pages),
  plus resolved `found-prior-2009` and spot-checked 19 further DOI records.
- `knowledge/bib-audit/bib-corrections.md` — main deliverable: correction table
  (record id / field / old / new / evidence URL per change), 18 verified-unchanged
  records, blocked-page register, `found-prior-2009` resolution, DOI spot-check
  appendix, reproducibility log.
- `knowledge/bib-audit/proposed-records.jsonl` — 23 proposed corrected records
  (full original fields preserved + `bib_audit_note` documenting each change).
- `knowledge/bib-audit/proposed-other-lane-fixes.jsonl` — 2 out-of-scope repairs
  as proposals only (a wrong DOI in `aqft-locality`, a title drift in `foundations`).
- `AGENT_REPORT.md` — this file.

Key repairs found: one **broken archive.org identifier** (`found-reichenbach`),
one **quarantined unidentifiable record** (`found-prior-2009`), one **wrong DOI
in a DOI-labeled record** (`aqft-bisognano-wichmann-1976` → 10.1063/1.522898),
two title corrections to exact catalog form (`found-maxwell-1993`,
`found-deasy-2015`), one canonical-URL replacement (`found-stein-1991` off
paperzz.com), four mutable GitHub URLs/repo records pinned to commit SHAs, and
ten records enriched with missing years, versions, DOIs, or authors.

## Search capability check

- OpenCode `websearch`: **failed** (2/2 attempts, "Web search cancelled").
- MCP `web-search-prime` (Code Mode): **works**; used for 4 targeted queries;
  one transient 429, retried successfully.
- `curl`/`webfetch` against public catalogs (Crossref, OpenAlex, Open Library,
  archive.org, GitHub API, SEP, Gutenberg, eprints, Scholars@Duke, AFP,
  fourmilab, INSPIRE): **works**. No credentials, no package installs, no
  config changes.

## Source coverage

- 37/37 non-arXiv/non-DOI records processed: 18 verified unchanged, 18 with
  proposed corrections/enrichments (in 25 JSONL proposal records incl. 2
  other-lane items), 1 quarantined as unidentifiable.
- `found-prior-2009`: DOI resolves to an unrelated Mind book review; philosopher
  Katherine Hawley's full OpenAlex bibliography (96 works, 1995–2021) contains
  no such title; title search across OpenAlex + two search engines find only
  physics items by other authors. **Intended source cannot be identified**;
  nearest verified alternatives listed with explicit conjecture labels.
- Blocked pages (recorded unread, never read): JSTOR ×3 (JS challenge),
  academic.oup.com ×8 (403), Springer ×2 (challenge), MIT Press (403),
  PhilPapers (Cloudflare), survey2020 `/all` (403; sub-page confirmed via
  search summary only).

## Verification commands and results

Representative commands (all reproducible):

```sh
curl -s "https://api.crossref.org/works/10.1093/mind/fzp077"   # -> Fernandez review, Mind 118(471):840-843
curl -s "https://api.crossref.org/works/10.1063/1.522676"      # -> Wong & Yeh JMP 16(6):1239-1243 (NOT Bisognano-Wichmann)
curl -s "https://api.crossref.org/works/10.1063/1.522898"      # -> Bisognano & Wichmann, JMP 17(3):303-321, 1976
curl -s "https://archive.org/metadata/directionoftime00reic"   # -> {} (broken id)
curl -s "https://archive.org/metadata/directionoftime0000reic" # -> UC Press 1971, ISBN 9780520018396
curl -s "https://api.openalex.org/works?filter=author.id:A5018607675&per-page=100"  # Hawley, 96 works, no such title
curl -s "https://api.github.com/repos/leanprover-community/physlib/commits?per_page=1"
python3 scripts/agents.py brief kb-bib-repair                  # task brief re-read
```

JSONL integrity checked: 25 proposal lines parse; IDs unique and all present in
existing lane files; original fields preserved (see commands below).

```sh
python3 - <<'EOF'
import json
ids=set()
for f in ['knowledge/bib-audit/proposed-records.jsonl','knowledge/bib-audit/proposed-other-lane-fixes.jsonl']:
    for line in open(f):
        r=json.loads(line); assert r['id'] not in ids; ids.add(r['id'])
print(len(ids), 'unique valid records')
EOF
```

## Strongest contrary evidence / audit challenges

- The conjecture that Hawley's "Metaphysics and Relativity" (10.4324/9780203879306.ch47)
  was the intended `found-prior-2009` target is **not verified** — the chapter's
  content was not read. What would defeat it: any Hawley text actually titled
  "The Future of the Universe" (none found in OpenAlex/Crossref/two search
  engines), or a foundations-lane record of the original search that produced
  the DOI.
- The PhilPapers-survey record's existence claim rests partly on a search
  summary (the results page itself 403s) — per contract this is discovery-level,
  not a page read.
- JSTOR/OUP/Springer/MIT bibliographic confirmations rely on Crossref/Open
  Library rather than the publisher pages the records cite; URL staleness on
  those publisher domains is possible and should be re-checked by a lane that
  can access them.
- My OpenAlex pagination for Hawley fetched 96 of a reported 101 works
  (per-page cap 100 + sorting); the 5 unseen items are fragments/indexes of
  edited volumes visible by title in the fetched set. Residual risk that a
  differently-indexed Hawley item exists is small but nonzero; Crossref
  author+title queries found none.

## Limitations

- All verification is catalog/landing-page metadata level; no substantive
  content of any source was read or re-audited; existing `read_depth` claims of
  other lanes were not re-adjudicated (except where a record's own limits note
  conflicted with catalog evidence, which is flagged).
- The two pinned Physlib file URLs use a commit taken **after** the original
  same-day reads; line locators must be re-diffed before reuse (caveat embedded
  in the proposed records).
- `phil-lewis` issue number (APQ 13(2)) remains unconfirmed: SEP bibliography
  gives volume and pages only; JSTOR/PhilPapers blocked.
- No source IDs were created, merged, or duplicated; `found-brading` vs
  `disc-brading-empirical-2013-full` same-DOI cross-lane duplication is flagged
  for synthesis, not changed.

## Proposed next tasks

1. Coordinator applies `proposed-records.jsonl` to the four lane files and
   decides `found-prior-2009`: retire, or replace with a chosen verified source
   (candidates and their verification status in section C of bib-corrections.md).
2. `aqft-locality` lane: confirm the Bisognano–Wichmann II repair (read the
   actual JMP 17(3) paper — is it what the lane meant by "part II"?) and accept
   or reject `proposed-other-lane-fixes.jsonl`.
3. Human/machine access pass for the blocked set (JSTOR ×3, OUP ×8, Springer ×2,
   MIT, PhilPapers, survey2020) to convert "unread" records into checked ones.
4. Pin and build the three GitHub repos at the recorded SHAs (methods/
   formalization lanes) to upgrade those records from discovery/code-audited
   claims to reproducible ones.
5. Optional: replace `found-stein-1991`'s aggregator-read provenance with a
   legitimate full-text access (e.g., UA library JSTOR/Chicago access) and note
   it, since the paperzz copy could not be re-inspected.
