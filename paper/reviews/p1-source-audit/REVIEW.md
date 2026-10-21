# Source and quotation audit: *Local presents and the block* (P1\*\* retarget)

Date: 2026-10-21. Auditor: independent source-accuracy review, not a
philosophical referee report. Target: `paper/main.tex`, identical at commits
`5a9ec90` ("Retarget article at Brading P1-double-prime") and `22d82a18`
(HEAD); `git diff 5a9ec90 HEAD -- paper/main.tex` is empty. Compiled from a
temporary copy: **8 pages**, no undefined citations, no BibTeX warnings.
Nothing in the repository was edited except the two files in this directory.

This report checks only what the paper attributes to sources: quotations,
locators, antecedents, ellipses, and bibliographic data. It does not endorse or
reject the paper's thesis.

---

## 0. Summary

The retarget is largely clean at the level of quotation. Every quoted string
I could locate is present in the cited primary text, with **two genuine
quotation errors (A1, A3) and one wrong page locator (A2)**, plus several
unmarked truncations and missing locators. Specifically:

- **P1\*\* (2015, p. 17) is quoted exactly**, including "that exists", "the
  present for that thing", and both "(a)" and "(b)". The wording is identical
  to the printed page image.
- **"In order to avoid the block universe, all we need is (a)" is exact**
  (2015, p. 17), and so is the paraphrase used in the abstract.
- **(a) is a per-thing bound on the extent of that thing's present relative to
  the universe's evolution. The paper's `∀i U_i ⊊ W` is a faithful, and in
  fact charitable, formalisation of it** (see §4 below). (b) is an extent claim
  relative to the thing's own history; Brading explicitly says (b) "could be
  omitted". The paper's reading of (b) is correct.
- The 2013 quotations (P1, P2, present definition, defeat condition, n. 3,
  "local, not global", "the unity of what there is…") are exact and correctly
  located.
- **Defect A1:** the block quote labelled "Its full text is:" and cited to
  *both* Brading 2013 p. 1110 and Brading 2015 p. 17 contains **"dependent on
  the dynamics"**. The 2013 text reads **"dependent on dynamics"**; only the
  2015 text has the article. The quotation is 2015's, not 2013's.
- **Defect A2:** Saunders's "not only transitivity, but also symmetry, is
  required" is on **preprint p. 2**, not p. 3, and the sentence is truncated
  before "by the presentist" without an ellipsis. The companion quotation
  ("nothing less than an equivalence relation…") *is* on p. 3.
- **Defect A3:** `"Exists relative to me"` is not Brading's text; she writes
  "Does my son **exist** relative to me…". The capitalisation is the paper's.
- Unmarked truncations: the n. 6 quotation drops the clause that supports the
  paper's word "short-lived" without an ellipsis; the n. 6 quote also silently
  changes first person ("I") to indirect speech ("she"); the interaction
  passage is introduced as "In full:" although a sentence is elided.
