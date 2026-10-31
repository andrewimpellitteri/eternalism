# Review queue

Snapshot of 31 October 2026, taken from the local board after the coordinator stopped. It lists the
62 tasks still in `claimed` or `review`. **Nothing here is accepted.** Inclusion in the tree
means a file is preserved, not that its claims hold.

"Coordinator notes" lists documents that mention the task or its folder. A mention can be a rejection
or a request for repair, and "none found" means only that a text search found nothing. The list
was built by search, not by reading the notes.

Board state lives in the ignored `.agent-runtime/`, so this file is a dated copy. Refresh the state
with `python3 scripts/agents.py status`.

## Accepting a task

`accept` needs the branch to be an ancestor of `HEAD`, and it needs the task's worktree. Files rescued
below were copied, not merged, so accepting one of those tasks still needs `git merge agent/<task>`.
Branches are all kept. If a worktree has been removed, restore it first:

```bash
git worktree add .worktrees/<task> agent/<task>
```

## Rescued on 31 October: not previously in the tree

33 tasks whose results existed only on local branches or in uncommitted worktree files.
Treat these as unreviewed worker submissions unless a coordinator note says otherwise.

| Task | State | Output | Coordinator notes |
|---|---|---|---|
| `horizons-echo-exactness` | review | [horizons/glm/echo-exactness](horizons/glm/echo-exactness/) | none found |
| `horizons-echo-robustness` | review | [horizons/glm/echo-robustness](horizons/glm/echo-robustness/) | none found |
| `horizons-perturbation-referee` | claimed | [horizons/glm/perturbation-referee](horizons/glm/perturbation-referee/) | none found |
| `horizons-scalar-priority` | review | [horizons/glm/scalar-priority](horizons/glm/scalar-priority/) | none found |
| `lawful-central-history-review` | claimed | [lawful-completions/central-history-review](lawful-completions/central-history-review/) | [FINITE_CONTROL_ACCEPTANCE.md](lawful-completions/coordinator/FINITE_CONTROL_ACCEPTANCE.md), [NEXT_FRONTIER_TASKS.md](ontology-reconstruction/coordinator/NEXT_FRONTIER_TASKS.md) |
| `lawful-completions-constraints` | review | [lawful-completions/constraints](lawful-completions/constraints/) | [CONSTRAINTS_REVIEW.md](lawful-completions/coordinator/CONSTRAINTS_REVIEW.md), [BASELINE_NOTES.md](lawful-completions/coordinator/BASELINE_NOTES.md) |
| `lawful-completions-priority` | review | [lawful-completions/priority](lawful-completions/priority/) | [PRIORITY_REVIEW.md](lawful-completions/coordinator/PRIORITY_REVIEW.md), [BASELINE_NOTES.md](lawful-completions/coordinator/BASELINE_NOTES.md) |
| `lawful-finite-cone-continuity` | review | [lawful-completions/finite-cone-continuity](lawful-completions/finite-cone-continuity/) | [BATCH2_INITIAL_REVIEW.md](lawful-completions/coordinator/BATCH2_INITIAL_REVIEW.md) |
| `lawful-higher-regularity-audit` | review | [lawful-completions/higher-regularity-review](lawful-completions/higher-regularity-review/) | [QUOTA_HOLD_2026_10_30.md](ontology-reconstruction/coordinator/QUOTA_HOLD_2026_10_30.md), [REVIEW_DISPOSITION_2026_10_30.md](ontology-reconstruction/coordinator/REVIEW_DISPOSITION_2026_10_30.md) |
| `lawful-scalar-common-extension` | review | [lawful-completions/scalar-common-extension](lawful-completions/scalar-common-extension/) | [BATCH2_INITIAL_REVIEW.md](lawful-completions/coordinator/BATCH2_INITIAL_REVIEW.md) |
| `ontology-bridge-premises` | review | [ontology-reconstruction/bridges](ontology-reconstruction/bridges/) | none found |
| `ontology-bridges-repair` | review | [ontology-reconstruction/repairs/bridges](ontology-reconstruction/repairs/bridges/) | [BATCH2_RUN_PLAN.md](ontology-reconstruction/coordinator/BATCH2_RUN_PLAN.md) |
| `ontology-constitutive-bridge-pilot` | review | [agentic-philosophy/constitutive-bridge-pilot](agentic-philosophy/constitutive-bridge-pilot/) | none found |
| `ontology-constitutive-extent-test` | review | [ontology-reconstruction/constitutive-extent](ontology-reconstruction/constitutive-extent/) | [CONSTITUTIVE_SUBMISSION_REVIEW.md](ontology-reconstruction/coordinator/CONSTITUTIVE_SUBMISSION_REVIEW.md), [NEXT_PHILOSOPHICAL_TESTS.md](ontology-reconstruction/coordinator/NEXT_PHILOSOPHICAL_TESTS.md) |
| `ontology-coordination-unity` | review | [ontology-reconstruction/coordination-unity](ontology-reconstruction/coordination-unity/) | [NEXT_FRONTIER_TASKS.md](ontology-reconstruction/coordinator/NEXT_FRONTIER_TASKS.md) |
| `ontology-cycle-recovery-test` | review | [ontology-reconstruction/cycle-recovery](ontology-reconstruction/cycle-recovery/) | [NEXT_FRONTIER_TASKS.md](ontology-reconstruction/coordinator/NEXT_FRONTIER_TASKS.md) |
| `ontology-equivalence-repair` | review | [ontology-reconstruction/repairs/equivalence](ontology-reconstruction/repairs/equivalence/) | [BATCH2_RUN_PLAN.md](ontology-reconstruction/coordinator/BATCH2_RUN_PLAN.md) |
| `ontology-expansion-equivalence` | review | [ontology-reconstruction/equivalence](ontology-reconstruction/equivalence/) | none found |
| `ontology-modal-category-bridge` | review | [ontology-reconstruction/modal-category](ontology-reconstruction/modal-category/) | [NEXT_PHILOSOPHICAL_TESTS.md](ontology-reconstruction/coordinator/NEXT_PHILOSOPHICAL_TESTS.md), [MODAL_CATEGORY_REVIEW.md](ontology-reconstruction/coordinator/MODAL_CATEGORY_REVIEW.md) |
| `ontology-modal-density-search` | review | [agentic-philosophy/result-search-round1/modal-density](agentic-philosophy/result-search-round1/modal-density/) | [CLAIM_STATUS.md](CLAIM_STATUS.md), [CURRENT_SYNTHESIS.md](CURRENT_SYNTHESIS.md) |
| `ontology-natural-assignments` | review | [ontology-reconstruction/classification](ontology-reconstruction/classification/) | [BATCH2_RUN_PLAN.md](ontology-reconstruction/coordinator/BATCH2_RUN_PLAN.md) |
| `ontology-null-refinements-review` | review | [ontology-reconstruction/null-refinement-review](ontology-reconstruction/null-refinement-review/) | [QUOTA_HOLD_2026_10_30.md](ontology-reconstruction/coordinator/QUOTA_HOLD_2026_10_30.md), [REVIEW_DISPOSITION_2026_10_30.md](ontology-reconstruction/coordinator/REVIEW_DISPOSITION_2026_10_30.md) |
| `ontology-occurrence-warrant-search` | review | [agentic-philosophy/result-search-round1/occurrence](agentic-philosophy/result-search-round1/occurrence/) | [CLAIM_STATUS.md](CLAIM_STATUS.md) |
| `ontology-persistence-priorart` | review | [ontology-reconstruction/persistence-priorart](ontology-reconstruction/persistence-priorart/) | [QUOTA_HOLD_2026_10_30.md](ontology-reconstruction/coordinator/QUOTA_HOLD_2026_10_30.md), [REVIEW_DISPOSITION_2026_10_30.md](ontology-reconstruction/coordinator/REVIEW_DISPOSITION_2026_10_30.md) |
| `ontology-rival-contracts` | review | [ontology-reconstruction/rivals](ontology-reconstruction/rivals/) | none found |
| `ontology-rivals-repair` | review | [ontology-reconstruction/repairs/rivals](ontology-reconstruction/repairs/rivals/) | [BATCH2_RUN_PLAN.md](ontology-reconstruction/coordinator/BATCH2_RUN_PLAN.md) |
| `past-shadow-ltb-sources` | review | [lawful-completions/past-shadow/sources](lawful-completions/past-shadow/sources/) | none found |
| `prior-art-becoming` | review | [bowtie-horizons-prior-art/becoming](bowtie-horizons-prior-art/becoming/) | none found |
| `screening-review` | review | [bowtie-horizons-screening-review](bowtie-horizons-screening-review/) | [SCREENING_OWNER_HANDOFF.md](lawful-completions/coordinator/SCREENING_OWNER_HANDOFF.md), [CLAUDE_SCREENING_REVIEW.md](lawful-completions/coordinator/CLAUDE_SCREENING_REVIEW.md) |
| `stein-core-repairs` | review | [stein-gr/tasks/core-repairs](stein-gr/tasks/core-repairs/) | none found |
| `stein-interpretation-audit` | claimed | [stein-gr/tasks/interpretation](stein-gr/tasks/interpretation/) | none found |
| `stein-null-boundary-audit` | claimed | [stein-gr/tasks/null-boundary](stein-gr/tasks/null-boundary/) | none found |
| `stein-priority-audit` | review | [stein-gr/tasks/priority-audit](stein-gr/tasks/priority-audit/) | none found |

