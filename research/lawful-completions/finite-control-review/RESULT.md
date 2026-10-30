# finite-control-review: compactness, continuity, degree and incoming mass at fixed incoming mass

2026-10-30. Independent review submission for coordinator inspection. Scope:
the finite-control proof chain as assembled in `coordinator/C11_FINITE_CONTROL.md`
with inputs `COMPACTNESS_CONTINUITY_REPAIR.md`, `CUBIC_TRACE.md`,
`INCOMING_MASS.md`, `AXIS_C11_RECONSTRUCTION.md`, `DEGREE_ROUTE.md`,
`FINITE_CONTROL.md`, `SMOOTH_FINITE_CONTROL.md`. Primary source pinned and read
directly: Luk–Oh–Yang, arXiv:1605.03893v1 (12 May 2016), e-print TeX and HTML
rendering. This review owns the finite-control chain; it does not re-audit the
smoothness bootstrap and does not accept or reject any lane.

**Verdict in one paragraph.** The replacement of the rejected GLM Lipschitz
argument by compactness plus characteristic uniqueness is logically sound, and
every step I could check against the v1 source is either printed verbatim where
the notes claim it, or is an elementary derivation that I re-derived and
confirmed. The chain's load-bearing external inputs are nevertheless weaker
than "printed theorem": the source's characteristic uniqueness proof is
omitted ("easy to show", "routine iteration argument"), the u-side halves of
Proposition 3.18 are an explicit sketch, and the extension from one fixed
profile to a varying compact profile family is correct but is this project's
extension, not printed text. The exact strongest category owned by this chain
alone is C¹,¹ (metric and scalar, Cartesian atlas) with a.e./distributional
Einstein–scalar equations, unique local geodesics, a geodesic center, and the
Cauchy-slice property — with no pointwise axis curvature, no C⁰-inextendibility
(the Galloway–Ling–Sbierski input verbatim requires "at least C²"), no smooth
MGHD, no ADM equality, no uniqueness at null infinity, no continuous scattering
selection, and no bare-metric nonisometry. The hardest missing step is listed
in §4; a detailed account of what would break if it fails is §5.

## 1. Point-by-point obligation audit

Each item: obligation → what the source actually prints (locator) → verdict.

### O1. Exact characteristic uniqueness class of LOY v1

- Definition 2.1 (`def:C1-sol`): a C^k solution is a triple (r,φ,m) satisfying
  SSESF with ∂_u r, ∂_v r, φ, ∂_v(rφ), ∂_u(rφ) ∈ C^k, inf ∂_u r > −∞,
  inf ∂_v r > 0, and r(a,a)=m(a,a)=0 on the axis Γ; global = for all u₁>u₀.
  Data and gauge: (2.4) (∂_v r)^{-1}∂_v(rφ)|_{C_{u₀}} = Φ and (2.5)
  ∂_v r|_{C_{u₀}} = 1/2.
- Theorem 1.1 asserts "the unique solution to (SSESF) arising from the given
  data"; §2.1 states local well-posedness for C^k data, k ≥ 1, "We omit the
  proof, which is a routine iteration argument"; §1 says uniqueness is "easy to
  show".
- **Verdict: pinned, with a proof-status caveat.** The uniqueness class is
  exactly Definition 2.1 at k ≥ 1 with data (2.4) and gauge (2.5). The
  compactness limit (r ∈ C²_loc, φ, ∂_v(rφ), ∂_u(rφ), m ∈ C¹_loc) is in the
  k=1 class — the notes' claim "∂_u r and ∂_v r are C¹ because r is C²" matches
  the definition, which regulates the listed first derivatives, not r itself.
  The uniqueness *proof* is not in v1. COMPACTNESS_CONTINUITY_REPAIR correctly
  treats uniqueness as an external theorem; the residual is recorded in §4.

### O2. Finite-domain, profile-uniform compactness constants

