# Defense of countable additivity as a completed-history condition

Sole-worker philosophical note, 2026-10-21. Chosen principle: **countable
additivity (regular Borel extension) as a condition on a completed-history
reading**, not on physics as such. This is a bridge-premise defense, not a
derivation of ontology. Read depths are stated; no new primary full-text reads
were added.

## 1. The principle, stated precisely

Let `Omega` be the compact space of infinite labelled histories, `A` the
cylinder algebra, and `mu` a finitely additive complex charge on `A` with the
prescribed cylinder values. The completed-history condition is:

> **(CA)** `mu` extends to a countably additive regular complex Borel measure
> on `sigma(A)`, with the same values on `A`.

Equivalently, `sup_n sum_{|C|=n} |mu(C)| < infinity` for the cylinder levels
(the bounded-variation criterion). This is a condition on the reading's
measure, not on the topology of spacetime and not on an observer's access.

## 2. Strongest argument for (CA)

1. **Completion is a countable object.** A completed history is a point of
   `Omega`; the events a completed-history reading needs are countable unions
   and intersections of cylinder conditions (a post occurs, a stem recurs, a
   limit event holds). A merely finitely additive charge need not assign
   values to those unions, and need not be continuous from below. If the
   reading says completed histories are all real, it should be able to
   evaluate the countable event algebra they generate.
2. **Response stability is the same condition.** On the compact path space,
   bounded variation, uniform stability of continuous-observable responses,
   and regular extension are equivalent (`research/operational-stability/
   RESULT.md`, Theorem 1). The equivalence is not a technical convenience:
   it says that a reading which treats the amplitude functional as physical
   must have responses that vanish when the control vanishes uniformly. A
   finitely additive charge with unbounded variation violates this at some
   finite resolution.
3. **The completion horn is explicit in the literature.** Arageorgis argues
   that the growing-block imagery the causal-set programme pursues is
   "parasitic on a block universe view" because the relevant dynamics is a
   probability measure defined only in the infinite-time completion
   (*Belgrade Philosophical Annual* XXIX (2016), p. 52). Wüthrich and
   Callender reply that there is "gauge-invariant growth" in the number of
   elements even when identities are indeterminate (arXiv:1502.00018v1,
   Sec. 4), and preserve a qualified becoming at metaphysical cost (Sec. 5).
   The disagreement is precisely about what completion is allowed to add.
   (CA) makes the cost explicit rather than hiding it in a finitely additive
   surrogate.
4. **The selected theorem gives the condition teeth.** For complex
   percolation outside `[0,1]`, the prescribed scalar amplitudes cannot be
   countably additive on the doubly-principal algebra
   (`research/paper-novel/main.tex`). A completed-history reading that keeps
   both the amplitude rule and (CA) is therefore excluded; one that drops
   (CA) must say what it uses instead. That is a real conditional burden, not
   an ontology proof.

## 3. Strongest argument against (CA)

1. **Physics may require only finite additivity on accessible events.** The
   event-filter and record-loss results show that a restricted observer
   algebra can have well-defined finite probabilities while the full
   amplitude functional has infinite variation
   (`research/event-filter-resources/`, `research/record-loss-robust/`).
   Demanding a regular Borel extension may impose structure no physical
   observer can access.
2. **Countable additivity does not select the dynamics' measure.** A Dirac
   measure at a completed causet is countably additive and normalized but
   generally does not encode the prescribed amplitudes. (CA) is a regularity
   condition, not a completeness condition; it can be satisfied by measures
   that are physically irrelevant. So (CA) is not sufficient to ground the
   reading, even if it is necessary for one formulation of it.
3. **The event algebra is a modelling choice.** The covariant post algebra,
   the stem algebra and the full cylinder algebra are different. A
   completed-history reading may legitimately use a smaller algebra; the
   non-extension result on a larger algebra does not automatically bind it.
   Arageorgis himself notes that a cardinality-based growth response is
   available at substantial philosophical cost (p. 52); that is a different
   bridge, not a refutation of (CA).
4. **No empirical discriminator.** (CA) is not testable independently of the
   model. It is a bridge premise about what counts as a completed history's
   event, not a physical law.

## 4. Verdict

**Known/conditional, not new.** The defense is a clean statement of a
condition already implicit in the extension literature
(Surya–Zalel 2020, Theorem 2.1; Dowker–Johnston–Surya 2010, Claims 1–2) and in
Arageorgis's completion critique. Its strongest form is the response-stability
equivalence, which turns (CA) from a mathematical convenience into a
continuity demand on a physical reading. Its strongest objection is that
physics may only license finite additivity on an accessible subalgebra; the
project's own event-filter work makes that objection concrete.

The decisive consideration is therefore not "does physics prove countable
additivity?" (it does not) but "what does the completed-history reading claim
to evaluate?" If it claims countable event combinations of completed
histories, (CA) is the right condition; if it claims only finite accessible
events, (CA) is an extra bridge premise that must be defended on other
grounds. Either way, (CA) does not select eternalism over presentism; it
constrains one way of formulating a completed-history reading.

## 5. What would change the verdict

- A physical observer model whose accessible event algebra is provably not
  countably generated, with finite-additive probabilities sufficient for all
  its predictions, would make (CA) a dispensable idealization.
- A derivation of countable additivity from a physically motivated continuity
  principle (not merely mathematical convenience) would strengthen the
  defense beyond "known/conditional".
- A completed-history reading that assigns truth values without any measure
  would fall outside the argument entirely; (CA) would not bind it.

## 6. Sources and read depth

- Arageorgis 2016: full text at the conclusion, printed p. 52; quotation
  verified in `research/source-gates/`.
- Wüthrich–Callender: arXiv:1502.00018v1, full text at Sections 4–5; journal
  edition not collated.
- Surya–Zalel 2020: Theorem 2.1 and Appendix B, targeted full text from the
  project source records.
- Dowker–Johnston–Surya 2010: Claims 1–2 and the bounded-variation argument,
  targeted full text from the project source records.
- Stein 1991 printed theorem: **blocked**; not used here. Earman 2008 and
  Malament 1977 were not newly reread for this note.
