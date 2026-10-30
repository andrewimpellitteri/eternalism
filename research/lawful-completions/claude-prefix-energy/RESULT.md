# Readings at fixed prefix masses

30 October 2026. Claude Code (Opus 5.5), at the user's request. Candidate
derivation for lawful-prefix-energy-control. It has no board claim and does not
replace that task. It is conditional on the finite-control chain, whose
independent review is still open. No novelty or ontological claim. Repairs from
REVIEW.md, an adversarial read, are incorporated here.

## Result

**Theorem (conditional).** Fix 0<T₁<⋯<T_N. On the inputs of
C11_FINITE_CONTROL.md there are a compact profile family, a positive vector
e⁰ with e⁰₁<⋯<e⁰_N<e⁰_(N+1), and constants r,ε_*>0 such that for 0<ε<ε_* and
every (z,e) within r/2 of (0,e⁰) there is a selected scattering limit with:

- the same flat pointed causal past of b;
- φ(γ(T_j))−φ(b)=εz_j for j≤N;
- prefix masses E_j=ε²e_j/4 for j≤N, with E_j defined in §1;
- total incoming mass E=ε²e_(N+1)/4.

Taking e=e⁰ fixes all N+1 masses and leaves an open ball of readings of radius
εr/2. The suggested route closes. §6 shows the construction cannot be extended
to the full mass function. Smoothness is a separate conditional clause in §5.

## 1. The cut is geometric

Let N_j be the incoming radial null cone ending at γ(T_j), which is the
boundary of J⁻(γ(T_j)) in spherical symmetry, and define

    E_j = lim m along N_j as r→∞.

Here m=(r/2)(1−g(∇r,∇r)) is the Hawking mass of the symmetry spheres, so this
needs no coordinate. In LOY gauge N_j is v=v_j, where (v_j,v_j) is the axis
point at central proper time T_j, and r→∞ along it as u→−∞. Hence
E_j=m_-(v_j). Since ν<0 and m_u≤0, m increases to E_j along N_j.

E_j is a boundary quantity of the past of the reading event. It is not a local
detector energy, not ADM mass, and not a datum at b. It is fixed at each model's
own v_j. The value of m_- at a common coordinate V is not fixed.

## 2. Family

Fix δ>0 with T_(j−1)+2δ<T_j−2δ for all j, where T₀=A∈(0,T₁). Choose smooth
nonzero functions with disjoint supports:

    supp F_k ⊂ (T_k−δ,T_k+δ),   F_k(T_k)=1,
    supp C_k ⊂ (T_(k−1)+δ,T_k−δ),
    supp G after 2T_N+1.

Put A strictly before every support. On the compact box

    R = {|x|≤ρ, |b_k−b⁰_k|≤b⁰_k/2, k≤N+1},   b⁰_k>0,

define Φ=εf, f=Σ_k(x_kF_k+√b_k C_k)+√b_(N+1) G. Every b_k stays positive, so
(x,b)↦f is continuous in C² and smooth into each fixed norm. All supports are
common. C_k and G vanish at every T_j, and F_k(T_j)=δ_kj.

Write c_k=‖C_k‖²₂, c_(N+1)=‖G‖²₂, a_k=‖F_k‖²₂, a_k⁻=∫^(T_k)F_k². Then

    L_j(x,b) = Σ_(k≤j) b_k c_k + Σ_(k<j) x_k²a_k + x_j²a_j⁻,    j≤N,
    L_(N+1)(x,b) = Σ_(k≤N+1) b_k c_k + Σ_(k≤N) x_k²a_k.

Set e⁰=L(0,b⁰). Its entries strictly increase.

## 3. Finite-cone map

For cone index n let t_(n,j) be the axis coordinate at proper time T_j, and set

    H_n,j = φ_n(t_(n,j),t_(n,j)),
    p_n,j = ∫_(−∞)^(t_(n,j)) f²  for j≤N,   p_n,N+1 = ∫f²,
    Y_n(x,b) = (ε⁻¹H_n, p_n).

p_n is built from the profile and the clock on purpose: it is not the
finite-cone mass, and §5 identifies its limit with the actual mass.

**Continuity.** COMPACTNESS_CONTINUITY_REPAIR.md applies with parameter space R,
so H_n and t_(n,j) are continuous. The integral is jointly continuous in its
upper limit and in (x,b), so p_n is continuous. No Lipschitz bound is needed.
That note leans on a global uniqueness statement which LOY v1 does not prove.
Repair A in ../claude-finite-control-audit/RESULT.md gives the same continuity
directly, since (x,b)↦Φ is continuous in C¹.

**Estimates.** With the same source inputs and ε̃=C₀ε for this family,
CUBIC_TRACE.md gives |t_(n,j)−T_j|≤Cε² and |φ_n(t,t)−εf(t)|≤Cε³. Since
f(T_j)=x_j and |f′|≤M,

    |ε⁻¹H_n,j−x_j| ≤ Cε².

For ε small, t_(n,j) stays in (T_j−δ,T_j+δ), so the cut stays in the support
window of F_j. Therefore

    |p_n,j−L_j| ≤ sup f²·|t_(n,j)−T_j| ≤ Cε².

In mass units this is the suggested O(ε⁴) prefix error. All constants are
uniform in n and (x,b). Compensators have no effect on readings at order ε or
ε², because the leading central response is local in t. They do enter at order
ε³, for example through the clock shift.

## 4. Joint degree

Let Y⁰(x,b)=(x,L(x,b)). It is smooth and injective on R, by triangular
inversion: given (x,e),

    b_j=(e_j−e_(j−1)−x_j²a_j⁻−x_(j−1)²(a_(j−1)−a_(j−1)⁻))/c_j,

