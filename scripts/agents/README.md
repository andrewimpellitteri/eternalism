# OpenCode GLM workboard

Adapted from the local `4o_clone` claim-board and `awning_wo` isolated-agent
patterns. The installed OpenCode 2.0.32 help lists `--standalone`, not the old
example's `--pure`. Coordination uses only Python's standard library.

## Launch

Run from the main checkout with an initial commit and a clean working tree.
The default model is `zai-coding-plan/glm-5.3-flash`. Existing OpenCode login
and global MCP settings are inherited when OpenCode registers them; see the
search note below.
The local override does not disable MCP. No keys are copied into this repo.

```sh
python3 scripts/agents.py list
python3 scripts/agents.py brief kb-foundations
python3 scripts/agents.py launch --dry-run kb-foundations kb-formalization kb-frontier
python3 scripts/agents.py launch kb-foundations kb-formalization kb-frontier
python3 scripts/agents.py status
```

Three initial lanes are deliberately independent. Queue `kb-agent-methods`
after one finishes. Runtime/log files are under `.agent-runtime/`; worktrees
are under `.worktrees/`. Both are ignored by Git. Claims and events are shared
across worktrees through the main checkout and protected with a file lock.
Do not run `git clean -fdx`: it would destroy these untracked work products.

Dry-run checks task dependencies, active ownership, IDs, and target paths without
creating claims, worktrees, processes or model calls. Actual launch also checks
OpenCode installation, a committed baseline, and a clean main checkout.

When a disjoint worker has unfinished files in the main checkout, the coordinator
may use `launch --from-committed-head TASK ...`. This explicit option pins one
committed HEAD for the batch and preserves all working files. It still rejects
uncommitted changes to WORKBOARD.jsonl, AGENTS.md, the runner, worker configuration
and proposed task output paths. Uncommitted research inputs are absent from the
new workers; commit any inputs they require first. The default launch continues
to require a clean checkout. Neither mode stashes or commits another worker's work.

**Search.** Runs before 16:30 on 2026-10-19 had no search: OpenCode 2.0.32 did
not register the pre-2.0 global `web-search-prime` entry, its key had expired,
and every built-in `websearch` call returned `Web search cancelled`. Those
lanes used direct `webfetch` only, so their coverage is narrower than their
briefs asked for. The entry was re-registered in the 2.0 `mcp.servers` shape;
`opencode mcp list` under the worker environment now shows it connected. Check
that before launching search-heavy lanes.

**Rate limits.** About a dozen simultaneous GLM workers hit z.ai `429` (code
1302) at once. Workers now hold one of `AGENT_MAX_CONCURRENT` slot locks
(default 6) under `.agent-runtime/slots/`; extra workers queue with heartbeats.
A run that hits a rate limit backs off and resumes the same OpenCode session,
up to four attempts. Usage-quota exhaustion stops without a retry loop.
Automatic review requires a clean tree, a new committed `AGENT_REPORT.md`
relative to the recorded launch base, and new committed task-owned output.
Inherited baseline reports, report-only changes, out-of-scope commits and
missing launch bases do not qualify, even after exit 0. A nonzero exit after
this complete handback can enter review with the exit code and any quota
message noted, since OpenCode sometimes exits 1 after completing.
`result.json` records the reason and attempt count.

Workers use `opencode run --standalone --auto --format json`. Each writes a
capability check for its MCP search access, research files, and AGENT_REPORT.md.
Public web research is allowed. Permission rules are accident guards, not an OS
sandbox; allowed file scopes require review. A supervisor updates heartbeats.

## Review and integrate

A fresh committed handback meeting the checks above moves the task to `review`,
never `done`. A successful process exit alone is not a submission.
Inspect `.agent-runtime/runs/TASK/{events.jsonl,stderr.log,result.json,worker.log}`
and `.worktrees/TASK/AGENT_REPORT.md`. Read the diff, confirm owned-file scope,
inspect sources, and rerun relevant checks. Check `git status` in the worker
worktree for uncommitted output; an incomplete commit must not be accepted.

The coordinator integrates approved work in dependency order. For example:

```sh
git diff HEAD...agent/kb-foundations --stat
git merge --ff-only agent/kb-foundations
python3 scripts/agents.py accept kb-foundations --agent glm-kb-foundations \
  --notes 'Reviewed sources, checked scope, integrated branch.'
python3 scripts/agents.py sync
```

After other branches have landed, a fast-forward may be impossible. Inspect and
merge the reviewed branch normally; do not force or discard another lane's work.
The acceptance command checks that the recorded branch is an ancestor of the
main checkout's HEAD. It cannot establish scientific correctness for you.
Commit the refreshed workboard before launching the next batch.

The root `AGENT_REPORT.md` is an allowed handback file, as shown in every task
brief and required by the worker supervisor. Acceptance allows that exact file
alongside the task's owned paths; any other unowned file still blocks acceptance.
When integrating multiple lanes, archive the root report inside its lane-owned
directory and remove the root copy in the integration commit to avoid collisions.

## Recover a stopped or failed task

```sh
python3 scripts/agents.py stop kb-frontier
python3 scripts/agents.py status
python3 scripts/agents.py release kb-frontier --agent glm-kb-frontier \
  --notes 'Verified process stopped; preserved worktree and recorded recovery plan.'
```

Stop checks that the recorded PID still identifies this supervisor before
signaling its process group. It preserves the claim and all work. A stopped or
failed process never silently frees a task for a second writer. Inspect its
worktree before releasing, continuing manually, or moving it aside for a retry.
Existing branches/worktrees are never overwritten by launch.

The runner's local state is authoritative for live claims. The generated
WORKBOARD.md is a snapshot; `list` and `status` show current local state.
