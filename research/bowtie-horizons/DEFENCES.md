# Defences against the main objections to the screening results

28 October 2026, native Claude, task `bowtie-horizon-rationale`. Covers the
two dialectical weaknesses of RESULT.md and SCREENING.md: the
location/composition clause, and the "treat (BO) as primitive" reply. The
prior-art and premise-L weaknesses are being audited separately
(`prior-art-prediction`, `prior-art-bst`, `prior-art-becoming`,
`screening-review`). Text below cites C&R ch. 9 (user-supplied PDF, read
full text for the pages named) and *Replies to Critics* §8. Analysis is ours
and unreviewed.

## 1. The location clause, read with C&R's own principles

**Source facts (authors' claims, full text).**
- *Replies* p.489: "what exists in spacetime is what has the causal
  potential to shape the future (or else serves as a spatiotemporal location
  for things that do)".
- Ch. 9 (D21), p.144: a resident m is in spacetime and, everywhere, if m is
  located at x and x exists then m exists; and if m exists, it is located at
  some (existing) point.
- (A26R), p.144: a spacetime point is located exactly at itself.
- p.151: "Mereological fusions, if they exist, exist whenever, and wherever,
  one of their parts exist"; p.151–152: such fusions are "located wherever
  any of their parts are located".
- (P2R): at s, no point of s's strict causal future exists.

**Proposition D1 (over-generation).** Read the location clause as a
sufficient condition. Assume (i) the fusion s ⊕ z of the point s and a point
z ∈ J⁺(s)\{s} exists, and (ii) a fusion has causal potential if some part
does. Then z exists at s, contradicting (P2R).

*Proof.* s exists at s and has causal potential (any point can affect its
own strict future, which is nonempty). By p.151 the fusion exists at s, and
by (ii) it has causal potential. By p.151–152 and (A26R) it is located at z.
The clause then makes z exist at s. ∎

So the clause cannot be combined with "some-part" inheritance and the
existence of mixed fusions unless the future is excluded by hand. But a
clause amended to "…or serves as a location, outside the strict future, for
things that do" makes every elsewhere point x exist via the fusion s ⊕ x.
It then just restates (BO) together with (P2R): the domain is fixed by the
explicit future exclusion, and causal potential does no selecting.

**The remaining readings.**

| Reading of fusion potential / composition | Domain the clause yields | Status |
|---|---|---|
| Some part suffices; mixed fusions exist | Includes future points | Contradicts (P2R) (D1) |
| Same, but future excluded by hand | D_BT exactly | Recovers (BO) by stipulation; potential idle |
| All parts must have potential | Locations of potent parts only: D_pot | Clause adds nothing beyond D_pot |
| Restricted composition (e.g. persisting bodies) | D_pot plus locations of bodies with potent stages | Matter-dependent; not uniform over the elsewhere; (P1R) still fails at a threshold in ΛCDM (RESULT §6) |

No reading both respects (P2R) and makes causal potential select exactly
D_BT. This covers the readings we could identify, not every conceivable
composition principle. A reviewer should look for a principled restricted
composition that yields exactly D_BT; we know of none.

Note that C&R's own (D21) does **not** say that a resident's existence makes
all its locations exist. The over-generation comes only from the *Replies*
location clause, read as sufficient. A defender can therefore drop or
restrict that clause without touching the logic of ch. 9.

## 2. Treating (BO) as primitive: what C&R's stated considerations secure

The view stays consistent if (BO) is taken as primitive. The question is
whether C&R's offered considerations reach the events at issue. Those events
are D_BT(s) \ H(s), which is nonempty in exact dust + Λ (RESULT Prop. 9;
coordinator EXACT_DUST_LAMBDA.md).

| Consideration (locator) | What it secures at s | Reaches D_BT \ H? |
|---|---|---|
| Causal-potential reading (p.139; *Replies* p.489) | D_pot(s); with persistence, H(s) | No, by definition |
| Persistence of perceived limbs (pp.151–152) | Points in J⁺(y) \ J⁺(s) for limb locations y ∈ J⁻(s). All are elsewhere points sharing a past with s, so they lie in H(s) by Prop. 8 (causally simple case) | No |
| Rebuttal of Savitt achronality and Putnam-type principles (pp.152–156) | Defensive only: shows bow-tie *may* reject (3), (4), (BO+) | Not an argument for including any event |
| Recapture of classical views via (PR1), (PR2) (pp.156–161; App. 3 unread) | Under (PR1) the elsewhere shrinks to a simultaneity hypersurface. In that prerelativistic order any two points have a common later point, so the order is future-directed and D_pot = H = D_BT (Prop. 1 is purely order-theoretic) | No: recapture cannot discriminate D_BT from H |

**Conclusion (bounded).** On the pages read, every consideration C&R offer
for bow-tie is already satisfied by H, or by D_pot, wherever it applies. In
an exact Einstein–dust–Λ model, the events D_BT \ H are included by (BO)
alone. So the reply "(BO) is primitive" is available, but it concedes that
these events are included without any of the authors' stated reasons. That
is the precise cost.

Limits:
- Appendix 3 (recapture details) is unread. The recapture row relies on the
  main-text sketch (pp.157–159) and the order-theoretic Prop. 1.
- The persistence row uses the authors' own description of the limbs case.
  A larger extended observer could need more points; the project's
  `research/future-domain-persistence/` result found the argument does not
  force the full elsewhere.
- C&R say the bow-tie realm is "the best version of relativistic GBT"
  (p.150). Comparative-virtue arguments not listed above could exist
  elsewhere in the book.

## 3. Status of the four candidate claims after these defences

| Claim | Defence status |
|---|---|
| X1 instantaneous potential violates (P1R) without pairwise common futures | Holds for the point-level reading. The location clause cannot rescue it without D1 or stipulation |
| X2 historical repair misses D_BT \ H in dust + Λ | Holds. Reached only by primitive (BO) (§2) |
| X3 D_pot is the minimal screening realm | Mathematical; prior-art audit pending (likeliest overlap: Geroch prediction, BST) |
| X4 rigidity line at D_pot | Conditional on premise L; review pending |

Needed from the user: C&R *Nothing to Come* Appendix 3, and any other
chapter where the bow-tie preference is argued, to close the remaining
source gate.
