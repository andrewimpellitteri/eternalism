# Local smoothness repair for the compact incoming-profile construction

30 October 2026. Coordinator proof with three bounded adversarial checks
and explicit integration repairs; see SMOOTHNESS_REVIEW_STATUS.md.
This is a local regularity argument, not an application of Kilgore's global
weighted theorem. The full interpolation theorem retains its separate
integrated-review gate; SMOOTH_FINITE_CONTROL.md states the exact upgrade.

## Scope and the order of the argument

Use the same compact smooth incoming family, exact flat wedge v<A, finite
incoming mass E and global reduced bounds as C11_FINITE_CONTROL.md. The
already reviewed reconstruction gives a C¹,¹ four-metric and scalar. The
aim is smoothness in a regular Cartesian polar-areal atlas. The steps are:

1. Uniform all-order estimates only in the exterior u≤u_*<A on each finite
   advanced interval [A,V], giving a smooth early complete Cauchy surface.
2. A global polar-areal change of coordinates, initially only C¹,¹.
3. A regular Cartesian symmetric-hyperbolic scalar system whose metric
   coefficient gains one spatial derivative from the radial constraints.
4. Local energy estimates and weak–strong uniqueness, propagating the
   early smooth data through the known Lipschitz solution.

No all-order estimate on the entire receding-cone domain is presumed.

## 1. Exterior Goursat system and its tame derivative induction

Set p=rφ, q=p_v, λ=r_v, ν=r_u, f=1−2m/r, r₀=(v−u)/2 and h=r−r₀.
For u_n≤u≤u_*<A, A≤v≤V, use

    X=(λ,q),      Y=(h,ν,p,m),
    Q=2mνλ/(f r²),
    X_u=F=(Q,Qp/r),
    Y_v=G=(λ−1/2,Q,q, f(q−λp/r)²/(2λ)).

Characteristic data are

    X(u_n,v)=(1/2,Φ_n(v)/2),
    Y(u,A)=(0,−1/2,0,0).

The flat-wedge proof supplies the second line. The first-order source
bounds imply |q|≤Cε and |p|≤Cε(V−A). The mass equation implies
0≤m≤Cε²(V−A). All components of X,Y are uniformly bounded; r≥(A−u)/3,
f≥1/2 and λ≥1/3. For h use its finite v integral. Constants may depend
on u_*,A,V and each fixed profile norm, but not on u_n.

Every derivative of F with respect to its bounded arguments and its
explicit v-dependence is O((A−u)⁻²). Derivatives of G are uniformly
bounded. These statements use the displayed rational formulas with r≥R>0;
derivatives of r⁻¹ only improve decay, and derivatives of f⁻¹ are harmless
since m is uniformly bounded and f≥1/2.

Induct on the pure-v derivative order k. Given bounds through k−1,
Y_(v^k)=∂_v^(k−1)G is already bounded. Differentiating X_u=F k times yields

    ∂_u X_(v^k) = F_X X_(v^k) + H_k,
    |F_X|+|H_k| ≤ C_k(A−u)⁻².

H_k includes F_Y Y_(v^k), now known. Initial X_(v^k) is bounded by the
common kth derivative norm of Φ_n. The integrating-factor/linear-system
Gronwall estimate uses only

    ∫_(u_n)^(u_*) (A−s)⁻² ds ≤ 1/(A−u_*).

It gives a uniform kth derivative bound. Then Y_(v^(k+1)) follows from G.
There is no smallness threshold depending on k. For mixed u-derivatives,
X_(u^j)=∂_u^(j−1)F is known from lower u-orders, and

    ∂_v Y_(u^j) = G_Y Y_(u^j) + G_X X_(u^j) + lower terms,
    Y_(u^j)(u,A)=0.

Finite-v Gronwall closes this induction; v derivatives of these identities
give all mixed orders. This is an exterior argument with no r=0 division.
For finite approximants differentiations are justified by local smooth
Goursat evolution. Its local content is elementary here: on an off-axis
rectangle the equations are

    X(u,v)=X(u_n,v)+∫_(u_n)^u F(s,v,X,Y)ds,
    Y(u,v)=Y(u,A)+∫_A^v G(u,z,X,Y)dz.

