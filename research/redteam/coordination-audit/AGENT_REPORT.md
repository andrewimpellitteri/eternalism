# rt-coordination-state-audit

Claude coordinator, 2026-10-20 08:20 UTC. The brief asked for a read-only audit
and a plan for the coordinator to execute. The coordinator executed most of that
recovery earlier the same session, so this report records evidence, actions
already taken, and what remains. The live-state edits below were coordinator
actions, not taken under this task.

## Root cause of the idle claims

At about 20:34 UTC on 2026-10-19 the z.ai plan hit its 5-hour usage limit (code
1308). At the same moment, commit a0c506f was adding red-team rows to
`WORKBOARD.jsonl` before their `owns` field was filled in. Each GLM supervisor's
heartbeat called `tasks()`, which raised `KeyError: 'owns'`, and the supervisor
exited (`REFUSED: 'owns'` in `worker.log`). Six claims were left with no process
and clean worktrees at b3497f2 / f399398. That is the "claimed but idle" pattern
the red team saw.

## Fixes already in main

| Commit | Change |
|---|---|
| 337ed00 | `beat()`: a failed heartbeat no longer kills a worker. Quota (1308) errors stop retries with a clear reason. New `agents.py resume` restarts a claimed task in its existing worktree. `tasks()` rejects a row missing a required key with `ValueError`. The test baseline is green. |
| 337ed00 | `resume` refuses if the supervisor or an OpenCode run for the task is alive. (The first draft's `pgrep` guard never fired on macOS; fixed.) `--dry-run` has no side effects. |

## Claim inventory at 08:20 UTC

| Task | Agent | Class | Evidence |
|---|---|---|---|
| kb-pw-critiques | glm | active | OpenCode and supervisor alive; resumed 07:53 |
| kb-csg-quantum-boundary | glm | active | OpenCode and supervisor alive |
| kb-sector-conditioning | glm | active | OpenCode alive; restarted 08:18 with a 4-slot cap |
| kb-clock-interactions | glm | active | OpenCode alive; restarted 08:18 |
| kb-putnam-ablation-prior | glm | queued | supervisor alive, waiting for a slot |
| rt-fulltext-claim-spotcheck | codex | active | claimed 08:12; uncommitted outputs in `knowledge/audits/fulltext-spotcheck/` |
| rt-source-canonicalization | codex | active | claimed 08:12 |
| article-working-draft | codex-article | **unknown / idle** | no update since 2026-10-19 19:53 UTC; no worktree (shared checkout); a Codex TUI process exists but this claim's outputs are unchanged since the 16:08 snapshot |
| rt-coordination-state-audit, rt-paper-claim-ledger | claude-coordinator | active | this session |

Released or finished this session: `kb-relational-markov-audit` (merged 9a0dc93),
`grid-adversarial-design` (stale Codex claim, accepted after review), the three
Luna review lanes, and the grid and test tasks.

## Merge state

All 19 `done` tasks with worktrees have their `agent/*` branch in main. No
review-state branch is waiting. Branches cut before known corrections:
`kb-pw-critiques` starts from f399398, and the four RC lanes from b3497f2. Before
merging them, check that they reuse current source IDs and do not reintroduce
metadata fixed since then, for example in 795618a and 7fd614f.

## Remaining recovery checklist

1. **article-working-draft:** ask the user or the Codex session whether it is
   still working. If not, release it with `--notes` naming the preserved files
   (`paper/` is committed through 34f0357). Do not edit `paper/` meanwhile;
   `rt-paper-claim-ledger` is read-only on it.
2. **Unpushed main:** main is 114 commits ahead of `origin/main`. Pushing is the
   user's decision.
3. **Worktrees:** 24 exist and 19 are for done tasks. They can be pruned with
   `git worktree remove` after the user agrees; nothing in them is unmerged.
4. **WORKBOARD.md:** regenerated on each transition and often dirty; commit it
   with coordinator commits rather than treating it as drift.
5. **Concurrency:** run GLM at 2–4 slots. The z.ai 5-hour quota ran out with six
   concurrent workers. Code 1308 now ends a run as `failed` with the quota reset
   time in the reason, rather than retrying.

## Deliberately not done

No push, no worktree removal, no release of the Codex claims, no killed
processes other than three queued supervisors this coordinator had started
(restarted with `resume`), and no edits to Codex's uncommitted files.

## History rewrite, 2026-10-21

At the user's direction, the Clifton–Hogarth 1995 scan
(`knowledge/putnam-ablation/primary/clifton-hogarth-1995.pdf`, copyrighted, rights
not established) was removed from every commit on `main` with `git filter-branch`.
The rewritten `main` was force-pushed to the public GitHub repo with a lease on the
old tip `a265fdb`. The file stays on local disk and is ignored by
`knowledge/**/primary/*.pdf` in `.gitignore`. Two Codex commits made during the
rewrite were replayed with their original author, date and message.

Every commit hash changed. `history-rewrite-2026-10-21.tsv` maps each old hash to
its new one (185 rows; subject, author and date verified pairwise), so hashes
cited in reports and board notes can be translated.

Still to do: GitHub serves the old commits by hash until GitHub Support purges
cached objects (no forks exist). Eleven local `agent/*` branches and their worktrees
still contain the file; never push them, and prune them when the worktrees are
retired.
