# Bibliography metadata review

Task: `article-working-draft`; review scope: `paper/references.bib` against citation use in `paper/main.tex` and authoritative publisher/arXiv records. I did not edit either manuscript file. Book checks were metadata-only and do not verify the cited books' arguments.

## Findings

The 14 `main.tex` citation keys match all 14 BibTeX keys: no missing bibliography records and no uncited records. Bibliographic identity is otherwise consistent for most entries. The highest-impact correction is `HoehnSmithLock2019`: the BibTeX entry is `@misc` with `year=2019`, so natbib prints a 2019 citation, but the audited text is arXiv v3 revised 13 April 2021 and the paper is published in *Physical Review D* 104, 066001 (2021), DOI 10.1103/PhysRevD.104.066001. The version 3 and journal metadata agree on 2021; the initial arXiv submission date is 29 November 2019. The journal title omits the arXiv title's opening “The.” Proposed treatment: use the journal publication metadata (year 2021, volume and article number) for the bibliographic citation, while stating that the inspected text was arXiv v3 and pinning that identifier/date in the note or URL. This does not claim the journal body was inspected or compared against v3. Keeping the current internal BibTeX key avoids a `main.tex` edit; natbib prints the `year` field, not the key.

`Callender2011` correctly identifies the handbook, year, OUP URL, and editor field; its publisher DOI is omitted. Add the DOI. Three other OUP books are accurately identified but omit available publisher DOIs (`Bourne2006`, `Cameron2015`, `Skow2015`); adding those DOIs improves traceability. These are bibliographic completeness improvements, not content corrections.

Priority checks found no wrong DOI in the listed entries. Brading's 10.1086/673897 is confirmed for the paper at *Philosophy of Science* 80(5), 1101–1111 (2013); it is distinct from adjacent same-issue DOI records. Stein's 10.1086/289609 resolves to his 1991 *Philosophy of Science* article (58(2), 147–167), not the separate 1968 *Journal of Philosophy* paper. This distinction matters because the 1968 DOI formerly propagated elsewhere in project history was wrong (10.2307/2023910); that is not the DOI currently in this manuscript's Stein 1991 entry. Putnam's DOI and volume/issue/pages also match JSTOR's issue contents. McTaggart's DOI and pages match OUP's *Mind* record.

Bernal–Sánchez's title, authors, journal, 2005 year, pages, and DOI match Springer and arXiv metadata. The bibliography URL is unversioned even though the version audited is v3, last revised 15 February 2005. Pin it to `gr-qc/0401112v3`; keep 2005 as the journal citation year. The manuscript's updated `SOURCE_AUDIT.md` records the primary-text spotcheck and limits it to the checked theorem statements; no proof was reproduced. This bibliography task independently checked metadata only.

The remaining book records match the publishers' author/editor, title, publisher, DOI where present, and publication year. I verified metadata only; none of these book arguments was read for this audit. `SmithAhmadi2019` matches the *Quantum* publisher record and its 2019 publication date; the journal record identifies arXiv v3. Full item-by-item findings and exact source URLs are in `metadata-ledger.json` and `metadata-ledger.md`.

## Citation and evidence limits

The title/author/date checks establish record identity only. They do not validate the manuscript's paraphrases. The accompanying `SOURCE_AUDIT.md` already records variable reading depths, limits for Putnam and Stein, and incomplete Brading coverage. No entry should be treated as content-verified from bibliographic metadata. The books were not argument-audited. I did not compile the LaTeX or modify shared source files; coordinator integration/build remains outstanding.

## Recommended acceptance criteria

1. Keep all 14 manuscript citation keys resolvable, with no uncited BibTeX records.
2. Use the 2021 journal-publication year for HSL and explicitly identify arXiv v3 as the text inspected; do not imply that the journal body was checked against v3.
3. Preserve Callender's already-correct editor field; add its authoritative publisher DOI along with the three other OUP book DOIs listed in the proposed patch.
4. Pin Bernal–Sánchez to v3 while retaining its journal year and DOI.
5. Build the paper after integration and check rendered author-year citations and bibliography entries, since the proposed HSL change affects citation year.

## Final integration disposition

I rechecked the integrated `references.bib` against the current `main.tex`: all 14 citation keys still match, with no missing or uncited entries. The HSL entry now uses the 2021 journal metadata and contains the explicit note that the inspected text was arXiv:1912.00033v3, revised 2021-04-13; `SOURCE_AUDIT.md` separately states there was no journal-body collation. This wording does not overstate which edition was read. Callender2011 retains its already-correct editor field; the handbook DOI and the three proposed book DOIs are present. Bernal–Sánchez now points to versioned arXiv v3 while retaining the 2005 journal year and DOI. The coordinator reports that the integrated PDF renders the HSL 2021 citation and handbook editor correctly and that all nine pages were visually reviewed with no layout issues; I did not independently rebuild or visually inspect that PDF.
