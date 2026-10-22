# An observer can recognize an event while losing its interference

Coordinator audit, 22 October 2026. Corrects the operational interpretation of
`research/covariant-observer-witness/RESULT.md`. Known finite operator and
information-loss reasoning, not a novelty claim or a cosmological observer model.

## The two measurement targets

For a finite orthonormal history register, an event E with m>0 histories has
membership projector and normalized coherent-filter projector

    D_E = sum_(C in E) |C><C|,
    Q_E = |u_E><u_E|/m,    u_E=sum_(C in E)|C>.

For a normalized preparation |psi>=sum_C a_C|C>, the probabilities are

    <D_E> = sum_E |a_C|^2,
    <Q_E> = |sum_E a_C|^2/m.

They agree only under additional state/event-specific conditions. Membership
in an accessible event algebra does not establish access to Q_E. We use the
rank-one scalar history target; no identification with arbitrary endpoint-summed
quantum measures is made.

The source comparison matters: Mozota Frauca–Sorkin, arXiv:1610.02087v1,
Section 5.2, Eqs. (42)–(46), uses a superposition filter and retains final-system
labels. Its Eq. (43) includes a final-endpoint delta. Our rank-one register is
the project’s explicitly specified simpler preparation, not the general theorem.
Full text at this construction re-read on 22 October; not a new full-paper read.
Source: https://arxiv.org/html/1610.02087v1 .

## Exact access criterion and three distinct observer channels

For a fixed channel C, an output effect 0<=F<=I exactly implements a target
input effect T on every density matrix iff C*(F)=T. This follows from
Tr[F C(rho)]=Tr[C*(F)rho] and separation of Hermitian operators by states.
An arbitrary output-only ancilla or measurement still defines an output effect.
A fixed positive calibration eta changes the target to eta T; it cannot restore
matrix elements missing from the adjoint image.

Partition the history basis into finite isomorphism classes b and let Π_b be
their orthogonal projectors.

1. **Cardinality record only at a fixed n:** C_card(rho)=Tr(rho)|n><n|.
   The adjoint image is scalar multiples of I. A nontrivial D_E or Q_E is
   not accessible on all inputs.
2. **Classical shape record:** Γ(rho)=sum_b Tr(Π_b rho)|b><b|.
   Its adjoint image is the commutative algebra {sum_b f_b Π_b}. A diagonal
   output effect supplies one number f_b in [0,1] per class. Γ can be
   implemented by the isometry |C> -> |[C]>_observer |C>_environment followed
   by discarding the environment. It resolves a class but discards coherence.
3. **Class pinching with the quantum register retained:**
   Δ(rho)=sum_b Π_b rho Π_b. Its adjoint image is the larger noncommutative
   block-diagonal algebra direct-sum_b B(Π_b H). It retains within-class
   coherence and removes between-class coherence. It is not the same algebra
   as the span of class projectors and not dephasing *within* a class.

For an event that is a union of classes, D_E belongs to both adjoint images.
But Q_E belongs to Δ's image iff E is supported in one class: its block
Π_b Q_E Π_c = |u_(E∩b)><u_(E∩c)|/m is nonzero whenever E meets both b and c.
For Γ, even a single class containing multiple histories generally loses Q_E's
within-class off-diagonal elements. These are exact statements for all input
states. For one completely known preparation, reproducing one known number
is a much weaker task and can even be done by a constant-output channel.

## A concrete failure in the report's own three-element event

At p=(1+i)/2 and q=conjugate(p), A(C)=p^L q^h, with L the covers and h the
incomparable pairs. The event (L-h) mod8 in {0,1} at n=3 consists of exactly
two distinct finite classes, each with one natural-labelled representative:

    V=(0,0,3),        Lambda=(0,1,1),

using predecessor bit masks. Each has L=2,h=1 and A=(1+i)/4. Hence m=2,
|sum_E A|^2=1/2. For the normalized coherent complex-percolation register,

    <D_E>=1/4,       <Q_E>=1/4,
    Tr[Q_E Δ(|psi><psi|)]=1/8.

