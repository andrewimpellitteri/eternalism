# AGENT_REPORT — kb-relational-markov-audit

Task: audit the derivations of arXiv 2606.08595 (Nandi & Petruccione, v1) against
the four open questions in `knowledge/COORDINATOR_REVIEW.md`. Branch
`agent/kb-relational-markov-audit`; worktree
`/Users/andrew/eternalism/.worktrees/kb-relational-markov-audit`.

This is a resumed run: `git status` and `git log` showed the previous attempt left
**no** committed or untracked work in the allowed paths (working tree was clean,
no `knowledge/relational-markov/` existed), so this run started from the clean
baseline rather than discarding anything.

## Done / files

- `knowledge/relational-markov/audit.md` — the deliverable: four-question table
  with verdicts, equation locators and quotes; per-question evidence; conceptual
  placement (ontology/passage/determinism/causal order/clock time/thermodynamic
  arrow kept distinct); nearest predecessors with defeat conditions; limitations.
  Verdicts: **Q1 unclear (and the main text's account of its own derivation is
  contradicted by the supplement's steps)**; **Q2 unclear (none of the four
  non-Markovianity notions is formulated; only O(g²) generator-level time-
  nonlocality is established)**; **Q3 established-in-one-sentence / consequences
  unclear / outcome probabilities absent**; **Q4 established (all dynamical
  results are O(g²) under stated extra assumptions)**.
- `knowledge/relational-markov/sources.jsonl` — 5 records, validated: unique IDs,
  required fields present, `read_depth` from the allowed vocabulary, full-text
  record carries the extended fields (authors, version, DOI, locators,
  assumptions, conclusion, proof_status, related IDs, open questions).
- Reused existing IDs rather than duplicating: `seed-relational-markov-2026`,
  `frontier-relational-markov-2026` (referenced as related IDs of the new
  full-text record). New lane-prefixed IDs: `rmark-nandi-petruccione-2026`
  (full-text), `rmark-chruscinski-2022`, `rmark-nestmann-2021`,
  `rmark-blpv-2016`, `rmark-anastopoulos-hu-2013` (all abstract).

## Search capability check

- **`web-search-prime.web_search_prime` (Z.ai MCP): WORKED.** Test query
  "arXiv 2606.08595 relational Markovianity clock conditioning" returned the
  target paper's abs/HTML/PDF pages as the top three hits plus related literature.
  Used for citation chasing (Anastopoulos–Hu identifier). The OpenCode built-in
  `websearch` errored once ("cancelled") on the same lookup; `webfetch` worked
  throughout for landing pages.

## Source coverage

- Audited paper: full text read via the LaTeXML HTML build (main + Supplemental
  Material, Eqs. 1–61); equation numbers/content cross-checked against MathML
  alttext. PDF not opened (recorded in limits).
- Comparison anchors at abstract depth (per task, "at the abstract level at
  least"): Chruściński 2209.14902; Nestmann–Bruch–Wegewijs 2002.07232v2 (= PRX
  11, 021041); Breuer–Laine–Piilo–Vacchini 1505.01385 (= RMP 88, 021002);
  Anastopoulos–Hu 1305.5231v3 (= CQG 30, 165007).
- Citation chasing stayed deliberately small (4 added sources); Page–Wootters,
  Gambini–Porto–Pullin, Trushechkin etc. are discussed via the audited paper's
  reference list but deliberately **not** recorded as read sources.

## Verification commands and results

- Identifier verification: fetched landing pages `arxiv.org/abs/{2606.08595,
  2209.14902, 2002.07232, 1505.01385, 1305.5231}`; each record's version, dates,
  journal ref and DOI were taken from the landing page itself. Notably, the
  Anastopoulos–Hu arXiv ID was *found by search and verified* to be **1305.5231**
  (not from memory); its published DOI 10.1088/0264-9381/30/16/165007 and the
  NBW/BLPV journal DOIs are as listed on their landing pages. All DOIs cited are
  either arXiv-issued DataCite DOIs shown on the landing page or publisher DOIs
  listed there as "Related DOI"; no DOI was recorded from a secondary source.
- Full-text extraction: `curl -sL https://arxiv.org/html/2606.08595v1` (271,569
  bytes) + Python tag/alttext conversion; JSONL validated with a Python schema
  check (5 records, unique IDs, required+extended fields, read_depth vocabulary).
- Text searches used as evidence: "instrument" occurs only in the main text
  (Eqs. 5 context); "postselection"/"Kraus"/"outcome" occur nowhere; "normaliz"
  occurs only at Eq. (7) and in unrelated flow-vector contexts. These negative
  results back the Q1/Q3 verdicts.

