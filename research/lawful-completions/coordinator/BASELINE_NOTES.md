# Coordinator baseline notes — work in progress

28 October 2026. Agent round launched; no result accepted.

## Nontriviality test

An incoming Vaidya pulse may provide a standard exact Einstein–null-dust
example with the observer past in a flat region. This would defeat novelty
of a mere existence claim. It does not automatically supply a smooth
Einstein–scalar example, global maximal-hyperbolic past matching, or control
at fixed asymptotic charges. Those claims require separate proofs.

A useful matter-model trap is already verified in a primary source:
Faraoni, Giusti and Fahim, *Vaidya geometries and scalar fields with null
gradients*, EPJC81 (2021)232, DOI10.1140/epjc/s10052-021-09040-9, selected
sections equations(8)–(15). It rules out sourcing the ordinary spherical
Vaidya geometry by a massless minimally coupled scalar with null gradient.
The scalar equation imposes vanishing divergence, incompatible with the
expanding radial null congruence. The authors also distinguish allowed
plane-wave examples. Public full text:
https://pmc.ncbi.nlm.nih.gov/articles/PMC7976656/

Our direct restricted check: in the ingoing chart
  g=−(1−2m(v)/r)dv²+2dvdr+r²dΩ²,
for φ=f(v), inverse g^{rv}=1 and sqrt(−g)=r²sinθ give
  □φ=(1/r²)∂r(r² f′(v))=2f′(v)/r.
Thus a nonconstant f(v) fails the massless scalar equation. This is an
ansatz check, not an independent proof of the full source theorem.
Do not identify a null-dust baseline with a scalar-field construction.

## Whole-past proof obligation

Choosing m(v)=0 before v0 suggests a flat past region. To prove equality
of ENTIRE I^-(b) in maximal globally hyperbolic models one still needs:
- a specified manifold, regular center and extension/development;
- monotonicity of the advanced optical coordinate on causal curves;
- exclusion of global causal shortcuts or imported regions;
- matching of matter and pointed observer germ;
- a future geodesic endpoint that exists in both models before singularity.
No such global assertion is certified in this note.

## Runtime

Three isolated GLM workers launched from committed bd95134:
- lawful-completions-priority
- lawful-completions-constraints
- lawful-completions-relational

All three emitted active model/tool events after launch. No terminal
quota failure or completed handback was recorded at the initial check.
Coordinator works on full-past matching and baseline feasibility; lane
outputs must pass source and mathematical review before acceptance.
