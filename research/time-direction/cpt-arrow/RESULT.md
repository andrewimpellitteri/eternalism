# The CPT step in the lawful-arrow argument

11 November 2026. Claude Code (Fable 5.2), worker for task `novel-cpt-arrow`. Checked
only by the session that wrote it. Nothing here is claimed as new. No temporal ontology
is selected. Sources and read depths: [sources.jsonl](sources.jsonl).

The step checked is the last paragraph of §2 of
[settling/RESULT.md](../../agentic-philosophy/settling/RESULT.md): "For local,
Lorentz-invariant quantum field theories the CPT theorem supplies such a symmetry. On
that basis an arrow is either a boundary condition, or it needs a failure of locality
or of Lorentz invariance."

## Verdict

**The step survives only in a corrected form, and one of its premises is philosophical.**

1. **The reversal exists, in the form Proposition 2 needs, and the curved-spacetime
   theorem is the one that gives it.** Hollands and Wald's PCT theorem relates the
   theory on (M, g, e, T) to the theory on (M, g, e, −T): same manifold, metric and
   orientation, opposite time orientation, fields replaced by their adjoints. That is
   a flip of the time orientation alone, which is what Proposition 2 uses. The flat
   theorem of Jost is a symmetry of one fixed background that also moves points by
   x ↦ −x. It becomes the flip only after composing with that isometry.
2. **"Locality or Lorentz invariance" is the wrong list of hypotheses.** The flat
   theorem needs the whole Wightman framework, and of locality only weak local
   commutativity. The curved theorem needs Hollands and Wald's axioms. Greenberg's
   claim that CPT violation forces Lorentz violation is disputed in print.
3. **For general relativity and classical tensor fields no CPT theorem is needed.**
   The class is closed under the flip whenever the laws do not mention the time
   orientation. The Einstein equation and the energy conditions do not. Classically
   there are local, covariant laws that do mention it, so the settling note's
   conclusion is false for classical theories as stated.
4. **CPT closes the class only if a world and its charge-conjugate with reversed
   time orientation count as having the same orientation-free content.** If matter
   versus antimatter is a primitive fact, the Standard Model already has a lawful
   arrow relative to it, through the violation of T. This is a known dispute
   (Feynman, Greaves and Arntzenius on one side; Roberts on the other). The physics
   does not settle it.

## The corrected claim

A **world** is (M, g, e, T, s): a globally hyperbolic spacetime, an orientation e, a
time orientation T and a matter state s. The **flip** sends it to (M, g, e, −T, s′),
where s ↦ s′ is a fixed pointwise rule. For classical tensor fields s′ = s. For a
quantum field theory s′ is the state ω̄ that Hollands and Wald's map assigns.

**Proposition 2′.** Let a class of worlds be closed under the flip. A local clock
whose value at a germ equals its value at the flipped germ is constant along every
timelike curve. No rule that reads a time orientation off flip-invariant content can
hold in every member.

*Proof.* As for Proposition 2. If x precedes y in a world, the clock is no greater at
x than at y. In the flipped world y precedes x and the clock values are unchanged. For
the second sentence, a world and its flip have the same flip-invariant content and
opposite time orientations. ∎

**When the class is closed under the flip.**

