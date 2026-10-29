# AGENT_REPORT — prior-art-bst (BST settledness/horizons prior-art audit)

Date: 2026-10-28. Worker: OpenCode GLM headless (agent/prior-art-bst).
Task brief: prior-art audit of four screening claims (X1–X4) against BST
sources. Output is a submission for independent review, not a final truth
claim. No novelty claim is made.

## Done / files

- Located and read (full-text) all named sources: Belnap 1992; Belnap,
  Müller & Placek 2022 (open-access OUP monograph, KOPS PDF, 456 pp.);
  Earman 2008; plus the directly relevant Placek & Belnap 2012, Müller &
  Placek 2018, and Placek 2014. Discovery-level: Müller 2013, Dorato &
  Hoefer 2021 (full text owned by the sibling lane bowtie-horizons).
- Files written (owned paths only):
  - `research/bowtie-horizons-prior-art/bst/RESULT.md` — verdict table,
    quotes with locators, focus-question answers, contrary evidence.
  - `research/bowtie-horizons-prior-art/bst/sources.jsonl` — 8 records per
    the knowledge-base source contract.
  - `AGENT_REPORT.md` (this file), copied to repo root as required.

## Headline verdicts

- X1: PARTIAL ingredients in Belnap 1992 p. 395 (event horizons threaten the
  common-causal-future requirement; question tabled), BMP 2022 pp. 26–29 and
  Fact 9.14 p. 316 (later-witness criterion; GR violations acknowledged;
  directedness ⇒ one history), Placek 2014 preprint p. 3 (Schwarzschild and
  de Sitter named as failing the BST92 historicity criterion). No source
  derives any growth/(P1R) failure of an existence or causal-potential domain.
- X2: NOT-FOUND everywhere (no historical-potential repair H, no dust+Λ
  threshold).
- X3: PARTIAL ingredients — BST settles elsewhere-event status modally
  (wings in the intersection: Belnap 1992 pp. 400, 410–412; BMP pp. 54–56);
  causae causantes causal reach explicitly may not extend across space (BMP
  p. 362). No influence-based definition of settled-at-b, no minimal
  screening region, no Cauchy-slice characterization.
- X4: premise-level only — BMP Theorem 9.2 (Choquet-Bruhat–Geroch MGHD/MVCD
  uniqueness, pp. 319–320, incl. a Ringström 2009 p. 188 quote), §9.3.5
  global determinism ("agree on initial segments ⇒ agree as wholes"),
  Earman 2008 p. 201 IVP remark, Müller-Placek 2018 GR section. No claim
  that a proper sub-slice realm fixes the future while the causal past does
  not.
- Whole-book keyword scan of BMP 2022: "horizon" 0, "de Sitter" 0, "causal
  potential" 0, "growth" 0, "MGHD" 0, "black hole" 0, "Correia" 0,
  "Rosenkranz" 0; "settled" 38 (all modal usage).

## Search capability check

- `scholar_search` (MCP): worked, first try (tool + server recorded in
  RESULT.md). Used to verify Crossref DOIs: Belnap 1992
  10.1007/bf00414289; Earman 2008 10.1016/s1871-1774(08)00010-7; Placek-
  Belnap 10.1007/s11229-010-9846-8; BMP 10.1093/oso/9780190884314.001.0001.
- `exa web_search_exa` / `web_fetch_exa`: worked; used for locating texts
  and for reading PDFs (see verification below).
- `web-search-prime`: NOT used (quota exhausted until 2026-11-17 per brief;
  not retried). `serpapi_search`: not needed.
- Access gate: PhilSci-Archive WAF rejects curl ("Request Rejected") — PDFs
  read via exa fetch instead. The UC Cincinnati mirror of Belnap 1992 is
  dead (404); read from the exa cache of the JSTOR scan (JSTOR stable
  20117060). Both gates recorded in sources.jsonl.

## Source coverage

8 sources recorded in sources.jsonl (6 full-text, 2 discovery). Citation
chasing: BMP ch. 2 → Müller 2014, Placek 2011 (follow-up leads, unread);
BMP ch. 9 → Choquet-Bruhat–Geroch 1969, Ringström 2009 p. 188, Chruściel
2011 (anchors, not re-read); Placek-Belnap 2012 → Earman 1986/2007 (context).

## Verification commands and results

Work dir /private/tmp/opencode/prior-art-bst (outside the repo; nothing
there is committed):

- `curl -sL -A "Mozilla/5.0" -o bmp2022.pdf
  https://kops.uni-konstanz.de/bitstreams/d8a2ea75-40fc-4976-8db5-595df6e9ff49/download`
  → 3,020,666 bytes; `file` → "PDF document, version 1.6"; 456 pages
  (JXA PDFKit `PAGES:456`).
- `curl -sL -o earman2008.pdf https://sites.pitt.edu/~jearman/Earman2008a.pdf`
  → 206,948 bytes; 19 PDF pages = printed pp. 187–205.
- PDF text extraction via stock-macOS JXA + PDFKit (`pdfextract.js`):
  `osascript -l JavaScript pdfextract.js FILE first last maxchars`. BMP
  page-offset check: PDF p. 333 ↔ printed 318, PDF p. 44 ↔ printed 29
  (offset +15), used for all BMP locators.
- Keyword scans: `grep -c -i` over the full BMP text (1,089,684 bytes):
  counts as listed above; equivalent regex checks over the exa-extracted
  texts of Belnap 1992, Placek-Belnap 2012 (78,172 chars), Müller-Placek
  2018 (98,900 chars), Placek 2014 (61,496 chars).
- DOI verification via `scholar_search` Crossref records (see above).

## Strongest contrary evidence

See RESULT.md §"Strongest contrary evidence": (1) the common-future
ingredient of X1 is already in BST print, with named GR failures; (2) the
wings-in-intersection answer is a rival worked-out account of "what is real
at a point event" that includes all spacelike events; (3) BMP already
anchors GR determinism in MGHD uniqueness and Ringström's genericity
remark; (4) Earman 2008 already asserts growing-block/relativity tension
without horizons.

## Limitations

- Belnap 1992 read from an OCR-noisy JSTOR scan via exa cache; quotes are
  repaired readings (marked in RESULT.md). Live mirror dead.
- Placek-Belnap 2012, Müller-Placek 2018, Placek 2014 read in preprint
  versions; published pagination unverified (recorded per record).
- BMP close reading limited to targeted sections; remainder covered by the
  keyword scan only. A differently-worded discussion would not be caught by
  vocabulary scans.
- Absence of hits is not novelty: verdicts bound only the sources and
  depths listed.

## Unresolved questions / proposed next tasks

In RESULT.md §"Proposed next tasks": read Müller 2014, Müller 2011,
Placek 2011 (later-witness counterexamples and generalized historicity);
companion audit of Stein 1968/1991 vs X3/X4; check NDPR review of
Nothing to Come for horizon objections; cite Belnap 1992 p. 395 and
Placek 2014 p. 3 in the X1 claim contract if kept.

## Compliance

Stayed within owned paths (`research/bowtie-horizons-prior-art/bst/` and
root `AGENT_REPORT.md`); no board/runner/AGENTS.md/knowledge-base edits; no
installs; no subagents; no pushes or merges; web-search-prime not retried.
Extracted PDFs/texts kept in /private/tmp/opencode/prior-art-bst (not
committed).
