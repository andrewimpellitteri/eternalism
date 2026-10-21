# Agent report: covtree-complex-levels

Sole-worker result, 2026-10-21. Files: `RESULT.md`, `check.py`, this report.

## Result

- **Inside the disk (`|q|<1`):** every covtree level has a unique stage limit,
  not only level 2 and principal nodes. The `n`-stem set is a function of the
  `n`-skeleton `K_n`, and the skeleton chain has summable increments by the
  regularized-measure Lemma 1. This extends the growth-completion level-2
  statement to all levels.
- **Boundary `|q|=1`, non-root-of-unity:** the originary (`2-chain`) amplitude
  is `p prod_{j=1}^{m-1}(1-q^j)`. Since `1-q^j` never tends to `1`, the product
  cannot converge to a nonzero limit. Numerically it oscillates/decays for
  `q=e^{i}` and oscillates strongly for `q=e^{i sqrt2}`. If a limit exists it
  is zero, so the boundary does not define a normalized covtree amplitude.
- **Root-of-unity boundary:** the originary product can vanish exactly
  (`q=-1` at `j=2`, `q=1` at `j=1`); other nodes are not classified here.

## Checks

`python3 research/longshots/covtree-complex/check.py`:
- verifies the unit-factor identity `|(1-q^j)-1|=1`;
- prints the boundary partial products for two non-root-of-unity `q` and shows
  non-convergence to a nonzero value;
- checks convergence of the interior `q=1/2` originary product.

## Scope and limits

- The interior existence argument is inherited from the regularized-measure
  Lemma 1; this task did not reprove its skeleton-chain estimates.
- The boundary statement is a failure of a nonzero limit for one node, not a
  classification of every covtree node on the unit circle.
- No new primary full-text reads; Zalel 2302.10582 and Dowker–Zalel
  2212.01149 locators are inherited. No novelty, physical or ontology claim.