- One quotation inside the body has no citation at all ("as represented in
  Minkowski spacetime", line 129).
- Locators are missing for Clifton–Hogarth (Thm 1, p. 365), the Stein
  "definiteness" citation, Pooley, Mason and Balaguer; Saunders's "whole of
  reality" (preprint p. 1) appears in a sentence with no citation at all.
- The limits paragraph misstates the Mason read depth and points to a
  non-manuscript "review record".

No invented quotation was found. The `"the"` insertion, the capitalised
"Exists" and the n. 6 pronoun shift are real text (2015; Brading's own "exist";
"can be made…") in altered form, not fabrications.

Verdict on source accuracy: **fix A1–A3 and the unmarked truncations before
submission; the rest are locator and labelling repairs.** The P1\*\*
retarget itself is source-faithful.

---

## 1. Primary texts actually inspected

| Source | Copy | SHA-256 | Depth |
|---|---|---|---|
| Brading 2013, *Presentism as an Empirical Hypothesis*, *Phil. Sci.* 80(5):1101–1111 | public 11-page published-layout PDF (same URL as `research/article-admissibility/primary-review/SOURCES.md`) | `c93ca072e14c4fd0f1c638ff960db17847231479ec9bf168cf0d69f9644bb054` (matches project record) | full text (all 11 pp.) extracted; **pp. 1105, 1109, 1110 inspected as page images** |
| Brading 2015, *Physically Locating the Present…*, *SHPS A* 50:13–19 | public 7-page published-layout PDF (same URL) | `7caceae74aebe28d1775561cd307dce50f912570eb1a7f9a709d70c699b08f6b` (matches project record) | full text (all 7 pp.) extracted; **p. 17 inspected as a page image** |
| Saunders 2000, *Tense and Indeterminateness* | PhilSci-Archive 2241 preprint (`for_Pittsburgh.pdf`), 12 pp. | `2f372cdf7a6e88e4445c4d3b1f5d1b707c1be96a521dd0fa40fbac7fea105b70` | preprint pp. 1–4 read; published S600–S611 **not collated** |
| Pooley 2013, *Relativity, the Open Future, and the Passage of Time* | PhilSci-Archive 9936 preprint, "14 August, 2013", 37 pp. | `8ada9fc62b31d1f5a0b884891035d98842083bd8e6dbff2af83c238a0ce99ddc` | abstract and introduction (preprint pp. 1–2) read; remainder not read |
| Clifton & Hogarth 1995 | project copy `knowledge/putnam-ablation/primary/clifton-hogarth-1995.pdf` | `1bcf93f94e5ff3252b154006b82c53e6462aa763e6d608525b630d100e8fa364` | text of Thm 1, proof, Cor. 1 (printed pp. 365–367) read |
| Stein 1991 | **not inspected by me**; used `knowledge/audits/stein-printed-pages/PRINTED_VERIFICATION.md` (printed pp. 148–150; OCR + visual line check) | — | inherited verification only; no new JSTOR scan, per brief |
| Mason 2025/2026 | PhilSci-Archive 25374 preprint (`Temporal Perspectives Probabilities and Openness.pdf`), 25 pp. | `38312ca49099069e579f26195315e5a4115299b226e6c3a490294af9711ca780` | preprint pp. 1, 7–8, 17–18 read; published Synthese version not accessible (publisher page blocked) → **abstract only for the published version** |
| Balaguer 2026 | Crossref records for book `10.1093/9780197845745.001.0001` and chapter `10.1093/9780197845745.003.0011` | — | **book and chapter abstracts only**; no book text |

Copies were downloaded to a temporary directory outside the repository and
are not committed.

---

## 2. Quotation and locator table

Legend: **PASS** exact and correctly located; **PASS(c)** exact but
compressed/truncated in a way that does not alter meaning (style note);
**FAIL** quotation or locator defect.

| # | Paper (line) | Quoted or attributed text | Source and locator | Verdict | Exact correction |
|---|---|---|---|---|---|
| Q1 | 86–88 | "(P1) All and only things that exist now are real" | Brading 2013, p. 1101 | **PASS** | — |
| Q2 | 87–88 | "(P2) Special relativity is a complete account of spatiotemporal structure" | Brading 2013, p. 1101 | **PASS** | — |
| Q3 | 160–162 | "The present is a spatiotemporal region of whatever size is necessary to sustain the dynamical system in question" | Brading 2013, p. 1109 (italic in original; n. 7 attaches after "question.") | **PASS** | Removing the footnote marker is acceptable; no change needed |
| Q4 | 166–167 | "this version of presentism is defeated and the block universe triumphs" | Brading 2013, p. 1109; original: "If that turns out to be the case, then this version of presentism is defeated and the block universe triumphs." | **PASS** | — |
| Q5 | 174–176 | "(P1\*) For each and every thing, that thing exists only presently, where the spatiotemporal extent of that 'present' is dependent on **the** dynamics, and it is something to be determined empirically" cited "(Brading 2013, 1110); (Brading 2015, 17)", introduced by "Its full text is:" | 2013, p. 1110: "…is dependent on **dynamics**, and it is…"; 2015, p. 17: "…is dependent on **the** dynamics, and it is…" | **FAIL (A1)** | The quoted wording is 2015's. Either cite only `\citep[p.~17]{Brading2015}` for this text, or quote 2013 verbatim ("dependent on dynamics") with the 2013 locator and give 2015's variant separately. Do not attach one wording to both pages. |
| Q6 | 50–56 | Full P1\*\* display | Brading 2015, p. 17 (page image checked) | **PASS** | — |
| Q7 | 59–60 | "In order to avoid the block universe, all we need is (a)" | Brading 2015, p. 17 | **PASS** | Full stop sits outside the closing quote; acceptable British style, or move it inside |
| Q8 | 180–182 | "having the entirety of the block universe labeled as the 'present' doesn't seem to save anything that the presentist was hoping to save" | Brading 2015, p. 17 | **PASS** | Mid-sentence start is signalled by lower-case "having"; an opening `\ldots` would be more explicit but is not required |
| Q9 | 186, 395 | "all we need is (a)" | Brading 2015, p. 17 | **PASS** | — |
| Q10 | 219 | "local, not global" | Brading 2013, p. 1110: "…and so the present is (at least in the first instance) local, not global." | **PASS** | — |
| Q11 | 246–247 | "the totality of existing things" | Brading 2013, p. 1105 n. 3 (page image checked) | **PASS** | — |
| Q12 | 253–255 | Brading notes that she "can be made of things whose dynamically sustained regions of spacetime are much smaller than mine" | Brading 2013, p. 1109 n. 6: "Moreover, **I** can be made of things whose dynamically sustained regions of spacetime are much smaller than mine, **so they come into and go out of existence on much shorter timescales than I do.**" | **FAIL (B1)** | Quote "I can be made of things… much smaller than mine, so they come into and go out of existence on much shorter timescales than I do" (p. 1109 n. 6). The dropped clause is the textual warrant for the paper's own word "short-lived" and is omitted without ellipsis; the first-person "I" is silently replaced. |
| Q13 | 271–277 | Interaction passage, with `\ldots` after "as real as we are", introduced by "In full:" | Brading 2013, p. 1110 | **PASS(c) / FAIL (B2)** for "In full" | The elided sentence is: "The dynamics grounds the unity of what there is, both of the parts and of the whole (consisting of interacting parts), and this is what prevents the presentist from becoming a solipsist." Replace "In full:" with "With one sentence omitted:" (the ellipsis itself is correct). |
| Q14 | 281–282 | "We belong to the same world," "the rest of that world is as real as we are," "the unity of what there is, both of the parts and of the whole" | Brading 2013, p. 1110 | **PASS** | — |
| Q15 | 283 | "Exists relative to me" | Brading 2013, p. 1110: "Does my son **exist** relative to me when he is in London and I am here? **Of course.**" | **FAIL (A3)** | Write: "**exist relative to me**" is answered affirmatively ("Of course") and glossed by interaction…; the capital "Exists" does not occur in the source, and the interrogative form is lost. |
| Q16 | 306–308 | "the unity of what there is, both of the parts and of the whole (consisting of interacting parts)" | Brading 2013, p. 1110 | **PASS** | — |
| Q17 | 129 | "as represented in Minkowski spacetime" | Brading 2015, p. 17, P1\*\*(a) | **FAIL (B3)** | Quotation has **no citation**. Add `\citep[P1**(a), p.~17]{Brading2015}`. |
| Q18 | 361–362 | "nothing less than an equivalence relation will do for the presentist"; "not only transitivity, but also symmetry, is required" cited `\citep[p.~3]{Saunders2000}` | Saunders preprint p. 3: "But nothing less than an equivalence relation will do for the presentist."; **preprint p. 2**: "It is unfortunate that Putnam did not make it clear that not only transitivity, but also symmetry, is required **by the presentist**." | **FAIL (A2)** | Split the locators: "…will do for the presentist" (preprint p. 3); "not only transitivity, but also symmetry, is required by the presentist" (preprint p. 2). The bare fragment "…, is required" truncates the sentence without ellipsis. |
| Q19 | 365–367 | "no equivalence relation" (Saunders), with `\citep{CliftonHogarth1995}` for the trichotomy | Saunders preprint p. 3: "Therefore there is no equivalence relation, proving Putnam's point."; Clifton–Hogarth Thm 1, printed p. 365: "…it can only be the relation of past chronological connectibility, or the relation of past causal connectibility, or the universal relation." | **PASS** for wording; **B4** for missing locators | Quote is a verbatim substring. Add `(Thm 1, p.~365)` to the Clifton–Hogarth citation, and use Clifton–Hogarth's own term "past chronological connectibility" rather than, or alongside, "past-timelike". |
| Q20 | 374–375 | "whole of reality" | Saunders preprint p. 1: "If we are to take the position seriously, as a philosophical thesis, it is a public space – for nothing else exists, this is the whole of reality…" | **FAIL (B4)** | Add locator (preprint p. 1). "Public, non-provincial" is a fair paraphrase of the same page ("…it had better not be a view which is provincial"), but is not quoted. |
| Q21 | 188–192 | Stein's theorem "lists reflexivity, transitivity, invariance under time-orientation-preserving automorphisms, and one past-pointing related pair", plus "of any number of dimensions—of course at least two" | Stein 1991, p. 149, via `PRINTED_VERIFICATION.md` | **PASS** | The "one past-pointing related pair" compresses "ab is a past-pointing (time-like or null) nonzero vector"; acceptable because the causal-past wording is supplied two sentences later. First sentence of the paragraph (`\citep{Stein1991}`) should carry the page: `\citep[p.~149]{Stein1991}`. |
| Q22 | 192–195 | "the proof also uses the non-universality condition (iv) and the prose premise that every event in the causal past—timelike or null—is definite as of the point" | `PRINTED_VERIFICATION.md` (pp. 148–150) | **PASS** | Consistent with the audit, including its correction that (iv) alone is insufficient. I did not inspect the scan. |
| Q23 | 293–294 | Mason treats "what exists" as perspective-relative | Mason preprint p. 1: "There is no 'existence simpliciter' that can be specified absolutely, what exists depends on one's perspective." | **PASS** for wording (substring of "what exists"), **FAIL (B5)** for locator/labelling | Add locator (preprint p. 1; published pagination not inspected). |
| Q24 | 291–293 | "Balaguer's R-presentism makes existence relative to a frame of reference, with no frame-independent fact about which 3-manifold is real" | Balaguer chapter abstract: "(b) there's no frame-independent fact of the matter about which 3-dimensional manifold is the 'real' one"; "what exists is relative to a frame of reference" | **PASS** | No quotation, accurate against the chapter abstract (the stated read depth); add chapter locator pp. 212–237. |
| Q25 | 379–383 | Pooley's two easy routes; hard route "eschews a global Now" and links passage to the open future | Pooley preprint abstract p. 1: "(1) does not take passage seriously. (2) does not take relativity seriously."; p. 2: "Such a view will eschew a global Now." | **PASS** for content; **B4** for missing locator | Add preprint pp. 1–2 locators; the manuscript cited only `\citep{Pooley2013}`. |

---

## 3. Findings, ordered by severity

### A. Must fix (quotation or locator errors)

**A1. P1\* is 2015's text cited as 2013's (lines 174–178).**
The 2013 printed page reads "dependent on dynamics"; the 2015 printed page
reads "dependent on the dynamics". The paper prints 2015's wording under a
joint `\citep[p.~1110]{Brading2013}; \citep[p.~17]{Brading2015}` and calls it
"Its full text". A referee checking p. 1110 finds a one-word mismatch.
*Correction:* cite only 2015 for that wording, and add a note that 2013 has
"dynamics" without the article, or quote the 2013 version with the 2013
locator. (The more serious antecedent defect flagged in
`paper/reviews/external-2/REVIEW.md` M3 is **fixed**: the full clause is now
quoted, so "it" has its antecedent.)

**A2. Saunders locator and unmarked truncation (lines 361–362).**
Two quotations share one `[p. 3]`. "Nothing less than an equivalence relation
will do for the presentist" is on preprint p. 3; "not only transitivity, but
also symmetry, is required" is on preprint p. 2 and ends "…required **by the
presentist**." The page labels here are preprint pages (12-page PhilSci 2241
copy), while the bibliography entry is the published S600–S611 article; a
reader holding the published version cannot use "p. 3".

