# Claim contract: clock content

10 November 2026. Coordinator session (Claude Code, Fable 5.2), at the user's request.
A research proposal under the gate in [NOVELTY.md](../../../knowledge/NOVELTY.md).
It is **not** a result. It has not been challenged by a reviewer who did not propose
it, which the gate requires before any implementation. No temporal ontology is
selected.

Inputs: [local-clock note](../../stein-gr/local-clock/RESULT.md) and
[fixing note](../fixing-exchange/RESULT.md), both self-reviewed only.

## 1. Exact question and proposed statements

**Question.** Are the conditions under which a class of admissible worlds supports
(a) a shared present, (b) an intrinsic time orientation and (c) a fixed past with an
open future three independent conditions, or grades of one?

**Definitions.** An admissible class is a restriction-closed class of spacetimes
(possibly with fields) together with its lawful histories.

- An **order clock** is a nontrivial local clock in the sense of the local-clock note:
  an isometry-invariant function of local germs, monotone along timelike curves in
  every member. An **unoriented** order clock is monotone in one of the two time
  directions on each connected region where it is not constant, with the direction
  read off the clock.
- A **content imbalance** at a standpoint b is info(I⁺(b)) ≠ info(I⁻(b)) in the sense
  of the fixing note: strict inclusion of the vanishing spaces K in the linear case,
  or unequal entropies of equal-resolution readings under a stated measure.

**Statements, with their present status.**

| # | Statement | Status |
|---|---|---|
| S1 | A non-universal local becoming that reaches outside the causal past exists if and only if the class has an order clock | Proved with disjoint unions; one direction in the connected category (local-clock note, Theorem 4) |
| S2 | For discrete readings of a stationary class there is no content imbalance between equal-length bases. So a content imbalance implies that the distribution of the reading depends on time, which is a statistical clock | Proved; elementary (fixing note, Propositions 4 and 7) |
| S3 | S2 fails for exact fixing at infinite precision | Proved by example (doubling map) |
| S4 | An order clock does not imply a content imbalance | Proved by example: Minkowski spacetime with a scalar of timelike gradient has a clock, and a linear test field on it has none |
| S5 | **Alignment conjecture.** Where a class has an unoriented order clock and a content imbalance, both defined from the same structure, the open side is the side toward which the clock advances | **Retired as stated after the test in §8.** The sign was a convention and the content was cone geometry. Replaced by S5′ |
| S5′ | For a linear field with finite propagation speed and a local cutoff, the imbalance between the two cones of a standpoint is the difference of the cone sizes, and the orientation it defines points toward the larger cone. An initial singularity truncates the cone on its own side | Supported by the lattice count in §8 in 1+1 dimensions. Not a theorem here |
| S6 | **Grades.** Classes sort into: no clock; clock without imbalance; clock with imbalance. These carry the structural signatures of block, moving-spotlight and growing-block descriptions respectively | A classification proposal. S1–S4 show the three grades are non-empty and distinct. The matching to ontologies is a bridge premise, not a theorem |
| S7 | **Level-relativity.** One physical theory can have grade 0 at the level of its fundamental class and grade 2 at a coarse-grained or boundary-conditioned class | Open. No worked example |

The proposal stood or fell on S5 and S7. S5 has now fallen (§8). What is left is S7, and S6 without it is a relabelling.

## 2. Nearest predecessors

None of these was read for this contract. Each entry says what must be checked.

| Predecessor | Their claim, as understood | Difference to test |
|---|---|---|
| Callender, *What Makes Time Special?* (2017). Discovery depth: publisher description and one review snippet | Time is distinguished from space by informational features of the laws; manifest time is not fundamental | Whether he already ties a shared present and the open future to one invariant of the solution space. If so, S6 is his |
| Crutchfield, Ellison and Mahoney, arXiv:0902.1209 and arXiv:1107.2168. Snippet depth | For stationary processes, past–future mutual information and entropy rate are time-symmetric, while causal-state structure is not | S2 is theirs as mathematics. They also have an asymmetry that survives stationarity (causal irreversibility), which S6 ignores and may need |
| The paper's own clock-equipped rival (§`sec:becoming-rival`), with Markosian, "The Open Past" (1995), snippet depth | Adding a time function gives local shared presents; an open future has an open past as its price | S1 and S2 are the exact forms of these two. The proposal adds only their conjunction and S5 |
| Also to check: Rovelli (thermal time; perspectival arrow), Price (1996), Ismael on perspectival openness, Earman (1986) ch. II | Temporal asymmetries as perspectival or boundary-condition effects | Whether any of them states a grade structure or an alignment claim like S5 |

## 3. What would change relative to those predecessors

If S5 and S7 hold: the shared present, the time orientation and the fixity asymmetry
would be shown to co-vary under one parameter of the admissible class, with exact
criteria for the first (S1) and third (S2), instead of being treated as separate
perspectival or emergent effects. The practical change for this project is that time
orientation stops being an input to Part I, which is the first gap in
[PARITY_MAP.md](../../PARITY_MAP.md).

If only S1–S4 hold: nothing changes beyond the two notes.

## 4. Smallest reproducible examples and verification route

| Example | Shows | Verification |
|---|---|---|
| Closed dust model, massive linear field | Before maximum expansion the future is the open side and density falls toward the future. After it both reverse. S5 holds there | Compute F(I⁺(b)) directly from the kernel analysis behind Theorem `thm:massive`, without the mirror proposition |
| Three-state irreversible Markov chain in `fixing-exchange/check_exchange.py` | S2: forward and backward conditional entropies agree when stationary and differ by the entropy change otherwise | Already runs. Rerun with a different chain |
| Doubling map | S3 | By hand |
| Minkowski with a clock scalar | S4 | By hand |
| **Decisive test for S5:** spatially flat dust FLRW expanding forever, linear field, with a stated ultraviolet cutoff | Prediction: the future is the more open side at every standpoint, by an amount that grows with epoch | Not done. Needs a mode count for I⁻(b) and I⁺(b) at fixed comoving cutoff. A named task with its own review |
| **Second test:** de Sitter spacetime | No curvature clock (constant curvature). Prediction: no intrinsic alignment, although event horizons make both sides open | Not done |

