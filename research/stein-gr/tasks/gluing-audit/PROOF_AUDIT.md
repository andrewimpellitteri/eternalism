# PROOF_AUDIT: domain transfer and the flat detour (Lemmas B, C, D, F)

Task: `stein-gluing-audit`. Auditor: head session (`claude-head`), direct user
request. Date: 2025-10-25. Source audited: `research/stein-gr/main.tex` at
commit `498de2f3` ("State the no-shared-present corollary and the resulting
trilemma"), the current checkout head for this file. Read against:
TASK_PLAN.md, SECOND_PASS_REVIEW.md (treated as proposals, not axioms), and
the imported causal-theory sources at the locators listed at the end.

Scope: Lemmas B, C, D, F, the constants paragraph, the two transfer
embeddings, and their assembly into Theorem 7(a). Not in scope: Theorem 8–9,
Proposition 10, the causal-set and Gödel propositions (other lanes), global
notation policy (core-repairs lane).

## Verdict summary

**No blocking finding.** All transfer and embedding hypotheses are verified
under the stated hypotheses of Remark 3 (off-shell, kinematic category).
Three cosmetic proof-writing items and two precision upgrades are listed;
none affects a mathematical conclusion. Both SECOND_PASS_REVIEW repairs are
verified as present and correct in the audited source. No counterexample to
any lemma was found; the two candidate counterexamples I constructed (boundary
tie case; boosted end-cap escape) are resolved below, one with a one-sentence
manuscript repair.

## 1. Lemma B (adapted coordinates) — VERIFIED

The construction is the composition of Gaussian normal coordinates of S with
Riemannian normal coordinates of the intrinsic metric h along the compact arc
c. Checks:

- Injectivity/diffeomorphism on T̄_{ρ₀}: the map (t, s, y) ↦ exp_{σ(s,y)}(t n)
  is smooth on the compact strip for ρ₀ ≤ δ₀ (δ₀ from the acausal discs);
  restrict ρ₀ so that it is a diffeomorphism — standard tubular-neighborhood
  argument for a spacelike hypersurface, with the strip compact.
- Φ({0} × ·) = σ(·) ∈ S ✓; Φ(t, ·) ∈ I⁺(S) for t > 0 and ∈ I⁻(S) for t < 0 ✓
  (future unit normal, geodesic departure).
- Φ*g = −dt² + h_t(s,y) ✓ (Gauss lemma for the normal coordinate t).
- The estimate ‖Φ*g − η‖ ≤ K(|t| + |y|) on T̄_{ρ₀}: both Φ*g and η are smooth
  and agree at (0,0,0,0) to zeroth order (orthonormal frame on c) — smoothness
  on the compact strip gives a Lipschitz-type bound in the coordinate
  separation from the arc; the stated linear-in-(|t|,|y|) form is what is used
  later, and only the existence of K is needed. VERIFIED as sufficient.

## 2. Lemma C (cone control) — VERIFIED, one cosmetic note

For k with ‖k − η₁‖ ≤ ε (operator norm) and v = (1, u):

- k(v,v) ≤ η₁(v,v) + ε‖v‖² = −1 + |u|² + ε(1 + |u|²) < 0 whenever
  |u|² < (1−ε)/(1+ε); the hypothesis ε < (1−μ²)/(1+μ²) gives exactly
  μ² < (1−ε)/(1+ε). ✓
- k(v,v) ≥ (1−ε)|u|² − (1+ε) > 0 whenever |u|² > (1+ε)/(1−ε); the hypothesis
  ε < (λ²−1)/(λ²+1) gives λ² > (1+ε)/(1−ε). ✓
- Lorentzian signature: spatial block ≥ (1−ε)I > 0 and k(∂_t,∂_t) ≤ −(1−ε) < 0
  give (−,+,+,+) by the Schur-type argument. ✓
- Convex-combination stability: for χk + (1−χ)η₁ both summands satisfy the
  same strict bounds, hence so does the combination. ✓

Cosmetic note C1: the statement introduces η_c = −c²dt² + ds² + |dy|² with
general c, but the proof and every use are for c = 1 (η₁). Drop η_c or state
the lemma for η₁ only.

## 3. Constants paragraph — VERIFIED, consistent, no circularity

Order of choices is load-bearing and correct: (μ, λ, ε) fixed under Lemma C's
constraint; then ρ₀, K from Lemma B (they depend only on g, S, c); then r with
3r < ρ₀, 6Kr ≤ ε, 8λr < L. Checks:

- On T_{3r}: |t| < 3r and |y| < 3r, so ‖Φ*g − η‖ ≤ K(|t|+|y|) < 6Kr ≤ ε ✓ —
  Lemma C then applies to Φ*g on T_{3r} and to g' everywhere (g' − η is a
  convex combination of two matrices bounded by ε). ✓
