# Coordinator review notes

Status: 2026-10-19. Metadata-level review only. It checks record structure and
identifier correspondence, not scientific claims. Lanes are not accepted by this note.

## kb-foundations, kb-formalization, kb-frontier (in review)

Checked programmatically (34 records across three lanes):
- Every record has the required contract fields (`id`, `title`, `url`,
  `checked_on`, `read_depth`, `kind`, `relevance`, `limits`); all `read_depth`
  values are in the allowed set; IDs are unique across lanes.
- All 19 arXiv URLs resolve through the arXiv API, and the recorded titles match.
- `full-text` records carry the extra fields (authors, version, locator,
  assumptions, conclusion, proof status, dependencies, related IDs, open questions).
  Lanes name the locator field differently (`locator`, `section_locator`); a
  downstream consumer must accept both.

Not checked: that any assumption, conclusion, or theorem locator matches its
source. Full-text records need spot-checks against the source before acceptance.

Discrepancies and gaps:
- `frontier/candidates.md` says "15 records"; `sources.jsonl` has 16.
- Formalization: Physlib and AxQM are not pinned to commits and nothing was
  built, so no reuse claim is supported yet.
- Foundations: Malament's primary paper and Stein 1968 were not read. Putnam was
  read only partially (pp. 240-242).
- Frontier: abstract-level only. No candidate has passed the novelty gate.
- Coverage is far under the 60-100 screened / 12-20 deep-anchor targets. The
  `theory-map` gate should treat these lanes as seed material, not a review.
