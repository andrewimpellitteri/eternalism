# Small potential changes can remove actual future determination

27 October 2026. Coordinator derivation, submitted for independent review.
This is a bounded analytic extension, not an integrated manuscript result or
a novelty claim. Prior sources and remaining access limitations are in GATES.md.

## 1. What is stronger than the earlier robustness submission

Failure of the identity ψ(t+π,−X)=−ψ(t,X) on arbitrary solutions does not
show that an event formerly fixed by past data becomes unfixed. To show actual
loss of determination one needs two solutions agreeing throughout the specified
past but disagreeing at the specified target. The construction below provides
that pair, with the same light cones and an arbitrarily small constant change
to the rescaled potential.

The target is in the observer's **timelike future**, inside the dust strip,
not just at a spacelike antipodal echo and not at the excluded crunch boundary.

## 2. Setup and statement

Let E=R×S³ be the unit Einstein cylinder with metric −dt²+dΩ³² and
Λ²=−Δ_S³+1. Its positive eigenfrequencies are k=n+1, n=0,1,... . On the
strip M=(0,2π)×S³ consider unrestricted smooth solutions of

    ∂t²ψδ + (Λ²+δ)ψδ = 0.                         (1)

Define Fδ(b) by agreement of any two solutions on I_s^-(b), as in the paper.
The spacetime and input region do not vary with δ. Fix b=(τ,Y), 0<τ<π,
and a target

    x_s=(2π−s,Y),       0<s≤τ.                   (2)

**Proposition (conditional only on the standard smooth Cauchy theory and the
unperturbed result already proved in the manuscript).** The target x_s belongs
to F0(b). For a fixed nonzero smooth g≥0 with support disjoint from the closed
cap C=bar B(Y,τ), choose the solutions with data ψδ(0)=0, ∂tψδ(0)=g.
There is ε>0 such that, for every 0<|δ|<ε, these solutions vanish on
I_s^-(b) but are nonzero at x_s. Consequently x_s is not in Fδ(b).

The same g and target work on both sides of δ=0. In particular the conclusion
holds for sufficiently small positive δ. The size of ε is not asserted to be
uniform over all data or targets, and no complete formula for Fδ is claimed.

## 3. Proof

### A. Identical zero data throughout the standpoint's past

Choose the support of g compactly inside S³\C; this is possible since τ<π.
There is a distance ρ0>τ from Y to this support. For z=(t,Z) in I_s^-(b),
0<t<τ and d(Z,Y)<τ−t. Any point W on the η=0 slice influencing z must have
d(W,Z)≤t and therefore d(W,Y)<τ. Its initial data are zero. The finite
propagation theorem for (1) is independent of the zero-order constant δ.
Thus ψδ vanishes on the entire I_s^-(b), for every δ under consideration.

This uses full smooth solutions, not a finite mode truncation. Individual
spectral projections need not vanish on the past; their cancellation matters.

### B. A positive resolvent coefficient

Put h=Λ^(-2)g. The integral kernel of (−Δ+1)^(-1) on the unit S³ is

    G(r) = (π−r)/(4π² sin r),       0<r<π,
    G(π) = 1/(4π²).                              (3)

To check (3), for radial H the identity

    (−Δ+1)H = −(sin r H)'' / sin r

shows that G solves the homogeneous equation away from its pole. The kernel
is smooth at the antipode since (π−r)/sin r has an even smooth expansion
there. Near r=0 it is 1/(4πr)+O(1), the correctly normalized three-dimensional
fundamental singularity. Integrating over a small sphere gives unit flux.
Invertibility of −Δ+1 on the compact sphere then identifies the resolvent.

G is strictly positive, so

    h(Y) = integral_S³ G(d(Y,Z))g(Z) dV(Z) > 0.   (4)

No claim that local agreement forces the spatial mean to vanish is used;
that claim in the earlier GLM submission was false.

### C. Differentiate the exact propagator

