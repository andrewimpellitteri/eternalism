# Finite-cone continuity from compactness and uniqueness

29 October 2026. Coordinator replacement proof for the rejected GLM Lipschitz argument. Source-conditional mathematical corollary; independent proof review pending. No novelty claim and no smooth four-dimensional reconstruction claim.

## Exact aim

The finite-degree route needs continuity of each finite-cone readout map H_n. It does not need a Lipschitz estimate, a modulus uniform in n, or a globally selected continuous scattering map. Discard the invalid implication W<=delta+aW -> W<=delta exp(aT) in the worker submission. The proof below does not use its difference estimates.

## Source inputs actually checked

Luk–Oh–Yang, arXiv:1605.03893v1 (12 May 2016): Theorem 1.1 and Remark 1.2; Definition 2.1 and cone conditions (2.4)–(2.5), plus the local existence/uniqueness paragraph; Proposition 3.18 including its uniformity in the cone cutoff and in the second-derivative size; Section 4 from its higher-order bounds through compact convergence and the limiting equations. Sections 3.3–3.4 supply the bounded field and m=O(r^3) behavior at the axis.

The needed consequence of these printed bounds is: on every closed finite characteristic triangle, families with common small-data constants and a common second-profile-derivative bound are relatively compact in

    r in C^2; phi, partial_v(r phi), partial_u(r phi), m in C^1.

This is the same topology used in the source's Section 4 compact-limit construction, including the axis. Section 4 explicitly provides mixed derivative control from the equations and C^2 compact bounds for m. We use the estimates with a fixed cone vertex and varying profiles instead of one profile and moving vertices. The constants depend on the common hypotheses, not on an individual member.

Typography check: Section 4's displayed small bound for the sum of first through third derivatives of r cannot be literal for its first-derivative term: lambda=1/2 on the cone. Use Theorem 1.1 for order-one geometry and Proposition 3.18/Section 4 for the higher-order boundedness. No step needs an impossible O(epsilon^2) bound for lambda itself. The leading phi in Section 4's convergence display is likewise read as the approximating phi^(j). These checks should be retained in a source audit.

## Setting

Let X be a compact metric parameter space. Let x -> Phi_x be continuous in C^2 with common compact support [A,B], common LOY smallness constants (gamma,epsilon_tilde), and a common bound for Phi_x''. Choose epsilon_tilde below both source thresholds epsilon_1(gamma),epsilon_2(gamma). The FINITE_CONTROL.md family has these properties on a closed ball where beta stays positive.

Fix u_0<A. For each x let S_x=(r_x,phi_x,m_x) be the unique normalized finite-cone global C^1 solution on Q_[u_0,infinity), provided by Theorem 1.1; smooth profile data give the higher-order bounds above. Fix a compact readout triangle inside that domain. Write lambda_x=partial_v r_x.

### Proposition

The map x -> S_x is continuous on every compact triangle in the indicated topology. In particular its axis traces phi_x(t,t) and lambda_x(t,t) vary continuously in the uniform topology on every bounded axis interval. The associated finite-cone central-clock readout map H_n is continuous.

## Proof: identify every subsequential limit

1. Take x_j -> x. The profile hypotheses and higher bounds are uniform in j. On the exhaustion triangles D_R={u_0<=u<=v<=R}, Arzela–Ascoli and diagonal extraction give a sublimit S with the displayed compact convergence. The axis r=m=0 is included in these closed triangles, so its boundary conditions persist.

2. The limit has the regularity required by Definition 2.1 for k=1: partial_u r and partial_v r are C^1 because r is C^2, and phi and both first derivatives of r phi are C^1 by the convergence. The uniform geometry bounds pass to lambda>=1/3, -2/3<=nu<=-1/6 and 1-mu>=1/2. They supply the definition's positive lower lambda bound and finite lower nu bound, and keep all off-axis denominators nonzero.

