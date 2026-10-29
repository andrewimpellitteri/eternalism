# Regularity of the Luk–Oh–Yang past-null-infinity limit

**Assessment: quotient regularity is proved at finite orders; spacetime-metric
`C²`/`C∞` at the axis and `C¹` dependence on the incoming profile are not
closed by the audited theorems.** This is a source audit and a precise estimate
obligation, not a counterexample to those regularity claims.

## Source theorem and smooth compact profiles

The target is Luk–Oh–Yang (LOY), arXiv:1605.03893v1 (12 May 2016), in the
normalization `Ric = 2 dφ⊗dφ`. Theorem 1.7 and §4 construct a global limit on
the quotient `Q={(u,v):u≤v}` from finite outgoing cones `C_{u_n}`, with
`u_n→−∞`, for a `C²` incoming profile `Φ` satisfying (1.20). A smooth compactly
supported `Φ` satisfies the finite-derivative hypotheses after amplitude
scaling, for any fixed `0<γ<1`; this audit makes no claim about a uniform
neighborhood in a profile norm.

The exact finite-cone estimates relevant to regularity are:

1. Theorem 1.1, (1.8)–(1.9), gives bounds uniform in `u₀` for `λ=r_v`,
   `ν=r_u`, `μ=2m/r`, `φ`, first derivatives of `rφ`, and pure second null
   derivatives of `rφ` and `r`.
2. Proposition 3.18, (3.44)–(3.47), assumes bounded second derivative of
   `Φ`. On each triangular domain `D(u₀,v₀)` it uniformly bounds third
   normalized pure derivatives of `rφ` and second normalized pure derivatives
   of `log λ` and `log ν`, with constants independent of `u₀`, `v₀`, and the
   profile's second-derivative bound `A` except for the displayed linear
   dependence on `A`. The proof explicitly uses averaging formulas near the
   axis and commutation away from it.
3. Section 4, especially its compactness passage following (4.1), records the
   extracted convergence on every compact quotient set as
   `(φ, ∂v(rφ), ∂u(rφ))` in `C¹`, `r` in `C²`, and `m` in `C¹`. It also records
   uniform higher pure-derivative bounds and says corresponding mixed bounds
   follow from the equations. Remark 4.1 supplies additional weak-derivative
   bounds. These are quotient statements for a subsequential limit.

Thus one may use the paper's regularity and estimates at the stated quotient
level. Do not upgrade the compact-convergence sentence to `C²` convergence of
all reduced unknowns: in particular, it explicitly gives only `C¹` convergence
for `m` and for `φ` and the first derivatives of `rφ`.

## Why this does not yet prove a `C²` spacetime metric at the axis

The reconstructed four-metric is

```text
g = −Ω² du dv + r² dσ²,     Ω² = −4νλ/(1−μ),     μ=2m/r.
```

The axis `u=v` is a boundary of the two-dimensional quotient, not a regular
coordinate locus for `(u,v,θ,ϕ)` as four-dimensional coordinates. Quotient
`C²` bounds alone do not establish the parity/compatibility conditions needed
for a `C²` tensor in a regular Cartesian chart at the fixed-point axis. Also,
the formula `m/r` divides by a quantity vanishing at that axis. The paper
states `m=0` there and gives regularity properties used in the reduced
equations, but Theorem 1.7 does not state that the limiting four-metric is
`C²` (or `C∞`) in an axis-regular atlas. Its compactness conclusion for `m` is
only `C¹`.

There is a plausible finite-order route, but the final uniform estimate and
reconstruction are not written as a theorem in LOY. Proposition 3.18 supplies
the third quotient derivatives that help make second derivatives of `r`
equicontinuous on compact sets. To conclude `g∈C²` in a regular chart one still
needs a uniform, axis-inclusive estimate for the derivatives through order
two of the reconstructed regular-chart coefficients, including the quotient
`m/r`, plus the axis parity/compatibility identities, and compactness strong
enough to pass those derivatives to the selected limit. For `C∞`, one needs
such estimates and reconstruction at every order, uniformly as `u₀→−∞`.
Smoothness of each finite-cone solution is not that uniform statement.

