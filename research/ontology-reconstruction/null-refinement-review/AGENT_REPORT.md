# Agent report: ontology-null-refinements-review

30 October 2026. Headless GLM worker (zai-coding-plan/glm-5.3-flash), branch
`agent/ontology-null-refinements-review`. Task: red-team the sixteen-case 1+1
no-parity census and the corrected topology/persistence refinements in
`coordinator/ONE_PLUS_ONE_CENSUS.md`, audit `coordinator/check_1plus1_refinements.py`,
read `coordinator/PERSISTENCE_CONVENTIONS.md` for the different n≥2 scope, and
try to refute every Oct30 correction claim rather than affirm the counts.
Coordinator owns acceptance; this is a review submission, not a truth claim.
No novelty claim is made; source/mathematical novelty is unclaimed.

## Done and files

* Full line-by-line audit with verdicts, proofs, and counterexample attempts:
  `RESULT.md` (obligations O1–O9 census structure, R1–R14 refinement rows,
  C1–C4 checker audits, P0–P5 salvage probes, interpretation separations,
  repairs N1–N2, unproved extensions).
* Fresh independent exact checker (no coordinator imports, no salvage code):
  `check_null_refinement_review.py` — exact sign-atom algebra, all 64 region
  unions → 16 past sets, every refinement count, the additive-semigroup
  D-forms, point-level S/F_t/boost/P_t/P_c corroboration, E-level transitivity
  spot pairs, sign-convention validation against (t, x), boost rescaling
  witness. Exit 0 in 0.615 s.
* Source records: `sources.jsonl` (3 records, discovery/abstract depths,
  schema per knowledge/README.md).
* Root `AGENT_REPORT.md` (this run's authorized root report, overwriting a
  stale prior lane's file that remains in git history).

## Search capability check

`web-search-prime` was NOT used (quota exhausted per brief; not retried).
Tested instead: MCP server `exa`, tool `web_search_exa` — **worked**. Query 1
returned the primary Springer record for Clifton & Hogarth 1995 (DOI
10.1007/bf01089733, Synthese, 1995-06-01) plus the SEP entry corroborating
Synthese 103:355–387. Query 2 returned Bigaj 2008 (DOI
10.1016/s1871-1774(08)00012-0) with PhilPapers abstract confirming the
transitivity-failure / cumulativity discussion. Recorded in `sources.jsonl` at
discovery/abstract depth. No source was cited beyond the depth actually read.

## Source coverage

Primary objects of audit are project files (census, four coordinator
checkers, PERSISTENCE_CONVENTIONS, persistence-review RESULT and fifth-family
script, salvaged worker checker — SHA256 re-verified before probing, original
untouched). External coverage is deliberately minimal because the claims
audited are internal mathematics and novelty is explicitly unclaimed: two
named predecessors checked at the shallowest honest depth (see
`sources.jsonl` limits). The dedicated census-depth prior-art audit the census
calls for remains open and was not this task.

## Verification commands and results

Runner: `python3 /private/tmp/opencode/t15.py python3 <script>` — hard 15 s
timeout per check (rule: ≤15 s hard, finish ≤10 s; total compute budget 30 s).
Actual: every run ≤ 0.615 s; eleven recorded runs total ≈ 2 s.

* Coordinator scripts all exit 0: `check_1plus1_census.py` (0.160 s),
  `check_1plus1_refinements.py` (0.041 s), `check_null_region_algebra.py`
  (0.028 s), `check_1plus1_pc_census.py` (0.028 s).
* My checker: exit 0 (0.615 s), all eight PASS blocks.
* Salvage probes: as-is fails at line 231 (defect i); +null regions →
  ValueError in the interval helper (defect ii, line 58); +tuple decode →
  `len(valid)==0`, exposing inverted NEG/POS boundary disjuncts (**new
  defect, not coordinator-named**); +fixed tests → all counts through
  transitivity-12 pass, then two DESC expectation sets omit "Zero" (**second
  new defect**); +Zero restored → crash at `len(ftc)==7` (defect iv: correct
  count is 8, exactly as census §4 says); +8 → O6e/O7 pass, then O8 crashes at
  the `rx, ry = region_of_point(x, y)` string unpack (defect iii, original
  line 459; silent for 2-char names like "Ip", the first seed-7 point).
* Detail, verdicts, and evidence per obligation: `RESULT.md`.

## Audit outcome (summary)

* The corrected census verifies in full under exactly its fixed premises:
  sixteen-case completeness (wedge saturation via the h > max(a/A, B/b)
  argument; per-side monotone chains; no cross-side chronological coupling;
  4×4 independence), reflection invariance = 4 rules vs 10 mirror classes,
  P_c+F_t = 9 vs P_c+F_c = 4, F_c+P_t = 9, closedness = 4 (J, C, and the two
  closed null half-spaces {u_L≤0}, {u_R≤0}), closedness+F_c = 1 (J),
  transitivity = 12 with the complete additive-semigroup derivation
  (4 no-wedge rules + 8 one-wedge rules of the form {u_L<0} ∪ ({0}×D),
  D ∈ {{0}, [0,∞), (−∞,0], ℝ}), transitivity+closedness = 3,
  +P_c = 5, +F_c = 8, +P_c+F_c = 3.
* Closedness and transitivity of the null half-spaces were checked
  analytically (preimage of a closed ray; {u≤0}+{u≤0}={u≤0}); the n≥2 table
  was not transferred, and the divergent rows are exactly the ones the census
  flags.
* All six attempted counterexamples failed (RESULT §5); the strongest
  surviving counterexample to the *transfer* of n≥2 rows is the half-space
  pair, which is the census's own claim and was confirmed.
* Two cosmetic census wordings flagged (N1: "mandatory by S" should say "by S
  and the added P_c"; N2: boost η sign convention is a labeling choice).

## Limitations

* Analytic proofs and exact symbolic certificates only; no Lean formalization
  (none was in scope for this task).
* The completeness reduction (boost orbits, saturation) is analytic, re-derived
  here, and corroborated by exact rational witnesses; it is not machine-checked.
* Prior art at discovery/abstract depth only; CH 1995 theorem content is
  inherited from the project's existing full-text audit, not re-read from the
  scan this run.
* Salvage probes ran on copies under /private/tmp/opencode; the preserved
  original was hash-verified before and left untouched. Probes P2–P5 required
  cumulative patches, so their intermediate outputs characterize the salvage's
  defects, not a runnable submission.

## Unresolved questions / proposed next tasks

1. Lean formalization of the census plus the transitivity subfamily (small,
   self-contained target).
2. The dedicated census-depth prior-art audit (Thyssen 2025 degrees; Bigaj
   2008 full text; Clifton–Hogarth descendants; BST settled-set literature).
3. The n≥2 no-parity analogue: does a controlled per-side family exist for
   n ≥ 2 without spatial reflections (rotation transitivity is what dies)?
   Open; not claimed either way.
4. Drop translation covariance and classify what remains (the reduction to a
   single past set P fails); open, likely much larger family.
5. Coordinator-side: adopt N1/N2 wordings at integration; record the two
   additional salvage defects (inverted boundary disjuncts; two omitted
   "Zero" atoms) wherever the salvage's disposition is finalized.
