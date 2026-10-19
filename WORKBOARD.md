# Workboard

Generated from WORKBOARD.jsonl and central local claims.
Run `python3 scripts/agents.py sync` to refresh; `list` reads live state.

First milestone: prior work → theory map → independent novelty audit.

| State | Task | Priority | Depends on | Owner |
|---|---|---|---|---|
| review | `kb-foundations` — Map the strongest time arguments and their physical assumptions | 10 | — | luna-foundations |
| review | `kb-formalization` — Inventory reusable relativity and quantum formalizations | 10 | — | luna-formalization |
| review | `kb-frontier` — Screen recent physics of time and identify tractable extension targets | 10 | — | luna-frontier |
| open | `kb-agent-methods` — Audit AI-assisted physics and design evidence-preserving synthesis | 9 | — | — |
| blocked | `theory-map` — Synthesize a broad assumption and observable map without erasing disagreements | 9 | kb-foundations, kb-formalization, kb-frontier, kb-agent-methods | — |
| blocked | `novelty-audit` — Independently challenge proposed contributions against closest prior work | 10 | theory-map | — |
| blocked | `baseline-reproduction` — Reproduce the selected target's smallest existing result in Python | 8 | novelty-audit | — |
| blocked | `extension-search` — Find a new consequence, counterexample or equivalence boundary | 8 | baseline-reproduction | — |
| blocked | `lean-certificate` — Verify selected mathematical claims and audit their meaning | 7 | extension-search, kb-formalization | — |
| blocked | `adversarial-review` — Try to break the result, its novelty and its ontological inference | 10 | lean-certificate | — |
| blocked | `synthesis` — State what physics supports, excludes and cannot decide | 6 | adversarial-review | — |

Agent delivery enters review. Only integrated, reviewed work becomes done.

See scripts/agents/README.md for launch, recovery, and review commands.
