# Fixed-spacetime, equal-charge continuum of future readings

Coordinator deduction, 2026-10-28. Conditional geometric theorem; independent reviews pending. No priority or novelty claim. This replaces neither the smoothness audit nor the more demanding control-of-dynamics problem.

## Exact hypotheses

Let (M,g,phi) be one time-oriented classical spacetime with a complete unit-speed timelike geodesic gamma: R -> M. Suppose:

1. For every beta<a, the entire closed causal past J^-(gamma(beta)), its scalar field, and a neighborhood of the marked event are isometric to the corresponding Minkowski past with constant scalar. The identifications send dot-gamma to the same future unit vector. No extra external clock, asymptotic time origin, or radiation-phase mark is included in the prescribed past data.
2. q(tau)=Ric(dot-gamma,dot-gamma) at gamma(tau) is continuous and nonnegative, vanishes for tau<a, and q(tau_*)=q_*>0 at some finite tau_*>a.

The Einstein--massless-scalar normalization Ric=2 dphi tensor dphi makes q=2(dphi/dtau)^2. These hypotheses already contain the necessary classical reconstruction and central nontriviality; the LOY source audit must establish them in the chosen category before applying this theorem to that family.

## Theorem and proof

For every fixed T>tau_*-a, there exists a family of marked spacetimes indexed by y in [0,q_*], each with the **same underlying** (M,g,phi), such that:

- their entire pointed closed pasts, including scalar field and launch tangent, are isometric;
- their launched geodesics exist through the same elapsed proper time T;
- their relational readings Q_y(T) equal y;
- every defined unmarked global spacetime invariant is identical across the family.

Proof: continuity and flatness imply q(a)=0. The intermediate value theorem gives, for each y, some s_y in [a,tau_*] with q(s_y)=y. Set beta_y=s_y-T. Since T>tau_*-a, every beta_y<a. Mark b_y=gamma(beta_y), U_y=dot-gamma(beta_y). The unit-speed launched geodesic is gamma_y(t)=gamma(beta_y+t), hence Q_y(T)=q(s_y)=y. Hypothesis 1 supplies the pointed-past isometries. The unmarked spacetime is literally the same for every y, so an invariant of that unmarked spacetime, if defined, is equal. No formula identifying incoming energy with ADM mass is used. Choosing one s_y for each y does not imply that y -> beta_y is continuous or differentiable. Q as a function of beta is continuous, and its image contains the whole interval; this is the intrinsic set-valued statement.

Distinct readings rule out a field-preserving, time-orientation-preserving global isometry carrying (b_y,U_y) to (b_z,U_z) when y!=z: such an isometry would preserve the launched geodesic and its proper-time-T curvature reading. An isometry between pasts need not extend to a global pointed isometry.

## Scalar-scattering application and remaining gate

In the full regular quotient Q={u<=v}, a compact incoming profile zero for v<A gives an exactly flat wedge v<A by finite-cone uniqueness and compact limits. Causal monotonicity of v places the entire past of any central b with v_b<A inside that wedge. There are arbitrarily early central b, with infinite flat proper-time extent. Thus hypothesis 1 follows once the regular spacetime reconstruction is justified.

A nonzero incoming profile forces a nonconstant central scalar trace if the radial equation Psi_uv=K Psi has locally bounded K through the center and the regular center identities hold. The sideways 1+1 uniqueness argument is recorded in SCATTERING_PAIR.md. Continuity/differentiability of that trace then provides q_*>0. This bounded-K and reconstruction argument remains a source-correspondence gate, not an assumption to suppress.

## Exact strengthening and exact limitations

This gives an interval of one future invariant reading at a common sufficiently large T without profile differentiability, a canonical scattering selection, a second solution, energy compensation, or an identification of incoming energy and ADM mass. If ADM mass exists for this spacetime, all members have exactly the same ADM mass. This does not prove its existence. The same holds for any other unmarked global charge.

The family varies the observer's position relative to the radiation in a fixed spacetime. It is an existential nonprediction construction, not a claim of an ability to alter incoming data while holding an externally fixed observer event or asymptotic phase fixed. Adding an asymptotic time origin and requiring that origin to be aligned across models may distinguish these marked pasts or disallow the construction; that is a different data contract. It is not a new dynamics or a violation of Cauchy uniqueness.

At several times T_1,...,T_N the obtainable vectors lie in the image of the one-parameter curve beta -> (q(beta+T_1),...,q(beta+T_N)); this theorem proves no open N-dimensional range. It also does not supply a continuous inverse selection, arbitrarily prescribed small T at a fixed mass, a self-gravitating detector, or nonisometric unmarked completions.

## Novelty kill test

The marking theorem is elementary once a single nontrivial solution with an infinite exactly flat past wedge is supplied. It should be treated as a corollary/baseline unless a primary prior-work audit establishes a meaningful missing statement. A frontier target must additionally forbid this marking freedom (for example by fixing an external phase/relational anchor) or prove independent multi-reading variation in nonisometric completions. Before imposing such an anchor, verify that it is itself available in the stipulated observer's past; otherwise the strengthened problem silently grants extra information.

## Red-team clarification: what “the same event” can mean

The energy review correctly distinguishes fixed unmarked history from distinct unmarked solutions. However, requiring that b have the same literal manifold label does not invariantly eliminate this construction. Identify each pointed past with one abstract past P, and transport the ambient marked models along those identifications. They then extend the same abstract marked event while remaining distinguishable as pointed extensions by Q(T). A coordinate or set-theoretic demand that the label b stay fixed is insufficient. Requiring globally nonisometric **unmarked** completions, or specifying an additional invariant boundary/relational anchor, is a substantive stronger contract. Calling this merely a coordinate transformation would also be wrong: unequal readings exclude a global isometry of the marked models.

Independent regularity review confirms the field-side quantity 2(dphi/dtau)^2 is continuous in the audited quotient class and can be positive, using the explicit cubic trace estimate. Its identification with Ric(U,U) at the axis in a C2 four-metric still inherits the axis-reconstruction gate. Do not report a fully classical curvature theorem from the quotient calculation alone.
