# Source canonicalization — coordinator report

Task: `rt-source-canonicalization`; claim `codex-source-canonicalization`. Date: 2026-10-20.

## Delivered

`inventory.py` is a standard-library read-only inventory/compare script. It prints JSON/JSONL to stdout and never edits source records or coordination state. `summary.json` freezes input hashes and Git cutoff; `duplicate-inventory.jsonl` records every copy and raw field difference, including absence vs null. `canonical-map.jsonl` names canonical locations/depths and superseded copies for all snapshot IDs, while leaving unresolved copies explicitly separate. `INVENTORY.md` is the readable table; `MERGE_GATE.md` gives executable checks and recovery/integration limits. Historical stale inputs and gate results are saved separately. No checker patch is proposed or applied.

## Counts and classification

Current snapshot: 22 registers, 365 records, 302 unique IDs, 59 duplicated IDs, 63 surplus copies and 3 depth conflicts. Compared with the brief's 320/257, records and unique IDs each increased by 45; duplicate/depth-conflict counts match. Claude integrated five relational-Markov records during this run, explaining the increase from the earlier citation-gate 360/297 snapshot.

Categories: 54 identical source payloads after excluding two provenance annotations, 1 stale research copy, 3 explicitly approved deeper ico-qrf supersessions, 1 unresolved equal-depth knowledge conflict. Raw annotation differences remain visible. Canonical choices follow the named coordinator rule, not reader votes or generic maximum-depth selection; they are not scientific correctness certifications.

## Independent review, checks and evidence

A native reviewer independently recounted raw JSON without importing the inventory and matched the counts. Seven temporary-fixture tests cover annotation-only copies, stale identifiers, explicit supersession, unresolved conflicts, missing vs null and incoming holds. The reviewer exposed a new-ID gate returning zero despite requiring review; the coordinator corrected it, and all seven tests now pass. Every nonempty incoming payload is pending review, including new IDs. Zero is an empty comparison, not acceptance.

Historical replay uses actual theory-map records from commit `cc5344e`, not invented DOI fixtures. The stale Stein, Malament and Deasy records are all held and their URL differences exposed. `historical-gate-results.json` gives the complete evidence. This is comparison against corrected canonical records, not a fresh online DOI audit.

The one unresolved ID is `frontier-page-wootters-measurements-2023`. Parallel primary-text checking resolves the author/date discrepancy in favor of the ico-qrf fields; the script still flags the equal-depth record decision rather than silently discarding extracted disagreement. The owning coordinator must choose a canonical record after field review and apply source corrections separately.

## Limits and ownership

This task produces the promised inventory/map/checklist; it does not delete copies, rewrite sources, update claimed reader depths, edit the checker, or adjudicate physical truth. Same-paper aliases with different IDs are outside the automated ID grouping. The full-text spotcheck separately identifies RC-4 aliases and primary-text issues. No source register, shared seed, runner, paper, grid or other task's worktree was changed. No credentials, dependency installs, network lookups or large runs were used by the inventory script. The current strict source scan remains blocked by source-record issues; this report does not claim a green corpus.

Status: reviewed implementation and evidence ready for coordinator integration and acceptance after the named-file commit.
