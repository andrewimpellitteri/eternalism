# Germ-precedence cohomology is a relabelling of the no-local-clock theorem

10 November 2026. Longshot lane `longshot-cohomology-of-time`, GLM worker. Submission for
independent review, not a truth claim; checked only by the session that wrote it. Source
records: [sources.jsonl](sources.jsonl). The idea under test: Fewster and Verch
(lc-coh-fv2012, §1; technical basis §2.3) conjecture that the Cauchy-wedge study of the
spacetime category might support a cohomology theory, and Sanders realized this for
Dirac-field freedoms. Can cohomology of the germ-precedence preorder of the local-clock
note (`research/stein-gr/local-clock/RESULT.md`) say more than its Theorem 4?

**Verdict: relabelling.** The nerve of the germ-precedence category is degenerate exactly
when the class has no local clock, and its H¹ has no content here for a structural reason.
No new consequence or computable obstruction beyond the note was found. Per the brief's
question (4), the lane stops here. Two minor by-products are recorded in §4.

## 1. Exact question and proposed statement

Let 𝒞 be a class of spacetimes as in the note (restriction-closed, closed under finite
disjoint unions, contains 𝕄), with germ-precedence g ⊴ g′ iff some member has events
w ≪ x with germs g, g′.

**Candidate (simplest precise form).** Present P(𝒞) := (germs, ⊴) as a thin category
(reflexive–transitive closure of ⊴ as arrows; thinness makes "comparable by a chain"
the same as existence of an arrow). A local clock is then a functor P(𝒞) → L into an
ordered set L (the note's monotonicity), and "no local clock" is: every such functor is
constant.

* (C1) No-local-clock ⟺ the flat germ is initial in P(𝒞) (weakly initial = initial
  because the category is thin). Given an initial object, the nerve B P(𝒞) is
  contractible (a category with an initial object is equivalent to the terminal
  category), so H⁰ collapses to a point and Hⁿ(B P(𝒞); A) = 0 for all n ≥ 1 and all
  coefficients. This is precisely the note's Theorem 4, criterion 3, in nerve language.
* (C2) If the flat germ is not initial, indicator functors on its down- and up-sets
  (the note's proof of 2 ⇒ 3) are nonconstant clocks; and no Sanders-style H¹
  classification of "clock freedoms" can exist: Sanders' H¹(SSpac, ℤ₂) classifies
  sign-twists coming from the nontrivial automorphism group ℤ₂ of the fiber functor,
  while clock targets are rigid posets (automorphism-free), so there is nothing for an
  H¹ to classify. Connectedness/π₀ and the Hom-rigidity of (C1) exhaust the invariant.

## 2. Three nearest predecessors

| Predecessor | Assumptions | Result | Relation to (C1)–(C2) |
|---|---|---|---|
| Sanders, *The locally covariant Dirac field*, Rev. Math. Phys. 22 (2010) 381–430, §3.4 Thm 3.15 (lc-coh-sanders2010, full-text) | Category SSpac of GH spin spacetimes; Dirac structures with adjoint/charge-conjugation/γ; freedoms = sign choices on intertwiners (ℤ₂ automorphisms) | Number of inequivalent Dirac structures (4-dim fibers) = number of elements of H¹(SSpac, ℤ₂) ("first Stiefel–Whitney classes of the category"); obstructions vanish on the observable algebra | Occupies the method (nerve cohomology of a spacetime category classifying freedoms) but for non-rigid targets; shows why the mechanism cannot transfer to clocks (C2) |
| Fewster–Verch, Ann. Henri Poincaré 13 (2012) 1613–1674, §1 conjecture sentence, §2.3 Props 2.4/2.6, footnote 5 (lc-coh-fv2012, full-text) | Loc with causally convex isometric embeddings; chains of Cauchy wedges | Loc splits into Cauchy-wedge-connected components labelled by oriented-diffeomorphism classes of Cauchy surfaces; authors conjecture "a cohomology theory with many ramifications"; footnote 5 already builds nonconstant monotone ℕ-valued functions χ on the spacetime category | Source of the conjecture; also prior art for monotone functions on Loc (object level), one level above the note's germ-level clocks |
| Becker–Schenkel–Szabo, *Differential cohomology and locally covariant QFT*, DOI 10.1142/S0129055X17500039 (2017) (lc-coh-bss2017, full-text of abstract–§3) | Loc^m (finite-type GH manifolds); an abstract differential cohomology theory on Man restricted to Loc^m | Generalized Maxwell maps as natural transformations, solution subfunctors, presymplectic Pontryagin duals, CCR quantization satisfying causality and time-slice but violating locality via topological subfunctors | Later work cohomology *on* Loc: gauge/gerbe freedoms only; nothing on germs, precedence, or clocks |

Also noted at discovery depth: Ruzzi, Rev. Math. Phys. 17 (2005) 1021–1070 (poset
homotopy and net cohomology inside one spacetime, for superselection sectors), and
Roberts–Ruzzi–Vasselli's poset net-bundle line (lc-coh-rrv2012); Sanders defines the
category-cohomology machinery citing Roberts–Ruzzi (TAC 16 (2006) 855–895) and Segal
(1968). No source found that applies cohomology to germs, becoming, or local clocks.

## 3. What changes relative to the predecessors, and why it matters

Nothing physical. The cohomology conjecture of lc-coh-fv2012 has been realized in the
literature for *field and bundle* freedoms (spin signs, ℤ/ℤ² gauge twists, gerbes),
whose coefficient objects have nontrivial automorphisms. The germ-precedence setting has
rigid targets, so the entire strength of the Sanders mechanism (classifying twisted
structures by H¹) is unavailable; what remains is π₀/H⁰-rigidity, which is exactly the
note's Theorem 4. The proposal is therefore a dictionary, not a new invariant.

## 4. Smallest reproducible example and independent check

**Toy class A: all GH spacetimes (kinematic).**
*Lemma T (transplant, constructed here).* For every germ g of class A, flat ⊴ g and
g ⊴ flat. Construction: realize g at p in a GH spacetime; take Gaussian-normal
coordinates on a small ball around a spacelike disk through p, so the germ is represented
as −dt² + h_t(y); transplant that split-form metric into the cylinder ℝ × ℝ³ with H_s
equal to it near (−1, 0), flat near (0, 0), smoothly interpolated in between; the curve
s ↦ (s, 0) is timelike since g(∂_s, ∂_s) = −1, giving w ≪ x; reflect in s for the other
direction. What is used: (F1) local split-form representation of a Lorentzian metric near
a spacelike disk (standard Gaussian normal coordinates, cf. O'Neill / FV's normal-form
discussion), and (F2) ℝ × Σ with −dt² + complete h is GH with Cauchy slices (FV Prop 2.1
proof, citing their ref [34, Prop. 5.2]). F1, F2 are flagged for verification at source;
the interpolation is elementary.
*Computation A.* Hence the flat germ is initial in P(A); by (C1) B P(A) is contractible:
H⁰ a point, all higher cohomology zero, and Hom(P(A), L) = constants for every ordered
set L — the class has no local clock, matching the note's Theorem 4.

**Toy class B: Scal never increases along future causal curves (the note's §4 class).**
Unconditional: (i) g ⊴ g′ ⇒ Scal(g) ≥ Scal(g′) at the base events, so κ = −Scal is a
nontrivial local clock P(B) → ℝ (realized strictly in expanding dust FLRW, whose Scal is
positive and strictly decreasing along cosmic time — textbook trace identity R = 8πGρ for
dust, ρ ∝ a^{−3}; flagged for source verification). (ii) Ball certificates, computable
from the germ alone: if g ⊴ flat then every point q of a germ ball of g that can see the
flat region causally has Scal(q) ≥ 0, so inf Scal ≥ 0 over such balls; symmetrically
flat ⊴ g forces sup Scal ≤ 0. These are per-germ certificates of biconnectivity failure,
which Theorem 4 asserts only abstractly. (iii) Grading: reach-flat ⊆ {Scal ≥ 0 germs},
from-flat ⊆ {Scal ≤ 0 germs}; germs of one sign in some ball chain to or from flat by the
Lemma-T construction constrained to a monotone Scal profile (one-sign case constructed;
mixed-sign case open), so π₀(P(B)) = 1 plausibly while flat is neither initial nor
terminal — the nerve is not a cone and carries no usable H¹.

**Independent check route.** Re-read lc-coh-fv2012 §1–2.3 and lc-coh-sanders2010 §3.4
(Thm 3.15) and confirm the reduction "clocks = functors into rigid posets ⇒ no H¹";
verify (F1), (F2) and the dust-FLRW identity at source; optionally formalize "thin
category with initial object ⇒ contractible nerve" in Lean on a discretized germ poset.
No large computation is involved.

## 5. What would show the claim wrong, trivial, already known, or physically irrelevant

* **Wrong:** Lemma T fails (the split-form transplant does not give a GH member) — then
  computation A becomes conditional; the relabelling verdict survives regardless.
* **Trivial:** it already is, in part: contractibility of a coned nerve is a degenerate
  case, stated here only to close the lane.
* **Already known:** any literature giving a cohomology classification of order- or
  clock-structures on spacetime categories. Searches run (2026-11-10, scholar/openalex +
  arXiv): "cohomology category Loc locally covariant quantum field theory"; "cohomology
  category of globally hyperbolic spacetimes germs preorder clock"; "locally covariant
  Dirac field Sanders"; "homotopy of posets net cohomology globally hyperbolic Ruzzi".
  Nothing occupies the germ-clock object. The note's own Theorem 4 already contains
  criterion 3, which is why the verdict is relabelling rather than discovery.
* **Physically irrelevant:** yes on-shell. Both transplant lemmas use kinematic freedom
  (no field equations); the note's open problem for dominant-energy classes remains open,
  and the ball certificates say nothing about matter-restricted classes (a star has
  spacelike Scal gradients, as the note already observes).
* **Weakness of the increment:** the ball certificates concern kinematically constructible
  members; whether curvature-monotonicity conditions of this shape are already standard in
  the singularity-theorem/generic-condition literature was not fully searched (flagged).

## 6. Kinds of novelty kept apart

* **Mathematical:** minor — Lemma T and its one-sign class-B variant; ball-extremal
  certificates. New only relative to the repo's own note; uncited-literature check limited
  to the searches above.
* **Formalization:** modest — the thin-category/initial-object dictionary for Theorem 4;
  no Lean artifact produced in this lane.
* **Physical:** none. No new consequence for any realistic class; the curvature clock −Scal
  was already in the note and, as order-valued functors from scalar-curvature thresholds,
  already in Fewster–Verch's programme (lc-coh-fv2012, §4.3 per the note's reading).
* **Philosophical:** none beyond the source note. No ontological bridge is touched.

**Conclusion.** The idea is not in the literature in this form, but it adds nothing: the
cohomology proposal restates the no-local-clock criterion as degenerate nerve cohomology
and is structurally barred from a Sanders-style H¹. Per the brief's question (4): stop.
