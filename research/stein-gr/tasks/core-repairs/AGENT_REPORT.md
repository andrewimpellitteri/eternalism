# AGENT_REPORT.md — stein-core-repairs

Status: submission for coordinator review, 2026-10-25. Worker ran headless in
worktree `/Users/andrew/eternalism/.worktrees/stein-core-repairs`, branch
`agent/stein-core-repairs`. This is a review submission, not an accepted
completion.

## Done / files

- **`PATCH.md`** (this directory): verification that both
  `SECOND_PASS_REVIEW.md` findings are already repaired in the current
  source, with occurrence-by-occurrence checklists, statement-invariance
  argument, three optional non-blocking refinement passages, and a
  verification log. **No replacement passages are proposed for repaired
  material** — per the brief, already-landed fixes are verified and marked
  resolved rather than re-patched.
- **`AGENT_REPORT.md`** (this file).
- No other files created, edited, or committed. `main.tex`, `DRAFT.md`,
  prior reviews, board, runner, and shared registers untouched.

## Pinned source

- `research/stein-gr/main.tex`, 900 lines,
  SHA-256 `7ccc1d37b521e4a25af54c28ffc067066243bd190da79125d922037c90345886`,
  identical at run start and run end.
- Git: HEAD `0c6d2c5`; the manuscript's last change is commit `f8caaa6`
  (2026-10-25 09:35) "Apply second review's repairs: strict chronology in
  topological steps, complete Lemma D case split" — 5 hunks, 31 insertions,
  18 deletions, no theorem-statement hunks, PDF rebuilt in the same commit.
- Prior source state reviewed for context: `SECOND_PASS_REVIEW.md` pinned
  `33f4a667…abb6` (the pre-repair revision). The diff `33f4a667 → 7ccc1d37`
  for the five hunks was inspected directly via `git show f8caaa6`.

## Search capability check (required by brief)

| Tool | Result |
|---|---|
| MCP server `web-search-prime`, tool `web_search_prime` | **FAILED.** Two calls returned `MCP error -429, code 1310: "Weekly/Monthly Limit Exhausted. Your limit will reset at 2026-11-17 10:00:29"`. Recorded as unavailable for this run. |
| Harness `websearch` | **Worked.** One relevant query (Clifton–Hogarth 1995 becoming/reflexive convention); used to confirm the CH 1995 bibliographic identity (Synthese 103, 355–387, doi:10.1007/BF01089733). |
| `webfetch` | **Worked.** Fetched arXiv abstract page and full HTML of Minguzzi–Sánchez v3 (primary-source verification). |

The task needed verification of already-cited sources, not new literature
discovery, so the `web-search-prime` outage did not limit the outcome. If a
later lane needs Z.ai search this week, it should expect the same quota
failure and plan the fallback.

## What was verified (summary; details in PATCH.md)

1. **Strict vs reflexive chronology — RESOLVED.** Framework (ll. 139–145)
   defines `I^±_s`, declares MS's `I^±` strict; imports (ll. 324–330) state
   all topological facts with strict sets; regularity proof (ll. 358–364)
   uses `Int J^- = I^-_s` and adds the diagonal back before closing with
   (CB); the open diamond in Lemma D(iii) (ll. 556–559) uses strict sets.
   All four MS imports matched **verbatim** against
   arXiv:gr-qc/0609119v3 HTML (Prop. 2.16; Prop. 2.17; Prop. 2.31
   preamble+(i)+(ii); Thm. 2.30(i)–(ii); §2.3 conventions; plus the
   causally-simple closure identity `Ī = J̄ = J` in §2.4 that underwrites the
   regularity closure chain).
2. **Lemma D first-exit cases — RESOLVED.** `p ∈ Σ` disposed of before the
   stopping times; `τ_0 ≤ τ_exit` **with equality included** covers the
   simultaneous t=0/shell crossing in the forward inclusion; the reverse
   inclusion is re-run with roles exchanged and no global `t` on `M`, its
   exit/reaches-S dichotomy covering the simultaneous case there as well;
   pullback legitimacy near the closed tube justified by `χ = 1`. I
   independently re-derived the reverse-inclusion assembly (prefix pulled
   back + escape path timelike for both metrics + continuation below `t=0`),
   the escape-path arithmetic (`μr > r/2`, `r/2 + μr < 3r`, speeds `< μ`,
   `6Kr ≤ ε`), the cone-inclusion sandwich
   `D_{η_λ} ⊆ D_{g'} ⊆ D_{η_μ}` from Lemma C, and the `t(ψ(p)) > 0` step
   (left implicit in the text — see PATCH.md §6 R1).
3. **Statements unchanged.** `f8caaa6` touched no definition/theorem/
   lemma/corollary statement; strict sets are derived notation; the reflexive
   CH convention and (CB) are preserved. No genuine statement change exists
   or is needed.
4. **No new mathematical assumption.** Repairs are definitional clarification,
   restated locators, and completion of a geometric case split. MS
   Props. 2.16–2.17 need no causality; the closure identity is used at GH,
   where it holds; simultaneity was a missed case of the geometry, not a new
   hypothesis.

## Source coverage and read depth

