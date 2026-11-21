# Page-Wootters: objections and defenses, objection by objection

Status: submission for review, 2026-10-20. Worker lane `kb-pw-critiques`.
Source records: `sources.jsonl` (all identifiers verified against Crossref /
INSPIRE / arXiv landing data on 2026-10-20; see AGENT_REPORT.md for commands).
Depth labels follow `knowledge/README.md`. Nothing here is a novelty claim.

Reading conventions for this file:

- **Paper claims** = what the named authors assert (at the recorded depth).
- **Established** = peer-reviewed results whose statement this lane read in the
  primary text at the stated depth (still not independently reproduced unless
  `reproduced`).
- **Conjecture (ours)** = clearly tagged; must not be attributed to any source.

## Setting taxonomy

Same-label theories differ; each row below names the setting precisely:

- **S1 finite-dimensional** clock+system with equally-spaced bounded spectrum
  (qubit/spin clocks; Pegg-style Age; periodic time-crystal clocks).
- **S2 covariant-POVM** clocks: possibly non-orthogonal time states, bounded or
  unbounded spectrum, constraint conditioning with physical inner product
  `<psi|delta(C)|phi>` (trinity setting).
- **S3 interacting** clock-system constraint `C = H_C + H_S + H_int`.
- **S4 quantum-gravity / canonical** setting: Wheeler-DeWitt constraint,
  minisuperspace or full superspace, group-averaging inner products.

Per AGENTS.md: these distinctions are kept because results do not transfer
across them, and because conditional-time statements are about **clock time**
(relational clock readings), which is not interchangeable with temporal
ontology (presentism/eternalism), objective passage, determinism, causal order,
or the thermodynamic arrow. Section 4 maps each objection onto these distinct
notions so later lanes cannot conflate them.

## 1. Objection-by-objection table

Reply status values: `answered` (a published reply read at least at abstract
level addresses the same construction), `partially answered`, `contested`
(published disagreement without adjudication), `unanswered (as read)`, `open`.

