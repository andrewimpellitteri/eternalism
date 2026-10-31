# Adversarial review of SCREENING.md (causal-potential screening and rigidity)

31 October 2026. Task `screening-review`, analytic red-team of
`research/bowtie-horizons/SCREENING.md` (read-only), lines cited as L<nn>.
No installs, no child agents, no board or manuscript edits. No novelty claim.

**Method.** Every proof step was re-derived line by line under the stated
setting (smooth, connected, time-oriented, globally hyperbolic (M,g); ≤ causal
precedence with null pairs included; D_pot, D_BT, H, W, screening as defined at
L9–L27). Counterexample searches were run in 1+1 and 2+1 Minkowski space,
conformally related FLRW slabs, and the 1+1 spatial cylinder (Minkowski/ℤ),
which is globally hyperbolic. Literature search for premise (L) used
`scholar_search` (Openalex) and Exa `web_search_exa`/`web_fetch_exa`;
`web-search-prime` was not called (quota exhausted until 2026-11-17, per brief).
A 1+1 arithmetic sanity script was run; commands are in AGENT_REPORT.md.

## Verdict summary

| Item | Verdict |
|---|---|
| Lemma 1 (identity, L28–L34) | CONFIRMED |
| Theorem 2 (⇐), L44–L46 | CONFIRMED (one small gap filled, §2.1) |
| Theorem 2 (⇒) ∂P construction, L48–L69 | CONFIRMED only as a C⁰ Cauchy surface in the Bernal–Sánchez convention; ∂P is **not acausal** in general (explicit 1+1 counterexample, §2.2). NEEDS-FIX: state the convention |
| Theorem 3(a) step 1 (causal convexity of W, L107–L112) | CONFIRMED |
| Theorem 3(a) step 2 (h(I⁻(b₁)) = I⁻(b₂), L113–L116) | CONFIRMED |
| Theorem 3(a) step 3 (J⁺(b₁) ⊆ D⁺(K₁), L118) | CONFIRMED; the citation of Theorem 2 is rescued only by the identity J⁻(J⁺) = I⁻(I⁺); one-line fix (§4.3) |
| Theorem 3(a) step 4 (endpoint cases, inner continuity, L120–L136) | CONFIRMED with three completions (§4.4) |
| Theorem 3(b) conditional logic, L138–L142 | CONFIRMED given a D-agreement premise; the marking step Ψ(b₁)=b₂ is verified in §5 |
| Premise (L′), L88–L103 | REFUTED as literally stated (definition-level counterexample, §6); no source located for any corrected form; access gate recorded |

No counterexample was found against Lemma 1, Theorem 2 (⇐), any Theorem 3(a)
step, or the conditional logic of 3(b). The load-bearing defect is premise (L′),
which the draft already flags as unverified; this review sharpens that flag
into a definitional refutation plus a precise replacement premise.

## 1. Lemma 1 — CONFIRMED

Claim (L30): D_pot(b) = J⁻(J⁺(b)) ∖ (J⁺(b) ∖ {b}).

Check. (⊆) For x ≠ b in D_pot(b): ¬(b ≺ x) with b ≠ x gives x ∉ J⁺(b); the
witness z satisfies b ≤ z, so z ∈ J⁺(b) and x ≤ z; hence x lies in the right
side. b itself lies in J⁻(J⁺(b)) because J⁺(b) ∋ b, and b ∉ J⁺(b) ∖ {b}. (⊇)
For x ≤ z, z ∈ J⁺(b), x ∉ J⁺(b) ∖ {b}, x ≠ b: x ≠ z (else x ∈ J⁺(b) ∖ {b}),
so x ≺ z; if z ≠ b then b ≺ z is the witness; if z = b, pick z′ ∈ I⁺(b)
(nonempty in any spacetime) and push up: x ≤ b ≪ z′ gives x ≺ z′, b ≺ z′. The
draft's proof (L32–L34) is complete.

