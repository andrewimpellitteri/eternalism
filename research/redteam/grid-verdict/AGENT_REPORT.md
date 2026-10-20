# rt-grid-kill-criteria

Written by the Claude coordinator on 2026-10-20 after `grid-regression-tests`
and `grid-adversarial-design` were accepted.

## Independence caveat

The same coordinator wrote the gate fixes in 9d821f3 and this verdict, so this is
not an independent red-team review of those fixes. An independent reader should
re-run the control dry run before the pilot.

## Files

- `CRITERIA.md`: claim typing; per-stage kill/hold/advance/survive evidence
  requirements; dry run of the eight controls in `research/grid-review/controls.jsonl`;
  design gaps G1–G5; what is undecidable by design.
- `GO_NO_GO.md`: no-go for bulk assignment; go for a 12-cell S1 pilot once
  G1 and G2 are fixed; caps and audit triggers.

## Control results under these criteria

| Control | Outcome |
|---|---|
| 01, 02 | Pass, and enforced mechanically by the runner (tests named in CRITERIA.md). |
| 04, 05 | Pass; reviewer-enforced. |
| 03, 07, 08 | Pass on disposition, but CONTRACT.md has no kill reason for a refuted claim (G1), so a correct worker cannot record it faithfully. |
| 06 | Pass under these criteria; **false kill under CONTRACT.md's literal `ontology-leap` wording** (G2). |

No control was forced. The undecidable parts (bridge justification, truthmaker
adequacy, priority, source correspondence) are listed in CRITERIA.md.

## Not done

- Did not edit `grid/`, `scripts/grid.py` or the other grid tasks' files, per the brief.
- Did not assign or launch any grid cell.
- The pilot thresholds are operating heuristics, not estimates of the literature.
