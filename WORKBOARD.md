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
| done | `adversarial-review` — Try to break the result, its novelty and its ontological inference | 10 | — | codex-adversarial |
| done | `synthesis` — State what physics supports, excludes and cannot decide | 6 | adversarial-review, paper-novel-result | opencode-coordinator |
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
| done | `article-admissibility-case` — Test the article admissibility standard against one strongest rival case | 8 | article-working-draft | codex-admissibility |
| done | `rt-clifton-hogarth-primary` — Read the user-supplied Clifton-Hogarth primary and resolve RC-2 secondary discrepancies | 10 | — | codex-clifton-primary |
| done | `rt-new-lane-canonical-references` — Resolve inherited copies from the newly integrated sector and CSG lanes | 9 | rt-source-repair-integration, kb-sector-conditioning, kb-csg-quantum-boundary | codex-new-lane-refs |
| done | `novelty-verdict-selected` — Decide whether the selected complex-percolation result is actually new | 10 | baseline-reproduction, extension-search, lean-certificate | opencode-coordinator |
| done | `rank-factor-boundary` — Resolve the rank-dependent post-factor boundary (construct or no-go) | 10 | novelty-verdict-selected | opencode-coordinator |
| done | `vector-measure-boundary` — Test the no-go for Banach/Hilbert-valued measures | 9 | novelty-verdict-selected | opencode-coordinator |
| done | `covariant-value-rules` — Classify weaker covariant post-value rules | 9 | novelty-verdict-selected | opencode-coordinator |
| done | `clock-three-picture` — Compute the RC-1 finite three-picture clock model (fallback) | 8 | novelty-verdict-selected | claude-coordinator |
| done | `independent-replication` — Independently re-derive the selected two-cap bound and countermodel | 9 | novelty-verdict-selected | opencode-coordinator |
| done | `paper-novel-result` — Write the paper for the surviving new result | 9 | adversarial-review | codex-paper-novel |
| done | `glm-adversarial-scalar` — Fresh GLM challenge to the scalar and conditional covariant theorems | 10 | — | glm-glm-adversarial-scalar |
| done | `glm-vector-indicator-boundary` — Determine the scope of the indicator-valued vector counterexample | 9 | — | glm-glm-vector-indicator-boundary |
| done | `runner-committed-launch` — Allow isolated workers from a checked committed baseline during disjoint active work | 10 | — | codex-runner |
| done | `glm-rank-renewal-boundary` — Try to settle the rank-only renewal problem with analytic bounds | 10 | — | opencode-coordinator |
| done | `glm-probe-corrections` — Apply the reviewed vector and covariant-probe corrections without strengthening claims | 9 | — | glm-glm-probe-corrections |
| done | `longshot-regularized-measure` — Long shot: regularized covariant measure for complex percolation | 6 | — | claude-longshot |
| done | `longshot-growth-completion-dilemma` — Long shot: growth-vs-completion dilemma theorem for complex percolation | 6 | — | claude-longshot |
| done | `longshot-birth-order-interference` — Long shot: interference trace of birth order under norm-only covariance | 6 | — | claude-longshot |
| done | `runner-report-handback` — Align root report acceptance with the worker brief and runner | 10 | — | codex-runner |
| done | `article-revision-2` — Revise the working article to capture the 20-21 October work | 7 | — | claude-coordinator |
| done | `glm-vector-norm-adversarial` — Try to falsify the new norm-only Hilbert and Banach classifications | 10 | — | opencode-coordinator |
| done | `longshot-residual-review` — Longshot residual review | 8 | — | claude-reviewer |
| done | `bc-holonomy-stage4` — Bc holonomy stage4 | 7 | — | codex-native-bc |
| done | `covtree-complex-levels` — Covtree complex levels | 6 | — | opencode-coordinator |
| done | `sorkin-cc-complex-percolation` — Sorkin cc complex percolation | 6 | — | opencode-coordinator |
| done | `constraint-formulation-compare` — Constraint formulation compare | 7 | — | codex-native-clock |
| done | `article-revision-2-review` — Article revision 2 review | 8 | — | codex-exec-reviewer |
| done | `paper-source-gates` — Paper source gates | 7 | — | codex-source-gates |
| done | `bridge-principle-defense` — Bridge principle defense | 8 | — | opencode-coordinator |
| done | `operational-stability-boundary` — Derive the operational stability boundary of finite-history amplitudes | 9 | — | codex-stability |
| done | `event-filter-resource-boundary` — Test whether event filters can access divergent-history witnesses at finite cost | 9 | — | codex-event-filter |
| done | `clock-action-correspondence` — Repair finite-clock comparison: charge origin, aliasing and valid cyclic actions | 10 | — | codex-clock-audit |
| done | `covariant-observer-witness` — Can a covariant internal observer access the unstable finite-history event? | 10 | — | opencode-coordinator |
| done | `record-loss-robust-boundary` — Find the robust interference boundary for partial access to environmental records | 9 | — | opencode-coordinator |
| done | `bc-nonvanishing-continuation` — Does Bell-causal phase freedom survive when every transition is nonzero? | 10 | — | codex-native-bc-nonzero |
| done | `rank-renewal-convergence` — Settle the weighted convergence obligation for rank-only post values | 10 | — | opencode-coordinator |
| done | `operator-qbc-phase-holonomy` — Does Bell-causal phase freedom survive operator-valued QBC? | 10 | — | opencode-coordinator |
| done | `observer-growth-channel` — Derive a causal-set observer channel and test the unstable event | 10 | — | opencode-coordinator |
| done | `paper-priority-referee` — Targeted priority audit and referee-style review of the selected paper | 9 | — | opencode-coordinator |
| done | `growth-completion-c3-revision` — Correct growth-completion Prop. 5/C3 and re-audit downstream covtree claims | 9 | — | opencode-coordinator |
| done | `empirical-discriminator-audit` — Audit proposed empirical discriminators for temporal ontology | 8 | — | opencode-coordinator |
| done | `completion-access-dilemma` — Completion, access, and the growing-block dilemma | 9 | — | opencode-coordinator |
| done | `article-reframe-scope` — Freeze the reframed article thesis, abstract and section plan | 10 | — | opencode-coordinator |
| done | `brading-existence-bridge` — When does a local present restrict existence? The Brading coverage problem | 10 | — | opencode-coordinator |
| done | `admissibility-burden-calibration` — Calibrate specification burdens: contradiction, likelihood, explanation and admissibility | 9 | — | opencode-coordinator |
| done | `favoring-account` — A positive account of defeasible favoring, not only exclusion | 9 | — | opencode-coordinator |
| done | `strongest-opponents` — Reconstruct Saunders and Pooley at their strongest | 9 | — | opencode-coordinator |
| done | `examples-scope-cleanup` — Decide and execute the example/scope cleanup | 8 | — | opencode-coordinator |
| done | `article-rebuild-integration` — Integrate the reframed article, cut the prospectus material, and build | 10 | article-reframe-scope, brading-existence-bridge, admissibility-burden-calibration, favoring-account, strongest-opponents, examples-scope-cleanup | opencode-coordinator |
| done | `article-rereview` — Independent re-review of the reframed article | 9 | article-rebuild-integration | opencode-coordinator |
| done | `gh-gate-sync` — Read-only GitHub gate status checker | 6 | — | opencode-coordinator |
| done | `existence-form-trilemma` — The form-of-existence trilemma for local presentism | 10 | — | opencode-coordinator |
| done | `p1-double-prime-revision` — Retarget the article at Brading's P1** and the coverage premise | 10 | — | opencode-coordinator |
| done | `refocus-cpobc-correspondence` — Audit CPOBC source correspondence and the remaining research boundary | 10 | — | luna-refocus-correspondence |
| done | `refocus-cpobc-reproduction` — Independently reproduce a CPOBC obstruction and assess feasibility | 10 | — | luna-refocus-reproduction |
| done | `refocus-rank-audit` — Audit the rank-dependent post theorem frame and priority | 10 | — | luna-refocus-rank |
| claimed | `refocus-selection-integration` — Integrate refocus audits, repair inherited claims and select the next target | 10 | refocus-cpobc-correspondence, refocus-cpobc-reproduction, refocus-rank-audit | codex-refocus-coordinator |
| done | `observer-effect-correspondence` — Separate class membership, coherent event filtering and completed-history covariance | 10 | — | codex-observer-effects |
| done | `bc-all-stages-extension` — Extend Bell-causal phase holonomy to every stage with bounded scalar variation | 10 | — | codex-bc-all-stages |
| done | `bc-phase-priority-and-invariants` — Audit phase-model priority and test an intrinsic completed-history quantity | 10 | bc-all-stages-extension, observer-effect-correspondence | codex-phase-invariants |
| done | `bc-matched-cylinder-pair` — Test a two-phase pair with equal cylinder norms and different intrinsic completed values | 10 | bc-phase-priority-and-invariants | codex-matched-norms |
| done | `bc-matched-diffuse-continuation` — Seek a non-atomic matched-cylinder pair beyond the unit-timid obstruction | 10 | bc-matched-cylinder-pair | codex-matched-diffuse |
| done | `llm-creative-research-loop` — Apply recent LLM mathematics methods to a tested creative research loop | 10 | bc-matched-diffuse-continuation | codex-creative-loop |
| done | `observer-postselection-boundary` — Derive observer access and its postselection cost from scalar history data | 10 | llm-creative-research-loop | codex-observer-postselect |
| done | `observer-sequential-dilation` — Build coherent observer preparation and readout from individual growth transitions | 10 | observer-postselection-boundary | codex-sequential |
| done | `observer-local-control` — Test whether growth-transition controls can depend only on an observer causal past | 10 | observer-sequential-dilation | native-local-control |
| done | `observer-growth-intertwiner` — Determine whether sequential dilation descends to a symmetry-compatible quotient | 10 | observer-sequential-dilation | native-growth-intertwiner |
| done | `observer-control-resources` — Bound memory and control precision for the sequential observer protocol | 9 | observer-sequential-dilation | native-control-resources |
| review | `stein-core-repairs` — Prepare exact repairs for chronology conventions and first-exit cases | 10 | — | glm-stein-core-repairs |
| review | `stein-gluing-audit` — Independently challenge domain transfer and the flat detour | 10 | — | claude-head |
| claimed | `stein-null-boundary-audit` — Verify residual null freedom and construct a mixed-curvature example | 9 | — | glm-stein-null-boundary-audit |
| open | `stein-causet-audit` — Audit the convex-embedding causal-set theorem and its prior-work contrast | 9 | — | — |
| review | `stein-priority-audit` — Try to defeat novelty of cross-spacetime becoming classifications | 10 | — | glm-stein-priority-audit |
| open | `stein-energy-rigidity-audit` — Check energy-condition rigidity and isolate a legitimate extension problem | 9 | — | — |
| claimed | `stein-interpretation-audit` — Audit what the covariance theorem says about locality and becoming | 8 | — | glm-stein-interpretation-audit |
| blocked | `stein-paper-integration` — Integrate accepted Stein-GR repairs into one source and verification record | 10 | stein-core-repairs, stein-gluing-audit, stein-null-boundary-audit, stein-causet-audit, stein-priority-audit, stein-energy-rigidity-audit, stein-interpretation-audit | — |
| blocked | `stein-final-referee` — Independently referee the frozen integrated Stein-GR manuscript | 10 | stein-paper-integration | — |
| blocked | `stein-energy-pocket-probe` — Test one bounded route to energy-compatible flat-pocket gluing | 7 | stein-energy-rigidity-audit, stein-final-referee | — |
| review | `horizons-independent-redteam` — Independently red-team Unreal Is Not Open before expert circulation | 10 | — | codex-horizons-referee |
| review | `book-exploration-samples` — Park prose book concept and two exploratory chapter samples while keeping paper priority | 2 | — | codex-book-exploration |
| review | `horizons-echo-exactness` — Determine or sharply bound the conformal scalar fixed region on closed dust | 9 | — | glm-horizons-echo-exactness |
| review | `horizons-scalar-priority` — Audit prior work and exact sources for scalar sharpness and antipodal echo | 9 | — | glm-horizons-scalar-priority |
| review | `horizons-echo-robustness` — Test how narrowly the antipodal scalar identity depends on its field equation | 9 | — | glm-horizons-echo-robustness |
| done | `horizons-boundary-fix` — Fix closed fixed-region boundary and nearby echo scope errors | 10 | — | codex-horizons-boundary |
| review | `horizons-perturbation-continuation` — Close primary-source gaps and test actual fixed-event loss under a small field perturbation | 10 | — | codex-horizons-continuation |
| claimed | `horizons-perturbation-referee` — Independently try to break the actual-determination perturbation proof | 10 | — | glm-horizons-perturbation-referee |
| review | `github-current-paper-gates` — Refresh GitHub release gates from current mathematical and philosophical critiques | 10 | — | codex-github-gates |
| claimed | `horizons-philosophy-contract` — Draft a precise openness argument and strongest opponent replies | 10 | — | glm-horizons-philosophy-contract |
| claimed | `horizons-priority-gap-check` — Bound the remaining original-source gaps and priority risk for horizons | 9 | — | glm-horizons-priority-gap-check |
| done | `horizons-bounded-ambiguity` — Quantify bounded hidden-field ambiguity without confusing exact openness and practical prediction | 9 | — | codex-bounded-ambiguity |
| done | `horizons-noisy-record-control` — Separate noisy field records from exact pointwise determination | 9 | — | codex-noisy-record |
| review | `runner-fresh-submission` — Reject inherited reports as new worker submissions | 10 | — | codex-runner-fresh |
| review | `native-horizons-norm-review` — Independently review quantitative ambiguity and noisy-record controls | 10 | — | native-norm-review |
| review | `native-time-bridge-recovery` — Recover precise philosophical contract after GLM quota interruption | 10 | — | native-bridge-recovery |
| review | `native-horizons-source-recovery` — Recover bounded original-source gap audit after GLM quota interruption | 10 | — | native-source-recovery |
| review | `horizons-mass-review-recovery` — Finish interrupted scalar mass proof review and repair its independent control | 10 | — | codex-mass-recovery |
| review | `native-horizons-mass-final-review` — Independently finish the small-mass proof audit after GLM quota failure | 10 | — | native-mass-final |
| done | `horizons-reviewed-integration` — Integrate reviewed mass contrast, norm bounds and philosophical contract into horizons paper | 10 | — | codex-horizons-integration |
| done | `horizons-mass-all-fixing` — Investigate complete loss or survival of extra fixing at positive mass | 10 | — | codex-mass-classification |
| done | `future-truth-preliminary` — Preliminary audit of future truth, existence and event-relative settledness | 9 | — | codex-future-truth |
| done | `future-ground-growing-block` — Audit complete grounds in strongest law-based growing-block account | 9 | — | codex-future-growing |
| done | `future-ground-objections` — Audit objections to truthmaker and local-ground completeness demands | 9 | — | codex-future-objections |
| done | `future-ground-tense-domain` — Reconstruct and test stage-sensitive tense and existence semantics | 9 | — | codex-future-tense |
| done | `future-ground-relativistic-branching` — Audit whether causal-past alternatives constitute branching physical possibilities | 9 | — | codex-future-branching |
| done | `future-ground-coordinator` — Synthesize and red-team a future-truth grounds contract | 9 | — | codex-future-coordinator |
| done | `future-rival-gr-compatibility` — Test existing generalized GR history definition against closed dust | 9 | — | codex-rival-gr |
| done | `future-rival-retrospection` — Audit truth of earlier future-tense utterances without a selected history | 9 | — | codex-rival-retrospection |
| done | `future-rival-selection` — Test whether a covariant actual-history selector can come from same-past data | 9 | — | codex-rival-selection |
| done | `future-rival-coordinator` — Construct paired future-truth interpretations and source access gate | 9 | — | codex-rival-coordinator |
| done | `future-rival-original-chapters` — Reconstruct original bivalent and relativistic rival from essential chapters | 9 | — | claude-rival-chapters |
| review | `future-ground-temporal-asymmetry` — Test principled asymmetry between past-directed and future-directed grounding | 9 | — | codex-ground-asymmetry |
| open | `future-gr-dust-atlas` — Extend dust history correspondence to local patches and manifold postulates | 7 | — | — |
| done | `future-domain-persistence` — Test persistence and edge objections to causal-past existence | 9 | — | codex-domain-persistence |
| review | `lawful-completions-priority` — Kill-test priority and scope of past-preserving Einstein completions | 10 | — | glm-lawful-completions-priority |
| review | `lawful-completions-constraints` — Audit constraint-preserving local control of coupled Einstein futures | 10 | — | glm-lawful-completions-constraints |
| done | `lawful-completions-relational` — Define invariant future outcomes and pointed observer matching | 10 | — | native-lawful-relational |
| claimed | `lawful-completions-coordinator` — Integrate lawful-completion theorem target and exact past-preservation baseline | 10 | — | codex-lawful-coordinator |
| review | `bowtie-horizon-rationale` — Test whether a common-future rationale recovers bow-tie domains under horizons | 8 | — | claude-native-bowtie |
| claimed | `past-shadow-lemma` — Prove the past-shadow criterion for entire-past matching by Cauchy data | 9 | — | glm-past-shadow-lemma |
| claimed | `past-shadow-ltb-numerics` — Numerically check an exact Einstein-dust LTB pair outside the past shadow | 9 | — | glm-past-shadow-ltb-numerics |
| review | `past-shadow-ltb-sources` — Source audit for LTB embedding, Weyl formula, shell crossing and Einstein-dust well-posedness | 8 | — | glm-past-shadow-ltb-sources |
| claimed | `bowtie-horizon-review` — Independent adversarial review of the bow-tie horizon propositions | 8 | — | glm-bowtie-horizon-review |
| done | `lawful-collapse-geometry` — Derive a causal barrier from the supplied Einstein-scalar collapse theorem | 10 | — | native-collapse-geometry |
| review | `lawful-collapse-extension` — Audit complete-past extension of the scalar cone-collapse construction | 10 | — | native-collapse-extension |
| review | `lawful-scattering-regularity` — Close or isolate the smooth-metric and scattering-map regularity gate | 10 | — | native-scattering-regularity |
| review | `lawful-scattering-energy` — Derive exact incoming energy and test a later-pulse compensation mechanism | 10 | — | native-scattering-energy |
| done | `lawful-bowtie-rigidity` — Red-team whole-bow-tie Cauchy rigidity and its ontological scope | 10 | — | native-bowtie-rigidity |
| done | `lawful-historical-potential` — Test exact persistent causal-potential repair against the bow-tie realm | 10 | — | native-historical-potential |
| open | `screening-review` — Adversarial review of the causal-potential screening and rigidity theorems | 9 | — | glm-screening-review |
| review | `prior-art-prediction` — Prior-art audit: prediction and domain-of-dependence literature vs screening claims | 9 | — | glm-prior-art-prediction |
| review | `prior-art-bst` — Prior-art audit: branching space-times settledness vs screening claims | 9 | — | glm-prior-art-bst |
| review | `prior-art-becoming` — Prior-art audit: relativistic becoming literature vs horizon and causal-potential claims | 9 | — | glm-prior-art-becoming |
| done | `lawful-screening-repair` — Red-team repaired smooth screening and fixed-background determination | 10 | — | native-screening-repair |
| review | `lawful-finite-cone-continuity` — Prove the finite-cone continuity needed by fixed-energy scalar control | 10 | — | glm-lawful-finite-cone-continuity |
| review | `lawful-scalar-common-extension` — Extend repaired common-development argument to smooth Einstein scalar matter | 10 | — | glm-lawful-scalar-common-extension |
| review | `ontology-rival-contracts` — Source-faithful rival temporal ontology contracts | 10 | — | glm-ontology-rival-contracts |
| review | `ontology-natural-assignments` — Bounded classification of covariant existence assignments | 10 | — | glm-ontology-natural-assignments |
| review | `ontology-bridge-premises` — Adversarial audit of ontology-selecting bridge premises | 10 | — | glm-ontology-bridge-premises |
| review | `ontology-expansion-equivalence` — Determine genuine extra ontological structure versus redescription | 10 | — | glm-ontology-expansion-equivalence |
| review | `ontology-equivalence-repair` — Repair expansion examples and audit definability quantifiers | 10 | — | glm-ontology-equivalence-repair |
| review | `ontology-bridges-repair` — Rebuild noncircular bridge arguments and their strongest objections | 10 | — | glm-ontology-bridges-repair |
| review | `ontology-rivals-repair` — Repair the grounding and translation test for temporal rivals | 10 | — | glm-ontology-rivals-repair |
| claimed | `lawful-axis-source-review` — Audit exact LOY finite-order inputs for Cartesian axis reconstruction | 10 | — | glm-lawful-axis-source-review |
| claimed | `lawful-axis-lift-review` — Red-team finite-order mass, parity and Cartesian C1,1 lifting proof | 10 | — | glm-lawful-axis-lift-review |
| claimed | `ontology-persistence-review` — Audit chronological versus causal persistence and corrected flat-space census | 10 | — | glm-ontology-persistence-review |

Agent delivery enters review. Only integrated, reviewed work becomes done.

See scripts/agents/README.md for launch, recovery, and review commands.
