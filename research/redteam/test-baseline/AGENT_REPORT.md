# rt-fix-live-contract-test

Done by the coordinator in the shared checkout on 2026-10-20.

## Files changed

- `tests/test_agents.py`: replaced the `len(agents.tasks()) == 11` contract with
  board-agnostic tests; added a board-size regression and a resume dry-run test.
- `scripts/agents.py` (coordinator edit, outside the worker brief): `tasks()` now
  rejects a row that lacks a required key with `ValueError("task X lacks owns")`
  instead of a bare `KeyError`.

## Before

```
$ python3 -m unittest discover -s tests
FAIL: test_live_task_graph_and_seed_contract
AssertionError: 48 != 11
Ran 8 tests ... FAILED (failures=1)
```

## After

```
$ python3 -m unittest discover -s tests -v
Ran 12 tests ... OK
```

## What each assertion protects

| Test | Regression it catches |
| --- | --- |
| `test_live_task_graph_is_valid` | Duplicate or invalid IDs, unsafe `owns`, unknown or cyclic deps (through `tasks()`); a row dropped between the file and the book; a row missing a field the runner indexes; a task that owns nothing. |
| `test_seed_sources_contract` | Duplicate seed IDs, non-https URLs, read-depth labels outside the five allowed, empty `limits`. |
| `test_worker_permission_contract` | A worker config that disables the user's search MCP or forbids webfetch. |
| `test_validation_is_board_size_agnostic` | A count hard-coded back in; a half-written row with no `owns`. |
| `test_resume_dry_run_keeps_previous_result` | `resume --dry-run` renaming `result.json`, which the first draft of `resume` did. |

## Why the `owns` check matters

On 2026-10-19 at about 20:34 UTC, six GLM supervisors heartbeated while the board
held red-team rows that did not yet have `owns`. `tasks()` raised `KeyError: 'owns'`
and every supervisor exited with `REFUSED: 'owns'`, leaving six claims with no
process. The runner now also tolerates a failed heartbeat (`beat()`).

## Remaining gaps (not fixed)

- `tasks()` builds the ID map before validating, so a row with no `id` still raises
  `KeyError` rather than `ValueError`.
- `priority` is not validated; it is display-only today.
- The live-board tests read the current `WORKBOARD.jsonl`, so a coordinator edit in
  progress can fail them. That is intended.
