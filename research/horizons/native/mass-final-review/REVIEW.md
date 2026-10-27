# Final independent review: ordinary dust mass

Reviewed 27 October 2026. I reconstructed section 6 of `research/horizons/continuation-2026-10-27/RESULT.md` before reading the coordinator's `native/mass-recovery/RESULT_REVIEW.md` and verification record. This is an analytic proof review, not a novelty/source review.

## Verdict

**Survives analytically, with the stated fixed-background classical scope and a conditional massless-theorem premise.** The strongest potentially fatal point is the sign/pointwise positivity of the first variation: a positive operator in the Hilbert-space sense would not suffice to show a positive value at `Y`. Here the calculation gives an explicit strictly positive integral kernel, so that objection is resolved. The exceptional `k=1` coefficient is essential and is correctly incorporated.

## Reconstructed proof and exact quantifiers

Fix `a_m>0`, a standpoint `b=(τ,Y)` with `0<τ<π`, and any nonzero smooth real `g≥0` compactly supported in `S³ \ bar B(Y,τ)`. Put `T=2π`, `Λ²=−Δ+1`, and let `ψ_λ` solve

`ψ_tt + (Λ² + λa(t)²)ψ = 0`, `ψ(0)=0`, `ψ_t(0)=g`, with `λ=m²` and `a(t)=(a_m/2)(1−cos t)`.

Because the support of `g` is compact and disjoint from the closed cap, its distance from `Y` is some `ρ₀>τ`. For a point `(t,Z)` in the strip-past `I_s^−(b)`, `0<t<τ` and `d(Z,Y)<τ−t`. Its backward domain of dependence on the auxiliary slice `t=0` lies inside `B(Y,τ)`, where both data vanish. The zero-order coefficient `λa²` does not alter the principal part or its finite propagation speed. Thus `ψ_λ=0` throughout the specified open strip-past for every `λ`; this is an exact statement for the full smooth solution, not a finite spectral truncation.

Smooth interior Cauchy evolution extends the solution uniquely through `t=0,T`: the coefficient `a²` is smooth on an extended cylinder interval. Differentiating in `λ` at zero, `w=∂_λψ_λ|₀` has zero data and solves `w_tt+Λ²w=−a²S₀(t)g`. Duhamel gives

`w(T)=−∫₀ᵀ S₀(T-u)a(u)²S₀(u)g du = ∫₀ᵀ a(u)²S₀(u)²g du`,

since on eigenfrequency `k∈N`, `S₀(T-u)=−S₀(u)`. The minus sign in the forced equation and the minus sign from the periodic sine multiplier cancel; the resulting sign is positive.

For a mode of frequency `k`, direct integration yields

`∫₀ᵀ a(u)² sin²(ku)/k² du = 5πa_m²/16` for `k=1`, and `3πa_m²/(8k²)` for `k≥2`.

The `k=1` value differs from the generic formula because `a²` has a `cos(2u)` Fourier component. Since `Λ⁻²` has multiplier `1/k²` and the constant-mode projection `Π₀` selects exactly `k=1`,

`w(T)=[(3πa_m²/8)Λ⁻²−(πa_m²/16)Π₀]g`.

On unit `S³`, the kernel of `Λ⁻²` is `(π−r)/(4π² sin r)` and that of `Π₀` is `1/(2π²)`. Hence the displayed operator has kernel

`K(r)=a_m²/(32π)[3(π−r)/sin r−1]`.

For `0<r≤π`, set `x=π−r`; then `(π−r)/sin r=x/sin x≥1` (with the continuous value 1 at `r=π`). Therefore `K(r)≥a_m²/(16π)>0` on the relevant support, and `w(T,Y)=∫K(d(Y,Z))g(Z)dV(Z)>0`.

By smoothness of the extended first variation, some `ε_t∈(0,τ)` satisfies `w(t,Y)>0` for `T−ε_t<t≤T`. Choose once and for all any `s∈(0,ε_t)` and set `x_*=(T−s,Y)`. This event is interior to the dust strip and lies in `I^+(b)`; `0<s<τ`. For this fixed event and these fixed data, smooth dependence on `λ` gives `ψ_λ(x_*)=λw(x_*)+o(λ)`. Thus there is an `m_*>0`, depending on the chosen `a_m,τ,Y,g,s`, such that for **every** `0<m<m_*`, `ψ_{m²}(x_*)≠0`, while `ψ_{m²}` and zero agree exactly on `I_s^−(b)`. Therefore `x_*∉F_m(b)` for every such positive mass. The target and data are chosen before the small-mass interval; no uniform interval over targets or data is proved. Conditional on the manuscript's massless fixing theorem, `x_*∈F₀(b)`, so it is a massless-fixed event that becomes unfixed.

## Falsification attempts and repair assessment

- **Duhamel sign:** checked directly from the inhomogeneous equation and the mode identity at `T=2π`; both signs are needed and the result is positive.
- **Exceptional homogeneous mode:** the `k=1` Fourier cross-term gives `5πa_m²/16`, not the generic `3πa_m²/8`. The correction `−πa_m²Π₀/16` and the constant-projector kernel normalization are consistent.
- **Positive kernel versus positive operator:** the proof needs pointwise positivity, not just nonnegative spectrum. The explicit kernel is strictly positive for every relevant separation, including the antipode.
- **Exact past and auxiliary slice:** support separation plus finite propagation gives exact past vanishing for the untruncated smooth solution. Since `q=a²` extends smoothly, interior Cauchy evolution supplies the auxiliary endpoint values; the construction does not assume physical passage through the dust singularity.
- **Target and mass order:** continuity first fixes one `s>0` and one interior event; only then does differentiability produce an event-dependent `m_*>0`. The claim is not a target-uniform or all-events statement.
- **Different perturbations:** this is constant ordinary physical mass on dust, which becomes `λq(t)` with `q=a²` in the rescaled equation. It is distinct from the constant rescaled-potential shift `δ` (which corresponds to physical potential `δ/a²`) and is not inferred from that result.

The coordinator repair explains the abandoned numerical contradiction through RK4 component errors, use of the wrong potential in constant-potential controls, and comparison of a finite projection with an infinite-support identity. The recovered controls correct those comparisons and explicitly expose the finite-mode baseline residual/sign reversal. They corroborate finite-mode identities only; neither those controls nor the reported kernel grid establish exact past vanishing, the all-mode kernel identity, or the small-mass theorem. My verdict is based on the analytic derivation above, not the numerical pass.

## Minimal safe theorem and limitations

For each fixed `a_m>0`, `0<τ<π`, and `Y∈S³`, choose nonzero `g∈C∞(S³)`, `g≥0`, with compact support outside `bar B(Y,τ)`. Then there is a fixed `s∈(0,τ)` and a threshold `m_*>0` such that, for every `0<m<m_*`, the ordinary conformally coupled scalar of mass `m` on the fixed closed-dust background has a smooth solution agreeing with zero on `I_s^−(b)` and differing from zero at the interior event `(2π−s,Y)`. Assuming the paper's massless fixing theorem, this event belongs to `F₀(b)` and not to `F_m(b)` for every such mass.

This is a linear classical field result on a fixed background. It does not characterize `F_m`, show that every extra fixed event is lost, give a threshold uniform in choices, establish a detector-level effect, include backreaction/interactions/quantization, or select a temporal ontology. The massless fixing theorem and its source/priority audit remain external dependencies. No external literature was consulted for this review.
