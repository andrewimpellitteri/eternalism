# AGENT_REPORT — P1 source and quotation audit

Task: independent source-accuracy audit of `paper/main.tex` (P1\*\* retarget)
at commit `5a9ec90`, for the coordinator. Output restricted to
`paper/reviews/p1-source-audit/`. No commits, pushes, board edits, or other
repository edits were made.

## Files changed

| Path | Status | Contents |
|---|---|---|
| `paper/reviews/p1-source-audit/REVIEW.md` | new | Quotation/locator table (Q1–Q25), findings A/B/C, the three P1\*\* questions, bibliography checks, limits |
| `paper/reviews/p1-source-audit/AGENT_REPORT.md` | new | This report |

Nothing else in the repository was written. `paper/main.tex` was not modified.
The temp build and PDFs are under
`/private/var/folders/k0/46qrmwrj74gcdwzmbtsxlbpm0000gn/T/opencode/p1src/`
(outside the repo, not committed).

## Target identity

- `git rev-parse HEAD` = `22d82a18a20fbf9a5926d56bdff94c1670f99058`
  ("Update article records for P1-double-prime retarget").
- `git diff 5a9ec90 HEAD -- paper/main.tex` is empty, so the audited text is
  the `5a9ec90` version.
- Compile check from a temporary copy (`paper/main.tex` + `paper/references.bib`,
  `pdflatex` → `bibtex` → `pdflatex` ×2): **8 pages**, no undefined
  citations, no BibTeX warnings.

## Sources, versions and read depths

| Source | Copy used | SHA-256 | Depth |
|---|---|---|---|
| Brading 2013, *Presentism as an Empirical Hypothesis*, *Phil. Sci.* 80(5):1101–1111 | public 11-page published-layout PDF (URL as in `research/article-admissibility/primary-review/SOURCES.md`) | `c93ca072…4bb054` — matches project record | full text extracted (11 pp.); **page images of pp. 1105, 1109, 1110 read** |
| Brading 2015, *Physically Locating the Present*, *SHPS A* 50:13–19 | public 7-page published-layout PDF (same source) | `7caceae7…8f6b` — matches project record | full text extracted (7 pp.); **page image of p. 17 read** |
| Saunders 2000, *Tense and Indeterminateness* | PhilSci-Archive 2241 preprint `for_Pittsburgh.pdf` (12 pp.) | `2f372cdf…105b70` | preprint pp. 1–4 read; published S600–S611 **not collated** |
| Pooley 2013, *Relativity, the Open Future, and the Passage of Time* | PhilSci-Archive 9936 preprint, 14 Aug 2013 (37 pp.) | `8ada9fc6…99ddc` | abstract + introduction (preprint pp. 1–2); rest unread |
| Clifton & Hogarth 1995 | project copy `knowledge/putnam-ablation/primary/clifton-hogarth-1995.pdf` | `1bcf93f9…8fa364` | Thm 1, proof, Cor. 1 (printed pp. 365–367) |
| Stein 1991 | **not inspected**; used `knowledge/audits/stein-printed-pages/PRINTED_VERIFICATION.md` | — | inherited verification (OCR + visual line check of pp. 148–150) only, per brief |
| Mason 2025 preprint / 2026 Synthese | PhilSci-Archive 25374 PDF (25 pp.) | `38312ca4…ca780` | preprint pp. 1, 7–8, 17–18; published version blocked at publisher → abstract only |
| Balaguer 2026, *How to Be a Presentist* | Crossref metadata for book `10.1093/9780197845745.001.0001` and chapter `.003.0011` | — | book and chapter abstracts only; no book text |
| Bibliographic data | Crossref REST API, 2026-10-21 | — | DOI/title/volume/page checks for 8 entries |

## Checks performed

1. **String-level quotation check.** Extracted PDF text with a PDFKit Swift
   script (same technique as `paper/render_pdf.swift`), normalised quote marks,
   dashes, and line-break hyphenation, then searched each quoted fragment from
   `main.tex` as a substring. Every fragment was found verbatim except:
   - P1\* with "the dynamics" is not in the 2013 text (the 2013 wording is
     "dependent on dynamics"; the article appears only in 2015),
   - "Exists relative to me" (source has "exist relative to me"),
   - the Saunders symmetry fragment on the page the paper cites (found on
     preprint p. 2),
   - the n. 6 fragment begins after the source's "I" (verbatim from "can be
     made").
