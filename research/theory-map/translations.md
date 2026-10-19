# Proposed connections: explicit maps, domains, and failures

Status: worker submission for review, 2026-10-19. Every connection below is
one of: **explicit map** (the actual correspondence is written out, from
formulas recorded in the cited sources), **partial map** (the map is written
for a stated domain and known failures are listed), or **conjectural**
(no defensible map yet; the bridge is recorded as a question with a
falsifier). Nothing here is an accepted result. Formulas are transcribed only
from the lane records at their recorded read depth; where a record did not
contain the equation, the connection is labeled conjectural rather than
filled from memory.

Labels: `[map]`, `[partial-map]`, `[conjectural]`, `[disagreement]` (pointer
to `disagreements.md`). Every entry names the assumption whose change breaks
the connection (the falsifier), per the handoff contract's requirement.

---

## X01 — Interacting Page–Wootters ↔ free-clock trinity `[partial-map]`

- **Nodes:** N10 (Smith–Ahmadi) ↔ N11 (relational trinity).
- **Map (explicit where stated):**
  - N11 side: constraint `C_H = H_C + H_S ≈ 0`, no interaction; clock POVM
    `E_T(dt) = mu dt |t><t|`; equivalence of Dirac / PW / relational
    Heisenberg pictures via reduction maps and physical inner product
    (Theorems 1–6 as recorded).
  - N10 side: constraint `H = H_C + H_S + H_int`; conditioning on clock time
    gives `i d/dt psi_S(t) = H_S psi_S(t) + integral K(t,t') psi_S(t') dt'`,
    `K(t,t') = <t|H_int|t'>`, with norm constancy from the chosen
    time-independent physical inner product (Eqs. 4–27 as recorded).
  - Shared object: the PW conditional state on the clock-page; the map agrees
    on this object where `H_int = 0` (then N10 reduces to the PW leg of N11).
- **Domain:** N11's equivalence holds only for the uncoupled constraint and
  its covariant rank-one clock POVM class (nonorthogonal/overcomplete and
  bounded/half-line spectra included; arbitrary degeneracy not).
- **Failure modes:** (i) for `H_int ≠ 0` only the N10 conditional equation is
  established — no Dirac-observable or relational-Heisenberg counterpart is
  proved there, so the three-picture equivalence is not known to survive;
  (ii) N10's norm constancy depends on the stated inner-product choice, not
  on a theorem for all covariant instruments; (iii) N13 records that even the
  free periodic-clock trinity needs an updated PW conditioning rule for
  continuous system spectra — so "PW conditioning" is not one fixed map.
- **Falsifier:** a theorem giving necessary and sufficient conditions for a
  three-picture equivalence under interaction would close the gap this edge
  exposes (see RC-1); conversely the equivalence failing for a named
  interaction class is the intended counterexample target.
- **Sources:** `frontier-smith-ahmadi-interacting-2019` (full-text),
  `frontier-relational-trinity-2019v3` (full-text),
  `knowledge/frontier/theorem-matrix.md`.

## X02 — Trinity ↔ relativistic sector decomposition `[partial-map]`

- **Nodes:** N11 ↔ N12.
- **Map (explicit):** replace the autonomous clock Hamiltonian by the
  quadratic clock momentum `H_C = s p_t^2/2`, `s = ±1`, giving
  `C_H = s p_t^2/2 + H_S ≈ 0`; decompose physical states into frequency
  sectors `sigma = ±`; apply the N11 reduction construction **per sector**
  with sector POVM states (Eqs. 25–29) and sector-dependent normalization
  (incl. factor 1/2). Equivalence theorems hold sectorwise.
- **Domain:** uncoupled split; quadratic clock momentum; the two sectors are
  superselection-like for the conditioning: conditional probabilities must
  respect sector localization.
- **Failure modes:** (i) coherent cross-sector clock superpositions are not
  covered by the sectorwise theorem; naive conditioning can spoil
  normalization (N12 Sec. VI); (ii) no cross-sector frame-change
  invertibility; (iii) turning points and interacting/generalized
  constraints excluded.
- **Falsifier:** a published normalized sector-coherent conditioning with
  well-defined probabilities, or a proof that sector coherence is never
  operationally accessible without an external phase reference — both would
  change this edge's status (see RC-3).
- **Sources:** `frontier-relativistic-trinity-2020v1` (full-text),
  `frontier-relational-trinity-2019v3` (full-text).

## X03 — Trinity ↔ periodic-clock trinity `[conjectural]`

