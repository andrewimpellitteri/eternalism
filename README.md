# Computational philosophy of time

Investigate which claims about time are supported, excluded, or left
underdetermined by physics. The repository name is a question, not a preferred
answer. Python supports exploration and reproduction; Lean supports selected
proofs after their physical and philosophical meanings have been checked.

Start with [WORKBOARD.md](WORKBOARD.md), the
[knowledge base](knowledge/README.md), and the
[novelty strategy](knowledge/NOVELTY.md).

## First milestone

Build a source-backed account of prior work, existing formalizations, recent
physics, and AI-assisted research methods. Compare a broad set of theories using
explicit assumptions and observables. Choose a narrow contribution only after
an independent novelty audit. A literature collection is infrastructure, not
evidence that a new result has been discovered.

## Agent workflow

```sh
python3 scripts/agents.py list
python3 scripts/agents.py brief kb-foundations
python3 scripts/agents.py launch --dry-run kb-foundations kb-formalization kb-frontier
python3 scripts/agents.py launch kb-foundations kb-formalization kb-frontier
python3 scripts/agents.py status
```

Uses `zai-coding-plan/glm-5.3-flash`, matching the existing Awning agent workflow.
Override with `--model provider/model`. Each task has a separate Git worktree,
central claim, event log, and report. No research agents launch automatically.
See [the runbook](scripts/agents/README.md). Python standard library only for
coordination; research dependencies are chosen after the knowledge-base gate.

