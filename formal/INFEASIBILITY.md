# Lean certificate: light kernel, infeasibility review, and proof route

Status: 2026-10-20. A **light Lean 4.35.0 core toolchain** is installed with
`elan`; no mathlib was fetched, and the user explicitly asked not to download
large Lean libraries. A self-contained no-mathlib finite kernel is built in
`formal/lean/Certificate.lean` (see `formal/lean/README.md`). A faithful
all-level encoding is still deferred: this note records why, what a non-vacuous
encoding would require, and the proof route actually used.

## Light kernel now built

`formal/lean/Certificate.lean` checks, by finite evaluation (`decide`), the
finite combinatorial kernel of the selected proof:

- naturally labelled causet counts (`1, 2, 7, 40`);
- the two-cap decomposition `G ↦ G ⊕ {u} ⊕ {v}` for sizes 3–5;
- the cover identity `L(cap G)=L(G)+M(G)+1` and unchanged incomparable pairs;
- the amplitude factorization at the concrete integer instance `p=2, q=3`,
  `k=2`.

Toolchain: Lean 4.35.0, commit `eb6cafb…`, core only, no imports, no `sorry`,
no `axiom`; `#print axioms` reports no axioms for the named theorems. Build:
`lean formal/lean/Certificate.lean`. This is a finite kernel, not the
analytic all-level theorem and not the conditional covariant theorem.

## Why the full theorem is not formalized now

The selected statement is the labelled doubly-principal complex-percolation
classification (`research/creative/RESULT.md`), with the conditional covariant
post-factor extension (`COVARIANT_RESULT.md`). A faithful Lean statement needs
all of the following:

1. **Causal-set layer:** naturally labelled finite partial orders, covers and
   strict relations, principal and doubly-principal orders, cylinder sets,
   the labelled poscau tree, and the sigma-algebra they generate.
2. **Measure layer:** a finite complex measure on that sigma-algebra, finite
   total variation, finite additivity on disjoint cylinders, and the extension
   criterion. Mathlib has general measure theory, but not this causal-set
   instance.
3. **Analytic layer:** the two-cap decomposition, the real-percolation
   probability identity, the Euler product `∏(1-s^j)>0`, the divergence of
   `|p|(|p|+|1-p|)^{n-2}c_s`, and the contradiction with finite total
   variation.
4. **Conditional layer:** covariant post events, the laminar family, continuity
   from below, finite inclusion–exclusion, and the added common-factor axiom.

This is a multi-week formalization, not a session task. Mathlib is large; the
user's instruction rules out pulling it for this pass. Encoding the theorem as
an axiom, or proving a vacuous finite identity and calling it the theorem, is
explicitly rejected by the task.

## What a non-vacuous Lean target would look like

A realistic staged project, smallest first:

1. **Finite kernel (Lean core or a small mathlib subset).**
   For a naturally labelled finite order `G` on `Fin k`, define
   `cap G : Fin (k+2) → ...` by adjoining two universal maxima. Prove:
   - `cap G` is doubly principal;
   - every doubly-principal order on `Fin (k+2)` is `cap G` for a unique `G`;
   - covers add `M(G)+1`, incomparable pairs are unchanged.
   This is pure finite combinatorics and does not need measure theory.
2. **Amplitude identity.**
   With `A_p(C)=p^L(1-p)^{binom(n,2)-R}`, prove
   `V_{k+2} = |p| Σ_G |p|^{L(G)+M(G)} |1-p|^{h(G)}` at the level of finite
   sums. This needs real/complex powers only for integer exponents, so a
   rational/real formalization is enough.
3. **Probability identity.**
   Define the independent-edge random graph order and prove the endpoint
   probability identity `Σ_G r^{L(G)+M(G)} s^{h(G)} = ∏_{j=1}^k (1-s^j)`.
4. **Analytic bound and measure contradiction.**
   Prove the Euler product is positive for `0<s<1`, the lower bound diverges,
   and a finite complex measure cannot have arbitrarily large finite disjoint
   sums. This is where mathlib measure theory is needed.
5. **Conditional covariant layer.**
   Only after 1–4; this is a separate project.

Steps 1–3 are the useful formalization contribution; step 4 is the analytic
theorem; step 5 is conditional. A future Lean task should pin a mathlib commit
and start at step 1, not at the theorem statement.

## Proof route used in this pass

1. **Paper-level proof audit** (`research/proof-audit/CERTIFICATE_AUDIT.md`):
   every step of `RESULT.md` and `COVARIANT_RESULT.md`, the assumptions used,
   the finite-to-infinite quantifier, and the correspondence to the primary
   source.
2. **Independent exact finite certificate:** `V_5 = 3/4 + 3√2/16` and
   `V_6 = 31/32 + 55√2/64` at `p=(1+i)/2`, computed in exact `Q(√2)` by
   `experiments/baseline/reproduce.py` and checked again by
   `research/creative/proof-audit/verify_small.py`.
3. **Separate proof audit** already in the repository
   (`research/creative/proof-audit/AUDIT.md`) reconstructed the all-level proof
   and challenged the covariant corollary.
4. **Reproducible commands** in `formal/check_certificate.sh`. This is a finite
   instance check plus a proof audit, not a machine-checked all-level theorem.

## What this does and does not certify

- It certifies the finite certificate and the combinatorial bookkeeping at the
  stated levels (including the light Lean kernel), and it audits the paper
  proof's assumptions and scope.
- It does **not** certify the all-level theorem or the conditional covariant
  theorem in a proof assistant. No Lean build of those statements exists, and
  no opaque assumed target is used.
- The physical/ontological meaning is narrower than the mathematics: the
  theorem is a measure-existence classification, not a physical dynamics or an
  ontology result.
