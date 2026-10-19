# Agent report: kb-time-interpretations

Status: worker submission for independent review (not accepted completion).
Worktree: `/Users/andrew/eternalism/.worktrees/kb-time-interpretations`, branch
`agent/kb-time-interpretations`. Date: 2026-10-19.

## Done / files changed

- `knowledge/time-interpretations/sources.jsonl` (new, 29 records): lane-prefixed
  `time-` IDs covering ABL/two-state formalism (6), retrocausal and all-at-once
  formulations (7), Everettian (2), consistent/decoherent histories (10),
  superdeterminism (4). Each record has `id, title, url, checked_on, read_depth,
  kind, relevance, limits`; full-text records add authors, exact version/DOI,
  section locators, assumptions, conclusion, proof status, dependencies, reused
  `related_source_ids`, and open questions.
- `knowledge/time-interpretations/comparison.md` (new): theory-comparison contract
  filled for five anchor families at model/version level, the master table of
  fixed-future / branching / empirical-equivalence claims with locators, bridge
  premises for ontological claims, contrary-evidence pointers, and nearest
  predecessors / defeat conditions (no novelty claims).
- `AGENT_REPORT.md` (this file).
- No other files touched; no coordination files, seed sources, or other lanes
  modified.

Task-specific requirements from the brief, addressed:

- Reused rather than duplicated existing IDs: `phil-everett` (Everett 1957,
  referenced as dependency of time-sep-everett-2023 and time-wallace-2012),
  `found-stein-1991`, `found-rietdijk`, `found-putnam` (bridge-premise discussion),
  `phil-belnap` (branching analogy), `phil-grw`, `phil-bohm-foliation` (Type I
  contrast), `seed-bell-temporal-order`, `frontier-records-histories-2016`,
  `frontier-records-time-asymmetry-1993`, `phil-price-arrow`, `phil-callender`
  (arrow/passage context). Checked `knowledge/frontier/`, `knowledge/foundations/`,
  `knowledge/methods/` before writing (read sources.jsonl of all four lanes plus
  seed-sources.jsonl; no existing record overlapped this lane's scope except
  phil-everett, which was reused, not duplicated).
- Fixed-future, branching, and empirical-equivalence claims recorded per
  interpretation with locators (comparison.md master table).
- Temporal ontology, objective passage, determinism, causal order, clock time,
  and thermodynamic arrow kept distinct (comparison.md distinctions table);
  eternalism is nowhere identified with determinism; the Everett anchor shows a
  deterministic dynamics without a single fixed future-content.
- No novelty claims. Nearest predecessors and what would defeat any suggested gap
  are listed (comparison.md final section).

## Search capability check (required)

- `web-search-prime` / Z.ai research MCP tools: **unavailable to this worker**.
  `tools.opencode.list_mcp_resources()` returned zero resources and zero
  templates (no MCP server exposes search here), and no search MCP tool exists in
  this session's tool catalog. Recorded as unavailable rather than claimed.
- Built-in `websearch` tool: **failed on all three attempts** with
  `{"error":{"type":"unknown","message":"Web search cancelled"}}`.
- Fallback public web tools used instead, all working:
  - Direct page fetches: arXiv abs pages, arXiv search UI (author/all-field
    queries), plato.stanford.edu entries.
  - `api.crossref.org`: DOI verification and bibliographic queries.
  - `arxiv.org/e-print/<id>`: TeX source downloads for eight primary anchors,
    read locally (scratch dir `/private/tmp/opencode/kbti/`, not committed).
- Blocked/failed accesses, recorded honestly: `journals.aps.org` (403, so
  time-abl-1964, time-aav-1988, time-cramer-1986 full texts unread);
  `api.semanticscholar.org` (429); `export.arxiv.org` API (429, worked around via
  the arXiv search UI); one misdownloaded paper (arXiv:1903.10738 turned out to
  be an unrelated numerical-analysis paper — my recalled ID was wrong; deleted,
  and the correct ID 1906.04313 located via the search UI and verified from its
  own TeX before use).

## Source coverage