2. **Page-image inspection** of Brading 2013 p. 1105 (n. 3), p. 1109 (present
   definition, defeat condition, nn. 6–7), p. 1110 (P1\*, interaction passage)
   and Brading 2015 p. 17 (P1\*, P1\*\*, "all we need is (a)", "doesn't seem to
   save anything"). This confirms the text extraction and the run of
   page numbers (1101–1111; 13–19).
3. **Locator check per quotation** against the printed page on which the
   phrase occurs (footer/running head), not the PDF page index.
4. **Negative claims.** Checked that Brading neither asserts nor denies
   coverage: 2013 p. 1110 (assumes genuine subsystems; "local, not global") and
   2015 p. 18 (genuine subsystems "smaller in spatiotemporal extent than the
   entirety of spacetime" remains the "crucial question"). The manuscript's
   "Brading does not state (C) or its negation" is correct.
5. **Special-question checks.** (a) formalised as `∀i U_i ⊊ W` against P1\*\*(a);
   (b) against P1\*\*(b) and Brading's gloss that (b) "could be omitted";
   "In order to avoid the block universe, all we need is (a)" compared
   character-for-character after normalisation.
6. **Build check** for page count, undefined citations, BibTeX warnings, and
   the rendered bibliography (`main.bbl`) for title capitalisation, missing
   volume/article data and chapter note formatting.
7. **Depth consistency check** against `paper/SOURCE_AUDIT.md` and
   `research/existence-form/NOVELTY_AUDIT.md`; found the manuscript's
   "abstract/chapter level" label wrong for Mason and its "review record"
   reference dangling.

## Findings (detail in REVIEW.md)

Must fix:

- **A1** P1\* block quote: 2015 wording ("dependent on **the** dynamics") cited
  to both Brading 2013 p. 1110 and 2015 p. 17 under "Its full text is". 2013
  p. 1110 reads "dependent on dynamics".
- **A2** Saunders: one `[p. 3]` covers two quotations; "not only transitivity,
  but also symmetry, is required" is on preprint p. 2 and is truncated before
  "by the presentist" without an ellipsis.
- **A3** "Exists relative to me" is not Brading's text (she writes "exist
  relative to me", as a question, answered "Of course").

Should fix: n. 6 pronoun shift and unmarked omission of the clause supporting
"short-lived"; "In full:" followed by an ellipsis; uncited "as represented in
Minkowski spacetime"; missing locators (Clifton–Hogarth, Stein, Pooley, Mason,
Balaguer, Saunders "whole of reality"); preprint-vs-published pagination;
limits paragraph depth statement; 2013/2015 attribution ambiguity at lines
43–47; n. 3 "Then" step.

Notes: "replaces"; fn. 7 "spatiotemporal" compression; (a) as a reading and the
thing/system quantifier domain; "system-relative" label for Balaguer/Mason;
Mason's credit to Savitt/Rovelli; uncited "often read"; bibliography data.

Passed: P1, P2, present definition, defeat condition, n. 3 phrase, "local, not
global", the "unity of what there is" phrase, P1\*\* in full, "all we need is
(a)", "having the entirety…", 2015 P1\* wording, Stein's dimension clause and
(iv) discussion, Saunders's equivalence-relation quote, "no equivalence
relation", Pooley's routes, Balaguer chapter abstract, Mason perspective claim.

No invented quotations were found. The three alterations are real text in
altered form (2015 wording, capitalised verb, n. 6 clause boundaries), not
fabrications.

## Limitations

- Stein 1991 was not re-inspected; this audit inherits the project's
  OCR-plus-visual verification and cannot certify the printed dash glyph or
  anything on pp. 148–150 beyond that record.
- Saunders and Pooley were read in preprint form only; no published-version
  collation, so no published page numbers are asserted.
- Mason's published 2026 text was not accessible (publisher challenge page);
  all Mason verdicts are about the 2025 preprint.
- Balaguer was checked at abstract level only; the manuscript's use is within
  that depth, but chapter-body claims cannot be certified.
- Brading copies match the recorded hashes but were not collated with a
  publisher-hosted file. Extraction was PDFKit text plus page images, not a
  typeset comparison.
- This is a source audit. It does not adjudicate the coverage argument, the
  Saunders/Pooley responses, or the parity verdict.

## Unresolved questions for the coordinator

1. Which pagination will the paper cite for Saunders, Pooley and Mason? If the
   published versions are not collated, the citations need an explicit
   "preprint p. N" convention in text or bibliography.
2. Is the Mason read depth to be recorded as the 2025 preprint pp. 1–25 (as
   `NOVELTY_AUDIT.md` says), and should the manuscript cite the 2025 preprint
   directly for the "what exists" phrase rather than the 2026 article?
3. Does the author want P1\* quoted in the 2013 wording (the version the text
   first introduces) or the 2015 wording (the version the retarget is about)?
   Either is defensible; the current joint citation is not.
4. Should the Balaguer citation be upgraded to the chapter
   (`10.1093/9780197845745.003.0011`, pp. 212–237) to match the claim's source?

## Coordination

Read-only outside `paper/reviews/p1-source-audit/`. No workboard, runner,
`AGENTS.md`, seed, or manuscript edits; no commits, pushes, merges, resets,
deploys, or agent launches. This submission is for coordinator review, not
accepted completion.
