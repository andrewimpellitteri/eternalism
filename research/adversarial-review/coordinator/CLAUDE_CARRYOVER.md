# Claude interruption: preserved experiment and bounded disposition

Coordinator closeout, 2026-10-21. The user supplied the stopped session log.
It ends with a session-usage-limit message during literature fetching, followed
by a partial attempt to collect experiment output. This is an interruption,
not a completed research submission. The desktop Claude host still existing
does not establish that the research turn is running.

The article revision already landed in 09c32b7. The experiment under
`research/longshots/regularized-measure/` was still untracked and has now been
preserved verbatim, excluding generated Python bytecode. The accompanying
`CLAUDE_CARRYOVER_MANIFEST.json` records 34 files, sizes and SHA-256 hashes.
No result report, source register or proof of the general summability claim
was present. The task's existing `claude-longshot` claim is preserved; this
closeout does not accept that task or pretend to replace its worker handback.

## What has actually been checked

The coordinator reran `python3 crosscheck.py 9` against the saved enumeration
aggregates. All eight stem polynomials match the independent skeleton-chain
calculation at every stage 1 through 9; the two-antichain closed form matches
as well. This reruns the comparison, not the original exhaustive enumeration.
The check prints failure but does not itself supply a failing exit status;
the coordinator inspected all printed results. No large enumeration was rerun.

Saved Gaussian-rational sequence calculations cover a real control and four
nonclassical parameters, through stages 40, 60 or 80. Their reported numerical
stability for |q|<1 is evidence about particular sequences, not a measure on
the whole covariant algebra. The saved inclusion-exclusion/additivity check
tests one specific stem identity. It does not prove additivity for arbitrary
events or independence from all approximation or ordering prescriptions.

## A bounded analytic obstruction the coordinator can establish

For the two-antichain stem, the saved exact identity is

`a_n = 1 - product_{j=1}^{n-1}(1-q^j)`.

This identity also has a direct all-stage justification: two minimal elements
form a two-antichain stem, so absence of that stem means the first element is
the unique minimal element. At the birth with j existing elements, the new
element is minimal exactly when all j incoming edges are absent, of weight
q^j. Fresh incoming edges are independent of earlier edge choices. Multiplying
the complementary finite-step weights gives the displayed polynomial identity,
valid for complex p by finite polynomial algebra as well as for probabilities.

At p=-1/2, q=3/2. Write P_n for that product. Then

`|P_n| = q^{n(n-1)/2} product_{j=1}^{n-1}(1-q^{-j})`.

The remaining product tends to a positive constant, since its factors lie in
(0,1) and sum_j q^{-j} is finite. Thus log|a_n| grows as
`n(n-1)log(q)/2 + O(1)`. Consequently both power series
`sum a_n z^n` and `sum a_n z^n/n!` have radius zero. Ordinary Abel summation of
the sequence and ordinary analytic Borel summation are unavailable: their
defining series have no positive-radius germ. Applying the same tests to the
increment series gives the same obstruction. Also |a_{n-1}|/|a_n| tends to zero;
earlier terms are negligible against the last term, so the first Cesaro means
are asymptotic to a_N/N and remain unbounded. This is a one-parameter,
one-event obstruction to these specified methods, not a no-go for every
regularization, analytic continuation or generalized Borel prescription.

## What must remain unverified

- The q-Borel/Padé outputs give sharply different results across directions
  and truncations for several events. Some two-antichain outputs appear
  stable. Neither observation proves a direction-independent summation rule
  on an event algebra. Tiny printed final terms are not error bounds.
- Finite growing variation and sampled ordering diagnostics do not establish
  an infinite rearrangement counterexample. The grouping script's general
  rearrangement comment should not be promoted to a proved result here.
- The skeleton-chain code refers to a missing `REPORT.md` proof. Finite
  polynomial checks support it on their tested domain, not at all stages.
- A common, linear, regular summation operator would preserve a finite event
  identity when all involved sequences are in its domain. Separate Padé fits
  are not such an operator without further proof.
- The pasted literature search is incomplete, and a conference slide claim
  is not a verified primary theorem. No new source reading or novelty claim
  is asserted in this closeout.

Disposition: preserve as an incomplete experimental lane; ordinary Abel/Borel
already fail in the explicit q>1 case above. Any continuation must first state
the generalized summation operator, its domain, consistency on overlaps,
linearity and approximation invariance. Keep it out of both papers until an
independent review establishes those obligations. No packages or large runs
were started to produce this closeout.
