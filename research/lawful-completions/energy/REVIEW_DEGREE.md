# Red-team audit: finite-cone degree and passage to a global solution

**Verdict: the degree-before-limit architecture is valid as an existential proof route, conditional on the explicitly listed finite-cone continuity, uniform perturbation, and joint compactness/readout hypotheses. It requires neither differentiable scattering selection nor global uniqueness.** The mass-specific objection is resolved for incoming boundary mass by REVIEW_INCOMING_MASS.md; ADM remains open.

## Degree before the joint limit

For each finite-cone index \(n\), the map \(H_n\) is defined on the same closed parameter ball. If \(H_n\) is continuous and

\[
\sup_{n,|x|\le\rho}|\epsilon^{-1}H_n(x)-x|\le\eta<\rho-|z|,
\]

then the boundary homotopy from \(x-z\) to \(\epsilon^{-1}H_n(x)-z\) avoids zero. Its degree is one, so for each \(n\) there is an \(x_n\) with \(H_n(x_n)=\epsilon z\). This argument is correct and is performed before any subsequence extraction. No derivative of \(H_n\) or limiting scattering map is needed. A separate target-specific subsequence is allowed; the claim is existential for each target, not a single selection map over all targets.

The displayed FINITE_CONTROL.md condition using \(\eta<\rho/2\) works uniformly for every \(|z|<\rho/2\). More generally, choose a target strictly inside the ball and make the remainder smaller than its distance to the boundary.

## N-dependent profiles and exact readout passage

Taking roots \(x_n\) and then a subsequence \(x_n\to x\) is sound only if the compactness argument covers the solutions with the varying profiles \(\Phi_{\epsilon,x_n}\). Here the specific family is favorable: common compact support, smooth finite-dimensional parameter dependence, and \(\beta\) bounded away from the square-root boundary give uniform bounds on each fixed profile derivative; in particular they give the common \(\sup|\Phi''|\) bound needed in Theorem 1.7 and in the higher-order section 4 estimates. The common LOY smallness hypotheses must also hold with one common smallness constant. Under those bounds, the source's uniform-in-vertex estimates and Arzela–Ascoli compactness can be applied diagonally to the n-dependent sequence. A citation to fixed-profile compactness alone would not suffice; the uniform constants are the essential justification.

Compact convergence on finite spacetime sets alone does not recover radiation at past null infinity. FINITE_CONTROL.md addresses this correctly by using the explicit section 4 trace and lapse estimates, first passing \(n\to\infty\) at fixed \((u,v)\) with \(\Phi_{\epsilon,x_n}(v)\to\Phi_{\epsilon,x}(v)\), and then taking \(u\to-\infty\). The estimates are uniform on every fixed compact \(v\)-interval for this uniformly bounded profile class. They identify the limit's radiation data with \(\Phi_{\epsilon,x}\), which is needed before using its charge.

The equation \(H_n(x_n)=\epsilon z\) passes to the limit if the compact convergence is strong enough to pass the axis scalar and the normalized proper-time clocks on the common finite readout window. Uniform positive upper and lower lapse bounds imply convergence of the clock integrals and their inverse parameterizations there. Uniform convergence of scalar fields then passes the readings. The exact flat wedge also passes on compact subsets before \(A\), with its common flat proper-time normalization. These are concrete compactness consequences to verify in the proof; they are not supplied by degree alone.

## Mass and selection audit

The compensated profile identity gives the same exact \(\frac14\|\Phi_{\epsilon,x_n}\|_2^2\) for every \(n\), and smooth parameter convergence preserves that value at \(x\). This profile calculation by itself would not identify the selected global solution's mass. The fixed-\(V\) global transport argument in REVIEW_INCOMING_MASS.md supplies the missing step: for the joint limit with recovered incoming profile \(\Phi_{\epsilon,x}\), exact pre-pulse flatness sets the integration constant to zero, and uniform finite-interval flux convergence yields \(E_{\rm in}=\frac14\|\Phi_{\epsilon,x}\|_2^2\). Thus the common-charge claim is valid for **actual incoming boundary mass** in the reduced solution category under those hypotheses.

The construction's use of target-specific subsequences is not a selection defect for an existential theorem. No uniqueness theorem for the global limit is needed: each target obtains at least one limit carrying that target's readings and the same incoming boundary mass. A stronger claim of a canonical, continuous, or shared selection across targets would need additional hypotheses and is not established.

## Remaining gates and scope

1. Prove, or cite a precise continuous-dependence result proving, that each finite-cone \(H_n\) is continuous on the common parameter ball, including the center and proper clock. Uniqueness of the characteristic solution alone does not formally supply continuous dependence.
2. In the uniform remainder, check that every constant is common in \((n,x)\), including profile, center-clock, and late-tail causal-window bounds. The prompt assigns the trace calculation elsewhere; this review does not redo it.
3. Present the n-dependent Arzela–Ascoli argument with the uniform derivative constants and show convergence of the clocks/readouts. The source's fixed-profile extraction should not be cited without this check.
4. Keep the theorem's category precise. Incoming mass is now accounted for; reconstruction of the reduced axis solution as a regular four-dimensional metric remains the separate regularity gate. The calculation gives no ADM existence or equality with incoming mass.
5. The re-marking example in REVIEW_REMARKING.md shows why abstract pointed-past equality alone does not establish distinct unmarked developments: a fixed abstract mark can be embedded at different flat-era events. FINITE_CONTROL.md appropriately avoids claiming unmarked nonisometry, but substantive novelty or physical-control language must state whether these embedding freedoms are allowed and compare with prior results before promotion.

No novelty conclusion is made. No broad literature survey was performed.

## Source and access

Primary source: Luk, Oh, and Yang, [arXiv:1605.03893v1](https://arxiv.org/abs/1605.03893v1), full text selectively checked 2026-10-28. Theorem 1.7 supplies the global reduced solution hypotheses; section 4, (4.1) and the immediately preceding uniform estimates, supplies compactness bounds and radiation recovery. The degree argument is a standard finite-dimensional consequence of Brouwer degree under the stated continuity and uniform-boundary hypotheses. This audit assesses the coordinator's proposed synthesis; it does not independently certify the uncompleted finite-cone continuity/readout estimates.
