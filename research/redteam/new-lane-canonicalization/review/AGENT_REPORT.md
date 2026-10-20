# Independent review of dual-archive reference integrity

## Scope

Reviewed `research/redteam/new-lane-canonicalization/check_references.py` against its two snapshot/manifest pairs, the prior accepted source-repair reference set, the new sector-conditioning and causal-set references, and the canonical-alias registry. Added only this report and `test_check_references.py` under the assigned review directory. All adversarial tests use temporary fixture roots; no source registers, snapshots, board state or scripts were changed.

## Fixture coverage

Ran:

```text
python3 -m unittest discover -s research/redteam/new-lane-canonicalization/review -v
Ran 8 tests; all passed.
```

Fixtures cover: both manifests and snapshot digests; an identical archived copy recurring across stages and provenance resolving it from either matching archive; a distinct removed lane copy in the second snapshot; incorrect direct target; global same-ID copies in separate files (must fail and list both paths); archive-byte and shared-seed tampering; prior depth/version/date/hash/revision/lane tampering; required alias registry and member edition/depth validation; and a shallow seed alias that stays abstract rather than inheriting the canonical full-text depth.

## Live-corpus result

`python3 research/redteam/new-lane-canonicalization/check_references.py --root .` now reports reference-integrity pass: **67 references** (63 from the first migration plus 4 from the second), 336 unique IDs, 8 alias groups, and no global duplicate IDs. Both archived record counts and snapshot digests validate; the unchanged seed hash validates against both manifests. The four new references point to the new-lane archive: two sector-conditioning and two causal-sets copies. The previous 63 references remain pointed to the first archive and resolve under the new checker.

The checker correctly fails if a current global duplicate is introduced, rather than merely listing it as non-blocking inventory debt. Alias validation matches each member's exact version and read depth to its current record. This is structural validation only; it does not certify alias identity or source claims.

## Disposition

No remaining reference/alias-integrity blocker found in the generalized checker under this review. The earlier snapshot-specific checker and its report remain unchanged; the new checker correctly handles the two archives and staged reference provenance. No source-semantic, edition-entailment, or scientific-claim audit is implied.
