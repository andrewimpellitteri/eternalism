# RESULT — independent adversarial review of AXIS_C11_RECONSTRUCTION.md

29 October 2026. Worker: `lawful-axis-lift-review` (red team). Coordinator claim
under review: the LOY limit has a locally C^{1,1} four-metric and scalar in an
explicit Cartesian chart, with uniform bounds, C¹ convergence of the selected
subsequence, and the geodesic/weak-field consequences of §5. The claim is
**unaccepted**; this review tries to refute it. **Verdict: the analytic argument
survives line-by-line scrutiny after deliberate attack; two specification-level
defects need repair (one hypothesis omission that is load-bearing, one asserted
lemma that must be proved); no fatal gap found.** Details and exact repairs
below. This is a submission for coordinator review, not an accepted truth.

## 0. Method and separation of layers

Per the brief, three layers are kept separate:

* **L1 (pure analytic lemma).** Hypotheses only, no source. This is the layer I
  own. Hypotheses are stated in §1 below; everything in §§3–6 is conditional on
  them and on nothing else.
* **L2 (source-to-lemma correspondence).** Whether Luk–Oh–Yang v1 actually
  supplies the uniform input orders, including the axis. I pin what I could
  verify first-hand and record the rest as an open gate for the source lane.
* **L3 (interpretation).** Geodesic, clock, and weak-field conclusions are
  assessed as separate, weaker statements. No ontology, no smooth MGHD upgrade,
  no novelty or priority claim is made here (the coordinator likewise claims
  none, §6 of their document).

Verification assets: hand proofs (this file), a pure-stdlib finite-difference
check script `verify_checks.py` (14 checks, 0.04 s wall), and primary fetches
recorded in `sources.jsonl`. No check replaces an analytic proof; they only
corroborate formulas and sharpness models.

## 1. Explicit hypotheses (L1 input)

* **(H1)** r_n ∈ W^{3,∞} on each compact quotient half-triangle T (u ≥ v side
  of the axis, i.e. the closed set ρ ≥ 0), with uniform bound; r_n → r in C¹
  up to order 2 **including the axis**; r(t,0) = 0.
* **(H2)** φ_n ∈ W^{2,∞} on T with uniform bound; φ_n → φ in C¹ **including
  the axis**.
* **(H3)** Each (r_n, φ_n, m_n) solves the quoted SSESF system on T:
  * (E1) m_v = (1−μ)r²φ_v²/(2λ), m_u = (1−μ)r²φ_u²/(2ν), μ = 2m/r;
  * (E2) r_uv = 2mνλ/[(1−μ)r²];
  * (E3) (rφ)_uv = r_uv φ.
  m_n = 0 on the axis.
* **(H4)** Nondegeneracy, uniform: 0 < c ≤ λ = r_v ≤ C, −C ≤ ν = r_u ≤ −c,
  1−μ ≥ 1/2 (hence μ ≤ 1/2), all on T.

> **Specification note (OBJ-1).** The task brief's hypothesis list names "mass
> equations and nondegenerate λ/ν" but not (E2)/(E3). The coordinator's §3
> genuinely consumes both. I verified by direct derivation that (E3) is not a
> restatement of anything in (E1): the mass equations constrain m given r, φ,
> and impose **no** axis condition on φ. Hence φ_ρ(t,0)=0 is *not* derivable
> from (H1),(H2),(E1),(H4) alone. This is load-bearing; see §3/O8 and §7.

Derivative budget consumed (max order used anywhere below): **third derivatives
of r, second derivatives of φ** — both inside (H1),(H2). I audited every step
for a hidden extra derivative; none exists (audit table in §6). No step
differentiates D/ρ² or any quotient twice; the coordinator's stated avoidance
is correct and was checked.

## 2. Weighted mass estimates — verdicts O1–O4

**O1. m = O(r³) — CORRECT.** Integrate (E1) along fixed u from the axis using
dr = λ dv and λ ≥ c: |m(u,v)| ≤ ∫₀^r C r'² dr' = C r³/3, with C uniform (uses
|φ_v| ≤ C from (H2), 1−μ ≥ 1/2). Constants uniform on T. ✔

