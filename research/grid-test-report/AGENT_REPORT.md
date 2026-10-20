# grid-regression-tests

Done by the Claude coordinator on 2026-10-20 in the shared checkout. The
coordinator also owns `scripts/grid.py`, so the fixes are in the same change.

## Files

- `tests/test_grid.py`: 37 standard-library tests. Each runs in a temporary root
  with patched `ROOT`, `AXES` and `BOARD`; no live board, results, claims,
  network or model calls.
- `tests/fixtures/grid/axes.json`: 3 physics, 2 bridges, 2 ontologies, 2 moves.
- `tests/fixtures/grid/controls.jsonl`: five scientific controls drawn from
  `research/grid-review/controls.jsonl`, each with domain, witness or argument,
  proposed disposition and review limits.
- `scripts/grid.py`: gate fixes listed below.
- `before.txt`, `after.txt`: verbatim `-v` output against the old and fixed runner.

## Result

```
$ python3 -m unittest discover -s tests -p test_grid.py -v
before: Ran 37 tests  FAILED (failures=20, errors=2, skipped=1)
after:  Ran 37 tests  OK (skipped=1)
$ python3 -m unittest discover -s tests
after:  Ran 49 tests  OK (skipped=1)
```

## Defects found in the old runner, and the fix

| Defect (failing tests before) | Fix |
|---|---|
| Invalid records promoted: `cells()` discarded `results()` problems (`test_invalid_advance_is_not_promoted`) | `results()` fails closed; only records with no problem enter the result map. |
| Shape barely checked: empty predecessors and queries passed; no type, move, falsifier or read-depth checks (`test_minimal_malformed_advance_rejected`, `test_each_required_advance_field_enforced`, `test_field_types_enforced`, `test_predecessor_content_enforced`) | `contract_problems()` checks types, nonempty content, `read_depth` enum, `move` against axes, and `falsifier`. |
| Any truthy `kill_reason` accepted; invalid kills counted as coverage (`test_kill_reason_enum_enforced`, `test_invalid_kill_is_not_coverage`) | Enum from CONTRACT.md enforced; invalid kills are left out of status tallies. |
| Unknown cell IDs accepted (`test_unknown_cell_id_rejected`) | `cell_problem()` accepts only IDs the runner can generate from the axes, including ordered T1 pairs. |
| Non-object JSON lines crashed `results()` (`test_malformed_and_non_object_lines_reported_not_fatal`) | Reported as problems. |
| Unassigned records, or records written in another batch's directory, promoted (`test_unassigned_cell_is_not_promoted`, `test_result_outside_assigned_batch_is_not_promoted`) | A record counts only from `grid/results/<assigned task>/`. |
| Conflicting duplicates silently resolved by the most conservative verdict, with `recs[0]` supplying the claim (`test_conflicting_claims_quarantined`, `test_conflicting_verdicts_reported`) | Identical copies dedupe; records differing in verdict, claim or kill reason are quarantined and reported. |
| Orphan, unassigned or stale adversary survivors expanded (`test_orphan_survivor_not_expanded`, `test_unassigned_survivor_not_expanded`, `test_stale_survivor_claim_not_expanded`, `test_survivor_of_invalidated_parent_not_expanded`, `test_survivor_of_killed_parent_not_expanded`) | An `A-` record needs a valid `advance` parent with the identical claim; an `S2-` record needs a valid `survive` parent. The adversary brief now says to copy the claim exactly. |
| S2 records re-entered the adversary stage (`test_expansion_cells_never_reenter_adversary`) | `adv` draws only from `S1-`/`T1-`; S2 is terminal. |
| `--batch 0` crashed and negative batches misbehaved (`test_invalid_batch_size_rejected_without_writing`) | argparse rejects batches below 1 before any write. |
| Duplicate assignments silently overwrote; any `grid-*` task ID (e.g. `grid-regression-tests`) was parsed for cells (`test_duplicate_assignment_reported`, `test_non_grid_task_with_grid_prefix_is_not_an_assignment`) | Only `grid-(s1|t1|adv|s2)-NN` tasks are parsed; duplicates are reported by `status`. |

## Unresolved contract choices (for rt-grid-kill-criteria)

1. **S2 cardinality.** CONTRACT.md names `S2-…-Oz-Mw` (ontology × move, 54 per
   survivor with live axes); README.md and the runner use ontology only (9).
   `test_s2_cardinality_matches_agreed_contract` is skipped with this reason
   rather than fixing a count. The validator currently accepts only the runner's form.
2. **Stage verdicts.** CONTRACT.md lists `kill/hold/advance`; the adversary brief
   says `kill/survive`, and the runner also accepts `hold` for `A-` cells. Tests
   assert the runner's current sets.
3. **Exact claim copying.** Requiring the adversary to copy the parent claim
   verbatim is a coordinator choice. It blocks stale survivors but also blocks
   an adversary that narrows the claim; a narrowed claim would need a new cell.
4. **Transfer direction.** T1 IDs are unordered pairs (`Pa < Pb`); a record does
   not yet state source → target.
5. **Kill on an orphan.** An `A-` kill without a valid parent is also left out
   and reported, which is conservative.

## Known gaps left

- `--append` is not a locked transaction; two coordinators generating batches at
  once could assign a cell twice. `status` now reports that case but does not
  prevent it.
- Validation is shape only. A shape-valid record can still cite a source that
  does not say what it claims; `test_gate_checks_shape_not_bridge_quality`
  documents that an unargued leap passes the same gate as a defended bridge.

## Scientific controls

The three mechanically checked controls (observation vs. intervention, finite
witness vs. universal claim, completed paths vs. determinism) verify only their
finite witnesses in the stated domain. The defended-bridge and unargued-leap
dispositions are proposals for independent human review. No test certifies
entailment, priority, novelty or metaphysical truth.

## Update after rt-grid-kill-criteria (2026-10-20)

Choices 1 and 2 above are now settled in `grid/CONTRACT.md`: S2 is
`S2-<cell>-Oz` (one cell per ontology, terminal), and adversary cells use
`kill/hold/survive`. `refuted` was added as a kill reason. The skipped
cardinality test is replaced by `test_s2_cardinality_is_one_cell_per_ontology`.
Choices 3–5 remain as stated.