| # | Objection (exact form) | Source(s) | Setting | Reply status | Reply source(s) | Depth (objection) |
|---|---|---|---|---|---|---|
| O1 | **Preferred time variable**: the conditional-probability interpretation "requires one to pick out a 'preferred time variable' (or preferred class of such variables) from among the dynamical variables"; not all variables are fit to "set the conditions", and no criterion is given by the theory | pw-unruh-wald-1989 (Sec. I; Eqs. 1.14-1.15) | S4 (minisuperspace + parametrized particle), noninteracting | **Partially answered** for modern formalism: covariant-POVM conditioning makes "clock" a frame choice with transformation rules, but the choice is still extra structure; revived at operator level by Stoica 2026 | frontier-relational-trinity-2019v3 (full-text, frontier lane); frontier-time-delocalization-2026; pw-stoica-preferred-time-2026 | full-text |
| O2 | **No perfect clock theorem**: if the Hamiltonian is bounded from below, no dynamical variable can correlate monotonically with Schrodinger time; so a dynamical variable cannot play the interpretive role of `t` ("Heraclitian property") | pw-unruh-wald-1989 (theorem, Eqs. 1.38-1.39; footnote 16 flags conflict with Peres 1980) | Ordinary QM with lower-bounded H | **Contested-lineage**: PW-style constructions use unbounded-below ideal clocks (giving up the premise); POVM constructions accept non-ideal clocks and corrections; the Peres disagreement is unresolved in primary texts read here | pw-peres-1980 (abstract); pw-favalli-smerzi-time-observables-2020 (bounded clocks, discrete time predictions); frontier-page-wootters-measurements-2023 (non-ideal clocks) | full-text |
| O3 | **Ergodicity**: "the suggestion by Page and Wootters that dynamical evolution can be described in terms of stationary observables as a dependence upon internal clock readings is manifestly not viable for sufficiently complicated (i.e., ergodic) systems: there are no nontrivial stationary observables" | pw-unruh-wald-1989 (Sec. I) | S4, systems ergodic on energy surfaces | **Unanswered (as read)**: no published reply found in this pass; later work evades rather than answers by dropping the stationary-observable framing (constraint conditioning instead). Do not claim it is refuted | (none found; searches recorded in AGENT_REPORT.md) | full-text |
| O4 | **Measure ambiguity**: the conditional "probability density" needs a measure on the conditioning variable's space, which "contain[s] as much information about the probability distribution as does Psi"; normalization/`dμ` choice undetermined | pw-unruh-wald-1989 (Sec. I, after Eqs. 1.14-1.15) | S4 | **Partially answered**: the physical inner product (group averaging / conditional choice) fixes the measure per model, but that choice is exactly where the inner-product objection (O6) bites | frontier-smith-ahmadi-interacting-2019 (chosen conditional inner product, time-independent normalization required); pw-held-maxfield-inner-products-2025 | full-text |
| O5 | **Physical inner product failure**: group-averaged would-be inner products can be **indefinite** ((p,q)=(1,1) SL(2,R) example), divergent, or renormalizable only into superselection sectors; Giulini-Marolf: strongly convergent indefinite averaging admits **no rigging map** | pw-louko-group-averaging-2006 (Secs. 2, 4, 5) | S4-analog finite-dimensional constrained systems | **Partially answered**: group averaging defended as "the correct physical inner product" where it works; KG product admitted non-positive; per-model construction remains the rule | pw-held-maxfield-inner-products-2025 (abstract); pw-hartle-marolf-1997 (KG vs induced schemes physically inequivalent, abstract) | full-text |
| O6 | **Two-time propagator**: Kuchar "questioned the possibility of constructing a two-time propagator" within PW | pw-kuchar-2011 as reported by pw-favalli-smerzi-time-observables-2020 App. A (second-hand, labeled) | PW (S1/S2, noninteracting) | **Answered at construction level**: Giovannetti-Lloyd-Maccone 2015 builds multi-time conditional probabilities (attribution via Favalli-Smerzi and Paiva et al. reference lists); whether multi-time conditionals satisfy classical consistency conditions is not settled by what this lane read | pw-favalli-smerzi-time-observables-2020 App. A; GLM "Quantum time" PRD 92, 045033 (DOI verified; abstract not retrieved this session — treat attribution as second-hand) | abstract (of the reporting source) |
| O7 | **Clock ambiguity**: "a theory set up to describe one set of physical laws can equally well be interpreted as describing any other laws of physics by making a different choice of time variable or clock" | pw-albrecht-iglesias-clock-ambiguity-2008 (abstract) | Time-reparametrization-invariant theories (S4 lineage) | **Contested, then sharpened**: Marletto-Vedral 2017 titled as the ambiguity-free construction; Stoica 2026 argues no purely relational condition solves it (extends to evolution-law spectra) and proposes fixing the physical meaning of observables | pw-marletto-vedral-2017 (abstract); pw-stoica-clock-ambiguity-2026 (abstract) | abstract |
| O8 | **Preferred-time problem (operator form)**: an entangled clock+world state admits infinitely many product-state decompositions, each defining a different equally valid clock-time operator, hence different histories that are superpositions of each other | pw-stoica-preferred-time-2026 (abstract) | PW (general bipartite states) | **Open**: no reply read; note it refines O1 from "which variable" to "which operator/decomposition on the same variable" | (none read) | abstract |
| O9 | **Conditional probabilities are not ordinary conditionals**: physical states do not factorize; `<psi_phys|E_A⊗E_B|psi_phys>` diverges for continuous-spectrum constraints; two-clock "conditionals" coincide with each other and with the would-be joint, and the naive denominator is identically 1; reduction maps are only partial isometries per superselection sector | pw-hosseini-lock-toa-2026 (Sec. IV, Eqs. 31-32; Secs. II-III, App. A) | S2 covariant-POVM, free particle, noninteracting | **Absorbed, not refuted**: the relational program reinterprets conditionals as reduction-map images rather than classical conditionals (trinity Sec. VI is cited by Hosseini-Lock itself for the critical "time from entanglement" discussion); Adlam presses the interpretive cost | frontier-relational-trinity-2019v3 (full-text, frontier lane); pw-adlam-watching-clocks-2022 (abstract) | full-text |
| O10 | **Bounded-clock paradoxes**: the empirical predictions of the bounded periodic-clock time-measurement proposal are "paradoxical" as arrival-time solutions (three criticisms) | pw-cavendish-unphysical-2024 (abstract) | S1 finite-dimensional periodic clocks | **Contested**: authors' reply asserts all three criticisms are "without merit", one resting on "a logical mistake"; no independent adjudication read; Hosseini-Lock show the periodic-clock proposal is physically distinct from ideal-clock PW (different ToA distribution) | pw-maccone-reply-2025 (abstract); pw-hosseini-lock-toa-2026 Sec. V | abstract |
| O11 | **Clock back-reaction / interaction**: interacting constraints modify conditional dynamics (memory kernel `K(t,t')=<t|H_int|t'>`), with chosen inner product required to give time-independent normalization; nonlinear effective equations for quasi-ideal clocks; clock measurement seems to require breaking isolation | frontier-smith-ahmadi-interacting-2019 (full-text, frontier lane); pw-mendes-nonlinear-pw-2021 (abstract); pw-kuypers-rijavec-measuring-time-2024 (abstract) | S3 | **Partially answered**: interaction corrections computed in models; Kuypers-Rijavec prove the clock can be measured while preserving PW features; trinity-equivalence for interacting POVM clocks remains open (frontier-lane open question, unchanged) | pw-rijavec-unitarity-2025 (necessary/sufficient unitarity conditions, abstract); pw-paiva-nonhermitian-2022 | abstract+full-text mix (per row source) |
| O12 | **Non-Hermitian conditional dynamics under motion/gravity**: from the perspective of an accelerating or gravitationally interacting (distance-varying) clock, `H_eff=[I+f(X)]^{-1}H` is non-Hermitian; conditional norm non-constant; "there is no clock frame ... for which the effective dynamics is exactly Hermitian" (their claim, given their gravity modeling) | pw-paiva-nonhermitian-2022 (main text Eqs. 7-19, Discussion) | S3, post-Newtonian fixed background | **Partially answered**: unitarity recoverable by normalization or by metric (Dirac/Pauli) methods, but metric choice is non-unique and may lack positive-definite metric (ghost states) — which reconnects to O5; Rijavec's constant-rate condition is a clean partial criterion | pw-rijavec-unitarity-2025 (abstract); pw-paiva-nonhermitian-2022 Discussion | full-text |
| O13 | **Realistic clocks destroy unitarity**: relational time with quantum (realistic) clocks induces fundamental decoherence and information loss | pw-gambini-porto-pullin-2004 (abstract; NJP 6, 45; PRL 93, 240401) | S3/S4 with consistent discretizations | **Contested lineage**: later work treats non-unitarity as conditional-perspective effect (O12) rather than fundamental; no direct published refutation read this pass | pw-paiva-nonhermitian-2022 (Discussion, contrast drawn there) | abstract |
| O14 | **Isolated clock cannot be measured**: measurement requires interaction, but PW assumes a noninteracting clock | pw-kuypers-rijavec-measuring-time-2024 (abstract; problem statement) | S2 noninteracting baseline | **Answered at construction level** by the same paper (proof that the clock can be measured preserving core features); costs for conditional dynamics unassessed here | pw-kuypers-rijavec-measuring-time-2024 | abstract |
| O15 | **Operational/interpretational gap**: the "reference frames" of PW/IQRF may not be operationally meaningful absent an interpretation; unsuitable for defining an equivalence principle; operational content only in the large-reference-system limit | pw-adlam-watching-clocks-2022 (abstract; FoP 52, 99) | Interpretation of S1-S3 and temporal QRFs | **Unanswered (as read)**: the QRF lane's own 2026 operational-meaning paper explicitly does NOT address this criticism (frontier-qrf-operational-meaning-2026: "Adlam 2022 criticism ... explicitly not addressed") | (none; recorded as open by frontier-qrf-operational-meaning-2026) | abstract |
| O16 | **No arrow of time from PW**: the mechanism itself supplies no thermodynamic or ontological arrow; entropy increase in PW simulations/experiments is a property of the chosen conditioning/state, not a fundamental arrow | pw-favalli-smerzi-time-observables-2020 Sec. 4.3 ("The answer is clearly negative" for PW as such; emergent arrow only via extra entanglement assumptions); related: frontier-records-time-asymmetry-1993 (full-text, frontier lane) | S1/S2 + interpretive | **Answered-by-consensus in the defense literature** (arrows are emergent, added by assumptions about subsystems/entanglement production); the Sergent preprint (pw-sergent-arrow-2026, unread lead) argues the stronger negative; do not treat experiments (Moreva 2014/2017) as arrow evidence | pw-moreva-2014 (abstract; claims correlation-illustration only); disc-moreva-pagewootters-2017v1 (existing record) | full-text |
| O17 | **Ancilla/clock-resource conditions**: the clock Hilbert space must exceed the system's (`d_c >> d_s`) or some system states are excluded from the dynamics; quantum frames must be treated on a par with systems (Aharonov-Kaufherr) | pw-favalli-smerzi-time-observables-2020 Sec. 4.3; pw-aharonov-kaufherr-1984 (abstract) | S1 (finite-dimensional), QRF framing | **Open**: the `d_c >> d_s` requirement is stated, not removed; its physical cost for cosmological systems is unassessed in what was read | (none read) | full-text/abstract mix |
| O18 | **Experience/change objection (Kuchar school)**: conditional probabilities as such do not explain the appearance of temporal flow (the reason Kuchar examined "ten major attempts" and found shortcomings) | pw-kuchar-2011 (abstract only: "I critically examine ten major attempts ... and discuss their shortcomings") | S4, interpretive | **Open**: Adlam 2022 presses the modern form (O15); Rovelli's programmatic defense (relations, not evolution) does not, in what was read, constitute a derivation of experienced flow | pw-rovelli-forget-time-2009 (abstract); pw-adlam-watching-clocks-2022 | abstract |

