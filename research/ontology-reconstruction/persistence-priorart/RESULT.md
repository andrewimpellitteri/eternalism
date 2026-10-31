# Prior-art audit: challenge the persistence censuses against primary predecessors

30 October 2026. Worker `ontology-persistence-priorart`. Target claims: the
internally reviewed **n≥2 four-case census** (I, J, B, C under S, P_t, proper
orthochronous Poincaré covariance, F_t; `coordinator/PERSISTENCE_CONVENTIONS.md`
§§3–4) and the **1+1 no-parity sixteen-case census and its refinements**
(`coordinator/ONE_PLUS_ONE_CENSUS.md`). My job is premise/conclusion comparison
with the closest printed predecessors and a conservative disposition
(known / immediate corollary / unresolved). This is a submission for
coordinator review, not a novelty verdict. No numerical novelty score is
given, and no temporal ontology is selected.

Conventions: x≪b strict chronological, x≤b reflexive causal; E_b the events at
standpoint b; S: b∈E_b; P_t: b≪c ⇒ E_b⊆E_c; P_c: b≤c ⇒ E_b⊆E_c; F_t:
E_b∩I⁺(b)=∅; F_c: E_b∩J⁺(b)={b}; candidates I=I⁻∪{b}, J=J⁻,
B=M\(J⁺\{b}), C=M\I⁺.

## 1. Search capability check (required at start)

| Tool | Result |
|---|---|
| `scholar_search` (openalex backend) | **worked** (first call, Clifton–Hogarth query; returned Savitt 2020 etc.); later calls: openalex OK, arxiv HTTP 400 on one malformed query, crossref HTTP 429 twice |
| `exa.web_search_exa` / `exa.web_fetch_exa` | **worked** (all calls; this is what found the Bigaj full text) |
| Direct public APIs (`fetch`): OpenAlex, Crossref, Semantic Scholar citations, arXiv export API | **worked** |
| `webfetch` on link.springer.com | **blocked** (CSP/challenge page); used exa fetch instead |
| `serpapi_search` | **failed after capability test** ("Your account has run out of searches") — one call attempted, no results |
| `web-search-prime` | **not used** (quota exhausted per task brief) |

## 2. What was found: the closest actual theorems

### 2.1 Bigaj 2008 — strongest near predecessor, now at full-text depth

The project previously held Bigaj's chapter only at discovery depth (known via
Thyssen p. 41, marked "closed access; blocked"). This task located an
author-posted complete text (academia.edu; printed version: ch. 12 of Dieks
(ed.), *The Ontology of Spacetime II*, Elsevier 2008, pp. 229–244, DOI
10.1016/S1871-1774(08)00012-0) and read Section I through the references.

Exact content (web-text wording, journal pagination not visible):

* Stein's requirements as rendered there: (i) reflexive; (ii) transitive;
  (iii) non-universal; (iv) "If b lies in the causal past of a … then Rab";
  (v) definable in terms of Minkowski geometry. Stein's uniqueness: only J⁻.
* The B-type candidate is already discussed: "the relation R_ab, defined as
  'b lies outside the future light cone of a or … b = a,' is relativistically
  invariant, but it does not satisfy condition (ii) — it is not transitive",
  and per Stein "if we took the transitive closure of R … it would become the
  universal relation". That is the census's saturation mechanism, printed in
  1991/2008 terms, used **with** transitivity.
* Cumulativity: "for every worldline [λ] and any points a, b and c such that
  b, c ∈ [λ], if Rab and Rbc, then Rac" (worldline glyphs lost in OCR).
* His result: "there are two pairs of relations R1, S1 and R2, S2 that satisfy
  Stein's weakened requirements": **R1ab iff b is located outside the future
  light cone of a, or a = b** (= our B), S1ab iff b is inside the future light
  cone of a excluding a; **R2ab iff b is located inside the past light cone of
  a** (= our J), S2ab iff b is outside the past light cone of a. "S1 is
  transitive, while R1 is not, and R2 is transitive, but S2 is not."
