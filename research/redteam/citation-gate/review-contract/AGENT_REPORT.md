# Independent review — citation gate contract

Task: `rt-citation-gate-hardening`
Reviewed commit: `60e5af3` plus the uncommitted checker/test edits visible during review
Date: 2026-10-20
Review scope: brief compliance, local record-contract correspondence, saved baseline/after outputs, and reporting accuracy. No external research or live lookups were performed.

## Findings

- **Historical warning reconciliation is internally consistent, with a documented baseline gap.** `historical-warnings.json` has 37 entries and the triage table has 37 numbered rows. Each historical ID/message has a corresponding row. The saved current-before run has 35 warnings (17 files, 274 records); the saved default-after run has 11 warnings; strict-after has 15 errors. The report and triage explicitly say the brief's 39-warning count could not be reproduced and do not invent two missing identities. Treat 39 as an unreconciled historical claim, not as a demonstrated omission from the 37-row table.
- **The committed triage dispositions are reasonable proposals, not source verification.** The `acceptable-with-reason` rows rely on fields/versions visible in the current lane records; they explain the old parser's false warnings for explicit empty lists and ID-attached `vN` spellings. The `fix-record` rows retain missing metadata/version and copied-depth conflicts for lane owners. The report correctly says the five incomplete full-text records and three unpinned records remain unresolved. This satisfies the brief's proposal-only constraint and does not imply the sources were checked.
- **The saved before/after outputs are a point-in-time snapshot.** Their warning lists and counts agree with the report. They predate the current working-tree edits; future claims about the edited checker or test count should be added as a dated follow-up rather than silently attributed to commit `60e5af3`.
- **The committed checker had two reproducible contract-edge defects now addressed by the visible working patch.** Its `r.get(...)` truthiness checks treated whitespace-only strings/list items as present, and the arXiv version check did not reliably associate a version-field pin with the paper ID (or distinguish an unrelated standalone `vN`). The current patch adds recursive content checks and groups versioned arXiv references by base ID; it also feeds exact version-field IDs into strict online validation and detects conflicting editions. Keep the final report tied to this current patch and confirm corresponding tests cover whitespace-only scalar/list content, legacy IDs, DOI-linked records with an arXiv version field, multiple papers, and conflicting pins.
- **The requested offline fixtures and scope are present in the committed change.** The test file uses temporary source files and mocks online metadata; the recorded test set covers the known DOI/title mismatch, missing full-text fields, duplicate IDs, depth conflicts, and a clean record. Commit `60e5af3` changes only the checker, its tests, and citation-gate artifacts. The visible uncommitted changes to `scripts/check_sources.py` and `tests/test_check_sources.py` remain within the task's allowed paths. Separate root-owned workboard/grid edits are outside this review and should not be attributed to this task.

## Acceptance criteria

1. Run the brief's offline unittest command after the current patch is settled; verify it passes with network disabled. Record the final test count and commit/state clearly.
2. Run default and strict offline checks on the live knowledge tree and save fresh outputs. Keep the old snapshot labeled historical; reconcile the new error/warning counts with the updated dispositions.
3. Demonstrate strict rejection of the historical wrong DOI/title fixture and the missing-full-text fixture, and strict acceptance of a clean fixture. Ensure title matching cannot let a second identifier or generic title hide the wrong DOI.
4. Ensure strict edition resolution checks the cited arXiv edition from URL or version text, rejects conflicting edition pins and unrelated `vN` tokens, and keeps default behavior backward compatible.
5. Confirm every recorded historical warning remains represented by a named triage disposition, while the unexplained difference between the brief's 39 and the reproducible 37 is still stated plainly. No other lane's `sources.jsonl` should be changed as part of this task.

## Limits

This was a repository-level audit of saved artifacts and current code, not a fresh run of the checker, a DOI/arXiv lookup, or verification that any source record's substantive claims are true. The final validation criteria above remain for the coordinator to complete after the in-progress patch is settled.
