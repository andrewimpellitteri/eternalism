# Agent report: lawful-finite-cone-continuity

29 October 2026. Worker lane for DEGREE_ROUTE/FINITE_CONTROL gate 1
(finite-cone readout continuity). Worktree
`lawful-finite-cone-continuity`, branch `agent/lawful-finite-cone-continuity`.

## Done / files

- `RESULT.md` — the deliverable: **Theorem 2** proves that for each fixed
  finite cone `u₀` and each compact smooth profile family obeying (H1), every
  finite-cone solution depends Lipschitz-continuously on the parameter `x` on
  the closed readout triangle, **axis included**, via a direct Volterra
  difference estimate (no differentiation of any solution map, no uniqueness
  beyond printed characteristic uniqueness). Corollary: the readout map
  `H_n(x) = (φ_x(t_x(T_j;x), t_x(T_j;x)))_j` (proper-time clock included) is
  Lipschitz on the parameter ball; constants `C_n` may depend on the cone n,
  which suffices for the Brouwer-degree step. Also: cone-trace Lemma 1,
  degree-step red team (§4), root-passage audit from printed §4 material (§5),
  falsifiers (§6), exact locators (§7), limitations (§8).
- `sources.jsonl` — knowledge/README-schema records: LOY v1 (full-text
  re-verification with per-equation locators), three discovery/abstract-level
  search leads (no applicable printed continuous-dependence theorem found).
- `AGENT_REPORT.md` — this file; root `AGENT_REPORT.md` mirrors it.

## Search capability check (required by brief)

- `web-search-prime`: **not retried** (quota exhausted until 2026-11-17, per
  task brief).
- `scholar_search`: **worked** (2026-10-29). Queries: (i) LOY bounded-variation
  paper (found; confirms published venue Ann. PDE 2017); (ii) "continuous
  dependence" + characteristic initial value problem + Einstein/Goursat;
  (iii) SSESF solution-map/continuous-dependence. No exact applicable primary
  continuous-dependence theorem surfaced; three leads recorded at
  discovery/abstract depth in `sources.jsonl`.
- Primary fetch: direct `curl` of `https://arxiv.org/html/1605.03893v1`
  (HTTP 200, 1,505,633 bytes, LaTeXML HTML). `ar5iv.labs.arxiv.org` timed out
  (curl exit 28 at 90 s) — arxiv.org HTML used instead; `exa` not needed.
  No packages installed; extraction by a local stdlib Python tag-stripper.

## Source coverage

- Read at full-text depth this session (selected sections): LOY
  arXiv:1605.03893v1 — §1.2, §2.1–2.3, §3.1–3.6 (statements; proofs of
  Lemma 2.6, 3.1, 3.2, Prop 3.3, 3.4, 3.8, 3.10, 3.11, 3.13, 3.14 read in
  full), §3.7–3.8 statements, §4 entire. Theorem 1.1/1.7 statements and
  Remarks 1.2/1.3.
- Not read: Prop 3.16 proof, Prop 3.18 proof (statements only; neither is
  load-bearing for Theorem 2 — (3.16)/(3.17), which are load-bearing, were
  read). Published Ann. PDE version not compared (v1 numbering only).
- Prior work duty: coordinator records `lawful-coord-luk-oh-yang2016` and
  `lawful-coord-christodoulou1991` reused (not duplicated); REVIEW_DEGREE,
  CUBIC_TRACE, DEGREE_ROUTE, FINITE_CONTROL, regularity/RESULT.md read and
  cross-checked.

## Verification commands and results

```sh
# version check: exactly [v1], title match
curl -sL https://arxiv.org/abs/1605.03893          # [v1] only, 12 May 2016
curl -sL https://arxiv.org/html/1605.03893v1 -o arxiv_html.html
# stdlib Python: strip tags, alttext->inline math -> loy_text.txt (148,906 chars)
grep -n '@@H' loy_text.txt                          # section/theorem map
sed -n '417,517p' loy_text.txt                      # Def 2.1, (2.4)-(2.5), LWP sentence:
  # "locally well-posed ... unique ... We omit the proof"  => continuous
  # dependence NOT printed (the gap this lane fills)
sed -n '517,614p' loy_text.txt                      # (2.6)-(2.16) verified verbatim
grep alttext checks: (1.8) => 2m/r < 1/2; (1.20) => sup|Phi''| < inf;
  (3.24) => |2m nu/((1-mu) r^2)| <= C eps^2 r_+^{-1-gamma}   [Lemma 3.7]
  (2.17), (3.9), (3.28), Prop 3.10 axis identities nu+lambda=0, mu=0;
  S4 two printed estimates (log-lambda and the eps^3 trace estimate) — all verbatim
```

Cross-checks that matter for the proof: (2.23) `rλ⁻¹∂_vφ = ϑ − φ` gives the
regular quantity `χ` used in the averaging-difference step; (2.10)+(2.23) give
`2m = ∫_u^v (1−μ)χ²λ dv′` (matches (2.18) after substitution); (3.28) + axis
identities give the ν-reconstruction used for `Δν`; (3.5) gives `r ~ (v−u)`
uniformly on the class, which is what makes every `1/r` in the q-difference
lemma cancel without axis splitting.

## Strongest contrary evidence

- The source itself: no printed continuous-dependence theorem for this system;
  its LWP is asserted with proof omitted. If that "routine iteration" were the
  only route, gate 1 would be closed only by reconstructing it; this lane's
  estimate is independent of it (uses only printed a priori bounds + the
  equations).
- General Goursat-problem literature exists (2026 preprints, discovery depth)
  but covers different system classes and asserts no continuous dependence —
  so no citation shortcut exists; recorded rather than used.
- Self-falsifiers listed in RESULT.md §6 (e.g., failure of Lemma 3.7's kernel
  bound near the axis would break Step 3(a); none found — (3.24) follows from
  (3.16)/(3.17), whose proof was re-read).

## Limitations

1. Constants `C_n` grow with the cone index (poly in `T_n = t* − u₀`);
   uniform-in-n continuity is neither proved nor needed for degree.
2. Result is at the reduced (1+1) quotient level with the printed axis
   identities; **no claim** about the four-dimensional axis chart or C² metric
   reconstruction (regularity lane's gap stays open).
3. Hypothesis (H1) (uniform class smallness/support/Lipschitz data map) is
   assumed; `FINITE_CONTROL.md`'s β-family plainly satisfies it but the class
   constants (C₀, L₀, Ã, ε̃ ≤ min(ε₁, ε₂)) should be recorded once by a
   follow-up task.
4. v1 numbering only; journal version not diffed. arXiv HTML rendering used.
5. Gate 2 (parameter-uniform compactness with n-dependent profiles) is audited
   (RESULT.md §5) from printed material, not re-proved; residual reviewer
   checks listed there. ADM identification and global-uniqueness questions
   untouched.

## Unresolved questions / proposed next tasks

- Write out the double-family Arzela–Ascoli extraction (gate 2) with the
  printed §4 constants and the two residual checks named in RESULT.md §5.
- Record the explicit class constants for the FINITE_CONTROL family and the
  resulting admissible ε-window.
- After gates 1–2 close: re-audit INCOMING_MASS.md transport in the
  n-dependent limiting class; separately keep the 4D axis-reconstruction and
  novelty gates open.

## Submission status

Worker submission for independent review; not accepted completion. No
coordination files, runner, workboard, seed sources, or other lanes were
touched; no packages installed; no subagents launched.
