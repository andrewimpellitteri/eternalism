# Adversarial audit of the C¹,¹ finite-control candidate

30 October 2026. Independent reader. Scope: `coordinator/C11_FINITE_CONTROL.md`
and its feeders. Two repairs below are this reader's own derivations. They are
single-reader work, not reviewed, and not attributed to Luk–Oh–Yang (LOY).
`claude-polar-identity-check/` was not read. No novelty or ontological claim.

## Verdict

**No counterexample and no fatal gap. The candidate survives, conditional on
LOY's first-order theorem and v-side higher bounds, but not as written:** the
proof of finite-cone continuity needs one repair and the limit's regularity
needs a second. With both, the sketched u-side of Proposition 3.18 is no
longer used anywhere. The theorem remains a conditional result.

**Strongest gap: the step S = S_x in COMPACTNESS_CONTINUITY_REPAIR step 4.**
All of H_n's continuity and even its well-definedness rest on it. C11 §2
cites "unique global reduced C¹ characteristic solution", but the source
gives less. The paragraph after (2.5) asserts uniqueness only on some slab
Q_[u₀,u₁], with the proof omitted as "a routine iteration". Theorem 1.1 says
"the unique solution" with no class named. §3.5 gets global existence from "a
standard continuity argument". Restarting at C_{u₁} leaves gauge (2.5), so a
global statement needs a regauge the notes never perform. Repair A below is a
direct Volterra uniqueness and Lipschitz estimate using only (1.8)–(1.9). It
replaces the compactness proof for H_n outright.

**Second gap:** compact convergence, the classical limit and the C¹,¹ metric
all consume (3.46), (3.47), (3.57), which v1 only sketches. AXIS §6 says a
defect there would not touch the lifting lemma. That is literally true but
understates it: C11 item 1 would fall, since F needs ν_uu. Repair B reconstructs
these bounds on compact triangles from v-side input.

## Point-by-point audit

Notation: L=λ⁻¹p_v, M=ν⁻¹p_u, p=rφ, K=2mν/((1−μ)r²), K′=2mλ/((1−μ)r²).
ε̃=C₀ε is LOY's parameter for the family.

| # | Item | Verdict |
|---|---|---|
| 1 | Finite-cone continuity | **REPAIRABLE** (A, optionally B) |
| 2 | Parameter and vertex uniformity, limit order | **VERIFIED** given B |
| 3 | Cubic remainder, clock inversion | **VERIFIED** |
| 4 | Degree, quantifier order | **VERIFIED** |
| 5 | Flat wedge, full causal past | **VERIFIED** |
| 6 | Actual incoming mass | **VERIFIED** |
| 7 | LOY hypotheses, thresholds, factors | **VERIFIED**, with one reading note |

**1. Finite-cone continuity.** Not circular: bounds are uniform over x before
any limit, and uniqueness is an input. The limit is in Definition 2.1 with
k=1 if §4's convergence holds, since p and r in C² give the listed C¹
functions, and (1.8) passes to closed inequalities, giving both infima. The
axis is handled: r=m=0 persist and the right sides extend to zero by
m≲ε̃²r³ (3.16). Note the m part is cheaper than claimed, because
m_v=(r²−2mr)φ_v²/(2λ) is polynomial in converging quantities, so no second
derivative of m is needed. Defects: the uniqueness scope above, and the
u-side consumption. The restart route also works: use Remark 2.2 with
ũ=f(u), ṽ=f(v), f′=2λ(u₁,·), giving C¹ data L(u₁,·) with uniform norm, and
step by translation invariance. Repair A is cleaner because it also removes
the omitted iteration proof from this step.

**2. Uniformity.** Fixing γ∈(0,1) first gives ε₁(γ), ε₂; then C₀(γ,family);
then ε. Nothing circular. Every LOY constant depends on γ alone, and §4's
bounds see Φ only through ε̃ and A, so §4 extends to varying Φ_{x_n} and u_n.
Prop 3.18 is on D(u₀,v₀), which exhausts Q_[u₀,∞) as v₀ grows with A global,
so the "block" concern in AXIS is harmless. The limit order is sound: for
u≥u_n both §4 remainders are inequalities at fixed (u,v), so n→∞ gives them
for the limit with Φ_{x_*}, using Φ_{x_n}(v)→Φ_{x_*}(v). Only then u→−∞. The
right sides depend on v−u≥A−u on [A,V], so convergence there is uniform.
Note §4 never mentions subsequences; C11 is right to take them, and the limit
need not be unique. Different targets may use different ones.

