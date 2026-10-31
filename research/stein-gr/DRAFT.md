# Stein's theorem in general relativity — working draft

24 October 2026. Claude session draft for independent proof check. Not
reviewed. Nothing here is a novelty claim until the checks below pass.

## 0. Question

Clifton & Hogarth (1995, Synthese 103, p. 385) leave open whether their
Minkowski becoming theorems extend to general relativity: "each general
relativistic spacetime has its own metric-preserving automorphisms and each
its own distinctive geometry, leaving no obvious way to extend Theorem 1
beyond Minkowski spacetime, much less to extend Theorem 2." This draft
proposes a formalization and a partial answer.

Key observation (also Codex's dust test, §5.3): within a single curved
spacetime, metric definability (isometry invariance) is far weaker than in
Minkowski, because generic spacetimes have no isometries. A single-spacetime
analogue of Stein's theorem is therefore false. The proposal replaces
"definable in one spacetime" by "one rule, uniform across all globally
hyperbolic spacetimes, compatible with isometric embeddings of causally
convex regions" (local covariance, in the sense of Brunetti–Fredenhagen–Verch
2003). The classification is then *derived* by a gluing argument; it is not
built into the axiom. §4.4 isolates exactly which assumption excludes
curvature-defined alternatives.

## 1. Framework

