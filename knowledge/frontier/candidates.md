# Bounded candidate contracts

Screened records: 15 in `sources.jsonl`. These are follow-up targets, not novelty findings. Deepest source review in this lane is abstract-level; no candidate has passed a novelty gate.

## Comparison contract by lineage

| Lineage and anchor | Time and state structure | Clock / causal assumptions | Observable or mathematical output | Ontological reach and current gap |
|---|---|---|---|---|
| Causal sets: sequential growth (1999), becoming (2015), embedding uniqueness (2026) | Locally finite partial orders; growth models add stochastic birth histories, while an embedding theorem concerns maps from order to Lorentzian geometry. | Growth dynamics and covariance conditions are model premises; embedding uniqueness requires a “well-conditioned” embedding (exact conditions not yet extracted). | Growth probabilities/invariants or uniqueness of geometric reconstruction, depending on model. | A birth order or unique embedding does not establish objective passage. Need compare observables/records across growth and completed-history descriptions. Exact theorem claims remain abstract-level. |
| Relational quantum clocks: Trinity (2019v3), relativistic Trinity (2020v1), Page–Wootters measurement (2023), spacetime QRF (2021), relational Markovianity (2026) | Global constrained/correlated state with conditional subsystem descriptions; finite-resolution and non-ideal clocks are already in the predecessor lineage. | Clock POVM, allowed clock state/dynamics, frequency sector, interaction, and conditioning procedure matter. Trinity papers establish equivalence claims only for their specified classes. | Conditional state/evolution, clock-relative event probability, or effective open dynamics. | Clock choice changes a description; empirical distinguishability requires observables and access restrictions. Do not claim “non-ideal clocks” broadly as a gap. Need identify an explicit class outside trinity hypotheses. |
| Quantum reference frames and causal order: operational meaning (2026), beyond subsystems (2026), time delocalization (2026), plus spacetime QRF anchor | Frame can be quantum and possibly not a tensor factor; temporal frames can relocate event descriptions. | Transformation/invariant-subalgebra and operational-access assumptions determine what changes between frames. Distinguish frame-relative order from process-matrix indefinite causal order. | Frame-transformed observables or causal/temporal correlations. | Representation changes alone do not establish gauge symmetry or ontology. Need test whether an operational invariant distinguishes extensions, and track background time assumptions. |
| Thermal time / emergent spacetime: noncommutative Minkowski application (2025), spin-glass exploration (2025) | Flow may be state-dependent (thermal/modular) or geometry proposed to emerge from a non-gravitational model. | Requires an algebra/state pair or a specified microscopic model and emergence map; thermodynamic equilibrium and semiclassical limits may be substantive premises. | Modular flow, correlation functions, or reconstructed geometric observables. | A mathematical flow is not automatically clock time; emergent geometry is not evidence of temporal passage. This pass has no full-text checked 2026 result in this lineage. |

## At most three concrete audit targets

### 1. Well-conditioned causal-set embedding uniqueness (2607.05840v1)

- Exact question: under the paper’s definition of “well-conditioned,” what data and regularity bounds make a causal-set embedding into a Lorentzian manifold unique, and what equivalence relation (if any) remains?
- State of evidence: abstract says the authors introduce the notion and prove a uniqueness result. Read depth is abstract. No theorem wording or proof is asserted here.
- Nearest predecessors: causal-set reconstruction/faithful-embedding literature; classical sequential growth (gr-qc/9904062); philosophical becoming analysis (1502.00018). The result may be mathematically orthogonal to growth dynamics, so the latter two are interpretive/contextual rather than theorem antecedents.
- Tractable next step: obtain v1 full text, extract the theorem and definitions; implement finite poset checks for small cardinalities to search for counterexamples when conditioning bounds are relaxed. This tests examples only, not the continuum theorem.
- Novelty falsifier: an earlier theorem already gives the same uniqueness under equivalent hypotheses; or “well-conditioned” simply encodes near-isometry strongly enough to make the result a routine rigidity corollary.
- Reproduction: theorem audit plus finite examples likely feasible; proof reproduction requires checking compactness/regularity and Lorentzian distance assumptions. No implementation or proof check yet.
- Philosophical bridge: even exact reconstruction of metric geometry from order would constrain geometry recoverable from causal structure; it would not imply an evolving present, a fixed future, or a privileged becoming relation.

### 2. QRFs beyond tensor-factor subsystems (2607.24976v1)

- Exact question: which algebraic or operational conditions allow a quantum reference frame that is not a tensor factor, and how do transformations and relational observables compare with subsystem-based QRFs?
- State of evidence: abstract says the authors generalize QRFs beyond frames corresponding to tensor factors. No equations or construction read.
- Nearest predecessors: spacetime QRFs and superpositions of proper times (2101.11628); relational trinity including non-ideal clocks (1912.00033v3); operational meaning of QRFs (2607.03417v1). These cover nearby framework, clock, and interpretation issues but do not establish whether the new algebraic case is already implied.
- Tractable next step: extract the smallest finite-dimensional example and compare the transformed observable algebra and accessible probabilities with an explicit subsystem embedding, if one exists.
- Novelty falsifier: equivalent frame transformations follow from a known subsystem dilation or algebraic QRF result; or the generalization changes representation only and yields no new operationally accessible predictions under the stated access model.
- Reproduction: finite-dimensional linear algebra is a plausible route if the paper provides a finite example. Need source inspection before estimating proof complexity.
- Philosophical bridge: observer-relative state assignment is not observer-created passage. Consequences concern access and description unless a new observable prediction or physical constraint is derived.

### 3. Time delocalization across temporal QRFs (2603.08845v1)

- Exact question: when transforming between temporal QRFs, which causal/temporal relations are invariant, and when does apparent delocalization differ from a process with indefinite causal order?
- State of evidence: abstract says relational evolution comes from correlations between system and clock and addresses causality across temporal frames. March 2026, within past year but outside 90 days. No derivation read.
- Nearest predecessors: Page–Wootters measurement events (2308.10967); relativistic relational trinity (2007.00580v1); QRF/indefinite-order formulation (2211.15685v3, located in discovery search but not yet added as a screened source). Exact assumption comparison remains open.
- Tractable next step: reproduce the paper’s smallest finite clock/system state and compute frame-conditioned event probabilities and causal witnesses; vary clock resolution/coherence while holding the process fixed.
- Novelty falsifier: a previously published frame transformation already yields the same correlations, or the causal-order witness depends on an external time parameter that makes the proposed “indefinite” interpretation a coordinate-description effect only.
- Reproduction: likely finite-dimensional if examples are explicit; must not generalize a finite witness to all temporal QRFs.
- Philosophical bridge: frame-dependent event localization underdetermines whether passage is fundamental. The comparison must keep clock time, causal order, and objective becoming separate.

## Selection status

No target is recommended as a novel contribution yet. Target 1 is the clearest theorem-shaped question; target 2 is promising only if the new frame class changes operational predictions; target 3 is the sharpest route to disentangling clock-relative order from indefinite order. The next gate should be full-text extraction and backward/forward citation audit, especially of algebraic QRFs and causal-set embedding rigidity.
