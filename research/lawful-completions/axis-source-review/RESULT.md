# SOURCE-to-input audit: LOY finite-order inputs for the C¹,¹ axis reconstruction

29 October 2026. Independent adversarial source audit (lane
`lawful-axis-source-review`). Target claim under review:
[coordinator/AXIS_C11_RECONSTRUCTION.md](../coordinator/AXIS_C11_RECONSTRUCTION.md).
Primary source read at full-text depth from the verbatim arXiv v1 LaTeX
(SSESF-LargeBVScat.160512.tex, arXiv:1605.03893v1, submitted 12 May 2016,
only version on record). All displayed formulas below were checked against
the LaTeX source line-by-line; line numbers cited are v1 source lines.

**Summary verdict.** The coordinator's source-input list is *accurate as to
which quantities must be bounded*, and every input it needs is either printed
in LOY or derivable from printed estimates by short calculations. Two inputs
are *not* printed theorems: (a) the axis-inclusive uniform bound on the mixed
second derivative `φ_uv` and mixed third derivatives `r_uuv, r_uvv` rest on one
prose sentence in §4; (b) Prop 3.18's u-side halves are proof-sketch level.
Neither gap is fatal: derivations (a-supply) are given here and verified. The
§4 first-derivative "small bound" for r is a confirmed typo; the coordinator's
replacement (`λ ≤ 1/2` from `r_uv ≤ 0`) is correct and is in fact also the
paper's own argument at (3.1). No FAIL verdicts. Overall: the source
correspondence **supports** the coordinator's C¹,¹ reconstruction at the
printed strength, conditional on the derivations in §4 below being checked
at integration; the reconstruction remains a finite-order, subsequence-level
quotient result and must not be relabelled C².

## 0. Reading depth and exact source

- Luk, Oh, Yang, *Solutions to the Einstein-scalar-field system in spherical
  symmetry with large bounded variation norms*, arXiv:1605.03893v1 (12 May
  2016). Authors confirmed from the arXiv v1 abstract page; v1 is the cited
  and only-recorded version in this lane. Read depth: **full-text** (verbatim
  LaTeX v1 source fetched from arxiv.org/e-print and grepped; every locator
  quoted below was read in the source).
- Theorem 1.1 = `thm:main.finite` (source l. 351-376); (1.8) = `eq:main:geo`,
  (1.9) = `eq:main:apriori`; data condition (1.20) = `eq:IDcond` (l. 358-361);
  Remark 1.2 (l. 377-379): ε, C independent of u₀. Theorem 1.7 = `thm:main`
  (l. 452-464) with extra hypothesis `sup_v |Φ''| < ∞` (`thm:main.add.assumption`).
- Proposition 3.18 = `prop:high-d` (l. 1795-1816), (3.44)-(3.47) =
  `eq:est4dvdvdvrphi`, `eq:est4dvdvdvr`, `eq:est4dududurphi`, `eq:est4dududur`;
  Lemma 3.19 = `lem:est4dvdvdv:prelim` with (3.48)-(3.53); Cor 3.20 (3.54);
  u-side second-normalized-φ bound (3.55) = `eq:est4duduphi` (l. 1986-1993).
- §4 = `sec.proof.inf` (l. 2030-2079); compactness passage l. 2043-2059;
  Remark 4.1 l. 2081-2088.
- Setup: Def 2.1 `def:C1-sol` (l. 505-531); axis identities (2.4) `eq:bc4high-d`
  (l. 533-538); normalized axis identities (2.19) `eq:bc` (l. 749-756);
  SSESF system (l. 315-324); Ω² = −4∂_ur∂_vr/(1−2m/r) (l. 310-313);
  Raychaudhuri-type equations (2.10)-(2.11) `eq:wave4dvr`, `eq:wave4dur`
  (l. 715-720); mass equations (2.12)-(2.13) `eq:dv-m`, `eq:du-m` (l. 721-727);
  bootstrap (3.4) `eq:btstrp:geom`; derived (3.1) `1/3 < ∂_vr ≤ 1/2` (l. 892-895);
  r ≍ v−u (3.2) `eq:rvminusu`; Prop 3.3 (3.7)-(3.10); Prop 3.4 (3.11)-(3.12);
  Prop 3.5 (3.13)-(3.14); Prop 3.16 (3.26)-(3.29).

