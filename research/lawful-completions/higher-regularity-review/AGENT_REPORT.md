# AGENT_REPORT — lawful-higher-regularity-audit

30 October 2026. Worker submission for independent review, not an accepted
completion. Coordinator owns acceptance. Branch
`agent/lawful-higher-regularity-audit`, worktree
`/Users/andrew/eternalism/.worktrees/lawful-higher-regularity-audit`.

## Done

* Read AGENTS.md (both root and worktree copies), README.md,
  knowledge/README.md, knowledge/NOVELTY.md, the task brief, and the named
  coordinator files: `AXIS_C11_RECONSTRUCTION.md`,
  `RECENT_LITERATURE_2026_10_29.md`, `SMOOTH_SCALAR_REPAIR.md`,
  `coordinator/sources.jsonl`, plus `KILGORE_SCOPE_REPAIR.md`,
  `SMOOTHNESS_BOOTSTRAP.md`, `SMOOTHNESS_REVIEW_STATUS.md`,
  `SMOOTH_FINITE_CONTROL.md`, `C11_FINITE_CONTROL.md`, and the regularity and
  axis-source-review lane outputs (prior-work inspection before novelty).
* Resolved the selected-full-text vs abstract-level Kilgore tension at
  primary-source depth: fetched the arXiv v1 TeX of 2108.13377 and read the
  abstract, footnote 1 (verbatim; first of four footnotes), Definitions
  2.4–2.6, Theorems 3.1/3.3 + Remark 3.2, region definitions, §6 gauge
  lemmas, §7 axis regularity (Remark 7.1, Prop 7.2, Lemma 7.3, Cor 7.4,
  Lemma 7.5, Cor 7.6), and the verbatim restatement of Luk–Oh's dispersive
  criterion ((D1)–(D8), N≥11) and stability theorem.
* Re-verified the LOY v1 loci directly from the arXiv e-print TeX
  (1605.03893v1): Theorems 1.1 and 1.7, Definition 2.1, the u-side
  "Sketch of proof" label of Proposition 3.18's third-derivative halves, the
  §4 k=0..2 r-derivative display (k=0 contradicts the λ=1/2 gauge), the
  Arzelà–Ascoli convergence passage, and the incoming-recovery limit order.
* Audited our compact smooth incoming-profile family against every Kilgore
  hypothesis: solution domain, initial surface, derivative orders, axis
  parity, constants and cone-vertex uniformity (point-by-point table, §3 of
  RESULT.md).
* Ran three bounded computational checks (0.13 s total, under the 10 s/30 s
  caps, no analytic claim replaced by numerics).
* Wrote `RESULT.md` (full audit with point-by-point obligations and the
  strongest counterexample), `sources.jsonl` (4 records, schema-compliant),
  this report, and the authorized root `AGENT_REPORT.md`.

## Not done / explicitly avoided

* Luk–Oh 2108.13379 full text not fetched (brief: "only if necessary" — not
  necessary; hypothesis package available verbatim via Kilgore's
  restatement, flagged as secondary). Only the abstract page was fetched.
* No published-LOY §3–§4 comparison: access blocked (see below). No
  corrections invented.
* No new existence theorem, no bridge lemma claimed, no manuscript edits, no
  board/runner/seed changes, no installs, no child agents, no pushes.

## Search capability check

* `exa.web_search_exa` — **worked**. Used once to locate the published LOY
  record; returned the Springer landing page (DOI 10.1007/s40818-017-0038-4,
  Ann. PDE 4:3, 2018, published online 17 Nov 2017) and the arXiv/INSPIRE
  records. A second exa query for open-access copies of the published PDF
  also ran (no OA copy exists; author pages link only to arXiv v1).
* `web-search-prime` — not used, per brief (separate quota exhausted).
* Direct primary fetches used `curl` against arxiv.org e-print/abs endpoints
  and link.springer.com; all in-scope, public sources only.

## Source coverage and reading depths

| Source | Depth | Access |
|---|---|---|
| Kilgore arXiv:2108.13377v1 (TeX) | full-text, selected loci verbatim (abstract, §1 fn1, §2 defs, §3 thms, §5 intro, §6.1–6.2, §7 all, Luk–Oh restatement) | open |
| LOY arXiv:1605.03893v1 (TeX) | full-text, selected loci verbatim recheck | open |
| LOY published Ann. PDE 4:3 (2018) | abstract + metadata only | **blocked** (303 → idp.springer.com; no OA copy on Luk/Oh/Yang pages) |
| Luk–Oh arXiv:2108.13379 (v1 2021-08-30, v2 2021-12-14) | abstract only | open; full text deliberately not fetched |

