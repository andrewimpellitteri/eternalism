# GLM adversarial review: scalar and conditional covariant theorems

Status: 2026-10-21, recovery run of task `glm-adversarial-scalar`. Worker:
headless OpenCode GLM (second-family review; evidence only through its
arguments, never a vote). Verdicts: **Theorem 1 SURVIVE** (narrow), **Theorem 2
SURVIVE conditional** (as stated), **novelty delta SHRINK** on one specific
point found in the primary source (Section 6 below). No counterexample to
either theorem was found.

## 0. Chronology of the two runs (recorded honestly)

- **Run 1 (independent, 2026-10-21 ~05:30).** Wrote and committed
  `INDEPENDENT_NOTES.md` (commit `c830a3f`, 05:34:40) — a full proof
  reconstruction and falsifier-attempt list written before any
  adversarial-review content was read; the file itself states what had been
  read up to that point. Then wrote and ran `check_bounded.py`
  (`check_bounded.out`, 05:42, "22/22 passed") but exited before any report.
  The preregistration claim in the task brief is **true**: the commit hash and
  timestamp are the evidence. The run-1 check script had real defects (below),
  none of which invalidated the pre-registered predictions it printed.
- **Run 2 (this recovery, informed).** Coordinator recovery note +
  `INTERIM_GLM_CHECK.md` (read read-only) identified my run-1 encoding errors.
  Everything in Sections 2–7 below that postdates the coordinator feedback is
  labeled informed; Section 1 summarizes what was already independent. I did
  not rewrite `INDEPENDENT_NOTES.md`; chronology is preserved in git.

## 1. Search capability check (required up front)

- `web-search-prime` (Z.ai MCP): **FAILED**, error 1310 "Weekly/Monthly Limit
  Exhausted … will reset at 2026-11-17", tested in both runs. Recorded rather
  than worked around.
- `serpapi_search`: **worked** (used for the landscape/thesis-locator query).
- `webfetch`: **worked** on arxiv.org HTML full texts (both primary papers
  below were read in full from `arxiv.org/html/...`).
- Not accessed: Zalel 2021 thesis (PDF-only; per recovery instructions I did
  not redownload theses or open binary PDFs as text). Its Ch. 6 §6.2.3
  (printed pp. 89–90) locator for the same unresolved calculation is taken
  from the prior source-priority review and is **not independently verified by
  me** (my thesis read depth: none).

## 2. Done and files

- `INDEPENDENT_NOTES.md` (committed run 1, unchanged): independent
  reconstruction of both theorems (steps T1–T9, C1–C10), 7 + 7 falsifier
  attempts, pre-registered checks N1–N7 and source checks S1–S5.
- `check_bounded.py` (corrected this run): exact-arithmetic check suite,
  stdlib only, enumerations at n ≤ 5, 26 checks, **exits nonzero on any
  failure**.
- `check_bounded.out`: final run, `26/26 checks passed`, exit 0.
- `AGENT_REPORT.md` (this file) + root copy.

Verification command (from the worktree root):

```
python3 research/adversarial-glm/scalar/check_bounded.py
echo $?   # 0
```

## 3. Run-1 defects found by the coordinator, and two more found by the new exit code

All four were **encoding errors in my check code**, not gaps in the theorems.
Each is fixed and now asserted against independent anchors.

1. **N4b exponent (coordinator-traced).** I computed the ordinal-block
   certificate W with the two-cap helper exponent `L+M(G)+h+1` (M = maxima).
   For principal 5-blocks M=1, so that sums exponent `L+h+2`. The historical
   certificate (`covariant-stopping/reduced_poscau_obstruction.py`, verified
   read-only this run: per-block exponent `E(G)=L+min(G)+10−R`, printed
   `r5 = 105/128 + 9/(8√2)`, `W = r5/√2`) uses the **minimum** count: the
   object is the ordinal block {⊥}+G+{⊤}, whose prepended bottom contributes
   `min(G)` covers and whose labels force `R = R(G)+11`, so the correct
   exponent is `L+min(G)+h+1`. Corrected check N4c reproduces
   `W = 9/16 + 105/(128√2)` exactly, with the `(L+min, 10−R)` histogram over
   the 40 blocks matching the builder's asserted bivariate histogram (N4b), and
   `W > 71/64` proven by integer arithmetic (`√2 > 4/3`), not floats (N4d).
   My run-1 quantity (principal-body two-cap partial sum `55/64 + 31√2/64`) is
   kept only as a clearly-labeled auxiliary cross-check N4f — it is a genuine
   partial sum of V₇ but is **not** the certificate.
