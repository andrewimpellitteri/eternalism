# Adversarial review: scalar result survives, vector probe needs correction

Coordinator checkpoint, 2026-10-21. **The gate remains in progress.** Three native
reviews and the coordinator boundary check are complete; two user-authorized
headless OpenCode GLM workers are now running. No second-family result has yet
been received or accepted. The paper gate must remain closed pending review of
those submissions and disposition of the corrections below.

## Findings and disposition

| Target | Verdict | Evidence and scope |
|---|---|---|
| Labelled doubly-principal scalar iff | SURVIVE, narrow | Two-cap bijection, endpoint probability product, positive infinite product and divergent disjoint-cylinder variation checked analytically; p=0,1 handled separately. |
| Covariant all-principal common-factor theorem | SURVIVE, conditional | Requires exactly the all-principal value rule, finite countable additivity and normalized infinite-post mass. Covariance alone supplies none of these dynamics. |
| Doubly-principal-only classifier | KILL | The infinite-block Dirac countermodel satisfies the weakened rule with zero factor for every p. It does not satisfy the full rule. |
| Rank-only measure classification | UNRESOLVED | Stationary kernel is a useful reduction; truncated roots and attenuation do not construct a measure or rule one out. Endpoint, convergence and priority corrections are required. |
| Vector probe's infinite-extension and semivariation claims | REPLACE | The standard L² indicator construction gives a norm-prescribed infinite-dimensional extension on the displayed circle, with semivariation one and infinite total variation. An infinite R² extension outside [0,1] is impossible. |
| Local-renewal refinement | SURVIVE after correction | The common factor starts at rank two; the unused κ_1 is unconstrained. Correct the shape-dependent-factor endpoint qualification. |
| Finite Lean certificate | SURVIVE as finite kernel | No axioms or sorry; it does not encode sigma-algebras, countable additivity, the infinite product or the all-level iff theorem. |
| Clock fallback | OUTSIDE THIS REVIEW | A separate claimed coordinator lane is working on it; its live files were not changed here. |

The scalar theorem solves the specific previously inconclusive doubly-reduced
case in the primary sources checked by the source reviewer. Its estimate is
short and elementary relative to an existing extension criterion. This supports
a narrow mathematical note, not a new general extension criterion, new physics,
global priority or a temporal ontology. See the source-priority report for the
strongest triviality objection, actual search boundaries and exact source reads.

## Material correction: the vector counterexample

For `|p|²+|1-p|²=1`, put `r=|p|²`, take classical labelled percolation `P_r`, and
set `μ(E)=1_E` in `L²(P_r)`. The norm of a cylinder indicator is precisely the
prescribed amplitude modulus. Norm countable additivity follows from probability
continuity on the disjoint tail; finite partitions give semivariation one. The
scalar lower bound gives infinite total variation for nonreal p on the circle.

The full analytic proof, phase/common-direction caveat, finite-dimensional
no-go and independent finite corroboration are in
`coordinator/VECTOR_COUNTERMODEL.md`. This construction is standard functional
analysis applied here; no novelty follows from finding it during this review.
Do not describe it as a phase-preserving quantum dynamics. The pending GLM
follow-up studies only the finite-Lalpha indicator construction's locus, not
all Banach-valued measures.

## Corrections required before a broader presentation

1. Replace the historical vector report's blanket bounded-semivariation no-go
   and its claim that the infinite norm-prescribed extension is wholly open.
   Separate finite-dimensional, bounded-total-variation, fixed-direction and
   general infinite-dimensional statements. Finite polygons do not establish
   extension or newness.
2. Correct local-renewal indexing to n≥2, using κ_2 in the full formula, and
   qualify division-based shape-factor claims at p=0,1.
3. Remove p=0 from the rank-kernel classical `R(1)=1` assertion; make labelled
   multiplicities explicit; do not equate the measure no-go with divergence of
   a complex scalar generating series without a separate proof.
4. Keep rank-only existence and its priority unresolved. A finite root search
   and zero floating residual are insufficient evidence for either claim.
5. Integrate and assess the GLM submissions through their arguments and source
   correspondence before claiming the requested two-family adversarial gate.

`coordinator/BOUNDARIES.md` supplies the rank-one counterassignment and detailed
locations. This review deliberately leaves builder artifacts unchanged and
preserves them as the objects reviewed. No disputed claim has been silently
repaired and then presented as an independent clean pass.

## Evidence, verification and provenance

- `input-manifest.json` pins 24 builder inputs at be41977. Recomputed hashes on
  2026-10-21 found no changes to any pinned input while these reviews ran.
- `proof/AGENT_REPORT.md`: independent analytic challenge to both theorems and
  the vector counterexample, with assumptions separated.
- `implementation/AGENT_REPORT.md`: successful baseline/certificate/replication
  checks, alternative encoding and multiplicity checks, finite formal scope,
  plus a separately recorded later vector correction. Minor replication script
  hygiene is documented there; the analytic theorem does not depend on it.
- `source-priority/AGENT_REPORT.md` and `PRIMARY_EVIDENCE.md`: actual primary
  source sections, bounded citation search, modest significance objection and
  standard vector-measure predecessor with access limitations.
