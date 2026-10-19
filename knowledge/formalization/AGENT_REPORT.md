# Agent report: kb-formalization

Files changed:
- `knowledge/formalization/sources.jsonl`
- `knowledge/formalization/reuse-map.md`
- `knowledge/formalization/REPORT.md`
- `knowledge/formalization/AGENT_REPORT.md`
- `knowledge/formalization/code-audit.md` (second pass)

Evidence and checks:
- Read repository AGENTS.md, README.md, knowledge/README.md, knowledge/NOVELTY.md, and `python3 scripts/agents.py brief kb-formalization`.
- Inspected the Physlib repository README/tree, AxQM repository README, and arXiv full text for the Schutz/Isabelle and Stannett–Németi/Isabelle papers through public pages.
- Labeled source depths conservatively. No code was cloned or built, no packages installed, and no project files outside the assigned output path changed.
- Recorded exact paper locators and open code-version gaps rather than inferring code results from publication claims.

Limitations:
- GitHub pages did not expose immutable commit SHAs in this pass. Physlib and AxQM must be pinned before any actual code reuse.
- Isabelle work is paper-level full-text inspection only; source, session graph, and axiom/dependency closures remain unaudited.
- AxQM source declarations and finite-dimensional clock suitability remain uninspected. Its `main` branch is a benchmark with proof holes, not a completed public proof library.
- No finite-model tool was inspected or run. This is a bounded first pass, not a comprehensive prior-work or novelty audit.

## Second-pass update

Static source inspection added in `code-audit.md`. Physlib HEAD was pinned via its history page to `67d742760382efce9419feefa348902aab797a07`; the pinned `QuantumInfo/States/Mixed/MState.lean` was inspected. POVM and relativity code were retrieved at mutable `master`, with the failure to pin those file views recorded. AFP's current generated outline provided exact locale declarations and version/date context; Isabelle source/session was not downloaded. No builds or installs were run.

Concrete code reads: `MState` is a finite-indexed PSD trace-one Hermitian matrix; `POVM` is finite-outcome PSD matrices summing to identity, with outcome distribution and channel marginal theorem; `minkowskiMatrix` defines diagonal signature matrix and `dual` algebra but defers Lorentz group; `SpeedOfLight` is just a positive real parameter. Finite-dimensional exact `[T,H]=iℏI` is ruled out by trace cyclicity, but finite periodic clocks and finite POVM readout remain possible and are not thereby equivalent to ideal real-line clocks. Minimum viable substrate: Physlib MState + POVM for a theorem specifically stated with finite clock outcomes; otherwise Python/SMT is more direct for first finite exploration.

Unresolved questions:
- Which exact pinned Physlib version and transitive declarations should be used for a target finite-clock theorem, and what are the full Lean axiom closures?
- Can AFP theory/session sources be retrieved with a pinned Isabelle version to audit assumptions/admissions and source-paper correspondence?
- Which relational-trinity finite-dimensional theorem is the smallest faithful clock equivalence target, and what gap remains after tracing its exact assumptions?
