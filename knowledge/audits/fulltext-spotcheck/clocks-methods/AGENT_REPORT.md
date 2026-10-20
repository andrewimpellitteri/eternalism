# Clocks and methods full-text spotcheck

## Method

The sampling frame selected seven records under `audit_lane=clocks-methods`: five clock/QRF papers tied to RC-1, RC-3, or RC-5, plus two methods papers. I opened the frozen primary arXiv HTML version for each record and checked its title/author/version header, the listed section/equation locators, and the claim wording needed by the source contract. The seven source IDs are listed in `findings.jsonl`; the Page–Wootters measurement record has two frozen copies, both checked against the same primary version. The primary full texts were accessible; no abstract-only substitutions were used. I did not reproduce calculations, reconstruct theorem proofs, inspect companion repositories, or perform a general proof audit. Each source has at most one short quotation in the artifacts, below the 20-word per-source limit.

## Results

Six records are confirmed at the stated spotcheck scope. One record is marked `claim-overstated` because one frozen copy has conflicting author and version-date metadata. The primary header resolves the conflict: the authors are Ladina Hausmann, Alexander Schmidhuber, and Esteban Castro-Ruiz; arXiv v1 is dated 21 Aug 2023. The `knowledge/frontier/sources.jsonl` copy instead names Vincent Baumann and Max Lock and gives 2023-11-10; the `knowledge/ico-qrf/sources.jsonl` copy matches the primary author list and date. This review leaves both source registers unchanged for coordinator integration.

The substantive clock claims are located and correctly bounded in the records. In particular, the three-way relational trinity assumes an uncoupled clock/system constraint; the interacting Smith–Ahmadi result is a specific conditional-kernel construction; the relativistic trinity is sectorwise and treats cross-sector coherence as inaccessible to its relational Dirac observables; and the non-ideal measurement result is specific to the PM event model. These distinctions prevent the papers from being read as a general theorem about interacting clocks, universal memory, ontology, or fundamental discreteness.

The QRF-beyond-subsystems record correctly flags that its rigorous core assumes finite-dimensional Hilbert spaces and compact Lie groups, while continuous Example 29 is outside those assumptions and omits correct normalization. The two methods records are confirmed only as author-reported methodological claims. Diagrammatica's counts and comparisons remain within its toolkit-supported single-vertex decay benchmark; the Lean paper's companion repository/build and axiom dependency closure were not audited.

## Contract impacts

- **RC-1:** the spotcheck confirms several restricted precedents: Smith–Ahmadi's interacting conditional kernel; the relational trinity's no-interaction equivalence; and one model-specific interacting nonlocal-clock example. They do not establish necessary/sufficient conditions for general interaction-dependent autonomy or isometry. The QRF paper's continuous example cannot be treated as rigorous inside the paper's finite-dimensional framework; its finite Abelian analogue is the bounded formal example.
- **RC-3:** the relativistic trinity confirms sectorwise equivalence and superselection-based inaccessibility for the paper's relational Dirac observables. It does not itself prove a universal no-go for every possible conditioning instrument or external phase reference. The paper does not provide the contract's proposed sector-coherent rule.
- **RC-5:** the measurement-events paper confirms nonideal-clock PM time-nonlocal/nonunitary evolution in its model and ideal-clock TO/PM equivalence. Its discrete-time recovery is an author-argued conditional result under its setup, not evidence that physical time is fundamentally discrete. The spotcheck does not classify all four memory criteria.
- **RC-2/RC-4:** none of the seven sampled records directly supplies those contract claims.

## Dispositions and limits

Per-record evidence, exact versions, locators, verdicts, and downgrade proposals are in `findings.jsonl`. No source registers or unrelated files were edited. All seven primary HTML sources were accessible. The check confirms selected statements and locators only; proofs, repository code, logs, numerical results, and independent reproduction remain outside scope. The Page–Wootters copy conflict is the only correction proposed from this lane.

## Final synthesis review

I reviewed the coordinator's `AUDIT.md`, `AGENT_REPORT.md`, `verification.json`, the pinned-cutoff sampler/frame, and this lane's seven records. Counts reconcile: 20 full-text records plus two required primaries gives 22; verdicts sum to 22 (16 confirmed, three claim/metadata overstatements, two locator/edition corrections, one unreadable); 21 relevant bodies were accessible; lane counts are 7/7/8. The frame's three RC-4 aliases include one ID already selected by the seeded draw, leaving two additions to the original 20-record selection. The root audit's claims about preserved draws, unique coverage, and the sample being descriptive rather than a population error-rate estimate are consistent with the sampler and verification summary.

The RC-1/RC-3/RC-5 boundaries in the synthesis match this lane's primary checks: restricted no-interaction trinity vs. specific interacting-kernel/QRF examples; frequency-sector restrictions and no general external-reference no-go; and model-specific nonideal-clock PM behavior without a four-criterion memory classification. I found no cross-report inconsistency requiring correction. The measurement-record author/date conflict is accurately stated and remains an owner/canonicalization decision; source registers remain untouched.
