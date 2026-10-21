# Agent report: totality-logic audit

## Task

Independent philosophical-logic audit of `paper/main.tex` at commit `4be7c99`
(“Rebuild note around the totality reductio of P1\*\*”). The audit assesses
whether the draft’s totality reductio, its 2013/2015 “incompleteness” claims,
its retreat-to-subsystems argument, and its four-event model establish their
conclusions from Brading’s texts.

## Files changed

- `paper/reviews/totality-logic/REVIEW.md` (new; the audit)
- `paper/reviews/totality-logic/AGENT_REPORT.md` (new; this report)

No other files were edited. No commits, pushes, merges, or agent launches. The
modifications present at the start of the task (`output/pdf/temporal-ontology-working-draft.pdf`,
`paper/check_records.py`, `paper/verification.json`) were committed by the
coordinator in `b08d14f`, not by this agent. At the time of writing, the working
tree contains an uncommitted edit to `paper/main.tex` made outside this task;
it is noted under Limitations and was not touched. The untracked
`research/existence-form/alternative-contribution/` directory was read only.

## Sources and read depth

| Source | Version / locator | Depth |
|---|---|---|
| Brading, “Presentism as an Empirical Hypothesis,” *Phil. Sci.* 80 (2013) 1101–1111 | Public published-layout PDF, SHA-256 `c93ca072e14c4fd0f1c638ff960db17847231479ec9bf168cf0d69f9644bb054`; matches `research/article-admissibility/primary-review/SOURCES.md` | Full text, all 11 printed pages; pages 1102–1106, 1109–1110 checked closely |
| Brading, “Physically Locating the Present,” *SHPS-A* 50 (2015) 13–19 | Public published-layout PDF, SHA-256 `7caceae74aebe28d1775561cd307dce50f912570eb1a7f9a709d70c699b08f6b`; matches the same record | Full text, all 7 printed pages; pages 16–18 checked closely |
| Savitt, SEP *Being and Becoming in Modern Physics*, §3.3 “Localizing Time” | Live SEP entry, substantive revision 6 October 2021 | Full text of §3.3, not the whole entry |
| `research/existence-form/alternative-contribution/REVIEW.md` | Working tree | Full text |
| `paper/reviews/p1-logic-audit/REVIEW.md` | Working tree | Full text |

Saunders, Pooley and Clifton–Hogarth were not independently re-read. Their use
in the draft is peripheral; the audit assesses it only against the project’s
recorded quotations and says so in `REVIEW.md` §10.

## Evidence and checks

1. **Hash verification.** Both Brading PDFs were fetched from the public URLs in
   `SOURCES.md`; `shasum -a 256` matched the recorded hashes exactly.
2. **Quotation verification.** Every Brading quotation in the draft was checked
   against the extracted text. All are verbatim. The defects are:
   - the 2013 n. 3 locator is printed on p. 1105, not p. 1106 (draft l. 133);
   - the n. 3 quotation stops before “Different principles of unity might be
     used for the different cases,” which is material to the paper’s
     “scale-free” diagnosis;
   - T1 cites p. 16, but the unconditional “what exists are the genuine
     unities” is p. 17; the p. 16 sentence is conditional.
3. **Logical checks.**
   - T1: “applies all the way up to the material universe as a whole” gives
     scope, not unity; the p. 16 aggregation sentence is a condition, not an
     assertion that the universe satisfies it. T1 needs a separate premise.
   - T4: “necessary to sustain” is not “contains all members”; the Cauchy-slice
     / global-slab alternative is not excluded by p. 17’s “common to all
     systems” qualifier; the p. 16 aggregation sentence does not require `W`.
   - 2013 defeat condition: “for whatever system we try to consider” is
     universal; the “in other words” is valid one way, not as an equivalence.
     The condition is sufficient, not exhaustive.
   - 2015 survival condition: “only if” is necessary, not sufficient; the draft
     attacks a sufficiency claim Brading does not make.
   - Four-event model: `W={a,b,c,d}`, `H_1={a,b,c}`, `U_1={a,b}`, `H_2={b,c,d}`,
     `U_2={c,d}`. (a) and (b) hold; union is `W`; the histories and presents are
     coherent; (b) is not trivially violated. The model is valid as a formal
     non-implication, but it drops “necessary to sustain” and assumes a common
     domain that 2013 n. 7 denies.
   - “Scale-free”: misdescribes Brading; 2013 n. 3 allows different principles
     for different cases, and 2015 p. 18 says subsystems are “as picked out by
     the dynamical laws.”
