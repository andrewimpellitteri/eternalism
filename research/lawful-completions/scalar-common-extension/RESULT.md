# Smooth Einstein–massless-scalar field-preserving common development: theorem, corollary, and audit

29 October 2026. Worker submission for independent review; not an accepted
result. No novelty claim. Extends the repaired vacuum common-development
argument (`coordinator/COMMON_EXTENSION_REPAIR.md`, `coordinator/REPAIR_RESULT.md`,
reviewed in `screening-repair-review/REVIEW_COMMON_EXTENSION.md`) to smooth
Einstein massless real scalar matter, and audits the specific items named in the
task brief.

Summary of what this document establishes:

1. **Theorem A (source-backed, proved).** The precise field-preserving
   common-GHD-extension theorem for smooth Einstein–scalar data is a published
   theorem: Ringström, *The Cauchy Problem in General Relativity* (EMS, 2009),
   Theorem 14.3 (p. 158), in the author's normalization; the containing-both
   form is proved in the author's posted correction note
   (`people.kth.se/~hansr/mghd.pdf`: Definition 6.1, Lemma 6.4, Definition 6.7,
   Lemma 6.10, Lemma 10.1). This resolves the gate left open in
   REVIEW_COMMON_EXTENSION.md ("for scalar/matter readings, accept only after a
   field-preserving common-development result ... is cited").
2. **Corollary C (assembled here, conditional on named geometric inputs).** The
   smooth scalar analogue of the repaired common-duration theorem: matched
   geodesic readings *and matched scalar readings* agree at every finite proper
   duration for which both models define them. Proof is a step-by-step
   replacement of Sbierski Theorem 2.7 by Theorem A in the repaired argument,
   with the field transported along the identified path.
3. **One precise gap isolated.** The domain step on the matched side requires
   `K_2 = h(Σ_1)` to be **closed in M_2** (equivalently edgeless) for the
   standard domain theorem (`D(K)` open globally hyperbolic, `K` Cauchy) to
   apply. Closedness is *not* established in COMMON_EXTENSION_REPAIR.md or its
   review; a partial positive result (no accumulation on `J⁺(b_2)`) is proved
   here as Lemma D. The corollary is stated conditional on this gate.

Throughout, `(n+1)`-dimensional time-oriented Lorentzian manifolds, `n ≥ 3`;
all fields smooth. The unqualified symbol `D` denotes the causal (two-sided)
domain of dependence; `D⁺` its future part.

## 1. Setting and conventions

### 1.1 The two normalizations and the conversion

Task normalization (matches Luk–Oh–Yang's reduced SSESF convention, see
§5):

- (E1) `Ric(g) = 2 dφ ⊗ dφ`,
- (E2) `□_g φ = 0`,

with stress-energy tensor obtained from the Einstein equation
`G = T`:

- `T_ab = 2 ∂_a φ ∂_b φ − (∇φ)² g_ab`, where `(∇φ)² = g^{cd} ∂_c φ ∂_d φ`.

Ringström's normalization (correction note, equations (2)–(3), quoted verbatim
in the extraction record `sources.jsonl`, id `scalar-ringstrom-mghd-note`):

- `Ric − dϕ ⊗ dϕ − (2/(n−1)) V(ϕ) g = 0`,
- `□_g ϕ − V₀(ϕ) = 0` (`V₀` the derivative of the potential `V`).

**Conversion.** For `V ≡ 0` (the massless case), Ringström's system is
`Ric = dϕ ⊗ dϕ`, `□_g ϕ = 0`. The linear field redefinition
`ϕ = √2 φ` maps the task system exactly onto Ringström's massless system:
`dϕ ⊗ dϕ = 2 dφ ⊗ dφ`, and the wave operator is invariant under constant
rescaling. Both systems are thus the same theory up to field normalization;
every development, isometry, or embedding statement transfers verbatim after
rescaling the field. Nothing below depends on the normalization; locators are
given in Ringström's, with conversion stated where the constraint equations are
written.

### 1.2 Initial data and constraints

Ringström, correction note Definition 2.1: initial data consist of an
`n`-dimensional manifold `Σ`, a Riemannian metric `γ̄`, a symmetric
2-tensor `κ̄`, and two smooth functions `ϕ̄₀`, `ϕ̄₁`, satisfying

