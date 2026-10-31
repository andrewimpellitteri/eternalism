# R3 expanded: a uniform second-profile-derivative ball

31 October 2026. Coordinator derivation for the C1,1-target route. This is a
conditional estimate, not independent reconstruction of the external source
bootstrap or acceptance of the full central-history theorem. No novelty claim.

## 1. Precise imported estimates

Work first with smooth finite-cone input f. Put p=r phi, lambda=r_v,
nu=r_u, D=lambda^(-1) partial_v, and

    K=2m nu/((1-2m/r)r^2),       A_src=4||f''||_infinity.

Use the small-data regime 0<epsilon<=1, with constants independent of the cone
vertex and A_src. The required displayed estimates are LOY arXiv:1605.03893v1,
Theorem 1.1 and Remark 1.2; (3.4), (3.11)–(3.13), (3.16), (3.24), (3.31), (3.35);
Proposition 3.18 (3.44)–(3.45), Lemma 3.19 (3.49), and Corollary 3.20 (3.55).
The source labels portions of the higher-order proof as sketches. We import
these estimates as stated; this note proves the operator consequence below.
Selected primary reading and exact limits are in [sources.jsonl](sources.jsonl).

For convenience set w(r)=min(1,r^(-2)), with w(0)=1. These source estimates give

    1/3<=lambda<=1/2,       1/6<=-nu<=2/3,
    |phi|<=C epsilon max(1,r)^(-gamma),
    |phi_v|<=C epsilon min(1,r^(-1)),
    |lambda_v|<=C epsilon^2,
    |lambda_vv|<=C epsilon(A_src+epsilon),
    |K_v|<=C epsilon^2 w(r),
    |K_vv|<=C epsilon(A_src+epsilon) w(r).

The last line uses partial_v^2 K=lambda^2 D^2 K+lambda_v D K.
For lambda_vv, differentiate D log(lambda)=lambda_v/lambda^2 and use (3.45).
The mass bound gives the useful stronger near-axis behavior

    |K|<=C epsilon^2 k(r),
    k(r)=r for r<=1;       k(r)=r^(-1-gamma) for r>=1.

For phi_vv use (3.49)/(3.44) near the axis and (3.13) away from it:

    |phi_vv|<=C(A_src+epsilon)                 if r<=1,
    |phi_vv|<=C epsilon/r                     if r>=1.

The conversion is phi_vv=lambda^2 D^2 phi+lambda_v D phi. Thus no global
constant multiple of A_src is integrated over an arbitrarily long cone without
a decaying weight. Since -r_u=-nu>=1/6, all integrals in u of the displayed
integrable radial weights have bounds independent of the cone vertex.

## 2. Axis coefficient Lambda

On the regular axis u=v=t, K(t,t)=0 and lambda_u=lambda K. Hence

    Lambda(t)=2lambda(t,t),
    Lambda'(t)=2lambda_v(t,t),
    Lambda''(t)=2lambda_vv(t,t)+2lambda(t,t)K_v(t,t).

It follows that

    ||Lambda''||_infinity <= C epsilon(A_src+epsilon).

The formula follows by differentiating the axis trace, not by setting K to zero
before differentiating an off-axis expression. All steps here are for smooth
finite approximants. Lower-regularity closure is a later operation.

## 3. The correction I and its boundary term

Put F=2lambda K phi and I(t)=integral_(u0)^t F(s,t) ds. Since F(t,t)=0,

    I'(t)=integral_(u0)^t F_v(s,t) ds,
    I''(t)=F_v(t,t)+integral_(u0)^t F_vv(s,t) ds.

The boundary term is `F_v(t,t)=2lambda K_v phi`, bounded by C epsilon^3.
Expand the integrand exactly:

    F_vv/2 = lambda_vv K phi + 2lambda_v K_v phi
             +2lambda_v K phi_v + lambda K_vv phi
             +2lambda K_v phi_v + lambda K phi_vv.

Each row is integrable with a vertex-independent bound:

| Term | Bound after u integration |
|---|---|
| lambda_vv K phi | C epsilon^4(A_src+epsilon) |
| 2lambda_v K_v phi | C epsilon^5 |
| 2lambda_v K phi_v | C epsilon^5 |
| lambda K_vv phi | C epsilon^2(A_src+epsilon) |
| 2lambda K_v phi_v | C epsilon^3 |
| lambda K phi_vv, r<=1 | C epsilon^2(A_src+epsilon) |
| lambda K phi_vv, r>=1 | C epsilon^3 |

For the first row the far-radius weight is r^(-1-2gamma), integrable because
gamma>0. For the last row it is r^(-2-gamma). The remaining far weights are at
least as integrable. Near r=0, K=O(epsilon^2 r), K_v and K_vv are bounded, and the
u integration has finite length. Therefore, including the boundary term,

    ||I''||_infinity <= C epsilon^2(A_src+epsilon).        (R3-I)

This makes explicit the part of the original sketch needed for closure.

## 4. Trace operator and closure

Use ||f||_Lip=||f||_infinity+Lip(f) and the corresponding sum norm for C1.
Thus a radius-2M ball satisfies the source's pointwise bound
|f|+|f'|<=2M. Convolution preserves this sum norm.
Let Y=||y''||_essential-sup, assume ||y||_C1<=M, and use zero extensions allowed by
the vanishing neighborhoods in the target hypothesis. Set

    T_n f=chi [Lambda y(tau)-I],       tau'=Lambda,
    a=2Y+1.

Choose the smooth cut-off with 0<=chi<=1 and a fixed C2 bound. It equals 1 up to
tbar=3T_max/2 and vanishes past tbar+1.
Its derivatives meet only y(tau)=0, since tau(tbar)>=T_max. On chi=1,

    (Lambda y(tau))''
      = Lambda'' y(tau)+3Lambda Lambda' y'(tau)+Lambda^3 y''(tau).

Use Lambda<=1, |Lambda'|<=C epsilon^2, the bound for Lambda-double-prime, and
(R3-I). The cut-off derivatives contribute only O(epsilon^3), from I and I'.
With epsilon=2 kappa M and kappa>=1 depending only on the common window,

    ||(T_n f)''||_essential-sup
       <= Y + C epsilon^2 A_src + C epsilon^3.           (R3-T)

For a trial Z with Lip(Z')<=a, f=J_eta Z is smooth and ||f''||<=a, so A_src<=4a.
The outer J also preserves the second-derivative bound. Choose the smallness
threshold, independent of Y, so that

    4C epsilon^2<=1/4,       C epsilon^3<=1/4.

Then the right side of (R3-T) is at most

    Y+a/4+1/4 = (3/2)Y+1/2 <= a.

Together with the separate low-order radius-2M and support checks, this proves
invariance of the convex ball with Lip(Z')<=a. That ball is compact in C0;
indeed the derivative bound also gives C1 compactness. The finite-cone
continuity input and Schauder can therefore be used on this stronger ball.
The constructed physical profiles Psi=J_eta Z retain ||Psi''||<=a, uniformly in
n and eta. The target's Y can be arbitrarily large; it affects the regularity
bound a but not the smallness threshold in M.

This component still relies on the stated source estimates and the separate
continuity/low-order bounds. The project must separately inspect the compact
limit and regular-axis reconstruction before asserting the full C1,1 model
conclusion. No all-order bound, smooth limit, global scattering-map selection
or uniqueness is proved by this second-derivative estimate.
