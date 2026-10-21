# Example and scope decisions for the reframed article

Date: 2026-10-21. Input to `article-rebuild-integration`. The reframed paper is
about Brading, local presents and unrestricted existence; these decisions keep
it from drifting back into a prospectus.

## 1. Quantum three-state-clock/qubit example — CUT

**Decision:** remove Case II from the main text.

**Reason:** at the sampled couplings the selected energy sectors are
one-dimensional. Any linear reduction map on a one-dimensional sector is a
scalar, so the apparent nonisometry is a reweighting, not a state-dependent
obstruction. The example is underreported (matrices, clock states/POVM,
reduction maps, inner product, sampled values) and does not test relational
equivalence on a nontrivial state family. Keeping it would repeat the external
review's point 7.

**What remains:** one sentence in the revision/status note: "The earlier clock
calculation was a one-dimensional diagnostic and is not used." If a future paper
wants the clock case, it must specify a nontrivial sector and a defended inner
product first.

## 2. Finite record example — CUT from main text; optional appendix only

**Decision:** remove the record proposition from the main argument. It may
survive as a short appendix only if the paper needs an example of likelihood
bookkeeping; it should not be a case study.

**Reason:** the proposition assumes matching probability measures and complete
outcome kernels, then proves matching outcome probabilities. The disputed
physical content is in the hypotheses. The finite-path model is revealed data
plus an access restriction, not a memory-bearing subsystem whose dynamics
explains the restriction. The external review's controlled-process construction
(sequential randomness versus presampled causal response) is a better
bookkeeping illustration if one is needed, but it does not establish temporal
ontology.

**What remains:** if retained, one appendix paragraph with the controlled-process
construction, explicitly labelled bookkeeping.

## 3. LAGEOS / preferred-frame material — CUT to one footnote or remove

**Decision:** remove the detailed LAGEOS numbers from the main text. If a
comparison to other cases is needed, one sentence:

> Parameter constraints such as the LAGEOS preferred-frame bound constrain a
> named gravity model, not an ontology; a timelike vector field is not by itself
> a preferred foliation.

**Reason:** the numerical precision does almost no argumentative work; the
conclusion is unchanged if the bound improves. The vector/foliation distinction
must be explicit if the case is mentioned at all.

## 4. Causal-set discussion — MOVE to future work

**Decision:** remove from the main argument. One sentence in the conclusion or
future-work note:

> The causal-set material concerns covariant event structure and extension; it
> does not yet connect that structure to physically available records or to a
> temporal ontology.

**Reason:** the paper lacks the bridge from covariant events to records and then
to ontology. The external review is right that the draft is broadest where it is
least complete.

## 5. Stein — KEEP as a compact source note

**Decision:** keep only the corrected four-way distinction, in a footnote or a
short paragraph where the local-present/definiteness connection is used:

- displayed theorem;
- non-universality (condition iv);
- causal-past inclusion (timelike or null);
- chronological-past inclusion.

The reflexive strict chronological past counterexample must remain. Do not
make Stein a central section.

## 6. Repeated disclaimers — CONSOLIDATE

**Decision:** replace the repeated "no novelty / no ontology / no empirical
prediction" notes with one status paragraph at the end. The paper should state
its limited conclusion and its non-claims once, not after every section.

## 7. What stays

- The existential contrast and the coverage objection (core).
- Brading reconstruction (core).
- The burden calibration as a short methodological section, not the paper's
  centre.
- The favoring account as the verdict form.
- Saunders/Pooley as the strongest-objection section.
- One conclusion with a limited verdict and defeat conditions.

## 8. Integration instructions

`article-rebuild-integration` should:

1. Build the new paper around `paper/REFRAME.md`.
2. Use `research/brading-existence/RESULT.md` for the core.
3. Use `research/admissibility-calibration/RESULT.md` for the burden section.
4. Use `research/favoring-account/RESULT.md` for the verdict form.
5. Use `research/strongest-opponents/RESULT.md` for the objections section.
6. Cut items 1–4 above; keep item 5 compact; consolidate item 6.
7. Rebuild, run `paper/check_records.py`, inspect the PDF, update
   `verification.json` and `READINESS.md`.

## Non-claims

These cuts do not deny that the clock, record, LAGEOS or causal-set work is
useful in its own lane. They deny that it belongs in this paper's main argument.