**A3. "Exists relative to me" (line 283).**
Brading writes "Does my son exist relative to me when he is in London and I am
here? Of course." The quoted fragment changes the verb's capitalisation and
drops the interrogative and the affirmative answer. Because this fragment
carries the paper's central withdrawal of the relativized-existence reading,
it must be exact. Note also that Brading does answer the existence question
affirmatively; the paper should say so and explain why "exists relative to me"
is not a relativized existential quantifier (its reason — "we belong to the
same world … the rest of that world is as real as we are" — is already quoted
two lines earlier, so the repair is one sentence).

### B. Should fix (unmarked truncation, missing locator, mislabelled depth)

**B1. n. 6 quotation (lines 253–255).** From "I can be made…" through "…than
I do" is one sentence. The paper keeps the first half, deletes the second
without ellipsis, and replaces "I" with "she" outside the quotes. Quote the
whole sentence or add `\ldots`; the deleted clause is the only textual support
for the paper's "short-lived".

**B2. "In full:" followed by an ellipsis (line 269).** Self-contradictory;
replace with "With one sentence omitted" and, optionally, name the omitted
sentence, since it contains the "unity of what there is" phrase the paper
relies on later.

**B3. Uncited quotation (line 129).** "as represented in Minkowski spacetime"
is Brading's P1\*\*(a) wording; it needs a citation.

