# Prescribing a whole central scalar history

30 October 2026. Claude Code (Opus 5.5), at the user's request. Exploratory
candidate with no board claim, addressing the function-space question in
coordinator/RESPONSE_REDUCTION.md. No novelty or ontological claim. A first
version failed review; REVIEW.md gives the errors and repairs R1–R4, which are
incorporated here. R1 was rechecked by hand. R2–R4 are single-reader, and R3 and
R4 are sketches.

## Claim

**Candidate (conditional).** Fix γ∈(0,1), T_max>0 and 0<A<T_max. There is
M_*>0 depending only on T_max and γ with the following property. Let y be C¹,¹,
vanish on [0,A+2δ] and near T_max, with ‖y‖_(C¹)≤M≤M_*. There is **no size
condition on y″**. For every E≥cM²T_max there is a selected scattering limit in
the C¹,¹ category of C11_FINITE_CONTROL.md, with the same flat pointed causal
past of b, total incoming mass E, and

    φ(γ(T))−φ(b)=y(T)   for every T∈[0,T_max].

There is no N. C11 gives a schedule-dependent E_*; here the threshold depends
only on the window. For samples with spacing Δ, amplitudes up to about M_*Δ are
reached with one threshold.

**Conditional on:** Theorem 1.1 and the §3 bounds of LOY v1; Repair A; the
compactness inputs of C11; and for R3 the sketched Lemma 3.19 and (3.46)–(3.47),
or Repair B, whose qualitative regularity premise is open.

**Three limits.** For y merely C¹ the C¹,¹ category is impossible, since φ∘γ must
be C¹,¹; the conclusion is then a C¹ reduced solution with γ read as the symmetry
axis, subject to R4. Smooth y to a smooth model is open. Uniqueness of Φ is not
claimed.

The warning that trace maps may lose derivatives is answered as follows: no loss
occurs. y↦Φ has order zero, being a reparametrized identity plus a correction
that is smoothing in its dependence on Φ.

## 1. Exact axis identity

Write p=rφ, L=λ⁻¹p_v, K=2mν/((1−μ)r²), so λ_u=λK and p_uv=λKφ. On a cone at u₀
with λ=½ and L=Φ,

    2λL(u,v) = Φ(v) + ∫_(u₀)^u 2λKφ(s,v) ds.

On the axis L=φ. So, with φ_c(t)=φ(t,t),

    Λ(t)φ_c(t) = Φ(t) + I(t),
    Λ(t) = 2λ(t,t) = exp∫_(u₀)^t K(s,t)ds,
    I(t) = ∫_(u₀)^t 2λKφ(s,t) ds.

All three depend on Φ only on v≤t. The clock is τ(t)=∫₀^tΛ. Define

    𝒯Φ(t) = χ(t)[Λ(t) y(τ(t)) − I(t)],

with χ=1 up to t̄=3T_max/2, cutting to zero within one unit. A fixed point implies
φ_c=y∘τ on the window, since τ(t)≥2t/3 puts t̄ past it. The converse is not needed
and is false in general, because a fixed point also fixes Φ beyond the window.

## 2. Bounds

Use the ball with Lipschitz norm at most 2M, supported in a common window of
length ℓ≤t̄+2, so LOY's parameter is ε̃=max(1,ℓ^γ)2M. LOY v1 prints the needed
facts: (3.24) |K|≲ε̃²r₊^(−1−γ); (3.31) for K_v; (3.35) |λ⁻¹∂_vlog λ|≲ε̃²; (3.25)
and (3.29) for Λ−1 and I. Together with φ_v=λ(L−φ)/r these give

    |Λ−1|+|Λ′|≲ε̃²,   |I|+|I′|≲ε̃³,

uniformly in the cone vertex. The boundary term of I′ vanishes because K=0 on Γ.
Therefore ‖𝒯Φ‖_(Lip)≤(1+Cε̃²)‖y‖_(C¹)+Cε̃³≤2M for M≤M_*. These constants do not see
Φ″. They do see ‖Φ′‖, through the r≤1 estimates: 𝒯 is bounded Lip→Lip and not
C⁰→Lip. Off the axis, K, λ and φ_v involve L but not L_v, which is why Λ, I are C¹
for Lipschitz Φ.

The first draft claimed only Theorem 1.1's stated bounds are used. That is true of
the second-order bounds; the K, I and φ_v estimates are §3 bounds.

## 3. Continuity

At fixed n, Repair A gives continuity of the solution in C¹ data. The mollifier in
§4 is bounded C⁰→C¹, so Repair A suffices. Repair A′, dropping δL_v, also checked
on second read, is only needed if the mollifier is dropped: δ(L−φ)=O(W) with no
rate, δm=O(r²W), δK=O(W), and the fixed-v inequality is still Volterra.

## 4. Fixed point by Schauder

Let B be the functions supported in [A+δ,t̄+2] with Lipschitz norm at most 2M. It is
convex and compact in C⁰. Use a retarded mollifier

    J_ηf(t)=∫₀¹ρ(σ)f(t−ησ)dσ,   ρ smooth, supported in (0,1), η<½.

