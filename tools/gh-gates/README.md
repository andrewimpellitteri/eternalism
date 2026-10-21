# GitHub gate status checker

Read-only checker for the five external gates in `GATES.md`.

The local workboard (`WORKBOARD.jsonl`, `scripts/agents.py`) remains
authoritative for task claims, worktrees and execution. GitHub Issues are used
only for release/review gates.

## Usage

From the repository root:

```sh
python3 tools/gh-gates/check_gates.py
python3 tools/gh-gates/check_gates.py --json
```

The script calls only:

```sh
gh issue view N --json number,title,state,labels,url,updatedAt
```

It never creates, edits, closes or comments on an issue, and it does not read or
print credentials. If `gh` is missing, it exits `2` with a clear error; if a
gate lookup fails, it prints the error and exits `3`. It does not retry.

## Mapping

| Issue | Gate | Local tasks |
|---|---|---|
| #1 | Theorem note external review | `paper-novel-result` |
| #2 | Article reframe and substantive application | the eight reframe tasks |
| #3 | Rank-only no-go independent audit | `rank-renewal-convergence` |
| #4 | Source closure and correspondence | `paper-source-gates` |
| #5 | Submission decision and release sign-off | all upstream gates |

The mapping is in `gates.json`; edit it when a gate or local task changes.

## Policy

- A gate closes only with evidence or a linked commit.
- Workers do not close gates; the coordinator does at release.
- Do not put confidential referee text, private data or copyrighted scans in an
  issue.
- `status:blocked` on #5 is expected until #1–#4 are resolved or explicitly
  deferred.

## Test

```sh
python3 tools/gh-gates/check_gates.py
```

Expected: five rows, #5 marked blocked, exit 0.