**O2. m_a = O(r²) — CORRECT.** Direct from (E1): |m_a| ≤ (1/2)(1)·r²·C/c = C r².
No integration needed. ✔

**O3. m_ab = O(r) — CORRECT, with a wording repair.** Differentiating (E1) once
(e.g. in u):
1. −μ_u r²φ_v²/(2λ): μ_u = 2m_u/r − 2m r_u/r² = O(r) by O1,O2 ⇒ term O(r³).
2. (1−μ)·2r r_u·φ_v²/(2λ): r_u = ν bounded ⇒ **term O(r) (dominant)**.
3. (1−μ)r²φ_v φ_vu/λ: φ_vu bounded by (H2) ⇒ term O(r²).
4. −(1−μ)r²φ_v²λ_u/(2λ²): λ_u = r_vu bounded by (H1) ⇒ term O(r²).
All ⊂ O(r) on compacta; conclusion |m_ab| ≤ C r holds with uniform C. Mixed
(m_uv), pure (m_uu, m_vv), and time-rotated combinations (m_tρ = −m_tu + m_tv
with m_tu = m_uu + m_uv, m_tv = m_uv + m_vv) all inherit O(r); m_tt = O(r²) by
the identical budget (needed for μ_tt below).

*REPAIR-N1 (wording, cosmetic).* The coordinator's §2 sentence "Every term is
O(r)" is imprecise: terms 3–4 are O(r²) and term 1 is O(r³); only term 2 is
exactly O(r). The stated bound |m_ab| ≤ C r is nonetheless correct and even
slightly suboptimal (O(r) is what is used). No mathematical consequence. ✔

**O4. μ = 2m/r extends C^{1,1} across the closed half-plane — CORRECT.** Off
the axis, the exact quotient identity holds:

μ_ab = 2m_ab/r − 2(m_a r_b + m_b r_a + m r_ab)/r² + 4m r_a r_b/r³,

which I verified symbolically-by-fd on a model (check B: agreement to 6 digits
for (rr), (tr), (tt)). Term bounds: 2m_ab/r ≤ 2C (O3); 2m_a r_b/r² ≤ C (O2,
(H4)); 2m r_ab/r² = O(r) (O1, (H1)); 4m r_a r_b/r³ ≤ C (O1 kills the 1/r³; no
lower bound on r beyond r ≥ 0 is used). So the weak Hessian is uniformly
bounded off the axis. Axis extension: define μ(t,0)=0. First derivatives:
μ_a = 2m_a/r − 2m r_a/r² = O(r) → 0; μ_t = 2m_t/r − 2m r_t/r² with
m_t = m_u + m_v = O(r²) ⇒ μ_t = O(r) → 0. Second derivatives: μ_tt is bounded
(m_tt = O(r²), r_tt, r_t bounded), μ_tρ bounded (m_tρ = O(r) from O3's budget
plus W^{2,∞}(r)). Hence μ ∈ W^{2,∞}(T) with continuous first derivatives and
μ = dμ = 0 on the axis; by Morrey (W^{2,∞} ⊂ C^{1,1}) μ is C^{1,1} on the
closed half-plane. The coordinator's closing remark — no undefined division is
assigned a value on the axis — is accurate. ✔

**μ_n → μ in C¹ — CORRECT.** Ordinary quotient convergence off the axis; in the
strip ρ < δ, |μ_n − μ| ≤ Cρ_n² + Cρ² ≤ Cδ and |dμ_n − dμ| ≤ Cρ_n + Cρ ≤ Cδ,
using r_n, r uniformly comparable (B_n(t,ρ) = ∫₀¹ r_{nρ}(t,sρ)ds ≥ 2·(1/3) − Cρ
≥ c > 0 by (H4) and (H1)). ✔ (Uses LOY Theorem 1.1's (1.8): r_v > 1/3, which I
verified verbatim in the ar5iv fetch of v1 §1.)

## 3. Parity identities — verdicts O5–O8

