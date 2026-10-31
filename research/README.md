# Research index

Every lane under `research/`, grouped by what it is for. Paths stay where they are on purpose:
24 scripts, several hash manifests, the workboard and the archived GitHub issue bodies all key on
them, so moving a folder would break the checks that make the results reproducible.

Groups are editorial and say nothing about whether a result is correct. For that, use the
[claim ledger](CLAIM_STATUS.md). For work nobody has signed off, use the
[review queue](REVIEW_QUEUE.md).

## Start here

| Document | Use it for |
|---|---|
| [The unified paper](what-the-past-can-fix/what-the-past-can-fix.pdf) | The main output: 42 pages, four parts |
| [Paper red-team](what-the-past-can-fix/REVIEW.md) | What is tight and what is only a survey |
| [Claim ledger](CLAIM_STATUS.md) | Status of each claim and its dependencies |
| [Current synthesis](CURRENT_SYNTHESIS.md) | The dated narrative, newest first |
| [Parity map](PARITY_MAP.md) | How far the repo is from the field of time, and the order of work |
| [Review queue](REVIEW_QUEUE.md) | The 62 tasks with no sign-off |

## The paper and its two source manuscripts

`what-the-past-can-fix/parts/` is generated from the two manuscripts by `assemble.py`. Repair the
sources or the script, not the generated files.

| Lane | What it is |
|---|---|
| [what-the-past-can-fix](what-the-past-can-fix/) | The unified paper |
| [stein-gr](stein-gr/) | Part I source: Stein's theorem in general relativity |
| [horizons](horizons/) | Parts II and III source: fixing, horizons, massive classification |

## Current work feeding the paper

| Lane | What it is |
|---|---|
| [time-direction](time-direction/) | First parity step: the arrow read. Not yet red-teamed |
| [lawful-completions](lawful-completions/) | Part III: past-preserving Einstein completions, screening, rigidity |
| [ontology-reconstruction](ontology-reconstruction/) | Part IV: rival contracts, bridges, persistence, constitutive tests |
| [agentic-philosophy](agentic-philosophy/) | Literature audit, totality and metaontology reads, result search |
| [bowtie-horizons](bowtie-horizons/) | Common-future rationale for bow-tie domains |
| [bowtie-horizons-prior-art](bowtie-horizons-prior-art/) | Prior-art audits for the screening claims |
| [bowtie-horizons-screening-review](bowtie-horizons-screening-review/) | Adversarial review of screening and rigidity |
| [future-truth-preliminary](future-truth-preliminary/) | First audit of future truth and settledness |
| [future-truth-grounding](future-truth-grounding/) | Grounds in the law-based growing block |
| [future-truth-rivals](future-truth-rivals/) | Paired future-truth interpretations |
| [future-truth-rival-chapters](future-truth-rival-chapters/) | Rival reconstructed from original chapters |
| [future-ground-asymmetry](future-ground-asymmetry/) | Past-directed versus future-directed grounding |
| [future-domain-persistence](future-domain-persistence/) | Persistence objections to causal-past existence |
| [local-fragmentalism](local-fragmentalism/) | Strongest local-fragmentalist view and its red-team |
| [where-openness-lives](where-openness-lives/) | Early proved note on where the open future lives |
| [brading-universe-frontier](brading-universe-frontier/) | Idea note on the universe case. Discovery depth only |

## Causal sets and observers (programme closed)

The earlier programme. Its surviving result is the complex-percolation note in `paper-novel`.

