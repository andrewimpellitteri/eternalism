# Probe corrections: apply the reviewed vector and covariant-probe corrections

Status: 2026-10-21. Task `glm-probe-corrections`, worktree
`.worktrees/glm-probe-corrections`, branch `agent/glm-probe-corrections`.
Submission for coordinator review — not an accepted completion, not a new
result claim.

**Resumed run (provenance corrected by coordinator).** The first supervisor
was queued at a two-worker limit and was stopped before model activity so it
could resume at the user-authorized four-worker limit. No model usage-quota or
rate-limit interruption occurred in this lane. On resume, `git status` was clean
at `e0c833e` and no partial correction work existed in the owned paths, so this
submission was produced entirely in the resumed session. The separate search
MCP quota failure is documented below. All committed builder artifacts were
preserved as reviewed; corrections are dated and marked, nothing was silently
rewritten or erased.

## Inputs read (full text)

- `research/adversarial-review/AGENT_REPORT.md` (gate checkpoint, 2026-10-21)
- `research/adversarial-review/coordinator/VECTOR_COUNTERMODEL.md`
- `research/adversarial-review/coordinator/BOUNDARIES.md`
- the three builder artifacts (`research/extensions/{vector-measure,
  covariant-values,rank-factor}/AGENT_REPORT.md`) and their scripts
- `AGENTS.md`, `README.md`, `knowledge/README.md`, `knowledge/NOVELTY.md`,
  task brief via `python3 scripts/agents.py brief glm-probe-corrections`
- (technique reference, read-only) `research/adversarial-review/coordinator/
  check_boundaries.py` for the exact Gaussian-rational pattern

## Search capability check (required at start)

| Tool | Result |
|---|---|
| `web-search-prime` (Z.ai MCP) | **FAILED** — MCP error -429, code 1310, "Weekly/Monthly Limit Exhausted", resets 2026-11-17 10:00:29 |
| built-in `websearch` | **FAILED** — "Web search cancelled", empty result |
| direct `webfetch` | **WORKED** |

The working fallback fetch was
`https://en.wikipedia.org/wiki/Vector_measure` (2026-10-21, **discovery
depth**). It corroborates two things relevant to provenance: the indicator
example `mu(A)=chi_A` is the standard illustration that one set function is
countably additive as an `L^1`-valued vector measure and not as an
`L^infinity`-valued one; and it cites Diestel & Uhl, *Vector Measures*, Math.
Surveys 15, AMS 1977 — the same reference the review's source-priority report
pins at Example 16, pp. 7–8. **I did not access Diestel–Uhl pp. 7–8**; that
primary-source record, with its stated access limitations, stands unchanged.
Recorded as `research/probe-corrections/sources.jsonl` (passes
`scripts/check_sources.py`: 1 record, 0 errors, 0 warnings). No novelty claim
rests on any of this.

## Corrections applied (before → after scope, per owned file)

### `research/extensions/vector-measure/`

**`AGENT_REPORT.md`** — BEFORE: proved the bounded-variation no-go (Theorem 1)
and a finite-level polygon construction (Theorem 2); presented the infinite
norm-prescribed extension as wholly open; asserted the scalar no-go "extends
to bounded-variation/semivariation vector measures". AFTER: dated correction
section plus in-place markers implementing the reviewed corrections —

1. Added the reviewed **L²(P_r) indicator counterexample**: for
   `|p|²+|1-p|²=1`, `r=|p|²`, `mu(E)=1_E` in `L²(P_r)` on the full labelled
   history space is a countably additive norm-prescribed extension on all
   cylinders (`||mu(cyl C)||² = P_r(cyl C) = |A_p(C)|²`), total mass norm 1,
   **semivariation one**, and **infinite total variation for nonreal p** on
   the circle (two-cap bound). At `p∈{0,1}` it is the classical probability
   case. Provenance: `coordinator/VECTOR_COUNTERMODEL.md` (2026-10-21);
   explicitly flagged as standard functional analysis, not a new theorem, and
   not a phase-preserving dynamics.
2. **Blanket semivariation impossibility replaced**: the no-go covers finite
   total variation (always) and finite semivariation (finite dimension only);
   the L² example has semivariation one with infinite variation.
3. **Fixed-direction reduction** (`mu(C)=A_p(C)v` → scalar no-go) stated as a
   separate proposition.