## 1. Obligation-by-obligation verdicts

Notation: λ = ∂_v r > 0, ν = ∂_u r < 0, μ = 2m/r; quotient coordinates
t = (u+v)/2, ρ = (v−u)/2 ≥ 0, so on quotient functions ∂_t = ∂_u+∂_v and
∂_ρ = −∂_u+∂_v (chain-rule factors cancel); ψ = λ⁻¹φ_v, χ = ν⁻¹φ_u.
"Axis-inclusive" = bound holds on the closed domain PD_{[u₀,∞)} ∋ Γ.
"u₀-uniform" = constant independent of the cone vertex u₀ (Remark 1.2; Prop
3.18 statement l. 1804-1815).

### O1. Two-sided first-derivative and geometry bounds (Thm 1.1 (1.8)) — PASS

Printed verbatim: `∂_v r > 1/3`, `−1/6 > ∂_u r > −2/3`, `2m/r < 1/2`, with
Remark 1.2 making ε, C independent of u₀. This is the coordinator's "r_v=λ
and −r_u=−ν bounded above and away from zero, and 1−2m/r ≥ 1/2" except that
(1.8) gives λ *only a lower* bound. That is exactly what the brief anticipates;
see O2.

### O2. Upper bound on λ without the §4 typo — PASS (verified workaround)

`λ_u = ∂_u∂_v r = 2mνλ/((1−μ)r²)` is the first printed SSESF equation
(l. 318) — exactly the coordinator's formula. Sign inputs: m ≥ 0 follows from
m(a,a)=0 (2.3b), the printed mass equation `∂_v r ∂_v m = ½(1−μ)r²(∂_vφ)²`
(l. 322), λ > 0 and 1−μ > 1/2; ν < 0 from (1.8). Hence `λ_u ≤ 0`, and with the
printed initial gauge `∂_v r|_{C_{u₀}} = 1/2` (constant along C_{u₀}, l. 545-547),
`λ ≤ 1/2` everywhere. This is also the paper's own derivation inside the
bootstrap: (3.1) at l. 892-895 states `1/3 < ∂_v r ≤ 1/2` "by the bootstrap
assumptions on ∂_u r and 1−μ". Valid for each cone solution and, by pointwise
passage (the limit solves SSESF classically, l. 2059), for the limit. The
coordinator's refusal to use §4's small bound for first derivatives of r is
correct; see O10 for the typo itself.

### O3. What Theorem 1.1 (1.9) actually bounds — PASS (as printed; scoping noted)

(1.9) bounds: |φ| ≤ Cε min{1, r^{−γ}}; |∂_v(rφ)| ≤ C(|Φ(v)| + ε min{1,r^{−γ}});
|∂_u(rφ)| ≤ Cε; and |∂_v²(rφ)| + |∂_v²r| + |∂_u²(rφ)| + |∂_u²r| ≤ Cε.
So (1.9) contains **pure second null derivatives of rφ and r only** — no mixed
derivatives, no first derivatives of φ. The coordinator never attributes more
to Theorem 1.1 (its §1 correctly sources φ-orders from §4), so this is a
scoping confirmation, not a defect. Note |∂_u²r|, |∂_v²r| ≤ Cε supply the
first derivatives of ν and λ needed later.

### O4. Axis-inclusive first derivatives of φ — PASS (printed)

(3.9) `eq:btstrp:pf:dvphi`: |λ⁻¹∂_vφ| ≲ min{(|Φ(v)|+εr₊^{−δ})/r, **ε**} — the
near-axis branch comes from the differentiated averaging formula (2.23) with
the bootstrap bound on (∂_v r⁻¹∂_v)²φ; proof l. 1032-1038 explicitly does the
axis-inclusive case. Prop 3.16 (3.27) `eq:est4duphi`: |ν⁻¹∂_uφ| ≤ Cε min{1, r⁻¹},
with a dedicated near-axis argument (l. 1669-1686). Since λ ≥ 1/3, ν ≤ −1/6,
both |φ_v|, |φ_u| ≤ Cε uniformly, axis-inclusive and u₀-uniform (these
estimates are bootstrap-stage but the bootstrap is closed in §3.6-3.7, and §4
cites exactly these labels at l. 2043). This is the load-bearing input for the
weighted-mass estimates and it is printed.

