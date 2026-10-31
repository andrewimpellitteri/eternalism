# Agent report

## Files changed

- `research/lawful-completions/smooth-realm-contrast-review/RESULT.md` — bounded audit of §§1–3, with the strongest issue first.
- `research/lawful-completions/smooth-realm-contrast-review/AGENT_REPORT.md` — this report.

## Evidence and findings

- Read `AGENTS.md`, `README.md`, `knowledge/README.md`, `knowledge/NOVELTY.md`, the output of `python3 scripts/agents.py brief lawful-smooth-realm-contrast`, and the assigned target plus relevant coordinator inputs (`HORIZON_REVIEW.md`, `C11_FINITE_CONTROL.md`, `SMOOTH_FINITE_CONTROL.md`, `SMOOTH_SCALAR_REPAIR.md`, `COMMON_EXTENSION_REPAIR.md`, and `BOWTIE_RIGIDITY.md`).
- Strongest finding: §1 should explicitly distinguish strict causal precedence `≺` (including null pairs, as defined in `HORIZON_REVIEW.md`) from chronological precedence `≪`. The identity for `D(b)` follows because the cone argument produces a common chronological successor; if `≺` is instead read chronologically, the null-related Minkowski point gives a counterexample.
- Verified the uniform timelike estimate `−2/9+(8/3)(1/16)=−1/18` and the common-future straight-path construction.
- Checked the intrinsic-to-ambient Cauchy step in §§2–3 using that `W` is an open past set, the curve intersection is an initial connected portion, the global cone bound rules out finite-`t` ambient endpoints, and the slice/image is acausal. Under these inputs, the argument works.
- Checked that the full scalar field match identifies scalar Cauchy data and that uniqueness of the smooth scalar MGHD yields the global development comparison. The marked observer tangent remains a required matched-germ condition.

## Checks

- Analytic proof audit only; no computation or external sources used. No source records were required.
- No tests run; this was a bounded mathematical review.

## Limitations and unresolved questions

- Smoothness, global hyperbolicity, cone control, and the smooth field-preserving MGHD uniqueness theorem were task inputs, not reproved.
- The separate interpolation/degree review and philosophical source argument were outside scope.
- No ontology or novelty verdict is offered.
