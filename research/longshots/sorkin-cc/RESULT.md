# Sorkin even convergence for complex-percolation stem events

Sole-worker application, 2026-10-21. Primary: Sorkin, "Toward a fundamental
theorem of quantal measure theory", arXiv:1104.0997v1. Read depth: full text
at Section 7 and its theorem, PDF pp. 37-38; not a full-paper audit.

## The prescription, stated exactly

Sorkin defines a sequence of events `A_n` to be **evenly convergent** to `A`
with respect to the vector measure `mu` when:

1. `A = lim A_n` set-theoretically;
2. `mu(A) = lim mu(A_n)` exists;
3. for every `epsilon>0` there is `N` such that for all `n>N`,
   `sum ||mu(Z)|| < epsilon`, where the sum ranges over cylinder events
   `Z` at level `n` that **straddle** `A` (meet both `A` and its complement).

This is the measure-based criterion of Section 7 (conditions (i)-(iii),
p. 38). Sorkin proves that disjoint open events with evenly convergent
canonical approximants have additive limits, and that the C1 and C2 canonical
approximants agree when condition (iii) holds. The theorem is stated for open
events; it does not by itself extend the measure to the whole sigma-algebra.

## Application to stem events

A stem event `E_S = {C : S is a down-set of C}` is open in the path topology:
membership is witnessed by a finite down-set. For `|q|<1`, the `n`-skeleton
chain `K_n` has summable trajectory variation (regularized-measure Lemma 1),

```
sum_m (m+1)^{n-1} max(1,|p|)^{n-1} |q|^{m-n+1} < infinity.
```

The cylinders at level `m` that straddle `E_S` are exactly those whose
`n`-skeleton is not yet decided for or against `S`; their total norm is
bounded by the skeleton tail, which tends to zero. Hence condition (iii)
holds, `mu(E_S)` exists as the limit of the stage values, and the limit is
independent of the canonical approximant (C1/C2). Disjoint stem events with
evenly convergent approximants add by Sorkin's theorem. This gives existence,
order-independence in the even-convergence sense, and finite additivity on
the open stem events.

For `|q|=1` the skeleton tail need not vanish. The originary amplitude
`p prod_{j=1}^{m-1}(1-q^j)` has no nonzero limit (see
`research/longshots/covtree-complex/RESULT.md`), so condition (iii) fails for
at least one stem event; even convergence is not available on the boundary.

## Finite stem values

Exact Gaussian-rational sums over labelled causets through `m=6` (not yet the
infinite limit):

| stem | p=(1+i)/2, m=4 | m=6 | p=0.8+0.3i, m=4 | m=6 |
|---|---|---|---|---|
| 2chain | 0.875 | 0.742188-0.171875i | 0.772205+0.037590i | 0.751389+0.036248i |
| 2anti | 0.875-1.000i | 0.667969-1.386719i | 0.162715-0.437142i | 0.145965-0.426680i |
| 3chain | 0.625+0.375i | 0.367188-0.132812i | 0.589220+0.272970i | 0.554445+0.245893i |
| 3anti | -0.625-0.375i | -1.101562+0.140625i | -0.060750+0.007314i | -0.055153+0.015966i |
| V | 0.375 | 0.152344-0.167969i | 0.268165-0.129306i | 0.248705-0.144676i |
| Lambda | 0.750-1.000i | 0.410156-1.558594i | -0.065080-0.399552i | -0.102646-0.390432i |

The values are settling in the tested range; the skeleton lemma is the
convergence proof, not the table. The `2chain` row is the *stem-present*
event, which is weaker than the originary event (the first element below all
later ones); the two must not be equated.

## Verdict

- `|q|<1`: Sorkin's even convergence applies to stem events; values exist,
  are approximant-independent, and are finitely additive on disjoint open
  stem events. This is the same domain as the skeleton-chain convergence, so
  it does not add a new extension theorem.
- `|q|=1`: even convergence can fail; the boundary is not covered.
- DJS's uniqueness question is answered here only in the even-convergence
  sense, not for arbitrary countably additive extensions of the stem algebra.

## Prior work and limits

Sorkin 1104.0997v1 Sec. 7 supplies the criterion and the disjoint-open-event
theorem. Dowker–Johnston–Surya 1007.2725 raise the uniqueness question for
complex percolation. The skeleton-chain convergence is the project's
regularized-measure Lemma 1. No new general extension theorem, priority claim
or physical/ontological conclusion is made. The finite table is corroboration,
not the proof.

## Check

`python3 research/longshots/sorkin-cc/check.py` computes the six stem values
at the two complex `p` values through `m=6` and prints them; it is an exact
Gaussian-rational enumeration of labelled causets.
