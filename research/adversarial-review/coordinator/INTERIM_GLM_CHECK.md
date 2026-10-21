# Interim GLM numerical discrepancy: encoding audit

Coordinator observation, 2026-10-21. The GLM scalar worker is still running;
this is not its final submission or verdict. Its current `check_bounded.out`
reports a failed ordinal-block W check. Do not treat that interim failure as a
counterexample to the scalar theorem.

The worker's loop over 40 principal five-orders calls its two-cap helper on
`w=L+M`, which gives exponent L+M+h+1. For a principal five-order M=1, so it
actually sums exponent L+h+2. The historical ordinal-block certificate instead
uses exponent L+min(G)+h+1: its seam contributes an edge to each minimal element.
These are different statistics whenever min(G) differs from one.

Recomputing with the correct seam using the coordinator's independent
forward-edge closure enumerator gives exactly
`W=9/16+105 sqrt(2)/256 = 9/16+105/(128 sqrt(2))`.
The 40-block count and coefficient pair both pass. This check is now asserted
in `check_boundaries.py`. A reviewer should preserve its failed attempt as an
encoding mistake, repair the test, and distinguish it from a failed theorem.

The interim script also hard-codes V_2 as `1/2+sqrt(2)/4`; the only DP two-order
is the two-chain, whose modulus is `1/sqrt(2)`. Its two-cap helper on the empty
G computes the latter correctly. This printed edge case must be corrected.
The script currently prints failures without a nonzero exit; any report of a
clean check must inspect and resolve the actual failed assertions, not cite
exit zero as success.

These observations are confined to a read-only inspection of the worker's
unfinished artifacts. No worker file was changed. Assess its final committed
submission afresh; it may already resolve these issues before handback.
