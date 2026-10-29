# Incoming energy and a conditional late-pulse compensation lemma

**Updated disposition: incoming mass closed in the reduced class; finite-control theorem remains conditional.** The actual incoming boundary energy of a compact profile is \(E_{\rm in}=\frac14\int\Phi^2\), by integrating the exact mass transport law on each fixed finite \(v\)-interval of the global limit. The limit order and hypotheses are detailed in REVIEW_INCOMING_MASS.md. This does not identify the incoming charge with spatial-diagonal ADM mass. Exact finite-dimensional interpolation by degree remains conditional on finite-cone readout continuity, the uniform trace remainder, and joint compactness/readout passage; see REVIEW_DEGREE.md.

## Exact nonlinear flux calculation

Luk–Oh–Yang use (Ric_{μν}=2∂_μφ∂_νφ), (g=-Ω^2du,dv+r^2dω^2), λ=∂_vr, and μ=2m/r. Their equation (2.10), §2.2, states

\[
\lambda^{-1}\partial_vm=\frac12(1-\mu)r^2(\lambda^{-1}\partial_v\phi)^2,
\quad\text{so}\quad
\partial_vm=\frac12\lambda(1-\mu)\bigl(r\lambda^{-1}\partial_v\phi\bigr)^2.
\]

For the global LOY limit with compact incoming profile, §4 gives on past null infinity λ→1/2 and λ⁻¹∂_v(rφ)→Φ(v). Since λ⁻¹∂_v(rφ)=φ+rλ⁻¹∂_vφ and φ→0 at fixed v as r→∞, the radiation limit controls the exact flux. Uniformly on every fixed finite v-interval, the source decay estimates give μ→0 and the lapse and trace estimates give the remaining limits. Exact pre-pulse flatness sets m(u,A)=0. Integrating the mass transport equation from A to fixed v>A yields m_-(v)=¼∫_A^v Φ(s)²ds directly; letting v→+∞ afterward gives the actual incoming boundary energy. No derivative is interchanged with a boundary limit. See REVIEW_INCOMING_MASS.md for hypotheses and estimates.

## Direct finite-cone derivation and limit order

On each approximating cone (C_{u_0}), Luk–Oh–Yang prescribe λ=1/2, λ⁻¹∂_v(rφ)=Φ, and m(u₀,u₀)=0. Their equation (2.17) gives exactly

\[
\phi(u_0,v)=\frac{\int_{u_0}^{v}\Phi(s)\,ds}{v-u_0},
\]

because r=(v−u₀)/2 and λ=1/2 on that cone. Also rλ⁻¹∂_vφ=Φ−φ. Integrating (2.10) from the regular vertex therefore yields the exact nonlinear identity

\[
m(u_0,v)=\frac14\int_{u_0}^{v}(1-\mu(u_0,s))(\Phi(s)-\phi(u_0,s))^2\,ds.
\]

For Φ supported in a fixed compact interval [A,B], the scalar term on [A,B] is O((v−u₀)⁻¹) as u₀→−∞, while r=(v−u₀)/2→∞ there and the cone mass stays bounded, so μ=2m/r→0. For v>B, Φ=0 and φ=C/(v−u₀), where C=∫Φ; the remaining tail contribution is bounded by a constant times C²/(B−u₀) since the source theorem gives 0≤μ<1. Hence, first taking u₀→−∞ at fixed v and then v→+∞, the incoming mass limit is

\[
m_{\rm in}^{\rm cone}(v):=\lim_{u_0\to-\infty}m_{u_0}(u_0,v)=\frac14\int_{-\infty}^{v}\Phi(s)^2\,ds,
\qquad E_{\rm in}^{\rm cone}:=\lim_{v\to+\infty}m_{\rm in}^{\rm cone}(v)=\frac14\int_{\mathbb R}\Phi(s)^2\,ds.
\]

This computes the iterated finite-cone mass limit, first u₀→−∞ at fixed v and then v→+∞, and independently confirms the quarter coefficient. The global fixed-v transport calculation above establishes the actual incoming boundary mass without a moving-vertex interchange.

