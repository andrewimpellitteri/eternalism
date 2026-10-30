# Local persistence for the center-normalized radial wave system

30 October 2026. Coordinator derivation supporting SMOOTHNESS_BOOTSTRAP.md.
This supplies the nonlocal step; a standard theorem for a pointwise
nonlinearity is not by itself a theorem for the coefficient used here.

## 1. Statement and inputs

Let U=(P,W) be rotationally invariant: P is a radial scalar and W a radial
Cartesian vector. On an interval I and all of R³ assume U is locally
Lipschitz and solves, distributionally,

    U_T=Σ A_j ∂_j(c[U]U),                              (1)

where the constant symmetric matrices A_j exchange P and W_j. The radial
constraints defining f[U] and c[U] are exactly §4 of the bootstrap note,
with e=|U|², center values f(0)=c(0)=1, and f≥δ>0 locally. Suppose:

* U is smooth near an entire slice T=T₀;
* c has a finite upper bound on I′×R³ for every compact I′⊂I;
* on finite balls the constraint maps obey (A), the tame H^k→H^(k+1)
  bound for c−1, and (B), the L²→H¹ difference bound, with constants
  depending on k, radius, ||U||∞ and a positive lower bound for f only.

Then U is smooth on I×R³ in the connected time direction from T₀. The
argument also applies backwards. These are local spatial assertions; no
global Sobolev norm of U or smooth conformal null infinity is required.

The exterior and low-order arguments in SMOOTHNESS_BOOTSTRAP.md supply
the first input. Its final estimate for c supplies the second. Its §4
derives the third by explicit ray integrals. What follows explains local
existence, uniqueness and continuation under precisely those inputs.

## 2. Local construction and preservation of symmetry

First localize on a fixed ball B_L. Extend its smooth rotationally
invariant initial data to smooth compactly supported data on R³. For H³
data a bounded ball-extension operator followed by rotational averaging
gives the same operation with a bounded H³ norm. Averaging acts on a
scalar and a vector with their respective rotation representations.

Choose smooth radial cutoffs χ₀,χ₁∈[0,1], both one on B_L, with χ₀ one
on the support of χ₁, and both compactly supported. In the coefficient
operator replace e by χ₀|U|² and then replace c by

    ĉ=1+χ₁(c−1).

The resulting maps have the same tame and difference bounds on the whole
space, with constants depending on the fixed cutoffs. In particular
ĉ−1∈H^(k+1), ĉ>0, and the original coefficient is recovered on B_L.
No data outside B_R affect c at a point of B_R⊂B_L. The latter fact is
essential for local comparison, since c is nonlocal inside that radius.

Positivity is available for the iterates, without assuming their
constraints remain close in a derivative norm. For any bounded
nonnegative energy e, set H(R)=∫₀ᴿs e(s)ds. The constraint has solution

    f(R)=exp[−H(R)] R⁻¹ ∫₀ᴿ exp[H(s)]ds>0,
    f(R)≥exp[−B²R²/2]   if e≤B².                    (2)

The bound at R=0 is interpreted by continuity. Thus a common L∞ bound
on a fixed coefficient-support ball gives a common positive δ for every
Picard step. Cutoff energies preserve nonnegativity and radial symmetry.

Freeze ĉ at U^n and solve the linear symmetric-hyperbolic equation

    U^(n+1)_T=Σ A_j ∂_j(ĉ[U^n] U^(n+1))

with the same initial data. Smooth approximations or spatial Friedrichs
regularization justify the linear solution and its energy identities;
the estimates below are independent of that regularization. The linear
equations commute with rotations, so uniqueness preserves the required
radial scalar/vector subspace. No coefficient identity is being used
outside that subspace.

Use the base norm H³, for which H³(R³) embeds in W¹,∞. On an H³ ball
the tame constraint bounds, (2), and the usual differentiated linear
energy estimate give a common short interval with uniform H³ bounds.
The length depends on the base norm and cutoffs, not higher norms.
For the differences of consecutive iterates, the forcing is

    Σ A_j [ (ĉ_n−ĉ_(n−1))∂_j U^n
                   + ∂_j(ĉ_n−ĉ_(n−1)) U^n ].

