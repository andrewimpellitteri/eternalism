# Locality sees no spacelike scale, and Stein's theorem in GR is a no-local-clock theorem

10 November 2026. Coordinator session (Claude Code, Fable 5.2), at the user's request.
Self-reviewed only: [REVIEW.md](REVIEW.md) records an adversarial pass by the same
session, which repaired two proof gaps and withdrew one novelty statement. Same model
family as the earlier internal reviews, so this is not an independent check. The proofs are elementary and were checked by hand only. Nothing
was formalised or run. No temporal ontology is selected. Priority is not claimed: the
search in §8 was short.

Target: Part I of [What the Past Can Fix](../../what-the-past-can-fix/main.tex)
(source: [stein-gr/main.tex](../main.tex)), and the open
[pocket problem](../ENERGY_CONDITIONS.md).

## 0. What this note adds

1. **Theorem 1.** Local covariance (LC) alone, with no transitivity, no chronological
   becoming and no persistence, forces any relation between spacelike-separated
   events of Minkowski spacetime to be all or nothing. The proof uses only flat
   spacetimes, so it holds on-shell.
2. **Theorem 2.** For events that are not causally related, the verdict of a local
   relation depends only on the two local germs of the metric.
3. **Theorem 3.** A classification of every local relation on Minkowski spacetime.
   Timelike thickness survives locality. Spacelike selectivity does not.
4. **Theorem 4.** On a class of spacetimes closed under restriction and disjoint
   union, Theorem `thm:main`(a) holds if and only if the class has no local clock.
   Equivalently, every local geometry can occur both chronologically after and
   chronologically before a flat region. This replaces the pocket problem, which is a
   sufficient condition, by an exact one that is much weaker.
5. **Example 5.** A full subcategory of GH, with the same morphisms and no added
   structure, on which Theorem `thm:main`(a), Theorem `thm:main`(b) and Corollary
   `cor:nopresent` are all false. The becoming relation there is cosmic time read off
   the Ricci scalar. It satisfies (LC). So the off-shell premise cannot be dropped in
   general, and the paper's statement that cosmological time "violates only locality"
   holds for the proper-time definition of cosmic time and fails for the
   curvature definition.

Items 1, 3 and 5 are fully proved below. Item 2 is fully proved when disconnected
spacetimes are objects and is a proof sketch in the connected category. Item 4 is
fully proved with disjoint unions. In the connected category only a weaker one-way
statement is proved (§5).

## 1. Setting

**Loc** is the category of oriented, time-oriented globally hyperbolic spacetimes with
finitely many connected components. Morphisms are isometric embeddings that preserve
both orientations and have open causally convex image. **Loc₀** is its full
subcategory of connected spacetimes. Fewster and Verch define both
(arXiv:1106.4785, §§2.1–2.2; locator from a tool extraction, see §8). The paper's GH is
Loc₀.

A **local relation** assigns to each object M a relation R_M ⊆ M × M with

- **(LC)** for every morphism ψ : M → M′, x R_M b ⟺ ψ(x) R_M′ ψ(b).

Both directions are used. The paper calls the right-to-left direction Reflection
(Remark `rem:lc`). A **becoming theory** is a local relation that is transitive (T) and
contains the reflexive chronological past (CB).

Two events are **unrelated** if neither is in the causal past of the other. The
**germ** of M at x is the class of pointed neighbourhoods (U, x) under isometries that
preserve both orientations, with two neighbourhoods identified when they agree on a
smaller one. Write g_x for it. Morphisms preserve germs.

A class C of spacetimes is **restriction-closed** if every open causally convex
globally hyperbolic subset of a member is a member. It is treated as a full
subcategory.

## 2. Theorem 1: no spacelike scale

Let Cyl_ℓ be ℝ_t × ℝ² × S¹_ℓ with the flat metric, where the circle has length ℓ. It
is flat, vacuum, connected and globally hyperbolic, and {t = 0} is a Cauchy surface.

**Theorem 1.** Let C ⊆ Loc₀ be restriction-closed and contain Minkowski spacetime 𝕄
and every Cyl_ℓ. Let R be a local relation on C. Then R_𝕄 contains either no
spacelike pair or every spacelike pair.