| Setting | Closed? | Why | Depth |
|---|---|---|---|
| Spacetimes alone, class defined without T (all of Loc₀, vacuum, an energy condition) | Yes | By inspection. Nothing in the definition mentions T | Elementary |
| Spacetimes alone, class defined with T (the curvature clock class, expanding cosmologies) | No | By design | Elementary |
| GR with classical tensor matter obeying equations built from g, e, ∇ and the fields | Yes | The equations do not mention T | Elementary |
| Classical tensor fields on Minkowski spacetime, polynomial equations invariant under the proper orthochronous Lorentz group | Yes | Greaves and Thomas, Theorem 1: such a theory is invariant under total reflection. Total reflection preserves e and reverses T | Their statement read; proof not read |
| Classical laws with an inequality directed by T (entropy production, positive viscosity) | No | See below | Elementary |
| Classical spinor fields | Not established | Greaves and Thomas §8: the classical PT theorem fails to generalise | Their statement read |
| Quantum fields on Minkowski spacetime under the Wightman axioms with weak local commutativity | Yes | Jost's theorem, then compose with x ↦ −x (Hollands and Wald eqs. 88–89) | Jost not read; cited through four papers that state it |
| Quantum fields on curved spacetime under Hollands and Wald's axioms | Yes | Their Theorem 3: an antilinear \*-isomorphism A(M, g, e, T) → A(M, g, e, −T), natural under embeddings, with the dual map on state spaces | Theorem and remarks read; proof of the input relation (their eq. 64) not checked |

**So the corrected sentence is:** on a class of worlds governed by a theory in one of
the "Yes" rows, a lawful arrow is impossible relative to flip-invariant content. An
arrow then needs one of three things: a boundary condition; the failure of a premise
of the relevant theorem; or content that the flip does not preserve.

## Reasons

**1. The flat theorem is not literally the map Proposition 2 uses.** The usual
statement gives an antiunitary Θ on one Hilbert space with Θφ(x)Θ⁻¹ equal to the
conjugate field at −x. It is a symmetry of the theory on one background with one time
orientation. Proposition 2 compares a world with the world that has the same germs and
the opposite orientation. Hollands and Wald make the link explicit: the reflection ρ
maps (ℝᴰ, η, e, T) to (ℝᴰ, η, e, −T), and their map is χ_ρ ∘ Ad_Θ. In a general
spacetime there is no such isometry and only their form exists. Their own gloss is
that the theory on M is "the same" as the theory on M̄ with fields replaced by charge
conjugates, and that the theorem relates an expanding universe to the corresponding
contracting one and says nothing about processes within one universe.

**2. Quantum laws do mention the time orientation.** The spectrum condition, flat or
microlocal, is stated relative to T. Closure under the flip is restored because the
map is antilinear. This is why the quantum case needs a theorem and the classical
tensor case does not.

**3. The hypotheses.** Jost's theorem, as stated by Greenberg and by Dütsch and
Gracia-Bondía: in the Wightman framework, weak local commutativity at Jost points is
necessary and sufficient for CPT symmetry. So the premises are the state-space,
domain and covariance axioms, the spectrum condition, and weak local commutativity.
Greenberg argues that CPT violation in an interacting theory implies non-covariant
time-ordered functions. Chaichian, Dolgov, Novikov and Tureanu give nonlocal models
that are invariant under the proper orthochronous group and violate CPT, with the
time order of timelike-separated points written into the interaction. They also cite
Lorentz-violating theories that keep CPT. Dütsch and Gracia-Bondía argue that
Greenberg's argument presupposes Wightman functions for interacting fields that
nobody has constructed. The Chaichian model is an example of the corrected claim: its
law mentions T, and it is not local.

**4. Classical counterexamples to "local and Lorentz-invariant implies no arrow".**

- The project's own curvature clock class: "the Ricci scalar never increases along
  future causal curves" is local and generally covariant, and is not closed under the
  flip.
- A viscous fluid. With u the future-directed unit flow, the stress tensor is
  ρuᵃuᵇ + p hᵃᵇ − 2ησᵃᵇ − ζθhᵃᵇ. The shear σ and expansion θ are odd in u and the rest
  is even. Flipping T replaces u by −u, so the same metric and stress tensor solve the
  equations with −η and −ζ. With positive viscosity required by law, the flipped world
  is excluded. This is an effective theory, not a fundamental one.
- Malament's equation ∇ₐ(F_mn F^mn) = Jₐ. It is a polynomial tensor equation. It is not
  time reversal invariant in his sense, because he takes F and J to be defined
  relative to the time orientation, so that both change sign under the flip.

