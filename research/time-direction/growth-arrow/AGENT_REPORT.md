# Agent report: novel-growth-arrow

Native research worker (Claude Code, Fable 5.2), 11 November 2026. Submission
for review. Nothing committed. No file outside this directory was changed.

## Files

- `RESULT.md`: verdict, reasons, numbers, credits, limits.
- `sources.jsonl`: 12 records with read depth.
- `growth_reversal.py`: standard-library check, exact rational arithmetic.
- `check_output_n6.txt`, `check_output_n7.txt`: its output for N = 6 and N = 7.
- `AGENT_REPORT.md`: this file.

## Verdict in brief

Transitive percolation has no direction by law: its measure on unlabelled
causal sets is exactly reversal-invariant at every stage, and the only
asymmetry is the built-in beginning. Generic sequential growth is not
reversal-invariant, and is so if and only if it is percolation. Birth order is
label gauge per the authors. So the reading lane's sentence holds for generic
growth as a statement about the law, fails for percolation, and in neither case
is the direction the growth order.

## Evidence

- Rideout–Sorkin (gr-qc/9904062v3) read whole; Brightwell et al.
  (gr-qc/0210061v2) read whole; Sorkin (gr-qc/0703098v1) read whole.
- Passages read in Rideout–Sorkin's second paper (gr-qc/0003117),
  Wüthrich–Callender (1502.00018v1), Bento–Dowker–Zalel (2109.10749) and Dowker
  et al. (1910.07292). Each record says which passages.
- Prior statements found: percolation's time-reversal symmetry (Rideout–Sorkin
  second paper; Wüthrich–Callender); only percolation treats past and future
  births alike (Bento–Dowker–Zalel, Lemma 3.4 and Claim 3.5).
- Proposition A (reversal-invariance at all stages iff percolation) has a
  three-line proof in RESULT.md and is confirmed exactly by the script.

## Checks

`python3 growth_reversal.py 6` runs in about two seconds; `7` takes a few
minutes. Assertions that pass:

- counts of naturally labelled posets 1, 2, 7, 40, 357, 4824, 96428 and of
  unlabelled posets 1, 2, 5, 16, 63, 318, 2045 for n = 1..7;
- probabilities sum to 1 at every stage for every model;
- every natural labelling of one order has the same probability;
- the ratio of the probabilities of "top over an n-antichain" and its reverse is
  exactly tₙ/t₁ⁿ.

Results: percolation (p = 1/2, 1/3, 3/4) has largest difference exactly 0 for
n ≤ 7. tₙ = 1/n! has total variation 0.414 and divergence 0.93 bits at n = 7.
Originary percolation is asymmetric, and exactly symmetric once conditioned on
a top element as well.

## Limitations

- n ≤ 7. The general statements rest on the formulas, not on the enumeration.
- Proposition A covers the generic family only.
- Four papers were read in part. The paper on renormalisation after posts was
  not found or read and is recorded as an unverified lead.
- arXiv version numbers are missing for the three papers read through the ar5iv
  rendering.
- The text extractions dropped figures.
- The "all the integers" argument in §2 of RESULT.md is mine, about labelled
  stretches. It is elementary but unreviewed.

## Unresolved questions

1. Does the reversal asymmetry of a generic model persist far from the
   beginning, for example in the stretch between two late posts, or do the
   effective couplings flow toward percolation? This decides whether the
   generic arrow is fully separable from the beginning.
2. Is past-finiteness to count as law or as boundary condition? RESULT.md says
   boundary condition in substance. A reader may fairly say law.
3. Is there a covariant observable, a combination of stem questions, that
   exhibits the asymmetry in the completed causal set? Stems are one-sided, so
   the comparison with "reversed stems" is not available inside the theory.
4. Does anything survive in a quantum growth dynamics? Not addressed.
5. Whether Proposition A is stated somewhere in the reversal form. I searched
   once and read the nearest paper; I did not search exhaustively.

## Requests to the coordinator

- The settling note's §5 sentence on sequential growth and the reading lane's
  item 6 could be split as in RESULT.md §5. I did not edit either file.
