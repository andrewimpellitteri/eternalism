# External review and submission gates

The local workboard (`WORKBOARD.jsonl`, `scripts/agents.py`) remains the
authoritative state for task claims, worktrees, quotas and execution. GitHub
Issues are used only for a small number of **external gates** with public,
publication-safe acceptance criteria.

Do not mirror every board task into an issue. Do not put confidential referee
text, unpublished priority details, private data or copyrighted scans in an
issue. Keep those in the repository's local review directories.

## Gate issues

| Issue | Gate | Scope | Local tasks / evidence |
|---|---|---|---|
| [#1](https://github.com/andrewimpellitteri/eternalism/issues/1) | Theorem note external review | `research/paper-novel/` | `paper-novel-result`; `REVIEW_PACKET.md`, `verification.json` |
| [#2](https://github.com/andrewimpellitteri/eternalism/issues/2) | Article reframe and substantive application | `paper/main.tex` | `article-reframe-scope`, `brading-existence-bridge`, `admissibility-burden-calibration`, `favoring-account`, `strongest-opponents`, `examples-scope-cleanup`, `article-rebuild-integration`, `article-rereview` |
| [#3](https://github.com/andrewimpellitteri/eternalism/issues/3) | Rank-only no-go independent audit | `research/rank-renewal-convergence/` | `rank-renewal-convergence`; `COORDINATOR_REVIEW.md` |
| [#4](https://github.com/andrewimpellitteri/eternalism/issues/4) | Source closure and correspondence | Stein, Putnam, Zalel thesis, DZ pagination | `paper-source-gates`, `knowledge/audits/stein-printed-pages/` |
| [#5](https://github.com/andrewimpellitteri/eternalism/issues/5) | Submission decision and release sign-off | final release only | all of the above |
| [#7](https://github.com/andrewimpellitteri/eternalism/issues/7) | Stein-GR proof scope and locality premise | `research/stein-gr/main.tex` | proof-lane dispositions; `stein-interpretation-audit` |
| [#8](https://github.com/andrewimpellitteri/eternalism/issues/8) | Horizons determination and claim correspondence | `research/horizons/main.tex` | `horizons-independent-redteam`, `horizons-boundary-fix`, `horizons-philosophy-contract` |
| [#9](https://github.com/andrewimpellitteri/eternalism/issues/9) | Philosophical bridge, openness and strongest opponents | current papers and local-fragmentalism interpretation | `horizons-philosophy-contract`, `stein-interpretation-audit` |
| [#10](https://github.com/andrewimpellitteri/eternalism/issues/10) | Optional mass-extension proof and scope | `research/horizons/continuation-2026-10-27/` | `horizons-perturbation-referee`, `horizons-priority-gap-check` |

`#5` remains `status:blocked` until the gates applicable to an explicitly
selected submission bundle are satisfied. The original causal-set note (#1),
legacy article (#2) and rank result (#3) are not automatically dependencies
of the newer papers: record their exclusion or deferment without falsely
closing their independent gates. #4 applies to sources actually used by the
selected manuscript. #10 is required only if the optional mass extension is
included. #9 checks philosophical claims actually made, not whether every
mathematical result vindicates a temporal ontology.

## Current-paper acceptance contract, 27 October 2026

The working focus is Stein-GR and horizons, not a final author-approved release
selection. Exact public issue bodies and dispositions are archived in
`research/gates-2026-10-27/`. No inspected issue was closed in this refresh:
drafting, internal review and a build are not external release approval.

- **Mathematical scope:** freeze the source/PDF and account for every worker
  submission. Geometric sufficiency is not dynamical necessity. An exact
  law-relative statement specifies the background, permitted solutions, past
  data, observables and separating alternatives.
- **Philosophical scope:** distinguish existence, tense/passage, lawful
  alternatives, semantic unsettledness, knowledge and practical prediction.
  State the laws and global solution restrictions as additional premises.
  Give the strongest determinist growing-block and eternalist replies;
  identify the inference constrained, not an ontology selected by definition.
- **Locality:** defend cross-spacetime naturality independently; distinguish it
  from signalling and microcausality. Compare clock-equipped and restricted
  categories charitably. Treat transitivity as a premise, not a lexical proof.
  State off-shell versus physical Einstein-matter scope.
- **Interpretive value:** if local fragmentalism is advocated, specify what its
  grounding/explanation adds beyond causal restriction in eternalism. Preserve
  appropriate empirical/truth-conditional equivalence. Do not demand such a
  defense from a paper that explicitly limits itself to conditional mathematics.
- **Robustness:** an optional extension must show actual loss of fixing at a
  specified interior target, not only failure of an echo identity. Distinguish
  constant rescaled potential from ordinary dust mass and exact fixing from
  finite-precision prediction. The new derivation is not accepted just because
  the numerical controls or a GLM run finish.
- **Sources:** exact original passages or honest unread status; no priority
  certificate from failed searches, inaccessible books or secondary summaries.
  A waiver narrows the claim and does not turn an unread source into evidence.

## How to check a gate

Read-only helper: `python3 tools/gh-gates/check_gates.py` (or `--json`).
It only calls `gh issue view` and never writes to GitHub. Manual equivalent:

```sh
gh issue view 1 --json number,title,state,labels,url
gh issue view 2 --json number,title,state,labels,url
gh issue view 3 --json number,title,state,labels,url
gh issue view 4 --json number,title,state,labels,url
gh issue view 5 --json number,title,state,labels,url
gh issue view 7 --json number,title,state,labels,url
gh issue view 8 --json number,title,state,labels,url
gh issue view 9 --json number,title,state,labels,url
gh issue view 10 --json number,title,state,labels,url
```

A gate closes only with evidence in the issue or a linked commit. Closing an
issue without evidence is the same failure mode as accepting a task without
review. Do not close a gate from a worker; the coordinator does it at release.

## Labels

- `gate:submission` — release/submission gate.
- `gate:review` — independent review gate.
- `gate:source` — source-access gate.
- `gate:decision` — author/coordinator decision.
- `status:blocked` — blocked by an unmet gate.
- `area:paper`, `area:article`, `area:rank` — scope.

## Reopen rules

- #1 reopens on a counterexample, a prior proof of the doubly-principal
  classification, or a source mismatch.
- #2 reopens if the rebuilt paper still ends as a prospectus or the Brading
  existence argument fails.
- #3 reopens on a gap in the imported two-cap/laminar frame or a normalized
  rank-only measure outside `(0,1]`.
- #4 reopens on a contradicting scan, an available thesis, or an edition change.
- #5 reopens if any upstream gate reopens or the release commit changes.
- #7 reopens on a proof/category mismatch or an inference beyond the admitted
  spacetime class.
- #8 reopens if solutions/observables change or summary language upgrades a
  geometric guarantee into necessity.
- #9 reopens if bridge premises change or an ontological conclusion exceeds
  the defended argument.
- #10 reopens if the physical perturbation, data, target, solution class or
  novelty claim changes.
