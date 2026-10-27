# Independent front-jet and spherical-corner review

## Result

For the stated retarded kernel, the proposed second radial front jet is correct. With \(T=t-s>0\), at the right front \(r=T\), derivatives taken in \(r\) while holding \(t,s\) fixed give

\[
R=1,\qquad R_r=\frac12 I(t,s),\qquad
R_{rr}=J(t,s):=\frac{V(s)+V(t)}4+\frac{I(t,s)^2}{8},
\quad I(t,s)=\int_s^t V(x)\,dx.
\]

For the double-image region \(T>\pi\), \(2\pi-T<r<\pi\), the kernel specified in the brief has corner limit

\[
\lim_{T\downarrow\pi,\ r\uparrow\pi} S_3(t,s;r)=\frac{J(t,s)|_{t-s=\pi}}{2\pi}>0.
\]

The limit is joint and path-independent within that region. This is a local corner calculation; it proves no global all-mass or all-target support/fixing statement.

## Goursat derivation

Set \(u=T-r\), \(v=T+r\), so \(t=s+(u+v)/2\), \(r=(v-u)/2\), and the right/left characteristic fronts are \(u=0\), \(v=0\). In the interior the equation is

\[
4R_{uv}+V\!\left(s+\frac{u+v}{2}\right)R=0,
\quad R(0,v)=R(u,0)=1.
\]

Its characteristic Volterra equation is

\[
R(u,v)=1-\frac14\int_0^u\! da\int_0^v\! db\ V\!\left(s+\frac{a+b}{2}\right)R(a,b).
\]

It directly gives, on \(u=0\), \(R_v=R_{vv}=0\),

\[
R_u(0,v)=-\frac14\int_0^v V(s+b/2)db=-\frac12 I(t,s),
\quad (v=2T).
\]

Differentiating the integral equation twice in \(u\) and then restricting to \(u=0\) yields

\[
R_{uu}(0,v)=-\frac18\int_0^v V'(s+b/2)db
 +\frac1{16}\int_0^v V(s+b/2)\int_0^b V(s+c/2)dc\,db
 =-\frac{V(t)-V(s)}4+\frac{I^2}8.
\]

At fixed \(t,s\), \(\partial_r=-\partial_u+\partial_v\), hence \(R_r=-R_u+R_v=I/2\) and \(R_{rr}=R_{uu}-2R_{uv}+R_{vv}\). The PDE gives \(R_{uv}=-V(t)/4\) at the right-front point. Therefore

\[
R_{rr}= -\frac{V(t)-V(s)}4+\frac{I^2}8+\frac{V(t)}2
 =\frac{V(s)+V(t)}4+\frac{I^2}8.
\]

This explicitly uses fixed-\(t,s\) radial differentiation. Differentiating along the moving front \(r=t-s\) would be a different derivative and is not the calculation above. Smoothness up to the characteristic follows locally from the Volterra equation for smooth \(V\); here \(V\) is analytic.

## Spherical image sign, factor, and path

Write \(T=\pi+\alpha\), \(r=\pi-\epsilon\), where \(0<\epsilon<\alpha\). Both image arguments are strictly inside their cones. Put

\[
W(T,d)=R_r(t,s;T-d),
\]
where \(d\) is the inward distance from the right front. Then the chain rule in the second image gives

\[
\partial_r E(t,s;r)+\partial_r E(t,s;2\pi-r)
=\tfrac12\{W(T,\alpha+\epsilon)-W(T,\alpha-\epsilon)\}.
\]

Thus the stipulated \(S_3\) equals

\[
\frac{W(T,\alpha-\epsilon)-W(T,\alpha+\epsilon)}{4\pi\sin\epsilon}.
\]

Since \(W_d(T,0)=-R_{rr}(t,s;T)=-J(t,s)\), smoothness gives numerator \(2\epsilon J(t,s)+o(\epsilon)\) as \((\alpha,\epsilon)\to(0,0)\) with \(0<\epsilon<\alpha\). More strongly, the symmetric difference quotient is \(-2W_d(T,\alpha)+O(\epsilon^2)\) locally, so it tends to \(2J(s+\pi,s)\) uniformly over such paths. Since \(\sin\epsilon/\epsilon\to1\), the stated limit is \(J/(2\pi)\). The chain sign and the factor \(1/2\) from \(E\) are both needed for this factor and positive sign.

For \(V(t)=\mu(1-\cos t)^2/4\), \(\mu>0\), one has \(V\ge0\) and \(I>0\) on every interval of positive length (the integrand is nonzero except at isolated points). Consequently \(J>0\), including at length \(\pi\). Explicitly

\[
I(t,s)=\frac{\mu}{4}\left[\frac32(t-s)-2(\sin t-\sin s)+\frac14(\sin 2t-\sin 2s)\right].
\]

## Exact constant-potential control

For bounded constant \(V=c\ge0\), the exact Riemann function is

\[
R(T,r)=J_0\!\left(\sqrt{c}\sqrt{T^2-r^2}\right)
=\sum_{n=0}^{\infty}\frac{(-c/4)^n(T^2-r^2)^n}{(n!)^2}.
\]

