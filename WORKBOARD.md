# Workboard

Generated from WORKBOARD.jsonl and central local claims.
Run `python3 scripts/agents.py sync` to refresh; `list` reads live state.

First milestone: prior work → theory map → independent novelty audit.

| State | Task | Priority | Depends on | Owner |
|---|---|---|---|---|
| open | `grid-regression-tests` — Test idea-grid validation, provenance and stage transitions | 10 | — | — |
| claimed | `grid-adversarial-design` — Independently review the idea-grid gates and build adversarial control cases | 9 | — | codex-grid-review |
| done | `kb-foundations` — Map the strongest time arguments and their physical assumptions | 10 | — | luna-foundations |
| done | `kb-formalization` — Inventory reusable relativity and quantum formalizations | 10 | — | luna-formalization |
| done | `kb-frontier` — Screen recent physics of time and identify tractable extension targets | 10 | — | luna-frontier |
| done | `kb-agent-methods` — Audit AI-assisted physics and design evidence-preserving synthesis | 9 | — | glm-kb-agent-methods |
| done | `theory-map` — Synthesize a broad assumption and observable map without erasing disagreements | 9 | kb-foundations, kb-formalization, kb-frontier, kb-agent-methods | glm-theory-map |
| open | `novelty-audit` — Independently challenge proposed contributions against closest prior work | 10 | theory-map | — |
| blocked | `baseline-reproduction` — Reproduce the selected target's smallest existing result in Python | 8 | novelty-audit | — |
| blocked | `extension-search` — Find a new consequence, counterexample or equivalence boundary | 8 | baseline-reproduction | — |
| blocked | `lean-certificate` — Verify selected mathematical claims and audit their meaning | 7 | extension-search, kb-formalization | — |
| blocked | `adversarial-review` — Try to break the result, its novelty and its ontological inference | 10 | lean-certificate | — |
| blocked | `synthesis` — State what physics supports, excludes and cannot decide | 6 | adversarial-review | — |
| claimed | `kb-causal-sets` — Extract causal-set growth, covariant becoming and embedding results at theorem level | 9 | — | glm-kb-causal-sets |
| claimed | `kb-thermal-records` — Map thermal time, modular flow, records and the arrow of time | 9 | — | glm-kb-thermal-records |
| done | `kb-ico-qrf` — Compare indefinite causal order, process matrices and temporal quantum reference frames | 9 | — | glm-kb-ico-qrf |
| claimed | `kb-gr-qg-time` — Map global spacetime structure and the problem of time in canonical quantum gravity | 9 | — | glm-kb-gr-qg-time |
| review | `kb-aqft-locality` — Audit algebraic QFT, locality and relativistic causality as constraints on time claims | 8 | — | luna-aqft-locality |
| review | `kb-arrow-cosmology` — Separate the cosmological and thermodynamic arrows from temporal ontology | 8 | — | luna-arrow-cosmology |
| review | `kb-discriminators` — Collect proposed observational or experimental discriminators for time ontologies | 8 | — | luna-discriminators |
| done | `kb-time-interpretations` — Map time in retrocausal, Everettian, two-time and block-history interpretations | 8 | — | glm-kb-time-interpretations |
| claimed | `kb-bib-repair` — Repair and verify bibliographic records, including books and JSTOR items without DOIs | 9 | — | glm-kb-bib-repair |
| claimed | `kb-axiomatic-relativity` — Extract the axiomatic and definability results behind simultaneity and relativity | 9 | — | glm-kb-axiomatic-relativity |
| claimed | `kb-relational-markov-audit` — Audit the derivations of the 2026 relational-Markovianity and clock-conditioning paper | 8 | — | glm-kb-relational-markov-audit |
| claimed | `kb-preferred-foliation` — Map theories that add a preferred foliation or relativistic collapse structure | 8 | — | glm-kb-preferred-foliation |
| claimed | `kb-pw-critiques` — Collect critiques and defenses of the Page-Wootters construction | 8 | — | glm-kb-pw-critiques |
| claimed | `kb-novelty-prepass-a` — Pre-pass search for prior work defeating candidate A, growing history versus completed history | 8 | — | glm-kb-novelty-prepass-a |
| claimed | `article-working-draft` — Write an argument-driven LaTeX working article without claiming an unestablished result | 8 | kb-foundations, kb-formalization, kb-frontier, kb-agent-methods | codex-article |

Agent delivery enters review. Only integrated, reviewed work becomes done.

See scripts/agents/README.md for launch, recovery, and review commands.
