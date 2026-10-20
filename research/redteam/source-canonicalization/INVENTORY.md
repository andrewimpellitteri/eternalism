# Source-copy inventory

Snapshot: 365 records in 22 registers; 302 unique IDs, 59 duplicated IDs, 63 surplus copies, 3 depth conflicts. The source hashes and exact Git cutoff are in `summary.json`. This is a read-only proposal, not a claim that source contents are correct.

`identical-copy` compares source payloads after excluding the two theory-map provenance annotations `inherited_from` and `map_role`; raw differences including those annotations are still preserved in JSONL. `depth-superseding` uses three explicit coordinator decisions, not a general deepest-reading rule.

| ID | Class | Canonical location / decision | Differing fields |
|---|---|---|---|
| `form-afp-schutz-outline` | identical-copy | knowledge/formalization/sources.jsonl:9 | inherited_from, map_role |
| `form-axqm` | identical-copy | knowledge/formalization/sources.jsonl:4 | inherited_from, map_role |
| `form-isabelle-schutz` | identical-copy | knowledge/formalization/sources.jsonl:2 | inherited_from, map_role |
| `form-isabelle-special-relativity` | identical-copy | knowledge/formalization/sources.jsonl:3 | inherited_from, map_role |
| `form-physlib` | identical-copy | knowledge/formalization/sources.jsonl:1 | inherited_from, map_role |
| `form-physlib-minkowski-code` | identical-copy | knowledge/formalization/sources.jsonl:8 | inherited_from, map_role |
| `form-physlib-mstate-code` | identical-copy | knowledge/formalization/sources.jsonl:6 | inherited_from, map_role |
| `form-physlib-povm-code` | identical-copy | knowledge/formalization/sources.jsonl:7 | inherited_from, map_role |
| `found-brading` | identical-copy | knowledge/foundations/sources.jsonl:11 | inherited_from, map_role |
| `found-broad-1923` | identical-copy | knowledge/foundations/sources.jsonl:8 | inherited_from, map_role |
| `found-deasy-2015` | identical-copy | knowledge/foundations/sources.jsonl:10 |  |
| `found-malament-1977` | identical-copy | knowledge/foundations/sources.jsonl:3 |  |
| `found-maxwell-1993` | identical-copy | knowledge/foundations/sources.jsonl:7 | inherited_from, map_role |
| `found-prior-2009` | identical-copy | knowledge/foundations/sources.jsonl:9 |  |
| `found-putnam` | identical-copy | knowledge/foundations/sources.jsonl:6 | inherited_from, map_role |
| `found-rietdijk` | identical-copy | knowledge/foundations/sources.jsonl:5 | inherited_from, map_role |
| `found-sarkar-stachel-1999` | identical-copy | knowledge/foundations/sources.jsonl:14 | inherited_from, map_role |
| `found-sep-malament` | identical-copy | knowledge/foundations/sources.jsonl:4 | inherited_from, map_role |
| `found-stein-1968` | identical-copy | knowledge/foundations/sources.jsonl:1 |  |
| `found-stein-1991` | identical-copy | knowledge/foundations/sources.jsonl:2 | inherited_from, map_role |
| `found-wuthrich-callender` | identical-copy | knowledge/foundations/sources.jsonl:12 | inherited_from, map_role |
| `frontier-canonical-clock-sectors-2026` | identical-copy | knowledge/frontier/sources.jsonl:4 | inherited_from, map_role |
| `frontier-causal-becoming-2015` | identical-copy | knowledge/frontier/sources.jsonl:15 | inherited_from, map_role |
| `frontier-causal-embedding-2026` | identical-copy | knowledge/frontier/sources.jsonl:2 | inherited_from, map_role |
| `frontier-causal-growth-1999` | identical-copy | knowledge/frontier/sources.jsonl:14 | inherited_from, map_role |
| `frontier-emergence-time-qg-2012` | identical-copy | knowledge/frontier/sources.jsonl:20 | inherited_from, map_role |
| `frontier-emergent-spin-glass-2025` | identical-copy | knowledge/frontier/sources.jsonl:17 | inherited_from, map_role |
| `frontier-local-observer-unitarity-2026` | identical-copy | knowledge/frontier/sources.jsonl:5 | inherited_from, map_role |
| `frontier-page-wootters-measurements-2023` | true-conflict | UNRESOLVED: choose and reconcile equal-depth knowledge copies against primary text | assumptions, authors, conclusion, dependencies, inherited_from, limits, locators, map_role, open_questions, proof_status, related_source_ids, relevance, url, version |
| `frontier-qrf-beyond-subsystems-2026` | identical-copy | knowledge/frontier/sources.jsonl:1 | inherited_from, map_role |
| `frontier-qrf-indefinite-order-2022v3` | depth-superseding | knowledge/ico-qrf/sources.jsonl:1 | assumptions, authors, conclusion, dependencies, inherited_from, limits, locators, map_role, open_questions, proof_status, read_depth, related_source_ids, relevance, url, version |
| `frontier-qrf-operational-meaning-2026` | depth-superseding | knowledge/ico-qrf/sources.jsonl:4 | assumptions, authors, conclusion, dependencies, inherited_from, limits, locators, map_role, open_questions, proof_status, read_depth, related_source_ids, relevance, url, version |
| `frontier-records-histories-2016` | identical-copy | knowledge/frontier/sources.jsonl:23 | inherited_from, map_role |
| `frontier-records-time-asymmetry-1993` | identical-copy | knowledge/frontier/sources.jsonl:24 | inherited_from, map_role |
| `frontier-relational-markov-2026` | identical-copy | knowledge/frontier/sources.jsonl:6 | inherited_from, map_role |
| `frontier-relational-trinity-2019v3` | identical-copy | knowledge/frontier/sources.jsonl:9 | inherited_from, map_role |
| `frontier-relativistic-trinity-2020v1` | identical-copy | knowledge/frontier/sources.jsonl:10 | inherited_from, map_role |
| `frontier-smith-ahmadi-interacting-2019` | identical-copy | knowledge/frontier/sources.jsonl:13 | inherited_from, map_role |
| `frontier-spacetime-qrf-2021` | identical-copy | knowledge/frontier/sources.jsonl:11 | inherited_from, map_role |
| `frontier-thermal-clock-relational-2011` | identical-copy | knowledge/frontier/sources.jsonl:19 | inherited_from, map_role |
| `frontier-thermal-noncommutative-2025` | identical-copy | knowledge/frontier/sources.jsonl:16 | inherited_from, map_role |
| `frontier-thermal-time-concept-2024` | identical-copy | knowledge/frontier/sources.jsonl:21 | inherited_from, map_role |
| `frontier-thermal-time-original-1994` | identical-copy | knowledge/frontier/sources.jsonl:18 | inherited_from, map_role |
| `frontier-thermodynamics-clocks-2020` | identical-copy | knowledge/frontier/sources.jsonl:22 | inherited_from, map_role |
| `frontier-time-delocalization-2026` | depth-superseding | knowledge/ico-qrf/sources.jsonl:3 | assumptions, authors, conclusion, dependencies, inherited_from, limits, locators, map_role, open_questions, proof_status, read_depth, related_source_ids, relevance, url, version |
| `meth-diagrammatica-2026` | stale-copy | knowledge/methods/sources.jsonl:8 | assumptions, conclusion, dependencies, inherited_from, map_role, version |
| `meth-sw-lean-2026` | identical-copy | knowledge/methods/sources.jsonl:4 | inherited_from, map_role |
| `seed-axiomatic-relativity` | identical-copy | knowledge/seed-sources.jsonl:2 | inherited_from, map_role |
| `seed-bell-temporal-order` | identical-copy | knowledge/seed-sources.jsonl:11 | inherited_from, map_role |
| `seed-besnard-simultaneity` | identical-copy | knowledge/seed-sources.jsonl:5 | inherited_from, map_role |
| `seed-brading-presentism` | identical-copy | knowledge/seed-sources.jsonl:6 | inherited_from, map_role |
| `seed-causal-becoming` | identical-copy | knowledge/seed-sources.jsonl:8 | inherited_from, map_role |
| `seed-causal-growth` | identical-copy | knowledge/seed-sources.jsonl:7 | inherited_from, map_role |
| `seed-einstein-1905` | identical-copy | knowledge/seed-sources.jsonl:1 | inherited_from, map_role |
| `seed-isabelle-relativity` | identical-copy | knowledge/seed-sources.jsonl:4 | inherited_from, map_role |
| `seed-lorentz-data-2026` | identical-copy | knowledge/seed-sources.jsonl:13 | inherited_from, map_role |
| `seed-physlib` | identical-copy | knowledge/seed-sources.jsonl:3 | inherited_from, map_role |
| `seed-problem-of-time` | identical-copy | knowledge/seed-sources.jsonl:9 | inherited_from, map_role |
| `seed-qrf-proper-times` | identical-copy | knowledge/seed-sources.jsonl:10 | inherited_from, map_role |

## One unresolved choice

`frontier-page-wootters-measurements-2023` has two knowledge copies at full-text depth with differing authors, date, extraction and bibliographic details. The accompanying primary-text spotcheck identifies the arXiv v1 authors as Ladina Hausmann, Alexander Schmidhuber and Esteban Castro-Ruiz, dated 21 August 2023; the ico-qrf author/date fields match, while the frontier fields do not. Source: https://arxiv.org/html/2308.10967v1, header. The coordinator also inspected this header. This supports a correction proposal, but the script deliberately leaves the canonical choice unresolved rather than treating equal depths as interchangeable. Review all extracted fields before designating one copy and replacing other payloads with ID references. See `knowledge/audits/fulltext-spotcheck/clocks-methods/findings.jsonl`.

## Counts reconciled

The brief quoted 320 records / 257 IDs / 59 duplicated IDs / 3 depth conflicts. The current snapshot has 45 more records and 45 more distinct IDs; duplicate and depth-conflict counts are unchanged. The earlier citation-gate snapshot had 360 records / 297 IDs; five additional relational-Markov records were integrated by Claude during this run. No changes to those incoming records were made here. Counts describe the indexed registers and cutoff, not research quality.
