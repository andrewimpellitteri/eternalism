# CANDIDATE — Route B (modal nontriviality): the dense comb refutes Theorem 1 of Müller 2020 as stated

Lane: `result-search-round1/modal-density`. Date: 2026-10-31. Worker: ontology-modal-density-search (GLM-5.3-flash, OpenCode headless). Status: **worker submission for independent review — not accepted completion, not a novelty verdict.**

---

## 1. The literal source hypothesis

Primary source (read in full, open-access version of record):
Thomas Müller, "Defining a Relativity-Proof Notion of the Present via
Spatio-temporal Indeterminism", *Foundations of Physics* **50** (2020) 644–664,
DOI 10.1007/s10701-019-00267-x (published online 14 June 2019; CC-BY 4.0).

The hinge is **Theorem 1** (pp. 661–662), quoted exactly:

> "For full precision, let us call a BST structure *featureless* if either (i) it
> contains just a single history (i.e., no indeterminism), or (ii) it has at
> least one history consisting wholly of choice points and in which there are no
> modal correlations." (p. 661)
>
> "**Theorem 1** Let ⟨W,<⟩ be a BST structure that is not featureless. Then for
> any history h ∈ Hist(W), the relation of co-presentness ∼ restricted to h,
> ∼|h, is a non-trivial equivalence relation on h, i.e., *neither the identity
> nor the universal relation* on h, defined wholly in terms of the
> relativistically sound basic notions of BST." (pp. 661–662)

The hypothesis class is "BST structure" **as defined in the paper's own
Definition 6** (p. 657): a non-empty partial ordering that is (a) dense and
without maxima or minima, (b) continuous — each lower-bounded chain has an
infimum in W, each upper-bounded chain has a supremum-in-h for each history
containing it — and (c) satisfies the prior choice principle (a lower-bounded
chain O ⊆ h1∖h2 yields a choice point c < O maximal in h1 ∩ h2). Footnote 23
(p. 657) explicitly omits Weiner's postulate "to keep matters simple". No proof
of Theorem 1 is given in the paper; it follows two finite illustrations
(Figs. 5–6) and the parenthetical "(barring the deterministic one-history case)".
Footnote 26 (p. 661) adds: "The identity relation would result **if every event
were a choice point** and there were no modal correlations."

The supporting BT-level claim (§2.3, p. 655) is: "The non-overlapping regions of
co-presentness are exactly those intervals on the tree of branching histories
that lie between two **consecutive** choice points. Unless every moment is a
choice point, some regions of dynamic co-presentness contain more than one
moment."

## 2. Exact candidate: the dense comb

W = ℝ_T ∪ ⋃_{q∈ℚ} (q,∞)_q, where ℝ_T is the trunk (usual order) and each
offshoot (q,∞)_q is a disjoint copy of the reals above q, ordered so that
t_T < r_q iff t ≤ q and q < r. No other comparabilities. This is exactly the
brief's stress test: real trunk, one deterministic offshoot attached at every
rational, no other branching.

**Maximal directed sets (histories).** Any two trunk points t > q and offshoot
points r_q, s_q with q < t have no common upper bound in W, so no directed set
mixes them. Hence Hist = {h_T} ∪ {h_q : q ∈ ℚ}, with h_T = ℝ_T and
h_q = {t_T : t ≤ q} ∪ (q,∞)_q. Every event belongs to a history.

**Containing-history sets.** H(t_T) = {h_T} ∪ {h_q : q ≥ t}; H(r_q) = {h_q}.
For t < t′, density of ℚ gives h_p ∈ H(t_T)∖H(t′_T) for t ≤ p < t′, so the
H-sets of distinct trunk events are **strictly nested** (all infinite), and each
offshoot event has a singleton H. **Every two trunk events have different
history sets** — the comb's defining feature.

**Choice points.** By the paper's split definition (§3, p. 658: e is a choice
point for h1, h2 iff e ∈ h1 ∩ h2 and h1 ∩ h2 contains no event above e):
h_T ∩ h_q = (−∞,q]_T has maximum q, so h_T ⊥_q h_q and **the choice points are
exactly ℚ**. Irrational trunk events are in every containing history pair's
undivided part (for any pair h_p, h_q ∈ H(t) with p < q, the intersection
(−∞,p]_T contains events above t) — so **an irrational trunk event fails to be a
choice point** while trunk events pairwise differ in history sets. Both halves
of the brief's stress question hold.

**Clause-by-clause audit against Definition 6 (and the postprint postulates).**
All checks are symbolic hand proofs; no numerical grids were used (none are
admissible here, and none are needed).

