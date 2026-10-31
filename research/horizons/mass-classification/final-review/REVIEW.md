# Fresh adversarial review: positive-mass fixing classification

Reviewed 27 October 2026. The proof audited here is pinned to `research/horizons/mass-classification/RESULT.md` at SHA-256:

`8142be49585e770d58f871a6c203a8ca7d6da78150dc62151199a35df6409273`

The current `RESULT.md` hash is `b89b8a0510fe58e9500485c1eba65cc749fb22fdec011e25e8cd2f48cdf337ed`. Since the pinned version, the coordinator added the massless-versus-massive comparison, made the already-used one-image specialization explicit as (6a) with its line-kernel factor, and updated the historical review-dependency paragraph to point to the completed reviews. These are bounded scope and clarity updates; no theorem or proof step changed. The mathematical verdict below remains the one recorded against the pinned proof text.

## Verdict

**SURVIVE**, for the exact fixed-background, linear, smooth classical problem and quantifiers stated in that pinned file. I found no fatal mathematical flaw in the proposed classification

\[
F_m(\tau,Y)=J^-(\tau,Y)\quad(0<\tau<\pi),\qquad
F_m(\tau,Y)=M\quad(\pi\leq\tau<2\pi),
\]
for every ordinary constant mass (m>0). This is a review of the argument, not an originality or priority verdict.

The proof's key inference is a joint-support claim, not a claim that either kernel is pointwise nonzero or positive throughout an image cell. On each connected open cell, if both Cauchy traces vanished on a radial interval, source-time local uniqueness would give a spacetime open zero set. Joint real analyticity would then make the velocity kernel zero on the whole cell. The near-diagonal direct limit rules this out in (D_1); the positive antipodal-corner limit rules it out in (D_2). Thus the union of the two Cauchy-kernel supports has no open hole in the relevant causal ball or sphere. This is exactly the strength needed for fixing.

## Independent reconstruction and strongest attempted falsifier

I tried to break the argument at the two-image normalization and at the use of a lower-endpoint derivative as the second Cauchy trace. Let (E(t,s;r)=\tfrac12\mathbf1_{t-s\geq |r|}R(t,s;r)) be the line velocity kernel. Its (2\pi)-periodization has Fourier coefficients (S_{|k|}(t,s)/(2\pi)); differentiating and dividing by (-2\pi\sin r) gives the spherical degree-((k-1)) coefficient (kS_k/(2\pi^2\sin r)). This matches the (S^3) projection kernel. In a one-image cell the factor (1/2) in (E) therefore gives

\[
K=-\frac{R_r}{4\pi\sin r},
\]

so (r=(t-s)/2\downarrow0), (R_r=V(s)r/2+O((t-s)^2)), yields (K\to -V(t)/(8\pi)\ne0). In the two-image cell the image derivative has opposite signs and gives the stated symmetric quotient with denominator (4\pi\sin\epsilon); the second front jet is

\[
R_{rr}(t,s;t-s)=J(t,s)=\frac{V(t)+V(s)}4+\frac18\left(\int_s^t V(u)\,du\right)^2.
\]

At the corner (t-s\to\pi), (r\to\pi), this yields (K\to J/(2\pi)>0). The signs and factors agree with the characteristic coordinates and bounded constant-potential control. I found no lost zero mode: the circle (k=0) term is removed by the radial derivative, while the constant (S^3) harmonic corresponds to (k=1) and is retained.

For the source-variable check, each mode's fundamental matrix (U(t,s)) obeys \(\partial_sU=-U A(s)\), with (A=\begin{psmallmatrix}0&1\\-q(s)&0\end{psmallmatrix}\), (q(s)=k^2+V(s)). Its upper-right entry gives \(\partial_s S_k=-C_k\), and differentiating again gives (S_{k,ss}+q(s)S_k=0). Thus (C=-\partial_s S) supplies the displacement trace, and together with (S) the traces are Cauchy data for the correct backward equation in the source variables. The radial form is

\[
K_{ss}-K_{rr}-2\cot(r)K_r+(1+V(s))K=0.
\]

The sign of (V(s)) and the source, rather than target, time are essential; both check out.

The characteristic Volterra series also survives scrutiny. On each compact complex polydisc the iterated integrals have the independent bounds (M^n|A|^n|B|^n/(n!)^2); normal convergence proves joint holomorphy of this particular Riemann function in ((A,B,s)). Pullback and the two-image formula give joint real analyticity of (K) on each cell. This does not rely on the false generalization that smooth solutions of analytic-coefficient hyperbolic equations are analytic. The cells are connected: (D_1) is an intersection of strict linear half-spaces, and (D_2) is the indicated open triangle. Local uniqueness across the initial source-time slice creates a zero subset with (s>0); the identity theorem is then applied inside the same cell. No continuation across a front or caustic is needed.

I also tested the support-to-fixing step for an endpoint loophole. Vanishing on the open past strip implies zero initial traces on its open ball by smooth extension of the rescaled equation to the auxiliary cylinder. Conversely, compactly supported smooth data in the open exterior of the closed cap yield exact past-zero solutions by finite propagation. If either kernel support meets that open exterior, a compactly supported smooth test datum there detects it; choosing it as velocity or displacement data gives the required counter-solution. The argument does not incorrectly assume that all past-zero smooth data are strictly supported outside the cap. For the reverse inclusion, continuity gives fixing on (J^-(b)). At τ=π the open trace ball omits only the antipode, and smoothness forces both traces to vanish there too; for τ>π the trace ball is all of (S^3). These boundary arguments are sound.

## Correction and limits

No substantive correction is required for the theorem as stated. One clarity edit is advisable in the candidate proof: immediately after (5)–(6), state the one-image-cell specialization (K=-R_r/(4\pi\sin r)). The displayed general formula and image sum imply it, and (11) uses the correct factor, but spelling out the specialization makes the normalization auditable and avoids a factor-of-two misreading.

The conclusion concerns exact solution fixing for all smooth real solutions of the specified rescaled linear equation on this fixed closed-dust background. It does not by itself establish a physical detector/measurement claim, a quantum or finite-energy analogue, an ontology of time, or a source-priority/novelty claim. The literature search and cited predecessor material were not independently audited here; possible prior results on FRW propagators, Riemann functions, spherical kernels, or lacunae remain open for the separate novelty review. The bounded controls check normalizations and a local corner limit, not the global theorem; the proof's global quantifiers stand or fall with the analytic support argument reconstructed above.

## Scope of the massless comparison

The added comparison is consistent with the positive-mass proof and narrows the interpretive takeaway. For 0<τ<π, the reported massless result has a closed three-diamond fixed set, whereas every positive ordinary mass has exactly J⁻(b). Thus the asserted loss concerns all *extra* fixing before maximum expansion; it does not remove the post-maximum fixing common to both cases. At τ=π, both columns give all of M, but this is the dense initial-trace-cap effect: the trace ball is the sphere except for the antipode, and smoothness forces the traces to vanish there too. For τ>π, the trace cap itself is the whole sphere, so all of M is fixed directly. The positive-mass proof stands independently of the massless three-diamond classification; that theorem is needed only to state the comparison. I did not independently re-prove the massless classification.
