# Committed-baseline launch

Coordinator implementation, 2026-10-21. User requested headless OpenCode GLM
workers while the separate clock task had unfinished files in the shared checkout.

Added explicit `launch --from-committed-head`; the default dirty-checkout refusal
remains. The opt-in checks committed coordination/instructions/configuration and
clean proposed output paths, pins one HEAD for the entire batch, and creates
isolated worktrees from that hash. Uncommitted unrelated files are neither copied
nor changed. Required research inputs must be committed before launch.

Changed scripts/agents.py, scripts/agents/README.md and tests/test_agents.py.
The real-Git regression checks the default refusal, opt-in baseline, isolation,
preservation of tracked and untracked concurrent work, rejection of dirty board
and worker output paths. `python3 -m unittest discover -s tests -p test_agents.py`:
13 tests passed. No provider call was part of the regression.

This does not freeze other coordinators or provide a filesystem sandbox. Existing
claim locking and ownership checks remain required. A worker report is still a
submission for review, and provider availability is only established by a run.
