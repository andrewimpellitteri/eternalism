# Formalization prior-work report

Date: 2026-10-19  
Scope: public-source audit (second pass includes static source inspection) of candidate formalization substrates for finite quantum clocks and assumption-sensitive relativity. No code was locally built or kernel-checked.

## Findings

The most directly relevant existing formal work is the Isabelle/HOL formalization of Schutz's axioms for Minkowski spacetime. Its paper and the current AFP generated proof outline report formalized temporal-order results and make assumption boundaries explicit: symmetry is encoded with pointwise invariance on a path, a stronger reading than a possible setwise interpretation; path density is segregated into a separate locale; and the second part of Theorem 12 is omitted. The outline exposes locale statements including `MinkowskiPrimitive`, `MinkowskiSpacetime`, and `MinkowskiDense.path_dense`. These are useful patterns for an assumption atlas, not evidence for a metaphysical conclusion. The underlying Isabelle theory/session and transitive admission closure were not downloaded or audited.

Stannett and Németi provide earlier Isabelle work on first-order relativity and report a checked theorem excluding superluminal travel by inertial observers under their axiom system. This makes “formalize special relativity in Lean” alone weak as a contribution. The precise axioms must be recovered from code before theorem reuse or a novelty comparison.

Physlib is a plausible Lean foundation, and this second pass inspected actual source. At commit `67d742760382efce9419feefa348902aab797a07`, `MState d` represents positive trace-one Hermitian matrices over a finite index type. The current-master `POVM` source defines finite-outcome POVMs, measurement probabilities, and a measurement channel whose classical marginal is proved equal to the measured distribution. Current-master `MinkowskiMatrix.lean` defines `diag(1,-1,…,-1)` and Minkowski-dual algebra; it expressly defers the Lorentz-group characterization. `SpeedOfLight` is only a positive real parameter. Static inspection only: no build, no exact common SHA for every current-master file, and no axiom closure audit.

AxQM is a finite-dimensional quantum-information proof-synthesis benchmark with a public task library and forked Mathlib, according to its README and paper abstract. The public `main` branch leaves task statements with `sorry`; solution proofs are private, and the README instructs users to select one of two benchmark branches. It may offer useful formal vocabulary for finite-dimensional clocks, but it is not evidence of a ready-made clock formalization. Any use needs branch pinning and inspection of definitions, dependencies, and axioms.

## Reusable-results table

| Prior work | Published/README claim | Inspected code result | Current reuse confidence |
|---|---|---|---|
| Isabelle/HOL Schutz axioms / AFP | Paper reports temporal-order and geometric results; AFP lists BSD license and session. | Current generated outline exposes locale premises; theory/session source not retrieved or built. | Strong precedent for path/betweenness assumption structure; not clock semantics. |
| Stannett–Németi Isabelle relativity | Paper reports proof of no superluminal inertial observers in first-order relativity. | None; paper full-text only. | Strong prior-art baseline, no reusable declaration yet. |
| Physlib | README describes combined Lean physics and quantum-information libraries. | Static source inspection of `MState`, POVM measurement/channel, Minkowski matrix/dual, and speed-of-light parameter. One exact commit pinned for `MState`; other files viewed at mutable `master`. No build. | Useful finite-matrix/probability substrate; no clock conditioning/equivalence or complete observer/causal structure identified. |
| AxQM | README/paper describes finite-dimensional quantum proof tasks and grading protocol. | Repository README only; tasks and code not inspected. | Candidate for vocabulary/benchmarks only. |

## Minimal missing foundations

For a quantum-clock comparison, the minimal target is a precisely stated model: clock and system state spaces, joint dynamics or constraint, relational conditioning/observable, and the map connecting descriptions. The inspected `MState`/`POVM` declarations can represent finite states and finite-resolution readout, but not the ideal real-line clock assumptions automatically. Exact finite-dimensional matrix CCR is impossible by trace cyclicity: `tr([T,H])=0`, but `tr(iℏI)=iℏ·dim(H)≠0` for nonzero ℏ. This excludes that exact algebra only, not periodic finite clocks or finite POVM clocks. A finite model extends a published theorem only after showing its hypotheses and observables survive discretization. “Non-ideal clocks” broadly is already occupied by trinity prior art in the shared seed.

For assumption-sensitive relativity, the minimal foundation is a named first-order signature and a set of independently selectable physical axioms. State the target theorem in one minimal locale; produce bounded countermodels after axiom removal only as leads, then seek general proofs or model-theoretic certificates. If the question concerns ontology, add a distinct bridge premise; do not define “present” or “existence” so that the desired ontology is built into the formalization.

## Risks and limits

No project was cloned, installed, or built. Static code reads are explicitly marked `code-audited` in `sources.jsonl`, with no implication of build or kernel replay. Physlib `MState` is pinned to an exact commit; POVM and MinkowskiMatrix remain mutable-master views. A successful Lean or Isabelle check would establish only the encoded theorem under its dependency closure. For each proposed result, review the complete transitive axioms/admissions and dependencies, and independently map every formal definition and theorem premise to the cited paper or physical model. Neither a proof assistant nor finite model search by itself validates the physics or entails presentism, eternalism, objective passage, determinism, or a thermodynamic arrow.

## Sources

See `sources.jsonl` and `code-audit.md` for source depth, declaration names and locators, assumptions, version pins, proof status, dependencies, and open questions. The minimum finite-clock substrate is Physlib's finite density-matrix and POVM definitions, conditional on a target theorem whose assumptions survive discretization. Python or SMT is faster for initial finite exploration until the model stabilizes. Quantum-clock paper hypotheses still need theorem-level transcription before formalization.
