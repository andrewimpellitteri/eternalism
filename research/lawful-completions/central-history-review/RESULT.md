# central-history-review: audit of the whole central scalar-history candidate

31 October 2026. OpenCode GLM worker for `lawful-central-history-review`.
Submission for coordinator inspection; **not** acceptance. Scope: audit the
conditional whole-function candidate in
`../claude-central-history/RESULT.md` (as repaired by its `REVIEW.md` R1–R4),
against the brief's checklist. I did not overwrite Claude's files, implement a
competing theorem, or alter any coordination file. No novelty or ontological
claim. Inputs read: `claude-central-history/{RESULT,REVIEW,CONTRACTION,
REVIEW_CONTRACTION,PRIOR_WORK,CARD}.md` (verified byte-identical to commit
`5f50cee`); `coordinator/C11_FINITE_CONTROL.md`,
`FINITE_CONTROL_ACCEPTANCE.md`, `COMPACTNESS_CONTINUITY_REPAIR.md`,
`RESPONSE_REDUCTION.md`, `NEXT_FRONTIER_TASKS.md` §3;
`claude-finite-control-audit/{RESULT,SECOND_READ,REPAIR_B_REVIEW}.md`;
`finite-control-review/RESULT.md`. `CONTRACTION.md`, `REVIEW_CONTRACTION.md`
and `PRIOR_WORK.md` were treated as **candidates**, not accepted inputs, per
the brief. R3 and R4 were treated as sketches throughout.

## Verdict

**No counterexample found. The integrated-class claim (readings on the whole
window, conditional on Theorem 1.1 + printed §3 bounds + Repair A + C11
compactness) survives my audit except for one assembly step: §4's
trace-error estimate `|Ψ−𝒯_nΨ| ≤ 2η·Lip(𝒯_nΨ)` is carried by no input listed
in the claim's conditional list.** It needs a vertex-uniform C⁰ difference
estimate for the trace map — the substance of the separate `CONTRACTION.md`
candidate (one adversarial read, not accepted) — or a bounded reassembly that
uses Repair A′ and makes the trace error exactly zero at each finite n; I
verified that reassembly closes §5 with no further input. Second gap: the
claim consumes Theorem 1.1 on a merely Lipschitz ball, while the theorem is
printed for smooth data; the needed density extension is real but unstated.
The C¹,¹ form of the claim still rests, as the candidate itself labels, on
LOY's own sketches (Lemma 3.19, (3.46)–(3.47) — sketch status confirmed
verbatim in v1) or on Repair B's open qualitative premise; that remains the
first genuinely unmet obligation of the strongest form. R2's tail is now
verified directly against the source: LOY's own (5.1) Step 1 prints exactly
the disjoint-bump argument with parameter `C_γ·ε′` independent of the number
of bumps. Everything else on the brief's checklist checked out.

## 1. Strongest finding: §4's trace-error bookkeeping is uncarried

RESULT.md §4 derives, from the fixed point `Ψ = J_η𝒯_nJ_ηΨ`,

> `|Ψ−𝒯_nΨ| ≤ 2η·Lip(𝒯_nΨ)` on `t ≤ t̄`, "which is Λ times the trace error".

Splitting the fixed-point identity gives

    Ψ − 𝒯_nΨ = J_η𝒯_nJ_ηΨ − 𝒯_nΨ
             = [𝒯_nJ_ηΨ − 𝒯_nΨ] + [J_η𝒯_nJ_ηΨ − 𝒯_nJ_ηΨ],
    ‖Ψ − 𝒯_nΨ‖ ≤ ‖𝒯_nJ_ηΨ − 𝒯_nΨ‖_C⁰ + 2η·Lip(𝒯_nΨ).

The second term is standard. The first is the problem:

