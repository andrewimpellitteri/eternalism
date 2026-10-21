# Coordinator report: refocus-selection-integration

Takeover of a stopped coordinator. The prior holder `codex-refocus-coordinator`
died locally; the user recovered its committed audits (`4823f0c`, `8821700`)
and uncommitted edits (`b308ee3`) to branch `refocus-recovery`. Those outputs
are preserved unchanged except where listed below.

## Files changed

- `research/qbc-holonomy/RESULT.md`: erratum block plus in-place corrections
  (commutative ≠ scalar direct sum; norm-GC ≠ vector GC; pure-Pauli ansatz ≠
  2×2 no-go; check scope). Taken from the correspondence lane's
  `CORRECTIONS.md`.
- `research/refocus-2026-10-21/coordinator/SELECTION.md`: decision.
- `research/refocus-2026-10-21/coordinator/AGENT_REPORT.md`: this file.
- Reviewed and kept the recovered edits to `research/qbc-holonomy/check.py`,
  `research/rank-renewal-convergence/RESULT.md` and `check_weighted.py`.

## Checks run

- `python3 research/rank-renewal-convergence/check_weighted.py`: pass.
- `python3 research/refocus-2026-10-21/rank-audit/check_bipartite_bound.py`: pass.
- `python3 research/refocus-2026-10-21/cpobc-reproduction/check.py`: pass.
- `python3 research/qbc-holonomy/check.py`: pass (scalar markers only).
- `python3 scripts/check_sources.py --strict research/refocus-2026-10-21`: 0 errors.
- `python3 scripts/agents.py validate`: pass.

## Limitations

Priority for either target is not established. The posts-algebra framework is
imported. No CAS run. Finite checks corroborate stated finite identities only.
