# Screening repair review

## Counterexample-first result

The repaired claims survive at their stated scope. Two important overclaims fail: exact agreement on a dense readout set is not a finite/noisy-data result, and vacuum common-GHD uniqueness does not supply matter-field matching or equality of observer lifetimes. The latter limits are detailed in [REVIEW_COMMON_EXTENSION.md](REVIEW_COMMON_EXTENSION.md).

## Smooth screening characterization

For the repaired definition—smooth spacelike Cauchy hypersurfaces disjoint from `J⁺(b)\{b}`—the characterization is sound:

`R ⊂ B_b` screens every such slice iff `P_b ⊂ R`, where `P_b=J⁻(J⁺(b))\(J⁺(b)\{b})=W_b∪{b}`.

For sufficiency, each past-inextendible causal curve from `z∈J⁺(b)` crosses the Cauchy slice at `y≤z`, outside the forbidden strict future. Thus `y∈P_b`. For necessity, choose `x∈P_b` and witness `z∈J⁺(b)` with `x≤z`. If `x=b`, use a smooth temporal level through `b`; if `x≺b` (distinct causal precedence, including null), use one through `x`, which lies strictly below `b` in temporal value; if `x` is spacelike to `b`, extend the finite acausal set `{x,b}` to a smooth spacelike Cauchy surface. The source supports this last case, including disconnected compact acausal sets. A past causal curve from `z` through `x`, continued to the past, crosses that acausal surface only at `x`. Omitting `x` from `R` therefore violates screening. This avoids the earlier null-containing C⁰-surface convention issue.

## Fixed-background field determination

Let `L` be one fixed smooth normally hyperbolic scalar operator on one fixed smooth globally hyperbolic `(M,g)`. For smooth global solutions `Lu=Lv=0`, exact equality on `W_b` implies equality on `J⁺(b)`: set `w=u-v`; on `K=Σ∩W_b`, for an earlier smooth Cauchy slice `Σ`, both `w` and its normal derivative vanish. Screening gives `J⁺(b)⊂D⁺(K)`. Apply arbitrary-solution homogeneous Cauchy uniqueness to `w` restricted to the open GH domain `D(K)` with Cauchy surface `K`.

Bär–Ginoux–Pfäffle Corollary 3.2.4 explicitly states uniqueness for **any** smooth homogeneous solution with zero value and normal derivative on a smooth spacelike Cauchy surface; Proposition 3.2.5 gives the local uniqueness form. This is the needed statement, unlike relying only on their compactly-supported-data global existence theorem. The application still requires the standard domain fact that the chosen full `D(K)` is open globally hyperbolic and `K` is Cauchy there.

If exact values agree on a countable dense subset of `W_b`, continuity first gives equality throughout `W_b`, so the same proof applies. This depends on exact values, continuity, a common spacetime, and the same operator; it says nothing about finite-precision observations or distinct backgrounds/operators. Counterexample to dropping the shared-operator condition: in Minkowski space, `u≡1` solves `□u=0`; for nonzero smooth compactly supported `V` in the strict future, solve `(□+V)v=0` with `u`'s Cauchy data before `supp(V)`. Finite propagation gives `v=u` outside the causal future of the support, while `u` fails the second equation on `supp(V)`. Thus agreement in the past realm alone does not identify solutions of different equations.

## Scope

The exact geometric screening boundary and fixed-background smooth test-field determination are distinct results. The common-extension proposal is separately conditional and vacuum-geometric unless a coupled common-development theorem is supplied. No full coupled-GR, low-regularity scattering, whole-future, observer-lifetime, or novelty claim is established here.

## Optional completeness strengthening

The coordinator's stronger corollary passes conditionally, and must remain explicitly conditional. Once the main common-extension proof supplies a smooth local transition at the marks matching the observer germs, global hyperbolicity gives a causal geodesic from `b_i` to every `q_i∈J⁺(b_i)` (Avez–Seifert). Transfer its initial causal tangent through the local transition. If every future causal geodesic from each mark is complete, both corresponding geodesics exist to the endpoint parameter; their images in the common development agree by geodesic IVP uniqueness. This yields `F_1(J⁺(b_1))⊂F_2(J⁺(b_2))`; reverse the roles for equality. The transition between embedding images then gives an onto isometry of the marked causal futures. The same reasoning using timelike geodesics yields the chronological-future version under completeness of every future timelike geodesic from each mark. Neither completeness assumption follows from realm data or the earlier finite-overlap theorem. The GHD/domain and vacuum-versus-matter gates above remain in force.