2. **V₂ print bug (coordinator-traced).** Run 1 hard-coded the printed
   `V_2 = 1/2 + √2/4`; the only doubly-principal 2-order is the 2-chain, whose
   modulus is `|p| = 1/√2`. Corrected N2pre computes `V_2 = 0 + (1/2)√2` from
   the empty body; the printed table now starts at 0.707107.
3. **No nonzero exit.** Run 1 printed `FAILED:` but exited 0. Fixed:
   `sys.exit(1)` on any failure. This immediately caught items 4a–c below in
   this run, before any report was written.
4. **Latent shape-key defect (found by the new exit code, run 2).** My run-1
   `shape_key` canonicalized comparability **graphs** (min/max per mapped
   pair), which merges a poset with its order dual (V vs Λ on 3 labels);
   poset isomorphism must preserve relation direction. Fixing it exposed two
   further slips, each caught by the nonzero exit and fixed: (a) grouping by
   `min(key)` instead of the full canonical tuple; (b) applying the two-cap
   body helper (exponent `w+h+1`) to already-capped objects, double-counting
   the `u≺v` cover — `|A_p(C)|` on a capped object is `|p|^L |q|^h` directly.
   The corrected `N(H) = |natural relabellings|` bookkeeping is additionally
   validated by N2c: `linear extensions = |S|·|Aut|` for every poset n ≤ 5.

Lesson recorded: every failure signal in run 1 and run 2 was an encoding or
scope error in *my own check artifacts*; the corrected suite reproduces all
run-1 pre-registered predictions (N1, N2, N3, N5, N6, N7) plus the certificate
W. None of this constitutes a counterexample; conversely, passing checks are
consistency checks only, per RESULT.md's own warning.

## 4. Theorem 1 (labelled doubly-principal iff p ∈ [0,1]) — SURVIVE

Falsifier attempts (all from run-1 notes, re-audited this run):

- **Infinite-total-variation escape:** dead — finite total variation is a
  theorem for finite countably additive complex measures, not an extra
  assumption. The uniform-in-n bound is what makes divergence the
  contradiction.
- **Labels vs unlabelled multiplicities:** dead for Theorem 1 — the
  prescription is per labelled cylinder and same-size labelled cylinders are
  disjoint; the shape-grouping identity `Σ_[H] N(H)|A_p(H)| = V_n` used by the
  covariant theorem is exactly checked at n = 5 (N2b), including shape
  invariance of `A_p`.
- **Two-cap bijection gap:** none found; counts 1, 2, 7 doubly-principal
  orders at n = 3, 4, 5 equal arbitrary `(n−2)`-body counts (N1).
- **Normalized random-graph identity:** `Σ_G r^w s^h = F_k(s) =
  Π_{j=1}^k(1−s^j)` verified exactly at k ≤ 4 for two (r,s) pairs (N5), e.g.
  `F_4(1/4) = 722925/1048576`; the mask-level probability
  `r^L s^{C(n,2)−R}` decomposition also checked.
- **Product positivity:** `c_s = Π(1−s^j) > 0` on (0,1) is standard
  (`log(1−x) ≥ −2x` tail); numerically `c_s ≈ 0.0375` at `s = 2^{-1/2}`.
- **p = 0 and p = 1:** consistent — every doubly-principal C has L ≥ 1 so
  `A_0 ≡ 0` (zero measure works); at p = 1 only the chain cylinder is nonzero
  (Dirac at the chain). Structure checked (N7a/N7b).
- **Constructive thin-support escape:** dead — prescriptions fix `|μ([C])| > 0`
  on a disjoint divergent family regardless of support.

Endpoint and assumption audit: the statement quantifies over finite-valued
countably additive complex measures on `R̃_p` with prescribed cylinder values;
both directions used only elementary pieces (triangle inequality for
`t = a+b > 1`; Bollobás–Brightwell random graph order; FHT extension for
p ∈ [0,1]). The V-bound `V_n ≥ |p| t^{n−2} c_s` is analytic; the finite
certificates (`V_5 = 3/4 + 3√2/16`, `V_6 = 31/32 + 55√2/64`, W > 71/64) are
consistency checks, exactly as RESULT.md says, and my corrected script
reproduces all of them.

