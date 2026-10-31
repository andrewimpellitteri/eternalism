# Repair log — equivalence lane

Lane: `ontology-equivalence-repair`. Date: 29 October 2026.
Status: submission for independent review; accepts nothing itself; selects no
ontology.

Target: coordinator findings 1–5 in section 1 of
[../../coordinator/BATCH1_INITIAL_REVIEW.md](../../coordinator/BATCH1_INITIAL_REVIEW.md),
against the predecessor submission at commit
`d26520bf3b1580f8f2cb3345083db4a3518c7c92` (worktree
`ontology-expansion-equivalence`, READ ONLY). Repaired content lives in
[RESULT.md](RESULT.md); checks in [check_repairs.py](check_repairs.py);
sources in [sources.jsonl](sources.jsonl).

Provenance and preservation. Before work began the predecessor worktree was
verified at exactly `d26520bf3b1580f8f2cb3345083db4a3518c7c92` with a clean
status; after work it was re-verified untouched (its HEAD and status are
unchanged; no writes were made there). Only relevant predecessor material was
copied or adapted into this lane's own outputs; nothing in any other lane was
modified.

## Finding 1 — "The displayed causal-past definition is wrong."

- Coordinator finding: predecessor §4 displayed `J⁻(b) = {x : x ≪ b ∨ x = b}`,
  which is `I⁻(b) ∪ {b}` under the chronological reading of ≪ and omits the
  nonzero null cone; correct chronological-language definition:
  `J⁻(b) = {x : ∀y (b ≪ y → x ≪ y)}`.
- Action: adopted the coordinator's formula as Lemma 1 and supplied an
  analytic proof (composition direction via causal+timelike = timelike with
  the reversed Cauchy–Schwarz step spelled out; separation direction via the
  ε-witness `y_ε = b + εv` and exact limits of the quadratic form).
  RESULT.md §2. All downstream statements (clause (2), the undecided region
  N, the closed-cone candidate, contract-theory axioms) now cite the corrected
  form. Finite rational witnesses in check_repairs.py Part B1 illustrate it;
  labeled WITNESS, not proof.
- Status: **resolved** (analytic proof, Minkowski domain; curved analogue
  recorded OPEN in the ledger).

## Finding 2 — "The poset demonstrates absence of uniform recovery, not absolute inexpressibility."

- Coordinator finding: elements are individually definable (a: unique strict
  successor; b: unique strict predecessor; c: isolated), so each particular
  linear order is definable by a finite disjunction; what fails is a *single*
  base-language definition recovering the chosen growth order across all
  three expansions.
- Action: RESULT.md §4 now displays the parameter-free element formulas
  (φ_a, φ_b, φ_c), states pointwise definability (stronger than the rigidity
  the predecessor used), displays per-expansion pair formulas δ_i and
  certifies each against its growth relation exactly; then proves failure of
  uniform recovery exactly (pairwise-distinct relations; semantic census of
  all 512 relations on P finds exactly three strict linear extensions; a
  formula has one extension on the fixed structure), and adds the theory-level
  Beth restatement (three expansions over one shared reduct ⟹ I1 fails ⟹ no
  uniform explicit definition). "Inexpressible" rhetoric removed everywhere;
  the test sentence ("c became real before b") is reported as varying across
  expansions while each instance is base-definable. Checks strengthened in
  check_repairs.py Part A (A1–A6), replacing the predecessor's single-script
  claims with per-claim PASS lines.
- Status: **resolved** (per-expansion definability displayed and certified;
  uniform-recovery failure exact and finite; scope guard §4.4).

## Finding 3 — "The claimed 1+1 failure is unsupported and can be repaired directly."

- Coordinator finding: the 1+1 chronological-automorphism group is larger,
  but it contains translations, orthochronous boosts, positive dilations and
  spatial reflection; the origin stabilizer is transitive on the entire
  nonzero past null cone; chronological inclusion and the bound E_b ⊆ J⁻(b)
  leave only the null boundary undecided; a larger group cannot create
  additional invariant subsets of an already-transitive subgroup orbit; no
  full Zeeman classification needed.
- Action: the census is restated (RESULT.md §3.3) with G = any
  ≪-preserving group containing the displayed subgroup — in particular
  G = Aut(M, ≪) itself in every dimension ≥ 2 — and proved along exactly the
  coordinator's route (translation reduction; nesting; orbit dichotomy on N;
  both candidates invariant under all ≪-preserving maps because they are
  {≪}-definable; persistence verified). Boost ray-motion computed explicitly
  in null coordinates; reflection swaps rays; dilations scale radius.
  Zeeman demoted from premise to context (dim ≥ 3 identification of the
  causal-order group; Remark 2 quoted verbatim in RESULT.md §3.3 with his
  wording). The predecessor's "in 1+1 the census below fails" claim is
  **retracted** in the ledger and §3.4. Actual group and dimension assumptions
  tabulated in §3.4, including the reflection-free variant (four expansions
  in 1+1, still two in dim ≥ 3) and the 0+1 collapse (one expansion: no
  nonzero null vector exists). Exact rational witnesses for the group facts in
  check_repairs.py Parts B2–B4 and Part C.
- Status: **resolved** (census repaired analytically; assumptions tabled;
  Zeeman dependency removed from the proof; witness checks added).

