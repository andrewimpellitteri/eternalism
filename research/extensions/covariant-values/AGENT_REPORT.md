# Covariant value rules: local renewal upgrades the doubly-principal-only rule

Status: 2026-10-20. Probe `covariant-value-rules`. This proves a boundary
refinement of the conditional covariant theorem and an explicit `p=0`
countermodel. It is not a new headline classification and does not select a
temporal ontology.

## Setting

`D_H` is the covariant event that a post has inclusive past `H` (principal,
`n=|H|`); `N(H)` counts natural labelings; `A_p(H)=p^L(1-p)^{binom(n,2)-R}`;
`ν` is a finite countably additive complex measure on `R_p` with
`ν(P∞)=1`. `H⊕{x}` is the principal order obtained by adjoining a new universal
maximum.

## Theorem (local renewal + weakened rank rule)

Assume `p≠0` and:

**(A)** there are numbers `κ_n` such that for every **doubly-principal** `H` of
size `n`, `ν(D_H)=κ_n N(H)A_p(H)`;

**(B)** local renewal: for every principal `H`,
`ν(D_{H⊕{x}})=p ν(D_H)`.

Then `κ_n` is a constant `κ`, and `ν(D_H)=κ N(H)A_p(H)` for **every** principal
`H`. Consequently, by the conditional all-principal theorem, `p∈(0,1]`.

**Proof.** For principal `H` of size `n`, `J=H⊕{x}` is doubly principal
(unique max; deleting it returns the principal `H`), with `N(J)=N(H)` and
`A_p(J)=p A_p(H)`. By (A),
`ν(D_J)=κ_{n+1}N(H)pA_p(H)`. By (B),
`ν(D_H)=ν(D_J)/p=κ_{n+1}N(H)A_p(H)`. Thus the full formula holds for every
principal `H`, with `κ_{n+1}`. If `H` is doubly principal, (A) also gives
`ν(D_H)=κ_nN(H)A_p(H)`; comparing on a chain (where `N(H)A_p(H)=p^{n-1}≠0`)
gives `κ_n=κ_{n+1}`. Hence `κ_n` is constant, and the all-principal theorem
applies. ∎

**Converse.** For `p∈(0,1]`, classical CTP restricted to `R_p` satisfies (A)
and (B) with `κ=c(1-p)` (and `κ=1` at `p=1`).

## The `p=0` boundary

The division by `p` is essential. At `p=0`, the Dirac history
`(A_2⊕{z_1})⊕(A_2⊕{z_2})⊕…` is a normalized covariant measure with no
doubly-principal post past; the doubly-principal-only rule holds with
`κ_n=0`, and local renewal holds trivially as `0=0·ν`. So (A)+(B) do **not**
exclude `p=0`; the `p=0` exclusion in the all-principal theorem uses the
all-principal factorization, not local renewal.

This is the precise boundary: local renewal upgrades the weakened rule to the
full rule for every `p≠0`, but at `p=0` the Dirac measure escapes both.

## Rule table

| Rule | Verdict |
|---|---|
| Doubly-principal-only, no local renewal | **No classification.** Dirac history with `κ=0` is normalized for every `p`; the weakened rule has no content. |
| Doubly-principal-only + local renewal, `p≠0` | **Forces the all-principal common factor**, hence `p∈(0,1]`. |
| Same, `p=0` | **Countermodel survives.** Dirac history is normalized and satisfies both rules with `κ_n=0`. |
| All-principal common factor + normalization | `0<p≤1` (conditional theorem). |
| Rank-only on all principal `H` | **Open.** Reduces to the convolution equation in `research/extensions/rank-factor/`; no construction or no-go. |
| Shape-dependent factor | **Vacuous.** Any measure can be written as `κ_H N(H)A_p(H)` by division. |
| Local renewal alone (no rank rule) | **Does not force rank-independence.** It only says `ν(D_H)/(N(H)A_p(H))` is constant along top-extension chains; shape-dependent assignments can satisfy it. |
| Asymptotic/decaying rank factors | **Open** (same convolution problem). |

## Relation to the existing source

`research/creative/COVARIANT_RESULT.md` states that local renewal **together
with rank-only on all principal H** forces `κ_{n+1}=κ_n`. The theorem above
weakens the starting point: rank-only is assumed only on doubly-principal `H`,
and local renewal extends it to all principal `H` for `p≠0`. The `p=0` Dirac
exception is explicit. This is a boundary refinement, not a new headline
classification.

## Checks

`check.py` verifies for `p=(1+i)/2` and principal `H` of sizes 1–4:

- `H⊕{x}` is principal and its restriction is `H` (hence doubly principal);
- `A_p(H⊕{x})=p A_p(H)` (max error 0);
- at `p=0`, the Dirac history's post pasts are principal but not doubly
  principal; the weakened rule with `κ_n=0` and local renewal `0=0·ν` hold;
  the Dirac measure is normalized.

Run: `python3 check.py`.

## Verdict

**Boundary theorem + explicit `p=0` countermodel.** This is a real refinement of
the conditional theorem: local renewal is exactly what upgrades the weakened
doubly-principal rule for `p≠0`, and `p=0` is a genuine exception. It should be
a short section in the short note, not a standalone headline. No physical or
ontological claim follows; the rules are measure-theoretic compatibility axioms.

## Files

- `research/extensions/covariant-values/AGENT_REPORT.md` — this report.
- `research/extensions/covariant-values/check.py` — finite checks.

Standard library only; no installs; no board edits.
