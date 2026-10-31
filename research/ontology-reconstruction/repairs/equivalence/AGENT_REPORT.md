# AGENT_REPORT — ontology-equivalence-repair

29 October 2026. Lane `ontology-equivalence-repair`, branch
`agent/ontology-equivalence-repair`, worktree
`/Users/andrew/eternalism/.worktrees/ontology-equivalence-repair`.

**Handback (authorized runner slot).** Task complete; this is a worker
submission for independent coordinator review, not an accepted result, not an
ontology selection. No push, merge, deploy, board edit, runner edit, extra
agents, or installs were performed. Predecessor worktree
`ontology-expansion-equivalence` verified at exactly
`d26520bf3b1580f8f2cb3345083db4a3518c7c92` (clean) before work began and
re-verified clean and unchanged after; it was used read-only.

**Provenance note on this root slot.** Before this commit, AGENT_REPORT.md at
the repository root held the stale handback of the `stein-gluing-audit` lane
(25 October 2026, `claude-head`), whose deliverable lives in its own lane
directory and whose text remains in git history at commit `0c6b383`
(HEAD~1). Per BATCH1_INITIAL_REVIEW ("root report changes are the runner's
authorized handback slot; archive them before integration"), this lane's
handback replaces that stale content; nothing of the audited result is lost.

## Done / files

Repairs of all five coordinator findings (BATCH1_INITIAL_REVIEW §1) plus the
brief's specific obligations. Deliverables (the only research files written):

- `research/ontology-reconstruction/repairs/equivalence/RESULT.md` —
  self-contained repaired result: corrected causal-past definability with
  analytic proof (Lemma 1); cone census repaired by the subgroup orbit
  argument, now holding in 1+1 as well, with exact group/dimension assumption
  table (including the reflection-free 4-expansion variant and the 0+1
  collapse); clause-wise exclusions separating causal boundedness from
  nonuniversality; the poset example rebuilt as per-expansion definability
  (displayed formulas) vs exact failure of uniform recovery, with
  "inexpressible" rhetoric removed; the Barrett 2018 map re-derived with
  pinned quantifiers from primary text read this run; category vs Morita
  hypotheses pinned (Weatherall criteria/morphisms, Tsementzis doctrine
  scope, Barrett–Halvorson locator-not-read, AMNS 2023 counterexamples); one
  corrected test (EDT-R) with its strongest limit stated.
- `research/ontology-reconstruction/repairs/equivalence/REPAIR_LOG.md` —
  point-by-point responses to findings 1–5 plus brief obligations, each with
  action, location, and resolved/gated status; compliance section.
- `research/ontology-reconstruction/repairs/equivalence/sources.jsonl` —
  15 records, lane prefix `eqr-`, schema per knowledge/README.md; validated
  (parse, required fields, depth vocabulary, full-text extended fields,
  unique IDs — all pass).
- `research/ontology-reconstruction/repairs/equivalence/check_repairs.py` —
  strengthened finite check (standard library, exact `fractions.Fraction`
  arithmetic): Part A exact poset checks A1–A6 (rigidity, three labellings,
  displayed element formulas, displayed per-expansion pair formulas certified
  on all 9 pairs, pairwise-distinct growth relations + semantic census of all
  512 relations, test-sentence variation); Parts B1–B4 and C1 exact rational
  witnesses for the Minkowski facts (definability formula on six point kinds,
  ≪-preservation by sampled boost/dilation/reflection on 100 sampled pairs,
  exact-boost isometry, null-cone orbit walks, candidate invariance on a
  closed witness set, 0+1 collapse).
- This root `AGENT_REPORT.md` (authorized handback).

No other files were touched. Nothing under any other lane was modified.

## Search capability check (required by brief)

At session start, per brief ordering (web-search-prime NOT retried):

- `scholar_search` — **worked** (OpenAlex backend). First query returned
  Barrett 2018 (with DOI and abstract) plus two new highly relevant leads:
  Andréka–Madarász–Németi–Székely 2023 (RSL) and Barrett–Manchak 2026
  (PhilSci-Archive 30643).
- `exa` — **worked** (`web_search_exa` and `web_fetch_exa`). Fetches used:
  the PhilPapers Barrett PDF (substantial full text extracted through exa's
  pipeline of the same URL whose direct fetch 403'd for the coordinator —
  access route recorded in sources.jsonl), the Zeeman 1964 public PDF
  (first page incl. abstract, theorem, Remarks 1–4), arXiv abstract pages
  (2211.14232v2, 1507.02302v1, 1301.2412v2), arXiv HTML v3 of Weatherall
  (≈66k chars), and PhilSci record pages.
- `serpapi_search` — **quota exhausted** ("Your account has run out of
  searches"). Recorded, not worked around; not needed.
- `web-search-prime` — not retried, per brief.
- Access limits retained honestly: Barrett–Manchak 2026 PDF body not
  extractable (PhilSci direct fetch rejected; exa returned title+abstract
  only; no arXiv copy) → recorded abstract-only, flagged "read in full
  before any use". Hodges 2008 and Svenonius 1959 originals unread
  (inherited locators). Zeeman proof body not audited. Weatherall HTML
  substantially but not exhaustively read.

## Source coverage

15 records in `sources.jsonl`: 4 at full-text depth this run (Barrett 2018;
Zeeman 1964 first page; Weatherall 2016 arXiv HTML; predecessor RESULT.md),
5 abstract-depth records fetched this run (AMNS 2023, Tsementzis 2017,
Semenov–Soprunov 2015, Barrett–Manchak 2026, plus abstract leads
Minguzzi–Sánchez 2008 and Stoica 2016), 1 discovery record
(Barrett–Halvorson 2016, locator only), 5 project records (predecessor
RESULT + its 34-record sources register at their recorded depths, the two
coordinator documents, the knowledge-base contract). No source was upgraded
from abstract to proof anywhere in the deliverable; second-hand locators are
marked as inherited.

## Verification commands and results

```sh
# predecessor preservation (before and after work)
git -C /Users/andrew/eternalism/.worktrees/ontology-expansion-equivalence rev-parse HEAD
#   -> d26520bf3b1580f8f2cb3345083db4a3518c7c92 ; status clean both checks

# strengthened finite check (owned deliverable)
python3 research/ontology-reconstruction/repairs/equivalence/check_repairs.py
#   -> A1–A6, B1–B4, C1 all PASS; wall time 0.006 s (< 10 s bound; total
#      session computation far under the 30 s bound; no dense-grid or
#      pairwise enlargements; standard library only)

# sources.jsonl schema validation
python3 -  # parse JSONL; required fields; depth vocabulary; full-text
           # extended fields; unique ids
#   -> records: 15, unique: 15, issues: [] -> VALIDATION PASS
```

Debug history (for review transparency): three early script defects were
found and fixed before the final run — a wrong per-expansion formula
construction (self-keyed instead of stage-pair disjunctions), a sign error in
the Minkowski tests (chronological = Q > 0 under Q = t² − x²), and three
component/sign typos in witness literals. The committed script is the
passing version; nothing in the deliverable depends on the intermediate
runs.

## Strongest contrary evidence

Summarized from RESULT.md §8; the load-bearing ones:

- Barrett 2018's own theorems are partly *pro*-symmetry (E2 ⟺ S1; E1 ⟺ S2 ⟺
  S3): the repaired examples instantiate exactly the pockets his results
  mark out (incomplete contract theory; rigid/pointwise-definable base), and
  do not contradict them.
- If any source states the Lemma 1 formula (causal past definable from
  chronology) explicitly, §2 becomes exposition of a known fact — proof
  intact, derivation-claim not. Bounded negative search performed (two
  scholar/exa queries; the closest hits — Stoica 2016's horismos-based
  reconstruction and the causal-hierarchy survey — are recorded as adjacent
  leads at abstract depth); no completeness claim for this search.
- Barrett–Manchak 2026 may already contain the §5 map in GR form; it is
  unread beyond the abstract, so §5 makes no priority claim against it.
- A rival restricting the comparison group to exclude spatial reflection
  gets four expansions in 1+1 (recorded, §3.4) — which strengthens
  underdetermination rather than restoring uniqueness; noted so the census
  is not oversold.

## Limitations

- All Minkowski claims are Minkowski-domain; curved-spacetime analogue of
  Lemma 1 and of the census is OPEN (leads recorded at abstract depth only).
- The empirical-agreement note for the cone pair remains informal
  (timelike finite-precision records), marked [OURS: PROPOSAL].
- Finite checks: Part A is exact/complete for the fixed 3-element structure;
  Parts B/C are explicit witnesses illustrating analytically proved
  statements — they are not the proofs, and they say nothing about
  unsampled points.
- Inherited project-record depths (STRONGEST_VIEW, discriminators-audit,
  etc.) were not re-verified this run.
- All verdicts are base-relative; no broad equivalence, inexpressibility, or
  novelty claim is made anywhere in the submission (explicit in §0, §6, §9).

## Unresolved questions / proposed next tasks

1. Obtain and read the Barrett–Manchak 2026 full text (PhilSci 30643);
   compare its implicit-definability hierarchy with the §5 map and check
   whether any Example-1-style census already appears there.
2. Read Tsementzis 2017 and Barrett–Halvorson 2016 bodies before any Morita
   identification is used in synthesis; inspect AMNS 2023 Example 2's
   construction before citing its negative examples beyond the abstract.
3. Curved (FLRW / static) analogues of the cone census, and the separation-
   axiom conditions under which the Lemma 1 formula characterizes the causal
   past (Minguzzi–Sánchez lead).
4. Reconcile this lane's verdict matrix with the bridges- and rivals-repair
   lanes in the coordinator's planned premise-by-rival matrix (BATCH2 plan).
5. The 0-expansion (existence-failure) column still rests on the
   predecessor's cited project theorem (percolation completion); a fresh
   source-audited census template would be useful before it feeds any
   classification lane.

## Blockers

None blocking. Recorded for honesty: serpapi quota exhausted; Barrett–
Manchak 2026 full text inaccessible this session; Hodges/Svenonius originals
unread (inherited locators only, marked throughout).