For the fixed initial velocity g,

    ψδ(t) = Sδ(t)g,
    Sδ(t) = sin(t sqrt(Λ²+δ))/sqrt(Λ²+δ),
    Cδ(t) = cos(t sqrt(Λ²+δ)).

These operator functions are differentiable in δ near zero on smooth data,
uniformly on compact time intervals in every Sobolev norm. This follows
directly by differentiating their spectral multipliers: k≥1, and the smooth
data have faster-than-polynomial spectral decay. Taking sufficiently high
Sobolev order also justifies point evaluation of the derivative.

At T=2π the integer spectrum gives

    S0(T)=0,       C0(T)=identity,
    ∂δ Sδ(T)|0 = π Λ^(-2),
    ∂δ Cδ(T)|0 = 0.                              (5)

Differentiate the exact sine subtraction identity

    Sδ(T−s) = Sδ(T) Cδ(s) − Cδ(T) Sδ(s).

For w(t)=∂δ ψδ(t)|0 this yields

    w(T−s) = π C0(s)h − (∂δ Sδ(s)|0)g.          (6)

The second term in (6) is zero at Y: finite propagation gives
Sδ(s)g(Y)=0 for |s|<ρ0, for every δ, so its δ derivative is zero there.
The first term at Y is πh(Y). Indeed, Λ²h=g vanishes on B(Y,ρ0), so the
time-independent field h solves the unperturbed wave equation locally there.
Uniqueness in the double cone based on that ball gives C0(s)h(Y)=h(Y)
for |s|<ρ0. Our target satisfies s≤τ<ρ0. Thus

    w(2π−s,Y) = πh(Y) > 0.                      (7)

### D. Actual loss at an interior timelike-future event

The unperturbed value ψ0(2π−s,Y) is zero: integer-frequency periodicity gives
S0(2π−s)g=−S0(s)g, whose value at Y vanishes by finite propagation.
More generally, the closed three-diamond theorem in the paper places x_s
in F0(b), including s=τ by continuity. Also 2π−s>τ because τ<π, so x_s
is in I^+(b), and 0<2π−s<2π places it inside M.

Equation (7) gives the local expansion

    ψδ(x_s) = δ πh(Y) + o(δ).                   (8)

For all sufficiently small nonzero δ this is nonzero. The pair ψδ and zero
therefore agrees on I_s^-(b) but disagrees at x_s, proving x_s∉Fδ(b).
Together with x_s∈F0(b), this proves the proposition.

## 4. Physical scope: what the parameter means

On the full Einstein static metric, positive δ is an additional ordinary
mass-squared in the conformally coupled scalar equation. But on the closed
dust metric g_dust=a(t)² g_E, writing φδ=ψδ/a gives

    (Box_g − R_g/6 − δ/a(t)²) φδ = 0.            (9)

The potential δ/a² is smooth on the open dust strip. It is not a constant
physical mass, and it becomes large near the excluded cosmological endpoints.
On any compact substrip it tends smoothly to zero with δ. An ordinary
constant physical mass m on dust would instead give the rescaled potential
m²a(t)²; (5)–(8) do not prove the same result for that different perturbation.
Section 6 supplies a separate Duhamel argument for ordinary physical mass.

Nor does this establish a result about interactions, QCD, quantization, or
backreaction. The spacetime is fixed. The geometric domain Det is unchanged
and its sufficient guarantee remains valid. What changes is the extra
law-relative determination beyond that guarantee.

## 5. Interpretation and limitations

The extra late-time determination is **not robust as an exact equality
constraint** in the named family: arbitrarily small positive potential shifts
can remove specified fixed future events. This is stronger than failure of
the all-solution echo identity. It is weaker than an exact description of the
new fixed region or proof that all extra determination disappears.

