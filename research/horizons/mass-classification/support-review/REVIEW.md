# Adversarial support review: all-mass fixing claim

Reviewed 27 October 2026; updated after the combined derivation and front-jet review. Scope: audit the reduction from exact fixing to the two Cauchy kernels, the closed-dust-strip geometry, the Volterra analyticity proof, and the image-cell continuation. This review does not claim novelty or independently verify the manuscript's massless classification.

## Verdict

The combined support proof **survives**, within its stated fixed-background smooth classical scope, subject to the precise checks below. Lemma 1's characteristic Volterra series proves joint holomorphy of the special line Riemann tail directly; it does not infer analyticity of arbitrary hyperbolic solutions from analytic coefficients. Periodization then transfers that analyticity to the spherical kernel on each open image cell. The two initial traces give zero Cauchy data for the source-time PDE, hence an open zero set, and the identity theorem propagates it through the connected cell. The direct and double-image nonzero-cell arguments cover every target time in the physical strip. The independent front-jet derivation confirms the sign, factor, and strictly positive corner limit.

I correct one overstatement in the first version of this review: smooth traces vanishing on the closed cap need not be compactly supported strictly in its open complement; their support can meet the cap boundary. The combined proof does not need that equality. Vanishing on the past gives traces zero on the open cap and then on its closure by smoothness. For the converse witness, failure of joint support containment yields a test bump compactly supported in the open complement. This one-sided use is sufficient and handles the boundary correctly.

I found no remaining gap in the stated all-mass/all-target support classification after checking the arguments in `research/horizons/mass-classification/RESULT.md` and `front-jet-review/RESULT.md`. This is a mathematical review of the supplied derivation, not a source-priority or novelty verdict. The original manuscript's separate massless theorem remains a premise only where the result compares fixing sets across mass; the positive-mass classification itself does not require that theorem.

## Exact support reduction

Let (P(t,s)) be the Cauchy evolution for

\[
 u_{tt}+(-\Delta_{S^3}+1+V(t))u=0,
\]

and write its displacement and velocity kernels at target (X) as (C(t,0;X,Z)) and (S(t,0;X,Z)). The identity

\[
 C(t,0;X,Z)=-\partial_s S(t,s;X,Z)|_{s=0}
\]

uses the standard source-time derivative identity for the two-parameter Cauchy propagator. For smooth initial data ((f,g)), the value at ((t,X)) is the distributional pairing with (C f+S g).

For a closed cap (C_Y=\overline B(Y,\tau)), smooth initial traces of a solution vanishing on the chronological past vanish on the open cap and, by continuity, on its closure. Conversely, smooth data compactly supported in the open complement yield past-zero solutions by finite propagation. These two facts suffice; the latter class need not exhaust every smooth pair of traces vanishing on the closed cap. The event ((t,X)) is fixed exactly when

\[
 \operatorname{supp}_Z C(t,0;X,\cdot)\subset C_Y
 \quad\hbox{and}\quad
 \operatorname{supp}_Z S(t,0;X,\cdot)\subset C_Y.
\]

This criterion includes the boundary correctly: a kernel nonzero as a distribution on any open subset of the complement gives a smooth bump datum witnessing nonfixing; conversely support containment annihilates every such datum. It does not require pointwise kernel values at a caustic or at the antipode. “Both kernels” is essential because displacement and velocity data are independently free.

For homogeneous (V), rotational invariance makes these kernels radial in (r=d(X,Z)\in[0,\pi]). If their **joint support** is the closed ball of radius (t) for (0<t<\pi), then the intersection of the two containment conditions is exactly (d(X,Y)+t\le\tau), by the spherical ball-inclusion criterion for τ<π; equivalently the fixing set is (J^-(b)) on the strip. If the joint support is all of (S^3), the criterion fails for every proper cap, so there is no extra fixing outside the causal past.

The cap geometry is sharp. For balls of radii (r_1,r_2<\pi) on the unit sphere, \(\overline B(X,r_1)\subset\overline B(Y,r_2)\) iff \(d(X,Y)+r_1\le r_2\). The forward implication follows by taking a minimizing geodesic from (Y) through (X) and continuing to distance (r_1) (or an approximating direction if (X=Y)); the reverse implication is the triangle inequality. At radius (r_1\ge\pi), the closed ball is the whole sphere. At \(\tau\ge\pi\), the past trace cap is all of (S^3), so vanishing on the past forces zero Cauchy data on the entire auxiliary slice and hence the zero solution; this part of the fixing claim is independent of mass.

## Image cells, endpoints, and quantifiers

For a target conformal time (0<t<2\pi) and source time (s=0), the proposed direct-image interior cell is

\[
 r<t<2\pi-r,
\]

and the double-image cell is \(2\pi-t<r<\pi\). These are the smooth interiors separated by the direct and wrapped null fronts. For (0<t<\pi), the double-image cell is empty; only the direct cell can establish the claimed radius-(t) support. At (t=\pi), the direct cell contains every (0<r<\pi); if a nonzero joint kernel occurs there, its support closure is the whole sphere, including the antipode. Thus the special antipodal coefficient is not needed to conclude whole-sphere support at exactly (t=\pi).