- 29 records; read depth: 8 full-text, 18 abstract, 3 discovery.
- Coverage by family: ABL 1964 (abstract via CrossRef + two fetched bibliographies
  that cite it), TSVF review (full TeX), weak-value experiment (abstract), Physics
  Today program statement and critical exchange (abstract); Wharton-Argaman RMP
  2020 (full TeX incl. bibliography file used to verify Bell/Cramer/Brans/Hall/
  Shimony locators), Price-Wharton and Wharton all-at-once papers (abstracts with
  verified IDs/DOIs from the arXiv author listing), 2026 Entropy circuits paper
  (abstract, inside the last 90 days, flagged unrefereed), Cramer 1986 (abstract,
  CrossRef), RBW blockworld (abstract); SEP Everett 2023 (full text) + Wallace
  2012 (discovery, metadata only); Griffiths 1984 (abstract, CrossRef), GMH 1990
  (discovery, locator verified from two fetched bibliographies), GMH 1994 (full
  TeX), Hartle 2005 (full TeX), SEP CH 2024 (full text), Kent 1997 / GH reply /
  Kent reply / Dowker-Kent 1996 (abstracts via arXiv), Zampeli et al. 2026
  (abstract); 't Hooft 2016 (selected sections, full TeX), Hossenfelder-Palmer
  2020 (full TeX), Palmer 2009 (abstract), Bell 1977 (discovery, second-hand).
- Last-90-days search: performed via the arXiv author/all-field listings
  (2026-10-19). Recent items found and recorded: time-wharton-circuits-2026
  (Entropy, accepted Sept 2026) and time-zampeli-2026 (Found. Phys. 56, 3 (2026),
  arXiv v4 Dec 2025). Without a working search backend, citation-forward checks
  beyond arXiv listings were not possible.

## Verification commands and results

```
python3 /private/tmp/opencode/kbti/build_sources.py
  -> records: 29
  -> validation errors: 0
  -> read_depth distribution: {'abstract': 18, 'full-text': 8, 'discovery': 3}
  -> written: knowledge/time-interpretations/sources.jsonl
```

The same script enforces the knowledge/README.md contract: required fields
present, `read_depth` in {discovery, abstract, full-text, reproduced,
code-audited}, unique IDs. Re-run:

```
python3 /private/tmp/opencode/kbti/build_sources.py   # exit 0, 0 errors
python3 -c "import json;[json.loads(l) for l in open('knowledge/time-interpretations/sources.jsonl')];print('jsonl ok')"
  -> jsonl ok
```

Bibliographic verification performed (all via fetched primary records, none from
memory where a check was possible):

- ABL 1964 = Phys. Rev. **134**, B1410-B1416, DOI 10.1103/PhysRev.134.B1410
  (title "Time Symmetry in the Quantum Process of Measurement"): CrossRef record;
  independently confirmed in the reference lists of fetched Cramer 1986 (RMP),
  Griffiths 1984 (JSP), and Wharton-Argaman TeX.
- AAV 1988 PRL 60(14):1351-1354; Cramer 1986 RMP 58(3):647-687; Griffiths 1984
  JSP 36(1-2):219-272; Ritchie et al. 1991 PRL 66:1107-1110; APT 2010 Phys.
  Today 63(11):27-32 and 2011 exchange 64(5):62-63; Wallace 2012 ISBN/DOI:
  CrossRef records fetched and matched.
- arXiv versions and journal refs verified from arXiv abs pages:
  gr-qc/9304023v2 (published in Physical Origins of Time Asymmetry, CUP 1994),
  gr-qc/0403001v2 (Am. J. Phys. 73, 101-109 (2005), DOI 10.1119/1.1783900),
  0812.1148v4 (Proc. R. Soc. A 465, 3187-3207, DOI 10.1098/rspa.2009.0080),
  1912.06462 (DOI 10.3389/fphy.2020.00139), 1906.04313v2 (RMP 92, 021002),
  quant-ph/0105101v2 (LNP 72, 369-412, DOI 10.1007/3-540-45846-8_13).
- Bell 1977 "Free variables and local causality" (Epistemological Letters 15),
  Brans 1988 (IJTP 27, 219-226), Hall 2016 (Springer chapter, DOI
  10.1007/978-3-319-31299-6_11), Shimony-Horne-Clauser 1976 (Epist. Lett. 13):
  locators taken from the fetched `RMPBibTexFile.bib` of the Wharton-Argaman
  RMP; Bell 1977 primary text NOT accessed (recorded as discovery/second-hand).
- Kent 1997 PRL 78:2874-2877; Griffiths-Hartle PRL 81:1981; Kent PRL 81:1982;
  Dowker-Kent JSP 82:1575-1646: arXiv abstract pages (IDs and journal refs).
- SEP entry authorship checked from page copyright blocks: qm-everett (c) 2023
  Jeffrey Barrett, revision 2023-06-20; qm-consistent-histories (c) 2024 Robert
  B. Griffiths, revision 2024-06-19.

## Strongest contrary evidence found

