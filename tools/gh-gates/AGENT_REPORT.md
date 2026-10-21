# Agent report: gh-gate-sync

Sole-worker tool, 2026-10-21. Files: `check_gates.py`, `gates.json`, `README.md`,
this report.

## Result

A read-only status checker for the five external gates. It maps each issue to
its local task IDs and prints state, labels and blocked status via
`gh issue view --json`. It never writes to GitHub and does not print
credentials.

## Checks

- `python3 tools/gh-gates/check_gates.py` — five rows; #5 blocked; exit 0.
- `--json` output parsed correctly.
- `env PATH=/usr/bin:/bin python3 ...` — clear "gh CLI not found" error, exit 2.
- `gates.json` is valid JSON; issue numbers match `GATES.md`.

## Limits

- The checker is read-only by construction; it cannot enforce gate closure.
- The mapping is manual and must be updated when gates or task IDs change.
- It requires network/auth to actually query issues; offline use fails cleanly.
- No runner or workboard edits.
