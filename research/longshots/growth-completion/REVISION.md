# Revision record: Prop. 5 and Theorem A(C3)

Date: 2026-10-21. Corrects the principal-singleton covtree identification in
`REPORT.md`. Historical text is preserved in `ERRATUM.md`; this file records
the revised statements and the checks.

## What changed

- **Prop. 5** no longer claims `D'_H = N_{H}`. The correct identity is
  `N_{H} = D'_{H^-}`, where `H^-` is `H` with its top removed. The stage-m
  value of `N_H` is
  `N(H)A_p(H) prod_{j=1}^{m-n}(1 - q^j(1-p^k))`, `k=#max(H^-)`.
- **Theorem A(C3)** keeps the `D'_H` amplitude formula
  `N(H)A_p(H)(q;q)_{m-n}` and the non-extension conclusion, but no longer
  identifies `D'_H` with the covtree node `N_H`.
- **Escape E3** now says the principal-node values are the corrected product,
  not the `D'_H` values; the qualitative covtree discussion survives.

## Evidence

`research/longshots/review/gc_review.py` independently enumerates labelled
causets and checks, at `p=0.8+0.3i`, every principal shape and `m` from `n` to
7:

- the enumerated `N_H` matches the corrected product to rounding error;
- the enumerated `D'_H` matches the original post-tail formula;
- `N_{chain2}` equals the `D'_{pt}` values and `N_{chain3}` equals the
  `D'_{chain2}` values, confirming the index shift;
- the explicit infinite counterexample `{a<b, a<c}` plus an infinite chain
  above `b,c` is in `N_{chain2}` but not in `D'_{chain2}`.

The review and erratum are `research/longshots/review/REVIEW.md` and
`ERRATUM.md`.

## Downstream audit

- `regularized-measure/REPORT.md` Lemma 2 and Theorem 2 use `D'_H`, not `N_H`;
  they are unaffected (finite equivalence checked on 47,022 cases).
- `research/paper-novel/main.tex` uses `D'_H` for the conditional covariant
  theorem; no use of `N_H`.
- `research/conclusions/SYNTHESIS.md` records the corrected identity.
- `research/longshots/covtree-complex/RESULT.md` extends the interior
  existence to all levels via the skeleton chain; it does not rely on the
  false equality.

## Limits

The finite checks are numerical; the structural counterexample is exact. The
infinite covtree-node equivalence is argued structurally, not formalised.
This revision does not reopen the accepted variation bound or the
non-extension conclusion.
