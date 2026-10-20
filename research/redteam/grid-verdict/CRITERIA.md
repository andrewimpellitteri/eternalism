# Grid advance / kill / hold criteria

2026-10-20. Inputs: `grid/CONTRACT.md`, `grid/axes.json`, `scripts/grid.py` at
9d821f3, `research/grid-review/` and `research/grid-test-report/`. These
criteria say what evidence a verdict needs. The runner checks record shape and
provenance only (`research/grid-test-report/AGENT_REPORT.md`); everything
below beyond shape needs a reviewer.

## Claim typing (applies before any verdict)

Every claim is typed before it is judged, because the evidence needed differs.

| Type | Must state | Evidence that can establish it | Evidence that cannot |
|---|---|---|---|
| Existential / instance | the model and parameters | one checked instance | — |
| Universal over a family | the family, quantifiers, hypotheses | a proof (by hand or Lean), or a cited theorem read at full text | any number of finite instances (control 04) |
| Equivalence | which kind: observational (passive record distributions), interventional (named intervention class), representational (a structure-preserving map), ontological | for each kind, a map preserving that kind's objects; interventional needs the intervention class fixed in advance | equality of a weaker kind (control 03); a representation change alone |
| Entailment (philosophical) | premises listed, conclusion | a derivation, plus a check that no countermodel satisfies the stated premises | agreement among agents or a gold label (control 07) |
| Bridge conditional "if criterion C, then ontology claim O" | C as an explicit premise | validity of the conditional; separately, an argument for C | the physics alone |

A claim that cannot be typed (e.g. "determinism" without saying which of
dynamical uniqueness, settled truth, existing future or predictability) is not
precise and cannot advance (control 08; review flags B03, B05, B10, B11).

## Stage S1 / T1 (proposer)

**kill** — exactly one reason, with the evidence named:

| Reason | Required evidence in the record |
|---|---|
| `known` | predecessor `ref` with locator where the claim is stated; read depth recorded. An abstract-depth `known` kill counts as coverage at abstract depth only. |
| `trivial-by-definition` | the definition, and the short derivation from it (control 05, definition-relative half). |
| `ontology-leap` | the bridge premise is undeclared, circular, or identifies the target by stipulation (control 05, metaphysical half). **Not** merely that the ontological relevance runs through an explicit, argued bridge (control 06). |
| `incoherent` | the term or quantifier that has no consistent reading. |
| `no-checkable-instance` | why no finite or explicit model exists, not just that none was built. |
| `out-of-scope` | which axis assumption the cell violates. |
| *refuted* (missing from CONTRACT.md) | the counterexample in `smallest_instance`, checked. See gap G1. |

**hold** — the claim is typed and precise, and at least one of: a critical
predecessor is unread or blocked; the smallest instance is unbuilt; fewer than
five defeat queries were run; the claim type needs a proof that is not yet
written. The record lists exactly what is missing. A failed search or provider
error is a hold, never a kill or a gap claim.

**advance** — all of:
1. typed claim with domain, quantifiers and hypotheses;
2. `smallest_instance` checked, and for a universal claim a proof or a cited
   full-text theorem, not instances;
3. three predecessors, the nearest read at full text, each with `differs`;
4. a one-sentence delta over the nearest predecessor and why it is not a
   direct corollary of it;
5. five logged defeat queries with results;
6. every bridge premise listed and marked *argued* or *assumed*;
7. a falsifier that names a computation, paper or model.

Advancing requests an adversary. It is not a novelty or truth finding.

## Stage A (adversary)

The adversary sees the claim only, searches independently first, then sees the
proposer's evidence for a correspondence check (`research/grid-review/HANDOFF.md`, item 8).

- **kill**: any S1/T1 kill reason with the same evidence, found by the adversary.
- **survive**: the adversary ran at least five of its own queries, attempted a
  counterexample at the smallest instance, checked definitional triviality and
  checked each bridge premise, and none succeeded. The claim is copied verbatim
  (enforced by the runner since 9d821f3).
- **hold**: a critical source could not be read. A hold is not a survive.

## Stage S2 (expansion, terminal)

The verdict is the effect on one ontology package: *excludes under named
premises*, *neutral*, *supports only through named bridge*, or *forces a
revision*. CONTRACT.md's `kill/hold/advance` does not express this (gap G3).
No S2 record feeds back into any stage.

## Dry run against the eight controls

"Criteria" = the rules above. "Runner" = `scripts/grid.py` at 9d821f3.

| Control | Expected | Under these criteria | Under runner | Result |
|---|---|---|---|---|
| 01 schema | validation error; no promotion | not an advance: missing move, falsifier, predecessor content | rejected (`test_minimal_malformed_advance_rejected`) | pass |
| 02 orphan survivor | provenance hold; no expansion | not a survive: no eligible parent | rejected (`test_orphan_survivor_not_expanded`) | pass |
| 03 observation ⇒ intervention | reject universal claim by counterexample; not an ontology dispute | equivalence claim must name its kind; checked counterexample refutes it | cannot encode: no *refuted* kill reason | pass (criteria); gap G1 |
| 04 finite ⇒ universal | do not advance; narrow or prove | universal claim needs a proof; instances only support the existential | shape-valid record would pass | pass (criteria); reviewer-only |
| 05 circular definition | reject metaphysical inference; definitional conclusion trivial | `trivial-by-definition` for the definitional half, `ontology-leap` for the metaphysical half | either reason is in the enum | pass |
| 06 explicit bridge | do not kill solely because a bridge is explicit | not `ontology-leap`; judge validity, motivation and priority (likely `known` via the Putnam/Stein literature, with locator) | runner accepts any kill reason the worker picks | pass (criteria); **fails under CONTRACT.md's literal `ontology-leap` text** — gap G2 |
| 07 truthmaker entailment | reject entailment; require an extra premise | entailment must survive a countermodel check; the one-record countermodel defeats it | cannot encode: no *refuted* reason | pass (criteria); gap G1 |
| 08 completed paths ⇒ determinism | reject under dynamical determinism | requires the determinism sense; with dynamical uniqueness, the two-path witness refutes it | cannot encode | pass (criteria); gap G1 |

All eight land on their expected disposition under these criteria. Three
cannot be recorded faithfully in the current contract, and control 06 is a
false kill under the contract's literal wording.

## Design gaps (for the coordinator to amend `grid/CONTRACT.md`)

- **G1** Add a `refuted` kill reason requiring a checked counterexample.
  Without it, false universal claims get forced into `incoherent` or `known`.
- **G2** Redefine `ontology-leap` as an undeclared, circular or stipulative
  bridge. The current text ("a bridge premise that does all of the work")
  kills every explicit conditional bridge argument, which is the philosophical
  contribution the project wants to test.
- **G3** Give S2 its own verdict set (excludes / neutral / supports-via-bridge /
  revises) and settle S2 cardinality (ontology only, 9 per survivor; or
  ontology × move, 54). Recommendation: ontology only. The move is already fixed
  by the parent claim, and 54 cells per survivor multiplies cost.
- **G4** Record transfer direction (source → target) in T1 records.
- **G5** State the adversary verdict set (`kill/survive/hold`) in CONTRACT.md.

## Undecidable by design

These need human judgment and the grid must not pretend otherwise:

- whether an argued bridge premise is *justified* (control 06's motivation);
- whether a present concrete truthmaker is philosophically adequate (control 07's open half);
- priority and novelty: a survivor has passed two AI kill attempts, nothing more;
- source correspondence: whether a cited predecessor actually says what the record claims.