Useful strengthening used below, and implicit in the draft: by push-up,
**J⁻(J⁺(b)) = I⁻(I⁺(b))** in any spacetime (x ≤ z ∈ J⁺(b) and w ∈ I⁺(z) give
x ≪ w ∈ I⁺(b)). So W := I⁻(I⁺(b)) ∖ J⁺(b) (L77) and
D_pot(b) = W ∪ (∂I⁻(I⁺(b)) ∩ D_BT(b)). This identity is what makes the
Theorem 3(a) step 3 citation work; see §4.3.

Requirements: only irreflexivity of ≺, transitivity/antisymmetry of ≤, push-up
and I⁺(b) ≠ ∅. Global hyperbolicity is not needed. No counterexample exists at
this level; quotient and conformal attempts change nothing (the statement is
order algebra).

## 2. Theorem 2 (screening characterization, L40–L69)

Screening (L23–L27): R screens b's future iff J⁺(b) ⊆ D⁺(Σ ∩ R) for every
Cauchy surface Σ (C⁰ allowed) disjoint from J⁺(b) ∖ {b}.

### 2.1 Direction (⇐), L44–L46 — CONFIRMED, one gap filled

Let D_pot(b) ⊆ R, Σ Cauchy with Σ ∩ (J⁺(b) ∖ {b}) = ∅, z ∈ J⁺(b), c a
past-inextendible causal curve from z. The draft asserts c meets Σ at some
y ≤ z. Two completions:

(i) *Existence of the meeting point for causal (not just timelike) curves.*
Under the Bernal–Sánchez convention (their definition, quoted in §2.2), a
Cauchy hypersurface is crossed exactly once by every inextendible **timelike**
curve and, as they state, "at least once by any inextendible causal curve".
Equivalently (standard in GH), t|c is strictly monotone with image all of ℝ,
where t is any Cauchy temporal function.

(ii) *The meeting point satisfies y ≤ z unless z = b.* Let y be a meeting
point. If y ∈ J⁺(z), then y ∈ J⁺(b), so y ∈ Σ ∩ J⁺(b) ⊆ {b}, i.e. y = b; then
b ∈ J⁺(z) and z ∈ J⁺(b) give z = b by antisymmetry. So for z ≠ b, y ≤ z, and
then y ∈ J⁻(J⁺(b)) ∖ {y = b case} with y ∉ J⁺(b) ∖ {b}, i.e. y ∈ D_pot(b) ⊆ R
by Lemma 1. For z = b, every meeting point y ≤ b lies in I⁻(b) ⊆ D_pot(b), or
equals b ∈ D_pot(b) ⊆ R. In both cases every past-inextendible causal curve
from z meets Σ ∩ R: z ∈ D⁺(Σ ∩ R).

### 2.2 Direction (⇒) and the ∂P construction, L48–L69 — CONFIRMED under the Bernal–Sánchez convention; the surface is not acausal in general

The construction P = I⁻(x) ∪ I⁻(Σ_c), Σ := ∂P, is correct step by step:

- P is an open past set; ∂P is achronal (the draft's argument at L52–L55 is
  valid: P is a past set, P is open, so P ∩ ∂P = ∅, and u ≪ w ∈ ∂P forces
  u ∈ P).
- Every inextendible causal curve meets ∂P: points with t < c lie in
  I⁻(Σ_c) ⊆ P and points with t > C lie outside P because
  P ⊆ I⁻(Σ_C) = {t < C}; here "t(q) < c ⟹ q ∈ I⁻(Σ_c)" uses that t is a
  Cauchy temporal function (existence: Bernal–Sánchez, gr-qc/0512095,
  Theorem 1.2), and the connectedness step at L57 is the standard separation
  argument. Since an inextendible causal curve crosses every Cauchy level, the
  t-ranges are unbounded and the argument closes.
