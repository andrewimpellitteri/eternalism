# baseline-reproduction — Dowker–Zalel finite-level variation on (doubly-)reduced poscau

Status: 2026-10-20. Claimed by `opencode-coordinator` because the GLM quota was
exhausted. Selected target: the labelled doubly-principal complex-percolation
classification, with RC-1 as fallback (`research/redteam/selection-gate/DECISION.md`).
This task reproduces the **published baseline** that the candidate extends. It
does not reproduce the candidate's all-level theorem, and it makes no novelty or
ontological claim.

## Named published result

Dowker & Zalel, *Observables for cyclic causal set cosmologies*,
arXiv:2212.01149v2, Secs. III.3–III.4 and V, Eqs. (23)–(26), (30)–(31),
Theorems 14–15, Figs. 6–7.

**Result reproduced.** For Complex Transitive Percolation
`A_p(C) = p^L (1-p)^{binom(n,2)-R}` (Eq. 26), on the reduced poscau the level-`n`
minimum variation `zeta_n^min` (Eq. 25), and on the doubly-reduced poscau the
valency-greater-than-one minimum `zeta_bar_n^min` (Eq. 30), equal
`|p| + |1-p| - 1` for `n = 2, 3, 4` in the regions coloured in Fig. 6/7.

**Explicit scope.** The figures are numerical and region-coloured. The paper's
stronger suggestion — a level `m` above which the equality holds for every
`p` — is not proved and is not reproduced here. The asymptotic improved
criterion Eq. (31) is not evaluated; only its finite inputs (`S_n`, `S_bar_n`,
`S_n^{v=1}`) are reported. The covariant algebra `R_p` and the candidate's
doubly-principal extension theorem are outside this reproduction.

## Implementation

Files (standard library only, no dependencies):

- `experiments/baseline/poscau.py` — natural-labelled causet enumeration,
  cover/relation counts, amplitudes, down-set children, and the two tree
  constructions.
- `experiments/baseline/reproduce.py` — the reproduction and checks.
- `experiments/baseline/test_poscau.py` — seven unit checks.

Construction used:

1. Causets are naturally labelled partial orders on `{0,…,n-1}` (`i ≺ j ⇒ i < j`),
   enumerated by relation masks and filtered for transitivity. Counts:
   `n=1…6` → `1, 2, 7, 40, 357, 4824`.
2. A causet is principal iff it has a unique maximal element. A child is
   obtained by adding element `n` above any down-set of the parent; the
   principal child is the down-set of all elements. A child is doubly principal
   iff it is principal and its parent is principal.
3. Reduced poscau: a node's children are one singleton node per principal child
   plus one merged node of all non-principal children. Doubly-reduced poscau:
   the same with “doubly principal”.
4. A node amplitude is the sum of the causet amplitudes in the node; the
   transition amplitude is the ratio of child to parent node amplitudes. This
   makes the sum over children exactly one whenever the parent amplitude is
   nonzero, and is the semi-ring/tree additivity the paper relies on.
5. `zeta(node) = sum_i |A(child_i)| / |A(node)| - 1`; for the doubly-reduced
   tree the improved criterion uses the minimum over nodes of valency greater
   than one, and `S_n`, `S_bar_n`, `S_n^{v=1}` as in Eq. (30).

## Results

At `p = (1+i)/2`, `|p| + |1-p| - 1 = 0.414213562373…`:

| level | reduced `zeta_min` | doubly `zeta_bar_min` | nodes (red/dbl) |
|---|---|---|---|
| 2 | 0.414213562373 | 0.414213562373 | 2 / 2 |
| 3 | 0.414213562373 | 0.414213562373 | 4 / 3 |
| 4 | 0.414213562373 | 0.414213562373 | 11 / 5 |

This is the published finite-level value for `n = 2, 3, 4`. The reduced tree has
no valency-one nodes at these levels; the doubly-reduced tree does, and its
`zeta` is zero on them, which is exactly why the paper introduces the
valency-greater-than-one criterion.

Grid (`p` real and imaginary from `-0.5` to `1.5` in steps of `0.1`, 441 points):

