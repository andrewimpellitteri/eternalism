# Theory map: model/version-level comparison graph

Status: worker submission for review, 2026-10-19. This file integrates the
accepted knowledge-base lanes (foundations, formalization, frontier, methods,
seed) into a comparison graph whose unit is **a particular model/version plus
interpretation**, per the contract in `knowledge/README.md`. It records
ontology, dynamics, clocks, observers, symmetries, observables and empirical
status per node; connections live in
[`translations.md`](translations.md) and contested points in
[`disagreements.md`](disagreements.md). There is **no weighted metaphysical
truth ranking** anywhere in this map; empirical-status notes report what the
cited sources claim, at the recorded read depth.

Conventions:

- Node IDs `N01`–`N30`. Every node lists its source records from
  [`sources.jsonl`](sources.jsonl) with the recorded `read_depth`
  (`discovery`, `abstract`, `full-text`, `code-audited`). Depths are those of
  the producing lane except where a record says `map_role:
  new-check-by-theory-map`.
- Ontology fields state what the *model/its authors* commit to, not what is
  established. "Passage fundamental?" and "Future fixed?" are recorded as
  model commitments or open choices, never as findings of this map.
- Claims are labeled: **[paper-claim]** (authors' assertion), **[theorem,
  as-recorded]** (cited derivation at the recorded depth, not reproduced
  here), **[map-conjecture]** (our unverified bridge, must be marked
  conjectural in `translations.md`).
- Physical premises, mathematical definitions, and philosophical bridge
  premises are kept separate in each node; bridge premises are the only route
  from any node to an ontology, and none is forced by the physical premises
  alone.

Graph summary: 30 nodes, 6 clusters (A–F), 19 recorded connections
(`X01`–`X19` in translations.md), 9 registered disagreements (`D01`–`D09`).

---

## Cluster A — Relativistic kinematics, simultaneity, and ontological arguments

### N01 — Einstein-synchrony Minkowski kinematics (baseline frame structure)
- **Model/version:** Minkowski spacetime with inertial frames, Einstein clock
  synchronization, standard Lorentz transformations; 1905 kinematical section.
- **Sources:** `seed-einstein-1905` (discovery; fourmilab translation page
  screened by seed lane). Versions/locators not yet extracted at theorem level.
- **What exists / passage / fixed future:** no ontological commitment in the
  kinematics itself; supplies frame-relative simultaneity and causal cones.
- **State space / dynamics / causal structure / clocks:** events in
  `R^{1+3}`; light cones fix causal connectibility; clocks synchronized by
  light-signal convention per inertial frame.
- **Symmetries / preferred structure / access:** Poincare invariance; no
  preferred foliation; each inertial observer's simultaneity hyperplane is
  frame-relative.
- **Observables / empirical status:** time dilation, light-speed invariance —
  experimentally supported within SR's domain; deviation bounds routed through
  `seed-lorentz-data-2026` (see N06).
- **Bridge premises:** treating Einstein simultaneity as ontologically loaded
  is a bridge choice, not part of the kinematics (see D03).
- **Equivalences / domain restrictions:** synchronization convention within an
  inertial frame is otherwise arbitrary at this level; Malament-type
  uniqueness (N02) adds the structural premises that change this.

### N02 — Malament framework: causal definability of simultaneity
- **Model/version:** Minkowski + causal connectibility `kappa` + one inertial
  observer worldline; candidate simultaneity relations definable from that
  structure, subject to equivalence-relation, non-universality,
  cross-worldline-pair, and invariance conditions. Result: standard Einstein
  synchrony is unique under those conditions. **[theorem, as-recorded via
  secondary + critic sources]**
- **Sources:** `found-malament-1977` (abstract; primary text NOT accessed),
  `found-sep-malament` (full-text, secondary exposition),
  `found-sarkar-stachel-1999` (full-text, primary critique).
- **Ontology:** none established — a conditional definability result, not a
  theorem about metaphysical presentness or eternalism.