There is no discontinuity claim about measured field amplitudes: (8) is small
as δ tends to zero. A sharp exact-fixing predicate can change while solutions
depend continuously on the equation. Measurement precision and approximate
prediction require separate definitions. The unbounded amplitude rescaling of
the unrestricted smooth solution class also matters for any proposed error
bound.

The argument uses classical spectral facts and causal propagation. Its
formulation may be useful for this project's interpretation of determination,
but global priority is unverified. Known tails and loss of Huygens behavior
must not be presented as new discoveries.

## 6. Ordinary constant physical mass on dust: a separate argument

The distinction in section 4 is substantive, but the correct dust mass
perturbation also admits a positive first-variation argument. This section
does not infer it from a constant rescaled potential.

Take the ordinary conformally coupled massive equation on the same fixed dust
metric,

    (Box_g − R_g/6 − m²)φ_m = 0.

Put λ=m², ψλ=aφ_m, a(t)=(a_m/2)(1−cos t). The rescaled equation is

    ψλ_tt + [Λ² + λ q(t)]ψλ = 0,
    q(t)=a(t)²=(a_m²/4)(3/2−2cos t+(1/2)cos 2t). (10)

This q is smooth through 0 and 2π in the extended cylinder equation, even
though those slices are excluded from the physical dust strip. Use the same
data (0,g), g≥0 nonzero supported off bar B(Y,τ). Every solution ψλ still
vanishes on I_s^-(b) by finite propagation. The smooth parameter derivative
w=∂λψλ|0 solves

    w_tt+Λ²w = −q(t) S0(t)g,       w(0)=w_t(0)=0.

Duhamel's formula and S0(2π−u)=−S0(u) give

    w(2π) = integral_0^(2π) q(u) S0(u)² g du.    (11)

In degree n=k−1, the multiplier in (11) is

    integral_0^(2π) q(u) sin²(ku)/k² du
      = 5π a_m²/16                 if k=1,
      = 3π a_m²/(8k²)              if k≥2.       (12)

These are direct orthogonality integrals for the three cosine terms in (10).
Let Π0 be the projection onto spatial constants; its kernel is 1/(2π²).
Equations (11)–(12) are therefore the exact operator identity

    w(2π) = [ (3π a_m²/8)Λ^(-2) − (π a_m²/16)Π0 ]g.

Using (3), its integral kernel at distance r is

    K(r) = a_m²/(32π) [3(π−r)/sin r − 1].       (13)

For 0<r≤π, (π−r)/sin r≥1, so K(r)>0. It follows that w(2π,Y)>0.
By smoothness there is ε_t>0, chosen smaller than τ, such that
w(t,Y)>0 for 2π−ε_t<t≤2π.

Fix **any** t_* in (2π−ε_t,2π). This is an interior event in the timelike
future of b, fixed in the unperturbed conformal scalar theory. At this fixed
target, smooth dependence on λ gives

    ψλ(t_*,Y) = λ w(t_*,Y)+o(λ).

Thus for all sufficiently small **positive** ordinary physical masses m
(λ=m²>0), ψλ(t_*,Y) is nonzero. Paired with the zero solution, it witnesses
x_*∉F_m(b), although x_*∈F_0(b). The event and data are chosen first; the
allowed mass interval may depend on them. This proves actual loss of at
least a late comoving future region, not a characterization of all F_m.

This is a fixed-background, linear classical field result. It introduces no
Einstein backreaction or interacting/quantum theory. The proof samples the
extended rescaled solution at 2π only to obtain an interior sign neighborhood;
it does not treat the singular dust endpoint as an observable event. Exact
fixing can change while the value difference is O(m²).

### Remaining independent checks

The extra argument's vulnerabilities are explicit: the Duhamel sign, the
exceptional homogeneous-mode coefficient in (12), the normalization of Π0
and the Green kernel, and the legitimacy of using the smooth rescaled
extension to obtain a fixed interior target. The accompanying controls
check the elementary identities and convergence; independent proof review
is still required before manuscript integration or any novelty assessment.
