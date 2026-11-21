# AGENT_REPORT — ontology-constitutive-extent-test

30 October 2026. Resumed run (earlier attempt interrupted by provider quota;
state inspected on resume: worktree clean at `1d1102a`, temp Brading extracts
preserved, no prior output lost). Submission for coordinator inspection; not
accepted completion and not a truth claim. Full argument in
[RESULT.md](RESULT.md); source register in [sources.jsonl](sources.jsonl);
bounded witness in [check_constitutive_extent.py](check_constitutive_extent.py).

## Done (against the brief's done-when)

- **Physical system and independent unity criterion explicit (done-when #1).**
  Criterion U1–U4 (interaction, boundedness, activity, autonomy) stated in
  RESULT.md §2.2 before any extent selection, with no clause mentioning
  "now", present, concreteness, or a desired inventory; activity scale is
  law-fixed (Kepler period, Kapitza drive period, delay latency — check C4).
  Systems: Newtonian gravitational Kepler pair (primary), Kapitza driven
  inverted pendulum, and a delayed-feedback bound oscillator as the explicit
  boundary of the Newtonian bound system's adequacy. Uniqueness of grounds
  not claimed.
- **Constitutive versus predictive extent tested by argument (done-when #2).**
  Central negative result (RESULT.md §4): for Markovian Newtonian dynamics,
  any physically expressible unity criterion is either state+law evaluable
  (instants qualify; no discrimination) or contains the primitive process
  premise P (constitution = process), which the dynamics does not test —
  the **reconstruction dilemma**. Where sufficiency is itself
  non-instantaneous (delay loop), the forced window is a determination fact
  and cross-cuts unity (instances α: no binding; β: binding, same window —
  RESULT.md §3.3, check C3). Naive instant criteria are refuted where they
  deserve it (Kapitza instantaneous-stiffness sign misclassifies the stable
  driven bound state on 50.4% of the cycle, RESULT.md §3.2, check C2), but
  the correct criterion there is itself state+law reconstructible.
- **Ontological bridge and rival counteraccount assessed symmetrically
  (done-when #3).** Bridge 1 (determination→unity) fails in both directions
  (scattering states; delay instances α/β). Bridge 2 (unity→current
  concreteness) needs anchoring, tense asymmetry, and inventory premises the
  criterion does not supply (RESULT.md §5.2); the only candidate independent
  reason found is Brading's own grounding premise, read first-hand and cited
  as a premise, not a result. The instantaneist reconstruction is presented
  first (§1) as the strongest rival and assessed in a four-way symmetric
  table with process, subsystem-block, and event-realist inventories (§6);
  no primitive counting, no scores, no ontology selection.
- **Non-claims honored** (§9): no claim that every sufficient Cauchy region
  is constitutive; no claim that stage-criterion failure proves whole-history
  ground; no uniqueness; no ontology or novelty from consensus.
- **Falsifier** stated precisely (§8): a Markovian system with a unity
  criterion not equivalent to any state+law functional, established by
  dynamics alone — impossible inside Markovian dynamics by determinism, so
  any genuine falsifier needs non-Markovian physics *and* a
  constitution-not-just-constraint demonstration. Sub-falsifiers for the α
  instability, law-fixed scales, and the Kapitza reconstruction point.
- **Primary Brading passages read before attribution.** Both public copies
  downloaded this run; SHA-256 values match the project's recorded audits
  exactly (2013: `c93ca072…`; 2015: `7caceae7…`). Passages cited in
  RESULT.md were read in context from the extracted text; Savitt SEP §3.3
  fetched first-hand from the live entry (revision 6 Oct 2021 confirmed).

## Files

Owned directory `research/ontology-reconstruction/constitutive-extent/`:
`RESULT.md`, `sources.jsonl` (9 records), `AGENT_REPORT.md` (this file),
`check_constitutive_extent.py`. Authorized root `AGENT_REPORT.md` (companion
summary). Nothing else touched; no coordination files, board, runner, shared
seeds, manuscript, or other lanes edited.

## Search capability check (required at start)

- `web-search-prime` (Z.ai server): **failed** — MCP error -429, code 1310,
  "Weekly/Monthly Limit Exhausted. Your limit will reset at 2026-11-17
  10:00:29", on the first relevant query. Not retried; recorded here per the
  brief.
- `scholar_search` (openalex/arxiv/crossref): **worked** — used for the
  Dowe 2000, Müller-adjacent, and Kapitza-adjacent queries; returned exact
  DOI records (e.g. Dowe DOI 10.1017/cbo9780511570650, arXiv:2102.12711).
- `exa` web_search_exa and web_fetch_exa: **worked** — fetched the live SEP
  entry (full page, s. 3.3 located), the Jun–Bechhoefer PRE PDF
  (author-hosted), arXiv:2102.12711 (abs + full text incl. references), and
  ran the post-2021 formalization search.
- `serpapi_search`: available; not needed after the above succeeded; not
  exercised. PhilPapers not retried (HTTP 403 in prior lanes).

## Source coverage

Primary (read first-hand this run): Brading 2013 (full text; hash-matched),
Brading 2015 (full text; hash-matched), Savitt SEP §3.3 (full section),
Jun–Bechhoefer 2012 (abstract + §I from the author-hosted PDF),
Golovinski–Dubinkin arXiv:2102.12711v1 (abstract + intro + reference list,
used only for classical locators). Secondary leads at abstract depth:
Müller 2019 (FoP), Dowe 2000 (CUP). Discovery-only (locators via the
arXiv reference list, explicitly marked): Kapitza 1951, Landau–Lifshitz
Mechanics. Project-internal authorities (read, cited by path/commit):
NEXT_PHILOSOPHICAL_TESTS.md §2, CONSTITUTION_IS_NOT_PREDICTION.md,
paper/SOURCE_AUDIT.md, paper/reviews/savitt-delta/REVIEW.md,
sibling lane outputs (persistence-review; EXPLANATORY_ROLE_TEST.md).

Post-2021 formalizations of Brading's sustaining-region idea: searched
(exa + scholar_search), none found within those venues; absence beyond
searched venues is not evidence of absence.

## Verification commands and results

```
cd research/ontology-reconstruction/constitutive-extent
python3 check_constitutive_extent.py     # total 0.26 s wall (budgets 15 s/10 s/30 s)
shasum -a 256 /private/tmp/opencode/constitutive-extent/brading2013.pdf
#   c93ca072e14c4fd0f1c638ff960db17847231479ec9bf168cf0d69f9644bb054  (matches audit)
shasum -a 256 /private/tmp/opencode/constitutive-extent/brading2015.pdf
#   7caceae74aebe28d1775561cd307dce50f912570eb1a7f9a709d70c699b08f6b  (matches audit)
python3 -c "import json;[json.loads(l) for l in open('sources.jsonl')]"  # 9 records OK
```

Key witness numbers (illustrations of labeled analytic claims, never proofs):
C1 Kepler |ΔE| ≈ 1.6e−14, |ΔL| ≈ 8e−15 over one period, gross exchange
2.667 with net work 0; C2 |Tr M| = 1.308 (stable a=0.2) vs 2.092 (unstable
a=0.02), destabilizing-instant fraction 0.504 in the stable case; C3 slice
insufficiency sup 0.0059, α root Re = +0.2165 (growth) vs β root Re =
−0.3185 (decay); C4 scales 2π / 0.314 / 0.5, all parameter-fixed.

## Strongest contrary evidence

- The state–law reconstruction itself (RESULT.md §1): same physics, same
  predictions, every candidate constitutive fact reproduced as a functional
  of the instantaneous state — the strongest counterexample to the
  constitutive-extent thesis, and the reason the core result is negative.
- Brading's own texts cut against any *definitive* stage criterion: she
  leaves the extent "an empirical matter" that "might be … the size of the
  block universe" (2013, 1109) — so a successful interval criterion was
  never her settled claim, and our failure verdict does not refute her
  program, only bounds what a Newtonian test can give it.
- Savitt's co-presence remark independently anticipates the anchoring gap;
  a reviewer could read §5.2 as re-deriving his objection rather than
  adding to it. The delta claimed is only the two-bridge separation and the
  exact missing premise P.

## Limitations

- Point-mechanical Newtonian systems only; the retarded-field case
  (particle data insufficient without field history) is untested and is the
  natural stronger domain (proposed task 2).
- "Physical = functional of the solution" is itself a premise; a P-defender
  who rejects it escapes §4's dilemma, and engaging that requires
  Dowe/Salmon at full-text depth (proposed task 1).
- Müller 2019 and Dowe 2000 read at abstract depth only; both flagged as
  prior-result threats, neither adjudicated.
- The delay model idealizes the feedback trap (no Langevin noise,
  sampled-hold, or exposure averaging).
- No Lean or other formal verification; all analytic claims are elementary
  and argued inline. PhilPapers remained unread (403 in prior lanes).

## Proposed next tasks

1. **Dowe-process lane** (full text): does conserved-quantity process
   constitution supply P without collapsing into state+law functionals?
   Tests §4's only exit.
2. **Retarded-coupling lane**: repeat the test with delayed field coupling
   where insufficiency of particle-only data is internal to the physics.
3. **Müller 2019 full-text audit**: transposition test of
   indeterminism-based co-presentness onto sustaining regions.
4. **Anchoring lane**: formalize extent vs. location vs. inventory as three
   explicit premises, connecting to the persistence/census machinery.
