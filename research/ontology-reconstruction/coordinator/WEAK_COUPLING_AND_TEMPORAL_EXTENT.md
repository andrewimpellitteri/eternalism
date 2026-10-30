# How sharp must a law-constitutive present be?

30 October 2026. Coordinator argument, initially unreviewed. This is a
robustness test adjacent to, rather than a replacement for, the isolated
`ontology-constitutive-extent-test` worker. Its bounded target is the move
from physical individuation to an exact boundary of concrete existence.
The mechanics and interval lemma below are elementary; no novelty claim.

## 1. The strongest reply comes first

Genuine systems need not be perfectly isolated. Brading explicitly treats
interacting component bodies as unities, and her proposed presents need
not be transitive across systems. Therefore the connectedness of an
interaction graph cannot refute her account. Nor does an approximate
boundary make a physical system unreal.

The narrower question is whether a proposed criterion has enough content
to support the particular ontological conclusion drawn from it. Exact
autonomy, robust approximate autonomy, material identity and the duration
of an activity are different criteria. Each can do useful work without
fixing which events alone are concrete for a system.

Primary source check: Brading 2015, published-layout author copy, pp16–18,
§§4–5, directly reread. She extends law-constitutive unity to interacting
parts, reverses the explanatory priority of presence and reality, and
leaves genuine subsystem existence open. Her proposal does not identify
unity with the graph criterion tested here. Brading 2013, pp1104–1105,
§4, likewise includes both composite and component unity. These texts
motivate the question; they do not contain our model or lemma.

## 2. An exact material-autonomy test

Take four equal masses on a line, with displacements x_i from fixed
equilibrium positions and momenta p_i. In units with mass and the two
internal spring constants equal to one, let

    H_κ = (1/2)Σ_i p_i² + (1/2)(x_2−x_1)²
          + (1/2)(x_4−x_3)² + (κ/2)(x_3−x_2)²,
    0 ≤ κ ≤ 1.

The equilibrium positions specify spring rest lengths; they are not
external anchoring potentials. The whole is translation invariant.
This is a finite Newtonian model, not an Einstein–matter spacetime or
an empirical model of the universe. Its constituent material variables
are stipulated in advance, rather than derived from the Hamiltonian.

Define *exact autonomous material subsystem*: a nonempty set S of these
masses whose equations for (x_i,p_i), i∈S, depend only on those variables
for every admitted initial state. This is a state-space condition, not
the accidental vanishing of the force on one solution.

For this model, S is autonomous exactly when no positive-strength spring
crosses from S to its complement. The forward direction follows because
a crossing spring contributes κ_ij x_j to p_i'; varying x_j while fixing
all S variables changes that derivative. In the reverse direction every
force term uses variables in S. Thus the minimal autonomous material
sets are the connected components of the positive-coupling graph.

At κ=0, A={1,2} and B={3,4} are its two components. At every κ>0 the graph
is connected, so the only nonempty autonomous material subsystem is the
four-mass whole. In particular,

    (p_1+p_2)' = κ(x_3−x_2),
    (p_3+p_4)' = −κ(x_3−x_2),
    (Σ_i p_i)' = 0.

The exact-autonomy classification changes at zero coupling. This does
not show that A and B cease to be bodies or genuine unities: that would
equate unity with a criterion that Brading need not accept. It identifies
what an exact-isolation reconstruction of her view would buy and lose.

## 3. Robust behaviour survives this sharp change

Write z=(x,p), z'=A_κ z, where

    A_κ = [0 I; −K_κ 0] = A_0 + κ B.

K_κ is the graph Laplacian of the three springs. In the Euclidean norm
on these dimensionless variables, ||K_0||=2, ||B||=2 and
||A_κ||≤4 for 0≤κ≤1. For the same initial state at time zero, variation
of constants gives, for either time direction,

    ||z_κ(t)−z_0(t)|| ≤ 2κ |t| exp(4|t|) ||z(0)||.

For t≥0, use
κ∫_0^t exp(A_κ(t−s)) B exp(A_0 s) z(0) ds and the stated operator bounds;
the reversed integral gives the same bound for t≤0. Consequently the
trajectories converge uniformly on every fixed finite interval as κ→0.
The bound is deliberately crude, and does not assert approximation
uniformly for arbitrarily long times. Other fixed finite-dimensional
norms change constants, not compact-time convergence.

For a specified tolerance η, state bound ||z(0)||≤R and observation
duration T, the sufficient condition

    2κ T exp(4T) R ≤ η

allows A and B to be treated as approximately independent in this norm.
The condition depends on the duration, tolerance and state class. It is
not a proposed universal physical threshold, and it is not a necessary
condition for a successful approximation.

This is a counterweight to an exact-isolation objection: physical
subsystems can remain useful and robust under weak external interaction.
Discontinuity of an exact classification alone is no refutation; exact
physical distinctions can be discontinuous. A further argument would be
needed to make robustness mandatory for fundamental ontology.

Butterfield's arXiv:1106.0702v1, selected §§1.1–1.2, is prior philosophical
context: robust finite-system behaviour can warrant physical reality
without reifying an ideal limit. His examples and emergence claims are
not an argument for a temporal ontology or for our particular criterion.

