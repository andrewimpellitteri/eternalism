# Higher-regularity audit: Kilgore/Luk–Oh hypotheses against the two-sided LOY scattering family

30 October 2026. Worker submission for independent review; coordinator owns
acceptance. Reading depths are stated per source and in `sources.jsonl`.
Nothing here is a novelty claim, a smoothness theorem, or a nonsmoothness
theorem. Search tool used: `exa.web_search_exa` (worked; result recorded in
`AGENT_REPORT.md`).

## 0. Scope and verdict in three lines

1. **The source-level tension resolves in favor of the selected-full-text
   record.** Kilgore's v1 footnote 1 (TeX line 136, first of four footnotes)
   verbatim excludes direct control of the LOY past-null-infinity scattering
   spacetimes, and the Theorem 3.1 hypothesis package is not satisfied by our
   compact smooth incoming-profile family — not uniformly across the cone
   sequence, and under the literal reading of one display not even per-cone.
2. **The exact missing lemma stays missing from the literature**; the
   in-project conditional supply is `SMOOTHNESS_BOOTSTRAP.md` §1 + §§2–6 with
   `LOCAL_POLAR_PERSISTENCE.md`, at their stated finite-region scope, pending
   integrated review.
3. **The smooth common-development gate remains conditional on that
   bootstrap.** No unconditional source route exists: Ringström needs smooth
   Cauchy data, Galloway–Ling–Sbierski needs ≥C², and the Luk–Oh route needs
   the (D1)–(D8) dispersive package at N≥11, which is strictly stronger than
   smoothness and unverified for our family.

## 1. Resolution of the source-level tension

The two conflicting records were:

* `lawful-coord-kilgore-axis-context-20261029` and
  `lawful-coord-kilgore-uniformity-20261030` (selected full text): footnote 1
  explicitly excludes direct control of the LOY scattering models; Definition
  2.5's weighted norm diverges across the translated cone sequence.
* `RECENT_LITERATURE_2026_10_29.md` item 2 (abstract level): "new bounds
  controlling higher derivatives of both the metric components and the scalar
  field for the same global SSESF class our limits belong to" — suggesting the
  global bounds may help the axis/higher-order gates.

Primary verbatim reading of the v1 TeX (`nonlin_stab.tex`, arXiv e-print
2108.13377v1) confirms, at statement level:

> **Footnote 1 (line 136, verbatim).** "In [Luk–Oh–Yang], Luk–Oh–Yang also
> construct global spacetimes by solving a scattering problem from past null
> infinity. For technical reasons I do not directly control such global
> spacetimes, but instead start from the spacetimes defined to the future of a
> cone. It thus remains open whether there are future and past complete
> spacetimes satisfying the assumptions of Luk–Oh's result [Luk–Oh] in both
> the future and past directions."

So the exclusion is explicit, and additionally the two-sided applicability of
Luk–Oh's own criterion is recorded by Kilgore as **open**. The abstract-level
suggestion is refuted at the theorem-statement level by three facts, each
verified verbatim (locators in `sources.jsonl`):

* (K1) Theorem 3.1's hypotheses are Definitions 2.5–2.6: characteristic data
  on the cone `C₁` **and** on `underline C_R`, asymptotically flat of order
  ω′ ≥ 2 in C^k **towards I⁺ and I⁻**, plus local scattering. Our scattering
  family is built to have prescribed nondecaying data at past null infinity
  (LOY Theorem 1.7: `lim_{u→−∞} 2∂_v(rφ)(u,v) = Φ(v)`), which is precisely
  what Definition 2.5's I⁻ bound rules out under its literal reading (§3, H2).
* (K2) The theorem's constants depend on the **data constants**. Verbatim
  (line 356): "≲ … bounded by B up to a constant depending on the constants
  A, A′ above, the order of derivative |α|, the initial Bondi mass M_{−∞},
  and some more complicaated [sic] quantities depending on low order behavior
  of solutions." No uniformity over a family of data sets is claimed, and the
  A-dependence is not quantified anywhere in the loci read.
* (K3) There is no cone-vertex parameter in the theorem: the vertex is fixed
  at (1,1) by normalization. Vertex-uniformity for our sequence `u_n → −∞`
  becomes uniformity across data sets whose translated weighted norms diverge
  (§3, H1; computational CHECK2).

What the paper does legitimately offer our chain is **methodology**: its §7
averaging-operator axis treatment is prior art for regular-axis parity (with
the direction-of-implication caveat recorded in §4 below), and Theorem 3.1
shows all-order commutation is viable in a related cone-future class. Neither
is a theorem about our family.

## 2. The exact hypothesis loci (v1, verbatim-anchored)

