# Agent report: lawful-finite-cone-continuity

29 October 2026. Worker submission (branch `agent/lawful-finite-cone-continuity`)
for DEGREE_ROUTE/FINITE_CONTROL **gate 1: finite-cone readout continuity**.

## Result in one paragraph

**Gate 1 is closed at the reduced-solution level.** For each fixed finite cone
`u₀` and any compact smooth profile family satisfying uniform LOY hypotheses
(common support, common smallness `ε̃ ≤ min(ε₁(γ), ε₂(γ))`, Lipschitz parameter
map), `RESULT.md` Theorem 2 proves: the finite-cone solution depends
Lipschitz-continuously on the parameter `x` on the closed readout triangle,
**axis included**, including the scalar axis trace `ϑ(t,t)` and the proper-time
clock `τ_x(t) = ∫ 2λ_x(s,s)ds` and its inverse. Hence the readout map
`H_n(x)` of `FINITE_CONTROL.md` is Lipschitz (a fortiori continuous) on the
parameter ball, with constants that may depend on the cone n — exactly the
per-n continuity the Brouwer-degree step requires. The proof is a direct
Volterra difference estimate built solely from printed Luk–Oh–Yang
(arXiv:1605.03893v1) material: the transports (2.6), (2.8), the averaging
identities (2.17), (2.18)+2.10, the ν-reconstruction (3.28), the small kernel
bound (3.24) `|K| ≤ Cε²r₊^{−1−γ}`, and the uniform geometry (3.1)/(3.5)/(3.25)/(3.27).
No differentiable or continuous global scattering selection is assumed or
produced; no 4D axis-regularity claim is made.

## Files (all owned paths)

- `research/lawful-completions/finite-cone-continuity/RESULT.md` — theorem,
  full proof, degree red team, root-passage audit, falsifiers, locators.
- `research/lawful-completions/finite-cone-continuity/sources.jsonl` —
  schema-compliant records (LOY v1 full-text; 3 discovery leads).
- `research/lawful-completions/finite-cone-continuity/AGENT_REPORT.md` —
  detailed report (this file mirrors it).

## Key findings for the reviewer

1. LOY §2.1 states characteristic LWP **without proof and without continuous
   dependence** ("We omit the proof, which is a routine iteration argument") —
   gate 1 was genuinely open; no applicable printed continuous-dependence
   theorem exists in the searched literature (leads recorded, discovery depth).
2. The axis difficulty is resolved without any pointwise bound on the singular
   kernel `K = 2mν/((1−μ)r²)`: (3.24) makes `|K| ≤ Cε̃²` pointwise uniformly on
   the class, and the q-difference step rewrites the mass average as
   `2m = ∫(1−μ)χ²λ dv′` with the regular quantity `χ = ϑ − φ = rλ⁻¹∂_vφ`,
   whose compensating powers of `r ~ (v−u)` (from (3.5)) cancel every `1/r`
   at the axis. The sharper `|Δr(u,v)| ≤ (v−u)·sup|Δλ|` (not `T_n·sup`) is
   essential there.
3. Root passage to the global limit (gate 2) is audited from printed §4
   material: all §3–§4 constants depend on the data only through `ε̃` and `Ã`,
   so the §4 Arzela–Ascoli argument extends verbatim to n-dependent profiles
   within the family; the limiting radiation data is identified via (4.1)'s
   fixed-`(u,v)` order of limits; `H_{n_k}(x_{n_k}) = εz` passes to the
   subsequential limit solution. Two residual reviewer checks are named.
4. Division of labor preserved: per-n continuity here; the uniform remainder
   `sup_{n,x}|ε⁻¹H_n(x) − x| ≤ Cε²` remains CUBIC_TRACE's (§4-based), as the
   degree homotopy needs.

## Search capability check

`scholar_search` worked (2026-10-29). `web-search-prime` not retried (quota
exhausted until 2026-11-17, per brief). Primary source fetched directly:
`curl https://arxiv.org/html/1605.03893v1` (HTTP 200; v1 confirmed as the only
arXiv version via the abs page). No installs; stdlib-only local extraction.

## Strongest contrary evidence

The source prints no continuous-dependence statement, so the lemma is a new
derivation from printed estimates rather than a citation; its falsifiers are
listed (RESULT.md §6): failure of (3.24) near the axis, breakdown of (H1), or
a counterexample to characteristic uniqueness would break it — none found;
(3.24) was re-derived via (3.16)/(3.17) whose proof was re-read.

## Limitations

Per-n constants (growing like `poly(T_n)`); reduced-quotient level only (no 4D
axis claim); (H1) assumed, class constants to be recorded; v1 numbering only
(journal version not diffed); Prop 3.16/3.18 proofs unread (statements not
load-bearing); gate 2 audited, not re-proved. Full list in the lane report.

## Status

Worker submission for independent review — not accepted completion. Owned
paths only; no coordination/runner/workboard/seed changes; no subagents; no
installs; nothing pushed.