## 4. Separability needs a choice of physical parts

Because K_κ is real symmetric, an orthogonal change x=OQ, p=OP
diagonalizes it and is canonical. Then

    H_κ = (1/2)Σ_α [P_α² + ω_α² Q_α²].

There is one translation mode and three positive-frequency modes when
κ>0. At κ=0 there are two translation modes. In mode variables the
equations separate even when the material interaction graph is connected.
This is elementary normal-mode mechanics, not an ontology equivalence.

Therefore a criterion of unity formulated as unrestricted coordinate
inseparability would give a different answer from material autonomy.
The latter keeps the physical body/spring decomposition fixed; its
justification can appeal to localization, interventions or constituent
identity. Those are substantive resources, not illicit additions. The
point is to state them, rather than claim that bare separability of a
differential equation individuates its physical objects by itself.
No mixing of separated material variables is declared a physical gauge
symmetry here.

## 5. A temporal refinement obstruction

Even a defensible criterion of material unity need not determine a
temporal thickness. State the following restricted lemma explicitly.

Fix a system and a marked time b. Let C(I,b) mean that an open interval I
containing b supplies the proposed constitutive extent. Assume:

1. At least one such I qualifies.
2. If I qualifies, every smaller open interval J with b∈J⊂I qualifies.

There is no inclusion-minimal qualifying open interval. Given any I,
choose ε>0 with (b−ε,b+ε)⊂I, then choose a strictly smaller such interval.
Each qualifies by assumption 2. This proves neither that a singleton
qualifies nor that the zero-duration limit constitutes a physical thing.

The material-autonomy criterion in §2 has this restriction property:
the same time-independent force law and its cross-derivatives apply on
every nonempty time interval. Momentum conservation of the closed whole
also holds on every subinterval. Those criteria therefore supply no
smallest positive temporal extent. They do not select the whole history
either: it is simply one among many qualifying intervals.

The premise fails for a criterion requiring a completed collision,
cycle, communication exchange or other specified activity. That is a
live response. It must identify the relevant activity and explain why
its extent constitutes the persisting system's present, rather than
merely the extent of that activity. Several constitutive grounds are
permitted; a uniqueness objection applies only to an account claiming
a uniquely selected extent. The lemma does not rule out such an account.

## 6. Overlap agreement does not imply inventory inheritance

For comparison, let U_a={a,b}, U_b={b,c}, U_c={c}. Interpret all physical
predicates by restricting one consistent assignment to these domains.
All descriptions agree on their intersections. Yet b∈U_a and c∈U_b
while c∉U_a. No contradiction follows from overlap agreement alone.
This finite construction is not a relativistic ontology or a model of
Brading's full account.

The additional rule

    b∈U_a and x∈U_b  ⇒  x∈U_a

is inventory transitivity. Our earlier classification work studies its
consequences; it is stronger than overlap agreement. An argument cannot
impose it merely by describing local ontologies as coherent. Conversely,
rejecting it still leaves the positive task of explaining relations
between local presents. The issue is explanatory, rather than a formal
contradiction established by this example.

## 7. The philosophical conclusion and its strongest rival

The positive methodological claim is *match the boundary claim to its
warrant*. A robust dynamical organization can support realism about a
system without supplying an exact, exhaustive boundary of concrete
existence. If the proposed present is approximate or scale dependent,
its account of existence must say how that qualification is interpreted.
Approximate unity does not by itself establish vague existence; neither
does it establish that everything outside the approximate region is unreal.

A strong law-constitutive rival can accept all the mechanics, retain
interacting A and B as genuine systems, and ground their presents in
specific sustaining processes rather than autonomy. It may allow a
plurality of extents, or a scale-relative account with no sharp exclusion
claim. That response survives this note. Its next obligation is to show
which physical process does the constituting and why its temporal extent
has the asserted existential role.

An event realist can likewise retain emergent systems, interaction and
activity durations within an unrestricted history. This note gives that
view no exclusive explanation of the mechanics, nor any presumption that
all future events currently exist. The comparison turns on the additional
constitutive and existential explanation, not on counting systems or
discarding everything approximate.

The best question is now: **what distinguishes the continuing existence
of a system from the completion of one activity that helps sustain it?**
A successful physical answer could underwrite a proper temporal extent.
A negative answer to a stage selector does not establish whole-history
constitution by default.

## 8. Defeaters and next obligations

This argument should be narrowed if a source-faithful criterion of unity
already fixes the relevant physical decomposition and a nonhereditary
sustaining extent independently of the desired temporal ontology. A
model with an empirically supported transition or threshold can also
undercut the claim that a sharp boundary lacks independent warrant.
No such criterion has been excluded by the oscillator calculation.

Before an ontology preference: test a concrete sustaining-process proposal
against its strongest same-physics rival; distinguish the system from an
activity token; defend any exact exclusion or scale-relative semantics;
and obtain independent criticism. The two isolated GLM tasks keep their
own scopes. No finite-control, smoothness, source-access or novelty gate
is closed by this note.