with e₀=0 and the x_0 term absent, and

    b_(N+1)=(e_(N+1)−e_N−x_N²(a_N−a_N⁻))/c_(N+1).

Its Jacobian is block triangular with determinant Π_(k≤N+1)c_k>0. Y⁰ is the
restriction of a polynomial shear, which is a diffeomorphism of R^(2N+1), so
Y⁰(∂R) is the boundary of Y⁰(R). Any r>0 with r<ρ and
(2r+2r²max_k a_k)/c_j<b⁰_j/2 for all j gives a ball B_r(0,e⁰) inside Y⁰(R), and
its concentric half ball stays more than r/2 from Y⁰(∂R). Here r does not depend
on ε, n or the target.

If Cε²<r/2, the homotopy Y⁰+s(Y_n−Y⁰) has no zero of (·)−w on ∂R for w in that
half ball. Hence deg(Y_n,R,w)=deg(Y⁰,R,w)=1, and every such w has a root
(x_n,b_n) with Y_n(x_n,b_n)=w. All 2N+1 equations are solved together. This is
before any limit, and no differentiability of H_n is used.

## 5. Limit and actual masses

Extract (x_n,b_n)→(x_*,b_*)∈R. The argument of C11_FINITE_CONTROL.md §6 with
varying profiles gives a global limit with profile Φ_*, n→∞ before u→−∞. Clock
and axis convergence pass H_n and t_(n,j) to the limit, and the exact flat wedge
persists because every profile vanishes before A.

Since t_(n,j)→t_j and the profiles converge, p_n,j→∫^(t_j)f_*². INCOMING_MASS.md
holds at every finite V>A in the limit, so

    m_-(t_j)=¼∫^(t_j)Φ_*²=ε²p_j/4=ε²e_j/4.

By §1 this is E_j. For the total use its V→∞ statement. Different targets may
use different subsequences. No global scattering map or uniqueness at past null
infinity is used.

**Category (separate conditional clause).** The Theorem is stated in the
C¹,¹ category of C11_FINITE_CONTROL.md. A smooth upgrade would need the chain of
SMOOTH_FINITE_CONTROL.md and all its external inputs. Its proof appears not to
depend on the family, since it uses all-order profile norms and A strictly
before the supports, but that note speaks of C11's families and this has not
been separately checked. r, m and N_j are geometric, so each E_j survives the
C¹,¹ change of atlas.

## 6. A limit on the construction: finite cuts, not the full function

Work in selected limits of compact smooth profiles with flat wedge v<A and LOY
smallness ε̃=C₀ε. Normalize V by v=t on the wedge and λ→½ as u→−∞. Write
y_i,j=φ_i(γ(T_j))−φ_i(b). CUBIC_TRACE.md carries its trace bound to any compact
limit, so no uniqueness at past null infinity is needed.

**(a) Equal m_- as functions of V.** Then |Φ₁|=|Φ₂| at every V, including zeros,
and |Φ₁| is Cε-Lipschitz. With t_i=t_i(T),

    |φ₂(T)| = |Φ₂(t₂)|+O(ε³) = |Φ₁(t₂)|+O(ε³) = |Φ₁(t₁)|+O(ε³) = |φ₁(T)|+O(ε³).

The sign is not used, and should not be: t₁ and t₂ may lie on opposite sides of
a zero of Φ₁.

**(b) Equal E(T)=m_-(t(T)) on an interval of proper time.** This is the function
the Theorem's cuts sample, and Φ₁²=Φ₂² does not follow from it, because clocks
differ. Since t′(T)=1/(2λ) on the axis,

    E′(T)=Φ²(t(T))/(8λ),    2λ=1+O(ε²),

so |Φ₁(t₁)|=|Φ₂(t₂)|(1+O(ε²)), and |φ₂(T)|=|φ₁(T)|+O(ε³) again.

In either case ||y₂,j|−|y₁,j||≤Cε³ for each j, so

    y₂ ∈ ∪_σ Π_j [σ_j|y₁,j|−Cε³, σ_j|y₁,j|+Cε³],

which is at most 2^N boxes of side 2Cε³. Components merge when |y₁,j|≤Cε³, and
then the sign of that reading is undetermined. A ball of radius above Cε³ is
impossible, whereas §4 gives radius comparable to ε at finitely many cuts.

This is not a threshold result. It contrasts finite cut lists with a continuum
at fixed ε. Longer finite lists appear reachable with list-dependent r and ε_*,
though that is not written out, and the order ∀list∃ε_* must not be exchanged.
It says nothing about structure below order ε³.

## 7. Scope and limits

- All of §§3–5 inherits the finite-control inputs: continuity, uniform cubic
  remainder, varying-profile compactness, and the incoming-mass identity.
  A failure there fails here.
- The chart is local near b⁰, but every positive strictly increasing vector is
  an e⁰, taking b⁰_k=(e⁰_k−e⁰_(k−1))/c_k. Only r and ε_* depend on that choice
  and on the schedule, and the scale of e⁰ is not a free large parameter.
- Fixed E_j fixes the mass between adjacent cuts, E_j−E_(j−1). It does not fix
  the mass in a proper subinterval meeting a varying pulse. The compensators
  still differ between models, and so does exterior data.
- Fixed E_j is a statement about models compared across the family. It is not a
  claim that an observer at b can access E_j, and E_j for j≥1 is not in the
  causal past of b.
- No code was used for this argument. Nothing here selects an ontology.
