# Independent review: percolation-dominated scalar completion

## Verdict

I find no flaw in this stronger completion argument under its stated
definitions. The Möbius inversion support estimate, nonvanishing bound, and
`L1(P0)` convergence all work. The resulting labelled scalar measure is
absolutely continuous with respect to the real-percolation reference and
therefore gives zero mass to the countable family of eventually-all-timid
histories. This remains a scalar completion with norm-only cylinder
covariance; it does not establish full label covariance of the vector measure
or decoherence functional.

## Möbius inversion and the seed correction

Set `F(C)=1/q(C)`. The recursion is
`F(C)=sum_(P ideal of C) w(P)`, so Möbius inversion on the lattice of order
ideals gives

\[
w(C)=\sum_{S\subseteq\operatorname{Max}(C)}(-1)^{|S|}F(C\setminus S).
\]

Here `C\S` is the induced ideal obtained by deleting maximal elements. The
ideal-lattice Möbius function vanishes for all other differences; every
subset of `Max(C)` contributes once. This is the correct inverse, including
when distinct ideals have the same isomorphism type.

For the percolation reference, `F_0(C)=delta^{-|C|}`. Its inverse is

\[
w_0(C)=\delta^{-|C|}(1-\delta)^{|\operatorname{Max}(C)|},
\]

because the sum over deleted maxima is the binomial expansion of
`(1-delta)^|Max(C)|`. Let `Delta F=F-F_0`. It vanishes at sizes zero and at
all sizes at least three. Exact seed values give:

| Type | `Delta F` | `b(Delta F)=|Re|+|Im|` |
|---|---:|---:|
| singleton | `-8` | `8` |
| two-chain | `-96` | `96` |
| two-antichain | `(-488-16i)/5` | `504/5` |

For an `n`-element `C`, only subsets `S` leaving `C\S` of size one or two
can contribute to `w-w0`. There are at most `n` and `binom(n,2)` such subsets,
respectively. Subadditivity of `b` therefore gives

\[
b(w(C)-w_0(C))\le 8n+\frac{504}{5}\binom n2\le 51n^2.
\]

Since `|Max(C)|<=n` and `delta=1/10`,
`w_0(C)=10^n(9/10)^|Max(C)|>=9^n`. At `n=3`, `9^n=729>459=51n^2`;
the ratio `9(n/(n+1))^2` is greater than one for all `n>=3`, so the strict
inequality persists. Thus `|w(C)|>=w0(C)-|w-w0|>0` for every `n>=3`.
The empty, singleton, chain-two and antichain-two weights are respectively
`1,1,2,(-3-16i)/5`, all nonzero. This proves every transition is nonzero
because each `q(C)` is nonzero.

The seed multiplicities agree with the earlier construction: in the
two-antichain the proper ideals consist of the empty ideal once and the
singleton ideal type twice. Their `w`-sum is `3`; hence
`w=(20/(3+4i))-3=(-3-16i)/5`, and the timid transition is `(11-12i)/20`.
The `cp` paths likewise count both distinct singleton precursors separately,
giving `(3+4i)/40,(3+4i)/40,1/8` and phase ratio `(3-4i)/5`.

## Transition perturbation and variation control

For parent size `n>=3`, `q(C)=delta^n`, just as for the reference process.
For any ideal `P` of `C`, `|P|<=n` and the preceding bound implies
`b(w(P)-w0(P))<=51n^2` (the empty ideal has zero difference). There are at
most `2^n` actual ideals. Consequently the complete row difference, including
the full/timid precursor, obeys

\[
\sum_{P\text{ ideal of }C}|t(C,P)-t_0(C,P)|
\le 51n^2(2\delta)^n=:\zeta_n.
\]

The row sum of `t0` is one: it is the transition law from independently
selecting each old element with probability `1-delta` as a direct parent and
taking transitive closure. Equivalently, for an ideal `P`, the transition
probability is
`t0(C,P)=delta^(n-|P|)(1-delta)^|Max(P)|`. The gregarious value is
`delta^n`. Thus `sum_P |t(C,P)|<=1+zeta_n`, and

\[
V_{n+1}:=\sum_{|D|=n+1}|A(D)|\le V_n(1+\zeta_n).
\]

Since `zeta_n=51n^2 5^{-n}` is summable, `V_n` is uniformly bounded by
`V_3 product_(k=3)^infinity(1+zeta_k)`. This use of the row bound counts
each ideal subset, not each ideal isomorphism type.

## The `L1(P0)` completion

All `t0(C,P)` are strictly positive, so every finite cylinder has positive
`P0` probability and the conditional measures in the proposal are defined.
Let `F_n` be the density of `nu_n` with respect to `P0`, constant on each
depth-`n` cylinder:

\[
F_n|_{[C]}=A(C)/P_0([C]).
\]

If `D` is a child of `C` through precursor `P`, then
`A(D)=A(C)t(C,P)` and `P0([D])=P0([C])t0(C,P)`. Integrating the absolute
density difference over that child cylinder gives exactly
`|A(C)| |t(C,P)-t0(C,P)|`. Summing over parents and children proves

\[
\|\nu_{n+1}-\nu_n\|_{TV}
=\|F_{n+1}-F_n\|_{L^1(P_0)}
\le V_n\zeta_n.
\]

The right side is summable, so `F_n` is Cauchy in `L1(P0)` and converges to
some `F`. The measure `nu=F P0` is a countably additive complex measure and
`|nu|=|F|P0`, hence `nu` is absolutely continuous. For any fixed cylinder
`[C]` of depth `m`, the integral of every `F_n` with `n>=m` over `[C]` is
the sum of amplitudes of its depth-`n` descendants, equal to `A(C)` by
iterating MSR. `L1` convergence preserves this cylinder value. The same
argument gives total mass one.

There is no hidden support-collision issue in this construction: unlike the
atomic padding, every `nu_n` is a density against the same reference measure.
The `L1` estimate compares densities on the common child-cylinder partition.

## Nonconcentration on timid tails and scope

For nonempty parent `C`, a full-past transition satisfies
`t0(C,C)=(1-delta)^|Max(C)|<=0.9`, since `Max(C)` is nonempty. A proper
precursor has `n-|P|>=1`, so
`t0(C,P)<=delta=0.1`. Thus every transition after the initial birth is at
most `0.9`. Any infinite labelled history has depth-`n` cylinder probability
at most `0.9^(n-1)`, which tends to zero; `P0` has no point atoms. There are
only countably many histories that are all-timid after some finite prefix,
so their union is `P0`-null. Absolute continuity then makes it `|nu|`-null
as well. In particular, this completion is not concentrated on the frozen
tails used by the earlier construction.

I independently checked the seed inversions, the two correction norms,
`w0>=9^n`, and the cylinder-density increment identity using exact rational
complex arithmetic. A separate small enumeration through parent size four
verified recursion/Möbius agreement, MSR, reference row sums, nonzero
transitions, and the row-error bound. No packages were installed, no shared
checker was run or changed, and no broad literature or priority audit was undertaken. The
argument supplies a labelled scalar measure with the prescribed cylinder
amplitudes. It does not make those amplitudes or the associated rank-one
decoherence functional invariant under relabeling, and it does not establish
physical admissibility or a full operator-QBC model.
