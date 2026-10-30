# Agent report: lawful-axis-source-review

29 October 2026. Worker submission for coordinator review — not accepted
completion.

## Task

Audit the exact LOY (arXiv:1605.03893v1) finite-order inputs behind the
coordinator's C¹,¹ axis-reconstruction note
(`research/lawful-completions/coordinator/AXIS_C11_RECONSTRUCTION.md`):
verify axis-inclusive, u₀-uniform availability of *all* mixed derivatives
needed for r through order 3 and φ through order 2; separate exact printed
assertions from prose assertions and from coordinator derivations; confirm the
§4 first-derivative typo and the valid λ-upper-bound workaround; check profile
hypotheses for smooth compact profiles and compact families; verdict
PASS/REPAIR/FAIL per source input and one strongest residual objection.

## Done and files

- `research/lawful-completions/axis-source-review/RESULT.md` — obligation-by-
  obligation verdict (O1-O15), consumed-source-order enumeration, verification
  record, strongest residual objection.
- `research/lawful-completions/axis-source-review/sources.jsonl` — 4 records
  per the knowledge-base schema (primary full-text record pinned to verbatim
  v1 LaTeX).
- `AGENT_REPORT.md` (this file) and the authorized root `AGENT_REPORT.md`.
- No other files touched; no coordination files, board, runner, seeds, or other
  lanes modified.

## Search capability check

- `scholar_search` (arxiv index): **worked** — first query located the exact
  lineage (returned Kilgore 2108.13377v1 abstract identifying
  Luk-Oh-Yang 1605.03893). Recorded in sources.jsonl at abstract depth.
- `exa.web_fetch_exa`: **worked** — fetched the arXiv v1 abstract page
  (authors: Jonathan Luk, Sung-Jin Oh, Shiwu Yang; v1 dated 12 May 2016).
- `serpapi_search`: available but not needed; `web-search-prime` not retried,
  per brief.
- Primary text obtained by direct fetch of `arxiv.org/e-print/1605.03893v1`
  (public source, no installs; gzip member name `SSESF-LargeBVScat.160512.tex`
  confirms v1 date).

## Source coverage and depth

Primary: LOY v1 LaTeX, **full-text** — every quoted locator read in source:
Theorem 1.1 + (1.8)/(1.9), (1.20), Remarks 1.2-1.3, Theorem 1.7 + extra
assumption, Def 2.1, axis identities (2.4)/(2.19), SSESF system, Ω²
definition, (2.8)-(2.13) wave/mass equations, (3.1)-(3.2), Prop 3.3 (3.9),
Prop 3.4 (3.11), Prop 3.5 (3.13), Prop 3.16 (3.26)-(3.29), Prop 3.18
(3.44)-(3.47), Lemma 3.19 (3.48)-(3.53), Cor 3.20, (3.55), §4 passage
(l. 2043-2059) incl. the typo line and the mixed-derivative prose sentence,
Remark 4.1. Secondary: regularity lane RESULT.md (full-text, project file);
coordinator note (full-text, project file); Kilgore (abstract only — explicitly
not imported).

## Verification commands and results

- `curl -sL arxiv.org/e-print/1605.03893v1 | gunzip` → exact v1 LaTeX; grep of
  all labels/locators cited (documented in RESULT.md §0).
- Exact-arithmetic algebra sanity check (pure Python, rationals, model
  r = aρ+bρ³ odd, φ = p+qρ² even; < 1 s, alarm 10 s): T1 r_uv ≡ (r_tt−r_ρρ)/4
  and r_uv(t,0)=0 — TRUE; T2 (ν+λ)(t,0)=0, (νφ_u+λφ_v)(t,0)=0 — TRUE;
  T4 Leibniz axis bookkeeping for parity (3) — TRUE; T5 D = F−A has vanishing
  ρ⁰, ρ¹ coefficients — TRUE; T6 ψ+χ axis structure — TRUE. T3 (−4νλ =
  r_ρ²−r_t²) verified by inspection as a difference-of-squares. An earlier
  checker draft produced spurious FALSE values from bugs in the checker itself
  (sign typos, dropped constant); corrected run is the record. Total compute
  well under the 30 s budget; no finite sampling stands in for any analytic
  step.

## Key findings

1. **No FAIL verdicts.** Every consumed input is printed or derivable from
   printed estimates with u₀-uniform constants; the coordinator's order list
   ("r through order 3, φ through order 2") is exactly the consumed set.
2. **Typo confirmed and quarantined:** §4 line l. 2049-2050 claims
   |∂_v rⁿ|+|∂_u rⁿ| ≲ ε(A+ε), contradicting (1.8) and the gauge; the k = 1, 2
   parts are fine. The coordinator never uses it; the λ ≤ 1/2 workaround
   (r_uv = 2mνλ/((1−μ)r²) ≤ 0 from printed SSESF + m ≥ 0 + gauge) is valid and
   is also the paper's own (3.1) argument.