For \(\pi<t<2\pi\), the direct cell covers (0<r<2\pi-t\), while the double-image cell covers (2\pi-t<r<\pi\). Whole-sphere support then requires a nonzero result in the double-image cell (or an independent argument there), not merely the direct near-diagonal tail. The antipode itself can be included by closure when nonzero values approach it; no pointwise evaluation at the caustic is needed. The loci \(r=t\), \(r=2\pi-t\), and \(r=\pi\) are characteristic/caustic boundaries, not smooth interiors for the asserted cell analyticity. They must be reached by support closure, not crossed as though the same smooth-cell formula applied there.

The slice (s=0) is auxiliary. For each smooth solution on the physical open dust strip, choose an interior Cauchy slice and evolve the rescaled equation to (0): the coefficient (V(t)=m^2a(t)^2\) extends smoothly through (0), so ordinary Cauchy well-posedness supplies unique smooth traces. This does not assert physical continuation of the unrescaled field through the dust singularity. In particular, support claims at (t=0) should be read through the auxiliary rescaled equation, while target events remain in (0<t<2\pi).

## Analyticity and open-cell zero audit

The coordinator's Lemma 1 supplies the needed special-kernel argument. With (A=(t-s+r)/2), (B=(t-s-r)/2), its Volterra iterates integrate (V(s+u+v)) over nested rectangles. On any compact complex polydisc, all nested segments stay in a compact coefficient domain. If (M) bounds (V) there, induction gives 
\[
 |H_n(A,B;s)|\le M^n|A|^n|B|^n/(n!)^2.
\]
The resulting series converges normally on every compact polydisc. Parameterizing each complex segment by a real parameter shows every iterate is holomorphic in (A,B,s); local uniform convergence makes the sum jointly holomorphic. Differentiation is valid locally term by term. The integral equation gives (H_{AB}+V(s+A+B)H=0) and unit characteristic-front values. This proves analyticity of this particular line tail, not arbitrary solutions of the hyperbolic equation.

Periodizing the retarded line kernel is exact: its circle Fourier coefficients solve the scalar Cauchy problems with frequencies (k^2+V(t)), with coefficient (S_k/(2\pi)). Differentiating the circle series and dividing by (2\pi\sin r) gives the stated (S^3) harmonic projection kernel, including the sign and factor in (5). On each open image cell only the listed finite images occur; their analytic tails and the nonvanishing denominator (\sin r) give joint analyticity of the spherical kernel. This argument does not cross a wavefront or caustic.

If both initial kernel traces vanish on a radial interval strictly inside one initial cell, the source-time PDE has zero Cauchy data there: the velocity kernel is (K(t,0;r)), and the displacement kernel is (-K_s(t,0;r)). Local hyperbolic Cauchy uniqueness gives a zero on an open set with (s>0). Each cell is connected, so the real-analytic identity theorem makes the kernel identically zero there. The direct near-diagonal limit and the double-image corner limit contradict that conclusion in their respective cells. This step uses both independent traces; spatial analyticity of a single initial trace would not suffice.

## Initial review conclusion (superseded)

The first review treated joint analyticity and the double-image corner coefficient as open dependencies. The combined derivation and independent front-jet review now address them. The conditional theorem below records the logic of the original review; its hypotheses are supplied in the current `RESULT.md`, so this is no longer the final verdict.

The initial review's strongest falsifier was a **proof gap**, not a counterexample: no joint analyticity or substitute unique-continuation theorem had then been established for the global time-dependent Riemann kernel, and the double-image nonzero jet was uncomputed. On that earlier record, the claim

\[
F_m(b)=J^-(b)\quad\text{for every }m>0\text{ and every }b=(\tau,Y),\;0<\tau<\pi,
\]

did not follow. A non-Huygens tail, a perturbative first variation, or nonzero kernels at generic sampled points would not by themselves repair those gaps or exclude exceptional resonant masses.

The conditional statement proposed in the initial review was: fix (m>0), (0<\tau<\pi), and (Y\in S^3); assume joint cell analyticity and local Cauchy uniqueness, nonvanishing somewhere in each direct cell, and (for (t>\pi)) somewhere in each double-image cell. Then the joint support is (overline B(X,t)) for (t<\pi) and all of (S^3) for (\pi\le t<2\pi), implying (F_m(b)=J^-(b)). The combined derivation now supplies these conditions for every fixed positive mass and each target time: the direct-cell limit is (-V(t)/(8\pi)\ne0), and the double-cell corner limit is (J(t,t-\pi)/(2\pi)>0).

No novelty conclusion follows. The proof's scope remains the stipulated linear classical equation on the fixed closed-dust background and exact agreement on the full chronological strip-past.

## Evidence and limits

Read `research/horizons/main.tex` Sections 3–6, the prior ordinary-mass, norm, and recovery reviews, the full combined `research/horizons/mass-classification/RESULT.md`, and the full independent `research/horizons/mass-classification/front-jet-review/RESULT.md`. Rechecked the Volterra iteration bound, variable substitutions, periodization factors/sign, source-time identity and PDE, connectedness of both image cells, direct tail limit, front-jet formula, corner quotient, trace-to-support logic, and cap boundaries. No external mathematical source was consulted and no novelty claim is made.
