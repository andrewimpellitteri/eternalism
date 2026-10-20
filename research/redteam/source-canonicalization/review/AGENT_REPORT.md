# Independent review of source canonicalization inventory

Task: `rt-source-canonicalization`
Review scope: independent live-tree recount, category and field-diff logic in `inventory.py`, and temporary-fixture tests. I did not edit `inventory.py`, source registers, the board, or shared caches.

## Independent recount

I counted `*sources.jsonl` files under `knowledge/` and `research/` with a standalone Python snippet that parsed the files directly and did not import `inventory.py`:

- 22 files, 365 records, 302 unique IDs.
- 59 IDs occur more than once; these account for 63 surplus copies.
- Three duplicated IDs have differing read-depth values.

The brief's 320 records / 257 unique IDs is stale for the current tree; its 59 duplicated IDs and three depth conflicts still match. The current inventory summary matches the independent counts exactly. The three conflicts are `frontier-qrf-indefinite-order-2022v3`, `frontier-qrf-operational-meaning-2026`, and `frontier-time-delocalization-2026`.

Current classification totals are 54 identical-copy, 1 stale-copy, 3 depth-superseding, and 1 unresolved true-conflict. The unresolved equal-depth knowledge conflict is `frontier-page-wootters-measurements-2023`: Frontier, ICO/QRF, and theory-map copies differ on authors, assumptions, conclusions, provenance, version, and related fields. The frozen review notes do not name this record among the three explicit deeper-lane supersessions, so a coordinator decision is appropriate. It should not be silently canonicalized by depth.

The script follows the documented default that a unique `knowledge/<lane>/sources.jsonl` copy is canonical over a research re-copy, and it uses the three explicit ICO/QRF supersessions listed in review notes. It retains all copies and exposes field differences in inventory output. The canonical-map output itself reports canonical path and superseded-copy locations, not their differing field values; a reviewer needing the disagreement must inspect inventory output as well.

## Fixture tests and finding

The owned test file is `test_inventory_review.py`. It uses only temporary directories and standard-library `unittest`, with no network, live record, cache, or board mutation. It covers provenance-annotated identical payloads, stale research copies, the explicit depth-supersession rule, unresolved equal-depth knowledge copies, missing-versus-null field differences, and the incoming-copy gate.

Command: `python3 -m unittest research/redteam/source-canonicalization/review/test_inventory_review.py -v`

Initial run found that a temporary incoming file with a new ID was labeled `review-new-id` but exited 0. The coordinator subsequently changed the incoming gate so nonempty source payloads always return nonzero pending review, and the rerun now passes all seven tests (`python3 -m unittest research/redteam/source-canonicalization/review/test_inventory_review.py`). The fixture therefore confirms the corrected behavior for both a new ID and an existing-ID conflict. Acceptance criterion: every nonempty incoming payload remains pending human review and returns nonzero; source payloads are never auto-cleared.

The incoming-gate fixture also reproduces the known stale-DOI propagation case. Git history confirms that `cc5344e` carried Stein 1968 DOI `10.2307/2023910` in the theory-map copy, while knowledge/foundations was corrected to `10.2307/2024512`; commit `1ee2847` replaced the stale theory-map copy. Given the corrected knowledge record and stale DOI as incoming, the fixture reports `hold-existing-id` and identifies `url` as changed. This catches the known case, although the test fixture stores those verified historical values directly rather than reading git objects at test runtime.

## Acceptance notes and limits

The classification logic preserves disagreements in the full inventory and refuses to select among equal-depth multi-knowledge copies. The explicit supersession list is a coordinator policy assertion, not an inference from read depth or a verified source reading. Current status and counts can change as workers integrate; re-run the independent count before acceptance. This review assesses local code and records only; it does not verify cited-paper claims or the source identifiers themselves.

## Final artifact cross-check

I compared `INVENTORY.md`, `MERGE_GATE.md`, coordinator `AGENT_REPORT.md`, `summary.json`, `independent-recount.json`, `canonical-map.jsonl`, and `historical-gate-results.json` against my independent recount and reran the seven stdlib fixture tests; all seven pass. The saved recount and summary agree at 22 registers, 365 records, 302 unique IDs, 59 duplicated IDs, and 63 surplus copies. The unresolved `frontier-page-wootters-measurements-2023` map entry has `canonical: null`, an empty `superseded_copies` array, and its three copies listed separately in `unresolved_copies`.

The historical Deasy replay holds the stale theory-map URL and reports the URL difference against the saved canonical `https://doi.org/10.1007/s11098-014-0398-5`; the stale input is `https://doi.org/10.1111/phc3.12294`. This is consistent with the saved knowledge register and notes. The artifacts describe a historical comparison and explicitly make no fresh DOI-resolution claim. The inventory, gate instructions, counts, map treatment, and historical replay are consistent on the checked points.
