# Agent report: incoming energy and finite-control audit

## Result

The exact nonlinear incoming boundary mass in the Luk–Oh–Yang normalization is $E_{\rm in}=\frac14\int_{\mathbb R}\Phi(v)^2\,dv$ for smooth compact profiles in the reduced global solution class. This is obtained by integrating the exact mass transport equation on each fixed finite interval $[A,V]$ in the global limit. The flat pre-pulse wedge supplies $m(u,A)=0$; uniform decay, lapse, and radiation-trace estimates give the flux limit $\frac14\Phi^2$. No moving-cone interchange or derivative-of-limit step is used. The result identifies incoming boundary mass, not ADM mass.

For a finite-dimensional compensated profile family, exact profile-norm equality survives a convergent parameter subsequence. Section 4 radiation recovery is uniform when the profile family has common compact support, common LOY smallness, and uniform derivative bounds. Applying the fixed-profile mass calculation to the resulting global limit gives its actual incoming boundary mass. The degree-before-limit route needs no differentiable global scattering map or uniqueness among global limits for its existential target-by-target conclusion.

## Remaining gates

- Prove finite-cone readout-map continuity on the common parameter ball, including the center and proper-time clock.
- Verify every constant in the perturbative remainder is uniform in cone index and profile parameter, including the common readout window and late-tail causal separation.
- Present the n-dependent compactness argument and show convergence of the central fields and clocks needed to pass exact readings.
- Regular four-dimensional reconstruction at the axis remains with the regularity audit. ADM existence and equality with incoming boundary mass remain open.

## Evidence and checks

- Primary source: Luk–Oh–Yang, arXiv:1605.03893v1, full text selectively checked. Locators and assumptions are recorded in `sources.jsonl`; the direct global-mass deduction is detailed in `REVIEW_INCOMING_MASS.md`.
- `sources.jsonl` was parsed and checked for the required keys `id`, `title`, `url`, `checked_on`, `read_depth`, `kind`, `relevance`, and `limits`.
- The exact normalization gives $\frac12\lambda(1-\mu)(\psi-\phi)^2\to\frac14\Phi^2$, where $\psi=\lambda^{-1}\partial_v(r\phi)$.
- The degree, n-dependent profile recovery, selection scope, and remaining gates are reviewed in `REVIEW_DEGREE.md`. The marked-extension correction and conditional axis Ricci regularity are recorded in `REVIEW_REMARKING.md`.
- No computational tests, installs, broad source survey, commits, or external actions were performed.

## Scope

No novelty claim, ADM claim, smooth four-dimensional theorem, or canonical global solution-selection claim is made. Source theorem existence alone does not prove the finite-cone continuity and readout-passage gates listed above.
