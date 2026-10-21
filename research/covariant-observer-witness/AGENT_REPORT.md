# Agent report: covariant-observer-witness

Sole-worker result, 2026-10-21. Files: `RESULT.md`, `check.py`, this report.

## Result

A finite comparison of two observer algebras for the phase-aligned event:

- **Cardinality-only:** the event is a proper subset of the level, so its
  projector is outside the algebra (and outside the adjoint image of the
  identity channel on that algebra). Unreachable by construction.
- **Unlabelled-causet / permutation-orbit:** for complex percolation at
  `p=(1+i)/2`, the phase `(L-h)pi/4` is an isomorphism invariant, so the
  ray event is a union of classes and lies in the class-pinching channel's
  adjoint image. The phase survives the label quotient. The symmetric binary
  register shows the same behaviour because its phase depends only on the
  word count.
- Within-class dephasing does not remove the class-level phase; retaining only
  cardinality does. The distinction is the algebra, not the number of records.

The selected class sum grows in the finite range tested (exact values in
`RESULT.md`), but no infinite divergence theorem is claimed. The explicit kill
criterion is boundedness of the class sum or failure of class-invariance of
the phase.

## Checks

`python3 research/covariant-observer-witness/check.py`:
- enumerates labelled causets through `n=6`;
- verifies that `A_p` and its phase are constant on isomorphism classes;
- verifies that the selected event is a proper subset of every level;
- computes exact class sums and exact binomial register sums through `n=20`.

All assertions pass. This is finite corroboration; the infinite scaling
question is open.

## Scope and limits

- `A_iso` is a mathematical quotient, not a derived causal-set observer,
  local region, or physical instrument. No claim that a cosmological observer
  can access class labels, phases, or coherent erasure.
- No new full-text primary reads; covariant-event definitions are inherited
  from the audited Surya–Zalel / Dowker–Zalel records and the project's
  event-filter reports.
- No new general observer theorem, no priority claim, no ontology claim.