## Already in the tree, never formally accepted

21 tasks.

| Task | State | Output | Coordinator notes |
|---|---|---|---|
| `book-exploration-samples` | review | [book-exploration](book-exploration/) | none found |
| `bowtie-horizon-rationale` | review | [bowtie-horizons](bowtie-horizons/) | [SCREENING_OWNER_HANDOFF.md](lawful-completions/coordinator/SCREENING_OWNER_HANDOFF.md), [HORIZON_REVIEW.md](lawful-completions/coordinator/HORIZON_REVIEW.md) |
| `future-ground-temporal-asymmetry` | review | [future-ground-asymmetry](future-ground-asymmetry/) | none found |
| `github-current-paper-gates` | review | `GATES.md` | none found |
| `horizons-independent-redteam` | review | [horizons/coordinator-review](horizons/coordinator-review/) | none found |
| `horizons-mass-review-recovery` | review | [horizons/native/mass-recovery](horizons/native/mass-recovery/) | none found |
| `horizons-perturbation-continuation` | review | [horizons/continuation-2026-10-27](horizons/continuation-2026-10-27/) | none found |
| `lawful-collapse-extension` | review | [lawful-completions/collapse-extension](lawful-completions/collapse-extension/) | none found |
| `lawful-completions-coordinator` | claimed | [lawful-completions/coordinator](lawful-completions/coordinator/) | [MAXIMALITY_AND_EXISTENTIAL_OPENNESS.md](ontology-reconstruction/coordinator/MAXIMALITY_AND_EXISTENTIAL_OPENNESS.md), [DIRECT_RECOVERY_2026_10_30.md](ontology-reconstruction/coordinator/DIRECT_RECOVERY_2026_10_30.md) |
| `lawful-scattering-energy` | review | [lawful-completions/energy](lawful-completions/energy/) | [CLAIM_STATUS.md](CLAIM_STATUS.md) |
| `lawful-scattering-regularity` | review | [lawful-completions/regularity](lawful-completions/regularity/) | none found |
| `native-horizons-mass-final-review` | review | [horizons/native/mass-final-review](horizons/native/mass-final-review/) | none found |
| `native-horizons-norm-review` | review | [horizons/native/norm-review](horizons/native/norm-review/) | none found |
| `native-horizons-source-recovery` | review | [horizons/native/source-recovery](horizons/native/source-recovery/) | none found |
| `native-time-bridge-recovery` | review | [horizons/native/bridge-recovery](horizons/native/bridge-recovery/) | none found |
| `ontology-process-explanation-review` | claimed | [agentic-philosophy/process-explanation-review](agentic-philosophy/process-explanation-review/) | [PROCESS_EXPLANATION_REPORT.md](ontology-reconstruction/coordinator/PROCESS_EXPLANATION_REPORT.md), [PROCESS_EXPLANATION_TEST.md](ontology-reconstruction/coordinator/PROCESS_EXPLANATION_TEST.md) |
| `prior-art-bst` | review | [bowtie-horizons-prior-art/bst](bowtie-horizons-prior-art/bst/) | none found |
| `prior-art-prediction` | review | [bowtie-horizons-prior-art/prediction](bowtie-horizons-prior-art/prediction/) | none found |
| `refocus-selection-integration` | claimed | [refocus-2026-10-21/coordinator](refocus-2026-10-21/coordinator/) | none found |
| `runner-fresh-submission` | review | `scripts/agents.py` | none found |
| `stein-gluing-audit` | review | [stein-gr/tasks/gluing-audit](stein-gr/tasks/gluing-audit/) | none found |

## Stale claims with no output

8 tasks hold a claim but left no files in their owned paths. No worker process is running
for any of them. They are candidates for `python3 scripts/agents.py release`, which needs a note.

| Task | State | Owned path |
|---|---|---|
| `bowtie-horizon-review` | claimed | `research/bowtie-horizons-review/` |
| `horizons-philosophy-contract` | claimed | `research/horizons/glm/philosophy-contract/` |
| `horizons-priority-gap-check` | claimed | `research/horizons/glm/priority-gap-check/` |
| `lawful-prefix-energy-control` | claimed | `research/lawful-completions/prefix-energy-control/` |
| `past-shadow-lemma` | claimed | `research/lawful-completions/past-shadow/lemma/` |
| `past-shadow-ltb-numerics` | claimed | `research/lawful-completions/past-shadow/ltb/` |
| `stein-causet-audit` | claimed | `research/stein-gr/tasks/causet-audit/` |
| `stein-energy-rigidity-audit` | claimed | `research/stein-gr/tasks/energy-rigidity/` |
