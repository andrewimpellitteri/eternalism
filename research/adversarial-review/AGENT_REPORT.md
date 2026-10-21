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