## Strongest contrary evidence (against my verdicts)

- The paper's own framing could be read as: the instrument `J^(σ)` is an
  *abstraction* and the gate construction its *microscopic model*, with both
  yielding the same kernel — the supplement does derive the kernel Eq. (11) from
  a concrete clock-bath model, and the factorization step (Eqs. 36–42) is correct
  as written. If a reviewer can construct the Kraus operator of `J^(σ)` from
  `F_σ(T̂−τ)` and show the conditioned dynamics of Eqs. (5)-(7) equals the
  gated-channel dynamics of Eqs. (23)-(31), the Q1 contradiction dissolves into
  "established".
- For Q2, one could argue a time-nonlocal kernel in the generator *entails*
  semigroup failure trivially (no Markovian semigroup has such a generator), so
  the paper "really" establishes at least that. My audit stops short because the
  paper defines no map family and no composition law to fail, and because
  NBW/Chruściński-level results show kernel presence does not fix the
  standard non-Markovianity notions; but a reviewer favoring the trivial reading
  would downgrade the severity, not the facts, of Q2.
- For Q4, "second order" is stated by the paper itself (`+O(g³)`), so a reviewer
  might say the paper never claims more; true for the derivation sections, but
  the Conclusion's unhedged "demonstrating that temporal nonlocality is not
  merely a consequence of environmental complexity" goes beyond the derivation —
  that mismatch is the substance of the Q4 finding.

## Limitations

- HTML-only read of v1; no PDF cross-check; no page locators.
- The step between supplement Eqs. (33) and (44) (TCL promotion) was assessed,
  not re-derived; nothing numerically or machine verified; no code reproduced
  (per task).
- Comparison papers at abstract depth; their section-level criteria not
  extracted, so the Q2 verdict is phrased against the audited text plus the
  taxonomy framing of the comparison abstracts, not against their internals.
- AH correspondence (audited Eq. 61 vs AH's equation) explicitly **not**
  verified; recorded as an open question in the source record.
- Chruściński 2209.14902 shows no journal ref on its landing page; if a
  published review version exists, the record should be updated after
  verification.

## Proposed next tasks

1. **AH correspondence check** (small, well-scoped): read AH 1305.5231v3
   full text; compare audited Eq. (61) operator-by-operator (ordering, kernel
   definitions N/D vs G decomposition, signs, order in κ).
2. **Divisibility analysis** (medium): for the supplemental per-τ linear map,
   construct the two-parameter family and test P/CP-divisibility; this would
   turn the paper's "generically non-Markovian" into a precise statement or a
   counterexample — including checking whether the normalized Eq. (7) route and
   the linear Eq. (31) route differ in divisibility.
3. **Chruściński + NBW full-text pass** (small): extract exact divisibility
   definitions and the `G = K̂[G]` fixed-point theorem with locators, to certify
   the Q2 taxonomy placement against definitions rather than abstracts.
4. **Coordinator follow-up**: if a v2 of 2606.08595 appears (e.g. with a Kraus
   form for `J^(σ)` or a normalized-state master equation), re-audit Q1–Q3
   against it; today's "unclear" verdicts are version-specific.

## Coordinator review (2026-10-20)

Checked against the arXiv HTML of 2606.08595v1 (fetched 2026-10-20):

- Quoted verbatim and present: "Applying the clock instrument and tracing over the bath and clock sectors…" (before Eq. 10); "the normalized conditioned state evolves nonlinearly…" (after Eq. 7); "Promoting the perturbative expansion…"; "Equation (44) is generically non-Markovian…"; the Fig. 1 caption's "in the sharp-clock limit"; both Conclusion sentences; "if the dressed kernel is of positive type".
- Eq. (23) gates the bath operator with `F_σ(T̂(x)−τ(x))` inside the interaction (Eq. 24), and Eq. (31) is a plain partial trace over clock and bath, as the audit says.
- "instrument" occurs only twice, both in the main text; "postselect", "outcome", "Kraus", "divisib", "backflow" and "process tensor" never occur. "semigroup" occurs only as GKLS/Lindblad background and in citations. The Q1–Q3 verdicts follow.
- The audit's linear-channel argument for the supplement's per-τ map holds if `F_σ` is real-valued, which the text implies but does not state.
- Not re-checked: the Q4 equation-by-equation order claims beyond Eqs. (10), (30), (31), (37), (43).
- Moved this report into the lane directory and removed two `10.48550/arXiv` DOI fields that the Crossref-based checker cannot resolve.
