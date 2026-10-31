# Historical-potential classification on complete conformal cylinders

2026-10-28. Coordinator conjecture with proof below, independent adversarial review requested. Elementary theorem for an explicitly reconstructed existence rule; no novelty claim.

## Setting

Let (S,h) be a connected complete Riemannian manifold of positive dimension. Let M=(a,B)xS with finite a<B, conformal to the ultrastatic metric -deta^2+h by a smooth positive factor. Write L=B-a and d=d_h(p,q). Completeness gives minimizing geodesics, and causal order on the cylinder is eta_y-eta_x>=d_h(x,y). Define instantaneous D and its least persistent enlargement H as in HISTORICAL_POTENTIAL.md.

**Proposed theorem.** For spacelike s=(sigma,p), x=(xi,q),

       x in H(s) iff d < 2L+sigma-xi.                  (1)

Consequently H(s)=D_BT(s) for every s iff diam(S)<=L, where the diameter may be infinite. This includes noncompact complete S; compactness is not required. The statement concerns the whole cylinder, not a quotient lacking global hyperbolicity or a physical conformal factor not solving the chosen equations.

## Common-future criterion

A common strict causal future for r=(rho,y),x=(xi,q) exists iff d_h(y,q)<2B-rho-xi. Necessity follows by adding the two causal distance inequalities. For sufficiency, a minimizing geodesic from y to q supplies a point where the two growing metric balls meet at some time below B; if one endpoint is already later than the nominal meeting time, use that endpoint and move slightly timelike into its future. Thus endpoint ordering does not invalidate the strict test.

## Necessity of (1)

If r<=s witnesses membership, d_h(p,y)<=sigma-rho. By the triangle inequality,

 d <= d_h(p,y)+d_h(y,q)
   < sigma-rho+2B-rho-xi
   < 2(B-a)+sigma-xi.

The exceptional x=r case is impossible for spacelike x,s.

## Sufficiency without unbounded spatial directions

Assume d>|xi-sigma| and d<2B-2a+sigma-xi. We seek a time rho satisfying

 a<rho<=sigma,    rho>xi-d,
 d<2B+sigma-xi-2rho.                                 (2)

The lower endpoint rho_0=max(a,xi-d) is strictly below sigma, by a<sigma and d>xi-sigma. At rho_0=a the last inequality is the assumed strict bound. At rho_0=xi-d it follows from

 2B+sigma-xi-2(xi-d)-d
   =2(B-xi)+(sigma-xi+d)>0,

using xi<B and d>xi-sigma. Hence choose rho just above rho_0, still below sigma, preserving all strict inequalities.

Then d>|xi-rho|: the xi-rho branch follows from rho>xi-d; the rho-xi branch follows from rho<=sigma and d>sigma-xi. Let R=sigma-rho. Moving y along a minimizing geodesic from p toward q by distance at most R makes ell=d_h(y,q) range over [max(0,d-R),d]. We need

        |xi-rho|<ell<2B-xi-rho.

The lower bound is strictly less than d. The upper bound is strictly greater than |xi-rho| because xi,rho<B. The left endpoint max(0,d-R) is strictly below that upper bound by (2). Thus the reachable interval intersects the required open interval. Choose such ell and y. Now r<=s; r and x are spacelike; and they share a future. Therefore x belongs to D(r) subset H(s).

This proof needs only a minimizing geodesic toward q. Unlike the original Euclidean argument, it does not require moving arbitrarily far away from q, so compact spatial sections cause no problem.

## Diameter equivalence

If diam(S)<=L, every spacelike pair has d<=L<2L+sigma-xi, since sigma> a and xi<B. Equation (1) admits every elsewhere event; past/equality are already included and future events are excluded. Thus H=D_BT everywhere.

Conversely, if diam(S)>L, choose p,q with d>L and choose sigma=a+delta, xi=B-delta for sufficiently small delta>0, with delta<L/2 and L+2delta<d. Then d>|xi-sigma|=L-2delta, so the pair is spacelike, but d>=2L+sigma-xi=L+2delta. It lies in D_BT(s) and not H(s). Hence equality fails.

## Examples and scope

- Global de Sitter: unit S^3 has diameter pi and total conformal duration pi. The criterion is saturated and H=D_BT.
- Flat dust+Lambda: complete spatial R^3 has infinite diameter while total conformal duration is finite. H differs from D_BT, as in EXACT_DUST_LAMBDA.md.
- The flat de Sitter PATCH has infinite conformal past, outside this finite-L theorem; the separate earlier construction gives H=D_BT there.

These are causal-geometric comparisons, not observational tests or an ontology selected by the Einstein equations. A compact complete spatial section of sufficiently large diameter relative to L can fail too; 'compact versus infinite' is not the actual dividing line. Physical realization of each cylinder requires its own field-equation and regularity check.