Coordinates t = (u+v)/2, ρ = (v−u)/2 ≥ 0, so ∂t = ∂u + ∂v, ∂ρ = −∂u + ∂v. For
any C² X: X_ρρ = X_uu − 2X_uv + X_vv = X_tt − 4X_uv (verified numerically,
check A).

**O5. r_t(t,0) = r_tt(t,0) = 0 — CORRECT.** Tangential differentiation of
r(t,0) ≡ 0; passes to the C² limit. ✔

**O6. r_ρ(t,0) = λ − ν = 2λ =: a(t) > 0 — CORRECT and internally forced.**
r_ρ(t,0) = −r_u + r_v = ν + λ at u = v = t; but r_t(t,0) = 0 gives
ν(t,t) + λ(t,t) = 0, so ν = −λ on the axis and r_ρ(t,0) = λ − ν = 2λ. The
coordinator's display is exactly this identity (it is *not* an extra sign
convention). With (1.8)'s λ > 1/3, a ≥ 2/3, matching §5's clock bound. ✔

**O7. r_ρρ(t,0) = 0 — CORRECT.** r_ρρ(t,0) = r_tt(t,0) − 4r_uv(t,0);
r_uv(t,0) = 2mνλ/[(1−μ)r²] → 0 by O1 (m = O(r³) kills the 1/r²), both sides
continuous off the axis and extending continuously to it. ✔

**O8. φ_ρ(t,0) = 0 — CORRECT *given (E3)*; the identity (E3) is a required
hypothesis.** Two equivalent routes, both verified:
* Route 1 (coordinator's): expand (rφ)_uv = r_uv φ + λφ_u + νφ_v + rφ_uv using
  (E3) r_uv φ on the right. At the axis: r_uv φ = 0 by O7, rφ_uv = 0 since
  r = 0, so 0 = λφ_u + νφ_v = −λφ_ρ(t,0) (using ν = −λ on axis and
  φ_u = (∂t − ∂ρ)φ/2 etc.), hence φ_ρ(t,0) = 0. Requires φ_uv bounded
  ((H2)) for the expansion to be legitimate; ✔.
* Route 2 (independent check I derived): for g = −Ω²du dv + r²dσ² the wave
  equation is exactly φ_uv = −(ν/r)φ_v − (λ/r)φ_u (the Ω-terms cancel: √|g|g^{uv}
  = −2r², so no Ω_u/Ω_v terms appear). Multiplying by r gives (rφ)_uv = r_uv φ.
  So (E3) ⇔ wave equation, and route 2 reproduces route 1 exactly.
  (LOY's own (SSESF) second equation is literally ∂u∂v(rφ) = [2m∂u r ∂v r /
  ((1−2m/r)r²)]φ = r_uv φ — verified verbatim in the ar5iv fetch of v1.)
* It passes to the limit by (H2) C¹ convergence (φ_{n,ρ}(t,0) = 0 ∀n).

> **OBJ-1 (strongest objection found).** Without (E3), O8 is **false** and the
> scalar part of the theorem fails: φ(t,ρ) = ρ satisfies (H1)–(H2),(E1),(H4)
> bookkeeping (the mass equations see only φ_a², insensitive to axis parity)
> and lifts to φ_cart = |x|, which is not C¹ (check F: p_uv − r_uv φ = −1/2 ≠ 0
> on the flat model; axis-even φ = f(t) gives 0). The four-metric claims are
> unaffected (they use O7, not O8). **REPAIR-N2 (required):** state (E2) and
> (E3) explicitly in the hypothesis list of the reconstruction note. Trivial
> repair — the equations are exactly LOY's (SSESF) — but the coordinator's §1
> currently lists only "the mass equations" and LOY derivative bounds, so the
> note as written does not formally contain one of its own needed inputs.

## 4. Quotient coefficients and the (5) bounds — verdicts O9–O10

**O9. B = r/ρ, A = B², F = (r_ρ² − r_t²)/(1−μ), D = F − A are C^{1,1} with
uniform bounds; axis values (4) hold — CORRECT.**
* B ∈ W^{2,∞} via the Hadamard formula B = ∫₀¹ r_ρ(t,sρ)ds (needs r_{ρtρ},
  r_{ρρρ}: third derivatives of r — within (H1); **this is the only step that
  consumes W^{3,∞} rather than W^{2,∞} of r**). A = B² ∈ W^{2,∞}.
