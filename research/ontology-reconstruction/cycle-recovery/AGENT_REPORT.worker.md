# Agent report: ontology-cycle-recovery-test

31 October 2026. Headless GLM worker (OpenCode, `zai-coding-plan/glm-5.3-flash`),
isolated worktree, task `ontology-cycle-recovery-test` (coordinator
NEXT_FRONTIER_TASKS.md §2). Submission for independent review — not an
accepted completion.

## Task

Compare the Stuart–Landau limit cycle's intrinsic durations (cycle period vs
transverse recovery) as candidate constitutive extents, under a unity
criterion stated independently of any desired present; strong rivals with
exact falsifiers; prior work before original interpretation; no grids, no
novelty/ontology by definition.

## Deliverables

- `research/ontology-reconstruction/cycle-recovery/RESULT.md` — analysis:
  effective model + protocol + clock normalization + dissipative throughput;
  unity criterion U(S) stated before any extent language; analytic
  derivations (r* = √(μ/β), T = 2π/|ω|, λ⊥ = −2μ, exact phase neutrality for
  real β, recovery-duration formula and its protocol dependence, invariant
  ρ = 4πμ/|ω|); strongest counterexample first; constitutive comparison
  (restoration earns unity-grounding; cycle supplies the only sharp intrinsic
  duration; neither earns "present" — exact missing premises recorded);
  rivals R1–R3 with exact falsifiers; contrary evidence; novelty verdict;
  limitations; next tasks.
- `research/ontology-reconstruction/cycle-recovery/sources.jsonl` — 16 source
  records with strict metadata and honest depths (4 full-text, 5 abstract,
  7 discovery).
- `research/ontology-reconstruction/cycle-recovery/AGENT_REPORT.md` — lane
  report (done/files, search capability check, coverage, verification,
  contrary evidence, limitations, blockers, next tasks).

## Search capability check

- `web-search-prime`: **failed** — HTTP 429, code 1310, weekly limit exhausted
  (resets 2026-11-17). Recorded; first relevant search did not execute.
- `scholar_search` (openalex/arxiv/crossref) and `exa` web search: **worked**;
  three small batches. All claim-bearing sources fetched and read directly;
  no claim rests on an unfetched page.

## Verification

- Exact-arithmetic verification script
  (`/private/tmp/opencode/cycle-recovery/verify.py`): 10/10 checks PASS,
  elapsed 0.000 s (Fraction arithmetic; no grids; within hard ≤15 s /
  actual ≤10 s / total ≤30 s budget). Covers every algebraic claim in
  RESULT.md §4. Two earlier drafts of the *test code* had assertion bugs
  (analysis unchanged); corrected and re-run — final run passes as reported.
- Primary fetches read directly: Andronov 1929 (Comptes Rendus translation,
  full text), Pietras & Daffertshofer 2019 Physics Reports (full text,
  selected sections incl. printed §4.4 oscillator formulas), Montévil & Mossio
  2015 (HAL, full text, Definitions 1–4, fn. 14/25), Backmann 2025
  (Metaphysica, full text).

## Key results (for the coordinator's inspection)

1. Restoration has an intrinsic **rate** (2μ) but no sharp intrinsic
   **duration** (t_ε = ln[c(E*−ε)/ε]/(2μ), monotone in both protocol
   parameters).
2. Cycle activity is not necessary for the unity: the ω=0 family member
   satisfies the same criterion with the same throughput and recovery rate,
   no cycle, no clock (family contrast, not a same-law intervention).
3. Positive internal comparison: restoration earns unity-grounding; the cycle
   period is the model's only sharp protocol-independent intrinsic duration;
   a free dimensionless invariant ρ = 4πμ/|ω| separates the two selection
   proposals empirically inside the family.
4. Precise failure of the ontological step: neither duration is the extent of
   a concrete present without (i) an independently justified tolerance
   protocol, (ii) a clock-essentialist premise, and (iii) the constitution
   argument itself — none supplied by the effective model.
5. No mathematical novelty claimed: every §4 quantity is printed (Pietras &
   Daffertshofer §4.2/§4.4; Andronov 1929; Stuart 1960 abstract-level
   provenance). No printed predecessor found, within stated search limits,
   for the assembled internal comparison; classified as a juxtaposition of
   elementary printed results.

## Limitations

Effective-model scope only (real-β Hopf truncation); web-search-prime
quota-exhausted; three philosophical primaries known at quotation level via
the full-text-read Backmann survey; Nakao 2016 fetched but not read (abstract
only; role carried by the full-text-read review). Full details in the lane
report.

## Unresolved questions

See lane report §Proposed next tasks: the ρ-discriminator test, the tolerance-
protocol constitution question, the Backmann ordering-horn bridge, and the
optional generic-cubic correction.
