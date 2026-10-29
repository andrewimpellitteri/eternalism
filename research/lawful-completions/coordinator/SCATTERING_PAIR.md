# Candidate exact matched-past pair from a global scalar scattering solution

28 October 2026. Derived baseline, awaiting independent review. No novelty
claim. This applies the global weak-radiation family inspected in
collapse-extension/SCATTERING_FOLLOWUP.md, rather than extending the strong
1991 cone-collapse solution. The two routes must not be identified.

## External input and exact scope

Luk–Oh–Yang, arXiv1605.03893v1, Theorem1.7 and §§2.1,4,6, constructs a
regular spherical Einstein–massless-scalar solution on the full quotient
Q={(u,v):u≤v, u,v finite}, with regular centre u=v, past-null-infinity
profile Φ, and two-sided causal geodesic completeness. Their field
normalization is Ric_ab=2∂_aφ∂_bφ, as opposed to 8π in Christodoulou1991;
constant scalar rescaling relates the conventions. In these coordinates

  g=−Ω²du dv+r²dΩ₂²,   Ψ=rφ,
  Ψ_uv=KΨ,   K=r_uv/r.

Choose nonzero smooth compactly supported sufficiently small Φ, vanishing
for v<v₀. The approximating-cone construction and local uniqueness give
exact Minkowski geometry and φ=0 on v<v₀; the selected extension-lane audit
states this deduction explicitly. These are primary-source premises for
this candidate, not an independent reproof of global scattering existence.

## 1. The causal-past match is global in this family

Choose b on the regular centre with u_b=v_b=t_b<v₀. Future causal curves
have nondecreasing u,v (including at the regular centre by continuation).
The entire past of b lies in v≤t_b<v₀, hence in the exactly flat region.
Under its Minkowski identification, every past-directed curve from b also
stays in that region. Thus the full chronological pasts match in both
directions, not merely by a map of a finite diamond. The closed past and
marked germ at b lie strictly inside the same flat wedge as well.
This statement needs the source's full regular quotient, not only a
truncated outgoing-cone solution.

## 2. Global hyperbolicity from the regular full quotient

Let t=(u+v)/2 and ρ=(v−u)/2. Away from the centre ∇t is timelike, and t
extends as a temporal function across the regular centre. On any future
causal curve parametrized by t, 0≤du/dt,dv/dt≤2, so |dρ/dt|≤1. If an
inextendible causal curve had a finite upper t endpoint, its u,v coordinates
would be bounded, starting from any one point on the curve. The angular
sphere is compact, and the regular centre fills in ρ=0. Thus the curve
would remain in a compact subset of the smooth spacetime. Strong causality
from the temporal function excludes total imprisonment of an inextendible
causal curve in such a compact region. Equivalently, local extension at
its accumulated points contradicts inextendibility. Reverse time gives
t→−∞ at the other end. Every t=constant slice is consequently Cauchy;
its topology is R³. This is an elementary deduction from the full regular
quotient, not a general implication of geodesic completeness alone.

Spacelike completeness additionally follows if source bounds on Ω give
a uniform positive lower bound for the radial induced length element.
It is not needed for the Cauchy/topology assertion itself.

Candidate maximality argument (also for review): let Σ be a smooth t slice
and suppose the solution embeds in a larger GH development N of the same
Σ data. In N, any q to the future of Σ is reached by a maximizing timelike
geodesic normal to Σ (the usual GH existence theorem for distance from a
Cauchy hypersurface); similarly in the past. Its initial normal datum is
in our solution, where the timelike geodesic exists through every finite
proper time by completeness. Uniqueness of the geodesic initial-value
problem in N identifies the two geodesics, forcing q into the image. Thus
there is no larger GH development. This applies in a common regularity
category in which these geodesic and coupled Cauchy results hold; do not
assert it for an arbitrary nonsmooth extension. The source's regularity at
the centre and compatibility with the chosen MGHD category need checking.

## 3. A nontrivial profile cannot remain invisible at the centre forever

This is a direct 1+1 hyperbolic uniqueness argument, conditional on source
regularity at the centre. In t,ρ coordinates the reduced equation is

  Ψ_ρρ−Ψ_tt = −4KΨ.

Regularity gives Ψ(t,0)=0, and ∂ρΨ(t,0)=∂ρr(t,0)φ(t,0). Suppose, for a
contradiction, that φ(t,0)=0 for every real t. Then Ψ and its ρ derivative
both vanish on ρ=0. Treat ρ as the evolution variable of this linear 1+1
wave equation with coefficient K taken from the given solution. On each
finite sideways characteristic triangle, K is bounded: at the regular
centre m=O(r³), so K=[2m r_u r_v]/[(1−2m/r)r³] extends regularly; away from
it smoothness suffices. Zero Cauchy data on the entire t-axis force Ψ=0
on every such triangle by the standard energy estimate/Volterra uniqueness.
This uses the special two-variable radial reduction; it is not a general
claim about timelike Cauchy problems in higher dimensions.

For specificity, d'Alembert's source formula with zero data gives

  Ψ(ρ,t)=−2∫₀^ρ∫_{t−(ρ−s)}^{t+(ρ−s)}K(s,z)Ψ(s,z) dz ds.

Iteration on a compact triangle gives a convergent Volterra bound with
zero initial term, hence Ψ=0. Since every finite (ρ,t) is in a triangle
based on a finite segment of ρ=0, Ψ vanishes globally. This contradicts
the nonzero prescribed radiation limit Φ. Therefore φ(t,0) is nonzero at
some finite centre event. The exact flat wedge has φ(t,0)=0 before v₀,
so smoothness implies a finite later point where its centre proper-time
derivative is nonzero.

## 4. A future relational curvature outcome differs

The centre is a timelike geodesic by spherical symmetry. Mark b and its
unit tangent, and choose the finite proper time T at a point where
∂τφ≠0 established above. Both models have that launched segment through T
by their causal geodesic completeness. Define

  Q(T)=Ric_ab(γ(T)) dotγ^a(T) dotγ^b(T).

In the scattering solution Q(T)=2(∂τφ)²>0. In Minkowski with constant
scalar Q(T)=0. This is a diffeomorphism-invariant, observer-marked curvature
functional; it does not depend on a scalar sign convention, an additive
scalar shift, or a coordinate identification of future events. T is chosen
after establishing existence of a varying point, not arbitrarily prescribed
in advance. This proves only existence of one separated reading if the
candidate premises and uniqueness argument pass review. It does not prove
control of a list of prescribed times, a self-gravitating detector, or
fixed equal incoming energy (the Minkowski member has zero incoming energy).

## Remaining checks before any B-level claim

- Check source regularity at the centre and inherited full-quotient bounds.
- Independently audit the sideways uniqueness argument; it is special to
  spherical reduction and assumes local boundedness of K at ρ=0.
- Audit the GH argument; do not infer it solely from causal completeness.
- Independently audit the normal-geodesic maximality argument in §2 and
  the compatibility of source smoothness with the coupled MGHD category.
- Prior-art verdict: a corollary of established spherical scattering
  existence is likely baseline work, not frontier novelty. Keep C-level
  fixed-energy finite-control conjecture separate in NEXT_CANDIDATE.md.