* F: numerator N = r_ρ² − r_t² ∈ W^{2,∞} (third derivatives of r); reciprocal
  1/(1−μ) ∈ W^{2,∞} (O4 and 1−μ ≥ 1/2); product closure ⇒ F ∈ W^{2,∞} ⊂
  C^{1,1}. Note F = −4νλ/(1−μ) exactly, since r_ρ² − r_t² = (λ−ν)² − (λ+ν)² =
  −4λν — consistent with LOY's definition (1.2) Ω² = −4∂u r ∂v r/(1−2m/r),
  which I verified verbatim in the primary fetch.
* Axis values: A(t,0) = B(t,0)² = a(t)²; F(t,0) = −4λν/(1−0) = (2λ)² = a²; ✔
  A_ρ = 2BB_ρ, B_ρ(t,0) = r_ρρ(t,0)/2 = 0 ⇒ A_ρ(t,0) = 0; F_ρ(t,0):
  F_ρ = (2r_ρ r_ρρ − 2r_t r_tρ)/(1−μ) + N μ_ρ/(1−μ)², and at the axis the first
  term dies by O7 (r_ρρ = 0) and O5 (r_t = 0), the second by O4 (μ_ρ = 0) ⇒
  F_ρ(t,0) = 0 ✔. D_t(t,0): F_t(t,0) = 2r_ρ r_ρt(t,0) = 2aa′ (using
  μ_t(t,0) = 0, r_t(t,0) = 0), and B_t(t,0) = r_ρt(t,0) = a′ so
  A_t(t,0) = 2BB_t = 2aa′; hence D_t(t,0) = 0 ✔. (4) fully verified.
  This confirms the coordinator's "r_ρ is C^{1,1} ⇒ B C^{1,1}" phrasing only
  via the integral formula; their text is fine, but note the integral formula
  is what avoids needing r/ρ to be C².

**O10. |D| ≤ Cρ², |D_ρ| ≤ Cρ, |D_t| ≤ Cρ, bounded weak second derivatives of D
— CORRECT, and correctly free of D/ρ² derivatives.** D ∈ W^{2,∞} with
D(t,0) = D_ρ(t,0) = D_t(t,0) = 0; fundamental theorem in ρ gives the three
linear-quadratic bounds; D_tρ, D_tt, D_ρρ ∈ L^∞ give the weak-Hessian bound.
**No second derivative of D/ρ² is ever taken** — audited, confirmed. ✔

## 5. Cartesian lifting — verdicts O11–O15

Chart: x ∈ R³, ρ = |x|, n_i = x_i/ρ; g_tt = −F(t,|x|), g_ti = 0,
g_ij = A(t,|x|)δ_ij + D(t,|x|)n_i n_j, g_ij(t,0) = a(t)²δ_ij. I verified the
decomposition independently: F dρ² contributes F n_i n_j and r²dσ² contributes
(r²/ρ²)(δ_ij − n_i n_j) = A(δ_ij − n_i n_j), so g_ij = Aδ_ij + (F−A)n_i n_j
with A = r²/ρ² = B², D = F − A exactly. ✔

**O11. Scalar-type lift (F, A, φ_cart) — CORRECT.** For quotient H ∈ C^{1,1}
with H_ρ(t,0) = 0: ∇H_cart = H_ρ n = q·x with q := H_ρ/ρ bounded (≤ C from
O10-type bounds); second derivatives off the axis are H_ρρ n_i n_j +
(H_ρ/ρ)(δ_ij − n_i n_j) — bounded; mixed/time blocks H_tρ n_i, H_tt bounded.
Hence H_cart ∈ W^{2,∞}_loc(R_t × R³) ⊂ C^{1,1}, uniformly in n. Continuity of
the gradient at the axis is exactly the hypothesis H_ρ(t,0) = 0. ✔