3. Away from the axis, pass to each SSESF equation using this convergence: r>0 there, the second derivatives of r and r phi converge, and the first derivatives of m and phi converge. At the axis the mass estimate m=O(epsilon_tilde^2 r^3), bounded phi derivatives and nonzero lambda,nu make the right sides extend continuously to zero. The wave-equation sides are continuous from the C^2 convergence of r and r phi. Thus the same regular reduced equations and boundary interpretation hold up to the axis. This is exactly the limit-passage category used in Section 4, rather than a proposed Cartesian metric extension.

4. The initial data are the limiting profile Phi_x. On u=u_0, lambda_j=1/2 and partial_v(r_j phi_j)=Phi_xj/2; uniform convergence on each finite initial segment passes both equalities to the limit. The vertex normalization r=m=0 persists. The diagonal limit is defined on the full finite-cone domain. It is therefore a global normalized C^1 solution of the same characteristic problem as S_x, in the source's uniqueness class. Theorem 1.1/local characteristic uniqueness identifies S=S_x.

5. Any subsequence of S_xj has a subsubsequence with that same limit. If the whole sequence failed to converge on one compact triangle, a subsequence remaining a positive distance away in one indicated norm would, by the same relative compactness and uniqueness, have a subsubsequence converging to S_x: contradiction. This proves sequential continuity, hence continuity since X and these local function-space topologies are metrizable.

No subtraction of 1/r expressions, no Gronwall estimate and no differentiability of a solution-selection map are used.

## Clock and readouts: explicit passage

Choose a common pre-pulse launch coordinate t_b in (u_0,A) and proper-clock target values T_j<=T_max. Set t_star=t_b+2T_max+1. On the axis define the reduced central clock

    tau_x(t)=integral_[t_b,t] 2 lambda_x(s,s) ds.

Since lambda>=1/3, tau'_x>=2/3, so tau_x(t_star)>T_max uniformly. The inverse t_x(T) is defined on the same [0,T_max]. Uniform convergence of lambda_xj to lambda_x implies uniform convergence of the clocks, and

    sup_T |t_xj(T)-t_x(T)| <= (3/2) sup_t |tau_xj(t)-tau_x(t)| -> 0.

Uniform convergence of phi_xj on the axis and uniform continuity of the limiting phi_x there now give

    phi_xj(t_xj(T_j),t_xj(T_j)) -> phi_x(t_x(T_j),t_x(T_j)).

Thus every H_n is continuous. Source flat pre-pulse uniqueness makes phi_x(b)=0 for all x. If readouts subtract the launch value, the same conclusion follows directly from continuity of that value as well.

The clock is a reduced geometric expression. Calling it the proper-time clock of a classical four-dimensional regular central worldline still requires the separately gated axis reconstruction. This note does not bypass that gate.

## Parameter-dependent cones and degree roots

For fixed n, use u_0=u_n. The proposition supplies precisely the per-n continuity required by degree. The separate CUBIC_TRACE.md uniform remainder must still be used with constants uniform in n and x; no such uniformity follows merely from continuity.

For a sequence of degree roots x_n in X, extract x_n -> x_*. The same source bounds are uniform on the full family and in u_n. Section 4's exhaustion argument therefore applies to the varying profiles as well. It yields a global reduced sublimit with the stated compact convergence. No uniqueness at past null infinity is claimed or needed here.

At each fixed (u,v), the Section 4 remainder bounds pass to the limit along with Phi_xn(v)->Phi_x*(v). Only THEN send u->minus infinity to recover the incoming profile Phi_x*. Uniform clock and axis convergence on the fixed readout interval pass the root equations exactly. This is existential, target-by-target interpolation, not continuity of a global scattering map.

With the separate reviewed incoming-mass calculation and uniform cubic remainder retained, this repairs the named continuity obstacle and the profile-uniform compactness step at the reduced-solution level. It does not close smooth axis reconstruction, source novelty, or unmarked nonisometry. The replacement argument itself should receive independent review before the acceptance ledger is upgraded.