**3. Cubic remainder.** It can be re-derived in two lines from (1.8), (3.11),
(3.16), with no Prop 3.18. By (2.8), |log(2λ)|≤∫|K|≲ε̃²r₊^(−γ) using
|K|≲ε̃²r₊^(−1−γ) and (3.7). Since p_uv=λKφ,
|L−Φ/(2λ)|=λ⁻¹|∫λKφ|≲ε̃³r₊^(−2γ). On Γ, L=φ. Also 0≤1−2λ≲ε̃² there, using
λ≤½. Hence |φ(t,t)−Φ(t)|≲ε̃³. The clock satisfies τ≤t and
|τ(t)−t|≲ε̃²t. So 0≤t_n(T)−T≲ε̃²T on [0,T_N], and |Φ′|≤ε̃ moves the reading
by O(ε̃³). Inverse continuity uses τ′≥2/3 with factor 3/2, and t_n(T_N)≤3T_N/2
lies inside [0,2T_N+1]. Flat check: p=g(v)−g(u) gives φ(t,t)=2g′(t)=Φ(t).

**4. Degree.** Brouwer applies directly to x↦x−ε⁻¹H_n(x)+z, which maps the
closed ρ-ball to itself once Cε²<ρ/2 and |z|<ρ/2. Order: N, T_j; then
A, F_k, G, β₀, ρ, γ; then C₀, C; then ε_*. E=ε²K²/4 gives ε=2√E/K, so
|y|<(ρ/K)√E is exactly |z|<ρ/2. Neither E_* nor c depends on E or y. C does
not depend on ε because the error is C(C₀ε)³/ε. Note G lies beyond the
domain of dependence of every reading, so H_n depends on x only through ΣxₖFₖ.

**5. Flat wedge and past.** The double integral and Gronwall are correct; M
is monotone, hence measurable. p=0 forces φ=m=0, r_uv=0, λ=½, r=(v−u)/2, so
F=1. v=t+ρ is nondecreasing since t′≥|ρ′|, also across the center because
v(s) is Lipschitz with a.e. nonnegative derivative. J⁻(b)={v≤0} needs only
A>0. It holds for each approximant on {u_n≤u≤v<A} and passes to the limit.

**6. Incoming mass.** m_v=(λ(1−μ)/2)(L−φ)² is exact, from (2.10) and
rλ⁻¹φ_v=L−φ. m(u,A)=0 is exact by item 5 and continuity. On [A,V],
λ→½ and L→Φ uniformly, |φ|≲ε̃r^(−γ) with r≥(v−u)/3. μ→0 follows even without
(3.16): the integrand is bounded and 1−μ≤1, so m is bounded there and r→∞.
Thus lim m(u,V)=¼∫_A^VΦ², then V>B gives E=¼‖Φ‖₂². No exchange of limits.

**7. Hypotheses.** (1.7): min(a,L)≤L^γa^(1−γ) is correct, on all of R. (1.20)
is trivial. Φ=2p_v on the cone in Theorem 1.1, matching (2.4)–(2.5) and §4.
A=sup|(λ₀⁻¹∂_v)²Φ|=4ε sup|f″| is the correct factor. Prop 3.18 needs no
smallness of A: ε₂ is independent of A. *Reading note:* Theorem 1.1 literally
says "there exists ε" with the same ε in (1.7), which alone would not give a
scale. §3.5's "ε≤ε₁" and §3.8's "(1.7) with ε≤ε₁" do supply every smaller
value, so the scaling used here is legitimate. §4's k=0 r-derivative typo and
its leading φ typo are as COMPACTNESS says.

## Repair A: direct Volterra continuity and uniqueness

