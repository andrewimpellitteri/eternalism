# Whole-bowtie Cauchy rigidity: red-team result

**Geometric lemma: PASS** for connected, smooth, time-oriented globally
hyperbolic spacetimes and an onto, time-orientation-preserving isometry of the
open exteriors `U_i=M_i\\J⁺(b_i)`. An explicit conformal-bump example shows
that this geometric fact alone does not force the ambient metrics to be
isometric. A dynamical rigidity conclusion requires a specified common theory
and Cauchy uniqueness in its actual regularity category.

## Counterexample-first check

The stronger statement “an isometry of the whole open bowtie by itself forces
the two ambient futures to be isometric” is false for arbitrary smooth
globally hyperbolic Lorentzian metrics. Let `M=R⁴` with Minkowski metric `η`
and marked event `b=(0,0)`. Choose a smooth nonzero function `ψ` supported in
a compact subset of `I⁺_η(b)` and set `g₁=e^{2ψ}η`, `g₀=η`. Conformal rescaling
preserves causal cones, so both spacetimes are connected and globally
hyperbolic and have the same `J⁺(b)`. The identity is an onto,
time-orientation-preserving isometry from `U₀` to `U₁`, since `ψ=0` there; it
also extends as the identity near `b`. For generic `ψ`, `g₁` has nonzero
curvature in its support, so the ambient metrics are not globally isometric
to Minkowski space. This is not a counterexample to the Cauchy-slice lemma:
the common past slice remains Cauchy in both. It shows why the subsequent
deterministic-field/MGHD premise is indispensable.

## Geometric lemma and proof

Let `(M_i,g_i)` be connected, smooth, time-oriented globally hyperbolic
spacetimes with events `b_i`, and let
`h:U₁→U₂` be an onto, time-orientation-preserving isometry, where
`U_i=M_i\\J⁺(b_i)`. Global hyperbolicity makes `J⁺(b_i)` closed, so `U_i` is
open. It is a past set: if `y∈U_i` and `x≤y`, then `x∈U_i`, since
`b_i≤x≤y` would otherwise put `y` in `J⁺(b_i)`.

By Bernal–Sánchez, choose a smooth Cauchy temporal function `t₁` on `M₁` and
shift it so `t₁(b₁)=0`. Set `Σ₁=t₁⁻¹(−1)`. This is a smooth spacelike Cauchy
hypersurface. Temporal monotonicity gives `t₁≥0` on `J⁺(b₁)`, so
`Σ₁⊂U₁`. Thus `Σ₂=h(Σ₁)` is a smooth spacelike hypersurface in `M₂`.

To prove that `Σ₂` is Cauchy, take any inextendible causal curve `c` in `M₂`.
Choose a Cauchy temporal function `t₂` shifted so `t₂(b₂)=0`. Its past end
has `t₂→−∞`; hence `c` has a past-inextendible tail in `{t₂<0}⊂U₂`. Because
`U₂` is a past set, the whole further-past tail stays in `U₂`. Pull it back by
`h` to a past-inextendible causal curve segment in `U₁`. It is
past-inextendible in `M₁`: an endpoint in `U₁` would extend the original tail
through `h`, while an endpoint `p∉U₁` would satisfy `b₁≤p≤x` for a tail point
`x∈U₁`, a contradiction.

Now use the **same original target curve** `c`, not an arbitrary future
continuation of its pullback. Since `J⁺(b₂)` is a future set, once `c` enters
`J⁺(b₂)` it cannot return to `U₂`. Thus the part of `c` beginning at its
past-inextendible tail and remaining in `U₂` is a maximal initial segment.
Pull back that exact segment by `h`. If its source-side future end is
inextendible in `M₁`, it is an inextendible causal curve and meets the Cauchy
surface `Σ₁`; the crossing lies on this pulled-back segment. If it has a
finite endpoint `p` in `M₁`, then `p` cannot lie in `U₁`: otherwise `h` and
the original target curve continue the same pullback segment. Hence
`p∈J⁺(b₁)`, so `t₁(p)≥0`. The past-inextendible end has `t₁→−∞`, and therefore
the pulled-back original segment crosses `t₁=−1` before reaching `p`, while
still in `U₁`. This proves that the original `c` meets `Σ₂`.

For the “at most once” direction, do **not** infer global acausality from
spacelikeness alone. `U₂` is causally convex: if the endpoints of an ambient
causal segment lie outside `J⁺(b₂)`, no intermediate point can lie in
`J⁺(b₂)`, since that set is a future set. Consequently any causal segment in
`M₂` between two points of `Σ₂⊂U₂` stays in `U₂`. Its pullback by `h` would be
a causal segment in `M₁` between two points of the Cauchy hypersurface
`Σ₁`, which is impossible unless the endpoints coincide. Thus `Σ₂` is
acausal and every inextendible causal curve meets it at most once. Therefore
`Σ₂` is Cauchy.