- **Symmetries / preferred structure:** invariance under causal automorphisms
  preserving the observer worldline; Sarkar–Stachel show **temporal-reflection
  invariance** is the premise excluding future/past null-cone alternatives —
  contested as physically unwarranted (D02).
- **Observables / empirical status:** mathematical; no empirical content by
  itself.
- **Bridge premises:** "definable-from-causal-structure ⇒ non-conventional" is
  an interpretive step the critics contest.
- **Domain restrictions:** fixed observer worldline; fixed definability
  notion; Besnard's follow-up (`seed-besnard-simultaneity`, abstract) explores
  definability vs broader coordinate freedom — hypotheses unextracted.

### N03 — Putnam/Rietdijk block-universe argument (SR + bridge premises)
- **Model/version:** N01 kinematics + Putnam's ontological thesis "all and
  only things that exist now are real" (p.241) + principle III ("There Are No
  Privileged Observers", pp.241–242) + transitive closure of "simultaneous in
  x's coordinate system" + abundance of observers/fields (pp.246–247).
  Conclusion drawn: no consistent past/present/future ontological difference;
  block view.
- **Sources:** `found-putnam` (full-text, partial pp.241–247 as audited),
  `found-rietdijk` (abstract; primary argument unverified),
  `found-stein-1991` (full-text, rebuttal), `knowledge/foundations/audit.md`
  (second-pass audit).
