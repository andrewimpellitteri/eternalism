# Luk–Oh–Yang past-null-infinity route: same-past baseline

**Assessment: strong candidate for baseline B, independently of collapse.**
Theorem 1.7 of Luk–Oh–Yang constructs a spherical Einstein–massless-scalar
solution on the full double-null quotient `Q = {(u,v): u∈R, u≤v<∞}` that is
causally geodesically complete to both past and future from prescribed small
smooth radiation data `Φ` at past null infinity. For compactly supported `Φ`
whose support begins at `v₀`, finite-propagation uniqueness gives an exactly
flat region `v<v₀`. Thus a central marked event `b=(t_b,t_b)` with `t_b<v₀`
has its entire chronological past in this flat region. The flat reference is
the `Φ≡0` Minkowski solution. This route does not match or extend the particular
1991 collapse-cone solution.

## Exact theorem and hypotheses

The paper is arXiv:1605.03893v1 (12 May 2016), §1.2, Theorem 1.7, printed
pp5–6. In the paper's gauge, `u=v` on the regular center and
`∂ᵥr→1/2` as `u→−∞`. The data are a smooth function `Φ:R→R` satisfying, for
some `γ>0`,

`∫ᵤᵛ |Φ(v′)|dv′ ≤ ε(v−u)^(1−γ)` for every `−∞<u≤v<∞`,

`|Φ(v)|+|Φ′(v)|≤ε` on `R`, and the additional regularity condition
`supᵥ|Φ″(v)|<∞` (equation (1.20)). The theorem says that for each `γ>0`
there is a sufficiently small `ε` and a solution to the spherical
Einstein–massless-scalar system that is causally geodesically complete in both
directions and obeys

`lim_{u→−∞} 2∂ᵥ(rφ)(u,v)=Φ(v)`, `lim_{u→−∞}∂ᵥr(u,v)=1/2`.

For a nonzero compactly supported profile, choose `0<γ<1`; scaling its
amplitude makes the pointwise, derivative, and integral bounds hold. The
second-derivative bound is finite for every smooth compactly supported profile.
The paper does not assert that its example is a black-hole or collapse
solution. Its theorem statement gives a complete global solution generated as
`u₀→−∞`, not an explicit claim in the theorem's words that it is the MGHD of
complete spacelike Cauchy data. For B, the coordinator should verify the
global-hyperbolicity/Cauchy-surface and MGHD identification in the precise
regularity class before treating that label as established.

## Exact-flat-past deduction

This conclusion is not separately numbered as a corollary in the paper. It
follows from the construction and local uniqueness, with the causal-coordinate
interpretation made explicit:

1. In the approximating characteristic problem from `C_{u₀}`, the data are
   `2∂ᵥ(rφ)=Φ(v)`, with regular center values `r=m=0` and gauge
   `∂ᵥr=1/2` (Theorem 1.1, printed pp2–3; setup §2.1, printed pp7–8).
2. If `Φ(v)=0` for every `v<v₀`, then on the portion `u₀≤v<v₀` the data are
   exactly the zero-scalar Minkowski cone data. Local uniqueness and finite
   propagation keep the triangular region `u₀≤u≤v<v₀` flat.
3. Theorem 1.7 obtains its solution by taking `u₀→−∞` using estimates uniform
   in `u₀` (printed pp5–6). For each finite point with `v<v₀`, the approximating
   region is eventually present and exactly flat; the limit is therefore
   exactly flat there.
4. In `Q`, future causal curves have nondecreasing `u` and `v`. For
   `b=(t_b,t_b)` with `t_b<v₀`, every point in `I⁻(b)` has `v<t_b<v₀`; the
   marked center germ is also in the flat region. Hence the whole chronological
   past, not just a bounded diamond or its slice footprint, is Minkowskian.

This is an inference from the theorem's approximating-cone construction and
its stated local uniqueness, rather than verbatim language in Theorem 1.7.
It does not show that the same cone data as Christodoulou 1991 admit this
completion, and it does not by itself certify a fixed-time central-observer
outcome that differs from Minkowski. A nonzero `Φ` makes the global solution
nontrivial by its past-null-infinity data; pinning down a nonzero invariant
along the central geodesic at a specified proper time requires a separate
argument.

## Candidate matched-past pair and review gate

Take one admissible nonzero smooth compactly supported `Φ` with support in
`[v₀,v₁]`, scaled to Theorem 1.7's bounds, and choose `b` on the center before
`v₀`. Compare that solution with `Φ≡0`, whose development is Minkowski. Under
the theorem plus the flat-wedge deduction, the pointed models have isometric
entire `I⁻(b)`, matching the regular-center observer germ, while the radiation
solution is nontrivial to the future. This is a substantially cleaner route
to a same-past pair than the black-hole candidate.

Two scope checks remain before calling it a completed B result:

- Theorem 1.7 does not itself use the label “MGHD.” The following coordinate
  argument establishes global hyperbolicity and complete Cauchy slices. The
  normal-maximizer argument can establish maximality in a shared regularity
  category if its embedding and regularity hypotheses are verified below; it
  does not rely on C⁰-inextendibility.
- Define the `Q` outcome and prove a specific invariant/relational observable
  differs. Do not infer that a nonzero incoming profile automatically gives a
  different outcome on the central observer's worldline at an arbitrarily
  prescribed time.

## Global-hyperbolicity and MGHD audit

For smooth compactly supported `Φ`, the source provides the needed geometric
bounds uniformly in the finite-cone approximants: Theorem 1.1, equation (1.8),
has `λ=∂ᵥr>1/3`, `−2/3<ν=∂ᵤr<−1/6`, and `μ=2m/r<1/2`; §4 states that these
uniform estimates pass to the `u₀→−∞` solution. Also `m≥0`: the axis value is
zero and the mass equation (2.10), with `λ>0` and `1−μ>0`, gives
`∂ᵥm≥0` along each outgoing cone. Hence `0≤μ<1/2`. From the metric identity
(1.2),