4. **Finite-dimensional no-go** stated separately: no `R²`-valued (or any
   finite-dimensional) countably additive norm-prescribed extension exists off
   `[0,1]`; the counterexample is necessarily infinite-dimensional.
5. **Finite polygon assignments demoted**: `(Re A_p(C), Im A_p(C))` already
   gives an exact finitely additive norm-matching assignment on every finite
   tree; finite existence is not a step toward infinite extension and the
   polygon data are not evidence for it.
6. "What remains open" restated: the open problem is the classification away
   from the circle locus. The pending GLM finite-Lalpha-locus lane is
   acknowledged without assuming its unreviewed result.

**`vector_measure.py`** — docstring corrections only (discloses floating
point, not "exact"; points to `check_indicator.py`; notes Re/Im triviality and
the updated infinite-extension status). Functionality untouched; rerun output
identical to the reviewed baseline (407 nodes, `norm_err=1.110e-16`,
`sum_err=6.206e-17`, 0 failures, level sums `1, 1.41421, 2.62132, 6.0481,
16.751`).

**`check_indicator.py`** — NEW. Exact (Gaussian-rational, `Fraction`-based,
standard library) checks at `p=(1+i)/2`:

- 407 exact norm-prescription identities `|A_p(C)|² = P_{1/2}(cyl C) =
  2^{-(L+e)}` on every labelled causet of sizes 1–5;
- 50 exact node identities: the Re/Im assignment is finitely additive through
  level 5 (finite existence is trivial, as the review states);
- exact partition normalization `Σ P_j = 1` at levels 3,4,5 with the
  simple-function norm bound `||Σ a_j 1_{E_j}||² = Σ|a_j|²P_j ≤ 1`
  (equality at `|a_j|=1`) — finite corroboration of the semivariation-one
  statement, explicitly not a proof of it;
- level norm sums recomputed from exact dyadic squares and shown growing;
  the script states that divergence is the analytic two-cap bound, not a
  finite check.

### `research/extensions/covariant-values/`

**`AGENT_REPORT.md`** — BEFORE: the theorem concluded "`κ_n` is a constant `κ`"
(unqualified); the rule table called the shape-dependent factor "Vacuous … by
division" without endpoint qualification, and described the doubly-principal-
only rule as having "no content". AFTER: dated correction section plus
in-place markers —

1. Theorem narrowed: `κ_n` is constant **for `n≥2`** (common factor `κ_2`);
   `κ_1` is unconstrained because there is **no doubly-principal order of
   size 1** (deleting the singleton's maximum leaves the empty order, which
   has zero maxima); the chain comparison `κ_n=κ_{n+1}` holds only for `n≥2`.
   The all-principal conclusion is unchanged (`κ_1` is never used).
2. Added the literal counterassignment from `BOUNDARIES.md`: `p=1`, Dirac
   measure on the infinite chain, `κ_1=17`, `κ_n=1` for `n≥2` satisfies (A),
   (B), and normalization.
3. Shape-dependent factor: division by `A_p(H)` is available **only for
   `p∉{0,1}`** (then all principal amplitudes are nonzero); at the endpoints
   vanishing amplitudes impose genuine zero-value conditions and arbitrary
   measures cannot be factored by division.
4. DP-only Dirac witness clarified as **existential**: it shows the rule does
   not exclude `p=0`; it does not show every measure satisfies the rule, and
   for `p∉{0,1}` a shape-independent `κ_n` genuinely restricts a measure.

**`check.py`** — rewritten. Exact arithmetic throughout (integers at
`p=0,1`; Gaussian rationals at `p=(1+i)/2`; previously float with a 1e-12
tolerance while the report claimed "max error 0"). New exact assertions: cap
identity (11 identities, exact); no doubly-principal singleton (smallest DP
size is 2); the `κ_1=17` chain-Dirac counterassignment — (A) on all 4
doubly-principal `H` of sizes 2–4 with exact `N(H)A_1(H)` (real shape
multiplicities via canonical-form counting) and (B) on all 4 principal `H` of
sizes 1–3, normalization by construction; division availability —
`A_p(H)≠0` on all 51 principal `H` of sizes 1–5 at `p=(1+i)/2`, `A_0(H)=0` on
all 50 principal `H` of sizes 2–5 (singleton has `A_0=1` but is not doubly
principal), `A_1(H)=0` on the 46 non-chain principal `H` and `=1` on the 4
chains; the `p=0` Dirac-history block is kept, now labelled as an existential
witness.

