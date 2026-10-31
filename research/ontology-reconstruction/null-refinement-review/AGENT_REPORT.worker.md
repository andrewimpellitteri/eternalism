# Agent report: ontology-null-refinements-review

30 October 2026. Headless GLM worker. Branch
`agent/ontology-null-refinements-review`. Lane report with full detail:
`research/ontology-reconstruction/null-refinement-review/AGENT_REPORT.md`;
line-by-line verdicts: `research/ontology-reconstruction/null-refinement-review/RESULT.md`.

## Task

Red-team the coordinator's sixteen-case 1+1 no-parity census
(`research/ontology-reconstruction/coordinator/ONE_PLUS_ONE_CENSUS.md`) and
`check_1plus1_refinements.py`, read `PERSISTENCE_CONVENTIONS.md` for the
different n≥2 scope, and try to refute the Oct30 correction claims: reflection
invariance is four rules versus ten mirror classes; closed rules are J, C and
two null half-spaces; P_c+F_t gives nine whereas P_c+F_c gives four; plus the
wedge saturation, monotone per-side chains, no-cross-side sufficiency, and
every refinement-table converse under exactly the fixed premises.

## Result

**No counterexample found. Every corrected claim verifies.** All counts
reproduced by this lane's independent exact checker and by analytic
re-derivation: 16-case completeness; 4 invariance rules vs 10 mirror classes;
P_c 9 / F_c 9 / both 4; closed 4 = {J, C, {u_L≤0}, {u_R≤0}}; closed+F_c = 1;
transitive 12 (additive-semigroup proof re-derived: 4 no-wedge + 8 one-wedge
rules of the form {u_L<0} ∪ ({0}×D)); transitive+closed 3; +P_c 5; +F_c 8;
+P_c+F_c 3. Closedness and additivity of the half-spaces proved analytically;
the n≥2 rows were not transferred. Conditional set theory, topology, and
physical regularity kept separate; no ontology selected; no novelty claimed.

Salvaged quota-interrupted checker audited by probe runs (original untouched,
SHA256 re-verified): all four coordinator-named defects confirmed (line-231
assertion; tuple/string helper mismatch; O8 `rx, ry = region_of_point(...)`
string unpack at original line 459; the wrong `len(ftc)==7`, correct 8), plus
two defects the coordinator did not name: inverted NEG/POS boundary disjuncts
in the same helper, and two DESC expectation sets omitting "Zero". After
correction the salvage's algebra agrees with the census on every count.

## Files changed

* `research/ontology-reconstruction/null-refinement-review/RESULT.md` (new)
* `research/ontology-reconstruction/null-refinement-review/AGENT_REPORT.md` (new)
* `research/ontology-reconstruction/null-refinement-review/sources.jsonl` (new)
* `research/ontology-reconstruction/null-refinement-review/check_null_refinement_review.py` (new)
* `AGENT_REPORT.md` (root, authorized, this file — replaces a stale
  stein-gluing-audit report left in the worktree; that content remains in
  history)

## Evidence and checks

Search capability: MCP `exa` `web_search_exa` worked (web-search-prime not
touched, per brief). Clifton–Hogarth 1995 DOI/journal and Bigaj 2008
cumulativity abstract verified; recorded in lane `sources.jsonl` at
discovery/abstract depth with explicit limits.

Compute: hard 15 s timeouts; eleven runs, each ≤ 0.615 s, total ≈ 2 s (budget
30 s). Coordinator scripts all pass. Lane checker
`check_null_refinement_review.py` (fresh, exact sign-atom algebra, no
coordinator imports) exits 0. Probe log in lane `RESULT.md` §3/§8.

## Limitations

No Lean formalization; completeness reduction is analytic (re-derived) with
exact witnesses, not machine-checked; prior art at discovery/abstract depth
only (CH theorem content inherited from the project's full-text audit);
n≥2 no-parity analogue and the no-translation-covariance family are open and
unclaimed.

## Submission status

This is a worker submission for independent coordinator review, not accepted
completion. No board, runner, seed, or manuscript files touched; nothing
pushed or merged.