*Proof.* Proper orthochronous Poincaré maps are automorphisms of 𝕄, so (LC) makes R_𝕄
invariant under them. They act transitively on ordered spacelike pairs of a given
interval, so there is a function f on (0, ∞) with x R_𝕄 b ⟺ f(s) = 1, where s is the
interval.

Fix 0 < a < ℓ and ρ > 0 with a + 2ρ < ℓ and ℓ − a + 2ρ < ℓ. In Cyl_ℓ put
x = (0, 0, 0) and b = (0, 0, a), the last coordinate being arc length θ on the circle.
Let

    S₁ = {t = 0, |y| < ρ, θ ∈ (−ρ, a + ρ)},
    S₂ = {t = 0, |y| < ρ, θ ∈ (a − ρ, ℓ + ρ)}.

Each is an open tube in the Cauchy surface, so each is acausal. They join x to b
the short way and the long way round. Put N_i = int D(S_i).

Let π : 𝕄 → Cyl_ℓ be the covering map and S̃_i a lift of S_i, a straight tube in the
hyperplane t = 0. Then π maps int D_𝕄(S̃_i) isometrically onto N_i:

- If p̃ ∈ D_𝕄(S̃_i), an inextendible causal curve through π(p̃) lifts to one through
  p̃, which meets S̃_i. So π(p̃) ∈ D(S_i).
- Let p ∈ D⁺(S_i) at height τ with foot q. The past cone of p meets {t = 0} in the
  image of the closed ball B̄(q̃, τ), where q̃ ∈ S̃_i lifts q, and that image lies in
  S_i. The preimage of S_i is a disjoint union of translates of S̃_i, and the ball is
  connected and contains q̃, so B̄(q̃, τ) ⊆ S̃_i. Hence (τ, q̃) ∈ D⁺_𝕄(S̃_i) and it
  projects to p. The case of D⁻ is the mirror image.
- D_𝕄(S̃_i) lies over S̃_i, where π is injective.

N_i is causally convex. Let p, q ∈ D(S_i) and p ≤ r ≤ q, and let λ be an inextendible
causal curve through r. The curve back from q to r and then along the past half of λ
meets S_i, and so does the curve from p to r followed by the future half of λ. If
neither meeting point is on λ, there are s₂ ≤ r ≤ s₁ in S_i, and acausality gives
s₁ = s₂ = r. For interiors take p′ ≪ p and q ≪ q′ in int D(S_i). N_i is globally
hyperbolic because it is isometric to int D_𝕄(S̃_i), whose causal diamonds are compact
diamonds of 𝕄. It is connected. So N_i is an object of C, and both N_i ↪ Cyl_ℓ and
N_i ≅ int D_𝕄(S̃_i) ↪ 𝕄 are morphisms. In the first lift the endpoints are at
interval a. In the second they are at interval ℓ − a. Four applications of (LC) give

    f(a) = [x R b in N₁] = [x R b in Cyl_ℓ] = [x R b in N₂] = f(ℓ − a).

Given s, s′ > 0, take a = s and ℓ = s + s′. So f is constant. ∎

**Remarks.**

- The only curvature in the proof is none. The statement therefore holds on GH, on
  GH_DEC, on vacuum spacetimes and on flat spacetimes.
- The mechanism: the causal hull of a spacelike pair is the two points. A thin tube
  joining them is a causally convex region, and its flat geometry fixes an interval,
  but a different tube fixes a different one. Reflection makes every tube
  authoritative. For a timelike pair the causal hull is the diamond between them,
  which every causally convex region containing the pair must contain, and the
  diamond fixes the proper time.
- In 1+1 dimensions the same argument on ℝ × S¹ also identifies left with right
  separations.

## 3. Theorem 2: unrelated events are related only through their germs

**Theorem 2.** Let C ⊆ Loc be restriction-closed and R a local relation on C. If
x, b ∈ M and x′, b′ ∈ M′ are unrelated pairs with g_x = g_x′ and g_b = g_b′, then
x R_M b ⟺ x′ R_M′ b′.

