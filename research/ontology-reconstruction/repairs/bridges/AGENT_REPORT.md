# Agent report: ontology-bridges-repair (runner handback)

29 October 2026. Worker submission for coordinator review; not accepted
completion, not an ontology verdict, no novelty claim. This root report is the
authorized runner handback; it supersedes the previous content of this slot
(`stein-gluing-audit`, 25 October) — archive that before integration, per
[BATCH1_INITIAL_REVIEW](../../coordinator/BATCH1_INITIAL_REVIEW.md).
Full lane outputs live in
[research/ontology-reconstruction/repairs/bridges/](./).

## Task and done/files

Rebuild the bridge-premises lane per the coordinator's §2 findings
(nonentailment vs. circularity; protocol-scoped clipped-Minkowski repair;
three reconstructed bridges; one positive route with defeaters). Predecessor
submission read at its pinned commit
`c15901c3197044c557dc968ffd5e6851f61e283b` in its preserved worktree
(verified clean; unmodified — read-only input).

Files written and to be committed (branch `agent/ontology-bridges-repair`):

- `research/ontology-reconstruction/repairs/bridges/RESULT.md` — self-contained
  repaired framework (neutral reduct, separate existence predicate, admissible
  class, exact SU/UNIQ premises), four-failure-mode taxonomy, three repaired
  bridges, E_all/E_past coexistence analysis, clipped-model protocol repair,
  anchoring constraint, positive route with four defeaters, machine-check
  report, four-way separation table.
- `research/ontology-reconstruction/repairs/bridges/REPAIR_LOG.md` —
  point-by-point response to every coordinator finding and brief bullet, plus
  open items.
- `research/ontology-reconstruction/repairs/bridges/sources.jsonl` — 29
  records, schema-validated (unique IDs, required fields, honest depths).
- `research/ontology-reconstruction/repairs/bridges/checks/expansion_enum.py`
  — standard-library finite-witness program (explicit witnesses, sizes ≤ 4
  elements, ≤ 65 536 enumerated families, no dense grids, no timed-out search
  rerun or enlarged).
- `AGENT_REPORT.md` — this handback.

## Search capability check (recorded per brief)

- `scholar_search` **worked** (29 Oct 2026): query 1 returned exact Crossref
  metadata for Kim, "Concepts of Supervenience", PPR 45(2) (1984), p. 153,
  DOI 10.2307/2107423, and Kim 1987, PPR 48(2), p. 315, DOI 10.2307/2107631;
  query 2 returned Malament 1977, Noûs 11(3), p. 293, DOI 10.2307/2214766,
  plus contrary-scope papers (Rynasiewicz 2001; Sarkar–Stachel 1999).
- `exa.web_fetch_exa` **worked**: fetched Rynasiewicz 2001 (PhilSci-Archive
  293 PDF); abstract + opening section read (~3.5k chars).
- `web-search-prime` **not used, not retried** (per brief). `serpapi_search`
  not tested (not needed).

## Source coverage

Fresh this session: Kim 1984/1987 and Malament 1977 and Sarkar–Stachel 1999
(Crossref metadata, discovery depth), Rynasiewicz 2001 (full-text partial:
abstract + intro). Reused at the predecessor's recorded depths and re-registered
as project records (not re-read, and no claim depends on a fresh reading):
Putnam 1967, Stein 1991, Wüthrich–Callender v1 §§1–4, Pooley 2013 preprint,
Arageorgis 2016, C&R chs. 7/9 extraction, Brading 2013, Dieks 2005,
Rideout–Sorkin 2000, red-team synthesis. Project-internal documents read in
full: coordinator review/run plan, ROADMAP, PREMISE_STRESS_TEST,
ROLE_OF_EXISTENCE, EXPLANATORY_ROLE_TEST, POINT_OF_DISAGREEMENT,
COMMON_EXTENSION_REPAIR, REPAIR_RESULT, mass-classification REVIEW_STATUS,
predecessor RESULT + sources. Partial: CURRENT_SYNTHESIS (first sections),
CLAIM_STATUS (cited row only) — recorded as discovery depth. No source was
upgraded from abstract to proof by assertion anywhere.