* **Definition 2.4** (`charinit`, line ~322): C^k solutions on domains of
  dependence, with axis conditions `lim (ν+λ)(u,u±ε) = 0` and the analogous
  `∂_v(rφ)+∂_u(rφ)` condition.
* **Definition 2.5** (`asymflat`, lines 333–343): data on `C₁` given by
  `∂_v(rφ)(1,·) ∈ C^k[1,∞)`, on `underline C_R` by `∂_u(rφ)(·,R) ∈ C^k(−∞,1]`
  (prose parenthetical), with bounds
  `sup_{C₁} v^{ω′+l} |∂_v^{l+1}(rφ)| ≤ A` and
  `sup_{underline C_R} (1+|u|)^{ω′+l} |∂^{l+1}(rφ)| ≤ A′` for `l ≤ k`.
  **Recorded inconsistency:** the second display prints `∂_v^{l+1}` where the
  parenthetical introduces `∂_u(rφ)` data; under the literal `∂_v` reading the
  display tests the transverse derivative along I⁻ (this matters in §3, H2).
  In my TeX equation count the two displays are (2.5)–(2.6); the coordinator
  register's "(2.4)" appears to count the Remark 2.1 gauge-transform display.
  Harmless, but recorded.
* **Definition 2.6** (`localbvscat`, lines 346–361): local scattering =
  (i) the lifted (3+1) solution is future causally geodesically complete;
  (ii) `∫_{C_u∩{r≤r₀}} |∂_v²(rφ)| → 0` and
  `∫_{C_u∩{r≤r₀}} λ^{-1}|∂_v λ| → 0` as `u → ∞`.
* **Theorem 3.1** (`main1`, lines 507–525): hypothesis verbatim: "Let (φ,r,m)
  be a locally scattering solution to (SSESF) with initial data asymptotically
  flat of order ω′ ≥ 2 in C^k (k ≥ 1) towards I⁺ and I⁻." Conclusion: ten
  estimate families (3.11)–(3.20) of the printed text, all `|α| ≤ k`,
  `|β| ≤ k+1`, with constants per (K2).
* **Remark 3.2** (lines 526–528): existence of a *global* solution from the
  prescribed data is **not** explicitly checked by the paper ("we will not
  explicitly check that data of the type above gives rise to a global
  solution… This is, however true, and we will assume as much", citing
  Dafermos). Relevant here: the data set is on `C₁ ∪ underline C_R`; our
  construction prescribes no independent `underline C_R` half, so even per-n
  applicability presumes a sideways extension we have not built.
* **Theorem 3.3** (`main2`, lines 530–533): `k ≥ 11` gives a dispersive
  spacetime solution of size (C,γ₀,k), hence Luk–Oh future stability.
