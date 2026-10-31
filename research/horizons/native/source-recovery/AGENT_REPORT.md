# Agent report: native-horizons-source-recovery

## Files changed

- `research/horizons/native/source-recovery/SOURCE_GAPS.md`
- `research/horizons/native/source-recovery/sources.jsonl`
- `research/horizons/native/source-recovery/AGENT_REPORT.md`

## Verdict

Partial source recovery. I personally inspected the original Earman scan images
for printed pp. 125–130 in this continuation; the retrieved PDF/images were
created by the stopped run, and its OCR/summary is separately recorded. The
inspection confirms broad overlap on prediction framing, the Cauchy-surface
case, and the Maxwell constraint example citing Ellis–Sciama. Ellis–Sciama
pp. 41–42 remain unread. For Wald I saw only search-index excerpts, not the
original selected pages; Wald remains discovery-level and unverified. The paper
should retain the overlap disclosure and make no priority claim for the
three-diamond theorem.

## Evidence and checks

- Read the required repository instructions, README, knowledge README,
  novelty strategy, and assigned brief. Read the existing horizon gates and
  current theorem statement before source evaluation.
- Examined the stopped GLM run’s event log and result. It reported quota
  exhaustion (HTTP 429/code 1308); no GLM restart was made. I then visually
  inspected `/private/tmp/opencode/ear_big_69.png` (p. 125),
  `ear_big_70.png` (pp. 126–127), `ear_big_71.png` (pp. 128–129), and
  `ear_big_72.png` (pp. 130–131) with `view_image`. The underlying inherited
  PDF is `/private/tmp/opencode/earman1995.pdf`. The stopped-run OCR output is
  separately locatable at `.agent-runtime/runs/horizons-priority-gap-check/
  events.jsonl`, line 131; it corroborates page mapping but is not my sole
  evidence. Its saved record reports Google Books search-inside blocked for
  Ellis–Sciama.
- Bounded public-source search found original book/catalog information for
  Earman and search-index excerpts pointing to Wald Appendix D. I did not
  inspect Wald’s scan; those excerpts remain discovery-level leads.
- Checked that `sources.jsonl` is valid JSONL and that only the lane directory
  was changed.

## Limits and unresolved questions

The original Ellis–Sciama target remains inaccessible. The Earman reading is
selected-page full text, not a proof audit of the book or a complete
theorem-to-source comparison. Wald remains unverified in this lane: only
search-index excerpts were read, and the exact scalar-rescaling page/equation
is unresolved. Nothing here certifies novelty, priority, or absence of a
predecessor.
