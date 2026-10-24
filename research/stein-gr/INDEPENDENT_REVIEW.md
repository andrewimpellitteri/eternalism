# Independent check of the first Stein–GR draft

24 October 2026. Review of `DRAFT.md` as read in this session. The draft is
being developed concurrently; line references below refer to that snapshot.
This note does not edit the draft, certify priority, or accept Theorem 2.

## Disposition

The cross-spacetime hypothesis answers the earlier single-spacetime dust
test: that example is not a counterexample to the stated theorem. The
remaining proof has a false existence claim, but it has a short repair.
The main domain-of-dependence step can also be supplied, conditional on
the adapted coordinates and cone bounds. Details follow so that these
are usable repairs rather than merely requests for more proof.

## 1. A false claim in the universal branch, and its replacement

Draft lines 195–197 assert that any causally related pair has a third event
spacelike to both. This fails in globally hyperbolic spacetimes with compact
Cauchy surfaces. Take the Einstein static spacetime

    M = R × S^3,  g = -dt^2 + h_round,

with unit-radius round S^3. Let b=(0,p), x=(3π,p). If z=(τ,q) is spacelike
to b, then |τ| < d(p,q) ≤ π. If it is spacelike to x, then
|τ-3π| < d(p,q) ≤ π. The two inequalities are incompatible. Every constant-t
slice is Cauchy, so the example lies in the draft's category.

**Repair (finite spacelike chains).** On a connected GH spacetime define
p~q when they are joined by a finite chain of spacelike pairs. Every
equivalence class is open: choose z spacelike to p in a causally convex
normal neighborhood. Since J^+(z) and J^-(z) are closed in a GH spacetime,
some open neighborhood V of p consists entirely of points spacelike to z.
Every q in V is joined to p by p,z,q. Connectedness now implies that there
is only one equivalence class. Once all ordered spacelike pairs belong to B,
transitivity along a finite chain gives B=M×M. No common spacelike event
for arbitrary distant pairs is needed.

## 2. Cone interpolation: a sufficient quantitative proof

Use explicit conventions

    η_c = -c^2 dt^2 + ds^2 + |dy|^2,   0 < μ < 1 < λ.

Suppose the Euclidean operator norm of g-η_1 is at most ε on the entire
support of the cutoff, with

    ε < min{1, (1-μ^2)/(1+μ^2), (λ^2-1)/(1+λ^2)}.

For h=χg+(1-χ)η_1 the same norm bound holds. Its spatial block is positive
definite and h(∂t,∂t)<0; the Schur complement therefore proves Lorentzian
signature. For v=(1,u), |u|≤μ implies h(v,v)<0, while |u|≥λ implies
h(v,v)>0. Thus the η_μ timelike cone is inside h's, and h's causal cone is
inside the η_λ timelike cone. Choose the common time orientation using ∂t.
This avoids relying on a general convexity claim for arbitrary Lorentzian
metrics. The estimate must hold on T_{3r}, not just T_r.

On R^4 the uniform outer cone bound also gives the claimed Cauchy property:
a future causal curve has |d(s,y)/dt|≤λ. If its t-coordinate has a finite
endpoint, its spatial coordinates have a finite limit and the curve is
extendible. Hence every inextendible causal curve crosses every t-level.

## 3. Lemma D: first-exit proof supplying the missing localization

Make Σ a **closed** spatial slab (or a smoothly rounded closed version)
inside t=0, with transverse radius r/2 and longitudinal interval
[-r/2,L+r/2]. The displayed Σ in the draft has an open transverse ball
and is not compact. Its interior contains x,b; this is preserved by rounding.

Required coordinate hypotheses must be explicit:

1. The chart contains the closure of T_{3r}, with t=0 lying in the original
   smooth Cauchy surface S throughout this chart, not merely along c.
2. Both metrics contain the η_μ timelike cone on this tube, with μ>1/2.
3. They agree on T_{2r}; t=0 is part of a Cauchy surface in each ambient
   spacetime. In M' this is the full coordinate hyperplane.

**Local escape paths.** Every point q on the boundary of T_{2r} with t(q)>0
has a past-directed timelike path, contained in T_{3r}, to a point of
S\Σ. For a lateral or longitudinal boundary point, use a vertical path.
For t(q)=2r, use a vertical path if its spatial projection is already
outside Σ. Otherwise travel transversely outward with coordinate speed
μ/2 until t=0. The transverse displacement is μr>r/2, so its endpoint
is outside Σ, while the path stays inside T_{3r}. Its speed is strictly
less than μ, so it is timelike for both metrics. Reverse time for t(q)<0.
At t=0 the shell is already disjoint from Σ. Paths can be smoothed without
losing these strict inequalities.

