# Locality sees no spacelike scale, and Stein's theorem in GR is a no-local-clock theorem

10 November 2026. Claude Code (Fable 5.2), at the user's request. Checked only by the
session that wrote it. Proofs are elementary and done by hand. No temporal ontology is
selected and no priority is claimed. Sources: [sources.jsonl](sources.jsonl).

The statements marked ★ are in [stein-gr/main.tex](../main.tex) and the unified paper.

## Setting

**Loc** is Fewster and Verch's category: oriented, time-oriented globally hyperbolic
spacetimes with finitely many components, and isometric embeddings with causally convex
image. **Loc₀** is its connected part, the paper's GH. A **local relation** assigns to
each spacetime a relation between its events that every morphism preserves and
reflects (the paper's LC). A **becoming theory** is a local relation that is transitive
and contains the chronological past. The **germ** of a spacetime at an event is its
local isometry class there. A class of spacetimes is **restriction-closed** if it
contains the causally convex open subsets of its members.

## 1. No spacelike scale ★

**Theorem 1.** Let a restriction-closed class contain Minkowski spacetime 𝕄 and the
flat cylinders ℝ × ℝ² × S¹. A local relation on it relates either no spacelike pair of
𝕄 or every one.

*Proof.* On 𝕄 the verdict depends only on the interval s, say through f(s). On the
cylinder with circle of length ℓ, take two events on the slice t = 0 at arc distance a.
Thin tubes in that slice join them the short way and the long way. The interior of the
domain of dependence of each tube is causally convex in the cylinder and is isometric
to the corresponding region of 𝕄, where the events are at interval a and ℓ − a.
Locality, applied to both inclusions of both regions, gives f(a) = f(ℓ − a). Taking
a = s and ℓ = s + s′ gives f(s) = f(s′). ∎

The proof uses only flat spacetimes, so it holds on-shell. No transitivity is used.

**Theorem 3 (all local relations on 𝕄).** The restriction to 𝕄 of a local relation is
a union of: the diagonal; all future null pairs; all past null pairs; all spacelike
pairs; and the timelike pairs whose proper time lies in an arbitrary set, separately
for each time direction. Every such union occurs, because equality, horismos, causal
unrelatedness and Lorentzian distance are preserved and reflected by morphisms.

**Corollaries.**

- A symmetric local relation among causally unrelated events of 𝕄 is empty or is
  spacelike separation. Dropping transitivity buys the whole elsewhere and nothing
  thinner.
- A local transitive relation contains no spacelike pair of 𝕄 or is universal there.
  Chronological becoming is not needed for that.
- A present can be thick in time and stay local. It cannot be selective in space. The
  causal hull of a timelike pair is a diamond, which fixes their proper time. The
  causal hull of a spacelike pair is two points.

## 2. Unrelated events are related only through their germs

**Theorem 2.** On a restriction-closed subclass of Loc, the verdict of a local relation
on a causally unrelated pair depends only on the two germs.

*Proof.* Small diamonds around the two events form a causally convex subset with two
components, which is an object of Loc. An isometry of germs carries small diamonds to
small diamonds. ∎

In Fewster and Verch's framework unions of causally disjoint diamonds are standard
objects, so this is an observation in their setting. In the connected category it needs
a gluing argument that has only been sketched.

## 3. The no-local-clock criterion

Let a class be restriction-closed, closed under finite disjoint unions, and contain 𝕄.
Write g ⊴ g′ if some member has events w ≪ x with germs g and g′. A **local clock** is
a function of germs into an ordered set that is monotone along ⊴. It is nontrivial if
it takes two comparable values.

**Theorem 4.** The following are equivalent.

1. Every becoming theory that is not universal on 𝕄 lies inside the causal past in
   every member. (The paper's main theorem, part (a), on this class.)
2. The class has no nontrivial local clock.
3. Every germ can be reached from the flat germ, and can reach it, by a finite chain
   of ⊴ steps.

*Proof.* (3 ⇒ 1) A related spacelike pair gives, by Theorem 2, a relation ρ on germs.
In a disjoint union, chronological becoming and transitivity show ρ is closed under ⊴
on the left and under its converse on the right. Chains then give ρ(flat, flat), so the
theory relates spacelike pairs of 𝕄 and is universal there. (1 ⇒ 2) Given a clock κ,
the relation "x ≪ b, or x = b, or κ(x) < κ(b)" is a becoming theory equal to I⁻ on 𝕄
that relates unrelated events. (2 ⇒ 3) The indicator of the germs reachable from flat
is a clock, and so is the indicator of those that cannot reach flat. ∎

In the connected category one direction survives: a two-valued local clock that
varies inside one member defeats the theorem there.

**Consequence.** The paper's open pocket problem asks for one spacetime containing a
whole curved slab and flat pockets joined by a flat slab. Criterion 3 asks only that
each single germ occur after and before a flat region, in possibly different
spacetimes. Whether the dominant-energy class satisfies it is open.

## 4. A curvature clock ★

Take the spacetimes whose Ricci scalar never increases along future causal curves. The
class is restriction-closed and contains 𝕄, every vacuum spacetime and expanding dust
FLRW. On it the three relations below are local, transitive and contain I⁻.

| Relation | On 𝕄 | On expanding dust | What fails on this class |
|---|---|---|---|
| J⁻, or Scal(x) > Scal(b) | J⁻ | every earlier epoch has become | Main theorem (a) |
| J⁻, or Scal(x) ≥ Scal(b) with Scal(x) > 0 | J⁻ | cosmic time, with shared presents | No-shared-present corollary |
| Scal(x) ≥ Scal(b) | universal | cosmic time | Main theorem (b) |

So the off-shell premise cannot be dropped in general, and cosmic becoming read off a
curvature scalar is local. What it violates is the demand that the rule work on every
kinematically possible geometry. The class is not realistic: a star has a spacelike
density gradient.

## Credits

- The locality of the rule Scal(x) ≥ Scal(b) was already noted in
  [DRAFT.md](../DRAFT.md) §4.4. What is added is the class, the shared-present variant
  and Theorem 4.
- Fewster and Verch (arXiv:1106.4785v3, §§2.1–2.2 and 4.3, read) supply the category,
  and already build order-valued functors from a scalar-curvature threshold for
  another purpose.
- Nothing matching Theorem 1 was found in four short searches. It may be known in
  locally covariant field theory.

## Limits

- Theorem 1 uses reflection through the cylinder. Restricting locality to simply
  connected targets escapes it.
- Theorems 2 and 4 are proved with disconnected objects. If a becoming rule need not
  cover those, the equivalence is unproved.
- Theorem 4 does not prove the on-shell theorem. It restates what must be shown.
- An earlier draft claimed that criterion 3 is necessary in the connected category.
  That was wrong and is removed.