### `research/extensions/rank-factor/`

**`AGENT_REPORT.md`** — BEFORE: `R_k` defined without stating its domain;
"For `p∈[0,1]` the series sums to 1"; "for `p∉[0,1]` it generally diverges at
`λ=1`, which is the existing no-go" (and the same claim in the known-result
reduction); "new structural lemma" stated as a priority claim. AFTER: dated
correction section plus in-place markers —

1. **`R_k` domain made explicit**: the sum runs over naturally labelled
   post-free orders `T` of size `k-1`, each labelling counted once
   (`poscau.causets`), equivalently over unlabelled shapes `τ` with
   multiplicity `N(τ)`; the derivation requires that multiplicity.
2. **`R(1)=1` restricted to `0<p≤1`**: at `p=0` every `R_k=0` (`R_1=p=0`;
   for `k≥2` each post-free `T` is nonempty with `M(T),min(T)≥1`, so every
   term carries a positive power of `p`), hence `R(1)=0` at `p=0` — the
   classical infinite-post probability is not one there.
3. **Division conditions stated**: the convolution reduction divides by
   `N(H)A_p(H)`, nonzero at every rank for `p≠0` (chains), but impossible at
   `p=0` for ranks `≥2`.
4. **TV→series inference withdrawn**: the total-variation no-go concerns
   absolute sums over disjoint cylinder families and does not imply divergence
   of the complex series `Σ_k R_k`; whether `R(1)` converges for nonreal `p`
   is open, and "diverges at `λ=1`, which is the existing no-go" was removed
   from both places it appeared. Added to the explicit do-not-claim list.
5. **Rank-only existence and the lemma's priority kept unresolved**; the
   truncated root search is labelled a numerical diagnostic in both the script
   and the report. The PIVOT verdict and all historical negative results are
   preserved.

**`check_stationarity.py`** — rewritten. Exact sections with zero tolerance:
(A) 32 + 32 exact kernel identities `S(H,m) = N(H)A(H)R_{m-n}` at `p=1/2`
(Fraction) and `p=(1+i)/2` (Gaussian rationals) — previously float tolerance
`1e-9`; (B) edge cases `R_1=p` (both exact parameters) and `R_k=0` for
`k=1..7` at `p=0` (exact, the `R(1)=1` exclusion); (C) labelled `T`-sum equals
shape-multiplicity sum for `k=2..7` at `p=1/2` (exact) — this pins down the
definition corrected in (1) above; (D) `p=0.2+0.7j` kept as a floating-point
diagnostic (max error `2.371e-16`), labelled "NOT an exact check, NOT evidence
for existence or no-go".

**`kernel_sequence7.py`** — docstring and output-label corrections only
(labelled-`T` sum; truncated roots numerical-only). **`probe.py`** — unchanged.

## Unchanged by design

The selected scalar theorem, the Lean formal certificate, the root adversarial
review files, knowledge registers, runner, workboard, and the other GLM lane's
live outputs were not touched. `git status` at submission time shows only the
owned paths.

## Verification commands and results

All run from the worktree root unless noted; standard library only, no
installs, no large runs (largest enumeration is `poscau.causets(6)`-scale,
seconds).

| Command | Result |
|---|---|
| `python3 research/extensions/vector-measure/vector_measure.py` | exit 0; identical to reviewed baseline: 407 nodes, norm_err 1.110e-16, sum_err 6.206e-17, failures 0 |
| `python3 research/extensions/vector-measure/check_indicator.py` | exit 0; 407 exact norm identities, 50 exact Re/Im identities, exact partition normalization at levels 3–5, exact dyadic-square assertion, level sums `1, 1.41421, 2.62132, 6.0481, 16.751` |
| `python3 research/extensions/covariant-values/check.py` | exit 0; 11 exact cap identities; no-DP-singleton PASS; κ₁=17 counterassignment (A) 4 / (B) 4 exact; division 51 nonzero / 50+46 zeros / 4 chains; Dirac block PASS |
| `python3 research/extensions/rank-factor/check_stationarity.py` | exit 0; 32+32 exact kernel identities (zero tolerance); `R_1=p` and p=0 `R_k=0` exact; labelled-vs-shape-multiplicity exact for k=2..7; float diagnostic 2.371e-16 |
| `python3 research/extensions/rank-factor/kernel_sequence7.py` | exit 0; same `R_k` values as reviewed tables; roots now labelled truncated/numerical |
| `cd research/adversarial-review/coordinator && python3 check_boundaries.py` (read-only cross-check) | exit 0; 407 exact cylinder identities; κ₁ counterassignment verified — my counts match it exactly |
| `python3 scripts/check_sources.py research/probe-corrections/sources.jsonl` | 1 record, 0 errors, 0 warnings |

