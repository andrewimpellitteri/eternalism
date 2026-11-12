# AGENT_REPORT — ontology-expansion-equivalence

29 October 2026. Sole worker submission for independent review. Not an accepted
result; no board, runner, seed, manuscript, or other lane's files were touched.

## Done

Delivered in the owned directory `research/ontology-reconstruction/equivalence/`:

1. **RESULT.md** — the lane deliverable:
   - a modest comparison contract (CC) treating rival ontologies as
     model-theoretic expansions of a stated base (spacetime, causet, stagewise,
     or records — not assumed to be spacetime subsets, not assumed observable);
   - the six required notions separated (automorphism invariance, definability,
     existence/uniqueness of expansion, equivalence of categories, empirical
     equivalence, metaphysical equivalence) with a sourced implication map and
     its separations;
   - **Example 1 (cone binary)** — invariant-but-underdetermined added
     structure, with exact domain assumptions: on Minkowski spacetime of
     dimension ≥ 3 with base language `{≪}`, every expansion `E(b,x)` satisfying
     chronological inclusion, causal boundedness, self-realization, persistence,
     and full causal covariance is exactly `I⁻(b) ∪ {b}` or `J⁻(b)`. Both are
     invariant *and* definable; the choice is not determined. [proved here on
     Zeeman 1964 + a standard orbit argument; premises are our stipulations]
   - **Example 2 (labelled causet)** — forgetting structure demonstrably loses a
     stipulated grounding claim: a rigid 3-element poset has exactly three
     order-respecting labellings; the claim "c became real before b" is true on
     two and false on one, so it is inexpressible in the tenseless base.
     Machine-checked.
   - the **Expansion Divergence Test** (T0–T5) for the rival-contract and
     classification lanes, with six stated limitations;
   - an independent (logic-first) assessment of parsimony/default preference,
     converging with — but not following — coordinator/EXPLANATORY_ROLE_TEST.md;
   - a status ledger (established theorem / source result / our conditional
     proposal / open gate), contrary-evidence section, and next tasks.
2. **sources.jsonl** — 31 records in the knowledge/README schema (required keys
   verified by script), with read depths, versions/DOIs where verified, and
   limits. Two citation corrections made against primaries: Field 1973 (not
   1974); Svenonius' theorem involves permutations of elementary extensions
   (not plain automorphisms).
3. **check_poset_expansion.py** — standard-library certificate for Example 2.

Plus this runner-root AGENT_REPORT.md. Nothing else committed.

## Search capability check (required at start)

- `scholar_search` (openalex backend): **worked** on first relevant query
  (Svenonius/definability); returned the Semenov–Soprunov IGPL paper used later.
- `exa` MCP (`web_search_exa`, `web_fetch_exa`): **worked** throughout; fetched
  Barrett 2018 (PhilPapers PDF, three slices), Zeeman 1964 (publicly posted PDF),
  Barrett–Manchak 2024 (open-access PDF), Weatherall/Dewar/De Haro pages,
  Mounoud arXiv HTML, North PDF opening, C&R 2020 abstract page.
- `serpapi_search`: available; not needed after the above succeeded.
- `web-search-prime`: **not retried** (quota exhausted until 2026-11-17, per
  brief).

## Source coverage

Primary-source audit before proposals, per brief. Verified from primaries or
primary pages: Zeeman 1964 (statement + remarks), Barrett 2018 (substantial full
text: Props 1–3, Thms 1–3, Examples 1–6, Beth/Svenonius statements), Mounoud
2014 (Thm 1), Barrett–Manchak 2024 (abstract + intro), Weatherall 2016
(abstract + notes), Tsementzis 2017 (abstract), De Haro 2019 (abstract), Dewar
2019 (abstract), Correia–Rosenkranz 2020 (abstract), Semenov–Soprunov 2015
(abstract), North 2009 (opening), Ismael–van Fraassen 2003 (abstract), Sider
2001 (book abstract), Redhead 1975 (metadata), Field 1973 (listings).

Inherited at stated depths, not re-read: Malament 1977, Clifton–Hogarth 1995,
Wüthrich–Callender 2017, Rideout–Sorkin 2000, Brightwell–Luczak 2011, Lipman
2023, Fine 2005 (all project records). Unverified locators left explicitly
unknown: Winnie 1986, Svenonius 1959, Hodges edition identity, Swanson–Halvorson
2012, Hudetz 2018 body, North 2009 pages, Sider parsimony-section locator.

