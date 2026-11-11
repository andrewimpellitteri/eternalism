# AGENT_REPORT — read-problem-of-time

11 November 2026. GLM reading lane, task `read-problem-of-time`. Submission for
independent review; not accepted completion. No temporal ontology selected; nothing
below is a priority claim.

## Done and files

- `knowledge/reading/problem-of-time/READING.md` — the deliverable note, exactly the
  five required parts: main positions with named defenders and sources; five
  canonical arguments reconstructed premise-by-premise with standard objections;
  live open problems with progress criteria; section naming what in this repository
  must be revised given this area; ten ranked primary sources to read next.
  Addresses the special question: which of the four relations (having become,
  being fixed, existing, being true at a standpoint) survive if time is not
  fundamental, and what replaces them.
- `knowledge/reading/problem-of-time/sources.jsonl` — 25 records under the
  knowledge/README.md contract (id, title, url, checked_on, read_depth, kind,
  relevance, limits; full-text records carry authors, version/DOI, locators,
  assumptions, conclusions, dependencies, related IDs, open questions).- This report.

## Search capability check (required at start)

- `web-search-prime` (Z.ai): **failed**. First relevant query returned MCP error
  -429, code 1310, "Weekly/Monthly Limit Exhausted", reset 2026-11-17. Recorded
  here per the brief; not used again.
- `scholar_search` (OpenAlex/arXiv/CrossRef): **worked** throughout (used for
  bibliographic verification and discovery).
- Exa `web_search_exa` / `web_fetch_exa`: **worked** (primary-source fetches via
  ar5iv, PhilSci-Archive, author-hosted PDFs, APS abstract pages, SEP).

## Source coverage

Primary, full-text depth (partial but targeted, with locators recorded): Isham 1992
(gr-qc/9210011); Butterfield–Isham 1999 emergence paper (gr-qc/9901024 via
PhilSci-Archive); Rovelli "Forget time" (0903.3832); Barbour "The Nature of Time"
(0903.3489); Gryb–Thébault 2014 (1303.7139); Gryb–Thébault "Time Remains" 2015
(1408.2691); Earman 2003 "Tracking down gauge" (author-hosted PDF);
Huggett–Wüthrich *Out of Nowhere* introduction chapter (2101.06955);
Anderson 2012 review (1009.2157) — secondary, labelled.

Primary, abstract only: Kuchař 1991 (IJMPD 20 (2011) 3–86 reprint, DOI verified;
primary text not openly accessible — content reconstructed from Butterfield–Isham,
Anderson, Gryb–Thébault and labelled as such); Connes–Rovelli 1994
(gr-qc/9406019); Barbour 1994 I (CQG 11 2853); Barbour–Koslowski–Mercati 2014
(PRL 113 181101); Page–Wootters 1983 (PRD 27 2885); Hájíček 1991 (PRD 44 1337);
Gomes–Gryb–Koslowski 2011 (CQG 28 045005); Brown–Kuchař 1995 (PRD 51 5600);
Trinity (1912.00033); Marletto–Vedral 2017; Gomes 2017; Barbour shape-dynamics
introduction (1105.0183); Butterfield–Isham "Spacetime and the philosophical
challenge" (gr-qc/9903072).

Philosophical: Earman 2002 *Thoroughly Modern McTaggart* (Philosophers' Imprint
2(3)) — **not accessed**: quod.lib.umich.edu returned HTTP 403 to both fetch
tools; content limited to Exa-indexed highlights of the PDF (opening argument,
§10 title, the WdW/"stymied" passage, "far from being settled"), labelled abstract
in sources.jsonl. SEP "Quantum Gravity" (Weinstein–Rickles) — secondary, §3.2.2
highlights.

