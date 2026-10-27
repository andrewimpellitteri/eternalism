# Exact openness versus bounded hidden-field ambiguity

27 October 2026. Coordinator sidecar, not an integrated or independently
accepted manuscript result. This supplies a quantitative upper bound while
the separate GLM mass-loss proof and philosophical/source audits run.

## 1. The distinction

In a linear unrestricted solution class, one nonzero difference solution
vanishing on the prescribed past makes a target “unfixed.” Multiplying that
solution by any number produces arbitrarily large target differences. That
observation says nothing about finite-resource alternatives unless a norm
bound is specified.

Here the norm is explicit. The result controls bounded **hidden alternatives
agreeing exactly on the whole past**. It is not a noisy-observation inversion
theorem or a claim about what an actual observer can infer from measurements.

## 2. Setup and theorem

Work on the unit Einstein cylinder with Λ²=−Δ_S³+1. For a smooth spatially
constant potential q(t), let ψ_λ and ψ_0 solve, with the same smooth data
(f,g) at the auxiliary cylinder slice t=0,

    ψ_λ,tt + (Λ²+λq(t))ψ_λ = 0,
    ψ_0,tt + Λ²ψ_0 = 0.

For 0≤t≤T define

    Q(t)=integral_0^t |q(u)| du,
    N(f,g)=[||Λf||_L²²+||g||_L²²]^(1/2).

All L² norms use the ordinary unit-S³ volume measure (total volume 2π²).
This is a conformal Cauchy-data norm, not automatically an observer's measured
energy in a dust universe. The potential is homogeneous in space; that
assumption is essential to the mode-by-mode estimate below.

**Proposition.** For every smooth data pair and real λ,

    sup_X |ψ_λ(t,X)−ψ_0(t,X)|
       ≤ |λ| Q(t) exp(|λ|Q(t)) N(f,g) / sqrt(6).       (1)

For pure velocity data f=0, sqrt(6) improves to sqrt(12) with N=||g||_L².
No claim of sharp constants is made. This estimate does not assume an echo
identity or that the mass-loss extension has passed its separate review.

## 3. Proof

### A. Mode multipliers from the elementary Volterra equation

The eigenspace indexed by k=n+1 has Λ eigenvalue k≥1. Let C_λ,k and S_λ,k
be its fundamental position/velocity solutions, with data (1,0) and (0,1).
Variation of constants gives

    C_λ,k(t)=cos(kt)−(λ/k) integral_0^t sin(k(t−u))q(u)C_λ,k(u)du,
    S_λ,k(t)=sin(kt)/k−(λ/k) integral_0^t sin(k(t−u))q(u)S_λ,k(u)du.

Gronwall's inequality and |sin|,|cos|≤1 give

    |C_λ,k(t)|≤exp(|λ|Q(t)/k),
    |S_λ,k(t)|≤exp(|λ|Q(t)/k)/k.

Writing D_C,k=C_λ,k−cos(kt) and D_S,k=S_λ,k−sin(kt)/k, substitution yields

    |D_C,k|≤ |λ|Q(t)exp(|λ|Q(t)/k)/k,
    |D_S,k|≤ |λ|Q(t)exp(|λ|Q(t)/k)/k².             (2)

For example, the integral bounding the first difference is
(|λ|/k)∫|q(u)|exp(|λ|Q(u)/k)du = exp(|λ|Q(t)/k)−1,
which is at most the first bound in (2). The position difference acting on
Λf therefore has the multiplier D_C,k/k, bounded by the same constant
times k^(-2) as the velocity difference acting on g.

### B. Why the bound is pointwise despite only an energy-type data norm

The degree-n scalar harmonics on S³ have dimension (n+1)²=k². This follows
by subtracting the dimensions of homogeneous polynomials of degrees n and
n−2 in four variables. For any orthonormal basis Y_k,j of this eigenspace,
rotation invariance and integration of its trace give the addition identity

    sum_j |Y_k,j(X)|²=k²/(2π²),                  (3)

independent of X. Put B=|λ|Q(t)exp(|λ|Q(t)). Apply Cauchy–Schwarz jointly
to the coefficients of Λf and g in the point evaluation of the difference.
Its squared operator norm is bounded by

    sum_k [k²/(2π²)] ( |D_C,k/k|² + |D_S,k|² )
       ≤ (B²/π²) sum_(k≥1) 1/k² = B²/6.

