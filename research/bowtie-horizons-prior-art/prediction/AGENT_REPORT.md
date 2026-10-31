# Agent report: prior-art-prediction

28 October 2026. Task `prior-art-prediction`, OpenCode GLM headless worker,
worktree `agent/prior-art-prediction`. Submission for independent review; not
a final truth claim. No novelty claim is made from absence of hits.

## Done / files

- Audited the four screening claims X1-X4 from
  `research/bowtie-horizons/SCREENING.md` and `RESULT.md` against the named
  sources (Geroch 1977; Manchak 2008 + later prediction lineage; Earman 1986,
  1995; Hawking-Ellis 1973 chs. 6-7; Smeenk-Wuthrich arXiv:2009.07555) plus a
  targeted search, with focus on whether X3/X4 (minimal screening region;
  realm rigidity) are already stated.
- `research/bowtie-horizons-prior-art/prediction/RESULT.md` - verdict table
  (source x X1-X4, locator, read depth), exact quoted overlaps, per-claim
  summaries.
- `research/bowtie-horizons-prior-art/prediction/sources.jsonl` - 24 source
  records per the knowledge-base contract (id, title, url, checked_on,
  read_depth, kind, version/DOI, locators, limits).
- `AGENT_REPORT.md` (task copy) and root `AGENT_REPORT.md` (replaces a stale
  report left by the earlier `stein-gluing-audit` lane; that content is
  preserved in git history at 4716034).
- No other files touched; workboard, runner, and other lanes untouched.

## Search capability check

- `scholar_search` (openalex/arxiv/crossref/semanticscholar): WORKED from the
  first test query ("Prediction in general relativity" Geroch domain of
  prediction - openalex returned the UMN record). Used for paper discovery
  throughout.
- `exa web_search_exa` / `web_fetch_exa`: WORKED (search, PDF and HTML
  fetching). PDFs were read via exa extraction since no local PDF-to-text
  tool exists (pdftotext, pyobjc/Quartz absent).
- `serpapi_search`: FAILED mid-task - "Your account has run out of searches."
  Three Hawking-Ellis/Earman queries did not run; recorded, not retried.
- `web-search-prime`: NOT attempted, per brief (quota exhausted until
  2026-11-17).

## Source coverage (read depth)

- Full-text (this worker): Geroch 1977 (OCR scan, pp. 89-91 verified
  first-hand); Manchak 2008 (complete); Dorato-Hoefer 2021 (Disputatio symposium
  critique; keyword scan + targeted reads); Smeenk-Wuthrich 2021 (ar5iv text;
  secs. 2, 4 + refs); Lesourd 2021 (ar5iv; secs. 2-3); Friedman-Kaiser-
  Gallicchio 2013 (author PDF; abstract + secs. I-III); Jaeger 2025 NYU
  dissertation (philpapers PDF; abstract, ch. 1 intro, sec. 1.7.3); van der
  Schaaf 2026 (arXiv LaTeX source; ModalLogic + Discussion sections); Mariani
  2021 symposium intro (extract).
- Abstract-level: Budic-Sachs 1976, Muller-Hoissen 1981, Doboszewski 2019,
  Manchak-Weatherall 2018, Sbierski 2013, Ellis-Uzan 2016, Ryder 2026,
  Grandjean 2022 (extract), Teitel 2025, Arageorgis 2016, Manchak-Barrett
  2023.
- Access gates: Hawking-Ellis chs. 6-7 (CUP paywall; chapter abstracts only);
  Earman 1986 (archive.org lending-only; Google Books TOC); Earman 1995
  (author-site scan's text layer ends after the preface; pp. 125-130 target
  unread); UMN Geroch copy (WAF-gated for direct download; LSE copy used).

## Verification commands and results

- ar5iv text extraction + keyword scans (python3 over downloaded HTML):
  `sw-determinism.txt` 88,186 chars from arXiv:2009.07555; scans for
  "domain of dependence", "global hyperbolicity", "Choquet", "screen" (0
  hits), "minimal" (1 irrelevant hit) - supports X3 NOT-FOUND in SW.