*Proof.* The relation J⁺ is closed, so x and b have neighbourhoods U_x, U_b, each
causally convex and globally hyperbolic, with no causal curve between them. Then
N = U_x ∪ U_b is open and causally convex in M, and it is an object of Loc with two
components. Take the neighbourhoods to be small diamonds. If φ : V → V′ is a germ
isometry at x, then for p ≪ x ≪ q close to x the diamond I⁺(p) ∩ I⁻(q) lies in V and
the diamond of M′ on φ(p), φ(q) lies in V′, by strong causality. Timelike curves
between the endpoints stay in V and V′, so φ carries one diamond onto the other, and
both are causally convex and globally hyperbolic. Do the same at b. The resulting
N′ ⊆ M′ is isomorphic to N. Apply (LC) to
N ↪ M and N ≅ N′ ↪ M′. ∎

Conversely, any relation between germs defines a local relation on unrelated pairs.
So on Loc the local relations between unrelated events are exactly the relations
between germs.

**Connected category (sketch, not audited).** On GH = Loc₀ the same conclusion holds
off-shell. Choose spacelike Cauchy surfaces through the two pairs that agree near the
endpoints under the germ isometries (Bernal–Sánchez extension, as in the paper's
set-up). Take thin tubes S ⊂ M and S′ ⊂ M′ joining the pairs, and glue the two slabs
along their ends. The result is a Lorentzian collar of a solid ring. Embed the ring in
ℝ³ and extend the metric to ℝ⁴ with the cone control of Lemma `lem:C`. The argument of
Lemma `lem:D` then shows that the interiors of the two domains of dependence are
causally convex in the new spacetime and in the old ones. This needs a written proof
before it is relied on. Theorem 1 does not depend on it.

## 4. Theorem 3: all local relations on Minkowski spacetime

The proper orthochronous Poincaré group has these orbits on pairs: the diagonal Δ;
future null and past null pairs; spacelike pairs of interval s > 0; future timelike
and past timelike pairs of proper time τ > 0.

**Theorem 3.** Let C be as in Theorem 1 and R a local relation on C. Then R_𝕄 is a
union of: Δ or nothing; all future null pairs or none; all past null pairs or none;
all spacelike pairs or none; the future timelike pairs with τ ∈ T₊ and the past
timelike pairs with τ ∈ T₋, for arbitrary sets T± ⊆ (0, ∞). Every such union is the
restriction to 𝕄 of a local relation on all of Loc.

*Proof.* Invariance gives a union of orbits, and Theorem 1 handles the spacelike
ones. For the converse, each of the following is preserved and reflected by morphisms,
because causal curves between points of a causally convex set stay in it: equality;
horismos in either direction; being unrelated; and d(x, b) ∈ T, where d is the
Lorentzian distance. ∎

**Corollary A (local presents).** Let R be a symmetric local relation that relates no
two distinct causally related events. Then in 𝕄 the set of events R-related to b is
contained in {b}, or it is the whole elsewhere of b, possibly with b. No transitivity,
chronological becoming or persistence is assumed.

**Corollary B (transitivity without CB).** If R is local and transitive, then R_𝕄
contains no spacelike pair or R_𝕄 = 𝕄 × 𝕄. (Any two events of 𝕄 have a common
spacelike event.) So the flat no-shared-present conclusion does not need
chronological becoming. Adding (CB) and the paper's Lemma `lem:R` recovers the
Clifton–Hogarth trichotomy I⁻, J⁻, U. That is a consistency check from a stronger
premise, not a new proof of their theorem.

**Corollary C (the collar is local).** The proper-time collars P_a of
[SCALE_AND_FUTURE_EXCLUSION.md](../../ontology-reconstruction/coordinator/SCALE_AND_FUTURE_EXCLUSION.md)
extend to local relations on all of Loc, using d(b, x) < a. That note derives future
exclusion from dilation invariance and says the premise "needs its own justification".
Theorem 1 supplies the spacelike half of dilation invariance from (LC). Corollary C
shows the timelike half is independent of (LC).

**What this changes in the paper.**

- The trilemma after Corollary `cor:nopresent` says a defender of a shared present may
  "reject transitivity". Corollary A says what that buys in flat spacetime: the whole
  elsewhere and nothing thinner. The bow tie is the unique local shared present there,
  up to the light cone and timelike thickening.
- The paper notes that Bigaj reaches the pointy and bow-tie pair with "an
  exhaustiveness stipulation". Under (LC) exhaustiveness of the elsewhere is a
  theorem in flat spacetime. Bigaj's text was not reread for this note.
