# Defeat search: RC-5 (separating four memory criteria for clock-conditioned maps)

Status: 2026-10-19. Independent Claude-subagent pass; abstract, search-snippet or
section-level depth only, no full text read. Not a novelty claim and not the independent
audit. Three of the subagent's first-guess arXiv IDs were wrong and were discarded; the
IDs below were resolved by search and match their titles per the subagent. The arXiv API
was rate-limited, so the coordinator has not re-verified them.

## What Eq. (10) of arXiv 2606.08595 (Nandi and Petruccione) establishes (section-level)

- Setting: Schwinger-Tomonaga evolution on spacelike hypersurfaces with finite-resolution
  clocks, not Page-Wootters proper (relevant to COORDINATOR_REVIEW question D08).
- Form: a time-convolutionless master equation for the conditioned state, with an integral
  over the causal past J^-(x) of a kernel C = chi_sigma(x,y;tau) G_alphabeta(x,y), the
  product of a clock correlator and an environment correlator. The paper calls it the
  central result.
- Assumptions: second order in g with O(g^3) remainder; factorized initial state and clock
  independent of the bath; conditioning on the clock reading acts as postselection with
  normalization (Eq. 7), so the normalized state evolves nonlinearly; the step promoting
  the Dyson series to a state-local TCL form is not justified in the supplement; the GKLS
  form is recovered only under sigma >> tau_B, stationarity, a secular approximation and
  extension of the memory integral to infinite relational time.
- It does not test CP-divisibility, trace-distance backflow or a process tensor. Its only
  non-Markovianity reference is the 2016 Breuer-Laine-Piilo-Vacchini colloquium.
- Against the four criteria: it implies failure of the homogeneous semigroup law only if
  the kernel is nontrivial (not shown for a specific model); CP-divisibility, backflow and
  process-tensor memory are not established. What it states is a kernel-structure
  (Nakajima-Zwanzig-style) memory, a different category. A time-local TCL equation does not
  by itself imply indivisibility; that depends on the sign of the generator's rates, which
  the paper does not examine. Because of the nonlinear normalized evolution, linear-channel
  notions are not directly defined for it without extra structure.

This answers D08 provisionally. It is a section-level reading, not a derivation audit.

## Predecessors (depth per row)

| Identifier | Result | Depth | Covers RC-5 |
|---|---|---|---|
| 0908.0238 Breuer-Laine-Piilo 2009 | Trace-distance backflow measure | abstract | defines criterion (iii) only |
| 0911.4270 Rivas-Huelga-Plenio 2010 | Entanglement-based measure tied to CP-divisibility violation | abstract | defines (ii) only |
| 1405.0303 Rivas-Huelga-Plenio review 2014 | Compares divisibility-based and other definitions | snippet | partly: (ii) vs (iii) |
| 1102.4318 Chruscinski-Kossakowski-Rivas 2011 | Toy model where divisibility-based and distinguishability-based measures disagree | snippet | partly: (ii) vs (iii) example, not clock-conditioned |
| 1901.05223 Milz-Kim-Pollock-Modi | CP-divisible processes can carry non-Markovian temporal correlations (process tensor) | snippet | partly: (ii) vs (iv) |
| 1801.09811 Pollock et al. | Operational Markov condition for quantum processes | snippet | defines (iv); no clock |
| 2002.07232 Nestmann-Bruch-Wegewijs | Fixed-point relation between Nakajima-Zwanzig kernel and time-local generator | abstract | partly: bridges kernel and TCL form |
| 2209.14902 Chruscinski review 2022 | Time-local vs memory-kernel generators, CP-divisibility; multi-time criteria not mentioned in the abstract | abstract | partly: background |
| 1712.00081 Smith-Ahmadi; 2204.11740 Rijavec; 2107.11452 Mendes et al.; 2308.10967 Hausmann et al. | Clock-conditioned time-nonlocal, non-unitary or nonlinear dynamics | abstract or snippet | the map families; no divisibility, backflow or process-tensor test found |

## Verdict (subagent): partly occupied

- General separation of the criteria: occupied. CP-divisibility vs backflow (1102.4318),
  CP-divisibility vs multi-time Markovianity (1901.05223), and the semigroup vs non-semigroup
  distinction (Gaussian dephasing) are published at least as examples; details unread. A
  separating model for generic maps would be an application. Whether a single published
  model separates all four criteria at once was not checked.
- Clock-conditioned maps: families exist, no criterion classification found, but
  absence was not proved; a body-text read of those papers and citing works is needed.

## Narrowest unaddressed sub-case found (not a novelty claim)

A qubit system with a finite-dimensional clock (Smith-Ahmadi qubit-clock class or a
Page-Wootters construction with unitary clock-system interaction); define the conditioned
reduced maps Phi_tau so they stay linear (unnormalized conditioning with state-independent
outcome probability, or a fixed-reference normalization); compute exactly whether the
propagator between clock readings is CPTP, whether trace distance revives, and whether the
multi-time process tensor from clock-readout instruments satisfies the Markov condition.
The normalized, nonlinear case has no standard divisibility or process-tensor definition;
choosing one is a definition choice, not a result.

## Not done

Full-text reads of any predecessor; whether 2603.28277 (2026 review of genuine and
non-genuine non-Markovianity) already separates the criteria; forward citations; the
supplement of 2606.08595.