This continuation argument handles the point at which the pullback stops
being defined without changing curves: if the maximal target segment in `U₂`
ends at the excluded future set, its source endpoint is already to the future
of `Σ₁`, forcing a crossing on that same pulled-back segment before exit. If
the target segment never exits `U₂`, its pullback is future-inextendible in
the source and Cauchyness applies directly. No extension of `h` to the
bowtie boundary is used for the geometric lemma.

The connectedness assumption is compatible with the construction: a Cauchy
temporal splitting of connected `M₁` has connected level `Σ₁`, and every point
of `U₁` can be joined to its past intersection with `Σ₁` along a causal curve
contained in the past set. Hence `U₁` is connected. The same holds for `U₂`.
This is useful when comparing extensions of `h` in the dynamical corollary,
though the Cauchy proof itself only needs the displayed hypotheses.

## What follows dynamically, and what does not

The geometric result gives a common Cauchy surface, not equality of the
future metrics by causal geometry alone. Suppose additionally that both
spacetimes are maximal globally hyperbolic developments of the same complete
initial data for the same deterministic coupled field theory, in a category
where geometric Cauchy uniqueness is proved. If `h` preserves all matter
fields on `U₁`, then on a neighborhood of `Σ₁` it identifies the induced
metric, second fundamental form, matter data, and required normal derivatives.
Cauchy uniqueness then gives a global isometry of the developments extending
that initial-data identification. The exact coupled theory and regularity
category must be stated and sourced; the audited Choquet–Bruhat source proves
the vacuum result and describes the extension to hyperbolic matter systems as
conditional on their local existence and uniqueness. It is not by itself a
proof for every coupled theory, including the specific Einstein–scalar
regularity class in the scattering lane.

To conclude that the global isometry preserves the marked event `b` and an
observer tangent, one needs a boundary/germ premise. For example, require
that the whole-realm isometry extends continuously (smoothly when a tangent is
used) to `b₁`, maps it to `b₂`, and maps the specified tangent accordingly.
The Cauchy-development isometry agrees with `h` near `Σ₁`; since `U₁` is
connected, uniqueness of local isometries makes it agree with `h` throughout
`U₁`. A continuous extension to `b₁` then fixes the image of the marked
boundary point. Without this added premise, an isometry of the open sets says
nothing by itself about how the excluded events are paired, and global
development uniqueness alone need not preserve externally added marks.

For a bowtie realm that includes `b` and every event outside its strict future,
an isometry preserving the realm structure, fields, time orientation, and
marked event restricts to the hypothesized isometry of `U`. Under the stated
deterministic MGHD uniqueness assumptions and boundary/germ compatibility,
same-whole-bowtie/different-marked-future examples are excluded. This is a
conditional mathematical rigidity result. It does not establish that future
events exist, select an ontology, or make a causal past equal to a growing
block's whole existing realm; the coordinator's philosophical scope note
addresses those separate questions.

## Weaker robust corollary

Even if an alternate geometric argument were to fail, the weaker statement is
immediate: if an onto time-oriented isometry of the open bowties maps some
source Cauchy hypersurface `Σ₁⊂U₁` to a target Cauchy hypersurface, and fields
and full data are preserved, then the selected theory's ordinary Cauchy
uniqueness theorem applies. This weaker version must state Cauchyness of both
slices explicitly. The proof above establishes that condition from the
present smooth globally hyperbolic hypotheses, so this fallback is not needed
here.

## Scope and falsifiers

- The geometric lemma would fail if a target inextendible causal curve could
  avoid `U₂` to its past, or if the pullback's maximal future continuation
  could stop before crossing `Σ₁` without ending in `J⁺(b₁)`. A Cauchy temporal
  function and the endpoint cases above rule out both possibilities.
- The conformal-bump example falsifies any attempt to infer ambient metric
  isometry from the open-bowtie isometry without field equations and
  uniqueness.
- The deterministic corollary fails outside a uniqueness category, for
  stochastic/multivalued evolution, or when matter fields / normal data are
  not matched.
- Marked future observables do not follow from unmarked MGHD uniqueness unless
  the isometry matches the marked event and tangent.

No novelty claim is made. No specific coupled-field theorem is claimed beyond
the sourced vacuum instance and the explicitly conditional formulation.
