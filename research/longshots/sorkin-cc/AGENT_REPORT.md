# Agent report: sorkin-cc-complex-percolation

Sole-worker application, 2026-10-21. Files: `RESULT.md`, `check.py`, this
report.

## Result

- Stated Sorkin's even-convergence criterion exactly from arXiv:1104.0997v1
  Sec. 7, conditions (i)-(iii), including the straddler-sum condition.
- For complex percolation with `|q|<1`, stem events are open and the
  `n`-skeleton tail controls the straddler sum. The regularized-measure
  skeleton-chain lemma gives condition (iii), so stem-event limits exist, are
  independent of the C1/C2 approximant, and are finitely additive on disjoint
  open stem events by Sorkin's theorem.
- For `|q|=1`, the originary amplitude has no nonzero limit, so condition
  (iii) can fail; the boundary is not covered.
- Computed six stem values at two complex `p` through `m=6` (table in
  `RESULT.md`). These are finite corroboration, not the convergence proof.

## Scope and limits

- Sorkin's theorem is for open events; the report does not claim extension to
  the whole sigma-algebra or uniqueness among arbitrary countably additive
  extensions.
- The `2chain` stem-present event is distinguished from the originary event.
- Primary read depth: full text at Sec. 7 and the theorem, not the whole
  paper. DJS 1007.2725 and regularized-measure Lemma 1 are inherited.
- No new general extension theorem, novelty, physical or ontology claim.
