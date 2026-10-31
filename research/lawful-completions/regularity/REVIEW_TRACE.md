# Red-team trace: relabeling one scattering spacetime

**Scope.** This checks whether a continuous family of observer markings in one
already-existing LOY scattering spacetime can produce a continuous interval
of finite-time central readings. It does not redo the energy/charge review,
prove a `C²` four-metric at the axis, or establish a scattering-map theorem.

## Conditional marking theorem

Let one spherically symmetric solution have a distinguished central timelike
line `γ`, parametrized by proper time `τ` on an interval containing
`(-∞, τ*]`. Suppose there is `a<τ*` such that the entire central past region
through `γ(a)` is exactly flat with constant scalar field, and suppose a
continuous nonnegative reading `q(τ)` on the line satisfies

```text
q(τ)=0 for τ≤a,       q(τ*)=q*>0.
```

For any fixed `T>τ*−a`, mark `bβ=γ(β)` with
`β∈[a−T, τ*−T]`. These marks all lie before `a`. Their pointed entire
chronological pasts are flat and mutually isometric by Minkowski translations,
including the constant scalar and the central observer germ. All global
charges defined for the spacetime are literally the same, since the underlying
solution has not changed. The reading at proper time `T` after each mark is
`q(β+T)`. Continuity and the endpoint values give

```text
[0,q*] ⊆ {q(β+T): β∈[a−T, τ*−T]}.
```

Equality of the set with `[0,q*]` additionally requires `q(τ)≤q*` throughout
`[a,τ*]` (for example, choose `τ*` to be a maximum on that compact interval).
Without that extra condition the image may extend above `q*`; the interval
inclusion is the conclusion guaranteed by the hypotheses. This is the
intermediate-value argument and needs no variation of the spacetime or its
global charges.

The theorem is conditional on one solution and one continuous nonnegative
central reading. The audited LOY route can supply a quotient-level candidate
for `q`, as checked below, but identifying it with the geometric Ricci
contraction of a `C²` four-metric at the axis remains a separate regularity
step.

## Axis coefficient for sideways uniqueness

Use LOY's notation `λ=r_v`, `ν=r_u`, `μ=2m/r`. Their reduced equations give

```text
r_uv = 2mνλ / ((1−μ) r²),
K := r_uv/r = 2mνλ / ((1−μ) r³),
λ⁻¹ m_v = 1/2 (1−μ) r² (λ⁻¹ φ_v)².
```

For the limit in §4, `r` is `C²` on compact quotient sets, `φ` is `C¹`, and
`m` is `C¹`; the LOY bounds give `λ>1/3`, `−2/3<ν<−1/6`, `μ<1/2`, and a
uniform bound for `λ⁻¹φ_v` (Theorem 1.1, (1.8)–(1.9), passed to the limit).
On each compact set these imply local upper and lower bounds for `λ`. Fix
`u` and integrate the mass equation outward from the axis, using `m(u,u)=0`.
Since `r_v=λ` and `r(u,u)=0`, `r` is comparable to `v−u` locally; hence

```text
|m(u,v)| ≤ C ∫_u^v r(u,v′)² dv′ ≤ C′ r(u,v)³.
```

Also `1−μ>1/2`, while `ν` and `λ` stay bounded on compact sets. Therefore
`K` is bounded up to the axis on every compact quotient triangle. The estimate
does not require an `O(r³)` assertion to be assumed: it follows from the
axis mass condition and the displayed flux equation. The same argument works
for the finite-cone approximants with local constants uniform in `u₀` because
the quoted first-order bounds are uniform.

There is also a stronger, direct source citation: LOY Proposition 3.4,
equation (3.16), proves `m≤C ε² min{r³,r^(1−γ)}` for the finite-cone
solutions. On compact sets this gives `|K|≤Cε²` immediately from the `r³`
branch and the bounds for `λ`, `ν`, and `1−μ`; the estimate passes to the
quotient limit. Thus local boundedness of `K` is not a regularity conjecture.
The flux derivation above explains its axis scaling, while (3.16) is the
cleanest estimate to cite.

