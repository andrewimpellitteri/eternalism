# Agent report: ontology-natural-assignments (resumed run)

29 October 2026. Worker submission for independent review, not accepted
completion. Task claim and worktree preserved; only owned outputs committed.

## Done and files

- `research/ontology-reconstruction/classification/RESULT.md` — bounded
  classification of six candidate existence realms (E_all, J⁻, I⁻∪{b}, bow
  tie B, instantaneous potential D, historical potential H) against seven
  separated axes (isometry covariance, cross-model restriction, persistence,
  chronological inclusion, future exclusion, nonuniversality, transitivity)
  on explicit categories (C_GH / C_Mink / C_slab / C_cyl / C_slice), with
  four countermodels, four proved bounded lemmas, three defeated
  conjectures, one sharply bounded proposed target (T) and an independent
  philosophical reading.
- `research/ontology-reconstruction/classification/sources.jsonl` — 20
  records in the knowledge/README schema; validated (unique ids, required
  fields, valid depths).
- `research/ontology-reconstruction/classification/checks/countermodels.py`
  — rewritten exact-arithmetic witness checker (replaces the pre-resume
  dense-grid version; see Recovery below).
- `AGENT_REPORT.md` (this file, runner handback slot).

## Search capability check (required)

- `scholar_search` (MCP server `scholar_search`): **worked**. Query on
  Clifton–Hogarth/Stein definability returned the Crossref record
  (Synthese 103(3) 355–387, 1995, DOI 10.1007/bf01089733), which fixes the
  bibliographic identity of the main predecessor; openalex hits recorded as
  discovery leads only.
- `exa.web_fetch_exa`: **worked**. Fetched the arXiv abstract page
  arXiv:1502.00018v1 (Wüthrich–Callender), confirming version and date; the
  source register records abstract depth honestly.
- `web-search-prime`: **not retried**, per the brief's quota notice
  (exhausted until 2026-11-17). `serpapi` not needed. No credentials or
  private sources touched.

## Recovery from the interrupted attempt

- Preserved the pre-resume `checks/countermodels.py` intent but rewrote it:
  the dense pools (1539-point slab pool; 17×17×17 pairwise cube; cubic H(b)
  construction loop that timed out at 300 s) are **removed**. The new
  checker uses only explicit rational witnesses (`fractions.Fraction`) and
  displayed-inequality constants; universal statements are proved
  analytically in RESULT.md and are not re-established by enumeration.
- The pre-resume retraction of a historical-potential restriction
  counterexample was **resolved analytically, not from any search**: the
  full-Minkowski-ambient version of the claim is defeated (RESULT.md L3:
  future-directed ⟹ H = B, which restricts; plus an explicit in-U witness
  r=(−4/5,−1/5), z=(1/4,4/5)), while the finite-conformal-slab version is
  proved (CM4, exact rationals, with the finite past t > 0 used at exactly
  one displayed step). Both verdicts and their scopes are recorded in
  RESULT.md §4–5; neither is promoted from a search.

## Verification commands and results

```
time python3 research/ontology-reconstruction/classification/checks/countermodels.py
# 52 checks, all PASS; ~0.05–0.12 s total wall time; exit 0
# per-check O(1); max per-check time far below the 10 s / 15 s limits;
# total compute far below the 30 s budget
python3 - (sources.jsonl validation)  # OK: 20 records, unique ids,
# all required fields, valid read_depth values
```

One real arithmetic error was caught and fixed during development (a
mislabeled window constant 27/20 vs 3/2 in CM4 step iii); the corrected
case split is what now passes and is written up in RESULT.md §5.

## Source coverage

20 registered sources: 2 external items at abstract/discovery with fresh
verification (CH1995 Crossref metadata; WC2017 arXiv v1 abstract page), 6
further external records at discovery depth (locators recorded as
second-hand where so), and 12 project documents read in full text this
session (stein-gr main.tex; the five lawful-completions coordinator files;
HORIZON_LEMMA_REVIEW; PREMISE_STRESS_TEST; EXPLANATORY_ROLE_TEST;
CLAIM_STATUS; CURRENT_SYNTHESIS; NOVELTY). web-search-prime quota
constraint respected; no source is claimed as read beyond its recorded
depth. Stein 1968 locators remain unknown, as required.

## Strongest contrary evidence (against this submission's framing)

- A bow-tie theorist can accept every cell of the table and reject only the
  *salience* of A7: the table does not argue against coexisting spacelike
  events, it prices the premises (RESULT.md §6 O2, §9). The "dichotomy" O3
  is proved for six displayed rules only; T2 is open, so any reading of O3
  as a universal no-go would overstate the result.
- A fragmentalist can concede A2-failure of D and H as a *feature*
  (ambient-dependent potential), not a defect; the classification records a
  cost, not an inconsistency (§9 item 2).
- The slab categories are flat kinematic patches with artificial temporal
  boundaries; CM4's locality failure of H depends on the finite conformal
  past (L3 shows it disappears when the ambient is future-directed). The
  on-shell cylinder generalization is Target T and is unproved.
- Coordinator PREMISE_STRESS_TEST §1 already made the O4 point for
  E_all/E_past; this lane adds the axis table and the D/H rows, not the
  basic observation.

## Limitations

- No universal classification promised or attempted (RESULT.md §8).
- D's persistence column is category-relative via a project-internal
  reviewed lemma (HORIZON_LEMMA_REVIEW), not an external publication.
- CM1 configuration originates in the coordinator's stress test; this lane
  re-proves it with exact witnesses, but the source of the configuration is
  credited.
- Machine checks certify witnesses and displayed constants; the universal
  statements rest on the analytic proofs in RESULT.md §§4–5 and on
  elementary causal facts (push-up, causal convexity), not on enumeration.
- External sources read only at metadata/abstract depth this session; the
  stein-gr manuscript's page-locators for CH1995 were not checked against
  the journal PDF.

## Proposed next tasks

1. Target T (bounded): prove or refute H-restriction failure on every
   finite-duration complete cylinder; carry out the dust+Λ on-shell
   realization check (fix conformal factor and interval from the solution
   first).
2. Target T2: search for order-definable rules on C_slab satisfying A1–A6
   beyond {J⁻, I⁻∪{b}, B}; candidates with potential or distance
   quantifiers currently fail A2 — worth one adversarial attempt before
   conjecturing completeness.
3. A Lean formalization candidate: L1 (future exclusion of H) and CM4's
   exclusion case analysis are the smallest self-contained pieces; only
   after statement correspondence audit per AGENTS.md research standards.
4. Reconcile Section 9's three conditional readings with the rival lane's
   contracts at coordinator level; do not merge conclusions across lanes.

## Handback state

Branch `agent/ontology-natural-assignments`; commit contains only
`research/ontology-reconstruction/classification/{RESULT.md, sources.jsonl,
checks/countermodels.py}` and this root `AGENT_REPORT.md`. No board,
runner, shared seed, manuscript, or other lane files touched; no installs,
child agents, pushes, or merges. The prior root report content (an earlier,
already-integrated lane's handback) was replaced in the runner handback
slot per the task contract; its history remains in git.