3. **One REPAIR:** axis-inclusive uniform |φ_uv| ≤ C rests on a single §4 prose
   sentence. RESULT.md O7 supplies a three-step derivation from printed
   estimates ((3.9), (3.11), (2.8) + Gronwall from the axis), which also
   independently re-proves parity φ_ρ(t,0)=0 — the note's written parity
   derivation is correct but conditional on exactly this input.
4. **Mixed third derivatives r_uuv, r_uvv:** not displayed in LOY; the
   coordinator's differentiation of the printed r_uv equation is verified
   term-by-term; no circularity with the weighted mass bounds.
5. **Weighted mass chain verified:** |m| ≤ Cr³ is printed ((3.11)); |m_a|,
   |m_ab|, μ_a, μ_ab derivations check with the printed inputs; the O(r³) rate
   is load-bearing for the μ_ab quotient formula (O(r) or O(r²) would fail).
6. **Parity without a 4D atlas:** (2.4) is a quotient-level printed identity;
   r_ρρ and φ_ρ conclusions follow at quotient level; nothing assumes a smooth
   four-dimensional atlas.
7. **Profile hypotheses:** smooth compact profiles (and compact parameter
   families, estimate-uniformly) satisfy (1.20) + sup|Φ''| < ∞; LOY gives
   per-profile subsequences only (family limits and uniqueness are explicitly
   other lanes).
8. **Fidelity notes:** Prop 3.18's u-side halves are proof sketches (v-side
   full); §4's displayed sup domain overstates the proven domain for k ≥ 2
   terms (harmless on compact sets); Remark 4.1 is pure-directions only.

## Strongest attempted counterexample

Attacked the coordinator chain at its weakest link: tried to exhibit an input
consumed by the reconstruction that LOY neither prints nor cheaply yields —
candidates were (a) the §4 k=0 typo (real, but safely bypassed), (b) circularity
in the parity-φ derivation (real as written — it needs |φ_uv| ≤ C — but closed
by the O7 log-singularity/Gronwall lemma, which uses no parity input), (c) the
μ_ab quotient formula term 4m r_a r_b/r³ (fails for m = O(r) or O(r²), but O5's
printed O(r³) survives it), (d) φ_tt boundedness for the scalar lift (requires
|φ_uv| ≤ C — supplied by O7). Closest-to-fatal finding is (b)/(d): without the
supplied derivation, the scalar-field half of the C¹,¹ reconstruction rests on
an unnamed prose assertion; the metric half is unaffected. This is recorded as
the strongest residual objection in RESULT.md §4.

## Checks (what I verified vs. what I did not)

Verified: exact printed statements and domains for all cited locators;
u₀-uniformity statements (Remark 1.2, Prop 3.18); axis-inclusiveness of each
needed estimate (averaging-formula proofs, Prop 3.18's axis anchoring at
l. 2000-2009); the typo's inconsistency; all coordinator derivations flagged as
derivations (O2, O8, O9, O11, O12), term-by-term; the F = Ω² identity; profile
hypotheses. Not verified: the Cartesian lifting lemma (separate lane), the
smooth-MGHD question, scattering-map differentiability or uniqueness, whether
the u-side sketches of Prop 3.18 hide an error (recorded as residual), and no
Lean/numerical reproduction of LOY itself.

## Limitations

- Single primary source audited at full-text depth; the 2016 v1 preprint has no
  peer-reviewed version recorded in this lane, so "printed" means "v1-printed".
- The O7 lemma is my own derivation, not checked by a second reader; it is the
  only non-LOV mathematics this lane introduces.
- Prop 3.18 u-side sketch fidelity was noted, not reconstructed.
- I did not re-audit the coordinator's §5-§6 (geodesic uniqueness, a.e. Ricci)
  — out of lane.

## Proposed next tasks

1. Second-reader check of RESULT.md O7 (the supplied |φ_uv| ≤ C derivation) and
   O9 mixed-third-derivative derivation — these are now load-bearing.
2. Cartesiàn-lifting lane: integrate the quotient input list exactly as in
   RESULT.md §2 (no third-order φ inputs; pure third r inputs from (3.45)/(3.47)
   plus mixed from the r_uv differentiation).
3. Ask the coordinator note to (i) replace the §4 prose appeal by the O7
   derivation or a citation to it, (ii) mark the k = 0 typo explicitly when
   quoting the §4 bounds, (iii) add the sketch-fidelity caveat for Prop 3.18's
   u-side.
4. Scattering-map lane (separate): family-level diagonal subsequence and
   uniqueness remain open; do not import them here.

## Blockers

None. All brief items addressed; no completion claimed beyond the audit.
