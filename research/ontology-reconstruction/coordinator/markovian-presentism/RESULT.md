# Markovian laws and presentism: what the likelihood-one claim covers

> **8 November audit:** Several conclusions below are overstated. Read [the adversarial audit](AUDIT_2026-11-08.md) before relying on the semantic, Bell, wavefunction-realism or foliation claims. The reply is not yet validated.

7 November 2026, revised the same day. Coordinator session (Claude Code, Opus 5.5), at
the user's request. It follows up the
[6 November intake](../../../../knowledge/frontier/INTAKE_2026-11-06.md). This is a
bounded reconstruction with elementary observations. It claims no novelty and selects
no temporal ontology. No outside expert has read it. Sources and read depths are in
[sources.jsonl](sources.jsonl). Page numbers for Builes–Impagnatiello are those of the
2022 author preprint. Lettie also cites that version. The published OSM 14 text was
not compared.

**What the revision changed.** The first version said that a repaired argument
would have to cite backward determination, and that this would expose it to the
interpretation of quantum mechanics. That inference was wrong. Suppose the
evidence E is single-time determinism. E entails the Markov property, so
P(E | H) = P(Markov | H) · P(E | Markov, H). The Markov likelihood ratio therefore
survives inside any likelihood ratio for E. Observation O2 below stays true, but it
does not defeat the Bayesian argument. §4 is restated. §§5–6 are new. They follow a
citation sweep, Markosian's semantics, and a check of Horvat's proof.

## 1. The rival argument, stated as its authors give it

Builes and Impagnatiello (B&I) set up the argument as follows.
- **Markovian Determination (p. 2).** If the history H_t nomically necessitates a
  property of the future t+, so does the present intrinsic state T.
- **Markovian Chance (p. 3).** Ch_L(P | T) = Ch_L(P | H_t).
- **Relativistic version (pp. 3–4).** Each principle holds relative to every inertial
  slicing, and relative to every Cauchy foliation of a globally hyperbolic spacetime.
- **"Markovian\*" (p. 6).** Compatible with being Markovian, perhaps subject to
  debates about whether vector quantities such as velocity are intrinsic. Quantum
  theory is said to be "uncontroversially Markovian" (p. 6). Footnote 5 says the
  same of Bohm and orthodox collapse.

The core moves:
- **§3.** Neither Humean nor non-Humean eternalism predicts Markovianism\*.
- **§4.1.** Presentism plus Aristotelian causal powers entails it.
- **§4.2.** Nomic Presentism with any non-Humeanism entails it. Nomic Presentism says
  a tensed claim is true iff, and because, the present state and the laws
  necessitate it. The derivation uses the schema on p. 14 and the nomic equivalence
  of T and H_t on p. 15.
- **(∗) (p. 16).** Cr(M\* | ¬NHP) ≪ Cr(M\* | NHP) = 1, where NHP is non-Humean
  presentism.
- **Footnote 20.** Discovering non-Markovianity would falsify these views.
- **Second moral (p. 18).** Markovianism\* is a "perfectly precise datum".

## 2. Literature located (citation sweep, 7 November)

The sweep used OpenAlex's list of citing works (five indexed) and Exa searches.
Semantic Scholar was rate-limited. The papers that engage the argument:
- **Lettie (2024), read in full.** Rational priors can keep NHP improbable.
  Markovianism is one improbable member of a probable class.
- **Ryoo (2026).** The mirror argument for eternalism from non-Markovianity.
- **Howarth (2026).** Markovianity underdetermines existence. A Markovian embedding on
  an enlarged state is possible "under suitable conditions".
- **Mariani (2025, JGPS), §4.1 read.** For non-Markovian collapse models with
  coloured noise, whether properties of the laws bear on ontology depends on the
  Humean/non-Humean divide.
