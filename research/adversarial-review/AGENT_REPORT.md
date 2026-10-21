# Adversarial review closeout

Coordinator, 2026-10-21. **SURVIVE, narrow**, for the labelled scalar theorem
and the conditional common-factor covariant theorem. Native proof,
implementation and source reviews are integrated, as are the completed GLM
scalar review, probe corrections and indicator-measure follow-up. This closes
the review of those precise claims. It does not accept the outstanding rank
candidate, establish global priority, or authorize broader physical claims.

The earlier chronological checkpoint is preserved in
`coordinator/REVIEW_HISTORY.md`; its statements about then-running workers and
pending corrections are historical. This report gives the current disposition.

## Claim-by-claim disposition

| Target | Disposition | Conditions and evidence |
|---|---|---|
| Labelled doubly-principal scalar iff p in [0,1] | SURVIVE | Analytic two-cap bound and disjoint-cylinder variation argument; endpoints separated; native and GLM falsifier attempts found no counterexample. |
| Covariant common-factor iff 0<p<=1 | SURVIVE, conditional | Finite complex measure, all-principal value rule, one common factor, and normalized infinitely-many-post event remain essential. Covariance alone does not imply the rule. |
| DP-only weakening of that rule | KILL | Infinite-block Dirac countermodel with zero factor works for every p; it does not satisfy the all-principal rule. |
| Local-renewal refinement | CORRECTED | Constancy begins at rank two; kappa_1 is unconstrained by the refinement alone. Division arguments exclude p=0,1 where required. |
| Blanket vector semivariation no-go | WITHDRAW | Standard infinite-dimensional indicator measures defeat it. Finite-dimensional and fixed-direction obstructions remain separately valid. |
| Indicator-valued Lalpha realization | ACCEPT AS SCOPE | Reviewed GLM construction, endpoint domain and diagnostics corrected; known functional-analysis construction, not preserved quantum phases. |
| General Banach norm-only domains | SURVIVE ANALYTIC REVIEW; scoped | DP: p=1 or |p|<1, |1-p|<=1. All cylinders: endpoints or both strict inequalities. Native proof audit completed; supplemental GLM review did not finish. |
| Hilbert norm-only disk | SURVIVE ANALYTIC REVIEW; scoped | |p|^2+|1-p|^2<=1. Latent-edge conditional-expectation construction and squared-norm obstruction audited natively. Supplemental GLM review did not finish. |
| Rank-only classification | NOT ACCEPTED | Earlier renewal obstruction is conditional. A further proof candidate is preserved in RANK_FACTOR_NO_GO.md; its new convergence estimates require independent audit. |
| Claude regularized-measure experiment | SEPARATE BOUNDED KILL | Claude's coordinator recovered and committed REPORT.md in 461501a while this closeout was integrating, then accepted that task. This review independently reran only the finite polynomial comparison and establishes one ordinary Abel/Borel obstruction; the recovered report's stronger infinite claims still need independent audit. |
| Lean certificate | FINITE KERNEL ONLY | Existing build and axiom audit passed; it does not encode the infinite measure theorem or establish priority. |
| Clock application | CLOSED IN SEPARATE LANE | The other coordinator recorded a known-result/application outcome. It supplies no new result to this review. |

## Proof, computation and source evidence

`proof/AGENT_REPORT.md` reconstructs the scalar and conditional proofs and
challenges their assumptions. `implementation/AGENT_REPORT.md` records the
baseline, certificate and independent replication checks, including alternative
encodings. `source-priority/AGENT_REPORT.md` and `PRIMARY_EVIDENCE.md` identify
the precise previously inconclusive case and bound the priority search.

The completed second-family review is at
`../adversarial-glm/scalar/AGENT_REPORT.md`, with its coordinator disposition in
`COORDINATOR_REVIEW.md`. Its corrected exact suite passes 26/26 checks. Git and
tool chronology support an initial reconstruction before comparison; the
recovery and corrected checks are explicitly feedback-informed. The supervisor
exited 1 after committing a clean report; this was reviewed as a submission,
not called a successful process exit. Arguments and source correspondence,
not model agreement, support the verdict.