- **Ontology:** eternalist block — reached **only via the bridge premises**;
  the geometry alone does not force it (audit's explicit correction).
  Distinct from determinism and from truth-value determinacy (audit Sec. 2).
- **Failure modes / domain:** Rietdijk's steps unverified [paper-claim only];
  Stein rejects the global-present reading of frame simultaneity (pp.151–152).
  See D03.
- **Observables / empirical status:** none — metaphysical argument over
  kinematics.

### N04 — Stein local (event-relative) becoming
- **Model/version:** time-oriented Minkowski; candidate "definite as of"
  relation `R(a,b)` with requirements (i)–(iv): here-now base point,
  transitive propagation, reflexivity, and at every point some states remain
  unsettled (pp.148–150); geometrically, all points of `a`'s causal past
  count as definite. Under the full contextual premises, `R` is forced to be
  the causal-past relation. **[theorem, as-recorded with the audit's
  reconstruction — the OCR'd isolated p.150 statement is false as printed;
  countermodels are in `knowledge/checks/correspondence-cases.jsonl`
  cases 1–2]**
- **Sources:** `found-stein-1991` (full-text),
  `knowledge/foundations/audit.md`, `found-stein-1968` (discovery lead),
  `found-maxwell-1993` (full-text, dissent — D01).
- **Ontology:** permits event-relative becoming/open future without a global
  present [paper-claim]; whether `R` is "already become" is a bridge choice
  Stein himself flags as not settle-able by mathematics (p.150).
- **Domain restrictions:** time orientation assumed; GR analogue
  underdeveloped (p.159); conformal vs metric unit assumption removable
  (p.150). Not a proof of objective passage.
- **Precision note (from audit):** the two ablated-premise countermodels
  (universal `R`; reflexive strictly-timelike past) are exactly the checks
  cases — they refute the isolated transcription, not Stein's contextual
  argument.

### N05 — Brading's law-constitutive presentism
- **Model/version:** SR kept complete for spacetime structure; ontological
  unity of the real supplied by physical laws (law-constitutive approach)
  instead of a spacetime simultaneity surface; spacetime recast as an
  *epistemic* principle of unity (pp.1101, 1104, 1110 as inspected).
- **Sources:** `found-brading` (abstract) + `seed-brading-presentism`
  (abstract) + `knowledge/foundations/audit.md` Sec. 4 (selective text
  check; record remains abstract-depth).
- **Ontology:** presentism-compatible-with-SR [paper-claim]; explicitly a
  programmatic empirical hypothesis, **not** a demonstrated discriminating
  prediction (audit: no quantitative protocol in inspected passages).
- **Observables / empirical status:** none extracted; see N06 for what a
  testable version would have to name.
- **Bridge premises:** identification of law-grounded unity with presentness
  is the bridge; unquantified.
- **Connections:** X19 (to N06) — currently no explicit map; labeled
  conjectural/incomplete.

### N06 — Preferred-structure empirical constraints (SME data tables)
- **Model/version:** effective-field-theory coefficients for Lorentz/CPT
  violation, compiled and bounded against experiments (2026 edition of the
  Data Tables; v19 record).
- **Sources:** `seed-lorentz-data-2026` (abstract).
- **Role in map:** the empirical-status anchor for any node that posits
  physically coupled preferred structure (e.g., a testable descendant of N05).
  Constraints apply to *specified observable coefficients only*; an
  empirically hidden preferred structure is not excluded by them [record
  limits].
- **Ontology:** none — measurements constrain models, not ontologies.

### N07 — Strong growing-block / moving-spotlight formulations (NOT YET MAPPED)
- **Model/version:** deliberately left as an open family: Broad's growing
  block, Prior's tense-logical treatments, Deasy's moving-spotlight critique.
- **Sources:** `found-broad-1923`, `found-prior-2009`, `found-deasy-2015`
  (all discovery), `found-wuthrich-callender` (abstract, causal-set becoming
  angle). Read depths forbid node-level ontology/dynamics claims; the family
  is registered to keep the map broad without fabricating content.
- **Open:** the growing-block epistemic-access objection and strongest
  formulations remain unextracted (audit "remaining" list). Feeding task:
  future lane expansion.

---

## Cluster B — Causal sets

### N08 — Classical sequential growth (Rideout–Sorkin)
- **Model/version:** locally finite partial orders generated by stochastic
  birth of elements; transition probabilities subject to covariance
  (discrete general covariance), Bell causality and locality conditions
  [paper-claim at abstract depth].
- **Sources:** `seed-causal-growth` = `frontier-causal-growth-1999`
  (abstract), plus `frontier-causal-becoming-2015` (abstract; philosophical
  analysis `1502.00018`).
- **Ontology:** none established. Growth is a model premise; "becoming" is an
  interpretation contested by the Wüthrich–Callender analysis [abstract
  depth]. Stochastic growth ≠ indeterminism in every interpretation; growth
  ≠ objective passage (record limits + standards).
- **State space / dynamics / clocks:** posets + Markov growth dynamics; no
  clock construction; causal order is the primitive.
- **Observables / empirical status:** growth-probability invariants; no
  empirical program established at this depth.
- **Connections:** X20 (to N09, conjectural orthogonality), X21 (to N04,
  disagreement over becoming).

### N09 — Well-conditioned causal-set embedding uniqueness
- **Model/version:** maps from causal sets into Lorentzian manifolds under
  the authors' "well-conditioned" definition; uniqueness result stated
  [paper-claim, abstract only; conditions not extracted].
- **Sources:** `frontier-causal-embedding-2026` (abstract; 2607.05840v1).
- **Ontology:** none; order→geometry reconstruction constrains geometry
  recoverable from causal structure, not passage or a preferred present.
- **Domain restrictions:** theorem wording unextracted; may be orthogonal to
  growth dynamics (X15) since it concerns embeddings, not birth histories.

---

## Cluster C — Relational quantum clocks (constrained quantum dynamics)

### N10 — Page–Wootters with clock–system interaction (Smith–Ahmadi)
- **Model/version:** tensor-product clock C / system S; self-adjoint
  interaction; constraint `H = H_C + H_S + H_int`. Conditional state obeys
  `i d/dt psi_S(t) = H_S psi_S(t) + integral K(t,t') psi_S(t') dt'` with
  `K(t,t') = <t|H_int|t'>` (Eqs. 4–27 as recorded); norm constancy follows
  from the chosen time-independent physical inner product; Dyson-like
  perturbative series; gravity and periodic-qubit-clock examples.
- **Sources:** `frontier-smith-ahmadi-interacting-2019` (full-text;
  arXiv:1712.00081v3; Quantum 3, 160 (2019)).
- **Ontology:** none; conditional-time description, not passage.
- **Domain restrictions:** specific conditioning construction + stated inner
  product choice; does **not** prove the trinity equivalence (N11) for
  interacting covariant-POVM clocks.
- **Connections:** X01 (to N11), X05 (to N18), X17 (to N15).

### N11 — Relational trinity, free nonrelativistic clock (Höhn–Smith–Lock)
- **Model/version:** kinematical clock/system partition; autonomous
  constraint `C_H = H_C + H_S ≈ 0`, **no interaction** (Sec. II.2; App. A);
  clock time a covariant rank-one POVM `E_T(dt) = mu dt |t><t|`; clock states
  may be nonorthogonal/overcomplete; spectra `R`, half-line, bounded interval
  (Eqs. 13–16). Theorems 1–6: Dirac observables, PW conditional Schrödinger,
  and quantum symmetry-reduced relational Heisenberg descriptions equivalent
  under these hypotheses. **[theorem, as-recorded, full-text lane read]**
- **Sources:** `frontier-relational-trinity-2019v3` (full-text;
  arXiv:1912.00033v3; PRD 104, 066001 (2021)).
- **Ontology:** none — equivalence of *descriptions*; the paper's own
  conclusion flags clock–system interactions as the major open extension.
- **"Non-ideal" scope (corrected by frontier second pass):** nonorthogonal
  covariant POVMs and restricted spectral support ARE included; arbitrary
  degenerate spectra, arbitrary POVMs, and interactions are NOT.
- **Connections:** X01, X02, X03, X18.

### N12 — Relativistic trinity with frequency sectors (Höhn–Smith–Lock)
- **Model/version:** constraint `C_H = s p_t^2/2 + H_S ≈ 0`, `s = ±1`
  (Eq. 10); doubly degenerate `p_t`; decomposition into frequency sectors
  `sigma = ±` (Eqs. 11–12); sector POVM states (Eqs. 25–29); equivalence
  proved **per sector** (Thms. 1–2, Sec. V); sector-dependent normalization
  incl. factor 1/2; conditional probabilities must respect sector
  localization — mixing sectors can spoil normalization (Sec. VI).
  **[theorem, as-recorded, full-text lane read]**
- **Sources:** `frontier-relativistic-trinity-2020v1` (full-text;
  arXiv:2007.00580v1; Frontiers in Physics 9 (2021), 10.3389/fphy.2021.587083).
- **Ontology:** none; clock time and frequency-sector bookkeeping are
  descriptive structure.
- **Domain restrictions:** uncoupled split; quadratic clock momentum; no
  cross-sector frame-change invertibility; turning points and interacting
  clocks unresolved.
- **Connections:** X02 (from N11), X07 (to N17, conjectural).

### N13 — Periodic-clock relational trinity (Chataignier–Hoehn–Lock–Mele)
- **Model/version:** relational dynamics relative to periodic clocks,
  classical and quantum; clock-neutral / PW / relational-Heisenberg
  equivalence for periodic clocks via partial group averaging over one
  cycle; quantum observables invariant only for periodic quantities
  (transient per-cycle invariance otherwise; winding numbers do not yield
  invariants); original PW conditional probabilities **fail for continuous
  system energy spectra** and are updated; periodic evolution w.r.t. periodic
  clock can be monotonic w.r.t. an aperiodic clock. **[paper-claim, abstract
  read by this worker]**
- **Sources:** `map-periodic-clock-trinity-2026v3` (abstract;
  arXiv:2409.06479v3; NJP 28 (2026) 034504).
- **Ontology:** none claimed; explicitly keeps periodic/aperiodic clock
  parameterizations consistent without passage.
- **Domain restrictions:** abstract-level; theorem hypotheses unextracted;
  treated here as a falsifier lead for X03 and RC-1/RC-3, not as verified.
- **Connections:** X03 (to N11, conjectural bridge), X09 (conditioning-
  update bridge toward N10/N14).

### N14 — PW with gravitational-decoherence interaction + quasi-ideal clock (Mendes–Brito–Soares-Pinto)
- **Model/version:** Page–Wootters mechanism; clock–system interaction of the
  gravitational-decoherence type; clock model: quasi-ideal clock (approximate
  canonical time-energy algebra); reported result: **non-linear**,
  initial-condition-dependent equation of motion for the conditioned mixed
  state. **[paper-claim, abstract read by this worker]**
- **Sources:** `map-pw-quasi-ideal-2021v1` (abstract; arXiv:2107.11452v1).
- **Ontology:** none.
- **Audit target:** the precise sense of "non-linear" (state-dependent
  generator vs norm/postselection artifact) is unextracted; contrasts with
  N10's linear kernel — see X04 and RC-5.
- **Connections:** X04 (to N10, explicit difference, mechanism unextracted).

### N15 — Relational (non-)Markovianity proposal (Nandi–Petruccione-type, 2026)
- **Model/version:** clock-conditioned open-system dynamics; claims about
  exact Markovianity once time is relational [paper-claim, abstract].
- **Sources:** `frontier-relational-markov-2026` (abstract;
  arXiv:2606.08595v1) + `knowledge/COORDINATOR_REVIEW.md` audit questions
  (instrument Eqs. 5–7 vs supplemental clock-controlled interaction Eqs.
  23–31; which non-Markovianity notion; postselection vs linear channel;
  second-order vs exact).
- **Ontology:** none; internal to open-system dynamics.
- **Status:** under coordinator audit (D08); not accepted as established.
- **Connections:** X17 (to N10).

### N16 — Unitarity relative to a dynamical local observer's clock (2026)
- **Model/version:** observer-clock comparisons in fixed-background vs
  dynamical-gravity settings; claims about (non)unitarity relative to the
  local clock [paper-claim, abstract only, unextracted].
- **Sources:** `frontier-local-observer-unitarity-2026` (abstract;
  arXiv:2608.16762v1).
- **Ontology:** none extracted.
- **Connections:** X18 (to N11, conjectural).

---

## Cluster D — Quantum reference frames and causal order

### N17 — Spacetime QRFs and superpositions of proper times (Giacomini–Castro-Ruiz–Brukner-type anchor)
- **Model/version:** spacetime quantum reference frames; superpositions of
  proper times [paper-claim, abstract].
- **Sources:** `seed-qrf-proper-times` = `frontier-spacetime-qrf-2021`
  (abstract; arXiv:2101.11628).
- **Ontology:** none established; proper-time superposition is not passage
  (record limits).
- **Connections:** X07 (conjectural normalization/coherence parallel with N12).

### N18 — Temporal QRF measurement events: TO vs PM (Baumann–Lock)
- **Model/version:** clock Hilbert space `L^2[-E,E]` with bounded clock
  energy; two protocols: **TO** (twirled/covariant observables + external
  measurement) vs **PM** (ancilla + clock-triggered interaction `K_SA(t)` in
  the constraint). For ideal clocks the two agree on multi-time predictions;
  for finite-spectrum clocks PM conditioning is generally time-nonlocal
  (memory-kernel) and may be nonunitary; a finite/discrete-time construction
  restores unitarity for general measurement interactions. **[paper-claims
  from full-text lane read]**
- **Sources:** `frontier-page-wootters-measurements-2023` (full-text;
  arXiv:2308.10967v1).
- **Ontology:** none — operational event notions differ between protocols
  (D06); finite clock spectra do not imply fundamental discreteness.
- **Connections:** X05 (to N10), X06 (to N19).

### N19 — QRFs beyond tensor-factor subsystems (Ludescher–Mekonnen–Galley–Müller)
- **Model/version:** perspective-neutral QRFs generalized to covariant
  **instruments**, finite-dimensional Hilbert spaces + compact Lie groups
  (framework premises); App. B.1: interacting conditioned equation with
  kernel `K(t,t') = (<t| x 1) H_int (|t'> x 1)`; finite Abelian example
  `C = P1 + P2 + K(X1 - X2)^2` with physical states `|d; K d^2>` — the
  first-particle frame yields no autonomous generator, while the
  center-of-mass (non-local) frame decouples relative-coordinate evolution.
  **[theorem for the stated finite model, full-text lane read]**
- **Sources:** `frontier-qrf-beyond-subsystems-2026` (full-text;
  arXiv:2607.24976v1).
- **Ontology:** none — representation change alone changes no observable
  prediction; the record says so explicitly.
- **Domain restrictions:** continuous-`R` example lies outside the
  finite/compact framework and ignores normalization (recorded); the finite
  example does not characterize all interactions.
- **Connections:** X06 (to N18), X08 (kernel parallel to N10).

### N20 — Time delocalization across temporal QRFs (2026)
- **Model/version:** relational evolution from clock–system correlations;
  causal/temporal relations across temporal QRF changes [paper-claim,
  abstract; derivation unread].
- **Sources:** `frontier-time-delocalization-2026` (abstract;
  arXiv:2603.08845v1).
- **Ontology:** none established; frame-dependent event localization must not
  be conflated with fundamental indefinite order (record limits).
- **Connections:** X10 (conjectural, to N21).

### N21 — Indefinite causal order and quantum coordinates (de la Hamette–Kabel–Christodoulou–Brukner)
- **Model/version:** a relativistic causal-order observable for
  operationally defined events; authors report it does **not** distinguish
  the optical-bench quantum switch from the gravitational quantum switch
  (superposed gravitational fields), supporting their thesis that both
  realize indefinite causal order equally. **[paper-claim, abstract read by
  this worker; PRL 135, 141402 (2025)]**
- **Sources:** `map-indefinite-order-quantum-coordinates-2025v3`
  (abstract; arXiv:2211.15685v3).
- **Ontology:** authors argue for parity of "realization" theses; this map
  records the sharper operational content: their observable cannot tell the
  two implementations apart — an invariance claim to audit, not settled
  metaphysics.
- **Connections:** X10 (to N20), X11 (to N22).

### N22 — Bell-type temporal-order correlations
- **Model/version:** device-independent-style route to challenging classical
  temporal order under specified assumptions [paper-claim, abstract].
- **Sources:** `seed-bell-temporal-order` (abstract; arXiv:1708.00248).
- **Ontology:** none; a theoretical proposal, not a realized
  gravity-mediated experiment (record limits).
- **Connections:** X11 (to N21, conjectural: whether the Bell-type
  correlations and the N21 observable track the same operational property).

### N23 — Operational meaning of QRFs (2026)
- **Model/version:** conceptual/operational analysis of what QRF claims mean
  [abstract].
- **Sources:** `frontier-qrf-operational-meaning-2026` (abstract;
  arXiv:2607.03417v1).
- **Role:** access-condition vocabulary for X06/X10; content unextracted.
- Also registered: `frontier-canonical-clock-sectors-2026` (discovery; title
  only, excluded from ranking per lane caution) and
  `frontier-qrf-indefinite-order-2022v3` — now superseded by this map's N21
  record of the same paper at abstract depth.

---

## Cluster E — Thermal time, thermodynamic clocks, records

### N24 — Thermal time hypothesis (Connes–Rovelli)
- **Model/version:** generally covariant algebraic quantum theory; modular
  automorphism flow of a von Neumann algebra in a given state proposed as
  time flow [paper-claim/hypothesis; full text opened, formulas NOT
  transcribed by the lane].
- **Sources:** `frontier-thermal-time-original-1994` (full-text access,
  no formula extraction; gr-qc/9406019; CQG 11 (1994) 2899).
- **Ontology:** none established; the flow is state-dependent and its
  physical identification is the open bridge question (record open question).
- **Connections:** X12 (to N28), X13 (to N26/N27 — contested).

### N25 — Thermal clocks and relationalism (Menicucci–Olson–Milburn)
- **Model/version:** statistical state `rho` over a large finite quantum
  system; local subsystem clock protocols; derived clock consistency
  condition reported operationally equivalent to the Tolman–Ehrenfest
  relation **without assuming gravity/metric**; independent thermality is an
  extra assumption. **[paper-claim, full-text lane read]**
- **Sources:** `frontier-thermal-clock-relational-2011` (full-text;
  arXiv:1108.0883v1).
- **Ontology:** none; candidate TTH flow vs ordinary physical time is kept
  distinct by the authors.
- **Open (recorded):** can a finite thermal clock operationally distinguish
  its modular parameter from calibrated lab time after rescaling freedoms?
- **Connections:** X14 (conjectural, to N28).

### N26 — Realization modes of thermal time (Martinetti–Rovelli)
- **Model/version:** observer/field examples where the modular flow is
  geometrical, partially geometrical, or non-geometrical; identification of
  algebra, geometric flow, and state-dependence left open. **[authors'
  analyses, full-text lane read]**
- **Sources:** `frontier-emergence-time-qg-2012` (full-text;
  arXiv:1203.4995v1).
- **Ontology:** none; explicitly not a theorem that time emerges.
- **Connections:** X13 (contested with N27).

### N27 — Chua's circularity critique of strong TTH
- **Model/version:** analysis of the strong TTH reading (faithful normal
  states; KMS equilibrium grounding dynamics): argues modular flow is
  mathematically defined but not automatically physical time; equilibrium's
  usual characterization presupposes time. **[authored philosophical
  argument, full-text lane read]**
- **Sources:** `frontier-thermal-time-concept-2024` (full-text;
  arXiv:2407.18948v1).
- **Ontology:** negative claim against one strong reading (D04); weaker
  relational/operational variants remain live.
- **Connections:** X13 (contested with N26/N24).

### N28 — Thermodynamics of clocks (Milburn)
- **Model/version:** open nonequilibrium clock models; Gibbs–Boltzmann
  steady state; jump-process clock readings; high-rate "good clock" limit
  produces a flow analogous to thermal-time dynamics; finite clock rate
  gives intrinsic decoherence corrections (Sec. 5.2, Eqs. 94–99). **[model-
  specific result, full-text lane read]**
- **Sources:** `frontier-thermodynamics-clocks-2020` (full-text;
  arXiv:2007.02217v1).
- **Ontology:** none; author's irreversibility reading of clocks is not the
  thermodynamic arrow as ontology (record limits).
- **Connections:** X12 (explicit analogy to N24 within the stated model),
  X14 (conjectural with N25).

### N29 — Decoherent histories from records (Hartle)
- **Model/version:** closed-system consistent/decoherent histories; records
  = correlations in a final state; probabilities require decoherence
  consistency; no moving present posited. **[framework, full text opened;
  math not extracted]**
- **Sources:** `frontier-records-histories-2016` (full-text access;
  arXiv:1608.04145v1).
- **Ontology:** none; records support inference, not passage (record limits).
- **Connections:** X15 (disagreement D05 with N30).

### N30 — No time asymmetry from quantum mechanics (Page)
- **Model/version:** comparison of time-asymmetric decoherence functionals
  vs time-symmetric formulations; challenges inferring fundamental time
  asymmetry from records/histories alone; contingent boundary conditions
  matter. **[author argument, full text opened; not fully reconstructed]**
- **Sources:** `frontier-records-time-asymmetry-1993` (full-text access;
  gr-qc/9304027).
- **Ontology:** none; an adversarial predecessor against conflating records,
  thermodynamic arrow, and passage.
- **Connections:** X15 (D05).

### Cluster E coverage leads (not nodes)
`frontier-thermal-noncommutative-2025` (abstract; deformed-spacetime TTH
application — algebra/state/modular details unextracted) and
`frontier-emergent-spin-glass-2025` (discovery; relevance to temporal
ontology unclear) are registered leads only. `seed-problem-of-time`
(abstract; review, arXiv:1206.2403v2) is the routing node for canonical-
quantum-gravity problem-of-time issues, which this map otherwise does not
expand (no dedicated node; see gaps).

---

## Cluster F — Formalization anchors (reuse, not ontology)

### N31 — Lean/Isabelle formalization infrastructure
- **Model/version:** Physlib (Lean; `MState.lean` pinned to commit
  `67d742760382efce9419feefa348902aab797a07`; POVM and MinkowskiMatrix
  inspected at mutable `master`); Isabelle/HOL Schutz axiomatization (locale
  hierarchy; strengthened symmetry reading; `MinkowskiDense`; continuity
  omitted); Isabelle/HOL Stannett–Németi "no FTL observer" proof; AxQM
  benchmark library (main-branch `sorry` by design).
- **Sources:** `form-physlib`, `form-physlib-mstate-code`,
  `form-physlib-povm-code`, `form-physlib-minkowski-code`,
  `form-isabelle-schutz`, `form-isabelle-special-relativity`,
  `form-afp-schutz-outline`, `form-axqm`, `seed-physlib`,
  `seed-isabelle-relativity` (depths as recorded; three Physlib records
  code-audited at declaration level by the formalization lane; **no local
  build or kernel replay has run anywhere in this project**).
- **Role:** any research contract's certificate route (RC-2, RC-4) must map
  statements onto these bases only after dependency/`#print axioms` audits
  (per `knowledge/formalization/reuse-map.md`).
- **Ontology:** none; a proof assistant checks encoded statements only.

### N32 — Machine-assisted methods and audit pattern
- **Model/version:** audited AI-formalization workflows (Seiberg–Witten
  formalization with physical axioms + oracle checks; convention-fixing
  methodology). Records at full-text depth in the methods lane.
- **Sources:** `meth-sw-lean-2026`, `meth-diagrammatica-2026`.
- **Role:** verification strategy for the map's contracts (freeze versions,
  provenance sweep, oracle + adversarial pass), per
  `knowledge/methods/handoff-contract.md`.

