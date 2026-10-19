# Clock-carried memory under restricted clock access

**Status:** clock-memory probe: bounded exact witness, no surviving novelty
claim. Separate causal-set peer review: supports a candidate extension theorem
on a labeled algebra. Checked 2026-10-19.
**Read depth:** primary-source full text at relevant sections for Pollock et al.
and Guo; relevant sections for Baumann–Lock; project-recorded section-level
extraction for Smith–Ahmadi; abstract plus partial body for Shaari. This is not
a systematic review or a proof formalization.

## Outcome

The useful result is a small intervention witness: if two otherwise identical
two-step models place a copied classical bit either in a clock register or in
an environment register, an unsharp clock readout that also replaces the clock
state distinguishes these two *specified architectures* after a system reset.
The witness is exact for every readout sharpness, including zero sharpness,
because the state replacement itself is the operative intervention. This is a
model check, not a general source-identification theorem. The underlying logic
is a register-local causal break and is already covered in substance by
operational process and causal-model frameworks. No new physical or
mathematical result is claimed.

That no-new-result disposition applies only to the clock-memory probe in this
report. The separate causal-set addenda independently audit a candidate
nonextension theorem for the labeled doubly-reduced cylinder algebra; that
review supports the stated proof under its assumptions and does not assert a
global priority claim or extend the conclusion to the covariant intersection
algebra.

## Hypotheses considered

1. **Clock-only multi-time memory has a new dimension/Fourier signature.** A
   finite clock of dimension `d` should constrain accessible temporal data
   more strongly than a generic environment of the same size, perhaps through
   a clock-covariant Fourier/Hankel-rank bound. The generic memory bond/rank
   bound is already standard process-tensor machinery (and explicitly treated
   as memory size by Guo). Budroni, Vitagliano & Woods also already study
   finite-state classical clocks versus quantum instruments through temporal
   output sequences and memory-limited clock performance. Any proposed
   tightening would need an exact clock covariance group, spectrum/degeneracy,
   allowed interventions, and a comparison with quantum hidden-state/process
   realizations. No such tighter bound was derived here. Rejected as
   unsupported and likely a representation restatement until that work is
   done.

2. **System-only conditioned dynamics identify whether memory lives in the
   clock.** They do not. The same bit-copy process can put the latent register
   in `C` or in an inaccessible environment `E`, with identical statistics
   under the stated no-clock-access experiment. This is the standard hidden
   realization ambiguity; presenting the register relabeling as novelty would
   be an observational-equivalence tautology. Rejected.

3. **A clock-local erase can distinguish clock-only and environment-only
   memory in a chosen architecture.** This survives only as the exact bounded
   witness below. It assumes the reset operation acts on `C` alone and the
   comparator memory `E` is isolated from it. The extension of causal-break
   reasoning to a second, selected register is immediate; novelty is rejected.

4. **Covariant reset trades clock timing quality for erasure of clock-stored
   history.** A quick qubit encoding test does not yield a new tradeoff. For
   `|ψ_±⟩=(|0⟩+e^{±iφ}|1⟩)/√2`, the stored-bit trace distance is
   `D=|sin φ|`, while the off-diagonal visibility of the equally weighted
   clock state is `V=|cos φ|`, so `D²+V²=1` by direct calculation. (With the
   different pair `( |0⟩±e^{iφ}|1⟩ )/√2`, the states are orthogonal for every
   `φ`, giving `D=1` and `V=0`.) Data
   processing bounds the distinguishability after a channel; asymmetry
   monotonicity constrains covariant processing. These are standard
   distinguishability/resource statements, and “clock timing quality” needs
   a task-specific operational definition before a stronger constrained
   optimization can be posed. Killed as a novelty hypothesis at this stage.

## Exact finite witness

Let `S`, clock register `C`, and (in the comparison model only) environment
register `E` be qubits. Write `z,r,f ∈ {−1,+1}` for initial system bit, clock
readout outcome, and final system bit. Choose `z` uniformly by the initial
system instrument

