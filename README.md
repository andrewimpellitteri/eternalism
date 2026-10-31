# Computational philosophy of time

Which claims about time does physics support, exclude or leave open? The repository's name is a
question, not an answer: this project has no preferred temporal ontology.

## Read this first

**[What the Past Can Fix](research/what-the-past-can-fix/what-the-past-can-fix.pdf)** is the main
output, a 42-page paper in four parts. Its thesis is that what has become, what is fixed, what
exists and what is true are four different relations.

| Part | Subject | State |
|---|---|---|
| I | Stein's theorem in general relativity | Reviewed internally |
| II | What a law can fix from the past | Reviewed internally |
| III | Same past and whole-realm rigidity, conditional on published inputs | Reviewed internally |
| IV | Stages, truth policies, totality and persistence | Report-depth survey |

All review so far is by models from the same family, so none of it is independent. No outside
expert has read this work, and the paper claims no novelty and selects no ontology. The paper's
[red-team](research/what-the-past-can-fix/REVIEW.md) records what is tight and what is not.

## Where things stand

- [Claim ledger](research/CLAIM_STATUS.md): the status of each claim.
- [Current synthesis](research/CURRENT_SYNTHESIS.md): the dated narrative, newest first.
- [Parity map](research/PARITY_MAP.md): how far the repo is from the field of time, and what to
  read next. The largest gap is the direction of time.
- [Review queue](research/REVIEW_QUEUE.md): worker results nobody has signed off.
- [External gates](GATES.md): what must happen before any release.

## Layout

| Path | Contents |
|---|---|
| [`research/`](research/README.md) | Every research lane, indexed by purpose |
| [`knowledge/`](knowledge/README.md) | Source records and reading maps, with read depth labelled |
| `paper/` | The earlier admissibility article, not the unified paper |
| `output/pdf/` | Builds of earlier drafts |
| `experiments/` | Python reproductions, mostly from the causal-set phase |
| `formal/` | Lean certificate |
| `grid/` | Idea-grid contract and axes |
| `scripts/`, `tests/`, `tools/` | Coordination, source checks and GitHub gate tools |
| `sources-local/` | Copyrighted books kept on this machine only. Ignored by git |

Lane paths are stable identifiers. Scripts, hash manifests and archived records depend on them,
so index a lane rather than move it.

## Checks

```bash
python3 -m unittest discover -s tests
```

```bash
python3 scripts/check_sources.py
```

```bash
python3 scripts/check_links.py
```

To rebuild the paper, regenerate its parts and run LaTeX three times:

```bash
python3 -I research/what-the-past-can-fix/assemble.py
```

```bash
cd research/what-the-past-can-fix && pdflatex -interaction=nonstopmode -no-shell-escape main.tex
```

## Agent workflow

[AGENTS.md](AGENTS.md) sets the research standards. `WORKBOARD.jsonl` defines tasks, and
`WORKBOARD.md` is generated from it. Workers run through `scripts/agents.py`, each with its own Git
worktree, claim and report. Nothing launches automatically. See [the runbook](scripts/agents/README.md).

```bash
python3 scripts/agents.py status
```
