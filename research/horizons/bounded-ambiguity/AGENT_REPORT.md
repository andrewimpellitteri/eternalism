# Coordinator submission: bounded ambiguity

27 October 2026. Task: horizons-bounded-ambiguity. Status: submitted for
independent review, not accepted or integrated into either paper.

## Changes and evidence

- RESULT.md gives a self-contained pointwise upper bound for a spatially
  homogeneous time-dependent scalar potential on the unit Einstein cylinder.
  It applies the estimate to all smooth hidden alternatives with a bounded
  conformal Cauchy-data norm and exact agreement on the entire past.
- For ordinary physical mass on the fixed dust background, the upper bound
  is O(m²). Physical fields require the additional factor 1/a(t).
- check_bound.py and verification.json provide bounded numerical controls,
  not a numerical proof of the infinite-mode theorem.
- sources.jsonl records the classical source context and actual reading depth.

## Checks

The standard-library check passed: exact constant-potential comparisons for
k=1,3,9; zero-perturbation control; S³ multiplicities for n=0..9; 24 dust
modes at three mass-squared values; modal and partial point-functional bounds;
and refinement from 2048 to 4096 steps. Maximum refinement difference was
5.73e-8, below the predefined 1e-7 threshold. No dependency installation.

The analytic proof uses Volterra/Gronwall bounds, the spectral addition
identity, and a summable evaluation kernel. The numerical truncation does
not establish the full operator estimate or exact past agreement.

## Limitations and review questions

Independent review must check the joint position/velocity normalization,
the smooth extension to the auxiliary endpoint slice, and the implication
from vanishing past data to the unperturbed fixing set. Smooth coefficients
on the closed auxiliary interval allow extension from an interior Cauchy
slice; the physical spacetime still excludes the singular endpoint.

This is not a noisy-record stability or practical-prediction theorem. The
norm is conformal initial data, not a measured physical energy budget.
Uniform physical-field control excludes singular endpoints. Spatially varying
potentials, interactions and backreaction are outside scope. Matching lower
bounds depend on the separate mass-loss proof surviving review. The estimate
uses classical ingredients and carries no novelty or ontology claim.

No manuscript, worker output or unrelated user changes were edited.
