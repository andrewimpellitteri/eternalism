# Agent report: support review

Updated 27 October 2026 after adversarial review of the combined mass-classification derivation.

## Files changed

- `research/horizons/mass-classification/support-review/REVIEW.md` — initial audit and follow-up verdict on the Cauchy-kernel support reduction, spherical geometry, image cells, endpoint and caustic treatment, Volterra analyticity, and the corner tail.
- `research/horizons/mass-classification/support-review/AGENT_REPORT.md` — this report.

No other files were changed. No board or manuscript files were touched. No commit, push, install, large run, or additional agent launch occurred.

## Finding

**Verdict: survives**, within the stated fixed-background smooth classical scope. The characteristic Volterra iteration has the claimed factorial-square bound on compact complex polydiscs, proving joint holomorphy of the special line tail. The exact circle periodization and harmonic projection relation then give joint analyticity of the spherical kernel on each open image cell with the stated normalization. The source-time PDE plus both zero traces gives a spacetime open zero set; connected-cell analyticity propagates it. The direct-cell limit is nonzero for every (m>0) and (0<t<\pi). The independent front-jet derivation confirms the double-image corner limit is positive for every (m>0) and (pi<t<2\pi). Cell closures cover precisely the claimed balls or sphere, and the cap argument handles the boundary correctly.

The critical quantifier correction is recorded: past-zero traces vanish on the closed cap by continuity, while strict exterior bump data suffice for a counterexample when support is not contained in the cap. These are one-way uses; strict exterior data are not claimed to exhaust all admissible smooth traces. At (t=\pi), direct-cell support closure reaches the antipode. For later times, the direct and double-image cell closures cover the two radial intervals on either side of (2\pi-t). At (\tau=\pi), the trace cap is dense and smoothness forces both traces to vanish everywhere.

## Evidence and checks

Read the combined `RESULT.md`, the full independent `front-jet-review/RESULT.md`, the task brief, relevant manuscript sections, and prior ordinary-mass, norm, and recovery reviews. Rechecked the Volterra construction and bound, PDE/coordinate transformations, periodization normalization and image signs, source-time identity, connectedness of cells, two-trace uniqueness step, direct limit, corner limit, support closures, and cap geometry. No external source or novelty search was used. No test was run; the independent corner derivation was inspected algebraically.

## Limitations and unresolved questions

No mathematical gap was found in the supplied combined argument for its stated equation and solution class. This is not an original-source priority audit or a novelty verdict; the manuscript's separate massless theorem has not been independently re-proved here. No counterexample mass was found.
