# Coordinator review of the parallel horizon side-test

28 October 2026. Read-only review of research/bowtie-horizons/RESULT.md,
check.py and the shared relational output. Claude's lane remains in review;
no parent side-test file or claim changed here.

## What checks analytically

For the explicitly reconstructed point-level domain D_pot, membership of
an elsewhere event is exactly existence of a common causal future. The
flat conformal-slab distance inequality and the de Sitter witness give a
correct failure of persistence under causal advance. D_BT itself remains
monotone by nesting of future cones. These observations are conditional on
the chosen interpretation of potential, rather than a refutation of BO.

The thin-shell radial ODE and advanced-time bound are consistent with
integration: from r0<2M at v1, dr/dv=(r−2M)/(2r), and integrating down to
r=0 gives v1−2r0+4M log(2M/(2M−r0)). This is not a proof of a smooth
Einstein–scalar pair, matching in maximal globally hyperbolic developments,
or a well-posed collapse replacement. Those source gates stay open.

## Two qualifications before integration

1. The unrestricted-fusion route is conditional on an existence/composition
   rule licensing the fusion before the elsewhere occupant's existence is
   established. An ambient mathematical occupant label is insufficient.
   A theorem that the location clause recovers every elsewhere point needs
   these quantifier/domain assumptions explicitly. Empty points also need
   treatment. The side-test's 'dilemma' should therefore be retained as
   conditional branches, not a proof exhausting all possible readings.
2. Loss of currently available causal potential does not force loss of
   existence if existence records past potential. A least monotone closure
   can be defined (below). It changes the criterion and need not recover BO;
   its existence shows why the point-level failure alone does not establish
   that no potential-based growth interpretation is possible.

## Candidate strengthening of the open monotonicity question

Let M be a connected, time-oriented, causally simple smooth spacetime
without boundary (global hyperbolicity suffices). Write p≺q for causal
precedence excluding equality, including null pairs. Use exactly the
side-test definition

  D(s)={s} ∪ {x : not(s≺x) and exists z (s≺z and x≺z)}.

**Candidate lemma:** D is monotone along all causal advances if and only
if M is future-directed (every pair has a common strict causal future).
This is an elementary lemma independently checked in
relational/HORIZON_LEMMA_REVIEW.md. No novelty claim or full source-priority
audit is made.

Proof candidate. Future-directedness gives D(s)=D_BT(s), hence monotonicity.
Conversely fix x with no common future with some s, and set

  P_x=I^-(I^+(x)).

Having a common strict causal future is equivalent to having a common
chronological future: extend a common causal successor slightly timelike
and use causal/timelike push-up. Hence P_x is exactly the set of standpoints
sharing a future with x. It is a nonempty proper open past set. Connectedness
supplies p∈∂P_x. Since P_x is open, p∉P_x. Also J^-(x)⊂P_x: extend x to a
chronological successor. Thus p∉J^-(x), and causal simplicity makes J^-(x)
closed, so a neighborhood of p is disjoint from J^-(x).

Choose r≪p in that neighborhood. For any such r, r∈P_x: the open set
I^+(r) contains p and therefore meets P_x; transitivity and past-set closure
put r in P_x. Since r∉J^-(x), not(r≺x). Therefore x∈D(r). But p∉P_x and
p≠x imply x∉D(p). With r≪p this contradicts monotonicity. QED if all
stated causal-topology hypotheses and identifications hold.

This would resolve side-test open question 1 within causally simple
connected spacetimes, including globally hyperbolic examples. It does not
classify causally pathological frames or establish priority.

## A distinct repair by retaining historical potential

For any causal frame with the stated domains, define

  H(s)= union over r≤s of D(r).

Then H is the least causally monotone enlargement of D: r≤s implies the
union index set nests, and any monotone enlargement containing each D(r)
must contain the displayed union. Also H(s)⊂D_BT(s). Indeed x∈D(r) excludes
r≺x, except the separate case x=r. If s≺x and r≤s, transitivity would give
r≺x; in the exceptional x=r case r≤s≺r violates causality. Thus no x in
H(s) is strictly causally future of s.

This provides a mathematically consistent, historical-potential event
assignment retaining the no-future condition and growth. It does not
establish a preferred ontology, uniform elsewhere existence, or a causal
explanation. It may depend on full histories and global futures through D.
Determining when H=D_BT is a separate question. Its use here is to keep
criticism of the instantaneous-potential reading accurately bounded.

## Verified checks and remaining source burden

Ran the side-test's standard-library check.py without editing it. It
reproduces the quoted conformal distances and thin-shell ODE comparison.
This repeats the implementation, not an independent cosmological fit or
analytic validation of the numerical thresholds. The de Sitter and radial
inequality arguments above carry the bounded analytic review.

Christodoulou1991 citation verified against publisher metadata:
*The formation of black holes and singularities in spherically symmetric
gravitational collapse*, CPAM44(3),339–373,
DOI10.1002/cpa.3160440305. Main text unread. A trapped-surface/black-hole
formation theorem alone does not immediately supply the side-test's full
causal separation property. The replacement must establish a matched
entire flat past and marked observer, a well-defined globally hyperbolic
model class, and the existence of a particular late exterior event with
no common future with the observer. Incompleteness of some null geodesics
alone does not entail that last global assertion. No additional paper
request has been made of the user during this review.

## Review status

Independent native review of the monotonicity equivalence and least
monotone closure is in relational/HORIZON_LEMMA_REVIEW.md. It confirms the
proof with connectedness, causal simplicity, time orientation and local
future/past availability explicit. This does not accept Claude’s entire
side-test, its fusion argument, or the thin-shell global completion claim.