The equality of the first two numbers in this particular preparation is an
accident of its aligned equal amplitudes; the off-diagonal target is still
different. The calibrated scalar measure is m<Q_E>=1/2 before the channel.
Applying the same filter and calibration after pinching gives 1/4 instead.

A state-independent impossibility witness is stronger. Let

    |+>=(|V>+|Lambda>)/sqrt(2),
    |->=(|V>-|Lambda>)/sqrt(2).

Both vectors are invariant under every permutation inside each finite
isomorphism class (their two occupied classes are singletons). Their Δ outputs
are identical; their Γ outputs are identical as well. Yet Q_E has probabilities
1 and 0, while D_E has probability 1 on both. No output-only filter can
reproduce the Q_E target on this family, even allowing any fixed eta>0.

For a normalized Q_E target, every output effect has worst-case absolute
probability error at least 1/2 on this pair. The effect D_E/2 is reachable
and its input operator differs from Q_E by norm exactly 1/2, so this lower
bound is sharp even over all input density matrices. On this pair, any
estimator using N independent channel outputs still sees identical output
laws: average squared error is E[(Z-1/2)^2]+1/4, so worst-case MSE is at least
1/4 for every N, attained by Z=1/2. This includes collective output measurements;
it excludes access to the discarded record or pre-channel control.

## Covariance alone does not cause this loss

The symmetry group that independently permutes basis representatives inside
each finite isomorphism class fixes u_E for a union-of-classes event. Q_E and
I-Q_E commute with that group. Their binary projective instrument therefore
is covariant. The class-pinching Kraus operators also commute with this group,
yet their channel destroys the between-class interference. Thus even this
strong finite within-class permutation symmetry allows the coherent target;
the extra irreversible record channel, not symmetry alone, removes access.

This group is an explicitly chosen finite register symmetry. It is not a
construction of the full gauge structure of causal-set cosmology. For primary
covariant-channel definitions we re-read Ludescher et al., arXiv:2607.24976v1,
Section II.1 (channel covariance and invariant algebra), not the full paper:
https://arxiv.org/html/2607.24976v1 . No unpublished theorem is attributed to it.

## A second gap: finite shape is not completed-history covariance

The event above is constant under isomorphism of the finite three-element
prefix. Its lift to a cylinder event on completed histories is nevertheless
not generally covariant. Take a four-element poset consisting of V and an
isolated point. Two natural enumerations have predecessor masks

    C4=(0,0,3,0),           C4'=(0,0,0,3).

They are isomorphic by exchanging the last two birth labels. The first
three elements of C4 form V and pass the phase-ray event. The first three
of C4' are an antichain, with L=0,h=3, and fail it. Append an infinite chain
of universal tops to the four-element poset, using the same continuation for
both enumerations. This gives two natural labelings of one completed
past-finite causet with opposite event membership. It is a direct counterexample
to promoting this finite class event to a completed covariant event.

Brightwell–Dowker–García–Henson–Sorkin, arXiv:gr-qc/0210061v2, Section 2,
defines covariance on relabelings of completed causets; Section 3 defines
existential stem events. Those definitions are full-text checked here, not the
later measure-theoretic proofs. Source:
https://arxiv.org/html/gr-qc/0210061v2 . An existential stem event is different
from selecting the first three births. Its calibrated measure and realizable
instrument require a separate construction. No limit of our finite filters
or quantum stem-generation theorem has been established.

## Disposition

Keep the exact finite class sums and the fact that the phase-ray subset is a
union of finite classes. Withdraw any inference that class pinching preserves
the coherent scalar-measure witness or that the finite prefix event already
satisfies completed-history covariance. The earlier finite algebra acceptance
must be read with these corrections. Independent checks are in check.py and
output.txt; independent analytic review is requested separately.