**B4. Missing locators.** Clifton–Hogarth (Thm 1, p. 365); Saunders "whole of
reality" (preprint p. 1); Stein opening mention (p. 149); Pooley (preprint
pp. 1–2); Mason (preprint pp. 1, 17–18); Balaguer (chapter pp. 212–237). None
of these is a wrong locator except A2; all are unverifiable as printed.

**B5. Preprint/published pagination is not distinguished.** The bibliography
entries for Saunders, Pooley and Mason point to published versions but the
only pages anyone can check are preprint pages. Either add "preprint p. N" in
the text and a note in the entry, or collate the published versions. This is
the same class of defect as A2 and should be fixed uniformly.

**B6. Limits paragraph misstates the source depths (lines 420–422).**
"Saunders and Pooley are read at the preprint depths stated in the review
record" refers to a document that will not exist for a reader, and "Balaguer
and Mason are used at abstract/chapter level" is wrong for Mason: the
"domain- and level-dependent" attribution and the "what exists" quotation come
from the 2025 preprint body (pp. 1, 17–18), which
`research/existence-form/NOVELTY_AUDIT.md` records as read at pp. 1–25 (OCR).
*Correction:* state each depth inline, e.g. "Saunders 2000: PhilSci-Archive
2241 preprint, pp. 1–3; Pooley 2013: PhilSci-Archive 9936 preprint, abstract
and introduction; Mason 2026: 2025 PhilSci-Archive preprint, pp. 1–25 (OCR),
published version not collated; Balaguer 2026: chapter abstract."