- `python3 coordinator/check_boundaries.py` from this directory: 407 exact
  cylinder identities through n=5 and the κ_1 counterassignment passed. The
  program imports no builder code. This is finite corroboration of the written
  infinite proof, not a substitute for it.
- `python3 scripts/check_sources.py --strict knowledge research/theory-map`:
  23 files, 327 records, zero errors/warnings for those explicit paths. This
  invocation is not described as a scan of every register in the repository.

No installs or large runs. Files changed are this owned review directory only;
separate runner and workboard changes enabling the newly requested GLM runs have
their own task/report at `research/runner-committed-launch/`. The native reviewers
share a model family, so their agreement is not independent statistical evidence.

## Remaining work

Review the two headless GLM submissions when available. Produce an explicit
correction disposition before accepting this gate. Until then, this document is
a review checkpoint and the `adversarial-review` claim remains active; it is
neither an accepted completion nor authorization to advance the paper task.

## Coordinator direction follow-up (2026-10-21)

The user authorized four concurrent headless GLM runs. The two queued workers
were confirmed stopped with clean worktrees and no model events, then resumed
with a four-slot limit; the original two sessions were preserved. All four are
now producing events or awaiting their current model step. No provider error
was recorded at the subsequent check; an initially quiet scalar reviewer began
emitting again without restart.

`coordinator/DIRECTION.md` records the revised project judgment: finish the
narrow scalar result and corrections, keep the rank attempt analytically
bounded, treat the standard vector construction as scope clarification, and
recommend closing the clock application after its separate coordinator review.
The clock coordinator has since committed its negative/application-only outcome
in c0a2176 and the updated reread verdicts in 2e8bfd4.

`coordinator/RENEWAL_OBSTRUCTION.md` gives a conditional renewal-inversion
obstruction and states the missing absolute-convergence obligation. Its exact
finite check passed 25 coefficient identities through degree five. This new
coordinator reduction is not independently reviewed and does not close the
rank-only existence question or the adversarial gate.

## Provisional norm-classification follow-up (2026-10-21)

`coordinator/BANACH_NORM_BOUNDARY.md` now contains a candidate exact
classification for existence in some Banach space when only DP cylinder norms
are prescribed, using a c0-valued weighted conditional-probability measure.
It separately treats the stricter all-cylinder prescription. Its explicit
boundary construction and disjoint-family obstructions passed exact finite
checks in `check_c0_construction.py`. The infinite argument is written out;
independent proof and priority review are still required. This does not
classify Hilbert-valued measures or restore complex phases, and it has not
changed the paper gate or promoted the candidate to accepted newness.

An interim failed GLM certificate check was traced independently to using the
wrong exponent for an ordinal-block weight. `coordinator/INTERIM_GLM_CHECK.md`
records the correct calculation and the printed V_2 edge case. The worker is
still running and its final submission must be reviewed afresh.

## Hilbert boundary and independent analytic follow-up (2026-10-21)

`coordinator/HILBERT_NORM_BOUNDARY.md` gives an exact candidate disk boundary for
the norm-only Hilbert realization problem. A conditional-probability measure in
an independent random edge environment supplies the disk's interior; a Hilbert
sign-average bound on disjoint squared norms and the two-cap estimate exclude
its exterior. The same disk applies to DP-only and all-cylinder prescriptions.
`check_hilbert_environment.py` passed 200 exact finite cylinder moment identities
at four parameters plus the squared DP level formula through rank five.

The independent proof reviewer audited this argument and the Banach c0 domains
analytically in `proof/VECTOR_FOLLOWUP.md`, finding no mathematical falsifier.
Its single wording clarification has been applied. A bounded source/priority
review is now pending. These are realizations of cylinder norm data in new vector
spaces, not extensions of the fixed complex scalar premeasure or its original
decoherence functional. The construction's interference is constructive and its
nonreal boundary is classically additive. Physical claims remain excluded.

`coordinator/ADDITIONAL_SOURCE_READS.md` records a now-readable author route to
Sorkin's fundamental-theorem preprint and the limited sections actually read.
The scope check reinforces the distinction between fixed-premeasure extension
and diagonal-only realization. Earlier unavailable/unread notes are preserved.
The selected scalar statement and paper gate are unchanged.

## Scope-review disposition and finite-union witness (2026-10-21)

`source-priority/VECTOR_FOLLOWUP.md` has completed its bounded primary-source
review. It found no matching exact parameter classification in the searched
sources, but identified standard moment, conditional-probability and c0-coordinate
techniques as the strongest significance defeaters. Recommendation: appendix or
scope-section treatment at most, rather than a separate quantum-extension note.
The Hilbert necessity argument remains a specific use of the squared two-cap
bound; a finite Gram matrix's positive-semidefiniteness does not prove the disk.

An exact finite-union check at p=1/2+i/4 gives original scalar quantum measure
221/4096 versus new Hilbert realization 669/4096 for the union of the three-chain
and three-antichain cylinders, despite matching each cylinder diagonal. This
makes the changed interference predictions explicit. The analytic proof audit
and scoped source verdict support the norm-only classifications without
conflating them with the original premeasure's extension problem.

The first GLM correction submission is now in review. Its claimed quota
interruption and exact complex-parameter checks must be verified rather than
copied from its handback; the coordinator is inspecting these before integration.