**Named gap (metric-axis reconstruction lemma).** For every compact subset `K`
of the regular four-dimensional spacetime, prove uniform-in-`u₀` bounds and
equicontinuity for the derivatives up to order two of `g^{(u₀)}` in a regular
axis chart, derived from the finite-cone equations and smooth compact `Φ`;
prove the required axis parity and regularity of `m/r`; then pass them to the
same `u₀→−∞` limit. The `C∞` version requires the analogous all-order estimates.
The exact falsifier for an attempted deduction from the listed LOY estimates
is an axis chart in which those estimates fail to control one of these second
derivatives or its continuity. The weaker statements actually printed in §4
do not themselves supply this lemma.

## Published follow-up checked

Kilgore, arXiv:2108.13377v1 (30 Aug 2021), §§1, 3–5 and 7, is directly relevant
as a method comparison. It says it improves LOY's cone-based estimates to all
derivative orders for sufficiently regular data, with extra care near the
axis; its regular-chart discussion explains parity and why the area radius
`r` itself is not smooth at the axis. But §1 explicitly says it does **not**
directly control LOY's past-null-infinity global scattering solutions and
leaves the two-sided complete case open. Its all-order estimates concern the
future of a cone and its later Cauchy extension. They show that all-order
commutation is viable in a related setup, not that the uniform-in-`u₀`
axis-inclusive estimates required above hold for the scattering limit. It
therefore does not close the LOY metric-axis gap.

## Profile dependence is a separate gap

Neither LOY Theorem 1.7 / §4 nor the checked Kilgore follow-up states a `C¹`
solution map from incoming profiles to the limiting solution or to a central
observer's finite-time readings. Proposition 3.18 is an a priori estimate for
one profile; it is not an estimate for differences, difference quotients, or
the linearized equations in a profile direction.

For a concrete `C¹` claim on a fixed compact support class, one needs a Banach
profile space (for example a specified `C^k` norm on a common compact support),
a well-defined selected scattering solution for every profile in an open
neighborhood, uniqueness in the chosen scattering class or another explicit
selection rule, and a parameter-uniform estimate for the linearized
finite-cone solutions and their remainders. Those estimates must persist
uniformly as `u₀→−∞` and imply convergence of the derivatives, not only
subsequence convergence of the solutions. For a central reading, the estimate
must also control the regular-axis restriction and the profile-dependent
proper-time parametrization of the central geodesic. Without these steps, a
formal differentiation of the finite-cone equations does not prove a `C¹`
limit map.

**Named gap (uniform scattering-map differentiability).** Establish
Fréchet-`C¹` dependence of the finite-cone solutions on `Φ` with derivative
and quadratic remainder bounds uniform in `u₀` on compact spacetime sets,
prove convergence of that derivative as `u₀→−∞`, and prove uniqueness (or
state a canonical selection) of the limiting scattering solution. For
observer readings, include the axis and proper-time variation. A falsifier is
failure of any one of: uniform derivative bounds, uniform remainder bounds,
derivative convergence, or uniqueness/selection. The linear Minkowski formula
for the central trace is only a linearized guide and cannot fill these gaps.

## Bounded verdict

- **Quotient finite-order estimates:** PASS, exactly at the statements and
  convergence strengths above.
- **`C²` spacetime metric including the axis:** CONDITIONAL / not established
  by the cited LOY theorem; the required regular-chart estimate and
  reconstruction lemma is named above.
- **`C∞` spacetime metric including the axis:** not established for this
  `u₀→−∞` family by LOY. The cone-based all-order follow-up is not the same
  scattering limit.
- **`C¹` dependence on the incoming radiation profile:** separate missing
  theorem; no parameter-uniform differentiated estimate or unique scattering
  map was found in the checked sources.

These conclusions concern regularity and solution-map dependence only. They do
not establish or refute maximal globally hyperbolic development uniqueness.
