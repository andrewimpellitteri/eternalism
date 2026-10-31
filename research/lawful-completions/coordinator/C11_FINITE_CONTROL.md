# Finite scalar readouts at fixed incoming mass in a C¹,¹ category

> **Later 30 October smoothness repair:**
> [SMOOTH_FINITE_CONTROL.md](SMOOTH_FINITE_CONTROL.md) upgrades the category
> of the selected compact-profile limits to smooth, complete MGHDs using
> a separate localized proof and checked completeness/inextendibility inputs.
> The continuity/degree assembly now has a separate
> [bounded accepted review](FINITE_CONTROL_ACCEPTANCE.md), 31 October.
> The native regularity audits and finite-control audit retain their scopes.
>
> **Energy timing:** the fixed total incoming mass includes the compensating
> tail after the complete readout window. Incoming mass by each reading
> time is not fixed. See [philosophical scope](PHILOSOPHICAL_SCOPE.md).

30 October 2026. Coordinator proof assembly and direct audit after the GLM
quota stop. **Finite-control chain internally reviewed, 31 October.**
The [acceptance disposition](FINITE_CONTROL_ACCEPTANCE.md) records repairs
and the external inputs retained. This finite-order proof alone gives no
smooth-MGHD, mathematical priority or ontological conclusion.

## 1. Exact proposed theorem and quantifier order

Fix N≥1 and 0<T₁<⋯<T_N. Subject to the external LOY inputs specified in
§2, there are constants E_*>0 and c>0 such that, for every 0<E<E_* and
every y∈R^N with |y|<c√E, there is a time-oriented, spherically symmetric
four-dimensional model (M,g,φ,b,U) with:

1. M=R×R³, g and φ locally C¹,¹ in the constructed Cartesian atlas;
   the Einstein–real-massless-scalar equations hold a.e./distributionally.
2. The entire pointed causal past J⁻(b), including its field and launch
   tangent, is exactly the same Minkowski past with φ=0 for all targets.
3. The actual iterated incoming Hawking-mass boundary limit is E:

       E = lim_(V→∞) lim_(u→−∞) m(u,V).

4. The unique central future unit geodesic γ with γ(0)=b, γ′(0)=U
   exists for all proper times and obeys φ(γ(T_j))−φ(b)=y_j.

The constants depend on the finite sample schedule and the fixed profile
basis. This does not give one uniform E_* or one nonzero reading resolution
for all N. Incoming mass is not asserted to be ADM mass. These are centered
field models; bare-metric nonisometry is a different question.

The construction also gives Cauchy time slices in this C¹,¹ model (§7).
It does not identify the spacetime as a smooth maximal development.

## 2. External inputs and what has actually been reread