- *Density, no maxima/minima:* between t_T and r_q with t < q use trunk
  midpoints; at t = q use the offshoot's own density (q_T < r′_q < r_q);
  within each copy use real density. Every event has events strictly above and
  below it. **Holds.**
- *Infima for lower-bounded chains:* a lower-bounded chain in W is a chain in a
  single history whose trunk part is bounded below in ℝ; its infimum is the
  corresponding real (in the trunk part), or q_T for chains starting in an
  offshoot, or the offshoot infimum β_q when attained. Chains unbounded below
  (e.g. (−∞,α)_T) have *no* lower bound in W, so the clause is vacuous for
  them. **Holds.**
- *Suprema-in-h:* for a chain C ⊆ h, the upper bounds inside h are h-events,
  and sup-in-h is the ℝ-supremum's copy (trunk chains: attained, since chains
  unbounded toward q are upper-bounded only by offshoot events, and sup-in-h =
  q when C = (−∞,q]_T). **Holds.**
- *Prior choice principle (chain version = Belnap 2003 Postulate 13-1, the
  paper's Def.-6 clause):* for O ⊆ h1∖h2 lower-bounded, the rational branch
  point c = min-branch is strictly below every element of O and is maximal in
  h1 ∩ h2. Checked for all pair types (h_T/h_q; h_p/h_q with p < q; h_q/h_T).
  **Holds.**
- *Beyond Def. 6, since the brief asks:* **Weiner's postulate** (Müller 2005,
  Postulate 4, p. 513: suprema of chains I, J ⊆ h1 ∩ h2 keep their order across
  h1, h2) — holds, because for I, J ⊆ (−∞,q]_T the suprema in h_T and in h_q
  coincide as reals ≤ q. **Historical connection** and generalized historical
  connection hold (all histories share the trunk). **No modal funny business**
  (Müller 2005 Definition 5): W contains *no* incomparable-but-compatible pair
  at all, so there are no space-like-related events and the condition is
  vacuously satisfied. The comb is a model of the **full Belnap 2003 postprint
  postulate set** (2-1, 4-1, 6-1, 7-1, 13-1, 13-5, 13-6, 13-8) and of Müller
  2005's Postulates 1 and 4.
- *Not featureless:* (i) fails — there are 1 + ℵ₀ histories; (ii) fails —
  irrational trunk events are not choice points, so no history consists wholly
  of choice points.

**Co-presentness on the trunk is the identity.** Computed directly, without
invoking the paper's Fact 4 circularly. By Definition 8 (p. 658), c ∈ cll(t_T)
iff some h ∉ H(t_T) splits at c from *all* of H(t_T); the only histories outside
H(t_T) are h_p with p < t, and h_p ⊥_c h′ requires c maximal in h_p ∩ h′, giving
c = p. Hence **cll(t) = ℚ ∩ (−∞,t)**. At a choice point c the partition Π_c of
H_c has two cells ({h_T} ∪ {h_q : q > c} undivided; {h_c} split off), so
CC(t) = {c ↝ Π_c(t) : c ∈ ℚ, c < t}. This set is injective in t (its index set
cll(t) strictly grows), so distinct trunk events are never co-present; offshoot
events share CC = {q ↝ {h_q}} only among themselves. Therefore
**∼|h_T = identity**, while ∼|h_q (q ∈ ℚ) is non-trivial (each offshoot is one
unbounded co-presentness class, as expected from the paper's own deterministic-
stretch verdict, §2.1 p. 651). Fact 4's ⇐ direction (H equal ⇒ ∼) holds in the
comb; the identity (*) H_e = ⋂Π_c(e) used in Fact 4's proof also verifies
directly — the failure is in **Theorem 1**, not in Fact 4.

