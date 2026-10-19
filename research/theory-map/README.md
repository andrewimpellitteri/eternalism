# theory-map — assumption and observable map

Status: **worker submission for independent review** (task `theory-map`,
branch `agent/theory-map`, 2026-10-19). This directory integrates the
accepted knowledge-base lanes into a model/version-level comparison graph
without erasing disagreements and without any weighted metaphysical truth
ranking.

## Files

- [`model-graph.md`](model-graph.md) — 32 model/version/interpretation nodes
  in 6 clusters, each citing source records with versions and read depths
  (`N01`–`N32`), plus the graph edge index.
- [`translations.md`](translations.md) — 22 proposed connections (`X01`–
  `X22`); each is an explicit map, a partial map with stated domain and
  failure modes, a labeled conjecture with falsifier, or a pointer into the
  disagreement register.
- [`disagreements.md`](disagreements.md) — 9 precise disagreements
  (`D01`–`D09`), each with parties, the exact disputed assumption, what
  could decide it, and why averaging is prohibited.
- [`research-contracts.md`](research-contracts.md) — 5 candidate research
  contracts (`RC-1`–`RC-5`) with testable mathematical content, predecessor
  comparisons, falsifiers, and novelty-kind separation. None is vetted.
- [`sources.jsonl`](sources.jsonl) — 62 source records: 59 inherited
  verbatim from the lane files (tagged `map_role: inherited` with
  `inherited_from` provenance) and 3 newly checked by this worker
  (`map_role: new-check-by-theory-map`, abstract pages fetched 2026-10-19).

## Method

1. Ingested the four accepted lanes (foundations, formalization, frontier,
   methods) plus the seed, coordinator review, second-pass audits, checks
   cases, and the methods handoff contract. The unit of comparison is the
   model/version + interpretation, per `knowledge/README.md`.
2. Built one node per distinct model/version/interpretation that the lanes
   support at the recorded depths; every node's six comparison fields
   (existence/passage/fixed future; state space, dynamics, causal structure,
   clocks; symmetries, preferred structure, access, boundary conditions;
   observables and empirical status; bridge premises; equivalences,
   contradictions, domain restrictions) are filled **only** from what the
   cited records state. Families the lanes cannot yet support (strong
   growing-block / moving-spotlight formulations) are registered as
   explicitly unmapped nodes rather than given fake content (N07).
3. Connected nodes only where a map could be written from recorded formulas
   (`[map]`/`[partial-map]`); everything else is `[conjectural]` with a
   falsifier. Representation changes are never counted as ontological or
   gauge equivalences; kernel/proof certificates would check encodings only
   (X22).
4. Registered disagreements verbatim-in-place: parties, disputed premise,
   decision procedure. No scores, votes, or averages anywhere.

## Coverage accounting (this map's inputs)

- Source records: 62 (see above). Inherited depths: 12 discovery, 22
  abstract, 21 full-text, 4 code-audited; 3 new abstract checks by this
  worker. Counts are coverage bookkeeping, **not** scientific evidence.
- Clusters: A relativistic kinematics/ontological arguments (7 nodes),
  B causal sets (2), C relational quantum clocks (7), D QRFs and causal
  order (7), E thermal time/records (7 + 2 registered leads), F
  formalization/methods anchors (2).
- Deepest-read lanes: relational-clock full-text set (5 papers) and the
  foundations audit (Stein/Putnam/Maxwell/Sarkar–Stachel). Thinnest:
  canonical quantum gravity (routing node only, via
  `seed-problem-of-time`), strong growing-block/moving-spotlight (N07,
  discovery-depth leads only), collapse/Bohmian preferred-structure
  families (not mapped at all — recorded gap, matching
  `knowledge/SEARCH_LOG.md`).

## What this map deliberately does not do

- No ontology is endorsed, weighted, or ranked; empirical status is
  reported per source claim.
- No equivalence is claimed beyond the sources' stated domains; every
  connection beyond them is labeled conjectural with a falsifier.
- Nothing here is kernel-verified; the map is prose + structured records
  for the review, novelty-audit, and reproduction tasks.
- New claims by this worker are confined to: graph structure, the
  conjecture labels, the three newly fetched abstract records, and the
  research-contract formulations — all flagged as such in place.

## Provenance caveats for reviewers

- Inherited records keep their lane depths; the foundations lane carries
  two bibliographic corrections and an unresolved print-vs-OCR question
  (`knowledge/REVIEW_NOTES.md`, `knowledge/foundations/audit.md`) that this
  map inherits rather than resolves.
- `found-malament-1977` remains abstract-depth; N02's conditions are
  relayed via full-text critics and a secondary exposition, and the node
  says so.
- The three `map-*` records are abstract-page reads only (arXiv landing
  pages, exact versions pinned in the records).