- A thick present can be local only if its thickness is temporal. The causal-diamond
  present of Arthur and Savitt appears to have that form. Their texts were not reread
  for this note.
- (LC) is strong. Take the relation "x and b lie in a common diamond
  I⁺(z₁) ∩ I⁻(z₂) with d(z₁, z₂) < ℓ₀". It is defined from the metric in every
  spacetime, and in 𝕄 it holds of a spacelike pair exactly when the interval is below
  ℓ₀. It violates Reflection, because a thin tube from x to b need not contain z₁ or z₂.
  Remark `rem:lc` should say that Reflection alone excludes every metrical relation
  between spacelike events, before (T) and (CB) are used. Theorem `thm:main` then
  splits into two steps: (LC) makes the spacelike verdict all-or-nothing by germ, and
  (T) with (CB) turns "all" into "universal".

## 5. Theorem 4: Stein's theorem in GR holds exactly where there is no local clock

Let C ⊆ Loc be restriction-closed, closed under finite disjoint unions, and contain 𝕄.
Let G be the set of germs of members of C, and write *flat* for the germ of 𝕄.

- **Precedence.** g ⊴ g′ if some M ∈ C has events w ≪ x with germs g and g′. Let ⊴*
  be its reflexive transitive closure. A chain may pass through different spacetimes.
- **Local clock.** A map κ from G to a partially ordered set with κ(g) ≤ κ(g′)
  whenever g ⊴ g′. It is **nontrivial** if κ(g) < κ(g′) for some g, g′.
- **Anchored.** g is anchored if flat ⊴* g ⊴* flat.

**Theorem 4.** The following are equivalent.

1. Every becoming theory B on C with B_𝕄 ≠ U has B_M ⊆ J⁻_M for all M ∈ C. (This is
   Theorem `thm:main`(a) on C.)
2. C has no nontrivial local clock.
3. Every germ of C is anchored.

*Proof.* (3 ⇒ 1). Let B be a becoming theory with x B_M b and x ∉ J⁻(b). If b < x,
Lemma `lem:R` gives e ≪ x unrelated to b, and e B x B b. So assume x and b unrelated.
By Theorem 2 the verdict on unrelated pairs is a relation ρ on germs, and
ρ(g_x, g_b) holds.

ρ is closed under precedence on the left. Suppose ρ(g₁, g₂) and g₀ ⊴ g₁, witnessed by
w ≪ x₁ in M₀. Let U_b be a small neighbourhood of an event b with germ g₂. In
M₀ ⊔ U_b the pair (x₁, b) is unrelated with germs (g₁, g₂), so x₁ B b. Also w B x₁ by
(CB), so w B b by (T), and (w, b) is unrelated. Hence ρ(g₀, g₂). The mirror argument
gives closure on the right under g₂ ⊴ g₃.

Since g_x and g_b are anchored, chains give ρ(flat, flat). Then every spacelike pair
of 𝕄 is in B_𝕄, and (T) gives B_𝕄 = U.

(1 ⇒ 2). Let κ be a nontrivial local clock with κ(g) < κ(g′). Put

    B_M = I⁻_M ∪ {(x, b) : κ(g_x) < κ(g_b)}.

(LC) holds because germs and chronology are preserved and reflected. (CB) holds.
(T): if x ≪ y and κ(y) < κ(b) then κ(x) ≤ κ(y) < κ(b), and the other two cases are the
same. B_𝕄 = I⁻ ≠ U. In the disjoint union of neighbourhoods with germs g and g′ the
relation holds between unrelated events. So 1 fails.

(2 ⇒ 3). The indicator of {g : flat ⊴* g}, valued in {0 < 1}, is a local clock. If it
is not nontrivial, every germ is above flat. The indicator of the complement of
{g : g ⊴* flat} is also a local clock, and the same argument puts every germ below
flat. ∎

