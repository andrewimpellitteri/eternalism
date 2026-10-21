# Agent report: bc-holonomy-stage4

## Files changed

- `research/longshots/bc-holonomy/stage4_countermodel.py` — standalone exact
  audit script; imports `birth_order_interference.py` without modifying it.
- `research/longshots/bc-holonomy/check-output.txt` — reproducible exact run.
- `research/longshots/bc-holonomy/REPORT.md` — model, full finite constraint
  system, exact witness, primary-source audit, limits, and interpretation.

## Evidence and checks

- Executed the script with Python 3 and standard library only; it ends with
  `CERTIFICATE: PASS`.
- Exact Gaussian-rational checks: MSR all nodes through parent size 4; all
  product-BC equations for every precursor pair through parent size 4 (1619
  equations cumulative); norm-GC for all generated natural labelings through
  stage 5 (357 labeled stage-5 causets).
- Confirmed a `cp` stage-3 and stage-4 class holonomy `(3-4i)/5` relative to
  the chosen canonical first labeling, with equal path norms squared `1/64`.
- Read relevant sections of the primary Rideout–Sorkin, Varadarajan–Rideout,
  Dowker–Johnston–Surya, Surya–Zalel, and Srivastava–Surya sources at the depths
  recorded in `REPORT.md`.

## Limitations and unresolved questions

- The stage-4 continuation uses zero amplitudes and the explicitly stated
  bilinear product-BC extension. A ratio-only rule without a zero convention
  does not cover it; no claim is made that this is the unique quantum
  zero-amplitude convention.
- This exhibits one solution, not the complete solution variety. No
  nonvanishing-amplitude stage-4 holonomy witness or no-go was established.
- Stage 5 is checked only for this continuation. No novelty or temporal
  ontology conclusion is claimed.