### O5. m = O(r³) at the axis — PASS (printed)

(3.11) `eq:btstrp:pf:m`: **m ≲ ε² min{r³, r₊^{1−δ}}**, proved by integrating the
printed mass equation from the axis (l. 1066-1079); (3.12): m/r^k ≤ Cε²r₊^{−k+1−δ}
for 0 ≤ k ≤ 3. This is the coordinator's |m| ≤ Cr³. Together with the mass
equations and |φ_a| ≤ Cε (O4) it gives |m_a| ≤ Cr² directly.

### O6. φ through order two, pure, axis-inclusive, uniform — PASS (printed, one imprecision)

§4 l. 2043-2051 displays, for each cone solution, the uniform bounds

    Σ_{k=0}^{2} sup_{PD_{[u_n,∞)}} (|∂_v^k φⁿ| + |∂_u^k φⁿ|) ≲ A + ε,
    Σ_{k=0}^{2} sup (|∂_v^{k+1}(rⁿφⁿ)| + |∂_u^{k+1}(rⁿφⁿ)|) ≲ A + ε,
    Σ_{k=0}^{2} sup (|∂_v^{k+1} rⁿ| + |∂_u^{k+1} rⁿ|) ≲ ε(A + ε).   [typo: see O10]

The k ≤ 2 φ sum covers exactly "all (pure) derivatives of φ through order two",
axis-inclusive (PD ∋ Γ). Inputs: k = 0, 1 from (3.8), (3.9), (3.27); k = 2 from
(3.48) |(∂_v r⁻¹∂_v)²φ| ≲ sup|(∂_v r⁻¹∂_v)³(rφ)| and (3.55) `eq:est4duduphi`
| (∂_u r⁻¹∂_u)²φ| ≲ sup|(∂_u r⁻¹∂_u)³(rφ)| (both non-degenerate: normalized
second derivatives of φ are bounded outright, so φ_uu, φ_vv ≤ C after commuting
with λ, ν). Imprecision: the k = 2 φ terms and the rφ, r sums of order ≥ 2 are
proved (via Prop 3.18) only on the domain-of-dependence blocks D(u_n, v₀), while
the displayed sup runs over PD_{[u_n,∞)}. For the Arzelà-Ascoli argument on
compact Ω ⊆ PD this is harmless (Ω ⊆ D(u_n, v₀) for n large and v₀ large), but
the displayed line overstates the proven domain. Bookkeeping note, not an input
defect.

### O7. Mixed second derivative φ_uv — REPAIR (prose-only in source; derivation supplied)

The only printed support is the §4 prose sentence (l. 2052): "Uniform bounds
for a corresponding number of mixed derivatives follow from the wave equations
for φ and r." No mixed estimate is displayed, and "corresponding number" is
unspecified. The coordinator consumes |φ_uv| ≤ C (axis-inclusive, u_n-uniform)
in the C^{1,1} quotient bound for φ and hence for the C¹,¹ Cartesian lift of
the scalar (its ∂_tφ Lipschitz requires φ_tt = φ_uu + 2φ_uv + φ_vv bounded).
Supplying the derivation from printed inputs (constants uniform in u_n):

1. From the printed wave equation (2.8) `eq:wave4dvrphi` written as
   ∂_u(φ + rψ) = −K·rψ with K = 2mν/((1−μ)r²), i.e. ψ_u = −c/r where
   c := φ_u + νψ + Krψ.
2. c is continuous; c(t,t) = 0 *after* the parity argument (O9). Before parity,
   boundedness of ψ already forces c ≡ 0 on the axis: if c(t₀,t₀) ≠ 0 then
   ψ_u ≍ −c/r along fixed v, and integrating du = dr/ν against 1/r gives a
   logarithmic blow-up of ψ, contradicting the printed (3.9) bound |ψ| ≤ Cε.
3. Rate: ∂_u(rc) = rB − cKr with B = φ_uu + ν_uψ + (Kr)_uψ, and |B| ≤ C from
   printed inputs (|φ_uu| ≤ C from O6; ν_u = ∂_u²r ≤ Cε from (1.9);
   K ≤ Cr from (3.11); (Kr)_u ≤ C from m_a, μ_a, r_a bounds). Gronwall
   integrated from the axis (c = 0 there) gives |rc| ≤ C∫_u^v r du' ≤ Cr²
   using (3.2) r ≍ v−u; hence |c| ≤ Cr, |ψ_u| ≤ C, and
   φ_uv = ∂_u(λψ) = λ_uψ + λψ_u ≤ C.
