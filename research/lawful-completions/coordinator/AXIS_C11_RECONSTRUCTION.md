# A finite-order repair: a C¹,¹ metric across the scattering axis

29 October 2026. Coordinator deduction, **awaiting independent review**.
This supplies a weaker, useful target than smoothness: the LOY limit has a
locally C¹,¹ four-metric and scalar in the Cartesian chart constructed below.
Consequently the geodesic initial-value problem is locally unique, including
at the center. It does **not** yet put the limit in the smooth category of
[SMOOTH_SCALAR_REPAIR.md](SMOOTH_SCALAR_REPAIR.md), establish a C² metric, or
license a pointwise Ricci measurement on the axis.

## 1. Exact external input

Use Luk–Oh–Yang, [arXiv:1605.03893v1](https://arxiv.org/html/1605.03893v1),
Theorem 1.1, Proposition 3.18, and §4's uniform bounds and compactness passage
immediately before (4.1). These give, on each compact quotient triangle,
uniform bounds for the finite-cone approximants at the following orders:

* all derivatives of r through order three;
* all derivatives of φ through order two;
* r_v=λ and −r_u=−ν bounded above and away from zero, and 1−2m/r≥1/2.

For clarity, the upper bound on λ also follows directly: m≥0 from its
outgoing mass equation, ν<0, and r_uv=2mνλ/[(1−μ)r²]≤0. Hence λ≤1/2
from its initial-cone normalization. Theorem 1.1 bounds −ν above and
below. No small upper bound on r's first derivatives is inferred.

The field equations are exact inputs in their own right, not consequences of
the bounds: r_uv=2mνλ/[(1−μ)r²] and (rφ)_uv=r_uvφ (the SSESF system), with
the mass equations (2.12)–(2.13). The parity identity (3) below needs the
second equation explicitly: the axis-odd lift φ=ρ satisfies the mass
equations and every derivative bound but violates (rφ)_uv=r_uvφ, and lifts
to |x|, which is not C¹. Omitting these equations from the input list would
make the statement false; the independent lift review demonstrated exactly
this failure mode.

The mixed members of the displayed order sets are not printed estimates in
LOY. The axis-inclusive u₀-uniform bound |φ_uv|≤C is supplied by the
following derivation, which uses only printed estimates and was verified
term-by-term by the independent source audit (29 October 2026,
`lawful-axis-source-review`, lemma O7) and re-derived by the coordinator the
same day. Let ψ=λ⁻¹φ_v and K=λ_u/λ=2mν/[(1−μ)r²]; expanding ∂_u(λφ+rφ_v)
and cancelling λ_uφ against r_uvφ gives ∂_u(φ+rψ)=−Krψ. Hence ψ_u=−c/r with
c:=φ_u+νψ+Krψ. If c(t₀,t₀)≠0, then ψ_u≈−c/r near the axis and du=dr/ν
makes ψ grow like log r, contradicting the printed axis-inclusive bound
(3.9); so c≡0 on Γ. Differentiating, ∂_u(rc)=rB−cKr with
B=φ_uu+ν_uψ+(Kr)_uψ, every term of which is bounded by printed inputs
(|φ_uu| from (3.55) plus nondegeneracy, |ν_u|≤Cε from (1.9), |ψ|≤Cε from
(3.9), and (Kr)_u≤C from the weighted mass bounds below); no step consumes
φ_uv, so there is no circularity. Gronwall from the axis, where rc=0, gives
|rc|≤Cr², hence |ψ_u|≤C and φ_uv=λ_uψ+λψ_u≤C. As a byproduct, c≡0 on Γ
re-proves parity (3) for φ without the expansion used there: ν=−λ on Γ
gives φ_u=λψ=φ_v there.

Pure third derivatives of r follow from (3.45), (3.47) and the lower-order
bounds. Mixed third derivatives follow by differentiating
r_uv=2mνλ/[(1−μ)r²] once: every resulting term is bounded using the weighted
mass bounds below, |ν_u|,|λ_v|≤Cε from (1.9), and m=O(r³) to kill the r⁻²
and r⁻³ quotients; the weighted mass bounds themselves consume no third
derivative of anything, so there is no circularity. This derivation was
checked term-by-term in the source audit.

Two source-fidelity caveats, recorded by the audit and respected here.
First, §4's displayed line claiming small first derivatives of r contains a
confirmed typo in its k=0 part (it contradicts (1.8) and the gauge); the
k=1,2 parts are consistent with (1.9) and Proposition 3.18, and nothing
below uses the k=0 part — Theorem 1.1 supplies the actual first-derivative
bounds. Second, the u-side halves of Proposition 3.18 are proof sketches in
v1 ("roles of u and v interchanged"); an error hidden there would degrade
the pure-third-derivative inputs to v-side statements only. The audit also
noted that §4's displayed k≥2 suprema are proved on domain-of-derivation
blocks rather than the full printed domain; on compact sets this is
harmless for the Arzelà–Ascoli argument.

The convergent subsequence has r_n→r in C² and φ_n→φ, m_n→m in C¹ on
compact quotient sets, including the axis. Thus the limit is C²,¹ for r
and C¹,¹ for φ on that quotient. Here Cᵏ,¹ means continuous derivatives
through order k with locally Lipschitz derivatives of order k. Statements
about the limit's next derivatives below are weak/a.e. statements.

Only these finite orders are used. No uniform fourth derivative, all-order
estimate, differentiable scattering map, or uniqueness at past infinity is
assumed. The argument applies to any subsequence with these bounds, also
when incoming profiles vary in a compact family with uniform source norms.

## 2. Weighted mass estimates remove the vanishing denominator

Work first with the finite-cone solutions; constants are uniform on a fixed
compact triangle whose small radial segments remain in a slightly larger
triangle. Write a,b for either null coordinate. The mass equations give

    m_v = (1−μ)r² φ_v²/(2λ),
    m_u = (1−μ)r² φ_u²/(2ν),        μ=2m/r.

The first-order field bounds and m=0 on the axis imply

    |m| ≤ C r³,       |m_a| ≤ C r².

For the first estimate integrate m_v from the axis at fixed u and use
dr=λ dv. It follows by differentiating μ off the axis that

    |μ| ≤ C r²,       |μ_a| ≤ C r.

Differentiate the displayed mass equations once. The dominant term is the
r_aφ_b² product, which is O(r); the remaining terms are O(r²) or smaller
(derivatives of λ,ν are bounded; derivatives of φ_u,φ_v are bounded by the
second-order field input; derivatives of 1−μ are O(r)). Hence

    |m_ab| ≤ C r,       |μ_ab| ≤ C.                       (1)

For the last bound the exact quotient formula is

    μ_ab = 2m_ab/r − 2(m_a r_b+m_b r_a+m r_ab)/r²
           + 4m r_a r_b/r³.

Each term is bounded by the preceding estimates. Extend μ=0 on the axis.
Its first derivatives tend to zero there, so this is a C¹,¹ extension on
the closed half-plane. Equivalently, apply the uniform estimates to the
approximants and take the limit. In particular the weak second derivatives
are bounded; no undefined division on the axis is being assigned a value.

The convergence μ_n→μ is in C¹ as well: it is ordinary quotient convergence
away from the axis, while |μ_n|≤Cρ² and |dμ_n|≤Cρ make the remaining thin
axis strip uniformly small. Here and below r and ρ are uniformly comparable.

## 3. The necessary first parity identities follow from the equations

Set t=(u+v)/2 and ρ=(v−u)/2≥0. Then

    ∂t=∂u+∂v,     ∂ρ=−∂u+∂v,
    r_t(t,0)=r_tt(t,0)=0,     r_ρ(t,0)=λ−ν=2λ>0.

The first two identities follow by differentiating r(t,0)=0 tangentially.
Since m=O(r³), the equation for r_uv gives r_uv=O(r). Therefore

    r_ρρ(t,0)=r_tt(t,0)−4r_uv(t,0)=0.                 (2)

Similarly p=rφ has p_uv=r_uv φ. Expand p_uv at the axis, using bounded
φ_uv for the approximants — supplied by the derivation in §1, which is
what makes this expansion legitimate rather than an appeal to §4's prose
sentence. The surviving term is νφ_v+λφ_u, so

    φ_ρ(t,0)=0.                                      (3)

(The §1 lemma also re-proves (3) independently: c≡0 on Γ with ν=−λ there
gives φ_u=φ_v=λψ on the axis.)

These identities pass to the limit under the stated C²/C¹ convergence.
They are precisely the finite-order identities needed below. We do not
infer an arbitrary collection of odd-derivative identities or smooth even
extensions from r(t,0)=m(t,0)=0 alone.

Define the quotient coefficient functions

    B(t,ρ) = r(t,ρ)/ρ = ∫₀¹ r_ρ(t,sρ) ds,
    A = B²,
    F = Ω² = (r_ρ²−r_t²)/(1−μ),
    D = F−A.

Because r_ρ is C¹,¹, the integral formula makes B, hence A, C¹,¹ on the
quotient. Formula (1) makes F C¹,¹ as well. At the axis (2) gives

    A(t,0)=F(t,0)=a(t)²,   a(t)=r_ρ(t,0)=2λ(t,t),
    A_ρ(t,0)=F_ρ(t,0)=0,
    D(t,0)=D_ρ(t,0)=D_t(t,0)=0.                       (4)

For example F_ρ=0 follows from r_ρρ=0, r_t=0 and μ_ρ=0. Uniform C¹,¹
bounds and (4) imply

    |D|≤Cρ²,   |D_ρ|≤Cρ,   |D_t|≤Cρ,                (5)

and bounded weak second derivatives of D. These estimates require no
second derivative of the quotient D/ρ².

## 4. Cartesian lifting lemma and proof

Let x∈R³, ρ=|x|, n_i=x_i/ρ off x=0. The four-metric is

    g_tt=−F(t,|x|),   g_ti=0,
    g_ij=A(t,|x|)δ_ij+D(t,|x|)n_i n_j.               (6)

Set g_ij(t,0)=a(t)²δ_ij. This follows directly from
g=−F dt²+F dρ²+r²dσ². The coefficients of (6) are locally C¹,¹, as the
following elementary argument shows.

A quotient C¹,¹ function H with H_ρ(t,0)=0 has a C¹,¹ radial lift:
its spatial gradient is H_ρ n_i; its second spatial derivatives off the
axis are H_ρρ n_i n_j+(H_ρ/ρ)(δ_ij−n_i n_j), which are bounded. Its
gradient extends continuously because H_ρ=O(ρ). Mixed and temporal second
derivatives are bounded as well. This treats F and A, and (3) treats φ.

For E_ij=D n_i n_j, its first spatial derivative is

    ∂k E_ij = D_ρ n_k n_i n_j
       +(D/ρ)(δ_ik n_j+δ_jk n_i−2n_i n_j n_k).

It tends to zero at the axis by (5). Its time derivative is D_t n_i n_j
and tends to zero there too. All second spatial derivatives are sums of
bounded angular factors times D_ρρ, D_ρ/ρ, or D/ρ². Mixed derivatives use
D_tρ and D_t/ρ; temporal second derivatives use D_tt. All are bounded.
Thus E_ij is C¹ across the axis with bounded weak Hessian, hence C¹,¹.
The Lipschitz estimate across the axis follows from the same two facts by a
two-case segment argument (the proof is inserted here following the
independent lift review, REPAIR-N3; the earlier sentence version asserted it
without proof). Let G=∇_{(t,x)}E and P=(t,x), Q=(s,y) in a compact ball.
Case 1: the segment PQ avoids the axis. G is C¹ on it with
|dG/ds|≤|Hess E|≤C, so |G(P)−G(Q)|≤C|P−Q|. Case 2: the segment meets the
axis at some (z*,0). Then |G(P)|+|G(Q)|≤C(ρ_P+ρ_Q)≤C(|x−z*|+|y−z*|)≤C|P−Q|,
using |G|≤Cρ from (5) and z* lying between P and Q on the segment. Hence G
is globally Lipschitz with a uniform constant and E∈C¹,¹ on the closed
half-plane, using only |∇E|≤Cρ and the off-axis Hessian bound. This avoids
assuming that D/ρ² itself has two continuous derivatives.

All constants are uniform in the finite-cone approximants. The induced
Cartesian coefficients converge in C¹ on compact sets. For E_ij the only
extra quotient in a first derivative is D/ρ, and

    |(D_n−D)/ρ| ≤ sup_{0≤s≤ρ}|∂ρ(D_n−D)(t,s)|.

Ordinary quotient C¹ convergence therefore suffices. The uniformly bounded
weak Hessians pass to the same selected limit. At the center the metric
is a(t)² times the Minkowski metric; off it F,A>0. This proves a Lorentzian
C¹,¹ metric everywhere in this atlas, not merely a quotient estimate.

## 5. What this actually closes

Since g⁻¹ is locally C¹,¹, its Christoffel symbols are locally Lipschitz.
The geodesic equation, as a first-order system for (position,velocity), has
a locally Lipschitz right-hand side on each bounded velocity set.
Picard–Lindelöf gives a unique local geodesic from each marked tangent.
This is a direct ODE deduction; a smooth geodesic theorem is unnecessary.

In particular ∂i g_tt(t,0)=0 and g_ti=0, so the center is a geodesic after
proper-time reparametrization. The exact clock is

    τ(t)=∫ from t_b to t a(s) ds = ∫ from t_b to t 2λ(s,s) ds.

The lower bound a≥2/3 makes it strictly increasing and unbounded in both
directions on the full quotient. The scalar readings and clock inversions
used in [CUBIC_TRACE.md](CUBIC_TRACE.md) and
[COMPACTNESS_CONTINUITY_REPAIR.md](COMPACTNESS_CONTINUITY_REPAIR.md) thus
have an actual unique four-dimensional geodesic interpretation, conditional
on this reconstruction passing review. Scalar readings require only the
C¹ scalar established here.

Off the axis the reduced equations imply the four-dimensional Einstein–
scalar equations. In this atlas g,φ are C¹,¹, so their second weak
derivatives are locally bounded. The axis has four-dimensional measure
zero, hence Ric(g)=2 dφ⊗dφ and wave_g φ=0 hold almost everywhere and
distributionally throughout the chart. There is no singular surface
curvature term: such a term is excluded by the C¹,¹ regularity just proved.
This is a weak solution statement, not a classical pointwise curvature
assignment at the axis.

## 6. Remaining gates and strongest objections

* **Source correspondence:** closed on 29 October 2026. The
  `lawful-axis-source-review` lane read the verbatim v1 LaTeX at full-text
  depth and verified every consumed locator, the u₀-uniformity statements,
  the typo, and the axis-inclusive availability of the mixed and third
  derivatives needed here; its O7 lemma replaces §4's prose sentence as the
  source of |φ_uv|≤C, and the coordinator has since re-derived it. Residual
  risks are recorded below rather than in this bullet.
* **Second-reader residuals:** the O7 lemma and the mixed-third-derivative
  derivation now have two readings each (source lane, coordinator). The
  u-side halves of Prop 3.18 remain proof sketches in LOY v1 and were not
  reconstructed; a defect there would weaken the pure-third-derivative
  inputs, not the lifting lemma. The lift review's O1–O19 verdicts are
  coordinator-inspected; its REPAIR-N1/N2/N3 are applied above.
* **Sharp target:** bounded weak Hessians do not establish their continuity.
  A model scalar radial function H(ρ)=ρ² sin(log ρ), H(0)=0, is C¹,¹
  after Cartesian lifting and has H_ρ(0)=0, but its Hessian has no center
  limit. It is not claimed to solve Einstein–scalar; it shows why the
  finite-order bounds alone cannot be relabelled C².
* **Smooth common development:** the smooth Ringström theorem still cannot
  be applied. One needs either stronger regularity of these particular
  scattering solutions or a field-preserving common-development theorem
  in a compatible lower-regularity class, with all of its hypotheses.
* **Curvature outcomes:** the original pointwise central Ricci functional
  in SCATTERING_PAIR.md still needs a classical-axis argument. The scalar
  finite-time control programme does not need that pointwise Ricci value.
* **Novelty:** this is a source-dependent finite-order reconstruction and
  repair to this project's proof chain. No mathematical priority or
  temporal-ontology conclusion follows from it.
