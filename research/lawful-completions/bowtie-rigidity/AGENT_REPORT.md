# Agent report: whole-bowtie Cauchy rigidity

**Submission status: complete; coordinator review pending.**

## Files changed

- `research/lawful-completions/bowtie-rigidity/RESULT.md`
- `research/lawful-completions/bowtie-rigidity/sources.jsonl`
- `research/lawful-completions/bowtie-rigidity/AGENT_REPORT.md`

## Evidence and result

Read the assigned project instructions and task brief, the coordinator's
`BOWTIE_RIGIDITY.md` and `PHILOSOPHICAL_SCOPE.md`, and the required project
readings. Independently tested the geometric claim against a conformal-bump
counterexample: it defeats the stronger inference from an open-bowtie
isometry to ambient metric isometry, but it does not defeat Cauchyness of the
image slice.

Proved the stated geometric lemma using a Cauchy temporal function. The source
slice `t₁=−1` lies in `U₁`. Every target inextendible causal curve has a
past-inextendible tail in `U₂`; pull back and continue only the maximal segment
of that same target curve that remains in `U₂`. If it is future-inextendible
in `M₁`, source Cauchyness gives a crossing; if it ends at the excluded future
set, temporal monotonicity forces a crossing before exit, still on the
original pulled-back curve. For at-most-once, use causal convexity of `U₂` and
pull back any ambient causal segment between two points of `Σ₂`; the resulting
segment contradicts acausality of the source Cauchy surface unless the points
coincide. Spacelikeness alone was not used to assert global acausality.

The dynamical conclusion is kept conditional on same-theory Cauchy uniqueness
with full matter data. The audited Choquet–Bruhat primary note proves the
vacuum MGHD uniqueness theorem and states the conditional extension to
hyperbolic matter systems; it does not itself establish the Einstein–scalar
regularity category needed by the scattering lane. Preservation of marked
events/tangents separately requires a boundary/germ compatibility premise.

## Checks

- Read exact source locators for Bernal–Sánchez Theorem 1.1 and
  Choquet–Bruhat's Theorems II–III and introduction.
- Audited connectedness of the open past set and the maximal continuation
  alternatives in the geometric proof.
- Confirmed the deliverables stay in the assigned directory; no board,
  runner, manuscript, shared seed, commit, install, or child-agent action.

## Limitations and unresolved questions

The result is geometric and conditional; it makes no novelty or ontological
claim. A specific coupled theory must supply a sourced Cauchy-uniqueness
theorem in the relevant regularity category. The conformal-bump example is a
counterexample only to ambient rigidity without field equations, not to the
Cauchy-slice lemma. Marked future readings need the stated extension/germ
condition.
