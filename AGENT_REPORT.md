# Agent report: kb-agent-methods

Task: Audit AI-assisted physics and design evidence-preserving synthesis.
Worktree: `.worktrees/kb-agent-methods`, branch `agent/kb-agent-methods`.
This is a submission for independent review, not a final truth claim.

## Done / files changed

- `knowledge/methods/sources.jsonl` — 10 source records (2 full-text reads,
  4 abstract reads, 2 repository/benchmark discovery records, 2 citation
  leads), each with version, locator, limits, and cross-lane `related_source_ids`.
- `knowledge/methods/prior-methods.md` — comparison of six public AI-assisted
  physics workflows; reusable-artifact inventory; consolidated failure-mode
  taxonomy F1–F10 with primary-source anchors; documented evidence that
  agreement ≠ correctness.
- `knowledge/methods/handoff-contract.md` — four specialist roles (extractor,
  translator, counterexample, reviewer), handoff artifact schema (JSONL
  fields, contract rules C1–C6), and an eight-step semantic-audit procedure.
- `knowledge/methods/pilot-design.md` — defect-injection pilot: two target
  families with known answers, 8 labeled defect classes + 2 clean controls,
  baselines B0–B2, blind scoring, pre-registered pass criteria, cost bounds,
  and a proposed (not created) workboard entry.
- `AGENT_REPORT.md` — this file.

Owned scope (`knowledge/methods/`, `AGENT_REPORT.md`) respected; no other
files modified; workboard, runner, and shared seed untouched.

## Search capability check

- Z.ai MCP `web-search-prime`: NOT available in this worker session.
  `tools.opencode.list_mcp_resources()` returned empty resources and templates;
  the built-in `websearch` tool failed twice with "Web search cancelled".
  Recorded as a blocker for search-led discovery; no search-engine result is
  claimed anywhere in this submission.
- Direct `webfetch` (HTTP GET): WORKS. Used against arxiv.org abstract pages,
  arxiv.org/html full texts, and github.com. All claims about papers below come
  from these primary fetches, at the depths recorded in sources.jsonl.
- Citation chasing replaced keyword search: reference lists of fetched
  full texts supplied the comparator set (FERMIACC, Agentic Diagrammatica,
  TPBench, Ax-Prover). The two unfetched leads are labeled `discovery` with
  explicit "do not quote specifics" limits.

## Source coverage and reading depth

Fetched and read this session:

| Source | Depth | What was taken |
|---|---|---|
| arXiv:2605.08212v1 (Hell & Thiele, CAS agents) | full-text (HTML) | setup, 4 contexts, pass rates 5/9, 5/9, 7/9, 3/9, failure discussions, grading rubric, reference list |
| arXiv:2607.07857v1 (Lu, Tjoa, Cirac, TNLean) | full-text (HTML main text + appendix extracts A.1–A.2, C, D.1–D.3, E.2–E.3) | role table, delegation/orchestration, memory system, gap taxonomy, cost figures, six review rounds |
| arXiv:2607.06379v1 (Douglas, SW in Lean) | full-text (HTML, Secs. 1–5 + appendices headers) | H0–H7 predicate design, dictionary, #print axioms footprints, oracle suites (278 checks), vacuity-hardening cases, adversarial-review incident |
| arXiv:2609.05157v1 (AxQM) | abstract | grading rule, task counts, private solutions |
| arXiv:2506.06214v2 (position paper) | abstract | claimed gaps, verification-framework call |
| arXiv:2603.22538v1 (FERMIACC) | abstract | scope claim only; flagged unaudited |
| arXiv:2603.26990v1 (Agentic Diagrammatica) | abstract | implicit-conventions problem, two remedies, known-answer catalog pattern |
| github.com/LionSR/TNLean | discovery (README + repo index) | pinned toolchain v4.35.0-rc3, paper-gaps convention, badges, licenses as displayed |

Not fetched (labeled as leads, not used for any specific claim):
arXiv:2502.15815 (TPBench), arXiv:2510.12787 (Ax-Prover); Douglas repository
internals; TNLean build; the Physlib/AxQM repositories (covered at discovery
depth by the kb-formalization lane, records `form-*` reused here by ID).

Deliberate exclusions: the multi-agent-debate ML literature and general
autoformalization surveys were not searched (search tooling unavailable;
kept out of scope rather than covered from memory).

## Verification commands and results

```sh
python3 scripts/agents.py brief kb-agent-methods   # read; scope confirmed
python3 -c "import json;[json.loads(l) for l in open('knowledge/methods/sources.jsonl')]"
# -> 10 valid records
```

- No packages installed; no code built; no agent launched; no paid run.
- Quantitative figures quoted in the deliverables (pass rates, costs, check
  counts, toolchain version) were copied from the fetched primary texts and
  are attributed to their authors' reports, not independently reproduced.

## Strongest contrary evidence (against our design's assumptions)

- Douglas's 62-passing-numerical-checks-then-3-gaps incident cuts both ways:
  it motivates statement-level review, but also shows review can reject
  candidates that pass every mechanical check — our procedure could
  false-reject correct artifacts. The clean-control false-accusation metric in
  the pilot exists to measure exactly this risk.
- TNLean's bottleneck finding ("enforcing mathematical intent") suggests role
  separation alone is insufficient; their fix required human strategic review
  rounds. Our design keeps a human/coordinator intent check for this reason.
- Hell–Thiele found context tailoring helps but can introduce new failure
  modes; our extraction-record design could similarly over-constrain
  translators to an extractor's misreading. The counterexample role receives
  sources, not just the map, partly to catch this.
- TheAxQM grading rule (kernel-only) is presented in prior-methods.md as a
  boundary case; its authors might respond that statement-level grading is
  deferred by design, not missed — the comparison table records what their
  benchmark claims, not an error on their part.

## Limitations

- No working search engine this session: the "compare public workflows" sweep
  is seed-anchored and citation-chased, not query-driven. Unfetched areas
  (debate literature, recent agent frameworks beyond the comparators) are
  explicitly unreviewed, not absent.
- TNLean, Douglas repo, AxQM: nothing cloned, built, or rerun; artifact
  reusability claims rest on README/paper text at the stated depths. No commit
  SHAs captured (GitHub page views did not expose them), so every code reuse
  item is gated on pinning.
- The two full-text reads of the method papers are authors' accounts of their
  own systems; no independent reproduction of any reported result.
- The pilot is a design only; its defect suite is synthetic and its pass
  criteria are pre-registered but untested.
- All sources are public; no credentials, private repositories, or personal
  data entered this context.

## Unresolved questions / proposed next tasks

1. Coordinator decision: create the `pilot-semantic-audit` task (draft entry
   in pilot-design.md §8) and authorize its run; without new authorizations
   nothing executes.
2. Pin commits for TNLean, mrdouglasny/seiberg-witten, AxQM before any reuse
   (an inspection-only task, no installs).
3. Full-text reads for the four abstract-level comparators (FERMIACC,
   Diagrammatica, AxQM, position paper v1→v2 diff) to firm up the comparison.
4. Family B of the pilot requires raising seed-qrf/temporal-measurement
   records from `abstract` to `full-text` — coordinate with the frontier lane's
   audit targets to avoid duplicate reading.
5. If search tooling returns, run the defeated-novelty searches NOVELTY.md
   asks for against the failure-mode taxonomy (has anyone benchmarked agents
   on injected physics-translation defects?).
