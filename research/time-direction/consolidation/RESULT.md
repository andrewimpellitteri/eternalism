# Two kinds of arrow: one consolidation of the direction-of-time lanes

18 November 2026. Coordinator session (Claude Code, Opus 5.5), at the user's request. This note has
not been independently reviewed: all review so far comes from one model family. The mathematics is
elementary, so no priority is claimed. No ontology is selected. New checks are in
[check_two_arrows.py](check_two_arrows.py). Every other claim points to the lane that established it,
at the status that lane gives it.

## The table

| Law class | Exact fixing | Amount (openness, entropy) | Values (who follows whom) | Production direction (homogeneous description) | Lane |
|---|---|---|---|---|---|
| Orientation-free laws, class closed under reversal (GR, classical fields, massive fields) | Mirrors exactly | Mirrors | Mirrors | None | [ARROW_READ](../ARROW_READ.md) §1, [review](../review/RESULT.md) |
| Same, but the geometry has an edge (closed dust) | Arrow toward the larger side, reversing at maximum expansion | — | — | — | [fixing-exchange](../fixing-exchange/RESULT.md) §2 |
| Deterministic reversible (finite permutations) | Reciprocal | Global entropy constant; an arrow appears only in the marginals of parts | Mirrors | **None at micro level, even with a boundary**: both directions are homogeneous. Macro: generically neither (audit A2) | [m-arrows](../m-arrows/RESULT.md) check 2, [records](../../records-asymmetry/RESULT.md) Results 1–2 |
| Stationary chain, reversible kernel | Reciprocal | Mirrors (C1) | Mirrors | None | [stochastic-fixing](../stochastic-fixing/RESULT.md) |
| Stationary chain, non-reversible kernel (biased cycle) | Reciprocal | **Whole slices mirror (C1); records between parts do not** | **Arrow**: the two-time joint law is not symmetric | **None**: K forward and K* backward are both homogeneous (C2) | stochastic-fixing; C1, C2 |
| One boundary, positive kernel (reversible or not) | Reciprocal | Arrow. Relative entropy to equilibrium falls away from the boundary; Shannon entropy rises away from it only if the kernel is doubly stochastic; **openness has no fixed sign** (C4) | If the kernel is non-reversible | **Away from the boundary, uniquely** | m-arrows lemma; C4 |
| Boundary in the middle (Janus) | Reciprocal | Arrows outward on both sides | — | Outward on both sides; no single orientation is homogeneous | m-arrows check 4, [records](../../records-asymmetry/RESULT.md) Result 5 |
| Two boundaries (bridge) | Reciprocal | Records ambiguous: equal past and future information at every interior time | — | **None either way** (C3) | records Result 10, [TWO_BOUNDARIES](../../records-asymmetry/TWO_BOUNDARIES.md); C3 |
| Collapse with reversal-invariant operators | — | Mirrors from a maximally mixed start; the asymmetry is the boundary | — | — | [settling](../../agentic-philosophy/settling/RESULT.md) Prop. 1 |
| Causal sets: percolation versus generic growth | — | Percolation mirrors at every stage | Generic growth: the measure is not reversal-invariant | Birth order is gauge in both | [growth-arrow](../growth-arrow/RESULT.md) |
| QFT with CPT; the Standard Model with a primitive matter label | Mirrors under CPT | — | Arrow relative to the matter label (T violation) | — | [cpt-arrow](../cpt-arrow/RESULT.md) |

"—" means the lane did not examine that column.

## The simple statement

Within finite Markov worlds, together with the closure results for fields, everything above reduces
to four claims. Two more were added the same day, and claim 6 replaces the "law" source in claim 2.

1. **One mirror.** If the whole specification is invariant under a time reflection composed with some
   relabelling, every arrow vanishes. The specification is the laws, the admissible class, the
   measure and the labels. Six lanes are this theorem in different dress.
2. **Two ways to break the mirror give two kinds of arrow.**
   - A **boundary** means non-stationarity, an edge in the geometry, or a prepared state. It gives
     arrows of *amount*: how much is open, recorded, or fixed.
   - A **law** means a non-reversible kernel, generic growth, or T violation relative to a label. It
     gives arrows of *value*: which states follow which.

   A law arrow on its own leaves every amount *of whole time slices* mirror-symmetric (C1: all 63
   time sets, any kernel). **Revised the same day:** it does not leave amounts *between parts*
   symmetric. In stationary non-reversible worlds a device records an event's past and not its future,
   with no boundary present ([chance records](../../records-asymmetry/chance/RESULT.md), R0 and R1).
   Exact fixing is reciprocal in every class, so it sees neither kind of arrow.

   **Corrected 19 November ([claim audit](../claim-audit/RESULT.md), A3).** Whole-slice symmetry
   holds for *Markov* descriptions only. A stationary process that is not Markov, which includes
   generic coarse-grained images, can give a set of times a different entropy from its mirror image,
   with no boundary. The smallest case found is a 6-cycle with three labels: 2.585 bits against
   2.252. Under stationarity alone, only single contiguous stretches of time are guaranteed to
   mirror.
3. **The direction of production is a boundary arrow, not a law arrow.** A chance law *with a
   strictly positive kernel* can be described homogeneously in exactly one direction, the one leading
   away from a single boundary. **Scope corrected 19 November** ([claim audit](../claim-audit/RESULT.md),
   A1). With zero entries, the backward description of a world with a sharp start was homogeneous
   over the whole run in 56 of 400 random kernels. In 65, it was homogeneous at some step while the
   distribution was still changing.
   - In a stationary world, even with a non-reversible kernel, both directions are homogeneous. So
     the asymmetric law fixes *no* production direction.
   - With two boundaries neither direction is homogeneous.
   - At a Janus point production runs outward, in both directions.
   - Under deterministic reversible laws homogeneity never picks a direction *at the micro level*.
     At the macro level it picks one only in special cases where the macro process is exactly
     Markov, as in [macro bridge](../macro-bridge/RESULT.md) B3–B4. Take 300 random coarse-grainings
     of reversal-symmetric permutations, each started from a macro boundary: 291 are homogeneous in
     neither direction, 9 in both, and none in exactly one (audit A2). So for generic coarse
     descriptions the homogeneity criterion gives no production direction at all.