This proves (1). Removing the position-data term halves the squared bound,
giving B/sqrt(12). The summability is the extra two powers in the difference
operator. It does not assert that every individual finite-energy field has
a well-defined point value; we first work with smooth solutions. The
bounded difference functional is what extends to the indicated data norm.

## 4. Apply it to alternatives hidden from a standpoint's past

On the strip M=(0,2π)×S³ fix b=(τ,Y), 0<τ<π. Let h_λ be the difference
of any two smooth solutions of the **same perturbed equation** agreeing on
I_s^-(b). Their smooth extended data (f,g) at t=0 vanish on B(Y,τ): for each
point inside that ball, h_λ vanishes on an open interval of positive times
approaching zero, so both traces vanish there. Let h_0 be the unperturbed
solution with these same data. Finite propagation makes h_0 vanish on
I_s^-(b) too.

Consequently, for every x=(t,X) fixed by the unperturbed theory,

    |h_λ(x)|≤|λ|Q(t)exp(|λ|Q(t)) N(f,g)/sqrt(6).  (4)

Define the normalized hidden ambiguity at x by

    A_λ(b,x)=sup{|h_λ(x)| : h_λ|I_s^-(b)=0,
                               h_λ smooth, N(data at 0)≤1}.

Then (4) gives A_λ(b,x)≤|λ|Q(t)exp(|λ|Q(t))/sqrt(6) for x∈F_0(b).
This is an all-admissible-alternatives upper bound, not merely an estimate
for the particular positive bump used in the mass-loss witness.

## 5. Ordinary physical mass in the dust model

For g_dust=a(t)²g_E, a(t)=(a_m/2)(1−cos t), the conformally coupled
ordinary mass m corresponds to λ=m² and q(t)=a(t)². Here

    Q(t)=(a_m²/4)[3t/2−2sin t+(sin 2t)/4],
    Q(2π)=3π a_m²/4.

Thus bounded ambiguity of the **rescaled** field at a massless-fixed target
is O(m²), at any fixed target and with the stated conformal-data norm.
For the physical field φ=ψ/a(t), divide the bound by a(t)>0. On a compact
substrip bounded away from the singular endpoints this remains a uniform
O(m²) estimate. It is not uniform in the physical field all the way to
the crunch, because a(t) tends to zero there. The auxiliary t=0 data norm
is a mathematically stated restriction; it is not inferred from observations
or imposed by the paper's original unrestricted solution class.

The separate mass-loss argument in continuation-2026-10-27/RESULT.md proposes
a normalized positive-bump witness with nonzero first derivative. **If that
proof survives independent review**, it supplies c_x m²≤A_m(b,x) at selected
late interior targets for small m>0, and (4) supplies a matching O(m²) upper
order there. No unconditional matching-lower-bound claim is made here.

## 6. What this does and does not add philosophically

The exact predicate “all compatible solutions agree” can change when a
small mass is added while normalized compatible target differences tend
continuously to zero. Thus exact openness is not an observed unpredictability
catastrophe. A measurement claim requires a tolerance, resource norm, and an
account of access to data; the geometry and an exact classification do not
provide those choices.

With unlimited amplitudes, any nonzero hidden solution can be scaled to make
the ambiguity arbitrarily large. With N≤1, (4) prevents that rescaling.
Neither convention is neutral about the intended physical question. This
helps the paper state its contribution precisely without inferring future
existence, free agency or experimental discrimination between ontologies.

We still assume exact agreement on the whole past. Small measurement errors
in a norm on observed records are a different inverse problem. This note
does not bound them, model a detector, or establish reliable reconstruction
from a finite causal history. There is also no interaction, space-dependent
potential, quantum-field, or backreaction theorem here.

## 7. Predecessors and review status

The ingredients are classical: Volterra/Duhamel equations, Gronwall estimates,
finite propagation and the S³ spectral addition identity. This is an elementary
quantitative application to this project's hidden-alternative definition, not
a claimed new PDE estimate. Selected full text of Baskin–Mazzeo,
arXiv:1210.8053v1, §§1–2.2, was checked for the wave-equation/finite-propagation
and functional-calculus context. It is not cited as proving this exact bound.
No exhaustive priority audit was performed.

Source: https://arxiv.org/html/1210.8053v1

The explicit constants, data-norm interpretation and implication (4) require
independent review before manuscript integration. The companion mass-loss
proposition remains separately under GLM review. This work does not edit
their outputs or rely on their acceptance.
