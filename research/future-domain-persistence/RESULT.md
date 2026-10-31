# Persistence at a point: what the causal-past model gives up

28 October 2026. Bounded analysis of C&R's persistence and recapture
objections. This compares explicit criteria; it does not choose an ontology.
Original chapter 9 main text was supplied by the user. Appendix 3 remains
unread. This construction uses Minkowski spacetime, not the dust PDE model.

## The objection and its strongest available clarification

**Authors' claims.** Chapter 9 pp.151–152 argues that a pointy existence
domain fails to accommodate limbs that continue to exist while located.
The argument already acknowledges finite light travel time and allows
mereological fusions, so neither observation alone answers it. The authors
prefer bow-tie domains partly because they contain locations outside the
strict causal past of the observer.

In *Replies to Critics* §8 pp.486–488, Dorato and Hoefer's proposed answer
is reported as locating limbs at observed points on the past light cone.
C&R reject that answer using two candidate persistence criteria: location
in the causal past plus location at the standpoint itself, or location in
the causal past plus location neither causally earlier nor later than the
standpoint. They prefer the second. Cone-surface points count as strictly
causally past in their convention. They distinguish continued existence
from continued location, citing Socrates as the reason existence alone
cannot define persistence. These are claims in the reply, rather than an
independent reading of Dorato–Hoefer or Lewis.

**Our formalization.** Let b be a standpoint, E_b=J⁻(b), and let W denote
a material worldline or worldtube in a mathematical representation. Write
W_b=W∩E_b for its realized event locations from b. Throughout, strict
causal past means J⁻(b)\{b}: it includes null-related points, and is
different from the chronological (timelike) past I⁻(b). This is a statement about
event locations only. Treating W_b as a persisting object requires additional
identity, composition and location clauses, none supplied by intersection.
The ambient W is a mathematical label; its entire extension is not asserted
to exist at b. The source's loc predicate and free logic are not reconstructed.

Define the source-inspired criterion P_CR for these event-location sets:

    W_b contains a strict causal-past location of b, and
    W_b contains a location outside both strict causal past and strict future of b.

This records the content of the second criterion above only for our
stipulated event-location interpretation. It is not a formula proved
equivalent in the book's full quantified language.

## A direct obstruction under that criterion

In a causal spacetime,

    J⁻(b) ∩ [M \ ((J⁻(b)\{b}) ∪ (J⁺(b)\{b}))] = {b}.

Thus P_CR for a pointy domain requires b∈W_b. A limb whose locations avoid
the observer's single standpoint cannot satisfy it. This is an exact
incompatibility of the criterion and the specified event domain. It is
neither an observational contradiction nor a refutation of the criterion.
The substantive question is whether persistence of a distant part should
require this kind of endpoint rather than merely a temporally extended
portion of its own history.

The criterion is stronger than 'some located history exists': E_b contains
many timelike curves. A claim that the pointy domain contains no extended
objects or no duration would be false in this model. C&R explicitly avoid
the simplest extension objection before presenting the persistence one.

## An analytic comparison using a stationary material element

Use 3+1 Minkowski spacetime, speed of light 1, b=(0,0), and the timelike
line γ(t)=(t,r e₁), with r>0. Causal comparison gives

    γ(t)∈E_b iff t≤−r.

So its realized segment is γ((−∞,−r]); the latest emission seen at b is
p=γ(−r). Earlier p₀=γ(−r−δ), δ>0, satisfies p₀≪p and both belong to E_b.
There is a nonzero proper-time interval of material history entirely in
the domain. But every γ(−r+ε), ε>0, lies outside E_b. Thus persistence
*along the element's history up through the observed emission* is present,
while persistence beyond that emission is absent from the domain at b.
P_CR fails because b is not on γ and γ has no spacelike location to b
inside E_b. A retarded segment is not a witness of P_CR.

For a later observer standpoint b_h=(h,0), h>0, the realized segment is
γ((−∞,h−r]). Hence pointy domains add new material locations as the observer
advances, and E_b⊂E_bh. This construction has growth and timelike material
continuation without an observer-independent simultaneous endpoint.
These claims follow from the inequalities, not from a proposed definition
that the element is alive or conscious.