Let S, S̃ be C¹ solutions on D={u₀≤u≤v≤V₀} with λ,−ν,1−μ bounded below and
|L_v|≤B on D (from (1.9) for the family, or by continuity). Set
W(u)=sup_v(|δlogλ|+|δL|+|δL_v|)(u,v), and take all constants from D.

At fixed u, every other quantity is an integral from the axis at the *same* u:

    r=∫λ dv,  φ=r⁻¹∫Lλ dv,
    L−φ=r⁻¹∫(L(u,v)−L(u,v′))λ dv′,
    m_v=(1−2m/r)(λ/2)(L−φ)²,
    ν=−λ(u,u)exp∫K′dv.

These give |L−φ|≲r, m≲r³, and then
δr=O(rW), δφ=O(W), **δ(L−φ)=O(rW)** (this uses δL_v), δν=O(W). Linear
Gronwall in v from the axis gives δm=O(r³W). So δμ=O(r²W), δK=O(rW), δK_v=O(W),
δ(φ_v)=O(W), with no loss at r=0, because m_v/r² and m/r³ are bounded and
their differences are O(W). Integrating at fixed v from the cone:

    log λ = log½ + ∫K ds,
    L = Φ + ∫K(φ−L) ds,
    L_v = Φ′ + ∫∂_v[K(φ−L)] ds,

all legitimate in the C¹ class for s<v. Thus W(u)≤C(W(u₀)+∫_{u₀}^uW), so

    sup_D(|δλ|+|δL|+|δL_v|) ≤ C_D ‖δΦ‖_{C¹[u₀,V₀]}.

δΦ=0 gives uniqueness on D, hence globally. Since φ=L on Γ, H_n is Lipschitz,
with a constant that may blow up in n, which is harmless. The rejected worker
step W≤δ+aW→W≤δe^(aT) is not used: here the structure is a true Volterra
inequality in u, because all same-u quantities are algebraic in W(u) and the
only u-integral is the last display. No Prop 3.18 and no compactness is used.

## Repair B: u-side third order on compact triangles

Let D=ν⁻¹∂_u, Λ=log(−ν), T a triangle {a≤u≤v≤b}. Note [∂_v,D]=−K′D. From
(2.7), (2.9):

    ∂_vDM + 2K′DM = DK′(φ−M) + K′Dφ,
    ∂_vD²M + 3K′D²M = D²K′(φ−M) + DK′(2Dφ−3DM) + K′D²φ,
    ∂_vD²Λ + 2K′D²Λ = D²K′ − DK′DΛ.

The first reproduces LOY's printed (3.38) identity via
D(λ/(1−μ))=(λ/(1−μ))r(Dφ)². The other coefficients mirror printed −6mν and
−4mν terms. **Axis transfer:** L_u=K(φ−L)=0 and M_v=0 on Γ, and all mixed
terms vanish there since K,K′ vanish, giving

    DM=−λ⁻¹L_v,  D²M=(λ⁻¹∂_v)³p,  Λ_uu=(logλ)_vv  on Γ.

The last uses K_u,K_v,K′_u,K′_v as ±λQ_a with Q=K′/λ and (∂_u+∂_v)Q=0 on Γ.
It is confirmed independently: (∂_u+∂_v)²(λ+ν)=0 on Γ gives r_uuu=−r_vvv.
So axis data are bounded by v-side (3.44)–(3.45).

Along fixed v, r is a parameter with D=∂_r. Hence D²φ=∫₀¹t²D²M(tr)dt,
rD²φ=DM−2Dφ, rD³φ=D²M−3D²φ. With G=½(1−μ)(Dφ)²:
m/r²=r∫₀¹t²G(tr)dt, D²μ=2rDG+4m/r³. Using (1.8)–(1.9), (3.16), (3.36)–(3.39),
this gives |D²K′|≤C(1+Y) with Y a sup of |D²M| along that line; the
quadratic term r(D²φ)² is linear in Y because |rD²φ|≲ε̃. Set
Y(δ)=sup{|D²M|:(u,v)∈T, v−u≤δ}. Both line types stay in {v−u≤δ}, K′≥0 makes
the integrating factor at most 1, and |φ−M|=r|Dφ|. Then
Y(δ)≤a+C∫₀^δ(1+Y), and D²Λ follows.