Its L² norm is at most C||U^n−U^(n−1)||₂, by (B) and the uniform W¹,∞
bound. The L² energy estimate therefore gives contraction in
C([T₀,T₀+h];L²) for sufficiently small h. Interpolation with the uniform
H³ bound gives convergence in C H^s for s<3, in particular some
s>5/2. This alone does not give strong H³ convergence. Instead the limit
is bounded and weakly continuous in H³. For each |α|≤3, v=D^αU solves
the linear equation v_T=Σc A_j∂_jv+G_α, with G_α∈L¹_tL²_x by the
same tame bounds. Spatial mollification gives its L² energy identity:
the commutator [J_η,c∂_j]v is uniformly bounded in L² by the Lipschitz
coefficient norm times ||v||₂ and tends to zero by approximation of v
with smooth L² fields (the smooth-field limit is immediate). Integrate
in time and let η→0. The resulting energy identity gives continuity
of ||v||₂; together with weak continuity it gives strong L² continuity
of v. Summing |α|≤3 supplies strong H³ time continuity of the solution,
without asserting strong H³ convergence of the iterates. This proves local existence
and uniqueness in the radial H³ class for the localized system.

Higher regularity uses this same interval. At order k≥3 the frozen
iteration estimate is tame: its right side contains the H^k norms of
U^(n+1) and U^n linearly, with coefficients bounded by the common H³
bound and the fixed cutoffs. Taking the maximum over finitely many
iterate indices and applying Gronwall gives a bound independent of
that number. At each fixed k it passes to the limit. This supplies
every finite k on the base interval; it is not an intersection of
intervals whose lengths might tend to zero. Time smoothness follows
by (1) and the smooth integral coefficient map. Smooth initial data
therefore give a smooth local auxiliary solution.

## 3. Tame estimate on central shrinking balls

Let L(T)=L₀−C₀(T−T₀)≥L_min>0 and suppose C₀>sup c on the portion
considered. Write E_k=||U||_(H^k(B_(L(T)))). For a commuted field
w=D^αU the principal boundary contribution to half the squared energy is

    (1/2)∫_(∂B_L) [ L′|w|²+c wᵀ A(n)w ],

where A(n)=Σn_jA_j has eigenvalues 1,−1,0,0. It is nonpositive.
The interior principal term costs ||∇c||∞ E_k². The remaining spatial
commutators and differentiated source obey the tame bounds

    ||[D^α,c]∇U||₂
       ≤ C_k( ||∇c||∞ E_k + ||c−1||_(H^k)||∇U||∞ ),
    ||D^α((∇c)U)||₂
       ≤ C_k( ||∇c||∞ E_k + ||∇c||_(H^k)||U||∞ ).

Ball Sobolev/product constants can be chosen uniformly when radii stay
in [L_min,L₀]; extension to a fixed ball is one justification. The
constraint estimate (A) then gives

    dE_k/dT ≤ C_(k,L₀,L_min,B,δ)(1+||∇U||∞) E_k.       (3)

This is linear in E_k. In particular no H^(k+1) norm of U or high norm
inside its coefficient is required. The identical calculation with
absolute time direction works for backwards continuation.

## 4. Weak–strong uniqueness against the given solution

Let U be the given locally Lipschitz weak solution and V a smooth
auxiliary solution from the same data on a ball. On a shrinking ball
inside that initial ball, put D=U−V and d=c[U]−c[V]. Subtraction gives

    D_T=Σ A_j ∂_j(c[U]D)
                   +Σ A_j(d∂_jV+(∂_jd)V).           (4)

The principal coefficient is the known c[U]; it suffices to shrink
faster than its speed. On this ball (B) implies

    ||d||₂+||∇d||₂ ≤ C||D||₂.

