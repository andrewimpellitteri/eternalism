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

## Codex recovery after the interrupted Claude session (2026-10-19)

Checked filtered process commands: no old project `agents.py` supervisors or
OpenCode workers remained. Preserved all worktrees and logs. Reassigned only
`kb-gr-qg-time`, `kb-novelty-prepass-a`, and `novelty-audit` to native Luna runs;
the existing causal-set handback was reviewed directly by the coordinator.

- **Causal sets:** integrated `9186c44`; corrected Madsen F2's missing square
  root from primary HTML and restricted record equivalence to specified
  measurable functions of the shared covariant history. Kept unread originals,
  proof limits, and the secondary Stein-transcription problem explicit.
  Source check: 0 errors/warnings. Exact finite check reproduced through n=5.
- **GR/QG:** integrated `56b7094`; bounded comparison of global-time existence,
  cosmological-time regularity, Gödel, canonical constraints and emergent-bulk
  diagnostics. Coordinator checked Bernal–Sánchez statements, Isham's foliation
  premise, and the spin-glass paper's restricted Proposition 1. Online source
  check: 0 errors, 2 unreachable DOI endpoint warnings. Kuchař remains unread.
- **Candidate A pre-pass:** integrated `efdb5f4`; partly occupied, with no
  demonstrated open remainder. Coordinator corrected the generic CSG theorem
  scope and the distinction between complex-valued extension to the full
  generated sigma-algebra and extension to a smaller covariant algebra. Two
  new arXiv records manually checked; automated check has 2 DataCite warnings.
- **Independent novelty audit:** integrated `1646e6e`; explicit no-selection,
  three or more predecessors per contract and exact unmet gates. Corrected a
  nonexistent Surya–Zalel version, retained Stein as an OCR/transcription read,
  and made postselection nonlinearity conditional rather than a diagnosis of
  the unread Nandi derivation. See `research/novelty-audit/AGENT_REPORT.md`.
- **Known bibliography correction:** updated the canonical AQFT 1976
  Bisognano–Wichmann record to title *On the duality condition for quantum
  fields*, DOI `10.1063/1.522898`. Project Crossref metadata cache agrees with
  the DOI's AIP redirect; body unread. This does not accept the AQFT lane.

All four recovery tasks are accepted as bounded research artifacts. Completion
of an audit is not passage through the novelty gate. `baseline-reproduction`
now also depends on the selection-decision gate and requires an actual selected
contract; an explicit no-selection does not authorize implementation.

The user then requested a creative fan-out. Three claimed, isolated native
probes explore finite-clock instrument obstructions, covariant stopping/observer
access, and interventions distinguishing clock memory from system memory. Their
outputs are proposals until separately challenged against primary predecessors
and checked by the coordinator. No ontology is preferred.

Validation: board paths/dependencies remain valid and acyclic. The existing
test suite has 7/8 passing; the live-board test still hard-codes 11 tasks (now
45), tracked by `rt-fix-live-contract-test`. Pre-existing uncommitted edits to
`scripts/agents.py` are preserved and are not part of these research commits.
