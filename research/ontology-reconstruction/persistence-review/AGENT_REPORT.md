# AGENT_REPORT — ontology-persistence-review

29 October 2026. Independent adversarial review of
`research/ontology-reconstruction/coordinator/PERSISTENCE_CONVENTIONS.md`
(commit `634988e`). Submission for coordinator inspection; not accepted
completion and not a truth claim. Full line-by-line verdicts in
[RESULT.md](RESULT.md); source register in [sources.jsonl](sources.jsonl).

## Done

- **Collapse claim verified (done-when #1).** S + P_c ⇒ J⁻(b) ⊆ E_b is a
  correct one-line argument needing only reflexivity and transitivity of the
  order; with causal boundedness it forces E_b = J⁻(b), so earlier
  two-case claims under S + P_c + boundedness collapse to one (J). The
  I⁻∪{b} candidate fails P_c on the exact null step (0,0)→(1,1) while
  satisfying P_t. Retractions R1–R3 in RESULT.md §7 specify which earlier
  submission claims must change; BATCH2 and PREMISE_STRESS_TEST claims
  need no retraction.
- **Census, converses, and added-premise table independently audited
  (done-when #2).** All 24 proof obligations (O1–O24 in RESULT.md) verified
  analytically and, where witness-checkable, by exact rational arithmetic:
  the covariance reduction, future-set lemma, saturation bridge
  (q_Z ≪ p_S ⇔ 2ZS > R²+S², iff both directions), null-orbit arguments,
  exhaustive four-case partition, all four converse clauses (including B's
  x=b edge case), all ten table rows, and the collar counterfamily.
- **Prior-art and ontology scope kept explicit (done-when #3).** CH 1995
  Theorem 1 ({I,J,U} under transitivity) interlocks with the census rather
  than duplicating it; Thyssen's bowtie present is elsewhere-only and is
  not B or C (primary passage fetched); no prior statement of the census
  found at the searched depth; no novelty claim made.
- **New finding:** in 1+1 Minkowski without parity, a **fifth** covariant,
  self-inclusive, chronologically persistent, F_t-respecting assignment
  exists (A' = {0} ∪ {a ∉ I⁻(0) : t+x > 0}, E_b = b − A'). This confirms
  the coordinator's n≥2 hypothesis is necessary for the census statement
  and resolves his open 1+1 caveat in the strongest way: the hedge should
  be upgraded from "the orbit argument changes" to "additional assignments
  exist". It does not refute the census, which is asserted only for n ≥ 2.

## Files

Owned directory `research/ontology-reconstruction/persistence-review/`:
`RESULT.md`, `sources.jsonl`, `AGENT_REPORT.md`, `check_independent.py`,
`check_1plus1_fifth.py`. Authorized root `AGENT_REPORT.md` (this file's
companion summary at repo root). Nothing else touched; no coordination
files, board, runner, shared seeds, or other lanes edited.

## Search capability check (required at start)

- `scholar_search` (server: scholar_search): **worked** — first relevant
  query returned openalex/crossref/arxiv records, including the Clifton–Hogarth
  crossref record (Synthese 103(3):355–387, 1995) and Thyssen 2019 metadata.
- `exa` web_search_exa and web_fetch_exa: **worked** — fetched Thyssen 2019
  open-access Springer HTML, Thyssen 2025 preprint (philarchive THYFDO),
  Thyssen RPM chapter (THYTRA), Savitt 2020 philsci PDF.
- `serpapi_search`: available but not needed after the above succeeded;
  not exercised. `web-search-prime`: not retried, per brief.
- Read depths recorded honestly in sources.jsonl; the CH primary scan was
  NOT reread (inherited full-text audit used, provenance recorded there).

## Source coverage

Primary/nearest-prior: Clifton–Hogarth 1995 (inherited full-text audit),
Thyssen 2019 (abstract + §§1–2 + bowtie excerpt), Thyssen 2025 Four Degrees
(abstract/TOC — checked near-miss, taxonomy not census), Thyssen RPM chapter
(abstract/TOC), Savitt 2020 (abstract/excerpts), Placek 2010 (discovery),
SEP background (discovery). Project files: coordinator deduction (full-text),
BATCH2_INITIAL_REVIEW (full-text), PREMISE_STRESS_TEST (full-text),
clifton-hogarth audit (full-text). Gaps: Thyssen §§3.4/7–8 not fully read;
growing-block and "wide present" literatures only sample-searched —
recorded as limits, not as evidence of absence.

## Verification commands and results

```sh
time python3 research/ontology-reconstruction/coordinator/check_persistence_witnesses.py
# PASS (all four lines); 0.08s wall — coordinator's script reproduced, not edited

time python3 research/ontology-reconstruction/persistence-review/check_independent.py
# PASS O1–O21 (17 PASS lines); 0.26s — exact Fraction arithmetic

time python3 research/ontology-reconstruction/persistence-review/check_1plus1_fifth.py
# PASS (5 PASS lines); 0.48s — fifth 1+1 assignment constructed and checked
```

Total compute ≈ 0.8 s, within the 10 s per-check / 15 s hard-timeout /
30 s total budget. No packages installed; standard library only. All finite
checks are witness checks; nothing finite proves the continuous-domain
census (labeled as such in every script and in RESULT.md).

## Strongest attempted counterexample

Within the asserted scope (n ≥ 2): norm-bounded elsewhere, one-sided null
additions, and mixed-wedge assignments — all eliminated, respectively, by
the saturation bridge (exact negative controls), null-nappe orbit
transitivity, and the proper π-rotation direction reversal. In 1+1 without
parity the fifth assignment above *succeeds*, with a complete analytic case
analysis (future of A' never reaches the left wedge/left null branch because
t_d+x_d > t_a+x_a ≥ 0 for all a ∈ A') plus exact boost-invariance
((cosh,sinh) = (5/3,4/3)), closure, premise, and distinctness checks. Best
reading: the coordinator's scoping was load-bearing and honest; the census
statement itself fails outside it.

## Checks

- Every table row of PERSISTENCE_CONVENTIONS §4 re-proved or given an exact
  failure witness; cl(I)=J and cl(B)=C exposed by boundary sequences.
- CH-theorem/census consistency cross-checked: adding transitivity to the
  census yields exactly {I, J}; removing F_t from it admits U — the two
  classifications meet and part exactly along the transitivity and F_t axes.
- Thyssen bowtie (elsewhere-only) verified distinct from B and C; the
  project's bow-tie row in BATCH2 §4 matches census candidate B.
- Precision notes N1–N4 recorded (implicit orbit-transitivity citations,
  B's x=b edge case, "ordered set" phrasing, strengthening the 1+1 caveat).

## Limitations

- No Lean formalization; the audit is analytic re-derivation plus exact
  witnesses, not machine-checked proof.
- 1+1 no-parity census not completed (one explicit fifth family + its
  mirror; further combinations likely).
- CH primary not reread; Thyssen partial; prior-art search is a
  discovery-level negative result, not a novelty verdict.
- The 1+1 finding is my own deduction, unreviewed; treat it as a candidate
  result like any worker output.

## Proposed next tasks

1. Coordinator integrates retractions R1–R3 and precision notes N1–N4 into
   the census writeup; upgrade the 1+1 caveat per RESULT.md O19.
2. Dedicated prior-art audit of the census (targeted: transitivity-free
   classifications of becoming/reality domains; BST "settled" sets; any
   formal past-plus-elsewhere proposals) before any novelty gate.
3. Optional: complete the 1+1 no-parity census (finite case analysis from
   the wedge/branch orbit structure); optional Lean formalization of the
   four-case census at stated scope.
4. Source-faithful mapping of named rivals (possibilism, growing block,
   elsewhere-present views) onto I, J, B, C and the collar family, without
   silently identifying distinct regions.
