# Full-text reads for candidate A / RC-4: causal-set sequential growth

Status: 2026-10-19. Independent Claude-subagent full-text read of Brightwell, Dowker,
Garcia, Henson, Sorkin (gr-qc/0210061v2) and Surya and Zalel (2003.11311, latest version;
version differences unchecked), plus the relevant sections of Rideout and Sorkin
(gr-qc/9904062). Locators are PDF page numbers; the papers have no numbered definitions.
Quotes are as reported by the subagent from its text extraction and were not re-read by the
coordinator. Surya-Zalel Secs. 2.2-3 (bounded-variation proofs) were skimmed only. Not a
novelty claim.

## What the papers contain

- Covariant observable (Brightwell et al. p.5; Surya-Zalel App. A p.22): a measurable set of
  labelled completed causets closed under relabelling. Their abstract: "answerable covariant
  questions ... correspond to measurable collections of causal sets which are independent of
  the labelings."
- Labelled-to-unlabelled step: the measure on unlabelled causets is the restriction of the
  labelled measure to the sub-sigma-algebra of label-invariant sets, equivalently the
  pushforward under the projection to isomorphism classes (Brightwell et al. p.4-5, p.16).
  It is not a separate theorem. Theorem 1 / Corollary 1 (p.6, p.8): stem sets generate the
  covariant sigma-algebra up to measure zero.
- Rideout-Sorkin p.9-10: labels are a "fictitious order of birth"; discrete general
  covariance is path independence ("the product of the transition probabilities along the
  links of gamma must be the same as for any other path arriving at C"); a statement like
  "when the causet had 8 elements it was a chain" is "meaningless before a certain birth
  order is chosen". They dismiss such statements by gauge fiat, not by derivation. Net
  arrival probability Prob_N(C) = W(C) P(C) (p.22).
- Brightwell et al. p.4 notes the dynamics does assign a probability to "is element 3 above
  element 1?" and calls it "not meaningful for us".
- Observers and records: nothing in any of the three papers. Stated open questions: whether a
  label-free dynamics would give a different physical measure, and whether relabellings are
  pure gauge (Brightwell et al. p.16-17); whether Bell causality can be formulated without a
  birth sequence (Rideout-Sorkin p.24-25).

## Consequence for RC-4(a) (hand derivation, coordinator)

Assume the property the papers state: for a naturally labelled causet c~ of n elements, the
probability of arriving at c~ equals P(C), a function of the isomorphism class C alone
(path independence / discrete general covariance, Rideout-Sorkin p.9, p.22). Then, conditional
on the final unlabelled causet C, the labelled outcome is uniform over the distinct natural
labellings of C, and so is the labelled prefix at any earlier stage m (it is determined by
the number of natural labellings of C extending it). This conditional distribution depends on
C only, not on the growth parameters t_k. So the unlabelled class is a sufficient statistic
for the dynamics' parameters and the birth-order data are ancillary: for a fixed covariant
growth law at finite stage, order-dependent records carry no information about which
dynamics (within the covariance class) produced the history beyond the distribution of the
unlabelled poset. Hence RC-4(a) restricted to fixed-covariance classical growth is, at the
level of this argument, an immediate corollary of path independence. That matches the
contract's own falsifier (iii) and the A defeat search. Limits: finite stage only; the
completed infinite case is not argued; this is the coordinator's short proof from the stated
property, not a published theorem, and it needs an independent check.

Finite check (coordinator, same day): `knowledge/defeat-search/csg_ancillarity_check.py`,
exact rational arithmetic, standard library only, n <= 5. With the Rideout-Sorkin transition
probabilities tau = lambda(w,m)/lambda(n,0) and two different coupling vectors, the 357
naturally labelled causets on 5 elements (63 isomorphism classes, matching the known counts)
each have a probability that is constant within its class; the statistic "element 3 is above
element 1" has an unconditional probability that differs between the two couplings
(0.754 vs 0.590) but a conditional law given the class that is identical on all 63 classes;
the labelled 3-element prefix has an identical conditional law given the final class. A
contrast law with label-dependent weights breaks path independence in 38 of 63 classes and
makes the conditional law parameter-dependent in 34 of 63. This supports the ancillarity
argument for the covariant family within that finite domain. It is not a proof for general n
or for the completed infinite case, and it tests the argument's premise (path independence of
the RS family) only numerically.

## What stays untouched by these papers

Comparison of different dynamics (non-Markov, order-dependent, or quantum complex-amplitude
growth where Surya-Zalel show the measure may fail to extend to the covariant algebra) that
share a final-poset distribution but differ in labelled path measure; any embedded-observer
or bounded-record access model; any observer-access hierarchy. The wider causal-set
literature and gr-qc/0202097 (on birth order and the problem of time) were not read.