- Against a naive "time-symmetric formulation settles the future" reading: the
  TSVF review's own Sec. V.C — creation/post-selection asymmetry attributed to
  the fixed memory arrow of time; measurement as an operation is time-asymmetric
  even where outcomes are symmetric (Sec. V.D).
- Against consistent histories as a complete realist theory: Kent 1997 (contrary
  probability-one inferences, including in GMH's generalized time-neutral
  theory), Dowker-Kent 1996 (need for a selection principle; Omnès'
  true-statement characterization shown incorrect), Kent's 1998 rejoinder, and
  the 2026 quasi-classical certainty-conflict result (Zampeli et al.). The SEP
  author concedes unicity-abandonment is "the principal stumbling block".
- Against "Everett is trivially empirically equivalent": SEP Everett Sec. 6 —
  without auxiliary assumptions pure wave mechanics "fails to be empirically
  adequate in any standard sense"; forward-looking probabilities need
  decision-theoretic or self-location additions. Wharton-Argaman Sec. VI.C
  (citing Maudlin 2010) makes the complementary point that removing the Born
  rule removes the empirical content that agreement is defined over.
- Against superdeterminism as a free lunch: Wharton-Argaman Sec. VI.C — explicit
  QM-agreeing superdeterministic toy models (Brans 1988; Hall 2016) covertly
  treat future settings as free inputs; Bell's own 1977 defense of free
  variables (second-hand); 't Hooft's admitted Hamiltonian-positivity and
  Lorentz-invariance obstacles.
- Against "all-at-once implies block universe": none of the anchors asserts the
  inference; Wharton-Argaman explicitly frame all-at-once as solution method
  (Sec. I, stationary-action analogy), and Hartle explains passage experience
  inside a four-dimensional setting as IGUS information processing, with the
  cognitive-universal claim flagged as conjecture.

## Limitations

- No full-text access to APS-paywalled primaries (ABL 1964, AAV 1988, Cramer
  1986, Ritchie 1991, Kent PRLs — the Kent-chain items are abstracts only).
  Their roles are filled by full-text reproductions (TSVF review, GMH 1994) and
  CrossRef-verified metadata; the records say so.
- Wallace 2012 read at discovery depth only (no chapter locators); GMH 1990 and
  Bell 1977 unread in primary form (discovery; second-hand locators verified
  from fetched bibliographies). Transactional interpretation covered only at
  abstract/secondary depth; Kastner's neo-transactional line not covered.
- Bassi & Ghirardi critiques covered only through SEP CH Sec. 9.3 locators and
  bibliographic entries; their primary texts were not fetched.
- 't Hooft read in selected sections of a long book; Part II technical
  development only at heading level. Claims that depend on it (Hamiltonian
  positivity, Lorentz invariance difficulties) are his own admissions.
- Search-backend outage: literature search limited to arXiv listings + CrossRef
  + citation chasing inside fetched papers; no general web search, so
  recent-literature coverage beyond arXiv (e.g., journals without arXiv
  versions) is thin; citation-forward checks incomplete.
- Read depth is heavily abstract-level (18/29); the comparison table's
  locators for abstract-depth rows point to abstracts and secondary
  classifications, not full arguments. The Everett 1957 primary remains
  discovery-depth in the shared KB (phil-everett); its page-numbered quotes
  here come from the SEP entry and were not checked against scans.

## Proposed next tasks

1. `kb-time-interpretations-2` (deep pass): fetch and read ABL 1964 (e.g., via
   library access or the 2025 reprint chapter found on CrossRef), Bell 1977
   (Speakable reprint), Kent 1997 + replies in full, Bassi-Ghirardi 1999/2000;
   upgrade the corresponding records and re-check the comparison table rows.
2. `kb-transactional-neo`: dedicated pass on transactional and neo-transactional
   (Cramer 1986 primary; Kastner) to complete the all-at-once family.
3. `kb-everett-relativistic`: check whether Everettian branching plus
   special-relativistic structure has published no-go/equivalence results
   (interfaces with the foundations lane's Rietdijk-Putnam material and the
   QRF lane; would test candidate D in knowledge/NOVELTY.md).
4. `kb-superdet-models`: audit the two named toy models (Brans 1988; Hall 2016)
   against Wharton-Argaman's Sec. VI.C claim that they restore free settings —
   small, checkable, and load-bearing for the superdeterminism row.
5. `kb-ch-set-selection`: collect published set-selection criteria (ordered
   consistency, Griffiths 2002 ch.16 arguments, 2026 proposal) into the checks
   lane as candidate formalization targets.

## Blockers

None remaining for this task. (Transient blockers hit and worked around: websearch
outage, arXiv API and Semantic Scholar rate limits, APS 403s — all recorded above.)