What excludes such laws is not locality or Lorentz invariance. It is the demand that
the law be a polynomial equation in tensor fields that are themselves independent of
T. A time orientation is not such a field. That is Greaves's diagnosis of the
classical PT theorem, as reported by the search record and by Roberts; her paper could
not be fetched.

**5. What the flip preserves.** Compare two readings of the Malament example. If F
and J are fields given independently of T, the flip leaves them alone and every
tensor equation is flip-invariant. If they are defined relative to T, with charge
density as seen by future-directed observers held fixed, the flip sends them to −F
and −J and invariance is a real condition. The two flips differ by charge
conjugation. The same choice appears in quantum theory. Hollands and Wald's flip
keeps the local field content and conjugates charges relative to the new future. So:

- If the content of a world is its tensor content, and "positive charge moving
  forward" and "negative charge moving backward" are two descriptions of one thing,
  the class is closed and Proposition 2′ gives no lawful arrow. This is the view
  Roberts attributes to Feynman and to Arntzenius and Greaves.
- If which things are matter is a primitive fact, the flipped world differs in
  content, Proposition 2′ is silent, and the violation of T in the weak interaction
  fixes the time orientation relative to that fact.

The laws fix the product of the time orientation and the matter label and neither
factor alone. Roberts, who holds that T violation shows time itself to be asymmetric,
concedes this much to Price: an orientation is required, "although it may not matter
which one we choose", and calling the kaon process future-directed for one orientation
or its conjugate future-directed for the other "really is a descriptive redundancy".

## What is already in the literature

- The theorems: Jost; Greaves and Thomas; Hollands (2004) and Hollands and Wald
  (2008). The curved-spacetime formulation as a relation between the two time
  orientations of one spacetime is theirs.
- Time reversal as the flip of a temporal orientation, valid in curved spacetime:
  Malament (2004).
- That a lawlike T asymmetry yields a convention for labelling the two directions and
  not an objective orientation: Price, quoted by Roberts. Roberts's reply and his
  concession are in his §7.4.2.
- That CPT is, or is not, the operation that deserves the name time reversal:
  Arntzenius and Greaves, Wallace, and against them Roberts, ch. 8.

What this note adds is only the fitting of these to Proposition 2: which map the
proposition needs, which theorem supplies it, and which premise is not physics. I did
not find the combination stated, and I did not search hard enough to say it is absent.

## Limits

- Proposition 2 is proved for germs of spacetimes. The project has no definition of a
  local clock on quantum states. Proposition 2′ assumes one in which the flipped germ
  is the same germ with the conjugate state. That is a schema, not a theorem of the
  project.
- A quantity monotone along every timelike curve in every state of a quantum field
  theory is unlikely to exist for reasons unrelated to CPT. The proposition has bite
  only on restricted classes of states, and closure of a restricted class under the
  flip is then a further assumption. Hollands and Wald's expanding and contracting
  universes show how it fails.
- Hollands and Wald's theorem is about their operator-product framework. Whether the
  Standard Model on a curved background satisfies their axioms is not established
  here. Their state space is defined by them; I did not check how positivity enters.
- Jost and Streater–Wightman were not read. Their content is taken from four papers
  that state it consistently.
- Greaves (2010), Arntzenius and Greaves (2009), Price, Earman, Albert and Swanson
  were not read. What is said of them comes from Roberts, Malament or search records
  and is marked so in the source file.
- Collapse theories, hidden-variable theories and quantum gravity are outside every
  row of the table.
- The viscous-fluid example is my own elementary calculation, not checked by anyone
  else. No script accompanies this note; nothing here is numerical.

## Requested change to the settling note

Replace the paragraph beginning "So a lawful arrow needs" by the corrected sentence
above with its three alternatives, and move "a failure of locality or of Lorentz
invariance" to an example of the second alternative. The summary line "every route to
a primitive present or arrow runs through physics of a kind that current theories
exclude by symmetry" should carry the condition of reason 5.
