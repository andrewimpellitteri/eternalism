# Interrupted: native correction not submitted

`constraint-formulation-compare` was reassigned to native agent Kepler
(`codex-native-clock`, session 01a15f25-1369-78f3-8bff-eff30b360420) on
2026-10-21 to repair the imported GLM snapshot after the independent
clock-action audit.

At 16:13:31Z Codex returned `usage_limit_exceeded` during an in-progress edit
of `formulations.py`. The final agent message is null; no `AGENT_REPORT.md`
was written and `REVIEW_STATUS.md` still records the earlier GLM submission
as `correction required`.

Preserved files in this directory:

- `SPEC.md` — draft corrected comparison (three formulations, conventions,
  closure/alias and local-covariance caveats). **Unreviewed.**
- `formulations.py`, `linalg.py` — draft implementation. Syntax-checked only;
  its output has not been independently reproduced against `SPEC.md`.
- `GLM_SUBMISSION.md`, `model_output.txt`, `sources.jsonl`,
  `REVIEW_STATUS.md` — imported GLM snapshot, retained read-only as the
  submission record.

Status: **interrupted, not a submission.** Do not treat `SPEC.md` or the code
as accepted. No retry was attempted after the quota failure. On resumption,
first reconcile `formulations.py` with `SPEC.md`, rerun the exact checks, and
have an independent reader verify the closure, alias and local-readout
covariance claims before any acceptance.
