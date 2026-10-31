# Bounded classification of covariant existence assignments E(b,x)

29 October 2026. Worker submission for independent review — not an accepted
result. Status labels used throughout: **[Established]** = standard or
internally reviewed result with locator; **[Author]** = position of a named
author or rival theory; **[Ours]** = this lane's construction, proved here at
the stated scope; **[Open]** = explicit open gate. This lane is logically
independent of the other three ontology lanes and of the two technical GLM
repairs rejected in BATCH2_INITIAL_REVIEW.md; no conclusion from those
submissions is used.

## 0. Claim contract and nearest predecessors

Question: on explicit spacetime categories, which candidate rules E assigning
to each pointed spacetime (M,b) a realm E(M,b) ⊆ M of events existing at b
satisfy which of five independently separated conditions — isometry
covariance, cross-model restriction (locality), persistence, chronological
inclusion + future exclusion + nonuniversality, and transitivity — and does
any combination select a unique realm?

Nearest predecessors and what changes here:

1. Stein 1968; Clifton–Hogarth 1995, Thm 1 (pp. 365–367) — **[Established,
   bibliographic record verified via Crossref 2026-10-29]**: in Minkowski, a
   transitive isometry-invariant becoming relation with chronological
   becoming is I⁻, J⁻ or universal. They classify *becoming relations*
   assumed transitive; they do not classify *existence realms*, do not
   separate persistence or restriction as independent axes, and do not treat
   potential-based enlargements (D, H).
2. Wüthrich–Callender 2017, §3 (arXiv:1502.00018v1, abstract read) —
   **[Established, author claim]**: within one causal set, automorphism
   invariance permits exotic becoming; the Stein analogue fails in CST.
   This lane's axes make the corresponding distinction for existence realms:
   within-model covariance (A1) is separated from cross-model restriction
   (A2), and the failure of A1-constraint in asymmetric models is the
   stein-gr manuscript's Proposition 3.7.
3. `research/stein-gr/main.tex` (this worktree, version 25 October 2026;
   read in full; audited by an earlier lane at commit 498de2f3 with one
   repaired Lemma F end-cap) — **[project manuscript, internal review
   status]**: under (LC)+(T)+(CB) on the Loc category, becoming is either
   universal everywhere or between I⁻ and J⁻ (its Thm 7). That result
   *assumes transitivity* and classifies a *relation*, not an existence
   realm family; it does not consider persistence (redundant for relations
   satisfying (CB)) or the potential realms D, H, which are not transitive.
   This lane keeps transitivity OUT of the shared premise set (Section 2,
   A7) precisely so that bow-tie-style theories are not excluded by fiat.
4. `lawful-completions/coordinator/HISTORICAL_POTENTIAL.md` and
   `DIAMETER_CLASSIFICATION.md` (read in full; coordinator derivations, not
   independently reviewed) — give the slab criterion for H and the
   cylinder H=D_BT diameter classification. Neither discusses restriction
   (A2) of H to subspacetimes. CM4 below fills that gap.
5. `ontology-reconstruction/coordinator/PREMISE_STRESS_TEST.md` §1–2 (read
   in full) — shows E_all and E_past agree on covariance+persistence+
   restriction, and gives the flat region on which instantaneous potential
   D fails restriction. This lane republishes that configuration with exact
   rational witnesses (CM1), extends the failure table to persistence (CM2)
   and to H (CM4, previously claimed then retracted; verified here), and
   adds the proved lemmas L1–L3.

Novelty boundary: no new theorem is claimed beyond the bounded lemmas and
countermodels proved in Sections 4–5 at their stated scopes. The trichotomy
of Section 6 is a cell-by-cell verification for six displayed rules; it is
**not** a classification of all possible rules (Section 8).

## 1. Categories (explicit, justified, on-shell/off-shell marked)

**C_GH**: connected smooth time-oriented globally hyperbolic (GH) spacetimes,
morphisms = smooth orientation- and time-orientation-preserving isometric
embeddings with open causally convex image (the Loc category of BFV2003, §2;
discovery depth). This is a *kinematic* category: every GH metric is an
object regardless of field equations (off-shell) — the same off-shell
premise flagged as Remark 2.5 in the stein-gr manuscript.

