# Independent review: scattering-pair §§2–4

28 October 2026. This review checks the coordinator's radial uniqueness, full-past, and global-hyperbolicity derivations in `coordinator/SCATTERING_PAIR.md`. It adds no literature survey and makes no novelty claim. The external existence and regularity results of Luk–Oh–Yang remain premises here; I have not re-proved their scattering theorem.

## Radial sideways uniqueness

**Verdict: sound, conditional on the stated regularity and field equations.** In the quotient coordinates, `u=t−ρ`, `v=t+ρ`; hence `∂u∂v=(∂t²−∂ρ²)/4`. From `Ψ_uv=KΨ`, one gets exactly

`Ψ_ρρ−Ψ_tt=−4KΨ`.

This is a 1+1 wave equation with `ρ` as evolution coordinate. Its principal part is hyperbolic with respect to `ρ`; the line `ρ=0` supplies the two data `Ψ(t,0)` and `Ψ_ρ(t,0)`. This special radial reduction is essential: it does not imply uniqueness from timelike data for a general higher-dimensional wave equation.

Regularity gives `r(t,0)=0`, and thus `Ψ(t,0)=0` regardless of the centre scalar. Moreover,

`Ψ_ρ(t,0)=r_ρ(t,0) φ(t,0)`.

So the supposition `φ(t,0)=0` for every finite `t` gives zero sideways Cauchy data. The normalization of `r_ρ` is immaterial for that implication; a regular nondegenerate centre also makes it nonzero, which is useful when interpreting the centre trace.

For coefficient control, the displayed mass formula for `K` has denominator `1−2m/r`. Near a regular centre, smoothness and spherical regularity must be read as locally uniform on compact centre-time intervals: `r_u,r_v` stay bounded, `m=O(r³)` uniformly there, and `1−2m/r→1`. Consequently `K=O(1)` near the centre. On compact subsets away from the centre, `K=r_uv/r` is bounded directly by smoothness and `r>0`; no mass formula is needed there. Thus `K` is locally bounded on every compact sideways characteristic triangle. Pointwise `m=O(r³)` without locally uniform regularity would not by itself justify this compact-triangle bound, so that regularity premise should remain explicit.

On a triangle with base interval `[t₀−R,t₀+R]` on `ρ=0` and tip `(R,t₀)`, d'Alembert's formula with zero data reads

`Ψ(ρ,t)=−2∫₀^ρ∫_{t−(ρ−s)}^{t+(ρ−s)} K(s,z)Ψ(s,z) dz ds`.

If `|K|≤C` there, the integral operator is Volterra in `ρ`. Iterating it on this finite triangle gives the standard convergent uniqueness estimate with zero initial term, so `Ψ=0` on the triangle. Every finite `(ρ,t)` is the tip of such a triangle; therefore vanishing centre trace for all real `t` forces `Ψ` to vanish throughout the regular quotient. That contradicts a nonzero prescribed radiation limit `Φ`. Accordingly, the centre scalar is nonzero at some finite event. Since it is zero on the centre for `t<v₀`, smoothness and the mean value theorem give a finite centre event at which `∂tφ≠0`.

The last step assumes the source's radiation field is indeed the limit/trace of `Ψ` on the corresponding past-null-infinity end, as stated in the coordinator's external-source premise. It is not a claim that arbitrary nonzero interior scalar data imply a nonzero radiation field.

## Relational curvature reading

Given the preceding finite event and the source normalization `Ric_ab=2∂_aφ∂_bφ`, along the unit centre tangent `u^a`,

`Q=Ric_ab u^a u^b=2(u^a∂_aφ)²>0`.

For the stated constant-scalar Minkowski comparison, `Q=0`. On the centre `u=v=t`, the metric gives `dτ=Ω(t,t)dt`; the source's normalization of the axis parameter does not by itself set `Ω(t,t)=1`. Since `Ω` is smooth and positive on each compact regular centre segment, a finite interval in `t` has finite proper length, and `∂τφ=Ω(t,t)⁻¹∂tφ` is nonzero wherever `∂tφ` is nonzero. The source's complete regular quotient contains this finite centre segment, so no arbitrary-time or coordinate-matching premise is needed. This establishes one differing relational reading, conditional on the scattering-solution premises. It does not establish a detector model or equal incoming energy.

## Full past and global hyperbolicity

The full-past argument is valid on the stated quotient. For future causal curves `u` and `v` are nondecreasing, including at the regular centre by continuation. If `b` is a centre event with `t_b<v₀`, every point in its causal or chronological past has `v≤t_b<v₀`, where the solution is exactly Minkowski with `φ=0`. Under the wedge's Minkowski identification this gives the same entire past as the comparison model, and the marked centre germ agrees. This depends on the full regular quotient and exact flat-wedge premise; a truncated characteristic development would not suffice.

**Global-hyperbolicity derivation: sound under the same full-quotient premises.** In `(t,ρ)`, the radial metric is conformal to `−dt²+dρ²`; angular motion only narrows the causal cone. Thus `∇t` is timelike (including at a regular centre), so `t` is a temporal function and the spacetime is strongly causal. Along a future causal curve parametrized by `t`, `|dρ/dt|≤1`, equivalently `0≤du/dt,dv/dt≤2`. If such an inextendible curve had a finite upper `t` endpoint, `u,v` and the angular point would remain in a compact subset of the regular quotient with the centre filled in. Strong causality excludes total imprisonment there; local continuation at an accumulation point then extends the curve, a contradiction. The same argument to the past gives unbounded lower `t`. Hence every inextendible causal curve meets each `t=constant` slice exactly once, and those slices are Cauchy. Their topology is `R³`, since each quotient half-line `ρ≥0` has its `S²` collapsed at the regular centre.

This proves global hyperbolicity for the stated smooth full quotient. It does not by itself prove that the quotient is the maximal globally hyperbolic development of a particular complete Cauchy data set. The coordinator reports a new maximality argument using normal geodesics from the same Cauchy surface and completeness in both time directions; that argument is under the extension lane's separate audit and is not evaluated here. Spacelike completeness is not needed for this Cauchy conclusion.

## Disposition

The radial argument closes the existence-of-a-finite-`T` step for the relational `Q(T)` pair, conditional on the cited scattering solution's full regular quotient, exact flat wedge, radiation limit, and locally uniform centre regularity. The coordinator's full-past and global-hyperbolicity deductions also follow from those premises. This supports the proposed B-level matched-past pair on a globally hyperbolic spacetime, subject to primary-source verification of those premises. It does not certify maximality, fixed incoming energy, a prescribed time list, or a self-gravitating detector.
