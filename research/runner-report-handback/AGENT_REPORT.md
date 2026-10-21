# Root handback scope consistency

Coordinator fix, 2026-10-21. The actual GLM correction worker produced its scoped
report and the root AGENT_REPORT.md required by the supervisor. Every brief
explicitly permits that root file, but acceptance rejected it as unowned.

Acceptance now permits exactly root AGENT_REPORT.md alongside the task owns
paths. It continues to reject every other unowned file. Coordinators archive
root reports into each lane-owned directory and remove the root copy during
integration to avoid report collisions. No scientific review/acceptance gate or
worker permission was relaxed.

A real-Git regression integrates a branch containing an owned result, root
report and rogue unowned file; acceptance rejects the rogue file, then succeeds
after its removal. This also exposed an ambiguity when a branch and worktree
path have the same name: the diff now separates revisions from paths with --.

Changed scripts/agents.py, scripts/agents/README.md and tests/test_agents.py.
`python3 -m unittest discover -s tests -p test_agents.py`: 14 tests passed.
No installs, model calls or changes to other workers' files.
