# Stage-4 scalar Bell-causality check for holonomy

**Result.** Nontrivial scalar holonomy is not forced to vanish by Markov sum,
norm-only covariance, and the zero-aware product form of scalar Bell causality
through stage 4. An exact countermodel is obtained by taking the already
constructed stage-3 Bell-causal norm-GC family from
`birth-order-interference/REPORT.md` and, from every 3-element parent onward,
allowing only the full-past child, with amplitude 1. The phase around the
3-element `cp` (2-chain plus isolated point) class remains nontrivial at stage
4. The same continuation verifies through stage 5 as a bounded consistency
check; no general stage-5 classification is claimed.

This is a scope result for a stated scalar, product-BC convention. It is not a
classification of all stage-4 solutions, and it is not evidence about
objective temporal passage. Because this continuation uses zero amplitudes,
the result is conditional on the zero-aware product equations specified below;
a ratio-only definition that leaves zero cases undefined cannot answer this
question for this model.

## Model and exact constraints

Use naturally labelled finite posets. A parent `C` has one possible
transition for each down-set/precursor `P ⊆ C`; write its complex transition
amplitude as `t(C,P)`. For a path `γ` from the one-element root to `C`, write
`A(C)=∏_(edges e in γ) t(e)`. The stage-n vector measure on a cylinder is
this scalar, and `D(γ,γ') = conjugate(A(γ)) A(γ')`.

The finite constraint system checked is:

1. **Markov sum rule (MSR):** for each parent `C`,
   `Σ_(P down-set of C) t(C,P) = 1` in `ℂ`.
2. **Norm-only general covariance (norm-GC):** for each stage `n` and every
   pair of naturally labelled causets `C,C'` isomorphic as unlabelled posets,
   `|A(C)|² = |A(C')|²`.
3. **Scalar product Bell causality (BC):** for every parent `C` and every pair
   of its precursors `P,Q`, let `B=P∪Q` with its induced order, and let
   `P̄,Q̄` be the corresponding subsets in the increasing-label
   identification of `B`. Require
   `t(C,P) t(B,Q̄) = t(C,Q) t(B,P̄)`.
   This is the cross-multiplied spectator-independence equation. It is checked
   as written, including when one or more factors vanish. No ratio is ever
   formed. For nonzero factors it is equivalent to equality of the classical
   relative transition ratios (or, here, their direct scalar-amplitude
   analogue). The complex-amplitude equation is a chosen scalar extension; it
   is not one of the operator-ordering prescriptions for general
   noncommutative QSG.

The checked through-stage-4 system includes BC for parents of sizes 1, 2, and
3, MSR at all those parents, and norm-GC at stages 2, 3, and 4. For the
additional stage-5 check, include size-4 parents and stage-5 norm-GC.

### Exact amplitude assignment

At the one-element parent, set

| Precursor | Child type | Amplitude |
|---|---|---:|
| empty | 2-antichain | `1/2` |
| full singleton | 2-chain | `1/2` |

For the 2-chain parent, set amplitudes for precursor sizes 0, 1, 2 to
`1/4, 1/4, 1/2`, respectively. For the 2-antichain, set amplitudes for the
empty precursor, each of its two singleton precursors, and its full precursor
to
`(3+4i)/20, (3+4i)/20, (3+4i)/20, (11-12i)/20`, respectively.

For every parent `C` of size `n ≥ 3`, set

```
t(C,P) = 1   if P=C,
          0   otherwise.
```

The specification above fixes every transition through stage 5 and defines a
continuation for all later finite stages. The finite checker audits stages
through 5 only.

## Why the constraints hold

For size-1 and size-2 parents, MSR is immediate by the displayed sums. For
every parent of size at least 3, there is one full precursor and every other
precursor has amplitude zero, so MSR is `1+0+…+0=1`.

The nonzero stage-3 path amplitudes for the `cp` class are exactly
`(3+4i)/40, (3+4i)/40, 1/8`. Each has squared norm `1/64`. Their relative
phases, relative to the first path in the canonical enumeration, are
`1, 1, (3-4i)/5`; the last is nontrivial. Their vector sum is
`11/40 + i/5`. Adjoining a universal top gives a four-element class with the
same three labelled amplitudes, since each final full-past transition has
amplitude one. Thus its holonomy is also nontrivial at stage 4.

For any parent of size at least 3, consider a BC pair `P,Q`. If both are
proper precursors, both parent-level amplitudes vanish. If one is full, then
`P∪Q=C`, so the reduced parent `B` is the same parent `C`; the two sides of
the product equation are identical, including when the other transition is
zero. This proves every BC equation involving a size-3-or-larger parent.
The size-1 and size-2 equations were evaluated exactly, not inferred from
ratios. The code checks all generated equations across every parent and
precursor pair.

At stage 4 or 5, a nonzero path must end by adjoining a universal top. Such a
top is unique. Removing it leaves the prior causet, and all natural labelings
of that prior causet have equal amplitude norms by the preceding-stage
norm-GC check. A path not ending in a universal top has amplitude zero in
every natural labeling of its isomorphism class. This proves norm-GC for the
deterministic continuation; the checker independently compares every pair of
generated isomorphic labelings through stage 5.

