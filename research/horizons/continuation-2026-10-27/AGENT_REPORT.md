# Coordinator report

Task: horizons-perturbation-continuation. Owner: codex-horizons-continuation.
Date: 27 October 2026. Manuscript baseline: 55e2ee7; no manuscript edited.

## Outputs

- RESULT.md: analytical actual-determination-loss construction for a small
  constant rescaled potential, plus a separate argument for an ordinary
  constant physical mass on the closed dust background.
- GATES.md: independently checked selected Manchak/Harte–Drivas passages,
  bounded predecessor audit, remaining source/priority limits and review gates.
- sources.jsonl: three source records with exact reading depth and locators.
- check_perturbation.py and verification.json: bounded spectral, quadrature,
  resolvent-normalization and Duhamel-integral controls.
- AGENT_REPORT.md: this report.

## Work and evidence

Read instructions, project READMEs/NOVELTY, assigned brief, current horizons
paper, where-openness-lives NOTE/VERIFY, coordinator reviews and the actual
GLM submissions. Independently checked primary selected text in Manchak's
22 January 2008 author preprint and Harte–Drivas arXiv:1202.0540v3.
The published Manchak author-copy URL timed out; archive preprint worked.
Ellis–Sciama, Earman and Wald originals remain explicit access gaps.

The key new step is a pair of smooth solutions agreeing on the entire input
past but differing at a timelike-future target formerly fixed by the conformal
scalar. The constant-potential argument evaluates a parameter derivative using
integer-frequency periodicity and a strictly positive elliptic resolvent.
The physical dust-mass argument uses the correct time-dependent rescaled
potential a(t)^2 and its distinct Duhamel first variation. Both keep causal
geometry and the domain-of-dependence guarantee unchanged. Both are submitted
for independent review, not accepted novel results.

## Checks and correction history

The first numerical control, 128/256 spectral modes, failed its convergence
assertion: finite truncation did not approximate the exact compact-support
zero sufficiently well. Preserved diagnostic values were about 4.6e-7 and
1.5e-8 at the unperturbed target. Increased the bounded comparison to
256/512 modes with 4096/8192 quadrature subintervals; no tolerance was loosened.
The final unperturbed residual is about 5.5e-11 and the constant-potential
parameter derivative agrees with the independent positive Green integral
to about 2.3e-12. Signed perturbation samples approach that derivative.

Ordinary dust-mass mode integrals k=1,2,7 were independently checked by
quadrature at 2π and away from the period against the exact Duhamel expression.
The special k=1 coefficient is 5π/16 at a_m=1. Spatial Green normalization
integrates to 1 within floating-point error. The target derivative in the
example is positive under either perturbation model. The script exits nonzero
on any failed check. These are bounded corroborations, not proofs of exact
support or the all-solution claims; those arguments are analytical.

## Limits

No dependency installs, large runs, worker-worktree changes or publication.
The proposition is classical, linear, fixed-background and solution-class
specific. It does not prove a complete perturbed fixed-region classification,
interacting quantum-field result, empirical effect, or temporal ontology.
Exact determination can fail while amplitudes vary continuously (O(delta),
or O(m^2) for ordinary mass). No global novelty or circulation clearance.

Independent GLM review should precede any integration; review the actual
argument, not this report's confidence. The unmodified main paper remains
the active priority and should acquire only a concise extension if justified.
