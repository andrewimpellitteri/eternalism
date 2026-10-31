# Independent red-team review: complete spatial sections

**Verdict: the proposed classification is correct under the stated cylinder assumptions.** I tried to break the minimizing-geodesic construction at cut loci, in noncompact spaces with unbounded diameter, and at the equality case `diam(S)=L`; none yields a counterexample. The result is a causal-geometric theorem for the whole open product slab, conditional on the stated definitions of `D`, `H`, and `D_BT`. It does not establish a preferred philosophical interpretation.

Let `d=d_h(p,q)`, `s=(sigma,p)`, and `x=(xi,q)` be spacelike. The strict criterion

```text
x in H(s) iff d < 2L + sigma - xi
```

passes in both directions. For necessity, if `r=(rho,y)<=s` witnesses membership, then `d_h(p,y)<=sigma-rho`; a common strict future for `r,x` requires `d_h(y,q)<2B-rho-xi`. The triangle inequality and `rho>a` give `d<2L+sigma-xi`. The exceptional identity `r=x` cannot occur for a spacelike `s,x` pair.

For sufficiency, the choice `rho_0=max(a,xi-d)` is strictly below `sigma`: `a<sigma`, and spacelikeness gives `xi-d<sigma`. At `rho_0=a`, the desired upper inequality is exactly the assumed strict criterion. At `rho_0=xi-d`, its margin is `2(B-xi)+(sigma-xi+d)>0`. Thus a finite `rho` just above `rho_0` can be chosen with `a<rho<=sigma`, `rho>xi-d`, and `d<2B+sigma-xi-2rho`. These inequalities imply `d>|xi-rho|` and, writing `R=sigma-rho`, `max(0,d-R)<2B-xi-rho`. The attainable distances from `q` along the chosen minimizing segment, as `y` moves from `p` toward `q` by lengths in `[0,R]`, fill `[max(0,d-R),d]`. Its right endpoint is above `|xi-rho|`, and its left endpoint is below `2B-xi-rho`; the target interval is nonempty because `xi,rho<B`. Hence a reachable `ell=d_h(y,q)` satisfies

```text
|xi-rho| < ell < 2B-xi-rho.
```

The first strict inequality makes `r,x` spacelike, so `r` does not strictly precede `x`; the second gives a common strict future below `B`. Therefore `x in D(r) subset H(s)`.

The common-future test used here is valid for all endpoint orderings, not only spacelike pairs. The infimum time of a common future is
`max(rho,xi,(rho+xi+ell)/2)`. Since both endpoints are below `B`, a common strict future exists inside the open slab exactly when `ell<2B-rho-xi`. If `r,x` are timelike or null related, the later endpoint controls this maximum and the inequality is automatic. At equality the limiting meeting time is `B`, which is excluded. This confirms the strict boundary convention used in the proof.

Completeness handles cut loci: Hopf–Rinow supplies a globally minimizing geodesic from `p` to `q`, and every subsegment of that selected minimizing geodesic is itself minimizing. No uniqueness of the geodesic is needed. Moving along it toward `q` realizes every distance in the stated interval, even when `q` is in the cut locus of `p`. No unbounded direction opposite `q` is needed, so compact spatial sections cause no difficulty.

The diameter corollary also survives endpoint checks. If `diam(S)<=L`, then every pair distance is at most `L`, while `2L+sigma-xi>L` for interior times; even when the diameter equals `L` and is attained, the slab criterion is strict with positive margin. If `diam(S)>L`, the definition of supremum supplies a pair with finite distance `d>L`, whether or not the diameter is attained. Choosing `sigma=a+delta`, `xi=B-delta` with `0<delta<L/2` and `L+2delta<d` gives a spacelike pair excluded from `H` but included in `D_BT`. This also covers infinite diameter: only one finite-distance pair above `L` is needed. Thus `H(s)=D_BT(s)` for every `s` exactly when `diam(S)<=L`.

No counterexample or additional regularity assumption surfaced beyond connectedness, positive dimension, Riemannian completeness, a finite open conformal-time interval, and the causal/strictness definitions in the coordinator note. The argument is not a source-priority audit, does not address the location/fusion clause, and makes no observational or ontology-selection claim.