**Verdict: SURVIVE.** No falsifier succeeded; reconstruction is complete from
stated premises; primary-source scope matches (Section 6).

## 5. Theorem 2 (conditional covariant iff 0 < p ≤ 1 under the all-principal rule (T)) — SURVIVE, conditional

- **Laminar-cover argument:** posts of a history have pairwise distinct past
  sizes (N6a); `D_{H⊕{x}} ⊆ D_H` witnessed structurally for all principal
  H, |H| ≤ 4 (N6b); the κ = 0 case is killed by the laminar cover of `P_∞`
  plus continuity from below — the one place a complex measure needs
  laminarity rather than a null-cover fallacy, which the draft states
  correctly.
- **All-principal vs doubly-principal rule:** the draft's infinite-block
  Dirac history `⊕_j (A_2 ⊕ {z_j})` does defeat the doubly-principal
  weakening for every p (my C8 check adds the missing lemma the draft leaves
  implicit: an orbit indicator is finitely additive *on a covariant algebra*
  because covariant events are unions of isomorphism orbits). This KILLs only
  the weakened variant, exactly as the draft itself says.
- **p = 0 exclusion:** `A_0(H) = 0` for all principal |H| ≥ 2, and that
  subfamily alone covers `P_∞` (every infinite-post history has a later
  post). Checked structurally (N7b).
- **Sufficiency 0 < p ≤ 1:** percolation restriction with
  `κ = c(1−p)`, `c(q) = Π_{j≥1}(1−q^j)` — all cited classical facts verified
  at full-text depth against Bombelli–Seggev–Watson v2 (Section 6).
- **Local-renewal refinement (boundary note, informed):** the prior review's
  correction is adopted — under the rank-only + local-renewal axioms the
  forced constant chain starts at rank two; κ₁ is not pinned by those axioms
  alone (my C9 verified the κ_{n+1} = κ_n step via the chain but did not
  examine the rank-1 endpoint). This requires an endpoint qualification in
  the refinement sections of COVARIANT_RESULT.md; it does not touch the
  conditional theorem itself, whose assumption (T) pins all ranks.

**Verdict: SURVIVE conditional** — the conditional character is intrinsic and
honestly stated (covariance alone supplies none of the dynamics; the L²
construction below shows the finite-complex-measure hypothesis is
load-bearing).

## 6. Primary-source correspondence, novelty boundary (SHRINK of the delta)

Read depths: **full text** = complete HTML read this run; **discovery** =
metadata/abstract or prior reviewer's locator only.

- **Dowker–Zalel arXiv:2212.01149v2 — full text** (Sec. III.4, IV, V, VI).
  Everything RESULT.md claims about it checks out verbatim: Eq. (29) defines
  ℛ_p as the covariant events containing all or none of `P_∞^c`; "doubly
  principal" is defined as in the draft; Theorem 14 gives
  `ℛ_p = ℛ̃_p ∩ ℛ`; and their extension criteria for Complex Transitive
  Percolation on doubly-reduced poscau are stated as **inconclusive**
  (valency-one nodes force `Σζ^min = 0`; the amended criterion (31) has only
  n ≤ 4 numerical support for `ζ̄^min = t−1`, with the `S^{v=1}` second term
  unresolved). No prior proof of nonextension exists in the paper: their
  conditional "if this is borne out…" is explicitly unproven. So no
  prior-result defeater; the draft answers a question the source leaves open.
- **Novelty SHRINK (the one substantive finding).** DZ Sec V's closing
  remark states that `S^{v=1}` "is the sum over absolute values of amplitudes
  of reaching a doubly principal causet" and that "in future it could be
  computed using techniques similar to those used to obtain the probability
  of a post [17]" — where [17] is Bombelli–Seggev–Watson. That is exactly
  the quantity the draft's proof computes (V_n), by exactly that type of
  technique (random graph orders). RESULT.md's novelty section cites Eqs.
  (29)–(31) and claims as delta "a direct lower bound for the
  doubly-principal cylinder variation … the elementary normalization
  argument"; it does not mention this sentence. Honest rescaling: the
  *reduction of the open question to that computation* is already printed in
  the primary source; the draft's contribution is executing it (the
  normalization to a random graph order and the endpoint-connectivity
  product, giving `V_n ≥ |p| t^{n−2} c_s`), plus the iff classification and
  the covariant conditional theorem. This corroborates and sharpens the prior
  source-priority review's "explicit solution of a named open case"
  framing; I found the verbatim anchor myself.
