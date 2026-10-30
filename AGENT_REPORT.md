# AGENT_REPORT.md — lawful-finite-control-review

Task: audit compactness continuity and finite scalar interpolation at fixed
incoming mass; red-team the compactness-plus-characteristic-uniqueness
replacement for the rejected GLM Lipschitz argument; pin LOY v1 locators;
identify the exact strongest 4D regularity category and the remaining gap.
Worktree: `agent/lawful-finite-control-review`. Status: **submission for
independent review; not accepted completion.**

## Done / files

- Read AGENTS.md, README.md, knowledge/README.md, knowledge/NOVELTY.md, and
  the task brief; then `coordinator/FINITE_CONTROL.md`,
  `COMPACTNESS_CONTINUITY_REPAIR.md`, `CUBIC_TRACE.md`, `INCOMING_MASS.md`,
  `AXIS_C11_RECONSTRUCTION.md`, `C11_FINITE_CONTROL.md`, `DEGREE_ROUTE.md`,
  `SMOOTH_FINITE_CONTROL.md`.
- Fetched and read the primary source directly: Luk–Oh–Yang arXiv:1605.03893v1
  e-print TeX (`SSESF-LargeBVScat.160512.tex`, 12 May 2016) plus the v1 HTML
  rendering for numbering; Galloway–Ling–Sbierski arXiv:1704.00353v4 (abstract
  + Theorem 1 statement); Crossref metadata for the published Ann. PDE version.
- Point-by-point audit of all thirteen obligations (uniqueness class,
  profile-uniform compactness constants, axis inclusion, order of limits, C²
  family hypotheses, exact norm-compensating tail and actual incoming mass,
  uniform cubic remainder, per-cone continuity, degree boundary, parameter
  subsequence, flat wedge, C¹,¹ geodesic readings, source-fidelity items):
  `research/lawful-completions/finite-control-review/RESULT.md`.
- Arithmetic sanity checks: `research/lawful-completions/finite-control-review/checks.py`
  — all pass, 1.5 s total (limits: ≤15 s per check, ≤30 s total honored).
- Source register: `research/lawful-completions/finite-control-review/sources.jsonl`
  (knowledge/README schema; honest read depths).

Files changed (all owned paths + authorized root report):
- `research/lawful-completions/finite-control-review/RESULT.md` (new)
- `research/lawful-completions/finite-control-review/checks.py` (new)
- `research/lawful-completions/finite-control-review/sources.jsonl` (new)
- `AGENT_REPORT.md` (root, authorized)

No board, runner, shared seed, manuscript, or other lane files touched. No
installs, no child agents, no pushes/merges. No worktree edits outside owns.

## Search capability check

- `scholar_search` (MCP): **worked** — arXiv API located 1605.03893v1 with the
  exact v1 date and abstract; OpenAlex and Crossref responded. One initial
  arXiv-API 400 on an over-complex quoted query; a simpler query succeeded.
- `web-search-prime`: **not used** (quota exhausted per brief; not retried).
- Direct primary fetch (curl): **worked** for arXiv e-print, arXiv HTML, and
  Crossref API. The published Springer full text was not accessed (paywall).

## Source coverage

- arXiv:1605.03893v1 — full-text at selected loci (Theorem 1.1 + Remarks,
  Definition 2.1, (2.4)–(2.16), Lemma 3.1, Props 3.3/3.4/3.8, Prop 3.18,
  §4, §6 closing); numbering cross-checked against the v1 HTML rendering.
- Ann. PDE 4(1), article 3 (June 2018), DOI 10.1007/s40818-017-0038-4 —
  metadata only (Crossref); body unread (paywall).
- arXiv:1704.00353v4 (Galloway–Ling–Sbierski) — abstract and Theorem 1
  statement verbatim: "A smooth (at least C²) time-oriented Lorentzian
  manifold that is timelike geodesically complete and globally hyperbolic is
  C⁰-inextendible."
All records with locators, assumptions, and limits are in the lane
`sources.jsonl`.

## Verification commands and results

- `curl -sL https://arxiv.org/e-print/1605.03893v1` → v1 TeX; every consumed
  locator verified in the TeX and re-verified in the rendered HTML.