| Lane | What it is |
|---|---|
| [paper-novel](paper-novel/) | The complex-percolation theorem note |
| [creative](creative/) | Creative passes behind the extension boundary |
| [extension](extension/) | Task report only |
| [extensions](extensions/) | Rank factor, vector measure and covariant value rules |
| [longshots](longshots/) | Long-shot bets on measures, birth order and Bell-causal phases |
| [adversarial-review](adversarial-review/) | Attempts to break the result and its novelty |
| [adversarial-glm](adversarial-glm/) | Fresh GLM challenge to the scalar theorems |
| [replication](replication/) | Independent rederivation of the two-cap bound |
| [proof-audit](proof-audit/) | Lean certificate and meaning audit |
| [novelty-audit](novelty-audit/) | Challenges against the closest prior work |
| [novelty-verdict](novelty-verdict/) | Whether the selected result is new |
| [rank-renewal-convergence](rank-renewal-convergence/) | Rank-only no-go, convergence obligation |
| [rank-renewal-followup](rank-renewal-followup/) | Analytic bounds follow-up |
| [vector-indicator-boundary](vector-indicator-boundary/) | Scope of the vector counterexample |
| [vector-norm-adversarial](vector-norm-adversarial/) | Falsification attempt on norm-only classifications |
| [probe-corrections](probe-corrections/) | Reviewed vector and probe corrections |
| [qbc-holonomy](qbc-holonomy/) | Operator-valued Bell-causal phases |
| [refocus-2026-10-21](refocus-2026-10-21/) | CPOBC correspondence and the refocus decision |
| [operational-stability](operational-stability/) | Stability boundary of finite-history amplitudes |
| [event-filter-resources](event-filter-resources/) | Cost of event filters |
| [record-loss-robust](record-loss-robust/) | Interference with partial record access |
| [clock-action-audit](clock-action-audit/) | Finite-clock comparison repair |
| [covariant-observer-witness](covariant-observer-witness/) | Covariant observer access to the unstable event |
| [observer-access-audit](observer-access-audit/) | Class membership versus event filtering |
| [observer-control-resources](observer-control-resources/) | Memory and precision bounds |
| [observer-growth-channel](observer-growth-channel/) | Causal-set observer channel |
| [observer-growth-intertwiner](observer-growth-intertwiner/) | Whether sequential dilation descends to a quotient |
| [observer-local-control](observer-local-control/) | Controls depending only on an observer's causal past |
| [observer-postselection-boundary](observer-postselection-boundary/) | Postselection cost of observer access |
| [observer-sequential-dilation](observer-sequential-dilation/) | Coherent preparation and readout |

## The earlier article (closed)

These lanes fed the admissibility article in [`paper/`](../paper/), which is not the unified paper.

| Lane | What it is |
|---|---|
| [article-admissibility](article-admissibility/) | Admissibility standard against the strongest rival |
| [admissibility-calibration](admissibility-calibration/) | Calibrating specification burdens |
| [brading-existence](brading-existence/) | The Brading coverage problem |
| [bridge-defense](bridge-defense/) | Bridge principle defence |
| [existence-form](existence-form/) | Form-of-existence trilemma |
| [examples-scope](examples-scope/) | Example and scope decisions |
| [favoring-account](favoring-account/) | Defeasible favoring |
| [strongest-opponents](strongest-opponents/) | Saunders and Pooley at their strongest |
| [source-gates](source-gates/) | Source gates for the article |
| [paper-priority](paper-priority/) | Priority audit and referee-style review |
| [discriminators-audit](discriminators-audit/) | Proposed empirical discriminators |
| [philosophy-completion](philosophy-completion/) | Completion and access dilemma essay |
| [conclusions](conclusions/) | 21 October bounded synthesis |

## Process and infrastructure

| Lane | What it is |
|---|---|
| [redteam](redteam/) | Citation gates, source canonicalization, selection gate, cross-model pilot |
| [theory-map](theory-map/) | Assumption and observable map from the first phase |
| [gates-2026-10-27](gates-2026-10-27/) | Exact public issue bodies. Do not edit |
| [grid-review](grid-review/) | Idea-grid gate review |
| [grid-test-report](grid-test-report/) | Idea-grid test report |
| [runner-committed-launch](runner-committed-launch/) | Runner change report |
| [runner-fresh-submission](runner-fresh-submission/) | Runner change report |
| [runner-report-handback](runner-report-handback/) | Runner change report |

## Parked

| Lane | What it is |
|---|---|
| [book-exploration](book-exploration/) | Prose book concept and two sample chapters |

## Older planning notes

[RESEARCH_PATHS.md](RESEARCH_PATHS.md) and [NOVELTY_SPRINT.md](NOVELTY_SPRINT.md) are historical
and carry their own status notes. Neither sets current direction.
