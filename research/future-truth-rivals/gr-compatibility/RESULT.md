# Placek’s Definition 15 on the closed-dust causal order

27 October 2026. Bounded clause-level check of a one-patch candidate. No later
generalized-manifold, atlas, or tangent-space postulates are claimed.

## Candidate

Use the closed-dust conformal cylinder

    M = (0,2π) × S³,
    g = a(τ)²(−dτ² + dΩ₃²),    a(τ)>0,

with its exact causal order, including equality:

    (τ,Y) ≼ (σ,Z)  iff  τ≤σ and dₛ₃(Y,Z)≤σ−τ.

The equivalence follows directly from the metric. Along any future causal curve,
round-sphere speed with respect to τ is at most one, so spatial distance is at
most elapsed conformal time. Conversely, when the distance is at most the time
difference, traverse a minimizing S³ geodesic at constant speed
`dₛ₃(Y,Z)/(σ−τ)≤1`; this gives a future causal curve. Equality at equal times
forces the same spatial point.

Take W=M and the single patch O={M}; for every e, take Oₑ={M}. Definition 15
does not require patches to be proper subsets or supply an atlas at this stage.
The clauses below establish that this is a genBST model under Definition15
with an explicit nonempty-chain convention. That convention is a source-
interpretation qualification, not wording verified in its displayed axiom.

## Definition 15 checks

**Partial order and density.** The displayed relation is reflexive and
transitive. If p≼q and q≼p, their conformal times agree, hence their spatial
points agree, so it is antisymmetric. For p≺q, take a minimizing spatial
geodesic and traverse it at constant speed over the time interval from p to q.
Its midpoint is a distinct event strictly between p and q. This also covers a
null-related pair, where the geodesic is traversed at speed one. Thus the
causal order is dense. It is nonempty.

**Clause 2(a), maximal-chain neighborhood.** No smooth-curve theorem is needed.
For any e=(τ,Y), events at the same Y with slightly smaller and larger τ are
strictly causally before and after e; hence W has no minimal or maximal
elements. By the usual maximal-chain principle (Zorn’s lemma, hence choice), take a
maximal chain t containing e′; no causal-curve theorem is involved. If e′ had
no chain member strictly above it, any q≻e′ would be comparable with every
point of t: every point of t is ≤e′, and transitivity gives that point ≤q. Then
q could be added to t, contradicting maximality. The symmetric argument
rules out e′ having no chain member strictly below it. Choose x≺e′≺y in t.
Since O=M, the required segment `t_{>x} ∩ t_{<y}` is a subset of O
automatically. This proves 2(a).

**Chain representation for 2(b) and 2(c).** Let C be a nonempty chain. Two
distinct events in C cannot have the same conformal time, because the causal
order at equal time relates only identical events. Its time projection X⊆(0,2π)
therefore gives a function f:X→S³, and for s<t in X, comparability and the
exact causal-order formula give

    dₛ₃(f(s),f(t)) ≤ t−s.

So f is 1-Lipschitz. S³ is complete. Any sequence in X tending to an endpoint
of X is consequently mapped to a Cauchy sequence with a unique limit, and the
limit is independent of the chosen endpoint sequence.

**Clause 2(b), lower-bounded chains.** Suppose C has a lower bound
q=(τq,Yq)∈M. Put τ₋=inf X. Since every s∈X obeys s≥τq>0, we have
τ₋∈(0,2π). If X has a minimum, let p be the corresponding member of C. If it
has no minimum, choose a coinitial sequence sₙ∈X with sₙ↓τ₋ and let
Y₋=lim f(sₙ), p=(τ₋,Y₋). For any c=(t,f(t))∈C, either p=c at the minimum or
pass to the limit in `dₛ₃(f(sₙ),f(t))≤t−sₙ` (using terms with sₙ≤t). This gives
p≼c, so p is a lower bound. If z=(u,Z) is any lower bound of C, then u≤s for
all s∈X, hence u≤τ₋. Passing to the limit in `dₛ₃(Z,f(sₙ))≤sₙ−u` gives
`dₛ₃(Z,Y₋)≤τ₋−u`; thus z≼p. Therefore p is the greatest lower bound in M,
and it is unique by antisymmetry. In the attained-minimum case no sequence
is needed: p∈C is below all members and every lower bound is below p.

