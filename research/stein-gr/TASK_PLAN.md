# Stein–GR delegation plan

25 October 2026. The authoritative tasks are in `WORKBOARD.jsonl`; regenerate
`WORKBOARD.md` with `python3 scripts/agents.py sync`. These are new tasks,
not claims that earlier author work or informal reviews never happened.
Workers must inspect current sources and prior reports before repeating work.

## Execution order

Start with three independent lanes: **core repairs, gluing audit, priority
audit**. These address correctness and whether the exact result is worth
pursuing. The other four first-wave lanes can run alongside them when slots
are available. The runner's default concurrency is six; seven open lanes are
not an instruction to launch seven workers simultaneously.

| Task | Concrete output | Distinct question |
|---|---|---|
| `stein-core-repairs` | Exact replacement passages in `tasks/core-repairs/PATCH.md` | Have strict/reflexive chronology and every first-exit case been repaired consistently? |
| `stein-gluing-audit` | Independent proof audit in `tasks/gluing-audit/` | Do the two domains really coincide, and are both transfer embeddings legitimate? |
| `stein-priority-audit` | Source comparisons and bounded novelty verdict in `tasks/priority-audit/` | Is this exact all-spacetime theorem already known, and what does it add? |
| `stein-null-boundary-audit` | Proof and explicit mixed-curvature example in `tasks/null-boundary/` | Is the residual classification exact, and does its non-uniqueness witness exist as claimed? |
| `stein-causet-audit` | Analytic proof, small witness checks and negative control in `tasks/causet-audit/` | Does the convex-embedding poset theorem hold, and how does it differ from the published weaker claim? |
| `stein-energy-rigidity-audit` | Rigidity/source audit in `tasks/energy-rigidity/` | Which energy-condition obstructions are established, and what extension actually remains open? |
| `stein-interpretation-audit` | Passage-level claim map in `tasks/interpretation/` | What follows from metric-only covariance, and what requires extra physical or philosophical premises? |

All paths in the table are relative to `research/stein-gr/`. Every lane owns
only its own directory and must provide `AGENT_REPORT.md`. The core-repair
worker proposes a patch; the gluing reviewer independently verifies the
geometry rather than acting as a second manuscript editor. A refutation,
a narrowed result, or a verified finding that the author already fixed the
problem is a useful submission.

## Integration and review gates

`stein-paper-integration` depends on **all seven** first-wave tasks. It is
reserved for an explicitly assigned coordinator after the current manuscript
author has finished editing. It owns only the named manuscript/build files,
readiness and verification records, and `integration/`; it does not own the
workers' outputs. Read and independently assess every submission before
accepting it. A successful worker exit is not an acceptance decision.

`stein-final-referee` depends on integrated source. Give it a frozen source
hash and, where feasible, a reviewer who did not write the repairs. Its
verdict must separate mathematical correctness, bounded priority confidence
and physical interpretation. Compilation alone passes none of these gates.

`stein-energy-pocket-probe` depends on the rigidity audit and final referee.
It is a separate, bounded research extension. It must not hold the current
kinematic paper hostage to an unrestricted Einstein-equation gluing problem.
Choose one named restricted ansatz and accept an honest obstruction as a
result. There is no authorization here to publish or submit either paper.

## Launch and ownership rules

- First inspect `python3 scripts/agents.py status` and active claims. The
  existing `refocus-selection-integration` claim is unrelated; preserve it.
- Commit the new task definitions and required input files before isolated
  launches. Root PDFs that remain untracked are not copied into a worktree;
  obtain the public primary source directly or have the coordinator prepare
  a permitted source snapshot. Never silently assume it is present.
- Use `python3 scripts/agents.py launch` for OpenCode workers. With unrelated
  unfinished work present, the documented `--from-committed-head` option
  preserves it and pins a committed baseline. Start with a dry run.
- For explicitly assigned native workers, the coordinator claims the named
  task first and gives the exact disjoint output directory. Do not start a
  second writer under the same claim. Native execution has the same report
  and review obligations.
- Do not launch the integration task while Claude or another author is
  editing `main.tex` or `DRAFT.md`, even if it has become dependency-ready.
- Workers never edit the workboard, shared manuscripts, runner or other
  lanes. The coordinator integrates reviewed changes and performs board
  transitions. Claims are not released merely because a process is quiet.

## Acceptance standard

Each brief specifies its falsifiers and deliverables. Across all lanes:
pin the exact source revision and primary-source versions; label read depth;
separate analytic proof from finite corroboration; identify additional
structure and the off-shell category assumption; preserve negative findings.
Do not count model agreement, a longer bibliography, or a clean PDF build as
evidence for a theorem or novelty.
