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

## Current research state

The [current integrated synthesis](research/CURRENT_SYNTHESIS.md) and
[claim-status ledger](research/CLAIM_STATUS.md) connect the causal-set, observer,
Stein--GR, horizons, future-truth and lawful-completion programmes. They include
the 28 October screening repair and distinguish reviewed results from open
coupled-matter, regularity and philosophical premises. Older notes retain their
dates; the current synthesis records what supersedes them. No temporal ontology
is selected by this integration.

## Earlier selection and novelty sprint

The first selection gate is complete: a primary target and a fallback are
recorded in `research/redteam/selection-gate/`, and the baseline, extension,
Lean kernel and certificate audit are accepted. The next phase is a bounded
sprint for one genuinely new result:

- [Novelty sprint](research/NOVELTY_SPRINT.md) — bets, gates, timeboxes and
  kill criteria.
- [Agentic philosophy playbook](research/agentic-philosophy/STATE_AND_PLAYBOOK.md)
  — what agents can and cannot do, and the swarm design used here.

No result is called new until the `novelty-verdict-selected` gate and an
independent adversarial review say so.


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

