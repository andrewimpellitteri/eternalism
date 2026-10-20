# Sector/frontier duplicate-ID canonicalization

## Decision

Both duplicate IDs name the same work and the same arXiv version in the frontier and sector-conditioning registers. I retained the established `knowledge/frontier/sources.jsonl` records as canonical so existing frontier and theory-map references stay stable. The two sector-conditioning payloads were removed from that lane and replaced with explicit inherited-source references to the frontier records. This is a canonical-location decision, not a judgment that one lane's reading is more authoritative by depth.

The full-text passes are both recorded at the same `full-text` depth. Their scopes differ: the frontier records describe the initial source readings, while sector-conditioning re-read the relativistic trinity by sections and Example 30 of the beyond-subsystems paper. I appended separately attributed `reading_history` entries to each canonical record, including those exact scopes and the sector worker's proof/normalization limits. The original snapshots and extracted source findings remain unchanged.

## Exact changes

- `knowledge/frontier/sources.jsonl`: added a `reading_history` array to `frontier-qrf-beyond-subsystems-2026` and `frontier-relativistic-trinity-2020v1`. Each retains the original frontier reader, depth, version, date and snapshot row/hash. The second entry attributes the 2026-10-20 sector-conditioning re-read and its locators. For Example 30, it preserves the report that the instrument-based single isometry jointly encodes the two sectors in orthogonal clock states, while the example lies outside the paper's finite-dimensional/compact-group framework, ignores normalization factors, and does not preserve cross-sector coherence in the output. For the relativistic trinity, it preserves the sector pass's section-focused re-read, publisher-HTML wording comparisons, main findings about Eq. (31)'s observable scope and footnote 16, and limits (proofs not re-derived; appendices unread).
- `knowledge/sector-conditioning/sources.jsonl`: removed only those two duplicated source payloads; the seven other lane records remain.
- `knowledge/sector-conditioning/source-refs.jsonl`: added two references to `knowledge/frontier/sources.jsonl`, with policy rationale, bounded-reading limits, and each removed row's historical reader/depth/version/date/path/line/hash.
- `research/redteam/new-lane-canonicalization/sector/AGENT_REPORT.md`: this decision and verification record.

## Evidence and verification

The two pairs have matching titles, source URLs, and arXiv version identifiers (`2607.24976v1` and `2007.00580v1`). Both lane copies were marked full-text; neither was selected by a max-depth or majority rule. The canonical locations were retained because they are the existing frontier homes referenced by related-source links and theory-map material. The sector lane's distinct reading work remains attributed rather than merged into the original reader's scope.

The frozen `before-records.jsonl` and `before-manifest.json` at revision `c480ff1ce0e9d4f01e5e8f5bdef4af86a7bc3326` were not changed. I verified the snapshot digest, and for each new reference verified that its archived path/line resolves to the removed source record, its normalized sorted-key JSON SHA-256 matches, and its `read_depth`, `version`, and `checked_on` match the archived row. Both canonical targets resolve and both removed IDs remain present there. The sector-owned source records pass:

```text
python3 scripts/check_sources.py --strict knowledge/frontier/sources.jsonl knowledge/sector-conditioning/sources.jsonl
2 files, 27 records: 0 errors, 0 warnings, 0 info
```

The whole-project strict source check also passed after the concurrent lane integrations visible at check time:

```text
python3 scripts/check_sources.py --strict knowledge research
25 files, 336 records: 0 errors, 0 warnings, 0 info
```

## Limits

This integration records prior reading claims and does not independently re-read the papers, validate their proofs, or upgrade either original full-text record. The canonical source records retain their original prose summaries; the additional sector evidence is explicitly scoped in `reading_history` and remains in `knowledge/sector-conditioning/extraction.md`. I did not edit the extraction, any other lane, source aliases, checker, coordinator files or board, and made no commit. No external source lookup or dependency install was performed in this reference-only task.