## 2. Which objections apply in which setting (matrix)

| Objection | S1 finite-dim | S2 covariant POVM | S3 interacting | S4 quantum gravity |
|---|---|---|---|---|
| O1 preferred variable | bites (choice of clock observable) | bites (frame choice) | bites | original home (Unruh-Wald) |
| O2 no perfect clock | bites (bounded spectra) | softened (non-ideal accepted) | n/a | premise givable up (unbounded clocks) |
| O3 ergodicity | unclear | unclear (no study read) | unclear | original home |
| O4/O5 inner product & measure | mild (finite dim) | bites (denominator, sectors) | bites | bites (group averaging pathologies) |
| O6 two-time propagator | answered by construction | answered by construction | reopens | reopens |
| O7/O8 ambiguity / preferred operator | bites | bites | bites | bites |
| O9 conditionals not classical | mild | sharp (continuous spectra) | sharp | sharp |
| O10 bounded-clock paradoxes | home | n/a | n/a | n/a |
| O11-O13 back-reaction / non-Hermitian / decoherence | n/a | n/a | home | home (GPP) |
| O15/O18 operational & experience | home | home | home | home |

## 3. Paper claims vs established vs ours

- **Established results this lane read in primary text** (statement level; none
  re-derived): Unruh-Wald no-perfect-clock theorem (proof read, not
  reproduced); Louko's indefinite group-averaging example and rigging-map
  failure cases; Hosseini-Lock's sector structure of the free-particle PW
  Hilbert space and the Kijowski-coincidence of their relational ToA
  distribution (equation-level read); Favalli-Smerzi's Age-as-time-operator and
  POVM resolutions of identity (appendix proofs read, not recomputed); Paiva
  et al.'s non-Hermitian effective Hamiltonians under their post-Newtonian
  modeling (main-text derivation read).