4. **Boundary arrows are located, but most of them are not signed.** Stationarity forces every amount
   arrow to vanish. A boundary guarantees only one monotone quantity: relative entropy to equilibrium,
   which falls away from the boundary. Shannon entropy rises away from it only if the equilibrium is
   uniform. The arrow of openness, how much more open the future window is than the past window, can
   point toward the boundary. That happened in 95 of the doubly stochastic test windows, by small
   amounts. So "a low-entropy start makes the future more open" is not a theorem in this class. It is
   a further fact about particular systems.

5. **In chance worlds the record arrow and the production direction have different sources, so they
   can disagree.** Records come from who copies whom, which is the law. Production comes from where
   the boundary is. With the boundary at the end, production runs from the end while devices record
   the earlier side ([chance records](../../records-asymmetry/chance/RESULT.md), R4). This survives
   in a deterministic world whose micro law is exactly time-reversal symmetric
   ([macro bridge](../macro-bridge/RESULT.md), B4).
6. **What was called a law arrow is a label arrow.** A deterministic, time-reversal-symmetric micro
   law with no boundary yields, through a coarse-graining that the reversal map does not preserve,
   exactly a non-reversible macro chance law with records ([macro bridge](../macro-bridge/RESULT.md),
   B1–B2). By Friedman–Ornstein, known only at secondary depth, every mixing finite Markov chain is
   time-reversal symmetric as a measure-preserving system. So within scope, arrows have two sources:
   - **boundaries**, which give amounts for whole slices and production;
   - **labels or coarse-grainings**, which give values and records.

   Claim 2's "law" row should be read as "labels".

   **Revised 19 November ([claim audit](../claim-audit/RESULT.md)).** The amount/value split does
   not line up with the two sources. Labels can also give amount arrows: whole-slice entropies of
   non-contiguous time sets, in stationary non-Markov descriptions (A3). What remains specific to
   boundaries, within scope, has two parts:
   - the relative-entropy gradient, which needs non-stationarity by definition and never rises away
     from the boundary, kernels with zero entries included (A6);
   - the production direction, for positive Markov descriptions.

   If the reversal map preserves the coarse-graining, every macro arrow tested vanishes (A4: 149 of
   149). That confirms claim 1 at the macro level.

## What follows for the ontologies

- **Growing block and Maudlin-style production.** Both need a production direction. In scope, the only
  physical thing that supplies one is a boundary. The two pictures are "the world began and grows" and
  "the world has an edge and is read away from it". They agree on every amount, every value and the
  production criterion. They differ only in whether the edge is a beginning of being. That difference
  is not physical in any instrument considered here. The question this lane was set up to answer,
  whether *begins* and *has an edge* differ, gets the answer: not in scope.
- **T violation and other law arrows** are the only candidates for an arrow intrinsic to the laws. But
  they are value arrows. They cannot ground the open future, records or production. So citing the weak
  interaction as evidence for passage, as Healey reports Maudlin does, invokes the wrong kind of arrow,
  unless a bridge premise is added that turns a value asymmetry into a direction of production.
- **Janus cosmologies** would need growth in two directions from one surface, or a growth direction
  that disagrees with the records on one side.
- **The "open future".** Even granted a boundary, the open future is not guaranteed by the boundary
  alone (claim 4). Fixing-exchange Proposition 3 says openness differs by H(c) − H(a). This note adds
  that the sign of that difference is not fixed by where the boundary lies.

## Where depth is still missing

Each of these could change a cell of the table:

1. **Records in chance worlds.** Done the same day: the record arrow is a law arrow, and it can
   disagree with production (claim 5). Still open: redundant traces, and longer lags.
2. **Kernels with zero entries**, between permutations and positive kernels: where does homogeneity in
   both directions begin?
3. **From deterministic to stochastic.** First pass done in [macro bridge](../macro-bridge/RESULT.md):
   a symmetric micro law gives a macro chance arrow through the coarse-graining, with no boundary.
   Still open: a many-part model with a Past-Hypothesis-like start. The original framing was:
   Albert's macro-dynamics is a coarse chance process.
   Conjecture: if it is approximately Markov and positive, claim 3 gives its production direction away
   from the Past Hypothesis. Ebtekar's stochastic automata (abstract only) look like the test bed.
4. **Generic causal-set growth.** It always has a beginning. Can its law arrow be separated from its
   boundary arrow, and is either one an amount arrow?
5. **Non-Markov stationary processes.** C1 is checked for Markov chains only.
6. **Classifying T violation as a value arrow.** This is a conjecture by analogy with C2. It has not
   been derived from the CPT lane.

## Limits

- The new checks cover 3-state chains, times 0 to 5 or 6, random kernels and floating point with a
  tolerance of 1e-9.
- C4 reports counterexamples. It does not measure how common or how large they are in physical
  systems.
- "Amount" and "value" are this note's own sorting, extended from the instrument sort in
  stochastic-fixing. They are not established terms.
- The bearing on ontology rests on the bridge premises named in [m-arrows](../m-arrows/RESULT.md) (H,
  M, P). It also rests on treating "the edge is a beginning" as the only remaining difference. A
  defender of growth can accept that and say it is the difference that matters. Nothing here refutes
  that.
