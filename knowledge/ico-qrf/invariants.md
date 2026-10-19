# Invariants, frame-dependent quantities, and smallest finite examples

Lane: kb-ico-qrf, 2026-10-19. Companion to `comparison.md`. Every entry is
traced to a locator in the version given in `sources.jsonl`. "Paper claim" vs
"established result" vs "our observation" is marked per cell where it matters.
No novelty claims.

## Table: invariants vs frame-dependent quantities per anchor

| Anchor (version) | Frame-invariant / transformation-invariant quantities | Frame-dependent quantities | Smallest finite-dimensional example given by the paper |
|---|---|---|---|
| **A** 2211.15685v3 (PRL 135, 141402, 2025); transformations: classical and quantum-controlled branch-wise diffeomorphisms (Eq. 7) | Branch order sign s^(i); product s^(1)s^(2) (Def. 2: +1 definite, −1 ICO); proper time τ_γ0 (Eq. 2); event identity as worldline coincidence (Eq. 4); operational order observable from σx,σy,σz statistics on the encoded qubit state (App. B, Fig. 4) [paper claim, in-paper argument]; *our observation*: "which source of indefiniteness" (events vs metrics) is explicitly NOT invariant, but "whether indefiniteness" is — the paper's own headline contrast | Localization of events (delocalized vs localized) — quantum-coordinate choice (App. A.1/A.2); whether the metric is superposed at the relevant points (A.1: superposed metric values at fixed points; A.2: flat along γ0); number of manifold points per event; metric field values at points (non-invariant); curvature scalar (distinguishes optical vs gravitational switch, though diffeo-invariant per branch) | Two branches (control qubit) + spin-1/2 test particle + two 2-level memory registers ℋ_A, ℋ_B (App. B protocol; encoded state (12) is a single qubit |ψ⟩=α|s=+1⟩+β|s=−1⟩); minimal *scenario*: 2 systems + test particle on 2 semi-classical metrics (Fig. 2) |
| **B** 2308.10967v1 (Quantum 9, 1616, 2025); transformations: TO twirl (Eq. 9); TO↔PM equivalence maps, ideal clocks only (App. D) | Global constraint solution |Ψ⟩ (static); multi-time probabilities for ideal clocks — TO = PM = standard QM (App. D, Eqs. 60–66) [proved in paper]; for a good-enough non-ideal clock, TO reproduces standard QM (Sec. IV.1) [paper claim via Höhn-Smith-Lock]; *our observation*: the equivalence result is the paper's invariance statement; no frame transformation exists between TO and PM off the ideal limit | Approach-dependent (TO vs PM, not clock-frame): unitarity of conditional evolution (TO unitary; PM non-unitary for finite E, footnote 2); time-locality (PM kernel F(t), Eq. 17); order of measurement events (TO: externally chosen, sharp; PM: fundamentally limited, cross-order term with disjoint supports, Sec. IV.2.3); probability rule denominator (Eq. 14); whether measurements exist at all when Ĥ_C=0 (Sec. IV.2.4's extreme case) | One qubit system + one qubit ancilla, with clock spectrum [−E,E]: perturbative non-unitarity example K_SA(t)=K δ(t−τ) (footnote 2); discrete-time unitary model: orthonormal clock basis {t_k=kπ/E}, Eq. (108), unitary step U (Eq. 22/109) [smallest *finite-dimensional* clock construction in the paper; the continuous non-ideal clock itself is infinite-dimensional by construction] |
| **C** 2603.08845v1 (2026); transformations: PW reduction maps ℛ_i (Eq. 13), frame change 𝒮_{i→j} (Eq. 15) | Physical state |Ψ⟩⟩; outcome probabilities under frame change ("the frame-change map preserves probabilities", Sec. V.2; App. B: p_|C1 = p_|C2 = p(b|…)); signaling relations A→B / B→A when interventions are constraint-embedded (Sec. VI.2–VI.3); subsystem interaction structure for ideal clocks (Eqs. 16–18, with caveat [H_B+H_C, H_BC]=0); whether order is definite (Sec. VI.3: same in both frames) or indefinite (Sec. VI.4 + Discussion: both frames agree, citing A) [paper claims]; *our observation*: the definite-vs-indefinite status being frame-invariant mirrors anchor A's invariance | Direction of time (constraint Ĥ_C1−Ĥ_C2+Ĥ_S, Eqs. 25–30; disagreement only approximate; footnote 3 speculation on the thermodynamic arrow); temporal localization of events (necessary delocalization, Sec. III — perfect synchronization non-normalizable); subsystem-locality of naive operations (Eqs. 45–47: local in C1's frame, global in C2's); which operation appears time-delocalized (Fig. 6); timing of the other clock's operation | Two-qubit signaling example (App. B): H_S = X_A⊗1+1⊗X_B (no signaling) vs X_A⊗X_B (signaling; Hadamard on A at t_i, Pauli-Y measurement on B at t_f, Eqs. 80–92) [the smallest fully worked example in the paper]; switch construction: 2 ideal clocks + subsystems A,B + ancillas A′,B′ (Sec. VI.4); clock-dependent order possible only for Hermitian unitaries, e.g. Pauli operators on a qubit (App. A, Eqs. 76–79) |
| **D** 2607.03417v1 (2026); transformations: none (explicitly deferred); factor-splitting only (App. A) | Measurement outcome as the *internal* state of registers (σ_int); possibility of broadcasting outcomes without decoherence (protocol Eqs. 6–10: Eve's register ends in product with Alice's position) [paper claim]; physics-invariance questions explicitly left open | Absolute position of lab/registers (superposed vs localized); which degree of freedom plays "abs" (centre of mass vs any fixed-relative-position constituent, App. A Eqs. 11–12); whether an outside observer sees "a superposition of completed registers" (resolvable by putting register internals outside the Heisenberg cut, Sec. 3.1) | A single register in state |s⟩ within a position qubit {|x0⟩,|x1⟩} superposition: state (6) → (10) is two 2-level position branches + 2-level (or larger) internal register [smallest instance of the broadcasting protocol; minimal even example is one qubit (|x0⟩+|x1⟩)/√2, Eq. (1)] |
| **E** 1105.4464v3 (Nat. Commun. 3, 1092, 2012); transformations: none in framework | Causal inequality bound p_succ ≤ 3/4 for all causally separable processes (Eqs. 1–2, App. .1) [established, peer-reviewed]; achievability (2+√2)/4 by the Eq. (7) process (Eq. 8, App. .5) [established]; classical processes always causally separable (App. .6) [established]; "causal order" = signaling direction, A⋠B etc. | Nothing is frame-dependent — no frames exist; per the paper: each party is certain of order inside its own lab while global order is unfixed (Fig. 2) | The process matrix (Eq. 7) on four 2-level systems A1, A2, B1, B2, with the two-outcome protocols ξ(x,a) (Eq. 20) and η(y,b,b′) (Eqs. 21–23): the minimal inequality-violating process in the paper |