- x ∈ ∂P (L59): x ∉ P and x ∈ cl I⁻(x) ⊆ cl P. ✓
- ∂P ∩ (J⁺(b) ∖ {b}) = ∅ (L60–L62): cl P ⊆ J⁻(x) ∪ {t ≤ c} (using
  cl I⁻(x) = J⁻(x), closedness of J⁻ in GH); J⁻(x) ∩ (J⁺(b) ∖ {b}) = ∅ by
  Lemma-1 bookkeeping (b ≤ y ≤ x with y ≠ b, y ≠ x forces x ∈ J⁺(b) ∖ {b});
  and t > t(b) > c on J⁺(b) ∖ {b}. For x = b the same reading works with
  J⁻(x) = J⁻(b) (the draft's parenthetical "(if x = b, y = b)"). ✓
- The witness curve (L64–L68): the z → x causal segment, then a past-directed
  timelike continuation from x. The continuation lies in I⁻(x) ⊆ P (a
  past-directed causal curve from x is contained in J⁻(x), its timelike part
  in I⁻(x)), so it misses ∂P; segment points w ≠ x satisfy x ≺ w, hence
  w ∉ J⁻(x) (antisymmetry) and t(w) > c; and the timelike continuation is what
  rules out a second intersection with a possibly null-segmented achronal
  surface — the draft's remark at L71–L72 is correct and is genuinely needed,
  because ∂P does contain null segments (§2.2 counterexample below). If
  x ∉ R, the curve misses Σ ∩ R entirely, so z ∉ D⁺(Σ ∩ R), contradicting
  screening. ✓

**The convention issue, made explicit.** Whether ∂P is an admissible test
surface depends on the definition of "Cauchy surface (C⁰ allowed)".

Bernal–Sánchez (gr-qc/0512095, "Further results on the smoothability of Cauchy
hypersurfaces and Cauchy time functions"; Lett. Math. Phys., DOI
10.1007/s11005-006-0091-5) define: "a Cauchy hypersurface is a subset S ⊂ M
which is crossed exactly once by any inextendible timelike curve (and, then,
at least once by any inextendible causal curve)"; they note "Cauchy
hypersurfaces are always achronal, but not always acausal". Under this
convention ∂P qualifies (achronal + met by every inextendible causal curve
gives exactly-once for timelike curves), and Theorem 2 is **CONFIRMED**.

**Explicit counterexample to acausality of ∂P.** In 1+1 Minkowski
(ds² = −dt² + dx²), b = (0,0), x = (0,1), t the standard time function,
c = −1, C = 1:

    P    = I⁻(0,1) ∪ {t < −1}
         = {t < 0, |x′ − 1| < −t} ∪ {t < −1},
    ∂P   = {t = −1, x′ ≤ 0} ∪ {t = −1, x′ ≥ 2}
           ∪ {t = −|x′ − 1|, x′ ∈ (0,2)}
           ∪ {(−1,0), (−1,2)}.

The third piece consists of two **null segments** of ∂I⁻(x): the points
u = (−0.5, 0.5) and w = (−0.25, 0.75) both lie on t = x′ − 1 ∈ ∂P, are
distinct and null-related (Δt = Δx = 0.25). So ∂P is achronal but **not
acausal**; an inextendible null curve running along t = −|x′ − 1| meets ∂P in
infinitely many points. Under the acausal convention ("met exactly once by
every inextendible causal curve", or smooth spacelike), ∂P is inadmissible and
the proof of (⇒) collapses. (Verified numerically; script in AGENT_REPORT.md.)

**Verdict: NEEDS-FIX (presentation), substance CONFIRMED under the cited
convention.** Fix: at L23–L27, define "Cauchy surface" explicitly as the
Bernal–Sánchez C⁰ convention (achronal, crossed exactly once by every
inextendible timelike curve), cite gr-qc/0512095, and note that this is also
the convention under which Bernal–Sánchez Theorem 1.2 supplies the Cauchy
temporal function used in the proof. If the smooth spacelike acausal reading is
intended instead, one needs a new lemma:

> (A) *Avoidance lemma.* For x ∉ J⁺(b) there is a smooth spacelike Cauchy
> hypersurface Σ with x ∈ Σ and Σ ∩ (J⁺(b) ∖ {b}) = ∅.

(A) is plausible — I verified it constructively in 1+1 Minkowski for both
relative positions of x and b (level sets when t(x) ≤ t(b); a tailored graph
below the cone t = |x′| when x is spacelike-right of b) — but I found **no
citation**, and the available extension theorems do not give it:
Bernal–Sánchez Theorem 1.1 extends only *compact* spacelike acausal
submanifolds (their Example 3.4 shows smooth extension can fail for achronal
sets, and the compactness hypothesis cannot simply be dropped). Note also that
the (⇒) proof needs more than (A): the witness curve must meet Σ only at x,
which for spacelike x means Σ must additionally avoid a segment of J⁻-side
points; a level-set choice achieves this only when t(x) ≤ t(b). This route is
open; the convention fix is the recommended one.

### 2.3 Attempts to break Theorem 2

1+1 Minkowski (both orderings of x and b), 2+1 Minkowski, the conformal FLRW
slab, and the GH cylinder (Minkowski/ℤ, where J⁺ wraps) produce no
counterexample to the screening equivalence itself: the (⇐) argument uses only
Cauchy-meeting plus Lemma 1, and the (⇒) obstruction is exactly the convention
issue of §2.2. Quotient pathologies (closed causal curves, non-time-
orientability) are excluded by the GH and time-orientation hypotheses.

## 3. Theorem 3(a), steps 1 and 2 — CONFIRMED

**Step 1 (L107–L112).** A causal curve from u ∈ W to w ∈ W cannot enter
J⁺(b) (else w ∈ J⁺(u) ⊆ J⁺(b)), and every point of it is ≤ w ∈ W ⊆ I⁻(I⁺(b)),
a past set; hence it stays in W. So ≤, ≪ and Lorentzian time separation on W
are intrinsic (the sup defining the time separation runs over curves that
cannot leave W), and the isometry h preserves them; h(K₁) is acausal because
any M₂-causal curve between two of its points stays in W₂ (step 1 applied with
b₂) and pulls back to an M₁-causal curve between two points of K₁ ⊆ Σ₁, which
is impossible. ✓ (K₁ = Σ₁ ∩ W₁ is a smooth spacelike acausal boundaryless
submanifold: open piece of the smooth spacelike level Σ₁, and h is an
isometry.)

**Step 2 (L113–L116).** For x ≪ b₁, points y₁ ≪ yₙ on a timelike curve from x
to b₁ lie in I⁻(b₁) ⊆ W₁ (≈ b₁ pushes into I⁺(b₁); yₙ ∉ J⁺(b₁) by
antisymmetry). h(yₙ) → b₂ by the homeomorphism-extension hypothesis and
h(y₁) ≤ h(yₙ) for all n; closedness of J⁻(b₂) in GH gives h(y₁) ∈ J⁻(b₂), and
push-up with h(x) ≪ h(y₁) gives h(x) ≪ b₂. Symmetry in h ↔ h⁻¹ gives
h(I⁻(b₁)) = I⁻(b₂). ✓ (Both closedness of J⁻ and antisymmetry are used; both
hold in GH.)

## 4. Theorem 3(a), steps 3 and 4 — CONFIRMED with completions

### 4.3 Step 3 (L118) — citation needs a one-line repair

As written, "J⁺(b₁) ⊆ D⁺(K₁) is Theorem 2 (⇐) applied to R = D_pot(b₁)".
Since K₁ ⊆ Σ₁ ∩ D_pot(b₁), the citation as stated gives only
J⁺(b₁) ⊆ D⁺(Σ₁ ∩ D_pot(b₁)), which is the wrong inclusion direction for K₁.
It is rescued by the identity of §1: J⁻(J⁺(b₁)) = I⁻(I⁺(b₁)), so

    Σ₁ ∩ D_pot(b₁) = Σ₁ ∩ (I⁻(I⁺(b₁)) ∖ (J⁺(b₁) ∖ {b₁})) = Σ₁ ∩ W₁ = K₁,

using Σ₁ ∩ J⁺(b₁) = ∅ (t₁ ≡ −1 < 0 = t₁(b₁) on Σ₁; t strictly increasing on
J⁺(b₁)) and b₁ ∉ Σ₁. Alternatively, direct: every past-inextendible causal
curve from z ∈ J⁺(b₁) meets Σ₁ at q ≤ z, and q ∈ J⁻(z) ⊆ J⁻(J⁺(b₁)) with
q ∉ J⁺(b₁) gives q ∈ K₁ by push-up. **Fix: insert the identity or the direct
argument.** (This also proves the stronger, useful fact used in §5:
**W₁ ⊆ D⁺(K₁)** — for y ∈ W₁, any past-inextendible causal curve from y
crosses Σ₁ at q ≤ y ∈ J⁻(I⁺(b₁)) ∖ J⁺(b₁) = K₁ — and b₁ ∈ D⁺(K₁).)

### 4.4 Step 4 (L120–L136) — CONFIRMED; three completions

The case analysis is exhaustive (a curve on a half-open parameter interval
either is future-inextendible or converges to a future endpoint), and the
"last exit point" e₂ exists: J⁻(z) ∩ J⁺(b₂) is compact (GH), c cannot be
imprisoned there (t is proper along inextendible causal curves), and
c⁻¹(J⁺(b₂)) is a closed initial interval of c because J⁺(b₂) is closed.
Completions:

(i) *Tail ⊆ W₂ is push-up, not step 1.* For a tail point q ≤ e₂ with
q ∉ J⁺(b₂), pick w ∈ I⁺(e₂) ⊆ I⁺(b₂) (push-up along e₂ ∈ J⁺(b₂)); then
q ≤ e₂ ≪ w gives q ∈ J⁻(I⁺(b₂)) = I⁻(I⁺(b₂)), so q ∈ W₂. The draft credits
this to step 1; step 1 only says curves *between W-points* stay in W.

(ii) *"A past endpoint p would lie in I⁻(I⁺(b₁))" (L125–L126) needs
GH-closedness.* γ ⊆ W₁ ⊆ I⁻(I⁺(b₁)) only gives p ∈ cl I⁻(I⁺(b₁)); conclude
p ∈ J⁻(I⁺(b₁)) = cl I⁻(I⁺(b₁)) using closedness of J⁻ (GH), hence
p ∈ I⁻(I⁺(b₁)). In a non-GH spacetime this step would fail; GH is assumed.
The rest of bullet 1 is correct: p ∈ J⁺(b₁) would force γ ⊆ J⁺(b₁) (p ≤ γ
along the curve), contradicting γ ⊆ W₁; so p ∈ W₁, and h(p) would be a past
limit point of the tail, extending the past-inextendible curve c —
contradiction.

(iii) *Inner continuity of I⁻ (L133–L134) is a theorem, no GH needed for
compact C:* if C ⊆ I⁻(q) is compact and qₙ → q, cover C by finitely many
I⁻(w_i) with w_i ≪ q (open cover, then w_i ≪ qₙ eventually since I⁺(w_i) is an
open neighbourhood of q), whence C ⊆ ⋃ J⁻(w_i) ⊆ I⁻(qₙ) for large n. The
remaining limit steps are fine: C′ ⊆ J⁻(pₙ) for all large n plus closedness of
J⁺(c′) (GH) gives C′ ⊆ J⁻(p); I⁻(b₁) ⊆ I⁻(p) follows after excluding
p ∈ I⁻(b₁) ⊆ W₁ (p ∉ W₁); and b₁ ∈ cl I⁻(b₁) ⊆ cl I⁻(p) = J⁻(p) gives
p ∈ J⁺(b₁), t₁(p) ≥ 0.

With these, the conclusion "in every case c meets h(K₁)" holds, and
J⁺(b₂) ⊆ D⁺(h(K₁)). The "boundary swap" discussion (L144–L149) is consistent
with the verified bullet 3: a pulled-back curve cannot end on ∂I⁻(I⁺(b₁)),
because its exit point lies in J⁺(b₂) and step 2 transports I⁻(b₁) ⊆ I⁻(p).

**Verdict Theorem 3(a): CONFIRMED**, with the §4.3 citation fix and the §4.4
completions to be inserted; no counterexample found in 1+1/2+1 conformally flat
or quotient models (GH and the homeomorphism-extension hypothesis block the
standard quotient attacks).

## 5. Theorem 3(b) conditional logic — CONFIRMED given a D-agreement premise; but see §6

Assume some premise delivers an isometry Ψ: D_{M₁}(K₁) → D_{M₂}(h(K₁)) with
Ψ = h (values and differentials) on a neighbourhood of K₁. Then:

- *Marking.* The agreement set A = {p ∈ W₁ ∩ D_{M₁}(K₁) : Ψ(p) = h(p), dΨ = dh}
  is clopen in W₁ ∩ D_{M₁}(K₁) (isometries agreeing at a point with equal
  differentials agree nearby — geodesic determination). The component C\* of
  W₁ ∩ D_{M₁}(K₁) containing a neighbourhood of K₁ also contains a small
  timelike cone below b₁: I⁻(b₁) ∩ {t₁ > −1} is path-connected (any two of its
  points are ≪ a common point of a small cone below b₁, and timelike curves to
  it stay above t₁ = −1), and from that cone one descends to K₁ along a
  past-directed timelike curve staying in I⁻(b₁) ⊆ W₁ ⊆ D⁺(K₁) (§4.3).
  Hence Ψ = h on a set whose closure contains b₁; for pₙ → b₁ in that set,
  Ψ(b₁) = lim h(pₙ) = b₂ by continuity of the extended h.
- *Range.* D⁺ is causally convex, so with part (a) on both sides and Ψ(b₁) = b₂:
  Ψ(J⁺(b₁)) = J⁺ within D_{M₂}(h(K₁)) of b₂ = J⁺(b₂) ∩ D_{M₂}(h(K₁)) = J⁺(b₂),
  since J⁺(b₂) ⊆ D⁺(h(K₁)).

So the proof structure of (b) is sound **conditional on the development
premise**. The load-bearing question is therefore only premise (L′).

## 6. Premise (L′), L88–L103 — REFUTED as literally stated; no corrected source located

(L′) reads: "For every smooth, spacelike, acausal hypersurface S in such an M
(not necessarily part of a global Cauchy surface), D_M(S) is the maximal
globally hyperbolic development of the data induced on S, unique up to
isometry."

### 6.1 Definitional refutation

In the standard framework, a "globally hyperbolic development of initial data
(M̄, ḡ, k̄)" **requires the data manifold to embed as a Cauchy surface**:

- Sbierski, arXiv:1309.7591v3 (full text read), Definition 2.1, condition 3:
  "ι(M̄) is a Cauchy surface in (M,g)"; footnote 3: "A globally hyperbolic
  development is not just a 'development' which is globally hyperbolic, but one
  also requires that the initial data embeds as a Cauchy hypersurface."
- Choquet-Bruhat & Geroch 1969 (abstract, INSPIRE): "Any solution of Einstein's
  equations which has a Cauchy surface may be embedded in exactly one such
  maximal development."
- Ringström 2009 (not accessed; scope per Sbierski §1 and Ringström's CQG 2015
  survey abstract): same full-Cauchy-data framework.

So "the maximal globally hyperbolic development of the data induced on S" is
not a defined object of that framework unless S embeds as a Cauchy surface of
the development. The draft's own target surfaces cannot: K₁ is a *proper open
part* of the Cauchy surface Σ₁ of M₁ (its complement in Σ₁ is nonempty exactly
when W₁ ≠ full slice, the generic case), and part (a) of Theorem 3 itself
produces h(K₁) as a screen that is "not… an open subset of a Cauchy surface of
M₂" in general (L95–L99).

### 6.2 Explicit counterexample to "D_M(S) is the maximal globally hyperbolic development"

Take 1+1 Minkowski space and the draft's own Finding-2 surface (also used at
L98–L99), S = {t = √(1 + x²)}, i.e. the upper branch of t² − x² = 1.

1. S is smooth, spacelike and acausal: for points (cosh u, sinh u),
   (cosh v, sinh v), (Δt)² − (Δx)² = 2 − 2 cosh(u − v) < 0 for u ≠ v.
2. D⁺(S) = {t ≥ √(1 + x²)}. If p is inside (t₀² − x₀² > 1, t₀ > 0) and c is
   any past-inextendible causal curve from p, then φ = t² − x² is continuous
   along c with φ(p) > 1 and, at the curve's crossing of t = 0,
   φ ≤ 0 < 1 (a past-inextendible causal curve has t → −∞, since a bounded t
   would give a limit point and an extension); by the intermediate value
   theorem c meets S. Conversely a point below S has a past-directed null ray
   staying strictly below S. D⁻(S) = S for the same reason. Hence
   D(S) = {t ≥ √(1 + x²)}: a **closed region with nonempty interior — not an
   open spacetime manifold**. "D_M(S) is the maximal globally hyperbolic
   development" is therefore ill-formed for this S.
3. S is contained in **no** Cauchy hypersurface of Minkowski space, in either
   convention. Any acausal Σ ⊇ S meets each vertical (timelike) line exactly
   where S does, so Σ = S as a set; but S is not Cauchy: the inextendible
   timelike curve γ(t) = (t, t + 1 − ½ arctan t) satisfies x(t) − t =
   1 − ½ arctan t > 1 − π/4 > 0, i.e. it rides the right null cone for all t
   with slope strictly below 1 (timelike), and it never meets S (verified
   numerically and by 2 − 2 cosh above). Nor does any achronal Σ ⊋ S exist
   that is Cauchy, since Cauchy hypersurfaces are achronal and the vertical-line
   argument pins Σ = S on all of ℝ. This also independently confirms the
   coordinator's Finding 2 example (CLAUDE_SCREENING_REVIEW.md), and shows the
   compactness hypothesis in Bernal–Sánchez Theorem 1.1 cannot be dropped.

### 6.3 The uniqueness/maximality clause fails for partial data

Under any reading of "development of (S, data)" that only requires a GH
spacetime containing S with matching data, maximal elements need not exist:
the region causally disconnected from D(S) ∪ S (here {t < √(1 + x²)} ∖ S) is
unconstrained by the data, and modifications of the spacetime there (e.g.
topology change attached in the deep past, with the future of the modification
kept out of cl D(S) ∪ S, so that causal relations between points of S are
unchanged) yield smooth globally hyperbolic developments of the same partial
data that are non-isometric (π₁ differs) and incomparable. Caveat recorded
honestly: writing the smooth vacuum (or other-theory) realization of such a
patch requires a construction I did not carry out; items 1–3 above do not
depend on it. The mechanism is the standard one visible in Sbierski's own
proof technique: gluing two developments along a common region produces a
non-Hausdorff space exactly when "corresponding boundary points" exist — for
full Cauchy data maximality forbids them (his §1.5/Thm 3.4 discussion); for
partial data they are precisely the branching at the Cauchy horizon of D(S),
and nothing forbids them.

### 6.4 Premise-L source search (access gate)

Searches run 2026-10-31 (all via `scholar_search`/Openalex and Exa; see
AGENT_REPORT.md for the query list and the tool check):

- "Sbierski maximal Cauchy development Einstein equations" → arXiv:1309.7591
  identified (see sources.jsonl). **Full-data only** (Thms 2.6–2.8).
- "\"partial Cauchy surface\" maximal globally hyperbolic development
  uniqueness" → nothing on point (hits are about timelike-boundary IBVPs,
  Kerr horizons, hole-argument exposition).
