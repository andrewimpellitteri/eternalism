# Adversarial polar chart and operator audit

30 October 2026. Scope: coordinator `SMOOTHNESS_BOOTSTRAP.md` §§2–4, §6 reconstruction formulas, and the C¹,¹ axis input in `AXIS_C11_RECONSTRUCTION.md`. I did not review the exterior derivative induction or the continuation proof in §5.

## Verdict

No counterexample to the polar chart identities or to the stated radial Sobolev gain and L² Lipschitz estimates was found. The operator claim is valid with the natural convention that integer `k≥0`, the fields are radial with the Cartesian regularity used by the iteration, and constants may depend on `k,L,B,δ`. It does not require a hidden high Sobolev norm. The draft should make the scaling estimate for the *nested* ray integral and the regularity of the flow across the axis explicit; these are proof details needed to make the advertised chart and operator claims checkable.

## Chart and weak-system checks

Write `n=−ν`. The bounds in `C11_FINITE_CONTROL.md` give `λ∈[1/3,1/2]`, `n∈[1/6,2/3]`. Thus

`b=(λ−n)/(λ+n)`, and direct endpoint bounds give `−1/3≤b≤1/2`, hence `|b|≤1/2`. On a flow line `t_ρ=−b`,

`dR/dρ=r_ρ−b r_t=4λn/(λ+n)≥4/9`.

So each line is globally increasing in area radius, `R→∞` as `ρ→∞`, and there is no radial fold. At the center `b=0`; the C¹ flow derivative in the center-time label solves a scalar linear ODE and stays strictly positive on each finite segment. The time label `T=τ(t_c)` is strictly increasing since `τ′=2λ(t_c,t_c)≥2/3`. Also along a slice `u=t−ρ≤t_c−ρ/2<t_c<A` when `t_c<A`, as asserted.

The derivative identities are consistent a.e.: from `T_ρ=bT_t`, `D=∂ρ−b∂t` gives `D log T_t=b_t`; from `R=r`, `D R=(r_ρ²−r_t²)/r_ρ`. These yield `c=r_ρ/T_t` and the diagonal polar metric identities. The radial derivative is `∂R=(2ν)⁻¹∂u+(2λ)⁻¹∂v`. Combining `Q_r±P` with the two mass equations gives `m_R=fR²(P²+Q_r²)/2`; `f=1−2m/R` then gives `f_R=(1−f)/R−Rf e`.

The lapse identity checks algebraically: `∂R log c=2m/(fR²)`. Since `μ=2m/R=R²Z`, this is `RZ/f`; integration from the regular center gives `log c=R²∫₀¹s(Z/f)(sX)ds`. The mass constraint is `μ_R+(1/R)μ=R(1−μ)e`; its regular solution is

`μ(R)=R⁻¹∫₀ᴿs²e(s) exp(−∫ₛᴿz e(z)dz)ds=R²Z(R)`.

The wave equation in divergence form yields the displayed Cartesian first-order system. For radial `φ`, `Q_r=O(R)` at a regular center, so the flux through a sphere of radius `ε` is `O(ε³)` for locally bounded `c,Q_r`; its limit is zero. Thus the weak formulation has no axis delta. This argument uses the scalar divergence identity and first-order coordinate change, not distributional Ricci covariance. With smooth Cartesian `U`, the integral formulas preserve radial smoothness; `g_ij=δ_ij+(Z/f)X_iX_j`, `g_TT=−c²/f`, and `φ_T=cP` are smooth at `X=0`.

## Sobolev gain and difference bounds

Let `e=|U|²`, `||U||∞≤B`, and work on `B_L⊂R³`. For the ray operator `T_jh(X)=∫₀¹s^j h(sX)ds`, scaling gives

`||D^ℓ h(s·)||₂≤s^(ℓ−3/2)||D^ℓh||₂`.

The integral exponent is `j+ℓ−3/2`; it is greater than `−1` for `j=1,2` and every `ℓ≥0`. Thus `T₁,T₂` are bounded on each integer `H^k`, including `k=0,1`. Also, uniformly in the lower endpoint `s₀`,

`J_{s₀}[h](X)=∫_{s₀}¹ z h(zX)dz`

is bounded on `H^k`: Minkowski gives integrand norm `z^(ℓ−1/2)||D^ℓh||₂`, integrable at zero. This supplies the nested-integral estimate that the draft only summarizes.

Since `e=|U|²`, its `H^k` norm is bounded by `C_{k,B}||U||_{H^k}` (the `k=0` estimate uses `||U||∞`; for `k≥1`, the usual tame product estimate does). The exponential and reciprocal compositions use only these bounds, `L`, `B`, and `f≥δ`; on `B_L`, the exponent is bounded in `L∞` by `L²B²/2`. Hence `Z∈H^k`, `∇c=cX Z/f∈H^k`, and Poincaré/radial integration with `c(0)=1` gives `c−1∈H^{k+1}`. Constants have no dependence on `||U||_{H^{k+1}}` or another hidden high norm. The claim is for radial scalar energy and radial vector `U`; it is not a nonradial coefficient identity.

For differences, `||e_U−e_V||₂≤2B||U−V||₂`. The same scaled Minkowski estimates bound both `T₂(e_U−e_V)` and `J_s(e_U−e_V)` in L², uniformly in `s`. The exponential difference follows from its bounded arguments and the mean-value formula; products with `e_U,e_V` are controlled using their L∞ bounds. Then `f^{-1}` differences use `f_U,f_V≥δ`, and the exponential formula for `c` gives `||c_U−c_V||₂≤C||U−V||₂`. Finally `∇c=c X Z/f` gives the same L² bound for `∇c_U−∇c_V`, with `|X|≤L`. This proves (B) under exactly the stated low-order bounds. No derivative of `U−V` is used.

## Repairs and residual

1. In §2, state explicitly that the global chart conclusion is a C¹,¹ conclusion on compact sets: the C¹,¹ bounds for `b`, the center-compatible quotient/axis behavior, and the C¹,¹ ODE flow must be carried through the Cartesian map `X=(R/ρ)x`. Positivity of the finite-segment flow derivative alone gives a C¹ local inverse; cite the C¹,¹ flow theorem and verify the radial quotient at `ρ=0` to justify the claimed C¹,¹ diffeomorphism. The supplied axis identities appear sufficient, but the draft currently compresses this regularity step.
2. In §4, include the uniform lower-endpoint estimate for `J_s` above and the `k=0,1` product/composition justification. This closes the precise place where a derivative or endpoint singularity could be suspected.
3. Qualify the zero-flux sentence with local boundedness of `cQ_r` (available from the locally Lipschitz low-regularity solution); then the sphere flux is explicitly `O(ε³)`.

Strongest residual: the center-compatible C¹,¹ regularity of the *global* flow-induced Cartesian coordinate map is asserted more quickly than it is derived. This audit verifies its algebra and monotonicity but does not reconstruct every quotient-flow derivative from the C¹,¹ axis hypotheses. It is a local chart-regularity proof obligation, not a counterexample to the Sobolev gain. This audit does not certify §1's exterior estimates or §5's local existence, uniqueness, and continuation argument.
