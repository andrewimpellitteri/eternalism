# Fix: inherited reports falsely classified as submissions

27 October 2026. Coordinator inspection, implementation and regression checks.

## Observed failure

The horizons-philosophy-contract and horizons-priority-gap-check GLM runs
both stopped on provider quota before writing their deliverables. Their launch
base e30a372 already contained a tracked root AGENT_REPORT.md. The launcher
treated that inherited report plus a clean tree as a completed submission,
despite HEAD still equalling the launch base. Both runs incorrectly entered
review. Neither has fresh owned deliverables; no scientific acceptance occurred.

The mass referee and Stein interpretation run also hit the quota. They left
uncommitted partial research files and were classified failed. All four
supervisors were confirmed stopped before state correction. No retry launched.

## Repair

Automatic submission detection now requires a known ancestral launch commit,
a clean worktree, a fresh committed root report relative to that base, and at
least one surviving changed task-owned file. Committed out-of-scope changes
fail detection. These checks apply even to exit zero. A genuine committed
handback after nonzero exit still enters review, with any quota message kept.
An inherited report, a new report alone, dirty work, unavailable base, or only
deleted task output cannot trigger automatic review.

The two false review states were corrected to claimed/failed while retaining
the same owner, branch, launch base and worktree. run-status-before.json and
run-status-after.json preserve the original result and correction evidence.
The local runtime results were corrected; original provider events remain.
Partial mass-referee notes/checker and the Stein CLAIM_MAP were copied into
preserved/ without editing their worktrees or presenting them as accepted work.
The remaining incomplete lanes are continued in separately claimed native
tasks with disjoint output directories; no GLM quota retry was attempted.

## Validation

25 agent coordination/contract tests pass, including eight real-Git regression
tests for inherited reports, fresh nonzero-exit submissions, report-only or
output-only work, dirty/untracked files, unowned commits, missing bases and
deletion-only submissions. The first run caught a test-fixture staging error
(adding an already git-removed path); the fixture was corrected and the suite
passed. No test tolerance or production requirement was weakened.

## Limits

This detects structural submission evidence, not substantive completeness,
correctness, appropriate source use or novelty. Coordinator inspection remains
mandatory. Ignored files are not deliverables. The preserved GLM notes contain
unfinished calculations and must not be used as a final referee verdict.
The bug fix does not make a failed provider run successful or resolve any
scientific GitHub release gate.
