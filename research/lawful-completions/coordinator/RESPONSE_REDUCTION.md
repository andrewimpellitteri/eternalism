# Conditional reduction of future control to three analytic lemmas

28 October 2026. Direct calculation; no existence, differentiability or
novelty claim. Use the exact source radiation normalization, not the 1991
cone derivative ψ. This sharpens NEXT_CANDIDATE.md.

## Linear response and proper time

In the Minkowski radial linearization, put Ψ=rφ, r=(v−u)/2,
Ψ=f(v)−f(u). Incoming profile Φ=2∂vΨ=2f′. The regular centre limit is
φ(t,0)=2f′(t)=Φ(t). Thus the first variation of a central field reading
at proper time T from a flat marked event b is F(t_b+T) for incoming
variation F, PROVIDED a differentiable exact scattering-to-reading map
exists. The normalization factor is one for Φ, not two.

At a baseline with zero scalar in the entire causal domain of those
readings, the endpoint-motion term is zero: dφ₀(deltaγ)=0. Therefore proper-
time/geodesic variation does not contaminate this first variation. A
causally later nonzero tail does not change that local baseline if the
exact scattering construction has the needed matching/selection property.

Choose N compact smooth early profiles F_k with
F_k(t_b+T_j)=δ_kj, and a later disjoint profile G. If causality plus C1
profile dependence hold, the reading map in early amplitudes α has identity
Jacobian at α=0, even about a nonzero tail baseline. This is a conditional
rank calculation, not an invocation of existence from a formal linearization.

## Exact energy compensation, conditional on the flux identity

Suppose the energy lane proves E(Φ)=c∫Φ² in the source normalization, with
c>0, and exact causal matching of the early readings. For disjoint early
supports and late G, Φ=Σα_kF_k+βG has

  E=cΣα_k²||F_k||²+cβ²||G||².

At β₀>0, fixing E₀=cβ₀²||G||² is accomplished exactly by

  β(α)=sqrt(β₀²−Σα_k²||F_k||²/||G||²)

for sufficiently small α. This variation is O(|α|²) around β₀, and the late
pulse does not affect early readings under the causal-matching premise.
The inverse-function theorem would then give a neighborhood of N signed
scalar readings at fixed energy, once the exact map is proven C1. No claim
that the source already proves this profile map or exact energy identity.

Scalar sign/shift symmetries do not need to obstruct physical formulations:
one may instead use [φ(T)−φ(b)]² near a small baseline where every difference
is nonzero and recheck rank; or use centre derivative readings and the
Ricci contraction 2(∂τφ)² near nonzero derivative baselines. Those variants
require the corresponding field/derivative regularity and response map.

The source's Ω²>2/9 implies dτ/dt≥sqrt(2)/3 on the centre. Hence a tail
supported after v_tail>t_b+(3/sqrt(2))T_N is safely after every central
reading through proper time T_N, within a family retaining that bound.
The coordinate choice of the tail is a construction tool; the readings
remain proper-time scalars. One still needs exact equality under changing
the late data, not merely finite propagation of an unrelated Cauchy problem.

## Ambition beyond the finite-dimensional checkpoint

Finite N plus a standard inverse-function argument might be only a routine
corollary of an existing smooth scattering map. Kill novelty if so. The
stronger question is whether an entire small future record on a finite
proper-time interval can be prescribed while the entire past and total
incoming energy remain fixed. This is a function-space control/range
problem, not a finite toy sampling claim.

It cannot be promoted automatically: nonlinear time reparametrization and
trace maps may lose derivatives; a Banach inverse-function theorem may fail
in the desired norms even if every finite matrix has full rank. Required
output is an exact range theorem or a named obstruction with compatible
function spaces. Do not replace it by a finite interpolation experiment.
