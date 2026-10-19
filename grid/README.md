# Idea grid

Agents give breadth: they can try every pairing of a physical framework with
an argument pressure or another framework, which no single reader would do.
The grid turns that breadth into a search with hard filters, so coverage is
systematic and survival, not volume, is what counts.

## Pipeline

| Stage | Cells | Question | Gate to next stage |
|---|---|---|---|
| `s1` pressure | 15 physics x 12 bridge premises = 180 | What does this premise say inside this framework, precisely? | `advance` per [CONTRACT.md](CONTRACT.md) |
| `t1` transfer | 15 x 14 / 2 = 105 | Does a result native to one framework settle a question in the other? | `advance` |
| `adv` adversary | one per advanced cell | Independent kill attempt; sees the claim only, not the proposer's sources | `survive` |
| `s2` expansion | survivor x 9 ontology packages | What does the surviving claim do to each package, through which bridge? | Claim contract in [NOVELTY.md](../knowledge/NOVELTY.md), then `novelty-audit` |

Axes live in [axes.json](axes.json), drawn from the package table and argument
ledger of [PHILOSOPHY_OF_TIME.md](../knowledge/PHILOSOPHY_OF_TIME.md).
Add items freely; never renumber, because cell IDs are built from item IDs.

## Commands

```sh
python3 scripts/grid.py cells                          # cells per family, unassigned
python3 scripts/grid.py tasks s1 --batch 12            # one task per physics row (preview)
python3 scripts/grid.py tasks s1 --batch 12 --limit 3 --append   # add to WORKBOARD.jsonl
python3 scripts/agents.py launch grid-s1-01 grid-s1-02 grid-s1-03
python3 scripts/grid.py status --worktrees             # coverage grids, verdicts, contract problems
python3 scripts/grid.py tasks adv --worktrees --batch 5      # after s1/t1 results land
```

`--append` writes to the shared board; coordinators only. Cells named in an
existing grid task are never reassigned. Integrate result branches before
generating `adv` or `s2` tasks from the main checkout, or pass `--worktrees`.

## Limits

- Same-model proposer and adversary share failure modes. Run the adversary
  stage on a different model (`launch --model`) where one is available, and
  spot-check kills as well as advances.
- A survivor has passed two AI kill attempts. That selects a candidate for the
  human novelty gate; it is not evidence of novelty or truth.
- A killed cell is covered at the depth its worker read, not settled. The
  status grid shows coverage, not the state of the literature.
