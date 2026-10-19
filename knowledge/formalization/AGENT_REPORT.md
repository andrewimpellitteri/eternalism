# Agent report: kb-formalization

Files changed:
- `knowledge/formalization/sources.jsonl`
- `knowledge/formalization/reuse-map.md`
- `knowledge/formalization/REPORT.md`
- `knowledge/formalization/AGENT_REPORT.md`

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

Unresolved questions:
- Which precise Physlib and AxQM declarations cover the target state, unitary, measurement, clock, observer, event, and causal-order primitives?
- Can the Schutz and Stannett/Németi theory files be recovered with versions matching their papers, and what are their exact premise and axiom closures?
- Which relational-trinity finite-dimensional theorem is the smallest faithful clock equivalence target, and what gap remains after tracing its exact assumptions?
