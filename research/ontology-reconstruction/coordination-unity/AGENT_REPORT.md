# AGENT_REPORT — ontology-coordination-unity

31 October 2026. Worker submission for independent review; not an accepted
completion. Branch `agent/ontology-coordination-unity`, worktree
`/Users/andrew/eternalism/.worktrees/ontology-coordination-unity`.

## Files changed (owned directory only)

All under `research/ontology-reconstruction/coordination-unity/`:

- `RESULT.md` — main deliverable: criterion selection, prior-work verdicts,
  intervention battery with nonvacuous contrast, two exact missing
  premises, event-realist rival assessment, falsifiers, next tasks.
- `sources.jsonl` — 6 records, lane prefix `coord-unity-`, honest depths
  (5 full-text, 1 discovery), SHA256 for every downloaded primary.
- `check_unity_interventions.py` — bounded verification script (stdlib
  only; runtime 0.001 s against the ≤15 s hard / ≤10 s actual limits).
- No other files touched; no board, runner, AGENTS.md, seed, manuscript or
  coordinator edits; no installs; no child agents; no push/merge.

## Search capability check

Brief requires testing one relevant search at start and recording the
server/tool and result:

- `web-search-prime.web_search_prime`: **FAILED** — MCP error -429,
  "Weekly/Monthly Limit Exhausted. Your limit will reset at 2026-11-17
  10:00:29". Reported here as required; not used for any claim.
- `scholar_search` (OpenAlex): **WORKED** — returned relevant records
  (Rider 2024; El-Hani et al. 2024/2025 individuation chapter with OAPEN
  OA link). Used for discovery.
- `exa.web_search_exa`: **WORKED** — located the HAL copies of
  Mossio–Moreno 2010 and Montévil–Mossio 2015. Used for discovery.
- Primary pages were then fetched directly (curl) and inspected before any
  extraction; no claim rests on a search snippet. `serpapi_search` and
  `webfetch` were not needed.

## Source coverage (depths as recorded in sources.jsonl)

- Katherine Brading, "Presentism as an Empirical Hypothesis" (2013):
  **full-text** — complete 11-page author-hosted copy read; §4
  (printed pp. 1104–1105) pinned; SHA256 recorded.
- Katherine Brading, "Physically Locating the Present" (2015):
  **full-text** — complete article read (9-page PDF at the coordinator's
  pinned URL; coordinator ledger lists a 7-page copy — both noted);
  §§4–5 locators pinned; SHA256 recorded.
- Mossio & Moreno, "Organisational closure in biological organisms"
  (2010, HPLS 32(2-3) 269–288): **full-text** — complete HAL author-final
  version read; closure working definition, causal-cycle gloss and
  billiard/river/water-cycle examples pinned; SHA256 recorded.
- Montévil & Mossio, "Biological organisation as closure of constraints"
  (2015, JTB 372: 179–191): **full-text (selected formal sections)** —
  Definitions 1–4 read directly at their §§3–5, plus the
  closure-not-at-an-instant passage (§5), footnote 25 (cycle distinction),
  §6 boundaries and footnote 27; HAL copy (repository pagination; file
  cover cites hal-01192916, DOI 10.1016/j.jtbi.2015.02.029); SHA256
  recorded; journal body not collated.
- El-Hani, Coutinho & Pinto-Leite, "Closure of Constraints and the
  Individuation of Causal Systems in Biology" (Routledge Handbook of
  Causality and Causal Methods, ch. 15): **full-text** — complete 16-page
  CC-BY-NC-ND OAPEN copy read; constraint/dependence/closure definitions,
  enabling-AND-dependent internal-item test, openness-ratio proposal,
  processual/diachronic sections pinned; SHA256 recorded; year metadata
  discrepancy (OpenAlex 2024 record vs title page 2025) noted in the
  record.
- Rider, "Closure of Constraints as a Theoretical Model" (Phil. of
  Science): **discovery only** — OpenAlex abstract; recorded as a lead,
  explicitly not read.
- Inherited provenance (not reread by this worker, referenced by ID):
  coordinator's full-text records `ontology-coord-smith2010-feedback`,
  `ontology-coord-boyd-chua1985-memory`, and the Brading robustness
  records. The apparatus specification and its Smith antecedent are used
  at the coordinator's stated depth, as FEEDBACK_CONSTITUTIVE_TEST.md
  itself does.

Requirement "inspect primary Brading and at least one nearest
process/organizational-closure work before attribution": satisfied — two
primary Brading articles and three primary closure-theory works read
directly before any attribution; RESULT.md flags every adaptation as a
departure rather than attributing it.

## Verification commands and results

```sh
curl -sL -o brading2013.pdf  https://a7ad7762-.../ugd/766654_811c...pdf   # 11 pages
curl -sL -o brading2015.pdf  https://a7ad7762-.../ugd/766654_f45c...pdf   # 9 pages
curl -sL -o mossio_moreno2010.pdf https://shs.hal.science/halshs-00792436v1/file/...  # 16 pages
curl -sL -o montevil_mossio2015.pdf https://hal.sorbonne-universite.fr/hal-01135879/document # 29 pages
curl -sL -o elhani_individuation.pdf https://library.oapen.org/bitstream/20.500.12657/97286/1/... # 16 pages
shasum -a 256 *.pdf       # hashes recorded in sources.jsonl
pymupdf gettext <pdf>     # text extraction (local CLI tool; no install)
python3 check_unity_interventions.py   # bounded computation
```

Script results (all inside the owned directory, stdlib only, 0.001 s):

- Rerouting vs intact: max impulse-response difference 0.00e+00; generator
  vs intact: 0.00e+00 (scripted identity); interruption vs intact:
  0.80 (= first echo) — the 2×2 behind the nonvacuous contrast.
