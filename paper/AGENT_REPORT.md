# Reviewed article working draft

Task: `article-working-draft`; existing claim: `codex-article`. Date: 2026-10-20.

## Work completed

Resumed the existing Codex article claim. The user's native-subagent instruction
supersedes the GLM default. Claude retains the failed GLM claims and literature
recovery; no such task was stopped, released, reassigned or resumed by this work.

Three native reviewers had disjoint argument, evidence and bibliography output
directories under `paper/reviews/`. Reports and dissent are preserved. The
coordinator edited article-owned sources and ledgers, rebuilt the existing PDF
and inspected its rendering. The novelty and selection gates remain unmet.

Manuscript changes clarify our Callender/Maudlin inference, the clock-rate bridge,
preregistered admissibility commitments and sensitivity to alternative profiles,
Stein's printed p. 149 theorem, whose display omits condition (iv) and requires
the contextual premise, the proposition's matched-kernel premise, the intervention's
exogenous variable, and smooth Cauchy slicings. The admissibility defense remains
under-developed. Frozen Brading and prospective physical claims were not expanded.

The source ledger records the new complete public journal-paginated Brading read,
with publisher-file collation and record reconciliation still open; a bounded
McTaggart pp.458-461 primary-passage check; and the existing Bernal-Sanchez primary
statement-level spotcheck. These are not shared knowledge-record depth upgrades.

The bibliography renders Hohn-Smith-Lock as 2021 while identifying arXiv v3 as the
text inspected; no journal-body comparison is implied. Four publisher DOI additions
improve traceability and Bernal-Sanchez's URL pins v3. Callender's editor field was
already correct; an initial reviewer misreading was corrected. All 14 citation keys
resolve. Metadata checks do not establish the books' arguments.

## Verification

- `python3 paper/check_records.py`: all five exact tests pass. They cover path laws,
  marginals, adaptive prefix access, intervention differences and marginalized
  evidence. They do not reproduce a physical paper or prove an ontology theorem.
- Existing pdfTeX/TeX Live 2026: pdflatex, BibTeX and two final LaTeX passes succeed
  without unresolved references, LaTeX errors or overfull hboxes.
- Existing macOS PDFKit with Swift 6.4 renders all nine pages. The coordinator
  visually inspected pages 1-9: equations, text, headings, citations, references
  and page numbering are legible without clipping or overlaps. The rendered HSL
  citation uses 2021 and the handbook entry identifies its editor.
- `verification.json` records tool/build information, 14-key correspondence,
  exact-test outcome, visual coverage and source/output hashes.
- Final argument and bibliography reviews found no introduced logical/quantifier
  blocker or citation orphan. Reviewers distinguish their checks from the
  coordinator's compilation and visual inspection.

The PDF skill's edit marker ran successfully once before authoring. No packages
were installed and no paid external model calls, uploads, publication or submission
occurred. Build logs and page PNGs are under ignored `tmp/pdfs/article/`.

## Strongest contrary evidence and limits

The argument reviewer finds the admissibility standard and positive explanatory
route under-defended; symmetry alone does not establish non-circularity. Strongest
published defender/critic arguments remain to be reconstructed. The probability
proposition assumes preservation and is not offered as novel. Source-record
reconciliation, complete predecessor/priority assessment, physical target
selection and later result-level review remain open; the Stein printed-page
comparison is closed.
A full Brading read alone establishes neither her proposed discriminator nor
her ontology.

This completes a reviewable provisional article, not an accepted scientific result
or a submission-ready manuscript. Generic authorship remains until human authorship
and affiliation are decided. Workboard review/acceptance is recorded by the
coordinator after the named-file commit. No knowledge register, paper-ledger task,
runner, grid, shared seed or other worker's worktree was changed by this task.

## External review, 21 October 2026