Set `t=(u+v)/2`, `ρ=(v−u)/2`, and `Ψ=rφ`. From `Ψ_uv=KΨ`,

```text
Ψ_ρρ − Ψ_tt = −4KΨ.
```

LOY Definition 2.1's `C¹` solution class requires `∂u(rφ)` and `∂v(rφ)` to be
`C¹`, so `Ψ` has the mixed regularity needed for this equation classically on
the quotient. Suppose the central trace `φ(t,0)` vanished for all `t`. Then
`Ψ(t,0)=0`; differentiating in the inward radial direction gives
`Ψ_ρ(t,0)=r_ρ(t,0)φ(t,0)=0`. On any finite sideways characteristic triangle,
bounded `K` and these zero Cauchy data imply `Ψ=0` by the standard Volterra
integral equation (or its local energy estimate), iterated across finitely
many subtriangles. Every finite quotient point lies in such a triangle.
Consequently `Ψ≡0`, contradicting the nonzero incoming radiation limit
`lim_{u→−∞}2∂v(rφ)=Φ`.

Thus the central scalar trace is not identically zero for a nonzero incoming
profile. If the profile vanishes for `v<a`, the exact flat-wedge deduction
from the finite-cone construction gives `φ=0` on the central line before the
pulse. Since the central trace is `C¹`, the mean value theorem yields some
finite `τ*>a` with `dφ/dτ≠0`.

## Direct cubic trace and minimal convergence

The sideways uniqueness argument is not needed to obtain central visibility.
More directly, LOY §4 immediately after (4.1) proves for every finite-cone
solution

```text
|λ_n⁻¹ ∂v(r_n φ_n)(u,v)
  − [λ_n(u_n,v)/λ_n(u,v)] Φ(v)|
    ≤ C ε³ max{v−u,1}^(−2γ),
|log λ_n(u,v) − log(1/2)|
    ≤ C ε² max{v−u,1}^(−γ).
```

At the axis, `∂v(rφ)=λφ` and `λ_n(u_n,t)=1/2`. Hence uniformly in cone
vertex and central coordinate `t`,

```text
|φ_n(t,t) − Φ(t)/(2λ_n(t,t))| ≤ C ε³,
|2λ_n(t,t)−1| ≤ C′ ε²,
|φ_n(t,t)−Φ(t)| ≤ C″ ε³,
```

where the last line uses `|Φ|≤ε` and the uniform positive lower bound on
`λ`. The limit passage needs only the compact convergence LOY actually
states: `φ_n→φ` in `C¹` and `r_n→r` in `C²`; thus `λ_n(t,t)→λ(t,t)` and
the estimate passes to the selected quotient limit. No convergence of `m`
beyond the stated `C¹`, no differentiability in `Φ`, and no `C²` metric
reconstruction are used here.

For `Φ=δF`, with a fixed smooth compactly supported `F` and `F(t*)≠0`, choose
`δ>0` small enough for LOY and so that the leading `δF(t*)` dominates the
`O(δ³)` remainder. Then `φ(t*,t*)≠0`; exact flatness before the support gives
`φ(t,t)=0` earlier. The center trace is `C¹`, so the mean value theorem
produces a point between them with nonzero center-time derivative. Since the
axis lapse is continuous and positive, the proper-time derivative is also
nonzero there. This proves positivity of the formal source reading at some
finite proper time without sideways uniqueness.

For a fixed launch point `t_b` before the support, the axis relations
`ν=−λ` and `μ=0` yield the proper-time clock
`τ_n(t)=∫_{t_b}^t 2λ_n(s,s)ds`. The log-`λ` bound gives
`τ_n(t)=(t−t_b)+O(ε²)` uniformly on each fixed finite time window. Its
inverse therefore obeys `t_n(T)=t_b+T+O_T(ε²)`. With
`|Φ′|≤ε`, the profile shift contributes `O_T(ε³)`, so