**In the connected category.** The equivalence is not claimed there. One direction
survives in a weaker form. Let C ⊆ Loc₀ be restriction-closed and contain 𝕄, and let κ
be a two-valued local clock that is not constant on some member M. Lemma `lem:E` joins
two events of M with different κ by a chain of consecutively spacelike events, and two
consecutive members of the chain differ in κ. The relation I⁻ ∪ {κ(x) < κ(b)} is then a
becoming theory on C that is I⁻ on 𝕄 and relates a spacelike pair in M. So **a
two-valued local clock that varies within one connected member defeats Theorem
`thm:main`(a) on the paper's own kind of category.** Example 5 is of this kind.
Without disjoint unions, an unanchored germ need not produce such a clock, because the
germ and a flat region may never share a member. Sufficiency in the connected category
needs the gluing sketched under Theorem 2, or the paper's own construction.

**Consequences for the pocket problem.**

- The pocket problem asks for one DEC spacetime containing the whole curved slab, two
  flat pockets and a flat slab joining them. Anchoring asks only that each single germ
  occurs chronologically after some flat region and before some flat region, in
  spacetimes that may differ, through chains of any length. No slab is transported.
- Chains are cheap. If w ≪ x in M then g_w ⊴ g_x. So a germ of M is anchored as soon as
  one germ in its chronological past is anchored below and one in its future is
  anchored above.
- Off-shell GH is anchored by the paper's M′, which is flat before and after the tube.
- The class of Theorem `thm:same-past` supplies anchoring from below on-shell: each
  member is exactly Minkowski on the wedge v < A, and every event has such points in
  its chronological past. Anchoring from above fails to be obvious there, because the
  outgoing radiation is not shown to have compact support.
- For GH_DEC the question is now a clean one in geometric analysis: **does every
  DEC germ occur chronologically after, and before, an exactly flat open set in some
  DEC spacetime?** I expect yes (Vaidya and compensated-void models do it for their own
  germs) but have not proved it. A germ of generic curved vacuum is the hard case: by
  the conservation theorem the matter that walls off a pocket must enter from outside
  the domain of dependence.

## 6. Example 5: a curvature clock

Let C_R be the full subcategory of GH whose members have Ricci scalar R non-increasing
along every future-directed causal curve. It contains 𝕄 and every vacuum spacetime
(R = 0), and spatially flat expanding dust FLRW (R is a positive multiple of the
density, which decreases in cosmic time, and cosmic time increases along every future
causal curve). It is restriction-closed. Its morphisms are those of GH. No structure
is added.

On C_R define three relations. Each satisfies (LC), because R(ψ(x)) = R(x). Each is
transitive and contains I⁻, because x ≤ y implies R(x) ≥ R(y).

| Relation | On 𝕄 | On expanding dust FLRW | What fails on C_R |
|---|---|---|---|
| J⁻ ∪ {R(x) > R(b)} | J⁻ | relates every earlier-epoch event to every later one | Theorem `thm:main`(a) |
| J⁻ ∪ {R(x) ≥ R(b) and R(x) > 0} | J⁻ | cosmic-time preorder, with the constant-density slices as shared presents | Corollary `cor:nopresent` |
| {R(x) ≥ R(b)} | U | cosmic-time preorder, not U | Theorem `thm:main`(b) |

Transitivity of the second: if x ≤ y and R(y) ≥ R(b) with R(y) > 0, then
R(x) ≥ R(y) > 0 and R(x) ≥ R(b). If R(x) ≥ R(y), R(x) > 0 and y ≤ b, then
R(x) ≥ R(y) ≥ R(b). Two steps of the second kind compose.

None of this contradicts the paper. These relations are not transitive on all of GH,
so they are not becoming theories there.

**Credit inside the repo.** The locality of the rule R(x) ≥ R(b) is not new here.
[DRAFT.md](../DRAFT.md) §4.4 states it for the dust model and concludes that the rule
is not the restriction of a becoming theory on GH. The unified paper dropped that
caveat. Proposition `prop:single` also gives a contrived class on which the theorem
fails (the regions of one generic spacetime together with those of 𝕄). What is added
here is the class C_R, the shared-present variant, and the criterion of Theorem 4.
See [REVIEW.md](REVIEW.md) §3.

What the example shows:

- **The off-shell premise is essential, not a convenience.** Remark `rem:offshell` and
  §`sec:energy` present dropping it as "not routine" and leave the pocket problem open
  as a sufficient condition. On C_R, and on C_R ∩ GH_DEC, the theorem and the
  corollary are false.
