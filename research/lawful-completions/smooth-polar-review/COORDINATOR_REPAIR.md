# Coordinator correction to the bounded polar audit

30 October 2026. The raw RESULT.md uses the phrase “Poincaré/radial
integration with c(0)=1” for the zeroth-order norm. A generic point-trace
Poincaré inequality is invalid in dimension three. Do not use it.

The valid bound follows directly from

    c−1=exp[R² T₁(Z/f)]−1,

the L² boundedness of T₁, multiplication by R² on a finite ball, and the
L∞ bounds on the exponent. The identity ∇c=cXZ/f then supplies the
extra derivative. At higher orders use the tame product/composition
estimates on this same explicit formula. This proves the intended
estimate without a point trace.

The source note also now gives the explicit C¹,¹ flow/inverse and
Cartesian Hessian argument and the uniform lower-endpoint J_s estimate
requested by the audit. The coordinator checked those repairs directly.
The bounded worker audit is not expanded into an independent review
of the exterior proof or local persistence theorem.
