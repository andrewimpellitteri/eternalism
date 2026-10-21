# Agent report: P1\*\* logic audit

Date: 21 October 2026. Worker: independent philosophical logic auditor
(subagent of the coordinator). Task: adversarial assessment of the argument in
`paper/main.tex` at commit `5a9ec90`, on the seven assigned questions.

## Files changed

Created, inside the assigned directory only:

- `paper/reviews/p1-logic-audit/REVIEW.md`
- `paper/reviews/p1-logic-audit/AGENT_REPORT.md`

Nothing else in the repository was modified. `paper/main.tex`, the workboard,
`AGENTS.md`, and the shared sources are untouched. `HEAD = 5a9ec90` and no
tracked file is modified; the only additions are the two files in the assigned
directory. No commits, no pushes, no agent launches.

Temporary working files (extracted PDF text, a compiled copy of the paper,
`pdftext.swift`) are in
`/private/var/folders/k0/46qrmwrj74gcdwzmbtsxlbpm0000gn/T/opencode/p1audit/`,
outside the repository.

## Materials and read depths

| Item | Depth | How |
|---|---|---|
| `AGENTS.md` | full | read |
| `paper/main.tex` @ `5a9ec90` | full, 428 lines | read; line references in REVIEW.md are to this file |
| `paper/reviews/external-2/REVIEW.md` | full | read; used as a checklist of which earlier items are actually closed at `5a9ec90` |
| `paper/REFRAME.md` | full | read |
| `research/existence-form/TRILEMMA.md` | full | read |
| `research/brading-existence/RESULT.md`, `research/strongest-opponents/RESULT.md` | full | read (predecessor versions the article draws on) |
| `paper/SOURCE_AUDIT.md`, `paper/READINESS.md` | full | read |
| Brading 2013 | **full text**, all 11 pages | downloaded from the public URL in `research/article-admissibility/primary-review/SOURCES.md`; SHA-256 `c93ca072…` matches the project record; text extracted with a PDFKit script I wrote |
| Brading 2015 | **full text**, all 7 pages (pp. 17–18 read closely) | same route; SHA-256 `7caceae7…` matches |
| Clifton–Hogarth 1995 | Theorem 1 and surrounding pp. 361–366 | local scan `knowledge/putnam-ablation/primary/clifton-hogarth-1995.pdf`, text-extracted |
| Stein 1991 | printed-page verification record only | `knowledge/audits/stein-printed-pages/PRINTED_VERIFICATION.md`; I did **not** see the scan |
| Saunders 2000 | **not independently read** | PhilSci-Archive 2241 returned HTTP 404 / request-rejected; assessed against the quotations recorded in `research/strongest-opponents/RESULT.md` and external-2 at the depths those records state (preprint pp. 1–3) |
| Pooley 2013 | **not independently read** | same archive failure; assessed against the recorded abstract/introduction quotations (preprint pp. 1–4) |
| Balaguer 2026 / Mason 2026 | not read | used by the paper only as nearby views; not audited |

No dependency installs, no credentials, no non-public sources.

## Checks performed

1. **Verbatim quotation check.** Every Brading quotation in `main.tex` was
   compared against the extracted source text: P1, P2, P1\*, P1\*\*, "all we
   need is (a)", the (b)-optional sentence, "doesn't seem to save anything…",
   the sustaining-region sentence, the defeat sentence, the interaction passage
   (with ellipsis), notes 3, 6 and 7. All verbatim except the P1\* wording,
   which matches 2015 rather than 2013 while citing both (minor issue C10 in the
   review).
2. **Clause-(a) correspondence.** Checked that (a) is a per-thing bound on the
   extent of the present and that the paper's `⊊` formalisation is a
   (charitable) strengthening; checked Brading's own p. 17 gloss "local, in
   being a spacetime region less than the extent of the entire 'block'".
3. **Coverage logic.** Re-derived the non-implication and the Proposition.
   The non-implication is correct; the Proposition's proof is not valid as
   written for small `W` (C1). Checked that the paper's §4.1 downgrade matches
   the logic,
   and that (C) is neither stated nor denied in Brading 2013/2015 (it is not).
4. **Target-aim check.** Searched both Brading papers for the sentence stating
   what (a) is supposed to achieve. Found "this calls the ontology of a block
   universe into question" (2015, p. 17), which the paper does not quote and
   does not distinguish from "secure a global existential restriction". This is
   the basis of major issue A1.
5. **Cross-document consistency.** Compared the article against REFRAME.md §7
   obligations (primitive-actuality reply; separation of repairs) and against
   TRILEMMA.md (P/Q/N forms). Checked which external-2 major/minor items are
   actually closed at `5a9ec90`: M1 (retarget) closed; M2/M4 (relativized
   existence) closed in substance; M3 (P1\* truncation) closed; M5 asserted not
   shown (B4); M6/M8 partly closed — "not that the evidence is silent" and
   "stronger than a catalogue" remain (A3); M7 partly closed; M10 partly
   closed.
6. **Build check.** Compiled a copy of `main.tex` with `pdflatex` + `bibtex`
   in the temp directory: 8 pages, no unresolved references, zero overfull
   boxes. The copy is identical to the committed file.
7. **Terminology audit.** Checked the paper's use of the four-way distinction
   (existence/presence/unity/endurance) for category consistency across §2, §5
   and §6, and checked the region/relation wording in §7.

## Main findings (summary)

Verdict in REVIEW.md: **needs revision**. The non-implication and its scoping
are sound; the retarget is real; the quotations are now accurate. Three
load-bearing defects: (A1) the verdict converts Brading's "avoid the block"
into "secure a global existential restriction" without argument; (A2) coverage
premise (C) is sketched, not established, and the §4.1 hedge is not propagated
to the abstract or conclusion; (A3) the §6 parity verdict is a global
comparative claim with no comparison and contradicts its own first sentence.
Moderate issues cover leftover editor-facing text, the over-read of the
interaction passage, the Pooley self-contradiction, the asserted bearer
neutrality, the question-begging "cost" of primitive actuality, and the
maximal-unity paragraph's internal contradiction.

## Limits

- Saunders and Pooley were not independently re-read. Statements about their
  texts rest on the project's recorded quotations, not on my own reading. If
  the coordinator wants those checked, the archive needs a working route or a
  published copy.
- Stein 1991 was taken from the project's printed-page verification, not from
  the scan.
- No dynamical model of system-presents was constructed. The coverage point
  audited here is the set-theoretic one; whether a physically admissible family
  covers `W` is premise (C) and remains open.
- Page-level visual inspection of the compiled paper was not performed beyond
  the page count and the LaTeX log.
- I did not evaluate Balaguer or Mason, novelty, or the bibliography metadata.
- I did not edit the paper. All fixes are recommendations only.

## Unresolved questions for the coordinator

1. Does the author accept that "avoid the block universe" requires a global
   existential restriction? If not, A1 cannot be repaired by argument and the
   verdict should be weakened rather than defended.
2. Should §6 be cut to a paragraph, or should the parity claim be argued from
   the trilemma? The current section is the weakest part of an otherwise
   disciplined paper.
3. Are Saunders's and Pooley's published versions accessible for a proper
   collation? The current reconstruction is only as strong as the project
   record.
4. Does the article intend to state the P-form (predicate) reading of P1\*\*
   explicitly and defend it against the quantifier-restriction reading
   (TRILEMMA's Q-form)? If yes, that belongs in §2.3 and would pre-empt the
   strongest remaining reply.