- **Nodes:** N11 ↔ N13.
- **Proposed bridge (conjecture):** both are instances of "covariant
  group-based clock + partial group averaging + three-picture equivalence",
  so the trinity schema should extend across spectral classes with the
  conditioning rule adjusted per class (periodic clocks: partial averaging
  over one cycle; continuous system spectra: updated conditional
  probabilities per N13).
- **Why it is only conjectural:** N13's record is abstract-depth (fetched by
  this worker); its theorem hypotheses, the updated conditioning definition,
  and the classical/quantum parallel are unextracted. The frontier second
  pass explicitly warns that spectral-class differences are where such
  bridges silently fail.
- **Falsifier:** N13's periodic invariance results (winding numbers give no
  clock-relative invariants) suggest nontrivial restrictions — if the
  periodic case forbids the bounded-interval constructions of N11 (or vice
  versa), the unified-schema conjecture fails for that class.
- **Sources:** `map-periodic-clock-trinity-2026v3` (abstract),
  `frontier-relational-trinity-2019v3` (full-text),
  `knowledge/frontier/candidates.md` (second-pass correction).

## X04 — Linear kernel vs nonlinear conditioned dynamics `[recorded difference]`

- **Nodes:** N10 ↔ N14.
- **Content:** N10's conditioned equation is linear with an additive kernel
  `K(t,t') = <t|H_int|t'>`; N14 reports a **non-linear**,
  initial-condition-dependent equation of motion for the conditioned mixed
  state (gravitational-decoherence interaction; quasi-ideal clock).
  Both cannot be the same conditioning map; the difference is real as
  recorded but its mechanism (state-dependent generator? nonlinear
  normalization? postselection?) is unextracted at abstract depth.
- **Domain/failure:** no map is asserted. Any claim that "PW with interaction
  is always linear" or "always nonlinear" would be false for one of the two
  recorded models.
- **Falsifier / next step:** extract N14's derivation (audit target folded
  into RC-5); identify which input/conditioning class each result assumes.
- **Sources:** `frontier-smith-ahmadi-interacting-2019` (full-text),
  `map-pw-quasi-ideal-2021v1` (abstract).

## X05 — Temporal-QRF protocols ↔ interacting Page–Wootters `[partial-map]`

- **Nodes:** N18 ↔ N10.
- **Map (explicit as recorded):** N18's PM approach realizes measurement by
  an ancilla A with a clock-triggered interaction `K_SA(t)` inside the
  constraint — structurally the N10 kernel situation with an ancilla in the
  role of S; N18's TO approach instead uses covariant/twirled observables
  with an external measurement protocol. For ideal clocks TO and PM agree on
  multi-time predictions; for finite-spectrum clocks PM conditioning becomes
  time-nonlocal (memory-kernel) and may be nonunitary.
- **Domain:** N18's clock `L^2[-E,E]`, bounded clock energy; the
  E→∞ orthogonal-clock limit is where agreement is stated.
- **Failure modes:** finite clock-state overlap produces the nonlocal terms;
  protocol difference (TO vs PM) is an operational event-notion difference
  (D06), not an equivalence failure; nonunitarity of reduced dynamics must
  not be read as nonunitarity of the global constrained dynamics.
- **Falsifier:** an explicit protocol-level disagreement surviving at E→∞
  would break the stated agreement; conversely a unitary discrete-time PM
  construction covering N10's interactions is claimed by N18 (Sec. 5) and
  would extend the map.
- **Sources:** `frontier-page-wootters-measurements-2023` (full-text),
  `frontier-smith-ahmadi-interacting-2019` (full-text).

## X06 — Ancilla-PM ↔ instrument-based non-subsystem QRFs `[conjectural]`

- **Nodes:** N18 ↔ N19.
- **Proposed bridge (conjecture):** N19's covariant instruments generalize
  the frame notion used in N18's protocols; the finite Abelian example
  (`C = P1 + P2 + K(X1 - X2)^2`, physical states `|d; K d^2>`, COM frame
  decoupling the relative-coordinate evolution) should map onto a PM-style
  construction with the COM frame as the "clock page".
- **Why conjectural:** N19's own recorded open question asks how operational
  probabilities are compared across subsystem and non-subsystem frames;
  without that comparison the bridge has no defined observable content.
- **Falsifier:** if no common event-statistics exist for an ancilla-PM
  protocol and the corresponding instrument frame in the finite Abelian
  model, the bridge fails operationally; if all differences are removable by
  a representation change (no observable content), the bridge is a
  reparameterization only and must be labeled as such (project standard:
  representation ≠ ontology).
- **Sources:** `frontier-qrf-beyond-subsystems-2026` (full-text),
  `frontier-page-wootters-measurements-2023` (full-text).