- T̄_{2r} ⊂ T_{3r} ✓. supp χ ⊂ T_{3r} with χ = 1 on T̄_{2r} ✓.
- M′ globally hyperbolic: causal vectors satisfy |d(s,y)/dt| ≤ λ (Lemma C,
  second bound), so t is strictly monotone along inextendible causal curves;
  a finite limit of t would force convergent spatial coordinates (|Δs|,|Δy| ≤
  λ|Δt|) and the curve would extend in the smooth complete-at-infinity metric
  on ℝ⁴ — so every level {t = c} is met exactly once and is Cauchy
  (MS Thm 3.75). ✓
- 8λr < L is used twice: the detour hyperplane slope |f'| = 8r/L < 1/λ in
  Lemma F, and the CB chains in the proof of Theorem 7(a). ✓

Precision upgrade D0 (cosmetic): state explicitly that χ ≡ 1 on an open
neighborhood of T̄_{2r} (standard bump property). Lemma D(ii) uses the
agreement g' = Φ*g "extended to a neighbourhood of T̄_{2r}", which is exactly
this.

## 4. Lemma D — VERIFIED (all three parts), two precision upgrades

### Escape paths

- Side points ((s_q,y_q) ∉ B₀): vertical descent to t = 0. Pure ∂_t is timelike
  (|u| = 0 ≤ μ); the path stays in T_{2r} ⊂ T_{3r}; endpoint has (s,y) ∉ B₀,
  hence on {t=0} \ Σ′, i.e. S \ Σ in M (Φ injective). ✓
- Lid points (t = 2r, |y_q| ≤ r/2): velocity (−1, (μ/2)ŷ). Coordinate speed
  μ/2 < μ ⇒ timelike for Φ*g and g′ ✓. Over coordinate time 2r the transverse
  displacement is μr, so the endpoint satisfies |y| ∈ [μr, r/2 + μr] ⊂ (r/2,
  3r), using μ > 1/2 (from ε < (1−μ²)/(1+μ²)) and μ < 5/2 (μ < 1). Stays in
  T_{3r} ✓. ✓
- Negative-time boundary: time-reversed paths ✓.

### (i) Both D-inclusions — VERIFIED

For p ∈ D⁺_M(Σ) \ Φ(T_{2r}): σ₁ = first meeting of Σ, q = last boundary
crossing before σ₁. Two checks the brief singles out:

- Stopping-event ties: the crossing set of the compact segment with the closed
  boundary is compact, so "last" is well-defined. The extreme case q = p (p on
  the boundary) is covered: σ₁ has t = 0 and t increases strictly along the
  future-directed segment inside the tube, so t(q) > 0. (A boundary point with
  t = 0 lies on S \ Σ and acausality already excludes it from D⁺(Σ).)
- After q the segment lies in the open tube, where the future direction has
  strictly increasing t; past-inextendibly continuing through the escape path
  gives a past-inextendible causal curve from p missing Σ — contradiction. ✓

The M′ copy of the argument uses that {t=0} is Cauchy in M′ ✓.

### (ii) ψ(D_M(Σ)) = D_{M′}(Σ′) — VERIFIED, repair confirmed

