# Uniform difference estimate and contraction

30 October 2026, repaired 31 October. Claude Code (Opus 5.5), at the user's
request. Exploratory, one adversarial read: REVIEW_CONTRACTION.md found no failing
line in §§1–3 and repairs R1–R5, applied here, which are single-reader. It addresses
open point 5 of RESULT.md. No novelty or ontological claim; the method is standard,
see PRIOR_WORK.md. LOY means arXiv:1605.03893v1, read as listed in that review.

## Result

**Lemma (candidate).** For compact data with an exact flat wedge, the difference
of two reduced solutions is controlled by the difference of their data with
constants independent of the cone vertex.

**Consequences, conditional on the same inputs:**

1. The whole sequence of finite-cone solutions converges, with no subsequence, and
   the limit does not depend on the sequence u_n.
2. So Φ↦S_∞(Φ) is a Lipschitz scattering map on the ball.
3. Solutions in the normalized flat-wedge class of §1 are unique at past null
   infinity. This holds in the integrated class.
4. 𝒯 is a contraction with one fixed point in the ball, and two fixed points obey
   ‖δΦ‖≤2‖δy‖ in C⁰. Φ is **not** unique for y: any bump past the window reaches
   the same readings. It is unique only causally, on the window, as in §4.
   Banach replaces Schauder and compactness in the integrated class; a retarded
   mollifier survives in the density step.

C11_FINITE_CONTROL.md states that it uses no uniqueness at past null infinity and
no selected scattering map. Those remain unused there; this would supply them for
the small compact class, as a separate candidate.

## 1. Setting

Fix A<V and ℓ=V−A, and u₀<A. Let S₁,S₂ solve the integrated system on
{u₀≤u≤v≤V}, which is all the proof uses, with the normalized wedge φ=m=0 and
r=(v−u)/2 on v≤A, and with:

    (B1) λ∈[1/3,1/2], −ν∈[1/6,2/3], 1−μ≥1/2;
    (B2) |L|+|φ|≤Cε̃;
    (B3) |L−φ|≤Cε̃ min(r,1).

(B1) is (1.8) with (3.4) for λ≤½. (B2) follows from (1.9). (B3) is (3.12) for r≤1,
and follows from (B2) for r≥1. The wedge normalization matters: geometric flatness
alone leaves a reparametrization, which breaks §4's uniqueness. Since m vanishes at
v=A for u<A and on the axis for u≥A, and m_v=½(1−μ)λ(L−φ)², these give

    (B4) m≤Cε̃² min(r³,ℓ)  for v≤V.

Then |K|≤C_ℓε̃² min(r,r⁻²). r≥c(v−u) gives ∫_(u₀)^v r₊(s,v)⁻²ds≤C, independent of u₀.
Printed (3.24) already makes ∫|K| finite, so (B4) is not what decides this. The
decisive use of the flat wedge is the left edge of δ, giving the min(r,ℓ) in the
δr, δp and δm rows. Without it δm/r²≲ε̃b/r, whose s-integral diverges
logarithmically. Right compactness of the data is not used.

Put X(u)=sup_v|δL(u,·)|, Z(u)=sup_v|δlog λ(u,·)|, and X̄(u)=sup_(s≤u)X, Z̄ likewise.
δ vanishes on v≤A, so same-u integrals run over [max(u,A),v], of length at most
min(cr,ℓ). Both X̄ and Z̄ are finite, since each solution is bounded.

## 2. Same-u table

At fixed u, all quantities below are at that level. Write b=X+ε̃Z and ϱ=min(r,1).

| Quantity | Identity | Bound |
|---|---|---|
| δr | r=(A−u)₊/2+∫λ | min(r,ℓ)Z |
| δp | p=∫Lλ | min(r,ℓ)b |
| δφ | φ=p/r | min(1,ℓ/r)b |
| δ(L−φ) | | b |
| δμ | μ=2m/r | |δm|/r+m|δr|/r² |
| δm | m_v=½(1−μ)λ(L−φ)² | ε̃ min(r²,ℓ)b |
| δ log(−ν) | ν=ν_base exp∫K′ | Z 1_(u≥A)+ε̃C_ℓ b |
| δK | K=2mν/((1−μ)r²) | C_ℓ r₊⁻²(ε̃X+ε̃²Z) |
| δM | p_u=−λL(u,u)+∫λKφ for u≥A, ∫_A^vλKφ for u<A | X+C_ℓε̃²b |

For δm: δm_v≲|L−φ|b+(L−φ)²(Z+|δμ|). With (B3) this is
≲ε̃ϱb+ε̃²ϱ²(Z+|δm|/r+m|δr|/r²). Gronwall in r has coefficient ε̃²ϱ²/r, which is
integrable over the interval.

For ν_base: if u<A then ν(u,A)=−½ exactly, and if u≥A then ν(u,u)=−λ(u,u), which
gives the Z term. δν enters K only multiplied by m/r²≤C_ℓε̃²r₊⁻².

For δK, its four terms are δm/r², (m/r²)δν, (m/r²)δμ and m|δr|/r³. For r≤1 they
give ε̃b+ε̃²r(Z+ε̃X). The bound has no rate at r=0, though δK itself vanishes there.

## 3. Absorption

At fixed v, log λ=log λ(u₀,v)+∫K ds and L=L(u₀,v)+∫K(φ−L)ds. Then

    |δ[K(φ−L)]|≤|δK||φ−L|+|K|(|δφ|+|δL|)≤C_ℓε̃²r₊⁻²(X+ε̃Z).