- reduced: equality at `n=2`: 340/441, `n=3`: 362/441, `n=4`: 384/441;
- doubly-reduced `zeta_bar`: `n=2`: 440/441, `n=3`: 303/441, `n=4`: 316/441.

Mismatches concentrate outside the positive-probability region and in parts of
the complex plane; the paper's figures colour exactly such regions. The grid is
coarse and is not a proof of the coloured boundary.

Improved-criterion inputs at `p=(1+i)/2`:

| tree | n | `zeta_bar_min` | `S_n` | `S_bar_n` | `S_n^{v=1}` | nodes |
|---|---|---|---|---|---|---|
| reduced | 2 | 0.414214 | 1.414214 | 1.414214 | 0 | 2 |
| reduced | 3 | 0.414214 | 2.144123 | 2.144123 | 0 | 4 |
| reduced | 4 | 0.414214 | 3.606013 | 3.606013 | 0 | 11 |
| doubly | 2 | 0.414214 | 1.414214 | 0.707107 | 0.707107 | 2 |
| doubly | 3 | 0.414214 | 1.707107 | 1.207107 | 0.500000 | 3 |
| doubly | 4 | 0.414214 | 2.358495 | 2.004941 | 0.353553 | 5 |

The nonzero `S_n^{v=1}` on the doubly-reduced tree is the term Dowker–Zalel
leave to future work.

**Separate candidate check.** The selected target's finite certificate at
`p=(1+i)/2` is reproduced exactly in `Q(sqrt 2)`, independently of
`research/creative/proof-audit/verify_small.py`:

- `V_5 = 3/4 + 3 sqrt(2)/16` (7 doubly-principal causets),
- `V_6 = 31/32 + 55 sqrt(2)/64` (40 doubly-principal causets).

This checks the candidate's finite arithmetic; it does not reproduce its
all-level divergence proof.

## Independent analytic and known-limit checks

- **Additivity:** for every causet at levels 1–4 (50 causets), the sum of child
  amplitudes equals the parent amplitude to `0.000e+00` (floating point). This
  is the tree/semi-ring consistency the transition-ratio construction relies on.
- **Real probability limit:** at `p = 0.5`, every `zeta` on both trees is `0`
  (max `|zeta| = 0`), as it must be for a positive probability walk.
- **Level-2 analytic value:** the reduced `zeta` minimum and the doubly
  `zeta_bar` minimum both equal `|p|+|q|-1` at `p=(1+i)/2`; the non-principal
  antichain node is strictly higher, which is why the paper compares minima.
- **Causet counts:** `1, 2, 7, 40, 357, 4824` for `n=1…6`, matching the
  natural-labelled enumeration used by the projects' earlier 40-block
  certificate.
- **Unit tests:** `python3 -m unittest -v test_poscau` — 7 tests, all pass.

## Discrepancies and limits

- `zeta` is computed in floating-point complex arithmetic. The exact
  `Q(sqrt 2)` arithmetic is used only for the `V_5`/`V_6` certificate. Equality
  assertions use `1e-9`; the reported values agree to `1e-12`.
- The published figures' exact coloured regions were not digitized. The grid
  reports mismatch counts and examples; it does not claim the full region.
- Only `n = 2, 3, 4` are computed, matching the published figures. The all-level
  suggestion and Eq. (31) asymptotics are not checked.
- The transition-amplitude-equals-ratio convention is not spelled out in the
  paper in one sentence; it follows from the tree/semi-ring construction and is
  validated by the additivity check and by matching the published minima.
- The read text is the arXiv HTML v2; the PDF/published version was not
  compared. No external dependency or install was used.
- This is a reproduction of a published numerical criterion, not a proof of the
  candidate theorem, not an external acceptance, and not a priority claim.

## Commands

```sh
cd experiments/baseline
python3 -m unittest -v test_poscau
python3 reproduce.py
```

## Handoff

`extension-search` can now work against a reproduced baseline. `lean-certificate`
should target the candidate's two-cap bound and the doubly-principal
classification, not this finite criterion. `adversarial-review` should check
whether the candidate's estimate is a corollary of Dowker–Zalel's criterion and
whether the finite certificate's `V_5`/`V_6` values are the right target.