The two stopping events (first t = 0 crossing τ₀; first shell exit τ_exit),
with the case split τ₀ ≤ τ_exit (equality included) versus τ_exit < τ₀, is
exactly the SECOND_PASS_REVIEW §2 repair, and the audited source contains it
(lines "If τ₀ ≤ τ_exit (equality included) … If τ_exit < τ₀, then t > 0 at the
exit point"). The pullback legitimacy uses the metric agreement on a
neighborhood of T̄_{2r} (upgrade D0). The reverse inclusion correctly avoids a
global time coordinate on M (exit-or-reach-S dichotomy from acausality of S).
Both repairs verified as proposals and accepted.

### (iii) Causal convexity, global hyperbolicity, connectedness — VERIFIED

- The inclusion J⁻(q) ∩ J⁺(Σ) ⊆ D⁺(Σ) for q ∈ D⁺(Σ), and the mixed-case
  acausality argument, are standard and correctly cited. ✓
- Openness now uses STRICT diamonds: J(p,q) ⊆ I⁺ₛ(p⁻) ∩ I⁻ₛ(q⁺) ⊆ D(Σ) with
  MS Props. 2.16/2.31 — this is the SECOND_PASS_REVIEW §1 repair, and the
  audited source carries the strict subscript. Verified against the
  Minguzzi–Sánchez convention (Int J^± = I_strict^±): with the manuscript's
  reflexive I the diamond would not be open, so the repair is necessary and
  correctly applied. ✓
- Connectedness: interior points join to rel-int Σ′ by vertical segments in
  I⁻(q⁺) ∩ I⁺(z⁻) ⊆ N′ (M′) and by transfer in M; this is the bicollar
  argument and is sound. Candidate counterexample (two wings of int D⁺ ∪ int
  D⁻ disconnected at Σ) fails because points of rel-int Σ are interior to
  D(Σ): every inextendible causal curve through them meets Σ at themselves.
  ✓
- The M′ interior claim via D_{η_λ}(Σ′) ⊆ D_{g′}(Σ′) ⊆ D_{η_μ}(Σ′)
  (narrower cones give larger domains of dependence) is a correct and elegant
  monotonicity. ✓

## 5. Transfer morphisms — VERIFIED

- N = int D_M(Σ) is open, causally convex, globally hyperbolic, connected, and
  contains x and b: x = c(0) = Φ(0,0,0,0) and b = c(L) = Φ(0,L,0,0) are
  relative-interior points of Σ′ (B₀ has positive margin around (0,0) and
  (L,0) since r > 0), and the proof of (iii) places relative-interior points
  of Σ′ in int D_{M′}(Σ′); transfer by (ii) gives x, b ∈ N. ✓
- N ↪ M and ψ|_N: N → ψ(N) = int D_{M′}(Σ′) are morphisms of GH: isometric
  (ψ is an isometry on Φ(T_{2r}) ⊇ N), images open and causally convex,
  orientation- and time-orientation preserving (Lemma B). ✓
- The transfer chain x B_M b ⟺ x B_N b ⟺ ψ(x) B_{M′} ψ(b) is (LC) applied to
  both morphisms. ✓

## 6. Lemma F (flat detour) — VERIFIED, one minor repair needed

- H = {t = f(s)}, f affine with |f′| < 1/λ: along g′-causal curves,
  d/dτ(t − f(s)) ≥ ṫ(1 − λ|f′|) > 0, so H is spacelike and Cauchy for g′ and
  for η (t − f(s) → ±∞). ✓
- Acausality of Σ″ ⊂ H ✓ (H spacelike; δ-neighborhood of an embedded arc in H
  is a compact 3-dimensional slab, acausal since H is). P, Q in its relative
  interior by construction. ✓
- Domains lie in the flat region: δ small against the distance from κ to
  T̄_{3r} keeps Σ″ and its Cδ-neighborhood where g′ = η. ✓
- Coincidence of domains with Minkowski: in boosted coordinates both metrics
  are exactly η on a neighborhood of Σ″ — the pullback B*(g′) = B*(η) = η on
  B⁻¹(U) for the flat neighborhood U ∋ Σ″, since g′ = η on U. The domain
  argument of Lemma D then runs verbatim in the boosted frame. ✓
- D_{M′}(Σ″) lies in the flat region (by the D-inclusion for the Cδ-tube) and
  equals int D_Mink(Σ″); inclusions into M′ and Mink are morphisms; (LC)
  gives P B_{M′} Q ⟺ P B_Mink Q. ✓

**Minor repair F1 (should be fixed at integration, not blocking):** the
escape along "the gradient of the distance to the arc" is spacelike at the
end caps of the 2δ-tube (there the distance gradient points along the arc
tangent). The uniform repair is the one used in Lemma D: past-directed
vertical descent (in the boosted frame) from every tube-boundary point lands
on the Cauchy plane outside Σ″ and is timelike; no distance-gradient is
needed. Also state C ≥ 2 (the Cδ-neighborhood on which both metrics are η
must contain the 2δ-tube). With this sentence replaced, Lemma F is complete.

## 7. Assembly of Theorem 7(a) — VERIFIED (given the off-shell premise)

The constellation w, v and the tilted arc satisfy the Lemma F hypotheses
(slope 8r/L < 1/λ from 8λr < L; positive distance from T̄_{3r} by
construction), CB + transitivity attach w to ψ(x) and ψ(b) to v, Lemma F
lifts w B_Mink v (Minkowski being the B = I⁻ or B ⊆ J⁻ case where the
classification of Theorem 6 leaves no spacelike pairs), and the spacelike-
chain lemma propagates the contradiction to every pair. The proof of (b)
(universality propagates) is one line by (LC). Both localization directions
are complete; detour acausality verified (§6). The whole argument rests on
the off-shell premise (Remark 3): g′ is a kinematic metric, not an
Einstein solution — correctly declared, and probed by the energy-rigidity
lane, not this one.

## 8. Counterexample attempts (brief requirement)

1. *Boundary tie q = p in Lemma D(i)* — resolved: t(q) > 0 by strict
   monotonicity inside the tube; the t(q) = 0 boundary case is excluded by
   acausality of S. No counterexample.
2. *Boosted end-cap escape in Lemma F* — the stated escape direction fails at
   end caps (spacelike gradient); repaired by uniform vertical descent (§6,
   F1). No counterexample to the conclusion.
3. *Disconnected interior of D(Σ)* — fails: rel-interior Σ-points are interior
   points of D(Σ), and the vertical join connects the two halves. No
   counterexample.
4. *Chauvinism of the chosen r* — r enters only through the constants; every
   inequality used is preserved for all smaller r > 0, and the constructed
   N shrinks with r while still containing x, b (relative-interior margin).
   No counterexample.

## 9. Imported causal facts and primary locators

All used with the strict/reflexive distinction as repaired:

- MS (Minguzzi–Sánchez, arXiv:gr-qc/0609119v3): Prop. 2.16 (I⁺ open),
  Prop. 2.17 (Int J^± = I_strict^±; closures), Prop. 2.31 (chronology–horismos
  composition), Thm. 2.30 (causal non-null-geodesic ⇒ timelike deformation),
  Rem. 2.12 (locally causally convex neighborhoods), Prop. 3.71 / Def. 3.70
  (causal simplicity; GH diamond definition), Thm. 3.75 (level surfaces of a
  Cauchy temporal function ⇒ GH). Read depth at these locators: this audit and
  SECOND_PASS_REVIEW both; not a new full-paper audit.
- Bernal–Sánchez [BS2006], Thm 1.1 + Rem 4.14 (smooth spacelike Cauchy
  hypersurface through/above an acausal submanifold): cited for S ⊇ D_x ∪ D_b.
  NOT independently verified in this audit — flagged as the one imported
  citation whose exact statement (compact acausal submanifold *with boundary*)
  should be checked against the Bernal–Sánchez text at integration.
- Synge world function first-variation (Lemma R, outside scope): verified
  independently by SECOND_PASS_REVIEW §3; no further finding.

## 10. Findings ledger

| ID | Severity | Location | Item |
|---|---|---|---|
| G1 | Cosmetic | Lemma C | η_c generality vestigial; state for η₁ |
| D0 | Precision | Constants | State χ ≡ 1 on a neighborhood of T̄_{2r} |
| F1 | Minor, fix at integration | Lemma F | End-cap escape cannot use the distance gradient; use uniform vertical descent; state C ≥ 2 |
| — | None blocking | — | Both SECOND_PASS repairs verified as applied and correct |

## 11. Remaining assumptions and hand-offs

- Off-shell premise (Remark 3) is load-bearing for Lemma B's auxiliary
  spacetime; the on-shell question is `stein-energy-rigidity-audit`'s.
- The one imported citation to verify at integration: Bernal–Sánchez Thm 1.1 /
  Rem 4.14 as stated for a compact acausal submanifold with boundary.
- No duplication of `stein-core-repairs`: this audit proposes no global
  notation patch; F1 is local to Lemma F's proof.