With the integrated weight this gives, for Z₀=Z(u₀), X₀=X(u₀),

    Z̄≤Z₀+C_ℓ(ε̃X̄+ε̃²Z̄),
    X̄≤X₀+C_ℓε̃²(X̄+ε̃Z̄).

If C_ℓε̃²≤¼, absorption gives

    X̄≤2X₀+C_ℓε̃³Z₀,    Z̄≤2Z₀+C_ℓε̃X₀.

This is W≤δ+aW→W≤2δ with a<1 and W finite, which is valid. The rejected GLM step
was W≤δ+aW→W≤δe^(aT). For a uniqueness statement with no smallness, the same
inequality read in s is Volterra with kernel k(s)=sup_v r₊(s,v)⁻²≲min(1,(A−s)⁻²),
integrable on (−∞,V].

## 4. Consequences

Same vertex: X₀=‖δΦ‖ and Z₀=0, so uniformly in u₀

    sup|δL|≤2‖δΦ‖,   sup|δlog λ|≤C_ℓε̃‖δΦ‖.

Different vertices u_m<u_n, same Φ: at level u_n the data differ only by the drift
of S_m, with Z₀≲ε̃²C_ℓ/(A−u_n) and X₀≲ε̃³C_ℓ/(A−u_n), from K≲C_ℓε̃²r⁻². Both are
normalized flat on v<A, and no other matching is needed, since the table never uses
the gauge on C_(u_n). Hence λ, L and the table's quantities are Cauchy in sup norm
on {u_n≤u≤v≤V}. Density, through the retarded mollifier of REVIEW.md, extends S_∞ to
Lipschitz Φ in the ball, as a solution of the integrated system. Limits of L are
not C¹ in v, so this lies outside LOY Definition 2.1.

Uniqueness: two solutions with the normalized wedge, (B1) and bounded L, φ, with
λ→½ and L→Φ uniformly on [A,V] as u→−∞, have X₀,Z₀→0 as u₀→−∞, so they agree by the
Volterra form. Every compact LOY limit with such data lands in this class, so all
those limits coincide with S_∞.

Contraction: from |Λ−1|≲ε̃², φ_c=Φ+∫K(φ−L) and I=Λφ_c−Φ,

    |δΛ|≲C_ℓε̃‖δΦ‖,   |δτ|≲ℓC_ℓε̃‖δΦ‖,   |δI|≲C_ℓε̃²‖δΦ‖.

So, with ε̃≍M,

    |δ𝒯|≤|δΛ||y|+Λ‖y′‖|δτ|+|δI|≤C_ℓM²‖δΦ‖≤½‖δΦ‖

for M≤M_*. 𝒯_∞ maps B to B: for t<A+δ the data vanish on v≤t, so 𝒯Φ=0 there; past
t̄+1, χ=0; and the norm bound of RESULT §2 holds for smooth Φ uniformly in the vertex
and passes to limits. B is complete in C⁰, so 𝒯_∞ has one fixed point. Two targets
with ‖y_i‖_(C¹)≤M give ‖δΦ‖≤2‖δy‖, using Λ≤1. The Lipschitz constant is O(M²), and
it does not see y″. M_* is not circular: the conditions are inequalities in M alone
once T_max and γ fix ℓ.

**Causal uniqueness.** If Φ₁,Φ₂∈B both satisfy φ_c=y∘τ up to τ=T_max, they agree up
to a common time t_*. Put T=min(t₁,t₂), apply the Lemma on {v≤s} for s≤T to get
sup_(t≤s)|δΦ|≤½sup_(t≤s)|δΦ|, so Φ₁=Φ₂ on [0,T], then τ₁=τ₂ and t₁=t₂. Past t_* the
profile is free within the ball. That freedom is exactly the late tail of C11.

## 5. Limits and what to attack

- §§1–3 use (1.8), (1.9) and (3.4), (3.12). Invariance in §4 also uses K_v, through
  (3.31) or (3.20), (3.30). Theorem 1.1 stays a trusted input, with its omitted local
  theory, its continuity argument and (3.3)'s printed φ. The bounds are used for
  smooth data and passed to the ball by closure.
- Convergence is in sup norm of the table's quantities. Derivative convergence, the
  C¹,¹ category and classical equations still need R3 of REVIEW.md and its
  third-order inputs. The smooth category is unchanged.
- C_ℓ grows with ℓ, so M_* depends on the window. Across a long tail C_ℓε̃²≤¼ may
  fail, and only the Volterra form applies.
- Repairs R1–R5 and the table have had one adversarial reading each.
- REVIEW_CONTRACTION.md's aligned tests suggest the rate Z̄≍ε̃‖δΦ‖ is sharp.

## 6. Numerics

uniformity_check.py, one pair of profiles, h=1/40, amplitude 0.3, perturbation 0.03.
Sanity check only; a finite list of vertices cannot prove uniformity. The base
profile has max|Φ′|≈2.66, far outside any ball where ε̃ is small, so this table says
nothing about the claimed regime. REVIEW_CONTRACTION.md adds smaller-data pairs.

| u₀ | sup\|δφ_c\|/sup\|δΦ\| | sup\|δlogΛ\|/sup\|δΦ\| |
|---|---|---|
| −4 | 1.158 | 0.546 |
| −8 | 1.161 | 0.555 |
| −16 | 1.163 | 0.561 |

The successive-vertex distances in sup|δφ_c| are 7.04e−4, 4.86e−4, 2.93e−4 for
(−4,−8), (−8,−16), (−16,−32). Their ratios 1.45 and 1.66 fit c/(|u₀|+a) with a≈2.3,
which predicts 1.45 and 1.67. The script does not test the constant.
