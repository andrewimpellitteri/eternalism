# Memory and finite-control budget for the sequential observer

24 October 2026. Resource accounting for the particular faithful full-history register and heralded circuit in `research/observer-sequential-dilation/RESULT.md`. This is a mathematical worst-case bound and an explicit sufficient precision schedule; it is not a hardware or universal observer bound, novelty claim, or temporal-ontology result.

## Full-history memory lower bound

At stage N, take the fixed labelled set [N], split it into fixed floors A and B with |A|=floor(N/2), |B|=ceil(N/2), and put every element of A below every element of B only when the corresponding selected edge is present. Put no other strict comparisons in the relation. For every subset S of A×B this is a strict partial order: there is no directed path of length two, so transitivity is vacuous; irreflexivity and asymmetry hold. Distinct S give distinct relations. Thus this explicit family contains

    2^(|A||B|) = 2^floor(N^2/4)

labelled posets. A register that faithfully assigns mutually orthogonal basis slots to every labelled N-history therefore has dimension at least this large, and requires at least floor(N²/4) qubits (ceil(log2 dimension) if padded to a power of two). This lower bound is exact for the exhibited subfamily's slot count, not an estimate of all causal sets.

The architecture restriction is essential: this argument says nothing about nonorthogonal encodings, compressed registers, quotienting labels, approximate storage, implicit oracles, or an observer that stores only a statistic. It also does not count precursor work space, herald flags, readout memory, or error-correction overhead. The accepted construction's transitions are defined over finite labelled histories; the present counting argument quantifies the full orthogonal history-register choice only.

## Channel error model and detector-gap guarantee

Let G=399999/30000000 be the strict lower bound on the ideal unconditional single-trial event/readout probability gap for the two models in the accepted result. For each model j, compare the implemented complete circuit (preparation, forward heralded growth, event instrument, inverse positive preparation, seed test, and final classical readout) with its ideal circuit as a trace-preserving channel including all failure outcomes. Let e_j be an upper bound on their diamond-norm distance. Telescoping composition and contractivity under trace-preserving channels give a final output total-variation distance at most e_j/2. Hence the implemented signed event-gap is at least

    G - (e_A+e_B)/2.

In particular, the explicit sufficient condition e_A<=G/2 and e_B<=G/2 preserves a positive gap at least G/2. The weaker aggregate condition e_A+e_B<=G also suffices. These bounds include all outcomes; postselecting and renormalizing success-only data would require a separate denominator/stability analysis and is not covered.

Here is a depth-independent, deliberately conservative allocation for each model. Set β=G/8. Allocate diamond distance at most β to each of four separately charged components: (1) initial seed preparation, (2) event test/instrument including its classical result, (3) reverse seed-acceptance test, and (4) final classical readout. For each growth stage n=3,4,... allocate to the forward controlled dilation and its reverse use separately

    ε_n = β * 2^(-(n-1)).

Since sum_{n=3}^∞ 2^(-(n-1))=1/2, the sum of these component budgets is 4β+β=5G/8 per model. Thus e_j<=5G/8 and the gap remains at least 3G/8 by the aggregate bound. Finite N uses the corresponding truncated sum. This is sufficient, not optimal. The separately stated G/2-per-model condition would retain the stronger G/2 margin.

For a coherently synthesized unitary block U replaced by U-tilde with operator norm distance δ, the induced unitary channels obey diamond distance at most 2δ (global phase may be aligned first). Therefore it suffices to choose each unitary's operator error no greater than half its allocated channel budget. For noisy/nonunitary components, budget their channel diamond distance directly. This accounts separately for initial state preparation, every controlled growth step, the event measurement instrument, each reverse block, seed projection implementation, and classical readout. If a physical event test is represented as a channel with a classical output, its error is included as one instrument component; exact event-membership computation itself is not thereby made efficient.

A fixed nonzero per-stage error ε does not provide a depth-uniform guarantee from this perturbation argument: the bound accumulates as O(mε) over m forward stages and m inverse uses and eventually exceeds any fixed gap. This is a failure of the guarantee, not a theorem that every fixed-error implementation loses the gap; correlated or canceling errors can behave better. To retain a uniform worst-case guarantee, summable per-stage errors (or an explicitly analyzed fault-tolerant scheme with a uniform whole-circuit bound) are sufficient. Failure of a nonsummable worst-case estimate alone does not establish that such schedules are necessary in every implementation. Fault tolerance does not follow from the present circuit specification.

## Exact controls, synthesis, and omitted resources

The ideal finite-dimensional construction permits exact algebraic coefficients such as square roots of finite row sums and exact unitaries extending the specified isometries. That mathematical existence statement is not a finite universal-gate compilation result. The error schedule above applies after a chosen finite synthesis/noise model supplies the stated diamond or operator-norm bounds. It gives no gate count, synthesis precision cost, fault-tolerant overhead, or bound on circuit depth.

The row sum s(C) in the predecessor circuit requires summing over actual finite precursor subsets with multiplicity. No efficient precursor oracle, arithmetic circuit, reversible comparator, or complexity bound is supplied here. Also uncharged: address generation and reversible history updates, storage/address bits beyond the history label, exact/algebraic arithmetic and coefficient loading, controlled rotations, coherent inverse access, herald ancillas, fault-tolerance, energy, locality, calibration, detector latency, and any physical mechanism for the model-dependent phase-bearing preparations. The full history memory grows at least quadratically in qubits under the stated faithful encoding; the work and precision costs can be much larger, but are not quantified.

## Evidence and status

The own bounded checker enumerates every edge subset in the stated height-two family for N<=8, verifies irreflexivity/asymmetry/transitivity, uniqueness and the exact 2^floor(N²/4) count. It uses rational arithmetic to verify the geometric allocation sum, total per-model error budget, the resulting gap margin, and linear accumulation of a fixed stage bound. These checks validate finite combinatorics and arithmetic only; the proof above establishes the general counting statement, while the channel telescope is an analytic argument not numerically simulated.

Primary source comparison: Kleitman and Rothschild's 1975 asymptotic enumeration paper studies the much broader count of partial orders and large classes of them. The present lower-bound proof does not use their asymptotic theorem; it is the direct injective construction above. Kretschmann, Schlingemann and Werner (arXiv:0710.2495v1, Section 2 Theorem 1; independently read at full-text depth) study continuity of completely positive maps and Stinespring dilations. Our error propagation is the elementary finite-circuit telescoping/measurement-contractivity bound, not their continuity theorem. Aharonov, Kitaev and Nisan (quant-ph/9806029v1, Sections 5.3–5.4, Lemmas 12–13) develop mixed-state circuits, diamond metrics and additive circuit-error bounds. They cite fault-tolerance work but do not prove the fault-tolerance threshold theorem previously attributed to them here. The exact version and source description are corrected following independent review; this observer circuit has no demonstrated fault-tolerant implementation. The formulas here are our application to the stated sequential protocol, not claims extracted from those papers.

No cost bound for general compressed observers, no physical implementation, no universal complexity lower bound, and no conclusion about temporal ontology follows.

## Integration disposition

The independent reviewer and coordinator retained the direct memory proof
and sufficient error allocation. They corrected the fault-tolerance attribution,
changed the AKN record to the inspected v1, reconciled KSW read depth, and
made the four fixed components explicit. The counting and elementary
perturbation bounds are standard ingredients applied here; no originality
claim follows.