- **Repair A does not bound it.** Repair A controls the solution difference by
  `‖δΦ‖_(C¹)` with `δΦ = J_ηΨ − Ψ`. For `Ψ ∈ B` merely Lipschitz,
  `(J_ηΨ)′ = J_η(Ψ′)` and `‖J_η(Ψ′) − Ψ′‖_∞` is **O(‖Ψ′‖_∞), not O(η)**:
  mollification does not converge in L∞ on arbitrary Lipschitz data. My
  numerical check (M=1, η=10⁻³, Ψ=2M|t|, ρ=6σ(1−σ)): C⁰ defect at the kink
  0.001 (= η·O(M)), derivative defect inside the window 2.00 and 3.37 —
  order M, not order η. So `‖J_ηΨ − Ψ‖_(C¹)` is not small, and for the
  C¹ sequence members it shrinks only at each member's own modulus of
  continuity of Ψ′, which is **not uniform over B** (B bounds Lipschitz
  constants, not moduli of Ψ′).
- **Repair A′ does not bound it at the needed rate.** A′ (dropping δL_v)
  gives C⁰ continuity of the solution map at each fixed n, with a Volterra
  constant over the triangle `{u_n ≤ u ≤ v ≤ t̄+2}` that may blow up as
  `n → ∞`. The fixed points need `η_n → 0` simultaneously with `n → ∞`; a
  per-n modulus with no uniformity cannot absorb `2Mη_n`.
- **The accepted C11 compactness inputs do not bound it.** They give
  continuity of the solution map in C²/C¹ data via compactness + uniqueness
  for the smooth finite-sample family, and neither the C² data convergence
  nor the smoothness holds here (`J_ηΨ` is C¹ at best, `Ψ` Lipschitz).

So, as written, the passage "fixed point ⟹ trace error O(η_n) ⟹ trace
equation exact in the limit" consumes a **vertex-uniform C⁰ difference
estimate for Λ, I, τ** that is neither Repair A, nor Repair A′, nor the
accepted C11 inputs. That estimate is exactly what `CONTRACTION.md`'s Lemma
supplies (its `|δ𝒯| ≤ C_ℓM²‖δΦ‖` in C⁰, uniform in the vertex for
`C_ℓε̃² ≤ ¼`), and `CONTRACTION.md` is a single-adversarial-read candidate,
not an accepted input. RESULT.md §6.5 does flag CONTRACTION as a separate
one-read candidate, but §4's derivation as printed does not depend on it
explicitly — the estimate is silently uncarried.

**Bounded repair (verified to close, no new inputs beyond the already-listed
conditionals plus Repair A′).** Drop the mollifier and apply Schauder to
`𝒯_n` directly:

