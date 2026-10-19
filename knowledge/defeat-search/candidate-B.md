# Defeat search: NOVELTY candidate B (quantum-clock result beyond idealizations)

Status: 2026-10-19. Independent Claude-subagent pass, mostly abstract level, with partial
full-text via arXiv HTML for five papers (2308.10967, 1912.00033, 2007.00580, 2512.19343,
2507.14131). Evidence for the novelty gate, not a novelty claim and not the independent
audit. The arXiv API was rate-limited, so the coordinator could not re-verify arXiv IDs
here; they are as fetched from arXiv abstract pages by the subagent. Two of the Codex
coordinator's theorem-matrix claims were spot-checked against arXiv HTML and confirmed
(see below).

## Verdict (subagent): B as worded is substantially occupied

- Finite resolution: occupied for the central question. Hausmann, Schmidhuber and
  Castro-Ruiz (arXiv 2308.10967) show two Page-Wootters formulations (twirled-observable
  and purified-measurement) agree for ideal clocks and disagree for finite-spectrum
  clocks: the purified-measurement equation becomes time-nonlocal and generally
  non-unitary, while the twirled-observable version stays unitary. That is a different
  pair from the Dirac / Page-Wootters-conditioning / relational-Heisenberg trinity, so
  the three-picture comparison with a finite-resolution clock is not shown there.
- Interacting clocks: occupied. Smith-Ahmadi 1712.00081 (kernel equation), Rijavec
  2204.11740 (non-unitarity for some mixed states), Mendes et al. 2107.11452 (non-linear
  equation, quasi-ideal clock), Ludescher et al. 2607.24976 (exact Schrodinger equation
  for interacting subsystems, abstract plus matrix), and 2308.10967 for measurement
  coupling. The trinity paper itself (1912.00033) names interactions "the most pressing
  generalization", cites Smith-Ahmadi, and anticipates approximate or non-unitary results.
- Restricted observer access: partly occupied (2304.07021, 2607.05578, 2512.19343, and
  the operator-class restriction in 2308.10967); no trinity-style comparison under
  restricted access found, but the search was not exhaustive.

## Coordinator-matrix spot-check (confirmed, arXiv HTML)

- 2007.00580 Eq. (10): C_H = s p_t^2/2 + H_S, with a clock and system "which do not
  interact"; the paper says this does not hold in generic general-relativistic systems.
- 1912.00033v3: constraint H_C + H_S with the explicit assumption that clock and system do
  not interact. The matrix omits that the paper itself lists interactions as the most
  pressing generalization.

## Other predecessors worth reading in full

2512.19343 Garmier, Hausmann, Castro-Ruiz (non-ideal finite-resource frames, back-reaction);
2507.14131 De Vuyst, Hoehn, Tsobanjan (algebraic and effective QRFs, ideal-frame theorems);
2409.06479 Chataignier, Hoehn, Lock, Mele (periodic clocks); 2604.21805 and 2608.16732
Stoica (non-interaction does not remove the clock ambiguity); 1803.02045 Bryan and Medved
(interacting clocks can be more accurate); 2504.05848 Favalli and Smerzi (bounded
resolution); 2608.09601 Ardenghi (composite clock, operator-valued normalization back-
reaction); 2512.19346 Vaidhyanathan and Milburn (relational Tomonaga-Schwinger, finite
resolution). Unresolved: no Lock-Hoehn paper titled "Quantum measurement and the
relational frameworks" and no Diaz/Giacomini/Brukner paper were found; the attribution in
the search prompt may be wrong.

## Smallest sub-case none of the read sources addresses (not a novelty claim)

Finite-dimensional, compact periodic or finite-group clock (Z_N), non-ideal covariant
rank-one POVM, clock-system coupling H_int with [H_int, H_C] nonzero on the physical-state
domain. Question: are the three trinity reductions (relational Dirac observable in the
physical inner product, Page-Wootters conditioned equation, relational Heisenberg
reduction) mutually consistent? Is the Smith-Ahmadi kernel evolution equal to the Dirac-
observable evolution on the state space reachable by the stated accessible operations, and
under what necessary and sufficient condition on H_int and the POVM overlap? Nearest
sources fall short: 2308.10967 (measurement coupling, not the trinity), 2607.24976 (exact
for some interactions, instruments framework), 2204.11740 (restricted interaction class).
Not verified as unaddressed in the full text of 2607.24976, 2107.11452 or 2409.06479.

## Caveats

Mostly abstract depth; forward-citation checks on 1912.00033 and 2308.10967 not done;
2025-26 sweep by arXiv search only.