Version pins: 2108.13377 has only v1 (30 Aug 2021); related published DOI
10.1007/s00023-022-01162-4 (not accessed). 1605.03893 has only v1
(12 May 2016). Details and exact loci in `sources.jsonl`.

## Verification commands and results

```sh
# primary fetches (public arXiv endpoints)
curl -sL https://arxiv.org/e-print/2108.13377v1   # Kilgore v1 TeX tarball
curl -sL https://arxiv.org/e-print/1605.03893v1   # LOY v1 TeX (gunzip → .tex)
curl -sI https://link.springer.com/content/pdf/10.1007/s40818-017-0038-4.pdf
#   → HTTP/2 303, location: idp.springer.com/authorize...  (paywalled)

# numbering checks
grep -n "footnote{" nonlin_stab.tex        # line 136 footnote is the first (of 4)
grep -n "newtheorem" nonlin_stab.tex       # shared per-section counter → Def 2.5/2.6
grep -n "sum_{k=0}^{2}" main.tex           # LOY §4 display at lines 2045/2047/2049
grep -n "Sketch of proof" main.tex         # line 1984, u-side third-derivative pair
```

Computational checks (plain Python, no installs; measured 0.13 s total):

* CHECK1 family identity: `||Φ_{ε,x}||₂ = εβ₀||G||₂` to 1.3e−16 relative with
  the project's β(x) definition; (1.7)-type integral bound verified.
* CHECK2 translated weighted norm: `A_n ≥ (v_*−u_n+1)^{ω′}·εβ_min|G(v_*)|/2`,
  finite per n, divergent across n (≈n² for ω′=2). Confirms
  KILGORE_SCOPE_REPAIR's lower bound with Theorem 1.1's 1/2 normalization.
* CHECK3 formal constant×decay at fixed physical points: n^{ω′−α−1} =
  +1/0/−1/−2 for α=0..3 — no uniform estimate extractable; and that already
  assumes an A-dependence the source never states.

## Strongest contrary evidence

Recorded in RESULT.md §7: the LOY scattering normalization itself
(`lim_{u→−∞} 2∂_v(rφ) = Φ(v) ≠ 0` in the support) violates the literal
I⁻ display of Kilgore's Definition 2.5 for every cone of our sequence, while
the C₁-side translated norm diverges and the constants are data-dependent.
Threefold hypothesis obstruction at statement level. It is explicitly **not**
a nonsmoothness or impossibility theorem, and it does not touch the
in-project conditional smoothness bootstrap.

## Limitations

* Published-version comparison (Prop 3.18 sketches, §4 k=0 display, Def 2.5
  display typo) is access-gated; v1 findings may or may not persist in the
  Ann. PDE text.
* Luk–Oh hypotheses rest on Kilgore's restatement plus the 2108.13379
  abstract; primary wording unverified (deliberately, per brief scope).
* Kilgore's §4–§5 induction, constants and stability proof were not audited —
  statement-level scope only, as recorded in sources.jsonl.
* The charitable ∂_u reading of the I⁻ display leaves an unverified decay
  rate for `∂_u(rφ)(u,v)` as `u→−∞` at fixed v; no source read fixes it.
* The three checks use explicit bump profiles on a grid; they verify the
  project-side algebra, not the papers' estimates.

## Unresolved questions

1. Does the published Ann. PDE §3–§4 expand the u-side proof or fix the k=0
   display? (access-gated; obligation 1 in RESULT.md §8)
2. Primary (D1)–(D8) wording in 2108.13379v2 (obligation 2).
3. Is Definition 2.5's second display a `∂_v`→`∂_u` typo in the published
   version? Either answer changes only the *per-n* obstruction, not the
   uniformity obstruction.
4. Rate of `∂_u(rφ)(u,v)` along I⁻ for scattering solutions (needed only for
   the charitable reading).

## Proposed next tasks

* Coordinator, with institutional access: published-LOY §3–§4 read (typo and
  sketch disposition), then update the axis-source-review residuals.
* Worker task: primary 2108.13379v2 §1–§3 hypothesis extraction before any
  Luk–Oh-route work on the smooth-common-development gate.
* Worker task (mathematical, only if the smoothness bootstrap passes
  integrated review): direct localized uniform higher-order estimates for the
  compact-profile scattering family (the RESULT.md §3 lemma) — noting
  Kilgore's route is closed at hypothesis level.

## Files changed (this submission)

* `research/lawful-completions/higher-regularity-review/RESULT.md` (new)
* `research/lawful-completions/higher-regularity-review/sources.jsonl` (new)
* `research/lawful-completions/higher-regularity-review/AGENT_REPORT.md` (new)
* `AGENT_REPORT.md` (repo root; authorized by the task brief)

No other files touched; no board, runner, shared seed, coordinator or
manuscript files modified.