1. `𝒯_n: B → B` without the inner J: for `Φ ∈ B` and `t < A+δ` the data
   vanish on `v ≤ t`, so Λ=1, τ=t, y(t)=0, I=0, hence `𝒯_nΦ(t)=0` there;
   past `t̄+1`, χ=0; the §2 norm bound gives Lip ≤ 2M. (This is the same
   left-edge argument RESULT.md §4 makes; the inner J is only needed for the
   mollifier route's continuity.)
2. Continuity `B → B` in C⁰ is Repair A′ (single-second-read; REVIEW.md item
   3 records it as verified and as the route "if the mollifier is dropped").
3. B is convex and C⁰-compact; Schauder gives `Ψ_n = 𝒯_nΨ_n` — the **trace
   error is exactly zero at every n**.
4. §5 then closes with no data-continuity input at all: along the
   subsequence, `Ψ_n → Ψ_*` in C⁰, the solution families `S_n(Ψ_n)` have
   uniform (1.8)–(1.9)/§3 bounds (same ball, same ε̃), so equicontinuity
   gives convergent axis traces `Λ_n → Λ_*`, `I_n → I_*`, `τ_n → τ_*` on
   compact axis segments, and the per-n identity
   `Ψ_n + I_n − Λ_n y∘τ_n = 0` passes to `Ψ_* + I_* = Λ_* y∘τ_*` exactly.
   The flat wedge passes per approximant; the mass identity is algebraic in
   converging quantities. No identification of subsequential limits with
   "the" solution at data Ψ_* is needed for the readings, so no
   uniqueness-at-Lipschitz-regularity input is consumed on this route.

Cost of the repair: Repair A′ replaces the mollifier as a load-bearing
single-reader derivation, and `𝒯_n` must be well defined on all of B (see
§2 below). Either that repair is adopted, or §4 must import
CONTRACTION.md's uniform estimate explicitly and inherit its review status.
This is the first obligation I found failed-as-written; it is an assembly
gap, not a counterexample, and the readings claim survives under either
route.

## 2. Second finding: Theorem 1.1's smooth-data scope vs the Lipschitz ball

Theorem 1.1 (verified verbatim, §6 below) hypothesizes "**a smooth function**
Φ satisfying (1.7)". The claim's fixed-point ball B contains non-smooth
members, and the construction applies the finite-cone theory to them:

- Mitigating, from the candidate's own §2 gain: `𝒯_nΦ ∈ C¹` for every
  `Φ ∈ B` when `y ∈ C¹` (Λ, I ∈ C¹ for Lipschitz Φ), so every fixed point
  is C¹ data, within the C^k, k≥1 local statement of LOY §2.1 (also
  verified verbatim). The mollifier route even starts from C¹ data
  (`J_η𝒯_nJ_ηΨ` is C¹).
- Still unstated: **global** existence for C¹ (not smooth) data is an
  extension — the printed theorem says "smooth". The lane implicitly
  consumes this everywhere (Definition 2.1's k≥1 class; C11's compact
  limits are C¹ solutions), so it is a bookkeeping obligation rather than a
  new gap, but RESULT.md's conditional list should name it: "Theorem 1.1,
  extended from smooth to C¹ data by its own local statement plus the
  uniform bootstrap".
- At the **Lipschitz** level (needed if 𝒯_n is iterated on B before taking
  the C¹ gain, and for the integrated-class limit) existence goes by
  density through C¹ members, with sublimit identification in the integrated
  class. The A′-route repair of §1 avoids needing uniqueness of
  subsequential limits; the mollifier route does not.
- Related scope note, verified verbatim: Theorem 1.7 (two-sided complete
  solution with `lim_{u→−∞} 2∂_v(rφ) = Φ`) requires `sup|Φ″| < ∞`
  (its (1.20)) — so the source's own two-sided theorem **cannot** be cited
  at Lipschitz regularity, and the candidate's own §5 compactness passage is
  what does that work. That passage is sound (§3 below) but should be
  labeled a project extension of the printed scattering-limit statement.

## 3. Confirmed items

Each item below was checked by my own derivation or directly in the arXiv v1
source; the depth is recorded per locus in §6.

1. **Exact axis identity — re-derived.** From the SSESF wave identity
   `φ_uv = −(ν/r)φ_v − (λ/r)φ_u` and `r_uv = λ_u = λK`, all cross terms
   cancel: `p_uv = λKφ`. Integrating `(λL)_u = p_uv` from the cone
   (`λ(u₀,v)=½`, `L(u₀,v)=Φ(v)`): `2λL = Φ + ∫2λKφ`. On Γ, `p(u,u)=0` gives
   only tangentiality, so `∂_v p(u,u) = λφ` and `L = φ` on Γ. Hence
   `Λ(t)φ_c(t) = Φ(t) + I(t)`, `Λ = exp∫K`, matching RESULT.md §1 and LOY's
   (3.14) per REVIEW.md. A fixed point of 𝒯 implies `φ_c = y∘τ` on the
   window (τ(t̄) ≥ T_max via Λ ≥ 2/3); only this direction is used, and the
   note says so.
2. **Causal/Volterra structure and B-invariance — re-derived.** Λ(t), I(t),
   τ(t) depend on Φ only at `v ≤ t` (sub-triangle domain of dependence,
   Repair A). The retarded J_η never moves a left edge and extends a right
   edge by ≤ η; 𝒯_nJ_ηΦ vanishes below A+δ and past t̄+1, so the χ slack
   (cut to zero within one unit, η < ½) makes `J_η𝒯_nJ_η: B → B` exact.
   Norm bookkeeping (`(1+Cε̃²)‖y‖ + Cε̃³ ≤ 2M` for `M ≤ M_*`, ball radius 2M
   vs target norm M) is consistent with REVIEW's correction.
3. **No derivative loss — confirmed with the correct scope.** `y ↦ Φ` has
   order zero (reparametrized identity plus a correction smooth in its Φ
   dependence off the axis). The constants see `‖Φ′‖` (through ε̃, via the
   r≤1 estimates) and no `Φ″`; the threshold M_* is fixed before the R3
   ball constant `a = 2‖y″‖+1`. The map is Lip→Lip and **not** C⁰→Lip, so
   continuous targets are out of scope — correctly stated in the claim.
4. **C¹ target vs C¹,¹ target — boundary is exactly C¹,¹.** Necessity:
   `g,φ ∈ C¹,¹` gives Γ Lipschitz, `γ ∈ C²,¹`, hence `φ∘γ ∈ C¹,¹`; so
   `y ∈ C¹ ∖ C¹,¹` admits no model in C11's category (REVIEW's argument;
   confirmed). Sufficiency for `y ∈ C¹,¹` is R3, conditional as in §4.