* **Luk–Oh criterion** (Kilgore's restatement, lines 415–460): Definition
  "Dispersive Spacetime Solution of Size (C,γ₀,N)" with items (D1)–(D8),
  `N ≥ 11`, including `|Γ^I h| ≤ C log(2+s)/(1+s)` and
  `|∂Γ^I h| ≤ C/((1+s)(1+|q|)^{γ₀})` for `|I| ≤ N+1` in a global coordinate
  system, plus non-symmetric curvature/coordinate conditions; then Theorem*
  "Large Data Stability, Luk & Oh". This is a **secondary** statement of
  Luk–Oh's hypotheses (primary 2108.13379v2 not fetched; abstract recorded).

Domain summary: Kilgore's estimates live on `Q = {u≥1, v≥u}` (proved) and
`O_R = {u≤1, v≥R}` (§5 sideways extension), collectively `I = {v≥|u|}` — the
future of a single finite cone. The LOY scattering solution lives on the full
quotient `Q = {(u,v): u∈(−∞,∞), v≥u}` with data at past null infinity. These
domains do not coincide even after translation; the translation
`ū = u−u_n+1`, `v̄ = v−u_n+1` sends fixed physical points to `ū, v̄ → ∞` with
`v̄−ū` fixed, i.e. deep interior decay-regime points, while pushing the profile
support to `v̄ ≈ −u_n`.

## 3. Point-by-point hypothesis audit of OUR compact smooth profile family

The family is `Φ_{ε,x} = ε f_x`, `f_x = Σ_k x_k F_k + β(x)G` of
`C11_FINITE_CONTROL.md` §3: smooth, compactly supported, pairwise-disjoint
supports, `||Φ_{ε,x}||₂ = εβ₀||G||₂`, `β(x) ≥ β_min > 0` on the parameter
ball, common C^k bounds for every k, and the (1.7) smallness with parameter
C₀ε independent of x and of the cone vertex. Cone `C_{u_n}`, data
`∂_v(rφ)(u_n, v) = Φ_{ε,x}(v)/2` (LOY Theorem 1.1 data condition).

| # | Kilgore hypothesis (v1 locus) | Our family | Verdict |
|---|---|---|---|
| H1 | Def. 2.5, I⁺ display on `C₁`: `sup v̄^{ω′+l}|∂_{v̄}^{l+1}(rφ)| ≤ A`, ω′≥2 | Per n: finite (`A_n ≤ εM₁(B−u_n+1)^{ω′+l}/2`, compact translated support). Uniform: NO — for `v_*` in the tail support of G, `A_n ≥ (v_*−u_n+1)^{ω′} εβ_min|G(v_*)|/2 → ∞` (CHECK2 confirms divergence ~n^{ω′} with the correct constant) | per-n OK; **uniform FAILS** |
| H2 | Def. 2.5, I⁻ display on `underline C_R` | Literal `∂_v` reading: for any v with `Φ(v) ≠ 0`, `∂_v(rφ)(u,v) → Φ(v)/2 ≠ 0` as `u→−∞` (LOY Thm 1.7 conclusion), so `(1+|u|)^{ω′+l}|∂_v(rφ)| → ∞`: **fails for every n**, i.e. the two-sided scattering normalization itself violates the display. Charitable `∂_u` reading: rate of `∂_u(rφ)(u,v)` as `u→−∞` at fixed v is not fixed by any source read; unverified. Additionally the construction prescribes no independent `underline C_R` data (Remark 3.2 gap) | **literal FAIL per-n**; charitable unverified |
| H3 | Def. 2.6 local scattering | (i) future causal geodesic completeness: available for the LOY scattering limits via LOY §6 per project records (`lawful-coord-loy-completeness-20261030`), external input, past half a one-sentence time reversal there; (ii) the two BV-type integrals along `C_u∩{r≤r₀}` as `u→∞`: never verified for our family in any project record or source read | **unverified** (plausible) |
| H4 | Thm 3.1 data regularity C^k, any k≥1; Thm 3.3 needs k≥11 | Smooth compact profiles: per-n OK for every k, with per-n constants | per-n OK; **no uniform statement available** |
| H5 | Constants (line 356) depend on A, A′, M_{−∞}, low-order behavior | Formal best case `C ≥ c·A_n` (the constant must dominate the data norm measured by main19-type estimates at the support) gives at fixed physical points `C(A_n)·v̄^{−(α+1)} ~ n^{ω′−α−1}`: diverges for α=0, flat for α=1, decays only for α≥2 — and already assumes an A-dependence the source never states (CHECK3) | **no uniform all-order estimate on fixed physical compact sets follows** |
| H6 | Axis treatment (§7): Remark 7.1 inputs `∂^{2l+1}_{r̂}φ|_Γ = 0` for `l ≤ ⌊k/2⌋−1` **from assumed smoothness** of the lift ("if the data is sufficiently smooth (C^∞ certainly suffices), then by persistence of regularity and Sobolev embedding the solution may be taken to be at least C^k"); Cor. 7.4 needs C^{2k} data, ω′≥2, on `Q` | Our chain derives finite-order parity from the field equations (`AXIS_C11_RECONSTRUCTION.md` (2)–(3), O7) and regains smooth parity through the regular constraint operators (`SMOOTHNESS_BOOTSTRAP.md` §§4–6). Kilgore's §7 runs the other direction (smoothness ⇒ parity), so it cannot be transplanted onto the C¹,¹ limit without first supplying exactly the smoothness we are trying to reach | **prior art, not a bridge** |

**Bridge-lemma status.** The lemma that Kilgore would have to supply, and
does not:

> **Lemma (localized uniform higher-order estimate; still open as a
> source-backed theorem).** For every compact quotient set K ⊂ {(u,v): u≤v}
> and every k ≥ 0, `sup_n sup_{K} |∂^α r_n| + |∂^α (r_nφ_n)| + |∂^α φ_n| ≤
> C(K,k)` for `|α| ≤ k`, with the constants independent of the parameter x in
> the compact profile ball and of the cone vertex u_n, together with the axis
> parity identities and equicontinuity of the top derivatives on K.

This is `KILGORE_SCOPE_REPAIR.md`'s "Exact remaining lemma", now sharpened by
this audit: (i) the I⁻ literal obstruction (H2) shows no version of this
lemma can be *derived from* Kilgore's Theorem 3.1 for our family; (ii) the
in-project conditional supply is `SMOOTHNESS_BOOTSTRAP.md` §1 (all-v-order
exterior Goursat induction uniform in u_n on finite windows, `u ≤ u_* < A`)
plus §§2–6 and `LOCAL_POLAR_PERSISTENCE.md` propagating smoothness through
finite physical regions. Scope differences that must be preserved: the
bootstrap does not bound global weighted norms, gives no decay in s or q, and
does not touch conformal null infinity — so it does not supply (D1)–(D8)
either. **No new bridge lemma is claimed here.**

## 4. Smooth common-development gate: source-faithful disposition

* **Gate chain and its regularity prices.** Ringström's common larger
  field-preserving GHD (`lawful-coord-ringstrom-common-scalar-20261029`,
  `lawful-coord-ringstrom-maximal-followup-20261030`) is stated for **smooth**
  initial data (PDF p.5 Definition 2.1); Galloway–Ling–Sbierski Theorem 1
  needs **at least C²**; LOY §6 completeness is an external input. Hence the
  gate can open for our limits only if the `SMOOTHNESS_BOOTSTRAP` +
  `LOCAL_POLAR_PERSISTENCE` chain (itself pending integrated review) first
  yields a smooth, complete slice. That chain is exactly where the
  conditional status of `SMOOTH_FINITE_CONTROL.md` §§1–2 sits; nothing in the
  present audit upgrades or weakens it.
* **Explicitly rejected inferences.** (a) Smooth profiles ⇒ smooth limit:
  profiles smooth gives per-n C^k solutions in the Definition 2.1 class only;
  limit smoothness needs uniform estimates (the lemma above). (b) C¹,¹ ⇒
  common development: none of the gate sources is stated at C¹,¹, and no
  source read supplies field-preserving common developments below smooth.
  (c) Smoothness ⇒ Luk–Oh stability: (D1)–(D8) at N≥11 is a global
  wave-coordinate decay package; smoothness is only item (D1)-adjacent
  infrastructure. Even full smoothness of our limit would leave (D2)–(D8)
  unverified — this is the precise gap on the Luk–Oh route named in
  `RECENT_LITERATURE_2026_10_29.md` item 3.
* **Disposition.** Gate stays **conditional** exactly as in
  `SMOOTH_FINITE_CONTROL.md` §4, with the added audit statement: the Luk–Oh
  route additionally requires proving the (D2)–(D8) package for the limit
  (or a localized replacement), which no source or project record currently
  does. Kilgore's footnote 1 independently marks two-sided Luk–Oh
  applicability as open in his framing.

## 5. Published LOY (Ann. PDE 4:3, 2018) — access record and v1 verbatim results

* Published metadata confirmed: Ann. PDE 4, Art. 3 (2018), DOI
  10.1007/s40818-017-0038-4; received 20 Jul 2016, accepted 25 Oct 2017,
  published online 17 Nov 2017.
* **Access blocked:** the Springer PDF returns HTTP 303 to the
  `idp.springer.com` authorize endpoint. No open-access copy found: Luk's
  Stanford page, Oh's KIAS and Berkeley pages, and Yang's PKU BICMR page all
  link only to arXiv:1605.03893. Per the brief, no corrections are invented;
  the v1-vs-published comparison of Proposition 3.18 and the §4 display
  **remains open** and is the top access-gated source question.
* v1 verbatim results obtained directly this session (TeX
  `SSESF-LargeBVScat.160512.tex`):
  * Proposition 3.18 = `prop:high-d` (line 1795) states both v-side
    ((est4dvdvdvrphi)/(est4dvdvdvr)) and u-side ((est4dududurphi)/
    (est4dududur)) third-normalized-derivative bounds; the u-side halves are
    proved under the literal environment `\begin{proof}[Sketch of proof of
    …]` (line 1984; "we only sketch the argument", line 1982). The
    axis-source-review caveat is confirmed verbatim. The **second-order**
    u-side pair has an active proof (ends ~line 1756); a competing sketch
    block at lines 1760–1784 is commented out and is not part of the paper.
  * §4 uniform display (lines 2044–2051) bounds
    `Σ_{k=0}^{2} sup |∂^{k+1}_v r^{(n)}| + |∂^{k+1}_u r^{(n)}| ≤ ε(A+ε)`;
    its k=0 slot claims `∂_v r, ∂_u r = O(ε)`, contradicting the gauge
    `∂_v r|_{C_{u_n}} = 1/2` (Theorem 1.1) and (main:geo)
    `∂_v r > 1/3`. The k=1,2 slots are consistent with `prop:high-d` and the
    Remark at lines 2081–2090. Confirmed: the coordinator's "k=0 typo"
    reading, and the bypass via Theorem 1.1 remains necessary and correct.
  * Theorem 1.7 (lines 452–464): hypotheses `Φ ∈ C^∞(ℝ)` with (1.7) and
    `sup|Φ″| < ∞`; conclusion line 462 prints "future and past casually
    geodesically complete" [sic; 'casually' for 'causally'] with scattering
    limits `lim_{u→−∞} 2∂_v(rφ)(u,v) = Φ(v)`, `lim ∂_v r = 1/2`. The
    convergence passage (lines 2052–2060) gives exactly the C¹/C²/C¹
    strengths our chain consumes; incoming recovery (main:pf:id) requires
    n→∞ first, then u→−∞, as used in `C11_FINITE_CONTROL.md` §6.

## 6. Computational checks (hard bounds respected)

Script logic reproduced here; wall time 0.13 s total (limit: 10 s each,
30 s total). Files `/private/tmp/opencode/hra_check1b.py`, `hra_checks.py`.

* **CHECK1 (family identity + smallness).** With the disjoint-support
  family and the project's `β(x) = √(β₀² − Σ x_k²||F_k||²/||G||²)`:
  `||Φ_{ε,x}||₂ = εβ₀||G||₂` to relative error 1.3e−16 (grid h=1e−4),
  `β(x) ≥ β_min > 0` on the tested ball point, and
  `∫|Φ| ≤ εM₀L^γ(v−u)^{1−γ}` verified numerically. Confirms the C¹,¹
  smallness inputs of `C11_FINITE_CONTROL.md` §3.
* **CHECK2 (weighted-norm divergence, H1).** `A_n ∈ [(v̄_*)^{ω′}εβ_min|G(v_*)|/2,
  1.1·ε(max|x_k|+β)(supp width −u_n)^{ω′}/2]` for `v̄_* = v_*−u_n+1`: finite
  per n, growing like n^{ω′} (ω′=2: 1.6 → 4.4e5 lower bound over
  n=10…10⁴). Confirms the KILGORE_SCOPE_REPAIR lower-bound calculation with
  the correct 1/2 normalization from Theorem 1.1's data condition.
* **CHECK3 (formal extraction failure, H5).** `n^{ω′−α−1}` at fixed physical
  points: +1 (α=0, diverges), 0 (α=1, flat), −1, −2 (α≥2, decays). Even the
  decaying cases rest on the unsourced assumption `C ≥ c·A_n`; the paper
  quantifies no A-dependence. No uniform estimate is extractable from the
  statements read.

An analytic conclusion above is nowhere replaced by these finite checks; they
only verify the project-side algebra entering the audit.

## 7. Strongest contrary evidence, and what would change the verdict

**Strongest counterexample to any "Kilgore upgrades our family" reading** —
and the sharpest form of the resolved tension: the very normalization that
makes our results interesting, LOY Theorem 1.7's
`lim_{u→−∞} 2∂_v(rφ)(u,v) = Φ(v)` with `Φ ≠ 0` on an open set, **provably
violates the literal I⁻ display of Kilgore's Definition 2.5 for every cone of
the sequence** (weight `(1+|u|)^{ω′+l}` times a nonzero transverse limit).
Combined with the diverging C₁-side norm (H1) and data-dependent constants
(H5), the obstruction is threefold and sits at the level of the theorem's own
statements. This is a **hypothesis obstruction only**: it does not show our
C¹,¹ limit fails to be C² or smooth, and does not contradict the in-project
conditional smoothness bootstrap.

Verdict-changing events: (i) access to the published Ann. PDE §3–§4 could
remove (or confirm) the u-side sketch and k=0 display residuals; (ii) a
published proof of localized uniform estimates for scattering families (or of
(D1)–(D8) for them) would close the bridge lemma; (iii) evidence that
Definition 2.5's second display is a typo for `∂_u` in the published version
would remove the per-n literal failure but not the uniformity failure (H1,
H5 still stand).

## 8. Obligations carried forward (point-by-point)

1. Obtain and read published Ann. PDE 4:3 §3–§4 (institutional access) —
   retires the sketch/typo residual; **owner: coordinator (access-gated)**.
2. Verify (D1)–(D8) wording against primary 2108.13379v2 §1–§3 before any
   Luk–Oh-route claim; **owner: a future worker task**.
3. If the smoothness bootstrap passes integrated review, the next mathematical
   task on the bridge is not Kilgore's theorem but a direct proof (or
   disproving example) for the localized uniform estimate of §3 above at the
   finite orders the axis reconstruction consumes; **owner: future worker**.
4. None of the above blocks `C11_FINITE_CONTROL`'s finite-order chain, which
   never uses Kilgore; its own integrated-review gate is unchanged.