**B7. Attribution ambiguity for the 2013/2015 sequence (lines 43–47).**
"Her 2013 paper states P1\*: … She then notices that this extent might be the
whole universe, in which case labeling the entire block 'present' does not
save what the presentist hoped to save." The "doesn't seem to save anything"
judgement is 2015, p. 17 (2013 p. 1109 only says the extent "might be the size
of the block universe" and states the defeat condition). The sentence has no
citation, so it reads as a 2013 claim. *Correction:* add
`\citep[p.~17]{Brading2015}` or split the sentence at the 2013/2015 boundary.

**B8. n. 3 dilemma slightly overstates the source (lines 246–251).**
n. 3 says the law-constitutive phrase covers "the unity of simple things,
composite things, and the totality of existing things", but also that
"Different principles of unity might be used for the different cases." The
paper's "If the totality is a genuine unity, its sustaining region is plausibly
the whole history. **Then** its present is not less than the universe's
evolution" turns a possibility into a consequence. *Correction:* "If the
totality is a genuine unity **and its sustaining region is the whole history**,
then…"; label the step as the paper's conjecture (it already does this for the
n. 6 route, but not here). Also soften "both suggested by Brading's own text":
n. 6 suggests a plurality of nested things, not coverage.

### C. Notes (no correction required for accuracy, but worth a sentence)

**C1. "replaces P1\* with P1\*\*" (abstract; line 47).** Brading writes "So one
more attempt seems in order, albeit a bit of a mouthful" (2015, p. 17). She
does not retract P1\*; "replaces" is a fair description of the proposal but is
the paper's characterisation.

**C2. fn. 7 compression (line 136).** The footnote denies determinate
"spatial or temporal relations" within a region and between systems; the paper
writes "spatiotemporal relations". Not a quotation, but the compression is
worth avoiding in a paragraph about what the footnote denies.

