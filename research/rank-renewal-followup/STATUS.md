# Rank-only renewal: bounded status, not a classification

Sole-worker status, 2026-10-21. This task is closed as a **bounded failure**,
not as a theorem or a no-go. The rank-only post-value problem remains open.

## What is verified

- The stationary next-post kernel and the bridge/first-post convolution
  `b_n = sum_{k=1}^n R_k b_{n-k}`, equivalently `U(z)(1-R(z))=1`, are exact
  through degree five at `p=0,1,1/2,(1+i)/2,-1`
  (`research/adversarial-review/coordinator/check_renewal_series.py`, 25
  identities).
- The derivation requires naturally labelled post-free orders (shape
  multiplicities `N(T)`), and division by `N(H)A_p(H)`; at `p=0` the division
  fails for ranks `n>=2`.
- Conditional obstruction: at any `z` where both `U` and `R` converge
  absolutely, `R(z)=1` is impossible. A geometric `kappa_n=lambda^n` with
  `lambda` in the common absolute-convergence domain cannot solve the
  recurrence. More generally, if `sum_j |b_j kappa_{n+j}|` and
  `sum_{j,k} |b_j R_k kappa_{n+j+k}|` are finite, the recurrence forces
  `kappa_n=0` for every `n`.

## The missing obligation

The existing variation bound gives an exponential upper bound on `kappa_n`,
but it does **not** prove that the two weighted series above converge at the
decay radius. Without that estimate, the obstruction is conditional. The
rank-only classification is therefore open:
- no normalized rank-only measure is constructed;
- no general no-go is proved;
- the finite root search is not evidence either way.

## Concrete falsifier / next test

A normalized rank-only measure whose `kappa_n` decays more slowly than the
radius of `R` would evade the conditional obstruction and would settle the
problem positively. Conversely, a proof that the weighted series diverge at
every possible decay radius would turn the obstruction into a no-go. Either
would change the status; a truncated polynomial root does not.

## Scope

No paper claim, no scalar/covariant theorem and no ontology conclusion
depends on this task. The selected paper explicitly excludes rank-dependent
factors. This note is a status record, not a new result.