- `r̄ − κ̄_ij κ̄^ij + (tr κ̄)² = ϕ̄₁² + ∇ⁱϕ̄₀ ∇_i ϕ̄₀ + 2V(ϕ̄₀)`,
- `∇ⁱ κ̄_ij − ∇_j (tr κ̄) = ϕ̄₁ ∇_j ϕ̄₀`.

In the task normalization with `V ≡ 0` (substituting `ϕ̄ = √2 φ̄`), the
constraint right-hand sides are `2(φ̄₁² + |∇φ̄₀|²)` and `2 φ̄₁ ∇φ̄₀`
respectively. Two audit-relevant features of Definition 2.1, both verified
verbatim today from the author's PDF:

- **No compactness, completeness, or asymptotic condition on `Σ` is stated.**
  "An `n` dimensional manifold `Σ`" with smooth tensors; the same convention
  as Sbierski's vacuum Definition 2.1 ("connected `d`-dimensional Riemannian
  manifold", no completeness), which was re-verified verbatim today from the
  ar5iv rendering of arXiv:1309.7591. Connectedness is needed for the
  common-development machinery applied componentwise; see §3.2.
- The development data include the **field value** `ϕ̄₀ = ϕ ∘ i` and the
  **normal derivative** `(Nϕ) ∘ i = ϕ̄₁`, not only the stress tensor. This
  matters for §3.4.

### 1.3 Symmetries of the scalar coupling (shifts and signs)

Equations (E1)–(E2) involve `φ` only through `dφ`, so they are invariant under
`φ ↦ −φ` and `φ ↦ φ + c` (`c` constant). Consequences used below:

- Developments of data sets differing by a shift or sign have isometric
  metrics but are *different data sets* for Ringström's theorems, because the
  data include the value `φ̄₀`. The common-extension theorem preserves `φ`
  pointwise relative to the data actually supplied; it does not, and need not,
  identify shifted copies.
- The stress tensor `T` determines `dφ` on a slice only up to an overall sign
  (from `T_an = 2(∂_a φ)(nφ)` and `T_nn = 2(nφ)² + (∇φ)²`), and never
  determines the additive constant. See §3.4 for why this forces the realm
  hypothesis to be field-preserving rather than merely T-preserving.

## 2. Theorem A: the field-preserving common-GHD extension (proved, source-backed)

**Theorem A (common development with fields, two directions).** Let
`(Σ, γ̄, κ̄, ϕ̄₀, ϕ̄₁)` be smooth initial data for the Einstein–nonlinear
scalar field system (Ringström normalization; `V ≡ 0` gives the massless task
system) on a connected smooth `n`-manifold `Σ`. Let
`(M₁, g₁, ϕ₁)`, `(M₂, g₂, ϕ₂)` be smooth time-oriented globally hyperbolic
developments of this data, with embeddings `i_j : Σ → M_j` (Cauchy, data
compatible: `i_j^* g_j = γ̄`, `ϕ_j ∘ i_j = ϕ̄₀`, `i_j^* κ_j = κ̄`,
`(N_j ϕ_j) ∘ i_j = ϕ̄₁`). Then:

(a) **Contained form** [Ringström 2009, Theorem 14.3, p. 158; restated
verbatim as Theorem 2.4 of the correction note]: there is a smooth time-oriented
GHD `(N, g_N, ϕ_N)` with embedding `i : Σ → N` and smooth time-orientation
preserving diffeomorphisms onto their images `ψ_j : N → M_j` such that
`ψ_j^* g_j = g_N` **and `ψ_j^* ϕ_j = ϕ_N`** (`j = 1, 2`), and
`ψ_j ∘ i = i_j`.

(b) **Containing form** [correction note Definition 6.1, Lemma 6.4,
Definition 6.7, Lemma 6.10, Lemma 10.1; used inside the proof of Corollary 10.2
there]: there is a smooth time-oriented GHD `(Ñ, g̃, ϕ̃)` of the same data
into which **both** `(M₁, g₁, ϕ₁)` and `(M₂, g₂, ϕ₂)` admit isometric
embeddings in the sense of the note's Definition 2.7, i.e. embeddings
preserving metric **and scalar field** and compatible with the initial-data
embeddings.

