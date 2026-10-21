# Clock action correspondence audit

Coordinator codex-clock-audit, 21 October 2026. Submission for independent review.

Files: RESULT.md, check.py, output.txt. Disjoint from the active GLM worker.

Derived exact finite-dimensional criteria for cyclic action, removable scalar
origin, aliases, minimal seed-output representation domain, local reading
covariance and all-input unitary conditioning. Classified cyclic admissibility
for eps=2 with the energy-projector interaction: precisely g^2=k^2-1.
A harmless origin repair removes one apparent disagreement. Generic g fails
on the seed-output domain. Even a resonant valid action at g=sqrt(3) fails
local reading covariance despite commuting with the clock Hamiltonian.

Verification: independent block-exponential 6x6 implementation with no worker
code/eigensolver. Tests check wrap, alias multiplicities, seed orbits, direct
reduction Gram matrices, and invalid finite-average projector diagnostics.
All assertions pass. The first run caught a missing two-dimensional alias at
g=sqrt(8); corrected multiplicity is four, and the text records it explicitly.

Primary reads: Boette–Rossignoli 1806.00956v2 Section II Eqs1–9;
Ludescher et al.2607.24976v1 SectionIV.1 and AppendixB.2 Example32 Eqs58–60.
Full-text at those sections only; exact URLs in RESULT. No full priority audit
or source-code audit. Known finite spectral reasoning; no novelty or ontology
claim. Kepler independently rederived all analytic claims and inspected the checks;
INDEPENDENT_REVIEW.md reports no mathematical refutation, with the stated
units, domains and floating-point verification limits. The active worker's
code and report have not been integrated or silently amended.