## X07 — Sector conditioning ↔ proper-time superpositions `[conjectural]`

- **Nodes:** N12 ↔ N17.
- **Proposed bridge (conjecture):** "coherence across clock-parameter
  branches" is the same normalization problem in both: N12's cross-sector
  clock superpositions (where naive conditioning breaks probability
  normalization) and N17's superpositions of proper times both require a
  rule for assigning probabilities to coherent superpositions of
  clock-parameter branches; a sector-coherent conditioning analysis (RC-3)
  would transfer.
- **Why conjectural:** N17 is abstract-depth; no formula from it is recorded
  in any lane, and the model classes differ (quadratic mass-shell sectors vs
  spacetime QRF transformations).
- **Falsifier:** a proof that proper-time superpositions reduce to a single
  sector choice, or that sector coherence is operationally inaccessible,
  severs the bridge.
- **Sources:** `frontier-relativistic-trinity-2020v1` (full-text),
  `frontier-spacetime-qrf-2021` (abstract).

## X08 — Smith–Ahmadi kernel ↔ N19 instrument kernel `[explicit parallel]`

- **Nodes:** N10 ↔ N19.
- **Map (explicit as recorded in N19 App. B.1):** both conditioned
  equations carry a kernel of the form `K(t,t') = (<t| x 1) H_int (|t'> x 1)`
  (N19's version) vs `K(t,t') = <t|H_int|t'>` (N10). N19 additionally
  distinguishes the clock generator from the full constraint and reports
  that certain interaction terms admit a valid **non-local** clock whose
  relational dynamics decouples (finite Abelian example).
- **Domain:** N19's framework: finite-dimensional Hilbert spaces, compact Lie
  groups; the continuous COM illustration is outside it (normalization
  ignored, as recorded).
- **Failure modes:** the finite Abelian example proves decoupling for the
  stated `K(X1-X2)^2` model only; no all-interactions characterization is
  claimed by the authors.
- **Falsifier:** an interaction outside the commuting-relative-potential
  class whose instrument-frame dynamics still decouples would extend the
  class; a commuting example where the induced reduced dynamics is not
  isometric would refute the reported decoupling reading (RC-1's first
  bounded test).
- **Sources:** `frontier-qrf-beyond-subsystems-2026` (full-text),
  `frontier-smith-ahmadi-interacting-2019` (full-text).

## X09 — Periodic-clock conditioning updates ↔ interacting conditioning `[conjectural]`

- **Nodes:** N13 ↔ N10/N14.
- **Proposed bridge (conjecture):** N13's finding that the original PW
  conditional-probability definition **fails for continuous system energy
  spectra** (periodic-clock setting) and N14's nonlinearity for mixed states
  may be two faces of one conditioning-definition problem: what exactly is
  being conditioned on, and with which normalization instrument.
- **Why conjectural:** both sides are abstract-level or partially extracted;
  no common formal variable is on the table yet.
- **Falsifier:** if N13's failure is purely spectral (absent in finite
  spectra) while N14's nonlinearity persists for finite spectra, the two are
  independent effects and the bridge dies.
- **Sources:** `map-periodic-clock-trinity-2026v3` (abstract),
  `map-pw-quasi-ideal-2021v1` (abstract).

## X10 — Temporal-QRF delocalization ↔ operational causal-order observable `[conjectural]`

- **Nodes:** N20 ↔ N21.
- **Proposed bridge (conjecture):** N21's relativistic operational
  causal-order observable — reported not to distinguish an optical quantum
  switch from a gravitational one — should delimit what N20's "time
  delocalization across temporal QRFs" can mean observably: any
  delocalization claim must either produce a difference in an N21-type
  observable or accept that it is a frame-description effect.
- **Why conjectural:** both are abstract-level; N21's equivalence claim is
  the authors' thesis; N20's derivations unread.
- **Falsifier:** a temporal-QRF transformation that changes an N21-type
  causal-order observable would defeat the conjectured constraint and would
  be a genuinely surprising, sharp disagreement — precisely the kind of
  target RC-style audits should look for.
- **Sources:** `map-indefinite-order-quantum-coordinates-2025v3` (abstract),
  `frontier-time-delocalization-2026` (abstract).

## X11 — Causal-order observable ↔ Bell-type temporal-order correlations `[conjectural]`

- **Nodes:** N21 ↔ N22.
- **Proposed bridge (conjecture):** both aim at challenging classical
  temporal order; whether N21's observable and N22's Bell-type correlations
  track the same operational property (indefinite order vs order-witness
  violation) is undefined without both full texts.
