# Agent report: historical causal-potential audit

## Result

Independently checked the exact finite-slab formula (x\in H(s)\iff |z|<2(B-a)+\sigma-\xi) for spacelike (s=(\sigma,0)), (x=(\xi,z)), including strict null and upper-boundary endpoints. No counterexample was found. The common-future test `|z-y|<2B-\xi-\rho` is valid for all event pairs: the infimum future time is `max{\rho,\xi,(\rho+\xi+|z-y|)/2}`. For spacelike pairs the average term is active; for timelike or null pairs the later endpoint dominates and the test is automatic. The proof then uses the reachable-distance interval as y ranges over the causal-past ball of s.

No substantive counterexample to the coordinator formula was found. One proof detail for the infinite-past case: do not literally use “rho near a” when a=-infinity; for each fixed spacelike pair choose a finite rho sufficiently negative to satisfy the two strict interval inequalities. The scope correction is material: with finite upper conformal endpoint and infinite conformal past, every finite spacelike separation enters (H(s)), so (H=D_{BT}). This includes the flat-slicing de Sitter patch with conformal interval ((-\infty,0)); it must not be used as a counterexample to the historical repair. The exact finite slab ((0,L)\times\mathbb R^3) instead has spacelike bow-tie points outside (H).

Checked the coordinator's scale factor and density by direct substitution into the flat Friedmann equations with Λ=3h², and checked both conformal-time endpoint asymptotics. The dust+Λ model is an exact fixed-matter realization with finite conformal interval, distinct from the scalar scattering family. No observational fit, broad source survey, or ontology/priority claim is made.

## Evidence and checks

- Read `README.md`, `knowledge/README.md`, `knowledge/NOVELTY.md`, the assigned brief, `HISTORICAL_POTENTIAL.md`, `HORIZON_REVIEW.md`, `research/bowtie-horizons/RESULT.md`, and `EXACT_DUST_LAMBDA.md`.
- Read-depth provenance is recorded in `sources.jsonl`. The Correia–Rosenkranz chapter was not reread; the existing project source register is cited only as provenance.
- Symbolic Friedmann substitution: `H=h\coth(3ht/2)`, `H^2=\Lambda/3+8\pi G\rho/3`, `\dot H=-4\pi G\rho`, and `\dot\rho=-3H\rho`. The conformal interval has `L=2^{2/3}\mathrm B(1/3,1/3)/(3hC)`, finite at both endpoints.
- No external search, code run, install, board edit, source manuscript edit, or commit.

## Limitations

The result audits the point-level mathematical definitions supplied by the coordinator. It does not establish that this is Correia–Rosenkranz's uniquely intended interpretation, resolve the location/fusion clause, or show observational discrimination. The infinite-past de Sitter recovery and finite-past dust+Λ non-recovery are model/domain-specific and do not by themselves settle a general ontology claim.

## Bounded diameter-classification review

Independently red-teamed `coordinator/DIAMETER_CLASSIFICATION.md` and found no counterexample under its stated assumptions. The full-slab formula and the equivalence `H(s)=D_BT(s) for every s iff diam(S)<=L` are valid for connected complete positive-dimensional Riemannian spatial sections, including compact spaces, noncompact spaces of infinite diameter, and the boundary case `diam(S)=L`. Hopf–Rinow provides a minimizing segment; its subsegments remain minimizing, so cut loci do not obstruct the attainable-distance interval. The common-future criterion remains valid for timelike/null as well as spacelike endpoint pairs, and its strict upper boundary is correctly excluded by the open slab endpoint.

See `REVIEW_DIAMETER.md` for the inequality audit and scope. The result is conditional on the coordinator's definitions and does not establish philosophical uniqueness, the location/fusion clause, or a novelty claim. The coordinator note was read in full; no new external source was consulted.