* Footnote 3 registers the Clifton–Hogarth chronological weakening: with
  chronological instead of causal inclusion one obtains "a slightly different
  notion of becoming which is reducible to past chronological connectibility"
  — i.e. our I is printed there as a known variant.
* He quotes CH 1995, p. 356 ("transitivity [secures] at least a minimum
  intersubjective agreement …") and Stein 1991, p. 151 (against transitivity
  of the indefiniteness relation), and answers CH's agreement worry: for an
  absolute (Stein-style) relation no separate agreement premise is needed.

**Premise-level relation to the censuses.** Bigaj's premise profile is:
reflexivity (S), **causal (null-inclusive) inclusion clauses on both the
definite and the open relation**, definability (= the covariance-style
invariance), non-universality, an **exhaustiveness stipulation** (Rab or Sab
for every pair), and cumulativity instead of full transitivity; no F_t/F_c
clause; setting is Stein's R⁴.

* The census's I fails his causal-inclusion clause (iv) at null steps; the
  census's C fails the corresponding open-relation clause (its complement,
  strict I⁺, is not causally past-closed: null steps fail). Hence
  **Bigaj's two pairs = census candidates ∩ Bigaj premises = {J, B}** in n≥2:
  given the four-case census plus the two one-line clause checks, Bigaj's
  completeness is an immediate corollary.
* Conversely the census is **not** a corollary of Bigaj: dropping causal
  inclusion for chronological P_t, dropping exhaustiveness, and adding F_t
  re-admits I and C. The two results interlock across the
  chronological/causal axis; neither subsumes the other.
* The 1+1 census strictly **corrects the scope of his dichotomy**: without
  spatial reflection the elsewhere is not one bloc (two wedges + four null
  branches), and e.g. the closed null half-space E_b = b + {u_R ≤ 0} satisfies
  every one of Bigaj's weakened requirements (causal past-closed, reflexive,
  exhaustive with invariant complement, definable, non-universal, cumulative)
  while being neither R1 nor R2. This is not an error in his chapter (his
  setting is R⁴, where n≥2 orbit transitivity holds), but a dimension-generic
  reading of his "exactly two" is false, and the sixteen-case census is the
  controlled repair.

### 2.2 Clifton–Hogarth 1995 (inherited full-text audit; primary not reread)

Theorem 1, pp. 365–367: definability + transitivity + reflexive chronological
inclusion ⇒ exactly {I⁻, J⁻, U}. Their proof's saturation step (an extra
spacelike or future pair forces U) is the printed ancestor of the census's
saturation lemma. Relation: the census's **transitivity row {I, J} is an
immediate corollary** of Theorem 1 plus the one-line observation that U fails
F_t. The census itself (no transitivity) is not a corollary of Theorem 1 —
transitivity is doing real exclusion work in their proof.

### 2.3 Stein 1991 (inherited audit; primary not reread)

J⁻ unique under reflexivity + transitivity + causal-past inclusion +
non-universality + definability (pp. 148–150). Relation: the census's
**boundedness∧P_c row (J only)** is the elementary symmetry-free collapse
(PERSISTENCE_CONVENTIONS §1), and Stein's theorem is its with-invariance
strengthening; both are known.

### 2.4 Thyssen works (brief-mandated)

* **Thyssen 2019** — upgraded to a primary fetch of the open-access article
  this session. §7.1: "The present for b … is just the absolute elsewhere of
  b — a spatially extended bowtie-shaped region", invariant, partitioning M
  into "absolute present (b + elsewhere of b), absolute future (upper
  lightcone of b) and absolute past (lower lightcone of b)". §7.2 bowtie
  presentism; §8.1 the transitivity objection applies to the bowtie present;
  §8.2 Peterson–Silberstein's uniqueness criterion; §9: SR underdetermines
  the dimensionality debate. **No census or classification appears in the
  fetched text.** His elsewhere-only present is a different region from B and
  C (past-plus-elsewhere) — confirmed textually, not just by inheritance.
* **Thyssen 2025 (four degrees)** — abstract + Stein-condition passage: a
  conceptual taxonomy; renders Stein's five conditions consistently with
  Bigaj's; no census.
