# Stein 1991 printed-page access review

## Result

No actual journal page image for pp. 148–150 was obtained. The isolated theorem/context mismatch remains unresolved between the printed article, OCR, and extraction. I do not attribute a theorem error to Stein. The currently accessible body text is OCR only and cannot satisfy the original-page-image check.

The target was kept distinct from Nicholas Maxwell’s 1993 discussion of Stein’s paper: Stein’s article is DOI `10.1086/289609`, *Philosophy of Science* 58(2) (1991), pp. 147–167, JSTOR stable `187456`. Maxwell’s separate 1993 article is DOI `10.1086/289737` and is not a substitute source.

## Bounded routes attempted, 2026-10-20

- **Publisher route:** Opening `https://doi.org/10.1086/289609` resolves to Cambridge Core’s Stein article page. It gives the abstract, bibliographic information, and a “Get access” control; no article body or page images are available in the public page response. This verifies identity/metadata only.
- **JSTOR route:** The public issue contents at `https://www.jstor.org/stable/i302078` identify Howard Stein’s article and pp. 147–167, with the article linked as `https://www.jstor.org/stable/187456`. Following the article’s download link to `https://www.jstor.org/stable/pdf/187456.pdf` failed to fetch the PDF. The public issue table of contents is not a page image.
- **Publicly indexed re-host:** `https://paperzz.com/doc/7354841/on-relativity-theory-and-openness-of-the-future` exposes a text transcription with journal page breaks and a JSTOR stable-URL header. The web text includes the p. 148–150 argument and displayed theorem, but no page image was exposed. Following its download link returned HTTP 403. I treat this as OCR/transcription, not as an authenticated or visually inspectable printed copy.
- **Bounded search for other scans:** Searches for an Internet Archive, Google Books, HathiTrust, or other public scan keyed to the exact title/JSTOR ID/DOI returned the same JSTOR record, the text re-host, metadata, and secondary citations; no additional inspectable image source surfaced. This was a limited search, not an exhaustive archive survey.

No access control was bypassed, no account or credentials were used, no TLS verification was disabled, and no source files were downloaded or installed. The publisher’s abstract and JSTOR/re-host metadata identify the intended item but cannot establish the wording or typography of its printed pages.

## What the OCR says—and what remains unverified

The accessible OCR places the four listed conditions and the theorem on journal p. 150. In that isolated transcription the hypotheses are reflexivity, transitivity, invariance under time-orientation-preserving automorphisms, and at least one past-pointing causal pair; the conclusion is equality with causal past. Read in isolation, that implication is refuted by the universal relation and by reflexive chronological past, respectively. These are countermodels to the transcribed four-condition statement only.

The same OCR sequence carries additional context immediately before the theorem: condition (iv) requires some unsettled states at every point, which excludes the universal relation; the physical interpretation is said to require inclusion of all causal-past points, which excludes reflexive chronology that omits the past-null boundary. The OCR also states the provisional no-distinguished-unit geometry, a time orientation, and the theorem’s dimension qualification (Minkowski dimension at least two), then notes that the no-distinguished-unit stipulation can be removed with a more elaborate argument. Those surrounding premises make the contextual argument intelligible, but OCR proximity does not prove whether the theorem was printed with an omitted premise or whether only the displayed extraction is defective.

The safe classification is therefore **still unresolved at the printed-page level**. Do not describe this as a printed-author error, a confirmed OCR omission, or a corrected theorem until a page image from the published article is inspected. No image was obtained against which to compare punctuation, line breaks, condition numbering, the theorem display, or adjacent text.

## RC-2 and article-freeze disposition

This check does not satisfy or unfreeze the original-page-image/source-correspondence gate in RC-2 or `paper/READINESS.md`. It confirms that the publisher and JSTOR records point to the intended 1991 article, and documents that the currently accessible full-body text is an OCR transcription. The contextual reconstruction and its countermodels remain a project-side interpretation of that OCR/context, not a verified correction to the printed theorem.

The broader RC-2 formal obligations remain: prove the contextual causal-past characterization under explicitly stated premises; separately establish any premise-removal claims beyond the two isolated countermodels; audit correspondence of any formalization to the source; and keep the mathematical relation distinct from objective passage or an ontological bridge. The paper remains a working draft rather than source-complete or submission-ready.

Files changed: only `knowledge/audits/stein-printed-pages/access-review/AGENT_REPORT.md`. No images, source records, shared references, paper, runner, or board were changed. No commits or installations were made. This was a bounded access attempt; lack of a public image here does not show that no library or licensed route exists.
