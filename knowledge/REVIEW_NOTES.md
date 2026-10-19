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

## Spot-check: kb-foundations full-text records (2026-10-19)

Verified against Crossref:
- `found-stein-1991`: **DOI wrong.** Recorded 10.1086/289737; Crossref gives
  10.1086/289609 for Stein, Phil. Sci. 58(2), 147-167. Journal, volume, pages
  and year are correct.
- `found-maxwell-1993`: **pages wrong.** Recorded pp. 327-344; Crossref gives
  pp. 341-348 (Phil. Sci. 60(2), a "Discussion" piece, DOI 10.1086/289737, which
  is correct). The recorded locator "p.343" falls inside the true range, but the
  wrong page range casts doubt on how the text was accessed.

Not verifiable by the coordinator: the cited URLs (paperzz.com, philpapers.org)
return Cloudflare challenges or 403 to curl and WebFetch, so the p.159 (Stein)
and p.343 (Maxwell) claims and the `full-text` read depth could not be
independently confirmed. Until re-checked from an accessible copy, treat
`read_depth` for these two records as unconfirmed and the argument-map content
that rests on them as unaudited. Putnam (already marked partial) was not rechecked.

Recommendation: do not accept `kb-foundations` until the two bibliographic
fields are corrected and the page-level claims are confirmed from a copy a
reviewer can open.
