# Candidate complete positive-mass fixing classification

27 October 2026. Coordinator derivation for adversarial review. The paper is
unchanged. No novelty, circulation, detector or ontology claim is made.

## Statement and exact scope

Fix a_m>0 and the closed dust metric on M=(0,2π)×S³,

    g=a(t)²(−dt²+dΩ³²),       a(t)=(a_m/2)(1−cos t).

For EACH ordinary constant physical mass m>0 let L_m be ALL smooth real
solutions of (Box_g−R_g/6−m²)φ=0 on M. Define F_m(b) using exact agreement
on the entire chronological strip-past P=I_s^−(b). The proposed theorem is

    F_m(b)=J^−(b)       if b=(τ,Y), 0<τ<π;
    F_m(b)=M           if π≤τ<2π.                         (T)

All quantifiers range over the stated fixed-background linear classical
problem. In particular (T) would hold for every positive mass, not just small
m or generic m. The proof concerns JOINT support of two Cauchy kernels, not
pointwise positivity of a global tail. Individual kernels may have zeros.

Write ψ=aφ, Λ²=−Δ_S³+1 and V(t)=m²a(t)². Then

    ψ_tt+(Λ²+V(t))ψ=0.                                (1)

V is entire as a function of complex t, nonnegative on real t, and strictly
positive on (0,2π). Smooth solutions of (1) on M extend uniquely to the
auxiliary cylinder by taking smooth data on any interior compact Cauchy slice.
This gives no physical continuation through a singularity of g. Since a>0
on M, physical and rescaled field agreement are equivalent there.

## Lemma 1: explicit joint analyticity of the line Riemann function

For source time s put A=(t−s+r)/2, B=(t−s−r)/2. Construct H(A,B;s) by

    H(A,B;s)=1−integral_0^A integral_0^B
                    V(s+u+v) H(u,v;s) dv du.           (2)

To justify analyticity rather than assume it from analytic coefficients, set
H_0=1 and H_(n+1)=−double_integral V H_n. Each H_n is entire in A,B,s:
parametrize the complex straight integration segments by real parameters
between zero and one. On any compact polydisc, enlarge the coefficient domain
to include the nested segments and let M_V bound |V| there. Successive
integration gives

    |H_n|≤M_V^n |A|^n |B|^n/(n!)².

Thus Σ_n H_n converges normally on every compact polydisc. Its sum is entire
and solves (2); derivatives may be taken locally term by term. The same
iteration estimate gives uniqueness. In particular

    H_AB+V(s+A+B)H=0,       H(A,0;s)=H(0,B;s)=1.        (3)

Put R(t,s;r)=H((t−s+r)/2,(t−s−r)/2;s). Symmetry in A,B makes R even in r.
The retarded line velocity fundamental solution is

    E(t,s;r)=(1/2) 1_{t−s≥|r|} R(t,s;r).               (4)

Indeed, inside the cone (3) is (∂t²−∂r²+V(t))R=0. On its two fronts R=1;
the tangential derivatives vanish. Distributional differentiation of (4)
therefore leaves only the normalized point source: since
δ(A)δ(B)=2δ(t−s)δ(r), its coefficient 1/2 gives unit source. Equivalently,
its initial displacement is zero and initial velocity is δ(r). Uniqueness
of the retarded Cauchy problem identifies (4) with the line propagator.

This establishes joint analyticity of the SPECIAL tail R; it does not claim
that arbitrary smooth solutions of an analytic hyperbolic equation are analytic.

## Lemma 2: periodization and the S³ radial kernel

Let S_k(t,s) solve the scalar mode equation with initial data (0,1) at s,
with frequency term k²+V(t). Periodize (4) in r with period 2π. Finite
propagation makes the image sum locally finite. Its circle Fourier series is

    E_per(t,s;r)=S_0(t,s)/(2π)
                      +(1/π)Σ_(k≥1) S_k(t,s) cos(kr).

Here S_0 is the line/circle zero-frequency mode, not the constant S³ mode.
Differentiation removes it. The scalar S³ degree-(k−1) projection kernel is

    k sin(kr)/(2π² sin r),       0<r<π.

Consequently the S³ velocity Cauchy kernel, as a distribution, is

    K(t,s;r)=−∂r E_per(t,s;r)/(2π sin r).              (5)

