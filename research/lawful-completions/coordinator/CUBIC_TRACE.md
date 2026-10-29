# Uniform cubic central trace estimate

2026-10-28. Coordinator source-backed deduction, awaiting independent red team. Primary input: Luk--Oh--Yang arXiv:1605.03893v1, Proposition 3.3, Proposition 3.4 (3.16), Lemma 3.1, Proposition 3.8 (3.25), and section 4 immediately following (4.1). Source depth: selected full text. Source register: coordinator/sources.jsonl, lawful-coord-luk-oh-yang2016.

## Corrected gate

Section 4 already states the uniform finite-cone estimate

 |lambda_n^{-1} partial_v(r_n phi_n)(u,v) - [1/(2 lambda_n(u,v))] Phi(v)|
 <= C epsilon^3 max(v-u,1)^(-2 gamma).

It also states

 |log lambda_n(u,v)-log(1/2)| <= C epsilon^2 max(v-u,1)^(-gamma).

At the axis u=v=t, regularity gives partial_v(r phi)=lambda phi. Therefore

 |phi_n(t,t)-Phi(t)/(2 lambda_n(t,t))| <= C epsilon^3,
 |2 lambda_n(t,t)-1| <= C' epsilon^2.

Since |Phi|<=epsilon, these imply the uniform central estimate

             |phi_n(t,t)-Phi(t)| <= C'' epsilon^3.

The constants are independent of the cone vertex. This is a direct use of an explicit source estimate, not a formal differentiation in the profile parameter. The same inequality holds in any compact limit for the prescribed profile, using the stated convergence and axis identities.

## Proper-time correction on a fixed future window

At the regular axis r(t,t)=0 gives nu=-lambda. Since m/r tends to zero there by (3.16), the reconstructed central lapse is Omega=2lambda>0. Fix a flat launch event at t_b before all profile supports, and normalize tau(t_b)=0. Then

 tau_n(t)=integral_{t_b}^t 2 lambda_n(s,s) ds,
 |tau_n(t)-(t-t_b)| <= C epsilon^2 |t-t_b|.

For T in a fixed bounded interval [0,T_max], invert this strictly increasing clock. For sufficiently small epsilon,

 |t_n(T)-(t_b+T)| <= C_T epsilon^2.

The source profile hypothesis |Phi'|<=epsilon consequently yields

 |phi_n(t_n(T),t_n(T))-Phi(t_b+T)| <= C_T' epsilon^3.

This compares actual central proper-time readings, subject to the regular-axis interpretation used in reconstructing the clock. Uniform compact convergence of lambda and phi passes both clocks and readings to the limit. No profile derivative of the global solution is used. The broader C2 four-metric reconstruction gate remains separate.

## Immediate useful consequences

1. A nonzero profile Phi=epsilon F with F(t_*) nonzero and fixed F yields a nonzero central trace for sufficiently small epsilon. Exact flatness earlier and the source's C1 scalar trace give a later nonzero derivative. This avoids relying exclusively on sideways timelike-boundary uniqueness to establish central visibility.
2. For a fixed finite-dimensional smooth compact profile class, normalize fixed F_k so F_k(t_b+T_j)=delta_kj and place the tail after the common readout window. If the family obeys LOY hypotheses with smallness parameter C_0 epsilon uniformly in its parameters, then H_n(x)=epsilon x+O(epsilon^3) uniformly. Replacing epsilon by C_0 epsilon changes constants only. The degree route therefore has its proposed quantitative remainder from the printed source estimates.

Not yet concluded here: continuity of every finite-cone readout map on the chosen parameter ball in the exact regularity class, compactness with n-dependent profiles including recovery of their incoming limits, or fixed physical mass of the global limits. Those are the remaining obligations for DEGREE_ROUTE.md. A charge calculated from profiles is not automatically a spacetime charge.

## Audit correction

The earlier blanket statement that control required a differentiable global scattering map was too strong. Such a map is needed for the particular inverse-function proof, not necessarily for existential finite interpolation via continuous finite-cone maps and compactness. The source already supplies a uniform cubic trace approximation; this should not remain listed as a wholly missing estimate.