**C_slab**: the flat conformal slab (0,1)×R¹⁺ᵏ with the restricted Minkowski
causal order, together with all its open causally convex GH subspacetimes.
Objects are flat: vacuum Einstein holds with matter identically zero, so the
flat members are **on-shell** for vacuum GR. The artificial temporal
boundaries t∈{0,1} are a kinematical restriction, not a cosmological
solution boundary; noted wherever used.

**C_Mink**: 1+1 Minkowski spacetime and its open causally convex GH
subspacetimes; flat, on-shell vacuum. C_Mink ⊂ C_GH.

**C_cyl(L,S)**: conformal cylinders (a,B)×S, S complete Riemannian, L=B−a
finite, with causally convex open subspacetimes — on-shell only after a
matter model is named (flat dust+Λ realizes S=R³, per
DIAMETER_CLASSIFICATION.md; the general cylinder is otherwise kinematic).
Used only for the proposed target in Section 8.

**C_slice(M,t)**: a GH spacetime with a *chosen* smooth cosmic time function
t (timelike gradient), morphisms restricted to isometric embeddings ψ with
t∘ψ = t. This is a different category with extra structure; see O5.

## 2. The axes (independent hypotheses)

A rule E assigns to each object (M,b) a subset E(M,b) ∋ b. The axes:

- **A1 (isometry covariance)**: for every isometry φ: M→M preserving
  orientation and time orientation, x ∈ E(M,b) ⟺ φ(x) ∈ E(M,φ(b)).
  Within-model only; strictly weaker than definability (BATCH1 review,
  point 3: the 1+1 origin stabilizer is already transitive on the nonzero
  null cone, so A1 leaves null-side choices open; and stein-gr Prop 3.7:
  generic single models constrain almost nothing).
- **A2 (cross-model restriction / locality)**: for every morphism
  ψ: N→M and b ∈ N, E(N,b) = ψ⁻¹(E(M,ψ(b))). This is (LC) of the stein-gr
  manuscript, specialized to realms. It compares intrinsic evaluation with
  ambient restriction; it is the axis that can fail for future-witness-
  dependent rules even over flat vacuum regions.
- **A3 (persistence)**: b ≤ c ⟹ E(M,b) ⊆ E(M,c).
- **A4+A5+A6 (inclusion/exclusion/nontriviality, kept separate in the
  table)**: A4 chronological inclusion I⁻(b)∪{b} ⊆ E(b); A5 future
  exclusion E(b) ∩ J⁺(b) = {b}; A6 nonuniversality E(b) ≠ M whenever the
  strict causal future J⁺(b)∖{b} ≠ ∅.
- **A7 (transitivity of existence-at)**: x ∈ E(b) and b ∈ E(c) ⟹ x ∈ E(c).
  **A7 is recorded, not assumed.** The Correia–Rosenkranz-style bow-tie
  theory rejects it **[Author position: C&R allow coexisting distinct
  events; see FUSION_MODEL.md, chapter 9 clauses]**; assuming A7 would
  exclude that rival by construction, not by theorem (the warning in the
  task brief; also stein-gr Cor 8 "no shared present" is the A7-bearing
  corollary).

Causal conventions: x ≤ y iff y is reachable from x by a future-directed
causal curve (reflexive, null included); ≺ excludes equality; ≪ is
chronological. Realms (all order-definable, hence A1 on every category):

- E_all(b) = M;  J(b) = J⁻(b);  I(b) = I⁻(b)∪{b};  B(b) = M∖(J⁺(b)∖{b})
  (bow tie = D_BT of HORIZON_REVIEW.md);  D(b) = {b} ∪ {x : ¬(b ≺ x), ∃z
  (b ≺ z ∧ x ≺ z)} (instantaneous potential);  H(b) = ⋃_{r≤b} D(r)
  (historical potential). A preferred-slicing realm E_t(b) = {x : t(x) ≤ t(b)}
  is defined only on C_slice(M,t).

