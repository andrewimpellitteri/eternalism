# RC-2 reread: premise dependency for definable definiteness and simultaneity

Coordinator reread, 2026-10-20, during `rt-loadbearing-rereads-rc`. Primary
text read: Clifton and Hogarth, *The definability of objective becoming in
Minkowski spacetime*, Synthese 103:355–387 (1995), from the user-supplied scan
in `knowledge/putnam-ablation/primary/clifton-hogarth-1995.pdf` (OCR layer,
printed pagination checked). Lane input: `kb-putnam-ablation-prior`. Not a
novelty claim.

## Verdict: SHRINK

Remaining case, in one sentence: *a finite, machine-checked premise-necessity
and non-interchangeability table for the Stein/Malament relations, with an
explicit countermodel for each dropped premise and the bridge-premise separation
made explicit; the uniqueness theorem itself is not new.*

The mathematical core of deliverable (1) is substantially pre-empted by
Clifton–Hogarth. What remains is the per-premise necessity table and a
certificate, not the characterization.

## Re-read passages (verbatim, coordinator-checked)

| Locator | Passage | Bearing |
|---|---|---|
| p.359 | `(R^4, η, T)` time-oriented Minkowski spacetime | fixed setting |
| p.361 | definability is "implicitly definable"; "R must be preserved under any φ"; "its corresponding map R must commute with any φ under composition" | the theorem's "definable" is automorphism-invariance, not first-order definability |
| p.362 | causal becoming `J⁻ ⊆ B` is Stein's stipulation; the authors "first justify `I⁻ ⊆ B`" | CH use the weaker chronological premise |
| p.363 | worldline becoming: `I⁻(b) ∩ λ ⊆ B_λ(b)`; worldline transitivity | the two worldline premises |
| p.364 | LEMMA: worldline becoming + worldline transitivity ⇒ chronological becoming | justifies `I⁻ ⊆ B`; no necessity claim for either premise |
| p.365 | THEOREM 1: definable + transitive + chronological becoming ⇒ `B` is `I⁻`, `J⁻` or `U` | the trichotomy; no `J⁻` premise |
| p.367 | COROLLARY 1(A): without time-orientation only `U` survives; COROLLARY 1(B): metrically definable iff causally definable | two necessity/equivalence corollaries |
| pp.371–372 | THEOREM 2: the same trichotomy for every `B_λ` under worldline becoming, worldline transitivity and definability from `η, T, λ` | worldline extension |
| p.376 | COROLLARY 2: reflexive `{R_λ}` with worldline transitivity are each definable from `η,T,λ` iff they define an absolute `R` definable from `η,T`; Malament Prop. 3 application | blocks worldline-dependent absolute simultaneity unless worldline transitivity is violated |
| pp.376–380 | privileged-worldline counterexamples (parallel inertial family with standard simultaneity planes; single noninertial worldline with past null cones); Peacock; Muller | independence evidence for the "no privileged worldlines" condition only |

## What this kills or shrinks

1. **The Stein characterization is published.** CH Theorem 1 is a
   context-preserving uniqueness result with definability, transitivity and
   `I⁻ ⊆ B`. The project's proposed "invariant + reflexive + transitive +
   contains the full causal past + unsettled condition ⇒ causal past" is a
   different presentation, but its mathematical content is not new. The
   contract should not claim a new characterization theorem.
2. **One premise's necessity is proved, one is not.** CH prove that
   time-orientation is needed (Cor. 1(A)) and give countermodels when privileged
   worldlines are allowed. They do **not** prove that transitivity or
   worldline transitivity is necessary, and they explicitly treat causal vs
   chronological inclusion as a motivated weakening (pp.362–365), not an
   ablation.
3. **The contract's `J⁻` inclusion is Stein's stronger premise, not CH's.**
   Any table must distinguish `I⁻ ⊆ B` from `J⁻ ⊆ B`; conflating them changes
   the theorem.
4. **The non-interchangeability part (deliverable 2) is still occupied.**
   Malament 1977's Proposition 3 and CH's Corollary 2 are the relevant
   no-go results; the project should not restate them as new.

## Disagreements with the underlying lanes (unresolved)

1. `kb-putnam-ablation-prior`'s earlier record (before the primary scan) knew
   CH's theorems only through Savitt. The primary confirms Savitt's list of
   candidates (`I⁻`, `J⁻`, `U`) and CH's chronological premise.
2. Thyssen 2023 fn51 says chronological inclusion would reduce CH's theorem to
   `I⁻` alone. False against p.365: `J⁻` and `U` remain. Recorded in the lane's
   source record.
3. Saunders 2000 p.3 says CH proved "no transitive worldline-dependent
   relation could be defined". Too strong: CH Theorem 2 leaves `I⁻`, `J⁻`, `U`
   (per worldline), and Corollary 2 only blocks recovering an absolute relation
   without violating worldline transitivity.
4. The crosswalk's "Clifton-Hogarth, whose adequacy conditions must be read
   first" is now satisfied; the adequacy conditions are not the contract's five
   premises, so the crosswalk's "very likely an easy lemma" estimate stands but
   the lemma is CH's, not ours.

## Claim-contract draft (NOVELTY.md gate)

- **Question.** Over a finite first-order Minkowski fragment (or `n ≤ 6`-point
  causal set), which premise subsets force `R = I⁻`, which force `R = J⁻`, and
  which admit `R = U` or a non-universal alternative; for each premise, exhibit
  a countermodel when it is dropped; and prove that the definiteness and
  simultaneity premise sets are non-interchangeable.
- **Nearest predecessors.**
  1. Clifton–Hogarth 1995: uniqueness/trichotomy under implicit definability,
     transitivity and chronological becoming; countermodels for
     time-orientation and privileged worldlines (read in full).
  2. Stein 1991: causal-past characterization; the repository's OCR theorem
     statement is false as isolated, with two countermodels already in
     `knowledge/checks/correspondence-cases.jsonl`.
  3. Malament 1977 (via Sarkar–Stachel and the project's secondary): uniqueness
     of Einstein synchrony under definability/invariance; Proposition 3 blocks
     nontrivial causally definable equivalence relations.
- **Delta.** A premise-by-premise necessity table plus finite enumeration
  certificate and an explicit bridge-premise column. Mathematical content is
  likely elementary and partly CH's; the contribution is formalization and the
  separation of physical from bridge premises.
- **Smallest example.** Enumerate all relations on a 5- or 6-point finite
  Minkowski fragment; verify CH's two countermodel families and the two
  existing Stein countermodels; emit a machine-checked certificate for the
  finite statement.
- **Falsifier.** Besnard 2012 or the Andréka et al. axiomatic-relativity
  literature already states the necessity table; CH's conditions already imply
  every entry; an existing Isabelle/Lean formalization of Stein's argument.
  Read Besnard and Andréka at full text before writing the contract.
- **Novelty kind.** Formalization and bridge-premise separation (reusable
  missing foundation). Not new mathematics, not new physics, no ontological
  consequence without the bridge premises. Not called novel or open.

## What remains unread

Callender 2000 (No Go proof), Bigaj 2008 (openness relation), Stein 1991
printed pages, Malament 1977 primary, Besnard 2012 full text, Andréka et al.
full text. The first two are the most likely to contain the necessity result
that would retire this remainder.