## Finding 4 — "Causal boundedness is stronger than nonuniversality."

- Coordinator finding: assuming E_b ⊆ J⁻(b) already excludes eternalism, the
  bow tie and other candidates; the resulting binary cannot select among all
  temporal ontologies; retain the warning.
- Action: RESULT.md §3.2 adds the clause-wise exclusion table (presentism
  excluded by inclusion (1); eternalism and bow tie by boundedness (2);
  standpoint-less variant by (3); two survivors), states boundedness as a
  substantive exclusivity premise that pre-selects the family before any
  census, and scopes the surviving "nonuniversality" to residual freedom
  within the bounded family only. The warning is carried into the corrected
  test's strongest limit (§6).
- Status: **resolved** (distinction explicit and tabled; warning retained in
  synthesis-facing text).

## Finding 5 — "The general logical map needs its own source audit."

- Coordinator finding: the map switches between fixed-model invariance,
  theory-wide invariance and per-model definability; these must not be
  identified without their different quantifiers; the Barrett/Beth/Svenonius
  and category/Morita claims need independent inspection; coordinator fetch
  of the PhilPapers PDF returned 403.
- Action: Barrett 2018 independently inspected this run at full-text depth
  through the exa fetch pipeline (the same PhilPapers URL; the coordinator's
  403 and this access route are recorded honestly in RESULT.md §1 and
  sources.jsonl, with the covered sections listed). RESULT.md §5 pins: the
  structure/theory level split (E_A/S_A vs E1/E2/I1/S1/S2/S3 with exact
  quantifiers and definitions), Prop 1, Prop 2 with the elementary-equivalence
  quantifier and Winnie's "lucid" footnote, Examples 5–6 as the pinned
  counterexamples, Beth (E1 ⟺ I1) with its Hodges locator marked
  inherited-not-read, Svenonius with the completeness hypothesis explicit,
  Thms 1–3, SYM* and its "serious shortcoming", Corollary 1, and Barrett's
  own Morita set-aside. Category/Morita hypotheses pinned separately
  (§5.3): Weatherall's Criteria 1/1′/2 with his exact category/morphism
  choices and the isomorphism-strictly-weaker-than-definitional-equivalence
  statement; Tsementzis' Johnstone-Morita ⟺ common definitional extension
  restricted to his doctrine scope (cartesian/regular/coherent/geometric/
  first-order); Barrett–Halvorson 2016 marked not-read; and the
  Andréka–Madarász–Németi–Székely 2023 concrete-isomorphic-but-definitionally-
  inequivalent examples as the standing warning. Existence vs uniqueness kept
  as a separate column (§5.4). No category equivalence is identified with
  Morita equivalence anywhere in this submission.
- Access limits retained: Barrett–Manchak 2026 PDF body not extractable and
  no arXiv copy — abstract-only record, flagged "read in full before any
  use"; serpapi quota exhausted (recorded); web-search-prime not retried per
  brief.
- Status: **resolved** (map re-derived with pinned quantifiers from primary
  text read this run; Morita caveat honored; access limits recorded). Gate:
  Hodges 2008 and Svenonius 1959 originals remain unread — inherited locators
  only, marked as such; BM2026 full text pending.

## Additional obligations from the brief

- *Corrected chronological-language definition with analytic proof* — done
  (Finding 1 above).
- *Audit the 1+1 exception via the subgroup orbit argument; report actual
  group and dimension assumptions* — done (Finding 3; §3.3–§3.4).
- *Distinguish causal boundedness from nonuniversality* — done (Finding 4).
- *Rigid three-element poset: explicitly define elements and each chosen
  linear order in the base, while proving no single base formula recovers all
  three expansions uniformly* — done (§4; displayed formulas; exact finite
  proofs).
- *Strengthen the finite check to test these exact claims without universal
  inexpressibility rhetoric* — done (check_repairs.py: A1–A6 exact checks
  including the displayed-formula certificates and the 512-relation census;
  B1–B4 and C1 rational witnesses; wall time 0.006 s, well under the 10 s /
  15 s bounds; no dense grids or pairwise enlargements).
- *Independently inspect Barrett; pin every quantifier/hypothesis; try other
  public primary copies for the 403'd PDF; retain access limits* — done
  (exa-mediated full text of the same URL; limits recorded).
- *One corrected preservation/recovery test and its strongest limit; no broad
  equivalence or novelty claim* — done (RESULT.md §6; explicit
  no-selection/no-broad-claim statements in §0, §6, §9).

## Compliance

- Stayed inside `research/ontology-reconstruction/repairs/equivalence/` and
  the root AGENT_REPORT.md; no board, runner, shared-seed, or manuscript
  edits; no installs; no extra agents; no push/merge/deploy.
- Committed only the named owned files plus the root report; no `git add -A`.
- Predecessor worktree preserved exactly at `d26520bf…`; verified before and
  after.
- Search: scholar_search and exa used (capability check recorded); serpapi
  quota exhausted (recorded, not worked around); web-search-prime not retried
  per the brief.
- Known gates for review: Hodges/Svenonius originals unread; BM2026
  abstract-only; curved-spacetime analogue of Lemma 1 open; predecessor's
  inherited project-record depths not re-verified this run.
