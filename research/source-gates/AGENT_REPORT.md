# Manuscript source gates

Reader: codex-source-gates, 2026-10-21. Proposals for the manuscript owner.

| Gate | Result | Evidence and limits |
|---|---|---|
| Arageorgis conclusion | CLOSED for quotation and locator | Public journal PDF, printed p. 52 (PDF page 20), visually inspected after local rendering; text extraction compared. |
| Wüthrich–Callender | CLOSED for cited preprint reading | arXiv:1502.00018v1, all five sections read as HTML; journal edition not collated; no mathematical proof reconstruction. |
| Putnam record reconciliation | ALREADY CLOSED in canonical register | Current found-putnam in knowledge/foundations/sources.jsonl records both reading histories and the corrected Principle III interpretation; older proposed record is historical. No fresh primary reading today. |
| Stein printed theorem | CLOSED for printed wording, with caveat | User-supplied 21-page JSTOR scan inspected (pp. 148-150, SHA-256 `fef022...153f7`). The theorem is on p. 149 and includes reflexivity; the displayed statement omits condition (iv), which the proof uses. See `knowledge/audits/stein-printed-pages/PRINTED_VERIFICATION.md`. |

## Arageorgis: verified primary passage

Source: https://scindeks-clanci.ceon.rs/data/pdf/0353-3891/2016/0353-38911629033A.pdf
Edition: Belgrade Philosophical Annual XXIX (2016), pp. 33–55.
Read depth today: full-text at the relevant conclusion, printed p. 52;
not a new full-paper read. The quotation is “parasitic on a block universe view.”
The argument concerns classical sequential growth and the completion needed
for its probability measure. The same page acknowledges a possible role for
cardinality-based growth at substantial philosophical cost. It explicitly
allows that quantum dynamics could change the interpretation.

Proposal: close the lossy-extraction gate for this passage; retain attribution
as the author's philosophical argument rather than a theorem selecting an ontology.
The PDF was downloaded and rendered in /tmp only; no primary PDF is added to git.

## Wüthrich–Callender: verified version and disagreement

Source: https://arxiv.org/html/1502.00018v1
Version: 30 January 2015; journal citation is BJPS 68 (2017), 907–925.
Read depth: full-text HTML, Sections 1–5 and references.
Section 4 states “There is gauge-invariant growth.” Its proposed interpretation
retains a determinate number of events while their identities can be indeterminate.
It raises the completed-future objection, replies through cardinality growth,
and distinguishes this from familiar local becoming. Section 5 preserves a
qualified possibility of becoming with metaphysical costs.

Proposal: keep this position distinct from Arageorgis's criticism. These
preprint section locators are verified; journal page locators are not.
This reading supplies no experimental discriminator and no proof that the
interpretation is uniquely required by the dynamics.

## Putnam: record proposal

Use the canonical foundations record, including reading_history. The first
pass read pp. 240–242; the second examined pp. 241–247. Principle III and the
later closure/observer-abundance argument are distinguished. Replace readiness
claims of unreconciled source records with this integrated status. Formal
reconstruction and defense of the philosophical bridge remain separate tasks.

## Checks and limitations

Visually inspected Arageorgis printed p. 52 with PDFKit rendering; matched the
short quotation and journal running head. Read Wüthrich–Callender Sections 1–5
from pinned HTML. Re-inspected current canonical and historical Putnam records
and the two Stein access reports. No source registry outside this task was edited.
No new novelty, ontology, or theorem claim follows from closing these gates.
Stein remains blocked and is deliberately not upgraded.

## Addendum, 21 October: Stein printed theorem inspected

A user-supplied 21-page JSTOR scan (DOI `10.1086/289609`, local SHA-256
`fef0224102cca5037a9da1878f541ee074e64412fe71e52504b94ebc915153f7`) closes the
printed-wording part of the Stein gate. The theorem is on **p. 149**, not
p. 150, and includes reflexivity and the "at least two dimensions" qualification.
The four conditions (i)-(iv) are on pp. 148-149. The displayed theorem omits
condition (iv), which the proof uses to exclude the universal relation; the
universal relation is a counterexample to the four displayed hypotheses alone.
The article must cite the theorem with that contextual premise or not cite the
isolated display. This is not a claim that Stein's broader argument fails.
