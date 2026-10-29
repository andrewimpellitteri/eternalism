# Relational future outcome: a conditional lemma and its limits

**Status: CONDITIONAL.** This establishes the kinematic, diffeomorphism-invariant part of the proposed observable. It does not construct two exact solutions of one coupled Einstein–matter theory with identical complete observer pasts. No priority or novelty claim follows.

## Candidate statement

Let \((M_i,g_i,\Psi_i,b_i,u_i)\), for \(i=1,2\), be smooth, time-oriented Lorentzian models, with all matter fields \(\Psi_i\) specified. Let \(b_i\) be events and \(u_i\in T_{b_i}M_i\) future unit timelike vectors, using signature \((-+++ )\). Suppose each metric is smooth on an open neighborhood sufficient to solve the geodesic initial-value problem, and its future unit-speed geodesic \(\gamma_i\) with \(\gamma_i(0)=b_i,\dot\gamma_i(0)=u_i\) exists on \([0,T]\). For any scalar field \(q_i\) (including a scalar formed covariantly from the fields and metric), define

\[
Q_i(T)=q_i(\gamma_i(T)).
\]

If a diffeomorphism \(F:U_1\to U_2\) identifies the metric, the marked event and tangent, and the scalar on neighborhoods containing the respective geodesic segments—\(F(b_1)=b_2\), \(F_*u_1=u_2\), \(F^*g_2=g_1\), and \(F^*q_2=q_1\)—then \(F\circ\gamma_1=\gamma_2\) on \([0,T]\), and \(Q_1(T)=Q_2(T)\).

**Proof.** Isometries preserve the Levi-Civita connection. Thus \(F\circ\gamma_1\) satisfies the geodesic equation for \(g_2\), with initial data \((b_2,u_2)\). Local uniqueness for the smooth geodesic ODE, continued along the common interval, gives \(F\circ\gamma_1=\gamma_2\). Pullback equality of \(q\) then gives the scalar equality at the endpoints. Replacing either model by a diffeomorphic copy leaves this construction unchanged by the same argument. This is a covariance proof, not an existence theorem for coupled solutions or a claim that arbitrary coordinate points in different models can be compared.

## What matching must contain

For the *observable's gauge invariance*, only the pointed observer germ and relevant fields along the segment need be identified by a diffeomorphism/isometry. For the shared target of this project, the stronger hypothesis is an isometry of the **entire** \(I^-(b_1)\) to \(I^-(b_2)\), preserving every matter field there, together with a smooth extension to the marked event that identifies \(g(b)\), the required field values at \(b\), and the future unit vector \(u\). If the claim is meant to match the closed causal past, separately require the map to extend over the relevant part of \(J^-(b)\), including its null boundary. Equality of open chronological pasts alone does not supply that extension, boundary data, or a tangent vector at \(b\). This result assumes those extensions; it does not prove them. The coordinator's full-past construction remains a separate obligation.

The normalization and time orientation of \(u\) matter: proper time \(T\) is measured from that unit future tangent. Without a matched tangent, distinct launches from the same event can sample different fields. With a non-unit vector, the numerical parameter is not proper time unless normalized. The \([0,T]\) existence condition is an actual hypothesis. It can fail because the geodesic exits the spacetime or encounters an inextendible boundary/singularity. Smoothness gives local ODE uniqueness; it does not guarantee existence up to an arbitrary \(T\).

Caustics do **not** destroy uniqueness of one geodesic with fixed initial data. They obstruct injectivity or smoothness of maps built from a congruence (for example, using a family of launches as coordinates), and can make such an extended relational chart ambiguous. The basic single-launch \(Q(T)\) needs no no-caustic assumption. A geodesic may have conjugate points and still be a unique initial-value solution. In a globally hyperbolic development, the result is only asserted while the marked geodesic segment lies in that development; no claim is made about extensions beyond a maximal globally hyperbolic development or about uniqueness among spacetimes with different global boundary conditions.

