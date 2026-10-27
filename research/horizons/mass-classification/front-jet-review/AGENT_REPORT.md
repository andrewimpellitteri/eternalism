# Agent report: independent front-jet review

## Files changed

- `research/horizons/mass-classification/front-jet-review/RESULT.md` — independent characteristic Volterra derivation, spherical image quotient, positivity conclusion, and constant-potential control.

## Evidence and checks

- Re-derived the right-front derivatives from the Goursat equation in characteristic variables, with radial derivatives explicitly at fixed \(t,s\).
- Checked the second-image chain-rule sign and retained the factor \(1/2\) in \(E\); the smooth double-image corner quotient tends to \(J/(2\pi)\), independent of the allowed approach path.
- Checked the formula against the exact convergent Bessel power series for constant potential \(c\ge0\).
- For the stated time-dependent potential, \(V\ge0\) and its integral on every positive interval is strictly positive, so this corner value is positive for every \(\mu>0\).

## Limits and unresolved questions

This is a local kernel calculation, not a support-based proof of global exact solution fixing. No claim is made about positivity throughout the full double-image region, all target times, exceptional resonances, or global Cauchy-data kernel support. The project-level all-positive-mass/all-target question remains open on the evidence of this sidecar.

## Checks

The derivation and constant-potential series were checked algebraically in this report. No tests, external sources, installs, large runs, or repository-level edits were made.


## Follow-up: coordinator Lemmas 1–3 audit

- Read `research/horizons/mass-classification/RESULT.md` and checked only Lemmas 1–3 as requested.
- Verified the compact-set Volterra majorant, line-to-sphere Fourier/projection factor, source-endpoint matrix identity and backward scalar PDE, the direct near-diagonal limit, and the front-jet/corner substitution. No correction was found.
- Confirmed the direct limit is \(-V(t)/(8\pi)\), nonzero for the coordinator's positive-mass dust potential on \(0<t<2\pi\), and the double-image corner coefficient remains \(J/(2\pi)\).
- Did not audit or endorse the no-hole/cap proof, global classification, or any novelty claim.