This closes the input without the prose sentence; it also *re-proves* parity
(3) for φ independently. Verdict: the reconstruction's needs are met, but at
integration the coordinator note should either cite this derivation or replace
the appeal to the §4 prose sentence by it.

### O8. Pure third derivatives of r — PASS (derivation from printed (3.45)/(3.47) verified)

Prop 3.18 bounds **second normalized pure derivatives of log λ and log ν**
((3.45): |(λ⁻¹∂_v)² log λ| ≲ εA + ε²; (3.47): |(ν⁻¹∂_u)² log ν| ≲ εA + ε²),
not r''' directly — the earlier regularity lane's characterization is exact.
The coordinator's step "(3.45), (3.47) and lower-order bounds give pure third
derivatives of r" is verified: e.g. ν_uu = ν²[(ν⁻¹∂_u)² log ν + ((ν⁻¹∂_u) log ν)²],
where the first normalized log-derivative is bounded by (3.29)
|ν⁻¹∂_u log ν| ≤ Cε² (and symmetrically (3.14)), and |ν| ≤ 2/3 from (1.8);
likewise λ_vv from (3.45) and |λ_v| ≤ Cε from (1.9). Constants u₀-uniform by
Prop 3.18's statement (l. 1815). Axis-inclusiveness of Prop 3.18 is explicit in
its proof: the u-side half is anchored at the axis using (2.4) with the printed
sentence "∂_v r, ∂_u r, ∂_v(rφ) and ∂_u(rφ) are C² up to the axis Γ" (l. 2000-2009).
Fidelity note: the u-side halves of (3.44)-(3.47) are proved by **sketch**
("with the roles of u and v interchanged ... we only sketch the argument",
l. 1982-1984); the v-side is complete. Standard symmetry; recorded honestly.

### O9. Axis parity identities — PASS (conclusions correct; one written derivation was conditional)

- r_t(t,0) = r_tt(t,0) = 0: printed, not merely derivable — (2.4) `eq:bc4high-d`
  states (∂_v+∂_u)^ℓ r(a,a) = 0 for ℓ = 0..k for any C^k solution, and (2.4)
  applies to the limit because rⁿ → r in C² and r = 0 on Γ is asserted at
  l. 2052. The coordinator's tangential-differentiation route is equivalent.
- r_ρρ(t,0) = 0: verified. Algebra: r_ρρ = r_tt − 4r_uv (exact; check T1).
  r_uv(t,t) = lim 2mνλ/((1−μ)r²) = 0 because |m| ≤ Cr³ (O5) makes the right
  side O(r). The note's derivation is correct.
- φ_ρ(t,0) = 0: conclusion TRUE. Two independent routes verified:
  (i) The coordinator's written route is *conditional*: it uses the printed
  SSESF equation ∂_u∂_v(rφ) = (2mνλ/((1−μ)r²))φ (l. 320), which at the axis
  gives (rφ)_uv(t,t) = lim r_uv·φ = 0, then expands by the Leibniz rule; the
  surviving term (λφ_u + νφ_v)(t,t) = 0 follows **only after discarding
  r·φ_uv → 0, which needs |φ_uv| ≤ C (O7)**. So as written it leans on the
  §4 prose sentence or on the O7 lemma.
  (ii) The O7 lemma needs no parity input and yields c ≡ 0 on Γ directly,
  i.e. φ_u(t,t) = −ν(t,t)ψ(t,t) = φ_v(t,t) (using ν = −λ from (2.4) with ℓ=1),
  hence φ_ρ(t,0) = 0. Machine-verified bookkeeping: check T4 (below).
  No step assumes a smooth 4D atlas; everything is quotient-level.

### O10. §4 "small bound" for first derivatives of r — CONFIRMED TYPO, correctly quarantined

The third displayed §4 line (l. 2049-2050) asserts
Σ_{k=0}^{2} sup(|∂_v^{k+1} rⁿ| + |∂_u^{k+1} rⁿ|) ≲ ε(A+ε). Its k = 0 part
claims |∂_v rⁿ| + |∂_u rⁿ| ≲ ε(A+ε), contradicting (1.8) (∂_v r > 1/3,
|∂_u r| ≥ 1/6) and the gauge normalization ∂_v r|_{C_{u₀}} = 1/2. The k = 1, 2
parts (second and third derivatives of r ≲ ε(A+ε)) are consistent with
(1.9) and Prop 3.18 and are fine. The coordinator does not use the k = 0 part
anywhere; the reconstructed inputs are (1.8) for first derivatives plus the O2
upper bound. Verdict: typo confirmed and isolated; no valid estimate is lost.

### O11. Weighted mass estimates |m_a| ≤ Cr², |m_ab| ≤ Cr, μ_a ≤ Cr, μ_ab ≤ C — PASS (derivation verified term-by-term)

Not printed as such in LOY; the coordinator derives them. Verified line-by-line
with printed inputs only (|φ_a| ≤ Cε from O4; second derivatives of φ bounded
axis-inclusively from O6; degenerate bounds r·(normalized second φ-derivative)
≤ C from (3.10)/(3.48)-(3.50) and (3.55) suffice because every such term is
multiplied by the r² or r prefactor of the mass equations; λ, ν, r_a bounds
from (1.8); λ_u, ν_v = r_uv ≤ Cr from the SSESF equation + (3.11); m_a ≤ Cr²
from the mass equations + O4; (3.2) r ≍ v−u):
- ∂_a of the printed mass equations gives |m_ab| ≤ Cr (each of the four-to-five
  product terms is O(r); the potentially dangerous φ_ba terms are harmless
  because they enter as r²φ_vφ_ba/λ with |φ_v| ≤ Cε, so even the degenerate
  C/r bounds on φ_ba suffice).
- μ_a = 2m_a/r − 2mr_a/r² ≤ Cr; μ_ab = 2m_ab/r − 2(m_a r_b + m_b r_a + m r_ab)/r²
  + 4m r_a r_b/r³ ≤ C: the last term is the only one that would blow up with
  m = O(r) or O(r²) (r_a does not vanish at the axis), which is why the O(r³)
  mass bound O5 is genuinely load-bearing. Verified: every term ≤ C.
- Extension of μ by 0 on Γ with |μ| ≤ Cr², |∂μ| ≤ Cr and bounded weak Hessian:
  C¹,¹ on the closed half-plane; μⁿ → μ in C¹ across the thin axis strip as the
  note describes. No division is assigned a value on the axis.

### O12. Same-subsequence quotient C^{2,1}/C^{1,1} bounds — PASS

All inputs above carry constants independent of u_n, so *every* subsequence
produced by the §4 Arzelà-Ascoli passage inherits: r ∈ C^{2,1} (needs all four
third derivatives: pure from O8, mixed r_uuv, r_uvv from differentiating the
printed r_uv equation once — each of the five product terms ≤ C using O11,
|ν_u|, |λ_v| ≤ Cε from (1.9), μ_a ≤ Cr from O11; no circularity: O11 uses no
third derivative of r); φ, m, μ ∈ C^{1,1} (φ needs φ_uv from O7; m needs
second pure φ-derivatives only); F = Ω², A = B², D = F − A ∈ C^{1,1} with
D(t,0) = D_t(t,0) = D_ρ(t,0) = 0 and |D| ≤ Cρ², |D_t|, |D_ρ| ≤ Cρ. The axis
values a(t) = r_ρ(t,0) = 2λ(t,t) ≥ 2/3 and A(t,0) = F(t,0) = a(t)² follow from
(1.8), (2.4), O9 and the Ω² identity in O13.

### O13. §4 compactness passage and convergence statements, axis included — PASS (verbatim)

Printed at l. 2052-2059: rⁿ → r in C²(Ω), (φⁿ, ∂_v(rⁿφⁿ), ∂_u(rⁿφⁿ)) →
(φ, ∂_v(rφ), ∂_u(rφ)) in C¹(Ω), mⁿ → m in C¹(Ω), on **every compact
Ω ⊆ PD**, with r = m = 0 on Γ asserted; PD contains Γ, so these are
axis-inclusive statements. The limit solves SSESF classically (l. 2059) and
retains the u₀-uniform bounds (l. 2060). The note's reading "on compact
quotient sets, including the axis" is exactly what is printed. Remark 4.1
(l. 2081-2088) additionally gives, for the limit, Lipschitz ∂²(rφ), ∂²r in the
pure directions with esssup weak third pure derivatives — pure directions only;
the mixed Lipschitz bounds used by the coordinator come from O7/O8/O12
derivations, not from Remark 4.1. Also printed: "it also follows that the C²
norm of mⁿ is uniformly bounded on any compact subset of PD_{[u_n,∞)}"
(l. 2052), consistent with (3.11), (3.13), (3.50).

### O14. Ω²/F identity and the C¹,¹ algebra — PASS

F ≡ Ω²: −4νλ = r_ρ² − r_t² follows from ν = (r_t − r_ρ)/2, λ = (r_t + r_ρ)/2
(difference of squares; machine check T1 covers the operator algebra
r_uv = (r_tt − r_ρρ)/4, and check T3 confirms the parity bookkeeping
(νφ_u + λφ_v)(t,0) = 0 structure). C^{1,1} functions form an algebra under
products and quotients with 1−μ ≥ 1/2, so F, A, D ∈ C^{1,1} from r ∈ C^{2,1},
μ ∈ C^{1,1}. Verified additionally by exact polynomial arithmetic (§4 below):
D = F − A has vanishing ρ⁰ and ρ¹ coefficients (check T5).

### O15. Profile hypotheses: smooth compact profiles and compact families — PASS (at the estimate level)

Theorem 1.7 needs Φ smooth with (1.20) on all of R²_{u≤v} — ∫_u^v|Φ| ≤
ε(v−u)^{1−δ}, |Φ| + |Φ'| ≤ ε — plus sup|Φ''| < ∞. Any smooth compactly
supported Φ, amplitude-scaled to |Φ| + |Φ'| ≤ ε, satisfies (1.20): for
v−u ≤ 1, ∫_u^v|Φ| ≤ ε(v−u) ≤ ε(v−u)^{1−δ}; for v−u ≥ 1 the integral is
bounded by the compact support while ε(v−u)^{1−δ} grows. A compact parameter
family {Φ_θ} with sup_θ(|Φ_θ| + |Φ'_θ|) ≤ ε and sup_θ|Φ''_θ| ≤ A satisfies all
hypotheses *uniformly* (Prop 3.18's ε₂ is independent of A; constants depend
linearly on A). Caveat outside this lane's claim: LOY produces, for each
profile, a subsequential limit along the chosen u_n; nothing in LOY gives a
common diagonal subsequence for a continuum of profiles or uniqueness of the
limit. The coordinator claims only estimate-level applicability ("applies to
any subsequence with these bounds"), which is correct; the family-level limit
belongs to the separate scattering-map lane.

## 2. Source orders actually consumed (brief requirement)

For the weighted mass estimate m_ab = O(r) and the metric coefficient F = Ω²:

- **m_ab = O(r)** consumes: the printed SSESF mass equations (φ through order
  1, squared); |φ_a| ≤ Cε (order 1 of φ, axis-inclusive: (3.9), (3.27));
  second derivatives of φ entering only via r·(normalized second derivative)
  or products with |φ_a| (order 2 of φ: (3.10)/(3.48), (3.55), and O7 for the
  mixed one); m = O(r³) (order 0 of m: (3.11)); m_a ≤ Cr² (order 1 of m, from
  the mass equations + O4); μ_a ≤ Cr (order 1 of μ, from O5 + (1.8)); λ_u =
  ν_v = r_uv ≤ Cr (order 2 of r, **mixed**, from the printed SSESF equation +
  (3.11)); |λ_v|, |ν_u| ≤ Cε (order 2 of r, pure: (1.9)); two-sided λ, ν, μ
  bounds (order 1 of r: (1.8) + O2); r ≍ v−u ((3.2)). **No third derivative of
  anything is consumed by m_ab = O(r).**
- **F = Ω² ∈ C^{1,1}** consumes, in addition: all four third derivatives of r
  (pure via (3.45)/(3.47) + (1.9) [O8]; mixed r_uuv, r_uvv via one further
  differentiation of the printed r_uv equation, using m_ab = O(r) [O9, O11]);
  μ_ab ≤ C (O11); and for the scalar lift, φ ∈ C^{1,1}, i.e. φ_uv ≤ C (O7).
- The coordinator's §1 summary "all derivatives of r through order three; all
  derivatives of φ through order two" is therefore **exactly right** as the
  consumed order set, with the caveat that the mixed members of these sets are
  not printed estimates in LOY (see O7, O9).

## 3. Verification commands and results

- Source acquisition: `curl -sL https://arxiv.org/e-print/1605.03893v1` →
  gunzip → `SSESF-LargeBVScat.160512.tex` (gzip member name matches the
  160512 date; single-file v1 source). All locators grepped in this file.
- Exact-arithmetic algebra check (pure Python, exact rational polynomial
  arithmetic on the model r = a(t)ρ + b(t)ρ³ (odd), φ = p(t) + q(t)ρ² (even),
  μ = κ(t)ρ²; wall time well under 1 s, hard alarm 10 s):
  - T1: r_uv ≡ (r_tt − r_ρρ)/4 identically; r_uv(t,0) = 0. TRUE.
  - T2: (ν + λ)(t,0) = 0 and (νφ_u + λφ_v)(t,0) = 0. TRUE.
  - T3: −4νλ = r_ρ² − r_t²: difference-of-squares identity, verified by
    inspection (an intermediate checker draft had a sign typo; not rerun).
  - T4: the Leibniz axis bookkeeping — (rφ)_uv − r_uv·φ agrees at the axis
    with (λφ_u + νφ_v)(t,t), and (r_uv·φ)(t,t) = 0. TRUE (this is precisely
    the parity-(3) step of O9(i)).
  - T5: D = F − A has vanishing ρ⁰, ρ¹ coefficients; lowest nonzero degree 2.
    TRUE.
  - T6: ψ + χ vanishing at the axis structure. TRUE.
  - (One earlier checker draft reported spurious FALSE values due to bugs in
    the checker itself — sign errors and a dropped constant term — not in the
    identities; the corrected run above is the record.)

## 4. Strongest residual objection

**The whole reconstruction has exactly one load-bearing input that is neither
a printed displayed estimate nor printed as a proved theorem: the
axis-inclusive, u₀-uniform bound |φ_uv| ≤ C.** It is asserted only by the §4
prose sentence "uniform bounds for a corresponding number of mixed derivatives
follow from the wave equations" (l. 2052), which does not name the derivatives,
their order, or their domain, and whose k ≥ 2 sibling displayed bounds are
stated on a larger domain than proved. Everything downstream that involves the
scalar field — parity (3) as written in the coordinator note, φ ∈ C^{1,1},
the C¹,¹ Cartesian lift of φ, and hence the distributional statement
Ric = 2 dφ⊗dφ in the reconstructed chart — depends on it. The metric-side
reconstruction (F, A, D, E_ij) survives without it. This audit supplies the
missing derivation (O7, three printed inputs: (3.9), (3.11), (2.8)), so the
objection is currently *answered*, but it is the right place to attack: a
flaw in step 2 or 3 of O7 (e.g. if (Kr)_u were not uniformly bounded on
PD_{[u_n,∞)} beyond the bootstrap domain) would remove only the scalar-field
half of the reconstruction, not the metric half. Secondary residual: the
u-side halves of Prop 3.18 (l. 1982-2010) are proof sketches; an error hidden
there would degrade O8/O12 to v-side-only statements.

## 5. What this audit does and does not establish

Established: the coordinator's finite-order source-input list corresponds to
LOY v1 at the stated orders and uniformities; the §4 typo is real and safely
quarantined; the needed mixed estimates, while not displayed in LOY, follow
from printed estimates by verified bounded derivations; the parity identities
hold without any prior smooth 4D atlas; smooth compact profiles (and compact
families, estimate-wise) satisfy the precise hypotheses; the same selected
subsequence carries quotient C^{2,1}/C^{1,1} bounds.

Not established here: the C¹,¹ Cartesian lifting lemma itself (separate lane);
smooth-MGHD applicability; differentiability of the scattering map; uniqueness
of the u₀ → −∞ limit; any claim that the reconstruction is C² or smooth; any
novelty or priority claim; the philosophical consequences of the reconstruction.
