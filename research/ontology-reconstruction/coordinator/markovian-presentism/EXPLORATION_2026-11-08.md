# What must travel with a change of clock?

8 November 2026. Speculative coordinator exploration; no accepted novelty or ontology conclusion. Builds on AUDIT_2026-11-08.md. No original-theory implementation undertaken before priority review.

## Selection

The most promising connection in this pass is between interacting quantum reference frames and operational quantum memory. Ask which experimental operations must be transported with a change of clock if a claim that the present screens off history is to retain its meaning.

The initial intuition: a description can retain all information while the operations available to its observer change. An equation being unitary does not settle whether an observer's restricted experimental process has memory. Conversely, changing descriptions cannot change the statistics of exactly the same physical experiments when those experiments are translated correctly.

This suggests looking for a boundary between two comparisons:

- the same experiments described in two frames;
- each frame's own restricted laboratory experiments.

They may yield different memory verdicts without contradiction. Establishing that general distinction would be familiar; identifying its exact boundary for interacting temporal frames could be useful.

## What the rereading actually established

Chataignier–Smith, arXiv:2610.28732v1, sections II.3–II.4, equations (19)–(26), Theorems 1–2 and displayed proofs, plus section V, were inspected directly. Their invertible reduction maps induce unitary frame changes with the physical inner products. They flag failure of the gauge-fixing operator's invertibility as an unresolved boundary. This does not by itself construct an equivalence of sequences of interventions. Earlier intake and other sections remain at inherited depth; domains and group averaging were not independently audited.

Horvat, arXiv:2610.41944v1, Principle 4 and equations (10)–(12), were reread directly. His comparison includes restarting from a surface event state, with a translation of subsequent worlds and a probability matching condition. Therefore our earlier proposal to replace this with an ordinary same-time conditional independence identity needs a substantive justification. No new verification of Proposition 3 was completed.

Taranto et al., Quantum Markov Order, PRL 122, 140401 (2019), DOI 10.1103/PhysRevLett.122.140401: publisher abstract and Definition 2/equations (4)–(5) excerpt read; arXiv:1805.11341v2 introduction also read. Instruments matter to memory length. The all-instruments restriction is already a central result, so a generic claim that memory depends on measurement cannot be ours. Proof appendices not audited. The HTML has an inconsistent displayed manuscript date; use the arXiv version identifier and publisher record, not that date.

Castro-Ruiz–Oreshkov, Relative subsystems and quantum reference frame transformations, Communications Physics 8, 187 (2025), DOI 10.1038/s42005-025-02036-x: abstract and sections on modelling frames, preferred factorisation and frame changes inspected in returned primary text. Relative subsystems and accessible algebras already have an explicit operational treatment. This is a close predecessor, not supporting evidence for novelty.

Sources:
- https://arxiv.org/html/2610.28732v1
- https://arxiv.org/html/2610.41944v1
- https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.122.140401
- https://arxiv.org/html/1805.11341v2
- https://www.nature.com/articles/s42005-025-02036-x

## Elementary baseline: what cannot be the discovery

Let two operational descriptions have a bijection between admissible experimental sequences, preserving outcome labels and joint probabilities. Require that this bijection also preserve the partition into history H, intervening block M and future F, including the allowed conditioning outcomes. For positive-probability conditioning events, the identity

p(f|m,h)=p(f|m)

holds in one description exactly when it holds in the other. Proof: both conditional probabilities are ratios of the same matched joint and marginal probabilities. Apply the inverse correspondence for the reverse implication. Zero-probability events are excluded here. This finite-outcome observation is elementary, not a new theorem.

The load-bearing condition is preservation of the experimental partition and admissible operations. A unitary map on instantaneous states alone supplies neither. A temporal frame change could mix which operations constitute the middle block or could map a local operation into an operation on several subsystems. Those are hypotheses to examine, not results established here.

