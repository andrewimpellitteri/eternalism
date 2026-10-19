# Thermal time, modular flow, records and the arrow: comparison

Completed by a Claude subagent after the original GLM worker died (see AGENT_REPORT.md). Not a verdict on any ontology. Read depths follow sources.jsonl; items tagged (existing) are records from other lanes that I did not re-read, and are only as deep as their own records say. Three things are kept apart throughout: a **flow** (a one-parameter group of automorphisms or translations), a **clock** (a physical system or protocol whose readings track a parameter), and an **arrow** (an asymmetry in a process, record or boundary condition). No source below establishes objective passage, presentism or eternalism.

## What defines a flow, a clock, an arrow

| Result | Defines | Does not define |
|---|---|---|
| Tomita-Takesaki: faithful normal state on a von Neumann algebra gives modular operator and group alpha_t (Connes-Rovelli Sec. 2.1 eqs. 6-8, citing the theorem; Borchers 2000 and Takesaki 1970 unread/discovery) | A **mathematical flow**, intrinsic to (algebra, state) | Any physical clock, any temperature scale, any direction of time (alpha_t and alpha_{-t} are both in the group) |
| Connes cocycle theorem (cited in Connes-Rovelli) | Flow is state-independent up to inner automorphisms: a canonical flow on Out(R) | That any representative is the physical time; the inner freedom is exactly where the clock choice would live |
| KMS condition / HHW 1967 (cited; unread) | Link between a state and inverse temperature beta for a *given* dynamics gamma_t; any faithful state is KMS at beta=1 for its own modular flow | That the given dynamics is physical, since equilibrium characterised by KMS already presupposes a time evolution (Chua's circularity worry, existing record frontier-thermal-time-concept-2024) |
| Bisognano-Wichmann 1975 (existing aqft-bisognano-wichmann-1975, full-text in that lane) | For the vacuum and a wedge algebra the modular flow equals the wedge-preserving boost (2 pi convention-dependent) | A universal clock; the flow is a boost parameter for that wedge, i.e. a proper-time-like parameter along Rindler observers, and the identification with an observer's clock is the Unruh/thermal-time bridge premise |
| Thermal time hypothesis (Connes-Rovelli Sec. 3.1) | A **proposal** that this flow is physical time and that temperature is the ratio of thermal to geometric time | Not a theorem; the authors call it a postulate supported by consequences |
| Time asymmetry from boundary conditions (arrow-* lane; Past Hypothesis) | A candidate **arrow** (low-entropy initial macrostate plus typicality) | A flow or clock; reversible dynamics are time-symmetric |
| Records (Hartle 2016, Page 1993, Mlodinow-Brun 2014) | Correlations carrying information about a history; a record **direction** | A clock; not the thermodynamic arrow unless extra premises are added; not passage |

Where each result sits: modular flow = flow; KMS/temperature = relation between state and a pre-given dynamics; operational thermal clocks = protocol proposals (Menicucci-Olson-Milburn, existing frontier-thermal-clock-relational-2011); Past Hypothesis, records = arrow-type statements.

## Anchor comparison (six-item contract)

Items: (1) what exists, passage, future; (2) state space, dynamics, causal structure, clock; (3) symmetries, preferred structures, observers, boundary; (4) predictions and empirical status; (5) bridge premises and alternatives; (6) equivalences, contradictions, domain limits.

### A. Connes-Rovelli thermal time hypothesis, gr-qc/9406019v1 (tr-connes-rovelli-1994, full-text via summariser)

1. Algebra/state: von Neumann algebra R, cyclic separating vector (equivalently faithful state on a C*-algebra by GNS). The paper does not claim passage is fundamental; it proposes time is state-dependent and emergent (relational stance in tr-rovelli-forget-time-2009, abstract only). The future is not addressed as fixed or open.
2. Modular operator from S A Psi = A* Psi, S = J Delta^{1/2}, flow alpha_t A = Delta^{-it} A Delta^{it}. Gibbs case: alpha_t = gamma_{beta t} (derived, Sec. 4.1). No causal structure is input; clock = the hypothesised identification of alpha_t with physical time, not constructed from a device.
3. Generally covariant context: no preferred time, so the state supplies one. Observer access enters via which state/algebra is used (Martinetti-Rovelli 2003, abstract: finite-lifetime observer gives different temperature). Boundary conditions: the choice of state is the boundary-like input; the paper does not say which state is the universe's.
4. No empirical test in the paper. Recovers Unruh temperature via BW (Sec. 4.3, derivation from a cited theorem); Hamilton equations formally (heuristic). van Neerven-Portal (abstract) claim thermal time is an unsharp observable for specific systems; unverified by me beyond abstract.
5. Bridge premises: that the modular flow *is* physical time (hypothesis); that the state is thermal/equilibrium in a time-free sense. Alternatives: state-relative flow as bookkeeping only (Chua, existing record); operational local thermal clocks (existing Menicucci et al.).
6. Equivalence: flows from different states agree modulo inner automorphisms. Conflict: equilibrium characterisation presupposes dynamics (Chua). Domain: the faithful-state/type-III-style structure is assumed; thermodynamic arrow not derived (modular flow is reversible as a group, orientation is a convention in sign, cf. paper's footnote 3 on sign convention).

### B. Modular theory and Bisognano-Wichmann (aqft-tomita-takesaki-1970 discovery; aqft-bisognano-wichmann-1975 full-text; tr-bisognano-wichmann-1976 discovery/metadata)

1. Algebra/state: wedge algebra of a Wightman-type field and the vacuum (1975 hypotheses in aqft record: Poincare-covariant, spectrum condition, unique vacuum, cyclicity). Nothing about passage.
2. Modular group equals the wedge boost; modular conjugation relates to TCP/reflection. Causal structure enters through locality of the algebra net. Flow = Lorentz boost for that wedge, a geometric parameter.
3. Symmetry: Poincare; preferred structure: the wedge (an observer family). Boundary: vacuum state.
4. Predictions only through Unruh-type interpretation, which is a separate physical bridge.
5. Bridge: proper time of the accelerated observer = modular parameter / 2 pi. This is where "clock" enters.
6. Correction recorded: DOI 10.1063/1.522898 is "On the duality condition for quantum fields", J. Math. Phys. 17, 303-321 (1976) per Crossref; the existing aqft-bisognano-wichmann-1976 record has a different DOI and title. I did not read the 1976 paper, so no result is attributed to it, and I did not check what 10.1063/1.522676 resolves to. The general (any net, any state) modular geometry is not given by BW.

### C. Hersent 2025, arXiv:2502.12750v1 (tr-hersent-2025, full-text, partial self-read)

1. Algebra A_l: noncommutative Minkowski (kappa- and rho-deformations) as Hopf dual of deformed translations; weight omega = spacetime integral (omega(1) = infinity, so a weight, not a state). No claim on passage.
2. Twisted cyclicity gives twist I; modular operator = I^2. kappa-Minkowski: flow is a translation of x0 by (d/kappa)t; rho-Minkowski: trivial flow (unimodular).
3. kappa case breaks kappa-Poincare invariance and selects a frame (author's Sec. 4.2). State: the "highest temperature" weight (author's reading, footnote about the Planck temperature).
4. Phenomenology (particle production, photon masses) described by the author as speculative and not derived. No empirical status.
5. Bridge premises: thermal time hypothesis applied to a non-normalisable weight; interpreting kappa as a temperature; relating trivial flow to discreteness of time. Also, because the modular flow is a translation by construction, the result that "thermal time equals global time" is a statement about the algebraic setup, not a measurement.
6. Preliminary version; local compactness only at formal-power-series level; inner-automorphism freedom left open; factor 2 in modular operator flagged by the author as troubling. Prior lines named by the author include Matassa 2013 and Poulain-Wallet 2018 (reference list per dead worker's log; those papers were not read). Mathematical flow here; no clock.

### D. Records and memory (frontier-records-histories-2016 and frontier-records-time-asymmetry-1993, existing, full-text in the frontier lane; tr-mlodinow-brun-2014 abstract only)

1. State: a decoherent-histories closed system (Hartle, Page); a generic memory-plus-environment system (Mlodinow-Brun). Records are correlations; passage is not assumed. Hartle's account is block-like (histories) but is silent on ontology.
2. Dynamics: unitary; consistency/decoherence needed for probabilities. Clock: not constructed by records.
3. Boundary: initial or final state matters; Page argues time asymmetry attributed to quantum mechanics may be an artefact of the initial-state assumption (existing record's summary). Mlodinow-Brun (abstract): memory direction matches thermodynamic arrow where the latter is defined, under robustness and non-fine-tuning principles, even for reversible memories.
4. No experimental test. Operational content: record-based inference, not a measured arrow.
5. Bridge: "psychological arrow" or memory direction = thermodynamic arrow depends on typicality/no-fine-tuning premises, and on the thermodynamic arrow itself being given by a boundary condition.
6. Domain: conditional on a defined thermodynamic arrow. A past-record/future-prediction asymmetry is not objective passage.

### E. Past-Hypothesis arguments (existing arrow-cosmology lane IDs, not re-read here)

Use arrow-goldstein-boltzmann-2001, arrow-gtz-no-ph-2016, arrow-earman-past-hypothesis-2006 (abstract), arrow-penrose-wch-1979, arrow-lazarovici-reichert-2018, arrow-wallace-gravity-entropy-2009 and the tables in knowledge/arrow-cosmology/comparison.md. The contract entries there already cover items 1-6. Added here only the interface: the PH supplies an *arrow* (a low-entropy boundary macroregion plus typicality). It does not supply a modular flow or a clock, and no thermal-time source I read invokes the PH. The relationship between the Connes-Rovelli state (which state counts as 'the' thermal state) and a PH low-entropy macrostate is, as far as this lane read, not addressed; this lane did not search for a paper that does.

## Where the literature conflates (flagged, with attribution)

- Thermal time hypothesis itself: calling the modular flow "time" merges a flow with clock time; the authors present it as a postulate (Connes-Rovelli Sec. 3.1), so the conflation is a bridge premise, not an oversight. Chua (existing) argues a strong reading is circular.
- "Thermal" suggests a thermodynamic arrow, but the modular group is time-reversible as a group; orientation is a sign convention. Hersent's trivial flow for the unimodular case is read as absence of thermal dynamics, not of an arrow.
- Hersent links absence of thermal time to "discreteness of global time": a mathematical property of the algebra read as a physical feature of time.
- Unruh/BW: boost parameter, a kinematic proper-time-like flow, read as a temperature; temperature relies on the clock identification.
- Records: memory direction vs thermodynamic arrow vs experience of passage (Mlodinow-Brun's title uses "psychological arrow"). Matching directions are conditional on the stated principles.
- Past Hypothesis: boundary condition vs law vs explanation of the arrow; Earman's objection concerns well-definedness of the entropy, not just the status.

## Nearest predecessors and defeaters (no novelty claim)

Nearest: Connes-Rovelli 1994; Rovelli 1993; Martinetti-Rovelli 2003; Menicucci-Olson-Milburn 2011; Chua 2024; van Neerven-Portal 2023; Matassa/Poulain-Wallet for the modular structure of kappa-Minkowski. A suggested gap such as "a modular flow of a state is no clock without an additional operational clock premise" is defeated by: a paper that supplies and tests such a premise generally; Chua-type arguments already stating it (they do, for the strong TTH); or a result that modular flows of physical states are measurable for realistic observers (van Neerven-Portal point toward this for specific systems).