Not accessed at all: DeWitt 1967 (PR 160 1113, paywalled; locator pinned from
Barbour 2009's reference list and labelled discovery); Barbour's *The End of
Time* and the print *Out of Nowhere* (copyrighted books); Kuchař 1991 full text;
Isham–Kuchař dust precursor (known only via a bibliography key in Gryb–Thébault
2014; exact reference unverified and flagged in its record).

## Verification commands and results

- Resume check: `git status --short` (clean), `git log --oneline -5` (HEAD
  13dcd6e), output paths absent — resumed without lost work, wrote all files fresh.
- Wrong-arXiv-ID catches (memory vs page, each resolved by fetching the abs page or
  searching): gr-qc/9905072 → correct Butterfield–Isham ID gr-qc/**9903072**;
  gr-qc/9404011 → correct Connes–Rovelli ID gr-qc/**9406019** (the former is a
  Smolin paper); 0903.3487 → correct Barbour ID **0903.3489**. Barbour 1994 part I
  title verified as "The evidence from the classical theory" (not the remembered
  subtitle); part II's title left unverified and unasserted.
- JSONL well-formedness: `python3 -c "import json,sys;
  [json.loads(l) for l in open('knowledge/reading/problem-of-time/sources.jsonl') if l.strip()]"`
  — all 24 records parse.
- Content checks: every quotation in READING.md was carried over only from fetched
  text visible in this session (Isham categories; Kuchař's abstract sentence;
  Gryb–Thébault constraint-interpretation sentences; Earman's "truly frozen
  universe" passage; Anderson's non-monotonicity and conditional-probability
  passages; Hájíček's verdict; BKM's "single past and two distinct futures").

## Strongest contrary evidence (to this lane's own framing and to the repo)

- Against taking the frozen formalism as the whole problem: Gryb–Thébault 2014
  argue the Hamiltonian constraint should be "interpreted as an identity … not
  imposed formally as a constraint", yielding genuine evolution — a direct rival to
  the Dirac-quantization route; Isham 1992 notes discreteness approaches could
  "render irrelevant much of the discussion involving the Wheeler–DeWitt equation".
- Against Rovelli-style relational time: Hájíček 1991 — "the procedure does not
  work, at least in the presented form"; Anderson's problems that good clocks are
  not guaranteed and conditional probabilities do not address becoming.
- Against the repo's three-candidate arrow menu: BKM 2014 claims an arrow from a
  time-symmetric law with no special initial conditions (records/complexity);
  Connes–Rovelli supply a state-dependent flow. The paper's direction section
  should register both (READING.md part 4).
- Against Earman's frozen-universe reading: the relational-change position
  ("Time Remains" target framing) accepts his gauge premises and denies the sting.

## Limitations

- Full-text reads are partial: windows around key sections, with locators recorded;
  not complete line-by-line reads of any long paper. Depths are labelled
  accordingly and honestly in sources.jsonl.
- Kuchař 1991 primary unavailable; his classification is reconstructed from three
  independent secondary reports, each labelled — this is the weakest link in the
  note and the top item of the to-read list.
- Earman 2002 only via indexed highlights (403 block).
- Books (copyrighted) not accessed; IOP/APS full texts paywalled where noted.
- Session was interrupted once (provider rate limit) and resumed; the clean worktree
  check confirmed no lost or duplicated output.
- No dependency installs, no contact with anyone, no edits outside owned paths.

## Proposed next tasks

1. Read Kuchař 1991 in full (gated source needed, or library access) and rewrite
   the internal-time reconstruction from the primary; check the repo's
   `stein-gr/local-clock` Theorem 4 against his exact obstruction statements.
2. Deep-read Rovelli 1991 + Hájíček 1991 and produce a note testing whether the
   repo's F_L fixing machinery has a relational-observable analogue; feeds
   NOVELTY candidate B.
3. Deep-read Gryb–Thébault "Time Remains" and write the break-through-test note
   naming what their succession/variation distinction forces the repo paper to
   revise.
4. Read DeWitt 1967 before any public use of "Wheeler–DeWitt" in the paper; and
   add the QG scope statement and arrow-menu additions flagged in READING.md
   part 4 (small edits to main.tex, on the coordinator's acceptance).
5. Obtain Earman 2002 through the user's gated sources; complete the frozen-universe
   entry in the note.
