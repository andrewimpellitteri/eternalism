# Red-team audit: actual incoming boundary mass

**Verdict: the proposed fixed-\(V\) global-limit argument closes the incoming Hawking-mass boundary limit in LOY's reduced global solution class, conditional on the stated source regularity and compact-profile hypotheses.** It does not identify that iterated null-boundary charge with ADM mass.

## Calculation and normalization

LOY normalize \(\operatorname{Ric}=2\,d\phi\otimes d\phi\), \(\mu=2m/r\), and \(\lambda=\partial_v r\). Their exact transport equation (2.10) is

\[
\partial_v m=\frac12\lambda(1-\mu)r^2(\lambda^{-1}\partial_v\phi)^2.
\]

Writing \(\psi=\lambda^{-1}\partial_v(r\phi)\) gives the exact identity \(\psi-\phi=r\lambda^{-1}\partial_v\phi\), so

\[
\partial_v m=\frac12\lambda(1-\mu)(\psi-\phi)^2.
\]

For a smooth compact incoming profile supported in \([A,B]\), the finite-cone solutions are exactly flat in the pre-pulse wedge \(v<A\): zero scalar characteristic data and regular-axis boundary conditions give \(m=0,\lambda=1/2,\nu=-1/2,\phi=0\) there by characteristic uniqueness. On compact subsets of that wedge, the same holds in a section 4 global limit. Continuity to the edge yields \(m(u,A)=0\) for each \(u<A\).

Fix finite \(V>A\). The global transport equation therefore gives

\[
m(u,V)=\int_A^V\frac{\lambda(u,v)}2(1-\mu(u,v))(\psi(u,v)-\phi(u,v))^2\,dv.
\]

Every limit used here is uniform on this fixed interval as \(u\to-\infty\):

- From the global bounds \(\lambda>1/3\), \(r(u,v)=\int_u^v\lambda(u,v')\,dv'\ge(v-u)/3\), so \(r\to\infty\) uniformly for bounded \(v\).
- Theorem 1.1 / Proposition 3.3 gives \(|\phi|\le C\epsilon\min(1,r^{-\gamma})\), hence \(\phi\to0\).
- Proposition 3.4, (3.16), gives \(m\lesssim\epsilon^2\min(r^3,r^{1-\gamma})\). Thus \(\mu=2m/r=O(\epsilon^2r^{-\gamma})\to0\) for large \(r\).
- Section 4, after (4.1), bounds \(|\log\lambda-\log(1/2)|\lesssim\epsilon^2\max(v-u,1)^{-\gamma}\), so \(\lambda\to1/2\) uniformly.
- The same passage gives the normalized radiation trace: its finite-cone error is bounded by \(C\epsilon^3\max(v-u,1)^{-2\gamma}\), with the factor \(\lambda(u_n,v)/\lambda(u,v)\) tending to 1. After the global limit, this yields \(\psi\to\Phi(v)\) uniformly on the fixed interval. Consequently \(\psi-\phi\to\Phi(v)\).

The flux integrand thus converges uniformly to

\[
\frac12\cdot\frac12\cdot1\cdot\Phi(v)^2=\frac14\Phi(v)^2.
\]

Integration over fixed \([A,V]\) proves the actual global boundary limit

\[
m_-(V):=\lim_{u\to-\infty}m(u,V)=\frac14\int_A^V\Phi(v)^2\,dv.
\]

For \(V\le A\), it is zero. Since \(\Phi\) is compactly supported, the subsequent limit \(V\to+\infty\) exists and equals \(E_{\rm in}=\frac14\int_{\mathbb R}\Phi(v)^2\,dv\). This is an iterated incoming boundary limit: first \(u\to-\infty\) at each finite \(V\), then \(V\to+\infty\). No derivative is interchanged with a limit, and no moving finite-cone vertex is used. Exact flatness fixes the integration constant; absent it, a residual mass term would remain possible.

## N-dependent profile sequences and scope

The section 4 proof is written for a fixed \(\Phi\), so applying it to the degree construction requires uniformity across the compact parameter family. The family in FINITE_CONTROL.md supplies the needed structure if its common support, LOY smallness conditions, and profile derivative bounds are uniform. In particular, the uniform second-derivative bound required by Theorem 1.7 / (1.20) controls the higher-regularity compactness constants; smooth finite-dimensional parameter dependence with \(\beta\) bounded away from its square-root boundary supplies such bounds. Along a convergent parameter subsequence \(x_n\to x\), \(\Phi_{\epsilon,x_n}\to\Phi_{\epsilon,x}\) smoothly. The section 4 estimates are uniform in cone vertex, and their displayed radiation errors are uniform on each compact \(v\)-interval. Passing first to the joint compact limit and then to \(u\to-\infty\) therefore identifies its incoming radiation with \(\Phi_{\epsilon,x}\), not merely the compact-region field limit.

Applying the fixed-profile mass calculation to that resulting global solution proves its **actual incoming boundary mass** is \(\frac14\|\Phi_{\epsilon,x}\|_2^2\). Thus the exact charge compensation survives the degree/subsequence passage for incoming mass, under the uniform-family hypotheses above. This closes the mass-specific gate in FINITE_CONTROL.md; it does not close its finite-cone continuity, parameter-uniform compactness, or four-dimensional reconstruction gates.

Nothing here proves existence of the spatial diagonal limit \(\lim_{r\to\infty}m(t-r,t+r)\), or equality of that ADM mass with \(E_{\rm in}\). No ADM claim should be attached to the degree result on this evidence.

## Primary source and access

Luk, Oh, and Yang, [arXiv:1605.03893v1](https://arxiv.org/abs/1605.03893v1), full text selectively checked 2026-10-28. Normalization and equations: (1.1), (1.2), (2.10), and initial gauge/profile definition (printed pp.1–2, 8–9). Decay: Theorem 1.1 (1.8)–(1.9), Proposition 3.3, Proposition 3.4 (3.16), printed pp.11–18. Global limit, regularity bounds and radiation recovery: Theorem 1.7 and §4, especially (4.1) and the estimates immediately preceding it, printed pp.5–6 and 27–29. The fixed-\(V\) integration is a deduction from these exact estimates, not a separately stated mass theorem in the paper. Source access was direct to the versioned arXiv HTML/PDF; no broad literature survey was performed.
