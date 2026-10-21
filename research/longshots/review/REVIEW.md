# Residual longshot review: covtree nodes versus post tails

Reviewer: coordinator reconstruction from `gc_review.py`, 2026-10-21. This
file replaces the report the original review run did not write. It reviews
`research/longshots/growth-completion/REPORT.md` Proposition 5 / Theorem A(C3)
and `research/longshots/regularized-measure/REPORT.md` Lemma 2 / Theorem 2.
The computations are an independent reimplementation from the definitions;
they do not import either reviewed script.

Reproduce: `python3 research/longshots/review/gc_review.py
research/longshots/review/gc_review_output.txt`.

## Verdict

**One accepted identification is false; the downstream non-extension
conclusions survive.**

- Growth-completion Prop. 5 states that for principal `H` with top `t`, the
  covtree node `N_{H}` (the set of infinite causets whose only `n`-stem is
  `H`) equals the post-tail event `D'_H`, and therefore has stage values
  `N(H) A_p(H) (q;q)_{m-n}`.
- That equality is false. The correct identity is
  `N_{H} = D'_{H^-}`, where `H^-` is `H` with its top removed. The stage-value
  formula for `N_H` is
  `N(H) A_p(H) prod_{j=1}^{m-n} (1 - q^j (1 - p^k))`, with
  `k = #max(H^-)`; equivalently it is the post-tail formula for `H^-`.
- The `D'_H` amplitude formula `N(H) A_p(H) (q;q)_{m-n}` itself is correct.
  Regularized-measure Lemma 2 and Theorem 2 use `D'_H`, not `N_H`, so their
  variation obstruction is not affected. The paper's covariant theorem also
  uses `D'_H` and is not affected.

## Explicit counterexample

Let `C` be `{a < b, a < c}` followed by an infinite chain above both `b` and
`c`. Its two-element down-sets are `{a,b}` and `{a,c}`, both isomorphic to the
two-chain. Hence the two-stem set of `C` is exactly `{chain2}`, so
`C` belongs to the covtree node `N_{chain2}`. But `b` and `c` are incomparable,
so no single top `t` of the chosen copy of `chain2` lies below every element
outside it. Thus `C` is not in the post-tail `D'_{chain2}`.

The same mechanism appears at level 1: `N_{pt} = Omega` has value `1` at every
stage, while the report's formula gives `(q;q)_{m-1}`, which tends to
`(q;q)_infty != 1`.

## Exact stage checks

At `p = 0.8 + 0.3i` (`q = 0.2 - 0.3i`), the independent enumeration gives:

| `H` | `m` | `N_H` value | `N(H)A_p(H)(q;q)_{m-n}` | corrected formula |
|---|---:|---|---|---|
| pt | 7 | `1` | `0.852650+0.425104i` | `1` |
| chain2 | 3 | `0.804000+0.411000i` | `0.550000+0.480000i` | `0.804000+0.411000i` |
| chain2 | 7 | `0.852650+0.425104i` | `0.555224+0.597554i` | `0.852650+0.425104i` |
| chain3 | 7 | `0.555224+0.597554i` | `0.261370+0.646960i` | `0.555224+0.597554i` |
| Lambda | 7 | `0.314088-0.015854i` | `0.246362+0.050981i` | `0.314088-0.015854i` |

The corrected column matches the enumerated `N_H` to rounding error in every
tested principal shape and every `m` from `n` to 7. The table also shows the
index shift: `N_{chain2}` equals the `D'_{pt}` values and `N_{chain3}` equals
the `D'_{chain2}` values.

The report's `D'_H` formula is separately correct: the post-tail sums match
`N(H) A_p(H)(q;q)_{m-n}` to rounding error in the same run.

## What survives

- Regularized-measure Lemma 2's finite equivalence `K_n(C) ~ H` iff the
  post-tail condition was checked on 47,022 labelled causets with `m <= 6`,
  `n <= 4`; zero mismatches. This is finite corroboration, not the infinite
  proof the script's comment referred to; that proof is not in the repository.
- The post-tail stage values and the common factor `(q;q)_infty` are
  unchanged, so regularized-measure Theorem 2's total-variation divergence
  and the paper's covariant theorem remain as stated.
- Level-2 and level-3 covtree total variation computations still run; the
  level-3 total variation grows through `m = 7`. The qualitative covtree
  escape discussion survives with corrected node values, because the
  corrected `N_H = D'_{H^-}` still has a finite `|q| < 1` limit.

## What needs correction

- Growth-completion Prop. 5 and Theorem A(C3): replace `D'_H = N_{H}` with
  `N_{H} = D'_{H^-}`, and replace the `N_H` stage-value formula by the
  corrected product above. The `D'_H` amplitude formula and the non-extension
  conclusion can stay.
- Any text that treats the stage-limit covtree node `N_H` as having the
  `D'_H` values. The covtree walk exists, but its node values are shifted by
  one rank and carry the extra `(1 - p^k)` factors.

## Limits

- All checks are finite, at selected complex `p`; the infinite-causet
  equivalence is argued structurally here, not formalised.
- The script uses floating-point arithmetic; agreement at `1e-16` is
  numerical corroboration, not exact algebra. The structural counterexample
  is exact.
- This review covers the two named longshot reports only. It is not a global
  priority search and does not reopen the accepted variation bound.