Bounds on T depend on b−a and the listed inputs, and are uniform in vertex
and x because transport starts on Γ, not on the cone. Mixed third derivatives
follow from the equations; φ_uu follows from D²φ. Regularity: needs C³ up to Γ,
which follows from smooth Φ by the same persistence claim LOY make at k=2.

## u-side dependence of the proof

| Step | As written | After repairs |
|---|---|---|
| H_n continuity | (3.46)–(3.47), (3.57) via C² convergence | none (A) |
| Cubic, clock, degree, flat wedge, mass | none | none |
| Compact limit in C²/C¹, classical equations | (3.46), (3.47), (3.57) | none (B) |
| AXIS φ_uv (O7), C¹,¹ metric | (3.47), (3.57) | none (B) |

Without any third-order u-side input, (1.9) still gives a C¹,¹ quotient limit
in r and p with uniform convergence of φ, m, λ, ν, which suffices for the
readings, mass and flat wedge, but not for classical equations or item 1.

## External inputs taken on trust

Not reproduced by this audit:

1. Theorem 1.1: global existence of the finite-cone solution with (1.8)–(1.9),
   including the §3 bootstrap, for ε≤ε₁(γ). Local existence's "routine
   iteration" is omitted in the source.
2. Prop 3.3, 3.4, 3.16 estimates (3.10)–(3.12), (3.16), (3.36)–(3.39); Lemma 3.1.
3. Prop 3.18 v-side (3.44)–(3.45). Lemma 3.19 is labelled a sketch in v1, so
   "v-side is fully proved" is too strong; its formulas are displayed.
4. §3.8 "routine persistence of regularity", omitted in the source.

Also AXIS's lifting lemma, checked here only at its bounds and algebra: O7's
identity w_u+Kw=rB and backward integral, axis parity, F, A, D, mixed-third
orders. Those checks held. Repairs A and B reduce inputs; they do not remove 1–4.

## Read depth

- **LOY arXiv:1605.03893v1 HTML.** *Full-text at these loci*, read as printed
  TeX annotations from the page DOM in the built-in browser: Theorem 1.1,
  Remarks 1.2–1.3, Theorem 1.7, §2.1 through Remark 2.4, start of §2.2 through
  (2.7), §3.1, Prop 3.4 statement and proof, §3.5 closing paragraph, Prop 3.11,
  §3.7 to (3.39) identities (rest of its proof not read), all of §3.8, all of
  §4 through Remark 4.1. *Full-text but model-mediated (WebFetch restatement,
  not verbatim, so weaker):* (2.8)–(2.11), Lemma 3.1, Prop 3.3, 3.8, (3.24).
  **Not read:** §§5–6, Prop 3.13–3.14, Lemma 2.6 detail.
  Reproduced: nothing whole; item 3's remainders were re-derived given bounds.
- WebFetch reported 223,736 characters; the DOM text was 147,656 and ran
  through the reference list. The difference appears to be markup.
- Published Ann. PDE version: not read.
- Source oddity: (3.3) prints (λ⁻¹∂_v)²φ, while §3.5 and §3.7 treat it as
  (λ⁻¹∂_v)²(rφ), and φ is not C² in a C¹ solution. The audit uses (1.9) instead.

## Unresolved

- Repairs A and B need a second reader; A's δ-table is the place to attack.
- LOY's v-side and first-order bootstrap remain trusted; published-version
  comparison is still open.
- Not audited: C11 §§7–8 beyond arithmetic of the cone bounds, `SMOOTH_*`,
  nonisometry, and nearest-prior-result comparison.
- Definition 2.1 does not itself list 1−μ>0 or ν<0. Repair A assumes them;
  both solutions compared here have them, so its uniqueness class is this
  narrower one.

**Suggested text changes for the coordinator:** C11 §2 should cite Theorem 1.1's
unqualified "unique" and §2.1's local statement separately, and replace
"unique global reduced C¹" with Repair A or the restart argument. AXIS §6 should
state that a u-side failure would remove C11 item 1, absent Repair B.