On small rectangles the smooth, locally Lipschitz rational vector fields
give a contracting integral system; differentiation/difference quotients
give the displayed derivative equations. Tile finite closed substrips
while the positive r,f,λ margins hold. The same a priori derivative
estimates prevent higher-order breakdown. No smooth-axis characteristic
theorem is being invoked to prove smoothness at the center.

Arzelà–Ascoli at every order gives smoothness of the selected limit on
u<A, v≥A. A further subsequence does not change the already fixed C¹/C²
limit. For v<A the fields are flat. Choose A strictly before the common
support so these regions overlap in an open flat strip. The original
Cartesian metric and scalar are therefore smooth on t<A, and in fact
wherever u<A, with the center covered by the flat strip.

## 2. Global polar-areal coordinates from the known low-regularity solution

In old coordinates t=(u+v)/2, ρ=(v−u)/2, put

    b=r_t/r_ρ=(λ+ν)/(λ−ν),       |b|≤1/2.

Here b is a coefficient, not the marked launch event. It is C¹,¹ on the
quotient, b(t,0)=0. Solve dt/dρ=−b(t,ρ) with center value t_c, label the
curve by central proper time T=τ(t_c), and take R=r as area radius.
The bounded coefficient makes the flow global; its center derivative is
positive. Along a T-slice,

    dR/dρ=4λ(−ν)/(λ−ν) ≥ 4/9.

Thus (T,R) covers R×[0,∞). Here are the regularity details, including the
center. If t=F(t_c,ρ), then

    F_ρ=−b(F,ρ),
    F_(t_c)=exp[−∫₀^ρ b_t(F(t_c,s),s)ds]>0.

Since b is C¹,¹, these first derivatives are locally Lipschitz. The inverse
label χ(t,ρ)=t_c has χ_t=1/F_(t_c) and χ_ρ=b/F_(t_c), with the flow
derivative evaluated at (χ,ρ); it is bounded away from zero on compact
sets. Consequently χ and T=τ∘χ are C¹,¹, and T_ρ=bT_t vanishes at ρ=0.
The radial scalar lift of T is C¹,¹: its spatial Hessian contains T_ρ/ρ,
bounded by the Lipschitz constant of T_ρ because T_ρ(t,0)=0. The axis
lemma in AXIS_C11_RECONSTRUCTION.md gives B=r/ρ C¹,¹ and B_ρ(t,0)=0,
so X_i=B(t,|x|)x_i is also C¹,¹. At the center the Jacobian is
diag(τ′,r_ρ I₃), with positive diagonal factors. The inverse function
theorem and the locally Lipschitz Jacobian give a C¹,¹ inverse there;
the radial monotonicity gives the global inverse away from the center.
The metric takes the form

    g=−α²dT²+a²dR²+R²dσ²,     a²=f⁻¹,
    c=α/a=r_ρ/T_t,             c(T,0)=1.

These are low-regularity coordinate identities, not an assumption of
smoothness. At a center time t_c<A, the entire T-slice obeys
u=t−ρ≤t_c−ρ/2<A. Its data and the coordinate change near it are smooth by
§1. This supplies a smooth complete initial slice for the next argument.

## 3. Derive the regular system without transforming distributional Ricci

Define P=c⁻¹φ_T, Q_r=φ_R, W_i=Q_r X_i/R, U=(P,W), e=P²+|W|². The name
Q_r denotes a scalar radial derivative, not the Q of §1. Initially U is
locally Lipschitz because φ and the coordinate map are C¹,¹. Radial
invariance gives ∇_Xφ=0 at the center and Q_r=O(R), so W=∇_Xφ has no
axis singularity.

The scalar wave equation in weak divergence form gives on all R³

    P_T=div(cW),       W_T=∇(cP).

The flux through a radius-η sphere is O(η³), since c is locally bounded
and Q_r=O(R); its vanishing excludes an axis delta. This uses first-order
change of variables in the weak wave identity, not curvature covariance
under an insufficiently regular map.

The reduced mass equations give directly

    ∂_R=(2ν)⁻¹∂_u+(2λ)⁻¹∂_v,
    Q_r+P=φ_v/λ,       Q_r−P=φ_u/ν,
    m_R=(fR²/2)e,
    f_R=(1−f)/R−Rf e.

