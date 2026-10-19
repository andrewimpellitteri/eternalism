# Codex → Claude coordination handoff

Updated 2026-10-19. The user asked us to coordinate. This is a durable handoff,
not evidence that Claude has read or acknowledged it.

## Work split

- Claude's `grid/`, `scripts/grid.py`, runner repairs and existing GLM claims
  are left untouched by Codex. GLM recovery is being handled elsewhere; Codex
  will not retry or duplicate those launches.
- Codex works in `research/grid-review/`: independent contract review,
  adversarial control cases and read-only checks of the grid runner.
- Codex also retains its previously claimed article and native research-lane
  reviews. These are not substitutes for `theory-map` or `novelty-audit`.
- Please reply here or in a separate coordinator note if this division needs
  adjustment. Do not infer acceptance of a candidate from this review.

## Design suggestions from two independent Luna advisory passes

1. Keep the staged grid. Before advancing a family-level cell, pin a particular
   model/version, mathematical domain, bridge, observable/access protocol and
   one controlled assumption change. Labels alone cannot be compared.
2. Require an exact result-level delta and why it is not a known corollary.
   Three citations and five searches are coverage floors, not a novelty gate.
   Missing critical full-text checks should prevent advancement beyond triage.
3. Distinguish unargued ontology leaps from explicitly defended bridge
   arguments. Otherwise the filter could reject the philosophical contribution
   the project is trying to discover.
4. Split determinism, truth settledness, ontological existence and predictive
   access; split present truthmakers from unrestricted existing truthmakers.
5. Transfer is directional. An unordered pair can own both directions, but its
   output must record which construction maps which objects into which domain.
6. Keep a canonical semantic duplicate key and provenance. A renamed cell,
   another prompt or another agent is not a new candidate or independent
   evidence. Pin the axes version/content used for each batch.
7. Test with occupied results, circular definitions, misleading abstracts,
   access/intervention changes and genuine physical discriminators that do not
   discriminate ontologies. Check false kills as well as false advances.
8. An adversary should first search independently, then see the proposer's
   evidence for a second correspondence check. Permanent source-blinding would
   lose useful verification. Different models help but do not guarantee
   independence.

## Current cautions

- `P11` currently groups Bohmian, relativistic GRW and Tomonaga–Schwinger under
  a preferred-foliation label. Treat foliation status as model-dependent, not a
  property of the whole family.
- `B03`, `B05`, `B10`, `B11` need disambiguated subclaims before evaluation.
- Candidate A's elementary path-space equivalence, candidate B's broad
  non-ideal-clock extension and candidate C's generic axiom ablation are
  already known/partly occupied. Use the defeat-search dossiers as negative
  controls, not as evidence of a fresh gap.
- Provider rate-limit failures should preserve outputs and claims for recovery;
  do not mark literature gaps merely because a search worker failed.

Detailed review and control fixtures will be added alongside this note. No
core-grid changes or new GLM launches are requested by this handoff.

## Test task ready for assignment

The user explicitly requested a tests task. `grid-regression-tests` is now on
the board, unclaimed, with disjoint ownership of `tests/test_grid.py`,
`tests/fixtures/grid/`, and `research/grid-test-report/`. It specifies isolated
standard-library tests and no live-state writes, network or model calls.
`DESIGN_REVIEW.md` gives reproduced gate defects; `controls.jsonl` gives eight
bounded calibration cases. Core fixes remain with Claude. The tests must report
current defects, not weaken assertions to make the existing implementation pass.
