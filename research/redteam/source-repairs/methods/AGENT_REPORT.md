# Methods source repair report

## Files changed

- `knowledge/methods/sources.jsonl`
- `research/redteam/source-repairs/methods/AGENT_REPORT.md`

## Repairs and evidence

- `meth-cas-agents-2026`: added source-bound `assumptions` and `conclusion`; preserved the existing experiment and rubric notes. The primary v1 HTML was checked for the setup and task scope (Secs. 1, 3.2–3.5), evaluation rule (Sec. 3.4), reported outcome and limitations (Secs. 4–5): <https://arxiv.org/html/2605.08212v1>. The summary limits the result to the paper's nine one-shot perturbation-DOF tasks and reported contexts.
- `meth-tensor-agents-2026`: added source-bound `assumptions` and `conclusion`, explicitly retaining the distinction between proof checking and checking whether the intended statement was formalized. Checked the exact v1 HTML metadata, FT-MPS scope, “Catching unintended formalizations,” discussion and App. E: <https://arxiv.org/html/2607.07857v1>. Existing limits about no independent rebuild remain.
- `meth-sw-lean-2026`: added `assumptions`, `conclusion`, and `dependencies`. These are supported by the accepted full-text spotcheck at `knowledge/audits/fulltext-spotcheck/clocks-methods/findings.jsonl` (`meth-sw-lean-2026`), with its exact v1 URL and section locators. Language keeps the SU(2) theorem report conditional on H0–H7 and named mathematical inputs, distinguishes the SU(N)/higher-genus skeleton, and does not present a repository build or axiom-footprint audit as completed.
- `meth-ax-prover`: completed the author list against the exact v4 HTML header and attached the directly related `meth-axqm-2026` benchmark record. Primary metadata: <https://arxiv.org/html/2510.12787v4>. The existing substantive reading boundary (“key sections read, rest skimmed”) and claims remain unchanged.

For all four records, `checked_on` now records the metadata/repair check on 2026-10-20. `reading_provenance` points to the frozen pre-repair copy in `research/redteam/source-repairs/before-records.jsonl` by line, source register line and ID, and retains each former depth, version, date, locator and (for Ax-Prover) the prior reader note. The repair basis then gives the exact primary or accepted audit locator and scope. No original read depth or version pin was silently changed.

## Checks

- Before repair: `python3 scripts/check_sources.py --strict knowledge/methods` reported 10 records, 4 errors, 0 warnings. Errors were the missing full-text fields addressed above.
- After repair: the same command reports **1 file, 10 records: 0 errors, 0 warnings, 0 info**.
- JSONL parsed successfully when the records were updated.

## Limits and unresolved items

The CAS, tensor-network and Ax-Prover results remain author-reported; neither the CAS runs nor the Tensor Network Lean build were reproduced. For SW-LEAN, the companion repository, build, transitive axiom footprint and paper-to-code correspondence remain unverified, as the accepted spotcheck states. Ax-Prover's existing paper-level limitations remain: proof grading does not itself check statement correspondence or axioms, and the QuantumTheorems statement review was one expert pass. These repairs complete required fields; they do not upgrade those evidence boundaries.
