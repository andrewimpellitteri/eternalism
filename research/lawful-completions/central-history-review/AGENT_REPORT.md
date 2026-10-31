# AGENT_REPORT.md — lawful-central-history-review

Worker: OpenCode GLM (zai-coding-plan/glm-5.3-flash), headless isolated
worktree `agent/lawful-central-history-review`. Date: 31 October 2026.
Status: **submission for independent review**; nothing here is an acceptance,
a novelty claim, or an ontological claim.

## Done / files changed

Audited the conditional whole-function candidate
`research/lawful-completions/claude-central-history/RESULT.md` (post
REVIEW.md R1–R4) against every checklist item in the brief, read all named
inputs, verified the primary-source loci in arXiv:1605.03893v1 directly, and
located one assembly gap plus one scope gap with a bounded repair.

Files created (all owned, nothing else touched):

- `research/lawful-completions/central-history-review/RESULT.md` — the audit.
- `research/lawful-completions/central-history-review/AGENT_REPORT.md` — this file.
- `research/lawful-completions/central-history-review/sources.jsonl` — two
  strict full-text records for the primary source (e-print + HTML render).

Read (not modified): `claude-central-history/{RESULT,REVIEW,CONTRACTION,
REVIEW_CONTRACTION,PRIOR_WORK,CARD}.md`, `volterra_check.py`,
`uniformity_check.py` headers; `coordinator/{C11_FINITE_CONTROL,
FINITE_CONTROL_ACCEPTANCE,COMPACTNESS_CONTINUITY_REPAIR,RESPONSE_REDUCTION,
NEXT_FRONTIER_TASKS}.md`; `claude-finite-control-audit/{RESULT,SECOND_READ,
REPAIR_B_REVIEW}.md`; `finite-control-review/RESULT.md`; repo README,
knowledge README/NOVELTY; WORKBOARD task brief via AGENTS.md instructions.
`CONTRACTION.md`, `REVIEW_CONTRACTION.md`, `PRIOR_WORK.md` verified
byte-identical to commit `5f50cee` (`git diff 5f50cee HEAD --stat` empty for
the lane) and treated as candidates, not accepted inputs, per the brief.

Headline result of the audit (details in RESULT.md): the integrated-class
whole-window claim survives conditional on its declared inputs **except**
that §4's trace-error estimate `|Ψ−𝒯_nΨ| ≤ 2η·Lip(𝒯_nΨ)` is carried by none
of them — it needs a vertex-uniform C⁰ trace-map difference estimate
(CONTRACTION.md's content, a non-accepted one-read candidate) or a bounded
reassembly on Repair A′ that makes the trace error identically zero per n;
I verified that reassembly closes §5 with uniform a priori bounds alone.
Second: Theorem 1.1 is printed for smooth data and the claim applies it to a
Lipschitz ball; the needed C¹/density extension is unstated (and Theorem
1.7's `sup|Φ″|` hypothesis bars citing the source's own two-sided theorem at
Lipschitz regularity). R3/R4 remain sketches (labels confirmed verbatim in
v1); R2's tail mechanism is now primary-verified (LOY's own §6 (5.1) Step 1,
parameter `C_γε′` independent of the bump count).

## Search capability check (required by brief)

- `web-search-prime` (Z.ai MCP): **failed** — quota exhausted, error 1310
  "Weekly/Monthly Limit Exhausted", resets 2026-11-17. Recorded here
  explicitly; no results were used from it.
- `serpapi_search`: **failed** — "Your account has run out of searches."
- `scholar_search` (arXiv source): **worked** — located the primary source
  with exact metadata (title, authors Luk/Oh/Yang, v1, 2016-05-12). A first
  compound query returned arXiv HTTP 400; a plain-keyword query succeeded.
- Direct arXiv fetches via curl: worked (abs metadata via scholar_search;
  e-print and HTML v1 both fetched). Used for all source verification.

## Source coverage

Primary source, full-text at selected loci (statement level; proofs of the
§3 bootstrap, §§5–7, Appendix, published version **not** read by me):
Theorem 1.1 with (1.7) and Remarks; §2.1 local paragraph; Definition 2.1;
Theorem 1.7 with its footnote and (1.20); (3.7), (3.12), (3.16), (3.24),
(3.25), (3.29), (3.31), (3.35); Prop 3.18 statement; sketch labels of Lemma
3.19 and (3.46)–(3.47); §4's two "n→∞ first, then u→−∞" statements; §6 (5.1)
Steps 1–3. Exact list with verdicts is in RESULT.md §6. No other external
sources were accessed; the prior-work sources in PRIOR_WORK.md were not
re-checked, and that file remains a candidate. Source records are in
`sources.jsonl` with `read_depth: full-text` at the listed loci only.