The coefficients in C need only the two bounded energies and positive
f bounds, which hold on this short compact region. The remaining
forcing in (4) is bounded by C||V||_(W¹,∞)||D||₂. The symmetric energy
identity gives d||D||₂²/dT≤C||D||₂²; zero initial difference implies
D=0. For Lipschitz U this identity follows by mollification and the
Lipschitz principal-coefficient commutator estimate, or directly by
the weak Green identity for H¹ fields. Thus the auxiliary solution
agrees with the given solution inside the comparison cone, including
the center. The cutoffs in §2 have no effect there, because both
constraint operators use only the inner radii.

## 5. Continuation, with a spatial buffer

Fix a finite time slab and a target compact set. Choose a central
comparison cone reaching beyond that set, with radius bounded below
by (say) one and shrinking faster than the known global bound for c.
Use a slightly larger initial ball and a strictly larger cone as a
spatial buffer. The given solution has finite W¹,∞ norm on the closure
of this larger finite cone and a common positive f lower bound there.

On each portion where the smooth auxiliary solution agrees with U,
these are its low-order bounds. Estimate (3) at k=3 gives a finite
uniform H³ bound up to any proposed finite breakdown time on a cone
strictly inside the larger one. The local construction in §2 can then
be restarted at times approaching that endpoint: extend the data from
an inner ball using the bounded H³ extension operator. Its radii stay
in a compact positive interval, so the extension bounds and the base
H³ lifespan are uniform. Choose the restart time close enough to the
endpoint that this lifespan crosses it and the speed times the added
interval fits in the spatial buffer. Uniqueness (4) identifies the
restarted solution with U on the smaller cone.

This is the local continuation argument: one always uses an outer
cone for the energy bound and a strictly inner cone for the restart;
no boundary regularity or extension of U past a physical boundary is
being assumed. Equivalently, construct the maximal local H³ solution
on these nested cones by patching the short solutions of §2 with §4.
The bounded-base-norm restart precludes a finite interior endpoint.
Since the initial slice is smooth on every ball, there is no external
edge of initial data to obstruct this localization. The constants for
any fixed target are finite, even if they grow with the chosen ball.

Here is the quantitative endpoint step. Let τ be the proposed endpoint,
let B_R be the target ball, and choose fixed r,η>0 with

    R+2η<r<lim_(T↑τ) L_inner(T).

The outer-cone estimate bounds H³(B_r) uniformly as T↑τ. Its bounded
extension and the local construction give a uniform lifespan h₀>0.
Put h=min(h₀/2,η/(2C₀)) and choose T₁<τ with τ−T₁<h/2. Restart from
T₁. It exists until T₁+h>τ and agrees with U on the comparison cone
whose radius stays at least r−C₀h>R+η. Thus it crosses τ on a whole
neighborhood of the target. Only this one restart is used to cross a
proposed endpoint; there is no sum of radius losses from a sequence
of intermediate local existence intervals. The initial outer cone is
chosen with this fixed margin throughout the finite target slab.

Once the base continuation is established, (3) propagates each finite
H^k norm through the same compact cone. Sobolev embedding at arbitrary
k and the equation give joint C∞ regularity there. Exhaustion over
finite target sets proves the assertion of §1.

## 6. Source and scope audit

The frozen linear iteration, Sobolev product/commutator estimates,
energy continuation and cone Green identity are standard methods.
A primary-author framework checked here is Guy Métivier, *The
Mathematics of Nonlinear Optics*, 7 March 2009,
[author PDF](https://www.math.u-bordeaux.fr/~gmetivie/NLO2008.pdf),
Theorem 3.2 (printed p.23), Lemma 3.8/Theorem 3.9/Lemma 3.10 (p.26),
and §3.6, Proposition 3.14 (pp.29–30). Selected full text was read.
Those results motivate the iteration and continuation argument; they
are not cited as an already proved nonlocal theorem. The extra
ingredient here is the explicit H^k→H^(k+1) constraint gain and its
L²→H¹ difference bound, which make the displayed iteration and energy
calculation close for this radial coefficient.

This is a mathematical derivation for the stated compact-profile
construction. It is not a new general well-posedness theorem for
Einstein matter, not a novelty claim, and not smoothness at a conformal
boundary. The external LOY low-order/source hypotheses remain inputs.