## Exact computation

Run from the repository root:

```sh
python3 research/longshots/bc-holonomy/stage4_countermodel.py
```

It imports the existing seed read-only and uses only its Gaussian-rational
arithmetic and finite causal-set enumerator. No external packages are used.
Exact output is in `check-output.txt`:

- generated labelled causets at stages 1–5: `1, 2, 7, 40, 357`;
- MSR failures: none;
- norm-GC failures at stages 2–5: none;
- BC product equations checked cumulatively for parents through sizes 1–4:
  `1, 10, 109, 1619`; failures: none;
- `cp` amplitude norms-squared: `1/64` for all three labelings;
- nontrivial relative phase: `(3-4i)/5`;
- stage-4 `cp` plus universal top: multiplicity 3, same amplitudes and phase.

The assertions in the script terminate nonzero if any listed exact claim fails.

## Primary-source audit and interpretation

- **Rideout–Sorkin, [“A Classical Sequential Growth Dynamics for Causal Sets”](https://arxiv.org/abs/gr-qc/9904062v2),
  arXiv:gr-qc/9904062v2 (10 Aug 1999; published Phys. Rev. D 61, 024002
  (2000)). Read depth: full-text, Sections 3 and 4.1–4.4, especially the BC
  definition and spectator construction in Sec. 3 and the sum rule in Sec. 3.**
  They define BC by equality of ratios for nonzero transition probabilities;
  the reduced parent is the union of the two precursors. Their discussion
  explicitly warns that zero-transition interpretations require separate
  treatment. This is the classical source for the union-of-precursors
  equation's geometry, not by itself a prescription for complex amplitudes.
- **Varadarajan–Rideout, [“A General Solution for Classical Sequential Growth
  Dynamics of Causal Sets”](https://arxiv.org/abs/gr-qc/0504066v3), arXiv:gr-qc/0504066v3 (8 Feb 2006; Phys. Rev. D
  73, 104021 (2006)). Read depth: full-text, Sections II–III.** They give
  separate clauses for vanishing *probabilities* (Sec. II.3, clauses
  (i)–(iv)); these are not simply a universal ratio. Our model has an exact
  zero-aware product identity, but we do not identify the paper's classical
  zero-probability clauses with a uniquely established quantum-amplitude
  convention.
- **Srivastava–Surya, [“Implementing Bell causality in Quantum Sequential
  Growth”](https://arxiv.org/abs/2603.25503v1), arXiv:2603.25503v1 (26 Mar 2026). Read depth: full-text, Secs. 2.2,
  2.4, 3.1–3.2, especially Eqs. (31)–(36), (49)–(52).** Their simple scalar
  `H ≃ C` model has a product-form decoherence functional and scalar
  transitions, while their QBC discussion makes ordering choices for
  noncommuting operators and identifies the classical ratio/product forms.
  It does not classify the present norm-only-GC phase freedom or prescribe
  our complex zero-amplitude product extension. We therefore state that
  convention explicitly rather than attribute it to them.
- **Dowker–Johnston–Surya, [“On extending the Quantum Measure”](https://arxiv.org/abs/1007.2725v1),
  arXiv:1007.2725v1 (16 Jul 2010). Read depth: full-text, Sec. 4.** This
  treats complex percolation and extension of its quantum vector measure.
  It motivates keeping finite-stage covariance separate from extension to
  the full sigma algebra. This finite countermodel proves neither such
  extension nor the measurability of arbitrary covariant events.
- **Surya–Zalel, [“A Criterion for Covariance in Complex Sequential Growth
  Models”](https://arxiv.org/abs/2003.11311v1), arXiv:2003.11311v1 (25 Mar 2020; CQG 37, 195030 (2020)). Read
  depth: full-text, Secs. 2–3.** It studies bounded variation and extension
  in complex sequential growth. The present construction is only a finite
  consistency witness plus a simple frozen continuation; no extension
  criterion is derived here.

The earlier birth-order report already supplies the prior stage-3 family and
its source comparison. This lane's bounded defeat check was to compare the
new implication against those primary sources and the recent QBC paper. Those
sources study classical full general covariance, complex-measure extension,
or operator QBC; none in the passages audited states that stage-4 scalar
product BC plus norm-GC eliminates the exhibited phase. This is not a
systematic priority search, and no novelty claim is made. The stage-4 result
is a short exact continuation of the earlier finite model, not a new
classification theorem.

## Limits and next question

The witness uses exact zero transitions at stages 4 onward. Its validity is
robust under the explicit bilinear product equations, and no division by zero
occurs. If the intended admissibility rule instead requires every transition
amplitude to be nonzero and defines BC only by ratios, this witness is outside
that restricted domain; that is a different constraint system. The old
stage-3 family has nonzero amplitudes through stage 3, and its relative
holonomy itself is not produced by the deterministic continuation.

No full solution variety for the unrestricted complex stage-4 polynomial
system is classified. We do not infer that all holonomy survives for
nonzero-amplitude stage-4 dynamics, or that any scalar result applies to
noncommutative QSG. Stage 5 was checked only for this same frozen family.
There is no transition from this mathematical result to eternalism,
presentism, or objective becoming without additional physical and
philosophical premises.
