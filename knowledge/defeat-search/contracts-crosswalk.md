# Crosswalk: theory-map research contracts vs independent defeat searches

Status: 2026-10-19. Coordinator note for the `novelty-audit` task. The theory-map worker
wrote its five contracts before the three independent defeat searches (candidates A, B, C;
abstract-level, Claude-subagent) existed, so the contracts' predecessor lists omit the
closest prior work those searches found. This is an input gap, not a worker error. It
does not edit the worker's files. None of this establishes novelty or its absence.

| Contract | Defeat search | Closest predecessors missing from the contract | Effect on the contract |
|---|---|---|---|
| RC-1 interaction-dependent clocks with autonomous isometric dynamics | B (substantially occupied as worded) | Hausmann, Schmidhuber, Castro-Ruiz 2308.10967 (twirled vs purified-measurement agree for ideal clocks, differ for finite resolution; non-unitary for measurement coupling); Rijavec 2204.11740; Mendes 2107.11452; Ludescher 2607.24976 (exact Schrodinger equation with interacting subsystems); the trinity paper's own statement that interactions are "the most pressing generalization" | RC-1 as worded needs a sharper class. The B search names the narrowest unaddressed case: finite-dimensional Z_N clock, non-ideal covariant POVM, coupling with [H_int, H_C] nonzero, with the question whether the three trinity reductions agree. RC-1's own Z_n example is close to this; it must be checked against 2607.24976 and 2308.10967 at full text first |
| RC-2 premise-dependency classification (Stein/Malament) | C (i) partly occupied, (ii) occupied | Clifton and Hogarth 1995 (Synthese 103:355-387, uniqueness of becoming relations under adequacy conditions), Czerniawski 2014/2020 (premise-necessity analysis of Putnam), Thyssen 2023 (eleven objections), Mamone-Capria 2012 and Giulini 2001 (classification of invariant simultaneity relations), Besnard 2012 (already listed), Lefever-Szekely, Madarasz-Stannett-Szekely | RC-2 deliverable (2), the Malament-side non-interchangeability table, falls in the occupied (ii) region. Deliverable (1), the Stein premise-necessity table, overlaps Clifton-Hogarth, whose adequacy conditions must be read first. Coordinator hand check: the universal relation and strict-timelike-past counterexamples are correct, and with invariance plus containing the whole causal past, adding any spacelike or future pair makes the transitive closure universal, so deliverable (1) is very likely an easy lemma. Its value, if any, is the machine-checked bridge-premise separation (C's narrowest sliver) |
| RC-3 sector-coherent conditioning | not searched | not covered by A, B or C | Needs its own defeat search; the B search found 2512.19343 and 2507.14131 (algebraic/effective frames) that may bear on sector structure |
| RC-4 record distinguishability in sequential growth | A (partly occupied) | Brightwell, Dowker, Garcia, Henson, Sorkin gr-qc/0210061; Surya and Zalel 2003.11311; Zalel 2302.10582; Riedel-Zurek-Zwolak 1312.0331; Hartle 1608.04145 | The covariant-observable/path-measure translation is already worked in CSG, so RC-4(a) with covariance-class parameters risks being the immediate corollary the contract's own falsifier (iii) warns about. The A search's open sliver, observer records that depend on growth order or labelling, matches RC-4's "access bound" and should be made the contract's center |
| RC-5 four memory criteria for clock-conditioned maps | not searched | not covered | Needs a defeat search against the dynamical-map literature (Chruscinski; Nestmann-Bruch-Wegewijs; Breuer-Laine-Piilo; Rivas-Huelga-Plenio; Pollock et al. process tensor) |

## Mathematical spot-checks by the coordinator (by hand)

The five project correspondence cases in `knowledge/checks/correspondence-cases.jsonl`
were checked: universal relation, strict-timelike-past relation, finite-dimensional
canonical commutator (trace argument), non-affine normalized update (diag(1, 1/sqrt 2)
sends the equal mixture to diag(2/3, 1/3), not the mixture of normalized outputs), and
Gaussian dephasing exp(-t^2/2) (CP-divisible, not a homogeneous semigroup). All correct.

## Suggested ordering for the novelty gate

1. Full-text reads that defeat or sharpen: Clifton-Hogarth 1995; Czerniawski 2020;
   Hausmann et al. 2308.10967 and Ludescher et al. 2607.24976 (exact interaction
   hypotheses); Brightwell et al. gr-qc/0210061 and Surya-Zalel 2003.11311 (proofs).
2. Independent defeat searches for RC-3 and RC-5.
3. Only then an independent reviewer challenges a one-page claim contract per surviving
   candidate (NOVELTY.md gate).

## Update after the full-text reads and the RC-3 / RC-5 defeat searches (2026-10-19)

Sources: fulltext-reads-clocks.md, fulltext-reads-causal-sets.md,
rc3-and-clifton-czerniawski.md, rc5-memory-criteria.md. All are subagent reads of arXiv HTML
or open-access PDF, not coordinator re-reads, and none is a novelty finding.

| Contract | Status after the reads | Why |
|---|---|---|
| RC-1 | Sliver not closed by Ludescher et al. or Hausmann et al. Still unread: Rijavec, Smith-Ahmadi body, Garmier et al., Hoehn-Smith-Lock interaction passages | Ludescher's "interacting" result is one worked example with a commuting interaction and an ideal Z_n clock; its local-clock interacting case is outside its framework. Hausmann et al. compare two formulations (TO vs PM) on a continuous bounded-spectrum clock, not a Z_N clock and not three pictures. Lane `kb-clock-interactions` is reading the remaining neighbours |
| RC-2 | Czerniawski does not contain the premise lattice; Clifton-Hogarth still unread (paywalled) | Czerniawski gives a deductive formalization and informal blocking checks, not subset analysis or countermodels, and shows transitivity is dispensable (p.107), which partly pre-empts one axis. Lane `kb-putnam-ablation-prior` tries to find a readable copy and other formal ablations |
| RC-3 | Partly occupied; contract text needs a corrected Delta | 2007.00580 already says sector coherence is inaccessible to relational Dirac observables and equivalent to a mixture; 2604.00092 gives the normalization obstruction and sector-wise remedy in a free-particle case. The narrow remainder is non-twirled conditioning instruments with an explicit external phase reference. Lane `kb-sector-conditioning` reads 2604.00092 and related in full |
| RC-4 | Part (a) retired as written; keep only the sliver | For fixed-covariance classical growth, the labelled outcome given the final unlabelled poset is uniform over natural labellings, independent of the growth parameters, so birth-order data are ancillary. This is the coordinator's short derivation from the stated path-independence property, finite stage only, needing independent checking. The open region is dynamics where path independence fails, quantum or complex-amplitude growth, and observer-access models. Lane `kb-csg-quantum-boundary` reads that region |
| RC-5 | Partly occupied; Eq. (10) audit answered provisionally | 2606.08595 Eq. (10) is a perturbative time-convolutionless memory-kernel statement that tests none of the four criteria; general separations of the criteria are published. Remaining case: a qubit system with a finite clock under linear (unnormalized or fixed-reference) conditioning, computing divisibility, backflow and the process tensor exactly. Lane `kb-relational-markov-audit` is auditing 2606.08595 |

Net: none of the five contracts is shown novel, none is shown dead outright, and three
(RC-3, RC-4a, RC-5 as generic separation) shrink to narrow remainders. The honest next step
is the independent `novelty-audit` (running), reading these notes as inputs, then a one-page
claim contract per surviving remainder.
