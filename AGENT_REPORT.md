# Agent report: lawful-axis-source-review

29 October 2026. GLM headless worker (`agent/lawful-axis-source-review`
worktree); independent adversarial SOURCE-to-input audit of the coordinator's
C¹,¹ axis-reconstruction note. Worker submission for review — not accepted
completion.

## Task

Audit the exact Luk-Oh-Yang (arXiv:1605.03893v1) finite-order inputs behind
`research/lawful-completions/coordinator/AXIS_C11_RECONSTRUCTION.md`: all mixed
derivatives needed for r through order 3 and φ through order 2, uniformly in
the cone vertex u₀ up to the axis; separate printed assertions from prose
assertions and coordinator derivations; confirm the §4 first-derivative typo
and the valid λ-upper-bound workaround; check profile hypotheses; deliver
PASS/REPAIR/FAIL per source input and one strongest residual objection.

## Deliverable

`research/lawful-completions/axis-source-review/` — `RESULT.md` (verdicts
O1-O15, consumed-order enumeration, verification record, residual objection),
`sources.jsonl` (4 records, schema-compliant), and lane `AGENT_REPORT.md`.

## Evidence and checks

- Primary source pinned to the verbatim arXiv v1 LaTeX
  (`SSESF-LargeBVScat.160512.tex`, 12 May 2016, only version); every cited
  locator (Thm 1.1 + (1.8)/(1.9), (1.20), Thm 1.7, Def 2.1, (2.4)/(2.19),
  SSESF system, (2.8)-(2.13), (3.1)-(3.2), (3.9), (3.11), (3.26)-(3.29),
  Prop 3.18 (3.44)-(3.47), Lemma 3.19, Cor 3.20, (3.55), §4 l. 2043-2059,
  Remark 4.1) read in source at full-text depth.
- Search capability check recorded: `scholar_search` (arxiv) worked;
  `exa.web_fetch_exa` worked on the v1 abstract page; `serpapi_search`
  available but unneeded; `web-search-prime` not retried per brief.
- Exact-arithmetic algebra check (pure Python, < 1 s, alarm 10 s): T1
  r_uv ≡ (r_tt − r_ρρ)/4; T2 (ν+λ)(t,0)=0 and (νφ_u+λφ_v)(t,0)=0; T4 Leibniz
  axis bookkeeping for parity (3); T5 D = F−A vanishes through O(ρ); T6 ψ+χ
  axis structure — all TRUE; T3 −4νλ = r_ρ²−r_t² verified by inspection. An
  earlier checker draft's spurious FALSE values were checker bugs (sign typos,
  dropped constant), documented honestly in the lane report.
- Verified the coordinator's derivations term-by-term: λ ≤ 1/2 from
  r_uv ≤ 0 (printed SSESF + m ≥ 0 + gauge; also the paper's own (3.1)); pure
  third derivatives of r from (3.45)/(3.47) + (1.9); mixed r_uuv, r_uvv from
  one differentiation of the printed r_uv equation using weighted mass bounds;
  μ_ab ≤ C requires the printed m = O(r³) ((3.11)) — O(r)/O(r²) would fail.

## Findings

- No FAIL verdicts. The coordinator's input list is order-accurate; the
  reconstruction's source correspondence **supports** the C¹,¹ claim at the
  printed (finite-order, subsequence, quotient) strength.
- **REPAIR (one):** the axis-inclusive uniform bound |φ_uv| ≤ C exists in LOY
  only as a §4 prose sentence ("uniform bounds for a corresponding number of
  mixed derivatives follow from the wave equations"). RESULT.md O7 supplies a
  bounded derivation from printed inputs ((3.9), (3.11), (2.8) + Gronwall from
  the axis), which also independently re-proves parity φ_ρ(t,0) = 0 — the
  note's written parity derivation is conditional on exactly this input.
- §4 first-derivative "small bound" (l. 2049-2050) is a confirmed typo
  (contradicts (1.8)); quarantined; coordinator's workaround correct.
- Parity identities hold at quotient level from printed (2.4) + SSESF + (3.11);
  no smooth 4D atlas assumed. Smooth compact profiles and compact parameter
  families satisfy the precise hypotheses uniformly (estimate level); LOY gives
  per-profile subsequences only (uniqueness/family limits out of lane).
- Fidelity notes: Prop 3.18 u-side halves are proof sketches; §4's displayed
  sup-domain overstates the proved domain for order-≥2 terms (harmless on
  compact sets); Remark 4.1 is pure-directions only.

## Limitations

- Audit of one preprint version (v1, no peer-reviewed version recorded).
- RESULT.md O7 is this lane's own mathematics (single-reader); flagged for
  second-reader check at integration.
- Did not audit the Cartesian lifting lemma, smooth-MGHD applicability,
  scattering-map differentiability/uniqueness, or the coordinator §5-§6.

## Unresolved questions

- Second-reader verification of the O7 and mixed-third-derivative derivations
  (now load-bearing).
- Whether Prop 3.18's sketched u-side proofs hide any constant/domain issue
  (residual objection #2).
