# Horizons source recovery: bounded original-source audit

Checked 2026-10-27. This note supplements `continuation-2026-10-27/GATES.md`;
it does not change the manuscript or certify novelty.

## Findings

### Ellis and Sciama (1972), pp. 41–42 — original passage still unread

The cited work is G. F. R. Ellis and D. W. Sciama, “Global and Non-Global
Problems in Cosmology,” in L. O’Raifeartaigh (ed.), *General Relativity: Papers
in Honour of J. L. Synge* (Oxford: Clarendon Press, 1972), pp. 35–59. The
stopped `horizons-priority-gap-check` run tried public discovery and book-search
routes; its saved notes say Google Books search-inside was captcha-blocked. The
bounded searches in this continuation recovered catalog/bibliographic records
and secondary citation context, but no view of the requested original pages.
That is an access boundary, not evidence that the chapter lacks a result about
the present theorem.

Earman 1995 p. 126 cites Ellis and Sciama in discussing information about a
charge outside an observer’s causal past and electromagnetic constraint
equations. This establishes how Earman invokes it, not what Ellis and Sciama
prove on pp. 41–42. Do not attribute a precise result to those pages until they
are read.

### Earman (1995), pp. 125–130 — original scan personally inspected

John Earman, *Bangs, Crunches, Whimpers, and Shrieks: Singularities and
Acausalities in Relativistic Spacetimes* (Oxford University Press, 1995), ch. 5,
§§5.2–5.4, printed pp. 125–130. Provenance: in this continuation I personally
opened and visually inspected the retrieved original-book scan images at
`/private/tmp/opencode/ear_big_69.png` (printed p. 125),
`/private/tmp/opencode/ear_big_70.png` (pp. 126–127),
`/private/tmp/opencode/ear_big_71.png` (pp. 128–129), and
`/private/tmp/opencode/ear_big_72.png` (pp. 130–131), using `view_image`.
The corresponding retrieved PDF is `/private/tmp/opencode/earman1995.pdf`.
These files were produced by the stopped run; I inspected the page images
directly in this continuation rather than relying on the stopped agent’s
interpretation. The stopped run’s OCR output is separately locatable in
`.agent-runtime/runs/horizons-priority-gap-check/events.jsonl`: event line 131
contains its shell output for `ear_ocr_69.txt` through `ear_ocr_72.txt` (PDF
pages 69–72), but that OCR/summary was not my sole evidence.

The inspected text shows: p. 125 frames the “two folklore dogmas” about
observation and determination from the causal past; p. 126 gives a Cauchy
surface in `J^-(p)` as an exception and then discusses Maxwell constraint
equations, explicitly citing Ellis and Sciama in the Fig. 5.3 example; pp.
128–129 define deterministic prediction via the future domain of dependence
and explain the Cauchy-surface case; p. 130 begins §5.4 on event and particle
horizons. This is a selected-page reading, not a proof audit or a reading of
the whole book.

Overlap: Earman supplies a clear antecedent for the Cauchy-surface prediction
case, causal-past prediction framing, and the Maxwell-constraint example that
points directly to the still-unread Ellis–Sciama pages. The inspected pages do
not state the manuscript’s exact model-specific equality
`F_L(b) = M ∩ cl(U_b)`, nor the three-diamond construction or its boundary
classification. The uninspected parts of the book are outside this comparison;
absence of that exact theorem from the whole work is not established.

### Wald (1984), Appendix D — search-index lead only; original not inspected

Robert M. Wald, *General Relativity* (University of Chicago Press, 1984),
Appendix D, “Conformal Transformations.” Provenance: I did not open or visually
inspect the Wald scan. The locator and apparent content came from search-index
excerpts returned by web search (results for the scan at `turn145search12` and
`turn145search13`), which state that Appendix D begins at printed p. 445 and
show its opening text; the same search result reports §4.3, Eq. (4.3.11),
cross-referencing Appendix D. These excerpts are a discovery lead, not my
inspection of the original text, so Wald remains unverified in this lane.
The manuscript’s specific solution-rescaling identity `psi = a phi` still
needs a directly inspected primary locator. Do not present this lane as having
verified Wald or use it to support priority for the echo or three-diamond
theorem.

## Theorem overlap and paper-safe priority wording

The current theorem in `research/horizons/main.tex`, Theorem
`thm:diamonds` (around lines 332–370), asserts the exact equality
`F_L(b) = M ∩ cl(U_b)` for the stated conformal scalar on closed dust when
`0 < eta_b < pi`, and gives a nonempty determined subset of `Isp(b)`. Earman’s
checked discussion overlaps with the broad distinction between geometric
prediction and law-relative field determination and with the exceptional
Cauchy-surface case. Wald is a discovery lead only. The inspected Earman pages
do not state the theorem’s exact three-diamond equality. Ellis–
Sciama is specifically flagged by the manuscript’s cited chain and remains
unread at the critical pages.

Suggested conservative wording while access remains incomplete:

> We give an exact characterization for this conformally coupled scalar on the
> closed-dust background. The general prediction and electromagnetic-constraint
> issues have antecedents in Earman (1995, §§5.2–5.3), who cites Ellis and Sciama
> (1972); the latter’s cited pages have not been verified here. We therefore
> make no priority claim for the model-specific characterization, which may
> overlap with those sources.

This describes the paper’s mathematical scope, not a novelty verdict. Do not
write “first,” “new,” or “not previously obtained” on the basis of this search.

## Bounded checks and unresolved items

- Read the stopped run’s `events.jsonl` selectively for source routes, then
  reused its recorded access work. It stopped on the reported provider quota
  error (HTTP 429/code 1308); GLM was not restarted.
- Checked bounded web discovery for the Ellis–Sciama chapter, the Earman book,
  and Wald Appendix D. I visually inspected the Earman original scan images
  listed above; the stopped run’s OCR is retained as provenance/context, not
  substituted for that inspection. Wald was not opened; only search-index
  excerpts were seen and are classified as discovery-level leads.
- No systematic citation search was performed. No proof audit of the manuscript
  theorem was performed. No novelty or priority certification follows.
- Unresolved: obtain readable access to Ellis–Sciama pp. 41–42; inspect Wald
  Appendix D itself and pin the exact scalar-equation page/equation; compare the
  full relevant proofs and assumptions before making any priority statement.
