# AGENT_REPORT — ontology-cycle-recovery-test

Date: 2026-10-31. Branch: `agent/ontology-cycle-recovery-test`.
Lane report for the task "Compare intrinsic cycle and recovery durations as
candidate constitutive extents". Submission for independent review — not an
accepted completion, not a novelty claim, not a temporal-ontology verdict.

**Scope discipline:** all outputs are inside the owned directory
`research/ontology-reconstruction/cycle-recovery/` plus the root handback file
`AGENT_REPORT.md`. No board, runner, coordinator, manuscript, shared-seed, or
other-lane files were touched. No installs, no child agents, no pushes, no
merges. No numerical grids were used for any claim (exact rational arithmetic
only, §Verification).

## Done and files

- Effective model stated with full protocol (input/output, external clock
  normalization, dissipative energy supply 2μE* = 2βE*² = 2μ²/β ≠ 0, Hopf
  normal-form reduction scope, amplitude-scaling invariance) — RESULT.md §2.
- Unity criterion U(S) stated **before** any present/extent language, checked
  against primary process-unity literature (Montévil–Mossio Definitions 1/4,
  their relaxation-time-scale concept, and their explicit footnote-25 denial
  that mere cycles are unities); Andronov's self-sustaining oscillation
  recovered as U + ω≠0 — RESULT.md §3. No claim that the SL system is a
  genuine autopoietic unity.
- Analytic derivations, no grids: amplitude r* = √(μ/β) (logistic amplitude
  law), cycle period T = 2π/|ω|, transverse recovery exponent λ⊥ = −2μ
  (Floquet exponents {0, −2μ}), exact phase neutrality (isochrons = radial
  rays for real β; scope limit vs generic complex-β spiral isochrons flagged
  via the printed phase map), recovery-duration formula
  t_ε = ln[c(E*−ε)/ε]/(2μ) with its protocol dependence, dimensionless
  invariant ρ = 4πμ/|ω|, and family contrasts (ω=0 sibling; pump cut; β→0) —
  RESULT.md §4.
- Constitutive comparison: positive internal verdict (restoration/throughput
  organization earns the unity-grounding role by a necessity asymmetry; cycle
  activity earns the operation/clock role and supplies the only sharp
  intrinsic duration; ρ-discriminator separates the two selection proposals)
  **plus** a precise failure verdict for the ontological step, with the exact
  missing bridge premises stated — RESULT.md §6. Multiple timescales and
  instantaneous reconstructibility are explicitly *not* treated as
  impossibility proofs.
- Strong rivals with exact falsifiers: instant/event-realist (same physics),
  cycle-selection, restoration-selection — RESULT.md §7.
- Strongest counterexample first (RESULT.md §1); strongest contrary evidence
  recorded (thick-presentism dilemma incl. Hestevold's activity-duration
  temporal atom; project-internal determination≠constitution precedent;
  Montévil–Mossio cycle disclaimer; printed status of all mathematics) —
  RESULT.md §8. Honest novelty verdict: no mathematical novelty claimed;
  no printed predecessor found for the assembled internal comparison within
  stated search limits, classified as a juxtaposition of elementary printed
  results — RESULT.md §10.

Files written:
- `research/ontology-reconstruction/cycle-recovery/RESULT.md` (analysis)
- `research/ontology-reconstruction/cycle-recovery/sources.jsonl`
  (16 records: 4 full-text, 5 abstract, 7 discovery, all with limits)
- `research/ontology-reconstruction/cycle-recovery/AGENT_REPORT.md` (this file)
- `AGENT_REPORT.md` (root handback; replaces a stale report left by an
  unrelated lane on the base branch)

## Search capability check (recorded per brief)

- `web-search-prime` (Z.ai MCP): **failed** — HTTP 429, code 1310 "Weekly/
  Monthly Limit Exhausted. Your limit will reset at 2026-11-17 10:00:29".
  First relevant test query did not execute. Same failure as the
  response-memory-priorart lane reported on 30 Oct.
- `scholar_search`: **works** (openalex + arxiv + crossref); used for the
  capability test and two source-locating queries.
