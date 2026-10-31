# Agent report — independent dense-comb review

## Files changed

- `research/agentic-philosophy/result-search-round1/modal-density-review/REVIEW.md` — clause-level audit, direct CC calculations, corrected interpretation, and bounded verdict.
- `research/agentic-philosophy/result-search-round1/modal-density-review/sources.jsonl` — direct primary source record.

## Evidence and conclusion

Read Müller’s open-access version-of-record PDF in full: Definitions 6–12, Theorem 1, footnotes 23–26, pp. 657–662 (DOI 10.1007/s10701-019-00267-x). Verified that the rational comb has exactly the trunk history and one history per rational branch; the order is dense, endpoint-free, and continuous in the stated chain sense; the chain-version prior-choice witness is the relevant maximal shared trunk event for every history pair; and the structure is not featureless. Direct application of Definitions 8–12 yields `cll(t_T)=Q∩(-∞,t)` and distinct CC sets at different trunk events, so `~` is identity on the trunk. This defeats Theorem 1’s “for any history” conclusion.

Correction: the first version of this review had an offshoot quantifier error. Definition 8 requires an existential outside history. For an offshoot event `r_q`, each earlier branch history `h_p` witnesses `p_T` for `p<q`, and `h_T` witnesses `q_T`. The corrected CC set includes every earlier continued transition and the departure transition at `q`. The tail has one CC class, while trunk events have different CC sets, so each whole branched history still has a nontrivial relation. The trunk counterexample is unchanged.

The bounded arbitrary-`D` follow-up is also checked in `REVIEW.md`: all `D⊆R` give Definition-6 structures under the requested nonempty-chain convention; trunk CC equality is equivalent to `D∩[s,t)=∅`; and for nonempty proper `D`, every history has a nontrivial relation iff `D` is not dense. Empty, full, and dense-proper endpoint cases are stated separately. This classification is confined to the comb family.

## Checks

- Maximal directed histories and history-containment sets checked symbolically.
- Density, no endpoints, chain infima/suprema, and PCP checked by cases as documented in `REVIEW.md`.
- CC computed from the paper’s definitions; Fact 4 used only as a cross-check, not as the proof of the trunk result.
- Follow-up verified the arbitrary branch-set order/chain/PCP cases, direct trunk and offshoot CC sets, featurelessness endpoints, and dense versus non-dense classification.
- No grids, installs, agents, thread messages, commits, or edits outside the owned directory.

## Limitations and unresolved points

- No independent priority/erratum search was done.
- No claim about a higher-dimensional relativistic physical manifold, Minkowski embedding, BST_NF, or whole-book framework.
- Sparseness is not shown to be a minimal or sufficient repair. “Arbitrarily small” redistribution has no supplied metric or perturbation map.
- The source lacks a proof immediately following Theorem 1; this review audits the written statement and example rather than reconstructing an intended proof.

## Correction log

2026-10-31 follow-up: corrected the offshoot cause-like-locus calculation after identifying an existential/universal quantifier mix-up. Added the general arbitrary-`D` derivation and the boundary cases to `REVIEW.md`.
