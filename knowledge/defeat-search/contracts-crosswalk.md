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
