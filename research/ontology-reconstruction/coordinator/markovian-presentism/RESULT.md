# Markovian laws and presentism: what the likelihood-one claim covers

7 November 2026. Coordinator session (Claude Code, Opus 5.5), at the user's request.
It follows up the [6 November intake](../../../../knowledge/frontier/INTAKE_2026-11-06.md),
which found that the repo had never engaged this argument. This is a bounded
reconstruction with elementary observations. It claims no novelty and selects no
temporal ontology. No outside expert has read it. Sources and read depths are in
[sources.jsonl](sources.jsonl). Page numbers for Builes–Impagnatiello are those of
the 2022 author preprint. Lettie also cites that version. The published OSM 14 text
was not compared.

## 1. The rival argument, stated as its authors give it

Builes and Impagnatiello (B&I) set up the argument in three steps.

- **Markovian Determination (p. 2).** For every time t, if the whole history
  H_t up to t nomically necessitates that the future t+ has an intrinsic
  property P, then the intrinsic state T at t already necessitates it.
- **Markovian Chance (p. 3).** This is the chance analogue:
  Ch_L(P | T) = Ch_L(P | H_t).
- **Relativistic version (pp. 3–4).** Each principle holds relative to every
  inertial slicing in special relativity, and relative to every Cauchy foliation
  of a globally hyperbolic spacetime in general relativity.

"Near" versions replace the instant by an arbitrarily short interval (p. 5).
"Markovian*" means compatible with being Markovian, given suitable intrinsic
quantities such as velocities (p. 6).

- **§3 (eternalism lacks a reason).** Humean eternalism gives no reason to expect
  Markovian* laws. Non-Humean eternalism doesn't either. Universals and primitive
  laws are too restrictive or too permissive. Local causal powers come closest, but
  face a dilemma. If locality is necessary, the necessity needs explaining. If it is
  contingent, its holding needs explaining. Their toy world is the periodic sequence
  …0011… with a simple second-order law.
- **§4 (presentism alone is not enough).** Presentism with primitive tensed laws can
  still violate Markovianism (pp. 10–11). Two packages entail it:
  - **§4.1:** presentism plus Aristotelian causal powers. Every constraint on the
    future is grounded in concrete present reality.
  - **§4.2:** Nomic Presentism. A tensed claim is true iff, and because, it is
    nomologically necessary given the present state. From this they derive
    Markovian Determination by a valid-argument schema (p. 14). If T necessitates
    Q, then whatever T∧Q necessitates, T necessitates. They derive Markovian Chance
    because T and H_t are nomically equivalent (p. 15).
- **Footnote 18.** Standard growing-block and moving-spotlight theories cannot use
  either strategy, because they contain concrete past entities.
- **§5 (the Bayesian claim).** Cr(Markovian* | ¬NHP) ≪ Cr(Markovian* | NHP) = 1,
  where NHP is non-Humean presentism. Footnote 20 adds that discovering
  non-Markovianity would falsify these presentisms.

## 2. What the existing replies already cover

- **Lettie (2024, preprint read in full).** He accepts the likelihood claim (∗). He
  denies that it fixes a high posterior, because a rational prior can make NHP very
  improbable. He offers an explanation that needs no temporal ontology: Markovianism
  is one of many "Markovian-like" universe-wide properties, each improbable, but
  some member of the class is probable.
- **Ryoo (2026, §§1–5 read).** He builds the mirror argument: non-Markovian
  foundations (Barandes, thermal time, open systems) would favour eternalism. He
  argues that the growing block faces a symmetry problem.
- **Howarth (2026, read through §5.2).** He separates reduced-state, embedding,
  fundamental-law and metaphysical screening-off. He names the needed bridge
  (BP1/TDEB). He notes that higher-order and memory dynamics can be embedded in
  Markovian dynamics on an enlarged state. His conclusion is that Markovianity
  underdetermines existence claims.

None of these replies examines what exactly B&I's derivation in §4.2 makes
certain. None connects the argument to relativistic locality or to Bell-type
results. §§3–5 below address those points.

## 3. Elementary observations about the deterministic principle

Represent a deterministic law over a fixed foliation by its solution set 𝓛. Each
history s ∈ 𝓛 assigns an intrinsic state s(t) to each time t. Two sets of futures
matter: those compatible with the whole history up to t, and those compatible with
the state at t alone.

    Fut_H(s,t) = { s′|_{>t} : s′ ∈ 𝓛, s′|_{≤t} = s|_{≤t} }
    Fut_T(s,t) = { s′|_{>t} : s′ ∈ 𝓛, s′(t) = s(t) }

