# Agent report: infrastructure red team (coordination and idea-grid)

24 October 2026. Head-session adversarial audit of `scripts/agents.py`,
`scripts/grid.py`, `scripts/check_sources.py`, `scripts/check_authors.py`,
`tools/gh-gates/check_gates.py` and the test suite, requested directly by the
user ("fix any bugs look for errors red team").

## Files changed

- `scripts/agents.py`
  1. Stale-claim crash (availability): a coordination-state record for a task
     ID no longer on `WORKBOARD.jsonl` made every subsequent `claim`/`launch`
     crash with `KeyError: '<retired-task>'` (a cryptic REFUSED at CLI level)
     until state was hand-edited. `assert_claimable` now skips board-unknown
     IDs; live claims still guard overlap.
  2. `owns` validation accepted `./escape`, `a//b`, `a/./b`, `//share/x`,
     `a/b//` — normalized to ordinary paths, so not exploitable, but the
     check exists to be fail-closed. Now rejected. All 117 live tasks
     validate under the stricter rule.
  3. `render_board` wrote `WORKBOARD.md` non-atomically while up to six
     workers heartbeat; concurrent writers could tear the generated file.
     New `atomic_text` helper (temp file + `os.replace`), matching the
     existing `atomic_json` pattern.
- `tests/test_agents.py`: regression tests for all three (owns spellings;
  stale-retired-claim neither crashes nor blocks live overlap guards;
  render_board output). Suite: 104 tests, green.
- `experiments/extensions/countermodel.py` (from the later math pass):
  `n_representatives` returned |Aut| = 2^j, contradicting the N(H)
  definition in `research/creative/COVARIANT_RESULT.md` (labelled
  representatives, n!/|Aut|). Now N(H_j) = (3j)!/2^j (3 and 180 for
  j = 1, 2); printed products and kappa values updated (0.375 vs 0.703125;
  kappa = 8/3 vs 1024/180). Conclusion unchanged: no common kappa under
  either convention, so the countermodel survives.

## Evidence

Adversarial probe (kept outside the repo, in the session temp directory):
~45 cases against agents.py and grid.py. All refusal paths held (file inside
claimed dir, duplicate IDs, unsafe paths, double claim, wrong-agent release,
review-state machine, unknown task, accept-time out-of-scope rename via
`git mv`, unassigned/wrong-batch/conflicting/orphan/reworded grid records,
bogus moves, thin evidence, malformed JSON lines). The three agent bugs above
were found by this probe; the initial four grid "failures" were probe bugs
(fake axis IDs, incomplete fixture boards) — the grid gates are fail-closed.

## Checks

- 104 tests in `tests/` green; `check_certificate.sh` chain green
  (reproduction, exact Q(√2) certificate, Dirac countermodel, boundary).
- `check_sources.py` offline: 324 records, 0 errors, 0 warnings.
- All three experiment programs run; formulations.py cross-checks against
  the independent replication output: agree.
- `scripts/agents.py validate` / `list` / `sync` green on the live board;
  `sync` output byte-identical to the committed WORKBOARD.md.

## Limitations

- Not fuzzed: events.jsonl parsing under partial writes (fail-open edge in
  scan_events is bounded by process exit semantics).
- The porcelain rename edge in `accept` fails closed (a legitimate owned-file
  rename is refused); left as is by design.
- `check_authors.py` opens files without explicit encoding; harmless on this
  machine, inconsistent with check_sources.py. Not changed.

## Unresolved questions

- Whether a stale claimed record for a retired task should also surface a
  warning in `status` output (currently visible only as a claimed row).