**O12. Tensor lift E_ij = D n_i n_j — CORRECT; the asserted lemma is true, and
I supply the missing proof.** 
* First derivative formula (verified by fd, check D):
  ∂k E_ij = D_ρ n_k n_i n_j + (D/ρ)(δ_ik n_j + δ_jk n_i − 2 n_i n_j n_k).
  With |D_ρ| ≤ Cρ, |D/ρ| ≤ Cρ: |∂k E_ij| ≤ 5Cρ → 0; ∂t E_ij = D_t n_i n_j,
  |D_t| ≤ Cρ → 0. So E ∈ C¹ jointly in (t, x) with vanishing gradient on the
  axis. ✔
* Second derivatives off the axis are sums of bounded angular factors times
  D_ρρ, D_ρ/ρ, D/ρ² (spatial), D_tρ, D_t/ρ (mixed), D_tt (temporal) — all
  bounded by O10. |Hess E| ≤ C off the axis. ✔
* **Cross-axis step (the one place a gap could hide).** The coordinator writes
  "a line-segment argument for the continuous gradient proves the Lipschitz
  estimate across the axis as well as off it" and asserts no D/ρ² regularity.
  This is true, but it is asserted, not proved, and the proof is *not* the
  naive one (a crossing segment leaves the region where Hess is defined).
  **REPAIR-N3 (required): insert the following two-case argument.** Let
  G = ∇_{(t,x)}E, h = |(t,x) − (s,y)|, and write r_x = |x|. 
  *Case 1: the segment from (t,x) to (s,y) avoids the axis.* Then G is C¹ on
  it and |dG/ds| ≤ |Hess E| ≤ C, so |G(t,x) − G(s,y)| ≤ Ch.
  *Case 2: the segment meets the axis.* Then r_x + r_y ≤ h + (distances to the
  crossing point) ≤ 2h + ... in fact r_x, r_y ≤ h + |z| for the crossing point
  z with |z| = 0, so max(r_x, r_y) ≤ 2h... more simply r_x ≤ |x − z*| and
  r_y ≤ |y − z*| with z* the crossing point, and |x − z*| + |y − z*| = h, so
  max(r_x, r_y) ≤ h and min ≥ 0; since |G| ≤ Cρ pointwise,
  |G(t,x) − G(s,y)| ≤ |G(t,x)| + |G(s,y)| ≤ C(r_x + r_y) ≤ 2Ch.
  Hence G is globally Lipschitz with constant ~5C on the compact ball ⇒
  E ∈ C^{1,1} with uniform bound. This uses **only** (i) |G| ≤ Cρ and (ii)
  |Hess E| ≤ C off the axis — precisely the two facts already proved, with no
  division by ρ² beyond bounded quotients. Numerics corroborate: crossing-pair
  ratio sup 2.51 (check D), consistent with the analytic constant. ✔

**O13. Uniformity across approximants — CORRECT.** Every constant above is a
function of the (H1)–(H4) uniform bounds only; the lifted C^{1,1} bounds are
therefore uniform in n. ✔

**O14. C¹ convergence of the lifted coefficients along the same subsequence —
CORRECT, including the delicate quotient.** A_n → A in C¹ (B_n → B in C¹ from
(H1)); F_n → F in C¹ (quotient C¹ of N_n and μ_n, reciprocal stable under
1−μ ≥ 1/2); φ_n → φ in C¹ by (H2); D_n → D in C¹. For the tensor part:
∂kE^n_ij − ∂kE_ij = (D_{nρ} − D_ρ)n_k n_i n_j + ((D_n − D)/ρ)(δ_ik n_j +
δ_jk n_i − 2 n_i n_j n_k); the first term → 0 by quotient C¹, and the second by
the Hadamard bound |(D_n − D)(t,ρ)/ρ| ≤ sup_{0≤s≤ρ}|∂ρ(D_n − D)(t,s)| ≤
sup|D_{nρ} − D_ρ| → 0 (both D_n and D vanish at ρ = 0). Verified numerically
(check E). The coordinator's §4 claim "ordinary quotient C¹ convergence
therefore suffices" is correct. Uniform weak Hessians pass to the same limit by
W^{2,∞} weak-* compactness, consistent with (but not needed beyond) the direct
C^{1,1} proof. ✔

