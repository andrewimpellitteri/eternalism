# Read-only merge gate for source registers

The existing rule is `knowledge/REVIEW_NOTES.md:131-134`: an inherited ID uses its canonical knowledge-lane record on main; keep only new IDs from copied lane submissions unless an explicit coordinator review supersedes that record. The three ico-qrf depth supersessions are named in lines 179-183. Do not pick by majority, most recent timestamp, longest extraction, or highest claimed reading depth.

1. Preserve the incoming worktree and its original report. Check ownership and process state through the runner before any recovery action. This audit makes no coordination changes.
2. Regenerate the read-only inventory and compare the source hashes with the saved snapshot. A changed source tree requires a fresh inventory. `python3 research/redteam/source-canonicalization/inventory.py --format summary` prints the live frame; `--format inventory` and `--format canonical-map` print detailed JSONL to stdout. They do not write source files.
3. Pass each incoming source JSONL file to `python3 research/redteam/source-canonicalization/inventory.py --incoming PATH`. Every nonempty input returns nonzero pending review. Existing IDs are `hold-existing-id`; brand-new IDs are `review-new-id`. Zero is only an empty comparison, never scientific acceptance. Source ID references, not copied payloads, should survive integration for inherited sources. The advisory map covers all 302 snapshot IDs and explicitly leaves unresolved choices null.
4. For every held ID, examine all raw field diffs, especially URL/DOI/arXiv/version, authors, date, assumptions, conclusion, proof status and limits. Missing and explicit-null fields are different. Provenance-only annotations do not change the source payload, but do not justify keeping another copied source register record. A proposed update to the canonical lane requires explicit coordinator/source-owner review rather than automatic rejection or overwrite.
5. Resolve the equal-depth measurement-paper conflict against the primary header and extracted claims. For the three approved deeper ico-qrf records, preserve which reader inspected which version and which other reader only screened its abstract. Never reinterpret an earlier reader's shallow record as a deep reading. A canonical record may carry the later extraction while its provenance retains both depths.
6. For new IDs, verify the identifier against the actual primary landing page and pin the edition read. Review full-text fields and locators against the source; the gate does not establish reading or entailment. Check aliases under different IDs separately: this script groups identical IDs and does not automatically prove same-paper identity across different IDs.
7. After the owning coordinator makes source edits in a separate authorized change, run `python3 scripts/check_sources.py --strict knowledge research`. Existing failures must be resolved or explicitly retained as blockers; passing this schema/identifier check still does not certify theorem truth, physical novelty or ontology. This audit leaves all source registers untouched and does not claim the current strict scan is green.

## Historical replay: stale DOI propagation

`historical-stale-input.jsonl` contains the actual three theory-map records from commit `cc5344e`, before the canonical corrections were propagated. `historical-gate-results.json` is the current inventory comparator's output; all three return `hold-existing-id` and an explicit URL diff:

| ID | Incoming stale DOI | Canonical DOI |
|---|---|---|
| found-stein-1968 | 10.2307/2023910 | 10.2307/2024512 |
| found-malament-1977 | 10.1111/j.1933-1592.1977.tb01280.x | 10.2307/2214766 |
| found-deasy-2015 | 10.1111/phc3.12294 | 10.1007/s11098-014-0398-5 |

Reproduce with `python3 research/redteam/source-canonicalization/inventory.py --incoming research/redteam/source-canonicalization/historical-stale-input.jsonl`; exit 1 is expected. This demonstrates stale-copy detection from Git history, not a fresh DOI-resolution experiment. The original error/correction evidence is recorded in `knowledge/REVIEW_NOTES.md:110-134`.