---

## Edge list (graph index)

| Edge | From → To | Type | Where |
|---|---|---|---|
| X01 | N10 ↔ N11 | partial map (equivalence boundary) | translations.md |
| X02 | N11 ↔ N12 | explicit sector decomposition map | translations.md |
| X03 | N11 ↔ N13 | **conjectural** spectral-class bridge | translations.md |
| X04 | N10 ↔ N14 | recorded difference; mechanism unextracted | translations.md |
| X05 | N18 ↔ N10 | explicit protocol/interaction map (partial) | translations.md |
| X06 | N18 ↔ N19 | **conjectural** operational comparison | translations.md |
| X07 | N12 ↔ N17 | **conjectural** coherence/normalization bridge | translations.md |
| X08 | N19 ↔ N10 | explicit kernel parallel (stated in N19 App. B.1) | translations.md |
| X09 | N13 ↔ N10/N14 | **conjectural** conditioning-update bridge | translations.md |
| X10 | N20 ↔ N21 | **conjectural**; invariance constrains delocalization | translations.md |
| X11 | N21 ↔ N22 | **conjectural** observable-vs-correlation bridge | translations.md |
| X12 | N24 ↔ N28 | explicit model-level analogy (N28 Sec. 5.2) | translations.md |
| X13 | N24 ↔ N26 ↔ N27 | contested connection (D04) | disagreements.md |
| X14 | N25 ↔ N28 | **conjectural** unification of clock operationalizations | translations.md |
| X15 | N29 ↔ N30 | disagreement (D05) | disagreements.md |
| X16 | N02 ↔ N03 ↔ N04 | explicit same-substrate structure contrast | translations.md |
| X17 | N15 ↔ N10 | audit target (D08) | disagreements.md |
| X18 | N16 ↔ N11 | **conjectural**, pending extraction | translations.md |
| X19 | N05 ↔ N06 | no map yet; **conjectural/incomplete** | translations.md |
| X20 | N08 ↔ N09 | **conjectural** orthogonality | translations.md |
| X21 | N08 ↔ N04 | **disagreement** (becoming vs representation), see D07 | disagreements.md |
| X22 | N31/N32 ↔ all | method edge: certificates check encodings only | translations.md |

(Edge numbering matches `translations.md`; X13, X15 and X17 are recorded
directly in `disagreements.md` as D04, D05 and D08 respectively.)

**Explicit non-ranking statement:** this map records commitments,
equivalences, and failures. It assigns no weights, scores, or truth ranks to
ontologies, and it treats agent votes, citation counts, and any composite
"truth score" as non-evidence (project research standards).