Since S is Cauchy (in particular acausal), a past extension after reaching
S\Σ cannot encounter Σ. Thus each positive-time shell point has a
past-inextendible causal curve avoiding Σ; analogously for the negative
shell and future curves.

**Localization in each ambient spacetime.** If p belonged to D^+(Σ) outside
T_{2r}, any past-inextendible causal curve from p would meet Σ. Its segment
before that meeting crosses the shell at q with t(q)>0: a shell crossing
with t≤0 could not be causally followed by a point on Σ, because vertical
paths place such q on or below the same Cauchy surface. Replace the remainder
of the curve at q by the local escape path and its past extension. This
gives a past-inextendible curve from p avoiding Σ, a contradiction. The
argument for D^-(Σ) is the time reverse. Hence D(Σ)⊂T_{2r} in both ambients.
This is the missing argument; local cone bounds should not simply be
asserted to imply global containment.

**Transfer in both directions.** Let p∈D_M^+(Σ), hence p∈T_{2r}. If p were
not in D_{M'}^+(Σ), choose a past-inextendible M'-causal curve avoiding Σ.
If it first exits T_{2r}, its preceding segment is also M-causal, and at
the exit point the local escape construction supplies an M-causal past
extension avoiding Σ. This contradicts p∈D_M^+(Σ). If it never exits,
the Cauchy property in M' forces it to cross t=0 at a point outside Σ;
the same segment in M, extended past S, again contradicts membership.
Interchange M and M' for the reverse inclusion, and reverse time for D^-.
This proves the transfer once the stated hypotheses are established.

The standard result that int D(Σ) is globally hyperbolic and causally
convex, and its connectedness here, should still receive a precise source
or proof. On the initial surface Σ is connected; each domain point can be
joined causally to its initial surface without leaving the domain.

## 4. Make the second flat transfer explicit

Draft lines 185–189 need more than a spacelike tangent along an arbitrary
detour: the detour must be acausal in both ambient spacetimes and lie on
appropriate Cauchy hypersurfaces. Here is an explicit option in the original
global R^4 coordinates (x at s=0, b at s=L):

    t(s) = -4r + (8r/L)s,
    y(s) = (10r sin(πs/L), 0),   0≤s≤L.

Choose 8λr<L. This curve lies in the hyperplane t=-4r+(8r/L)s,
which is spacelike and Cauchy for both η and g' by the uniform outer cone
bound. Where |t|≤3r, s/L lies in [1/8,7/8], so
|y|≥10r sin(π/8)>3r. Everywhere else |t|>3r. Consequently the curve is
entirely outside the metric modification, with a flat neighborhood of
positive width. Apply the local domain-transfer argument to a sufficiently
thin compact slab around this curve in that common hypersurface.
Reverse the sign of t(s) for the detour used in the universal branch.
This repairs the needed geometric construction without assuming that every
spacelike curve is globally acausal.

## 5. Checks passed and work still open

- Clifton–Hogarth, pp. 365–367: the three cases use spatial rotations,
  boosts and translations. The required rotations can be chosen in SO(3);
  no spatial reflection or time reversal is needed. This proof obligation
  passes at the level of the argument read, without invoking an abstract
  implication from automorphism invariance to model-theoretic definability.
- Bernal–Sánchez, arXiv:gr-qc/0512095v1, Theorem 1.1 and Remark 4.14:
  the stated extension of a compact acausal spacelike submanifold to a
  smooth Cauchy surface, including disconnected submanifolds, matches Lemma A.
  Read depth: the theorem and indicated discussion, not whole-paper audit.
- The null-concatenation condition and Weyl-gated example have no identified
  algebraic failure in this review; this is not an independent completed
  construction of the example with a mixed flat/curved GH spacetime.
- Still open: a fully specified adapted chart with t=0 agreeing with S;
  the separate future-pair reduction (especially null pairs); exact source
  locators for the causal-domain facts; priority; and integration of these
  repairs into a single consistently quantified proof.
- Scope: the category includes arbitrary GH metrics and all the specified
  embeddings, not just solutions of one fixed Einstein–matter system.
  An arbitrary metric interpolation need not remain in such an on-shell
  theory. Any physical interpretation must retain this distinction.

Source checked online: https://arxiv.org/html/gr-qc/0512095 .
Clifton–Hogarth was read from the locally extracted primary-paper text
`scratchpad/pdftext/ch1995.txt` supplied by the concurrent Claude session.
No literature-completeness or novelty verdict is made here.