The case is about one material line. A finite tube can be modeled by
positions x in a ball B(r e₁,ρ), 0<ρ<r, at all coordinate times. Its realized
portion obeys t≤−|x|. Every constituent line has a retarded endpoint, with
endpoints varying across the tube. The tube still avoids b, so the same
P_CR obstruction applies. This supplies extended support; it does not
establish anatomical structure, object identity, an embodied observer or
a theory of perception. In particular, it retains the source's simplifying
point-standpoint idealization.

## The obstacle cannot be removed merely by choosing a later real location

At a nonvertex point p on the past light cone of b, no q with p≪q can also
satisfy q≤b. In Minkowski coordinates, write the positive time lapse for
p≪q as larger than its spatial distance and the lapse for q≤b as at least
its distance. Adding and using the spatial triangle inequality gives
p≪b, contradicting null separation. Therefore no timelike material
continuation after the direct observed emission can remain in E_b.

This is stronger than a coordinate-simultaneity observation, but weaker
than an argument against the ontology. It proves that a proposed reply
must change the persistence criterion, the existence domain, or the
pointlike standpoint model. Repeating that the observed limb locations
already exist does not answer C&R's criterion. Conversely, demanding that
actual present observations reveal post-emission persistence needs a
further epistemic premise; light reception alone does not do so.

An explicitly weaker criterion could ask for a timelike interval in W_b
ending at its latest retarded location. The example satisfies it. That is
a candidate revision of persistence language, not satisfaction of P_CR.
It is also not by itself a life/death criterion: old remains or an ended
worldline can contain timelike intervals. Distinguishing a living current
limb from a historical one requires additional structure and justification.

## The two meanings of an edge

For E_b in this Minkowski example, b is its unique maximal event under
causal order: every other p∈E_b has p<b. This remains true for null-related
p; its null relation to b does not make it maximal under the full order.

The manifold-topological boundary, however, is

    ∂E_b = {(t,x) : t=−|x|}.

Away from the vertex it is a three-dimensional null hypersurface. It is
not a singleton and not a spacelike simultaneous present. Thus 'edge' may
mean a unique maximal event, a null boundary, or an absolute simultaneous
surface, with different answers. The extended null boundary rebuts a
literal claim that E_b has only a point of boundary. It does not rebut the
failure of distant persistence under P_CR or restore a spacelike present.

**Source scope.** Chapter 9 pp.157–160 makes a separate recapture argument:
under PR1 and PR2 the classical simultaneity classes are recovered, while
pointy views leave only singleton classes. The authors explicitly say PR1
fails in the relativistic setting; their argument compares the recovery of
classical temporaryist views. The objection therefore concerns fitness as
a relativistic successor to classical growing block, not a claim that a
Minkowski past cone has singleton topological boundary. Our boundary
calculation does not defeat that recapture concern. The translation proofs
in Appendix 3 remain unchecked.

## What this resolves for the project

The earlier E_b=J⁻(b) model is mathematically usable, but it cannot also
claim to satisfy the examined criterion of distant current persistence.
Its strongest available reply is to defend a different account of located
continuation and explain why classical simultaneity-based persistence is
not the criterion to preserve. That defense is an outstanding philosophical
bridge, not a new consequence of the dust field classification.

Admitting one suitable spacelike location would address the location
requirement for that one element; the persistence argument alone does not
force every spacelike event to exist. Moving from such a requirement to
the full bow-tie domain also uses the uniform treatment of the elsewhere
region in C&R's restricted comparison. Constructing an intermediate domain
consistent with their other principles is a separate problem, not done here.

Bow-tie domains can supply the missing spacelike locations while paying
their separately identified cost of nontransitive existence across
standpoints. The present construction does not show either cost to be
preferable. It also does not show that observations distinguish the two
ontologies: neither observation dynamics nor likelihoods were specified.
The mathematical causal-past fixing theorem remains valid on its stated
base. Treating that base as all of reality requires a separate defense.