5. **No smallness on the second derivative — confirmed at the strongest
   available level.** Prop 3.18's printed statement: ε₂ "independent of
   u₀, v₀ **and A**", bounds `≲ A+ε` and `≲ εA+ε²` with implicit constant
   independent of all four (verbatim). LOY's footnote to Theorem 1.7 states
   the ε-shrinkage for the u₀→−∞ procedure is "independent of the second
   derivative bounds of Φ" (verbatim). R3's closure introduces no y″
   smallness. Caveat: this rests on printed statements whose u-side proofs
   are sketched (§4).
6. **Uniform cone estimates — confirmed structurally.** Remark 1.2
   (verbatim: constants "independent of u₀") plus the (3.7) weight `k=2`
   and the near-axis behavior `K ≲ m/r² ≲ ε̃²r` from printed (3.16)
   `m ≲ ε²min{r³, r^{1−γ}}` make the §2 bounds vertex-uniform. REVIEW's
   hand-check of the I′ integrals (`∫|λK_vφ|, ∫|λKφ_v| ≲ ε̃³`, boundary
   term killed by K=0 on Γ) is consistent with printed (3.24), (3.31),
   (3.35), (3.25), (3.29), all of which I verified at exact numbering.
7. **Parameter-dependent compactness — confirmed for this candidate.** The
   profile ball is C⁰-compact; the solution families for `Ψ_n ∈ B` have
   member-uniform Theorem 1.1 bounds because ε̃ is fixed by `‖y‖_(C¹) ≤ M`
   (no parameter family in the C11 sense is iterated here). For R3's C¹,¹
   compactness the uniform third-order budget is exactly the sketched
   region — same caveat as §4.
8. **R2's tail — verified against the source.** LOY's (5.1)
   `Φ = ε′Σ_{k≥3}χ(v−u₀−2^k)` and its Step 1 print the exact mechanism
   REVIEW.md R2 cites: disjoint supports give at most one nonzero term per
   v, so `|Φ|+|Φ′| ≤ ε` with ε′ small (uniform in the number of bumps);
   the integral condition is `∫|Φ| ≤ 5ε′(log₂⌊v−u⌋+100) ≤ C_γε′(v−u)^{1−γ}`
   — parameter `C_γε′` **independent of the truncation level K**. Energy
   `β²‖G_K‖²₂/4` is linear in K (disjoint, comparable bumps), so any
   `E − E_w` is hit exactly by adjusting `β ∈ (0, ε′]` at suitable K;
   readings are untouched by domain of dependence (tail at `v ≥ c ≥ t̄+2`);
   the mass identity is algebraic in the limit, so INCOMING_MASS applies and
   E is the actual total including the compensator. **One missing one-liner:**
   the floor must dominate the window energy `E_w(y) ≲ M²(t̄+2) ≤ 3M²T_max`
   (from `‖Φ_w‖_∞ ≤ 2M`); an absolute c works and the claim's
   `E ≥ cM²T_max` form is fine, but the note should record the bound.
9. **§5's limit passage — coherent per-solution compactness.** Equicontinuity
   of r, λ, ν, L, M, φ, m on compact triangles follows from (1.8)–(1.9) plus
   the §3 bounds (`|K| ≲ r` at the axis from printed (3.16)); the incoming
   identification `L → Φ` at fixed data has a vertex-free rate
   `Cε̃³(A−u)^{−γ}`-type from the same bounds, so each subsequential limit
   has incoming profile `Ψ_*` and satisfies the integrated trace identity
   exactly. LOY's own limit order — "Taking the limit n→∞ first and then
   letting u→−∞" — is printed verbatim twice in its §4, and the candidate's
   order matches it.