* **Thyssen RPM chapter** — contents + abstract: §4.5 transitivity objection,
  §4.6 becoming objection; survey only.

### 2.5 Equivalent-classification search (narrow, per brief)

* Forward citation chase of CH 1995 via Semantic Scholar: 55 citing works
  scanned at title level (OpenAlex reports 115; that set was **not** chased —
  incomplete, see limits). Leads pulled to abstract: Müller 2019 (equivalence
  relation co-presentness — different relation type), Placek 2019 (BST
  settled-presents including spacelike events — different framework),
  Leininger 2020 (B-coming — conceptual), Jhou 2017 (exclusive disjunctivism —
  point-present variants), Aames 2022, Kügler 2020. None states a census.
* Targeted queries (exa, scholar_search) on: dropping transitivity for
  becoming; classification of invariant causal/chronological past-set
  reality relations; "complement of the future light cone" becoming; wide
  present / past-plus-elsewhere proposals. **No equivalent classification
  found.** New leads recorded: Godfrey-Smith 1979 (*Philosophical Studies*
  36, 233–244, DOI 10.1007/bf00372628 — metadata verified via Crossref;
  content paywalled, so his exact cone and premises remain unverified) as the
  printed conical-present proposal; Papadopoulos–Kurt–Papadopoulos,
  arXiv:1811.06097 ("a list of all possible causal relations in 2-dimensional
  Minkowski space is exhausted" — relations between pairs, not
  existence-assignment families; abstract only).

## 3. Falsifier-oriented nearest-predecessor table

Falsifier column: what finding would defeat the residual interest of the
census claim relative to that predecessor.

| # | Predecessor (depth) | Exact assumptions | Exact conclusion | vs n≥2 four-case census | vs 1+1 sixteen-case census | Falsifier |
|---|---|---|---|---|---|---|
| 1 | Bigaj 2008 (full-text, author web copy) | S; causal (null-incl.) inclusion both relations; definability; non-universality; exhaustiveness; cumulativity (worldline transitivity), no full transitivity; R⁴ | exactly two becoming relations: R1 = B (with diagonal), R2 = J | **shares {J, B}**; census re-admits I, C by chronological-not-causal inclusion and no exhaustiveness; not equivalent, interlocking | his single-elsewhere dichotomy fails without parity; null half-spaces satisfy all his clauses ⇒ 16-case census repairs scope | a printed statement that his premises also admit I or C, or a printed 1+1-no-parity refinement of his dichotomy |
| 2 | CH 1995, Thm 1 (full-text, inherited audit) | definability; transitivity; reflexive chronological inclusion | {I⁻, J⁻, U} | census+transitivity ⇒ its row is this theorem ∩ F_t (immediate corollary); census-without-transitivity not implied | no dimension analysis; n≥2 orbit facts used inside their proof | a printed no-transitivity classification by the same authors or in direct descendants |
| 3 | Stein 1991 (full-text, inherited audit) | reflexivity; transitivity; causal-past inclusion; non-universality; definability | R = J⁻ | covers the J row only; collapse lemma is the symmetry-free analogue | same | a printed symmetry-free collapse or census pre-1995 |
| 4 | Thyssen 2019 (full-text fetch, selected sections) | SR + Reichenbach ε; RP/WP arguments | elsewhere-only bowtie present; underdetermination | different region (elsewhere-only ≠ B, C); no census | same | bowtie-vs-B/C distinction or a census appearing in unread Thyssen material |
| 5 | Godfrey-Smith 1979 (discovery: Crossref metadata + secondary abstract only) | unknown (paywalled) | conical present proposal | candidate-level precedent for a cone-type present; no classification known | same | primary read showing a classification or an F_t/F_c-style premise analysis |
| 6 | Thyssen 2025 four degrees (abstract) | conceptual | taxonomy of becoming kinds | no census | no census | a classification theorem hidden in the unread body |
| 7 | Papadopoulos et al. 2018, arXiv:1811.06097 (abstract) | 2D Minkowski causal structure | exhaustion of causal relations + 30 topologies | different object (pair relations, not assignment families) | nearest math-side exhaustion in exactly 1+1 | body-level check revealing a classification of invariant past sets |
| 8 | Müller 2019 / Placek 2019 / Leininger 2020 / Jhou 2017 (abstracts) | various | equivalence-relation presentness; BST presents; B-coming; disjunctivism | different relation types or conceptual | same | any of them containing an invariant-assignment census in the unread body |