## 3. Classification table

Cells marked **[Ours-p]** carry a proof in Section 4; **[Ours-w]** a witness
in Section 5; **[Reviewed]** a project-internal reviewed source (locator
given). Ambient category: C_slab (identical table on C_Mink except as noted
in the D and H rows).

| Realm | A1 | A2 restrict | A3 persist | A4 | A5 | A6 | A7 trans |
|---|---|---|---|---|---|---|---|
| E_all | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ |
| J⁻ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| I⁻∪{b} | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| B (bow tie) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ (CM3) |
| D (potential) | ✓ | ✗ (CM1) | ✗ (CM2) | ✓ | ✓ | ✓ | ✗ (CM3) |
| H (historical) | ✓ | ✗ (CM4) | ✓ | ✓ | ✓ | ✓ | ✗ (CM3) |

Category dependence, stated exactly:
- On C_Mink (full Minkowski ambient) D still fails A2 (CM1's ambient *is*
  Minkowski), but A3 holds: D=B there by Lemma L3.
- H fails A2 on C_slab (CM4) but satisfies A2 on C_Mink (L3: H=B there, and
  B restricts by L2). The finite conformal past is essential; see Section 5.
- D satisfies A3 on any connected causally simple future-directed spacetime
  (D monotone ⟺ future-directed; **[Reviewed]**
  `lawful-completions/relational/HORIZON_LEMMA_REVIEW.md`, proof audited
  there; hypotheses: connected, time-oriented, boundaryless, causally
  simple; global hyperbolicity suffices). So "D fails persistence" is a
  slab-category fact, not a universal one.

## 4. Proved bounded lemmas

**L1 (future exclusion of H and D) [Ours-p]**. In any causal spacetime:
H(b) ∩ J⁺(b) = {b} and D(b) ∩ J⁺(b) = {b}. Proof: x ∈ D(r) with b ≤ r
gives ¬(r ≺ x) (or x = r); if b ≺ x then r ≤ b ≺ x gives r ≺ x or r = x by
push-up, and r = x yields x ≤ b ≺ x, a causal loop, excluded in causal
spacetimes. Contradiction either way; x = b is the surviving member. For H,
take the union over r ≤ b. ∎

**L2 (order-defined realms restrict) [Ours-p]**. For E ∈ {J⁻, I⁻∪{b}, B} and
every causally convex open U ⊆ M: E_U(b) = U ∩ E_M(b). Proof: causal
convexity gives J^±_U(b) = U ∩ J^±_M(b) (a causal curve between U-points
stays in U), likewise for I⁻; B is a Boolean combination; intrinsic and
ambient orders agree on U-points. Note the failure mode of D and H is
exactly that their definitions quantify over points *outside* U (future
witnesses, earlier standpoints). ∎

**L3 (future-directed ⟹ H = B, hence H restricts) [Ours-p]**. Let M be
causal and future-directed (every pair has a common strict causal future).
Then D(r) = B(r) for all r: ⊆ by definition of B as the ¬(r ≺ x)-set; ⊇
because x = r ∈ D(r) and otherwise future-directedness supplies the witness.
Hence H(b) = ⋃_{r≤b} B(r); ⊇ holds by r = b; ⊆: if x ≻ b and x ∈ B(r) with
r ≤ b, push-up gives r ≺ x (r = x would loop), contradicting x ∈ B(r). So
H(b) = B(b). B is persistent (Section 3, B/A3 proof: b ≤ c ≺ x forces
b ≺ x) and restricts (L2), so H satisfies A2 and A3 on any such category.
Instances: full Minkowski; the a=−∞ slab — recovering the HISTORICAL_POTENTIAL.md
remark that H = D_BT there. ∎

**L4 (the CM4 exclusion) [Ours-p]**. The case analysis of Section 5 (CM4):
with U, b, x as there, x ∉ H_U(b). Machine-checked at the listed rationals
in `checks/countermodels.py` (block CM4), including the reverse-triangle
bound 8/5 killing the q-branch, the window (27/20, 35/20) for the p-branch,
and the two-endpoint contradiction using the slab hypothesis t > 0 exactly
once. ∎