**C3. (a) as a formalisation, not a statement.** Brading states (a) as the
extent being "less than the entire spatiotemporal evolution of the universe";
`U_i ⊊ W` is the paper's reading of "less than" as proper parthood, with the
domain restricted to "systems". Two repairs: (i) say "reading 'less than' as
proper parthood (the strongest reading)"; (ii) note that P1\*\* quantifies over
"each and every thing that exists", which Brading identifies with "the genuine
unities" (2015, p. 17), so the system domain and the thing domain coincide only
under that identification. The non-implication is a fortiori for weaker
measure readings, which is worth saying because it strengthens the paper.

**C4. The "system-relative" label for Mason and Balaguer (lines 322–326).**
Balaguer's R-presentism is frame-relative existence. Mason's is
perspective-relative ("no 'existence simpliciter' that can be specified
absolutely", 2025 preprint p. 1). Neither is a system-indexed predicate. Use
"frame- or perspective-relative" for the route, and keep "system-relative" for
the paper's own construction.

**C5. Credit for "domain" (line 294).** Mason attributes the domain point to
Savitt (2006) and Rovelli (2019) in her own text (preprint p. 17), and says
Brading's empirical presentism is "naturally level-dependent". The paper's
"Mason's empirical presentism makes the present domain- and level-dependent"
compresses this. Acceptable in a single sentence, but a footnote would be
cleaner.

**C6. "often read as a system-relative existence claim" (line 268).** This is a
claim about the literature with no citation. Mason's preprint (pp. 7–8) reads
Brading's present as relative to a physical system and would serve as the
citation; otherwise say "can be read".

**C7. Bibliography (rendered with plainnat).**
- `Mason2026`: missing volume, issue and article number; Crossref gives
  *Synthese* 207(3), article 126, published 2026-03-12.
- `Pooley2013`: the published title is "XVI—Relativity, the Open Future, and
  the Passage of Time" (*Proc. Arist. Soc.* 113(3pt3):321–363). The "XVI" is
  omitted.
- plainnat lowercases mixed-case titles ("Presentism as an empirical
  hypothesis", "Physically locating the present…", "Relativity, the open
  future…"). Brace-protect if the venue cares.
- `Balaguer2026`: the note names the chapter but gives no pages; add
  pp. 212–237 and the chapter DOI, or cite the chapter as `@incollection`.
- All DOIs resolve and all volume/page data I checked with Crossref are
  correct (Brading 2013 80(5):1101–1111; Brading 2015 50:13–19; Stein 1991
  58(2):147–167; Clifton–Hogarth 1995 103(3):355–387; Saunders 2000
  67(S3):S600–S611).

---

## 4. The three questions the brief singled out

**(i) Is P1\*\* clause (a) exactly the paper's local-boundedness condition?**
Substantively yes, literally no. Brading's (a) is: "the spatiotemporal extent of
the present for that thing is … (a) less than the entire spatiotemporal
evolution of the universe as represented in Minkowski spacetime." The paper's
`∀i U_i ⊊ W` captures: per-thing bound, relatum = the universe's whole
evolution, "less than" = proper containment. Three differences, none of which
breaks the argument:

1. **Quantifier domain.** Brading: "each and every thing that exists"; paper:
   "every system *i*". These coincide if every existing thing is a genuine
   unity (Brading 2015, p. 17). The paper should say so once.
2. **"Less than".** Proper parthood is a reading; a measure reading ("smaller
   extent") is also available. The paper's reading is the stronger premise, so
   the non-implication survives either way — an a fortiori point the paper
   could make in one clause.
3. **W.** The paper's W is "the block as represented in Minkowski spacetime",
   which is exactly the representation (a) invokes. This is the right choice
   and answers the extern-2 M5 objection.

Conclusion: **(a) is local boundedness in the sense the paper needs**, and the
paper does not overstate Brading's text provided C3 is added. No source
contradiction.

**(ii) Is (b) an extent claim?** Yes. (b): "less than the entire spatiotemporal
evolution of that thing as represented in Minkowski spacetime", and Brading's
own gloss: "(b) could be omitted, but should be included if we also deem it
important to presentism that the 'present' of any given thing is less than the
entire spatiotemporal history of that thing" (p. 17). The paper's description
of (b) as an extent/presence-endurance claim, and as optional for avoiding the
block, is accurate (lines 119–121, 184–186).

**(iii) Is "all we need is (a)" exact?** Yes, verbatim: "In order to avoid the
block universe, all we need is (a)." (p. 17). The abstract's paraphrase ("She
says that (a) is all that is needed to avoid the block universe") is faithful.
The paper's use of the sentence — that (a) is a per-thing bound and therefore
insufficient for a global existential restriction — attributes to Brading only
what she says, and the insufficiency claim is the paper's own. No attribution
error.

Two related checks requested:

- **Does the paper misattribute a global-existence claim to "all we need is
  (a)"?** It does not say Brading intends (a) as global exclusion; it says (a)
  does not secure it. That is the correct logical gap. The one place to be
  careful is the abstract's "Brading's own stated sufficient condition does not
  secure a global existential restriction": "sufficient condition" is the
  paper's gloss of "all we need", and (a) is offered by Brading as sufficient
  *for avoiding the block universe*, not explicitly for a global restriction.
  This is a fair-but-interpretive step; it would be exact if the abstract said
  "sufficient, by her own account, for avoiding the block universe".
- **Does Brading state or deny coverage (C)?** No. 2013 p. 1110 assumes
  genuine subsystems and says the present is "local, not global"; 2015 p. 18
  says the "crucial question" of genuine subsystems "smaller in spatiotemporal
  extent than the entirety of spacetime" remains open. Neither asserts nor
  denies that the family of presents covers the universe. The paper's "Brading
  does not state (C) or its negation" (line 240) is **correct** on full-text
  reading of both papers.

---

## 5. What is accurate and should not be changed

- The 2013 reconstruction of law-constitutive unity, the epistemic role of
  spacetime, the sustaining-region present, and the defeat condition; the
  locators pp. 1104–1108, 1105–1108 and 1108–1109 are right.
- P1\*\* in full, with the "that exists" clause; "In order to avoid the block
  universe, all we need is (a)"; "having the entirety of the block universe
  labeled as the 'present' doesn't seem to save anything…".
- The withdrawal of the system-relative-existence attribution, and the use of
  the interaction passage for the single-domain verdict.
- The Stein paragraph: the dimension clause, reflexivity, condition (iv), and
  the chronological-past countermodel all match the project's printed-page
  verification.
- The Saunders "non-trivial" marking: the paper states in the text that the
  qualifier is its own strengthening (line 365–367), which is exactly right;
  Saunders's bare "Therefore there is no equivalence relation" (p. 3) is
  strictly false without it, since the universal relation is an equivalence
  relation.
- The Clifton–Hogarth trichotomy, in the terminology "past-timelike,
  past-causal or universal", matches Thm 1.
- The Balaguer and Mason characterisations are supported by the chapter
  abstract and the 2025 preprint respectively, at the depths the limits
  paragraph should state.

---

## 6. Limits of this audit

- I did not inspect the Stein 1991 JSTOR scan; the Stein entries rely on
  `knowledge/audits/stein-printed-pages/PRINTED_VERIFICATION.md`, whose text is
  OCR with a visual line check of the theorem display. I have not independently
  confirmed the printed dash glyph in "of any number of dimensions—of course at
  least two".
- Saunders was read in the PhilSci-Archive 2241 preprint, not in the published
  *Philosophy of Science* S600–S611. Preprint-to-published pagination is not
  asserted anywhere in this report.
- Pooley's full 37-page preprint was not read; only the abstract and
  introduction, which contain everything the manuscript attributes to him.
- Mason's published *Synthese* version was not accessible; the quotations and
  characterisations were verified in the 2025 preprint only.
- Balaguer was checked at book/chapter-abstract level only. Claims about the
  chapter's body, or about how R-presentism handles specific objections, cannot
  be certified from this audit.
- Brading 2013/2015 were read from public published-layout copies whose
  SHA-256 hashes match the project's records; neither was collated against a
  publisher-hosted file. Text was extracted with PDFKit and key pages (2013
  pp. 1105, 1109, 1110; 2015 p. 17) were checked as page images, so
  hyphenation/ligature artefacts in the extraction do not affect the
  verdicts above.
- This audit covers source accuracy only. It does not assess whether the
  coverage objection is novel, whether Saunders or Pooley are answered, or
  whether the parity verdict follows.
