# Prior-work knowledge base

The seed dates from 2026-10-19 and contains source-page and abstract-level
screening, not a systematic review or completed proof audit. The initial search
found relevant existing work; it does not establish that any proposed gap is new.
Later lanes read further at the depths their own records state.

## Current integration

The [28 October synthesis](../research/CURRENT_SYNTHESIS.md) and
[claim ledger](../research/CLAIM_STATUS.md) connect later research and supersede
outdated status summaries. Source depths remain controlled by each lane’s
records; integration does not upgrade unread sources or close novelty gates.

## Files

- `PHILOSOPHY_OF_TIME.md`: dense, source-linked map of ontology, tense, passage,
  persistence, openness, physical constraints, experience, arguments and gaps.
- `philosophy/sources.jsonl`: added philosophical/historical/physics reading
  register; mostly discovery/abstract depth, not a completed deep audit.
- `seed-sources.jsonl`: primary-source leads already checked at the stated depth.
- `SEARCH_LOG.md`: search coverage, queries, and missing areas.
- `NOVELTY.md`: candidate contributions, nearest predecessors, and rejection gates.
- `COORDINATOR_REVIEW.md`: cross-lane checks, unresolved issues, and acceptance limits.
- Task-owned directories will contain source records, argument maps, theorem
  extractions, and reproducibility notes. Workers never append concurrently to
  the shared seed.

## Source record contract

Each lane writes its own `sources.jsonl`. Use stable lane-prefixed IDs. Required:
`id`, `title`, `url`, `checked_on`, `read_depth`, `kind`, `relevance`, `limits`.
For full-text records add authors, exact version/DOI, section or theorem locator,
assumptions, conclusion, proof status, dependencies, related source IDs, and open
questions. For code, pin a commit and record what actually built locally.

`read_depth` is one of `discovery`, `abstract`, `full-text`, `reproduced`, or
`code-audited`. For a repository README alone use `discovery` and say so.
Separate publication status from confidence in correctness. Recent preprints
remain claims to examine, even when their titles sound decisive.

## Theory comparison contract

The unit of comparison is a particular model/version plus interpretation, not
a broad label such as "quantum gravity". Record:

1. What exists; whether passage is fundamental; whether the future is fixed.
2. Mathematical state space, dynamics, causal structure, and clock construction.
3. Symmetries, preferred structures, observer access, and boundary conditions.
4. Observable predictions and empirical status, separately from metaphysics.
5. Philosophical bridge premises and possible alternative interpretations.
6. Known equivalences, contradictions, counterexamples, and domain restrictions.

Map many papers to these shared questions before attempting synthesis. Do not
average incompatible theories into a composite "truth score".

## Initial coverage target

Screen broadly across classical relativity and cosmology; presentism, eternalism,
growing block and moving spotlight; relativistic/local becoming; causal sets;
relational quantum clocks and Page-Wootters; thermal time and records; quantum
reference frames and indefinite causal order; canonical quantum gravity; and
emergent spacetime. Collapse duplicate papers into research lineages. The first
pass targets 60–100 screened sources and 12–20 deeply read anchors, with counts
reported as coverage, never as scientific evidence. Revise those targets when
the search reaches diminishing returns.

Search the last 90 days separately from foundational work. Expand references
backward and citations forward from every serious candidate. Record exclusions,
contradictions, failed replications, and competing formulations.

