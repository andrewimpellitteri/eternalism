# Agent report: bc-nonvanishing-continuation

## Files changed

- `research/longshots/bc-nonzero/nonzero_continuation.py` — exact bounded
  certificate and norm-constraint row reduction.
- `research/longshots/bc-nonzero/check-output.txt` — output of the exact run.
- `research/longshots/bc-nonzero/REPORT.md` — BC reduction, stage-4
  parametrization, fixed-seed witness, norm-GC equations, source assumptions,
  and scope limits.

## Evidence and checks

- Standard-library Python exact arithmetic; script ends with
  `CERTIFICATE: PASS`.
- Verified all 49 transition amplitudes through the stage-3-to-4 step are
  nonzero, MSR at each parent, all 109 product-BC equations, norm-GC at stages
  2–4, and nontrivial stage-4 `cp` holonomy `(3−4i)/5`.
- Derived the empty-precursor BC recurrence analytically and reduced the 24
  exact stage-4 norm equations to rank 8 in 14 squared-modulus variables.
- The construction uses the fixed BCPH stage-3 seed; it is not a claim about
  arbitrary seeds or operator QBC.

## Limitations and unresolved questions

- The Bell-causality equation is the complex scalar amplitude-ratio rule
  inherited from the previous lane. Classical Rideout–Sorkin BC is phrased
  for probabilities; the report distinguishes these assumptions.
- The norm-equation row reduction is a projection onto 14 squared-modulus
  variables. It does not classify all complex solutions.
- No general stage-3 phase-family theorem or operator-valued result is claimed.