## 4. Immediate-corollary test (order theory)

Question from the brief: does elementary standard order theory make the
census an immediate known corollary? Answer, decomposed:

* **Given the analytic reduction** (Poincaré covariance + S ⇒ E_b = b + P;
  P_t ⇒ P a past set; orbit all-or-nothing; saturation chains), everything
  else **is** elementary combinatorics. `check_order_skeleton.py` encodes only
  those reduction outputs as input axioms and reproduces by exact
  enumeration: the four-case census and all ten added-premise rows
  (PERSISTENCE_CONVENTIONS §4), the sixteen-case census, and every refinement
  count in ONE_PLUS_ONE_CENSUS §4 (P_c 9, F_c 9, P_c∧F_c 4, closed 4,
  closed∧F_c 1, transitive 12, trans∧closed 3, trans∧P_c 5, trans∧F_c 8,
  trans∧P_c∧F_c 3; reflection-invariant 4; mirror classes 10). Runtime 0.05 s
  (hard alarm 15 s). The chain structure used: n≥2 E-space S ⇒ N⁻,
  N⁺ ⇒ S, plus causal variants; 1+1 per-side monotone triples n⁺ ≤ w ≤ n⁻.
* **The reduction itself is not order theory**: it uses the Lorentz orbit
  structure (single-orbit transitivity of null nappes and spacelike shells,
  n≥2) and the saturation lemma. The saturation mechanism is printed — CH's
  Theorem 1 proof (pp. 365–367) and Stein's universal-transitive-closure
  remark (as quoted in Bigaj 2008) — but always **chained with transitivity**
  to force U or J⁻. No printed source found chains it into a
  no-transitivity classification.
* Specific rows that **are** immediate corollaries of known results:
  transitivity row {I, J} ⊆ CH Theorem 1 + one-line F_t exclusion of U;
  boundedness∧P_c ⇒ J = the elementary collapse lemma (§1; pure order
  theory); closedness facts cl(I)=J, cl(B)=C are standard cone topology.
* Hence: the census **as a whole is not** an immediate corollary of any found
  statement, but it is **not order-theoretically deep** either — its
  non-elementary content is exactly the orbit/saturation reduction, whose
  ingredients are printed in adjacent premise settings. Failure to find
  wording is not evidence of novelty.

## 5. Required distinctions, verified at source level

* **Elsewhere-only present vs past-plus-elsewhere B**: Thyssen 2019 §7.1
  bowtie present = absolute elsewhere (quote above) ≠ B, C (which contain the
  causal past). Textually confirmed this session at primary depth.
* **Chronological vs causal persistence**: CH's chronological inclusion (⇒ I⁻
  survives, Theorem 1) vs Stein's/Bigaj's causal (null-inclusive) inclusion
  (⇒ J⁻ only). This is precisely the axis along which the census re-admits I
  and C; conflating the two would make the census look like a Bigaj/CH
  corollary, which it is not.
* **Symmetry invariance vs quotienting**: all printed predecessors use
  definability/equivariance (invariance of the relation under automorphisms);
  none quotients by mirror. The census's distinction — reflection invariance
  (4 assignments) vs mirror identification (10 classes) — is a standard
  group-action distinction with no printed counterpart found.
