# External review and submission gates

The local workboard (`WORKBOARD.jsonl`, `scripts/agents.py`) remains the
authoritative state for task claims, worktrees, quotas and execution. GitHub
Issues are used only for a small number of **external gates** with public,
publication-safe acceptance criteria.

Do not mirror every board task into an issue. Do not put confidential referee
text, unpublished priority details, private data or copyrighted scans in an
issue. Keep those in the repository's local review directories.

## Gate issues

| Issue | Gate | Scope | Local tasks / evidence |
|---|---|---|---|
| [#1](https://github.com/andrewimpellitteri/eternalism/issues/1) | Theorem note external review | `research/paper-novel/` | `paper-novel-result`; `REVIEW_PACKET.md`, `verification.json` |
| [#2](https://github.com/andrewimpellitteri/eternalism/issues/2) | Article reframe and substantive application | `paper/main.tex` | `article-reframe-scope`, `brading-existence-bridge`, `admissibility-burden-calibration`, `favoring-account`, `strongest-opponents`, `examples-scope-cleanup`, `article-rebuild-integration`, `article-rereview` |
| [#3](https://github.com/andrewimpellitteri/eternalism/issues/3) | Rank-only no-go independent audit | `research/rank-renewal-convergence/` | `rank-renewal-convergence`; `COORDINATOR_REVIEW.md` |
| [#4](https://github.com/andrewimpellitteri/eternalism/issues/4) | Source closure and correspondence | Stein, Putnam, Zalel thesis, DZ pagination | `paper-source-gates`, `knowledge/audits/stein-printed-pages/` |
| [#5](https://github.com/andrewimpellitteri/eternalism/issues/5) | Submission decision and release sign-off | final release only | all of the above |

`#5` is labeled `status:blocked` until #1–#4 are resolved or explicitly
deferred.

## How to check a gate

Read-only helper: `python3 tools/gh-gates/check_gates.py` (or `--json`).
It only calls `gh issue view` and never writes to GitHub. Manual equivalent:

```sh
gh issue view 1 --json number,title,state,labels,url
gh issue view 2 --json number,title,state,labels,url
gh issue view 3 --json number,title,state,labels,url
gh issue view 4 --json number,title,state,labels,url
gh issue view 5 --json number,title,state,labels,url
```

A gate closes only with evidence in the issue or a linked commit. Closing an
issue without evidence is the same failure mode as accepting a task without
review. Do not close a gate from a worker; the coordinator does it at release.

## Labels

- `gate:submission` — release/submission gate.
- `gate:review` — independent review gate.
- `gate:source` — source-access gate.
- `gate:decision` — author/coordinator decision.
- `status:blocked` — blocked by an unmet gate.
- `area:paper`, `area:article`, `area:rank` — scope.

## Reopen rules

- #1 reopens on a counterexample, a prior proof of the doubly-principal
  classification, or a source mismatch.
- #2 reopens if the rebuilt paper still ends as a prospectus or the Brading
  existence argument fails.
- #3 reopens on a gap in the imported two-cap/laminar frame or a normalized
  rank-only measure outside `(0,1]`.
- #4 reopens on a contradicting scan, an available thesis, or an edition change.
- #5 reopens if any upstream gate reopens or the release commit changes.
