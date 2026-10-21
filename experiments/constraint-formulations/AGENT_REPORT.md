# Agent report: constraint-formulation-compare (corrected)

Coordinator completion, 2026-10-21, of the native correction interrupted by
the Codex usage limit. The imported GLM submission remains in
`GLM_SUBMISSION.md` and `REVIEW_STATUS.md`; it is not accepted.

## Files changed

- `SPEC.md` — corrected three-formulation comparison, conventions, closure,
  alias and local-covariance criteria.
- `formulations.py` — corrected finite implementation of A, B1–B3 and C1,
  with exact eigenvalue-surface tables, closure/alias checks and the
  resonance diagnostic.
- `corrected_output.txt` — full run output.
- `AGENT_REPORT.md` — this disposition. `INTERRUPTED.md` is retained as the
  recovery record.

## What the corrected comparison establishes

- **A (eigenvalue constraint)**: the physical sector is `ker(H-lambda)`; the
  formulation imposes no lattice or periodicity condition and requires the
  selected `lambda` to be named. At `g=0`, the two-dimensional surfaces are
  `{1/2,3/2}` for `eps=1` and `{1}` for `eps=2`, matching the closed forms.
- **B (step invariance)**: B1 uses a uniform step and closes only at selected
  `eps`; B2 imposes closure with a compensating last step and gives a
  two-dimensional history space with `p=1/3` and cumulative maps equal to the
  free spin evolution at `g=0`; B3 is a finite non-wrapping diagnostic and is
  not called a `Z_3` action when it does not close.
- **C (finite-group action)**: `U_lambda=exp[-2pi i(H-lambda)/3]` is a
  `Z_3` representation iff every energy gap from `lambda` is an integer.
  `Fix(U_lambda)` can be computed when closure fails, but is then not the
  physical space of a claimed action. When closure holds,
  `Fix(U_lambda)=⊕_j V_{lambda+3j}`, so alias multiplicity must be shown.
  The scalar-origin repair at `g=0` reproduces the matched A sector; the
  unshifted comparison can be empty or aliased.
- **Decisive resonance**: at `K_en`, `eps=2`, `g=sqrt(3)`, `lambda=1`, the
  candidate closes and `V_1` is two-dimensional, but the local
  position/readout covariance defect is `0.75` and the factorization defect
  is `sqrt(2)/2`. Commutation with `H_C` alone is not local covariance.
- **No physical equivalence claim**: B2's compensating step changes the
  schedule; the table compares dimensions and readouts under stated
  conventions. No intertwiner is asserted.

## Checks

`python3 experiments/constraint-formulations/formulations.py` exits 0 and
writes the tables reproduced in `corrected_output.txt`. The zero-coupling
surface table matches the prior `experiments/clock-three-picture` model. The
resonance closure residual is `1.6e-15`; the local covariance defect is
`0.75`.

Two numerical repairs were made during completion:

1. The fixed-space dimension in the alias table is now computed from the
   spectral condition `(E-lambda)/3 in Z` rather than from a numerically
   fragile null space of `U-I`.
2. A rounded-origin diagnostic case (`lambda=-0.5527`) was removed. It was
   not part of `SPEC.md`, and rounding made its expected `V_lambda`
   dimension numerically ill-posed.

## Scope and limits

This is an application of published constructions, not a new result. The
primary reads recorded in `SPEC.md` are at the named construction, not a
full-paper or code audit. The `K_rd` sector has no full spectral
classification here. The model is a finite `Z_3` clock plus qubit; nothing
follows about temporal ontology or interacting-clock genericity.

## Unresolved

The `A` surface at `lambda=3`, `K_en`, `eps=2`, `g=sqrt(3)` shows
non-isometric `A_k` defects in the diagnostic output; it is outside the
matched `lambda=1` comparison in `SPEC.md` and is not interpreted. A full
intertwiner classification of B conventions remains open.