This convergent series solves \((\partial_T^2-\partial_r^2+c)R=0\) and equals 1 on both fronts. At \(r=T\), its first two radial derivatives are \(cT/2\) and \(c/2+c^2T^2/8\), exactly the formulas above with \(I=cT\). Applying the same two-image quotient gives \((c/2+c^2\pi^2/8)/(2\pi)>0\) at \(T=\pi\). This is an exact bounded control, not evidence for global fixing at all masses.

## Scope and unresolved issue

The computation establishes a strictly positive limiting value for this particular double-image kernel at the first antipodal corner, for every \(\mu>0\). Continuity then gives positivity in some interior neighborhood for each fixed \(s,\mu\). It does not show positivity throughout the double-image region, exclude cancellation at other radii/times, establish full Cauchy-data kernel support, or settle exact all-smooth future fixing for every positive mass. Those global quantifiers remain unresolved here.


## Bounded audit of coordinator Lemmas 1–3 (27 October 2026)

I checked the three named lemmas in `research/horizons/mass-classification/RESULT.md` only; this is not a review of the global no-hole or cap argument.

**Lemma 1, normal convergence.** The stated bound is valid on each compact polydisc after taking a compact set containing all straight nested segments \((\theta A,\eta B,s)\), \(0\le\theta,\eta\le1\). If \(M_V\) bounds \(|V(s+u+v)|\) there, induction on the iterates gives

\[
|H_n(A,B;s)|\le M_V^n\frac{|A|^n|B|^n}{(n!)^2}.
\]

The two factorials come from the independent ordered integrations in \(u\) and \(v\). The majorant series converges on every compact set, hence normally, and the same Volterra iteration gives uniqueness. Since \(V(t)=m^2a_m^2(1-\cos t)^2/4\) is entire, \(H\), and therefore its linear pullback \(R(t,s;r)\), is jointly entire. This justifies the local termwise differentiations used below and does not imply analyticity of arbitrary smooth PDE solutions.

**Lemma 2, normalization and source-time equation.** Periodizing the even line kernel gives Fourier coefficient \(S_{|k|}(t,s)/(2\pi)\) for each integer mode \(k\), hence the displayed cosine series with coefficients \(1/\pi\) for positive modes. Differentiating gives

\[
-\frac{\partial_r E_{\rm per}}{2\pi\sin r}
=\sum_{k\ge1}\frac{k\sin(kr)}{2\pi^2\sin r}S_k(t,s),
\]

which matches the stated degree-\((k-1)\) projection normalization. For the source-time derivative, the scalar mode fundamental matrix satisfies \(\partial_s U(t,s)=-U(t,s)A(s)\), \(A=\begin{psmallmatrix}0&1\\-q(s)&0\end{psmallmatrix}\), \(q=k^2+V\). Its upper-right entry is \(S_k\), and the matrix product gives \(\partial_s S_k=-C_k\), so \(C=-\partial_s S\). Also \(\partial_s^2 S_k+q(s)S_k=0\): differentiating the matrix identity a second time gives \(U A^2-U A'\); the upper-right component of \(UA'\) is zero and \(A^2=-qI\). This verifies the backward equation (9), including the \(+1+V(s)\) term for \(\Lambda^2+V\), and its radial form (10), away from fronts and distributionally as stated.

**Lemma 3, direct limit and corner insertion.** The Taylor expansion used there is consistent: with \(A=(h+r)/2\), \(B=(h-r)/2\), \(H=1-V(s)AB+O((|A|+|B|)^3)\), so at fixed \(t,s\), \(R_r=V(s)r/2+O(h^2)\) along \(r=h/2\). Only the direct image is active for small \(h=t-s\); therefore

\[
K=-\frac{R_r}{4\pi\sin r}\longrightarrow-\frac{V(t)}{8\pi},
\]

which is nonzero for the coordinator's physical potential at every \(0<t<2\pi\), \(m>0\), and \(a_m>0\).

For the double-image cell, the coordinator's \(H\)-derivatives on \(B=0\) give \(H_A=H_{AA}=0\), \(H_B=-I\), \(H_{AB}=-V(t)\), and \(H_{BB}=-V(t)+V(s)+I^2/2\). Applying \(\partial_r=(\partial_A-\partial_B)/2\) at fixed \(t,s\) reproduces (12) exactly. In (13), \(r=\pi-\epsilon\), the two interior arguments are \(\pi-\epsilon\) and \(\pi+\epsilon\); the chain rule makes the image derivative their difference in the order shown in the coordinator result. Equivalently, with \(T=\pi+\alpha\), their inward front distances are \(\alpha+\epsilon\) and \(\alpha-\epsilon\). The symmetric quotient tends path-independently to \(J/(2\pi)\), with the same sign and factor as the independent derivation above.

The earlier constant-potential check is a control of the characteristic jet and image quotient, not an additional assertion about the coordinator's dust background. For its potential, the parameter mapping is \(\mu=m^2a_m^2\).

**Audit boundary.** I found no correction needed in Lemmas 1–3. This bounded check does not assess Lemma 4, the global joint-support/no-hole argument, cap geometry, or theorem acceptance/novelty.