**Defeated conjectures (recorded honestly)**:
- *"H fails restriction in full Minkowski"* — **defeated** [Ours-p]: L3
  gives H = B on Minkowski, and the CM1/H block exhibits the witness
  r=(−4/5,−1/5), z=(1/4,4/5) with x ∈ D_U(r) inside the very region used in
  CM1. The pre-resume messages retracted this claim; this lane confirms the
  retraction was correct *for the Minkowski ambient* and shows the slab
  version (CM4) is correct. Both statements are proved, not inferred from
  searches.
- *"The structural axes A1–A6 select a unique realm"* — **defeated**: three
  order-definable realms (J⁻, I⁻∪{b}, B) satisfy all six (Section 3).
- *"D is never persistent"* — **defeated**: monotone exactly when
  future-directed on causally simple spacetimes **[Reviewed]** (locator in
  Section 3).

## 5. Countermodels (explicit rational witnesses; machine-certified)

All arithmetic is exact; `checks/countermodels.py` passes in < 1 s (timings
in AGENT_REPORT.md). Previous dense pools were removed; universal statements
are proved analytically, not enumerated.

**CM1 (D fails A2; flat vacuum region in full Minkowski)**. U = I⁻(p)∪I⁻(q),
p=(1/2,−1), q=(1/2,1); b=(0,−1), x=(0,1); z=(3/2,0) witnesses x ∈ D_M(b).
No common strict U-future of b,x exists: any such w=(s,m) has
s ≥ max(|m+1|,|m−1|) = |m|+1 ≥ 1 > 1/2 ≥ sup U. Configuration from
PREMISE_STRESS_TEST §2; witnesses here are exact rationals. U is open, a
past set (hence causally convex), connected (the cones overlap), GH
(compact diamonds), flat: the failure of A2 occurs on the smallest reasonable
category, on-shell, with no exotic causality.

**CM2 (D fails A3 on C_slab)**. s=(1/2,0) ≤ c=(3/4,0), x=(0,13/10);
w=(9/10,2/5) witnesses x ∈ D(s) (null steps allowed by ≺). x ∉ D(c): a
common strict slab future u=(t,m) of c,x needs t ≥ 3/4+|m| and
t ≥ |m−13/10|; t < 1 forces |m| < 1/4, then t ≥ 13/10−1/4 = 21/20 > 1.
Consistent with the published slab criterion d < 2B−ρ−ξ
(HISTORICAL_POTENTIAL.md). Scope: slab only (see CM2's reviewed positive
converse, Section 3).

**CM3 (A7 fails for B, D, H; Minkowski)**. b=(0,0), x=(0,2), y=(2,−1):
b,x and x,y spacelike; b ≺ y. So y ∈ B(x), x ∈ B(b), y ∉ B(b); witnesses
z₁=(5,0), z₂=(7/2,0) give the D-chain; r=(−8,10) ≤ x (null) with
z₃=(5,−2) gives y ∈ D(r) ⊆ H(x), while y ∉ H(b) by L1's cone argument
(r ≤ b=(0,0) ⟹ t_r ≤ −|w_r| ⟹ |y_w−w_r| ≤ 1+|w_r| ≤ 2−t_r = y_t−t_r, and
t_r ≤ 0 < 2 = y_t, so r ≺ y). One triple kills transitivity for all three
realms.

**CM4 (H fails A2 on C_slab; verifies the retracted claim at exact
rationals)**. Ambient M = slab (0,1)×R; U = I⁻(p)∪I⁻(q) with p=(9/10,8/5),
q=(9/10,−1/10); b=(1/2,0), x=(1/2,3/2). U is open, a past set, connected,
GH; its inclusion into the slab is a Loc-morphism; slab and U are flat
(on-shell vacuum). b ≪ q and x ≪ p (so b,x ∈ U), and b,x are spacelike.