* **Transitivity vs cumulativity**: Bigaj's cumulativity is transitivity
  restricted to worldline steps (equivalent, given causal inclusion, to
  family monotonicity along worldlines = P_c restricted to observers); the
  census's P_t is global chronological monotonicity with no transitivity of
  the existence-at relation. Related but distinct premises; Bigaj's own text
  marks the difference ("cumulativity can be preserved without demanding the
  relation of becoming to be transitive").

## 6. Strongest contrary evidence (against any residual novelty)

1. **Bigaj 2008**: prints a two-case invariant classification {J, B} under
   weakened (cumulativity) requirements, explicitly discusses the B-type
   relation's invariance and non-transitivity, and prints the I-candidate as
   a known chronological weakening (via CH). The census shares two of its
   four candidates and its entire saturation mechanics with this chapter.
   Before this task the project had Bigaj only at discovery depth — direct
   evidence that unsearched corners can move the disposition.
2. **CH 1995 Theorem 1**: subsumes the census's transitivity row outright.
3. **The 1+1 fifth/sixth families and null half-spaces are Rindler-adjacent
   standard objects**; only their assembly into a census looks unprinted.
4. Incomplete coverage: the OpenAlex citing set (115) was not fully chased;
   paywalled primaries (Godfrey-Smith 1979 content, Stein 1968, Bigaj's
   printed pagination) were not read; non-English literature was only
   abstract-sampled (one Polish source).

## 7. Conservative verdicts (per claim; no novelty score)

* **n≥2 four-case census**: **unresolved.** No printed equivalent found at
  accessible depth; nearest predecessors (Bigaj 2008 {J, B}; CH 1995 {I⁻, J⁻,
  U}; Stein 1991 {J}) sit at genuine premise distance (chronological vs
  causal inclusion, exhaustiveness, F_t, transitivity); its saturation core
  is printed in adjacent settings; several refinement rows are immediate
  corollaries of known theorems (§4). Not "known", not "immediate corollary"
  as a whole — and not "new" either: this audit does not and cannot clear the
  unsearched remainder.
* **1+1 sixteen-case census and refinements**: **unresolved**, with weaker
  coverage than the n≥2 side. No predecessor found; the closest printed
  relative (Bigaj's dichotomy) breaks without parity in a controlled way, and
  the census repairs its scope — but nothing was found *stating* the 16-case
  classification, and the search was narrower than the n≥2 one.
* **Refinement rows**: transitivity rows and the boundedness∧P_c row are
  **immediate corollaries** of CH Theorem 1 and the collapse lemma
  respectively; closedness facts are standard; the 1+1-only counts (9/9/4/4/1,
  12/3/5/8/3, reflection 4 vs quotient 10) have **no found printed
  counterpart**.
* Per the brief: **no ontology is selected, no novelty verdict is issued**,
  and "not found" is nowhere treated as evidence of newness. These
  dispositions are submissions for coordinator review.

## 8. Falsifiers for this audit itself

1. A printed statement of either census (pre-2026), or of the {J, B} pair
   with F_t-style premises, in: the unread OpenAlex citing set; Godfrey-Smith
   1979's body; French/German/Polish-language sources; physics-side causal
   -structure literature; PST/BST technical reports.
2. An error in my Bigaj extraction — in particular if his "future light cone"
   phrase means only the timelike interior (making his R1 = our C, not B),
   or if a printed-page passage adds premises my reconstruction misses.
   Verify against the printed chapter (pp. 229–244).
3. A printed derivation of the census from CH/Stein/Bigaj (making it an
   immediate corollary after all).
4. A proof that the skeleton check's input chains are wrong (they were taken
   from the reviewed analytic reduction, not re-proved here).

## 9. What was and was not done

Done: primary fetch and full-text read of Bigaj 2008 Section I (author web
copy); primary fetch of Thyssen 2019 (open access) with §7–§8 read;
CH 1995 and Stein 1991 handled through the inherited full-text audits with
their limits recorded; narrow equivalent-classification searches; 55-title
citation chase; skeleton check executed and passing; source records with
honest depths in `sources.jsonl` (16 records).

Not done: rereading the CH primary scan; accessing Bigaj's printed pagination
or the Godfrey-Smith 1979 body; chasing the OpenAlex 115-citing set;
body-level checks of Aames 2022, Papadopoulos et al. 2018, Kügler 2020,
Müller 2019; any Lean formalization; any curved-spacetime or quantum
generalization; any search of pre-1990 non-English literature.
