# Rank-only post factors: stationary kernel, recurrence, and pivot

Status: 2026-10-20. Probe `rank-factor-boundary`. This does **not** settle
whether a normalized rank-only measure exists for `p∉[0,1]`. It proves a new
structural lemma, reduces the question to a scalar convolution equation, and
records why the finite root search is inconclusive. Verdict: **PIVOT** — keep
the lemma, do not claim a counterexample or a no-go.

## Result

### Theorem (stationary next-post kernel)

Let `H` be a principal finite order of size `n` with unique maximum `p`, and let
`A_p(C)=p^{L(C)}(1-p)^{binom(|C|,2)-R(C)}` on Complex Transitive Percolation.
For `m>n`, let `J` range over principal orders of size `m` whose previous post
past is `H` (equivalently, the next post past after `H`). Then

`Σ_J N(J) A_p(J) = N(H) A_p(H) R_{m-n}`,

where `R_1 = p`, and for `k≥2`

`R_k = Σ_{T post-free, |T|=k-1} A_p(T) p^{M(T)+min(T)}`,

with `M(T)` the number of maximal elements and `min(T)` the number of minimal
elements of `T`.

**Proof.** A next post past `J` is the ordinal sum `H ⊕ S`: the previous post
`p` is below every element after it, and the next post `x` is above all of them.
`S` is principal (unique maximum `x`) and has no post other than `x`; conversely
`H⊕S` has previous post past `H` for any such `S`. Covers across the ordinal sum
are exactly the covers from `p` to the minimal elements of `S`; there are no
cross incomparable pairs. Hence `A_p(J)=A_p(H)A_p(S)p^{min(S)}` and
`N(J)=N(H)N(S)`. Writing `S=T⊕{x}` with `T` post-free gives
`A_p(S)=A_p(T)p^{M(T)}`, `min(S)=min(T)`, and the stated `R_k`. Summing over
`S` of size `k` gives the factorization. ∎

The finite check `check_stationarity.py` compares every `S(H,m)` from the
next-post enumeration against `N(H)A(H)R_{m-n}` for `H` up to size 5 and `m≤6`:
32 checks at `p=0.5` and at `p=(1+i)/2`, **max error 0.000e+00** (floating
point).

### Consequence for rank-only factors

For a rank-only rule `ν(D_H)=κ_n N(H)A_p(H)`, the laminar conservation identity
`ν(D_H)=Σ_{J next from H} ν(D_J)` becomes the scalar convolution

`κ_n = Σ_{k≥1} R_k κ_{n+k}`.

A geometric ansatz `κ_n=λ^n` solves it iff

`1 = Σ_{k≥1} R_k λ^k`.

The common-factor case is `λ=1`. For `p∈[0,1]` the series sums to 1
(classical probability); for `p∉[0,1]` it generally diverges at `λ=1`, which is
the existing no-go. A root `λ` with `|λ|<1/(|p|+|1-p|)` would give a decaying
rank-only sequence; if the total mass `Σ_n κ_n U_n` converges and the
laminar values extend to a countably additive measure, that would be a genuine
counterexample to the necessity of a common factor.

## Numerical coefficients

At `p=0.5`:

| k | `R_k` | terms in `T` |
|---|---|---|
| 1 | 0.5 | 1 |
| 2 | 0 | 0 |
| 3 | 0.03125 | 1 |
| 4 | 0.025390625 | 4 |
| 5 | 0.02203369140625 | 28 |
| 6 | 0.020195960998535156 | 283 |
| 7 | 0.018873311579227448 | 4141 |

At `p=(1+i)/2`:

| k | `R_k` |
|---|---|
| 1 | `0.5+0.5i` |
| 2 | `0` |
| 3 | `-0.125+0.125i` |
| 4 | `-0.21875+0.21875i` |
| 5 | `-0.40625+0.4140625i` |
| 6 | `-0.5888671875+0.94140625i` |
| 7 | `-0.32391357421875+1.87969970703125i` |

The coefficients are computed by `kernel_sequence7.py` from post-free `T` up to
size 6; `R_k` for larger `k` would need a post-free enumeration at size ≥7 or a
generating function.

## Root search and why it is inconclusive

Solving the truncated polynomial `1-Σ_{k≤7}R_k z^k` gives, for
`p=0.2+0.7i` (`1/(|p|+|1-p|)=0.558`), roots at `|z|≈0.486, 0.496, 0.521,
0.540, 0.554`, i.e. apparently inside the convergence radius. For
`p=(1+i)/2` (`1/t=0.707`) the smallest root is `≈0.750`, outside.

**This is not evidence for a counterexample.** The `R_k` grow roughly like
`t^k`; the truncated polynomial is being evaluated beyond its reliable radius,
and at a candidate `λ` the terms `R_k λ^k` are still growing at `k=7`
(e.g. for `p=0.2+0.7i`, `R_7 λ^7≈0.5` at `λ=0.486`). A root of the truncated
polynomial can move or disappear when the tail is included. No construction and
no no-go follows.

What would settle it:

1. derive a generating function or rigorous bounds for `R(z)=Σ R_k z^k` and
   evaluate it inside `|z|<1/t`;
2. or prove that no root with the required decay exists (e.g. by a
   maximum-modulus/positive-coefficient argument in the real case and an
   analytic continuation in the complex case);
3. or construct the measure directly on the laminar tree and verify countable
   additivity and the total-mass normalization.

## Verdict: PIVOT

The probe produced a **new structural lemma** (stationarity of the next-post
kernel and the scalar recurrence), not the desired classification. The
rank-only existence question is now a hard analytic/generating-function problem
beyond this two-week timebox. Preserve the lemma for the short note; pivot the
main effort to `vector-measure-boundary`, which has a crisper route to a
theorem or counterexample, and keep the labelled short note as the floor.

Do **not** claim:
- a rank-only counterexample;
- a no-go for rank-only factors;
- that the truncated roots are meaningful;
- any physical or ontological consequence.

## Files and checks

- `probe.py` — next-post enumeration and finite `S(H,m)` kernel.
- `kernel_sequence7.py` — `R_k` via post-free `T`, and truncated root search.
- `check_stationarity.py` — 32 exact finite comparisons; max error 0.
- Standard library only; no installs; no board edits.

## Known-result reduction

- For `p∈[0,1]`, `R(1)=1` and the common factor `κ=c(1-p)` is the classical
  result; the recurrence reduces to the probability identity.
- For `p∉[0,1]`, the common factor fails because `R(1)` diverges; the existing
  no-go is recovered.
- The rank-only case is new only in the weakened value rule; it does not change
  the labelled theorem.
