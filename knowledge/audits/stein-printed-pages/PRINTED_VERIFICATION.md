# Stein 1991: printed theorem verification

Date: 2026-10-21. Source: user-supplied 21-page JSTOR scan of Howard Stein,
"On Relativity Theory and Openness of the Future", *Philosophy of Science*
58(2) (1991), 147-167, DOI `10.1086/289609`, JSTOR `187456`.

Local file: `/Users/andrew/Documents/289609.pdf`
SHA-256: `fef0224102cca5037a9da1878f541ee074e64412fe71e52504b94ebc915153f7`
Pages inspected: printed pp. 148-150 (PDF pp. 2-4). The scan is image-based;
the text below was obtained by macOS Vision OCR of the page images, and the
theorem display was checked line by line against the image.

## Printed theorem (p. 149)

> **THEOREM.** If R is a reflexive, transitive relation on a Minkowski space
> (of any number of dimensions-of course at least two), invariant under
> automorphisms that preserve the time-orientation, and if Rab holds for some
> pair of points (a,b) such that ab is a past-pointing (time-like or null)
> nonzero vector, then for any pair of points (x,y), Rxy holds if and only if
> xy is a past-pointing vector.

The page also states the provisional no-distinguished-spatio-temporal-unit
assumption and the time-orientation stipulation; p. 150 continues with the
argument that removes the unit assumption.

## What this resolves

- The theorem is printed on **p. 149**, not p. 150. The earlier OCR/transcription
  locator was off by one page.
- The printed hypotheses explicitly include **reflexivity** and the dimension
  qualification "at least two"; the transcription was not missing reflexivity.
- The surrounding text on pp. 148-149 lists four conditions (i)-(iv). Condition
  (iv) says that for any point there are points whose state is still unsettled
  as of it. The proof uses (iv) to rule out the universal relation.

## What remains a real source issue

The displayed theorem does **not** list condition (iv). The universal relation
on Minkowski space is reflexive, transitive, invariant under the stated
automorphisms, and contains a past-pointing pair, yet it does not satisfy the
"if and only if" conclusion. So the four printed hypotheses alone are
insufficient; condition (iv), stated immediately above and used in the proof,
is required for the argument. This is a literal premise omission in the
printed display, not an OCR defect. It is not a claim that Stein's surrounding
argument fails; with (iv) and the causal-past interpretation, the argument is
intelligible.

The article must therefore cite the theorem with the contextual condition
(iv), or avoid presenting the isolated four-premise display as a valid
characterization. No broader error in Stein's paper is inferred.

## Checks

- Rendered every page with PDFKit; OCRed pp. 148-150 with macOS Vision
  (`accurate` recognition, language correction on).
- Compared the theorem display, the four conditions and the p. 149/150
  transition against the page images.
- The universal-relation countermodel is elementary and exact.

## Limits

- The OCR is machine transcription; punctuation was checked visually but the
  full article was not re-OCRed page by page.
- The scan is a JSTOR-derived image; page numbers and running heads match the
  published article. The PDF is kept local and is not committed.
- This closes the printed-page access gate for the theorem passage only; it
  does not complete a formal reconstruction of Stein's broader argument.
