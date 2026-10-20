# grid-adversarial-design

Written by the Claude coordinator on 2026-10-20. The Codex session that held the
claim (`codex-grid-review`) left its outputs unchanged after 2026-10-19 20:17
UTC and never wrote a report; the user asked the coordinator to finish open
blocking work.

## Files

- `HANDOFF.md`: Codex → Claude work split and eight design suggestions.
- `DESIGN_REVIEW.md`: seven runner gate defects, four contract choices to
  settle, gate improvements and a gold-label audit.
- `controls.jsonl`: eight synthetic controls (schema, provenance, mathematical,
  scope, circularity, false-kill, gold-label audit, determinism).

## Coordinator checks

- Reproduced the headline defect read-only:
  `contract_problems()` from `scripts/grid.py` (unchanged since 34f0357)
  returns `[]` for the malformed record in `DESIGN_REVIEW.md`.
- Checked the witnesses for controls 03 (passive equality without
  interventional equality) and 08 (completed paths with an indeterministic
  continuation). Both are correct counterexamples to the stated universal claims.
- Control 06 is a false-kill case and control 07 audits an agent-supplied gold
  label, so the "false advances and false kills" condition is met.

## Limitations

- The other six runner defects are taken from the review and were not each
  reproduced here. `grid-regression-tests` is the task that turns them into
  failing tests.
- The four contract choices in `DESIGN_REVIEW.md` (stage verdict sets,
  expansion cardinality, transfer direction, source-blind review) are still
  open. `rt-grid-kill-criteria` should settle them before tests fix expectations.
- Controls are synthetic calibration cases, not research results.