- `exa` `web_search_exa`: **works**; used for three small query batches
  (isochron/phase-amplitude primaries; closure-of-constraints OA locator;
  thick-presentism/constitutive-extent novelty probe). `web_fetch_exa`
  content was used to locate OA copies; every claim-bearing source was then
  fetched and read directly from the primary file.
- No claim rests on a page that was not fetched.

## Source coverage

4 sources read at full-text depth (Andronov 1929 translation; Pietras &
Daffertshofer 2019 selected sections incl. the printed §4.4 oscillator
formulas; Montévil & Mossio 2015 incl. Definitions 1–4 and footnotes 14/25;
Backmann 2025 in full); 5 at abstract depth (Stuart 1960 + companion 1958
abstracts; Lee–Ott–Antonsen; PRK ch. 2 preview; Nakao fetched-not-read;
Brading 2013 inherited record); 7 at discovery depth (Hestevold, Baron,
McKinnon via the full-text-read Backmann survey; Landau, Guckenheimer,
Kuznetsov, Brading 2015 via inherited records — all marked unresolved-or-
inherited URLs and explicit limits). Citation chasing: Andronov→PRK
attribution; Pietras→[12 Kuramoto, 82 Kuznetsov, 91 Guckenheimer, 164 Nakao];
Backmann→[Hestevold 2008 p. 334; Baron 2012; McKinnon 2003; Orilia 2012;
Dainton 2001]. The brief's requirement to read primary oscillator AND
process-unity precedents before original interpretation was met (Andronov,
Pietras–Daffertshofer, Montévil–Mossio, Backmann).

## Verification commands and results

- Fetches (curl) to `/private/tmp/opencode/cycle-recovery/`:
  `andronov_1929_translation.pdf` (139,790 B), `pietras_daffertshofer_2019.pdf`
  (3,871,563 B), `montevil_mossio_2015.pdf` (854,480 B via HAL hal-01192916),
  `backmann_2025_thick_presentism.pdf` (665,930 B), plus `nakao_2016_cphys.pdf`
  (fetched, not read). Two fetch attempts returned HTML (montevil.org wrapper;
  Cambridge chapter) and were re-sourced from HAL; one fetch returned the
  wrong paper (guessed arXiv id) and was discarded — recorded here rather
  than silently dropped.
- `python3 /private/tmp/opencode/cycle-recovery/verify.py` — exact Fraction
  arithmetic verification of all ten algebraic claims used in RESULT.md §4
  (logistic closed form; steady-state balance with nonzero throughput; −2μ
  transverse eigenvalue; recovery-time inversion; protocol monotonicity;
  polar flow decomposition; phase-rate independence of amplitude +
  phase-free radial law; ω=0 sibling Jacobian {−2μ, 0}; pump-cut state-
  dependent halving time with clock still running; scale-free invariant
  ρ = 4πμ/|ω|). **All 10 PASS, elapsed 0.000 s.** Budget: hard ≤15 s,
  actual ≈0 s, total well under 30 s. Two earlier drafts of the *test
  script* contained coding errors (wrong dE/ds factor, inverted inversion
  relation, misdirected inequalities); the analysis was unchanged, the test
  code was corrected, and the final passing run is the one reported. No
  grids, no searches, no floating-point claims.

## Strongest contrary evidence (defeaters found)

1. **All the mathematics is printed.** Pietras & Daffertshofer 2019 §4.2/§4.4
   print the Stuart–Landau form, R_c = √(u₀/u₁), T = 2π/ω, the transverse
   exponent λ₁ = −2u₀, and the phase map Θ = arg w − (v₁/u₁)ln(|w|/R_c)
   (radial isochrons for v₁ = 0). Any claim of mathematical novelty for §4
   would be defeated outright; none is made.
2. **The cycle-present proposal is occupied.** Hestevold's temporal atom
   ("a butterfly flapping its wings exactly twice", 2008 p. 334 via Backmann
   2025 p. 105) is a characteristic-activity-duration present; Backmann 2025
   argues all four thick-presentist views fail, and a cycle-present inherits
   his ordering/overlap dilemma (intra-cycle phase order is strict;
   consecutive cycle-presents overlap).