- **Cosmic becoming can be local.** Proposition `prop:nonlocal` defines cosmic time as
  the supremum of past proper time and shows it violates (LC) on the Milne wedge. The
  paper concludes that "natural global rules such as cosmological time violate only
  locality". The density clock gives the same slices in dust FLRW and satisfies (LC).
  What it violates is the demand that the rule be a becoming theory on every
  kinematically possible geometry. The Milne wedge is no objection to it: the wedge is
  flat, R = 0 there, and the rule returns J⁻ on the wedge and on 𝕄 alike.
- **The clock-equipped rival is the general case.** The paper's strongest rival adds a
  time function T to the objects. By Theorem 4 a non-universal becoming that reaches
  outside the causal past exists exactly when the admissible class has a local clock.
  A curvature scalar is one that needs no added structure. A matter scalar, such as a
  temperature or a comoving density, is one on a category enriched with matter fields.
- **This is where the arrow enters Part I.** [PARITY_MAP.md](../../PARITY_MAP.md) lists
  the thermodynamic arrow as the largest gap and notes that Part I takes time
  orientation as an input. Theorem 4 states the dependence exactly: local becoming is
  confined to the causal past if and only if no local quantity is monotone along every
  timelike curve of every admissible world. A universal local arrow is the same thing
  as a local clock. Whether the actual laws and boundary conditions supply one, exactly
  or after coarse-graining, is a physical question that the Stein lane has so far
  treated as outside its scope.

C_R is not a realistic class. A star has a spacelike density gradient, so no spacetime
with a star is in it. The mathematical point does not need realism. The philosophical
point needs a separate argument about which class of spacetimes a becoming rule must
cover, and that argument is not given here.

## 7. Limits and kill conditions

- Theorem 1 uses Reflection through the flat cylinder. A reader who restricts (LC) to
  simply connected or to inextendible targets escapes it. The paper's Theorem
  `thm:main` uses Reflection in the same way.
- Theorem 2 and the equivalence in Theorem 4 are proved on Loc, which has disconnected
  objects. On Loc₀ only the stated parts are proved, and anchoring is not shown to be
  necessary there. If a disconnected region is not an
  admissible standpoint for a becoming rule, the Loc versions lose force.
- "Germ" means the full germ of the metric, so a local clock may depend on infinitely
  many derivatives. No regularity of κ is assumed or obtained.
- Theorem 4 covers part (a) of Theorem `thm:main`. Part (b) is shown to fail on C_R but
  is not characterised.
- The anchoring of GH_DEC is open. So this note does **not** prove the on-shell
  theorem. It replaces one open sufficient condition by an exact criterion.
- Kill conditions: an error in the lift of D(S_i); a hidden use of transitivity in
  Theorem 1; a published statement of the same classification; a counterexample to
  anchoring in off-shell GH (which would contradict the paper's own theorem).
- A finite or special example has its stated domain only. C_R is not a claim about
  the actual universe.

## 8. Sources and search

Read depths follow the knowledge-base contract. Records are in
[sources.jsonl](sources.jsonl).

- Fewster and Verch, arXiv:1106.4785. The definitions of Loc and Loc₀ were taken from a
  tool extraction of the ar5iv HTML, §§2.1–2.2, first half of the paper only. Depth:
  abstract. Verify the locators before citing.
- Project sources: `stein-gr/main.tex` and the unified paper's Part I and Appendix
  (read in full for this note); `ENERGY_CONDITIONS.md` (first 120 lines);
  `SCALE_AND_FUTURE_EXCLUSION.md` and `PERSISTENCE_CONVENTIONS.md` (read).
- Prior-art search, 10 November 2026: three web queries and one alphaXiv query on
  locally covariant relations between events, uniqueness of an elsewhere present
  without transitivity, and locally measurable cosmic clocks set against Stein-type
  theorems. Nothing matching Theorems 1, 3 or 4 was found. The search returned Bigaj's
  non-transitive cumulativity result and the cosmic-time presentism literature
  (Crisp; Saudek 2020) at snippet depth. This bounds priority weakly. It does not
  certify it. The most likely place for an existing statement of Theorem 1 or 2 is the
  locally covariant QFT literature, which was not searched in depth.
- Not done: no independent review, no formalisation, no numerical check, no outside
  reader.