## Verification commands and results

```
python3 research/ontology-reconstruction/equivalence/check_poset_expansion.py
```
Output (abridged): automorphism group size 1; exactly 3 linear extensions;
pairwise non-isomorphic expansions: True; truth of "c added before b" per
expansion {False, True, True}; claim varies: True; ALL CHECKS PASS: True.

```
python3 - <<'EOF'  # JSONL schema check
...
EOF
```
Output: `JSONL OK` (all records parse; all 8 required keys present).

`LC_ALL=C grep` / `perl` check: no stray CJK characters in RESULT.md after two
character-corruption fixes during drafting.

The Example-1 proposition is a hand derivation (no executable certificate); its
checkable premises are Zeeman's theorem and orbit-transitivity of the
orthochronous Lorentz group on null directions (textbook kinematics). A reviewer
can defeat it by exhibiting a third dilation-invariant subset of the punctured
null boundary or an order automorphism outside Zeeman's group in dim ≥ 3.

## Strongest contrary evidence

1. **Barrett 2018 partly supports symmetry-based reasoning** (Thm 1: E2 ⟺ S1;
   Thms 2–3; Svenonius for complete theories). The examples are constructed to
   instantiate, not contradict, his theorems: the §4 contract theory is
   incomplete (the two expansions are not elementarily equivalent) and the §5
   base is rigid. If a reviewer reads the lane as "invariance never helps",
   that over-reads it; the correct statement is Barrett's trichotomy.
2. **Correia–Rosenkranz 2020** formalize presentism/expansionism as logics
   without existence-predicate expansions of physical models; the CC is one
   instrument, not the natural home of every rival (its residue-reporting clause
   is designed for this).
3. **Wüthrich–Callender-style gauge verdicts** would deny that Example 2's
   labelling is ever a commitment; the example then shows the price of the
   growth-realist stipulation, which is all it claims.
4. **Malament-style successes**: in categorical/complete settings invariance
   arguments do yield definability; the lane's warnings are scoped accordingly.
5. **Priority risk**: STRONGEST_VIEW R4 already says "the light cone is the only
   freedom"; Clifton–Hogarth recorded the null-line dilemma. What is claimed as
   new is only the exactly-two covariance collapse in the flat category, the
   causet certificate, the CC, and EDT. Bounded negative search: no screened
   source states the binary proposition (search queries on theoretical
   equivalence/definability/expansion, not a systematic sweep of temporal-ontology
   literature; no completeness claim).

## Limitations

- Example 1 is flat and kinematic (dim ≥ 3; fails in 1+1 per Zeeman's Remark 2);
  curved-spacetime and FLRW analogues are open. Its clauses (inclusion,
  boundedness, persistence) are stipulations covering the fragmentalist/
  growing-past family; presentism is outside the contract by design.
- The empirical-agreement claim for the §4 pair (timelike, finite-precision
  records) is an informal argument, not a theorem.
- Example 2 is a 3-element toy; ancillarity in classical CSG is inherited from
  project records, not recomputed (beyond the toy check).
- Mounoud's generic rigidity is compact-manifold-only; the noncompact spacetime
  analogue is open, so the in-domain rigidity warning rests on the toy case.
- Beth/Svenonius originals not read; the map relies on Barrett 2018's
  statements (proofs read from his text, not independently re-verified).
- No external review; no novelty verdict; submission only.

## Proposed next tasks

1. Rival-contracts lane: apply EDT T0–T2 to its four rival contracts (base =
   marked GH spacetime + records); read Correia–Rosenkranz 2020 full text before
   using their logics as the base theory.
2. Classification lane: adopt the T2 census format as its output schema; the
   cone binary is the flat matter-free template.
3. Curved/FLRW and 1+1 analogues of the expansion census; noncompact-spacetime
   genericity check for rigid bases.
4. Coordinator: the binary + P6/P6′ yields a sharp either/or to put to the
   strongest fragmentalist view (choose the closed cone on a defended premise,
   or accept an undecidable binary).

## Blockers

None. web-search-prime remains quota-exhausted until 2026-11-17 (not needed).