## Conditional separation criterion

Let \(\mathcal C\) be a specified family of exact solutions to one fixed coupled theory, each equipped with the same prescribed identification of the entire observer past and the pointed germ at \(b\). Suppose two members \(X,Y\in\mathcal C\) have well-defined launched segments through \(T\) and satisfy

\[
q_X(\gamma_X(T))\ne q_Y(\gamma_Y(T)).
\]

Then \(Q(T)\) separates those two pointed models as a diffeomorphism-invariant relational outcome. A useful sufficient *control condition*, stated conditionally rather than as an established GR controllability theorem, is a one-parameter family of exact admissible solutions \(X_\epsilon\in\mathcal C\) whose pointed past and launch data remain fixed and for which \(\frac{d}{d\epsilon}q_{X_\epsilon}(\gamma_{X_\epsilon}(T))|_{\epsilon=0}\ne0\). By differentiability, sufficiently small nonzero \(\epsilon\) then changes \(Q(T)\), so the derivative condition itself supplies a separating pair within the assumed family. The family must satisfy the field equations, constraints, matching, and any imposed asymptotic-charge conditions; a freely prescribed future perturbation is not enough. This derivative condition is falsified if the admissible tangent space has no such direction (or every allowed direction gives zero derivative). Constructing the exact family with the required matching remains an upstream obligation; it is not an additional logical requirement once that family and derivative condition are granted.

For a scalar matter field, setting \(q=\phi\) distinguishes field values but has a symmetry caveat: for a real minimally coupled scalar with an even potential, the transformation \(\phi\mapsto-\phi\) leaves its Klein–Gordon equation and stress tensor unchanged. In a theory where this is a physical global symmetry, \(\phi\) and \(-\phi\) are distinct field-labelled outcomes but are not separated by gravitational observables; if it is quotiented as gauge, \(\phi\) alone is not an observable on the quotient. The choice \(q=\phi^2\) removes this particular sign ambiguity but can still fail to separate models. The stress degeneracy is exact from the standard quadratic kinetic term and even potential, and cautions against treating a difference in matter labels as a difference in geometry.

Curvature scalars are diffeomorphism invariant but not a complete detector. Schmidt's exact plane-wave example is nonflat while all curvature invariants of the stated type vanish; the vacuum pp-wave discussion makes the same warning directly relevant to gravitational radiation. Therefore equality of polynomial curvature scalars cannot generally certify equality of local tidal physics. For Weyl curvature define the electric part relative to the marked unit velocity by \(E_{ab}=C_{acbd}u^cu^d\). The contraction \(E_{ab}E^{ab}\) is an observer-defined scalar using \(u\) and \(g\); no spatial triad is needed, though the contraction may vanish or be degenerate in special geometries. Comparing individual frame components of \(E_{ab}\), or a component-level geodesic-deviation response, requires a matched orthonormal spatial triad or specified transported frame in addition to \((b,u)\).

This \(Q\) is an ideal-probe functional on a solution, not a self-gravitating detector. A physical detector claim additionally specifies detector degrees of freedom, initial state, coupling, trajectory/backreaction, readout and noise; then the measured record must be shown to differ. No such detector is supplied here.

## Falsifiers and scope

The covariance lemma would fail if the identification ceased to be an isometry, failed to map the marked unit tangent, or the required geodesic segment did not exist. Its conditional separation application fails if no exact same-theory solutions with the required entire-past match and nonzero \(Q\)-change exist. A numerical perturbation, a finite diamond match, or constraint data without a justified development does not satisfy the criterion. A Cauchy region whose uniqueness domain already covers the entire relevant future would also block the proposed separation there.

The source review supports the relational-observable motivation and two specific scalar-invariant cautions; it does not establish newness, full-past matching, matter-realizable gluing, local controllability, or a fixed-theory counterexample. The result is consequently a bounded kinematic lemma plus a sharp conditional obstruction to overclaiming.
