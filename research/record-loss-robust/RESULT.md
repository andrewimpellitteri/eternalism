# Partial record access: a coverage boundary for block-correlated leakage

Sole-worker derivation, 2026-10-21. Extension of
`research/event-filter-resources/RECORD_LOSS.md`; no novelty claim. This is a
finite combinatorial boundary for a stated Gram-record model, not a general
erasure theorem and not a physical observer model.

## Model

There are `m` independent blocks, each containing `B` record positions, so
`n=mB` positions. Within a block the environment record is perfectly
correlated: the two target histories differ in the block's record, and
observing **any one** position in the block reveals that record. The Gram
overlap between the two block records is a fixed real `gamma` in `[0,1]`.

An observer accesses a set `A` of record positions, `|A|=k=f n`. A block with
`A ∩ block = ∅` remains hidden and contributes coherence factor `gamma`; an
accessed block contributes `1`. The two-history visibility is therefore

```
V(A) = gamma^{H(A)},   H(A) = # { blocks b : A ∩ b = empty }.
```

This is the diagonal two-history case of the Schur record channel. It is a
positive-filter/visibility statement, not a signed estimator.

## Targeted access: threshold at f = 1/B

If the observer may choose which positions to access and knows the block
partition, each accessed position can cover at most one block. Hence

```
H(A) >= max(0, m-k),
```

with equality attained by placing one access in each of `k` distinct blocks
when `k <= m`. Thus

```
min_A V(A) = gamma^{max(0, m - f m B)}.
```

For `f < 1/B` the exponent grows linearly in `m`; at `f >= 1/B` the visibility
is exactly `1`. The critical fraction is

```
f_c = 1/B.
```

This is a sharp access-model threshold, not a thermodynamic phase transition:
it is exact for every finite `m`.

## Random access: threshold only at full access

If each position is accessed independently with probability `f`, blocks are
independent and

```
P(block hidden) = (1-f)^B,
E[V] = [1 - (1-f)^B (1-gamma)]^m.
```

For fixed `B` and fixed `f<1`, `(1-f)^B>0`, so the visibility decays
exponentially in `m`; only `f=1` gives visibility one. There is no interior
threshold in this access model. If `B` grows with `m`, the boundary is set by
`m(1-f)^B`, so the answer depends on the block-size scaling.

## Comparison with independent per-bit leakage

For independent per-bit records (no block correlation), the same target pair
has visibility

```
V_ind = gamma^{n(1-f)} = gamma^{mB(1-f)}
```

under random access. Block correlation changes the exponent to
`m(1-f)^B`, which is much smaller when `f` is close to one and `B` is
moderate, so correlated records are easier to erase than independent bits.
Targeted access changes the threshold from `f=1` to `f=1/B`. Thus a resource
claim stated only in terms of the accessed fraction is not well posed without
the access model and the correlation structure.

## What this does and does not establish

- It gives an exact boundary for a finite block-correlated Gram model:
  targeted access needs only `1/B` of the positions; random access needs all
  of them; independent-bit leakage has the intermediate exponent above.
- It is not a general phase-transition theorem, not a statement about
  collective measurements, entangled inputs, environment-assisted correction,
  bias, or a physically realized observer.
- It assumes the observer knows the block partition and can target positions.
  If access is constrained (e.g., only contiguous records or only a fixed
  hardware port), the threshold changes; the coverage argument is the
  quantitative content.
- No causal-set growth dynamics is implemented here. The model is a finite
  record register; applying it to a cosmological observer requires a separate
  access model.

## Check

`check.py` enumerates all access sets for small `(m,B,k)` and verifies the
targeted minimum, and computes the random-access expectation exactly for
rational `f,gamma`. It also compares the block-correlated and independent-bit
exponents at a numerical example.

## Prior-work boundary

The all-or-nothing Schur-channel obstruction and the locally unbiased
estimator bound are in `RECORD_LOSS.md` and its independent review. The
inherited prior-work comparison there names Buscemi–Chiribella–D'Ariano,
arXiv:quant-ph/0611070v1 (environment-assisted reversal; environment access is
explicit), Buscemi quant-ph/0611111v2 (abstract only; erasure efficiency versus
corrected channel fidelity), and Frauca–Sorkin 1610.02087v1 Sec. 5.2 (coherent
history-record projector). I did not add new full-text reads in this task. The
coverage observation is elementary combinatorics; no new erasure theorem is
claimed.
