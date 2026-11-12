# AGENT_REPORT — prior-art-becoming

Task: prior-art audit of the relativistic-becoming literature against the four
screening claims X1–X4 (see `research/bowtie-horizons/SCREENING.md`,
`RESULT.md`, and `research/horizons/PRIOR_WORK_CHECK.md`, read-only).
Submission for independent review; not an accepted completion; no novelty
claim.

## Done / files

- `research/bowtie-horizons-prior-art/becoming/RESULT.md` — named-source
  coverage table (locator, access, read depth), X1–X4 verdict table
  (FOUND/PARTIAL/NOT-FOUND with brief quotes), claim-by-claim notes with
  verbatim passages, strongest contrary evidence, limits, falsifiers.
- `research/bowtie-horizons-prior-art/becoming/sources.jsonl` — 21 source
  records per the knowledge-base contract (validated: all lines parse; all
  required fields present).
- `AGENT_REPORT.md` (this file, repo root).

All 13 named sources located with exact locator and read depth, or an access
gate recorded (Stein 1968 discovery; C&H 1995 abstract + theorems via Savitt
2020; Dieks 1988 abstract; Arthur 2019 abstract; Savitt 2000 abstract;
Savitt 2009 abstract/PIRSA). Full texts read: Stein 1991, Dieks 2006
(preprint), Arthur 2006, Ellis 2006 (arXiv v3), Ellis 2014 (arXiv),
Ellis–Rothman 2010 (arXiv v2), Rovelli 2019 (ar5iv), plus extras Savitt 2020,
SEP survey, Dorato 2010 (targeted scan).

## Search capability check

- `scholar_search`: worked at session start (openalex + crossref; Clifton–
  Hogarth 1995 record confirmed). Crossref HTTP 429 twice mid-session;
  worked around with direct Crossref REST queries.
- `web-search-prime`: not retried (quota exhausted until 2026-11-17), per brief.
- `exa web_search_exa` / `web_fetch_exa`: worked overall; failures: arXiv
  `gr-qc/0605049` extraction failed on `/pdf` and legacy paths (succeeded at
  `arxiv.org/vc/.../0605049v3.pdf`); `philpapers.org/archive/STEOES.pdf` is a
  mis-filed student essay, not Stein 1968; `philsci.org/docs/savitt.pdf`
  (Savitt 2000 PSA'98 manuscript) timed out ×3.
- `serpapi`: quota exhausted mid-task ("Your account has run out of
  searches").

## Source coverage and verification

- Verification method: every quote used in RESULT.md was re-fetched and
  string-matched verbatim in a final verification pass (Ellis 2014 "Ricci
  eigenlines"/"bounded to the future"; Ellis–Rothman "concretizing"/
  "predicted from the past"; Rovelli §II/§IV.1/§V passages — all matched).
- Keyword scans recorded zero occurrences of "horizon" in the full texts of
  Rovelli 2019, Ellis 2014, Ellis–Rothman 2010, Savitt 2020, and the SEP
  survey; one occurrence ("Cauchy horizon", determinism remark) in Ellis 2006.
  These counts come from fetched full texts, not snippets.
- arXiv ID correction: Ellis 2014 "meshing together of times" is
  arXiv:1407.7243 (1408.2350 is an unrelated CS paper — caught by checking
  the abstract page before use). Dieks 1988 title correction: "…and the Flow
  of Time", Phil. Sci. 55(3): 456–460 (not "Flux").

## Verdict summary (details and quotes in RESULT.md)

- X1 (growth violation of the instantaneous causal-potential domain in
  non-future-directed spacetimes): NOT-FOUND in every source read. The
  Stein–Clifton–Hogarth line is Minkowski-only and its domains are monotone
  by construction; the Ellis EBU line grows the block by worldline proper
  time and never qualifies the boundary by horizons.
- X2 (historical-potential repair H missing spacelike events; threshold):
  NOT-FOUND. No source defines a persistent/historical enlargement of a
  becoming domain or any distance threshold.
- X3 (J⁻(J⁺(b))\J⁺(b) as the minimal screening region; bow-tie surplus
  causally idle): NOT-FOUND as a claim. The influence-based-criterion family
  is well occupied (Stein 1991 influence premise; Ellis 2006 Newtonian
  "present = events we can actually influence"; Ben-Yami 2019 mutual-
  interaction simultaneity; Arthur 2006/Savitt 2009 causal diamonds; Rovelli
  2019 diamond present) — but every instance is past-directed or
  mutual-interaction for extended events; none aims existence at b's future
  or proves minimality/screening.
- X4 (realm containing the potential region fixes b's future; causal past
  does not): NOT-FOUND in the becoming literature; PARTIAL background in
  Ellis 2006 (surface determinism "up to the Cauchy horizon") and
  Ellis–Rothman 2010 (past-does-not-predict-future, quantum premise). The
  nearest genuine prior (Geroch 1977 domain of prediction; Manchak 2008;
  Lesourd 2021) is recorded in `research/horizons/PRIOR_WORK_CHECK.md` at
  full-text depth and was not re-verified here.

## Strongest contrary evidence

The influence-based existence/simultaneity family (X3 adjacency) and the EBU/
CBU growth ontologies (X1/X2 adjacency) listed in RESULT.md "Strongest
contrary evidence / near misses", plus unread leads flagged there: Muller
1992 and Peacock 1992 (refuted by C&H), causal-set becoming (Callender–
Wüthrich 2016; Rideout–Sorkin), Ellis–Drossel 2020, Riggs 2024.

## Limitations

- Six sources not read at full-text depth (paywalls/crawler failures); their
  verdicts rest on abstracts or clearly labeled secondary statements.
- Version caveats: Dieks 2006 preprint vs published chapter; Ellis 2006 v3 vs
  v5 "Major revision"; Ellis 2014 arXiv vs NYAS; Rovelli 2019 ar5iv render
  (stamp 2024-03-07) vs published pagination; Stein 1991 OCR scan.
- Bounded search: no systematic sweep of growing-block critiques, causal-set
  growth dynamics, or the 1990s worldline-becoming proposals. Absence of hits
  is a negative result over a small targeted search, not evidence of absence.
- All verdicts and quotes are mine; an independent reviewer should
  re-verify at least the gated sources and the C&H theorems against the
  primary texts.

## Proposed next tasks

1. Read the gated primaries where a library access exists: Stein 1968,
   Clifton–Hogarth 1995 (theorems in original wording), Savitt 2000/2009,
   Arthur 2019 ch. 7 (horizon content), Dieks 1988.
2. Audit causal-set becoming (Rideout–Sorkin; Callender–Wüthrich 2016) and
   Muller 1992/Peacock 1992 for growth-monotonicity prior art near X1.
3. Check Ellis–Drossel 2020 and Riggs 2024 for horizon qualifications of the
   EBU boundary (X1/X2).
4. Cross-check X4 against Geroch 1977 / Manchak 2008 / Lesourd 2021 from the
   horizons lane in one integrated note (the two lanes' verdicts are
   complementary, not redundant).
