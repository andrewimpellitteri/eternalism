# Alternative to differentiating a scattering map

2026-10-28. Proposed proof architecture, not a proved control theorem or novelty claim.

## Why the earlier gate was too strong

A differentiable map from past-null-infinity profiles to globally selected solutions is sufficient for finite interpolation, but may not be necessary. Finite-cone solutions have ordinary local dependence on their smooth data. One can try to solve the interpolation problem **before** taking the infinite-past limit, then pass the equations to a jointly selected subsequential limit. This avoids differentiating an unspecified scattering selection.

## Precise finite-cone certificate needed

Fix N compact smooth profile directions F_k, a compact late direction G, a flat center launch event b, and common proper times T_j. Let Phi_{epsilon,x}=epsilon(sum x_k F_k + beta(x)G), where x lies in a fixed small closed ball and beta compensates the quarter-integral profile charge. The complete finite-cone profile class must remain in LOY's uniform smallness hypotheses, with uniform derivative bounds. Let H_n(x) be its vector of central proper-time scalar readings in the finite-cone solution with vertex u_n.

Sufficient estimates are:

1. For each n, H_n is continuous on the same parameter ball. Mark b inside the exactly flat pre-pulse region, whose flat proper-time normalization is the same for all x.
2. Uniform linear response WITHOUT differentiation: epsilon^{-1} H_n(x)=x+R_n(x), with sup over n,x of |R_n(x)| <= C epsilon^2 (or any remainder tending to zero uniformly with epsilon). Normalize F_k at the desired flat center times so the linear evaluation matrix is the identity. Proper-time motion and the late-tail causal boundary are part of this estimate.
3. Every sequence x_n in that ball has a converging subsequence of parameters and corresponding finite-cone solutions on compact spacetime sets, strongly enough to pass central proper-time readings and the exact flat past to the limit. Bounds must be uniform on the whole parameter ball; a theorem for a fixed profile alone is insufficient without checking the constants.

For a target z strictly inside the ball, make |R_n| smaller than dist(z,boundary). Brouwer degree of x+R_n(x)-z equals that of x-z on the boundary, so H_n(x_n)=epsilon z for some x_n for every n. Compactness and item 3 then give an actual global limit with those exact readings. Each target may use its own subsequence and selected solution; no canonical or continuous limiting solution map is asserted.

The identity for the compensated profile charge passes through x_n -> x, but identification with an actual global Bondi/ADM charge remains the separate mass-limit obligation. The result is not yet fixed-ADM control.

## Candidate uniform perturbative estimate

Use the exact identity along fixed v:

  partial_v Psi(u,v) = Phi(v)/2 + integral_{u_n}^u K Psi(u',v) du',
  partial_u lambda = K r,
  K=2m nu lambda / [(1-mu) r^3].

The cone gauge has lambda=1/2. If the source mass/field bounds imply integrable estimates K Psi=O(epsilon^3) near the axis and O(epsilon^3 r^{-1-delta}) at large r, and K r=O(epsilon^2) near the axis and O(epsilon^2 r^{-1-delta'}) at large r, uniformly in n and x for positive delta,delta', then integration yields lambda_axis=1/2+O(epsilon^2) and phi_axis=Phi(t)+O(epsilon^3). At the axis nu=-lambda and d tau/dt=2lambda, so over a fixed bounded coordinate-time window the clock correction is O(epsilon^2); bounded derivatives of the profiles then keep the scalar reading error O(epsilon^3). All constants must be checked from actual source estimates, not inferred from dimensional scaling.

This is a proposed route to a uniform remainder, not a claim those inequalities have been established here. In particular, compact-support class constants, behavior at the axis, radial integration, and clocks need an explicit proof.

## Red-team obligations

- Compactness must allow n-dependent profiles, not just a fixed incoming profile. Identify the limiting radiation data too; compact convergence alone does not do that at null infinity.
- Future readings must stay in a common compact coordinate window for all parameters; a lower lapse bound helps but is not the entire clock estimate.
- A scalar reading is invariant under coordinates but its sign is affected by internal phi -> -phi. Use signed scalar in the explicitly unquotiented field theory or recheck the degree/rank argument for curvature readings near nonzero baselines.
- N independent readings of one scalar along one observer still may be achieved by globally isometric solutions with different observer placements in special families. Demonstrate independent physical content or explicitly require nonisometric completions.
- None of this closes regular four-metric reconstruction at the axis, proves ADM existence, or establishes novelty.

Compared with the earlier inverse-function route, the theorem to seek is a uniform nonlinear remainder and finite-cone continuity, not necessarily a Frechet-differentiable scattering map. If that remainder is already standard in the primary literature, this is a corollary rather than a frontier contribution.
