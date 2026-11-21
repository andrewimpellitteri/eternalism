# Records in chance worlds

18 November 2026. Coordinator session (Claude Code, Opus 5.5). Not independently reviewed. The
models are elementary, and no priority is claimed. Check: [check_chance_records.py](check_chance_records.py).
This is gap 1 of the [consolidation](../../time-direction/consolidation/RESULT.md).

## Setting

Each world has two one-bit parts: an event S and a device D. The law is a stochastic kernel on the
four joint states. For parts X ≠ Y, define:

- **record:** I(X_t ; Y_{t−1} | Y_t), what X holds about Y's past beyond Y's present;
- **forecast:** I(X_t ; Y_{t+1} | Y_t), the same toward Y's future.

The label-free totals sum each measure over both ordered pairs. The recorder is a noisy copy: S
flips with probability a, and D takes the old S with probability c.

## Results

| Run | World | Outcome |
|---|---|---|
| R0 | Delay line, stationary (S a fresh fair bit, D ← previous S) | D records S (1 bit) and never forecasts it. S forecasts D (1 bit) and never records it. Totals 1 = 1 |
| R1 | 300 stationary random kernels | Per pair, the record–forecast asymmetry reaches 0.347 bits. The label-free totals differ by up to 0.275 bits. **No boundary is present** |
| R2 | 200 stationary reversible kernels | Every pair and every total mirrors, to 1e-15 |
| R3 | One boundary (D blank at 0), noisy-copy kernels | The blank start barely matters: D records S 0.408 bits against 0.409 in the stationary run (a = 0.1, c = 0.9, t = 3). The sign of total records minus forecasts is set by the coupling, not by the boundary. Random kernels: 666 of 1,500 windows point toward the boundary |
| R4 | End boundary: stationary noisy copy conditioned at T = 7 | The homogeneous description runs **backward** from T only. D still records S's **earlier** state (0.695 bits) and forecasts none |

## What this changes

1. **In chance worlds the record arrow is carried by the law: it is who copies whom.** Stationarity
   with a non-reversible kernel is enough. A reversible kernel gives no record arrow of any kind.
   This is unlike the deterministic lane ([RESULT](../RESULT.md), Results 1–2), where records needed
   a boundary and locally blank parts.
2. **Every copying link is counted twice.** A link from S at t−1 to D at t is a record seen from D
   and a forecast seen from S. So for pure copying, records and forecasts nearly balance once labels
   are dropped. The arrow lies in which part is the copier, which is a value arrow. In general the
   label-free totals do not balance (R1). So part-level amounts can carry a law arrow.
3. **Records and production can point opposite ways (R4).** Production direction is a boundary
   arrow: it is homogeneous only away from the boundary. The record arrow here is a law arrow. Put the
   boundary at the end, and the device records the earlier side while production runs from the end.
   In this class the alignment that the Mentaculus account needs is not automatic. It holds when the
   boundary sits on the side the law copies *from*.
4. **Ready states are not needed.** An overwriting device records whatever its prior state was. This
   agrees with Mlodinow and Brun's remark that initialization is not necessary in principle
   (`ra-mlodinow-brun-2014`). It also cuts against Albert's picture of the Past Hypothesis as the
   mother of all ready states, when the dynamics is genuinely stochastic. That picture was designed
   for deterministic dynamics (Loewer draft pp. 14–15).

The fresh-noise structure of a Markov law is itself an asymmetry: innovations are independent of the
past. That is close to Price's independence asymmetry. Here it is built into the law instead of being
assumed of initial conditions. This is a lead only; Price ch. 5–6 has not been reread for it.

## Limits

- Two one-bit parts, lag 1, horizons of 4 to 7 steps, and one record measure. A different measure,
  or many redundant traces (overdetermination), might sort differently.
- R4 is a single world with conditioning on one final state.
- "Law-carried" holds relative to the part labels. A defender of the boundary account can say that
  which part is the copier is fixed by the coarse-graining, and so by the boundary at macro level.
  That is gap 3 of the consolidation, untested.