## Notes on the "smallest example" column

- **A** never computes a finite-dimensional *dynamics*: the minimal
  finite-dimensional object is the encoded order qubit; the scenario-level
  minimum is the two-branch metric superposition of Fig. 2. The paper's
  footnote 1 concedes the metric Hilbert space is not constructed, so the
  "dimension" of the metric sector is undefined.
- **B**'s continuous clock (spectrum [−E,E]) is infinite-dimensional; the
  genuinely finite-dimensional construction in the paper is the discrete-time
  model (orthonormal basis t_k = kπ/E), which is also where unitarity is
  restored.
- **C** assumes ideal (infinite-dimensional) clocks throughout; its smallest
  worked numerical example is the two-qubit signaling gadget of App. B.
- **D** has no dynamics at all; its smallest example is the position-qubit
  state of Eq. (1) and the two-branch broadcast of Sec. 3.2.
- **E**'s Eq. (7) process is the smallest process-matrix example in the
  primary literature for inequality violation: four qubits total.

## Reading-depth caution

Cells marked "paper claim" or "our observation" are not established results;
only E's three rightmost invariant entries are peer-reviewed established
results read at full text this session. Discovery-depth sources
(`ico-chiribella-switch-2013`, `ico-oreshkov-time-delocalized-2019`,
`ico-castro-ruiz-dynamics-2018`, `ico-apadula-frame-process-matrices-2026`,
etc.) are used in `comparison.md` §6 only as leads and are not load-bearing
in the table above.
