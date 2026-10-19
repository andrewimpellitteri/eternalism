# Agent report: kb-novelty-prepass-a

Status: bounded native-recovery pre-pass, submitted for coordinator review.
This is not an independent novelty audit and does not certify that a gap is
open.

## Files written

- `knowledge/novelty-prepass-a/defeat-search.md` — dated query log, screened
  results, assumption/result predecessor comparison, bounded verdict and limits.
- `knowledge/novelty-prepass-a/sources.jsonl` — two new lane-prefixed records:
  Gudder (abstract/opening-summary depth) and Riedel–Zurek–Zwolak (abstract
  depth). Shared records were cited by ID and not copied.

## Fresh reading and reused material

Freshly read from primary pages in this lane: Brightwell et al. arXiv HTML v2,
abstract and selected sections through Theorem 1/Corollary 1; Surya–Zalel v1,
abstract, definitions and extension theorem statement/discussion; Gudder v1
abstract and opening summary. Freshly screened: Riedel–Zurek–Zwolak v2 abstract
and selected introduction paragraphs about formal versus accessible records.
The exact versions and locators are recorded in the log/source records.

Reused without claiming a fresh full-text read: Rideout–Sorkin and
Wüthrich–Callender extractions/records from the saved `kb-causal-sets` lane;
coordinator's `fulltext-reads-causal-sets.md`, `candidate-A.md`,
`contracts-crosswalk.md`; and `research/theory-map/research-contracts.md`.
These were treated as handback notes and checked for consistency against the
fresh Brightwell/Surya pages where relevant. Shared IDs `cs-rideout-sorkin-2000-v3`,
`cs-wuthrich-callender-2015-v1`, `cs-brightwell-2003-observables`, and
`cs-surya-zalel-2020` remain canonical; no duplicate records were created.
After delivery, the coordinator reported that the causal-set lane had been
reviewed and merged, and I read its updated `comparison-candidate-A.md` and
review report. The scope correction is reflected here: conditional record
equivalence applies to records defined as measurable functions of the shared
covariant history; labels are auxiliary gauge structure, not a preferred
foliation. The coordinator's fresh primary re-reads and finite `n <= 5` check
remain coordinator work, not this lane's independent verification.

## Evidence and conclusion

The fresh Brightwell read confirms that the paper's Theorem 1/Corollary 1
characterize covariant measurable questions using stem sets up to measure zero
for the generic CSG family described in Sec. 2 (exceptional cases excluded and
some coupling t_k positive for an index k ≥ 2). Surya–Zalel's Theorem 2.1 is a
complex-valued measure extension result from the cylinder algebra to its whole
generated sigma-algebra; it is not stated as a general theorem for arbitrary
Hilbert-valued measures, and failure on the whole sigma-algebra does not imply
failure on its covariant subalgebra. Gudder explicitly describes classical
growth as a path-space Markov chain and a quantum process on the path Hilbert
space. Riedel et al. provide a separate records/access lead.
The resulting verdict is **partly occupied**: the covariant path-measure side is
substantially occupied; a bounded operational observer-record comparison was
not found in this search, which is not evidence of novelty.

## Checks, limitations, unresolved questions

Identifiers were checked manually against versioned arXiv landing pages/HTML,
with exact versions shown in the records. The Riedel page was also checked for
the full title and v2 date (20 Dec 2013); both related IDs in its record were
verified to exist in the shared sources. No DOI was needed or recorded for the
two new sources. The exact online checker result was: `1 files, 2 records; 2
arXiv IDs and 0 DOI lookups checked: 0 errors, 2 warnings, 0 info`; both warnings
were `datacite unreachable`, while the arXiv version pages opened successfully.
No identifier is used as evidence for a result beyond the source material read
at its declared depth.

Brightwell and Surya–Zalel proof details were not independently reconstructed;
Surya–Zalel's detailed later proofs were not audited. Gudder's construction was
only screened, and Riedel et al. was screened at abstract/selected-introduction
depth. The causal-set
observer-record model, non-covariant access assumptions, and broader stochastic
path-space literature remain unsearched. The lane therefore cannot establish
that the access-model remainder is open. No tests, installs, large runs, agents,
board changes, commits, or shared-seed edits were made.

## Coordinator review (2026-10-19)

Codex reviewed all three files and checked Brightwell v2 Secs. 2–3 / Theorem 1
and Surya–Zalel v1 Theorem 2.1 directly in the primary HTML. Scope corrections
requested and applied: generic CSG hypotheses; complex-valued measure; extension
to the full cylinder-generated sigma-algebra versus a smaller covariant algebra.
The two new identifiers and version dates were independently checked against
versioned arXiv landing pages; Riedel's v2 title includes Part 1. The online
checker reproduced 0 errors and 2 DataCite-unreachable warnings. These manual
checks do not remove the recorded endpoint warnings or constitute proof audits.
Disposition: integrate as a bounded pre-pass; the remaining access question is
not established as open or novel.