- **Builes (2026, *Phil. Studies*), preprint searched; Markovianism never
  mentioned.** He treats temporally symmetric determinism as a live possibility. He
  presents Nomic Presentism as escaping the redundancy of fundamental facts. He
  concedes that it implies a possibly open past.
- **Olsen (2025).** Cites B&I only in a footnote.

None of these examines what the §4.2 derivation proves. None asks in which state
Markovianity is a datum. None connects the argument to Bell-type results. That is
not a priority claim. The search was limited, and the published OSM text is unread.

## 3. Elementary observations (deterministic case)

Represent a law over a fixed foliation by its solution set 𝓛 of histories s.

**(O1) The principle is a splicing property.** Suppose every set of future segments
counts as an intrinsic property. Then Markovian Determination is equivalent to closure
of 𝓛 under splicing at equal states. If s(t) = s′(t), then s up to t followed by s′
after t is in 𝓛.

*Proof.* The futures compatible with the history are always among those compatible
with the present state. If some future fits the state but not the history, take P =
"the future is one of those compatible with the history". The history necessitates P
and the state does not. If the principle holds, every splice is a solution. The
converse is immediate. ∎

This is the behavioural-systems notion of a Markovian system, or the "axiom of state"
(Rapisarda–Willems §3, excerpt depth). We claim no novelty for it.

**(O2) Backward single-time determination entails it.** If s(t) = s′(t) implies the two
pasts agree, every splice is s′ itself. Horvat's footnote 10 makes the parallel point.
As the revision note explains, this does not weaken (∗). It shows only where
deterministic Markovianism sits relative to determinism.

**(O3) Markovianity is relative to a choice of state.** For any 𝓛, the
past-induced state is the class of pasts with the same continuations. On that
state, 𝓛 is Markovian by construction. Its stochastic analogue is the predictive
state, which has the same continuation distributions.
- B&I's footnote 10 accepts a "coming from a 0/1" enlargement for …0011… but calls
  …000111… "clearly" non-Markovian.
- A three-valued phase state makes …000111… Markovian in exactly the same way.

## 4. What the §4.2 derivation proves, on its source's own semantics

Under Nomic Presentism, the restated principle on p. 14 (MD_pres) follows from the
schema *for every law L*. MD_pres takes "the history" to mean the present plus the true
WAS-claims. B&I's own …0011… law shows Nomic Presentism is consistent with laws that
are not Markovian on their stated state.
- **Markosian's semantics (2013, §6, pp. 13–14).** Markosian is one of the view's named
  sources. A tense-operator sentence is true at p iff it is true on every route of
  nomically possible history through p. Atomic tensed claims that fail on some route
  are false; he prefers bivalence (p. 10).
- **The routes.** With present state 1, two of the law's routes pass through p. So
  every WAS₁ and WILL₁ atom is false.
- **The law.** The tensed law (∗∗) begins with "always" and holds on every route, so it
  is true at p.