Dimension n = 4 (Clifton–Hogarth's Theorem 1 is proved for R^4).

**GH**: objects are connected, oriented, time-oriented, globally hyperbolic
smooth Lorentzian 4-manifolds (M, g). Morphisms ψ: M → M' are smooth
isometric embeddings preserving orientation and time orientation, with
ψ(M) open and causally convex in M'.

Conventions (as Clifton–Hogarth): I^-, J^- are taken reflexive. U_M = M×M.
"x B b" reads "x has become for b"; B(b) = {x : x B b}.

A **becoming theory** is an assignment M ↦ B_M ⊆ M×M satisfying, for every M:

- (LC) local covariance: for every morphism ψ: M → M',
  x B_M b ⇔ ψ(x) B_{M'} ψ(b).
- (T) B_M is transitive.
- (CB) chronological becoming: I^-_M ⊆ B_M.

Remarks. (CB) is derived by Clifton–Hogarth's Lemma (p. 364) from
"worldline becoming" + "worldline transitivity" + meshing; in curved
spacetime the same derivation works verbatim (any chronological pair is
joined by a timelike curve). (LC) includes invariance under every
time-orientation- and orientation-preserving isometry of each M, which for
Minkowski is the proper orthochronous Poincaré group.

## 2. Results

**Proposition 0 (one spacetime is not enough).** If M is a spacetime with no
nontrivial isometries and x, b ∈ M are spacelike-separated, then
R = J^- ∪ (J^-(x) × J^+(b)) is reflexive, transitive, contains I^-, is
invariant under all isometries of M, and relates x to b. (Transitivity: the
only nontrivial composition, P∘P, would require q ∈ J^+(b) ∩ J^-(x), hence
b ≤ x.) So Stein-type uniqueness fails completely for single generic
spacetimes; Theorem 2 below depends on requiring one rule across spacetimes.
Codex's dust-cosmology example is a symmetric special case.

**Theorem 1 (flat case; Clifton–Hogarth).** B_{R^{1,3}} ∈ {I^-, J^-, U}.

*Proof.* Proper orthochronous Poincaré maps are automorphisms of Minkowski
in GH, so by (LC) B_Mink commutes with them. Clifton–Hogarth Theorem 1
(p. 365) gives the conclusion from definability + transitivity + chronological
becoming; they state (p. 385–386) that the proof does not use spatial
reflections, and it uses only translations, rotations and boosts (proof
pp. 365–367). ∎ [CHECK: confirm no step of their proof uses an
orientation-reversing map.]

**Theorem 2 (no becoming outside the causal past).**
(a) If B_Mink ≠ U, then B_M ⊆ J^-_M for every M in GH.
(b) If B_Mink = U, then B_M = U_M for every M in GH.

Hence, for every becoming theory, either B_M = U_M for all M, or
I^-_M ⊆ B_M ⊆ J^-_M for all M.

**Theorem 3 (classification of the residual freedom).** Let B be a
non-universal becoming theory and N_M := B_M ∩ (J^-_M \ I^-_M) (the
null-related pairs it includes). Then N is locally covariant and
null-concatenation closed:

  (NC) if (x,y), (y,b) ∈ N_M and (x,b) ∈ J^- \ I^-, then (x,b) ∈ N_M.

Conversely, for any locally covariant N ⊆ J^- \ I^- satisfying (NC),
B := I^- ∪ N is a becoming theory. On Minkowski, N is either empty or all
null-related pairs (by Theorem 1).

**Theorem 4 (non-uniqueness).** There are becoming theories with
B_Mink = I^- that, on curved spacetimes, differ from I^-, J^- and U. Example:
N_M(x,b) iff x ∈ J^-(b) \ I^-(b), x ≠ b, and some null geodesic segment from
x to b contains a point where the Weyl tensor is nonzero. This N depends
only on the conformal structure (Weyl tensor and unparametrized null
geodesics are conformally invariant), so uniqueness fails even for becoming
relations determined by causal structure alone.

**Proposition 5 (regularity selects the endpoints).** For a non-universal
becoming theory: if every B_M is closed in M×M then B = J^-; if every
B_M \ Δ_M is open then B = I^-.

**Proposition 6 (locality is indispensable).** Natural but non-local rules,
e.g. "x B b iff τ(x) ≤ τ(b)" for a cosmological time function τ
(Andersson–Galloway–Howard) or a CMC time where defined, are invariant under
all isometries, transitive and satisfy (CB), yet relate spacelike pairs.
They violate (LC) because τ depends on regions outside every causally convex
neighbourhood of {x, b}. [TO WRITE: precise definition on all of GH, e.g.
J^- where τ is not regular.]

## 2b. Further results (added 24 Oct, unreviewed)

**Proposition 7 (Gödel-type universes are isolated).** Extend the category to
all oriented, time-oriented spacetimes, same morphisms. If M is totally
vicious (p ≪ p for all p; e.g. Gödel's universe), then (i) every morphism
ψ: N → M is onto, since ψ(N) is a nonempty causally convex open subset and
the only such subset of a totally vicious spacetime is M (MS Remark 2.12);
(ii) any theory satisfying (CB) has B_M = U_M, since I^-(p) = M.
Consequence: local covariance transmits constraints only along morphisms,
and the only morphisms into a totally vicious spacetime are its own
isometries. So universal becoming in Gödel's universe (Gödel's first step,
in Stein's terms) places no constraint, via (LC), on becoming in globally
hyperbolic spacetimes. Gödel's modal step needs a cross-world link stronger
than local covariance, and any such link is non-local. [TO CHECK: whether a
totally vicious spacetime can embed as a proper causally convex region of a
non-vicious spacetime; the claim above only uses morphisms *into* M.]
Literature to compare: Gödel 1949; Monton 2006 §6; Dieks 2006; Aames 2022;
Savitt 2005, 2017; Manchak 2016 ("On Gödel and the ideality of time").

**Proposition 8 (causal sets: Stein's theorem holds exactly).** Category:
locally finite posets (finite or countable), morphisms order-embeddings with
order-convex image. Becoming theory: (LC), (T), (CB: x ≤ b ⇒ x B b). Then
either B_C = ≤_C for every C, or B_C = C×C for every C.
Proof. If x, b are incomparable, {x, b} is convex (nothing lies between
incomparable elements), so both embeddings of the 2-antichain A2 into C are
morphisms; hence the verdict on incomparable pairs is one bit β, the same in
every causet and symmetric. If x > b, the interval I = [b, x] is finite and
convex, so x B_C b depends only on I. Case β = 1: in C' = I ⊔ {z} (z
incomparable to all), x B z B b, so the verdict on I is "yes"; with (CB),
B = universal. Case β = 0: if x B b for some x > b, let C' = I ∪ {e} with
e < x only. I is convex in C', so x B_{C'} b; e B x by (CB), so e B b with e
incomparable to b, contradicting β = 0. Hence B = ≤. ∎
Remark: discreteness removes exactly the freedom of Theorem 3, because a
causal set has no null boundary. Birth-order (labelling) relations of
sequential growth are not locally covariant; the covariant answer is ≤.
Contrast with Wüthrich & Callender (arXiv:1502.00018v1, §3, full text read;
BJPS 68(3) 2017 version not collated). They state that "The analogue of this
theorem, however, is straightforwardly false in CST", using automorphism
invariance within one causet: on the diamond causet d < b, c < a their
relation R adds ⟨b,c⟩, ⟨c,b⟩ to ≤ and is "invariant under automorphisms of
the structure", since b, c form a "non-Hegelian pair". Under (LC) this R is
not the restriction of any becoming theory: {b, c} is a convex 2-antichain,
so relating b to c fixes β = 1, and then Proposition 8 makes B universal on
every causet, including ⟨b, d⟩ ∈ B, which R excludes. So the same diagnosis
as in the continuum applies: definability inside one structure is too weak;
locality across structures restores Stein's theorem, here exactly. Their own
footnote 5 notes the counterexample "could be a small proper part of a much
larger causet"; (LC) is precisely the requirement that the relation on such a
part agree with the relation in the larger causet.

**Framing (Fewster & Verch 2011, arXiv:1106.4785, "Dynamical locality and
covariance: What makes a physical theory the same in all spacetimes?").** A
becoming theory is "the same in all spacetimes" in exactly the sense of
locally covariant QFT (Brunetti–Fredenhagen–Verch 2003). Their standard
category also contains all globally hyperbolic metrics, not only solutions
of Einstein's equations; so the off-shell premise of Theorem 2 (§4.5) is the
standard one in that literature, not an ad hoc loophole. [Read depth:
full text of arXiv:1106.4785v3 and math-ph/0112041v1 by a subagent; to be
re-checked before citing. Their Loc / Man is defined kinematically: objects
are globally hyperbolic, oriented, time-oriented spacetimes, morphisms
isometric embeddings with causally convex image preserving orientation and
time-orientation; no field equation appears in the definition. Neither paper
argues explicitly for including off-shell metrics. Deformation arguments
(Fulling–Narcowich–Wald) are used, FV §2.3.]

## 7. Hard branches (scouting, ranked)

H1. **On-shell Theorem 2.** Require becoming only on vacuum (or
energy-condition) solutions. The proof needs: given a vacuum region D_M(Σ)
around a spacelike pair, a vacuum spacetime containing an isometric copy of
it and exactly flat regions chronologically adjacent to x and b (w ≪ x,
b ≪ v) joined by a flat detour. By uniqueness of Cauchy developments this is
an initial-data / characteristic gluing problem. Tools: Carlotto & Schoen
2014 (arXiv:1407.4766, localized solutions of the constraint equations);
Aretakis, Czimek & Rodnianski 2021 (arXiv:2107.02441, 2107.02449,
2107.02456: characteristic gluing, with obstructions given by ten conserved
charges). Plane-wave sandwich spacetimes show the needed configuration
(flat region in the chronological past of a curved one) does occur in
vacuum. Deliverable within reach: Theorem 2 conditional on a precisely
stated gluing hypothesis G, plus G verified in a special class. Full G is
genuinely hard PDE work and may meet the ACR charge obstructions.

H2. **Physical selection of the null boundary.** Theorem 3 leaves only the
status of horismotic pairs open. Ask whether a physical principle decides it:
e.g. compatibility with the Fewster–Verch measurement framework in locally
covariant QFT (state update in causal futures), or "every event that can
influence b has become for b" via massless fields (gives J^-). A theorem
"measurement-compatible becoming is J^-" would remove the residual freedom
physically. Speculative; needs reading Fewster–Verch measurement papers.

H3. **Worldline-dependent becoming in GR** (Clifton–Hogarth Theorem 2
analogue). Same gluing, but the gluing must also carry an observer
worldline; stabilizers are trivial in curved spacetime, so meshing does more
work. Moderate.

H4. **Beyond global hyperbolicity.** Strongly causal or merely causal
spacetimes (no Cauchy surfaces through spacelike pairs). Needs local
replacements for Lemma A. Moderate–hard; connects to Proposition 7.

Scouting result for H1 (subagent, abstract depth): no existing theorem gives
G. Carlotto–Schoen produce exactly flat data only in a cone at infinity;
Aretakis–Czimek–Rodnianski need data near Minkowski and meet ten charge
obstructions; Czimek–Rodnianski (arXiv:2210.09663) remove the obstructions
but glue to Schwarzschild, not Minkowski. Structural point: if the flat region
contained a whole asymptotic end, positive-mass rigidity would force M' to be
Minkowski, so G needs bounded interior flat regions adjacent to an arbitrary
curved vacuum region. Open.

H1'. **Energy-condition version (middle branch).** Take the category of GH
spacetimes whose Einstein tensor satisfies the dominant (or null) energy
condition. Minkowski and the original M qualify; the difficulty is only the
interpolation zone, where the off-shell construction makes G_ab of size
~K/r with no sign control. This is an inequality-gluing problem, not an
equation-gluing problem, so it may be tractable (compare Corvino–Huang,
arXiv:1606.03078, DEC-preserving compactly supported deformations of initial
data; abstract depth). A positive result would say: Theorem 2 holds even if
becoming is only defined on spacetimes with physically reasonable matter.

Recommended order: finish Theorems 2–4 + Props 5–8 (core paper); then H1 as
the flagship hard extension, stated conditionally if G is not fully proved;
H2 as a short speculative section only if a theorem appears.

## 3. Proofs

Sources for standard causal facts: Minguzzi & Sánchez, "The causal hierarchy
of spacetimes" (arXiv:gr-qc/0609119v3; ESI Lect. 2008, DOI 10.4171/051-1/9),
cited as MS. Read at full text for the cited items:
- MS Prop. 2.16: I^+ is open in M×M.
- MS Prop. 2.17: cl J^+ = cl I^+, Int J^+ = I^+, boundaries coincide.
- MS Prop. 2.31: p,q horismotic ⇔ joined by a maximizing lightlike geodesic;
  (i) p ≪ r ≤ q ⇒ p ≪ q (and dually); (ii) r ∈ E^+(p), q ∈ E^+(r) ⇒
  q ∈ E^+(p) or p ≪ q. (E^+ = J^+ \ I^+, horismos.)
- MS Thm 2.30 (stated just before 2.31): a causal curve that is not a
  lightlike pregeodesic without interior conjugate points can be deformed
  (C^0-close) to a timelike curve with the same endpoints.
- MS Def. 3.63 + ladder: globally hyperbolic ⇒ causally simple, so J^±(p)
  are closed; MS Thm 3.75 (Geroch) and Thm 3.79 (GH ⇔ causal + compact
  diamonds / compact C(p,q)).
- Bernal & Sánchez 2006 (arXiv:gr-qc/0512095) Thm 1.1: in GH M, any spacelike
  acausal compact submanifold with boundary lies in a spacelike Cauchy
  hypersurface; Remark 4.14: the proof extends to non-connected such sets.

### 3.1 Theorem 3, Theorem 4, Proposition 5

Theorem 3. Given Theorem 2(a), B = I^- ∪ N with N ⊆ E^- := J^- \ I^-.
(LC) for N: I^- and J^- are locally covariant on causally convex images
(causal and timelike curves between points of a causally convex set stay in
it), so N = B ∩ E^- inherits (LC). (NC) is transitivity of B restricted to
horismotic pairs. Conversely, transitivity of B := I^- ∪ N: if one of the two
steps is chronological, MS 2.31(i) gives a chronological conclusion; if both
are in N, MS 2.31(ii) gives either a chronological pair or a horismotic pair,
and in the latter case (NC) applies. Reflexivity: I^- is reflexive by
convention. (CB) holds by construction. ∎

Theorem 4 (Weyl-gated example). N_M(x,b) :⇔ x ∈ E^-(b), x ≠ b, and some
lightlike geodesic segment from x to b contains a point where the Weyl tensor
is nonzero. (NC): if x→y→b along lightlike segments γ1, γ2 and x ∈ E^-(b),
then γ1γ2 is a causal curve from x to b between horismotic points, hence by
MS Thm 2.30 an unbroken lightlike pregeodesic; it contains γ1's Weyl point.
(LC): lightlike geodesics between points of a causally convex image stay in
it, and isometries preserve the Weyl tensor. Weyl = 0 in Minkowski gives
B_Mink = I^-; in Schwarzschild exterior (Weyl ≠ 0 everywhere) B = J^- there;
on a spacetime flat on an open set and curved elsewhere B lies strictly
between I^- and J^-. Conformal invariance: the Weyl tensor (as a (1,3)
tensor) and unparametrized lightlike geodesics are conformally invariant
(MS §2.6 for the latter). ∎

Proposition 5. If B is closed and contains I^-, it contains cl I^- = cl J^-
⊇ J^- (MS 2.17), so B = J^- by Theorem 2(a). If B \ Δ is open and contained in
J^-, then B \ Δ ⊆ Int J^- = I^- (MS 2.17), so B = I^- (reflexive). ∎

### 3.2 Theorem 2

**Lemma R (future pairs reduce to spacelike pairs).** Let x ∈ J^+(b), x ≠ b.
Then there is e ∈ I^-(x) with e spacelike to b (e ∉ J^+(b) ∪ J^-(b)).

Proof. Let V be a convex normal neighbourhood of b that is causally convex in
M (GH ⇒ strongly causal; MS Thm 2.14 [CHECK locator] gives causally convex
neighbourhoods inside convex ones). In V, p ∈ J^±_V(b) iff exp_b^{-1}(p) is
future/past causal (MS Prop. 2.10), and J^±_M(b) ∩ V = J^±_V(b) by causal
convexity (MS Remark 2.12). Take b1 ∈ V \ {b} on a future causal curve from b
to x, so b ≤ b1 ≤ x, and put u = exp_b^{-1}(b1) (future causal, nonzero).
Choose a spacelike a ∈ T_bM with g(u, a) > 0 (if u = e0 + n̂ in an orthonormal
frame, a = n̂). For q_ε = exp_b(εa), let F(ε) = g(exp_{q_ε}^{-1} b1,
exp_{q_ε}^{-1} b1) = 2σ(q_ε, b1), with σ Synge's world function, smooth on
V × V. Since ∇_q σ(q, b1)|_{q=b} = −u (first variation / Gauss lemma),
F(ε) = g(u,u) − 2ε g(u, a) + O(ε²). In both cases g(u,u) < 0 and g(u,u) = 0,
F(ε) < 0 for small ε > 0, and exp_{q_ε}^{-1} b1 stays future-directed by
continuity; so q_ε ≪_V b1, hence q_ε ≪ b1. Also exp_b^{-1}(q_ε) = εa is
spacelike, so q_ε is spacelike to b in M. By MS 2.31(i), e := q_ε ≪ x. ∎

Consequence: if x B b with x ∈ J^+(b) \ {b}, then e B x by (CB) and e B b by
(T), with e spacelike to b. So in (a) it suffices to exclude spacelike pairs.

**Lemma A (Cauchy surface through two spacelike points).** If x, b are
spacelike-separated, {x, b} is a compact acausal spacelike 0-submanifold; by
Bernal–Sánchez Thm 1.1 with Rem. 4.14 there is a smooth spacelike (hence
acausal) Cauchy hypersurface S ∋ x, b. Choose a smooth embedded curve
c: [−1, L+1] → S, unit speed for the induced metric, with c(0) = x,
c(L) = b.

**Lemma B (adapted Gaussian coordinates).** Let n be the future unit normal
to S and h the induced Riemannian metric on S. Take an h-orthonormal frame
(e1 = c', e2, e3) along c with (n, e1, e2, e3) positively oriented, let
σ(s, y) = exp^h_{c(s)}(y2 e2 + y3 e3) (Riemannian exponential *of S*), and
Φ(t, s, y) = exp^g_{σ(s,y)}(t n(σ(s,y))). For |t|, |y| < r0 this is a
diffeomorphism onto a neighbourhood of c (tubular neighbourhood of a compact
embedded curve; Gaussian normal coordinates near S). Then {t = 0} ⊂ S on the
whole chart, Φ^*g = −dt² + h_t(s, y) exactly, h_0 = δ on c, and by smoothness
and compactness |Φ^*g − η| ≤ K(|t| + |y|) on cl T_{r0}. [Corrected after the
independent review: the earlier chart exponentiated with g along S-tangent
directions, so {t = 0} was not contained in S.]

**Lemma C (cone sandwich; bound from the independent review).** Write
η_c = −c² dt² + ds² + |dy|², 1/2 < μ < 1 < λ. If the Euclidean operator norm
of h − η_1 is at most ε < min{1, (1−μ²)/(1+μ²), (λ²−1)/(1+λ²)}, then: the
spatial block of h is positive definite and h(∂t, ∂t) < 0, so h is Lorentzian
(Schur complement); for v = (1, u), |u| ≤ μ ⇒ h(v,v) < 0 and |u| ≥ λ ⇒
h(v,v) > 0. Hence C(η_μ) ⊂ C(h) ⊂ C(η_λ) (future cones, time-oriented by ∂t).
The bound is preserved by h = χ g + (1−χ) η_1 for χ ∈ [0,1], so no convexity
claim about general Lorentzian metrics is needed. It must hold on T_{3r}.

**Construction of M'.** Fix μ, λ, ε0 and choose r ≤ r0/3 with 3Kr ≤ ε0 and
8λr < L. Let χ: R^4 → [0,1] be smooth, χ = 1 on T_{2r}, supp χ ⊂ T_{3r}.
On R^4 set g' = χ Φ^*g + (1 − χ) η. Then the Lemma C bound holds everywhere, so every
g'-causal vector is η_λ-causal and has dt ≠ 0. Hence t is strictly increasing
along future g'-causal curves, and |d(s,y)/dt| ≤ λ along them; if t had a
finite limit along an inextendible curve, the spatial coordinates would
converge and the curve would extend. So every inextendible g'-causal curve
meets every {t = c} exactly once. So each {t = c} is a Cauchy hypersurface and M' := (R^4, g') is
globally hyperbolic (MS Def. 3.74, Thm 3.75), connected, oriented, time
oriented by ∂_t; flat (= η) outside T_{3r}; and ψ := Φ^{-1}: Φ(T_{2r}) → T_{2r}
is an isometry onto (T_{2r}, g') preserving both orientations.

**Lemma D (the slab region is self-determined).** Let B0 = {s ∈ [−r/2,
L + r/2], |y| ≤ r/2} and Σ = Φ({0} × B0) ⊂ S, Σ' = {0} × B0 ⊂ M'.
(D1) Σ is acausal in M (⊂ acausal S) and Σ' is acausal in M' (t strictly
     increasing).
(D2) D_{M'}(Σ') ⊆ D_{η_μ}(Σ') ⊂ T_r. [η_μ-causal curves are g'-timelike, so
     every inextendible η_μ-causal curve through p ∈ D_{g'}(Σ') meets Σ'. The
     η_μ-domain of the flat slab is {|t| ≤ dist(x, ∂B0)/μ}, of height
     ≤ r/(2μ) < r.]
(D3) D(Σ) ⊂ T_{2r} in both M and M' (identifying via Φ). [Escape paths, as
     in the independent review: every point q of ∂T_{2r} with t(q) > 0 has a
     past-directed path in T_{3r}, timelike for both metrics (coordinate
     speed < μ), ending on S \ Σ: vertical if its projection is outside B0,
     otherwise outward at speed μ/2 until t = 0, giving transverse
     displacement μr > r/2. Past of S \ Σ a causal curve cannot return to
     S ⊃ Σ (S acausal). If p ∈ D^+(Σ) lay outside T_{2r}, a past-inextendible
     causal curve from p meets Σ, so it crosses ∂T_{2r} at some q with
     t(q) > 0 before that; replacing its remainder at q by the escape path
     gives a past-inextendible causal curve from p missing Σ. Time-reverse for
     D^-. This uses only that {t = 0} ⊂ S (Lemma B) in M, and that {t = 0} is
     Cauchy in M'.]
(D4) ψ(D_M(Σ)) = D_{M'}(Σ'). [Let p ∈ D^+_M(Σ) and γ' past-inextendible
     g'-causal from ψ(p). γ' leaves T_{2r} (t → −∞). If γ' missed Σ', pull back
     its initial segment up to its first exit point e' ∈ ∂T_{2r}, extend it to
     a past-inextendible M-curve; it meets Σ (p ∈ D^+_M) but not on the
     pulled-back segment, so the exit point carries an M-causal escape path (D3), giving a
     past-inextendible M-curve from p missing Σ: contradiction. If γ' never
     exits it crosses t = 0 outside Σ, and the same segment in M continued
     past S again contradicts p ∈ D^+_M(Σ). The reverse inclusion is identical with M and
     M' exchanged, using (D2).]
(D5) N := int D_M(Σ) is causally convex in M, globally hyperbolic,
     connected, and contains x, b.
     (a) D(Σ) is causally convex for closed acausal Σ: let p, q ∈ D(Σ), r on
     a causal curve p → q, and suppose an inextendible causal curve λ through
     r misses Σ. If p ∈ D^-, q ∈ D^+: the future-inextendible curve (p→r)·λ^+
     meets Σ, necessarily on p→r; dually Σ meets r→q; acausality forces both
     meeting points to equal r, so r ∈ Σ. If p, q ∈ D^+: p ∈ J^+(Σ), so
     r ∈ J^-(q) ∩ J^+(Σ) ⊆ D^+(Σ). Similarly for D^-, and p ∈ D^+, q ∈ D^-
     forces p = q ∈ Σ by acausality.
     (b) For p, q ∈ int D choose p⁻ ≪ p and q⁺ ≫ q in int D (p ∈ cl I^-(p)).
     Then J(p,q) ⊆ I^+(p⁻) ∩ I^-(q⁺) (MS 2.31(i)), an open set (MS 2.16)
     contained in J(p⁻, q⁺) ⊆ D(Σ) by (a); so J(p,q) ⊂ int D, i.e. N is
     causally convex and J_N(p,q) = J_M(p,q) is compact.
     (c) N is causal (as M is) with compact causal diamonds, hence globally
     hyperbolic (MS §3.11 characterization [CHECK exact item]).
     (d) Connected, and x, b ∈ N: work in M' via (D4). D_{η_λ}(Σ') ⊆ D_{g'}(Σ')
     contains a neighbourhood of every point of int Σ', so int Σ' ⊂ N'. For
     p ∈ N' ∩ D^+ with t(p) > 0, D_{g'} ⊆ D_{η_μ} puts its spatial projection
     in int B0, so the vertical segment down to z ∈ int Σ' is g'-timelike;
     each point r on it lies in I^+(z⁻) ∩ I^-(p⁺) ⊂ N' for z⁻ ≪ z, p⁺ ≫ p in N'.
     So every point of N' is joined inside N' to the connected set int Σ'.
     Dually for D^-.

**Choice of constants (one ordering for the whole proof).** Fix
1/2 < μ < 1 < λ and ε from Lemma C. Lemma A and Lemma B give S, c (length L,
defined on [−1, L+1]), the chart radius r0 and constant K. Choose
r ≤ min{r0/3, 1/2} with 6Kr ≤ ε (so Lemma C applies on T_{3r}) and 8λr < L
(w, v spacelike). The escape paths of (D3) start in T_{2r} and move laterally
by at most μr < r, so stay in T_{3r}; μ > 1/2 gives displacement μr > r/2 and
η_μ-domain height r/(2μ) < r. The detour of Lemma F lies in R^4 outside T_{3r};
its slab Σ'' is taken thinner than its distance to T_{3r}.

Hence N is an object of GH and the inclusion N ↪ M and ψ|_N: N → M' are
morphisms (ψ(N) = int D_{M'}(Σ') is causally convex in M' by (D5) applied in
M'). By (LC): x B_M b ⇔ x B_N b ⇔ ψx B_{M'} ψb.

**Lemma F (flat detour; construction from the independent review).** In M'
let w = (−4r, 0, 0, 0), v = (4r, L, 0, 0) (ψx = 0, ψb = (0, L, 0, 0)). Then
w ≪' ψx and ψb ≪' v (vertical segments are η_μ-timelike); w, v are
η_λ-spacelike (8λr < L), hence spacelike-separated in M'. The curve
t(s) = −4r + (8r/L)s, y(s) = (10r sin(πs/L), 0), 0 ≤ s ≤ L, lies in the
hyperplane H = {t = −4r + (8r/L)s}, which is spacelike and Cauchy for both η
and g' (slope 8r/L < 1/λ). Where |t| ≤ 3r we have s/L ∈ [1/8, 7/8], so
|y| ≥ 10r sin(π/8) > 3r; elsewhere |t| > 3r. So the curve lies at positive
distance from the modification region. A thin compact slab Σ'' ⊂ H around it
is acausal in M' and in Minkowski, and the (D3)–(D4) argument (with the roles
of M, M' played by M' and Minkowski, agreeing near Σ'') shows that the
identity carries D_{M'}(Σ'') onto D_{Mink}(Σ''). So N'' := int D_{M'}(Σ'') ∋ w, v
has morphisms into M' and Minkowski, and w B_{M'} v ⇔ w B_Mink v. For (b) use
the time-reversed detour.

**Proof of (a).** Suppose B_Mink ≠ U, so B_Mink relates no spacelike pair
(Theorem 1), and suppose x B_M b. If x is spacelike to b: transfer to M',
then w B' ψx (CB), ψx B' ψb, ψb B' v (CB) give w B' v (T), so w B_Mink v with
w, v spacelike: contradiction. If x ∈ J^+(b) \ {b}: Lemma R gives a spacelike
pair in B_M, reduced to the previous case. Hence B_M ⊆ J^-_M. ∎

**Lemma E (spacelike chains).** In connected GH M (dim ≥ 2), any two points
are joined by a finite chain of consecutively spacelike-separated points.
Proof: let A_q = M \ (J^+(q) ∪ J^-(q)); A := {(a,q) : a ∈ A_q} is open in M×M
(J^± closed relation in GH — causal simplicity + MS 3.68 [CHECK that the
relation J^+ ⊂ M×M, not just each J^+(p), is closed in GH]). A_q ≠ ∅ (other
points of a Cauchy surface through q). Let S(p) = points reachable from p.
S(p) is open: choose z spacelike to q in a causally convex
normal neighbourhood; since J^±(z) are closed, a neighbourhood V of q is
spacelike to z, and every q' ∈ V is joined to q by q, z, q'. Its complement is open: if q ∉ S(p), pick c ∈ A_q; by openness of A there
is a neighbourhood W of q with c ∈ A_{q''} for all q'' ∈ W; if some q'' ∈ W
were in S(p) then c ∈ S(p) and so q ∈ S(p). Connectedness gives S(p) = M. ∎

**Proof of (b).** Suppose B_Mink = U. For spacelike x, b in M, transfer to
M' and take x' = (4r, 0, 0, 0), b' = (−4r, L, 0, 0): ψx ≪' x', b' ≪' ψb,
x', b' spacelike; a flat detour slab as in Lemma F joins them, on which B is
universal; so ψx B' x' B' b' B' ψb, and x B_M b. By Lemma E and (T) every pair
is related. ∎

## 4. What does the work

4.1 (LC) is not a uniqueness assumption: it allows rules that depend on
any local geometric data (Theorem 4 uses Weyl curvature).

4.2 (T) and (CB) are Stein / Clifton–Hogarth's premises, now required in
every spacetime, including the glued M'.

4.3 Theorem 2 needs GH to be closed under the gluing construction (flat
outside a compact set), and (LC) for the two embeddings N → M, N → M'.

4.4 Curvature-defined alternatives. A pointwise rule such as
"x B b iff R(x) ≥ R(b)" is local, so (LC) alone does not exclude it. It is
excluded only because (CB) and (T) must hold in every spacetime: Theorem 2
shows that any theory satisfying (LC), (T), (CB) and B_Mink ≠ U relates no
spacelike pair in any spacetime. So in particular, in Codex's dust model
(a = t^{2/3}, R = 4/(3t^2)), the R-ordering is not the restriction of any
such theory, although within that one spacetime it is isometry invariant,
transitive and contains I^-.

## 4.5 Scope: off-shell gluing

The category GH contains arbitrary globally hyperbolic metrics. The glued M'
need not solve Einstein's equations with any physically reasonable matter
(energy conditions may fail in the interpolation region). Theorem 2 therefore
assumes that a becoming rule is defined for every globally hyperbolic
geometry, not only for solutions of a fixed Einstein–matter theory. That is
the natural reading of a causal/kinematic notion of becoming (Clifton–Hogarth
work in Minkowski with no dynamics), but it is a premise, and the paper must
state it. An on-shell version (gluing within solutions satisfying, e.g., the
dominant energy condition) would need genuine gluing theorems for the Einstein
equations and is a natural hard extension.

## 5. Examples to include

5.1 Weyl-gated null boundary (Theorem 4).
5.2 Cosmological/CMC time (Proposition 6): natural, non-local.
5.3 Codex's dust test (§4.4).
5.4 Gödel-type spacetimes: outside GH; likely known in spirit (Aames 2022
cites Savitt 2017 on diamonds filling the spacetime). Remark only.

## 6. Open / to check

- Theorem 1: CHECKED. Clifton–Hogarth's proof (pp. 365–367) uses only
  b-preserving rotations, boosts and translations (proper orthochronous).
- Reduction lemmas: replaced. Lemma R (Clifton–Hogarth's case-(2) move in a
  convex causally convex neighbourhood) and Lemma E (spacelike chains; a
  point spacelike to both x and b need NOT exist in long-lived closed
  universes, so the earlier argument was wrong and is removed).
- Lemma B: corrected to Gaussian normal coordinates (review).
- Lemma C: explicit bound adopted from the review.
- Lemma F: replaced by the review's explicit detour in a common Cauchy
  hyperplane.
- (D5): int D(Σ) globally hyperbolic and causally convex — proof sketched;
  find a primary locator (Hawking–Ellis / O'Neill) or write it out.
- Integrate all quantifiers into one consistently ordered choice of
  μ, λ, ε, r, Y.
- On-shell version (§4.5).
- Lemma E: confirm closedness of the relation J^+ ⊂ M×M in GH (not only of
  each J^+(p)); MS Prop. 3.68 / standard.
- Lemma R: rewritten with the world-function first variation (covers null
  and timelike u). Check MS Thm 2.14 locator.
- (D5): written out; check the MS §3.11 locator for "causal + compact
  diamonds ⇒ GH".
- Whether disconnected objects or non-compact-Cauchy objects are needed
  (we use only R^4 and int D(Σ), both connected).
- Worldline-dependent extension (Clifton–Hogarth Theorem 2) — not attempted.
- Priority, read 24 Oct (full text): Stein 1970 (Phil. Sci. 37, 589–601)
  defends Gödel's computations against Chandrasekhar–Wright and poses
  technical questions about the eligibility of the model; no becoming
  relation, no definability result. Savitt 2005 (Monist 88, 413–422) argues
  passage survives CTCs via successive extended presents along a timelike
  curve; conceptual, no Stein-type theorem. Neither anticipates Theorem 2 or
  Proposition 7. Viglione 2026 (Erkenntnis, 10.1007/s10670-026-01075-2; open-access
  published version read in full) argues an informal Causal Connection
  Condition ("the fact that two events stand in a certain temporal relation
  ... can be considered absolute only if it obtains independently of the
  occurrence of any causally disconnected event") against metaphysical cosmic
  simultaneity; no mention of Stein's theorem or Clifton–Hogarth, no formal
  locality framework. Philosophical motivation for (LC), not prior art.
  Priority sweep (citations of Clifton–Hogarth and Stein 1991, plus the
  papers named) found no prior extension of Stein to curved spacetime. Gödel 1949b page range per Savitt 2005: Schilpp (ed.),
  pp. 557–562.