- Key verbatim confirmations: Remark 1.2 (u₀-independent constants); Prop 3.18
  (constants independent of u₀, v₀, A); §4 compactness topology and the two
  remainder displays; §4 order of limits "n→∞ first and then u→−∞"; (3.16)
  m ≲ ε²min{r³, r^{1−γ}}; (3.18) exact mass flux identity (matches
  INCOMING_MASS's integrand after the re-derived algebra X = λ⁻¹p_v − φ = rφ_v/λ);
  the §4 typo (r-line k=0 term impossible since λ ≈ 1/2); u-side Prop 3.18
  halves "we only sketch the argument"; uniqueness "We omit the proof, which is
  a routine iteration argument"; §6 past completeness one sentence.
- Independently re-derived (beyond the source): ∂_u(φ+rψ) = −Krψ and w_u + Kw
  = rB under LOY's convention r_u = ν (HTML (2.6)/(2.8) confirm ν = ∂_u r < 0);
  the backward ODE for w = rc giving the axis-inclusive |φ_uv| ≤ C; the
  weighted mass bounds |m_ab| ≤ Cr, |μ_ab| ≤ C; clock-inverse factor 3/2;
  degree-boundary positivity; flat-wedge Gronwall.
- `python3 checks.py` (in lane dir): 7/7 pass in 1.5 s — exact norm
  compensation (5·10⁻¹⁶ rel dev), δ_kj/tail normalization, (1.7) reduction
  min(v−u,L) ≤ L^{δc}(v−u)^{1−δc}, clock-inverse bound, worst-case homotopy
  positivity, Gronwall zero-seed case (+ nonzero-seed contrast). Labeled as
  arithmetic sanity checks; no analytic claim rests on them.

## Verdict summary

The compactness + characteristic-uniqueness replacement is sound logic and
correctly avoids the rejected Lipschitz route (including discarding the invalid
W ≤ δ + aW ⟹ W ≤ δe^{aT} step). Every consumed source locator resolves, and
the profile-family uniformity extension is justified because all consumed
constants depend on the member only through (δc, ε, A). The strongest category
owned by the chain alone is **C¹,¹** (metric + scalar, a.e./distributional
Einstein–scalar, unique local geodesics, geodesic center with the exact
proper-time clock, section-7 Cauchy slices) — with smooth MGHD, ADM equality,
null-infinity uniqueness, continuous scattering selection, bare-metric
nonisometry, pointwise axis curvature, and C⁰-inextendibility all outside it
(GLS's "at least C²" hypothesis verbatim excludes the bare C¹,¹ model).

**Hardest missing step:** the characteristic uniqueness proof is not in the
pinned source (asserted "easy to show" / "routine iteration argument", omitted).
It is the single load-bearing input of the continuity Proposition; everything
else is printed or elementary. Second: Prop 3.18's sketched u-side halves.
Third: the varying-profile extension, sound but not printed text. Full analysis
and falsifiers: `RESULT.md` §4–5.

## Strongest contrary evidence found

- Uniqueness proof omission and sketched u-side proofs in v1 (quoted above) —
  the chain's two soft external joints.
- The §4 r-line display typo and the one-line mixed-derivative assertion — the
  printed text alone does not prove the mixed third-derivative bounds used by
  the compactness topology; the project's own derivations fill this (checked,
  but they are not source-printed).
- The exact quarter-norm mass is a total over the whole profile including the
  post-readout compensating tail; it does not fix mass at reading times (the
  notes state this; confirmed by the construction).
- Galloway–Ling–Sbierski's C² hypothesis verbatim — blocks any temptation to
  claim C⁰-inextendibility or an MGHD universal property at C¹,¹.
No contrary evidence was found against the degree logic, the order of limits,
the flat wedge, or the incoming-mass identification.

## Limitations

- Published Ann. PDE version unread (paywall); all checks are against v1.
- Omitted/sketched source proofs were not reconstructed; treated as external
  inputs with recorded risk (as C11_FINITE_CONTROL §2 itself does).
- Smoothness-bootstrap lane, NONISOMETRY_LEMMA, and philosophical-bridge claims
  reported, not audited.
- No novelty sweep performed; the novelty/nearest-prior gate remains open.
- Numeric checks are sanity checks within the stated ≤15 s/≤30 s budget.

## Proposed next tasks

1. **Version diff (top):** obtain the Ann. PDE 4(1):3 (2018) full text and diff
   §2.1 uniqueness, Prop 3.18 u-side proofs, and §4 against v1. If the
   uniqueness argument is printed there, the chain's hardest external joint
   closes.
2. **Write the uniqueness proof:** reconstruct the omitted characteristic
   uniqueness argument at Definition 2.1's k=1 class (Picard iteration under
   the printed geometric bounds), as a project-owned lemma with full detail.
3. **Constant audit:** locus-by-locus sweep of §3's bootstrap confirming no
   consumed constant depends on data outside (δc, ε, A).
4. **Nearest-prior comparison** for the interpolation/control statement
   (scattering-theoretic controllability corollaries), feeding the open novelty
   gate.
5. If 1–3 close: upgrade the C¹,¹ theorem's dependency list to
   "printed-source-complete" and re-run an adversarial pass on O7/mass with the
   published text.