- Remark 1.2 (verbatim): "the constants ε and C in the above theorem are
  independent of u₀" — vertex uniformity of all Theorem 1.1 bounds (1.8)–(1.9).
- Proposition 3.18 (verbatim): ε₂ "independent of u₀, v₀ and A"; implicit
  constant "independent of u₀, v₀, A and ε", bounds ≲ A + ε and ≲ εA + ε².
- Section 4 display (verbatim, unnumbered): Σ_{k=0..2} sup(|∂^k_v φ|+|∂^k_u φ|)
  ≲ A+ε; same for ∂^{k+1}(rφ); Σ for r-derivatives ≲ ε(A+ε); "the C² norm of
  m⁽ⁿ⁾ is uniformly bounded on any compact subset"; then Arzelà–Ascoli with the
  displayed convergence (φ, ∂_v(rφ), ∂_u(rφ)) in C¹, r in C², m in C¹ on every
  compact Ω ⊆ PD, with r = m = 0 on Γ.
- **Verdict: the printed constants are member-uniform, so the compact-family
  extension is sound.** For Φ_(ε,x) = ε(Σx_kF_k + β(x)G) on the closed ball,
  A(x) = sup|(λ₀^{-1}∂_v)²Φ| = 4ε·sup|f_x″| is uniformly bounded; δc and ε are
  common; hence every consumed constant is uniform in (n, x). The extension
  from one fixed profile (what §4 prints) to varying profiles is this project's
  extension — correct, because no consumed constant depends on the member
  except through A — but it should stay labeled as an extension.
- Topology check: the repair's relative-compactness topology (r ∈ C²;
  φ, ∂_v(rφ), ∂_u(rφ), m ∈ C¹, axis included) is exactly §4's printed
  convergence topology. ✓