4. **Build check.** A copy of `paper/main.tex` and `paper/references.bib` was
   compiled in a temporary subdirectory of this review directory with
   `pdflatex`/`bibtex`: 8 pages, no unresolved references, no overfull boxes.
   The temporary PDFs and extracted text were removed after the audit; only the
   two Markdown deliverables remain.
5. **Text-extraction check.** The published-layout PDF text is clear; no OCR
   reconstruction was needed. I did not collate against the publisher’s HTML.

## Findings (summary)

- **T1:** not sound as a textual entailment. The “insofar as” at 2015 p. 16 is a
  genuine conditional; p. 17 adopts the identification as a working premise, and
  p. 16 says the law-constitutive approach is not argued for there. “Applies up
  to the universe” does not entail the universe is a unity.
- **T4:** not sound as stated. A proper, spatially global sustaining region
  (Cauchy slice / thick slab) is not excluded by the p. 17 sentence, which is
  qualified by “common to all systems.” The p. 16 aggregation sentence is a
  condition, not a premise about the universe. The draft’s §8 concedes a proper
  local region could make (a) true, contradicting §3’s categorical conclusion.
- **2013:** the distinction between the universal scenario and the
  universe-own-region scenario is correct, but the “incomplete” charge needs
  restatement: the condition is sufficient, not exhaustive, and the “in other
  words” is one-directional. The section’s opening “makes the same point in a
  different form” is wrong.
- **2015:** “necessary but not sufficient” is logically correct, but the
  criticism is misdirected; Brading asserts necessity, not sufficiency. The real
  criticism is that she treats subsystem existence as the decisive empirical
  question.
- **Retreat/coverage:** the quantifier restriction follows, but the “two costs”
  are not independent. The four-event model is valid and coherent, but models
  the paper’s formalisation, not Brading’s dynamics, and assumes a common domain
  that 2013 n. 7 denies.
- **Scale:** “scale-free” is a reconstruction; 2013 n. 3 explicitly allows
  different principles for different cases; 2015 p. 18 supplies a selection
  procedure (“as picked out by the dynamical laws”). “Brading supplies neither”
  is false.
- **Verdict:** needs revision. Publishable as a short note if T4 is defended or
  the result is reframed as a trilemma; not publishable as a categorical
  refutation in its current form.

## Limitations

- No independent re-read of Saunders, Pooley or Clifton–Hogarth; their use is
  inherited from the project record and is peripheral.
- No publisher HTML collation of the Brading PDFs; quotations are from the
  published-layout PDFs with verified hashes.
- No read of Brading 2011, 2012 or 2014. The 2015 p. 16 identity is a summary of
  those works; the 2014 chapter is the most likely place for a qualification.
  The paper’s “Brading holds” is inherited from 2015, not established across the
  corpus.
- No priority search. The audit is about logic and textual support, not novelty.
  The project’s `alternative-contribution/REVIEW.md` records the search limits
  (PhilPapers and Scholar unavailable), and those limits carry over.
- The review is a philosophical/logical assessment, not a proof of Brading’s
  view or of presentism/eternalism.
- The working tree changed during the audit: after commit `b08d14f`, an
  uncommitted edit to `paper/main.tex` rewrote the T4 sentence and the
  “scale-free” sentence. The audit’s quotations and line numbers refer to
  `4be7c99`; the later edit does not change the verdict. It removes the
  “universe’s unity is constituted by the relations among its members”
  formulation but does not add the premise that the universe satisfies the
  aggregation condition, and it does not address the n. 3 omission.

## Unresolved questions

1. **Is the universe a genuine unity on Brading’s account?** The strongest route
   is the isolation/conservation condition (2013 p. 1105; 2015 p. 16), but the
   “whole (consisting of interacting parts)” qualifier (2013 p. 1110) may exclude
   a spatiotemporal totality whose parts never interact. This needs a decision.
2. **Is “necessary to sustain” extensional or dynamical?** If dynamical, the
   Cauchy-slice alternative is live and T4 fails. If extensional (the region
   containing all members), T4 follows but the premise is not Brading’s.
3. **Does 2013 n. 7 defeat the common-domain formalisation?** If `W` is only the
   epistemic representation, the coverage argument is about the representation,
   not the ontology. The paper needs either a defence of the common domain or a
   restriction of the conclusion.
4. **Does the 2014 chapter restate or qualify the p. 16 identity?** Unread; a
   referee may require it.
5. **Is the Savitt delta sufficient?** Savitt’s universal premise applied to the
   universe is close to the draft’s T4; the delta is the target (P1\*\* and the
   universe’s own region) and the conclusion (metaphysical vs semantic), not the
   premise.
