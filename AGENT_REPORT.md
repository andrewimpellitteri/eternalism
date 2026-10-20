# lean-certificate — certificate audit for the selected complex-percolation claim

Status: 2026-10-20. Claimed by `opencode-coordinator`. No Lean toolchain is
installed (`lean`/`lake` absent), no mathlib was fetched, and the user asked not
to download large Lean libraries. This task therefore documents the
infeasibility of a faithful Lean encoding and audits the proof, the finite
certificate, the axioms, and the statement's meaning. It does not claim a
machine-checked all-level theorem and does not invent a vacuous encoding.

## Files

- `formal/INFEASIBILITY.md` — why a Lean build is deferred, the staged
  non-vacuous formalization route, and the proof route used.
- `research/proof-audit/CERTIFICATE_AUDIT.md` — step-by-step audit of the
  labelled and conditional theorems, correspondence table, axiom audit and
  meaning audit.
- `formal/check_certificate.sh` — reproducible checks; no Lean or dependency
  installs.

## What is verified

1. **Exact finite certificate.** At `p=(1+i)/2`:
   `V_5 = 3/4 + 3√2/16 ≈ 1.015165042945` and
   `V_6 = 31/32 + 55√2/64 ≈ 2.184089780164`, computed in exact `Q(√2)` by
   `experiments/baseline/reproduce.py` and independently by
   `research/creative/proof-audit/verify_small.py`.
2. **Finite combinatorics.** The two-cap decomposition, covers/incomparable
   counts, additivity of the pre-measure, and the `V_n` sums are checked at the
   implemented levels (the baseline enumerates 1, 2, 7, 40, 357, 4824
   naturally labelled causets for `n=1…6`).
3. **Published baseline.** The Dowker–Zalel finite-level minima
   (`ζ_n^min = ζ̄_n^min = |p|+|1-p|-1` at `n=2,3,4` for `p=(1+i)/2`) are
   reproduced.
4. **Countermodel.** The Dirac history defeats the doubly-principal-only
   factorization for every `p`; the all-principal rule is shown to fail on it.
5. **Unit tests.** Seven baseline tests pass; the project's 88 tests pass.

These are finite instances and a proof audit, not a proof-assistant proof of
the all-level theorem.

## Proof audit summary

The labelled theorem's steps are correct as read: the doubly-principal
decomposition, the cover/incomparable count, the `w(G)≥k` bound, the
random-graph endpoint identity `F_k(s)=∏(1-s^j)`, the positive Euler product,
the divergence for `p∉[0,1]`, and the finite-total-variation contradiction.
One wording gap: "finite-valued" should be stated as a countably additive
complex measure with finite total variation; the latter is standard but should
be explicit.

The conditional covariant theorem's laminar-family argument, `κ=0` and `p=0`
contradictions, shape grouping, and classical existence for `0<p≤1` are
correct as read. Assumption (T) is load-bearing and is not implied by
covariance: the Dirac countermodel satisfies the doubly-principal-only version
with `κ=0` for every `p`.

**Axiom audit (paper level, not a Lean dependency closure).** Classical logic
and standard set theory; countable additivity and finite total variation;
finite additivity and inclusion–exclusion; continuity from below; strict
triangle inequality; convergence and positivity of the Euler product. No
nonstandard axioms, no `sorry`, no assumed target theorem. There is no Lean
build, so no compiled transitive axiom closure exists to audit.

## Statement correspondence and meaning

- The Python code checks finite labelled causets, amplitudes and sums. It does
  **not** implement the sigma-algebra, countable additivity, measure extension,
  or the infinite limit. The correspondence table is in
  `research/proof-audit/CERTIFICATE_AUDIT.md`.
- The verified mathematical object is a scalar complex-measure existence
  classification on a labelled algebra. It is not a physical dynamics, a
  quantum measure, or an observable model.
- The conditional version adds a renewal factorization axiom on post events.
  It still does not select a temporal ontology, passage, determinism, causal
  order, clock time, or a thermodynamic arrow.
- Any ontological inference needs an explicit bridge premise not supplied by
  the theorem.

## What is not certified

- The all-level labelled theorem is not machine-checked in Lean. The
  infeasibility review and staged route are in `formal/INFEASIBILITY.md`.
- The conditional covariant theorem is not machine-checked; it is a paper proof
  with an independent audit and a countermodel for a weakened version.
- External mathematical acceptance and publication priority remain unresolved.
- Vector-valued measures and rank-dependent post factors are open boundaries,
  not verified claims.

## Reproduce

```sh
bash formal/check_certificate.sh
```

The script prints the toolchain status (Lean absent), runs the seven baseline
tests, the exact certificate/reproduction, the independent fresh-audit script,
the Dirac countermodel, the boundary checks, and source hashes. It installs
nothing.

## Limits

- No Lean/mathlib; no compiled proof or transitive axiom closure.
- Finite enumeration corroborates but does not quantify over all levels.
- The primary paper was read as arXiv HTML v2; the published PDF was not
  compared.
- The countermodel and conditional theorem are attributed to the creative pass;
  this task audits them rather than claiming them as new.