**O15. Lorentz signature and chart validity — CORRECT.** At the center
g = a(t)²·diag(−1,1,1,1); off the axis F > 0 (F = −4λν/(1−μ), ν < 0 < λ,
1−μ ≥ 1/2) and A = B² > 0 (B ≥ c uniformly, comparability above); g_ti = 0.
The chart (t,x) is the standard smooth R⁴ chart; off the axis the transition to
(t,u,v) is a diffeomorphism (ρ > 0), so the construction is compatible with the
quotient smooth structure. The claim is correctly scoped to this atlas. ✔

## 6. Consequences (L3) — separate verdicts

**O16. Geodesic IVP uniqueness — CORRECT, conditional, and not new.**
g ∈ C^{1,1} nondegenerate ⇒ g^{-1} ∈ C^{1,1} (Cramer + determinant bounded
away from 0 by continuity on compacta); Γ = g^{-1}∂g ∈ W^{1,∞}_loc, i.e.
locally Lipschitz. The geodesic system ẋ = p, ṗ = −Γ(x)(p,p) has a continuous
right-hand side, Lipschitz on bounded velocity sets; Picard–Lindelöf gives
local existence and uniqueness from each marked tangent. This is textbook for
C^{1,1}/Lipschitz connections — the coordinator's "a smooth geodesic theorem is
unnecessary" is right, and the deduction is standard, not a new result:
Minguzzi 2014 (Monatshefte 177:579–; arXiv:1308.6675) develops precisely this
Picard–Lindelöf/convex-neighborhood theory for Lipschitz connections and argues
C^{1,1} is the optimal class for causality theory. My verdict: **correct
conditional conclusion, correctly scoped, already known as methodology** (the
coordinator claims no priority). ✔

**O17. Central geodesic and proper-time clock — CORRECT, conditional, local.**
∂i g_tt(t,0) = −F_ρ(t,0)n_i = 0 and g_ti = 0 give Γ^i_tt(t,0) = 0, so the axis
x ≡ 0 with dτ = a(t)dt is an affinely parametrized geodesic. The clock
τ(t) = ∫_{t_b}^t a(s)ds = ∫ 2λ(s,s)ds is strictly increasing (a ≥ 2/3).
*Caveat:* unboundedness in both directions requires the global lower bound
a ≥ 2/3 on the **full** quotient and a global t-domain; the local bounds prove
only the local statement. The coordinator's sentence scopes this "on the full
quotient" — that is a global-input claim, legitimate only insofar as LOY's
global solution (two-sided complete class, Theorem 1.7 of v1) supplies it; the
source-lane audit should confirm the global a-bound there. My verdict: correct
as a conditional statement; the local version is fully proven by L1. ✔