## Verification commands and results

```sh
python3 research/ontology-reconstruction/repairs/bridges/checks/expansion_enum.py
# → "All checks passed in 0.7–1.8 s (bound: 10 s per check / 30 s total)"; exit 0.
```

Witnesses: W1 (3-chain: 6 families under shared constraints A1–A4; +UNIV → 1
= E_all; +DOWN+FUTEX → 1 = E_past), W2 (invariance excludes the privileged
family, 2 invariant families remain), W3 (4-diamond: TRANS filters nothing —
causal-past and bow-tie analogue both survive), W4 (chain+isolated: TRANS
filters the uniform bow-tie analogue, a hybrid survives — filtering is
category-relative), W5 (protocol surrogate: matched past records identical,
lifetimes differ, future records distinguish). JSONL validation: 29 records,
unique IDs, all required fields (script inline, exit 0).

## Strongest contrary evidence (kept in view)

1. C&R's later-grounded bivalence (ch. 7 (GR) p. 110; ch. 9 bow tie and
   intransitivity): denies the constitution cut while granting all physics —
   the strongest live rival to both A′ and B′, and the substance of defeater 2.
2. The reviewed closed-dust mass classification (F_m(b) = M for π ≤ τ < 2π):
   determination outruns the causal past, giving an exact internal defeater to
   the selected Stein route (RESULT §6.2, defeater 1) — cited at internal
   review status only.
3. Rynasiewicz 2001 and Sarkar–Stachel 1999: the Malament definability result
   does not settle interpretation by itself — new this session, integrated
   into §5.2 so Bridge C′ makes no unclaimed scope claim.
4. The coordinator's own points: assignment-pluralism does not refute
   supervenience (a rival may reject the plural class); and the Putnam
   argument is valid-but-unsound rather than circular.

## Limitations

- The positive route's step-4 tie-break (record-bearing vs. determination) is
  stated and motivated, not proven; the two tie-breaks demonstrably diverge
  (defeater 1). Choosing between them is left open.
- Internal results used at recorded internal-review status (sharpness
  example, readout agreement, F_m classification); external review pending —
  integration inherits that limit.
- Putnam/Stein/W–C/Pooley/Arageorgis/C&R/Brading not re-read this session;
  their locators and quotations are carried at the predecessor's recorded
  depth. Kim 1984 cited for the taxonomy name only (metadata depth); SU/UNIQ
  formulations are ours.
- Malament 1977 remains unread in full in this lineage (two sessions);
  Sarkar–Stachel 1999 metadata-only.
- The finite witnesses are exact about premise-set behavior on the stated
  reducts and about the protocol logic; they are surrogates, not
  relativistic theorems — the continuum claims rest on the cited
  project-internal results.

## Proposed next tasks

1. Coordinator: reconcile this repair with the equivalence- and rivals-repair
   lanes into the planned premise-by-rival matrix (BATCH2_RUN_PLAN).
2. A full-text read of Malament 1977 and Sarkar–Stachel 1999 to fix the exact
   scope conditions of the definability anchor before any stronger Bridge C′
   claim (cheap, bounded).
3. A Kim-1984-checked upgrade of the SU/UNIQ terminology (cheap; reviewer may
   fold into integration).
4. Investigate whether any independently motivated constraint set forces UNIQ
   without embedding an existence conclusion (RESULT §9) — the standing gap
   W1 exposes.
5. If the F_m classification survives external review: state the
   determination-tie-break rival's ontology precisely and test it against the
   record-bearing tie-break on the closed-dust model — the exact live dispute
   the Stein route must win or concede.

## Blockers

None blocking submission. Open items are recorded above and in REPAIR_LOG §8
rather than resolved by assertion. Search-service quota for
`web-search-prime` was assumed unavailable per brief; `scholar_search` and
`exa` sufficed for this scope.

## Compliance

Owned paths only (`research/ontology-reconstruction/repairs/bridges/` + this
root handback). No board/runner/shared-seed/manuscript edits, no installs, no
subagents, no push/merge/deploy. Commit below stages only the five named
files — never `git add -A`.
