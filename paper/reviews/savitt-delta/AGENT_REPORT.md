# Agent report: Savitt delta audit

Task: independent source audit of Steven Savitt, *SEP*, "Being and Becoming in
Modern Physics", §3.3 "Localizing Time" (rev. 6 Oct 2021), against the P1\*\*
coverage claim in `paper/main.tex` and `research/existence-form/NOVELTY_AUDIT.md`.
Date: 2026-10-21. Role: subagent, philosophical source audit. No agent launched,
no commit, no push, no board edit, no edit outside `paper/reviews/savitt-delta/`.

## Files changed

| Path | Status |
|---|---|
| `paper/reviews/savitt-delta/REVIEW.md` | created |
| `paper/reviews/savitt-delta/AGENT_REPORT.md` | created (this file) |

Nothing else was written. `paper/main.tex`, `paper/references.bib`,
`research/existence-form/NOVELTY_AUDIT.md` and the workboard were read only.
`paper/main.tex` has uncommitted edits from another lane; I read the working-tree
state and did not touch it.

## Verdict delivered

The paper's claimed increment — applying the objection to Brading 2015 P1\*\*
(a) and to "all we need is (a)" — is a **trivial extension, verging on a
restatement**. No defensible delta for a standalone article. Recommended:
drop the standalone paper; preserve the event/unity domain dilemma as a
paragraph in a larger paper and record Savitt §3.3 in the knowledge base.

## Evidence and checks performed

1. **Savitt §3.3 full text** read from the live entry and from 14 archived
   editions (`fall2014` … `fall2026`). Every quotation in `REVIEW.md` §2.1 was
   copied from the live HTML with entities resolved; no quotation is
   reconstructed from a secondary summary.
2. **Dating, independently re-checked.** "3.3 Localizing Time" and the passage
   are absent from `fall2014` (rev. 13 Aug 2013), `spr2018`, `win2020`,
   `sum2021`, `fall2021` (rev. 21 Aug 2017); present and identically worded in
   `win2021` (rev. 6 Oct 2021) through `fall2026`. Confirms first appearance in
   the 6 Oct 2021 revision and stability since.
3. **Negative claims verified by full-text search of the live entry**, not
   asserted from the priority audit: "Brading" ×4 (two in §3.3, one anaphoric,
   one in the bibliography); bibliography lists Brading 2013 only, no 2015; all
   four "2015" occurrences are Dorato–Wittman or Savitt 2009/2020. Within §3.3:
   "union" 0, "cover" 0, "domain" 0, "quantif-" 0, "P1" 0, "suffic" 0 (the one
   "suffic" hit in the section is "insufficient resources" in the unrelated
   Dieks discussion).
4. **Brading 2013 full text** (11 pp., SHA-256 `c93ca072…`) and **Brading 2015
   full text** (7 pp., SHA-256 `7caceae7…`), both re-downloaded and hashed
   here; hashes match `paper/SOURCE_AUDIT.md`. Text extracted with macOS
   PDFKit via a local Swift script (no dependency installed). The 2015 text
   layer drops `fi`/`fl` ligatures; quotes are restored and marked as restored
   in `REVIEW.md` §1.
5. **Decisive textual finding for question 2:** Brading 2013 p. 1110 already
   states the local-boundedness condition as a starting position ("the size of
   the spatiotemporal region required to sustain the system is less than the
   entire block universe, and so the present is … local, not global"). P1\*\*
   (a) promotes that same sentence to a clause. The retarget therefore changes
   the citation, not the target-content.
6. **Second decisive finding:** Savitt's "Presumably every dynamical system that
   has existed, does exist or will exist had, has or will have a region …" is
   the paper's premise (C) stated affirmatively. The paper's claim to add (C)
   is not sustainable, and Savitt's use of (C) yields a conclusion stronger
   than the paper's (he grants (C) and still denies presentism; the paper hedges
   on (C)).
7. **Quotation-fidelity checks on the two internal audits.** The priority audit
   merges Savitt's two paragraphs without marking the break; `NOVELTY_AUDIT.md`
   omits the sentence that states his conclusion ("But this is a
   characterization of a relativistic present, not relativistic presentism").
   Both noted in `REVIEW.md` §2.5.
8. **`main.tex` and `references.bib` contain zero occurrences of "Savitt" and
   zero of "Rovelli"** (grep, working tree). Recorded as a submission blocker
   independently of the novelty question.
9. Cross-read `paper/reviews/p1-priority-audit/REVIEW.md`,
   `paper/reviews/p1-logic-audit/REVIEW.md` and
   `research/existence-form/NOVELTY_AUDIT.md` in full. Where the logic audit's
   findings bear on the delta (A1 bridge, A3 parity, B4 domain), I used them as
   independent reasons that the residue cannot carry a standalone paper.

## Read depths (honest)

- Savitt §3.3: **full-text**, live plus 14 archives.
- Rest of Savitt entry: **discovery** (bibliography plus keyword search); not an
  argument-level read of §1–§3.2.
- Brading 2013: **full-text** (11 pp.).
- Brading 2015: **full-text** (7 pp., pp. 15–18 assessed closely).
- *SEP* "Presentism" (rev. 12 Feb 2026): **discovery** keyword check only
  (zero "Brading", zero "local present").
- Savitt 2006, Slavov 2022, Raźniak 2023, Balaguer 2026 body, Mason 2026
  published version: **not read here**; inherited as unresolved leads from the
  priority audit.
- PhilPapers: **unreachable** (HTTP 403, Cloudflare), same gap as the priority
  audit.

## Limitations

- I did not collate either Brading PDF against the publisher's version; the
  hashes match the project's source record, which is the strongest check
  available offline.
- General web search was largely uninformative this pass (one provider returned
  an exhausted-quota error; the other returned noisy unrelated hits), so no
  negative priority claim rests on it.
- The domain-dilemma paragraph in `REVIEW.md` §4 is my reconstruction of the
  strongest surviving formulation, not a claim that the project has defended it;
  it is a judgement about what could be argued, and I flag that it is
  sub-threshold for a standalone article.
- This audit assesses what is published and what the paper adds. It does not
  assess whether Savitt's objection or Brading's position is correct, and it is
  not a priority certificate.

## Unresolved questions for the coordinator

1. Does any other lane's source set (Mason 2026 published version, Balaguer 2026
   body, Slavov 2022) already apply Savitt's objection to Brading 2015? If yes,
   even the note-level residue disappears.
2. Is the project willing to drop the standalone article and fold the P1\*\*
   material into the quantifier-restriction / trilemma line, where the
   event/unity dilemma is load-bearing rather than decorative?
3. Should `research/existence-form/NOVELTY_AUDIT.md` be amended to quote
   Savitt's verdict sentence rather than only his premise? That file is outside
   this task's ownership; the recommendation is recorded in `REVIEW.md` §5.3.