- Apparatus change (τ 5→6 samples): physical loop taps {6,27,48,…} vs
  scripted generator {5,25,45,…}, max divergence 1.0000 — scripted
  equivalence is not robust; robust reproduction requires carriage.
- Graded cohesion: echo energy share = g² exactly (0.640000 / 0.250000 /
  0.010000 for g = 0.8 / 0.5 / 0.1) — approximate unity preserved as live.
- SCC verdicts: intact and rerouting cyclic ({IN,OUT,RET(2)}); interruption
  and generator acyclic (all singletons); backreaction ε>0 merges the
  source for every ε>0 while the graded gain ε/α varies linearly —
  sharp-vs-graded boundary fragility exhibited, not hidden.
- First run had two bugs (step input mislabeled as impulse; generator
  modeled as a partial replay); both were fixed and rerun; the committed
  script is the corrected one. All numbers in RESULT.md come from the
  final run.

## Strongest contrary evidence

1. Mossio–Moreno 2010 §3 (billiard-ball causal cycle) and Montévil–Mossio
   2015 footnote 25 (hydrologic cycle) **directly deny** that circulating
   constrained processes with externally maintained carriers constitute
   organization. This is the strongest evidence against the adapted
   criterion C2, and RESULT.md §3 turns it into the primary negative
   verdict instead of hiding it.
2. Brading 2015 (printed p. 18) leaves genuine subsystem existence an open
   empirical question and supplies no sustaining-extent criterion — so her
   account supports neither C2's sufficiency nor any present-extent claim.
3. The backreaction adversary: any exact graph criterion over-merges under
   arbitrarily weak bidirectional coupling (shown numerically);
   consequently no sharp exclusion claim is made and the one-way-source
   idealization is treated as an approximation needing a stated coupling
   hierarchy.
4. El-Hani et al. 2025 make individuation functional, not physical — which
   undercuts any attempt to read closure-style unity directly as a
   physical boundary or as an inventory restriction.

## Limitations

- The unity verdicts concern a linear delay-line toy apparatus; no
  quantum, relativistic-field or biological case is treated.
- Unity ≠ life: no self-maintenance claim; the loop remains a causal cycle
  under the only independently defended closure criterion (RESULT.md §3).
- Brading's and closure-theory texts were read once this session at
  recorded depths; no independent Newton-history or biology audit; HAL
  copies were not collated with journal bodies.
- `web-search-prime` quota exhausted (resets 2026-11-17); coverage relied
  on OpenAlex + exa discovery followed by direct primary fetches; any
  source neither fetched nor inherited is either marked discovery-only or
  omitted.
- C2 is this worker's adaptation, defended here only by the intervention
  contrasts; it is not attributed to any source author.

## Blockers

None preventing submission. The two substantive gaps are reported as
results (exact missing premises in RESULT.md §§3 and 6), not silently
papered over.

## Proposed next tasks

As listed in RESULT.md §9: (1) carrier self-maintenance variant to test
missing premise (1); (2) model-theoretic audit of the C2 departure from
autonomy theory (starting from the Rider 2024 lead); (3) quantitative
backreaction ledger for the two-channel loop; (4) dedicated bridge audit
for missing premise (2) — whether any source defends "only the organizing
activity's duration is concrete".

## Resumed-run addendum (31 October 2026, later same day)

The first attempt committed the full submission (`b9d6bbc`) and was
interrupted after that commit. On resume, working tree clean; all four
owned files intact; no rework needed. Verification performed on resume:

- `python3 check_unity_interventions.py` re-run: reproduces every number
  committed in RESULT.md §5 — reroute diff 0.00e+00, generator diff
  0.00e+00, interruption diff 8.00e-01, post-apparatus-change divergence
  1.0000 at sample 5 with loop taps (6, 1.0), (27, 0.8), (48, 0.64);
  echo shares 0.639999/0.250000/0.010000 vs exact g²; SCC verdicts for
  all five configurations; graded gains ε/α = 0.1000 / 0.0100. Wall time
  0.037 s — inside all computation limits.
- Script audit on resume: the generator identity is explicitly labeled
  "model generator, scripted input" in the output; the robustness
  subsection is the scripted equivalence's exposure, not a hidden
  triviality; SCC labeled textbook machinery; runtime assert enforces
  the budget. No integrity concern found.
- Search capability re-check on resume: `web-search-prime` still
  **FAILED** with the same MCP error -429 / code 1310, "Weekly/Monthly
  Limit Exhausted", reset 2026-11-17 10:00:29; `scholar_search`
  (OpenAlex) **WORKED** on a fresh closure/unity query (returns records;
  one new lead surfaced — Borkel, "A Formal Minimal Concept of Life",
  PhilPapers, abstract seen only, discovery depth, not used for any
  claim here).
- Cross-checks against required documents: NEXT_FRONTIER_TASKS §1's
  required elements (criterion before present extent, primary
  process/closure reading before attribution, the five-intervention
  battery with laws held fixed, the three adversaries, no
  definition-by-fiat) are each addressed in RESULT.md §§2–5;
  FEEDBACK_CONSTITUTIVE_TEST §5's positive question is the exact target,
  and its §3 response-support selector is used only as a refuted foil
  (RESULT.md §6); CONSTITUTIVE_SUBMISSION_REVIEW's repair requirements
  are respected — no reconstruction-implies-constitution step, no
  region-vs-instant conflation, no relabeled reconstruction.

No result-bearing content was changed by the resume; this addendum and
its commit are the only new changes. Submission remains a worker draft
for independent review.