The external report is preserved in `reviews/external-2026-10-21/`. It accepts
the central methodological claim but not the draft as an original research
contribution. The concrete Stein error is fixed: adding non-universality does
not recover the causal-past characterization; the reflexive strict
chronological past is a counterexample, and causal-past inclusion is the
missing premise. The quantum paragraph is relabelled as a one-dimensional
diagnostic. The architectural objections are assessed in `ASSESSMENT.md`; the
rebuild options are in `REVISION_PLAN.md`. The draft is not submission-ready as
a research paper.

## Reframe integration, 21 October 2026

The working draft was rebuilt around one application: Brading's system-relative
present and the coverage objection. The quantum, record, LAGEOS and causal-set
prospectus material was cut or moved per
`reviews/external-2026-10-21/REVISION_PLAN.md` and
`research/examples-scope/DECISIONS.md`. The new draft is 8 pages, retargeted at Brading's P1** and the coverage
problem. The second re-review required that retarget; independent source,
logic and priority checks are in progress.

## Totality rebuild and trilemma repair, 21 October 2026

Post-Savitt audits changed the target again. The Savitt-delta audit found that
the P1** coverage retarget is not an increment: Brading 2013 p. 1110 already
states local boundedness. The critical-note assessment and the
alternative-contribution scout found a stronger internal argument: Brading's
own principle identifies what exists with the genuine unities and applies the
law-constitutive approach to the material universe (2015 p. 16; 2013 p. 1105
n. 3). A first draft claimed a categorical reductio: the universe is a thing;
its sustaining region is W; P1** (a) is false of it.

The independent logic audit (`paper/reviews/totality-logic/REVIEW.md`) rejected
that form. T1 is an adopted premise, not a textual entailment; T4 is not sound
as stated, because a Cauchy slice or thick global slab is a proper region and
Brading's rejection of a spatially global present is qualified by "common to all
systems"; the 2013 condition is sufficient and the 2015 condition necessary, so
criticizing them for non-exhaustiveness attacks a straw man; the four-event
model needs its assumptions and 2013 n. 7; "scale-free" misdescribes a
scale-general approach. The draft was repaired into a three-horn trilemma
(10 pages): the universe's present is W (so (a) fails on the unrestricted
reading), a proper region (global, requiring a qualification; or local,
requiring an account), or outside the domain (split into not-a-unity and
term-of-art restriction). A prior no-present case is flagged. The conclusion is
conditional: P1** cannot be both universal and satisfied by the universe without
an account Brading does not supply. The defeat/survival criticism is now about
framing, using "the crucial question" (2015 p. 18) and "A great deal rests..."
(2013 p. 1110). The diagnosis is "scale-general," with a missing
scale-selection guarantee.

A second independent pass (`reviews/totality-logic/SECOND_PASS.md`) found four
remaining gaps in the 0f09900 draft: the no-present case, the two exits inside
horn 3, the patch-only cost for non-global proper regions, and the unextended
2013 n. 7 caveat. The current draft repairs all four.

Changes: `paper/main.tex` rewritten (10 pages); `paper/references.bib` gains
Savitt 2021 and Rovelli 2019; `paper/check_records.py` gains a finite test of
the two-system/four-event model. Verification: `python3 paper/check_records.py`
runs six tests, all pass, including the four-event model. pdfTeX/TeX Live 2026
builds four passes with BibTeX; no unresolved references or overfull boxes.
macOS PDFKit renders all ten pages; the coordinator inspected pages 1-10.
`verification.json` records nine citation keys, hashes, build and visual
coverage. Sources read at full text this session: Brading 2013 (hash
`c93ca072…`), Brading 2015 (hash `7caceae7…`), Savitt SEP §3.3 live. Balaguer
2026 body and Brading 2011/2014 are unread; they are the main prior-art gap.

This is still a working note, not an accepted result or a submission-ready
manuscript. The independent priority audit could not run: the subagent hit the
account's credit limit, and `paper/reviews/totality-priority/` is empty. A
bounded web/SerpApi search found no published statement of the universe
trilemma, but this is not a priority certificate. No submission, upload,
authorship decision or ontology claim is made here. No other task's worktree,
the runner, the grid or the shared seed sources were changed.
