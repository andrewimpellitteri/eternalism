# Draft 3: focused follow-up

2026-10-25. Uncommitted working source observed during the authorized book
exploration; main.tex SHA-256:
`bbd592692f26484d6a13591d07989709ed32205ae250d36ebb88e15c4bc84bbe`.
This follows REVIEW.md; it does not silently replace that frozen draft-2 audit.
The author is concurrently editing. No manuscript or PDF was changed here.

## What the revision resolves

The new solution-class definition F_L(b), the inclusion
Det(b) ∪ J^-(b) ⊆ F_L(b) for continuous fields, and the explicit flow-law
counterexample repair the central draft-2 conflation in the definitions.
The ball-proof parenthesis and rooted .2 formulation are also corrected.
The current source compiled successfully through the desktop compiler.

The new conformally coupled scalar sharpness argument on a spatially flat
FLRW slab passes a direct analytical check: choosing a plane-wave profile
f(η−η_b−k·(Z−Y)) supported on positive argument gives a smooth solution zero
on I_s^-(b) and nonzero at any specified x outside J^-(b), including when X=Y
(then any unit k works). Multiplication by the positive conformal factor
preserves agreement and disagreement. This is a solution-class necessity
argument, which was missing before. Its source/priority audit remains separate.

The echo mode identity is also algebraically consistent: on unit S³,
eigenvalues −n(n+2) give frequency n+1, whose π-time shift contributes
(−1)^(n+1); antipodal parity contributes (−1)^n; their product is −1.
Smooth global extension on the Einstein cylinder is justified by the ordinary
linear Cauchy problem from any interior slice. This verifies the claimed
inclusion, not exactness of F_L, not novelty, and not all cited source details.

## New limitation: the pre-threshold echo contains no timelike future of b

**Locations:** abstract's interpretation of the echo and the first numbered
philosophical conclusion, approximately lines 39–47 and 329–336 of this snapshot.
The proposition itself says nonempty and disjoint from Det; that survives.

Let b=(τ,Y), with 0<τ<π, and y=(s,X)∈J^-(b) inside the dust interval.
Write d=d_S³(X,Y). Causality gives

    s + d ≤ τ.

The echo is z=A(y)=(s+π,−X). Its positive time separation from b is

    Δ = s + π − τ > 0,

and on the unit sphere

    d_S³(−X,Y) = π − d ≥ s + π − τ = Δ.

Consequently z is **not** in I^+(b). If y is in the strict chronological past,
the inequality is strict and z is spacelike to b; boundary input points can
give future-null echoes. For the paper's own witness y=(τ/2,Y), the echo has
Δ=π−τ/2<π and spatial distance π, so is spacelike.

Therefore this echo proves field determination outside the fragment/causal past,
but does not by itself exhibit determined **timelike-future** events before
maximum expansion. It does occur at a later FLRW conformal time, which is a
different assertion. A wording such as “this happens more widely: the conformal
scalar ... before maximum expansion” following a claim about future events
needs this distinction. Keep “outside the causal past,” or supply a separate
proof of timelike-future determination. No such stronger implication follows
just from this inclusion.

This also makes the term “future” important throughout the paper: use the causal
future, future timelike cone, later cosmological slices, or events outside the
fragment explicitly as appropriate; they are not interchangeable.

## Residual quantifier overclaim

The introduction still asks “Which events does every deterministic local law
fix?” and the conclusion says “What every local deterministic law fixes is
decided by a slicing condition” (approximately lines 77 and 407).

Let G(b)=intersection over admissible L of F_L(b). What is proved generally is

    Det(b) ∪ J^-(b) ⊆ G(b).

There is no general reverse inclusion here. In particular, Det(b)=I_s^-(b)
in Minkowski space while every continuous law fixes J^-(b), so an exact
identification with Det is already false on the null boundary. The flat scalar
example establishes G(b)=J^-(b) in its particular flat-slab setting if the class
includes that scalar system; it does not prove a general universal-law
characterization on arbitrary globally hyperbolic spacetimes. The closed-model
sharpness question is explicitly left open later in the manuscript.

**Minimal replacement:** “Which events does the causal domain-of-dependence
criterion guarantee to be fixed?” and “A slicing condition characterizes a
geometric sufficient region of determination.” Retain the separate flat-model
sharpness result as an actual stronger statement for those models.

## Remaining philosophical wording

The third numbered conclusion still goes from a change in the geometric
guarantee to an epoch change in the answer to “is the future open from here?”
(approximately lines 347–352). Supply a specific system with fixed and unfixed
future targets in the same spacetime to establish the latter, or narrow this
sentence to the geometric guarantee. The new echo inclusion does not establish
that stronger claim; it neither proves exactness nor concerns timelike-future
echoes before the threshold.

F_L is a mathematical solution-agreement definition usable even when a solution
class is not deterministic; the statement that it is “silent” about all
indeterministic laws should mean those laws are outside this paper's treatment,
not that the definition cannot be evaluated for them. Clarifying the intended
modality avoids another slide toward Belnap-style settledness.

## Disposition

Substantial repair, with the original core distinction now explicit. **Not yet
an unqualified circulation clearance.** Narrow the two residual summary
inferences and distinguish spacelike echo determination from future prediction.
Then freeze the revised source for a final consistency pass. Exact primary
locators for the new conformal-field material and its prior work remain an
independent gate; algebraic plausibility and compilation do not close it.
