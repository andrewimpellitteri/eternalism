# Grid cell contract

Each cell pairs ideas that may never have been combined. A worker's job is to
find the strongest *precise, checkable* claim the pairing suggests, then try to
kill it. Most cells should die. A killed cell with a recorded reason is a
useful result; it marks that region of the grid as covered.

## Cell families

- **Pressure cell** `S1-Pxx-Byy`: inside framework P, does bridge premise B have
  a precise form, and does P make it true, false, or undecidable as stated?
- **Transfer cell** `T1-Pxx-Pyy`: does a theorem, construction, or technique
  native to one framework answer a question in the other?
- **Expansion cell** `S2-…-Oz-Mw`: a stage-1 survivor crossed with an ontology
  package and a move type. It is generated only from cells that advanced.

## Output: one JSON object per cell

Write `cells.jsonl` in your batch directory, one line per assigned cell, in
assignment order. Every assigned cell gets a line, including killed ones.

| Field | Content |
|---|---|
| `cell` | The assigned cell ID, exactly. |
| `verdict` | `kill`, `hold`, or `advance`. |
| `kill_reason` | When killed: `incoherent`, `trivial-by-definition`, `known`, `no-checkable-instance`, `ontology-leap`, or `out-of-scope`. Otherwise `null`. |
| `claim` | The strongest precise claim found: quantifiers, objects, and hypotheses stated. Write it even for a killed cell, so the kill can be audited. |
| `move` | One of the move IDs in `axes.json` (`M1`–`M6`). |
| `smallest_instance` | The smallest finite or explicit model in which the claim can be checked (Python, Lean, or by hand), or why none exists. |
| `predecessors` | At least three when advancing: `{"ref": source ID or URL, "read_depth": …, "shows": …, "differs": …}`. Reuse IDs from `knowledge/`. |
| `defeat_queries` | The literal searches run to find prior work that already makes the claim, with a one-line result for each. At least five when advancing. |
| `bridge_premises` | Every premise needed to move from the mathematical claim to a claim about temporal ontology. An empty list means the claim is purely physical or mathematical. Say so. |
| `falsifier` | What result, paper, or computation would show the claim wrong, trivial, or known. |
| `notes` | Anything that a reviewer must know: unread sources, guesses, open subquestions. |

## Verdict rules

- **kill**: any kill reason applies. `known` names the predecessor that already
  states the claim. `trivial-by-definition` explains which definition makes it
  hold. `ontology-leap` means the claim matters only through a bridge premise
  that does all of the work.
- **hold**: the claim is precise and not obviously known, but the defeat search
  or the smallest instance is incomplete. Say exactly what is missing.
- **advance**: precise claim, smallest checkable instance, three predecessors
  with stated differences, at least five logged defeat queries, and every
  bridge premise named. Advancing is a request for an independent kill attempt.
  It is not a novelty finding.

There are no numeric scores. Do not rank cells by plausibility, interest, or
confidence; the only ordering is how far a cell has survived the gates.

## Discipline

The AGENTS.md research standards apply in full. In particular, an abstract is
a lead, a finite instance has only its stated domain, a representation change is
not an ontological equivalence, and a definition that assumes an ontology cannot
establish it. Record unread or blocked sources as unread. Verify every arXiv ID
and DOI you record, for example with `python3 scripts/check_sources.py --online`
on a scratch `sources.jsonl`.