- **Falsifier:** a Bell-type violation obtainable in a process whose N21
  observable is trivially order-definite (or vice versa) shows the two
  operational notions diverge — itself a useful precise disagreement.
- **Sources:** `map-indefinite-order-quantum-coordinates-2025v3` (abstract),
  `seed-bell-temporal-order` (abstract).

## X12 — Modular flow ↔ thermal-clock jump process `[partial-map]`

- **Nodes:** N24 ↔ N28.
- **Map (explicit as recorded):** in N28's open clock model, the steady
  state is Gibbs–Boltzmann and the jump-process reading times define a flow
  that, in the high-rate good-clock limit, is analogous to thermal-time
  (modular) dynamics; finite clock rate adds intrinsic decoherence
  corrections (Sec. 5.2, Eqs. 94–99).
- **Domain:** the stated clock model and its high-rate limit; not a
  general TTH derivation.
- **Failure modes:** the analogy is model-specific; no modular flow of a
  specific algebra is computed on the N24 side at the recorded depth; the
  identification of the flow with physical time remains the contested bridge
  (D04).
- **Falsifier:** finite-rate corrections growing without bound in the
  high-rate limit, or clock-calibration freedom absorbing the flow, would
  break the claimed analogy.
- **Sources:** `frontier-thermodynamics-clocks-2020` (full-text),
  `frontier-thermal-time-original-1994` (full-text access).

## X18 — Local-observer unitarity ↔ trinity global unitarity `[conjectural]`

- **Nodes:** N16 ↔ N11.
- **Proposed bridge (conjecture):** global constrained dynamics is unitary in
  the trinity family, while reduced/conditioned descriptions may be
  nonunitary (seen in N10/N18); N16 reportedly compares unitarity relative
  to a dynamical local observer's clock across fixed vs dynamical gravity —
  the natural question is whether "unitary relative to which clock" has a
  protocol-independent answer in the trinity class.
- **Why conjectural:** N16 is abstract-only and unextracted; even its
  claimed result is not on record in usable form. No map is asserted.
- **Falsifier:** an extracted N16 result already contained in the N12
  sector/conditioning analysis (or contradicting its normalization rules)
  collapses this edge either to redundant or to a precise conflict.
- **Sources:** `frontier-local-observer-unitarity-2026` (abstract),
  `frontier-relational-trinity-2019v3` (full-text).

## X14 — Equilibrium thermal clocks ↔ nonequilibrium clock thermodynamics `[conjectural]`

- **Nodes:** N25 ↔ N28.
- **Proposed bridge (conjecture):** N25's consistency condition (reported
  operationally equivalent to Tolman–Ehrenfest without assuming gravity) and
  N28's Gibbs-steady-state clocks could be two regimes (equilibrium vs
  nonequilibrium) of one operationalization of TTH.
- **Why conjectural:** different premises (statistical state over a large
  finite system vs open master-equation dynamics); no shared protocol is
  written down; N25's own record flags dropped-thermality dependence.
- **Falsifier:** a protocol where the N25 condition holds but the N28
  high-rate flow is absent (or vice versa).
- **Sources:** `frontier-thermal-clock-relational-2011` (full-text),
  `frontier-thermodynamics-clocks-2020` (full-text).

## X16 — Same substrate, three structures: Malament / Putnam / Stein `[explicit contrast]`

- **Nodes:** N02 ↔ N03 ↔ N04.
- **Map (explicit):** all three fix the same substrate — time-oriented
  Minkowski spacetime with causal connectibility — and add exactly one
  structuring relation, with divergent outcomes:
  - N02: an equivalence relation of **simultaneity**, definable from
    `kappa` + observer worldline under invariance + equivalence +
    non-universality + cross-worldline conditions → unique Einstein
    synchrony (with temporal-reflection invariance doing decisive work, per
    Sarkar–Stachel).
  - N04: a **definiteness** relation `R`, reflexive, transitive, invariant,
    containing the full causal past, with an unsettled-points condition →
    forced to be the causal-past relation.
  - N03: the **reality-propagation** scheme: principle III + transitive
    closure of frame-relative simultaneity + abundance of observers → block
    conclusion (bridge premises doing decisive work).
- **Why this matters:** the three results are frequently conflated as "what
  relativity proves". They are non-interchangeable: N02's output is an
  equivalence relation on spacelike-separated pairs; N04's is the causal
  past (ordering, not equivalence); N03's is an ontological closure claim
  over observers. Each map's premises do not transfer to the others — e.g.,
  adding N02's simultaneity to N04's setup does not produce a global present
  (Stein pp.151–152), and N04's `R` satisfies none of N02's simultaneity
  conditions.