**Verdict on the exact inference.** The comb satisfies every written clause of
Definition 6 and is not featureless, yet Theorem 1's conclusion fails for
h = h_T. **Theorem 1 of Müller 2020 is false as stated.** Footnote 26's
sufficient condition for identity ("every event a choice point") is also shown
incomplete: identity on an entire history results from *dense but non-total*
chanciness. At the BT level (§2.3): the literal existential sentence ("unless
every moment is a choice point, some regions … contain more than one moment")
**survives** the comb, because each offshoot (q,∞)_q is one multi-moment region;
what fails is the *characterization* sentence — there are no "consecutive choice
points" (ℚ is dense), and the actual regions are trunk singletons plus whole
offshoot tails — and the uniform reading under which a non-choice moment shares
a non-singleton present with neighbours fails for every irrational trunk moment.

## 3. Scope separation (as the brief requires)

- **Exact BT result (§2.2–2.3, Defs. 1–5):** the comb is a jointed, left-linear
  BT structure; Def. 5/Fact 2 give singleton dynamic presents for all irrational
  trunk moments; the "consecutive choice points" characterization is false; the
  literal existential sentence is true. No BT *theorem* of the paper is
  contradicted (none is proved); the §2.3 *picture* is refuted.
- **BST with the written axioms (Def. 6, §4):** Theorem 1 has a counterexample.
  This is the candidate's exact target.
- **Additional Weiner/location restrictions:** the comb satisfies Weiner's
  postulate, so adding Weiner (Def. 2.10(6) of BMP 2021) does *not* repair the
  theorem. Müller 2005's BST+S (space-time points, Def. 21) can also be
  consistency-strengthened onto the comb (all histories are order-isomorphic to
  ℝ), so the location route does not obviously repair it either — flagged as
  not fully audited.
- **BST_NF (BMP 2021 Def. 3.15):** the BST92 comb has choice points, and Fact
  3.17 (p. 64) proves BST_NF structures have none, so the comb is not BST_NF. A
  BST_NF analogue (branch events doubled into choice sets
  c̈_t = {t_x : x ∈ {T} ∪ ℚ_{≥t}}) *is* a BST_NF structure (all of Def. 2.10
  plus PCP_NF verified), but there *every* trunk event lies in a nontrivial
  choice set, so h_T is featureless under Def. 10.4(ii) and Theorem 10.1 is not
  violated. The monograph's rescope to BST_NF is exactly what blocks this
  pathology — but the monograph never states that the 2019 journal statement is
  false, and no erratum exists (bounded search).
- **Genuine higher-dimensional relativistic spacetime:** no claim is made. The
  comb is a one-dimensional branching order with no SLR events and no Minkowski
  embedding; nothing here is a counterexample to any theorem about Minkowskian
  Branching Structures (monograph ch. 9), and per the brief no higher-dimensional
  claim is attempted without proof.

## 4. Strongest rival

"The theorem's intended scope was always the relativistically sound, physically
motivated fragment, and the authors' own 2021 monograph restates the result as
Theorem 10.1 for BST_NF, where the comb cannot arise (choice points are
impossible by Fact 3.17); the 2019 formulation is a superseded slip, so there is
nothing to correct." *Reply:* (a) the 2019 journal version remains the published
statement of the result, its Theorem 1 is false in its own written hypothesis
class, its proof is absent, and no erratum or retraction exists; (b) the
monograph silently re-scopes without flagging the 2019 statement as false, and
its own proof sketch for Theorem 10.1 (p. 359) would not transfer to BST92 —
which is precisely the gap the comb exhibits; (c) the philosophical moral
(indeterminism grounds an extended dynamic present) is drawn from the theorem in
both publications, and the comb shows it needs an extra premise (below) that
neither the written axioms nor the featureless clause supply; (d) the BT-level
§2.3 picture is refuted inside the paper's own simpler framework, where no
BST_NF rescope is available. Rival compatibility does not decide explanatory
merit; it bounds the delta (Section 7).

## 5. Independently motivated premise whose absence the comb exposes

**(S) Sparseness of chanciness:** along each history, choice events are
order-isolated — between any two events of a history there is a stretch
containing no choice point. (S) is independently motivated physically (chancy
events are localized interactions in a continuous spacetime, generically not
densely packed along a worldline), is *not* derivable from BST's written axioms,
and is strictly weaker and different from featurelessness: the comb violates (S)
on h_T while failing both featureless clauses. Under (S), the paper's argument
strategy goes through at least in the no-funny-business BT/BST92 core: two
events e < e′ in h with no choice point between them have equal enabling
transition sets, hence are co-present. Whether a repaired theorem
(non-featureless + (S) [+ an anti-funny-business clause, since space-like
cause-like loci can otherwise distinguish events in a choice-free stretch]) is
*provable* in full generality is **not established here** — that is the flagged
open formal residue, not part of the claim.

## 6. Second case: the accumulation comb

Choice points at {1/n : n ≥ 1} on a real trunk, one deterministic offshoot at
each. Then (a) trunk points in (1/(n+1), 1/n] share their enabling-transition
sets, so non-singleton regions *return* in every gap — confirming that
choice-denseness, not branching per se, produces the collapse; and (b) for every
trunk point t ≤ 0 there is no choice point below it, so TR(t) = ∅ for the whole
ray (−∞,0]: one **unboundedly thick** dynamic present below the accumulation
point. Independent consequence: under the paper's own definitions, the thickness
of the dynamic present is maximally unstable — it can be point-like (comb) or
infinite (accumulation comb) under arbitrarily small redistributions of *where*
chancy events sit, with the written axioms and featurelessness unchanged.
Müller's closing suggestion (§5, p. 662) that empirical results "could be used
to provide a verdict about the size of the Now" therefore requires data about
the spatio-temporal **distribution** of chancy events, not only about
space-like correlations.

## 7. Nearest three predecessors — delta and gaps

1. **Müller 2020 (the source itself).** Delta: explicit counterexample showing
   Theorem 1 false in its own Def.-6 hypothesis class; the fn.-26 identity
   remark completed (identity also results from dense-but-non-total chanciness);
   the absent proof replaced by a clause audit. Gap: no claim against anything
   the paper proves (Facts 1–4 hold in the comb).
2. **Belnap, Müller, Placek 2021, *Branching Space-Times: Theory and
   Applications* (OUP), ch. 10 (read in full).** The monograph restates the
   result as Theorem 10.1 for BST_NF with the same featureless clause (Def.
   10.4) and adds "sticky MFB" (Def. 10.9) for partitioning/transitivity — but
   never says the 2019 statement was false, contains no comb or dense-choice
   counterexample, and its ch.-10 proof sketch does not transfer to BST92.
   Delta: the verification that the rescope is *necessary*, not cosmetic, plus
   the BT-level §2.3 refutation, which the monograph drops without retraction.
   Gap: the monograph's authors may have known the BST92 issue privately
   (silent-rescope risk; priority unresolved).
3. **Belnap 1992/2003 postprint (read in full).** Supplies the postulate set the
   comb satisfies (2-1 … 13-8), Fact 13-11/13-12 (density + infima ≈ ≡), and
   Fact 13-15's "yes and no" — none of which excludes the comb. Gap: the
   postprint predates the co-presentness project and says nothing about it.
   Fourth, at discovery depth only: **Placek 2019 (Synthese 198:3603–3624)** —
   a different modal present (his Present(e) is horizon-style, not CC-based),
   and his "single event" degenerate case is the *all-events-chancy* regime,
   the dual of the comb; not a predecessor of this counterexample, but the
   nearest independently published instability observation.

**Priority/erratum status:** bounded targeted search found no published
correction, comment, erratum, or prior statement of this counterexample
(citation chase of Müller 2020 at discovery level — 17 citations per OpenAlex;
BJPS citing list checked; monograph chs. 1–3, 10 read in full). Priority
remains **unknown**; the claim submitted is the *corrective verification*, not a
discovery claim.

## 8. Falsifier

The candidate is defeated by any one of: (i) a clause-level error in the
Section-2 audit (the likeliest suspects are the suprema-in-h clause at branch
points and the chain-PCP; both re-derived above); (ii) a published predecessor
or erratum stating the comb (or any Def.-6-satisfying, non-featureless structure
with ∼|h = identity); (iii) a source passage explicitly restricting Theorem 1 to
choice-isolated or manifold-embedded structures. Additionally, the *scope*
claims die if the BST_NF analogue of the comb turns out *not* to satisfy
PCP_NF, or *not* to be featureless under Def. 10.4(ii) — both are load-bearing
for Section 3's separation.

## 9. Is a referee packet warranted?

**A short correction note is warranted; a full novelty-referee packet is not.**
The result is bounded and checkable: Theorem 1 of a published FoPh paper is
false as stated under its own Definition 6; the minimal repair is to add a
sparseness clause (Section 5) to the featureless definition — or, as BMP 2021 in
effect does, to rescope to BST_NF, which should then be flagged as a correction
of the 2019 statement; the §2.3 "consecutive choice points" picture should be
retracted. Philosophical scope (per the brief): this is a result about what the
BST *formalism as written* entails; it is **not** a refutation of objective
becoming, and it does not decide presentism vs. eternalism — it shows that the
indeterminism-to-extended-present inference needs an independently motivated
sparseness premise that is currently unstated, and that present-thickness is
formally unstable. Do **not** claim a breakthrough or a whole-ontology
consequence from this conditional, formal result.

## 10. Revision log

No objection-triggered revision has occurred; this is the original candidate,
preserved. One anticipated objection (Section 4) is answered in place rather
than by revising the candidate.

## 11. Proposed next tasks

1. Independent re-audit of the two riskiest clause checks (suprema-in-h; chain
   PCP) by a reviewer who did not propose the candidate.
2. Decide whether the repaired theorem (non-featureless + sparseness + no-MFB)
   is provable in BST92, or admits a further MFB-based counterexample
   (space-like cause-like loci inside a choice-free stretch).
3. Correspondence with the authors (or a short note) asking whether the 2019
   statement's falsity under Def. 6 was known when Theorem 10.1 was rescored to
   BST_NF; priority resolution.
4. Optional: audit whether Müller 2005's BST+S (Def. 21) genuinely admits the
   comb (Section 3, third bullet), since that would show even the
   location-strengthened BST92 framework does not repair the theorem.
