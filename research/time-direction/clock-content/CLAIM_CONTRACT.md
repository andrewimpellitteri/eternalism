# Claim contract: clock content (closed)

10 November 2026. Claude Code (Fable 5.2), at the user's request. A proposal under the
gate in [NOVELTY.md](../../../knowledge/NOVELTY.md). It was tested the same day and is
closed. Nothing here is a result beyond what the two notes it draws on already state:
[local clock](../../stein-gr/local-clock/RESULT.md) and
[fixing](../fixing-exchange/RESULT.md).

## The proposal

Both notes locate temporal structure in the class of admissible worlds. The proposal
was that they measure one thing, how far a local state can tell what time it is, and
that its grades match the structural signatures of block, moving-spotlight and
growing-block descriptions.

## Statements and outcomes

| # | Statement | Outcome |
|---|---|---|
| S1 | A local becoming reaching outside the causal past exists iff the class has an order clock | Proved in the local-clock note, with disjoint unions |
| S2 | A stationary class has no information imbalance between equal bases | Proved; it is Crutchfield, Ellison and Mahoney's |
| S3 | S2 fails for exact fixing at infinite precision | Proved by the doubling map |
| S4 | A clock does not imply an imbalance | Proved: Minkowski spacetime with a clock scalar |
| S5 | The open side is the side the clock advances toward | **Retired.** See below |
| S6 | Three grades match three ontologies' signatures | A relabelling without S5 and S7 |
| S7 | A theory can be grade 0 fundamentally and grade 2 when coarse-grained | Shown only in a textbook toy |

## The two tests

**Flat FLRW mode count** ([flrw_cone_count.py](flrw_cone_count.py)). Light-cone
lattice in 1+1 dimensions, big bang at row 0, standpoint on row n, last row T.
Information in the past cone is 4n − 4, in the future cone 4(T − n) − 4, and the two
cones share nothing. The predicted sign held, for a trivial reason: the imbalance is
the difference in cone sizes. Setting up the test also showed that an unoriented clock
has no preferred direction, so "the side the clock advances toward" was a convention.
S5 is retired.

**Kac ring** ([kac_ring.py](kac_ring.py)). Uniform ensemble: forward and backward
openness of the macrovariable are equal. All white at t = 0: the difference is +1.45,
+0.58, +0.18, +0.08 bits and then about zero, mirror-symmetric about t = 0, and
negative near the recurrence. So a constrained slice plus a macrovariable gives an
arrow of openness that points away from the slice on both sides and dies out at
equilibrium. This is standard, and the binning of the macrovariable was chosen after
seeing a parity artefact.

## Verdict

The unification is weaker than proposed. The two notes are linked one way (S2) and
separated two ways (S4, and the cosmological imbalance being cone geometry). Albert and
Price already locate the asymmetry of openness outside the laws, and neither states a
grade structure. Callender, Rovelli, Ismael and Earman were not read. Do not extend the
paper on the strength of this contract.
