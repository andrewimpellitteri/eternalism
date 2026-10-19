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

**Search is currently unavailable to workers (checked 2026-10-19).** OpenCode
2.0.32 reports `No MCP servers configured`: the global `web-search-prime` entry
uses the pre-2.0 config shape and is not registered, and every built-in
`websearch` call returned `Web search cancelled`. Workers fell back to direct
`webfetch` of arXiv pages. Re-register the server (see below) and confirm with
`opencode mcp list` before relying on search-heavy lanes.

**Rate limits.** About a dozen simultaneous GLM workers hit z.ai `429` (code
1302) at once. Workers now hold one of `AGENT_MAX_CONCURRENT` slot locks
(default 6) under `.agent-runtime/slots/`; extra workers queue with heartbeats.
A run that hits a rate limit backs off and resumes the same OpenCode session,
up to four attempts. A nonzero exit after a committed `AGENT_REPORT.md` and a
clean tree enters review with the exit code noted, since OpenCode sometimes
exits 1 after completing. `result.json` records the reason and attempt count.

Workers use `opencode run --standalone --auto --format json`. Each writes a
capability check for its MCP search access, research files, and AGENT_REPORT.md.
Public web research is allowed. Permission rules are accident guards, not an OS
sandbox; allowed file scopes require review. A supervisor updates heartbeats.

## Review and integrate

A successful process exit plus report moves the task to `review`, never `done`.
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