**(O1) The principle is a splicing property.** Suppose every set of future segments
counts as an "intrinsic property of t+". Then Markovian Determination is
equivalent to two statements:
- Fut_T = Fut_H for all s and t.
- Equivalently, 𝓛 is closed under splicing at equal states: if s(t) = s′(t), then
  the history that follows s up to t and s′ afterwards is in 𝓛.

*Proof.* Fut_H ⊆ Fut_T always holds. If a segment lies in Fut_T but not in Fut_H,
take P = "t+ ∈ Fut_H(s,t)". H_t necessitates P, but T does not. If the principle
holds, every segment of Fut_T lies in Fut_H, so the splice is a solution. The
converse is immediate. ∎

If admissible properties are restricted, the principle is weaker. That restriction
is B&I's to state. The splicing form is the standard behavioural-systems notion of
a Markovian system or "axiom of state". See Rapisarda & Willems, §3, read at
excerpt depth. We claim no novelty for it.

**(O2) Backward single-time determination entails it.** Suppose s(t) = s′(t)
implies s|_{≤t} = s′|_{≤t}. Then every splice is s′ itself, so 𝓛 has the Markovian
property. The step mirrors B&I's own schema on p. 14, with the laws in place of
Nomic Presentism's grounding claim. Horvat makes the parallel point (footnote 10):
time-symmetric deterministic theories leave no room for history to matter. So
unitary Schrödinger evolution, Hamiltonian flow and well-posed reversible
hyperbolic systems with Cauchy data are Markovian because they are backward
deterministic from a single time. No temporal ontology is needed. GRW-type and
other chancy laws are not covered, and there the chance principle carries the weight.

**(O3) The "Markovian\*" qualifier needs an independent criterion of intrinsic
state.** For any 𝓛, take as state the class of pasts with the same set of possible
continuations. This is the past-induced, Nerode-style state in behavioural theory.
The enlarged system is Markovian by construction.
- B&I's footnote 10 accepts such an enlargement for …0011…, through "coming from a
  0/1" properties.
- It then calls …000111… "clearly neither" Markovian nor nearly Markovian. But the
  same construction gives …000111… a three-valued phase state.
- So "Markovian\*" constrains anything only once B&I say which latent quantities
  count as intrinsic: velocities and the wavefunction yes, phase counters no.
- The paper raises the velocity debate (pp. 4–5) and then sets it aside by
  appealing to quantum theory. Whether the wavefunction is intrinsic to a time is
  itself disputed. Howarth makes the general embedding point. Applying it to the
  footnote-10 example is our elementary step.

## 4. What Nomic Presentism makes certain

On p. 14, B&I restate Markovian Determination for presentism with "the history" =
the present state plus all true WAS-claims. Call this MD_pres. Under Nomic
Presentism, the true WAS-claims are exactly those that L∧T necessitates. So MD_pres
follows by the schema *for every law L*. That includes the …0011… law, which
fails splicing.

The point is worth checking concretely for the footnote example under a
supervaluational reading. Thomason (1970), whom B&I list among the sources of Nomic
Presentism, gives one, though B&I do not commit to a semantics.
- With present state 1, two of the law's histories fit: the present is either the
  first 1 or the second.
- No WAS₁ or WILL₁ atom is necessitated, so each is gappy.
- The tensed law is true on every fitting history, so it is supertrue.
- So Nomic Presentism is consistent with this non-Markovian law, and MD_pres still
  holds.

On a classical compositional reading, the same iff-form law instance comes out
false at the present. Then Nomic Presentism's consistency depends on how tensed
laws are written. Either way, Nomic Presentism alone does not entail the property
of the *laws* (O1) that physics reports.

Therefore the proposition B&I make certain in (∗) is not the empirical datum.
- **What NHP makes certain:** MD_pres, which holds whatever the dynamics.
- **What physics reports (pp. 3, 6):** a property of 𝓛, namely splicing or
  single-time forward determination of the future or its chances.

There is a route from Nomic Presentism to the datum. Add that the past-tense
claims we take ourselves to know are true. Under Nomic Presentism they must then be
necessitated by L∧T. That is backward determination from the present, restricted
to those truths, and by (O2) it delivers the matching restricted Markov property.

**Consequence for the rival (a conditional assessment, not a refutation).** A
repaired argument would cite backward single-time determination of the
record-relevant past as its datum, not Markovianism. That changes its exposure.
- Backward determination fails for collapse and other chancy laws. Under Nomic
  Presentism they open the past, as B&I's own footnote 17 concedes.
- Markovian Chance does not fail for those laws.
- So the repaired argument depends on the interpretation of quantum mechanics in a
  way the stated argument does not.

