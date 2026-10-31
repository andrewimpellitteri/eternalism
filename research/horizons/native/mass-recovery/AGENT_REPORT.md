# Coordinator mass-review recovery

Task horizons-mass-review-recovery. Submitted for review, 27 October 2026.

## Changes

- RESULT_REVIEW.md reconstructs both perturbation arguments, documents
  physical scope and quantifiers, and records three errors in the interrupted
  numerical referee control plus one factor error in its intermediate prose.
- check_recovered.py is a repaired derivative of the preserved GLM control.
  It is not represented as a wholly independent implementation.
- verification.json records the completed bounded run and its limitations.

## Checks and evidence

Exact constant-potential solver controls for k=1,7,19 pass. Independent
midpoint quadrature confirms the exceptional k=1 dust coefficient and the
generic coefficients. The Green-kernel integral is 0.9999999999999999.
At the same 96-mode truncation, the constant-potential derivative differs
from its exact finite-sum reference by about 1.85e-9; the dust period derivative
differs from the finite-sum operator identity by about 1.31e-10. Halving the
time step at fixed cutoff changes the dust period derivative by 4.97e-10.
The completed standard-library run took about 55 seconds; no installs.

Truncation error is distinct: the unperturbed target residual is 1.60e-5,
and a raw finite-sum sample has the opposite sign from the exact theorem at
δ=−1e-4. Subtracting the finite baseline gives the expected signed increment.
The combined spectral/time comparison changes the derivative by 1.22e-5;
there is no certified infinite-tail error bound. These facts are reported,
not hidden behind a pass label. Exact past agreement and the sufficiently-small
mass result are analytical statements, not conclusions of finite projection.

The initial repaired run failed an inherited assertion comparing different
finite/infinite quantities. The reference was corrected to the exact finite
sum, keeping the 1e-7 solver tolerance. The final run passes all stated controls.

## Limits

This coordinator authored the original extension and therefore cannot supply
its missing independent proof review by repairing a stopped referee checker.
A separately claimed native final-proof review addresses that gate. The
massless fixing theorem is a premise; priority and missing original sources
remain separate gates. Neither manuscript nor original stopped worktree was
edited. No quantum, interacting, backreacting or ontological claim follows.
