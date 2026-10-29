# Agent report: scattering regularity

**Submission status: complete; coordinator review pending.**

## Files changed

- `research/lawful-completions/regularity/RESULT.md`
- `research/lawful-completions/regularity/sources.jsonl`
- `research/lawful-completions/regularity/AGENT_REPORT.md`

## Evidence and result

Read the assigned project instructions and brief, the coordinator's contract,
scattering pair, next-candidate note and round-one status, plus
`collapse-extension/SCATTERING_FOLLOWUP.md`. Deep-read the relevant parts of
Luk–Oh–Yang arXiv:1605.03893v1: Theorem 1.1 and Theorem 1.7, equations
(1.8)–(1.9) and (1.20), the axis setup in §2, Proposition 3.18 and estimates
(3.44)–(3.47) in §3.8, and the compactness passage and Remark 4.1 in §4.
Checked Kilgore arXiv:2108.13377v1 §§1, 3–5 and 7 as a directly relevant
published-method follow-up.

LOY proves uniform finite-order estimates for the reduced variables and a
quotient compactness limit. Its §4 convergence statement is specifically
`C¹` for `φ` and the first derivatives of `rφ`, `C²` for `r`, and `C¹` for
`m`. Proposition 3.18 improves the approximant estimates at third quotient
order for `rφ` and second normalized order for `log λ`, `log ν`, but does not
state the regular-chart `C²` metric estimate at the axis needed to upgrade the
compact limit to a `C²` four-metric. `C∞` needs all-order estimates uniform in
the cone parameter and an all-order axis reconstruction. The Kilgore paper
does not supply these for this family: it explicitly excludes direct control
of the LOY past-null-infinity solutions.

Profile differentiability is separate. The checked theorems do not establish
parameter-uniform linearized/difference-quotient estimates, convergence of
those derivatives as `u₀→−∞`, or uniqueness/canonical selection for the
profile-to-limit map. The report names the exact missing lemmas and falsifiers.

## Checks

- Compared every regularity claim in the result with the cited source locators.
- Preserved the distinction between quotient regularity, axis-regular metric
  regularity, and profile dependence.
- No tests, installs, large runs, commits, or out-of-scope edits were made.

## Limitations and unresolved questions

This is a bounded selective source audit, not a reproof of the LOY estimates
or a proof that the missing regularity statements are false. The source
establishes quotient-level regularity but does not itself close the metric
axis reconstruction at `C²`/`C∞`. The checked follow-up uses a different
cone-based family. No novelty or global regularity theorem is claimed.