This is an identity of the harmonic expansions and hence fixes normalization,
including any singular terms; we use its smooth values only away from fronts.
For 0<t−s<2π and 0<r<π there are at most two contributing images:

    E_per(t,s;r)=E(t,s;r)+E(t,s;2π−r).                 (6)

In the direct-only cell, (5) therefore specializes to

    K(t,s;r)=−R_r(t,s;r)/(4π sin r).                  (6a)

The factor 1/4π includes the factor 1/2 in the line kernel E.

For fixed physical target time 0<t<2π, the relevant connected open cells with
0<s<t are

    D_1: 0<r<π,       r<t−s<2π−r;
    D_2: 0<s<t−π,     2π−(t−s)<r<π.                 (7)

D_1 is connected: after decreasing r sufficiently one can vary s and then r
to any other point. More explicitly it is the intersection of strict linear
inequalities 0<s<t, 0<r<π, r<t−s, r<2π−t+s, so is convex. D_2 is an open
triangle, nonempty precisely when t>π. Formulae (4)–(6) and Lemma 1 make K
real analytic jointly in (s,r) on each cell. They also give analytic extensions
across s=0 near any radial interval strictly inside its initial cell. No
continuation across a wavefront or caustic is being assumed.

Let C(t,s) be the displacement Cauchy propagator. The mode fundamental matrix
identity gives

    C(t,s)=−∂s S(t,s),                                (8)

where S has kernel K. For example, differentiating the upper-right entry of
the fundamental matrix with respect to its lower endpoint gives minus its
upper-left entry. The same scalar Wronskian formula gives

    (∂s²−Δ_Z+1+V(s))K(t,s;X,Z)=0                    (9)

away from its wavefronts (and distributionally for the two-parameter Cauchy
kernel). Rotational invariance makes the smooth radial form of (9)

    K_ss−K_rr−2cot(r)K_r+(1+V(s))K=0.               (10)

The source-time derivative in (8), not a target-time derivative of a
time-independent propagator, is essential for this time-dependent equation.

## Lemma 3: neither analytic cell is identically zero

### Direct cell

As s tends up to t, put h=t−s and choose r=h/2>0. From (2), near A=B=0,

    H=1−V(s)AB+terms of total degree at least three in A,B.

Taking a radial derivative at fixed t,s yields R_r=V(s)r/2+O(h²). Since
sin r~r and only the direct image contributes along this path, (5) gives

    K(t,s;h/2) → −V(t)/(8π) ≠0.                     (11)

All these points lie in D_1 for h small. Thus K is not identically zero on
D_1 for every physical t and every m>0.

### Double-image cell: front jet and corner limit

For I(t,s)=integral_s^t V(u)du, differentiating (2) at B=0 gives

    H_A=H_AA=0,       H_B=−I,
    H_AB=−V(t),       H_BB=−V(t)+V(s)+I²/2.

Since ∂r=(∂A−∂B)/2 at fixed t,s, the right-front derivatives at r=t−s are

    R_r=I/2,
    R_rr=J(t,s):=[V(t)+V(s)]/4+I(t,s)²/8.           (12)

The H_BB formula follows by differentiating the integral defining H_B:
the coefficient derivative integrates to −V(t)+V(s), and
integral_s^t V(u) integral_s^u V(v)dv du=I²/2. These are radial derivatives
with t,s fixed, not derivatives along the moving front.

Fix t>π. Approach s_*=t−π from below, writing t−s=π+α and r=π−ε with
0<ε<α. Both images are strictly inside their line cones, so (5)–(6) give

    K(t,s;π−ε)
       =[R_r(t,s;π+ε)−R_r(t,s;π−ε)]/(4π sin ε).

The symmetric difference quotient and smooth analytic extension of R up to
the front show, uniformly for all such paths to this corner,

    K(t,s;π−ε) → J(t,t−π)/(2π)>0.                  (13)

Positivity follows already from V(t)>0 and V(t−π)≥0; the I² term is also
nonnegative. This establishes a nonzero point neighborhood inside D_2 for
every fixed m>0 and t>π. It does not assert positivity throughout D_2.

The independent front-jet-review/RESULT.md derives (12)–(13) with a different
characteristic-coordinate normalization and an exact constant-potential
Bessel-series control.

