# Agent report: article re-review

Task: `article-rereview`. Date: 2026-10-21. Worker: independent philosophical
referee. Output directory: `paper/reviews/external-2/` only.

## Files written

- `paper/reviews/external-2/REVIEW.md` — referee report with contribution
  verdict, section-by-section assessment, major issues M1–M10, minor issues
  m1–m15, citation-accuracy table, answers to the assigned checks, and a
  recommendation.
- `paper/reviews/external-2/AGENT_REPORT.md` — this file.

No other files were edited. No commits, board edits, workboard transitions,
pushes, or agent launches were made. `paper/main.tex` was not modified.

## What was read

| Source | Depth | Locator / note |
|---|---|---|
| `AGENTS.md` | full | — |
| `paper/main.tex` | full | source SHA-256 `3f472c449df07b8c1f4484e4dc1136077499254c740db52fd59c70cb1147c312` |
| `paper/REFRAME.md` | full | — |
| `paper/reviews/external-2026-10-21/REVIEW.md` | full | — |
| `paper/reviews/external-2026-10-21/ASSESSMENT.md` | full | — |
| `paper/reviews/external-2026-10-21/REVISION_PLAN.md` | full | — |
| `research/brading-existence/RESULT.md` | full | — |
| `research/admissibility-calibration/RESULT.md` | full | — |
| `research/favoring-account/RESULT.md` | full | — |
| `research/strongest-opponents/RESULT.md` | full | — |
| `paper/SOURCE_AUDIT.md`, `paper/READINESS.md`, `paper/AGENT_REPORT.md`, `paper/verification.json`, `paper/check_records.py` | full | used for read-depth and build-record checks |
| Brading 2013, "Presentism as an Empirical Hypothesis" | full text | public 11-page published-layout PDF, SHA-256 `c93ca072e14c4fd0f1c638ff960db17847231479ec9bf168cf0d69f9644bb054` (matches the project record); text extracted with PDFKit |
| Brading 2015, "Physically Locating the Present" | pp. 17–18 full; earlier sections by search | public 7-page PDF, SHA-256 `7caceae74aebe28d1775561cd307dce50f912570eb1a7f9a709d70c699b08f6b` (matches the project record) |
| Saunders 2000, "Tense and Indeterminateness" | pp. 1–3 full | PhilSci-Archive 2241 preprint, PDF SHA-256 `2f372cdf7a6e88e4445c4d3b1f5d1b707c1be96a521dd0fa40fbac7fea105b70`; published S600–S611 not collated |
| Pooley 2013, "Relativity, the Open Future, and the Passage of Time" | abstract + introduction (pp. 1–3) | PhilSci-Archive 9936 draft of 14 August 2013, PDF SHA-256 `8ada9fc62b31d1f5a0b884891035d98842083bd8e6dbff2af83c238a0ce99ddc`; full 37 pages and published version not read/collated |
| Stein 1991 | not inspected directly | relied on `knowledge/audits/stein-printed-pages/PRINTED_VERIFICATION.md` (printed p. 149; image OCR by the project); the JSTOR scan was not re-read here |

The downloaded PDFs were kept in the pre-approved temporary directory
(`/private/var/folders/k0/.../T/opencode/`), not in the repository. No packages
were installed. Text extraction used a small local Swift/PDFKit script; the
PDFs are text-based, not scans, so extraction is reliable for the quoted words.
The extraction renders parentheses in Brading 2013 oddly (`ðP1Þ`); I normalized
these to `(P1)` when comparing, without altering quoted words.

## Checks performed

1. **Hash check.** Brading 2013 and 2015 PDFs match the SHA-256 values recorded
   in `research/article-admissibility/primary-review/evidence.jsonl` and
   `SOURCES.md`. This confirms the files reviewed are the ones the project
   records as read.
2. **Quotation check.** Compared every quotation in `main.tex` against the
   primary texts: P1 (p. 1101), P1* (p. 1110 / 2015 p. 17), the interaction
   passage (p. 1110), the present definition (p. 1109), the defeat condition
   (p. 1109), the "labeling it 'presentism'" remark (p. 1101), and the P1**
   passage (2015 p. 17). One serious defect found: the P1* quotation in §1
   silently drops "the spatiotemporal extent of that 'present' is dependent on
   dynamics, and," changing the antecedent of "it" (REVIEW.md M3). The
   interaction passage is quoted accurately with an ellipsis.
3. **Textual-target check.** `grep` confirms `main.tex` never mentions P1**;
   the 2015 paper is used in one sentence and is described in §8 as read at
   "abstract/indexed depth." Brading 2015 p. 17 contains P1** and the sentence
   "In order to avoid the block universe, all we need is (a)."
