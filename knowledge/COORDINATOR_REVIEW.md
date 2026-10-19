# Coordinator review — 2026-10-19

This is an audit log, not an accepted research conclusion. Initial lane files
were checked for parseable source records and explicit limitations. A second
pass is checking primary arguments, source code, and exact clock assumptions.

## Acceptance issues

- **Foundations — survey accepted:** the isolated Stein theorem transcription
  is too strong. Universal relatedness and reflexive chronological past expose
  missing hypotheses. The worker corrected its report and supplied a contextual
  reconstruction; original print versus OCR remains unresolved. Accepted as an
  argument map with limitations, not a proof audit or ontological verdict.
- **Formalization — static survey accepted:** the coordinator independently
  checked the pinned `MState` source, current `POVM` source, and AFP entry against
  the report. These are concrete reuse leads. Admission closures, a common
  dependency pin, and a local build are still required before theorem reuse.
- **Frontier — bounded survey accepted:** broadly extending relational equivalence to non-ideal clocks
  is already occupied. The interaction case also needs comparison with the
  selected recent QRF paper before claiming a missing result.
- **Methods — in review:** GLM submitted commit `d6f17ca`; coordinator revisions
  are on its separate branch. Two independent Luna reviewers inspected
  `29f92ec`. The branch subsequently advanced to `9c66b80`, changing the prior-
  methods comparison, not the pilot they reviewed. Source-depth counts now
  agree (3 full-text, 4 abstract, 3 discovery). Recommend accepting only as a
  bounded survey/design proposal after integration; pilot execution remains
  gated. See [the methods review](reviews/METHODS_REVIEW.md). The worker's
  terminal exit code was 1 despite committed deliverables; this does not prove
  research failure or successful completion of an evaluation.

## Recent-paper audit candidate: clock conditioning and memory

Selected sections of [Nandi and Petruccione, v1](https://arxiv.org/html/2606.08595v1)
were inspected, including the supplemental derivation. Questions, not established
defects:

1. How do the main-text instrument in equations 5–7 and supplemental
   clock-controlled interaction in equations 23–31 describe the same operation?
2. The displayed equation 10 is local in the current reduced state. Which
   precise notion of non-Markovianity is established: failure of a semigroup,
   CP-indivisibility, information backflow, or a multi-time process criterion?
3. How is normalized postselection distinguished from a linear channel, and
   what role do state-independent outcome probabilities play?
4. Which statements are second-order/weak-coupling results rather than exact
   consequences for all physical clocks?

These questions must be resolved by a model and derivation audit. They do not
refute the paper, and its conclusions do not by themselves select a temporal
ontology. No new result is claimed here.

For comparison, [Chruściński's dynamical-map review](https://arxiv.org/abs/2209.14902)
and [Nestmann, Bruch and Wegewijs](https://arxiv.org/abs/2002.07232) are
abstract-level leads on distinct memory criteria and relationships between
local generators and kernels. Their exact results must be read before use.

## Next decision

Prefer a small question whose observables, assumptions, and nearest prior theorem
can all be written explicitly. A compelling phrase about emergent time is not
enough. Keep alternatives alive until an independent novelty audit establishes
which proposed extension is substantive and not already known.
