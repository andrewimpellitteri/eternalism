# Where does the direction of records come from?

*Coordinator draft, 17 November 2026. Finite reversible bit models, checked by exact enumeration in [check_records.py](check_records.py). Not independently reviewed. No priority claim: the observations are elementary and are probably known in the statistical-mechanics literature on records and counterfactuals. That literature has not yet been read for this lane.*

## The question

The [arrow audit](../ontology-reconstruction/coordinator/roadmap-audit-2026-10-31/ARROW_DISPOSITION.md) and the massive-field notes show that fixing is mirror-symmetric under a time-reversing isometry. Even so, a photograph of yesterday's rain is a trace, and a perfect forecast of tomorrow's rain is not. Take a reversible gate that flips a memory bit when a signal is 1. If the bit starts blank, its final value gives the signal. If the bit ends blank, its initial value gives the signal equally well. This lane asks what has to be added to the reversible law to make the first case a record and the second not:

- a low-entropy boundary;
- the location of correlations;
- counterfactual robustness;
- an independent causal direction.

The four results below are about these toy models only. They bound what a general account can say. They are not a general theorem.

## Models

A gadget has an event bit `S`, a device bit `D`, a coupling switch `K` and a scrambler `E`. Step 1 is the Toffoli gate `D ← D ⊕ (S∧K)`. Step 2 is `S ← S ⊕ E`, which makes the event transient: when `E` is uniform, `S` at time 2 carries no information about the event. Both gates are involutions, so the dynamics are reversible and fine-grained Shannon entropy is conserved. An ensemble is a uniform distribution over a listed set of microstates. Parts 2 and 4 use a reduced gadget `(S, D)` with the single step `D ← D ⊕ S`.

## Result 1. A global entropy profile does not say where the records are

Take two gadgets under the same dynamics.

- **Ensemble A.** Gadget 1 is blank and coupled (`D=0, K=1`). Gadget 2 is pre-correlated and uncoupled (`D′=S′, K′=0`).
- **Ensemble B** swaps these two preparations.

The two ensembles have identical values at t = 0, 1, 2 for:
- joint entropy, which is constant at 4 bits;
- the sum of single-bit marginal entropies (5, 6, 6);
- a coarse-grained Gibbs entropy over total Hamming weight.

The swap carries any coarse-graining that treats the two gadgets alike to the same profile. In both ensembles, device `D` at time 2 matches the event `S` at time 0 in every member, with mutual information 1 bit, while `S` itself has lost the information. Flip `S` at time 0, holding every other initial bit fixed: in A, `D` follows every time, and in B it never does. A's device holds a robust trace of the transient event. B's device holds an accidental match that would fail if the event had differed. A global entropy profile, however it is coarse-grained, does not locate the trace.

The Hamming-weight entropy is not monotone in this model. The claim is only that the two profiles are equal.

## Result 2. Counting microstates does not decide which way records point

Take n = 4 reduced gadgets and two initial cells of the same size, 2⁴ microstates each:

| Initial cell | Marginal entropy t0 → t1 | I(device after; event) | I(device before; event) |
|---|---|---|---|
| blank, `D=0` | 4 → 8 | 1.00 | 0.00 |
| pre-correlated, `D=S` | 8 → 4 | 0.00 | 1.00 |

Any entropy that counts microstates gives the two cells the same value. Only the blank cell produces past-directed records. The pre-correlated cell gives future-directed "pre-records", and its device ends blank. What separates the two is where the low entropy resides. In the blank cell, the low entropy sits in the device marginals and there is no correlation between device and event. In the pre-correlated cell, the same deficit sits in a correlation. A low-entropy boundary explains past-directed records only when its entropy measure is low because the parts are individually definite and uncorrelated. This makes precise the gap between being globally unusual and being locally prepared blank. In the table, the marginal-sum entropy increases exactly in the direction the records point.

## Result 3. Counterfactual robustness is symmetric until you say what is held fixed

Take one gadget and two ensembles:
- blank at t = 0, giving a forward record;
- blank at t = 2, its time reverse, giving a pre-record.

| Ensemble | Hold t=0 fixed, flip the event: late device depends / stays in cell | Hold t=2 fixed, flip the event: early device depends / stays in cell |
|---|---|---|
| blank at t=0 | 1.00 / 1.00 | 1.00 / 0.00 |
| blank at t=2 | 1.00 / 0.00 | 1.00 / 1.00 |

