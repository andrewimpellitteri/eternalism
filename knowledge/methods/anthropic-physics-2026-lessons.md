# Lessons from Anthropic's 2026 black-hole physics post

Status: methods note, 2026-11-18. Read depth: **discovery**. The source is a
public Anthropic blog post that the user pasted into a coordinator session. It
describes two preprints, which have not been read. Neither preprint's URL,
arXiv number or version was in the pasted text. Every statement about the work
below is the post's own claim. Nothing here is verified, reproduced or cited as
a result. No `sources.jsonl` record has been added, because the record needs a
primary locator that we do not have.

## 1. What the post reports (authors' claims)

- **Weak-coupling Hawking–Page transition in N=4 super Yang–Mills.** The post
  says Claude completed a three-loop calculation that Aharony and colleagues
  set up in 2003 and left unfinished. The result says whether the
  weak-coupling deconfinement transition is first order. The post reports that
  it is first order (abrupt).
- **Spinless modular bootstrap in 3D gravity.** The post says Claude found the
  exact large-c limit of the simplest Hellerman-type bound on the lightest
  black hole's mass: M₁ ≤ c/Λ with Λ ≈ 9.1266, and proved that this version of
  the bootstrap cannot do better. The method uses a spectral curve. One half of
  the proof, the optimality part, is said to follow the strategy of an OpenAI
  model's recent sphere-packing proof.

## 2. Why the physics does not bear on this project's questions

This section is our own inference, made under AGENTS.md's research standards.

- **The modular S-swap is Euclidean.** The post explains it with the argument
  that relativity puts space and time on an equal footing. But on the Euclidean
  torus, the "time" circle is inverse temperature. The modular S-transformation
  is a symmetry of the partition function: it is a representation
  transformation, not an ontological equivalence. It says nothing about
  passage, becoming or what exists. Any argument from it to a temporal ontology
  needs an extra bridge premise that has not been stated.
- **"Sum over histories" is a way of computing results.** It asserts no
  ontology of histories. Reading it as eternalist adds a premise.
- **Hawking–Page compares equilibrium saddles.** It is a dominance exchange
  between Euclidean saddles at fixed temperature. It touches neither the
  thermodynamic arrow nor how records form, so it does not feed
  `research/` work on records asymmetry.

## 3. Lessons for how this project works

These are our inferences. Each one maps a practice the post claims onto a gap
this repository already records.

1. **Independent duplicate computation.** The post says almost every piece of
   the N=4 calculation was done twice by agents working independently. Doing
   the same work twice is a different check from reviewing it once. This
   strengthens `prior-methods.md` §4 item 5: a reviewer that gets only the
   question, not the first worker's rationale, is closer to an independent
   recomputation (see `handoff-contract.md` R4).
2. **Anchoring to known results.** The post says parts of the calculation were
   compared with known results from the literature. A finite model or a
   derivation here should state up front which published special case it has
   to reproduce before its new output counts. The footprint-walker and
   record-ledger lanes are candidates for this.
3. **Agreement across different methods counts most.** The post says a
   physicist, using a different method, independently reached the same
   Hawking–Page answer. The bootstrap answer was likewise reached by more than
   one agent. The README notes that all review here so far is by one model
   family. Same-family agreement is still evidence of the kind
   `prior-methods.md` warns "is not correctness". An external solver, or a
   second derivation by a genuinely different route, is worth more than more
   rounds of same-family review.
4. **Lean is one layer.** The post says the bootstrap results were checked in
   Lean *and* a physicist checked every main result. That matches the AGENTS.md
   rule that a Lean build checks only the statement as encoded. The
   correspondence audit and human review remain separate gates (`GATES.md`).
5. **Choose problems that can be checked.** Both problems had an answer that
   could be checked against something definite: a calculation already set up
   in 2003, and a measured gap between proven and numerical bounds. Of the
   project's candidates, NOVELTY.md candidate A (where records stop being able
   to tell histories apart) has the closest shape. Before a lane starts, it
   should name the result that would count as settling its question and the
   known case that result must reproduce.
6. **Borrowing a tool from another lane.** The post says the key method came
   from an agent working on a related sphere-packing problem, and that agents
   read each other's progress posts. Cross-lane reading here should keep each
   lane's incompatible assumptions visible rather than merging them.
   NOVELTY.md requires this when synthesizing.
7. **Long runs, few results.** The post describes 22 candidate problems,
   roughly six weeks of background agents, and two solved problems. One
   earlier attempt failed in 61 parallel runs. Plan for a low success rate, and
   keep failed attempts as outputs (`prior-methods.md` §4 item 3).

## 4. Open items

- Read both preprints at abstract depth at least, record exact versions and
  locators, and add `meth-*` records to `sources.jsonl` if they are kept.
- Check whether either preprint describes its agent workflow in more detail
  than the post does: roles, how duplicates were kept independent, and the
  failure rate.
- None of this changes `GATES.md`. The main external gate is still review by
  someone outside the project, or a result reached independently by a
  different method.