(a) x ∈ H_M(b): witness r=(1/10,7/20) ≤ b (timelike), r,x spacelike, common
strict slab future w=(97/100,6/5): r ≺ w (87/100 ≥ 17/20), x ≺ w
(47/100 ≥ 3/10), t_w = 97/100 < 1. Note r itself lies in U (r ≪ q), so the
failure is not mere absence of early standpoints from U.

(b) x ∉ H_U(b). x ≠ any candidate r ≤ b in U (r_t ≤ 1/2, and r_t = 1/2
forces r = b ≠ x). Case A: if r ≺ x then x ∉ D_U(r) outright. Case B:
¬(r ≺ x) together with r ≤ b gives |3/2−y| > |y|, i.e. y < 3/4. A common
strict U-future w=(s,m) must satisfy w ≻ x and w ≪ p or w ≪ q:
  (i) w ≪ q impossible: 1/2+|m−3/2| ≤ s and s+|m+1/10| < 9/10 give
      |m−3/2|+|m+1/10| < 2/5, but the left side is ≥ |3/2−(−1/10)| = 8/5.
  (ii) w ≪ p forces |m−3/2|+|m−8/5| < 2/5, hence m ∈ (27/20, 35/20); then
      m > 27/20 > 3/4 > y.
  (iii) r ≺ w gives s ≥ t+m−y ≥ m+2t−1/2 > m−1/2 (here t > 0, the slab's
      finite past, enters — and only here), while w ≪ p gives
      s < 9/10−|m−8/5|: for m ≤ 8/5 this is s < m−7/10 < m−1/2 < s; for
      m > 8/5 it is s < 5/2−m ≤ 9/10 < 11/10 ≤ m−1/2 < s. Contradiction
      both branches. Hence no witness exists and x ∉ H_U(b). ∎

So on C_slab the historical-potential realm — the least persistent
enlargement of D, proposed in HORIZON_REVIEW.md as a coherent growth repair —
buys A3 at the price of A2. Per L3 the same realm is local on
future-directed ambients; the locality failure is a theorem about the
(category, rule) pair, not about H "in itself".

## 6. Observations the table licenses (and does not overstate)

- **O1 [Ours-p]**: A1–A6 jointly do not determine the realm. J⁻, I⁻∪{b}
  and B satisfy all six on both categories; the residual freedom is exactly
  the *elsewhere* (spacelike coexistence), and no structural axiom in the
  list touches it.
- **O2 [Ours-p]**: A7 separates {J⁻, I⁻∪{b}} (and E_all) from {B, D, H}.
  Since bow-tie theories reject A7 as a premise **[Author]**, any
  "exclusion of C&R" obtained by assuming A7 is by construction. This lane
  therefore reports A7 as a column, not a premise.
- **O3 [Ours-p, bounded]**: within the displayed family, *no* realm
  combining elsewhere-inclusion (spacelike members beyond the past) with
  A2 and a potential-based definition exists: B has A2+A3 but bare
  elsewhere-membership; D loses A2 (and on slabs A3); H keeps A3 but loses
  A2 on finite-past ambients. Proved for these six rules only; not a
  universal dichotomy (Section 8).
- **O4 [Ours-p]**: E_all fails only A5 and A6. Excluding whole-history
  eternalism thus requires exactly the substantive premises (future
  exclusion or nonuniversality), confirming and sharpening PREMISE_STRESS_TEST
  §1; it cannot be advertised as a neutral structural theorem.
- **O5 [Ours-p, conceptual independence witness]**: the preferred-slicing
  realm is not a rule on the structure-free categories at all; on
  C_slice(M,t) it satisfies A1–A7 *relative to slice-preserving morphisms*.
  Hence A1/A2 constrain (rule, category) pairs, and a locality premise
  cannot silently exclude global or foliated ontologies: the rival pays in
  added structure, not in consistency (the stein-gr manuscript's trilemma,
  Section 9, read at full text; our axis version). This is the formal sense
  in which "naturality/locality cannot exclude global alternatives by
  definition".

