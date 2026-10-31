# A fixed-matter GR realization of the historical-potential counterexample

2026-10-28. Direct exact-solution calculation; elementary baseline, no novelty or observational-fit claim. Depends on the causal classification in HISTORICAL_POTENTIAL.md, which is independently under review.

## Metric and matter

Use units c=1. Fix Newton constant G>0, cosmological constant Lambda=3h^2>0, and C>0. On M=(0,infinity) x R^3 take

 g=-dt^2+A(t)^2 dx^2,
 A(t)=C sinh(3ht/2)^(2/3),
 U=partial_t,
 rho(t)=[3h^2/(8 pi G)] csch(3ht/2)^2,
 T_ab=rho U_a U_b.

This is pressureless dust with fixed positive Lambda, not the scalar scattering theory used in FINITE_CONTROL.md. Do not merge the two model classes.

Direct checks:

 H=A'/A=h coth(3ht/2),
 H^2=(8 pi G/3)rho+Lambda/3,
 H'=-(3h^2/2)csch(3ht/2)^2=-4 pi G rho,
 rho'+3H rho=0.

These are the flat FLRW Einstein--dust equations including Lambda. U is geodesic and rho>0, so the dust obeys the dominant energy condition. This calculation verifies one exact coupled model without relying on fitted cosmological parameter values.

## Finite past and future conformal extent

Define eta(t)=integral_0^t A(s)^(-1) ds and L=eta(infinity). As t tends to zero, A(t) is proportional to t^(2/3), so the conformal integral converges at the lower endpoint. As t tends to infinity, A(t) is proportional to exp(ht), so it converges at the upper endpoint. Thus 0<L<infinity and the entire spacetime is conformal to (0,L) x R^3. Its standard constant-t slices are Cauchy; the big-bang boundary at t=0 is not an event of M.

Apply HISTORICAL_POTENTIAL.md with a=0 and B=L. For spacelike x=(xi,z), s=(sigma,0), the least persistent enlargement of the point-level causal-potential domain obeys

 x in H(s) iff |z|<2L+sigma-xi.

Take xi=sigma=L/2 and |z|=3L. Both events are regular interior events at finite cosmic time. They are spacelike, hence x belongs to the bow-tie realm at s. But x is absent from H(s), since 3L>=2L. Thus even retaining every formerly potential event does not recover the whole bow-tie realm in this fixed Einstein--dust--Lambda model.

The opposite example |z|=3L/2 at the same eta shows H really repairs instantaneous loss: x is not in D(s), which requires |z|<L, but x is in H(s), which requires |z|<2L.

## What the example establishes

It supplies a coupled-GR realization of the difference between bow-tie existence and the least persistent causal-potential enlargement. No thin shells, arbitrary cut-and-paste metric, quantum dynamics, or numerical fit is involved. The historical rule is coherent and persistent; it simply gives a different event realm. Other enlargements, including the entire bow-tie realm itself, can be stipulated. The result challenges uniqueness of the motivating criterion, not logical consistency of those alternatives.

It does not resolve the location/fusion clause, prove the authors intended our point-level reconstruction, or establish an empirical difference between ontologies. Those philosophical premises must remain visible.