## Lemma 4: the JOINT Cauchy support has no open holes

Fix t and X. Suppose both K(t,0;r) and its source-time derivative vanish on
an open radial interval strictly inside either initial cell, away from r=0,π
and any wavefront. By (8) these are zero velocity/displacement kernel traces
there. Local Cauchy uniqueness applied to (10) makes K zero in an open
spacetime neighborhood of that interval, including a nonempty open subset
with s>0. Lemma 2 supplies joint analyticity, so the real-analytic identity
theorem forces K=0 on the entire connected D_1 or D_2. This contradicts (11)
or (13), respectively.

Hence the union of the spatial supports of S(t,0;X,·) and C(t,0;X,·) is

    closed B(X,t)       for 0<t<π,
    all S³             for π≤t<2π.                 (14)

For t<π, finite propagation proves containment in the closed ball and the
no-hole argument proves density of joint support in its interior. At t=π,
the direct initial cell covers every 0<r<π and closure includes the source
and antipode. For t>π, the direct and double initial cells cover respectively
(0,2π−t) and (2π−t,π); their joint-support closures give all S³. No pointwise
claim is needed on their separating wavefront or the antipode.

An open spatial patch disjoint from the joint support would, by rotational
invariance, give such a radial interval: choose a point off the two poles
and the finitely many front spheres. Thus the radial no-hole statement is
sufficient for the full spatial support assertion.

## Theorem proof from support and cap geometry

Let 0<τ<π and C=closed B(Y,τ). A smooth solution vanishing on P has initial
data (f,v) at zero vanishing on the open ball B(Y,τ), and hence, with all
derivatives, on its closure. Conversely any smooth initial data supported
strictly outside C give exact past vanishing by finite propagation. These
facts suffice for the following necessity argument; no assertion that such
strictly supported data exhaust every admissible smooth datum is required.

If (t,X) is outside J^−(b), then the joint support in (14) is not contained
in C. For t<π, closed B(X,t) lies in C exactly when d(X,Y)+t≤τ: its maximum
distance from Y is min(π,d(X,Y)+t), and τ<π. For t≥π joint support is the
whole sphere, while C is proper.

Thus at least one of the two kernels has nonzero distributional restriction
to the open complement S³\C. A smooth real test datum compactly supported
there has nonzero pairing with that kernel. Choose it as displacement or
velocity data, and put the other datum zero. The resulting solution and zero
agree exactly on P but disagree at (t,X), proving nonfixing. Conversely
J^−(b) is fixed by continuity of fields vanishing on P. This proves the first
line of (T).

For τ=π, the open trace ball is S³ minus its antipode; smoothness forces both
initial data to vanish everywhere. For τ>π that trace ball is already the
whole sphere. Uniqueness then makes every past-zero solution zero globally,
proving the second line for every mass (including zero).

## Review dependencies and remaining priority limits

The two initial sidecar reviews intentionally treated global analyticity and
the corner coefficient as unproved dependencies. This derivation supplies both
explicitly. Their combination, normalization in (5), source-time identity (8),
normal convergence in (2), and the no-hole step are assessed in the updated
support review and the fresh final-review/REVIEW.md. Bounded controls cannot
replace those analytical checks. The coordinator's final scope disposition
and proof hash are recorded separately in REVIEW_STATUS.md.

For comparison with the existing massless theorem, the proposed classification
has the following scope:

| Standpoint time | Massless conformal scalar | Any positive ordinary mass |
| --- | --- | --- |
| 0<τ<π | Closed three-diamond fixed set | Exactly J^−(b) |
| τ=π | All of M (dense initial trace cap) | All of M for the same reason |
| π<τ<2π | All of M | All of M |

Thus the answer concerns loss of all EXTRA fixing strictly before maximum
expansion. It does not say a mass removes determination that the post-maximum
causal geometry already guarantees, or that it removes the dense-trace effect
at the exact threshold. The all-positive-mass proof itself does not depend
on the massless three-diamond classification; only this comparison does.

No complete original-source priority audit has been done. Existing Huygens,
Riemann-function, spherical propagator and lacuna results may already imply
this classification. Classical tools, a successful derivation and model
specificity do not establish novelty. No manuscript upgrade is authorized by
this document's theorem formatting alone.