## 7. Sharply bounded proposed classification target

**Target T [Open, proposed]**. On C_cyl(L,S) with 0 < L < ∞ and S complete
of positive dimension, prove or refute: *for every such cylinder there exist
a Loc-morphism U ↪ M and b, x ∈ U with x ∈ H_M(b) ∖ H_U(b)*; and prove the
positive half: *on every connected causally simple future-directed
spacetime, H satisfies A2* (this half follows from L3 + L2 and is proved).
Status: the finite-L half is open; CM4 is the L=1, S=R witness and the
construction needs only cone-pair placement near the upper conformal
boundary plus an early witness standpoint below b, but the cylinder version
requires the geodesic bookkeeping of DIAMETER_CLASSIFICATION.md and has not
been carried out. An on-shell realization exists in principle (flat
dust+Λ: L finite, diam S = ∞), but the dust+Λ cylinder's conformal factor
and interval must be fixed from the solution before the construction is
run; that check is part of T.

Secondary target T2 [Open]: characterize *all* order-definable rules on
C_slab satisfying A1–A6. Known members: the three realms of O1. Every
rule tried that includes elsewhere-points via *potential or distance*
quantifiers failed A2 (potential: CM1/CM4; distance-threshold rules fail
because geodesic distance is not restriction-stable), which suggests A2 is
the binding constraint; no completeness claim is made.

## 8. What this lane does NOT claim

- No universal classification of existence rules (T2 is open; the table
  covers six displayed rules).
- No new Stein-type theorem: everything transitivity-bearing here either
  cites CH/stein-gr or is a countermodel to transitivity.
- No ontological selection: Section 9 only.
- No claim that D or H are "the" C&R semantics: FUSION_MODEL.md shows the
  selected location/fusion clauses leave point realms underdetermined; that
  non-entailment is inherited here untouched.
- The slab categories are kinematic flat patches; only their flatness
  (vacuum on-shell status) is used, and their artificial temporal
  boundaries are flagged wherever load-bearing (CM4, T).

## 9. Philosophical reading (independent of coordinator preference)

The classification supplies what an explanatory-role audit needs, in the
sense of `ontology-reconstruction/coordinator/EXPLANATORY_ROLE_TEST.md`
§4 (read in full): an inventory of which distinctive existence claims do
which formal work. Three conditional readings, each contestable and none
endorsed as an ontology selection:

1. *The elsewhere is the whole disagreement.* Under A1–A6 the eternalist's
   extra commitment (A5, A6) and the bow-tie theorist's extra commitment
   (abandoning A7) are symmetric in status: each is an additional premise,
   and the structural axioms do not adjudicate (O1, O4). An argument for
   one over the other must therefore be explanatory or metaphysical, not
   structural — whichever direction it runs.
2. *Potential has a locality price.* If "exists here" is grounded in causal
   potential (D) or its persistent historical closure (H), then either the
   grounding relation quantifies beyond every local fragment (A2 fails,
   CM1/CM4) or persistence fails (CM2). A fragmentalist who wants both
   persistence and local grounding must locate potential in the fragment's
   own past — i.e. adopt something like H — and then accept ambient
   dependence of realm membership; that is a defeasible cost, not a
   refutation. [Ours, conditional]
3. *No hidden selection.* Because any realm can be made covariant and
   local by enriching structure (O5), the absence of a structural selector
   is itself the stable result: the disagreement among E_all, J⁻, B, H is
   live under all separated structural premises. This is an
   underdetermination finding in the ROADMAP's Phase-2 sense, not a
   verdict. [Ours, conditional]

## 10. Machine verification

`python3 research/ontology-reconstruction/classification/checks/countermodels.py`
— 52 checks, all PASS, total ≈ 0.05–0.12 s wall (AGENT_REPORT.md timings);
exact `Fraction` arithmetic; per-check O(1); no dense pools (pre-resume
300 s timeout eliminated). Each check certifies a listed witness or a
displayed constant of the analytic arguments above; universal statements
are proved in Sections 4–5 and are not re-established by enumeration.