Counterfactual dependence holds in both directions in both ensembles, because the gate is a bijection. So "would the device still work had the signal differed?" picks out nothing until you specify the intervention. The two cases separate on one point: whether the intervention keeps the world inside the ensemble's boundary cell. With the blank-past ensemble, an intervention that holds the past fixed respects the blank boundary. One that holds the future fixed backtracks into a non-blank past. Robustness here means dependence under interventions that preserve the boundary condition. The time-reversed ensemble, held at its own boundary, certifies its pre-records by exactly the same criterion.

## Result 4. In the toy, conditioning on a low-weight cell makes records typical toward that cell

Take n = 5 reduced gadgets with the uniform measure on microstates whose total Hamming weight is at most k at one time. The table gives per-gadget mutual information, averaged over gadgets:

| k | Cell at t=0: I(D_t1;S), I(D_t0;S) | Cell at t=1: I(D_t1;S), I(D_t0;S) |
|---|---|---|
| 2 | 0.236, 0.007 | 0.007, 0.236 |
| 4 | 0.082, 0.005 | 0.005, 0.082 |
| 6 | 0.008, 0.001 | 0.001, 0.008 |

Records point toward the conditioned time, with an exact mirror. The effect vanishes at k = 0, where the event is fixed too, and when the cell is the whole space. A low-weight cell works because it is low in marginal entropy, as in Result 2. It also lowers the entropy of the event, so the informative regime is intermediate. In this toy the thermodynamic account passes its fair test: under the conditioned uniform measure, past-directed records are typical rather than exceptional. That holds only because the weight macrostate makes device blankness typical. A cell of the same size defined by `D=S` would reverse the verdict.

## Where direction enters in these models

1. **The boundary cell.** One boundary is low in marginal entropy (Results 2 and 4). Which time carries the cell is an input. The dynamics are symmetric.
2. **The held-fixed set for counterfactuals.** Robustness is decided by which boundary an intervention must respect (Result 3). If the held-fixed set is identified with the conditioned low-entropy boundary, one assumption carries both. Then no independent causal direction is needed in these models. Without that identification, holding the past fixed is a separate stipulation. That stipulation is exactly where an independent causal direction would enter.
3. **Location, not quantity.** No global entropy number locates the traces (Result 1). The explanation needs the distribution of correlations over subsystems, which is more than an entropy profile.

For the project's question: if the identification in item 2 can be defended, the everyday sense that the past is settled by traces gets an explanation that is neutral between temporal ontologies. That explanation is a boundary condition plus a matching convention for counterfactuals. The models do not show that the identification is forced.

## Limits

- The models are finite, deterministic bit models with hand-chosen gates. There is no mixing, no macroscopic number of degrees of freedom, and no spacetime structure.
- "Entropy" here means Shannon entropy of explicit ensembles plus two named coarse-grainings. These are not Boltzmann entropies of a physical macrostate partition.
- The event is a single bit. Reliability is mutual information, with no noise model and no cost of operation.
- Result 4 uses one cell family, total Hamming weight. Its typicality verdict does not carry over to other measures.

## Next steps

1. **Read the literature.** None of these has been read for this lane, so read depth is discovery or none:
   - Mlodinow and Brun, [Phys. Rev. E 89, 052102](https://doi.org/10.1103/PhysRevE.89.052102), on robustness and fine-tuning.
   - Wolpert et al., [Memory Systems, the Epistemic Arrow of Time, and the Second Law](https://pmc.ncbi.nlm.nih.gov/articles/PMC10888154/), for its taxonomy of memory systems.
   - Albert's *Time and Chance* (2000), Elga (2001) on statistical mechanics and the asymmetry of counterfactual dependence, and Loewer on counterfactuals and the second law. These are leads from background knowledge. They are expected to state versions of item 2.

   Then position Results 1–4 against them, or retract them as known.
2. **Present-only conditioning.** Condition on the present macrostate alone, which is the Boltzmann-brain form of the typicality test. This needs a mixing reversible model with entropy growth on both sides of a fluctuation, such as a Kac ring or a reversible cellular automaton. In the present toy, a low present weight trivially implies a low past weight.
3. **Connect to the noisy-threshold theorem.** Add a preparation stage with a dissipation cost to the [noisy-record model](../horizons/noisy-past-and-future-averages.md), whose error model is time-symmetric. Ask whether the D(T)/√T threshold acquires a direction.
4. **Connect to the steering note.** The no-bypass premise of the [steering note](../agentic-philosophy/when-does-a-decision-steer.md) plays the role here of "the coupling, not a pre-existing correlation, produced the match" (Result 1, ensemble B). Check whether its four-actuator identification analysis transfers to record identification.
