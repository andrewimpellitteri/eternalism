# Known-answer negative controls for the creativity-loop pilot

Purpose: test whether candidate generation and audit distinguish a claim from
nearby stronger claims. Each control has a seeded failure and a clean
counterpart. A system that flags everything fails the clean counterpart; a
system that accepts everything fails the negative control. These are
mathematical/model checks, not votes or novelty judgments. No result licenses
an inference to temporal ontology.

## NC1 — L1 density does not imply L2 density

**Access/model assumptions.** Base space is `(0,1)` with Lebesgue measure
`dx`. A complex-measure extension is represented by `nu(E)=integral_E g dx`;
the pilot must not silently assume `g` is bounded or square-integrable.

**Negative control (known failure).** Choose `alpha=3/4` and
`g(x)=(1-alpha)x^(-alpha)=1/4 x^(-3/4)`. Then `g>=0` and

    integral_0^1 g dx = 1,
    integral_0^1 |g| dx = 1,
    integral_0^1 |g|^2 dx = (1/16) integral_0^1 x^(-3/2) dx = infinity.

Thus `g` is a normalized L1 density but not in L2. More generally,
`(1-alpha)x^(-alpha)` is normalized and in L1 for `0<alpha<1`, while it is
not in L2 for `1/2<=alpha<1`. An auditor must reject “L1 convergence/density,
therefore L2” absent a separate bound or argument. This says nothing by
itself about whether the associated complex measure is finite; it is finite
here because `g` is L1.

**Clean counterpart.** On the same space, `g0(x)=1` is normalized and belongs
to both L1 and L2. The valid claim “this particular density is L2” should pass
when the constant function is specified. The invalid general implication
should still fail. This catches blanket rejection of all L2 claims as well as
unjustified promotion from L1.

**Expected verdict.** Negative: `L1` alone does not entail `L2`; control:
`g0` is L2 by direct integration. Neither case needs a detector
interpretation.

## NC2 — Atomless labelled histories need not have atomless quotient measure

**Access/model assumptions.** A measurable quotient is a measurable map
`q:X->Y`; its pushforward is `q_*mu(B)=mu(q^(-1)(B))`. “Atomless on X” and
“atomless on Y” refer to the respective measurable spaces and measures. The
countermodel below is deliberately a general quotient model, not a claim
about the equivalence classes of any specific causal-set sample space.

**Negative control (known failure).** Let `X=[0,1]` with its Borel sigma
algebra and Lebesgue probability `mu`, let `Y={*}` with its full sigma
algebra, and let `q(x)=*` for every x. The labelled-space measure `mu` is
atomless, but `q_*mu({*})=1`; the quotient measure is a point mass. Therefore
atomlessness on a labelled space does not, without conditions on the quotient
map, imply atomlessness after identifying histories.

**Clean counterpart.** With the same atomless `(X,mu)`, use the identity
quotient `q(x)=x`; then `q_*mu=mu` remains atomless. More generally, if `q`
is measurable and every fiber `q^(-1)({y})` is countable, then each quotient
singleton has pushforward mass zero: it is a countable union of `mu`-null
singletons. This proves absence of quotient point atoms under those
assumptions, but absence of point atoms implies full atomlessness only with
additional structure (for example a standard Borel space and finite Borel
measure). An auditor should ask whether the actual equivalence classes are
measurable/countable and what sigma algebra is placed on the quotient; it
must neither transfer atomlessness automatically nor reject the countable
fiber result.

**Expected verdict.** Negative: the general implication is false. Control:
identity (or countable-fiber) quotient preserves zero singleton masses; state
the space and sigma-algebra assumptions before claiming atomlessness.

## NC3 — A rank-one quantum measure is not automatically a detector
probability

**Access/model assumptions.** On a finite outcome set, take a normalized
complex amplitude measure `nu` and its rank-one quantum measure
`mu(E)=|nu(E)|^2`. A detector probability requires a specified readout rule
(instrument/POVM or equivalent), normalized outcome probabilities, and any
decoherence conditions needed for additivity. Normalizing `nu(X)=1` does not
make `mu` additive.

**Negative control (known failure).** Let `X={0,1}` and
`nu({0})=nu({1})=1/2`. Then `nu(X)=1`, but

    mu({0})=1/4,  mu({1})=1/4,  mu(X)=1.

The disjoint singleton values sum to `1/2`, not `mu(X)=1`. Thus this
normalized rank-one quantum measure is not a probability measure on the
outcome sigma algebra. Calling its event values detector probabilities
without an instrument and a probability rule is an unsupported bridge.

**Clean counterpart.** In the same finite outcome space, specify a two-result
quantum measurement on a qubit in state `|+>=(|0>+|1>)/sqrt(2)` with projectors
`P_i=|i><i|`. The Born probabilities are
`p_i=<+|P_i|+>=1/2` and sum to one. The outcome branches are orthogonal, so
the associated decoherent alternatives have diagonal weights `1/2,1/2`.
This is a detector-probability claim supported by an explicit measurement
model; it is not the scalar rank-one event rule `|nu(E)|^2` above. An auditor
should accept this explicitly specified measurement result while refusing to
identify it with the negative-control quantum measure absent an additional
map and conditions.

**Expected verdict.** Negative: normalization of a scalar amplitude does not
imply additivity or operational probability. Control: the finite Born-rule
measurement gives normalized probabilities under the stated instrument.
Neither formal model alone establishes that a real instrument implements it.

## NC4 — A finite-prefix minimum count is not an invariant of the completed
causet

**Access/model assumptions.** Histories are natural enumerations of a single
countably infinite poset: each element appears after all its predecessors.
`M_n` denotes the number of minimal elements in the induced order on the first
n enumerated elements. A completed-causet property must be invariant under
changing the natural enumeration, whereas `M_n` is a finite-prefix statistic.

**Negative control (known failure).** Let the completed poset have elements
`a,b,c,x_1,x_2,...`, with `a,b,c` minimal and
`a<x_1<x_2<...`; there are no other comparabilities. Consider these two
natural enumerations:

    I:  a, b, x_1, c, x_2, x_3, ...
    II: a, b, c, x_1, x_2, x_3, ...

Both respect every predecessor relation and enumerate the same completed
causet. Yet `M_3=2` in I and `M_3=3` in II. The completed causet has exactly
three minimal elements in either presentation. Therefore “the first three
births have two minima” is not an invariant property of the completed
causet. This control concerns a finite-prefix claim, not the intrinsic event
“the completed causet has exactly two minimal elements.”

**Clean counterpart.** For this same completed causet, the property
“the completed order has exactly three minimal elements” is invariant under
both enumerations: its minimal elements are `{a,b,c}`. Likewise, the event
“the completed order has exactly two minimal elements” is false in both.
An auditor should reject the prefix-to-completion inference while retaining
the correctly defined completed-order statement.

**Expected verdict.** Negative: `M_3=2` depends on the natural enumeration.
Control: the completed minimum set and its cardinality are invariant under
these reorderings. No measure or typicality claim is needed for this
deterministic example.

## Scoring notes

Score each negative and its counterpart separately. A success requires the
right claim-level verdict and a reason tied to the stated assumptions; a
generic warning, unsupported rejection, or agent consensus does not count.
Record mathematical validity separately from empirical interpretation and
philosophical significance. These controls test transfer and calibration,
not creativity, source discovery, novelty, or the correctness of a physical
bridge premise.
