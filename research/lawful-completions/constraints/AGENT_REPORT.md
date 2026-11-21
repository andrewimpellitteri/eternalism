# AGENT_REPORT: lawful-completions-constraints

Worker submission for review - not accepted completion. Date: 2026-10-28.
Branch: `agent/lawful-completions-constraints`. Worktree:
`/Users/andrew/eternalism/.worktrees/lawful-completions-constraints`.

## Done / files

- Extracted exact hypotheses and conclusions of the four brief leads
  (arXiv:2107.02441, 2107.02449, 2210.09663, 1606.03078) at primary pages;
  deep-read (partial) Corvino-Huang Theorems 1.1-1.4 + Prop 2.1/2.2 +
  Example 2.4, and Czimek-Rodnianski Theorems 2.7/2.8/2.9 + Corollary 2.13.
- Delivered one conditional sufficient lemma (Lemma P: whole-past-preserving
  future change via fixed causal footprint + localized constraint-step
  surjectivity + free matter data) with proof sketch, honest
  elementary-vs-load-bearing labels, and falsifier.
- Named three missing steps (M1 genericity at degenerate interior annuli;
  M2 characteristic gluing with coupled matter; M3 KID correspondence at
  non-vacuum data), each with a falsifier.
- Compared assumptions to the shared hierarchy A-D without novelty inflation;
  verdict for the lane: CONDITIONAL.

Files (all inside allowed paths):
- `research/lawful-completions/constraints/RESULT.md` (main deliverable)
- `research/lawful-completions/constraints/sources.jsonl` (12 records,
  lane-prefixed IDs, contract fields incl. read_depth and limits)
- `AGENT_REPORT.md` (this file, root, for handback)

## Search capability check

- Briefed server/tool `web-search-prime` (Z.ai): **FAILED** - MCP error -429,
  code 1310, "Weekly/Monthly Limit Exhausted. Your limit will reset at
  2026-11-17 10:00:29". Tested with the query "Corvino Huang local gluing time
  symmetric initial data Einstein equations". Recorded per brief.
- Fallback used throughout: `serpapi_search` tool (worked; 11 queries) +
  direct `webfetch` of arXiv abs/HTML pages (worked for all primary pages;
  one inspirehep.net fetch returned no output - JS-rendered page, skipped).
  Two late SerpApi queries returned empty results (absence-check queries);
  absence claims in RESULT.md are qualified accordingly.

## Source coverage

Primary pages fetched: arXiv abs 2107.02441, 2107.02449, 2210.09663, 1606.03078
(+ its full arXiv HTML v2, secs 1-2.3 deep), 2308.13031, gr-qc/0610045;
arXiv HTML 2210.09663v1 (intro + secs 2.3-2.6 deep); researchseminars.org talk
page (Oh-Luk-Mao-Tao h-principle). Secondary attribution recorded for
Corvino-Schoen JDG 2006, Corvino CMP 2000, Chrusciel-Delay Memoir,
Fischer-Marsden/Moncrief - flagged in RESULT.md sec. 5 as required
verifications, not claimed as read. Read depths per contract in
`sources.jsonl` (abstract / full-text-partial / discovery, with locators).
Journal statuses: 1606.03078 published (Calc. Var. PDE, DOI verified on arXiv
page); gr-qc/0610045 published (CQG 24, 2007, journal-ref on arXiv page);
2107.02441/02449, 2210.09663, 2308.13031 v1-only, no journal-ref seen -
statuses unverified, recorded as limits.

## Verification commands and results

- `python3 scripts/agents.py brief lawful-completions-constraints` - brief
  retrieved; owns = `research/lawful-completions/constraints/` + root
  AGENT_REPORT.md.
- All arXiv extractions re-run locally, e.g.:
  `curl -sL https://arxiv.org/html/2210.09663v1` then a python
  strip-tags/extract of secs 2.3-2.6 (Theorem 2.7, 2.8, 2.9, Def 2.12,
  Cor 2.13 verbatim) - confirms the hypotheses quoted in RESULT.md
  (charge gaps Delta-E = C1*eps, |Delta-L| <= C2 eps^2, eps^-1 Delta-E
  dominating Delta-P, Delta-G).
- Corvino-Huang references cross-checked from the fetched HTML bibliography:
  [7] Corvino-Schoen, J. Differential Geom. 73 (2006) 185-217; [12],[13]
  Fischer-Marsden; [19] Moncrief, J. Math. Phys. 16 (1975) 493-498.
- No installs, no large runs, no child agents, no board/runner edits.

## Strongest contrary evidence

1. Corvino-Huang's own remark (sec. 1 after Thm 1.4): their deformations do
   NOT obtain DEC equality - kills any attempt to use DEC theorems for the
   fixed-matter lemma (the cheapest coupled shortcut).
2. Corvino-Huang Example 2.4: 10-dimensional adjoint kernel at flat data -
   any "no genericity needed" claim for interior annuli is false at flat
   base data; linearized range obstruction (pairing against kernel elements)
   is the concrete mechanism M1 asks about.
3. Czimek-Rodnianski Cor 2.13 requires a strictly positive ADM energy gap
   (Delta-E = C1 > 0) - obstruction-free gluing cannot match charges exactly
   to arbitrary targets; and its null theorems perturb the seed-side data at
   O(eps), so ACR/C-R null gluing cannot by itself preserve a specified past
   exactly (only the opposite end is matched exactly).
4. Novelty-kill risk for the lemma: the composition "free matter data +
   constraint-map surjectivity" is conceptually simple and may already be
   implicit in Chrusciel-Delay's Memoir (unread) - recorded in RESULT.md
   sec. 5; do not claim it as new until that is checked.

## Limitations

- Corvino-Schoen 2006 and the Chrusciel-Delay Memoir were not read at primary
  level; Lemma P's constraint step (P3) is conditional on their exact
  statements (support properties; validity at non-vacuum base data).
- Absence claims (no coupled-matter localized constraint gluing; no
  characteristic gluing with matter) are search-depth negatives only.
- ACR I/II read at abstract depth; C-R norm definitions (sec 2.2) unread -
  regularity recorded only via the authors' X / X^{h.f.} notation and ACR II's
  abstract-level C^{m+2}/C^2 statement.
- h-principle lead exists only as a talk abstract; no manuscript located.
- Single-point non-degeneracy of the changed observable is a genericity
  clause (open-dense-type argument), not proven here; flagged inside the lemma.

## Proposed next tasks

1. Primary verification pass on Corvino-Schoen 2006 (local surjectivity
   proposition) and Chrusciel-Delay Memoir (does it already cover prescribed
   (mu,J) source shifts at general (g,pi)?). This decides whether Lemma P is
   citation-complete or folklore-plus-packaging.
2. M1 sharp form: obstructed vs unobstructed compactly supported shifts on a
   flat interior annulus (projected-surjectivity pairing vs C-R/Mao-Oh-Tao
   nonlinearity).
3. M2 feasibility: linearized null constraint system with scalar transport -
   is the conserved-charge obstruction space still 10-dimensional?
4. Coordinator check: does the baseline Vaidya construction already realize
   Lane A/B (likely), so the coupled-scalar realization stays the new step?

## Blockers

None blocking submission. `web-search-prime` quota (resets 2026-11-17)
limited one search channel; fallbacks sufficed.