The coordinator re-read Dowker-Zalel 2212.01149v2 Sec. V after Eq. (31): the
paper already suggests computing a cumulative doubly-principal amplitude sum
with techniques for post probabilities. The target's contribution executes
that direction with an explicit bound and classification. It neither poses
the original question nor invents the suggested route. Bombelli-Seggev-Watson
0809.2258v2 Theorem 2.1 and Eq. (2) were also rechecked. Thesis coverage is in
the native source review, not an independent GLM thesis read. A short
mathematical note is defensible; general extension criteria and physical or
philosophical novelty are not established.

Coordinator checks retained and rerun at closeout:

- `coordinator/check_boundaries.py`: 407 exact finite identities through n=5,
  plus the rank-one counterassignment.
- `coordinator/check_renewal_series.py`: 25 coefficient identities through
  degree five. These do not close the missing infinite convergence step.
- `coordinator/check_c0_construction.py`: finite boundary constructions and
  disjoint-family checks at the displayed parameters.
- `coordinator/check_hilbert_environment.py`: 200 exact cylinder moments,
  squared DP level identities and the finite-union witness.
- GLM `check_bounded.py`: 26 exact checks; nonzero failure exit.
- Claude `crosscheck.py 9`: eight stem polynomial comparisons at each rank
  through nine, using saved enumeration aggregates; no enumeration rerun.

The norm-only Hilbert construction changes interference. At p=1/2+i/4 the
union of the three-chain and three-antichain cylinders has original scalar
quantum measure 221/4096 versus 669/4096 in the new realization, although each
cylinder diagonal matches. These are new realizations of selected norm data,
not extensions of the fixed premeasure, off-diagonal decoherence data or
physical dynamics. `proof/VECTOR_FOLLOWUP.md` and
`source-priority/VECTOR_FOLLOWUP.md` recommend appendix-level scope at most.

## Integrated corrections

The reviewed GLM probe corrections are integrated in c63d3cb and their report
at `../probe-corrections/COORDINATOR_REVIEW.md`. The wrong complex parameter,
object-truthiness test, rank indexing and unsupported finite-dimensional
proposal were corrected or withdrawn. The indicator follow-up was integrated
through e7bc238 after endpoint, first-arrival, source-contract and scope fixes;
see `../vector-indicator-boundary/COORDINATOR_REVIEW.md`.

Historical builder artifacts are not silently rewritten and presented as
independent clean passes. Any result manuscript must incorporate these
corrections explicitly, credit the already-suggested calculation, and retain
the source and formalization limits. The two scalar theorems' statements did
not change during this review.

## Stopped and unfinished work

The supplementary rank and norm GLM runs encountered provider transport
timeouts and then produced no completed reports. At the user's closeout they
were stopped with claims, worktrees and logs preserved. They are incomplete,
not accepted and not evidence for either truth or falsity. Monthly search-tool
quota exhaustion was a separate recorded limitation; it must not be described
as a model-usage failure. No further agents are launched by this closeout.

Claude's article revision landed in 09c32b7 before its session limit. At the
initial check its regularization experiment had no final report. Its
coordinator subsequently recovered the returned text and committed the report
in 461501a, accepting the lane as a bounded negative result. That concurrent
commit and its new follow-up task briefs were preserved in this integration.
`coordinator/CLAUDE_CARRYOVER.md` records the interruption and later recovery;
the hash manifest covers the 34 raw files present before the recovered report.
It separates the checks actually repeated here, one explicit ordinary-summability
obstruction, and the remaining independent proof obligations. The unreviewed
new rank proof candidate is also preserved without promotion.

## Paper handoff and remaining limits

The review gate is satisfied for a **short scalar mathematical note only**,
with the conditional covariant variant separately labelled and the accepted
corrections applied. No result paper has been written by this closeout. Do not
make the unfinished rank, generalized regularization or globally new vector
claims part of an accepted theorem package. The norm-only constructions can
serve as carefully scoped counterexamples or an appendix after ordinary
manuscript checking; they supply no new quantum extension of the original data.

Neither temporal ontology, objective passage nor an empirical distinction
between ontologies follows. Those questions still require physical dynamics,
observer access and defended bridge premises. The working philosophical
article and its submission gates remain a separate artifact.
