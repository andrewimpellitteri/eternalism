# Erratum: covtree node `N_H` is not the post tail `D'_H`

Date: 2026-10-21. Found by the independent residual review in
`research/longshots/review/REVIEW.md`; reproduce with
`python3 research/longshots/review/gc_review.py`.

Proposition 5 and Theorem A(C3) identify the principal-singleton covtree node
`N_{H}` (causets whose only `n`-stem is `H`) with the post-tail event `D'_H`.
The identification is false. The correct relation is

```
N_{H} = D'_{H^-},
```

where `H^-` is `H` with its top removed. The stage-value formula for `N_H` is

```
N(H) A_p(H) prod_{j=1}^{m-n} (1 - q^j (1 - p^k)),
k = #max(H^-),
```

not `N(H) A_p(H) (q;q)_{m-n}`. The latter is the correct formula for `D'_H`.

Counterexample: `{a<b, a<c}` followed by an infinite chain above `b` and `c`
has two-stem set exactly `{chain2}` but is not a post tail of the two-chain.
At `p = 0.8+0.3i`, `N_{pt} = 1` while the reported formula gives
`(q;q)_{m-1}`; the independent enumeration matches the corrected product.

What is unaffected: the `D'_H` amplitude formula, regularized-measure Lemma 2
and Theorem 2 (which use `D'_H`), the paper's covariant theorem, and the
variation-divergence conclusion. What changes: the covtree-node amplitude
display and any statement equating the stage-limit covtree walk's principal
nodes with `D'_H`. The qualitative covtree discussion survives with the
corrected node values.
