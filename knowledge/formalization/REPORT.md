# Formalization prior-work report

Date: 2026-10-19  
Scope: first-pass public-source audit of candidate formalization substrates for finite quantum clocks and assumption-sensitive relativity.

## Findings

The most directly relevant existing formal work is the Isabelle/HOL formalization of Schutz's axioms for Minkowski spacetime. Its paper reports formalized temporal-order results and makes important assumption boundaries explicit: symmetry is encoded with pointwise invariance on a path, a stronger reading than a possible setwise interpretation; path density is segregated into a separate locale for a density-dependent result; and some Schutz continuity results are omitted. These are useful patterns for an assumption atlas, not evidence for a metaphysical conclusion. The paper's own caveats also make source-to-paper correspondence an essential audit step.

Stannett and Németi provide earlier Isabelle work on first-order relativity and report a checked theorem excluding superluminal travel by inertial observers under their axiom system. This makes “formalize special relativity in Lean” alone weak as a contribution. The precise axioms must be recovered from code before theorem reuse or a novelty comparison.

Physlib is the obvious current Lean umbrella to inspect next. Its public README says it merged PhysLean and Lean-QuantumInfo and keeps `Physlib` and `QuantumInfo` as essentially separate build targets. Its current tree has relativity, space/time, quantum-mechanics, and quantum-information directories. These are promising navigational clues, not proof that the exact results needed here exist. This worker did not inspect declarations, pin a commit, build, or audit axioms.

AxQM is a finite-dimensional quantum-information proof-synthesis benchmark with a public task library and forked Mathlib, according to its README and paper abstract. The public `main` branch leaves task statements with `sorry`; solution proofs are private, and the README instructs users to select one of two benchmark branches. It may offer useful formal vocabulary for finite-dimensional clocks, but it is not evidence of a ready-made clock formalization. Any use needs branch pinning and inspection of definitions, dependencies, and axioms.

## Reusable-results table

| Prior work | Published/README claim | Inspected code result | Current reuse confidence |
|---|---|---|---|
| Isabelle/HOL Schutz axioms | Paper reports temporal-order and geometric results; assumption variants are discussed explicitly. | None; paper full-text only. | Strong precedent, no reusable declaration yet. |
| Stannett–Németi Isabelle relativity | Paper reports proof of no superluminal inertial observers in first-order relativity. | None; paper full-text only. | Strong prior-art baseline, no reusable declaration yet. |
| Physlib | README describes combined Lean physics and quantum-information libraries; tree includes relativity and quantum topics. | Directory index only, no source declarations. | Candidate dependency only. |
| AxQM | README/paper describes finite-dimensional quantum proof tasks and grading protocol. | Repository README only; tasks and code not inspected. | Candidate for vocabulary/benchmarks only. |

## Minimal missing foundations

For a quantum-clock comparison, the minimal target is not an entire ontology formalization. It is a precisely stated finite model: clock and system state spaces, the specified joint dynamics or constraint, the relational conditioning/observable, and the transformation connecting the two descriptions. One exact ideal-clock theorem from the relational-trinity paper should be transcribed with all finite-dimensional and clock assumptions before varying any single feature. A meaningful extension would compare operational predictions under an explicitly changed interaction, resolution, or observer-access condition. “Non-ideal clocks” at large is already occupied by the trinity prior art listed in the shared seed.

For assumption-sensitive relativity, the minimal foundation is a named first-order signature and a set of independently selectable physical axioms. State the target theorem in one minimal locale; produce bounded countermodels after axiom removal only as leads, then seek general proofs or model-theoretic certificates. If the question concerns ontology, add a distinct bridge premise; do not define “present” or “existence” so that the desired ontology is built into the formalization.

## Risks and limits

No project was cloned, installed, or built. No code result is represented here as code-audited. Physlib/AxQM current branch identifiers remain mutable and must be pinned. A successful Lean or Isabelle check would establish only the encoded theorem under its dependency closure. For each proposed result, review the complete transitive axioms/admissions and dependencies, and independently map every formal definition and theorem premise to the cited paper or physical model. Neither a proof assistant nor finite model search by itself validates the physics or entails presentism, eternalism, objective passage, determinism, or a thermodynamic arrow.

## Sources

See `sources.jsonl` for per-source read depth, exact locators where available, assumptions, proof status, dependencies, and open questions. The shared seed records additional mathematical and quantum-clock leads; this lane has not completed their theorem-level audit.
