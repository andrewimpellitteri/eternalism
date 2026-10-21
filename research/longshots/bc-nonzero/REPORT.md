# Nonvanishing stage-4 continuation of the fixed phase seed

## Verdict

The fixed stage-3 BCPH phase seed **does have an exact all-transition-nonzero
stage-4 continuation** under the scalar amplitude-ratio Bell-causality rule
used in the preceding `bc-holonomy` lane. No obstruction for this seed arises.
The construction is a one-complex-parameter subfamily; it preserves the
nontrivial `cp` holonomy `(3−4i)/5` at stage 4. This is a finite scalar QSG
counterexample to the proposed fixed-seed no-go, not a classification of all
stage-4 dynamics, not a no-go for other stage-3 phase families, and not an
operator-QBC result.

The relevant existing work is in the read-only
[zero-aware stage-4 report](../bc-holonomy/REPORT.md) and its stage-3 seed. The
new exact certificate is `nonzero_continuation.py`; its output is
`check-output.txt`.

## BC reduction and Markov parametrization

Let `t(C,P)∈ℂ` be the transition amplitude from a naturally labelled parent
causet `C` with precursor/down-set `P`. Set

```
g_C := t(C,∅),                 r_∅ := 1,
r_P := t(P,P)/g_P              for nonempty earlier causets P.
```

For a proper nonempty precursor `P⊊C`, apply Bell causality to the pair of
precursors `∅,P`. Their union is `P`; the reduced transitions in `P` are its
gregarious transition `g_P` and its timid transition `t(P,P)`. Thus

```
t(C,∅) t(P,P) = t(C,P) t(P,∅),
t(C,P) = g_C r_P.
```

The same expression holds for `P=∅` by `r_∅=1`. All denominators are valid in
the current task's domain because every transition is required nonzero. Let
`r_C:=t(C,C)/g_C`. MSR then gives

```
1 = Σ_(P down-set of C) t(C,P)
  = g_C Σ_(P down-set of C) r_P,
g_C = 1 / Σ_(P down-set of C) r_P,
r_C = 1/g_C − Σ_(P⊊C) r_P.
```

Consequently, once the earlier `r_P` values are fixed, the only new free
complex parameter at a parent `C` is its full-precursor value `r_C`
(equivalently `g_C`), subject to nonzero amplitudes and a nonzero MSR
denominator. At stage 4, if `B=P∪Q` is proper in a 3-element parent, then
`B` has at most two elements. The earlier seed has a unique natural labeling
for each 1- or 2-element causet, so `r_P/r_Q=r_P̄/r_Q̄` in this bounded case;
the recurrence therefore implies that pair's BC equation. If `B=C`, the
equation is an identity. This reduction is not asserted for later stages
where the reduced precursor can have multiple natural labelings with distinct
phase data. The checker nevertheless tests every stage-4 pair directly.

## Fixed seed and exact continuation

Use the fixed seed from `birth-order-interference/REPORT.md`:

- Stage 1: `t(1,∅)=1/2`, `t(1,1)=1/2`.
- From the 2-chain, precursor sizes `0,1,2` have amplitudes
  `(1/4, 1/4, 1/2)`.
- From the 2-antichain, the empty precursor, each singleton precursor, and
  the full precursor have amplitudes
  `((3+4i)/20, (3+4i)/20, (3+4i)/20, (11−12i)/20)`.

These transitions are all nonzero and obey MSR and scalar amplitude BC. The
induced `r` data for the two 2-causets are

```
r_∅ = 1,
r_(2-antichain) = (-3−16i)/5,
r_(2-chain) = 2.
```

For every naturally labelled 3-element parent `C`, choose the same
gregarious amplitude `g_C=1`. Define

```
S_C := Σ_(P⊊C, P down-set) r_P,
r_C := 1 − S_C,
t(C,P) := r_P       for P⊊C,
t(C,C) := r_C.
```

This is precisely the BC/MSR parametrization above with common denominator
`Σ_(P⊆C)r_P=1`. The exact proper sums and resulting timid amplitudes are:

| Stage-3 parent, canonical relation key | `S_C` | `r_C=t(C,C)` |
|---|---:|---:|
| 2-antichain + point `(3,())` | `(11−48i)/5` | `(-6+48i)/5` |
| `cp` labeling 1 `(3,((0,1),))` | `(22−16i)/5` | `(-17+16i)/5` |
| `cp` labeling 2 `(3,((0,1),))` | `(22−16i)/5` | `(-17+16i)/5` |
| `Lambda` `(3,((0,1),(2,1)))` | `(12−16i)/5` | `(-7+16i)/5` |
| `cp` labeling 3 `(3,((0,1),))` | `(22−16i)/5` | `(-17+16i)/5` |
| `V` `(3,((0,1),(0,2)))` | `6` | `-5` |
| 3-chain `(3,((0,1),(0,2),(1,2)))` | `4` | `-3` |

