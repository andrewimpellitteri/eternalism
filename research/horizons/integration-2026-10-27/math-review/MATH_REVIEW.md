# Mathematics review of the integrated horizons section

Reviewed 27 October 2026. Source reviewed: `research/horizons/main.tex`, SHA256 `fa438d7708a75601b9caff5fd18bcba4712a168c17aa1a5ddc6211383bdce2a3`.

## Verdict

**Nonblocker: the integrated mathematics survives comparison with the reviewed derivations; no new proof gap was introduced by compression.** The mass-loss statement is correctly event/data dependent and conditional on the manuscript's massless fixing theorem for membership in `F_0`. The norm result is an upper bound on every smooth exact-past-compatible alternative in the stated norm-bounded class. The noisy-record and finite-band statements retain their restricted mathematical scope.

This is a proof correspondence review, not a novelty or release-readiness judgment. It does not re-audit the massless three-diamond theorem or its sources.

## Checks against the source derivations

- **Ordinary physical mass and quantifiers.** The equation uses `lambda=m^2`, `q=a^2`, correctly distinguishing ordinary constant physical mass from a constant shift of the rescaled potential. For each fixed standpoint, the proof chooses compactly supported nonnegative data outside the closed cap, establishes exact vanishing throughout the open past by finite propagation, obtains a positive first variation at the endpoint of the auxiliary cylinder evolution, and then fixes an interior target before taking a sufficiently small positive mass interval. The interval is not claimed uniform in data or target. The event lies in the timelike future and in the open physical strip. The conclusion `x_* in F_0(b)` depends on Theorem `thm:diamonds`; the proof says so.
- **Propagator sign and mode/kernel normalization.** The minus sign in the inhomogeneous first-variation equation cancels the minus sign in `S_0(T-u)=-S_0(u)`, giving the positive integral in the manuscript. The separate `k=1` coefficient is `5 pi a_m^2/16`; for `k>=2` it is `3 pi a_m^2/(8k^2)`. The correction `-pi a_m^2 Pi_0/16`, the constant-projector kernel `1/(2 pi^2)`, and the unit-sphere resolvent kernel produce the stated `K(r)`. Its strict positivity follows from `(pi-r)/sin(r)>=1`, including the continuous antipodal value. This supports the pointwise positive first variation required by the proof.
- **Auxiliary endpoint.** The proof evaluates the smooth rescaled solution at `T` only after extending the coefficient and using smooth Cauchy evolution on the auxiliary cylinder. It then chooses a fixed nearby interior point `T-s`; no physical solution value at the dust singularity is asserted. Exact past vanishing follows from data supported outside the closed cap and finite propagation for the full smooth solution, not a finite spectral projection.
- **All-alternative norm estimate.** For spatially homogeneous smooth `q`, the Volterra/Gronwall multipliers give errors bounded by `B/k` in the position propagator and `B/k^2` in the velocity propagator, with `B=|lambda|Q exp(|lambda|Q)`. The position term acts on `Lambda f` and therefore has the additional `1/k`. Combining both coefficient families with the `S^3` addition identity gives squared point-evaluation norm at most `B^2/6`, and `B^2/12` for `f=0`. In the application, smooth extension turns exact past agreement into zero data on `B(Y,tau)`; the free comparison solution vanishes on the same past and at every `F_0` target. Thus the displayed estimate applies to every smooth admissible difference with the stated data norm, not merely to the positive-bump witness. The physical-field factor `1/a(eta)` and the restriction away from singular endpoints are retained.
- **Noisy records and spectral cutoff.** The sequence has unit conformal norm, target value growing as `sqrt(K)`, and full-strip squared field norm at most `pi/K^2`; restriction to the past region can only lower that record norm. The text explicitly says these solutions do not agree exactly on the past and that the example concerns the named field-amplitude norm, not a detector or horizon instability. The finite-cutoff analyticity claim is restricted to the finite spatial mode class and does not imply a cutoff-uniform record estimate.

## Recommended wording correction

No correction is required to make the argument valid. For standalone precision, state in the opening of the ordinary-mass proposition that the dust amplitude `a_m>0` is fixed throughout. It is implicit in the preceding definition of the background and in the source review, but spelling it out avoids reading the mass interval as uniform in the background parameter. Preserve the existing explicit dependency on `thm:diamonds`; do not strengthen the claim to a uniform mass threshold or a characterization of `F_m`.

## Limitations

No long numerical check was run; none was needed to resolve a concrete concern. The finite controls reported in the source reviews are not substitutes for the analytic arguments. This review does not establish detector-level observability, a physical interpretation of the conformal data norm, full massive fixing classification, backreaction or quantum-field results, temporal ontology, novelty, or release readiness.

## Final-source acknowledgment (27 October 2026)

Rechecked the requested small mathematical edits in the current `research/horizons/main.tex`: the proposition now explicitly fixes `a_m>0`, and the application defines `h_m=a(\phi_1-\phi_2)` as the rescaled difference before applying the norm estimate. These edits are consistent with the reviewed scope and do not change the quantifiers or proof dependencies. No repeat proof audit or computational checks were performed. Final source SHA256: `ff095411f7080b01cf5046ed127c4e73b188c0265e4445c524f0f79822734769`.
