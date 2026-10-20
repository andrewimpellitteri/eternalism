# Novelty sprint — one real result, not more infrastructure

Status: 2026-10-20. This replaces the open-ended literature pipeline as the main
line after the first selection gate. The goal is **one genuinely new,
defensible mathematical result** (plus its bounded philosophical audit), or an
explicit pivot/stop, within roughly six weeks. No result is called new until
the verdict gate below says so.

## Current asset

- **Selected theorem:** the labelled doubly-principal classification for complex
  transitive percolation (`research/creative/RESULT.md`). The direct predecessor
  (Dowker–Zalel 2212.01149v2, Sec. V) explicitly leaves the valency-one /
  doubly-principal extension question inconclusive; an independent proof audit
  found no falsifier; the finite certificate reproduces exactly.
- **Conditional extension:** a covariant post-factor classification
  (`COVARIANT_RESULT.md`) under an all-principal common factor and cyclic
  normalization; the doubly-principal-only weakening has a Dirac countermodel.
- **Open boundaries:** rank-only post factors (necessary attenuation bound only),
  vector-valued measures (total-variation step fails), shape-dependent factors
  (vacuous), covariant measures without a value rule (many).

The strongest defeater is priority: the selected estimate may be a short
corollary of Dowker–Zalel's own criterion. That must be settled before polishing
a paper.

## What counts as “new”

A **theorem or explicit countermodel** whose statement and assumptions are not
already in the read literature, with:

1. exact assumptions and scope;
2. three closest predecessors compared at assumption/result level;
3. a named strongest defeater and a falsifier;
4. a reproducible derivation or witness;
5. a clear separation of mathematical, formalization, physical and
   philosophical novelty.

**Not enough:** a survey, taxonomy, framework, corpus, application of a known
criterion, formalization of a known theorem, or an ontology essay without a new
mathematical result.

## Bets, in order

### Bet 1 — Rank-only post factor (highest upside)

For `ν(D_H)=κ_n N(H)A_p(H)` (shape-blind, rank-dependent), the same-rank
variation gives `|κ_n|V_n ≤ ‖ν‖`, so `κ_n` must decay at least like
`(|p|+|1-p|)^{-n}`. Is that necessary condition sufficient? The laminar
conservation identity `ν(D_H)=Σ_{J⊃H}ν(D_J)` for infinite-post histories may
force a recursion on `κ_n`. Resolve it: construct a normalized measure with
decaying `κ_n`, or prove no such measure exists (a stronger no-go than the
common-factor theorem). This is the crispest new theorem candidate.

### Bet 2 — Vector-valued measure boundary

A countably additive Banach-valued measure need not have finite total
variation, so the scalar divergence argument does not transfer. Construct a
Hilbert-valued measure on the doubly-principal algebra for `p∉[0,1]`, or prove a
no-go under bounded variation/semivariation. Either outcome is a new scope
boundary for the selected result.

### Bet 3 — RC-1 finite three-picture clock (fallback/application)

A `Z_3` clock + qubit with a non-ideal covariant POVM and
`[H_int,H_C]≠0`; compute the Dirac, Page–Wootters and relational-Heisenberg
reductions and the four memory criteria. The literature read so far excludes
this case by assumption. At best a worked application, but a concrete and
publishable one; use it if Bets 1–2 fail.

### Bet 4 — Covariant value rules (support)

Classify which weaker post-value rules still force `0<p≤1`: doubly-principal-only
(fails), local renewal (forces common factor), rank-only (open), shape-dependent
(vacuous). This supports Bet 1 and prevents overclaiming.

## Gates and timeboxes

1. **Verdict gate (`novelty-verdict-selected`, week 1).** Independent priority
   audit of the selected theorem and the conditional extension. Output:
   `PURSUE`, `PIVOT` or `STOP`, with the strongest defeater and a one-page
   claim contract. If `STOP`, pivot to Bet 2/3.
2. **Probe gates (weeks 2–4).** Each probe has a one-page contract and a
   two-week timebox. Kill if it has not produced a precise theorem,
   countermodel, or explicit obstruction. Preserve the negative result.
3. **Adversarial gate (week 5).** Independent review of the surviving claim:
   source correspondence, alternative encodings, counterexamples, novelty.
4. **Paper gate (week 6).** Write only if the claim survives; theorem first,
   proof, finite checks, prior art, limitations. No ontology inflation.

## Operating rules

- At most three active research agents; two model families for adversarial work.
- No more literature-only lanes; every lane must end in a claim, a countermodel,
  or a kill.
- Formal methods are light: exact finite checks and a no-mathlib Lean kernel
  first; a mathlib project only for a surviving theorem.
- Preserve negative results and search bounds; no agent votes as truth.
- The human/coordinator owns the question and the selection gate.
- Every claim carries its bridge premises; a measure-existence theorem does not
  select a temporal ontology.

## Deliverables

- `research/novelty-verdict/` — verdict and claim contract.
- `research/extensions/rank-factor/`, `research/extensions/vector-measure/`,
  `research/extensions/covariant-values/` — probe reports and checks.
- `experiments/clock-three-picture/` — fallback model.
- `research/adversarial-review/` — gate report.
- `research/paper-novel/` — paper only if the claim survives.

## Verdict update (2026-10-20)

`novelty-verdict-selected` returned **PURSUE — narrow** for the labelled
doubly-principal classification. It closes an explicitly stated open case
(Zalel 2021 thesis Ch. 6; Dowker–Zalel 2023 Sec. V), but the two-cap estimate is
elementary and the general measure-extension criterion is not new. Treat the
labelled result as a short-note floor; the rank-factor and vector-measure probes
remain the higher-upside bets. The full report is
`research/novelty-verdict/AGENT_REPORT.md`.
