# Coordinator review: bc-nonvanishing-continuation

Reviewer: coordinator, 2026-10-21. Submission by `codex-native-bc-nonzero`
(Gibbs), completed 16:08Z; claim remained `claimed` because native agents do
not pass through the OpenCode runner. Outputs inspected in
`research/longshots/bc-nonzero/`.

## Verdict

**Accept as a bounded existence result.** For the fixed BCPH level-2 data and
the stage-3 phase seed `(3+4i)/40, (3+4i)/40, 1/8` on `cp`, there is an exact
continuation in which every transition through the 3-to-4 step is nonzero,
MSR holds at every parent of size 1-3, all 109 scalar product-BC equations
hold, and norm-GC holds at stages 2, 3 and 4. The `cp`-plus-top stage-4
holonomy remains `(3-4i)/5`.

This answers the fixed-seed question: Bell causality, MSR and norm-only GC do
**not** force the displayed phase to disappear once zero amplitudes are
removed. It is not a classification and not a general phase no-go.

## Independent check

`coordinator_check.py` (this directory) re-derives the construction from
scratch: its own bit-mask poset enumeration, its own canonicalization, the
BCPH level-1/2 amplitudes entered directly from the birth-order report, and
the Bell/MSR parametrization re-derived rather than imported. It shares no
code with `nonzero_continuation.py` or the seed module.

Result (exact Gaussian rationals, exit 0):

- 49 transitions through the 3-to-4 step, all nonzero;
- MSR at every parent of sizes 1-3;
- 109 product-BC equations, all passing;
- norm-GC at stages 2, 3, 4;
- stage-3 `cp` path values exactly `(3+4i)/40, (3+4i)/40, 1/8`, so the
  phase seed is preserved;
- stage-4 norm system: 24 rows, rank 8, pivots `[0,1,2,3,4,5,8,9]`, i.e.
  `x_0=...=x_6` and `y_1=y_2=y_4`;
- `cp`-plus-top amplitudes `(-23-4i)/40, (-23-4i)/40, (-17+16i)/40`, common
  squared norm `109/320`, holonomy `1,1,(3-4i)/5`;
- the residual common-`q` family was rebuilt for `q = 2, 1+i, 1/2, -2+i`;
  each satisfies MSR, BC, nonzero amplitudes, stage-4 norm-GC and the same
  holonomy.

The worker's own run was rerun and its `check-output.txt` reproduced
byte-identically. The read-only seed file hash is unchanged
(`8c4b62ca...9f1f9`, matching the earlier report).

## Scope accepted

- Scalar complex transition amplitudes with the cross-multiplied product-BC
  rule used in the `bc-holonomy` lane; not classical probability BC and not
  operator-valued QBC (TOBC/NTOBC/CPOBC).
- The single fixed BCPH stage-3 phase seed; no claim for arbitrary stage-3
  phase families or other initial data.
- Bounded finite system through stage 4; no stage-5 BC, no extension to the
  infinite causet, no decoherence-functional or sigma-algebra claim.
- No temporal-ontology, novelty or priority claim.

## Limitations recorded (not grounds for rejection)

1. The 14-variable norm system is a projection onto squared moduli. It is an
   exact projection of the stage-4 norm equations for this ansatz (all
   level-3 gregarious amplitudes enter as `x_i`, full-precursor norms as
   `y_i`), but it does not classify all complex solutions. The load-bearing
   norm-GC verification is the direct comparison of `psi` over all 40
   labelled 4-causets, which the independent check repeats.
2. The report's phrase "counterexample to the proposed fixed-seed no-go"
   should be read strictly: the earlier lane left the nonzero extension open;
   this submission supplies a witness, not a refutation of a published
   theorem.
3. Source locators (Rideout-Sorkin Sec. 3; Varadarajan-Rideout Sec. II.3;
   Srivastava-Surya Secs. 3.1-3.2) were audited in the preceding
   `bc-holonomy` lane. This review did not re-read the primaries.