**Clause 2(c), upper-bounded chains.** Suppose C is bounded above by
b=(τb,Yb)∈M. Put τ₊=sup X. Then τ₊≤τb<2π, so τ₊∈(0,2π). If X has a maximum,
let p be that member; otherwise choose a cofinal sequence sₙ∈X with sₙ↑τ₊ and
put p=(τ₊,Y₊), where Y₊=lim f(sₙ). Passing to the limit in the causal-order
inequalities shows c≼p for all c∈C and p≼b. For any upper bound z=(u,Z) of C,
we have u≥τ₊; passing to the limit in `dₛ₃(f(sₙ),Z)≤u−sₙ` gives p≼z.
Consequently p is the least upper bound of C, independently of which upper
bound b was used. In particular, the set

    {x∈O : every c∈C obeys c≼x and x≼b}

has the unique minimum p, as required by 2(c).

In the attained-maximum case, p∈C is above all members, below b, and below
every upper bound directly, without introducing a limiting sequence.

The nonempty-chain convention is explicit here but not explicitly stated
in Definition15's displayed wording. If the empty set counted as a chain,
clause2(b) would require a greatest element of W, and the clause2(c) set
for C=∅ would be the entire causal past of b, which has no minimum. Both
clauses would fail. The earlier Definition1 explicitly excludes empty
chains; the omission in Definition15 leaves a source-reading qualification.
We do not claim an unconditional literal correspondence or diagnose a
source error without establishing the convention.

**Clauses 2(d), 3 and 4.** With O=M, interval closure (2d) is immediate;
choose Oₑ={M} for every e, so every event lies in a patch and the patches are
covered (3); the overlap-order agreement (4) is tautological for the single
patch.

## Consequence for splitting pairs and histories

Definition 17’s splitting pair requires two distinct minima above one chain,
relative to two upper bounds. Clause 2(c), as proved above, gives the same
least upper bound for that chain independently of the chosen bound. Therefore
there are no splitting pairs in this one-patch model. By Definitions 19–23,
all events are pairwise consistent and W itself is the unique maximal
consistent subset, hence the one generalized history. No global common-future
condition is imposed on its events. In particular, the antipodal events at
τ=3π/2 still have no common future inside M, as established in the adjacent
coordinator result; that does not prevent this generalized-history
construction.

This establishes the requested one-patch Definition15 correspondence for the
exact causal order conditional on nonempty chains. It does not establish that the single global patch yields
the intended local geometry, nor does it check Placek’s later topology, chart,
connectedness, countability, or tangent-space postulates in §§4.2–4.3. The
result is a clause-level compatibility check, not a full GR construction or
novelty claim.

## Primary source clauses inspected

Tomasz Placek, “Branching for General Relativists,” in *Nuel Belnap on
Indeterminism and Free Action* (2014), pp.191–221, DOI
10.1007/978-3-319-01754-9_10; original chapter PDF:
https://ruj.uj.edu.pl/server/api/core/bitstreams/4a4f0f7e-b396-4861-be25-8bd3f5cd531f/content

- Introduction, p.192: standard BST histories are maximal upward-directed
  subsets; the later-witness requirement motivates changing the history
  criterion for GR.
- §4.1, Definition 15, pp.200–201: generalized model, patch clauses 2(a)–(d),
  patch coverage and overlap-order agreement.
- §4.1, Definition 17, p.201: local splitting pairs from two distinct
  bound-relative minima above a common chain.
- §4.1, Condition 18 and Definitions 19–23, pp.202–203: Hausdorff separation,
  consistency, maximal consistent sets and generalized histories.
- §6, pp.217–218: relation between generalized histories and the later
  manifold construction; those later results are outside this check.

Read depth: selected full-text clause inspection in the original PDF. No
complete proof audit of Placek’s chapter is claimed.