The metric evolution equation is also recorded:

    ∂_T=(c/2)(−ν⁻¹∂_u+λ⁻¹∂_v),
    m_T=cfR² P Q_r,       f_T=−2cfR P Q_r.

For m_T substitute the two mass equations into ∂_T m and use
[(Q_r+P)²−(Q_r−P)²]/4=P Q_r. This is the momentum constraint. It is
also implied by the scalar system with the m_R and lapse equations: put
M=m_T−cfR² P Q_r. Those equations and f_T=−2m_T/R give M_R=−R e M, and
M(T,0)=0, so M≡0. A smooth radial solution of the auxiliary system thus
satisfies it without reference to the low-regularity solution.

For the lapse, write D=∂_ρ−b∂_t. Differentiating T_ρ=bT_t a.e. gives
D log T_t=b_t. Hence

    D log c=(r_ρρ−r_tt)/r_ρ=−4r_uv/r_ρ,
    ∂_R log c=−4r_uv/(r_ρ²−r_t²)=2m/(fR²).

All derivatives used exist a.e. and the quantities are locally Lipschitz;
the scalar Sobolev chain and product rules suffice.

The polar first-order formulation itself is established prior methodology,
not a new formulation: compare Gundlach–Martín-García, *Critical Phenomena
in Gravitational Collapse*, [§3.1, (20)–(26)](https://link.springer.com/article/10.12942/lrr-2007-5).
Their scalar is φ_source=φ/√(4π) in our normalization. We derive the
identities above directly from SSESF to check that they apply to this
initially low-regularity solution. The new obligation is the local
persistence argument for this selected scattering limit, not those
well-known polar equations.

## 4. Regular radial constraint operators and the derivative gain

For radial e, define a scalar function on Cartesian space

    Z[e](X)=∫₀¹ s²e(sX)
       exp[−|X|²∫_s¹ z e(zX)dz] ds.

Solving the first-order mass constraint with its regular center value gives

    μ=R²Z,       f=1−R²Z,
    c=exp[|X|²∫₀¹ s (Z/f)(sX) ds],
    ∂_i c=c X_i Z/f.

These formulas include the center. In particular there is no undifferentiated
division by R in the operator which determines ∇c from U. Smooth U gives
smooth coefficients with all required radial parity built in.

On B_L, the averaging operators T_j h=∫₀¹s^j h(sX)ds, j=1,2, are bounded
on every integer H^k: for a derivative of order l≤k,

    ||D^l h(s·)||_(L²(B_L)) ≤ s^(l−3/2)||D^l h||_(L²(B_L)),
    ∫₀¹s^(j+l−3/2)ds<∞.

Moser product/composition estimates applied to Z, f⁻¹ and c therefore give,
for ||U||∞≤B and f≥δ>0,

    ||c−1||_(H^(k+1)(B_L)) + ||∇c||_(H^k(B_L))
        ≤ C_(k,L,B,δ) ||U||_(H^k(B_L)).                 (A)

More explicitly, J_s h=∫_s¹ z h(zX)dz obeys

    ||D^l J_s h||₂ ≤ ∫_s¹ z^(l−1/2)dz ||D^l h||₂,

uniformly in s∈[0,1], including l=0. Multiplication by |X|² is bounded
on each H^k(B_L). The exponential argument has size ≤L²B²/2. Products
and the compositions exp and f⁻¹ are tame on their bounded ranges.
For the zero-order c−1 bound use the displayed exponential formula and
T₁(Z/f), rather than a point-value Poincaré inequality in three dimensions;
then ∇c=cXZ/f gives the extra derivative. The operators depend
only on data at radii ≤|X|. Differences give additionally

    ||c[U]−c[V]||₂ + ||∇c[U]−∇c[V]||₂
        ≤ C_(L,B,δ)||U−V||₂.                          (B)

These estimates concern radial scalar/vector fields. Picard steps preserve
that symmetry; no nonradial identity for ∇c is being asserted.

## 5. Local persistence and weak–strong uniqueness

Let A_j be the constant symmetric 4×4 matrix whose only nonzero entries
couple P and W_j. The regular system is

    U_T=Σ_j A_j ∂_j(c[U]U).

The detailed local construction, including localization, a common base
H³ existence interval, higher-order persistence, and continuation on
strictly smaller cones, is in LOCAL_POLAR_PERSISTENCE.md. It uses (A)
and (B), not a direct invocation of a theorem for pointwise nonlinearities.
Smooth local solutions of this auxiliary system are identified with the
known solution; no Einstein constraint-propagation theorem is needed.

For a smooth solution, commuting k spatial derivatives and using symmetry
gives on a ball shrinking faster than c the tame estimate

    d/dT ||U||_(H^k) ≤ C_(k,L,B,δ)(1+||∇U||∞)||U||_(H^k).  (C)

The boundary flux is nonpositive. The commutator term is controlled by
||∇c||∞||U||_(H^k)+||c−1||_(H^k)||∇U||∞. The source term is controlled by
||∇c||∞||U||_(H^k)+||∇c||_(H^k)||U||∞. Substitute (A); the highest norm
appears linearly. A high Sobolev norm is not hidden in the coefficient C.

For a Lipschitz solution U and a smooth solution V, subtract their equations.
The extra terms are (c[U]−c[V])A_j∂_jV and
∂_j(c[U]−c[V])A_jV. Estimate (B) and the L² energy identity give

    d/dT ||U−V||₂² ≤ C||U−V||₂².

The zero initial difference stays zero. Thus the smooth auxiliary solution
matches the given low-regularity solution throughout its local domain.
It inherits the latter's bounded Lipschitz norm and f≥1/2. Estimate (C)
then prevents higher norms from breaking down on any smaller finite cone.
Successive local existence intervals and uniqueness propagate smoothness
through it. All k are handled with the same low-order continuation bound;
their energy constants need not be uniform in k.

To choose cones covering arbitrary finite times, note m_u≤0 and the actual
incoming mass identity imply 0≤m≤E globally. For T in a compact interval,
write B for the low-order bound for U on R≤1. The mass constraint gives
m≤B²R³/6 there, hence ∂_R log c≤(2/3)B²R using f≥1/2. Since

    ∂_R log c = 2m/(fR²) ≤ 4E/R²       (R≥1),

c≤exp(B²/3+4E) has a finite global bound on that T interval. A sufficiently large
initial ball, shrinking at a fixed larger speed, covers any prescribed
compact polar-coordinate set. The entire initial slice was smooth, so
its required finite-ball Sobolev norms are finite. This proves smoothness
everywhere at finite coordinates without estimates at null infinity.

## 6. Smooth tensor reconstruction and remaining verification points

After U is smooth, Z, f and c are smooth. In the polar-areal Cartesian
atlas the original metric and scalar therefore have

    g_TT=−c²/f,       g_Ti=0,
    g_ij=δ_ij+(Z/f)X_iX_j,
    φ_T=cP,          ∇φ=W.

These are manifestly smooth at the center; all division/parity issues are
resolved by the integral formulas. To recover the full classical field
equations, use the mass/lapse constraints, m_T equation and scalar system
derived in §3. Off the center, with Ric=2dφ⊗dφ written as E=G−2T=0,
substitution in the smooth metric gives E^T_T=E^R_T=E^R_R=0. E^θ_θ has
second time derivatives of the metric, so it needs one more step. Put
s=E^θ_θ=E^φ_φ. Since ∇_μG^μ_ν=0 and ∇_μT^μ_ν=(□φ)∂_νφ=0, we get
∇_μE^μ_R=−2s/R=0, hence s=0 for R>0. Continuity of the smooth tensor
equations then extends them to the center. This avoids using transformation of
distributional Ricci under the preliminary C¹,¹ chart. The polar chart agrees with the
old Cartesian chart on the entire flat wedge, and T is precisely central
proper time, so the causal-past and finite-readout identities are preserved.

The smooth structure used here is the regular (T,X) atlas. Its transition
to the original low-regularity Cartesian coordinates is C¹,¹, not asserted
to be C∞ by this argument. This suffices to construct a smooth spacetime
representative, agrees with the original smooth structure on the flat
wedge, and keeps the marked central clock exactly T. A claim that the
old coordinates themselves are smooth would require a further coordinate
regularity argument and is not needed.

Checks of the exterior induction and chart/constraint operators are in
the two smooth-*-review directories; the persistence argument is a separate
coordinator derivation with its own review record. No novelty claim follows.
Smoothness at finite physical points is distinct from smooth conformal
null infinity, and the global weighted norms of Kilgore are not used.