- **Bombelli–Seggev–Watson arXiv:0809.2258v2 — full text.** Theorem 2.1
  `Pr(k is a post) = λ_{k−1}(q)λ_∞(q) ≳ κ²(q)`; Eq. (2) sequential exposure
  `λ_{k−1}(q) = (1−q)(1−q²)⋯(1−q^{k−1})`; Euler function `κ(q) > 0` on
  (0,1); and the explicit statement that a.s. infinitely many posts "was
  first proved by Alon et al." — precisely as COVARIANT_RESULT.md attributes.
- **Zalel 2021 thesis Ch. 6 — not accessed** (PDF-only). The
  §6.2.3 pp. 89–90 locator for the same unresolved calculation comes from the
  prior review; recorded as unverified by me.
- **Surya–Zalel arXiv:2003.11311 and Dowker–Johnston–Surya 1007.2725 —
  discovery depth only** this run (identified via DZ's reference list as the
  cited extension-criterion and foundations sources); not re-verified
  full-text.

## 7. Strongest contrary evidence found

- **Vector-valued escape (informed, from the prior review; re-derived
  independently here for the report):** for `|p|²+|1−p|² = 1` (e.g.
  p = (1+i)/2), `μ(E) = 1_E` in `L²(P_{|p|²})` is a countably additive
  Hilbert-valued measure with `‖μ(C)‖ = |A_p(C)|` on every cylinder, finite
  semivariation 1, **infinite total variation**. This shows the
  finite-complex-measure hypothesis in both theorems is load-bearing and
  cannot be quietly upgraded to "any measure". It does not contradict either
  theorem as stated (both quantify over ℂ-valued finite measures), but any
  presentation must carry the qualifier.
- **Encoding fragility (this task's own record):** four distinct encoding
  slips across two runs (Sections 3.1–3.4), all caught only after the exit
  code fix. Any future numeric claim in this area should require a
  fail-nonzero harness and independent anchors (the builder's bivariate
  histogram served here).

## 8. Limitations

- Finite checks bounded at n = 5 (task cap); all-level statements rest on the
  analytic arguments, not enumeration.
- Thesis Ch. 6 not read; its open-case statement is unverified by me.
- 1007.2725 / 2003.11311 at discovery depth only.
- web-search-prime quota-exhausted; the bounded 2023–2026 forward-citation
  sweep (S5) was not redone this run beyond the serpapi landscape query —
  novelty remains unverified globally (as RESULT.md itself states).
- This recovery run was informed by the coordinator feedback and (after the
  fixes) by the prior adversarial-review outputs; only run 1's committed notes
  are independent. The comparison is labeled, not hidden.

## 9. Proposed next tasks

1. Add the DZ `S^{v=1}` sentence and the thesis §6.2.3 locator to
   RESULT.md's novelty paragraph (small edit, big honesty gain), keeping the
   delta claim as "explicit execution + normalization argument + iff
   classification".
2. Verify Zalel thesis Ch. 6 §6.2.3 pp. 89–90 from the PDF (task with PDF
   allowance) to close the thesis priority gap.
3. Endpoint qualification edit in COVARIANT_RESULT.md's rank-only/local
   renewal sections (κ₁ unconstrained; common factor from rank two).
4. Optional: exact symbolic check of the amended DZ criterion (31) second
   term at n ≤ 5 to see whether their route also diverges — independent
   confirmation of the draft's claim that their ζ-route remains
   conditional.

## 10. Verdict summary

| Item | Verdict |
|---|---|
| Theorem 1 (labelled, iff p ∈ [0,1]) | **SURVIVE** (no counterexample; reconstruction complete; scope matches DZ) |
| Theorem 2 (covariant, conditional on (T), iff 0 < p ≤ 1) | **SURVIVE conditional** (weakened doubly-principal variant KILLed by the Dirac history, as the draft itself states) |
| Novelty of the delta | **SHRINK**: DZ v2 Sec. V explicitly names the doubly-principal amplitude sum and post-technique computation as the open remainder; the draft executes it (normalization + endpoint product) but does not pose the question |
| κ₁ / local-renewal refinement | Boundary correction adopted from prior review (informed) |
| Finite checks | 26/26 pass, fail-nonzero harness, exact arithmetic, n ≤ 5 |

This submission is for independent coordinator review; it is not an accepted
completion and makes no priority or physical claim.