`Ω² = −4νλ/(1−μ) > 2/9`.

Let `t=(u+v)/2` and `ρ=(v−u)/2`. The metric becomes
`−Ω²dt²+Ω²dρ²+r²dS²`, so `t` is temporal and each `t`-level is spacelike.
Along future causal curves `u` and `v` are nondecreasing. If such a curve had
a finite upper limit of `t`, both coordinates would remain bounded; its angular
part lies in compact `S²`, and the regular axis is included. It is therefore
imprisoned in a compact regular region, which strong causality rules out for an
inextendible causal curve. The past argument is symmetric. Thus the `t`-levels
are Cauchy and have topology `R³`. They are complete as Riemannian slices:
`∂ρr=λ−ν>1/2`, `r(t,0)=0`, and `Ω²>2/9`, so radial escape has infinite
induced length while the angular spheres are compact and the axis is regular.

The source's regularity statement is the gate for interpreting the geometric
argument above. Luk–Oh–Yang §4 records `C¹` compact convergence for `φ` and
the first derivatives of `rφ`, `C²` convergence for `r`, and `C¹` convergence
for `m`; Remark 4.1 specifies additional Lipschitz/weak-derivative bounds.
They call the limit a classical solution and set out regularity at the axis,
but do not state a full `C∞` spacetime metric theorem. Nor does this list,
without an additional derivation for `Ω²` including the axis, plainly establish
that the metric is `C²`. Accordingly, the bounded source audit supports the
regular full quotient and regular center used in the causal-coordinate
argument, but does not upgrade the metric to `C∞` or certify a `C²` common
development category.

## Review of coordinator's normal-geodesic maximality argument

The underlying argument is mathematically sound under its stated common-
category and embedding conditions. Treude–Grant, *Volume Comparison for
Hypersurfaces in Lorentzian Manifolds and Singularity Theorems*, arXiv:1201.4249,
Theorem 2.5 and Remark 2.4 (§2.2, preprint pp. 3–4), gives the needed standard
input: in a smooth globally hyperbolic spacetime, a Cauchy hypersurface is
causally complete, and every point to its future is joined to it by a
proper-time maximizing timelike geodesic normal to the hypersurface; the past
version is analogous. This is a theorem about a Cauchy hypersurface, not a
claim that geodesic completeness alone implies global hyperbolicity.

Suppose, more precisely, that the scattering solution is a `C²` (or smoother)
Lorentzian development and isometrically embeds into a larger globally
hyperbolic development `N` of the same marked `t`-slice `Σ`, with both metrics
in a category where the normal-maximizer theorem and geodesic initial-value
uniqueness hold. For arbitrary `q∈N` off `Σ`, Cauchy property puts it to the
future or past of `Σ`. Take the maximizing normal geodesic from `p∈Σ` to `q`.
Its initial unit normal data determine the same geodesic in the scattering
solution. Timelike geodesic completeness there extends that geodesic through
the finite proper-time parameter of `q`; the isometric embedding and ODE
uniqueness identify it in `N` with the maximizing geodesic, so `q` is in the
image. This proves there is no proper such GH extension. It does not by itself
prove the required isometric embedding of arbitrary developments: that comes
from the applicable Einstein–scalar Cauchy-development uniqueness theorem and
must use the same regularity category.

Verdict: conditional pass on the geometric proof and the maximality logic;
the available Luk–Oh–Yang text does not close the common-regularity/embedding
gate at `C²` by an explicit metric-regularity theorem. Therefore record the
paper's result as its globally hyperbolic, two-sided causally geodesically
complete classical solution, and leave its identification as the MGHD in a
specified `C²` category unresolved. An upgrade to a fully smooth category is
a separate target. No general `C⁰`-inextendibility theorem is needed for the
conditional normal-geodesic argument. This gate does not affect the exact
flat-wedge deduction within the source's own solution.

For the next, stronger control target, ask the coordinator to assess whether
this scattering family permits finite-dimensional control of a chosen
observable while a specified incoming energy or other scattering datum is
held fixed. That is beyond the basic same-past-pair deduction and should remain
a separate C-level question.

The coordinator's `NEXT_CANDIDATE.md` suggests the flat radial linear formula
`φ=[f(v)−f(u)]/r`, `r=(v−u)/2`, with regular-center limit `2f′(t)`, as a
possible guide to finite collections of central readings. Treat this only as a
linearized Minkowski heuristic. Luk–Oh–Yang Theorem 1.7 prescribes a limit of
`2∂ᵥ(rφ)` at past null infinity; it does **not** state a differentiable or
`C¹` solution-to-central-reading map in the incoming profile, nor a nonlinear
response Jacobian in the theorem's function spaces. The proposed causally later
pulse as a fixed-incoming-energy adjustment is also an unproved control step.
Neither belongs to the established pair result above.

## Limitations

- Read depth: full-text selective audit of the exact theorem, geometric setup,
  local characteristic uniqueness statement, and construction outline; not a
  line-by-line reproof of Sections 3, 4, and 6.
- Smooth compact support is a sufficient class for the theorem's stated
  regularity and smallness hypotheses, but “weak” here means amplitude small
  enough for those hypotheses, not a quantified physical energy threshold.
- Past-null-infinity data `Φ` are characteristic scattering data, not the
  1991 cone profile. No identification of the two data sets is claimed.
- The complete-past equality follows using causal order in the paper's `Q`
  coordinates and exact flatness on `v<v₀`; equality on only a finite diamond
  would not suffice.
