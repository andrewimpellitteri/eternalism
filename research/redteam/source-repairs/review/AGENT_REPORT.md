# Independent reference-migration review — final check

## Scope and files

Reviewed `integrate_references.py`, the updated `check_references.py`, `before-records.jsonl` and `before-manifest.json`, live source references, and `knowledge/canonical-aliases.jsonl`. Added/updated only this review directory, specifically `test_reference_integrity.py` and this report. The migration script ran only against a temporary fixture; no live source register or coordination state was changed.

## Disposition of prior findings

The three false-pass gaps from the first review are fixed in the current checker and covered by regression tests:

- **Deleted lane copy without its reference:** the checker now requires removed archived `(path, id)` copies to have reference coverage keyed to the original archive path/line. Fixture deletes the frontier ref while the ID remains in the canonical ico-qrf register; the checker now fails with `Removed copy lacks preserved reference`.
- **Missing alias registry:** absence of `knowledge/canonical-aliases.jsonl` now fails with `Missing curated alias registry`. The live registry contains eight groups, including the Brading and Putnam work IDs. Supplied aliases are checked against actual member records for exact version and read depth; invalid canonical membership and version/depth drift fail in fixture tests.
- **Archive/ref coordinated tampering:** `before-manifest.json` now pins the archive SHA-256. A fixture that changes an archived record and recomputes the reference metadata/hash now fails with `Archived snapshot digest mismatch`.

No remaining checker blocker found in this scoped review. Global cross-register duplicate IDs remain a separate, visible status and are not part of the checker’s reference-integrity pass.

## Checks

Ran:

```text
python3 -m unittest discover -s research/redteam/source-repairs/review -v
Ran 13 tests; all passed.
```

The fixtures cover migration output and canonical resolution; absent registry; valid/broken aliases; missing/wrong canonical target; lost IDs; removed-copy reference coverage; seed integrity; prior read-depth/version/hash tampering; archive digest tampering; and same-file duplicate IDs.

Live archive audit confirms every removed source copy in these migrated lanes has an exact path/line/ID/hash reference: frontier 4/4 and theory-map 59/59. Ico-qrf retains all 18 pre-migration records. The live seed SHA-256 matches `before-manifest.json`, and `before-records.jsonl` SHA-256 matches its manifest pin.

Alias metadata does not upgrade historical member depth. Every registry member's edition and depth matches its live record. Specifically, the Brading seed lead remains abstract with no version, and `phil-mctaggart` remains discovery depth; its bounded full-text passage check is recorded separately as an additional reading.

At final check, `check_references.py --root .` reports reference-integrity pass, 63 references, 340 records, 336 unique IDs, and eight alias groups. It still visibly reports four global duplicate IDs: `frontier-qrf-beyond-subsystems-2026` and `frontier-relativistic-trinity-2020v1` across frontier/sector-conditioning, plus `cs-brightwell-2003-observables` and `cs-surya-zalel-2020` across causal-sets/CSG-quantum. They are not cleared by the reference checker.

The migration fixture confirms the one-time migration removes a copied payload, creates an explicit reference, and preserves old version, depth, reader provenance and content hash. The live migration was not rerun because its one-time guard correctly refuses a second application.

## Limits

This review tests reference and alias structure, not source identity or semantic correctness. The checker’s global duplicate output remains a report requiring lane-owner review; it does not assert those duplicates are semantically equivalent.
