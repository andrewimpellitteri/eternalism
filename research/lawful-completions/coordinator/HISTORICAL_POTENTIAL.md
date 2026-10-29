# Exact historical-potential repair in a finite conformal slab

2026-10-28. Coordinator derivation; not yet independently reviewed or priority audited. This tests a repair to the point-level causal-potential reconstruction, not every reading of Correia--Rosenkranz's rationale or location clause.

## Fixed definitions and spacetime

Use the open flat conformal slab M=(a,B) x R^d, d>=1, a<B finite, with metric conformal to -d eta^2+dx^2 by any smooth positive conformal factor. Causal order is the ordinary Minkowski order restricted to this slab; distinct null-related events count as strict causal pairs. Define D(s) and its least persistent enlargement H(s) exactly as in HORIZON_REVIEW.md:

 D(s)={s} union {x: not(s prec x), and x and s have a common strict causal future},
 H(s)=union_{r<=s}D(r).

Write s=(sigma,0), x=(xi,z), d=|z|. Past and equality points x<=s always belong to H(s), and strict causal future points s prec x never do. Consider only spacelike pairs d>|xi-sigma|. Then the proposed exact condition is

            x in H(s) iff d < 2(B-a)+sigma-xi.       (*)

This differs from instantaneous D(s), whose condition is d<2B-sigma-xi. The additional 2(sigma-a) reach comes from earlier standpoints and their possible spatial motion.

## Necessity

Suppose r=(rho,y)<=s witnesses x in D(r). Then rho>a, rho<=sigma, |y|<=sigma-rho. A common strict future for x and r exists precisely when

 |z-y| < (B-xi)+(B-rho)=2B-xi-rho.

Thus
 d <= |z-y|+|y| < 2B-xi-rho+sigma-rho
   =2B+sigma-xi-2rho < 2(B-a)+sigma-xi.

The separate x=r case would imply x<=s and cannot occur in the spacelike case. This proves necessity including the strict boundary.

## Sufficiency

Assume x and s are spacelike and (*) holds. Choose rho in (a,sigma] sufficiently near a that

 d < 2B+sigma-xi-2rho.

The set of reachable y has |y|<=sigma-rho. Along the ray from 0 toward z the possible distances ell=|z-y| include every value in

 [max(0,d-(sigma-rho)), d+(sigma-rho)].

Choose ell in this interval satisfying simultaneously

       |xi-rho| < ell < 2B-xi-rho.

Such a choice exists: the upper bound is positive and strictly exceeds |xi-rho| because xi,rho<B. The left endpoint of the reachable interval is strictly below the upper bound by the chosen rho inequality (or equals zero). Its right endpoint strictly exceeds |xi-rho|, since d>|xi-sigma|: if xi>=rho, d+sigma-rho > xi-rho follows from d>xi-sigma; if xi<rho, d+sigma-rho > rho-xi follows from d>sigma-xi and rho<=sigma. Therefore the open interval between the two required bounds intersects the reachable interval. The chosen r and x are spacelike, so r is not in x's causal past; their common future condition holds. Hence x in D(r) subset H(s).

The strict spacelike requirement was only to prove this branch; chronological/null past and the marked event were handled separately.

## Consequences and checks

- H is persistent by construction and excludes all strict causal future events. This repairs the growth failure of instantaneous D.
- H generally differs from the bow-tie realm: take a=0, B=1, sigma=xi=1/2 and d=3. These points are spacelike. They are in each other's bow-tie elsewhere, but d>=2 prevents historical common-future potential at every r<=s.
- A point can be retained after losing instantaneous potential: in the same slab take sigma=xi=1/2,d=3/2. Instantaneous D requires d<1 and fails. Historical H requires d<2 and succeeds. Thus the repair has mathematical content, not just renaming D.
- The difference is conformally invariant at the event-domain level, so an arbitrary positive scale factor does not alter these causal conclusions. Whether a chosen factor solves a named fixed matter model is a separate physical premise; an arbitrary conformal slab is not automatically an admissible Einstein solution.
- For a=-infinity with finite B, the necessary bound becomes unbounded and the same constructive argument gives H(s)=D_BT(s). Thus the historical repair CAN recover bow-tie in a spatially flat de Sitter patch with infinite conformal past. Do not use that patch as a counterexample to the repaired criterion.
- With finite conformal past and noncompact spatial sections, the displayed far-elsewhere counterexamples remain. A concrete cosmological matter model needs its conformal interval and exact solution justified independently; no parameter fit is needed for this geometric proposition.

## Philosophical scope

Instantaneous causal potential plus persistence fails when common-future access is lost. Retaining historical potential is a coherent repair, but does not uniquely motivate the bow-tie realm across all conformal geometries. It agrees with bow-tie in some frames and excludes elsewhere events in others. This pressures the universality and explanatory uniqueness of one motivation, not consistency of bow-tie existence itself. The location/fusion clause could enlarge the domain further; its exact composition and quantifier commitments remain a separate premise.