- **Paper claims awaiting independent verification** (abstract-level only):
  GLM 2015 multi-time construction as answer to Kuchar's propagator objection
  (attribution is second-hand); Marletto-Vedral ambiguity-free construction;
  Albrecht-Iglesias quasiseparability proposal; Kuypers-Rijavec measurable
  clock theorem; Rijavec unitarity iff-conditions; Gambini-Porto-Pullin
  fundamental decoherence; Trassinelli Gleason-Bush derivation.
- **Conjectures (ours, tagged, no novelty claimed)**:
  - *Conjecture (ours)*: the metric ambiguity Paiva et al. need to restore
    unitarity is the same freedom as the physical-inner-product choice of
    constraint quantization (O12 ↔ O5). No source read asserts this identity.
  - *Conjecture (ours)*: O3 (ergodicity) and O9 (conditionals not classical)
    jointly suggest the PW conditional states should be read as
    reduction-map images (trinity) rather than as classical conditionals; if
    so, Unruh-Wald's O1/O4 objections transmute into the already-formalized
    frame-choice problem rather than remaining fatal. This is an
    interpretation, not a result.

## 4. Concept-separation ledger (per AGENTS.md)

- **Temporal ontology** (presentism vs eternalism etc.): no source read this
  pass establishes or refutes any ontology via PW. PW supplies correlations
  among clock readings; Unruh-Wald and Adlam both deny it fixes an ontology.