| Source | Depth this run | Use |
|---|---|---|
| Minguzzi–Sánchez, arXiv:gr-qc/0609119 **v3** (24 Apr 2008; v3 comments field: matches the ESI proceedings version cited as MS2008, pp. 299–358), HTML full text | full-text of §2.1–2.4 conventions and Props. 2.16–2.17, Thm. 2.30, Prop. 2.31; not a whole-paper audit | verified every imported locator used by the repaired passages |
| `main.tex` (pinned) | full read (all 900 lines) + targeted re-reads | object of verification |
| `SECOND_PASS_REVIEW.md`, `REVIEW_MAIN_PROOF.md`, `REVIEW_OTHER_RESULTS.md`, `INDEPENDENT_REVIEW.md` | full read of finding sections, grep of rest | avoided re-litigating resolved items; confirmed G1–G3 repairs and that my two findings were the open items |
| CH 1995 (Synthese 103) | **not read directly** (paywalled); p. 360 reflexive convention relied on as previously verified in `REVIEW_OTHER_RESULTS.md` line 114; bibliographic identity confirmed via web search | convention attribution |
| Bernal–Sánchez 2006, Choquet-Bruhat–Geroch 1969, Hawking–Ellis 1973, BFV 2003, FV 2012, WC 2017, Stein 1968/1991, etc. | not read this run (cited in manuscript; outside my two findings) | — |

## Verification commands and results

```text
shasum -a 256 research/stein-gr/main.tex   # before and after: 7ccc1d37…45886
git show f8caaa6 --stat ; git show f8caaa6 -- main.tex
grep -n 'Ichr\|Ifut\|\\ll\|\\gg\|horismos\|E\^-' main.tex   # 80 hits, all classified
webfetch https://arxiv.org/abs/gr-qc/0609119        # version pin
webfetch https://arxiv.org/html/gr-qc/0609119v3     # primary text
websearch "Clifton Hogarth 1995 definability objective becoming …"
pdflatex -interaction=nonstopmode -halt-on-error main.tex  (×2, on a copy in
  /private/tmp/opencode/stein-build)
  -> exit 0 both passes; 13 pages; 0 undefined references
```

No installs; no global configuration changed; no subagents launched.

## Strongest contrary evidence (what I tried to break)

- I attempted to break the repaired Lemma D(ii) in four ways and each
  resolved: (a) `t(q) = 0` "exit" in (i) — excluded by `t`-monotonicity plus
  spacelike `S`; (b) reverse-inclusion compression "the same two cases apply"
  — the assembly works, including simultaneous exit-at-S (reaches-S case);
  (c) escape-path endpoint arithmetic — correct; (d) pullback at the shared
  endpoint `τ_0 = τ_exit` — valid since `χ = 1` on `overline{T_{2r}}` and `Φ`
  is a diffeomorphism on `T_{ρ0}`.
- I attempted to find a residual strict/reflexive defect at all 80 chronology
  occurrences; none found. The only soft spots are explicitness gaps, logged
  as optional refinements R1–R3 in PATCH.md §6 (justify `t(ψ(p)) > 0`;
  attach "an open set" unambiguously — also fixes an overfull line introduced
  by the repair commit; define `≪'` at first use). All three are
  presentational; none blocks correctness.
- I checked that Prop. single genuinely *uses* reflexivity (`(x,b) ∈
  J^-(x)×J^+(b)`), i.e. the convention change did not silently alter any
  example — it did not.

## Limitations

- My verification is a careful hand check, not a machine-checked proof;
  PATCH.md's checklists record reasoning, not certificates.
- MS page-level locators for the printed ESI book were not verified (I
  verified the arXiv v3 HTML and rely on the v3 comments field for
  v3 ↔ proceedings-version equivalence). If the coordinator wants book-page
  locators as well, that is a small follow-up.
- CH 1995 was not read directly (paywalled); the p. 360 reflexive-convention
  attribution is inherited from `REVIEW_OTHER_RESULTS.md`'s check.
- Scope discipline: I did not re-audit regions outside the two findings
  (cone-control proof details, energy-condition section, causet section)
  beyond what the checklists touched; other lanes own those.
- The two "already fixed" verdicts mean the remaining value of this lane is
  the checklist and the optional refinements; if the coordinator wants
  changes, R1–R3 should be applied by the author/integrator, not by this
  worker's claim.

## Unresolved questions

- None blocking within scope. R1–R3 adoption is the author's/editor's call.
- Whether `web-search-prime` quota resets earlier than 2026-11-17 (relevant
  to other lanes, not this one).

## Proposed next tasks

1. `stein-gluing-audit`: independently re-derive Lemma D(ii) both directions
   (especially the reverse-inclusion assembly, which the manuscript states
   only in compressed form) — my verification should not be the only check.
2. Author/integrator: adopt or decline PATCH.md §6 R1–R3 (R2 also fixes an
   overfull line from `f8caaa6`).
3. `stein-paper-integration`: when integrating, keep the statement-freeze
   noted in PATCH.md §7; no statement edits are needed for these findings.
4. Coordinator: record that `web-search-prime` is quota-exhausted until
   2026-11-17 when scheduling literature lanes.