4. **Build check.** Copied `main.tex` and `references.bib` to a temporary
   directory and ran `pdflatex` + `bibtex` + two `pdflatex` passes. Result:
   7 pages, exit 0, no unresolved references, no overfull/underfull box
   warnings. The bibliography renders five entries (Brading 2013, Brading
   2015, Pooley 2013, Saunders 2000, Stein 1991).
5. **Citation-key check.** Five distinct citation keys are cited:
   `Brading2013`, `Brading2015`, `Pooley2013`, `Saunders2000`, `Stein1991`.
   All resolve. `CliftonHogarth1995` is in the bibliography but uncited, even
   though the Saunders paragraph relies on "the definability results" (m9).
6. **Internal-consistency check.** `paper/verification.json` says
   `"citation_keys": 14` and `"exact_example_checks": 5`; the current paper has
   five cited keys, and `paper/check_records.py` tests the finite path/causal
   examples that were cut from the 7-page draft. The build and page-count fields
   are current (source hashes match); the citation and exact-example fields are
   stale. This is a paperwork issue, not a defect in the paper, and it is
   reported here rather than in the referee report.
7. **Read-depth cross-check.** `paper/SOURCE_AUDIT.md` records Brading 2015 as
   read from the full published-layout copy, and `REFRAME.md` §3 requires
   full-text 2013/2015. The draft's §8 limits note says 2015 was read at
   "abstract/indexed depth." The note is inconsistent with the project's own
   records and with the frozen scope document. This is flagged in REVIEW.md
   (m11) and is the likely cause of the P1** omission.

## Summary of findings

Verdict in REVIEW.md: **major revision; no longer a prospectus, not yet a
research contribution.** The paper's argument is aimed at P1* (2013), which
Brading herself replaced with P1** (2015, p. 17) because P1* does not secure the
anti-block result. P1** clause (a) is the paper's local-boundedness condition,
and Brading says (a) is all that is needed to avoid the block. The coverage
non-implication therefore applies to her own strongest formulation, which the
draft never mentions. The paper's other headline claim — that P1* and the
interaction passage support a "system-relative existence" reading — is not
supported and is partly undercut by the paper's own presence/existence
distinction; the passage is better used for the negative verdict. The P1*
quotation is truncated without ellipsis. The four-repair map is useful but
misses the maximal-unity/primitive-actuality options; §6 delivers a schema
rather than a favoring verdict; §5 localizes rather than resolves the
weak/strong dilemma. Saunders and Pooley are reconstructed reasonably and
conceded, but Saunders's public-uniqueness reason and the existence/passage
distinction are not engaged at full strength.

## Limitations

- I did not inspect the Stein 1991 JSTOR scan; the Stein assessment relies on
  the project's printed-page verification. I did not independently verify
  Clifton–Hogarth 1995; the Saunders discussion is checked against the
  Saunders preprint, which paraphrases them.
- Saunders and Pooley were read from preprints, not the published versions; the
  Pooley reading is limited to the abstract and introduction. I did not search
  the wider local-presentism literature, so I make no priority or novelty claim
  about the coverage point.
- Brading 2015 pp. 17–18 were read in full; earlier sections were checked by
  search rather than read continuously. The P1** passage is on p. 17 and was
  read in full.
- The review is a philosophical assessment, not a formal verification. The
  coverage proposition is elementary and was checked by inspection, not by a
  proof assistant.
- I did not assess whether the paper's broader framing (e.g., "dynamical
  presentism") matches any established usage in the literature.

## Unresolved questions for the coordinator / author

1. Does the project accept the P1** retargeting as the right fix? It changes
   §3–§4, the abstract, and the conclusion, but it uses material the project
   already records as read.
2. Which dialectical line does the author adopt: (A) Brading already moved to
   system-relative existence, or (B) she intends P1*/P1** as a presentist
   reformulation and the coverage objection is a criticism? The report
   recommends B with P1** as the target and A as a fallback diagnosis.
3. Is the event-domain regimentation acceptable, or should the argument be
   restated over unities and their extents (Brading 2015 p. 17; 2013 p. 1109
   n. 7)?
4. Should §5 and §6 be cut to short paragraphs, or converted into an actual
   application (eligibility vs discrimination; parity verdict)?
5. Author metadata remains undecided; the "(Working manuscript)" line is still
   in `main.tex`, contrary to `REVISION_PLAN.md`.
6. Should `paper/verification.json` and `paper/AGENT_REPORT.md` be refreshed
   after the rebuild? They still describe the earlier 9-page/14-key draft in
   places.