An independent check must come from a reviewer who did not write the two notes, and
preferably from a different model family, since same-model review has shared failure
modes.

## 5. What would show the claim wrong, trivial, known or irrelevant

- **Wrong.** A class with an unoriented order clock and a content imbalance whose open
  side lies against the clock (kills S5). A class with a content imbalance at finite
  resolution and no clock of any kind (kills S2; would be an error in an identity).
- **Trivial.** In the closed dust model reflection symmetry forces both arrows to flip
  at the midpoint, so only the sign agreement is evidence, and one sign in one model is
  weak. If the FLRW test shows the alignment follows merely from "the larger cone is
  on the low-density side" in every big-bang model, S5 is a restatement of cone
  geometry and should be called that.
- **Known.** Searches to run before any further work: Callender (2017) chs. on Cauchy
  time and on laws; Rovelli on thermal time; "causal irreversibility" in computational
  mechanics; PhilPapers for "moving spotlight" with "entropy" or "clock"; the
  cosmic-time presentism literature for locally defined cosmic clocks. Any statement of
  a grade structure with a shared-present criterion and a fixity criterion defeats the
  novelty of S6.
- **Irrelevant.** The matching in S6 is to structural signatures. A defender of the
  growing block can accept every statement and deny that growth is a matter of clock
  content. The paper already holds that nothing here reaches existence, and this
  proposal does not change that. If no named view accepts the signature as part of its
  content, S6 has no philosophical consequence.
- **Dependent on an unargued premise.** Which class is admissible is the question of
  what laws are. Every statement is relative to that choice.

## 6. Kinds of novelty, kept apart

| Kind | Claim |
|---|---|
| Mathematical | None. S1 is a short argument on a known category. S2 is the chain rule of entropy |
| Formalization | None attempted |
| Physical | Only if the FLRW test gives a definite, cutoff-independent sign and rate |
| Philosophical | The conjunction: one parameter of the modal base grades three temporal structures usually argued separately, with exact criteria for two. Conditional on S5, S7 and the prior-art checks |

## 8. Outcome of the FLRW test, 10 November 2026

Script: [flrw_cone_count.py](flrw_cone_count.py). Self-run, unreviewed.

**Model.** Spatially flat FLRW is conformal to the half-space η > 0 of Minkowski
spacetime, and a conformally coupled massless field becomes the flat wave equation
there. The script uses the exact light-cone lattice in 1+1 dimensions, with the big
bang at row 0, a standpoint on row n and a last row T. The lattice spacing is a
comoving cutoff. Ranks are exact.

**Result.**

| Quantity | Value in every run |
|---|---|
| info(past cone) | 4n − 4 |
| info(future cone, up to row T) | 4(T − n) − 4 |
| common part | 0 |
| imbalance | 4(T − 2n) |

1. **The predicted sign holds.** With no last row the future is the heavier side at
   every standpoint, and the imbalance grows without bound.
2. **The reason is cone size and nothing else.** The imbalance is the number of
   lattice sites on the boundary of the future cone minus the number on the boundary
   of the past cone. Density never enters. With a last row at T the sign flips at
   n = T/2, which is the closed dust midpoint again.
3. **The two cones share nothing.** The common part is zero in every run. So in this
   model neither side fixes anything about the other. "Fixed past, open future" is
   false here in the exact sense. What is true is that both are open and there is
   more future than past.

**Judgment against §5.**

- The **triviality** condition is met. The alignment is "the larger cone lies away
  from the singularity", which is geometry.
- A second defect appeared while setting up the test. An unoriented clock has no
  preferred direction: "decreasing density" and "increasing density" are equally good
  conventions. So "the side toward which the clock advances" had no content. The
  orientation comes from the imbalance. The clock supplies only a local reading of
  where the standpoint sits.
- S5 is retired. S5′ records what the test supports.

**Consequences for the rest of the contract.**

- S6 survives only in a weaker form. Grade 1 is still a clock with no imbalance. Grade
  2 is a clock together with unequal cones, and its "open future" is a difference of
  amounts, not a fixed past. The closed dust model is special because its closed
  space lets the larger cone contain a Cauchy surface, which makes the smaller side
  exactly fixed.
- The thesis that the two notes measure one quantity is weakened. They are linked by
  S2 (an imbalance implies a statistical clock) and separated by S4 (a clock implies
  no imbalance) and now by this test (the imbalance in cosmology is set by global cone
  geometry, which a local clock can report but does not cause).
- S7 is untouched and is now the only open statement that could carry the proposal.

**Limits of the test.** One spatial dimension. Massless conformal field only: a
massive field violates Huygens' principle and could give a non-zero common part.
Comoving cutoff only: with a cutoff at fixed proper length the number of modes in a
comoving region grows with the scale factor, which would add to the future's weight
and was not modelled. Ten parameter pairs. De Sitter was not run.

## 7. Next bounded milestone

The FLRW mode count is done and S5 is retired (§8). Remaining: run the prior-art
searches in §5 at full-text depth for Callender and for the two computational-mechanics
papers, and decide whether S7 can be given a worked example. If not, close this
contract and keep only the two notes. Do not extend the paper on the
strength of this contract.
