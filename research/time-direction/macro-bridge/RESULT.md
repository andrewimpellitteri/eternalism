# From a symmetric micro law to a macro chance arrow

18 November 2026. Coordinator session (Claude Code, Opus 5.5). Not independently reviewed. The
model is elementary, and no priority is claimed. Check: [check_bridge.py](check_bridge.py). This is
gap 3 of the [consolidation](../consolidation/RESULT.md).

## The model

The micro state has three parts: an event bit S, a device bit D, and a ring tape of N bits, with
m = N/2. The law is U = R₂R₁, where:

- R₁ swaps D with tape[m] and reflects the tape (cell i to −i);
- R₂ swaps S with D and reflects the tape (cell i to 1−i).

Both R₁ and R₂ are involutions. So U is a bijection, and R₁UR₁ = U⁻¹: the law is exactly
time-reversal symmetric, with reversal map ε = R₁ (B0, all 1,024 states for N = 8). One step does
four things: S takes the tape bit arriving at m, D takes the old S, the old D goes onto the tape,
and the tape shifts by one cell.

## Results (exact, T = 6)

| Run | Micro ensemble | Macro (S, D) process | Production direction | Records at t = 3 |
|---|---|---|---|---|
| B1 | Uniform: stationary, no boundary, maximal entropy at every time | **Exactly the delay-line chance law** | Homogeneous in both directions: none | D records S 1.000, forecasts it 0.000 |
| B3 | Macro boundary at the start (S = D = 0) | The same law forward | Forward only; backward homogeneous after step 2 | Unchanged |
| B4 | Macro boundary at the end (S_T = D_T = 0) | — | Backward only; forward inhomogeneous from step 4 | Unchanged: D records S's earlier state |

B2: ε exchanges D with tape[m], so the reversal map does not preserve the macro labels.

## What it shows

1. **A symmetric deterministic law with no boundary at all gives a macro chance law with a record
   arrow (B1).** Its arrow is not a boundary arrow. It is not a micro-law arrow either, because the
   micro law is symmetric. It comes from the **coarse-graining**: the macro variables are not
   preserved by the micro reversal map (B2). Read backward, the role of the device is played by a
   tape cell. That is what claim 1 of the consolidation allows, because the labels are part of the
   specification.
2. **The misalignment of [chance records](../../records-asymmetry/chance/RESULT.md) R4 survives the
   bridge (B4).** In a deterministic, time-reversal-symmetric world, a macro boundary at the end
   makes production run backward while records still point to the earlier side. The consolidation
   had said that in deterministic worlds both arrows come from the boundary. That is now false:
   records can come from the coarse-graining.
3. **The general version (our inference, from secondary-depth sources).** A two-sided mixing Markov
   shift is weak Bernoulli, so it is isomorphic to a Bernoulli shift of equal entropy
   (`mb-friedman-ornstein-1970`). A Bernoulli shift with its product measure is conjugated to its
   inverse by the coordinate reflection, a measure-preserving involution. Pull that reflection back
   through the isomorphism, and **every mixing finite stationary Markov chain, viewed as a
   measure-preserving deterministic system, is time-reversal symmetric.** Its non-reversibility is
   then relative to the time-zero partition, the "present state" by which the chain is read, which
   the involution need not preserve. Werndl (`mb-werndl-2009`, discovery depth) uses the same
   machinery for the equivalence of deterministic and indeterministic descriptions. Whether she
   draws this corollary has not been checked.

## The revised source list

Within scope, the arrows have two sources, not three:

- **Boundaries:** where the measure is not invariant in time. These give amount arrows for whole
  slices and the direction of production.
- **Labels:** which variables count as which, when the dynamics is symmetric only up to a
  relabelling or a coarse-graining. These give value arrows, including the record arrow between parts.

What the consolidation called a "law arrow" is, for mixing finite Markov chains, a label arrow at
the level of the underlying deterministic system. CPT was already of this form: the laws fix the
product of time orientation and matter label. Generic causal-set growth has not been classified.

## Limits

- One micro model (N = 8, T = 6) and one coarse-graining. B4 conditions on a single final macrostate.
- The general corollary rests on Friedman–Ornstein and on facts about Bernoulli reflection known
  only from secondary reports. The isomorphism is not constructive. So it does not say which
  physical coarse-graining corresponds to the time-zero partition.
- Calling the source "labels" is a philosophical sorting. A defender of law arrows can reply that
  the physically privileged partition is fixed by the laws, so that the arrow is lawful after all.
  That is the CPT dispute again, generalized: is a partition, like a matter label, part of the
  physical content?