`P_z(ρ) = |z⟩⟨z| Tr ρ`, where `Z|z⟩=z|z⟩`.

At the first interaction, model **Clock-memory** applies `CNOT(S→C)` to
`|z⟩_S|0⟩_C`. At the intermediate time apply the system causal-break channel
`B_S(ρ)=|+1⟩⟨+1| Tr ρ`, which discards the old system value and re-prepares
`S=|+1⟩`. At the last interaction apply `CNOT(C→S)` and measure `Z_S`.
There is no other memory register.

The only allowed clock operation at the intermediate time is the two-outcome
read-and-replace instrument

`I_r^C(ρ) = Tr(E_r ρ) |+1⟩⟨+1|`,
`E_r = (I + r η Z_C)/2`, with `0 ≤ η ≤ 1`.

This is a valid linear CP instrument: each outcome map is CP and
`Σ_r I_r(ρ)=|+1⟩⟨+1|Trρ` is trace preserving. The effect is an unsharp binary
readout; the state replacement makes the intervention a complete erase of
`C`. If no clock operation is made, both models below return `f=z` with
probability one.

The comparator **Environment-memory** replaces `C` by an inaccessible qubit
`E`: use `CNOT(S→E)` at the first interaction and `CNOT(E→S)` at the last.
`C` is independent, starts in `|+x⟩`, and is not coupled to `S` or `E`. Apply
the same `I_r^C` at the intermediate time. This makes the readout outcome
unbiased in the comparator and ensures that the only accessible clock
operation acts on `C`, not on `E`.

The exact joint probabilities following `B_S` and `I_r^C` are

| Model | `p(z,r,f)` |
|---|---|
| Clock-memory | `(1 + r η z)/4` if `f=+1`; `0` if `f=−1` |
| Environment-memory | `1/4` if `f=z`; `0` if `f≠z` |

For every `η`, both distributions normalize and have `p(r)=1/2`. The event
`z=−1, f=−1` has probability `0` in Clock-memory and `1/2` in
Environment-memory. Thus this particular clock-local read-and-replace
operation distinguishes the two architectures after the system has itself
been reset. The system causal break alone would leave the stored bit available
in either register; the extra clock replacement determines whether it
survives.

**Proof status:** direct unitary/instrument calculation, independently checked
with exact rational arithmetic for `η=0, 1/2, 1`. No external dependencies.
The probabilities are also immediate from the copied basis states:
`C=|z⟩` or `E=|z⟩` after the first CNOT; `I_r` always outputs `C=|+1⟩`; the
final controlled-NOT therefore yields `f=+1` only in Clock-memory, while the
untouched `E` yields `f=z` in Environment-memory.

This is not an autonomous ticking-clock model: `C` is a finite two-state clock
register with a stipulated imperfect readout and externally timed gates. It
does not establish a general result for Page–Wootters constraints, continuous
clocks, initial `S-E` correlations, reset error, or a laboratory reset that
also perturbs `E`.

## Closest primary predecessors and comparison