## Verification commands and results

- `git show 5f50cee --stat`, `git diff 5f50cee HEAD --stat -- …
  claude-central-history/` → empty; lane files are the commit-5f50cee
  versions the brief names.
- `curl -sL https://arxiv.org/e-print/1605.03893v1` → gzip of
  `SSESF-LargeBVScat.160512.tex`, 3214 lines (matches prior lanes' records);
  `curl -sL https://arxiv.org/html/1605.03893v1` → 1,505,633 bytes; loci
  extracted from resolved `S#.E#` ids and TeX by direct reading (commands in
  session log; outputs quoted in RESULT.md §6).
- `python3 volterra_check.py` (Claude lane, unchanged) → RESULT.md §7's table
  reproduced exactly; `time` reports real 9.84 s, user 8.90 s. Within the
  brief's budget (hard ≤15 s, actual ≤10 s, total ≈12 s including two ~1 s
  mollifier toy checks).
- Mollifier toy check (RESULT.md §1): for Ψ=2M|t|, ρ=6σ(1−σ), η=10⁻³:
  C⁰ defect 0.001; derivative defect inside the smoothing window 2.00 and
  3.37 (order M) — confirms `‖J_ηΨ−Ψ‖_(C¹)` is not O(η) on the Lipschitz
  ball, which is why Repair A cannot carry §4's estimate.
- Hand re-derivations (no code): axis identity `p_uv = λKφ` and
  `Λφ_c = Φ + I`; `L = φ` on Γ from tangentiality; B-invariance of both
  `J_η𝒯_nJ_η` (χ slack absorbs the η right-edge shift) and `𝒯_n` itself;
  §2 norm bookkeeping; fixed point ⟹ trace, one direction; R3's
  `|(𝒯Φ)″| ≲ ‖y″‖ + Cε̃²A + Cε̃³` term accounting (uses ε̃ ≍ M);
  the A′-route closure of §5; `E_w ≤ M²(t̄+2) ≤ 3M²T_max` floor bound.

## Strongest contrary evidence

- Against the claim's §4 assembly: the uncarried trace-error estimate (§1 of
  RESULT.md) — this is the strongest objection found, with the toy check and
  the two failed carriers (Repair A, per-n A′) spelled out.
- Against R2's uniformity: Theorem 1.1's (1.7) also contains the pointwise
  bound `|Φ|+|Φ′| ≤ ε`, which a sum of K bumps could break — resolved
  against the objection by LOY's own printed Step 1 (disjointness), i.e. the
  objection was checked and retired at the source.
- Against smoothness scope: Theorem 1.7's printed `sup|Φ″|` requirement —
  the source itself cannot justify the Lipschitz-regularity scattering
  limit; the candidate's own compactness passage does, and should be labeled
  as an extension.
- No counterexample to the readings claim was found; the reproduced numerics
  show no derivative growth at fixed εω, and the fixed-amplitude failures
  lie outside the ball.

## Limitations

- Single-reader audit; my §1 repair shifts load onto Repair A′, which itself
  has had one second read, not independent review.
- I did not re-audit AXIS_C11_RECONSTRUCTION, INCOMING_MASS, CUBIC_TRACE
  beyond their accepted dispositions, nor the smoothness bootstrap; the
  smooth-target/smooth-model upgrade stays a separate open obligation.
- Published Ann. PDE version unread; the uniqueness-proof omission and the
  (3.3) φ/rφ anomaly remain trusted-input risks inherited from the lane.
- No fresh prior-work search (out of scope; PRIOR_WORK.md stays a candidate);
  no Lean or formalization work; numerics are one-domain sanity checks.
- Computation kept inside the brief's budget; no installs, no configuration
  changes, no credentials touched.

## Proposed next tasks

1. Rewrite `claude-central-history/RESULT.md` §4 on the Repair-A′ route (or
   import CONTRACTION explicitly and inherit its status); add the C¹-data
   global-existence extension to the conditional list; add the
   `E_w ≤ 3M²T_max` floor line. Bounded, high value.
2. Independent second read of Repair A′ (becomes load-bearing under 1).
3. Order-k bounds (linear at top order) or Repair B's qualitative premise,
   or the published-version diff, to move R3 off LOY's sketches.
4. Nearest-prior check of the whole-function inverse itself (PRIOR_WORK's
   open row), before any claim is written outside this lane.
5. Investigate whether M_* can be made T_max-uniform (blocked by (1.7)'s
   `max(1,ℓ^γ)` structure; candidate flags it as non-sharp).

## Blockers

None. web-search-prime and serpapi quota exhaustion was worked around with
scholar_search (arXiv) and direct arXiv fetches; all obligations in the brief
that could be met were met, and the remainder is recorded as open items
above rather than claimed as completion.
