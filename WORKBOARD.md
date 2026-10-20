# Workboard

Generated from WORKBOARD.jsonl and central local claims.
Run `python3 scripts/agents.py sync` to refresh; `list` reads live state.

First milestone: prior work → theory map → independent novelty audit.

| State | Task | Priority | Depends on | Owner |
|---|---|---|---|---|
| done | `grid-regression-tests` — Test idea-grid validation, provenance and stage transitions | 10 | — | claude-coordinator |
| done | `grid-adversarial-design` — Independently review the idea-grid gates and build adversarial control cases | 9 | — | codex-grid-review |
| done | `kb-foundations` — Map the strongest time arguments and their physical assumptions | 10 | — | luna-foundations |
| done | `kb-formalization` — Inventory reusable relativity and quantum formalizations | 10 | — | luna-formalization |
| done | `kb-frontier` — Screen recent physics of time and identify tractable extension targets | 10 | — | luna-frontier |
| done | `kb-agent-methods` — Audit AI-assisted physics and design evidence-preserving synthesis | 9 | — | glm-kb-agent-methods |
| done | `theory-map` — Synthesize a broad assumption and observable map without erasing disagreements | 9 | kb-foundations, kb-formalization, kb-frontier, kb-agent-methods | glm-theory-map |
| done | `novelty-audit` — Independently challenge proposed contributions against closest prior work | 10 | theory-map | luna-recovery-novelty-audit |
| done | `baseline-reproduction` — Reproduce the selected target's smallest existing result in Python | 8 | novelty-audit, rt-selection-decision-gate | opencode-coordinator |
| done | `extension-search` — Find a new consequence, counterexample or equivalence boundary | 8 | baseline-reproduction | opencode-coordinator |
| done | `lean-certificate` — Verify selected mathematical claims and audit their meaning | 7 | extension-search, kb-formalization | opencode-coordinator |
| open | `adversarial-review` — Try to break the result, its novelty and its ontological inference | 10 | — | — |
| blocked | `synthesis` — State what physics supports, excludes and cannot decide | 6 | adversarial-review, paper-novel-result | — |
| done | `kb-causal-sets` — Extract causal-set growth, covariant becoming and embedding results at theorem level | 9 | — | glm-kb-causal-sets |
| done | `kb-thermal-records` — Map thermal time, modular flow, records and the arrow of time | 9 | — | glm-kb-thermal-records |
| done | `kb-ico-qrf` — Compare indefinite causal order, process matrices and temporal quantum reference frames | 9 | — | glm-kb-ico-qrf |
| done | `kb-gr-qg-time` — Map global spacetime structure and the problem of time in canonical quantum gravity | 9 | — | luna-recovery-kb-gr-qg-time |
| done | `kb-aqft-locality` — Audit algebraic QFT, locality and relativistic causality as constraints on time claims | 8 | — | luna-aqft-locality |
| done | `kb-arrow-cosmology` — Separate the cosmological and thermodynamic arrows from temporal ontology | 8 | — | luna-arrow-cosmology |
| done | `kb-discriminators` — Collect proposed observational or experimental discriminators for time ontologies | 8 | — | luna-discriminators |
| done | `kb-time-interpretations` — Map time in retrocausal, Everettian, two-time and block-history interpretations | 8 | — | glm-kb-time-interpretations |
| done | `kb-bib-repair` — Repair and verify bibliographic records, including books and JSTOR items without DOIs | 9 | — | glm-kb-bib-repair |
| done | `kb-axiomatic-relativity` — Extract the axiomatic and definability results behind simultaneity and relativity | 9 | — | glm-kb-axiomatic-relativity |
| done | `kb-relational-markov-audit` — Audit the derivations of the 2026 relational-Markovianity and clock-conditioning paper | 8 | — | glm-kb-relational-markov-audit |
| done | `kb-preferred-foliation` — Map theories that add a preferred foliation or relativistic collapse structure | 8 | — | glm-kb-preferred-foliation |
| done | `kb-novelty-prepass-a` — Pre-pass search for prior work defeating candidate A, growing history versus completed history | 8 | — | luna-recovery-kb-novelty-prepass-a |
| done | `article-working-draft` — Write an argument-driven LaTeX working article without claiming an unestablished result | 8 | kb-foundations, kb-formalization, kb-frontier, kb-agent-methods | codex-article |
| done | `kb-sector-conditioning` — Read the sector-coherence and normalization literature behind RC-3 at full text | 9 | — | glm-kb-sector-conditioning |
| done | `kb-clock-interactions` — Read the interacting and non-ideal clock neighbours of RC-1 at full text | 9 | — | glm-kb-clock-interactions |
| done | `kb-csg-quantum-boundary` — Read the quantum and non-Markov boundary of covariant causal-set growth | 8 | — | glm-kb-csg-quantum-boundary |
| done | `kb-putnam-ablation-prior` — Find and read prior work on premise ablation of the Rietdijk-Putnam argument | 8 | — | glm-kb-putnam-ablation-prior |
| done | `rt-fix-live-contract-test` — Restore a green test baseline: fix the stale live task-graph contract test | 10 | — | claude-coordinator |
| done | `rt-source-canonicalization` — Canonicalize duplicated source records and read-depth conflicts across lanes | 10 | — | codex-source-canonicalization |
| done | `rt-citation-gate-hardening` — Harden check_sources.py so full-text contract violations fail, not warn | 9 | — | codex-citation-gate |
| done | `rt-fulltext-claim-spotcheck` — Independently spot-check full-text claims and primary Stein/Malament sources | 10 | — | codex-fulltext-spotcheck |
| done | `rt-loadbearing-rereads-rc` — Coordinator-level rereads of the papers that can kill or shrink RC-1 to RC-5 | 9 | kb-clock-interactions, kb-sector-conditioning, kb-csg-quantum-boundary, kb-putnam-ablation-prior, kb-relational-markov-audit | opencode-coordinator |
| done | `rt-cross-model-pilot` — Prepare and, if authorized, run the cross-model semantic-audit pilot | 8 | — | claude-coordinator |
| done | `rt-coordination-state-audit` — Audit claimed-but-idle worktrees, stale claims and unpushed main; write the recovery plan | 9 | — | claude-coordinator |
| done | `rt-paper-claim-ledger` — Build a claim-by-claim source ledger for the working paper and a freeze list | 9 | — | claude-coordinator |
| done | `rt-grid-kill-criteria` — Set advance/kill criteria for the idea-grid before any cell is assigned | 8 | grid-regression-tests, grid-adversarial-design | claude-coordinator |
| done | `rt-selection-decision-gate` — Force a selection: one bounded target, a fallback, or an explicit no-selection | 10 | novelty-audit, rt-loadbearing-rereads-rc, ctp-priority-audit, ctp-fresh-proof-audit, ctp-covariant-boundary | opencode-coordinator |
| done | `creative-clock-certificates` — Find a nontrivial finite-clock instrument obstruction or tradeoff | 10 | novelty-audit | luna-creative-clock |
| done | `creative-covariant-stopping` — Find an observer-access or covariant stopping boundary in causal-set growth | 10 | novelty-audit | luna-creative-stopping |
| done | `creative-clock-memory` — Find an operational intervention boundary between clock memory and system memory | 10 | novelty-audit | luna-creative-memory |
| done | `ctp-priority-audit` — Audit forward citations and priority of the doubly-principal extension theorem | 10 | creative-covariant-stopping | luna-ctp-priority |
| done | `ctp-fresh-proof-audit` — Try to falsify the extension theorem from a fresh derivation | 10 | creative-covariant-stopping | luna-ctp-proof |
| done | `ctp-covariant-boundary` — Find the precise covariant-event boundary of the block obstruction | 10 | creative-covariant-stopping | luna-ctp-covariant |
| done | `rt-source-repair-integration` — Apply audited source repairs and replace inherited source copies with references | 10 | rt-source-canonicalization, rt-fulltext-claim-spotcheck, rt-citation-gate-hardening | codex-source-repairs |
| done | `rt-stein-printed-page-check` — Compare Stein 1991 printed theorem pages with the OCR and contextual premises | 9 | rt-fulltext-claim-spotcheck | codex-stein-pages |
| claimed | `article-admissibility-case` — Test the article admissibility standard against one strongest rival case | 8 | article-working-draft | codex-admissibility |
| done | `rt-clifton-hogarth-primary` — Read the user-supplied Clifton-Hogarth primary and resolve RC-2 secondary discrepancies | 10 | — | codex-clifton-primary |
| done | `rt-new-lane-canonical-references` — Resolve inherited copies from the newly integrated sector and CSG lanes | 9 | rt-source-repair-integration, kb-sector-conditioning, kb-csg-quantum-boundary | codex-new-lane-refs |
| done | `novelty-verdict-selected` — Decide whether the selected complex-percolation result is actually new | 10 | baseline-reproduction, extension-search, lean-certificate | opencode-coordinator |
| open | `rank-factor-boundary` — Resolve the rank-dependent post-factor boundary (construct or no-go) | 10 | novelty-verdict-selected | — |
| open | `vector-measure-boundary` — Test the no-go for Banach/Hilbert-valued measures | 9 | novelty-verdict-selected | — |
| open | `covariant-value-rules` — Classify weaker covariant post-value rules | 9 | novelty-verdict-selected | — |
| open | `clock-three-picture` — Compute the RC-1 finite three-picture clock model (fallback) | 8 | novelty-verdict-selected | — |
| open | `independent-replication` — Independently re-derive the selected two-cap bound and countermodel | 9 | novelty-verdict-selected | — |
| blocked | `paper-novel-result` — Write the paper for the surviving new result | 9 | adversarial-review | — |

Agent delivery enters review. Only integrated, reviewed work becomes done.

See scripts/agents/README.md for launch, recovery, and review commands.
