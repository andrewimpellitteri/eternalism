# Lane C report: rank-factor audit

Status: submitted for coordinator review. Verdict: **CONDITIONAL PASS after repair**.

## Files written

* `RESULT.md` — independent structural and analytic audit, exact counterexample to a displayed bound, corrected (b=1) growth proof, exact claim contract, strongest defeater, limits.
* `sources.jsonl` — primary-source records with versions and read depth.
* `SEARCH_LOG.md` — bounded priority routes and exact predecessor comparisons.
* `check_bipartite_bound.py` — exact finite regression for the (b=1) capped-bipartite family and counterexample.

## Main finding

The rank-dependent no-go is not refuted, but the submitted proof's Lemma 2(iii) is false when (|1-p|=1) and (|p|<1). For (p=(50+120i)/169), exact moduli are (a=10/13,b=1), and the (m=1) capped-bipartite family exhausts the two naturally labelled principal 3-orders (chain and fork), so (W_3=2a^2=200/169), below the asserted (a(1+a)=230/169). The correct cover count is (|E|+m+z(E)), where (z(E)) counts isolated lower vertices. Summing gives (a^m((1+a)^m+a-1)^m) for odd levels and (a) times this for even levels. Its quadratic-exponential growth suffices for bridge-weighted convergence. The other exponent typo in the bridge lemma is repaired by bounding the number of distinct constrained edges by the total edge count. The star lower-bound inequality survives, though its claimed multiplicity explanation was wrong.

## Evidence and checks

* Ran `python3 research/rank-renewal-convergence/check_weighted.py`; all embedded finite exact checks passed. Its (b=1) check only uses (p=2), which explains why it did not expose the (a<1) issue.
* Ran `python3 research/refocus-2026-10-21/rank-audit/check_bipartite_bound.py`; exact enumeration for (m=1..4) matched the corrected and restricted-family formulas and reproduced the rational counterexample.
* Independently re-derived the disjoint same-rank events, laminar all-rank family, next-post child partition, ordinal-sum label multiplicity, total-variation attenuations, renewal convolution, three weighted-estimate regimes after correction, and endpoint handling. Exact script checks corroborate finite cases; the general proof is structural.
* Read the relevant primary sections of Dowker–Zalel 2212.01149v2, Surya–Zalel 2003.11311v1, and Dowker–Johnston–Surya 1007.2725v1. Compared the rank-rule scope against classical post papers. Bounded searches found no exact matching result; global priority is unverified.

## Strongest defeater and scope

The strongest immediate defeater was the false (b=1) lower bound. The exact counterexample is recorded, and the theorem's proof route is repaired with a corrected lower bound. Remaining mathematical defeaters are a structural flaw in the next-post child partition/renewal identity or a prior matching theorem under the exact all-principal rank-only rule. The rule is an added premise, not implied by covariance. The proof does not use a null-complement shortcut for complex measures: it uses literal ν(℘∞)=1 and only events inside ℘∞. Classical positive-parameter sufficiency imports the established infinite-post result; the original Alon et al. proof was not reproduced.

No commit or shared-board edits were made. No installations or extra agents were used.