3. **Cycles are not unities by primary process theory.** Montévil–Mossio 2015
   footnote 25 explicitly distinguishes closure of constraints from mere
   cycles of processes (hydrologic cycle), grounding the brief's caution; the
   lane accordingly claims at most a minimal U-criterion satisfaction, never
   closure.
4. **Determination ≠ constitution (project precedent).** The coordinator's
   W(I) counterexample already blocks both the "instant qualifies" and the
   mirror "interval therefore wins" inferences; R1–R3 are structured to
   respect that lesson, and the lane records the ontological step as a
   precise failure rather than engineering a victory.

## Verdict summary

- Restoration/throughput organization: earns the internal unity-grounding
  comparison (necessity asymmetry; ω=0 witness; pump-cut witness). Its
  intrinsic content is a **rate** (2μ); its duration is protocol-relative —
  no sharp extent without an independently justified tolerance.
- Cycle activity: ancillary to unity; supplies the model's only sharp,
  protocol-independent intrinsic duration (T = 2π/|ω|), i.e. the better
  candidate *if* an extent is demanded — at the price of an extra,
  unjustified clock-essentialist premise (ω=0 sibling refutes the general
  bridge).
- Neither duration is the extent of a concrete present by the effective
  dynamics alone. Exact missing premises recorded (tolerance protocol;
  clock-essentialism; the constitution step itself). No impossibility is
  announced; the internal discriminator (same ω, different μ) is offered as
  the concrete next test.

## Limitations

- Effective-model scope: real-β Stuart–Landau truncation near a supercritical
  Hopf bifurcation; generic complex-β models couple the modes (spiral
  isochrons, printed formula cited) and would weaken exact phase neutrality.
  Nothing here speaks to cosmology; the model does not decide universe
  ontology, and no claim that every stable cycle is a genuine unity is made.
- `web-search-prime` and no other quota'd tools were available; discovery
  relied on scholar_search + exa in three small batches. "No printed
  predecessor found" means within those limits, never "does not exist".
- Hestevold (2008), Baron (2012), McKinnon (2003) known only through the
  full-text-read Backmann survey (quotation-level); Landau, Hopf, Kuznetsov,
  Guckenheimer, Haken, PRK ch. 2 not read beyond discovery/abstract level;
  their roles are provenance, not load-bearing content.
- One planned read was skipped for budget: Nakao 2016 body (fetched, abstract
  only); its citation role is fully carried by Pietras–Daffertshofer, which
  was read in full.
- The root AGENT_REPORT.md inherited from the base branch contained an
  unrelated lane's report (stein-gluing-audit); it was replaced as the
  runner's handback file, consistent with the runner's expectation that the
  root report changes (see the response-memory-priorart lane's recorded
  runner behavior).

## Blockers

None blocking submission. Access limits (web-search-prime quota; paywalled
primaries) are recorded rather than assumed away.

## Proposed next tasks

1. Coordinator test of the ρ-discriminator: two SL systems, identical ω,
   different μ — no candidate unity criterion currently on file preserves
   cycle-extent equality while tracking the restoration difference; if that
   holds, restoration-selection is the only internally coherent process
   proposal (at protocol-relative extent).
2. Protocol task: what could make a tolerance (e.g. an environmental noise
   floor σ) physically constitutive rather than conventional? This is the
   exact missing premise for any sharp restoration-extent; natural companion
   to the coordinator's tolerance-dependent extents (RESPONSE_MEMORY_BENCHMARK
   §4).
3. Thick-presentism bridge: test whether taking intra-cycle phase order
   (θ strictly monotone) as internal times answers Backmann's ordering horn;
   if not, record thick presentism as a standing counter to every
   cycle-duration constitution proposal.
4. Optional small audit: generic complex-cubic first-order phase shift
   (v₁/u₁)(δr₀/r*) from the printed isochron formula, to check whether §6's
   internal verdict survives weak mode coupling; plus library access to
   Hestevold (2008) and Kuznetsov (1998) Ch. 3–4 to upgrade two discovery
   records.
