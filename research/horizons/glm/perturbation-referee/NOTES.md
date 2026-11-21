# NOTES: independent derivation and falsifier attempts, written before running the authors' checks

2026-10-27. Referee: horizons-perturbation-referee (GLM headless worker).
Target: `research/horizons/continuation-2026-10-27/RESULT.md`, sections 2–4
(constant rescaled potential) and 6 (ordinary constant physical mass on dust).

Order of work: the analytic reconstruction below was done from the documents
before running any check script (the authors' or my own). I did read the
supplied `check_perturbation.py` source during context gathering; my own
numerical path below (RK4 modal time-stepping) is deliberately different from
the authors' (closed-form Duhamel integrals plus quadrature), so agreement of
the two is evidence of correctness of the shared analytic model, not of a
common coding error.

## 1. Setup restated in my notation

Einstein cylinder E=R×S³, metric −dt²+dΩ³². −Δ_{S³} has eigenvalues n(n+2),
so Λ²=−Δ+1 has eigenvalues k² with k=n+1=1,2,…; integer frequencies. Dust
strip M=(0,2π)×S³, a(t)=(a_m/2)(1−cos t), dust metric g=a(t)²g_E. Fix
b=(τ,Y), 0<τ<π, and target x_s=(2π−s,Y), 0<s≤τ.

Predicate (paper main.tex, def. before Remark rem:laws): x∈F_L(b) iff any two
solutions in the class L agreeing on I_s^-(b) agree at x. Theorem thm:diamonds
(paper, proved): for the massless conformal scalar on the closed dust strip,
0<η_b<π, F_L(b)=M∩closure(U_b), U_b the three-diamond union; on the comoving
line X=Y the fixed times are exactly 0<η≤τ and 2π−τ≤η<2π.

So x_s∈F_0(b) for 0<s≤τ (boundary s=τ included by relative closedness) — this
is the sidecar's declared conditional premise; I re-derived the comoving-line
statement independently below (§4) and found it consistent.

## 2. Class match: there are no non-extendible strip solutions

Falsifier attempt X1: "unrestricted smooth solutions on the open strip" may be
a bigger class than the manuscript's L, so the sidecar's F_δ might be a
different predicate and the conditional premise might not transfer.

Refutation: M=(0,2π)×S³ is globally hyperbolic (product), Σ_ε={ε}×S³ is a
Cauchy surface. Any ψ∈C^∞(M) solving ψ_tt+(Λ²+δ)ψ=0 (δ constant; likewise
ψ_tt+(Λ²+λq(t))ψ=0 with q smooth) has smooth Cauchy data (ψ(ε),∂tψ(ε)) on
Σ_ε; the Cauchy problem on the cylinder (equation coefficients smooth on all
of R×S³) has a unique global smooth solution v; v|_M solves the same equation
on M with the same data; uniqueness on globally hyperbolic M gives ψ=v|_M.
Hence the strip class equals restrictions of global smooth cylinder solutions.
Consequences I use later: at δ=0 every solution satisfies the echo identity
ψ(t+π,−X)=−ψ(t,X) (spectral parity), so the paper's sufficiency direction is
valid for this class; the identity genuinely fails only for δ≠0, where
frequencies √(k²+δ) are non-integer.

## 3. The mass conventions, checked both directions (falsifier X9)

This was my strongest prior suspicion: a swap of a² vs a⁻², or a sign slip in
the conformal chain, would invalidate equation (10) and everything after it.

Conformal covariance (4d, g̃=Ω²g): (□_g̃−R̃/6)(Ω^{-1}u)=Ω^{-3}(□_g−R/6)u,
taken as the definition-level input (also verified by the project's earlier
sympy check in VERIFY_DRAFT3, item 2, residual 0).

(a) Constant cylinder shift, section 4: (1) ⟺ (□_E−1−δ)ψ=0. With g_dust=a²g_E,
Ω=a, u=ψ: (□_dust−R_dust/6)(ψ/a)=a^{-3}(□_E−1)ψ, hence (1) ⟺
(□_dust−R_dust/6−δ/a(t)²)φ=0, φ=ψ/a. So constant cylinder δ = physical
mass-squared m²(t)=δ/a² on dust: large near the excluded endpoints, constant
nowhere on dust. RESULT.md §4 states exactly this. Correct.

(b) Ordinary constant physical mass, section 6: (□_dust−R_dust/6−m²)φ=0 with
u=aφ gives a³(□_E−1)ψ−m²ψ·a·a²=0, i.e. (□_E−1−m²a²)ψ=0, i.e.
ψ_tt+(Λ²+λq(t))ψ=0, λ=m², q=a². Correct direction: the physical constant
becomes the time-dependent rescaled potential a², not a^{-2}.

q(t)=a²=(a_m²/4)(1−cos t)²=(a_m²/4)(3/2−2cos t+(1/2)cos 2t). Smooth on all of
R, so the extended equation is a smooth cylinder equation. Both (a) and (b)
check out; no sign or power slip found.

## 4. My own derivation of the section-6 argument (before reading further)

Data (ψλ(0),∂tψλ(0))=(0,g), g≥0 smooth nonzero, supp g ∩ B̄(Y,τ)=∅ (compact
S³, closed disjoint sets, so ρ0:=d(Y,supp g)>τ).

Step 1 (past agreement, all λ). For z=(t,Z)∈I_s^-(b): 0<t<τ, d(Z,Y)<τ−t. The
domain of dependence of z on the t=0 slice is B̄(Z,t)⊆B̄(Y,τ) since
d(W,Y)≤d(W,Z)+d(Z,Y)≤t+(τ−t)=τ (strict < in the open cone). Zero-order terms
do not change principal symbol, so finite propagation is λ-independent. Both
φλ and 0 therefore agree (vanish) on all of I_s^-(b), for every λ, small or
not. Same argument for the δ-equation. Confirmed.

Step 2 (w equation). Differentiate ψλ_tt+(Λ²+λq)ψλ=0 at λ=0: data are
λ-independent, so w=∂λψλ|0 solves w_tt+Λ²w=−q(t)S_0(t)g, w(0)=w_t(0)=0.
Duhamel: w(t)=−∫_0^t S_0(t−u)q(u)S_0(u)g du. Sign check: the minus from the
differentiated equation and the minus from S_0(2π−u)=−S_0(u) (integer
spectrum: sin((2π−u)k)=−sin(uk)) cancel at t=2π:
  w(2π)=∫_0^{2π} q(u) S_0(u)² g du, S_0(u)² the positive multiplier
  sin²(ku)/k², q≥0. So w(2π) is a positive operator applied to g≥0. (11) confirmed.

Step 3 (mode weights, my own computation). With q=(a_m²/4)(3/2−2cos t+(1/2)cos 2t)
and ∫_0^{2π}cos(ju)sin²(ku)du=−(π/2)δ_{j,2k} (j≥1), ∫sin²(ku)du=π:
- k≥2: no j∈{1,2} equals 2k, so ∫q sin²(ku)du=(a_m²/4)(3π/2)=3πa_m²/8;
  weight 3πa_m²/(8k²).
- k=1: 2k=2 collides with the cos 2t term:
  ∫q sin²u du=(a_m²/4)[(3/2)π+0+(1/2)(−π/2)]=(a_m²/4)(5π/4)=5πa_m²/16.
So the exceptional k=1 weight 5πa_m²/16 in (12) is correct, and it is SMALLER
than the universal 6πa_m²/16, i.e. the correction is −(πa_m²/16)Π₁. Since
k=1 ⟺ −Δ eigenvalue 0 ⟺ constants, Π₁ is the spatial-mean projection Π0,
kernel 1/Vol(S³)=1/(2π²). Operator form: w(2π)=(3πa_m²/8)Λ^{-2}g−(πa_m²/16)Π0 g.
Matches (12)–(13) algebraically.

Step 4 (kernel positivity). K(r)=(3πa_m²/8)G(r)−(πa_m²/16)(1/(2π²)) with
G(r)=(π−r)/(4π²sin r). f(r)=π−r−sin r has f(0)=π, f(π)=0, f′=−1−cos r≤0, so
(π−r)/sin r≥1 on (0,π], equality only at r=π. Hence
K(r)=a_m²/(32π)[3(π−r)/sin r−1]≥2a_m²/(32π)>0, including the antipode
K(π)=a_m²/(16π). So w(2π,Y)=∫K(d(Y,Z))g(Z)dV>0. The k=1 correction cannot
destroy positivity (falsifier X3 refuted).

Step 5 (unperturbed target value is exactly zero, without the theorem).
Using the folded propagation formula (my derivation): for t∈(π,2π),
ψ0(t,X)=∂t[sin t·M_f(−X,t−π)]+sin t·M_g(−X,t−π), because every strip solution
extends to the cylinder (§2) and satisfies the echo identity. With f=0:
ψ0(2π−s,Y)=−sin s·M_g(−Y,π−s). The sphere of radius π−s about −Y is exactly
the sphere of radius s about Y, which lies in B̄(Y,τ) for s≤τ, where g≡0.
Hence ψ0(x_s)=0 exactly. This independently re-derives the paper's line
377–380 "the past light cone wraps around and refocuses near Y at the big
bang, inside what is real from b". Same formula gives the past vanishing: for
(t,Z)∈I_s^-(b), ψ0(t,Z)=sin t·M_g(Z,t)=0 because S(Z,t)⊆B̄(Y,τ).

Step 6 (loss at a fixed interior event). w is a smooth function on the
cylinder; w(2π,Y)>0 and continuity give ε_t∈(0,τ] with w(t,Y)>0 for
2π−ε_t<t≤2π. Pick t_*∈(2π−ε_t,2π); then t_*>2π−τ (so x_*∈F_0(b), conditional
premise), t_*−τ>π>0 (timelike future), t_*<2π (interior). Differentiability
in λ at 0 gives ψλ(t_*,Y)=λw(t_*,Y)+o(λ), so ∃ε′>0 with ψλ(t_*,Y)>0 for
0<λ<ε′. Pair (φλ,0)=((ψλ/a),0): agrees on I_s^-(b) (Step 1), differs at x_*
(a>0 on the strip, so ψλ≠0 ⟺ φλ≠0). Hence x_*∉F_λ(b) for every
0<m<√ε′ although x_*∈F_0(b). The conversion ψ=aφ is harmless: a>0 smooth on
the open strip, so agreement/agreement-at-x is preserved.

Quantifier audit (the brief's central question): data g and event x_* are
chosen first; then ε′=ε′(g,Y,τ,t_*)>0 works for every 0<m<√ε′. So YES: there
is a single event, in the timelike future of b and fixed by the massless
theory, such that for every sufficiently small positive ordinary mass the
perturbed theory admits two solutions agreeing on the entire chronological
past of b in the strip yet differing at that event. What is NOT claimed, and
should not be read into the result: no uniformity of ε′ over data or targets;
no characterization of F_λ(b); no claim that every late event is lost (events
with s>τ were never fixed even at λ=0); no backreaction/interaction claim.

## 5. My own derivation of the section 2–4 constant-δ case

Past agreement: same cone argument, δ-independent. h=Λ^{-2}g (Λ² invertible,
spectrum k²≥1). Resolvent kernel of (−Δ+1)^{-1} on unit S³: my derivation via
addition theorem, projection kernel ((n+1)/(4π²))sin((n+1)r)/sin r:
G(r)=Σ_{n≥0}(1/(n+1)²)·(n+1)/(4π²)·sin((n+1)r)/sin r
=(1/(4π²sin r))Σ_{m≥1}sin(mr)/m=(π−r)/(4π²sin r), 0<r<π, using
Σ_{m≥1}sin(mr)/m=(π−r)/2. G>0; near r=0, G∼1/(4πr) with unit flux;
normalization ∫_{S³}G dV=1 since (−Δ+1)^{-1}1=1. (3)–(4) confirmed:
h(Y)=∫G g dV>0.

Propagator derivative: ∂δ[sin(t√(k²+δ))/√(k²+δ)]|_0
=t cos(kt)/(2k²)−sin(kt)/(2k³); at t=2π this is π/k², so ∂δS_δ(2π)|_0=πΛ^{-2};
∂δcos(2π√(k²+δ))|_0=−sin(2πk)π/k=0. Differentiating the exact identity
S_δ(2π−s)=S_δ(2π)C_δ(s)−C_δ(2π)S_δ(s) at δ=0:
w(2π−s)=πC_0(s)h−(∂δS_δ(s)|_0)g. Second term vanishes at Y for |s|<ρ0 by
finite propagation (δ-independent cones). First term: H(t,Z)=h(Z) solves the
unperturbed homogeneous equation wherever g(Z)=0 because Λ²h=g; H and
C_0(s)h share data (h,0) on B(Y,ρ0); double-cone uniqueness gives
C_0(s)h(Y)=h(Y) for |s|<ρ0. With s≤τ<ρ0: w(x_s)=πh(Y)>0. And
ψ0(x_s)=−S_0(s)g(Y)=0 (folded formula, §4 Step 5). So
ψδ(x_s)=δπh(Y)+o(δ), nonzero for 0<|δ|<ε, two-sided in δ. The auxiliary uses
of t=0 (data) and t=2π (periodicity) are computations on the extended
solution; only interior strip values are asserted. Confirmed.

## 6. Falsifier attempts, ledger

X1 non-extendible strip solutions break class match — refuted (§2).
X2 full-cylinder-past version of the claim — the pair does NOT agree on
   t≤0 (initial velocities differ). The stated predicate is the strip past
   I_s^-(b), matching the paper's definition; a "full past" reading would
   change the claim. Scope note, not a counterexample to the stated claim.
X3 k=1 correction destroys kernel positivity — refuted (§4 Step 4).
X4 Duhamel sign error — refuted (§4 Step 2, two independent sign checks).
X5 ε_t neighborhood could miss the fixed window [2π−τ,2π) — impossible:
   ε_t≤τ keeps every t_*>2π−τ; w>0 at 2π itself.
X6 quantifier inversion (uniform ε over targets) — not claimed; correct
   order (event first, then ε) is the philosophically relevant one and is
   what is proved.
X7 ψ0(x_s)≠0 for some admissible g — refuted exactly via the refocusing
   spherical-mean formula (§4 Step 5); no truncation or theorem needed.
X8 q only defined on the strip, so no smooth extension/derivative — refuted:
   q=a² is a polynomial in cos t, smooth on R.
X9 a² vs a^{-2} mass-convention swap — refuted (§3, both directions).
X10 boundary target s=τ might fail fixedness — covered by relative
   closedness of F_0(b) (manuscript + EXACT_CLOSURE_NOTE); conditional
   premise, flagged as such.
X11 pointwise differentiability in the parameter fails for rough data —
   irrelevant: data are smooth, spectral decay is faster than any polynomial;
   multipliers are O(k^{-2}) per parameter derivative.
X12 the stationary-field step C0(s)h(Y)=h(Y) — verified by double-cone
   uniqueness on the region where g=0; h is smooth (elliptic inverse).

No falsifier survived. The remaining exposure is: (i) the conditional premise
F_0(b) from the manuscript (outside this task's scope, separately reviewed);
(ii) the stated non-uniformity limits; (iii) physical scope (fixed background,
linear, conformal coupling, phantom-free dust kinematics only as background
choice).

## 7. Search capability check (required at start)

- MCP server `web-search-prime`, tool `web_search_prime`: CALLED at start with
  a relevant query; FAILED with HTTP-style error: code 1310, "Weekly/Monthly
  Limit Exhausted. Your limit will reset at 2026-11-17 10:00:29". Recorded
  here as required by the brief.
- Fallback public web tools (built-in websearch/webfetch): WORKED. Used for
  the bounded predecessor audit in REFEREE_REPORT.md.

## 8. Planned bounded controls (standard library only)

R1 modal RK4 time-stepping of ψ_tt+(Λ²+λq(t))ψ=0 per mode with a fresh bump g
   (support [π/2,5π/8] from Y, τ=π/3, s=π/6, t_*=2π−π/6), checking
   ψλ(t_*,Y)>0 for small λ>0 and ratio convergence to my predicted w(t_*,Y);
R2 same for the constant-δ case, checking ψδ(x_s) sign(δ)>0 and the derivative
   equals πh(Y) from an independent radial Green integral;
R3 direct quadrature re-derivation of the (12) weights for k=1,2,3,5,7 by
   midpoint rule (different rule and points from the authors' Simpson);
R4 kernel positivity K(r)>0 on a grid including neighborhoods of r=0 and π;
R5 normalization ∫G dV=1 by an independent rule.
No installs; single small run; tolerances reported as observed, assertions
only on my own predicted signs and identities.