- **So:** Nomic Presentism (with Markosian's ADT laws, p. 9) is consistent with a law
  that is non-Markovian on the stated state, and MD_pres holds. The past and future it
  makes true are thin, as Markosian accepts for indeterministic laws (p. 15).

The derivation therefore establishes MD_pres, a theorem of Nomic Presentism for any
law. It does not establish that the laws are Markovian on any state physics specifies.
To reach the laws, B&I need one more premise. Call it **governance from the present**:
a governing law can take as input only what obtains at the present.
- That is the Aristotelian premise of §4.1 in a different form. So §4.2 does not hold
  "together with any version of Non-Humeanism" (p. 13).
- The claim fails for constraint-type non-Humeanism, which constrains whole
  histories (Chen–Goldstein minimal primitivism; Adlam). B&I note both in their
  footnote 28.
- On the more plausible reading, the two strategies converge on one premise.

**Consequence.** This is an inferential correction, not a refutation. The confirmation
in (∗) can be credited only to NHP packages that include governance from the present.

## 5. Markovian in which state? The datum depends on interpretation

The second moral calls Markovianism\* a precise datum. By (O3) it has content only
relative to an independently fixed state. Physics fixes the state in more than one way.
- **Wavefunction state.** Schrödinger and GRW evolution of ψ is Markov.
  Goldstein–Tumulka–Zanghì (§ on the conditional probability formula, excerpt depth)
  state the Markov property of the GRW ψ-process. B&I's datum is true for this state.
- **Primitive-ontology state.** In GRW with flash ontology:
  - ψ_s is a function of the flashes before s and the initial ψ (same source).
  - Esfeld and Gisin argue ψ is nomological there, not part of what exists in
    spacetime. An initial flash configuration does not fix ψ (§2, excerpt depth).
  - On that reading, the chance of the next flash depends on the whole flash history.
    The ontic state is not Markov.
  - Footnote 5's claim that collapse theories are Markovian therefore holds only if ψ
    is intrinsic to the present, which is contested.
- **Local event state (Horvat, arXiv:2610.41944v1).** We checked his proof of
  Proposition 3 (statement and steps read, not formalised).
  - The translation clause in his Principle 4 only moves the conditioning surface Σ
    to the initial surface Σ_{t0}, where his measures are defined.
  - B&I's chance functions are defined at every time. So their Markovian Chance can
    play that role directly: Ch(a | e on Σ and history) = Ch(a | e).
  - His Probabilistic Locality, applied to the chance conditioned on the complete event
    state e at Σ, then gives the Bell-type contradiction in his equations (14)–(17).
  - So, adapting Horvat's argument (credit his), Markovian Chance on a complete
    local-beable state plus probabilistic locality implies Bell's local causality,
    which Bell violations falsify. GRWf is a concrete case of that failure.

**Upshot (our assessment).** B&I's datum holds when the present intrinsic state is the
global wavefunction on a Cauchy surface. That needs both wavefunction realism and a
global foliation. It fails, or is contested, for the two other states physics supplies:
primitive-ontology states and local event states.
- **Footnote 20.** Discovering non-Markovianity would falsify NHP, they say. On
  primitive-ontology readings, that discovery has arguably already been made.
- **Footnote 24.** For the local presentisms they cite (Emery, Balaguer), a local
  Markov-chance datum conflicts with Bell, given Horvat's locality principle.
- **What stays open.** None of this shows presentism is false. It shows the evidence
  for (∗) is interpretation-relative, and the interpretation needed is a substantive
  extra commitment.

## 5b. The foliation surplus

Added 7 November in the second pass. B&I state the relativistic datum as Markovianism
relative to *every* inertial slicing or *every* Cauchy foliation (pp. 3–4). Call this
D_all. Their presentist answer to relativity supplements physics with a privileged
foliation F\* (p. 17).

1. **NHP delivers Markovianity relative to F\* at most.** Both §4 strategies reason
   about "the present". Under a privileged foliation the present is an F\*-slice. Neither
   says anything about Markovianity relative to slices that mix the presentist's past,
   present and future. So NHP entails D_F\* (with the §4 caveat) and nothing about D_all.
2. **Markovianity on one foliation does not give it on all.** Here is a toy model
   (ours, elementary).
   - Two sites, A and B, are two lattice units apart. A signal speed of one unit per
     step defines the cones.
   - The law swaps them: A(t+1) = B(t) and B(t+1) = A(t). This law is Markov
     (deterministic) on the slices t = const.
   - Take the tilted spacelike slices S_k = {A_k, B_{k+1}}. They are achronal for the
     cones. On every solution B_{k+1} = A_k, so S_k carries only A_k.
   - But A_{k+1} = A_{k−1}. That is fixed by the history before S_k and not by S_k.
   - So the law is Markovian on F\* and not on the tilted foliation. The failure needs
     the cone-violating link from B_k to A_{k+1}.
3. **Locality gives D_all.** Suppose influence runs only through chains of intermediate
   events along causal curves. That is B&I's own statement of locality (p. 9),
   restricted to the light cones. Every Cauchy surface meets every inextendible causal
   curve, so the state on any Cauchy surface mediates all influence. In QFT this is the
   time-slice property. Chilian & Fredenhagen (arXiv:0802.1642, abstract read) treat
   it in perturbative QFT on globally hyperbolic spacetimes.
4. **The surplus favours locality, not presentism.** The part of the relativistic datum
   that goes beyond the F\* slices (all foliations) is entailed by relativistic locality.
   NHP does not entail it.
   - On the full datum, Cr(D_all | NHP) < 1. Meanwhile Cr(D_all | local causal powers
     with causal-curve mediation) = 1, and that is the eternalist option B&I call most
     promising (p. 9).
   - B&I's dilemma against that option ("why is locality necessary, or why does it
     hold?") is about the prior. It is not about the likelihood.
   - NHP with locality also predicts D_all, but there presentism does no work for the
     surplus.
   - The theories B&I cite as Markovian\* despite non-locality need an absolute or
     privileged foliation. That covers Newtonian gravity, Bohm, and relativistic
     Bohmian models with a privileged foliation (Dürr, Goldstein, Norsen, Struyve &
     Zanghì, arXiv:1307.1714v2, abstract read).
   - Those theories satisfy D_F\* and not, in general, D_all. So the examples B&I use to
     separate Markovianism from locality are exactly the ones that fail their own
     relativistic datum.
5. **Loops.** Jäger (2025, NYU dissertation; abstract, introduction and §1 definitions
   read) argues that local dynamics give "Boundary Markov". A thick boundary screens a
   region off from everything outside it, including in spacetimes with closed causal
   curves. Such spacetimes have no global present, so neither presentist strategy can
   be stated there. Jäger does not discuss presentism or B&I. The application is ours.
   If he is right, screening-off is a consequence of locality that reaches well beyond
   any foliation.

**Status.** Items 1–4 are elementary and checked here by hand. Item 2 is a toy, not a
physical counterexample. Whether some physical theory is Markovian on a privileged
foliation, empirically adequate, and fails D_all depends on the interpretation. Item 4
is our assessment. We found no prior statement of the surplus point in the six citers
read. That is not a priority claim.

## 6. Local presents and the finite-prefix result

The [finite-prefix corollary](../../../lawful-completions/coordinator/prefix-mass-audit/RESULT.md)
bears on the deterministic local analogue. It has internal acceptance and named inputs.
In its Einstein–massless-scalar class, the whole pointed J⁻(b) can agree while
finitely many future readings along γ vary. So the local deterministic principle cannot
tell rivals apart on those readings, because neither history nor present fixes them. The
non-vacuous datum needs global Cauchy data. This is a scope observation about one model
class only.

## 7. Bearing on the causal-production lane

This is unchanged from the first version.
- **B&I's dilemma hits our rival.** Their dilemma about local causal powers targets the
  repo's preferred rival to Tooley, a non-Humean directed governing relation.
- **Their footnote 18 hits Tooley's growing block.** It says a standard growing block
  cannot use either presentist route.
- **New: governance from the present.** By §4, the presentist explanation itself needs
  this premise. A growing theorist could adopt "governance from the latest edge" and
  inherit the same explanation. That would weaken footnote 18. This is our conjecture.
  It is not tested.

## 8. Limits

- **Unread.** Thomason (1970); Chen–Goldstein; Adlam (2022). The published text of
  B&I and the body of Builes (2026) beyond the searched passages.
- **Partial reads.** Goldstein–Tumulka–Zanghì and Esfeld–Gisin at excerpt depth. Their
  claims are cited as theirs.
- **Nothing formalised or reproduced.** The Horvat adaptation is a proof sketch, and
  needs a careful statement of which chance functions Probabilistic Locality governs.
- **No outside reader.** Same-model review is not independent.
