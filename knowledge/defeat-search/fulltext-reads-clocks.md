# Full-text reads for RC-1 / candidate B: Ludescher et al. and Hausmann et al.

Status: 2026-10-19. Two independent Claude-subagent full-text reads of arXiv HTML
renderings (no PDF, no journal version). Quotes are as reported by the subagents from their
own text extractions and were not re-read by the coordinator. Not a novelty claim.

Question put to both: for a finite-dimensional Z_N clock with a non-ideal covariant
rank-one POVM and a clock-system coupling H_int with [H_int, H_C] nonzero, does the paper
already give necessary and sufficient conditions for the Dirac-observable, Page-Wootters-
conditioned and relational-Heisenberg evolutions to agree?

## Answer from both: no

### Ludescher, Mekonnen, Galley, Mueller, arXiv 2607.24976v1 (27 Jul 2026, preprint)

- Setting: finite-dimensional Hilbert spaces, compact Lie group G; a QRF is a covariant
  instrument with Kraus rank 1 (Def 10). The authors say the operational part rests on
  "plausibility arguments", not axiomatic deduction (Sec V).
- No theorem about dynamics, interaction or clock equivalence. The Dirac-observable part
  (Def 21, Lemmas 22-23) is a static map with no Hamiltonian. The words "Heisenberg" and
  "relational Heisenberg" never occur.
- The "interacting subsystems" claim of the abstract rests on Example 29 (continuous,
  explicitly outside the framework), Example 32 (Z_n, ideal clock with orthogonal position
  projectors) and the review in App. B.1. Mechanism: for H = P1 + P2 + K(X1 - X2)^2 the
  constraint splits into commuting centre-of-mass and relative parts, so the centre-of-mass
  clock decouples (Eq. 52, Eq. 60) while the local clock does not (Eqs. 47-48). This is a
  sufficient structural reason for one model, with the interaction commuting with the
  clock generator P1 + P2. The case [H_int, H_C] nonzero is the opposite regime.
- The interacting local-clock case is stated to be outside their formalism: "These
  constraints now generate different structures in general, which is neither the case ...
  in [34], nor in our generalized framework" (App. B.1). The kernel equation (their Eq. 57,
  from Smith-Ahmadi) uses the resolution of identity of an ideal clock. The phrase
  "certain interaction terms" is never characterized, and the announced generalization to
  general clock seeds is not done.
- Ex. 30, the only non-ideal clock example, is non-interacting and outside the framework.
- Caveats from the subagent: v1, not peer reviewed; AI-disclosed figures; typos in Ex. 32
  notation; the proof of Lemma 2 was skimmed, not audited.

### Hausmann, Schmidhuber, Castro-Ruiz, arXiv 2308.10967 (Quantum 9, 1616, 2025)

- Compares only two formulations: twirled observable (TO, constraint H_C + H_S, no
  coupling) and purified measurement (PM, constraint with a clock-triggered coupling
  N_C |phi_t><phi_t| (x) K_SA(t)). It never compares Dirac vs Page-Wootters vs relational
  Heisenberg. No "relational Heisenberg" term in the paper.
- Clock: L^2[-E, E] with continuous bounded spectrum, infinite-dimensional; not finite-
  dimensional and not Z_N. A periodic finite-dimensional clock is mentioned only in App. E.3
  (a condition stated, no analysis).
- Agreement for ideal clocks is proved in App. D for sharp delta-kick purified measurements
  with free H_S. For finite spectrum the PM equation (their Eq. 16) is time-non-local and
  generally non-unitary, while TO stays unitary. The authors say the difference reflects a
  "different implicit notion of what an 'event at time t' means operationally", i.e. the
  two describe different experimental situations; they do not claim a failure of agreement
  within a single setup.
- Interaction restrictions: clock-triggered only (through POVM elements), solved
  perturbatively under H_S = 0 ("this case already captures the conceptual issues");
  convergence assumed; no general non-commuting coupling analysis.
- The discrete model (Sec 5, App G) restores unitarity with an orthonormal clock basis on
  Z (not Z_N) and states PM/TO equivalence "immediately" without working it out; discrete
  TO is not defined in the paper.
- The non-ideal TO unitarity and the "good clock" conditions are delegated to Hoehn-Smith-
  Lock; the non-unitarity references include Rijavec (not read).

## Effect on the earlier abstract-level defeat search (candidate B)

The B search called interacting clocks "occupied" partly on Ludescher's abstract. Full text
shows that claim is supported by one worked example with a commuting interaction, not a
general result. Hausmann et al. establish a finite-resolution phenomenon for a different
pair of formulations in a continuous bounded-spectrum clock. Neither pre-empts the narrow
sub-case recorded in candidate-B.md (finite-dimensional Z_N clock, non-ideal covariant
POVM, coupling not commuting with the clock Hamiltonian, three-picture agreement). Still
unread: Rijavec 2204.11740, Hoehn-Smith-Lock 1912.00033 (partly checked via the Codex
matrix), Garmier-Hausmann-Castro-Ruiz 2512.19343, Smith-Ahmadi 1712.00081 in the body, and
forward citations of both. The sliver is not shown to be open; it is shown not to be closed
by these two papers.
