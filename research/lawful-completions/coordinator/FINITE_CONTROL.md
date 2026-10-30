# Candidate finite scalar interpolation at fixed actual incoming mass

2026-10-28. Proof synthesis under explicit audit gates; not yet accepted as a smooth four-dimensional GR theorem, and not a novelty claim.

> **29 October repair update:** The GLM Lipschitz proof was rejected. [COMPACTNESS_CONTINUITY_REPAIR.md](COMPACTNESS_CONTINUITY_REPAIR.md) supplies a replacement continuity/compactness proof using the primary uniform bounds and characteristic uniqueness. It is a coordinator proof awaiting independent review; gates 1-2 below are not accepted solely on the worker submission. Classical four-dimensional axis reconstruction remains open.


> **30 October category update:** The source and Cartesian lift reviews
> are integrated. AXIS_C11_RECONSTRUCTION.md now supplies a conditional,
> internally reviewed C¹,¹ four-metric/scalar and unique centered geodesics.
> This repairs the geometric interpretation of scalar clock readouts at
> that regularity. It supplies no C²/smooth MGHD upgrade. A new independent
> finite-control review must still audit continuity, degree, varying-profile
> compactness and the complete interpolation statement below.

## Precise proposed statement

Fix a finite N and proper times 0<T_1<...<T_N. For sufficiently small pulse scale epsilon, seek an open ball of signed scalar reading vectors near zero realized by global LOY reduced solutions with:

- the same full pointed flat causal past at a central launch b, including constant scalar and unit launch tangent;
- the same positive incoming boundary mass E_in=(1/4) integral Phi^2;
- central readings phi(gamma(T_j))-phi(b) equal to the chosen vector.

These are solutions in the source's audited quotient class, with a reconstructed central clock. Promotion to smooth four-dimensional maximal developments remains gated by axis-metric reconstruction. The claim fixes incoming boundary mass, not ADM mass, and uses the real scalar without quotienting its sign. It does not yet require unmarked spacetimes to be globally nonisometric.

## Data family

Choose t_b<A<t_b+T_1 and smooth compact functions F_k with disjoint supports near t_b+T_k, all above A, with F_k(t_b+T_j)=delta_kj. Choose a nonzero smooth compact G supported after the entire common readout coordinate window. Set

 Phi_{epsilon,x}=epsilon [sum_k x_k F_k + beta(x)G],
 beta(x)=sqrt(beta_0^2 - sum_k x_k^2 ||F_k||_2^2/||G||_2^2).

Choose a closed parameter ball |x|<=rho on which beta is smooth and bounded away from zero. Every profile has exactly the same norm squared epsilon^2 beta_0^2 ||G||_2^2, with no cross terms. This compact finite-dimensional class has uniform support and uniform derivatives of every fixed order. Its LOY smallness parameter is at most C_0 epsilon for a fixed class constant C_0. Place G sufficiently late using the uniform central lapse lower bound; its values at all t_b+T_j are zero.

## Finite-cone maps and a degree argument

For a common sequence u_n -> minus infinity, let H_n(x) be the N-vector of the exact finite-cone central proper-time readings launched at t_b. All sufficiently early vertices put b in the exact flat wedge. The cubic source estimate and clock argument in CUBIC_TRACE.md give

 sup_{n,|x|<=rho} |epsilon^{-1}H_n(x)-x| <= C epsilon^2.

If H_n is continuous on the ball, choose epsilon so C epsilon^2<rho/2. For each |z|<rho/2, the homotopy x+s(epsilon^{-1}H_n(x)-x)-z never vanishes on the boundary |x|=rho. Its degree is that of x-z, namely one. Therefore some x_n has H_n(x_n)=epsilon z. No derivative of H_n, let alone of a limiting scattering map, is used.

## Passage to the global solution

Extract x_n -> x. The profiles converge smoothly because the parameter family is finite-dimensional and beta smooth. The source estimates, including the higher finite-order bounds, have constants uniform on this family. Apply the section 4 compactness argument to these n-dependent finite-cone solutions, retaining the parameter subsequence. On each fixed compact set the limiting equations and regular-axis identities persist.

The section 4 estimates for lambda and normalized partial_v(r phi) have constants uniform on the same family. First passing n -> infinity at fixed (u,v), with Phi_{epsilon,x_n}(v) -> Phi_{epsilon,x}(v), then sending u -> minus infinity recovers that limiting incoming profile. Thus it is not identified from compact convergence alone.

Compact convergence of phi and lambda passes the normalized central clocks, their inverses on the fixed readout window, and hence the exact equations H_n(x_n)=epsilon z to the limit. The exact flat wedge survives. INCOMING_MASS.md then identifies the actual incoming boundary mass with the common quarter-norm, if that derivation passes review. This establishes the target readings existentially for every |z|<rho/2; solutions for different targets may be selected on different subsequences.

## Remaining acceptance gates

1. **Finite-cone continuity:** verify or prove the continuous dependence of the source's characteristic solutions on this compact smooth parameter family, including the axis and clock, on every finite readout triangle. Source local wellposedness strongly suggests this, but a bare uniqueness assertion is not itself a proof of continuity. The finite triangle grows with n; continuity need not be uniform in n for degree, whereas the cubic remainder must be uniform.
2. **Parameter-uniform compactness:** explicitly audit the source's compactness proof with n-dependent profiles. Uniform derivative bounds and uniform initial hypotheses must control every constant; a pointwise-in-profile subsequence statement alone is insufficient.
3. **Global mass identification:** independently check INCOMING_MASS.md, including pre-pulse integration constant, normalization, uniform finite-v limit, and transport equation in the limiting class.
4. **Four-dimensional category:** close the regular-axis reconstruction before calling the result a classical C2/smooth MGHD theorem. Field-side scalar and central proper-time calculations do not automatically prove this.
5. **Novelty and substantive strength:** compare with known scattering/control corollaries. Exclude timing/marking freedom if the intended result is nonisometric unmarked completions, and do not claim independent physical control merely from an unexamined solution selection.

This route removes the need for a differentiable scattering map from the finite-interpolation proof architecture. It does not establish arbitrary function-space record control, ADM equality, or a detector model.


## Stronger bounded assembly, 30 October

[C11_FINITE_CONTROL.md](C11_FINITE_CONTROL.md) states the full C¹,¹ candidate,
including the external input list, explicit profile smallness, exact
flat-wedge proof, parameter/vertex limit order, actual incoming mass,
Cauchy-time bound and finite Boolean-independence corollary. The integrated
adversarial review stopped at GLM quota; direct coordinator rechecking
supplies no completed independent review. Smooth MGHD, pointwise axis
curvature and novelty remain separate gates.
