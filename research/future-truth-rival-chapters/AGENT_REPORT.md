# Agent report: future-rival-original-chapters

27 October 2026. Claude (claim holder `claude-rival-chapters`), continuing
the Codex coordinator round after a usage-limit stop.

## Files changed

- `CLAUSES.md`: exact clauses and printed-page locators from chapters 7 and
  9, with an explicit list of what the PDFs do not contain.
- `RESULT.md`: minimal faithful rival, the Contract L/S correspondence,
  domain derivation, bow-tie determination result, closed-dust observations
  and remaining gates.
- `sources.jsonl`: two full-text records with file hashes.
- This report.

No board, manuscript, runner, shared seed or other lane file was edited by
this task. Separately, as coordinator, I moved the four reviewed
future-rival-* tasks to done.

## Evidence

- The user placed the original Springer chapter PDFs in the repo root. PDF
  page labels 99–116 and 135–161 match the printed pages. Text was extracted
  with macOS PDFKit (no install), and both main texts were read in full.
- §4's domain computation uses only the named chapter-9 axioms, plus the
  dust causal criterion already reviewed in the gr-compatibility lane.
- §5 uses the slab {τ<τ_b} ⊂ M∖J⁺(b) and standard linear Cauchy uniqueness,
  as cited in the horizons draft (not re-audited).
- §7's counterexample to (C-AR2) is an exact inequality argument with its
  boundary cases checked.

## Checks

`sources.jsonl` was checked for the required keys and a valid read_depth.
No numerical runs. Formulas were checked against the extracted text. The
superscript layout of ω_t^loc/ω_t^ex was reconstructed from line breaks.

## Limitations

- Reference lists, Appendices 2–3 and chapters 1–5 are absent. The free logic
  and the reference of @m to non-existents are therefore unchecked.
- (GR_R) and the relativistic reading of "future contingent" are our
  transcriptions.
- The bridge premise in §5 (field values at existing points are natural
  features of what exists) is not defended.
- The dust frame is not checked against all of chapter 9's axioms.

## Unresolved

- Independent review (done_when item 3) has not been run. The task is
  submitted for review, not accepted.
- The project needs a reply to C&R's persistence and point-edge objections
  before relying on E_b=J⁻(b).
- Whether a causal-past ontology can motivate refusing the bow-tie domain
  without begging the question against C&R.

## Coordinator integration, 28 October 2026

Independent selected-source review is in review/REVIEW.md. Applied the
conditioning-base correction in RESULT §5 (new S_bow versus original S),
restricted the supervenience conclusion to one-point field claims, removed
a determination-to-grounding inference, and tightened p.100 attribution.
REVIEW_RESOLUTION.md records scope and remaining gates. Original report
above is the historical submission; this addendum updates its review status.