A symmetric mollifier fails, because −I is nonzero from the left edge of the data
and would be pushed left. This was the first draft's error. J_η never moves a left
edge and preserves the norm. For Φ∈B and t<A+δ the data vanish on v≤t, so Λ=1,
τ=t, y(t)=0 and I=0. Hence J_η𝒯_nJ_η maps B to B and is continuous, and Schauder
gives a fixed point. No contraction or differentiability is used, and blow-up of
continuity constants in n is harmless.

With Ψ=J_ηΦ, |Ψ−𝒯_nΨ|≤2ηLip(𝒯_nΨ) on t≤t̄, which is Λ times the trace error. Take
η_n→0.

## 5. Limit, mass and category

Ψ_n has a uniformly convergent subsequence. (1.8), (1.9) and the §3 bounds give
equicontinuity of r, λ, ν, L, M, φ, m, and |K|≲r controls the axis, so integrated
equations pass with n→∞ before u→−∞. The trace equation becomes exact. The flat
wedge passes because each approximant satisfies the C11 §4 lemma. The mass
identity needs no Φ′, because m_v=(λ(1−μ)/2)(L−φ)² is algebraic in converging
quantities, so INCOMING_MASS.md runs at this regularity.

**R2, tail.** A fixed tail counts in LOY's parameter, so it gives only E<E_*(G).
Use a truncation of LOY (5.1), G_K=Σ_(k=3)^Kχ(v−c−2^k), c≥t̄+2, amplitude β≤ε′.
Its parameter is ≲_γε′ independent of K, and (1.7) is additive. Energy grows
linearly in K, so every E above the floor is reached, with G depending on E. By
domain of dependence the tail does not change the readings.

**R3, category.** Add Lip(Φ′)≤a to B, which stays convex and compact. Prop 3.18 is
linear in A=4sup|Φ″| with ε₂ independent of A, so

    Λ″=2λ_vv+2λK_v on Γ,  |Λ″|≲ε̃(A+ε̃),  |I″|≲ε̃²(A+ε̃),

giving |(𝒯Φ)″|≤‖y″‖+Cε̃²A+Cε̃³. Then a=2‖y″‖+1 closes, and the threshold does not
see y″. Ψ_n is uniformly C¹,¹, so LOY §4 and AXIS_C11 apply.

**R4, sketch.** (𝒯_nΨ_n)′ converges uniformly, so Ψ_n→Ψ_* in C¹, and for y∈C¹ the
limit should be a C¹ solution in the sense of Definition 2.1.

## 6. Open points, strongest first

1. **Smooth y to smooth Ψ_*.** SMOOTH_FINITE_CONTROL.md assumes smooth profiles, and
   R3 stops at C¹,¹ because LOY has no uniform bounds past third order. Order-k
   bounds, linear at top order, are the missing input.
2. **R3's dependence** on the sketched third-order inputs, or on Repair B's
   open regularity premise.
3. **R2–R4** need a second reader.
4. **Trusted inputs.** Global existence rests on LOY's omitted local theory and the
   continuity argument of its §3.5, and LOY's (3.3) prints φ where Prop 3.13 closes
   rφ. The published version is uncompared.
5. **Uniform contraction.** Now in CONTRACTION.md, with one adversarial read. Φ is
   unique only causally on the window, not outright.
6. **Prior work.** Done in PRIOR_WORK.md: the setting and method are in print, and
   CARD.md records that no philosophical advance is earned.
7. M_*→0 as T_max→∞ comes from (1.7) and looks non-sharp.

## 7. Numerical attempts to falsify

volterra_check.py iterates Φ←Φ+Λ(y∘τ−φ_c) with y=ε bump(T) cos(ω(T−2)). It is a
sanity check on one domain, u₀=−4, and says nothing about uniformity in n.

| ε | ω | εω | last C⁰ ratio | last C¹ ratio |
|---|---|---|---|---|
| 0.30 | 2π | 1.88 | 0.058 | 0.060 |
| 0.10 | 6π | 1.88 | 0.008 | 0.009 |
| 0.05 | 12π | 1.88 | 0.012 | 0.009 |
| 0.033 | 18π | 1.88 | 0.009 | 0.009 |

At ω=6π, ε=0.30, 0.15, 0.075 gave 0.078, 0.019, 0.005. "Last ratio" is not a stable
rate: row 4 gives 0.0030, 0.0013, 0.0091 in sequence, and that row has about 9
points per wavelength. The ratios show no growth with ω at fixed εω, and no
derivative loss. Fixed-amplitude runs do degrade: ε=0.3, ω=12π stalled and ε=0.6,
ω=6π blew up. Those lie outside the ball, so they are not counterexamples.

## 8. A separate lead: small BV

The family's BV norm ½∫|Φ′| is independent of n. That is small only if M≲1/T_max,
which is stricter than ε̃ small. Luk–Oh arXiv:1402.2984v3, through a fetch summary,
reports Christodoulou 1993 Theorem 6.2 for global small-BV theory, Theorem 6.3 for
local BV uniqueness, and C¹ persistence. If complete, those proofs could replace
the first-order LOY input. The depth is citation only, and the original was not
read. Uniqueness there is also local, so Repair A would still be needed, and only
scale-invariant bounds can be used, because weighted norms grow with n.

## Sources and depth

LOY arXiv:1605.03893v1: printed loci as listed in REVIEW.md, read by that reviewer;
the §2 bounds rest on its reading. Luk–Oh and Christodoulou: §8 only. Kehrberger:
found by search, not read.