**O18. a.e./distributional 4D Einstein–scalar extension — CORRECT as a weak
solution statement, with the coordinator's own disclaimers.** Off the axis all
quotient equations are classical (limits inherit them by uniform convergence on
compacta away from the axis), and there the reduced system ⇔ Ric(g) = 2dφ⊗dφ,
□_g φ = 0 classically. Both sides are L^∞ functions for C^{1,1} g: Γ ∈
W^{1,∞} ⇒ distributional curvature = a.e. curvature with **no δ/membrane
terms** — this is exactly where the cross-axis C^{1,1} of O12 is essential
(less regular metrics can carry axis-supported distributional terms; C^{1,1}
excludes them). The axis has 4D measure zero, so the a.e. identity is the
distributional identity throughout the chart (framework consistent with
LeFloch–Mardare 2007, distributional curvature of low-regularity Lorentzian
metrics). Pointwise Ricci **at** the axis is not claimed, and cannot be — the
Hessian need not have a limit (check D's oscillating Hess model, matching the
coordinator's §6 sharpness example). My verdict: correct, conditional,
correctly labelled as weak/a.e., correctly *not* upgraded to pointwise or
smooth-category claims. ✔

**O19. Hidden-extra-derivative audit — CLEAN.** Maximal orders consumed:
r_{ρtρ}-type (third) for B (O9); r_aa (second) for m_ab (O3); μ_ab (second,
from O1–O3); φ_ab (second) for O3/O8. Nothing uses r⁽⁴⁾, φ''', or a second
derivative of D/ρ², B, or any quotient. The brief's "do not assume D/ρ² is C²"
instruction is respected by the argument as written. ✔

## 7. Objections, repairs, and the attempted counterexamples

**OBJ-1 (load-bearing; repair required).** Hypothesis list omits (E2)/(E3);
O8 needs (E3). Failure mode demonstrated: φ = ρ lifts to |x| ∉ C¹ (check F).
→ REPAIR-N2: add the two equations to the hypothesis list (they are verbatim
LOY (SSESF) equations 1–2; I verified both against the v1 primary text).

**OBJ-2 (asserted lemma; repair required).** The cross-axis Lipschitz claim
(O12) is stated without proof. → REPAIR-N3: insert the two-case proof of §5
above (uses only |∇E| ≤ Cρ and |Hess E| ≤ C off-axis).

**OBJ-3 (source correspondence gate stays open — L2).** The L1 argument
consumes uniform W^{3,∞}(r) (including mixed third derivatives) and
W^{2,∞}(φ) (including φ_uv) up to and including the axis. From my own fetch of
LOY v1 §1 I verified (1.8) (nondegeneracy: r_v > 1/3, −2/3 < r_u < −1/6,
2m/r < 1/2) and that (1.9) explicitly bounds **pure** second derivatives of r
and (rφ). I did **not** fetch §3–§4, so I cannot confirm first-hand that §4's
assertion covers **mixed** second derivatives of φ and **third** derivatives of
r on sets including the axis. The coordinator lists this as their own open gate
(§6 bullet 1); my review independently confirms it must stay open. The Kilgore
v1 abstract/intro (fetched) confirms all-order estimates for these solutions
exist in a published follow-up "with additional care given to controlling terms
near the axis" — relevant context, though Kilgore treats the cone-future
problem, not the global scattering limit, and the coordinator's argument does
not cite or use it (the brief's warning about Kilgore's cone theorem is
respected: nothing in AXIS_C11_RECONSTRUCTION.md appeals to it).

**OBJ-4 (cosmetic).** "Every term is O(r)" in coordinator §2 — see REPAIR-N1.

**OBJ-5 (scope).** Clock unboundedness and "full quotient" statements are
global-input claims (see O17); compact-local versions are what L1 proves.
Curvature is only L^∞ (no pointwise axis Ricci) — the coordinator's own §6
disclaimers are correct and I endorse them; the H = ρ²sin(log ρ) sharpness
model is genuine (verified: C^{1,1} lift, bounded Hess, no Hess limit).

**Attempted counterexamples (all fail — this strengthens the claim).**
1. *Axis-odd scalar* φ(t,ρ) = ρ: satisfies every listed hypothesis except
   (E3); lifts to |x| ∉ C¹. Fails as a counterexample **to the repaired
   statement** (which includes (E3)), and demonstrates OBJ-1 is load-bearing.
2. *Oscillating coefficient* D = ρ²sin(log ρ) + regular part: satisfies every
   input-type bound; lifts to a C^{1,1} tensor coefficient with bounded Hess
   and no Hess limit (check D: crossing-pair Lipschitz ratio ≤ 2.51; Hess
   oscillates ≈ −2.2…+2.0 without converging). Fails to break C^{1,1};
   confirms the sharpness boundary the coordinator claims (finite orders give
   C^{1,1}, not C²).
3. *Rougher D* with D_ρρ bounded but D/ρ² oscillatory: excluded from the
   hypothesis class by O10 itself (|D| ≤ Cρ² and |D_ρρ| ≤ C force |D/ρ²| ≤ C);
   the two-case proof then gives C^{1,1} regardless. No counterexample found.

**What would refute the (repaired) theorem:** (i) quotient data satisfying
(H1)–(H4) with |D_ρρ| unbounded near the axis — blocked by O9's W^{2,∞}
closure; (ii) axis-non-even φ satisfying all of (H1)–(H4) — blocked by (E3)
(O8); (iii) loss of signature — blocked by F > 0, A > 0 (O15); (iv) a failure
of LOY §4 to actually supply the mixed/third uniform orders including the axis
— an L2 risk that would force weakening the input, not the L1 lemma.

## 8. Line-by-line verdict summary

| # | Obligation | Verdict | Notes |
|---|---|---|---|
| O1 | m = O(r³) | CORRECT | integration, λ ≥ c |
| O2 | m_a = O(r²) | CORRECT | direct from (E1) |
| O3 | m_ab = O(r) | CORRECT | term 2 dominant; wording repair N1 |
| O4 | μ extends C^{1,1}, weak Hess bounded; μ_n→μ in C¹ | CORRECT | quotient formula verified (check B) |
| O5 | r_t = r_tt = 0 at axis | CORRECT | tangential |
| O6 | r_ρ(t,0) = λ−ν = 2λ | CORRECT | forced by O5 |
| O7 | r_ρρ(t,0) = 0 | CORRECT | via (E2) + O1 |
| O8 | φ_ρ(t,0) = 0 | CORRECT **conditional on (E3)** | OBJ-1/REPAIR-N2 |
| O9 | B,A,F,D C^{1,1}; (4) axis values | CORRECT | Hadamard; F = −4λν/(1−μ) checked vs LOY (1.2) |
| O10 | (5) bounds, no D/ρ² derivatives | CORRECT | audited O19 |
| O11 | scalar-type lift C^{1,1} | CORRECT | W^{2,∞} lift |
| O12 | E_ij C^{1,1} across axis | CORRECT | two-case proof supplied (N3) |
| O13 | uniformity in n | CORRECT | constants from (H1)–(H4) |
| O14 | C¹ convergence, same subsequence | CORRECT | Hadamard bound (check E) |
| O15 | signature/chart | CORRECT | center a²·Minkowski |
| O16 | geodesic IVP uniqueness | CORRECT/conditional/known | Minguzzi 2014 |
| O17 | central clock | CORRECT/conditional | global part needs source gate |
| O18 | a.e./distributional 4D | CORRECT/weak | no axis δ-terms; no pointwise Ricci |
| O19 | no hidden derivative | CLEAN | max: r⁽³⁾, φ⁽²⁾ |

## 9. Limitations of this review

* L2 depth: I fetched LOY v1 title page through §1.1 (abstract, (SSESF),
  Theorem 1.1, (1.8)–(1.9), Remarks) via ar5iv; §2–§5 were not fetched, and
  Prop 3.18/§4's mixed-derivative assertion is correspondingly unverified by
  me. Kilgore: abstract + §1 only; §7 not fetched. Minguzzi: abstract-level.
  All pinned in sources.jsonl with these limits.
* The finite-difference script is corroboration, not proof; its sharpness probe
  uses a model function that satisfies the *input-type* bounds but is not a
  solution of (H3) — it bounds what the hypotheses allow, which is the right
  role for a sharpness model.
* I did not attempt an independent proof of the smooth common-development gate
  (explicitly out of scope: coordinator §6 bullet 3), nor any novelty assessment
  beyond noting methodological precedents (Minguzzi; LeFloch–Mardare), since the
  coordinator claims no mathematical priority.

## 10. Proposed next tasks

1. **Source lane:** verify LOY v1 §4 (and Prop 3.18) supplies uniform mixed
   second derivatives of φ and third derivatives of r on axis-including
   compacta; verify the global a ≥ 2/3 input used for clock unboundedness.
   (Closes OBJ-2/O17's conditional part.)
2. **Coordinator edit:** apply REPAIR-N1/N2/N3 to AXIS_C11_RECONSTRUCTION.md
   (three small edits; N2 is semantic, N3 is a short inserted proof).
3. Optional: a Lean or detailed-symbolic encoding of the O12 two-case lemma,
   since it is now the only step whose written proof must be added rather than
   checked.
