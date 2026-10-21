# Covtree amplitudes for complex percolation: all levels inside the disk, failure on the boundary

Sole-worker result, 2026-10-21. Extends the level-2 computations in
`research/longshots/growth-completion/` and the skeleton-chain lemma in
`research/longshots/regularized-measure/REPORT.md`. No novelty claim.

## Setting

Complex percolation has `q=1-p`, `A_p(C)=p^L q^h`. A covtree node at level
`n` is a set of infinite causets with a prescribed `n`-stem set
`Gamma`: `N_Gamma = {C : stems_n(C)=Gamma}`. The stage-`m` value is the sum of
`A_p` over labelled `m`-causets whose `n`-stem set is `Gamma`.

## Inside the disk: existence at every level

Assume `|q|<1`. Let `K_n(C)={x : |past(x)| <= n-1}` be the `n`-skeleton.
Every `n`-element down-set of `C` is contained in `K_n(C)`, and its order is
determined by the induced order on `K_n(C)`. Hence the `n`-stem set is a
function of the finite skeleton `K_n(C)`.

The skeleton chain is an exact marginal Markov chain: a new element joins
`K_n` iff its past has size at most `n-1`; all other moves leave `K_n`
unchanged. With `s_m <= (m+1)^{n-1} max(1,|p|)^{n-1}|q|^{m-n+1}`, the
trajectory variation `T_n <= prod(1+2s_m)` is finite for `|q|<1`, so the
increments are summable and every stem-event amplitude converges locally
uniformly. This is Lemma 1 of `regularized-measure/REPORT.md`.

Since the stem set is a finite function of `K_n`, every covtree node value at
level `n` is the limit of its stage values, and the limit is unique (the
skeleton trajectory measure is countably additive). This holds for **all**
levels `n`, not only level 2 or principal singleton nodes.

## Boundary circle: no nonzero originary amplitude

Take `|q|=1` and `q` not a root of unity, for example `q=e^{i}`. The originary
event (the first element is below every later element) has the `2-chain` stem
set; its stage-`m` value is

```
p prod_{j=1}^{m-1} (1-q^j).
```

The factors `1-q^j` do **not** tend to `1`: `|(1-q^j)-1|=|q^j|=1` for every
`j`. A product can converge to a nonzero finite limit only if its factors tend
to `1`. Therefore the originary stage values cannot converge to a nonzero
normalized amplitude. If the product converges at all, its limit is `0`; if it
oscillates, there is no limit. Either way the boundary does not define a
normalized covtree amplitude for this node.

The finite computation shows the oscillation/decay: for `q=e^{i}` the
originary magnitudes `|p prod(1-q^j)|` are `3.94, 5.22, 11.15, 101.1, 23.98,
0.435, 0.054, 1.5e-5` at `m=10,50,100,200,500,1000,2000,5000`. For
`q=e^{i sqrt2}` they oscillate much more strongly: `1.76, 1.45, 8.06, 103.2,
51.8, 30.4, 49.5, 312.8` at the same stages. Neither sequence is settling to a
nonzero value; the phases also move. At roots of unity the product can vanish
identically (e.g. `q=-1` gives a zero factor at `j=2`, `q=1` at `j=1`).

## Verdict

- `|q|<1`: covtree amplitudes exist at every level and are unique; the
  growth-completion level-2 statement extends to all levels.
- `|q|=1`, non-root-of-unity: at least the originary amplitude fails to have a
  nonzero limit; the stage-limit covtree "measure" is not normalized. The
  boundary is not a continuous limit of the interior construction.
- Root-of-unity boundary: the originary product can vanish exactly; other
  nodes require separate treatment.

## Predecessors and read depth

Zalel, arXiv:2302.10582v1 (review) and Dowker–Zalel, arXiv:2212.01149v2
(Sec. V) define the covtree setting and leave the doubly-reduced complex case
open. The skeleton-chain lemma and its convergence proof are in the project's
`regularized-measure` report, which is the load-bearing prior artifact here.
No new primary full-text reads were added in this task; the locators are
inherited from the source records.

## Check

`python3 research/longshots/covtree-complex/check.py` computes the boundary
partial products at high precision and the interior `q=1/2` comparison, and
verifies the factor-distance identity `|(1-q^j)-1|=1` for unit `q`.
