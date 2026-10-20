# Citation gate hardening — reviewed implementation

Task: `rt-citation-gate-hardening`
Claim holder: `codex-citation-gate`
Date: 2026-10-20
Status: review corrections complete; coordinator acceptance follows the final commit.

## Files changed

- `scripts/check_sources.py`: enhance the existing `--strict` flag so full-text contract gaps, exact-version gaps, cross-file duplicate IDs, and depth conflicts are ERROR diagnostics. With `--online --strict`, a mismatched identifier remains an error even when another identifier matches or the returned title is generic. Default mode retains warning-based contract checks and exit policy.
- `tests/test_check_sources.py`: 24 deterministic tests for clean records, each required full-text field, explicit empty lists, exact versions (including legacy IDs and mixed pinned/unpinned references), DOI mismatch masking, ID/depth conflicts, malformed JSON, CLI routing and exit codes. Tests prohibit network calls and use temporary metadata caches and files.
- `research/redteam/citation-gate/TRIAGE.md`: dispositions for all 37 reproducible historical warnings, live-count reconciliation, the fourth formerly informational duplicate, and repair order.
- `research/redteam/citation-gate/{before-offline,before-strict,after-offline,after-strict,after-strict-all}.txt`: exact checker output and exit codes.
- `research/redteam/citation-gate/historical-warnings.json`: original checker replay against `a0c506f` knowledge records, 37 warnings.

No source registers, runner, grid files, seed sources, or other workers' worktrees were edited. Claude's six resumed literature workers and lane reviews were left intact. Coordinator claim/review transitions refresh the generated board; that shared snapshot is deliberately excluded from this change's commit.

## Findings and rationale

The existing `--strict` already returned nonzero for warnings. The gap was that the evidence violations remained warnings, and identical cross-file source copies were only INFO. Strict mode now reports those issues as errors; copied reading depths do not silently select the deepest reader. Strict online checking also rejects a bad DOI hidden by a matching arXiv title.

Two checker false positives needed correction: `arXiv:IDvN` does not have a word boundary before v, and an explicitly empty dependency/related-ID/question list is present data. Empty authors and absent fields still fail. This does not establish that a recorded empty list is truthful.

The brief's 39-warning baseline was not reproducible. First live output: 36 warnings; saved before output: 35 as Claude corrected records concurrently. Original-checker replays at `b3497f2`, `1a2eb46`, and `a0c506f` each produced 37. The triage preserves and dispositions those 37, including two warnings since corrected by Claude. Two unspecified warnings from the brief remain unidentified; no rows or source reads were invented to match a count.

## Initial verification (commit `60e5af3`)

- `python3 -m unittest discover -s tests -p test_check_sources.py -v`: 24 tests pass, offline.
- `python3 -m unittest discover -s tests -v`: all 36 tests pass, including existing runner/workboard checks.
- `python3 scripts/check_sources.py`: 17 files, 274 records; 0 errors, 11 warnings, 1 INFO; exit 0. Saved before: 0 errors, 35 warnings, 1 INFO; exit 0.
- `python3 scripts/check_sources.py --strict`: 15 errors, 0 warnings, 0 INFO; exit 1. Saved before: 0 errors, 35 warnings, 1 INFO; exit 1. This failure on existing evidence gaps is intentional.
- `python3 scripts/check_sources.py --strict knowledge research`: 21 files, 360 records; 74 errors; exit 1. Research/theory-map copies broaden the canonicalization backlog; knowledge-only checking is not full-project clearance.
- Historical Bisognano–Wichmann wrong-DOI case and correct-title/mixed-ID cases pass mocked tests. Metadata for the historical wrong DOI comes from the existing project Crossref cache. No network checks or dependency installs were run.

## Limitations and unresolved questions

These checks enforce the recorded evidence contract; they do not verify reading, theorem locators, source entailment, publication priority or philosophical conclusions. Existing title similarity/prefix heuristics remain. Strict lookup now resolves editions from source URLs and explicit version-field references, including `ID (vN)` and an edition-only `vN (date)` field for a single paper. Arbitrary prose mentioning a tool version is not accepted as a paper edition. When the cited edition title cannot be obtained, strict online mode fails on the resulting warning; it does not substitute the latest title. No live network verification was performed in this task.

Other lanes' records were intentionally not repaired. The five incomplete full-text records, three genuine unpinned versions and four duplicated IDs need owner/coordinator correction; depth downgrade is a proposal if the claimed extraction cannot be supported. The widened research scan also needs canonicalization review. The original snapshot above is preserved; the final review and validation are recorded below. The missing two identities behind the brief's quoted count of 39 remain a documented historical limitation, not invented triage entries.

## Review follow-up (2026-10-20)

The user requested continued review and then explicitly asked for subagents. Three reviewers received disjoint report directories within this claimed task: version/edition handling, evidence/input handling, and contract/report correspondence. Their original findings and fix dispositions are preserved under `review-versions/`, `review-evidence/`, and `review-contract/`. Reviewers edited only their assigned reports; the coordinator implemented and tested the corrections.

Corrections made after the initial commit:

- Reject whitespace-only scalar/list evidence and locators while preserving explicit empty lists for the three permitted fields.
- Tie strict edition pins to the actual paper ID, reject conflicting editions, group versioned/unversioned links to one paper, and keep unrelated tool versions from satisfying the paper-version requirement.
- Query editions pinned only in the version field during strict online validation; compare to the cited edition title and fail strict mode when only the latest title is available.
- Diagnose malformed IDs, title types and list/dict read depths rather than crashing. Later valid records remain checkable.

Both technical reviewers rechecked their reported defects after fixes and found no remaining blocker in their assigned scope. The contract reviewer verified the 37-to-37 historical warning/triage correspondence and set final checks, which the coordinator completed. These reviews check code and reporting; they are not independent source readings or evidence of scientific novelty.

Final saved validation:

- `review-tests.txt`: **39 checker tests pass**, network disabled and temporary caches only.
- `review-coordination-tests.txt`: **12 coordination tests pass**. Total focused checks: **51 tests**.
- `review-offline.txt`: 274 knowledge records, 0 errors / 11 warnings / 1 INFO, exit 0.
- `review-strict.txt`: 274 knowledge records, 15 errors, exit 1 as intended for the outstanding source-record gaps.
- `review-strict-all.txt`: 360 knowledge/research records, 74 errors, exit 1. No claim of a clean research corpus.

The before/after files without the `review-` prefix remain the initial implementation snapshot. Source records, other tasks' files, worktrees, runner and grid implementation were left untouched by this task. Only named task-owned files are included in the follow-up commit.
