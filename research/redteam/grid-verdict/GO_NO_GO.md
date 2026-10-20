# Go / no-go: assigning live grid cells

2026-10-20. **No-go for bulk assignment. Go for one bounded pilot once
CONTRACT.md gaps G1 and G2 are fixed.**

## Why not bulk

- 285 S1+T1 cells exist (180 + 105). The GLM provider throttled at about a
  dozen concurrent workers (2026-10-19) and exhausted a 5-hour quota with six;
  the runner now uses 2 slots. Bulk assignment would queue for days and starve
  the selection-gate critical path (`rt-loadbearing-rereads-rc` →
  `rt-selection-decision-gate`).
- Without G1 and G2, a correct worker cannot record a refuted universal claim,
  and the literal `ontology-leap` rule produces false kills of explicit bridge
  arguments. Coverage numbers from such a run would be misleading.
- Gates check shape and provenance only (9d821f3). The substantive criteria in
  `CRITERIA.md` need a reviewer per advance.

## Pilot

- **Scope:** two `s1` batches of 6 cells each (12 cells), chosen from physics
  rows whose lanes are accepted and full-text (e.g. P01 special relativity,
  with `foundations` and `axiomatic-relativity`). Not T1 yet: direction (G4) is open.
- **Cap:** at most 12 live (assigned, unresolved) S1/T1 cells and 3 live
  adversary cells at any time. No S2 until G3 is settled.
- **Expected outcome:** most cells killed, per CONTRACT.md. Treat these as audit
  triggers, not targets:
  - advance rate above about 1 in 6: audit every advance against `CRITERIA.md`
    before assigning adversaries;
  - every cell killed `known` at abstract depth: spot-check those kills for
    false kills before calling the region covered;
  - any `ontology-leap` kill: check it against G2 by hand.
  These thresholds are operating heuristics for a 12-cell sample, not
  statistics about the literature.
- **Adversary:** run the A stage on a different model where one is available
  (grid/README.md "Limits"). Same-model adversaries share failure modes.
- **Exit:** after the pilot, compare verdicts with a coordinator read of 3
  random kills and every advance. Expand only if no gate defect is found.

## Preconditions checklist

- [x] Gate fixes and regression tests (`grid-regression-tests`, 9d821f3)
- [x] Independent design review (`grid-adversarial-design`)
- [ ] CONTRACT.md amended for G1 (`refuted`) and G2 (`ontology-leap`)
- [ ] Pilot rows chosen from accepted lanes
- [ ] Provider quota checked before launch