- **Failure modes of conflation:** documented in D02/D03 and in the
  `knowledge/checks/correspondence-cases.jsonl` relation cases (isolated
  ablations are false).
- **Falsifier:** any premise-set that derives a global present from N02+N04
  structures without bridge premises would falsify the non-transfer claim —
  this is exactly RC-2's ablation program.
- **Sources:** `found-sarkar-stachel-1999` (full-text),
  `found-sep-malament` (full-text secondary), `found-malament-1977`
  (abstract), `found-stein-1991` (full-text), `found-putnam` (full-text,
  partial), `knowledge/foundations/audit.md`.

## X19 — Law-constitutive presentism ↔ empirical bounds `[conjectural/incomplete]`

- **Nodes:** N05 ↔ N06.
- **Content:** there is currently **no explicit map**: Brading's program (as
  inspected) names no observable coefficients, so no SME row of N06 can be
  attached to it. The honest map status is "no defensible translation yet".
  Any claim that "presentism is empirically constrained by Lorentz-violation
  data" is therefore unsupported for this node family.
- **Falsifier / next step:** a concrete preferred-structure descendant of N05
  naming observable coefficients would create the map (and inherit N06's
  bounds); failure to name any coefficient keeps the connection in
  "empirically idle until further notice".
- **Sources:** `found-brading` (abstract), `seed-lorentz-data-2026`
  (abstract), `knowledge/foundations/audit.md` Sec. 4.

## X20 — Growth dynamics ↔ embedding uniqueness `[conjectural]`

- **Nodes:** N08 ↔ N09.
- **Proposed bridge (conjecture, from the frontier lane):** embedding
  uniqueness is mathematically orthogonal to growth dynamics — the former
  concerns order→geometry maps, the latter stochastic birth histories — so
  neither constrains the other's interpretive use.
- **Why conjectural:** N09's "well-conditioned" conditions are unextracted;
  if they implicitly fix a growth history or labeling, orthogonality fails.
- **Falsifier:** an N09 hypothesis that quantifies over labelings/birth
  orders would couple the two; see RC-4's distinguishability program.
- **Sources:** `frontier-causal-embedding-2026` (abstract),
  `frontier-causal-growth-1999` (abstract),
  `knowledge/frontier/candidates.md`.

## X21 — Causal-set growth ↔ Stein becoming ↔ Wüthrich–Callender analysis `[disagreement]`

- **Nodes:** N08 ↔ N04; analysis node `frontier-causal-becoming-2015`.
- **Content:** registered as a disagreement, not a map: growth models
  *suggest* a becoming-friendly reading; Wüthrich–Callender (abstract) argue
  about what causal-set becoming can amount to; Stein's `R` is a
  fixed-geometry relation with no birth order. Identifying growth with
  passage is a bridge premise, not a result. See D07.
- **Sources:** `frontier-causal-growth-1999` (abstract),
  `frontier-causal-becoming-2015` (abstract), `found-stein-1991`
  (full-text).

## X22 — Machine-checked certificates ↔ map claims `[method edge]`

- **Nodes:** N31/N32 ↔ all nodes.
- **Content:** any certificate (Lean/Isabelle/countermodel) attached to a
  connection here checks only the encoded statement; correspondence auditing
  (sources ↔ encoding), nonstandard axioms, `sorry`, and transitive
  dependencies remain separate duties (N31/N32 records;
  `knowledge/formalization/reuse-map.md`). This edge is the map's standing
  limitation label: **no node or edge in this map is kernel-verified**.

---

## Surprising-bridge shortlist (all flagged, none verified)

1. **X06/X08 (finite Abelian interaction model ↔ PW kernels):** a
   non-local clock frame dissolving interaction-induced nonlocality is the
   same phenomenon Smith–Ahmadi's kernel creates; if the finite model's
   decoupling generalizes even one step (RC-1), the "interactions break
   relational equivalence" folklore gets a sharp boundary.
2. **X10 (N21's invariance vs N20's delocalization):** if temporal-QRF
   delocalization cannot move an N21-type observable, then a whole family of
   "quantum temporal frames change causal structure" claims reduces to
   description — a precise, decidable disagreement.
3. **X16 (definability schema):** Malament's uniqueness and Stein's
   causal-past characterization are two theorems of one schema — invariant,
   reflexive, transitive, adequately rich relations over
   `(M, kappa, orientation)` are rigid. The schema itself is teachable,
   testable (RC-2), and explains precisely why both are *not* ontological
   theorems.

No bridge above carries a truth-weight; each is a question with a falsifier,
queued for the novelty-audit and follow-up tasks.