Two assertion bugs were found and fixed while building the exact checks
(a wrong `|Σ±P_j|` norm computation in `check_indicator.py`, and passing a
relation where `probe.n_labelings` expects a canonical form in
`check_stationarity.py`); both were caught by the scripts' own assertions
before any conclusion was drawn from them.

## Strongest contrary evidence and limits of the corrections

- The L² counterexample's countable additivity, semivariation, and infinite
  variation are **analytic** statements whose proofs live in the coordinator
  review; my exact checks are finite corroboration only and say nothing at
  infinity. The scripts state this explicitly.
- The `κ_1=17` check verifies the counterassignment at finite sizes against
  the semantically defined chain-Dirac measure (`ν(D_H)=1` iff `H` is a
  chain). If the intended `D_H` events had limit-level structure not visible
  at finite `n`, finite checks could not see it; the same verification,
  however, was performed independently by the coordinator's checker, and the
  construction is analytic in `BOUNDARIES.md`.
- The `p=0` exclusion of `R(1)=1` and the shape-multiplicity identity are
  exact at the tested finite sizes; the `0<p≤1` identity `R(1)=1` itself is
  the known classical probability identity and was **not** re-derived here.
- The rank-only existence question, the `R(1)` convergence question for
  nonreal `p`, and the lemma's priority all remain open — the corrections
  remove overclaims; they add no new theorem.

## Remaining blockers and proposed next tasks

1. **Coordinator disposition** of this submission (accept or revise). The
   adversarial-review gate remains closed until the GLM submissions are
   assessed through their arguments, per the review checkpoint.
2. Carry-over: a generating function or rigorous bounds for
   `R(z)=Σ R_k z^k` inside `|z|<1/(|p|+|1-p|)` would settle the rank-only
   question; unchanged from the rank report's "what would settle it" list.
3. Carry-over, restated scope: classification of countably additive
   norm-prescribed Banach-valued extensions away from the circle
   `|p|²+|1-p|²=1` (now that the circle locus is resolved by the reviewed L²
   construction).
4. The finite polygon script remains a floating-point historical witness; an
   exact port is unnecessary for any current claim and was deliberately not
   attempted.
5. If the stationary-kernel lemma is to appear in the note, a novelty/priority
   check against the vector-measure and causal-set literature is still owed
   (the review flagged the priority claim as unverified).

## Files changed (all within owned paths)

- `research/extensions/vector-measure/AGENT_REPORT.md` (corrections)
- `research/extensions/vector-measure/vector_measure.py` (docstring)
- `research/extensions/vector-measure/check_indicator.py` (new)
- `research/extensions/covariant-values/AGENT_REPORT.md` (corrections)
- `research/extensions/covariant-values/check.py` (exact + edge cases)
- `research/extensions/rank-factor/AGENT_REPORT.md` (corrections)
- `research/extensions/rank-factor/check_stationarity.py` (exact + edge cases)
- `research/extensions/rank-factor/kernel_sequence7.py` (labels)
- `research/probe-corrections/AGENT_REPORT.md` (this report)
- `research/probe-corrections/sources.jsonl` (new)
- `AGENT_REPORT.md` (root copy of this report, per worker convention)

## Coordinator disposition, 2026-10-21

Reviewed and integrated after the fixes in `COORDINATOR_REVIEW.md`: corrected
exact complex test parameter, explicit Gaussian nonzero comparison, actual
queued/resumed provenance, and current vector scope. All listed small checks
were rerun on the corrected files. The root report copy was excluded from the
integration in favor of this owned report; the existing main root report was
preserved. This task's corrections are accepted independently of the still-open
adversarial/paper gate. Later coordinator norm-only classifications supersede
this submission's circle-only remaining-open description; they do not preserve
the scalar model's complex premeasure or its interference predictions.
