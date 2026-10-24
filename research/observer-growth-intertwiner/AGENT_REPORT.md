# Agent report: observer-growth-intertwiner

24 October 2026. Submission to coordinator review.

## Files changed

- `research/observer-growth-intertwiner/RESULT.md`
- `research/observer-growth-intertwiner/check.py`
- `research/observer-growth-intertwiner/sources.jsonl`
- `research/observer-growth-intertwiner/AGENT_REPORT.md`

## Main result

For the orbit-uniform isometry `J_n` over naturally labelled representatives,
all-input intertwining is equivalent to the appended coefficient from each
source orbit being constant across every child isomorphism class. The actual
phase-bearing and positive maps both violate this criterion at 3-to-4 births:
a four-element one-edge-plus-two-isolates representative can have an
antichain prefix while another has a one-edge-plus-isolate prefix. The first receives a nonzero
source-antichain coefficient and the latter receives exactly zero. The
nonzero interval is approximately `3.0542349977589e-5` in both maps.

This does not conflict with the special-state propagation identities in the
sequential-dilation result. Those establish behavior on selected inputs, not
an intertwiner on every orbit-basis input. Finite representative permutations,
prefix-compatible isomorphisms, and a completed physical gauge action are
kept distinct.

## Evidence and checks

- Read project instructions, required read-first files, task brief, accepted
  sequential-dilation result and independent review, and postselection result.
- Inspected Rideout–Sorkin's primary PDF covariance/natural-label passages and
  the project-recorded full-text passages of Surya–Zalel before implementation.
- Ran `python3 research/observer-growth-intertwiner/check.py`: PASS_OBSTRUCTION.
  It pins `bc-matched-diffuse/check.py` by SHA256 and uses its outward dyadic
  interval transition evaluator. It confirms the actual transition-derived
  coefficient, model normalizer, class multiplicities and the exact zero from
  unique-parent deletion.

## Limits and unresolved obligations

The checker is a minimal finite certificate, not an all-depth theorem or an
independent reconstruction of the model transition law. The result concerns
only the specified orbit-uniform embedding and the two named Kraus maps. Other
quotients retaining parent types, alternative embeddings, and phase conventions
remain open. Full completed-history covariance, physical locality and observer
availability are unresolved. No novelty or temporal ontology assertion is
made.

## Coordinator integration correction

The worker mislabeled one-edge posets as chains; the code's edge signatures
were correct. RESULT/output labels are corrected. The stronger checker now
uses an independent canonicalization/count and tests both models, pins both
helpers, and records the earlier 2-to-3 failure for the explicitly extended
seed-step map with B2=2. The original late schedule is unchanged. No minimum
depth claim is made without specifying which map is defined.