- "initial data hypersurface with boundary maximal development Einstein domain
  of dependence uniqueness" → nothing on point (IBVP literature; Sarbach–Tiglio
  review; Fournodavlos–Smulevici; An–Anderson — all timelike-boundary problems,
  a different question).
- "Cauchy problem initial data on achronal hypersurface not Cauchy …" →
  nothing on point.
- Exa: Bernal–Sánchez extension theorems located (compact-only, §2.2); Exa
  sweep for a partial-surface development statement → nothing.
- Wong 2014 ("A comment on the construction of the maximal globally hyperbolic
  Cauchy development", abstract only) generalizes the *construction* to any
  deterministic geometric theory, still for full Cauchy data.
- Müller arXiv:2404.06428 (abstract only) studies "maximal Cauchy
  developments" of Lorentzian length spaces — a lead for non-manifold settings,
  not a statement of (L′).

**Conclusion: premise (L′) is not available in the literature in its stated or
in any corrected form; the full-data theorems (CBG 1969; Sbierski 2015;
Ringström 2009) do not cover it, and Sbierski's Definition 2.1(3) positively
excludes the required generality. Ringström's 2009 monograph was not accessible
in this environment (recorded as an access gate); its scope was assessed from
Sbierski's and Ringström's 2015 survey descriptions.**

### 6.5 Recommended repair (replaces the two routes at L100–L103)

Replace (L′) by the weaker premise actually used by the proof of (b):

> **(L″) D-agreement.** For the given theory, if (M,g), (M′,g′) are maximal
> globally hyperbolic developments and K ⊆ M, h(K) ⊆ M′ are smooth spacelike
> acausal hypersurfaces with h: K → h(K) an isometry carrying the fields, then
> D_M(K) and D_{M′}(h(K)) are isometric via an isometry equal to h (with
> differential) on a neighbourhood of K.

(L″) suffices for §5 verbatim; no maximality or uniqueness of "the development
of partial data" is needed. Status: I could not locate (L″) in print either
(same gate). It should be provable by the standard local uniqueness
(Choquet-Bruhat 1952) propagated along causal curves inside D(K) — the same
mechanism as Sbierski's global uniqueness, restricted to the domain of
dependence, where no branching occurs — but until it is written out or sourced,
Theorem 3(b) must remain explicitly conditional. The alternative route at
L100–L103 ("prove h(K₁) lies in a Cauchy surface of M₂") is blocked in this
generality by §6.2 item 3 plus the compactness gate in Bernal–Sánchez Thm 1.1;
it may still be feasible for the specific h(K₁) via the pull-back structure of
step 4, and is worth a dedicated task.

## 7. Other checked statements

- Classification table (L156–L164): the J⁻(b) row is confirmed by explicit
  example in 1+1 Minkowski: b = (0,0), Σ = {t = −1} is Cauchy and disjoint
  from J⁺(b) ∖ {b}; z = (2,0) ∈ J⁺(b) has the past-directed timelike curve
  to (−1, −2.9) (Δt = 3, Δx = −2.9), which meets Σ outside
  J⁻(b) ∩ Σ = {|x| ≤ 1} — so z ∉ D⁺(Σ ∩ J⁻(b)): J⁻(b) does not screen. The
  equivalence "J⁻(b) screens iff D_pot(b) = J⁻(b)" matches Theorem 2.
- Lemma-1 corollary at L214–L216: D_BT(b) ∖ D_pot(b) = E(b) ∖ J⁻(J⁺(b)).
  Verified set-algebraically (x ≤ b would put x ∈ J⁻(I⁺(b)) ⊆ J⁻(J⁺(b))).
- The identity "D_pot(b) = I⁻(I⁺(b)) ∖ (J⁺(b) ∖ {b})" (via §1) is a
  presentation simplification the draft may adopt.

## 8. Falsifiers for this review

(i) A spacetime in which some inextendible causal curve misses ∂P of §2.2
(would break the connectedness argument of Theorem 2 (⇒) even in the weak
convention). (ii) A pair of GH spacetimes with isometric W-realms matching the
full hypotheses of Theorem 3 but with h(K₁) not in any Cauchy surface and
D-agreement failing (would refute (L″) and kill route (b) entirely). (iii) A
smooth spacelike acausal S with D(S) an open GH spacetime of which S is the
Cauchy boundary, for the S of §6.2 (would weaken the definitional refutation).
(iv) A printed statement of (L′)/(L″) in Ringström 2009 or elsewhere (would
close the access gate).
