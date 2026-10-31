# Dense-stage stress test for (GB1)

Checked 2026-10-27 against Loss's original PMC HTML. This is a conditional countermodel to an entailment from the explicitly listed clauses, not a claim that Loss's intended growing-block interpretation permits retroactive insertion of times.

## Claim under test

Loss says that (D), together with the assumption that each possible stage has multiple possible futures, makes (GB1) and (GB2) valid (§2.3, PMC HTML lines 174–178). His (GB1) is `A ∃x ¬P E x`; on a fixed history, its local content is that at every stage there is a currently existing entity which did not exist at any strictly earlier stage on that history. The stage-relative `P` clause is given at lines 171–173. This check asks whether proper domain inclusion alone supplies such a witness on a dense stage order.

## Dense time-indexed structure

Let the stage indices be `t ∈ (-∞,0)`. Define

```text
D(t) = T(t) = (-∞,t) ∪ {0}
```

and give `T(t)` the usual real-time order. Thus `0` is the unique latest existing time at every stage. For `t<u<0`, `D(t) ⊊ D(u)`: the newly included times are `[t,u)`. Time ordering on all old times is unchanged, and every stage's time set is linearly ordered with latest element `0`.

To meet the paper's explicit multiple-futures assumption as well, represent stages by past-functions `(t,p)`, where `p:(-∞,t)→{0,1}` is eventually zero toward `-∞`. Put `(t,p) R (u,q)` iff `t<u` and `q` extends `p` (that is, `q↾(-∞,t)=p`). Domains and time orders depend only on the first coordinate: `D(t,p)=T(t)`. Each node has multiple R-futures, by choosing different extensions on a nonempty interval after `t`. The R-past of a node is linearly ordered by restriction, and histories are maximal chains. This supplies a branching tree of possible stages while retaining the same dense, time-indexed domains on every branch.

The stated conditions check as follows:

| Stated condition | Check in this structure |
|---|---|
| (D): `mRn ⇒ D(m) ⊊ D(n)` | If `(t,p)R(u,q)`, then `t<u` and `(-∞,t)∪{0} ⊊ (-∞,u)∪{0}`. |
| Multiple possible futures | From any `(t,p)`, choose `u>t` and at least two distinct extensions `q` on `[t,u)`. |
| (T1): time sets persist | `T(t) ⊂ T(u)` for `t<u`. |
| (T2): old time order persists | The usual `<` relation is stage-independent. |
| (T3): unique latest time | `0` is in every `T(t)` and every other member is less than `0`. |
| `T(m) ⊆ D(m)` | Here `T(m)=D(m)`. |

These are the conditions stated in §§2.2–2.3, especially lines 149–168 and 174–178. Loss explicitly leaves the general necessary and sufficient conditions on `R` open (line 151). His footnote 17 (lines 304–305) sets aside stages at which growth stops; this structure has many futures at every node, so that caveat does not exclude it.

## Why (GB1) fails here

Fix any stage `(t,p)` on a history. Every entity `x∈D(t)` has an earlier stage on that same history at which it already exists:

- If `x=0`, choose any `v<t`; its history predecessor contains `0`.
- If `x<t`, choose `v` with `x<v<t`; the restriction of `p` to `(-∞,v)` is an earlier stage and `x∈D(v)`.

So for every currently quantified `x`, `P E x` is true. There is no witness for `∃x ¬P E x` at any stage, and (GB1) is false on every history. The same reason falsifies (GB3), which asks for a time that has never existed before, and (GB6), which asks for the unique latest time to have never existed before. By contrast, (GB2) holds by domain inclusion; (GB4) holds by (T1), and (GB5) holds because the time order is stage-independent. Thus the counterexample targets the fresh-existence conclusions while preserving the persistence/order conclusions.

The mechanism is dense first-existence without a first stage: each negative real `x` is absent at stages `t≤x` and present at all stages `t>x`, so it has no earliest stage of existence. Every pair of later stages adds entities, yet at any given stage every entity already occurs at some earlier stage.

## Repair and interpretation caveat

An exact sufficient condition for (GB1) at each stage `m` is a first-existence witness:

```text
for every m on the history, some x ∈ D(m) is absent from D(n)
for every n R-earlier than m.
```

In the one-sorted case `D=T` used here, requiring latest times to advance strictly across every R-comparable pair also rules out this model: the latest time at `m` is then absent from every earlier domain, and witnesses (GB1). With separate entity and time predicates, strict advancement of the latest *time* alone needs an additional identity/freshness link to establish `¬P E x`; an entity could formally exist before it counts as a time.

The formal countermodel keeps the latest time fixed and inserts newly existing times below it. That respects the displayed (D), (T1)–(T3), and branching conditions, but it is not the ordinary append-at-the-edge picture of a growing block. Loss's prose calls the conditions necessary, says they “plausibly” specify growth, and leaves the general conditions on `R` open (lines 151–168); Fig. 3 depicts the latest time advancing (lines 157–160). Thus the safe result is conditional: **the written clauses alone do not exclude dense retroactive insertion and do not entail (GB1); an intended append-only interpretation may supply the missing latest-time or first-existence premise.** This identifies an underspecified formal assumption, not a paper error or a refutation of the stage-theoretical account.

## Source and scope

Primary source: Roberto Loss, “Open future, supervaluationism and the growing-block theory: a stage-theoretical account,” *Synthese* 199 (2021), 14249–14266, corrected publication 2022, DOI 10.1007/s11229-021-03419-7, [original PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC8581605/). Selected locators: §§2.2–2.3, HTML lines 147–182; footnote 17, lines 304–305. This is a direct check of the displayed clauses, not a complete audit of every semantic or metaphysical commitment in the article.
