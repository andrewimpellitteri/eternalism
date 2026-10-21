# Covariant value rules: local renewal upgrades the doubly-principal-only rule

Status: 2026-10-20. Probe `covariant-value-rules`. This proves a boundary
refinement of the conditional covariant theorem and an explicit `p=0`
countermodel. It is not a new headline classification and does not select a
temporal ontology.

> **Corrections applied 2026-10-21** (submission for review), following
> `research/adversarial-review/coordinator/BOUNDARIES.md`: (i) assumption (A)
> constrains `κ_n` only for `n≥2`; `κ_1` is unconstrained (no doubly-principal
> singleton), the common factor is `κ_2`, and the literal counterassignment
> `p=1`, chain-Dirac, `κ_1=17` is verified; (ii) shape-dependent-factor
> division is available only for `p∉{0,1}` — at the endpoints vanishing
> amplitudes impose genuine zero-value conditions; (iii) the doubly-principal-
> only Dirac witness is an existential countermodel for every `p`, not evidence
> that every measure satisfies the weakened rule. The corrections are marked in
> place below; historical results are preserved. The finite checks were
> upgraded to exact arithmetic. Nothing here strengthens a claim beyond the
> reviewed material. [marker end]

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

Then `κ_n` is a constant for `n≥2` — say `κ_n = κ` for all `n≥2` — and
`ν(D_H)=κ N(H)A_p(H)` for **every** principal `H` (the common factor is `κ_2`).
Consequently, by the conditional all-principal theorem, `p∈(0,1]`.

> **[Corrected 2026-10-21]** following `research/adversarial-review/coordinator/
> BOUNDARIES.md`: the original statement read "`κ_n` is a constant `κ`" without
> the `n≥2` restriction. Assumption (A) quantifies only over **doubly-principal**
> `H`, and there is **no doubly-principal order of size 1**: deleting the maximum
> of the singleton gives the empty order, which has zero maxima. Hence `κ_1` is
> unconstrained by (A), and the comparison `κ_n=κ_{n+1}` on chains is available
> only for `n≥2` (it needs a doubly-principal `H` of size `n`). The literal
> counterassignment: at `p=1`, the Dirac measure on the infinite chain with
> `κ_1=17` and `κ_n=1` for `n≥2` satisfies (A), (B), and normalization — checked
> exactly in `check.py`. State the conclusion as "constant for `n≥2`"; do not
> treat an extension of the sequence to `κ_1` by convention as a derived
> constraint. The all-principal conclusion is unaffected: the derivation below
> yields `ν(D_H)=κ_{n+1}N(H)A_p(H)` for every principal `H` of size `n`, with
> `κ_{n+1}=κ_2` throughout, and `κ_1` is never used. [marker end]

**Proof.** For principal `H` of size `n`, `J=H⊕{x}` is doubly principal
(unique max; deleting it returns the principal `H`), with `N(J)=N(H)` and
`A_p(J)=p A_p(H)`. By (A),
`ν(D_J)=κ_{n+1}N(H)pA_p(H)`. By (B),
`ν(D_H)=ν(D_J)/p=κ_{n+1}N(H)A_p(H)`. Thus the full formula holds for every
principal `H`, with `κ_{n+1}`. If `H` is doubly principal, (A) also gives
`ν(D_H)=κ_nN(H)A_p(H)`; comparing on a chain (where `N(H)A_p(H)=p^{n-1}≠0`)
gives `κ_n=κ_{n+1}`. Hence `κ_n` is constant, and the all-principal theorem
applies. ∎

> **[Corrected 2026-10-21]** the comparison step needs a **doubly-principal**
> chain `H` of size `n`, which exists only for `n≥2`; hence `κ_n=κ_{n+1}` holds
> for `n≥2` and the common factor is `κ_2`. The statement "`κ_n` is constant"
> above should be read with that restriction (see the corrected theorem
> statement). [marker end]

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

> **[Corrected 2026-10-21]** following `coordinator/BOUNDARIES.md`: this is an
> **existential** statement. The Dirac history shows the doubly-principal-only
> rule (with a suitable `κ_n`, namely `κ_n=0`) does not exclude `p=0`. It does
> **not** show that every measure satisfies that rule, and the rule is not
> "vacuous" in that universal sense: for `p∉{0,1}` a shape-independent `κ_n`
> is a genuine restriction on a given measure. [marker end]

