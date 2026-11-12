# AGENT_REPORT: lawful-scalar-common-extension

29 October 2026. Worker submission for independent review. Task: supply the
precise field-preserving common-GHD-extension theorem for smooth Einstein
massless real scalar data (`Ric(g) = 2 dphi (x) dphi`, `wave_g phi = 0`) and
either prove the smooth scalar corollary of the repaired common-development
argument with exact source dependencies, or isolate what is missing.

## Done / files

- `research/lawful-completions/scalar-common-extension/RESULT.md` — the
  deliverable: setting and convention conversion, Theorem A (field-preserving
  common extension, both directions, with exact locators and erratum history),
  five task audits (hypersurface generality; restricted developments with one
  isolated gap; field- vs stress-energy preservation; scalar shifts/signs;
  first-jet/path/marks compatibility), Corollary C (the smooth scalar
  common-duration corollary, assembled with per-step dependencies), the
  three-tier completeness structure, distinctness from Luk–Oh–Yang, status
  ledger, verification record.
- `research/lawful-completions/scalar-common-extension/sources.jsonl` — 8
  source records in the knowledge/README schema with exact versions, locators,
  read depths, and limits.
- `AGENT_REPORT.md` (this file, repo root).

## Headline findings

1. **The needed coupled theorem exists and is published.** Ringström, *The
   Cauchy Problem in General Relativity* (EMS 2009), Theorem 14.3 (p. 158):
   any two smooth GHDs of the same Einstein–nonlinear-scalar data (general
   smooth connected initial manifold; `V ≡ 0` = the task's massless system
   after `phi_R = sqrt(2) phi_T`) admit a common GHD with time-orientation
   preserving diffeomorphisms pulling back **both the metric and the scalar
   field**. The containing-both form (the coupled analogue of Sbierski's
   vacuum Theorem 2.7, needed by the repaired argument) is proved in the
   author's correction note (`people.kth.se/~hansr/mghd.pdf`: Definition 6.1,
   Lemma 6.4, Definition 6.7, Lemma 6.10, Lemma 10.1), posted because the
   book's Chapter 16 MGHD proof contained a documented error (errata:
   p. 178, l. −14; the errata file shows **no items on pp. 147–163**, i.e.
   Theorems 14.2/14.3 are untouched). This closes the gate recorded in
   REVIEW_COMMON_EXTENSION.md ("accept [scalar/matter readings] only after a
   field-preserving common-development result ... is cited").
2. **One precise gap isolated in the repaired argument's geometry.** The
   domain step on the matched side needs `K_2 = h(Σ_1)` **closed (edgeless)
   in M_2** for the standard domain theorem (Minguzzi Def 3.35, Thm 3.45,
   Thm 3.50: `D(K)` open GH with `K` Cauchy holds for *partial Cauchy
   hypersurfaces*; closedness is the operative hypothesis). Neither
   COMMON_EXTENSION_REPAIR.md nor its review establishes this. Partial
   positive result proved here (Lemma D): `h(Σ_1)` cannot accumulate on
   `J⁺(b_2)`, via compactness of `J⁻(x) ∩ Σ_1` in GH spacetimes; the
   horizon part `∂I⁻(I⁺(b_2)) ∖ J⁺(b_2)` remains open. Corollary C is stated
   conditional on this gate. The gate is matter-independent and inherited
   from the vacuum repair.
3. **Stress-energy preservation is insufficient; field preservation is
   forced.** `T` on a slice does not determine the extrinsic curvature, so a
   merely T-preserving realm isometry cannot transport the Cauchy data and
   Theorem A cannot be applied; the realm hypothesis must be
   `h^* φ_2 = φ_1`. Conversely, with field-value data, pointwise field
   preservation on developments is then a consequence (coupled theorem, or
   BGP Corollary 3.2.4 on the common metric development). Shifts `φ ↦ φ + c`
   and sign flips are exact symmetries of the equations but are different
   data sets; no cross-identification is claimed.

## Search capability check (required)

- `scholar_search` (OpenAlex): **worked** (first test query returned
  Friedrich–Rendall 1999, Sbierski 2015, Rendall LRR, Dafermos 2003,
  Choquet-Bruhat SDG 2015).
- `exa` web_search/web_fetch: **worked** throughout (EMS Press pages and free
  chapter file, KTH author PDFs, ar5iv full texts, Springer PDF).
- Direct `webfetch`: **worked** (errata.html link extraction).
- `serpapi_search`: **quota exhausted** ("Your account has run out of
  searches") — recorded, not retried after exhaustion.
- `web-search-prime`: **not called**, per brief (quota exhausted until
  2026-11-17).

## Source coverage

Primary: Ringström 2009 book (statement chain via author-verbatim correction
note, errata, free Introduction chapter, detailed contents — interior proof
pages not lawfully accessed); Ringström correction note + errata (author PDFs,
read full-text selective); Ringström Acta Phys. Polon. 2013 survey (full-text,
confirms the book is the coupled Einstein–scalar setting); Sbierski
arXiv:1309.7591 (ar5iv, full-text selective; re-verified Def 2.1, Thm 2.7,
Lemma 3.1 verbatim); Bär–Ginoux–Pfäffle arXiv:0806.1036 (Corollary 3.2.4
verified verbatim this session); Minguzzi LRR 2019 (Def 2.130, Def 3.35,
Thm 3.45 as invoked, Thm 3.50). Distinctness-only at discovery depth:
Luk–Oh–Yang arXiv:1605.03893 (full-text audit lives in the coordinator lane's
record).

## Verification commands and results

All extraction was done by fetching public pages and searching within the
returned text (exa fetch + in-code locator search; webfetch for HTML). Key
verbatim extractions that back the submission:

- Sbierski: "Theorem 2.7 (Global uniqueness)... there exists a GHD M̃ that is
  an extension of M and M′"; "Lemma 3.1 ... psi_1 = psi_2" (proof via geodesic
  uniqueness read); "Definition 2.1 ... connected d-dimensional Riemannian
  manifold" (no completeness).
- Ringström note: system "(2) Ric − dϕ⊗dϕ − (2/(n−1))V(ϕ)g = 0, (3) wave_g ϕ
  − V₀(ϕ) = 0"; "Theorem 2.4 ... ψ∗_j g_j = g and ψ∗_j ϕ_j = ϕ"; "Lemma 6.10
  ... If M̃ is Hausdorff, then (M̃, g̃, ϕ̃) is a globally hyperbolic
  development ... such that (M,g,ϕ) and (M̂,ĝ,ϕ̂) can be isometrically
  embedded into it"; "Lemma 10.1 ... Then M̃ is Hausdorff"; Corollary 10.2
  proof line "Due to Lemma 10.1, M̃ is then Hausdorff, so that (M̃, g̃, ϕ̃)
  is a globally hyperbolic development of the initial data due to Lemma
  6.10."
- Errata: "...is incorrect; there are certainly totally ordered subsets of
  C(N, N0) which do not have upper bounds" (p. 178 item); no items on
  pp. 147–163.
- EMS Introduction chapter: "we shall restrict our attention to the
  non-linear scalar field case."
- Survey: "In [19] there is a complete proof ... in the Einstein-non-linear
  scalar field setting" with references resolving [19]/[20].
- BGP: "Corollary 3.2.4 ... If u solves Pu=0 on M, u=0 along S, ∇_n u = 0
  along S, then u=0 on M."
- Minguzzi: "Definition 3.35 An acausal edgeless (and hence closed) set is a
  partial Cauchy hypersurface"; Theorem 3.50 with the partial-Cauchy
  conclusion "D(S) = D(S′)" / S Cauchy.
- JSONL schema check: see command below.

Checks run:

```sh
python3 -c "import json;[json.loads(l) for l in open('research/lawful-completions/scalar-common-extension/sources.jsonl')]"  # passes (8 records)
git status  # only owned paths + root AGENT_REPORT.md staged for commit
```

## Strongest contrary evidence

- The erratum history itself: the book's MGHD proof was wrong once
  (documented), which is exactly why the submission's Theorem A(b) rests on
  the correction note's chain rather than the book's Chapter 16; and the
  note is an unrefereed author web document.
- The domain gate: Minguzzi's own Remark 3.51 (disk example) demonstrates the
  domain theorem's hypothesis is not vacuous; a smooth acausal hypersurface
  without intrinsic boundary need not be closed (open disk, punctured slice),
  so the repaired argument's phrase "acausal topological hypersurface without
  boundary" does not by itself license the D(K) theorem on side 2.
- The interior-proof access gate for Theorems 14.2/14.3: the statements are
  author-verbatim but the book's proofs were not independently audited; if
  the review rejects the statement chain, the fallback is auditing the
  correction note's self-contained Sections 6+10 (which suffice for both
  directions without the book's interior).

## Limitations

- Corollary C is conditional on (i) the screening containment
  (SCREENING.md Theorem 3(a), whose independent adversarial check was still
  outstanding per the repair document) and (ii) the isolated domain gate (G).
  Neither is closed here.
- No novelty claim is made for Theorem A (published) or for the assembly;
  the new elements of this submission are the coupled sourcing, the
  preservation/shifts audits, Lemma D, and the precise gap statement.
- Book interior pages and the original Penrose 1972 / Geroch 1970 domain
  locators were not fetched; recorded as gates, not assumed read.
- No installs, no large runs, no child agents, no workboard/runner/shared
  seed/manuscript changes; owned paths only.

## Proposed next tasks

1. Close or refute the domain gate: prove `h(Σ₁)` closed in `M₂` (extend
   Lemma D past the horizon part, or prove a rigidity property of realm
   isometries), or build a counterexample pair satisfying the repaired
   hypotheses with non-closed `h(Σ₁)`, or source a domain theorem for acausal
   embedded hypersurfaces without the edgelessness hypothesis.
2. Dezornified coupled common-extension (audit Ringström's Lemma 10.1
   independently; Sbierski's method is vacuum-only).
3. If (1) closes, re-run the marked-readout audit end-to-end for the scalar
   case from Corollary C.
4. Fetch primary locators Penrose 1972 Prop. 5.14 and Geroch 1970 Prop. 6 for
   the domain theorem chain.