## ADM mass and limits

The paper defines the initial Bondi mass on an outgoing cone C_{u₀} as lim_{v→∞}m(u₀,v), §1 equation (1.6). That is not the incoming boundary limit lim_{u→−∞}m(u,v), and neither iterated limit is, by definition alone, the ADM limit. On an asymptotically Euclidean spacelike Cauchy slice, ADM mass is the spatial-infinity limit of the Hawking mass; in asymptotically normalized null coordinates this is a joint limit with u→−∞ and v→+∞ along the slice. Identifying it with lim_{v→∞}lim_{u→−∞}m(u,v) requires a uniform asymptotic estimate controlling this joint, diagonal limit. Theorem 1.7 does not state that estimate or call this incoming integral the ADM mass. In an asymptotically flat Cauchy development where the diagonal limit is justified and equals the total incoming Bondi mass, the numerical value is therefore M_ADM=E_in; that equality is conditional here, not inferred from the theorem's geodesic completeness.

## Conditional exact compensation statement

Let Φ₀=Φ_early+a₀ψ_late be a smooth compact profile, with supports separated by a gap, ψ nonzero and compactly supported strictly after the entire marked observer segment on which readings are taken, and a₀≠0. Let Φ̃_early be a sufficiently small smooth compact perturbation supported before that segment. Define

\[
a^2=a_0^2-\frac{\int(\widetilde\Phi_{early}^2-\Phi_{early}^2)\,dv}{\int\psi_{late}^2\,dv},
\]

and take the root a with the sign of a₀. If the perturbation is small enough that the right side is positive, disjointness gives E_in(Φ_early+aψ_late)=¼(∫Φ_early²+a²∫ψ_late²), so the exact incoming energy functional above gives

\[
E_{in}(\widetilde\Phi_{early}+a\psi_{late})=E_{in}(\Phi_0).
\]

No cross term occurs because the supports are disjoint. This exact energy compensation is algebraic in the incoming profile and does not require differentiating a scattering map.

For paired profiles with identical data before the late-tail support, a common sequence of finite-cone vertices gives identical finite-cone solutions on the pre-tail domain by characteristic uniqueness. Taking a joint subsequence preserves equality there and yields existential global limits agreeing on pre-tail readouts; uniqueness among all global limits is not required. This does not imply that independently chosen global limits must agree.

Choose (V_{late}) above the maximum (v)-coordinate attained by the finite observer segment and all events used for the readings. Equality of the selected coupled fields on that wedge implies equality of the central proper-time parameterization and of any scalar or curvature readings along that segment. Future domain of dependence/characteristic uniqueness prevents the later pulse from affecting it. The common exact flat past before the earliest profile support is likewise preserved. A late pulse cannot preserve readings whose events lie in or to the future of its causal influence.

**Lemma (conditional finite-readout energy control).** Assume (i) the exact incoming boundary-mass formula above, (ii) profiles in a uniformly bounded smooth compact class for which the LOY construction applies, and (iii) finite-cone continuity, a uniform remainder, and compactness strong enough to pass clocks and readouts. For paired profiles with a common early part and a nonzero late-tail direction, the displayed amplitude adjustment preserves actual incoming boundary mass exactly; a common finite-cone sequence supplies global limits that agree on every pre-tail readout segment. For early-profile perturbations, the same amplitude formula preserves mass but not the readings; finite-dimensional target interpolation is covered by the degree route and remains conditional on its gates. No canonical solution map or ADM identification is concluded.

**Concrete falsifiers / obstruction checks.** The incoming-mass claim would fail if the pre-pulse integration constant were nonzero, any uniform fixed-interval limit failed, or the coefficient differed from ¼. Paired readout preservation additionally fails if the finite-cone pre-tail solutions are not identical or a readout reaches the tail's causal influence. The degree route fails if finite-cone maps are discontinuous, the uniform boundary remainder is too large, or the n-dependent sequence lacks compactness/readout convergence. At a₀=0 the local two-sided amplitude adjustment is degenerate at the energy minimum. No ADM conclusion follows.