A common mistake would be to take a bipartite entangling unitary, trace out different factors and call the resulting memory difference a new clock effect. That only demonstrates ordinary subsystem dependence unless the unitary and experimental restrictions are derived from a genuine clock construction.

## Candidate claim contract

Question: for a bounded class of interacting temporal frames with invertible physical reduction maps, when does the induced change of description extend to a probability-preserving correspondence between admissible multi-time instruments that preserves their history/middle/future partition?

Proposed output: a criterion in terms of the reduction maps and laboratory operation algebras; an explicit smallest clock model exhibiting failure of this criterion; a calculation showing whether a specified memory witness actually changes for each frame's independently motivated laboratory operations. Failure of the criterion alone is insufficient to prove a memory difference for a particular process.

Nearest predecessors: Chataignier–Smith supplies interacting frame maps; Taranto et al. supplies instrument-sensitive memory definitions; Castro-Ruiz–Oreshkov supplies relative accessible algebras. Compare also the 2020 clock-event-localisability work before deciding the criterion is new: https://www.nature.com/articles/s41467-020-16013-1 (discovery in this pass).

Potential added value: an exact account of when a clock change preserves temporal screening for available experiments, rather than only preserving the norm or instantaneous expectation values. No claim yet that the papers above omit this result.

Smallest example: first identify an existing finite or controlled finite-sector clock model satisfying the reduction hypotheses. Derive operations on the physical space, then derive both descriptions. Fix at least three experimental stages. Calculate identical predictions for transported experiments as a control, and compare the native operation sets separately. Do not truncate continuous clocks without bounding the resulting error or proving the relevant exact identities survive.

Independent check: a reviewer must audit the operational meaning, not just the matrix arithmetic. Compare the proposed criterion with known process-tensor transformations, quantum combs, subsystem-algebra normalizers and event-localisation results.

Kill conditions: the criterion is just an existing comb isomorphism theorem; the witness compares different physical experiments without acknowledging it; the frame map is not realizable by the stated clock model; the effect is solely discarding an environment; the example requires a singular reduction outside the advertised hypotheses; or all admissible transformations preserve the required partition automatically in the selected class.

Consequence: even success would distinguish full-state sufficiency from observer-accessible memory. It would not refute a fundamental/global-state Markovian claim, and it would not identify the ontology of time. Its relevance to presentism is to clarify which datum an empirical argument can legitimately use.

## Other dreams, and why not select them yet

1. An atlas of imperfect clocks: can locally invertible clock descriptions cover a physical sector where no single global clock works? Track transition maps and domain overlaps. Attractive, but local clock patches and the global problem of time are established territory. Moreover, maps of the form R_b R_a^{-1} telescope on common domains, so apparent holonomy may be a bookkeeping artefact. Only a proven domain or operational obstruction would be interesting.

2. Minimal physical memory of a present: quantify the least additional state needed to screen history for a fixed set of interventions. This connects intrinsic-state debates to predictive-state complexity. Minimal-state constructions already exist, and representational compression alone says nothing about what exists. Requires independently justified locality, covariance or resource constraints.

3. Reliable records versus nomically settled history: can a presentist route semantics preserve the observational content of records while rejecting unique past truths? This is closer to the philosophical reply, but source-faithful semantics and an account of reliability must precede a counterexample. A toy route that deletes the disputed truths is not enough.

## Next bounded milestone

Read the three nearest predecessors at proof/operational-definition depth and the clock-event-localisation paper; search specifically for multi-time intervention transformations between quantum reference frames. Produce either a precise nontrivial claim contract that survives this comparison or an explicit retirement note. Do not expand the presentism reply around this candidate until that milestone is passed.

## Search limits

Queries included quantum reference frames plus non-Markovian/process tensor and interacting clocks plus Gribov/invertibility. This was a targeted lead search, not an exhaustive priority audit. The recent Howarth HTML failed to load. The recent Semião–Chataignier paper remains at abstract depth. No experiment, simulation, external contact or independent review was performed.