The §4.1 causal-powers route is untouched by this section. It entails the principle
because there are no past bearers of power. It still needs the further claim that
present powers cannot respond to irreducible tensed facts, which B&I defend on
pp. 12–13.

This is the inferential revision a knowledgeable opponent would have reason to
make, as `research/agentic-philosophy/BREAKTHROUGH_TEST.md` requires. The point is
logically elementary, and we found no earlier statement of it in the three replies
read. That is not a priority claim: the search was limited, and the published OSM
text and later citers remain unread.

## 5. Relativity, locality and Bell

B&I's relativistic datum quantifies over global Cauchy foliations (pp. 3–4). Two
project-relevant results bear on how far it extends.

- **Local presents.** Some presentisms avoid global simultaneity: Stein-type
  pointed presents, and the views B&I cite in footnote 24 (Emery, Balaguer). For
  them, the natural local analogue compares what the causal past J⁻(b) fixes with
  what a local present fixes. The
  [finite-prefix corollary](../../../lawful-completions/coordinator/prefix-mass-audit/RESULT.md)
  bears on this.
  - It has internal acceptance and depends on named inputs.
  - In its Einstein–massless-scalar model class, the whole pointed J⁻(b) can agree
    while finitely many future scalar readings along γ vary.
  - So in that class the local deterministic principle cannot discriminate between
    rivals on those readings. Neither the history nor a local present fixes them.
  - The non-vacuous datum needs data on a global Cauchy surface. That is the
    structure a footnote-24 presentist declines to privilege.
  - This is a scope observation about one model class. It is not a theorem about
    all local presentisms.
- **Bell-type tension (our conjecture).** This rests on Horvat (arXiv:2610.41944v1),
  whose Proposition 3 we read as a statement only; its proof was not checked.
  - His Principle 4, "Irrelevance of History", is a surface-relative Markov-chance
    condition. It also carries a time-translation clause that B&I's principle lacks.
  - Proposition 3: his Probabilistic Locality plus Irrelevance of History imply
    Bell's Local Causality.
  - So anyone who keeps his local principle must accept that history is relevant,
    given Bell violations.
  - B&I's Markovian Chance is satisfied by quantum theory through a global state on
    Cauchy surfaces, which is not a local event-wise condition.
  - We conjecture that B&I's datum survives only in a global-state form. In
    Horvat's local event form, Bell violations count against it, and B&I's footnote
    20 treats that kind of failure as falsifying.
  - Whether Horvat's principle and B&I's principle are close enough for the
    transfer, given the translation clause, is open. Horvat does not cite B&I.

## 6. Bearing on the repo's causal-production lane

The [Tooley reconstruction](../causal-production/RESULT.md) leaves open whether
temporal actuality, or a real directed governing relation, better grounds the
asymmetry when laws vary. B&I bear on both sides of that dispute.

- **Their dilemma hits our rival.** The repo's strongest rival to Tooley is a
  non-Humean directed governing relation. B&I's §3 dilemma about local causal
  powers targets exactly this kind of rival. The repo has not answered that
  dilemma.
- **Their footnote 18 hits Tooley's view.** A standard growing block contains
  concrete past entities. So it cannot use either presentist route to the Markov
  property. A growing theorist who borrows Tooley's explanatory ambition inherits
  the question of why an existing past adds no constraint beyond the present.
- **Neither side wins.** By (O2), backward-deterministic physics supplies the Markov
  property to every ontology. So this pressure is real only for chancy or
  non-reversible laws. It does not decide between the two sides.

## 7. Limits and next tests

- **Sources.** The B&I text is the 2022 preprint. The published version, its
  citing literature beyond Lettie, Ryoo and Howarth, Markosian (2013) and Thomason
  (1970) are unread. Horvat and Rapisarda–Willems are partial or excerpt reads.
- **Proofs.** O1–O3 are elementary set-theoretic observations. No proof assistant
  was used. The supervaluational check in §4 uses one reading of Nomic Presentism.
  B&I may intend another.
- **Undecided.** Nothing here decides between presentism and eternalism. It
  locates which datum each package predicts.
- **Next test 1.** State the chance version of §4 precisely. Under Nomic
  Presentism, Markovian Chance is again immediate for every chance law. Check
  whether a records-based repair needs backward determination of chances, and
  whether GRW supplies it.
- **Next test 2.** Read Horvat's proofs, and test whether Principle 4 without the
  translation clause still yields Proposition 3.
- **Next test 3.** An observability question, recorded as a conjecture only.
  Dependence on a past event that leaves no present trace cannot be measured
  directly, since any measured correlation runs through present records. How much
  of observed Markovianism this selection effect explains is open.
