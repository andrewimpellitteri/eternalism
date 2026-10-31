# Red-team review: countably many centered isometry classes

**Verdict: the measure-zero argument is correct under its stated centered,
field-bearing comparison structure.** Its only analytic input is a `C¹`
central scalar trace in proper time for each representative solution; it does
not require `C¹` dependence of the solution on the incoming radiation profile.
It does not imply nonisometry of bare unmarked metrics.

## Minimal trace regularity and source check

For one solution, let `I⊂R` be the proper-time domain of its distinguished
oriented center `Γ`, and let

```text
f(τ) = φ(Γ(τ)),       τ∈I.
```

It is enough that `f∈C¹(I)`. Luk–Oh–Yang (LOY), arXiv:1605.03893v1, Definition
2.1 defines a `C¹` reduced solution with `φ` itself `C¹` on the quotient
including its axis boundary. In §4 immediately after (4.1), the compactness
limit is explicitly obtained with `φ⁽ⁿ⁾→φ` in `C¹(Ω)` on each compact quotient
set. Along the diagonal `u=v=t`, this gives a `C¹` coordinate-time trace.
Also §4 gives `r⁽ⁿ⁾→r` in `C²`; hence `λ=r_v` is `C¹` in the limit. The axis
identity `ν=−λ` follows by differentiating `r(t,t)=0`. To evaluate the metric
formula `Ω²=−4νλ/(1−μ)` at the axis, use Proposition 3.4, (3.16):
`m=O(r³)`, so `μ=2m/r=O(r²)→0`. The central lapse is therefore
`Ω(t,t)=2λ(t,t)>0`. Hence axis coordinate to proper time,
`dτ/dt=2λ(t,t)`, is `C¹` with a `C¹` inverse. The scalar trace is therefore
`C¹` in proper time.

This is a quotient/axis-trace statement. It does **not** prove that the full
four-metric is `C²` in a regular Cartesian atlas, nor that these solutions
belong to a particular `C²` MGHD category. Those remain separate gates. For
the readout lemma itself, the clean assumption is simply `f∈C¹(I)` together
with a well-defined positive continuous central lapse for the proper-time
parametrization. No derivative of `f` with respect to profile parameters is
used.

## Null-image proof

Fix durations `T₁,…,T_N>0`, with `N≥2`. The launch times for which all readings
exist form

```text
D = {β : β, β+T₁,…,β+T_N ∈ I}.
```

This is an interval (possibly empty or with endpoints omitted). Define

```text
F(β) = ( f(β+T_j) − f(β) )_{j=1}^N,       β∈D.
```

Since `f∈C¹`, `F∈C¹(D;R^N)`. Cover `D` by countably many compact intervals
whose interiors cover it. On each such compact interval `F'` is bounded, so
`F` is Lipschitz. A Lipschitz image of a bounded real interval has
`N`-dimensional Lebesgue measure zero when `N≥2` (cover the interval by `O(δ⁻¹)`
subintervals of length `δ`; their images fit in `O(δ⁻¹)` balls of radius
`O(δ)`, with total `N`-volume `O(δ^(N−1))`). Countable subadditivity gives
`|F(D)|_N=0`. Any subset of allowed launch times has image contained in this
same null set.

Now suppose the comparison maps preserve time orientation, the unparametrized
center `Γ`, and the scalar field (or its explicitly allowed internal
symmetries). An isometry maps proper time on `Γ` to proper time plus a
constant. Therefore every duration-`T_j` readout vector from a centered
isometric copy of this one solution lies in `F(D)`: varying the marked launch
event only varies `β`. A scalar shift cancels from each difference. If global
scalar sign reversal is admitted, include `−F(D)` as one additional null set.
If time-reversing comparisons are admitted, include the corresponding
time-reversed trace curve as another branch; any finite number of these
branches remains null.

If the attainable readout set for a family of solutions contains a nonempty
open ball in `R^N`, it has positive `N`-dimensional measure. Were that family
covered by countably many centered, field-preserving isometry classes, its
readouts would lie in a countable union of the null sets above, which has
measure zero. Contradiction. Hence there are uncountably many classes under
this specified centered equivalence relation. The argument rules out
explaining an open multi-reading range solely by changing the launch time in
one solution, and indeed rules out a countable collection of such classes.

## Qualification and limits

- The comparison category must preserve the **unparametrized center** and
  time orientation, and must preserve the scalar readouts up to only the
  stated finite symmetries. Equivalently, for spherical models one may require
  isometries equivariant with respect to the specified spherical action. This
  is not a claim that the center/action is intrinsically recoverable from a
  bare metric.
- Without center preservation, an isometry could send the chosen observer to
  another timelike curve. Its readouts need not lie on the single curve `F`;
  this proof then says nothing about bare unmarked metric nonisometry.
- The open-ball premise is external to this lemma. The LOY cubic trace and
  proper-time estimates can support finite interpolation, but this note does
  not prove that premise, profile-map continuity, an MGHD identification, or
  the `C²` four-metric gate.
- The argument needs `C¹` only along the center. Mere continuity is
  insufficient for the measure-zero conclusion: continuous curves can have
  positive-area image. No `C¹` scattering-map dependence is needed.

## Source record

- Luk, Oh & Yang, *Solutions to the Einstein-scalar-field system in spherical
  symmetry with large bounded variation norms*, arXiv:1605.03893v1 (12 May
  2016), [primary source](https://arxiv.org/html/1605.03893v1), selected
  full-text audit. Locators: Definition 2.1 (reduced `C¹` solution and axis
  boundary), metric formula (1.2), axis identities (2.1)–(2.3), Proposition
  3.4 (3.16) (`m=O(r³)`), and §4 after (4.1) (compact `C¹` convergence for
  `φ`, `C²` convergence for `r`). This supports the quotient scalar trace and
  lapse calculation; it does not assert `C²` regular-chart metric convergence.

No novelty claim is made for the elementary measure argument.