## Rule table

| Rule | Verdict |
|---|---|
| Doubly-principal-only, no local renewal | **Does not exclude `p=0`** — the Dirac history with `κ=0` is normalized for every `p` and satisfies the rule. [Corrected 2026-10-21: this is an existential countermodel, not vacuity of the rule for all measures; for `p∉{0,1}` a shape-independent `κ_n` genuinely restricts a given measure. Marker end.] |
| Doubly-principal-only + local renewal, `p≠0` | **Forces the all-principal common factor for `n≥2` (factor `κ_2`)**, hence `p∈(0,1]`. [Corrected 2026-10-21: `κ_1` is unconstrained; see theorem correction. Marker end.] |
| Same, `p=0` | **Countermodel survives.** Dirac history is normalized and satisfies both rules with `κ_n=0`. |
| All-principal common factor + normalization | `0<p≤1` (conditional theorem). |
| Rank-only on all principal `H` | **Open.** Reduces to the convolution equation in `research/extensions/rank-factor/`; no construction or no-go. |
| Shape-dependent factor | **Vacuous only for `p∉{0,1}`.** [Corrected 2026-10-21: the original entry, "Any measure can be written as `κ_H N(H)A_p(H)` by division," holds exactly when division by `A_p(H)` is available, i.e. `p∉{0,1}` — then all principal amplitudes are nonzero (exact check in `check.py`). At `p=0` or `p=1` some principal amplitudes vanish, arbitrary measures cannot be factored by division, and the zero-amplitude events impose actual zero-value conditions; the shape-factor form is not freely available at the endpoints. Marker end.] |
| Local renewal alone (no rank rule) | **Does not force rank-independence.** It only says `ν(D_H)/(N(H)A_p(H))` is constant along top-extension chains (where the division is defined); shape-dependent assignments can satisfy it. |
| Asymptotic/decaying rank factors | **Open** (same convolution problem). |

## Relation to the existing source

`research/creative/COVARIANT_RESULT.md` states that local renewal **together
with rank-only on all principal H** forces `κ_{n+1}=κ_n`. The theorem above
weakens the starting point: rank-only is assumed only on doubly-principal `H`,
and local renewal extends it to all principal `H` for `p≠0`. The `p=0` Dirac
exception is explicit. This is a boundary refinement, not a new headline
classification.

## Checks

[Updated 2026-10-21: `check.py` now uses exact arithmetic — Gaussian rationals
at `p=(1+i)/2`, integers at `p=0,1` — and asserts the reviewed edge cases.
Run: `python3 check.py`.]

- For `p=(1+i)/2` and principal `H` of sizes 1–4: `H⊕{x}` is principal and its
  restriction is `H` (hence doubly principal together with `H`);
  `A_p(H⊕{x})=p A_p(H)` **exactly** (11 exact identities; previously floating
  point with a tolerance);
- there is no doubly-principal order of size 1 (smallest is size 2): `κ_1` is
  unconstrained by (A);
- the `κ_1=17`, `κ_n=1 (n≥2)` chain-Dirac counterassignment at `p=1` satisfies
  (A) on every doubly-principal `H` of sizes 2–4 and (B) on every principal `H`
  of sizes 1–3, exactly, with normalization by construction;
- division availability: `A_p(H)≠0` for all 51 principal `H` of sizes 1–5 at
  `p=(1+i)/2` (exact); at `p=0`, `A_0(H)=0` for all 50 principal `H` of sizes
  2–5 (the singleton has `A_0=1` but is not doubly principal); at `p=1`,
  `A_1(H)=0` on the 46 non-chain principal `H` and `=1` on the 4 chains — so
  shape-factor division is available only for `p∉{0,1}`;
- at `p=0`, the Dirac history's post pasts are principal but not doubly
  principal; the weakened rule with `κ_n=0` and local renewal `0=0·ν` hold;
  the Dirac measure is normalized (existential witness only).

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
