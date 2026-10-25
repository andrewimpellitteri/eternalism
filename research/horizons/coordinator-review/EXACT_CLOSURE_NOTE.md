# Three diamonds: an immediate exactness corollary

2026-10-25. Read-only follow-up to the current manuscript's three-diamond
theorem, introduced in b62a51b. Current checkout HEAD at reading: bd77ba2.
This does not integrate GLM's rejected four-inequality formula or certify
novelty. All three GLM runs are now submitted to review, not accepted.

## The displayed sandwich already gives equality

The theorem states, for 0<τ<π and M=(0,2π)×S³,

    M ∩ U_b ⊆ F_L(b) ⊆ M ∩ closure(U_b),

where U_b is the union of the three open double cones centered at
(0,Y), (π,−Y), and (2π,Y), of radius τ in the product metric's optical
coordinates. In the smooth solution class, F_L(b) is relatively closed in M:

    F_L(b) = intersection over all solutions h vanishing on I_s^-(b)
             of {x in M : h(x)=0}.

Each zero set is closed by continuity. Therefore the left inclusion implies

    closure_M(M ∩ U_b) ⊆ F_L(b).

Since M is open in the Einstein cylinder,
closure_M(M ∩ U_b)=M ∩ closure(U_b). Combining with the right inclusion gives

    F_L(b) = M ∩ closure(U_b).

Writing d=d_S³(X,Y), the exact set is

    {d+η ≤ τ}
    union {π−d+|η−π| ≤ τ}
    union {d+2π−η ≤ τ},

intersected with 0<η<2π. Closure commutes with this finite union. This
formula is conditional on the manuscript's proved sandwich and the stated
continuous unrestricted solution class; no new PDE theorem is needed to
remove its boundary ambiguity. It is not the GLM formula involving whole
half-spaces in η±d, which fails the counterexample in GLM_FIRST_REVIEW.md.

## Consequences worth stating precisely

On the observer's comoving line X=Y, the middle diamond is empty because
π+|η−π|≥π>τ. Thus the exact fixed times are

    0<η≤τ  or  2π−τ≤η<2π.

The onset boundary η=2π−τ is fixed too, by continuity. The intervening open
interval is unfixed for this law. For example the same future event
x=(3π/2,Y) is unfixed from b_1=(2π/5,Y), but fixed from
b_2=(3π/4,Y). Both standpoints occur before maximum expansion. This supplies
a genuine law-relative epoch witness once the sandwich proof is accepted,
rather than inferring one from the geometric sufficient region.

At τ=π, outside the theorem's stated range, the same Cauchy-data argument
supplies a separate direct result: vanishing on I_s^-(b) forces both smooth
extended data at η=0 to vanish on B(Y,π), the entire S³ except its antipode.
Continuity fills that point, so uniqueness gives F_L(b)=M. Geometric Det(b)
remains I_s^-(b) at this exact threshold. Do not obtain this endpoint merely
by substituting into a theorem stated only for τ<π.

## Review limits

A direct pass through the current sandwich proof found no blocker in its
main mechanism: the spherical-mean propagator supplies supported separating
solutions outside the closed union, and finite propagation plus recurrence
gives the lower bound. The expression S(X,η) should be read via its folded
radius for η>π, or reduced by A as done in necessity; spheres have positive
geodesic radius at most π. Exact source correspondence, global primary-work
coverage and final philosophical wording still require their own checks.

This note strengthens the precision of the current result; it does not
establish that the result is new, physically realistic, or independently
supports any temporal ontology.