10. **Mass and quantifier scope — preserved.** E is the actual iterated
    incoming boundary limit including the late compensator; incoming mass by
    reading time is not fixed and the claim does not say it is. No ADM
    identification, no prefix-mass equality, no whole-realm matching is
    asserted anywhere in the candidate.

## 4. Sketches confirmed as sketches (not audited inputs)

- **R3 (C¹,¹ upgrade).** Its inputs beyond the printed Prop 3.18 statement
  are Lemma 3.19 and (3.46)–(3.47). I verified the sketch labels verbatim in
  v1: Lemma 3.19 — "Since it is rather routine, we will only sketch the
  proof of each estimate"; the u-side halves (3.46)–(3.47) — "To avoid
  repetition, we only sketch the argument". Repair B's replacement argument
  retains an open qualitative u-side regularity premise (`Y < ∞`), per
  REPAIR_B_REVIEW, whose own routes R1/R2 are unreviewed. So the C¹,¹ form
  of the claim remains conditional on material no worker has proven; this is
  the strongest form's first unmet obligation, and the candidate labels it
  accurately.
- **R4 (C¹ limit class).** A sketch, single-reader. Under the §1 repair the
  readings hold for `y ∈ C¹` in the integrated class regardless; what R4
  adds (limit is a C¹ solution in Definition 2.1's sense) stays unproven.
- **Smooth y → smooth model.** Open, as the candidate says;
  SMOOTH_FINITE_CONTROL covers the C11 compact-profile finite-sample family,
  not this fixed-point family. The missing input (order-k bounds, linear at
  top order) is correctly identified.

## 5. Finite-sample vs function-space; philosophical scope

- The candidate does **not** infer function-space control from the
  finite-sample theorems: it builds a separate whole-window fixed point, and
  the readings hold for all `T ∈ [0, T_max]` at once. The threshold
  `M_*(T_max, γ)` depends on the window and degrades as `T_max → ∞`
  (flagged by the candidate, §6.7); no uniform-in-window or
  schedule-uniform-in-N claim is made. C11's per-schedule `E_*(N)` is
  genuinely different, and the comparison sentence "amplitudes up to about
  `M_*Δ`" is heuristic prose, not a theorem — harmless, but it should not be
  quoted as a result.
- Philosophy: no ontology, novelty, non-supervenience or whole-realm claim
  is drawn; the header and CARD.md say so explicitly. PRIOR_WORK.md's
  verdict (setting and method in print — Kehrberger Remarks 2.4/6.1,
  Theorems 2.4, 2.5(b), 6.1 and §2.1; Kehle–Unger for the degree toolkit;
  the inverse statement itself unlocated but plausibly routine) stays a
  candidate: I did not re-search prior work in this task, and the
  nearest-predecessor gate remains open. My audit makes no priority claim.

## 6. Source verification (primary clauses)

Primary source pinned and fetched directly:
**Jonathan Luk, Sung-Jin Oh, Shiwu Yang, "Solutions to the
Einstein-scalar-field system in spherical symmetry with large bounded
variation norms", arXiv:1605.03893v1, 12 May 2016.** E-print TeX
`SSESF-LargeBVScat.160512.tex` (3214 lines, matching prior lanes' records)
plus the arXiv HTML rendering for resolved numbering. My read depth at the
loci below is full-text (statement level); I did not read the §3 bootstrap
proofs, §§5–7, or the published Ann. PDE version.

| Locus | Verified content | Verdict |
|---|---|---|
| Theorem 1.1 (`thm:main.finite`) + (1.7) | hypotheses = `∫_u^v|Φ| ≤ ε(v−u)^{1−δc}` **and** `|Φ|+|Φ′| ≤ ε`, data "**smooth**" | confirms §2's use, §2's scope gap |
| Remark 1.2 | constants "independent of u₀" (verbatim) | vertex uniformity sourced |
| §2.1 local paragraph | local well-posedness for C^k data, k ≥ 1, proof omitted | C¹-local exists; global extension unstated |
| Definition 2.1 (`def:C1-sol`) | C^k class exactly as the finite-control audit records | matches |
| Theorem 1.7 (`thm:main`) + footnote | two-sided solution, `lim 2∂_v(rφ) = Φ`, requires `sup|Φ″| < ∞`; ε shrinkage "independent of the second derivative bounds" | no-smallness sourced; Lipschitz scope gap sourced |
| (3.7), (3.12), (3.16), (3.24), (3.25), (3.29), (3.31), (3.35) | weights, `|λ⁻¹∂_vφ|`, `m ≲ ε²min{r³,r^{1−γ}}`, `|K| ≤ Cε²r₊^{−1−γ}`, λ bound, I integrand, K_v bound, `|λ⁻¹∂_v log λ| ≲ ε²` | all printed at exact numbering, as §2 cites |
| Prop 3.18 statement | ε₂ independent of u₀, v₀, A; bounds ≲ A+ε, ≲ εA+ε² | no-smallness on Φ″ sourced |
| Lemma 3.19 label | "we will only sketch the proof of each estimate" | sketch status confirmed |
| (3.46)–(3.47) label | "we only sketch the argument" | sketch status confirmed |
| §4 limit order | "Taking the limit n→∞ first and then letting u→−∞", twice, verbatim | matches C11 §6 / candidate §5 |
| (5.1) + §6 Step 1 | disjoint-bump data; pointwise bound by disjointness; integral by log-count; parameter `C_γε′` | R2's mechanism printed verbatim |
| §6 Step 3 | `∂_v m = ½r²(1−2m/r)(∂_vφ)²/λ` | flux identity printed |

Not read by me: proofs of Props 3.3–3.17, the §3.5/§3.8 bootstrap, §§5, 7,
the NLW part, Appendix A, the published Ann. PDE 4(1):3 version, and all
prior-work sources (Kehrberger, Kehle–Unger, Christodoulou 1993, Manchak,
Carlotto–Schoen) — PRIOR_WORK.md's records stand as candidates.

## 7. Numerics

`volterra_check.py` rerun unchanged in the Claude lane directory: **RESULT.md
§7's table reproduced exactly** (last ratios 0.058/0.060, 0.008/0.009,
0.012/0.009, 0.009/0.009; sweep 0.078, 0.019, 0.005). Runtime 9.8 s (single
domain, u₀=−4; sanity only — it says nothing about uniformity in n, which is
where my §1 gap lives). My §1 toy check (mollified kink, ~2 s) is a
counterexample to the C¹-smallness of `J_ηΨ − Ψ` on the Lipschitz ball, not
to the candidate itself. Total computation ≈ 12 s, within the brief's budget.

## 8. Limitations and proposed next tasks

Limitations: single reader (this audit); Repair A/A′ and CONTRACTION remain
one-or-two-read candidates — my §1 repair shifts weight onto A′ without
adding a second read; the published-version diff (uniqueness proof, (3.3)
φ/rφ anomaly) remains open and could change the trusted-input list; I did not
audit AXIS_C11_RECONSTRUCTION or INCOMING_MASS beyond their accepted
dispositions; no fresh prior-work search.

Proposed next tasks, strongest first:

1. **Rewrite RESULT.md §4 on the A′ route** (or import CONTRACTION
   explicitly) and state the C¹-data global-existence extension in the
   conditional list; add the `E_w ≤ 3M²T_max` floor line. Small, bounded.
2. **Second read of Repair A′** — it becomes load-bearing under repair 1.
3. **Prove or import the order-k bounds** (linear at top order) that would
   carry R3 past LOY's sketches, or prove Repair B's qualitative premise;
   alternatively diff the published Ann. PDE version, which may print the
   u-side arguments.
4. **Nearest-prior check for the whole-function inverse itself** (Kehrberger
   exterior uniqueness + a specialist pass), which PRIOR_WORK.md leaves
   open; decides whether the claim is more than a routine corollary.
5. Only after 1–2: state whether M_*(T_max,γ) can be taken
   T_max-uniform — currently blocked by (1.7)'s `max(1,ℓ^γ)` structure.