The relation-key convention is the seed's exact `canon()` representation.
Every proper `r_P` and every displayed `r_C` is nonzero. Hence every
transition through the 3-to-4 step is nonzero. The computed exact stage-4
`cp` plus universal-top cylinder amplitudes are
`(-23−4i)/40, (-23−4i)/40, (-17+16i)/40`; their common squared norm is
`(23²+4²)/1600 = 545/1600 = 109/320`. Their relative phases are
`1,1,(3−4i)/5`.

### Residual parameter family

More generally, for any common `q∈ℂ` satisfying `q≠0` and
`q≠S_C` for each of the seven stage-3 parents, set

```
g_C = 1/q,
t(C,P) = r_P/q       (P⊊C),
t(C,C) = (q−S_C)/q.
```

MSR and BC follow from the reduction, and every transition is nonzero. The
stage-4 norm equations derived below hold: all `|g_C|²=1/|q|²`, while the
three `cp` parents have the same `S_C` and therefore the same
`|t(C,C)|²=|q−S_cp|²/|q|²`. The phase seed's `cp` path ratios are preserved
because all three `cp` full-past transition amplitudes are equal. The
certificate uses `q=1`; it lies outside the seven excluded values and gives
the displayed Gaussian-rational transitions.

## Norm-GC derivation before the witness check

Write the seven naturally labelled 3-element parents in the seed enumerator's
order as `C_0,…,C_6`; define

```
x_i := |g_(C_i)|²,
y_i := |t(C_i,C_i)|²,
M_i := |A(C_i)|².
```

If a 4-element labeled causet is reached from `C_i` with proper precursor
`P`, its cylinder norm is `M_i |r_P|² x_i`. If its final precursor is full,
the norm is `M_i y_i`. Equating these expressions over all naturally
labelled representatives of each unlabelled 4-causet gives 24 rational
linear equations in the 14 real norm variables. Exact row reduction has rank
8 and leaves these constraints:

```
x_0 = x_1 = x_2 = x_3 = x_4 = x_5 = x_6,
y_1 = y_2 = y_4,
```

with `y_0,y_3,y_5,y_6` otherwise free in this linear projection. The actual
complex parameters additionally obey `g_C=1/(S_C+r_C)` and are not claimed
to realize every point of that projected norm solution set. The explicit
common-`g` family above satisfies the constraints exactly. In the canonical
enumeration, indices 1, 2, and 4 are the three natural labelings of `cp`, and
their `S_C` agree, which is why the phase can remain nontrivial.

## Reproducible checks

From the repository root run:

```sh
python3 research/longshots/bc-nonzero/nonzero_continuation.py
```

Only Python's standard library and the read-only seed module's exact
Gaussian-rational finite-poset routines are used. The certificate reports:

- all 49 transition amplitudes from stages 1 through 3 are nonzero;
- MSR holds at every parent through size 3;
- all 109 scalar product-BC equations for parents of sizes 1–3 hold;
- norm-GC holds at stages 2, 3, and 4;
- the exact stage-4 norm system has 24 rows, rank 8, and the constraints
  displayed above;
- the stage-4 `cp` holonomy is `(3−4i)/5`.

Assertions check the exact RREF, all transition nonzeros, MSR, BC, norm-GC,
and the nontrivial holonomy. No floating-point arithmetic is used.

## Source assumptions and scope

- Rideout and Sorkin, [“A Classical Sequential Growth Dynamics for Causal
  Sets”](https://arxiv.org/abs/gr-qc/9904062v2), arXiv:gr-qc/9904062v2,
  Sec. 3, especially Eq. (2) and footnote 8: the classical BC ratio is stated
  for nonzero **transition probabilities**. The present problem instead
  tests nonzero complex **transition amplitudes** with the scalar amplitude
  ratio/product equation inherited from the preceding BCPH construction.
  This extension is stated explicitly; it is not being passed off as the
  paper's classical probability theorem.
- Varadarajan and Rideout, [“A General Solution for Classical Sequential
  Growth Dynamics of Causal Sets”](https://arxiv.org/abs/gr-qc/0504066v3),
  arXiv:gr-qc/0504066v3, Sec. II.3: their zero-probability clauses matter for
  the previous zero-amplitude continuation, but do not enter this
  all-nonzero witness.
- Srivastava and Surya, [“Implementing Bell Causality in Quantum Sequential
  Growth”](https://arxiv.org/abs/2603.25503v1), arXiv:2603.25503v1, Secs. 3.1–3.2
  and Eqs. (31)–(36), (49)–(52): scalar `H≃C` gives a commutative product
  setting, while noncommuting operator QBC requires ordering choices. This
  witness concerns the scalar amplitude rule only; it establishes no result
  for TOBC, NTOBC, CPOBC, or noncommutative transition operators.

The construction is not a temporal-ontology result. Nor is it a generic
statement that arbitrary stage-3 phases continue: the demonstrated claim is
for the single BCPH seed specified above. A bounded source/claim audit finds
the cited classical work classifies probability transitions under full
general covariance, while the recent QBC work studies operator orderings;
neither source is used here as evidence that this particular norm-only-GC
phase continuation was previously classified. No novelty or priority claim
is made.
