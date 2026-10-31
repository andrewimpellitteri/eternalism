# Orbit-uniform growth intertwining fails at the first tested step

24 October 2026. This is a finite obstruction for a specified quotient map. It is
not a claim about full cosmological gauge symmetry, an ontology, or a general
no-go theorem.

## Contract and multiplicities

Let `X_n` be the finite set of naturally labelled n-birth histories in the
project's register. Let `O_n` be its partition into finite-poset isomorphism
classes. Write `m_n(o)=|o|`, counting distinct natural-label histories, not
isomorphism types of precursor ideals. The isometric orbit-uniform embedding is

    J_n |o> = m_n(o)^(-1/2) sum_{C in o} |C>.

The label registers at adjacent depths have distinct bases. For the phase-bearing
and positive success maps, respectively, the nonzero append entries are

    k_n(CP,C) = sqrt(|t(C,P)|/B_n) phase(t(C,P)),
    k+_n(CP,C) = sqrt(|t(C,P)|/B_n),
    B_n = 1 + zeta_n.

A child `D` has a unique last-birth parent `pi(D)`, so for either map `T_n`

    (T_n J_n |o>)(D) = 1_{pi(D) in o} k_n(D,pi(D)) / sqrt(m_n(o)).

Thus an all-input quotient map `L_n` satisfying `T_n J_n=J_(n+1)L_n` exists
**iff** this coefficient is constant over every child isomorphism class, for
every source orbit `o`. Necessity follows because `J_(n+1)` has equal coordinates
on each child orbit. For sufficiency, set

    (L_n)_(q,o) = sqrt(m_(n+1)(q)) (T_n J_n |o>)(D),   D in q.

The criterion implies this is independent of `D`; the resulting identity holds
on each quotient basis vector and hence all inputs. Since `T_n` and `J_n` are
contractions/isometries, this induced `L_n` is a contraction. The same criterion
applies separately to `K_n` and `K+_n`; phase cancellation cannot be presumed.

This criterion allows multiple parent isomorphism classes inside one child
class. It does not replace them by one parent or divide by the number of
precursor *types*. Orbit sizes and the actual unique parent of each labelled
child determine the coefficients.

## Corrected actual-model certificates

The submitted code certified a valid support mismatch but mislabeled its
posets as chains. They are **one two-element chain plus isolated vertices**;
the prefix `(0,0,1)` is one edge plus an isolate, not a three-chain. The
coordinator corrected the prose/output labels and independently checked the
relation counts. The abstract intertwiner criterion survives this correction.

For the original late step, use source orbit the three-element antichain
(multiplicity one) and

    D1=(0,0,0,1),    pi(D1)=(0,0,0),
    D2=(0,0,1,0),    pi(D2)=(0,0,1).

Both children have one relation and two isolated vertices, with six distinct
natural-label representatives. The source-antichain column has a nonzero
coordinate at D1 and exactly zero at D2. At D1 the actual transition is
q(anti3)w(single)=L^-3, so for both models and both maps that nonzero
coefficient is real positive, enclosed by

    [0.000030542349977589,0.000030542349977590],

with B3=1+zeta3. This is not evidence that 3-to-4 is the earliest possible
obstruction; the original checker only tested that late step.

An earlier certificate exists if the same Kraus encoding is explicitly
extended to the seed step with B2=2:

    d1=(0,0,1),     pi(d1)=(0,0) [anti2],
    d2=(0,1,0),     pi(d2)=(0,1) [chain2].

These children are the three-representative class consisting of one edge and
one isolated vertex. The source anti2 orbit has one representative. Its
column again has nonzero/zero coordinates on one child orbit. The actual
nonzero transition is u/4, u=(3+4i)/5; the positive coefficient is 1/sqrt(8),
the phase coefficient is u/sqrt(8), and its squared norm is exactly 1/8.
B2=2 is valid for both models: anti2 row variation is
(15+sqrt(265))/20<2; chain2 row variation is (5+sqrt(65))/10<2.
The original sequential protocol starts at depth three, so this is a named
early-step extension, not a silent change to its normalization schedule.

There is no earlier orbit-uniformity obstruction in this unique-parent setting:
all child orbits through depth two are singleton. The explicit early extension
therefore fails first at 2-to-3. The late construction still fails at its
3-to-4 step. Phase changes cannot repair this support mismatch; changing the
embedding, mixing parent information or altering which histories are identified
would be a different proposal requiring a new criterion.

The checker independently canonicalizes edge relations under vertex
permutations and counts the comparable pairs; it imports the actual transition
evaluator and arithmetic helpers with both SHA256 pins. It checks both models,
phase-bearing and positive maps, and the early majorant. Exact zero follows
from source-orbit membership and unique-parent deletion, not a numerical zero
test. See `output.json`. No all-depth or physical gauge result follows.

## Which symmetry survives

1. **Permutations within each finite isomorphism class.** These act on a
   fixed-depth register and fix orbit-uniform vectors. The transition maps do
   not commute with the full independent permutation group across adjacent
   levels: the witness above receives one representative of a child orbit from a
   source orbit and another representative from a different source orbit.
   Covariance of a finite readout instrument under such a register group does
   not make the growth map an intertwiner.
2. **Prefix-compatible isomorphisms.** An isomorphism that maps the retained parent prefix onto the retained
   parent prefix can compare transitions while carrying each actual ideal
   with it; such arrows retain more structure than an unmarked child orbit. It cannot identify `D1` and `D2`
   while holding the same source orbit fixed: their prefixes have different
   order types. Restricting to histories with a fixed parent type avoids this
   particular mismatch only by retaining parent information, so it is not the
   orbit quotient `J_n` above.
3. **Special preparation.** The matched positive state `phi_n`, and the
   phase-bearing target states in the sequential-dilation result, do evolve to
   their specified next-depth states under the actual transition map. Those
   state-specific identities do not imply `T_n J_n=J_(n+1)L_n` on every input.
4. **Completed physical covariance.** No action of completed-history
   relabelings on a physical Hilbert space, invariant measure, or local
   observer controls is constructed here. Nothing in this finite obstruction
   establishes or refutes such a physical gauge claim.

## Prior work and scope

Rideout and Sorkin's *A Classical Sequential Growth Dynamics for Causal Sets*,
Phys. Rev. D 61, 024002 (2000), arXiv:gr-qc/9904062v3, is a primary source for
natural labellings and discrete general covariance as label independence of
completed growth probabilities; full-text source-page inspection, especially
the opening definitions and covariance discussion (read depth: full-text,
selected passages). Surya and Zalel, *A Criterion for Covariance in Complex
Sequential Growth Models*, arXiv:2003.11311v1 (2020), Sections 2.3 and 3.1,
are recorded in the project source register at full-text depth for extension and
covariance criteria. Their result concerns extension/covariant observables,
not this Kraus-operator intertwining test. The application here is a finite
matrix criterion and an actual counterexample for the project's square-root
modulus/phase-bearing observer maps; it does not claim that probability-level
discrete covariance implies, or requires, this stronger amplitude-level
quotient identity.

The finite certificate is limited to the stated depth-three/four transition.
The checker imports a content-pinned model evaluator rather than independently
reimplementing the growth law. It does not prove an all-depth result, reproduce
the inherited analytic row bound, or test a physical observer. An alternative
embedding, a coarser quotient retaining parent-type multiplicities, or a
history-dependent phase convention could have a different criterion and must
be analyzed separately. No novelty or temporal-ontology inference follows.