1. **Pollock et al., “Operational Markov condition for quantum processes,”**
   arXiv:1801.09811v1, §§“Quantum stochastic processes” and “Criterion for a
   quantum Markov process,” especially the causal-break definition and main
   theorem. [Primary text](https://arxiv.org/html/1801.09811v1). Full text read
   at the relevant sections. They prove that system re-preparation is a
   causal break and residual dependence on earlier controls witnesses
   process memory; their operational process tensor includes all inaccessible
   environment correlations. They do not localize surviving memory to a
   particular finite clock register. Here a second intervention targets that
   register. This is a direct application of their causal-break logic, not a
   competing Markov criterion.

2. **Guo, “Memory Complexity of Quantum Processes,”** arXiv:2203.01492v2,
   §§I and IV, especially the definition of memory size as the purified
   process tensor Schmidt rank and the minimal environment size in its OQE
   realization. [Primary text](https://arxiv.org/html/2203.01492v2). Full text
   read at those sections. This already occupies the generic finite-memory
   dimension/resource direction. The present example asks which specified
   register survives a selected local replacement, not how large a minimal
   hidden realization must be.

3. **Baumann & Lock, “Time delocalization and causality across temporal
   quantum reference frames,”** arXiv:2603.08845v1, §§VI.1–VI.3 and Appendix C.
   [Primary text](https://arxiv.org/html/2603.08845v1). Relevant sections read.
   They explicitly model interventions through clock-system interaction
   terms in a Page–Wootters constraint and analyze operational causality and
   clock-relative interventions, including multiple clocks. They do not give
   the clock-versus-environment memory-erasure comparison above. Their setting
   is substantially richer; the present circuit is not a generalization of
   their result.

4. **Shaari, “Informational arrow of time in an extended two-qubit
   Page-Wootters model,”** *Physics Letters A* 577 (2026) 131456,
   DOI [10.1016/j.physleta.2026.131456](https://doi.org/10.1016/j.physleta.2026.131456).
   Abstract and partial body read. The article adds inaccessible auxiliary
   systems to a finite Page–Wootters toy model and reports dephasing/depolarizing
   noise and monotone entropy of conditioned system states. It already makes
   restricted access plus auxiliaries relevant to finite-clock dynamics, but
   the inspected material does not establish a multi-time intervention test
   for locating memory in the clock versus the auxiliary. Full proof and
   intervention-scope audit remain outstanding; no gap claim follows from
   that limited inspection.

5. **Smith & Ahmadi, “Quantizing time: Interacting clocks and systems,”**
   arXiv:1712.00081v3, clock-conditioned system dynamics and interaction-kernel
   equation. [Primary text](https://arxiv.org/abs/1712.00081v3); project
   `knowledge/defeat-search/fulltext-reads-clocks.md` records the relevant
   section-level extraction. This addresses interaction-induced
   time-nonlocal conditional evolution, not controlled memory-location
   discrimination by clock replacement.

6. **Budroni, Vitagliano & Woods, “Ticking-clock performance enhanced by
   nonclassical temporal correlations,”** *Physical Review Research* 3,
   033051 (2021), DOI [10.1103/PhysRevResearch.3.033051](https://doi.org/10.1103/PhysRevResearch.3.033051).
   Full text read, especially Sec. II (finite-state machines and quantum
   instruments), Sec. III, and Discussion. Their autonomous no-input discrete
   clock outputs tick/no-tick sequences; they compare classical transition
   matrices with quantum instruments under bounded memory and derive clock
   performance results. They already occupy the finite-memory temporal-clock
   correlation lane, so a generic clock rank witness would need to state a
   genuinely different intervention-access task. Their one-input/two-output
   finite-state machine observations do not by themselves give the
   clock-versus-environment erase comparison in this report.

## Six-part claim contract

1. **Question and exact result.** In the explicit two-qubit circuit above, can
   a clock-only read-and-replace instrument after a system causal break
   distinguish a copied bit stored in the clock from the same bit stored in a
   decoupled environment? **Yes:** the event `z=−1,f=−1` has probabilities
   `0` and `1/2`, respectively, for every `η∈[0,1]`.
2. **Nearest predecessors.** Pollock et al. (2018) provide the multi-time
   process and system causal-break criterion; Guo (2022) bounds/quantifies
   memory resources through purified-process memory size; Baumann & Lock
   (2026) model timed interventions relative to quantum clocks. Shaari (2026)
   is an additional restricted-access Page–Wootters precedent. Their exact
   settings and the present circuit are compared above.
3. **Difference and relevance.** The only incremental feature is that the
   intervention sequence explicitly resets one named candidate carrier of
   memory while leaving the other carrier untouched. It is useful as a
   design sanity check for an intervention protocol, but it follows ordinary
   local-channel reasoning and does not establish a general boundary.
4. **Smallest reproducible example and independent check.** Three qubits at
   most (`S,C,E`, with `E` absent in Clock-memory), two CNOTs, the stated
   linear system and clock instruments, and final `Z` measurement. Exact
   rational arithmetic verified normalization and the distinguishing event
   for `η=0,1/2,1`; the basis-state derivation establishes all `η`.
5. **Falsifier / novelty defeat.** The probability claim is falsified by any
   algebraic or implementation calculation giving a different distribution
   under the named channels. The architecture comparison ceases to diagnose
   register location if the reset couples to `E`, if `E` initially correlates
   with `C`, or if the inaccessible comparison model is allowed to change its
   clock-output channel. Novelty is defeated—and is currently rejected—by the
   fact that causal-break/process-tensor theory already gives the mechanism;
   any paper deriving the same local reset test for a quantum clock would
   further remove even the small protocol distinction. Search coverage is
   targeted, not exhaustive: no systematic forward-citation sweep or full
   audit of all 2026 finite-clock interventions was completed.
6. **Novelty kinds.** Mathematical novelty: none asserted; the calculation is
   elementary. Formalization novelty: none. Physical novelty: none; the
   clock is a controlled finite register, not an autonomous or gravitational
   clock. Philosophical consequence: none; register-local operational memory
   says nothing about temporal ontology, objective passage, or the
   thermodynamic arrow.

## Defeat-search notes

- Process tensors encode all intervention-accessible multi-time correlations;
  Pollock et al.'s operational Markov criterion already uses causal breaks.
- Generic finite memory dimension / process-tensor rank is prior art, so a
  `d_C^2` bound or its simple clock-label restatement is not selected.
- Finite-state clock instruments and memory-limited multi-time output
  correlations are already treated by Budroni, Vitagliano & Woods (2021);
  the unfinished Fourier/Hankel idea would need to beat that clock-specific
  comparison as well as generic process memory bounds.
- Quantum causal-model and instrument formalisms make interventions on
  designated nodes ordinary model changes. No separate causal-model theorem
  is claimed here.
- Clock-conditioned reduced maps or a time-convolution kernel do not identify
  where a latent memory register is located. Project audit RC-5 also warns
  against transferring linear-channel memory criteria to normalized,
  state-dependent clock-conditioned updates without first establishing
  linearity.
- A candidate coherence-versus-memory bound must outperform the elementary
  phase-encoding identity and data-processing/asymmetry bounds. No
  covariant-reset optimization was completed; none is claimed.
- Nandi & Petruccione, arXiv:2606.08595v1, remains an abstract/project
  section-level lead in the main audit; no defect or theorem-level comparison
  is inferred.

## Files, checks, limits

- **Files changed:** `research/creative/clock-memory/AGENT_REPORT.md`,
  `research/creative/clock-memory/causal-set-ordinal-module-review.md`, and
  `research/creative/clock-memory/all-nonclassical-parameters-review.md`.
- **Evidence:** for the clock probe, exact CP-instrument definitions,
  basis-state derivation, and rational normalization/distinguishing-event
  calculation above. For the finite causal-set instance, independent
  enumeration of the 40 principal five-label gadgets and their exact exponent
  multiplicities, followed by the ordinal-module seam and disjoint-cylinder
  audit. For the all-parameter causal-set argument, an analytic check that
  rooted principal-block weights partition the two-endpoint reachability
  event in an independent Bernoulli forward DAG; Harris positive association
  and the positive infinite-product bound give the lower bound needed for
  block repetition.
- **Checks:** standard-library `fractions.Fraction` calculation at
  `η=0,1/2,1`; standard-library finite relation-mask enumeration for the
  causal-set witness; direct overlap/visibility check for the corrected qubit
  state pair. The all-parameter proof was checked analytically; no extra code,
  installs, tests, large runs, or external source files were added.
- **Limitations:** the clock probe is a bounded circuit with no autonomy or
  clock Hamiltonian, reset imperfections, or initial cross-correlations; the
  recent-paper forward search is incomplete. The causal-set review concerns
  extension to the labeled doubly-reduced algebra only, with no result for the
  covariant intersection algebra and no global priority claim.
- **Unresolved:** whether clock covariance or spectral degeneracy yields a
  sharper multi-time memory-rank bound under a fixed admissible-instrument
  class; this needs a distinct mathematical statement and direct comparison
  with quantum hidden-state realizations before further work.