- **Objective passage**: not delivered by PW (O16, O18); defenses only claim
  emergent, assumption-laden arrows.
- **Determinism**: orthogonal; PW is a kinematic constraint formalism and is
  compatible with stochastic outcomes (Born rule recovered, Favalli-Smerzi
  Eq. 20/36). Nothing read links PW to determinism either way.
- **Causal order**: PW constraint conditioning does not by itself fix causal
  order; the indefinite-order/vintage claims belong to the ico-qrf lane
  (ico-baumann-noncausal-pw-2022; frontier-page-wootters-measurements-2023
  Sec. IV.2.3) and are recorded there, not here.
- **Clock time**: everything in this lane is about clock time (relational
  readings of clock observables), including all spectral conditions (O2, O10).
- **Thermodynamic arrow**: separable (O16); arise only when extra
  subsystem-entanglement assumptions are added (Favalli-Smerzi Sec. 4.3;
  Marletto-Vedral lineage).

## 5. Nearest predecessors for any downstream claim, and defeaters

This lane makes no novelty claim. For any future claim of the form "we show X
about PW/conditional time", the nearest predecessors are, by objection class:

- Equivalence results (any new "PW = relational observable dynamics" claim):
  frontier-relational-trinity-2019v3 (full-text) and its relativistic
  extension frontier-relativistic-trinity-2020v1. **Defeater**: an equivalence
  theorem that already covers the proposed clock class.
- Interacting clocks (any new "PW with interaction" claim):
  frontier-smith-ahmadi-interacting-2019, pw-mendes-nonlinear-pw-2021,
  pw-rijavec-unitarity-2025, pw-paiva-nonhermitian-2022. **Defeater**: a
  published interacting-clock result with the same clock class and observable.
- Bounded/periodic clocks (any new measurement claim): pw-maccone-sacha-2020,
  the pw-cavendish-unphysical-2024 / pw-maccone-reply-2025 exchange, and
  pw-hosseini-lock-toa-2026 Sec. V. **Defeater**: the contested exchange
  settling, or an existing result showing the proposed prediction.
- Conditionals-as-classical (any claim that PW probabilities behave like
  classical conditionals): pw-hosseini-lock-toa-2026 Sec. IV. **Defeater**:
  their three conditions or the sector structure.
- Inner-product existence (any claim that the physical inner product is
  unproblematic): pw-louko-group-averaging-2006; pw-hartle-marolf-1997.
  **Defeater**: a positivity/convergence theorem covering the model class.
- Preferred-time / ambiguity (any claim that clock choice is canonical):
  pw-unruh-wald-1989, pw-albrecht-iglesias-clock-ambiguity-2008,
  pw-stoica-preferred-time-2026, pw-stoica-clock-ambiguity-2026.
  **Defeater**: a principled, non-question-begging selection rule (the open
  problem O1/O7/O8).
- Operational content (any claim that PW observers are already
  operational): pw-adlam-watching-clocks-2022 and its explicit non-addressing
  by frontier-qrf-operational-meaning-2026.

## 6. Known gaps in this collection (honest limits)

- Kuchar 2011/1992 read at abstract level only; all attributions of specific
  arguments to him are second-hand via full-text-read reporting sources and
  are labeled as such in `sources.jsonl`.
- The Hosseini-Lock, Favalli-Smerzi, Paiva, Louko, and Unruh-Wald results were
  read but **not independently reproduced**; no `reproduced` record exists in
  this lane.
- GLM 2015, Marletto-Vedral 2017, Peres 1980, Maccone-Sacha 2020, and the
  Kuchar-Torre / Brown-Kuchar defense papers are abstract- or
  metadata-depth only.
- Blocked this session (recorded unread, never as read): APS landing pages
  (HTTP 403), ADS abstract pages (405), Chapman Digital Commons postprint of
  Adlam (Cloudflare), HAL copy of Trassinelli (bot check), philarchive page
  for Sergent (bot check), ResearchGate/academia mirrors (not attempted
  beyond listing).
