# Recovering the incoming mass in the selected global solution

2026-10-28. Coordinator deduction from LOY v1 estimates; independent review requested. This addresses the incoming Bondi limit, not ADM mass or regular four-metric reconstruction.

## Avoid the moving-cone limit

Work directly in any global compact limit produced by the LOY construction for a compact profile Phi supported in [A,B]. The pre-pulse wedge v<A has m=0 exactly. Continuity gives m(u,A)=0 for u<A. Fix a finite V>A. The exact global mass transport equation gives, for u<A,

 m(u,V) = integral_A^V [lambda(u,v)/2] (1-mu(u,v)) X(u,v)^2 dv,
 X=lambda^{-1}partial_v(r phi)-phi.

The source estimates hold in the limiting solution. On the fixed finite interval v in [A,V], as u tends to minus infinity:

- r >= (v-u)/3 tends uniformly to infinity;
- phi=O(epsilon r^{-gamma}) tends uniformly to zero (Proposition 3.3);
- mu=2m/r=O(epsilon^2 r^{-gamma}) tends uniformly to zero (Proposition 3.4);
- lambda tends uniformly to 1/2 by the explicit section 4 log-lambda estimate;
- lambda^{-1}partial_v(r phi) tends uniformly to Phi(v), by the explicit section 4 cubic remainder and the preceding lambda estimate.

All constants are independent of v in that fixed finite interval; the bounded compact profile supplies uniform |Phi|. Thus X tends uniformly to Phi. The entire mass-flux integrand converges uniformly to Phi(v)^2/4. Integrating over this fixed finite interval proves the actual global boundary limit

 m_-(V):=lim_{u->-infinity}m(u,V)= (1/4) integral_A^V Phi(v)^2 dv.

No derivative is interchanged with a boundary limit and no moving finite-cone vertex is identified with a fixed global point. For V<A the limit is zero. Taking V to plus infinity after this established global limit yields the total incoming boundary mass

       E_in := lim_{V->infinity} m_-(V) = (1/4) integral_R Phi^2.

This uses exact pre-pulse flatness to fix the integration constant; without that, a residual incoming mass could remain. It uses compactness-limit estimates for a specified profile. For n-dependent profiles converging in a common bounded smooth compact class, check that the same section 4 remainder constants are uniform, so the recovered radiation profile is indeed the parameter limit.

## Strength and limits

If the estimate passage and exact flat-wedge deduction are accepted in the source's reduced solution category, this closes the energy lane's named uniform finite-v flux-convergence obligation. The quarter-integral is then the incoming mass of the selected global solution, not merely a charge of approximating cone data.

It still does not identify the diagonal spatial-infinity Hawking-mass limit with this iterated boundary mass. ADM existence and equality remain separate. It does not improve axis atlas regularity. It does permit exact equal **incoming boundary mass** through the disjoint-tail amplitude formula once an admissible jointly selected family is constructed.