- Equicontinuity audit: C² convergence of r and rφ needs third-derivative
  bounds including mixed ones. Pure third derivatives are printed (Prop 3.18;
  §4's closing Remark even records the weak esssup bounds). Mixed third
  derivatives are asserted in one line ("Uniform bounds for a corresponding
  number of mixed derivatives follow from the wave equations for φ and r") —
  the coordinator derivations (AXIS_C11 §1–2) supply them; see O3. For m ∈ C¹
  convergence one needs uniform |m_ab| ≤ C: AXIS_C11 §2 derives this from one
  differentiation of (2.10)–(2.11) using first-order bounds and bounded φ
  second derivatives; I re-derived the term magnitudes (dominant r_aφ_b² = O(r)
  and O(r²) terms; μ_ab = O(1) from the exact quotient formula) and find it
  correct. ✓

### O3. Axis inclusion

- §4's compact Ω ⊆ PD includes Γ; the limit satisfies r = m = 0 on Γ (printed).
  All bounds are suprema over PD_{[u_n,∞)} and hence axis-inclusive. ✓
- The axis-inclusive |φ_uv| ≤ C (the "O7" replacement) is **not** printed; the
  source asserts mixed bounds in one line. I re-derived the coordinator's
  construction with LOY's own sign convention (ν = ∂_u r < 0, confirmed against
  the HTML (2.6)–(2.9)): from the wave identity ∂_u(φ + rψ) = −Krψ with
  ψ = φ_v/λ, K = λ_u/λ = 2mν/((1−μ)r²) ≤ 0 (printed (2.6), (2.8)), setting
  c = φ_u + (ν+Kr)ψ, w = rc gives w_u + Kw = rB (I verified this identity; it
  requires r_u = ν, which is LOY's convention), and the backward ODE solution
  w(u,v) = −∫_u^v e^{∫_u^s K} r(s,v)B(s,v) ds with w(v,v)=0 automatic. With
  K ≤ 0 (exponential ≤ 1), r(s,v) ≍ (v−s) from −1/6 > r_u > −2/3 (1.8), and B
  bounded from printed inputs (φ_uu from the §4 display/(3.57); ν_u, λ_u, first
  mass derivatives from (1.9), (3.16)–(3.19)), |w| ≤ C(v−u)², so c = O(r),
  ψ_u bounded, and φ_uv = λ_uψ + λψ_u uniformly bounded. c(v,v)=0 follows from
  continuity, and φ_u = φ_v on the axis follows (parity (3) re-proved).
  **Verdict: derivation correct; inputs printed except the (3.57) refined
  u-side form, which sits in Prop 3.18's sketched region** (see O12/residuals).

### O4. Limit passage with varying parameters and vertices; order of limits

- §4 prints, verbatim: "Taking the limit n→∞ first and then letting u→−∞, we
  obtain the desired statement", twice (after the log-λ display and after the
  cubic display). The printed target is (4.1): lim_{u→−∞} λ(u,v) = 1/2 and
  lim_{u→−∞} λ^{-1}∂_v(rφ)(u,v) = Φ(v) for every v.
- **Verdict: the C11 §6 order (n→∞ at fixed (u,v), then u→−∞) is exactly the
  source's own procedure, and the caution is right: compact convergence alone
  would not identify the limiting incoming profile.** For varying x_n the same
  passage holds because (i) every §4 input is member-uniform (O2), and
  (ii) Φ_(ε,x_n)(v) → Φ_(ε,x_*)(v) pointwise at fixed v by C² family
  continuity. The root equations pass to the limit through uniform clock,
  inverse-clock and scalar convergence on the fixed readout window
  (R ≥ 2T_N+1 inside the compact convergence region). ✓

### O5. C² profile family hypotheses

- Actually consumed: (1.7) with smallness C₀ε: ∫_u^v|Φ| ≤ C₀ε(v−u)^{1−δc} and
  |Φ|+|Φ'| ≤ C₀ε (Theorem 1.1, verbatim); sup|Φ″| < ∞ (Theorem 1.7's additional
  assumption, verbatim (1.18-block); Prop 3.18's A); x ↦ Φ_(ε,x) continuous in
  C².
- Verified: disjoint supports give ∫_u^v|Φ_(ε,x)| ≤ εM₀·min(v−u,L) ≤
  εM₀L^{δc}(v−u)^{1−δc} (inequality checked numerically; C₀ = M₀L^{δc} works on
  both regimes); |Φ|+|Φ'| ≤ C₀ε from the uniform family bounds; A(x) = 4ε·
  sup|f_x″| uniformly bounded; β smooth and ≥ β₀/2 on a small enough closed
  ball (the radius must be chosen from the norms — my first numeric run made
  the same mistake of fixing ρ arbitrarily, which is exactly why the
  construction's "choose ρ small enough" clause matters).
- Thresholds: ε ≤ ε₁(δc) (Theorem 1.1) and ε ≤ ε₂ (Prop 3.18, independent of
  A). The C11 §3 statement "the source's second-data-derivative parameter is
  bounded by 4ε sup||f_x″||∞" matches the source's definition A = sup|(λ₀^{-1}∂_v)²Φ|
  with λ₀ = 1/2. **Verdict: hypotheses verified.** ✓

### O6. Exact norm-compensating tail and fixed actual incoming mass

- Exact compensation: ||Φ_(ε,x)||₂² = ε²β₀²||G||₂² for every x (cross terms
  vanish by disjoint supports; verified numerically to 5·10⁻¹⁶ relative error;
  F_k(T_j)=δ_kj and G ≡ 0 on the readout window verified).
- Actual mass: the flux identity used by INCOMING_MASS is printed in the
  source: (3.18) m(u,v) = ½∫_u^v (1−μ)r²(λ^{-1}∂_vφ)²λ dv′, together with
  (2.10). With X = λ^{-1}p_v − φ = rφ_v/λ (algebra re-derived: p_v = λ(φ+rψ),
  so λ^{-1}p_v − φ = rψ), the integrand ½(1−μ)λX² equals m_v exactly.
  Pre-pulse exact flatness (C11 §4, verified below) fixes m(u,A)=0; the
  §4-remainder terms converge uniformly on finite [A,V]; so
  m₋(V) = ¼∫_A^V Φ², and E = lim_{V→∞} m₋(V) = ¼∫_ℝ Φ². Order: u→−∞ first,
  V→∞ after; no moving cone, no limit exchange. **Verdict: sound, and the
  identification is with the actual global solution's incoming boundary mass —
  not a charge of approximating data.** The timing caveat stands: the fixed
  total includes the compensating tail G after the readout window; incoming
  mass at each reading time is not fixed. ✓

### O7. Uniform cubic proper-time remainder

- Printed verbatim in §4 (after (4.1)):
  |λ_n^{-1}∂_v(r_nφ_n)(u,v) − [λ_n(u_n,v)/λ_n(u,v)]Φ(v)| ≲ ε³ max(v−u,1)^{−2δc},
  and |log λ_n(u,v) − log(1/2)| ≲ ε² max(v−u,1)^{−δc}. Notation note: the
  notes' "γ" is the source's δc (the (1.7) exponent); the source's separate γ
  in (1.9)/(3.16) is a different exponent. Constants: from proofs "proceeding
  as in the proof of Proposition 3.8" and "Proposition 3.10" — bootstrap-level
  constants depending only on δc (member-uniform by O2).
- Axis specialization: at u=v=t, ∂_v(rφ) = λφ (boundary tangentiality),
  |φ_n(t,t) − Φ(t)| ≤ Cε³ and |2λ_n(t,t) − 1| ≤ C′ε²; the timing correction
  |t_n(T) − (t_b+T)| ≤ C_Tε² uses τ′ = 2λ ≥ 2/3. All uniform in (n,x).
  **Verdict: sup_{n,|x|≤ρ} |ε^{-1}H_n(x) − x| ≤ Cε² is sound with member- and
  vertex-uniform constants.** ✓

### O8. Per-cone continuity (compactness + characteristic uniqueness)

- The repair's Proposition: for fixed u₀ and x_j → x, every subsequence of
  S_{x_j} has a subsubsequence converging on exhaustion triangles in §4's
  topology to a global C¹ solution with data Φ_x in Definition 2.1's k=1
  class; Theorem 1.1 uniqueness forces it to equal S_x; the standard
  contradiction closes convergence of the whole sequence; metrizability gives
  continuity.
- Checked: (i) closed geometry bounds (λ ≥ 1/3 etc., from (1.8)'s strict
  inequalities) pass to closed limits; (ii) initial gauge and data pass by C¹
  convergence on finite initial segments; (iii) vertex normalization persists;
  (iv) the off-axis equation passage is §4's own "it is clear that (r,φ,m)
  solves (SSESF) in the classical sense", with the repair's axis extension
  doing that step more carefully than the source via the weighted bounds;
  (v) no Lipschitz estimate, no modulus uniform in n, no Gronwall difference
  estimate is used anywhere — correctly none. The repair is also right to
  discard the invalid implication "W ≤ δ + aW ⟹ W ≤ δe^{aT}" from the rejected
  worker submission. **Verdict: the replacement proof is valid logic
  conditional on O1–O3.** ✓

### O9. Brouwer degree boundary

- H_n : closed ball → R^N continuous; ε^{-1}H_n(x) = x + R_n(x),
  sup_{n,x}|R_n| ≤ Cε². On |x|=ρ, |x + sR_n(x) − z| ≥ ρ − |z| − Cε² > 0 when
  Cε² < ρ/2 − |z|; the homotopy to x−z never vanishes on the boundary; degree
  = 1; a root exists in the open ball. Verified numerically in the worst case
  (R pointing at z). The identity linearization comes from F_k(T_j)=δ_kj; the
  scalar is signed (no φ→−φ quotient), consistent with DEGREE_ROUTE's
  red-team item. **Verdict: correct; no derivative of H_n or of any scattering
  map is used.** ✓

### O10. Parameter subsequence and incoming-profile recovery

- x_n (degree roots) in the compact ball → x_* subsequence; profiles converge
  in C²; all constants uniform; §4's diagonal compactness gives a global
  reduced sublimit; O4's order recovers Φ_(ε,x_*) as the incoming profile; the
  root equations pass exactly (uniform clock/inverse/scalar convergence).
  Different targets may select different subsequences — existential,
  target-by-target. **Verdict: sound; correctly not claimed to be a continuous
  or canonical global selection.** ✓

### O11. Exact flat wedge and the pointed causal past

- The Goursat/Gronwall lemma: p_uv = Vp with V = 2mνλ/((1−μ)r³) bounded (from
  (3.16) m = O(ε²r³) and (1.8)); zero Cauchy data on both boundaries of
  {u₀ ≤ u ≤ v ≤ V₀ < A} (data (2.4) vanishes below A; p=0 on Γ); the integral
  representation and M(U) ≤ C(V₀−u₀)∫_{u₀}^U M gives p ≡ 0 (scheme checked
  numerically, including that the zero-seed case is the substantive one).
  Then m=0, λ=1/2, r=(v−u)/2 on v<A: exact Minkowski; passes to compact
  limits. v = t+ρ is nondecreasing along future causal curves (F > 0), so
  J⁻(b) = {v ≤ 0} and the pointed past (field, tangent) is exactly the flat
  one. **Verdict: correct.** ✓

### O12. C¹,¹ reconstruction: genuine unique centered geodesic readings without smooth MGHD?

- What C¹,¹ gives (AXIS_C11 + my checks): radial lifts with H_ρ(t,0)=0 are
  C¹,¹; E_ij = Dn⊗n is C¹,¹ by the two-case segment argument (checked: off-axis
  weak Hessian bound + |∇E| ≤ Cρ ⟹ gradient Lipschitz across the axis);
  g^{-1} ∈ C¹,¹_loc ⟹ Christoffels locally Lipschitz ⟹ Picard–Lindelöf unique
  local geodesics; the center is a geodesic (∂_ρg_tt(t,0)=0, g_ti=0); the
  proper-time clock is τ(t)=∫2λ(s,s)ds — the same clock the reduced chain
  already used, so the readings φ(γ(T_j)) − φ(b) are genuine four-dimensional
  geodesic readings at C¹,¹. Distributional Einstein–scalar holds (axis has
  measure zero; no singular surface term is possible at C¹,¹).
- What C¹,¹ does **not** give: pointwise Ricci at the axis (open, as AXIS_C11
  says); C⁰-inextendibility — Galloway–Ling–Sbierski Theorem 1 verbatim
  requires "a smooth (at least C²) time-oriented Lorentzian manifold that is
  timelike geodesically complete and globally hyperbolic", so at bare C¹,¹ the
  input does not apply; the MGHD universal property (Ringström common
  development) likewise needs the smooth category. C11 §7's Cauchy-slice claim
  is correctly scoped to the constructed model (I checked the causal bound
  |dx/dt| ≤ √7 ≤ √12 from F ∈ [2/9, 8/3], A = (r/ρ)² ∈ [4/9,1], eigenvalues
  F radial and A tangential).
- **Verdict: yes — unique centered geodesic readings hold at C¹,¹, with no
  smooth-MGHD assumption; and the boundary of that category is exactly where
  the notes place it.** The two residuals feeding this: Prop 3.18's sketched
  u-side halves (line: "To avoid repetition, we only sketch the argument"),
  which include (3.57)'s refined form used as an O7 input at the per-member
  level (the §4 display supplies the sequence-level φ_uu bound regardless), and
  the unpublished uniqueness argument (O1).

### O13. Source-fidelity checks of specific printed claims

- §4's r-derivative display k=0 term (|∂_v r|+|∂_u r| ≲ ε(A+ε)) is a confirmed
  typo: impossible since λ ≈ 1/2 > 0 and (1.8) gives λ > 1/3. The notes' bypass
  (Theorem 1.1 for first derivatives; Prop 3.18 for higher) is right, and no
  step needs an O(ε²) bound on λ itself.
- The convergence display's leading "φ" must be read as φ⁽ⁿ⁾ — confirmed
  typography.
- The past-half geodesic completeness in §6 is one sentence ("completely
  identical manner", verbatim located); the citation "Theorem 1.7" for the
  two-sided completeness theorem resolves correctly in the v1 HTML numbering.
- Published-version citation: Annals of PDE 4(1), article 3, June 2018 (Crossref) —
  the coordinator's "Ann. PDE 4:3, 2018" is accurate.

## 2. Exact strongest 4D regularity category and remaining gap

Owned by this chain alone (no smoothness-bootstrap input):

> C¹,¹ existential interpolation: for each N, schedule 0<T₁<…<T_N, profile
> basis, there are E_*, c > 0 such that for every 0<E<E_* and |y| < c√E there
> is a time-oriented spherically symmetric model, M = R×R³, g and φ locally
> C¹,¹ in the constructed Cartesian atlas, Einstein–real-massless-scalar
> equations a.e./distributionally, identical pointed flat causal past at b
> (field and unit tangent), actual incoming boundary mass E, and unique
> centered geodesic readings φ(γ(T_j)) − φ(b) = y_j at the prescribed proper
> times; plus the section 7 Cauchy-slice property and the finite
> Boolean-independence corollary at N-dependent thresholds.

Not owned, correctly separated:

| Gate | Status in this review |
|---|---|
| Smooth MGHD upgrade | Separate chain (SMOOTHNESS_BOOTSTRAP / LOCAL_POLAR_PERSISTENCE / SMOOTH_FINITE_CONTROL); not assumed here; its own review disposition stands; nothing in the C¹,¹ theorem needs it |
| ADM existence/equality | Open (INCOMING_MASS is incoming-boundary only) |
| Uniqueness at past null infinity | Not claimed, not used (the selection is subsequence-based; §4 prints existence of a limit, not uniqueness) |
| Continuous global scattering selection | Not claimed; the degree route exists precisely because it is unnecessary for the existential statement |
| Bare-metric nonisometry | Separate lemma (NONISOMETRY_LEMMA), conditional dependency only |
| Pointwise axis curvature | Open at C¹,¹ |
| Novelty / nearest-prior | Open gate; nothing here is a priority claim. From the source side: LOY themselves construct, for each fixed admissible profile, a two-sided-complete global solution with that profile (Theorem 1.7/§4); what they do not do is prescribe finitely many axis readings through a compact parameter family at fixed incoming mass — the degree/interpolation layer is the candidate new step, and it awaits the nearest-prior comparison |

## 3. Verification commands and results

- Primary source: `curl -sL https://arxiv.org/e-print/1605.03893v1` → gzip of
  `SSESF-LargeBVScat.160512.tex` (3214 lines); loci verified by direct reading
  (Theorem 1.1 and remarks; Definition 2.1; (2.4)–(2.16); §3 props; Prop 3.18;
  §4; §6). Numbering cross-checked against `https://arxiv.org/html/1605.03893v1`.
- External input: `https://arxiv.org/html/1704.00353v4` Theorem 1 verbatim.
- Published metadata: Crossref API for DOI 10.1007/s40818-017-0038-4.
- Arithmetic checks: `python3 checks.py` (this directory), 1.5 s total
  (budget: ≤15 s per check, ≤30 s total): all pass — exact norm compensation
  (rel dev 5·10⁻¹⁶), δ_kj normalization and tail vanishing, the (1.7)
  min/L^{δc} reduction, clock-inverse factor 3/2, worst-case degree-boundary
  positivity, flat-wedge Gronwall scheme (zero seed stays zero; nonzero seed
  grows). These are sanity checks of stated inequalities, not proofs.
- Search capability test (recorded per brief): `scholar_search` worked
  (arXiv API + OpenAlex + Crossref all returned; arXiv located 1605.03893v1
  with the exact v1 date). web-search-prime was not used (quota exhausted per
  brief). Direct arXiv fetches worked.

## 4. Hardest missing step (strongest counterexample to the assembled claim)

**The characteristic uniqueness proof does not exist in the pinned source.**
Theorem 1.1 asserts uniqueness in Definition 2.1's C^k class (k ≥ 1); §1 calls
it "easy to show" and §2.1 omits the proof ("a routine iteration argument").
The continuity Proposition (O8) consumes exactly this uniqueness at k=1: every
compact sublimit of S_{x_j} is a global C¹ solution with data Φ_x, and the
identification S = S_x is what converts relative compactness into continuity
of H_n, hence into the degree roots, hence into the interpolation theorem. If
uniqueness failed at the C¹ class (two distinct global C¹ solutions with the
same data (2.4)–(2.5)), then: H_n need not be continuous (sublimits can
disagree); the degree argument loses its continuous boundary map; and the
passage of exact root equations to the limit loses its target. Everything else
(printed estimates, flat wedge, mass, C¹,¹ reconstruction of *some* sublimit)
would survive, but the theorem as stated would lose its load-bearing joint.
Mitigations, in increasing strength: (i) the failed implication the repair
discards is indeed invalid, so this is a genuine gap and not a disguise for it;
(ii) Christodoulou's BV framework, which the source builds on, proves
well-posedness in a much larger class — strong evidence the omitted argument is
fine; (iii) the published Ann. PDE 4(1):3 (2018) version may print the
argument — a version diff is the top next task; (iv) the iteration argument is
standard once λ, ν, μ are controlled, which Theorem 1.1's own estimates supply.

Second-hardest: **Prop 3.18's u-side halves are a sketch** (verbatim: "we only
sketch the argument"). Pure third u-derivatives of r and rφ feed the C²/C¹
compactness topology, and (3.57)'s refined u-side second-φ estimate feeds the
O7 derivation at the per-member level. A defect there would degrade the
compactness topology or force weaker norms, not the flat wedge, degree logic,
or mass identity. The §4 display asserts the sequence-level u-side bounds
regardless (citing the printed §3.5 estimates), which bounds the blast radius
to the per-member refined forms.

Third: the varying-profile compactness (O2) is an extension of printed
one-profile text. It is sound precisely because every consumed constant
depends on the member only through A; if any consumed proof in §3–4 hides a
member-dependent constant not controlled by (δc, ε, A), that step would need
re-audit. My locus-by-locus check found no such constant in the consumed
displays; a full sweep of §3's bootstrap is the residual.

## 5. What would falsify the review's verdict

1. A published-version diff showing v2/published changed the uniqueness
   statement's class (e.g., uniqueness only for smoother solutions), or added a
   hypothesis consumed by the chain.
2. A concrete C¹-class nonuniqueness example for SSESF data (2.4)–(2.5) — this
   would break O8 directly.
3. An error in the O7/weighted-mass derivations at the axis (they are
   coordinator-authored; my re-derivation confirms them, but they are the only
   nontrivial analysis in the chain not printed in a source).
4. A counterexample to member-uniformity: a consumed §3 estimate whose constant
   depends on the profile outside (δc, ε, A).

## 6. Limitations of this review

- The published Ann. PDE version was not read (paywalled); all source checks
  are against arXiv v1.
- I did not reconstruct the omitted uniqueness proof or the sketched u-side
  Prop 3.18 halves; they are treated as external inputs with recorded risk,
  exactly as C11_FINITE_CONTROL §2 does.
- The smoothness bootstrap, NONISOMETRY_LEMMA, and the philosophical bridge are
  out of scope; their status is reported, not audited.
- Numeric checks are arithmetic sanity checks of inequalities; none of the
  analytic claims rests on them.
- No novelty search beyond locating the primary source and its published
  version was performed; the novelty gate remains open.
