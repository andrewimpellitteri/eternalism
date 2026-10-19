# ICO vs process matrices vs temporal QRFs — anchor comparison

Lane: kb-ico-qrf. Date: 2026-10-19. All five anchors below were read at
`full-text` depth in this session (exact versions and locators in
`sources.jsonl`; the four arXiv anchors reuse the frontier lane's IDs).
Source records tagged `discovery` in sources.jsonl are leads only and are
marked as such wherever used.

Unit of comparison, per the knowledge-base contract: a particular
model/version plus interpretation, not a broad label. Labels below:

- **A** — de la Hamette, Kabel, Christodoulou, Brukner, arXiv:2211.15685v3
  (PRL 135, 141402, 2025). Quantum-coordinate ICO.
- **B** — Hausmann, Schmidhuber, Castro-Ruiz, arXiv:2308.10967v1 (published
  Quantum 9, 1616, 2025). Twirled-observable vs purified-measurement events
  with non-ideal clocks.
- **C** — Baumann, Lock, arXiv:2603.08845v1 (2026). Causality across
  temporal QRFs (Page-Wootters, two clocks).
- **D** — Vanrietvelde, arXiv:2607.03417v1 (2026). Operational meaning of
  QRFs (position QRFs only).
- **E** — Oreshkov, Costa, Brukner, arXiv:1105.4464v3 (Nat. Commun. 3, 1092,
  2012). Process-matrix baseline.

---

## 1. Comparison contract, filled per anchor

### A. Quantum-coordinate ICO (2211.15685v3)

1. **What exists.** A global state that is a superposition of two
   semi-classical spacetimes `α|1⟩|g(1)⟩ + β|2⟩|g(2)⟩` (Eq. 3), with events
   defined as worldline coincidences and extended across branches by
   `ℰ_X^(1)=ℰ_X^(2)≡ℰ_X` (Eq. 4). Passage is not a primitive; nothing in the
   paper asserts or denies objective becoming. The future being "fixed" is
   not at issue: each branch is a classical solution; indefiniteness lives in
   the quantum state, not in an open future.
2. **State space, dynamics, causal structure, clocks.** Kinematics: branches
   labelled by a control qubit; per branch, `(ℳ_i, g^(i))` globally hyperbolic,
   timelike curves γ0, γA, γB with single crossings. Dynamics: geodesic/curved
   motion assumed, not solved. Causal structure: per-branch sign
   `s^(i)=sign(Δτ)` of the proper-time difference along γ0 (Def. 1, Eq. 2).
   Clock: the test particle's proper time, made operational by spin precession.
3. **Symmetries, access, boundaries.** Symmetry group: classical
   diffeomorphisms per branch, and *quantum diffeomorphisms*
   `|1⟩⟨1|⊗𝒰1 + |2⟩⟨2|⊗𝒰2` (Eq. 7) — a quantum-controlled, branch-wise change
   of quantum coordinates. Observer access: agents in labs A, B perform
   non-disturbing measurements tuned to proper times τ1*, τ2* (Sec. on the
   operational encoding). Boundary conditions: endpoints of γ0 fix the time
   orientation.
4. **Observables and empirical status.** Observable: `s^(1)s^(2)` (definite
   +1, indefinite −1; generalization to N events / M branches by pairwise
   products, footnote 2). Encoding: state (12) `|ψ⟩=α|s=+1⟩+β|s=−1⟩`;
   σx, σy, σz tomography distinguishes coherent ICO from classical mixtures
   (App. B, Fig. 4). Empirical status: no experiment performed in the paper;
   relation to existing optical-switch experiments is interpretive (their
   claim). Consequence claimed by the authors: the optical and gravitational
   quantum switch realize the *same* ICO observable; ICO realization does not
   certify a superposition of metrics (curvature still distinguishes them).
5. **Bridge premises and alternative readings.** Premise: coincidences of
   worldlines across branches are "the same event" (Eq. 4) — an extension of
   the hole-argument-safe coincidence philosophy; Kabel et al. 2025 later
   formalize the needed cross-branch comparison map (App. A remark). The
   state (Eq. 3) is heuristic (footnote 1). Alternative reading: one could
   refuse branch-identity of events, making "event count" branch-relative —
   the paper shows event *localization* is already quantum-coordinate
   dependent, which supports its reading.
6. **Known equivalences, contradictions, restrictions.** Consistency with
   Vilasini–Renner Corollary 1 (PRA 110, 022227) claimed. Analogy with
   Castro-Ruiz–Giacomini–Brukner PRX 8, 011047 (order preserved under
   continuous reversible transformations) is asserted, not derived. Domain
   restriction: single crossings only; branch count finite; metric states
   semi-classical and (nearly) orthogonal.

### B. TO vs PM events with non-ideal clocks (2308.10967v1)

1. **What exists.** A Page-Wootters constraint `Ĥ|Ψ⟩=0` with a clock C
   (bounded spectrum [−E,E]), a system S and measurement ancillas; two
   operational definitions of "measurement event": externally ordered twirled
   observables (TO) vs clock-triggered dynamical interactions inside the
   constraint (PM). Passage/determinism: global state static ("timeless");
   non-unitarity of PM evolution for finite E is effective (resource-caused),
   not a fundamental indeterminism — the discrete-time variant restores
   unitarity.
2. **State space, dynamics, causal structure, clocks.** Kinematical
   `ℋ_C⊗ℋ_S⊗ℋ_A`; ideal clock = `|t⟩` continuum; non-ideal = covariant POVM
   `|φ_t⟩`, overlap sinc (Eqs. 2–6). TO dynamics: unitary, externally ordered
   (Eqs. 8–11). PM dynamics: constraint (12), non-ideal (15); conditional
   evolution Eq. (16) with memory kernel `F(t)` (Eq. 17) — time-non-local,
   generally non-unitary (footnote 2). Causal structure: not fundamental;
   "temporal order of events" is the order of clock-triggered measurement
   interactions.
3. **Symmetries, access, boundaries.** TO observables are invariant under the
   constraint flow (twirl, Eq. 9). Access: TO = an experimenter with external
   ordering power ("infinite resources", Sec. IV.2.4); PM = an internal
   observer who acts when her clock reads a value. Limit `E→∞` then
   instantaneous interaction, *in that order*.
4. **Observables and empirical status.** Ideal-clock multi-time probabilities
   identical in TO and PM (App. D, Eqs. 55–66). Non-ideal: modified
   probability rule (Eq. 14, non-trivial denominator); cross-order term
   survives even with disjoint measurement supports (Sec. IV.2.3, Eqs. 19–20,
   Fig. 3) → "fundamental limitation to the operational definition of the
   temporal order of events". No experiment; authors' discrete-time
   conclusion is a conditional claim ("if ... then time has to be discrete"),
   not evidence about fundamental time.
5. **Bridge premises.** "Measurement event" = clock-conditioned interaction
   (PM) vs externally chosen invariant operation (TO). The authors argue the
   two describe *different physical situations* off the ideal limit; an
   alternative reading (their App. F) is PM = TO with a restricted,
   time-non-local operator class. Process-matrix relevance is flagged
   (refs [32]–[34]) as a possibility, not derived.
6. **Equivalences, contradictions, restrictions.** Equivalence TO≡PM proved
   for ideal clocks only. Non-ideal TO reproduces standard QM for a
   sufficiently good clock (Höhn-Smith-Lock condition). Restriction: H_S=0 in
   the conceptual core; perturbative solution assumed convergent; no
   interaction with gravity modeled, only motivated.

### C. Causality across temporal QRFs (2603.08845v1)

1. **What exists.** Page-Wootters with two ideal clocks C1, C2, system S =
   A,B,(ancillas). Static global state ("block universe picture" in the
   abstract); evolution, time direction, and event timing are all relative to
   a chosen clock. Passage: not fundamental. Determinism: constraint dynamics
   is unitary; apparent non-unitarity would come only from clock-system
   interactions of the non-ideal kind (explicitly distinguished from the
   delocalization studied here).
2. **State space, dynamics, causal structure, clocks.** Kinematical
   `⊗_i ℋ_Ci ⊗ ℋ_S`; constraint `Ĉ=Σ Ĥ_Ci + Ĥ_rest` (Eqs. 11, 43); physical
   states by group averaging δ(Ĉ) (Eq. 5). Conditional dynamics relative to
   Ci is Schrödinger-like under stated commutator conditions. Clocks: ideal,
   with necessary time delocalization φ(t2) between them (Sec. III: perfect
   synchronization gives δ(0) divergence → non-normalizable).
3. **Symmetries, access, boundaries.** Transformation rules (see §2 below).
   Access: interventions must be *in the constraint* (Eq. 48/56 form) for
   subsystem-locality to survive frame changes; choosing alternative
   histories (solutions) does not survive (Sec. V.2, Eqs. 45–47).
4. **Observables and empirical status.** Frame-invariant: signaling relations
   and intervention/no-intervention probabilities (App. B: `p_|C1 = p_|C2`).
   Frame-dependent: which operation appears time-delocalized (Fig. 6);
   direction of time only approximately (Eqs. 25–31, footnote 3 — the
   thermodynamic arrow is discussed as *unlikely to be frame-disputed*, an
   explicit speculation). ICO: constraint (68) with each clock timing one
   intervention, τa=τb, bimodal φ(t2) → both orders contribute in *both*
   frames; equals the causal reference frame decomposition of the quantum
   switch; both frames agree the order is indefinite (Discussion, citing
   anchor A). Empirical status: none; toy construction.
5. **Bridge premises.** Operational causality = signaling between quantum
   operations (Eqs. 32–36), explicitly distinguished from relativistic
   light-cone/microcausality notions (Intro). The relational switch's control
   is a *choice of physical state* (φ(t2)), which the authors contrast with
   Castro-Ruiz et al. 2020 where a gravitating mass is the "physical" control.
6. **Equivalences, contradictions, restrictions.** Restricted to ideal clocks
   (their App. C method breaks otherwise; non-ideal case = anchor B's
   Quantum 9, 1616 paper). Equivalence to trinity/Dirac-observable approaches
   with interactions is left open by the authors. With sharply peaked φ and
   well-separated timings, order is definite and *the same* in both frames
   (Sec. VI.3) — frame-dependent order is the exception, not the rule.

### D. Operational meaning of QRFs (2607.03417v1)

1. **What exists.** A specification of what "relative to a QRF" means:
   measurements performed inside a lab whose absolute position may be
   superposed. No ontology of passage or openness at stake; explicitly no
   stance on the measurement problem (register internals may sit outside the
   Heisenberg cut).
2. **State space, dynamics, causal structure, clocks.** Factorization
   `|x0⟩+|x1⟩)_abs ⊗ |φ⟩_int` (Eqs. 1–3); outcome registers' *internal*
   states carry outcomes (Sec. 3.1); no dynamics, no causal structure, no
   clock in the paper. Temporal QRFs explicitly deferred.
3. **Symmetries, access, boundaries.** The "abs/int" split is conventional:
   any constituent at fixed relative position can be the reference factor
   (App. A, Eqs. 11–12) — the operational analogue of trading one origin for
   another. Access: broadcasting protocol (Eqs. 6–10) shows outcomes are
   accessible to well-localized agents without decohering the position
   superposition.
4. **Observables and empirical status.** Proposal for what should be measured
   (roleplay argument via Ives–Stilwell / muon analogies); "quantum ruler"
   cited as a concrete instance. No new prediction.
5. **Bridge premises.** Position-superposed observers ≠ outcome-superposed
   (Wigner's friend) observers. Alternative reading criticized: Adlam 2022
   (their ref [24]) — the paper positions itself against that criticism.
6. **Equivalences, contradictions, restrictions.** No transformation laws
   given (explicitly not the aim); restricted to position QRFs; ICO appears
   only as motivation (their refs [26]–[31]).

### E. Process-matrix baseline (1105.4464v3)

1. **What exists.** Bipartite correlations `P(ℳ_i^A, ℳ_j^B)=Tr[W(M_i⊗M_j)]`
   (Eq. 3) defined by local QM alone; no spacetime, no frames, no dynamics.
   No ontology of time claimed beyond the authors' quantum-to-classical
   emergence *speculation* (Discussion).
2. **State space, dynamics, causal structure, clocks.** W ≥ 0 and normalized
   on CPTP pairs (Eqs. 4–5); Hilbert-Schmidt characterization fixes the
   allowed term types (App. .3). "Causal order" = signaling structure:
   `A ⋠ B` = no signaling from A to B; definite order ↔ one direction.
3. **Symmetries, access, boundaries.** None specified — the defining
   structural contrast: the framework has *no transformation group between
   perspectives*; each party is certain about order inside its own lab (Fig. 2).
4. **Observables and empirical status.** Causal inequality `p_succ ≤ 3/4`
   from CS+FC+CL (Eqs. 1–2, App. .1); violated by the four-qubit process
   (Eq. 7) achieving `(2+√2)/4` (Eq. 8, App. .5); all classical processes are
   causally separable (App. .6). Peer-reviewed; mathematically established;
   physical realization of inequality-violating processes remains unproven.
5. **Bridge premises.** Events = party input/output ports; "indefinite causal
   order" = causal *nonseparability* of W, i.e. no decomposition
   `W = qW^{B⋠A} + (1−q)W^{A⋠B}` (Eq. 6). Reading a definite-order mixture
   (q ∈ (0,1)) as ICO is an error the framework explicitly excludes.
6. **Equivalences, contradictions, restrictions.** Bipartite, two-use only;
   unitary-instrument special cases recover circuits, states, channels (Sec.
   "Framework"). No time parameter anywhere.

---

## 2. Transformation rules (as recorded, per anchor)

| Anchor | Transformations defined | Rule |
|---|---|---|
| A | classical diffeomorphisms; **quantum diffeomorphisms** | `|1⟩⟨1|⊗𝒰1+|2⟩⟨2|⊗𝒰2`, 𝒰_i unitary reps of `φ^(i)` (Eq. 7); fields pull back by the inverse pushforward, `g^(i)=(φ^(i))_*^{-1}(g)`; A.1: branch-wise `φ^(i)` align crossing points onto one manifold → events localized, metric value at each point superposed (Eqs. 13–16); A.2: Fermi normal coordinates along γ0 flatten each branch metric on γ0 → events delocalized (Eqs. 17–19). Applicable iff single crossings and (nearly) orthogonal branch metrics. |
| B | none between TO and PM off the ideal limit | Ideal case only: twirl (Eq. 9) and reduction maps `R̂(τ)=⟨τ|`, `R̂^{-1}(τ)=∫dt |t⟩Û_S(t−τ)` (Eq. 55) equate TO and PM probabilities (Eqs. 60–66). Non-ideal: PM probabilities are *expressible* as TO conditional probabilities with time-non-local invariant operators (App. F, Eq. 106) — a representation result, not a frame transformation. |
| C | Page-Wootters frame change | Reduction map `ℛ_i(τ_i)=⟨τ_i|⊗1` (Eq. 13); inverse `ℛ_i^{-1}(τ_i)=δ(Ĉ)|τ_i⟩⊗1` (Eq. 14); frame change `𝒮_{i→j}(τ_i,τ_j)=ℛ_j(τ_j)ℛ_i^{-1}(τ_i)` (Eq. 15); observables `𝒪_{|C_j}=𝒮 𝒪_{|C_i} 𝒮†`; naive operations become globally non-local (Eqs. 46–47); constraint-embedded interventions `δ(T̂_j−τ)⊗K` transform preserving subsystem-locality by construction (Eqs. 52, 56–57, 62, 68). Valid for ideal clocks, single constraint, given clock correlations φ(t2). |
| D | none (explicitly deferred) | Only the factor-splitting move of App. A (centre of mass ↔ any fixed-relative-position constituent). |
| E | none | Bilinearity (Eq. 3) is the whole structure; there is no perspective change in the framework. |

Cross-check with the QRF-transformations literature anchors cite
(Vanrietvelde et al. 2020; Höhn–Vanrietvelde 2020; Krumm et al. 2021):
C's `𝒮_{i→j}` is the two-clock specialisation of that machinery; A's quantum
diffeomorphisms are asserted but *not* yet cast in that formalism (authors'
stated open problem).

## 3. Frame-invariant vs frame-dependent quantities

See `invariants.md` for the per-anchor table (required deliverable), including
the smallest finite-dimensional example of each paper.

## 4. Exactly when frame-relative order differs from process-matrix indefinite order

Terminology fixed first (all four anchors + E, using their own words where
loaded):

- **PM-ICO (process matrix):** causal nonseparability of `W` — no convex
  decomposition into definite-order processes (E, Eq. 6). Operational
  certifications: violation of the causal inequality (strong; E, Eq. 8) or a
  causal-nonseparability witness (weaker; Araújo et al. 2015 — recorded at
  discovery depth). A probabilistic mixture of definite orders with q∈(0,1)
  is **not** PM-ICO (E, Sec. "Framework").
- **Frame-relative order:** the ordering of two operations/events as
  described relative to a chosen clock or quantum coordinate system. Its
  definite-vs-indefinite status is a property of the *scenario description*
  (branch signs, conditional dynamics, constraint), not of a process matrix.

They are different predicates on different objects. Precise divergences
extracted from the anchors:

1. **Order can be frame-relative while the underlying process is definite**
   (no PM-ICO of any kind).
   - A: whether *which* description applies (delocalized events vs superposed
     metric) is quantum-coordinate dependent (App. A) — including cases where
     each branch has a perfectly definite order. In C's terms, the same
     physics redescribed relative to another clock can move which operation is
     sharply timed.
   - C, App. A (Eqs. 76–79): two ideal clocks with opposite signs in the
     constraint disagree about the order of two spontaneous operations *only
     approximately and only if* the operations' Stinespring dilations are
     Hermitian (time-reversal invariant), e.g. Pauli unitaries on a qubit; and
     even then the reduced state `ρ_{S'|C2}(Δτ) ≠ ℰ_A[ℰ_B[ρ]]` exactly — the
     "disagreement" is approximate state matching, not an exact order swap.
   - Limitation (C, Sec. VI.3): for sharply synchronized clocks and
     well-separated timings, both frames assign the *same* definite order.
     Frame-dependent order is not generic in that model.
2. **Order can be frame-invariantly indefinite without any PM-ICO being
   established.**
   - C, Sec. VI.4: the relational quantum switch — each frame sees the
     operation timed by the *other* clock time-delocalized, and with τa=τb and
     bimodal φ(t2) both frames see *both* orders contributing. Both frames
     agree the order is indefinite (explicitly "in keeping with" A). But the
     indefiniteness comes from a *superposition of two history solutions*
     selected by the chosen physical state; no causal game is played and no
     process matrix is written down, so causal nonseparability is *not
     established* in the paper. The authors themselves distinguish this
     state-choice switch from the "physical" mass-in-superposition switch.
   - B, Sec. IV.2.3: with non-ideal clocks in the PM approach, measurement
     interactions with disjoint time supports still contribute in both orders
     (Fig. 3) — "indefinite temporal order of events" arising from *finite
     clock resources inside standard QM on a fixed constraint*. The authors
     flag it as possibly "relevant to" process-matrix ICO but perform no
     process-matrix analysis. This is a limitation of an operational event
     notion, categorically different from causal nonseparability (their own
     App. F recasts it as time-non-local TO observables with unitary
     evolution).
3. **PM-ICO can exist where no frame-relative statement is available at all:**
   E's framework has no perspectives, so its inequality-violating process
   (Eq. 7) has no frame-relative order description unless an embedding into
   labs/spacetime is added. The Vilasini–Renner no-gos (PRA 110, 022227; PRL
   133, 080201 — abstract/discovery depth here) then constrain *which*
   embeddings are possible; A's no-go (no quantum coordinates with localized
   events + definite metric + ICO) is consistent with them.
4. **The two notions nonetheless align on one point:** in every anchor that
   has both a frame transformation and an order predicate (A, C), the
   *definite-vs-indefinite* status of the order is invariant across frames —
   A proves it for `s^(1)s^(2)` under quantum diffeomorphisms; C verifies it
   for the relational switch. What is frame-dependent is the *source* of the
   indefiniteness (delocalized events vs superposed metrics; which operation
   is smeared), not the indefiniteness itself. This parallels (in A's words,
   without derivation) the process-matrix result that causal order is
   preserved under continuous reversible transformations (Castro-Ruiz et al.
   PRX 8, 011047 — discovery depth here; follow-up debate in Selby et al.
   2024 and arXiv:2009.10027).

**Summary predicate table.**

| Scenario | Frame-relative order | PM-ICO? | Why they differ |
|---|---|---|---|
| Optical switch on fixed metric (A's reading) | indefinite, invariantly | not analyzed in A | ICO from superposed crossings; no W written |
| Gravitational switch (A/Zych et al.) | indefinite, invariantly | not analyzed in A | same observable s^(1)s^(2) |
| Mixture q of two definite orders | definite in every branch | no (E, Eq. 6) | ignorance ≠ ICO |
| C, sharply peaked φ, well-separated timings | definite, same in both frames | not analyzed | delocalization too small to mix orders |
| C, τa=τb, bimodal φ (relational switch) | indefinite in both frames | unestablished | superposition of histories; no causal game |
| B, PM, non-ideal clock, disjoint supports | "indefinite temporal order" of PM events | unestablished | clock-resource limitation; TO recasting is unitary |
| C, App. A, opposing clocks, Hermitian dilations | approximately frame-dependent order | no | approximate state-level disagreement only |
| E, process Eq. (7) | n/a (no frames) | yes (inequality violated) | framework contains no perspective notion |

## 5. Concept discipline (ontology vs formal notions)

- **Temporal ontology / passage:** none of A–E posits objective passage. C
  calls the PW constraint a block-universe picture; D explicitly defers
  temporal questions; A and E are silent beyond branch/operational structure.
- **Objective becoming vs clock time:** "time" in B and C is a clock reading
  (covariant POVM / time operator); in A it is proper time along γ0; in E
  there is no time. These are not interchangeable.
- **Determinism:** A's motivation mentions GR determinism vs QT probability;
  B's non-unitarity is resource-effective, and its discrete model restores
  unitarity — neither supports fundamental indeterminism claims.
- **Causal order:** three distinct operationalizations coexist in the set —
  signaling (C, E, and D's background), proper-time sign (A), and
  clock-triggered interaction timing (B). Conclusions about one do not
  transfer automatically to the others.
- **Thermodynamic arrow:** only C touches it, as an explicit *speculation*
  (footnote 3) that opposing clocks are unlikely to disagree about it, via
  chaos/thermalization typicality. It is not derived, and it is kept distinct
  from clock-direction disagreement.
- **Clock time vs temporal ontology:** ideal-clock assumptions (unbounded
  spectrum) are load-bearing in B and C; relaxing them is precisely where the
  TO/PM split (B) and the open problems of C live. No ontological conclusion
  survives on ideal-clock idealizations alone.

## 6. Nearest predecessors and what would defeat a suggested gap

No novelty claims are made by this lane. The nearest predecessors, per
candidate observation someone might extract from §4:

- *"Frame-relative ICO and process-matrix ICO coincide/are equatable."*
  Predecessors: Oreshkov 2019 (Quantum 3, 206 — time-delocalized subsystems;
  discovery depth); Baumann et al. PRR 4, 013180; Guérin–Brukner NJP 20,
  103031; Apadula–Grinbaum–Brukner arXiv:2604.02873 (frame perspectives for
  process matrices — discovery depth). **Defeated if:** 2604.02873 already
  gives the frame-perspective representation of process matrices covering the
  proper-time and PW cases; or Oreshkov 2019's construction already derives
  causal nonseparability for PW-type relational switches.
- *"Order definiteness is invariant under quantum frame changes."*
  Predecessors: anchor A itself (proves it for s^(1)s^(2)); Castro-Ruiz et
  al. PRX 8, 011047 (abstract framework); Selby–Sainz–Horodecki 2024 critique.
  **Defeated if:** any of these already states the invariance for the same
  transformation class (quantum-controlled branch-wise diffeomorphisms) and
  the same order predicate (proper-time sign).
- *"Non-ideal-clock temporal indefiniteness (B) is process-matrix ICO."*
  Precedents cautioning against: B itself (App. F recasting); E (no frames).
  **Defeated if:** a witness computation on B's scenario shows causal
  nonseparability — nobody has done this in the anchors; it is an open,
  checkable question, not a gap claim.
- *"Optical vs gravitational switch equivalence."* Predecessors: A (its main
  claim), Paunković–Vojinović (Quantum 4, 275, 2020 — the opposing camp,
  discovery depth via A's refs), Zych et al. Nat. Commun. 10, 3772 (2019)
  (`seed-bell-temporal-order`). **Defeated if:** an observable outside A's
  Def.-2 class distinguishes the implementations in a way that survives A's
  own curvature caveat.
