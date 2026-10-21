# Rank-only post factors: stationary kernel, recurrence, and pivot

Status: 2026-10-20. Probe `rank-factor-boundary`. This does **not** settle
whether a normalized rank-only measure exists for `p∉[0,1]`. It derives a
stationary-kernel identity whose priority is unverified, reduces the question to a scalar convolution equation, and
records why the finite root search is inconclusive. Verdict: **PIVOT** — keep
the lemma, do not claim a counterexample or a no-go.

> **Corrections applied 2026-10-21** (submission for review), following
> `research/adversarial-review/coordinator/BOUNDARIES.md`: (i) the sum defining
> `R_k` is now stated explicitly as a sum over **naturally labelled** post-free
> orders `T` (each labelling counted once), equivalently over shapes with
> `N(T)` multiplicity — verified exactly in `check_stationarity.py`; (ii) the
> claim `R(1)=1` is restricted to `0<p≤1` (at `p=0` every `R_k=0`, so
> `R(1)=0`); (iii) the division producing the scalar recurrence requires
> `N(H)A_p(H)≠0`, available at every rank for `p≠0` but not at `p=0` for ranks
> ≥2; (iv) the earlier suggestion that the total-variation no-go implies
> divergence of the complex series `R(1)` for `p∉[0,1]` is **withdrawn** — that
> inference is unproven; (v) rank-only existence and the priority of the lemma
> remain unresolved. Corrections are marked in place; historical results are
> preserved. The kernel identity is now checked in exact arithmetic.
> [marker end]

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

> **[Corrected 2026-10-21]** the sum over `T` runs over **naturally labelled**
> post-free orders `T` on `{0,…,k-2}`, each labelling counted once (this is
> what `kernel_sequence7.py` computes via `poscau.causets`). Equivalently,
> summing over unlabelled post-free shapes `τ` with multiplicity `N(τ)` (the
> number of natural labelings of `τ`) gives the same value; the two forms are
> checked to agree exactly for `k=2..7` at `p=1/2` in
> `check_stationarity.py` section C. The displayed derivation requires that
> multiplicity, so the domain must be stated as here. [marker end]

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

> **[Updated 2026-10-21]** the identity is now checked in **exact** arithmetic
> (Fraction at `p=1/2`, Gaussian rationals at `p=(1+i)/2`): 32 exact identities
> per parameter, zero tolerance, PASS. The non-dyadic point `p=0.2+0.7j`
> remains a floating-point diagnostic (max error `2.4e-16`) and is labelled as
> such by the script. [marker end]

### Consequence for rank-only factors

For a rank-only rule `ν(D_H)=κ_n N(H)A_p(H)`, the laminar conservation identity
`ν(D_H)=Σ_{J next from H} ν(D_J)` becomes the scalar convolution

`κ_n = Σ_{k≥1} R_k κ_{n+k}`.

> **[Corrected 2026-10-21]** this reduction **divides by `N(H)A_p(H)`**, so it
> requires `N(H)A_p(H)≠0` at the relevant ranks. For `p≠0` a chain supplies a
> nonzero value at every rank (`N(H)A_p(H)=p^{n-1}`). At `p=0` no rank `n≥2`
> permits the division (every principal `H` of size `n≥2` has `A_0(H)=0`), so
> the convolution equation is derived for `p≠0` only. [marker end]

A geometric ansatz `κ_n=λ^n` solves it iff

`1 = Σ_{k≥1} R_k λ^k`.

The common-factor case is `λ=1`. For `0<p≤1` the series sums to 1
(classical probability). [Corrected 2026-10-21: two changes. First, `p=0` is
**excluded**: at `p=0` every `R_k=0` — `R_1=p=0`, and for `k≥2` every post-free
`T` is nonempty with `M(T),min(T)≥1`, so each term carries a positive power of
`p` — hence `R(1)=0` at `p=0`, not 1 (exact check in `check_stationarity.py`
section B); the classical infinite-post probability is not one at `p=0`.
Second, **withdrawn**: the earlier text continued "for `p∉[0,1]` it generally
diverges at `λ=1`, which is the existing no-go". The total-variation no-go
concerns absolute sums `Σ|A_p(C)|` over disjoint cylinder families and does
**not** by itself imply divergence of the complex scalar series `Σ_k R_k`,
where cancellations can occur. Whether `R(1)` converges for nonreal `p` is
open here; no equivalence with the measure no-go is claimed. Marker end.]
A root `λ` with `|λ|<1/(|p|+|1-p|)` would give a decaying
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

The probe produced a structural lemma (stationarity of the next-post
kernel and the scalar recurrence), not the desired classification.
[Corrected 2026-10-21: the lemma's status as a "new structural lemma" is a
priority claim that remains unverified; no novelty is asserted here. Marker
end.] The
rank-only existence question is now a hard analytic/generating-function problem
beyond this two-week timebox. Preserve the lemma for the short note; pivot the
main effort to `vector-measure-boundary`, which has a crisper route to a
theorem or counterexample, and keep the labelled short note as the floor.

Do **not** claim:
- a rank-only counterexample;
- a no-go for rank-only factors;
- that the truncated roots are meaningful;
- that `R(1)` diverges for `p∉[0,1]` (added 2026-10-21: the TV no-go does not
  settle the complex series);
- any physical or ontological consequence.

## Files and checks

- `probe.py` — next-post enumeration and finite `S(H,m)` kernel.
- `kernel_sequence7.py` — `R_k` via naturally labelled post-free `T`, and the
  truncated root search (labelled a numerical diagnostic as of 2026-10-21).
- `check_stationarity.py` — as of 2026-10-21: 64 exact kernel identities
  (zero tolerance) at `p=1/2` and `p=(1+i)/2`; exact edge cases `R_1=p`,
  `R_k=0` at `p=0`; exact equality of the labelled `T`-sum and the
  shape-multiplicity form of `R_k` for `k=2..7`; plus a clearly labelled
  floating-point diagnostic at `p=0.2+0.7j`.
- Standard library only; no installs; no board edits.

## Known-result reduction

- For `0<p≤1`, `R(1)=1` and the common factor `κ=c(1-p)` is the classical
  result; the recurrence reduces to the probability identity. [Corrected
  2026-10-21: `p=0` excluded — `R(1)=0` there. Marker end.]
- For `p∉[0,1]`, the common factor fails as a finite-total-variation complex
  measure: the scalar no-go applies. [Corrected 2026-10-21: the earlier text,
  "the common factor fails because `R(1)` diverges; the existing no-go is
  recovered," is withdrawn — divergence of `R(1)` is not established, and the
  no-go is about total variation, not the complex series. Marker end.]
- The rank-only case is new only in the weakened value rule; it does not change
  the labelled theorem. Whether a rank-only measure exists remains unresolved,
 as does the lemma's priority.