```text
φ_n(t_n(T),t_n(T)) = Φ(t_b+T) + O_T(ε³).
```

Uniform compact convergence of `λ_n` and `φ_n` passes these clocks and
readings to the LOY limit. This validates the scalar finite-proper-time
approximation at quotient/classical level. It does **not** differentiate the
error estimate: an `O(ε³)` estimate for `φ` values alone does not estimate
derivatives of that remainder. The nonzero-derivative conclusion instead
follows from a nonzero scalar value, the earlier zero trace, and `C¹`
regularity.

## Continuity and the curvature-language boundary

The quotient estimates do suffice for a continuous **field-side** central
reading. The limit has `φ∈C¹` up to the axis. Along the symmetry axis the
induced proper-time element is `dτ=Ω(t,t)dt`, where
`Ω²=−4νλ/(1−μ)`. The mass estimate above gives `μ=O(r²)→0`; `r∈C²` gives
continuous `λ,ν`, and their sign bounds keep `Ω` continuous and positive.
Thus the central scalar derivative with respect to proper time is continuous,
and

```text
q_E(τ) := 2 (dφ/dτ)²
```

is continuous and nonnegative, vanishes on the flat pre-pulse segment, and is
positive at the `τ*` just obtained. This is exactly the reduced Einstein
source expression, in LOY's normalization `Ric=2 dφ⊗dφ`.

**Precise loss:** at the regularity stated for the `u₀→−∞` limit, `q_E` is
well-defined as a continuous matter/source reading on the central line. The
audited source does not prove that the reconstructed four-dimensional metric
is `C²` in an axis-regular chart. Accordingly it does not justify, at this
stage, treating `q_E` as a classical geometric tensor contraction
`Ric_g(U,U)` computed from that reconstructed metric. The conditional marking
theorem is valid at the quotient/classical Einstein–scalar level if its
observable is defined by the field-side expression; its interpretation as a
classical Ricci-curvature observable requires the missing metric-axis
regularity lemma already identified in `RESULT.md`. No conclusion about
general geodesic initial-value uniqueness or MGHD uniqueness follows here:
the marks use the symmetry-fixed central line of one existing solution.

## Verdict and concrete failure points

- **Bounded sideways coefficient:** PASS from LOY's mass flux equation and
  first-order quotient bounds, with the sharper direct citation LOY
  Proposition 3.4 (3.16); `K∈L∞_loc` up to the axis.
- **Nontrivial central field and continuous source reading:** PASS directly
  from the §4 cubic trace estimate, exact flat pre-pulse region, and `C¹`
  center trace; sideways uniqueness is an independent route, not needed for
  this step.
- **Continuous interval of same-spacetime marked readings:** PASS under the
  abstract hypotheses; the guaranteed result is range inclusion
  `[0,q*]⊆range`, and exact equality needs the stated maximum condition.
- **Classical `Ric_g(U,U)` at the axis:** OPEN under the audited regularity;
  this is the precise point where quotient regularity stops short of a
  geometric `C²` metric claim.

The sideways argument would fail if the limiting mass flux did not imply
`m=O(r³)` locally, if `1−μ` or the null expansions lost their local bounds,
or if the limit lacked the quotient derivatives needed to integrate the
equation for `Ψ`. The marked-reading conclusion would fail if the central
source reading were discontinuous, sign-indefinite, or did not vanish on the
flat segment. None of those failures occurs under the listed LOY quotient
bounds and the conditional assumptions above.

## Source locators

- Luk–Oh–Yang, arXiv:1605.03893v1: §1.2, Theorem 1.7 and (1.20); §2,
  Definition 2.1, Remark 2.3, equations (2.8)–(2.11); §3, Proposition 3.4
  (3.16), estimates (3.12), (3.37); §4, estimates immediately following
  (4.1), compactness passage, and Remark 4.1.
- The flat pre-pulse region is the finite-cone local-uniqueness inference
  audited in `../collapse-extension/SCATTERING_FOLLOWUP.md`; it is not a
  separately numbered corollary of Theorem 1.7.
