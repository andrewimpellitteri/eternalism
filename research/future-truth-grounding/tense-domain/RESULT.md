# Tense and existence across growth stages

Checked 2026-10-27. This is a finite semantic reconstruction of one issue in Roberto Loss's stage-theoretical account, not a new theory of temporal ontology.

## Finding

The decisive parameter is the **growth stage** at which an existential quantifier gets its domain. A future-stage operator that shifts evaluation to a later growth stage does not by itself make a quantifier range over that later stage's domain. In a frozen-domain semantics, a newborn is still unavailable to the existential at the shifted evaluation point. Letting the quantifier range over the domain of the stage where it is evaluated recovers the intended claim that a later stage contains something that did not exist at an earlier stage.

This is a semantic compatibility result: a specified stage-based model expresses growth. It does not show that any entities really come into existence, that future propositions are gappy, or that their truth is grounded in currently existing entities.

## Two indices and the toy structure

The toy uses only a growth-stage index `s`. `F_g φ` means that `φ` holds at some later growth stage on the selected stage-history, and `PastExists_g(x,s)` means that `x` existed at an earlier growth stage. There is no within-block time operator in this model: in particular, it does not use `F_t`. This avoids identifying temporal succession inside a block with succession between stages of block growth. In Loss's stage-theoretical semantics, the corresponding formal target is `A∃x ¬P E x` (his (GB1)); there `P` is also evaluated over the stage-history after the reinterpretation.

There are three stages on one history:

| Growth stage | Domain `D(s)` |
|---|---|
| `s0` | `{a}` |
| `s1` | `{a,b}` |
| `s2` | `{a,b,c}` |

The domains grow strictly. `b` is a fresh birth at `s1`; `c` is a fresh birth at `s2`. Every object in a domain persists at later stages. Define `PastExists_g(x,s)` iff `x` belonged to the domain at some stage strictly earlier than `s`. Thus at `s1`, `PastExists_g(a,s1)` is true and `PastExists_g(b,s1)` is false.

The target, evaluated initially at `s0`, is:

```text
F_g (∃x ¬PastExists_g(x))
```

Read this as “at some later growth stage, there is an entity in that stage's domain that was absent at every earlier growth stage.” To expose the contrast, carry an origin-stage parameter `o` while the future operator shifts the evaluation stage `s`:

```text
F_g φ at (s,h;o) iff for some later s' on h, φ holds at (s',h;o).
Shifting:  ∃x φ at (s,h;o) iff some d ∈ D(s) makes φ true at (s,h;o).
Frozen:    ∃x φ at (s,h;o) iff some d ∈ D(o) makes φ true at (s,h;o).
```

For the shifting evaluation set `o=s` at the start; for the frozen evaluation
set `o=s0` and keep it fixed under `F_g`.

With shifting domains, `s1` is a witness for `F_g`: choose `b ∈ D(s1)` and `¬PastExists_g(b,s1)` holds. The formula is true. With the domain frozen to `D(s0)={a}`, evaluation at either later stage can only choose `a`; `a` was already present at `s0`, so the matrix is false. The formula is false. The newborn is not contradicted or shown never to exist; the frozen quantifier simply cannot name it as a witness.

An equivalent relational presentation makes the scope explicit. Let `R` be the later-than relation on stages and `D(s)` the stage domain:

```text
Shifting:  ∃s' [s0 R s' ∧ ∃x∈D(s') ¬PastExists_g(x,s')]
Frozen:    ∃s' [s0 R s' ∧ ∃x∈D(s0) ¬PastExists_g(x,s')]
```

For the displayed model the first is true (witness `s1,b`); the second is false (the only possible witness is `a`). At terminal stage `s2`, `F_g` has no later-stage witness, so the fresh-birth formula is false under both clauses there. This is a finite toy counterexample to any inference that the example validates perpetual growth. It isolates the quantifier parameter at `s0` and does not depend on the truth value of a future-contingent proposition: the example has one history and deterministic births.

## What the source says

Loss (2021; corrected publication 2022), “Open future, supervaluationism and the growing-block theory: a stage-theoretical account,” §§2.2–2.3, first describes the growing-block domains `D(m)` at stages and requires `D(m) ⊂ D(n)` for a later stage (`R`, condition (D)). The stage-history future and past operators are then defined by shifting the stage coordinate; the existential clause ranges over `D(m)` at the stage where it is evaluated. Loss says these choices make (GB1) `A∃x ¬P E x` and (GB2) valid at every possible stage (HTML article lines 149–177; see exact passage locators in `sources.jsonl`).

The “quantifier troubles” section (§3) reconstructs Briggs and Forbes's `Σ_T` as ranging over entities present at some time on the fixed actualized timeline `T`. Loss's diagnosis is that this quantifier remains rigidly tied to `T` while their temporal operators shift only the ersatz-time coordinate. Consequently the claims intended to express new existence, including `Σ_T x ¬P Σ_T y(x=y)` and its metric-future counterpart, come out super-false (Loss, HTML lines 212–222). Loss's repair shifts the **timeline/stage** along a history under `F`/`P`, and uses a quantifier `𝓔` whose domain is sensitive to the timeline at which it is evaluated. He reports that the repaired version blocks future-only entities from counting as actual-timeline existents while validating the corresponding growth claims (lines 223–241).

The toy above is a finite simplification of that parameter shift. It makes the culprit transparent but does not reproduce the entire Briggs–Forbes formalism, its alternative quantifiers, supertruth clauses, or all of Loss's proof. In the relevant repair Loss's `P` and `F` operate over possible growth stages. The toy contains no within-block time coordinate or `F_t` operator, and supplies neither a relativistic nor a full two-dimensional tense semantics.

## Limits and open semantic choices

1. The result follows from the stipulated domains and clauses. Stage semantics is not an argument for growing-block ontology; Loss explicitly presents a non-reductive semantic framework and does not defend supervaluationism or gappy future truth in this paper (Introduction; conclusion).
2. The model has a single linear history. Supertruth across alternative histories, unsettled future contingents, and empty-history issues are not tested here.
3. “Fresh birth” is formalized as membership in a later domain without membership in any earlier stage domain. Whether that captures metaphysical coming-into-existence is a bridge premise, not a theorem of the model.
4. Names and assignments are treated as rigidly referring to elements of the toy's union domain. The example does not solve free logic, failed reference, or retrospective reports.
5. Loss says in a footnote (§2.3 n.17) that he sets aside growth that stops. The toy is explicitly finite and has a terminal stage, so it fails any perpetual-growth condition there. Its positive result concerns only evaluation at `s0` and does not validate perpetual growth.

## Source depth

Loss was read in the original PMC full-text HTML, including the abstract, Introduction, stage-setting, growth clauses, the full quantifier-troubles section, and conclusion. This is selected full-text reading, not a complete audit of every argument or of the cited Briggs–Forbes chapter. No PDF was needed because the primary article's complete HTML was available. A small self-contained standard-library evaluator is in `check_tense_domain.py`; its printed source labels identify Loss's diagnosis and repair as claims reported by Loss, not an independent full audit of Briggs and Forbes.