Primary [Luk–Oh–Yang v1](https://arxiv.org/html/1605.03893v1), 12 May 2016:

| Input | Exact locus | Scope consumed |
|---|---|---|
| Normalized finite-cone existence/uniqueness | Theorem 1.1; §2.1 Definition 2.1 and paragraph after (2.5) | Unique global reduced C¹ characteristic solution |
| Uniform geometric and low derivative bounds | (1.7)–(1.9), Remark 1.2 | Constants independent of cone vertex |
| Higher compactness budget | Proposition 3.18, (3.44)–(3.47); §4 before (4.1) | r and p=rφ through third order, φ and m through second on compact triangles |
| Incoming recovery and cubic error | §4 unnumbered estimates following (4.1) | Uniform in cone vertex; take compact limit before u→−∞ |

These selected statements/passages were reread directly on 30 October.
Local wellposedness and the u-side higher bounds have omitted/sketched
proofs in the source; this note does not independently reproduce them.
The §4 small first-r-derivative typo is bypassed using (1.8), λ≤1/2 and
Proposition 3.18. The accepted source audit plus the exact mixed-φ estimate
in [AXIS_C11_RECONSTRUCTION.md](AXIS_C11_RECONSTRUCTION.md) supply the
axis-inclusive budget. Mixed third derivatives of p follow by differentiating
p_uv=r_uvφ once; no third-φ bound is required for that step.

The characteristic uniqueness is an external theorem, not inferred from
compactness. No uniqueness of a past-null-infinity scattering solution is
used or claimed.

## 3. Admissible compact profile family

Set the launch coordinate t_b=0. Choose 0<A<T₁, smooth compact F_k with
pairwise disjoint supports around T_k and F_k(T_j)=δ_kj, and smooth nonzero
G supported after 2T_N+1. Choose β₀>0 and a closed ball |x|≤ρ small enough
that

    β(x)=√[β₀²−Σ_k x_k² ||F_k||²₂ / ||G||²₂]

is smooth and bounded away from zero there. Define

    Φ_(ε,x)=ε f_x,       f_x=Σ_k x_kF_k+β(x)G.

Disjoint supports give ||Φ_(ε,x)||²₂=ε²β₀²||G||²₂ exactly. Every profile
is smooth; x↦Φ_(ε,x) is continuous in C² and in each higher fixed norm.
Let [A,B] contain all supports and L=B−A>0. If |f_x|≤M₀ uniformly,

    ∫_u^v |Φ_(ε,x)| ≤ εM₀ min(v−u,L)
                     ≤ εM₀ L^γ (v−u)^(1−γ),   0<γ<1.

Together with a common C¹ bound this verifies (1.7) with smallness parameter
C₀ε, where C₀ is fixed independently of x and cone vertex. The source's
second-data-derivative parameter is bounded by 4ε sup_x||f_x″||∞. Choose
C₀ε below both source thresholds. No unproved uniformity over arbitrary
smooth data is being substituted for this one compact family.

## 4. Direct exact-flat-wedge lemma

On a finite cone u=u₀<A, consider u₀≤u≤v<A. Put p=rφ. Its equation is

    p_uv=Vp,       V=r_uv/r=2mνλ/[(1−μ)r³].

The first weighted mass bound m=O(r³) and geometric nondegeneracy make V
bounded on each such closed finite triangle. V can be assigned any bounded
axis value for the integral argument; no pointwise curvature is needed.
The incoming data give p_v(u₀,v)=0, and the regular axis gives p(u,u)=0.
Therefore

    p(u,v)=∫_u^v ∫_(u₀)^u V(s,w)p(s,w) ds dw.

Fix V₀<A and define

    M(U)=sup{|p(s,w)|:u₀≤s≤min(U,w), w≤V₀}.

The integral identity implies M(U)≤C(V₀−u₀)∫_(u₀)^U M(s)ds. To see the
supremum step, first apply the identity at any (u′,v′) in the defining
set with u′≤U; its inner integrand obeys |p(s,w)|≤M(s), and enlarging the
outer length to V₀−u₀ and the inner upper limit to U gives this bound.
M is bounded and nonnegative, so integral Gronwall with zero forcing gives
M=0. Hence p=φ=0. The mass equation and m(u,u)=0 give m=0; then r_uv=0,
λ=1/2 from the initial gauge, and r=(v−u)/2 from r(u,u)=0. Thus the
four-metric is exactly Minkowski on v<A. Constants need not be uniform in
u₀ here: every approximant is exactly flat and that identity passes to
every compact limit.

In four dimensions a future causal curve has t′≥|ρ′|, since
g=−Fdt²+Fdρ²+r²dσ² and F>0. Thus v=t+ρ cannot decrease, including across
the regular center by continuity. Every event in J⁻(b) has v≤0<A and lies
in the flat wedge. Conversely the Minkowski radial causal paths from all
points v≤0 to b stay in that wedge. The full causal past is therefore the
same pointed Minkowski past, not merely a finite segment of it.

## 5. Continuity and degree before taking the scattering limit

For each fixed u_n→−∞, let H_n(x) be the N scalar readings at the prescribed
central proper times. The finite-cone compactness/uniqueness proof in
[COMPACTNESS_CONTINUITY_REPAIR.md](COMPACTNESS_CONTINUITY_REPAIR.md) applies
to this smooth family: every sequence x_j→x has a compactly convergent
subsequence in r,p∈C² and φ,m∈C¹ on closed exhaustion triangles. Initial
gauge/data and axis conditions pass to the limit. Off-axis equations pass
ordinarily; the weighted bounds control the axis extension. The resulting
global finite-cone solution is in Definition 2.1's C¹ uniqueness class, so
it is the solution at x. Every subsequential limit is that same solution,
which proves continuity of the whole sequence in each compact norm.

The central clock τ_x(t)=∫₀^t2λ_x(s,s)ds has τ′≥2/3. Thus its inverse on
[0,T_N] is evaluated in the common interval [0,2T_N+1], and uniform clock
convergence implies uniform inverse convergence with factor at most 3/2.
This proves each H_n continuous. Neither continuity uniform in n nor a
selected continuous global scattering map is required.

[CUBIC_TRACE.md](CUBIC_TRACE.md) uses the explicit §4 estimates and the
uniform profile C¹ bound to obtain

    sup_(n,|x|≤ρ) |ε⁻¹H_n(x)−x| ≤ Cε².

At |x|=ρ, |z|<ρ/2 and 0≤s≤1, the norm of
x+s(ε⁻¹H_n(x)−x)−z is at least ρ−Cε²−|z|>0 when Cε²<ρ/2.
Brouwer degree equals that of x−z, namely one. Hence a root x_n exists
with H_n(x_n)=εz for each n. This is an existence argument, not an
intervention or differentiability statement.

## 6. The two limits and the actual mass

For a fixed target z choose a subsequence x_n→x_* in the parameter ball.
Profiles then converge smoothly. All source constants remain uniform in x
and u_n, so the same diagonal compactness proof gives a global reduced
solution on the entire quotient. First pass n→∞ at fixed (u,v) in the
source's two §4 remainder estimates. Only then take u→−∞. This recovers
λ→1/2 and λ⁻¹p_v→Φ_(ε,x_*)(v); compact convergence alone would not do so.
Clock/inverse/scalar convergence on the fixed readout interval preserves
the exact root equations. Different targets may use different subsequences.

The direct flat-wedge lemma fixes m(u,A)=0. For any fixed finite V>A the
exact mass flux identity is

    m(u,V)=∫_A^V [λ(1−μ)/2](λ⁻¹p_v−φ)² dv.

As u→−∞ on this finite v interval, r→∞ uniformly, φ,μ→0 uniformly,
λ→1/2 and λ⁻¹p_v→Φ uniformly. The integrand tends uniformly to Φ²/4.
Then let V→∞. This proves E=||Φ||²₂/4 for the selected global solution,
using [INCOMING_MASS.md](INCOMING_MASS.md) and its accepted bounded review.
There is no exchange of the two limits or moving-cone mass identification.

Set K=β₀||G||₂. Then E=ε²K²/4, and the target ball has radius ερ/2=
(ρ/K)√E. Choose ε_* to satisfy the source and degree inequalities, set
E_*=ε_*²K²/4 and c=ρ/K. This proves the quantifier order in §1.

## 7. Four-dimensional category and the Cauchy slices

The internally reviewed axis reconstruction applies to each selected
subsequence: g,φ are C¹,¹, with unique geodesics and the weak field equations.
At the center the clock is proper time and τ′≥2/3 on the whole real axis,
so the central geodesic has unbounded proper time in both directions.

There is also a direct global cone bound. Since λ∈[1/3,1/2],
−ν∈[1/6,2/3], and 1−μ∈[1/2,1], the quotient coefficients satisfy

    2/9 ≤ F=−4νλ/(1−μ) ≤ 8/3,
    4/9 ≤ A=(r/ρ)² ≤ 1.

The spatial Cartesian eigenvalues are F radially and A tangentially.
Consequently any future causal curve parametrized by t obeys
|dx/dt|≤√12. If an inextendible causal curve had a finite endpoint in t,
its spatial coordinates would be Cauchy and have a finite limit. One
could add that endpoint and extend along the timelike coordinate line,
contradicting inextendibility. Thus every such curve crosses each t-slice
exactly once. This is the Cauchy-surface property in the constructed
low-regularity model; it is not a smooth MGHD or maximality proof.

## 8. Two consequences, and their philosophical limits

For a fixed finite N choose δ=c√E/(2√N). Every vector δσ, σ∈{−1,+1}^N,
lies inside the target ball. Thus all 2^N truth patterns of

    φ(γ(T_j))−φ(b)>0

are realizable at the same incoming mass and the same complete causal past.
This is finite Boolean independence, with N-dependent thresholds and
amplitudes. It supplies no infinite-history control or detector-resolution
claim, and does not exchange ∀N∃E_* with ∃E_*∀N.

For N≥2, the open target ball and the C¹ central scalar trace meet the
hypotheses of [NONISOMETRY_LEMMA.md](NONISOMETRY_LEMMA.md). Its accepted
bounded measure argument implies uncountably many centered,
field-preserving isometry classes, using this now internally reviewed
interpolation theorem. Re-marking a countable set of centered histories
cannot cover the ball. No bare-metric nonisometry is inferred.

Philosophically the target is exact non-supervenience of those finite
future readouts on the causal past plus this conserved boundary datum.
It does not give identical full Cauchy data: the spacelike exterior may
differ. It does not give identical whole bow-tie realms, all admitted
present facts, or later-grounded future truths. Deterministic evolution
from complete Cauchy data and rival temporal ontologies remain compatible
with this construction. A separate bridge is needed to identify variation
across lawful completions with ontic openness or nonexistence of the future.

## 9. Current review disposition

The resumed GLM review supplied an O1–O13 audit. After direct inspection,
source checks and repairs to its arithmetic diagnostics, the coordinator
accepted its bounded finite-control scope on 31 October; see
[the disposition](FINITE_CONTROL_ACCEPTANCE.md). The exact nearest-predecessor
comparison remains open (the control/degree argument may be a familiar
scattering corollary). The
separate smoothness bridge is now supplied in SMOOTHNESS_BOOTSTRAP.md;
its precise category upgrade and external inputs are recorded in
SMOOTH_FINITE_CONTROL.md. The finite-order proof above does not itself
establish those stronger conclusions.
