# Search log

## 2026-10-19 — initial coordinator screening

Purpose: find existing work before selecting a contribution. Read depth is
recorded per source in seed-sources.jsonl. No paper proof or codebase has yet
been independently reproduced.

Search clusters used:

- Einstein 1905, simultaneity, clocks.
- Andréka / Madarász / Németi / Székely, axiomatic relativity, first-order logic.
- PhysLean / Physlib, Lean special relativity, Isabelle relativity verification.
- Stein openness of the future, Malament simultaneity, directed-time variants.
- Presentism as an empirical hypothesis; relativistic and causal-set becoming.
- Page-Wootters, temporal measurements, spacetime quantum reference frames.
- Bell theorem for temporal order, observer-dependent causal order.
- 2026 relational clocks, unitarity, finite-resolution clocks, Markovianity.
- 2026 physics formalization, multi-agent autoformalization, LLM + computer algebra.
- Experimental Lorentz/CPT constraints and quantum-gravity problem of time.

Repository precedents inspected read-only:

- `/Users/andrew/Documents/dev/4o_clone/WORKBOARD.md`, AGENTS.md, and the opening
  portion of scripts/agent_board.py: central claims and explicit file ownership.
- `/Users/andrew/Documents/dev/awning_wo/scripts/agents/` and
  docs/agents/HEADLESS_OPENCODE.md: task briefs, isolated worktrees, GLM, logs,
  reports, and review before integration.
- Installed OpenCode 2.0.32 `run --help`: use `--standalone`; the older example's
  `--pure` flag is no longer listed. CLI help was checked with writable local
  XDG runtime directories. No authenticated model call was made.

## Coverage gaps to resolve

- Full-text theorem-level reads of Stein, Malament, Rietdijk, Putnam, and replies.
- Strong presentist/growing-block/moving-spotlight formulations, not straw cases.
- Thermal time, records, causal dynamical triangulations, shape dynamics,
  consistent/decoherent histories, collapse and Bohmian preferred structures.
- Existing equivalence theorems among relational-time descriptions and their
  restrictions for imperfect/interacting clocks.
- Backward and forward citation searches; explicitly bounded last-90-day intake.
- Current Physlib commit/API, existing related proofs, and local build feasibility.
- Whether recent preprints survive independent scrutiny and have public code.
- Semantic faithfulness in AI autoformalization, not merely proof compilation.

Search result snippets and repository marketing claims are leads only. Do not
convert missing search hits into a claim that no one has studied a question.

## Z.ai MCP capability check

The connected `web-search-prime` tool successfully answered a search for
"relational quantum clocks equivalence trinity quantum dynamics Hohn Smith Lock
2021". Its leads were checked against the primary arXiv pages 1912.00033v3 and
2007.00580v1. They materially narrowed the proposed imperfect-clock extension:
non-ideal clocks already feature in the trinity work.

Read-only inspection of OpenCode's config confirmed `web-search-prime` is
enabled. Credentials and remote headers were not printed or copied. This checks
the connector in the coordinator's session; it is not an authenticated OpenCode
worker smoke test. Workers must record their own search capability check.