- Same pipeline for Lesourd arXiv:2101.08324 (48,376 chars); FKG PDF read via
  exa fetch with in-sandbox keyword slicing ("shared causal future", "event
  horizon", "conformal time" all located).
- Dorato-Hoefer fetched twice (9k then 45k chars); in-sandbox scans for
  "potential" and "horizon": ZERO hits - confirms SCREENING.md's
  characterization of the critics.
- van der Schaaf: arXiv e-print source downloaded, tarred out, grep
  "confluence" - exact lines recorded (2^-Minkowski counterexample; S4.2 =
  Goldblatt 1980).
- Geroch quotes verified against the LSE scan's OCR text; OCR noise
  normalized and marked in RESULT.md.
- One search hit (an exa highlight) pointed to a wrong arXiv ID guess
  (1305.3946, quantum optics); discarded and the correct ID 1305.3943
  located by search before quoting.

## Verdict summary

- X1: NOT-FOUND as a claim; premise FOUND (Friedman-Kaiser-Gallicchio PRD
  2013: explicit shared-causal-future criteria in exact FLRW+Lambda,
  event horizon z=1.87; van der Schaaf: confluence failure in globally
  hyperbolic spacetimes, S4.2 side).
- X2: NOT-FOUND everywhere read (no historical-potential domain in any
  source; threshold arithmetic exists only in other guises in FKG).
- X3: NOT-FOUND as stated. Nearest neighbors: Geroch's P(q) achronal-surface
  equivalence (formally adjacent, different purpose); Jaeger's Strong
  Boundary Markov (probabilistic, static backgrounds, no minimality, no
  J^-(J^+(b))); standard D(S)-determination ingredients. Weak idle half
  (elsewhere causally unrelated to e) is folklore (Grandjean extract);
  strong idle-surplus version not found.
- X4: PARTIAL. Deterministic-MGHD half is textbook (Choquet-Bruhat-Geroch
  via Smeenk-Wuthrich; Hawking-Ellis ch. 7, gated; Budic-Sachs /
  Muller-Hoissen deterministic points; Doboszewski definitions);
  causal-past-insufficient half is the Geroch-Manchak prediction line.
  The realm-wise formulation (any realm containing D_pot(b) fixes J^+(b)
  under deterministic MGHD while J^-(b) does not) was not found.

## Strongest contrary evidence (closest priors)

1. FKG 2013 for X1's physics: if X1's value rests on "pairwise common
   futures fail in exact LambdaCDM", that is published physics with Planck
   parameters (PRD 88, 044038).
2. Geroch's p. 90 equivalence (achronal S inside I^-(q) with x in D^+(S)) for
   X3: reviewers should compare Theorem 2's (<=) direction against it; the
   purposes differ (prediction of x from q's past vs screening of b's
   future), but a referee could see the S-characterization as the same move.
3. Budic-Sachs 1976 / Muller-Hoissen 1981 for X4: a "deterministic points"
   program tying determinism to compact slices and particle horizons -
   unread full texts; the closest formal neighbor to realm rigidity may be
   in there.
4. Jaeger 2025 for X3's concept: spacetime screening conditions exist in the
   literature, though probabilistic and static-background-only.

## Limitations

- Hawking-Ellis and both Earman books not read at target depth (gates
  recorded); any X3/X4-relevant statement in them cannot be excluded. The
  brief's focus question ("is X3/X4 already stated?") is answered against
  the sources actually accessible, not exhaustively.
- Budic-Sachs and Muller-Hoissen full texts paywalled; only abstracts.
- Coverage of the Disputatio 63 C&R symposium is partial (Dorato-Hoefer full;
  other six contributions + C&R's Replies unread).
- serpapi out of quota; web-search-prime per brief; no child agents, no
  installs, no global config changes.
- No novelty claim follows from these negative searches (project standard).

## Proposed next tasks

1. Obtain library access to Hawking-Ellis chs. 6-7 and Earman 1986 ch. III /
   1995 pp. 121-135; check for minimal-screening or realm-fixing statements.
2. Audit Budic-Sachs 1976, Muller-Hoissen 1981 (and Beem-Ehrlich 1979 GRG 11,
   89, cited by Muller-Hoissen) in full: their "deterministic points" may
   contain the nearest formal neighbor of realm rigidity and of premise (L).
3. Read the remaining Disputatio 63 symposium papers (Deng, Dyke, Markosian,
   Miller, Torre, Wawer) and C&R's "Replies to Critics" full text for
   horizon/causal-potential passages (SCREENING quotes pp. 488-489; verify).
4. Read Sbierski arXiv:1309.7591v3 and Ringström's monograph for premise (L)
   (existing SCREENING review target); same pass for Manchak-Barrett 2023
   (Heraclitus condition) as the X4 contrast half.
5. Targeted causal-set-theory search: "past of the future" constructions and
   growth axioms (X1/X3), not covered here beyond abstracts.
6. Pin the Goldblatt 1980 attribution from the repo copy (bf00370321.pdf) -
   flagged unchecked in research/horizons/PRIOR_WORK_CHECK.md.