In neither form is either development required to be maximal, to lie in an
ambient MGHD, or to satisfy any completeness condition; `Σ` is an arbitrary
connected smooth manifold. Form (b) is the exact coupled analogue of Sbierski's
vacuum Theorem 2.7, and is what the repaired argument's hypothesis 4 needs
(`F_i : N_i → N` with `F_i` defined on all of `N_i`).

**Proof status and exact dependencies.**

- Theorem A(a) is Ringström's published statement; the statement was verified
  verbatim today from the author's correction note (which quotes Theorem 14.3
  with page locator and restates it as its Theorem 2.4). Existence of a GHD
  (needed input) is [2009 book, Theorem 14.2, p. 156; note Remark 2.2 and
  Theorem 2.3].
- Theorem A(b) is assembled from the correction note's own chain:
  Definition 6.1 defines the field-preserving identification class
  `C(M, M̂)` (`ψ^*g = ĝ, ψ^*ϕ = ϕ̂`); Remark 6.2 gives non-emptiness from
  Theorem 2.4; Lemma 6.4 gives the unique maximal element (this uses Zorn's
  lemma via the note's Theorem 3.4; the note's use of choice is open and
  correct, unlike the flawed book step it replaces); Definition 6.7 defines the
  glued common extension `M̃` with metric `g̃` and *function* `ϕ̃`;
  Lemma 6.10 (verified verbatim: "If `M̃` is Hausdorff, then
  `(M̃, g̃, ϕ̃)` is a globally hyperbolic development of the initial data
  such that `(M,g,ϕ)` and `(M̂,ĝ,ϕ̂)` can be isometrically embedded into
  it"); Lemma 10.1 (verified verbatim in statement and proof opening): the
  common extension is Hausdorff. The combination is exactly what the proof of
  the note's Corollary 10.2 invokes ("Due to Lemma 10.1, `M̃` is then
  Hausdorff, so that `(M̃, g̃, ϕ̃)` is a globally hyperbolic development of
  the initial data due to Lemma 6.10.").
- **Documented erratum history, checked:** the book's MGHD proof contained an
  error (`[8, Theorem 16.6, p. 177]`; the incorrect claim is at
  [8, p. 178, l. −14/−13]: that every totally ordered subset of the then-used
  class has an upper bound). The errata file confirms the error is confined to
  that step; **no errata item touches pp. 147–163** (Chapters 13–14, where
  Theorems 14.2 and 14.3 live). The correction note supplies the corrected
  complete proof and does not flag Theorem 14.3.
- Residual audit limit: the book's interior proof pages (152–163, 176–183) were
  not independently audited (no lawful access); the chain rests on the
  author's own verbatim restatements, the free Introduction chapter, the
  detailed contents, and the errata. The note's §7–8 (boundary structure) and
  most proofs of §9 were read at statement level only; Lemma 10.1's proof was
  read in its opening and not re-derived.

## 3. Task-specific audits

### 3.1 Arbitrary connected noncomplete initial hypersurfaces

Allowed. Definition 2.1 (correction note) and Definition 2.1 (Sbierski) impose
no completeness, compactness, or asymptotic condition; Theorems 14.2/14.3 are
stated for smooth data on a general smooth `n`-manifold. In particular the
*restricted* initial manifold `K₁^b` below (an open submanifold of a Cauchy
slice, typically noncomplete as a Riemannian manifold) is admissible data.
Caveat recorded in §2: book interior proof pages not audited; the statement
chain is author-verbatim.

### 3.2 Restricted developments `D(K)`, and the isolated gap

In the repaired setup (SCREENING.md Theorem 3 setting, `t₁(b₁) = 0`,
`Σ₁ = {t₁ = −1}`), the earlier Cauchy slice lies entirely in the realm:
`Σ₁ ⊂ I⁻(b₁) ⊂ W₁`, so `K₁ = Σ₁ ∩ W₁ = Σ₁` is a **full** Cauchy surface of
`M₁`; `D_{M₁}(K₁) = M₁` needs no domain theorem on side 1. The genuine
restriction is on side 2: `K₂ = h(Σ₁) ⊂ W₂` is a smooth spacelike acausal
embedded hypersurface without intrinsic boundary (isometric image of the
slice), acausal in `M₂` by causal convexity of `W₂`, and
`J⁺(b₂) ⊆ D⁺_{M₂}(K₂)` holds by SCREENING.md Theorem 3(a) step 4 (reviewed;
inherited, not re-proved here). What the repaired argument then needs is:

- (G) `D_{M₂}(K₂)` is an open globally hyperbolic spacetime in which `K₂` is
  a Cauchy hypersurface.

**Gate found.** The precise source statement (Minguzzi, *Lorentzian causality
theory*, Living Reviews in Relativity 22 (2019) 3; read full-text today):

- Definition 3.35: a **partial Cauchy hypersurface** is an acausal *edgeless*
  set (hence closed); Definition 2.130 defines the edge.
- Theorem 3.45 (as invoked by Theorem 3.50; attributed there to Penrose 1972,
  Proposition 5.14, and Geroch 1970, Proposition 6): for `S` closed and
  achronal, `Int D(S)` is globally hyperbolic with the induced metric.
- Theorem 3.50: for `S` closed and achronal, and `S′` a Cauchy hypersurface of
  `Int D(S)`, the domains agree; **if `S` is a partial Cauchy hypersurface**
  (i.e. edgeless, hence closed) **then `D(S) = Int D(S)` is open globally
  hyperbolic with `S` Cauchy**.

The operative hypothesis is closedness (edgelessness) of `K₂` **as a subset of
`M₂`** — not merely smoothness, acausality, or absence of intrinsic boundary.
Counterpoint examples: an open disk in a Minkowski slice, or a punctured slice,
is smooth-spacelike-acausal without intrinsic boundary but is not closed, and
its edge/horizon structure is exactly what the theorem excludes. Neither
COMMON_EXTENSION_REPAIR.md ("acausal topological hypersurface without
boundary") nor REVIEW_COMMON_EXTENSION.md ("without intrinsic boundary")
establishes closedness of `h(Σ₁)` in `M₂`. **(G) is therefore an unresolved
access/geometry gate for the repaired argument on side 2, inherited by
Corollary C.**

**Partial result (Lemma D, proved here).** *No accumulation on the causal
future part of the realm boundary: if `p_k ∈ Σ₁` and `h(p_k) → z` in `M₂`,
then `z ∉ J⁺(b₂) ∖ {b₂}`.* Proof: suppose `z ∈ J⁺(b₂)`. Choose `w ∈ I⁺(b₂)`
with `z ≪ w` (exists since `J⁺(b₂) ⊆ I⁻(I⁺(b₂))`; push-up from
`b₂ ≤ z ≪ w`). For large `k`, `y_k := h(p_k) ∈ I⁻(w) ∩ W₂`; causal convexity
of `W₂` gives `y_k ≪ w` with the connecting curve in `W₂`, hence
`p_k ≪_{M₁} h⁻¹(w)`. In the globally hyperbolic `M₁` with Cauchy surface
`Σ₁`, the set `J⁻(h⁻¹(w)) ∩ Σ₁` is compact, so a subsequence
`p_k → p ∈ Σ₁`; continuity of `h` gives `z = h(p) ∈ h(Σ₁) ⊆ W₂`,
contradicting `z ∈ J⁺(b₂) ⊆ ∂W₂`. ∎

What remains open is accumulation of `h(Σ₁)` on the horizon part
`∂I⁻(I⁺(b₂)) ∖ J⁺(b₂)` (points spacelike-or-null to every common successor of
`b₂`, where the "fix one `w ≫ b₂`" compactness step is unavailable). Ruling
this out — or replacing (G) by a direct proof that `D_{M₂}(K₂)` is open GH
with `K₂` Cauchy — is a proposed next task (§6). Note the gate is independent
of the matter content: it sits entirely in the causal-geometric layer shared
with the vacuum repair.

### 3.3 Which preservation: field value vs stress tensor

The realm hypothesis must be **field-preserving** (`h^* ϕ₂ = ϕ₁` on `W₁`),
not merely stress-energy preserving, for the development-identification route:

- The common-extension theorems identify *Cauchy data*. The data include
  `(γ̄, κ̄, ϕ̄₀, ϕ̄₁)`. A metric isometry alone transports `γ̄`; field
  preservation transports `ϕ̄₀` and, by differentiating `h^*ϕ₂ = ϕ₁` and using
  time-orientation preservation (common future unit normal), also transports
  the normal derivative `ϕ̄₁`.
- `T` on a slice does **not** determine `κ̄` (the Gauss/Codazzi contractions
  constrain only `|κ̄|² + (tr κ̄)²` and `div κ̄ − d(tr κ̄)`), so
  T-preservation alone would leave the extrinsic-curvature data unmatched, and
  Theorem A could not be applied to the transported data. In the vacuum repair
  this issue is absent because there is no matter datum beyond `(γ̄, κ̄)`.
- Conversely, once the data (including the field value) match, field
  preservation on the developments is *not an extra assumption*: in Theorem A
  it is part of what the coupled theorem transports (`ψ_j^* ϕ_j = ϕ_N`), and
  it can also be re-derived on any common metric development by linear
  uniqueness: `ϕ_N ∘ F_j` and `ϕ_j` are both smooth solutions of the
  normally hyperbolic operator `□_{g_j}` on the GH development with equal
  value and normal derivative on the Cauchy surface, so Bär–Ginoux–Pfäffle
  Corollary 3.2.4 (verified verbatim today from arXiv:0806.1036: zero value
  and normal derivative along a smooth spacelike Cauchy hypersurface force the
  homogeneous solution to vanish) gives equality. This is the same
  arbitrary-solution uniqueness the screening-repair review verified at
  full-text depth; re-verified here for this lane's record.

### 3.4 Allowed scalar shifts and signs

With field-value data (§1.2), the shift/sign freedom is fixed by the data: two
developments of the *same* data have equal `φ` at the marks and along matched
curves. If one instead compares developments of data related by
`φ ↦ −φ` or `φ ↦ φ + c`, Theorem A applies to each data set separately and
yields no cross-identification; at the stress-tensor level the two families
are indistinguishable (same `T`, same `Ric`). Any "T-level realm matching
implies φ-level matching" shortcut is therefore invalid without the
data-value compatibility of §3.3.

### 3.5 Compatibility with the first-jet/path identification of the marks

The repaired argument's identification steps are metric-level and transfer
unchanged; the field rides along:

1. **First jet at `p ∈ K₁`.** `F₁`, `F₂ ∘ h` are isometric immersions into the
   common `(Ñ, g̃)` (Lemma 3.1 of Sbierski, re-verified verbatim today: two
   isometric immersions from a connected source agreeing in value and
   differential at one point agree everywhere; field-independent, applies to
   the metric). Value agreement at `p` is initial-data compatibility; the
   differential agrees on `T_p K₁` by restriction and on the normal by common
   time orientation.
2. **Path.** Along the comparison path `α` (domain lemma of
   COMMON_EXTENSION_REPAIR.md, unchanged), equality of maps holds; hence
   `ϕ̃(F₁(α(t))) = ϕ₁(α(t)) = ϕ₂(h(α(t))) = ϕ̃(F₂(h(α(t))))`: the scalar
   identities hold *because* the maps agree and both preserve `ϕ̃`.
3. **Marks.** Endpoint limit (homeomorphic mark extension in hypothesis 1)
   gives `F₁(b₁) = F₂(b₂)` and equality of field values at the marks.
4. **Launch tangents.** The transition isometry `F₂⁻¹ ∘ F₁` near the common
   mark is now field-preserving automatically (`ϕ₂ ∘ F₂⁻¹∘F₁ = ϕ₁` on the
   overlap, from `F_i^* ϕ̃ = ϕ_i`), so matched launch data include matched
   scalar state; an independently chosen tangent remains unmatched, as in the
   vacuum repair.

### 3.6 Regularity and class limits (no silent upgrades)

The corollary below is confined to the smooth category. It does not include
the low-regularity spherical scattering class (§5), does not revisit localized
maximality L′, and adds no completeness, maximality, lifetime, topology, or
whole-future claim. The clipped-Minkowski sharpness example of
COMMON_EXTENSION_REPAIR.md remains valid inside the scalar theory: it is the
case `φ ≡ const` (e.g. 0), which solves (E1)–(E2); equal realms, field
preserved, yet the central observer's proper time ends at `T` in `M₁`. Equal
survival still does not follow in the nonmaximal class, and the completeness
corollary still needs its explicit premise.

## 4. Corollary C: the smooth scalar common-duration corollary (assembled; conditional)

**Corollary C.** In the setting of the repaired vacuum theorem
(COMMON_EXTENSION_REPAIR.md hypotheses 1–5) with the following three changes:

- (i) the deterministic geometric field theory is the smooth Einstein massless
  real scalar system in the task normalization (E1)–(E2) (equivalently
  Ringström's massless system after `ϕ = √2 φ`);
- (ii) the realm isometry of hypothesis 1 is required to be field-preserving:
  a time-orientation preserving onto isometry `h : W₁ → W₂` with
  `h^* ϕ₂ = ϕ₁`, extending homeomorphically with `b₁ ↦ b₂`;
- (iii) hypothesis 4 (common-GHD extension for the data) is supplied by
  Theorem A(b) instead of Sbierski's vacuum Theorem 2.7;

— then: for the connected marked developments `C_i` with Cauchy components
`K_i^b` (component selection as verified in the repair and its review), the
common extension `Ñ` of Theorem A(b), and the marked first-jet/path
identification of §3.5, the embeddings `F_i : C_i → Ñ` satisfy
`F_i^* g̃ = g_i`, `F_i^* ϕ̃ = ϕ_i`, `F₁(b₁) = F₂(b₂)`; and **every matched
geodesic proper-time reading and every matched scalar reading** — the field
value `ϕ_i(γ_i(τ))`, and every scalar contraction built from `dϕ_i` and the
metric along the matched curve, e.g. `(∇ϕ)²`, `dϕ(γ̇)` — **agree at every
finite proper duration `T` for which both models define the corresponding
segments**.

*Proof assembly, with dependencies.* (1) Component and domain layer: side 1
`C₁ = M₁`, `K₁^b = Σ₁` (§3.2); side 2 needs (G) — **conditional**; the
marked-component match (`h(α)` lands in `C₂`; `J⁺(b_i) ⊆ C_i`) is the
repair's reviewed argument, unchanged. (2) Data layer: `h` transports
`(γ̄, κ̄, ϕ̄₀, ϕ̄₁)` exactly (§3.3); the transported tensors satisfy the
scalar constraints automatically (Gauss–Codazzi contraction of (E1)–(E2) in the
ambient solutions). (3) Extension layer: Theorem A(b) gives `Ñ` with
field-preserving embeddings — **proved (source)**. (4) Identification layer:
§3.5 — Sbierski Lemma 3.1 (metric; verified) + field transport. (5) Reading
layer: geodesic IVP uniqueness in the common smooth `Ñ` for the matched
initial data; scalar readouts agree since both curves are the same curve in
`Ñ` up to field-preserving isometry. (6) Scope layer: §3.6 — no upgrades.
∎

The three strength tiers of the repair carry over verbatim: common-duration
agreement unconditionally (modulo (G)); onto chronological-future
identification if every future timelike geodesic from both marks is complete;
onto causal-future identification if every future causal geodesic from both
marks is complete (Avez–Seifert input as in Minguzzi Theorem 4.123, per the
review lane's verified locator). Under those completeness premises the
identifying isometries are field-preserving by the same pullback argument as
§3.5(4). Completeness remains an extra premise, never a consequence of realm
matching.

## 5. Distinctness from the Luk–Oh–Yang low-regularity scattering limit

The coordinator's lane already records Luk–Oh–Yang, arXiv:1605.03893v1
(spherically symmetric Einstein–scalar system, bounded-variation norms,
characteristic construction, `Ric = 2 dφ²` normalization — the same field
normalization as the task) at full-text depth in
`coordinator/sources.jsonl`. This task's result is disjoint from and
independent of it: smooth (`C∞`) initial data and GHDs versus BV/low-regularity
profiles; standard Cauchy slices versus double-null characteristic data;
common-development uniqueness versus scattering construction. No low-regularity
uniqueness, existence, or scattering conclusion is used or implied here, and
the smooth corollary is not an upgrade path into that class.

## 6. Status ledger and next tasks

**Proved (source-backed, statements verified verbatim this session):**

- Theorem A(a), A(b) — field-preserving common extension, coupled Einstein
  scalar, general smooth connected data, no maximality (§2).

**Assembled here, conditional on named inputs:**

- Corollary C — conditional on (a) the geometric screening transport
  Theorem 3(a) of SCREENING.md (inherited; independent adversarial check of
  that lane still outstanding per COMMON_EXTENSION_REPAIR.md), and (b) gate
  (G) below.
- Lemma D (no accumulation on `J⁺(b₂)`) — proved here from GH compactness;
  uses only standard causality, no sources beyond Minguzzi/O'Neill-level
  facts already in the lane.

**Unresolved gates (explicit):**

- (G) Closedness (= edgelessness) of `h(Σ₁)` in `M₂`, or a direct proof that
  `D_{M₂}(h(Σ₁))` is open GH with `h(Σ₁)` Cauchy, or a reformulation of the
  side-2 development that avoids (G). Partial progress: Lemma D; the residual
  risk is accumulation on `∂I⁻(I⁺(b₂)) ∖ J⁺(b₂)`.
- Book-interior proof audit (Theorems 14.2/14.3 at pp. 156/158) — statement
  chain is author-verbatim (correction note + errata + free chapter +
  contents); interior pages not lawfully accessed.

**Proposed next tasks:**

1. Close or refute (G): either prove `h(Σ₁)` closed in `M₂` (extend Lemma D
   to the horizon part, or find a rigidity argument for realm isometries),
   or construct a counterexample pair satisfying hypotheses 1–3 with
   `h(Σ₁)` non-closed, or find a published domain theorem covering acausal
   embedded hypersurfaces without edgelessness.
2. If (G) closes, re-run the marked-readout audit end-to-end with the field
   (this document's Corollary C becomes unconditional modulo the screening
   containment).
3. Independently re-derive (or audit) Ringström's Lemma 10.1 for the coupled
   system, in the spirit of Sbierski's dezornification, to remove the Zorn
   dependence in Theorem A(b); the vacuum-only dezornification (Sbierski) does
   not cover the field.
4. Decide whether the T-only variant (realm isometry preserving only `g` and
   `T`) admits any replacement hypothesis that restores data matching; §3.3
   suggests it cannot without extra geometric input.

## 7. Verification record

Search capability check (required by the brief): `scholar_search` (server/tool
`scholar_search`, OpenAlex backend) — **worked** (returned Friedrich–Rendall,
Sbierski, Costa–Girão–Natário–Silva, Svedberg, Bernhardt records).
`exa.web_search_exa` / `exa.web_fetch_exa` — **worked** (EMS Press book pages
and free chapter file, Ringström KTH PDFs, ar5iv full texts, Minguzzi LRR
PDF). Direct `webfetch` — **worked** (errata.html HTML with links).
`serpapi_search` — **quota exhausted** ("Your account has run out of
searches"); recorded, not circumvented. `web-search-prime` — not called, per
brief (quota exhausted until 2026-11-17).

Primary fetches this session (all public): `ar5iv.labs.arxiv.org/html/1309.7591`
(Def 2.1, Thms 2.6–2.8, Lemma 3.1, Cor 3.2, Thms 3.4/3.6 extracted verbatim);
`people.kth.se/~hansr/errata.html` → `errata_book.pdf` (full list; no items on
pp. 147–163; error at p. 178 documented) → `mghd.pdf` (system eq. (2)–(3),
Def 2.1, Thms 2.3/2.4, Defs 2.5/2.7, Lemma 2.8, Def 6.1, Lemma 6.4, Def 6.7,
Lemma 6.10, Cor 9.3, Lemma 9.4, Lemma 10.1, Cor 10.2, references extracted
verbatim); `ems.press` contents + free Introduction chapter 1 (scalar-field
scope confirmed verbatim); `people.kth.se/~hansr/Cauchyproblem.pdf` (survey:
"[19] ... complete proof ... in the Einstein-non-linear scalar field setting"
verbatim, references [19]/[20] resolved); `ar5iv.labs.arxiv.org/html/0806.1036`
(BGP Corollary 3.2.4 statement and proof opening extracted verbatim);
`link.springer.com/content/pdf/10.1007/s41114-019-0019-x.pdf` (Minguzzi Def
2.130, Def 3.35, Thm 3.45 as invoked, Thm 3.50, D(S)/D(S) definitions
extracted). Full machine-checkable records with read depths: `sources.jsonl`
in this directory.

Exact-version notes: Sbierski statements taken from the ar5iv rendering of
arXiv:1309.7591 and cross-checked against the v3 quotes in
REVIEW_COMMON_EXTENSION.md; published version DOI 10.1007/s00023-015-0401-5
(pagination not consulted). BGP statements from arXiv:0806.1036 (v1 rendering);
the review lane's record gives PDF pp. 76–87 for the same locators. Ringström
2009 book: EMS, DOI 10.4171/053; the correction note and errata are undated
author web documents on `people.kth.se/~hansr/` (accessed 2026-10-29).
