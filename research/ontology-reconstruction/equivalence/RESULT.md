# Ontological expansion versus redescription: a comparison contract, two examples, and a test

Lane: `ontology-expansion-equivalence` (one of four independent 29 October lanes).
Date: 29 October 2026. Sole worker. **Status: submission for independent review, not
an accepted result.** Tags used throughout:

- **[PROVED (source)]** — established result, locator and my read depth given.
- **[PROVED here]** — short derivation given in this document, on stated premises.
- **[CONDITIONAL]** — follows from proved items plus a stated premise.
- **[OURS: PROPOSAL]** — our construction or contract, not a theorem about the world.
- **[OPEN]** — not established.

Everything here is relative to a stated base structure; no claim is made that any
ontology *is* a spacetime subset, that every expansion is observable, or that a
broad universal equivalence (or non-equivalence) theorem holds.

## 0. Answer in brief

The brief asked for six distinctions, two explicit examples, and a usable test.

1. **Comparison contract (CC, §2).** A rival ontology is compared to a base
   physical structure as a *model-theoretic expansion*: new vocabulary (existence
   `E(b,x)`, grounding, truth policy) interpreted over a stated base signature and
   theory, subject to covariance, persistence and admissibility clauses. Expansion
   is *adding predicates*, not carving subsets; domain-changing ontologies are
   handled by stagewise bases. [OURS: PROPOSAL]

2. **Six notions separated (§3, §6).** Automorphism invariance, definability,
   existence/uniqueness of expansion, equivalence of categories, empirical
   equivalence, metaphysical equivalence. The load-bearing logical map (definable
   ⟹ invariant; invariant ↛ definable; unique expansion ⟺ global explicit
   definability via Beth; invariance ⟺ only *local* definability; Morita
   equivalence ⟺ common definitional extension) is all **[PROVED (source)]** —
   it is Barrett 2018's organization of Winnie, Beth and Svenonius, plus Tsementzis 2017 —
   not ours. Our additions are the two in-domain examples and the test.

3. **Example 1 — the cone binary (§4).** On Minkowski spacetime of dimension ≥ 3,
   with base language `{≪}` (chronological order), any expansion `E(b,x)` =
   "the concrete realm from standpoint b" satisfying chronological inclusion,
   causal boundedness, self-realization, persistence, and full causal-automorphism
   covariance is **exactly one of two**: `I⁻(b) ∪ {b}` or `J⁻(b)`. Both are
   automorphism-invariant *and* explicitly definable; the choice between them is
   underdetermined by the base. Invariance is a constraint on the expansion
   family, not a selection principle. [PROVED here, on Zeeman 1964 + a standard
   orbit argument; conditions are OUR stipulations]

4. **Example 2 — the labelled causet (§5).** A rigid 3-element poset has exactly
   three order-respecting labellings (growth orders). Forgetting the labelling
   makes the stipulated growth-grounding claim "c became real before b" not
   merely false but **inexpressible** in the tenseless base (its truth varies
   across expansions of one shared base; certificate script included). Forgetting
   structure demonstrably loses a stipulated grounding claim — *relative to the
   growth-realist stipulation*. [PROVED here: finite, checked by enumeration]

5. **The Expansion Divergence Test (§8).** A five-step checklist (invariance
   audit, expansion census, definability, metaphysical audit, empirical audit)
   usable by the rival-contract and classification lanes, with its limitations.

## 1. Method

Read first: AGENTS.md, README.md, knowledge/README.md, knowledge/NOVELTY.md,
`research/ontology-reconstruction/ROADMAP.md`, `research/CURRENT_SYNTHESIS.md`,
`research/CLAIM_STATUS.md`, `research/lawful-completions/coordinator/BATCH2_INITIAL_REVIEW.md`
(rejection points respected: no reliance on the claimed continuity closure or on
the rejected scalar geometric objection), `research/ontology-reconstruction/coordinator/EXPLANATORY_ROLE_TEST.md`,
`research/local-fragmentalism/STRONGEST_VIEW.md` and `redteam/SYNTHESIS.md`,
`research/philosophy-completion/ESSAY.md`, `research/discriminators-audit/RESULT.md`.

Search capability check (start of session): `scholar_search` (openalex backend)
and `exa` (`web_search_exa`, `web_fetch_exa`) both **worked**. `serpapi_search`
was available but not needed after exa/scholar succeeded; `web-search-prime` was
**not retried** (quota exhausted until 2026-11-17, per brief). Details in
AGENT_REPORT.md.

Prior art was audited before technical proposals (primary pages fetched and
inspected; read depths recorded in `sources.jsonl`). Two corrections to common
citations found this way: Field's paper is **1973** (J. Phil. 70(14):462–481),
not 1974; and Svenonius' theorem is *not* "invariance under automorphisms ⟺
definability" — it quantifies over permutations of **elementary extensions**
(Semenov–Soprunov 2015, abstract; Barrett 2018 Thms 2–3).

## 2. The comparison contract (CC)

**[OURS: PROPOSAL]** Let a *physical model* be a structure `P` in a signature `Σ`
with a `Σ`-theory `T_P`. Nothing in the contract assumes `Σ` is a spacetime
signature: `P` may be a spacetime `(M, g, ≪)`, a causal set, a family of
stage-models, an algebra of observer records, or a category of such structures.
An **ontological expansion** of `P` is an interpretation on `P`'s domain(s) of
new vocabulary `Δ`, typically:

- a concrete-inventory clause: a relation `E(b, x)` ("x is concrete from
  standpoint b") or a domain-valued function — *not* a claim that the ontology is
  a subset of spacetime points;
- a standpoint/index status clause (which indices are standpoints, if any);
- an existence-at versus absolute-existence clause;
- a truth policy (e.g. outcome-matching, bivalence, supervaluation);
- grounding/dependence relations **if the rival stipulates them** (no rival is
  forced to have them);
- actualization/passage claims, if any.

Clauses of the CC:

1. **Covariance/equivariance.** Expansions are compared under a stated
   comparison group `G` (default: `Σ`-automorphisms). Equivariance is a
   well-formedness condition, never evidence of reality (§4).
2. **Persistence.** Along whatever order the base supplies (causal order, growth
   order, clock order).
3. **Admissibility.** Which auxiliary assumptions may be changed when comparing
   rivals (mirrors the manuscript's conditions (i)–(iv), discriminators-audit §1).
4. **Empirical channel.** Which quantities are observable, with a declared
   protocol class (so that "inert" vs "active" added structure is decidable per
   discriminators-audit Lemma 1/2).
5. **Residue reporting.** Every comparison must list which claims of each rival
   are (a) expressible and fixed in the base, (b) expressible and varying across
   admissible expansions, (c) inexpressible in the base. Category (b)+(c) is the
   rival's *added content relative to that base*.

The unit of comparison is a particular base + expansion + interpretation, as the
knowledge-base contract requires. Rivals that reject the shared base (e.g.
causet-first views with no spacetime arena) are compared by choosing a stagewise
base; if no shared base can be stated, the CC records incommensurability instead
of forcing a translation (as NOVELTY.md candidate D requires).

This is a *comparison instrument*. Per ROADMAP it must not force every rival into
a point-subset ontology, and per BATCH2_INITIAL_REVIEW the lane's claims are
logically independent of the two rejected technical submissions; nothing here
uses them.

## 3. The six notions and the verified logical map

Notation follows Barrett 2018 (read: philpapers PDF, §1–§5 through the SYM*
discussion, incl. statements and proofs of Props 1–3 and Thms 1–3):
`E_A` explicit definability in a structure; `S_A` invariance under the
automorphisms of the base reduct; at theory level `E1` (global explicit:
one formula works in every model), `E2` (local explicit: per-model formulas),
`I1` (implicit: same reduct ⟹ same `r`), `S1`/`S2`/`S3` (invariance under
automorphisms / elementary embeddings / isomorphisms of models).

| # | Notion | Informal content | Formal face | Status |
|---|---|---|---|---|
| N1 | Automorphism invariance (covariance) | structure preserved by base symmetries | `S_A`; theory-level `S1` | defined [PROVED (source) for the formal properties] |
| N2 | Definability from the base | the added structure is an abbreviation of base structure | `E_A`; `E1` global, `E2` local; `I1` implicit | [PROVED (source)] |
| N3 | Existence / uniqueness of expansion | does an expansion satisfying the rival's axioms exist? how many, up to expansion-isomorphism? | census of models of `T_P + A` over a shared reduct | notion is standard; censuses below are [PROVED here] |
| N4 | Equivalence of categories / Morita | same model category up to equivalence; syntactically, common definitional extension | Weatherall's criterion; Barrett–Halvorson via Tsementzis | [PROVED (source), abstract-level for Tsementzis] |
| N5 | Empirical equivalence | same likelihoods over a declared protocol class | project Lemma 1/2 (discriminators-audit §6) | [PROVED (project), bookkeeping on stated definitions] |
| N6 | Metaphysical equivalence | same existence/grounding/truth-policy commitments under a clause-preserving translation | no agreed criterion; candidate in §8 | [OPEN]; deflationary challenge acknowledged (STRONGEST_VIEW O2) |

Verified implications and separations (all locators in `sources.jsonl`):

- **N2 ⟹ N1** (definable structures are invariant). Barrett 2018 Prop 1/3.
  [PROVED (source), full-text]
- **N1 ↛ N2.** Rigid bases trivialize invariance: Barrett 2018 Example 5
  (countably many constants, only identity automorphism, `r` chosen non-definable);
  in spacetime kinematics, Mounoud 2014 Thm 1 (compact manifold, dim ≥ 2: metrics
  with trivial isometry group form an open dense set in the C^∞ topology —
  compactness is part of his theorem; the noncompact spacetime analogue is
  **[OPEN]** here). In-domain instance: Example 2 (§5). [PROVED (source) + in-domain
  certificate]
- **N1 ⟺ E2 only.** Barrett 2018 Thm 1: local explicit definability is exactly
  automorphism-invariance. So covariance tracks *per-model* definability, not
  uniform definability. [PROVED (source)]
- **E1 ⟺ I1** (Beth; via Hodges 2008 Thm 6.6.4 as cited in Barrett). Unique
  expansion (implicitly defined structure) ⟺ global explicit definability.
  Hence **failure of uniqueness ⟹ failure of explicit definability** (of the
  expansion relation *as fixed by the theory*). [PROVED (source, inherited locator)]
- **E1 ⟺ S2 ⟺ S3** (Barrett Thms 2–3); Svenonius' theorem: for **complete** `T`,
  `E1 ⟺ S1` (Hodges 2008 Cor 10.5.2 via Barrett); Svenonius' original statement
  uses permutations of elementary extensions (Semenov–Soprunov 2015, abstract).
  [PROVED (source); original Svenonius paper not read — locator unverified]
- **N3 is independent of N2.** Existence can fail: the project's own completion
  theorem (prescribed scalar doubly-principal extension exists iff `p ∈ [0,1]`;
  CLAIM_STATUS row 1) is literally a non-existence-of-expansion result for one
  model class. Uniqueness can fail while every candidate is definable: Example 1.
  [PROJECT reviewed result + PROVED here]
- **N4 ⟹ N2-flavored content, but N4 ↛ N6.** Morita equivalence of theories is
  syntactically common definitional extension (Tsementzis 2017, abstract;
  Barrett–Halvorson's notion); but a category equivalence or duality carries
  *interpretative constraints* as extra data (De Haro 2019, abstract; Read–
  Møller-Nielsen 2018, abstract) and does not by itself fix which existence or
  grounding clauses are preserved. Weatherall 2016 (abstract) argues Glymour's
  definability criterion (N2-based, Noûs 11(3):227–251, 1977) misses an important
  equivalence sense and proposes the category-theoretic one. [PROVED (source,
  abstract-level); the ↛ N6 step is OUR argument, §6]
- **N5 ↛ N6.** Project Lemma 1 (inert bridges give identical likelihoods) plus
  Example 1: two expansions agreeing on all timelike records yet disagreeing on
  null-boundary existence. [PROJECT + PROVED here]
- **N6 ⟹ N5** only given inert bridges; a bridge that changes the probability
  law would be a physical hypothesis (discriminators-audit §6 scope note).
  [CONDITIONAL]

One-line version: **covariance constrains; uniqueness (only) yields definability;
definability yields redescription; category/Morita equivalence yields shared
explicit content; none of these yields metaphysical equivalence without an extra,
philosophical premise about preserving existence/grounding clauses.** No broad
universal equivalence theorem is claimed, in either direction.

## 4. Example 1 — the cone binary (invariant but underdetermined)

**Domain assumptions (exact).** Base `P = (ℝⁿ⁺¹, ≪)`, Minkowski spacetime with
**spacetime dimension ≥ 3** (space dimension ≥ 2) and time-oriented causal order
`≪`; no metric, frame, or observer as base structure. Comparison group `G` = all
`≪`-preserving bijections (causal automorphisms). **[PROVED (source)]** Zeeman
1964 (first page and theorem statement read): the causality group is generated by
orthochronous Lorentz transformations, translations, and dilations; his Remark 2
notes the result "depends essentially upon space being more than 1-dimensional" —
hence the dimension restriction; in 1+1 the census below fails (many more
equivariant expansions exist).

An **expansion** is a relation `E ⊆ P × P`, written `E_b = {x : E(b,x)}`, with:

1. **chronological inclusion:** `x ≪ b ⟹ x ∈ E_b`;
2. **causal boundedness (non-universality):** `E_b ⊆ J⁻(b)`;
3. **self-realization:** `b ∈ E_b`;
4. **persistence:** `b ⪯ b′ ⟹ E_b ⊆ E_{b′}` (where `⪯` is `≪` plus identity);
5. **covariance:** `σ(E_b) = E_{σ(b)}` for every causal automorphism `σ`.

(1)–(4) are OUR stipulations, modeled on the project's fragmentalist premises
(chronological inclusion ≈ P2 of STRONGEST_VIEW; boundedness ≈ the Stein
non-universality premise; persistence ≈ P5). A presentist, for whom `E_b = {b}`,
violates (1) and is deliberately **outside** this contract — the example covers
the fragmentalist/growing-past family only. **[OURS: PROPOSAL]**

**Proposition.** On `P` as above there are **exactly two** expansions satisfying
(1)–(5): `E = I⁻(b) ∪ {b}` and `E = J⁻(b)`. **[PROVED here]**

*Proof sketch.* By (5) with translations, `E_b = E_0 + b`; so `E` is fixed by
`E_0`. By (1)–(3), `I⁻(0) ∪ {0} ⊆ E_0 ⊆ J⁻(0) = I⁻(0) ∪ ∂J⁻(0)`. The stabilizer
of `0` in `G` is (orthochronous Lorentz) × (dilations) by Zeeman's theorem. The
orthochronous Lorentz group acts transitively on past-directed null directions
and dilations act transitively on positive radii, so `∂J⁻(0) \ {0}` is a **single
orbit**. Hence `E_0` either contains all of `∂J⁻(0) \ {0}` or none of it, giving
`E_0 ∈ {I⁻(0) ∪ {0}, J⁻(0)}`. Both satisfy (1)–(5): the sets `I⁻(b)`, `J⁻(b)`,
and the diagonal are equivariant, nested under `⪯`, and satisfy (1)–(3). ∎

(Standard-input status: Lorentz-transitivity on the null cone is textbook
kinematics, applied here; Zeeman is the only substantive external premise. The
full write-up relies on his classification of the causality group; I read his
theorem statement and Remarks 1–5, not the body proof.)

**What the example shows.**

- **Invariance does not determine.** Both expansions are fully covariant, yet
  they disagree: for `x ∈ ∂J⁻(b) \ {b}`, `E(b,x)` is true on one and false on the
  other — a first-order-expressible disagreement about *which events are
  concrete from b*. Covariance is a constraint on the expansion family, not a
  selection principle. This is the brief's "invariant but underdetermined"
  example, with exact domain assumptions. [PROVED here]
- **Definability of each completion does not collapse the disagreement.** `I⁻`
  and `J⁻` are each explicitly definable from `≪` (`J⁻(b)` = `x ≪ b ∨ x = b`).
  The *contract* `(1)–(4)` fails `I1`: two expansions share the identical reduct
  `(ℝ, ≪)` but differ on `E`. By Beth, no formula of `≪` globally defines "the"
  realm. The two expansions are not elementarily equivalent (∃ a boundary-real
  event holds in one, not the other), so the contract theory is incomplete —
  exactly the pocket where Svenonius' completeness hypothesis fails and `S1`
  does not lift to `E1` (Barrett §4). Underdetermination at theory level and
  definability of each instance coexist. [PROVED here, on the sourced map]
- **Empirical agreement.** The two expansions agree on every timelike record:
  a boundary event differs from an interior one only in whether it *already*
  was concrete from `b` when its light signal arrives at `b`; at finite timing
  precision the arrival statistics are identical. This is an informal argument,
  not a theorem: it assumes records are timelike and finite-precision. So the
  pair is empirically equivalent (N5) while ontologically distinct (¬N6).
  [OURS: PROPOSAL, informal]
- **The binary matches known freedom.** Clifton–Hogarth recorded the competing
  null-line intuition and suggested giving it up (pp. 364–365; project R-F,
  not re-read this run); STRONGEST_VIEW R4 says "the light cone is the only
  freedom" and that P6/P6′ select `J⁻`. The new content here: **under full
  causal covariance in the flat category, the freedom is exactly a binary** —
  R4's freedom is not a continuum — and *no input from the causal base chooses
  between the two*, so P6 (signalling) or P6′ (closure) are doing genuine
  philosophical work, not physics work. [CONDITIONAL on the premises]
- **Curved spacetimes are worse, not better.** The Stein classification
  (I⁻(b) ⊆ F(b) ⊆ J⁻(b), off-shell, inherited) permits curvature-dependent
  intermediate rules; flat Minkowski is the *rigid* special case where only the
  binary survives. Underdetermination grows with symmetry loss, contrary to the
  folk thought that symmetry restores uniqueness. [CONDITIONAL, inherited]

**Reading guard.** This example does **not** say `I⁻` vs `J⁻` is mere
redescription (it is a real disagreement), and does **not** say every invariant
structure is undefinable (both are definable). It refutes: "covariance +
definability of the candidates + empirical equivalence ⟹ no ontological
difference."

## 5. Example 2 — the labelled causet (forgetting loses a stipulated grounding claim)

**Domain assumptions (exact).** Base `P`: the finite poset `a < b`, `c`
incomparable — a three-element "unlabelled causet" with tenseless order only.
Expansion: a growth labelling `ℓ: P → {0,1,2}` respecting the order (a linear
extension), read as "x comes to exist at stage ℓ(x)". Stipulated grounding claim
(growth realism, Sorkin-style): stage order is objective, so e.g. "c became real
before b" (`ℓ(c) < ℓ(b)`) is an objective fact. [OURS: PROPOSAL for the
stipulation; the poset facts below are PROVED here]

**Certificate** (`check_poset_expansion.py` in this directory, standard library;
output reproduced in AGENT_REPORT.md):

1. `Aut(P)` is **trivial** (the base is rigid).
2. There are **exactly three** order-respecting labellings:
   `(a,b,c) ↦ (0,1,2)`, `(0,2,1)`, `(1,2,0)` (stages as listed per element).
3. The three expansions are **pairwise non-isomorphic** as expansions (no base
   automorphism conjugates one to another — trivially, since `Aut(P)` is trivial).
4. The claim `ℓ(c) < ℓ(b)` is **false on the first expansion and true on the
   other two**: its truth varies across expansions of one and the same base.

**What the example shows.**

- **Forgetting demonstrably loses a stipulated claim.** The base language is
  interpreted on one fixed structure; every base sentence has a fixed truth
  value on it. A claim whose truth varies across expansions of that same base
  (item 4) cannot be the interpretation of any base sentence. So the tenseless
  completion cannot state the growth-grounding claim; the loss is of
  *expressibility*, not of truth-value on the base. [PROVED here: 3-element
  exhaustive check]
- **Invariance is vacuous here — by design.** Because `Aut(P)` is trivial,
  *every* relation on `P` is automorphism-invariant (Barrett 2018 Example 5 is
  the general form of this point). So invariance cannot certify that the
  labelling is recoverable; the census (three expansions) is what does the
  work. Rigid bases are not a pathology: genericity results (Mounoud 2014,
  compact case) suggest trivial-symmetry base structures are the rule, not the
  exception. [PROVED here in-domain; genericity PROVED (source) with compactness
  caveat]
- **Beth direction.** Three non-isomorphic expansions with a shared reduct ⟹
  `I1` fails for the labelling ⟹ (Beth) no global explicit definition of the
  growth order from the tenseless order. [PROVED here, on the sourced map]
- **The lost structure is empirically inert in the standard model class.** In
  classical sequential growth, conditional on the unlabelled poset, generation
  orders are equiprobable, and birth-order data are ancillary (project record:
  `knowledge/defeat-search/csg_ancillarity_check.py`, n ≤ 5; Brightwell–Luczak
  via project records; discriminators-audit D11). So in that model class the
  forgotten structure changes no likelihoods: the loss is exactly metaphysical,
  not empirical. [PROJECT records, inherited; not recomputed here except for the
  toy poset]
- **Where the burden lands.** Wüthrich–Callender (arXiv:1502.00018v1, Secs 4–5;
  project R-F) treat labelled identity as indeterminate and keep a qualified
  gauge-invariant growth; Sorkin's reading treats stages as real. The example
  does not adjudicate: it shows *precisely what is lost* by the tenseless
  representation if the growth-realist stipulation is made, and that the
  stipulation is not forced by the base. That is the brief's second example:
  forgetting structure loses a *stipulated* existence/grounding claim.
  [CONDITIONAL on the stipulation]

**Reading guard.** This is a toy domain: three elements. It certifies the logic
of the loss, not any physics. It does not show that growth realism is correct,
nor that the labelling is not gauge. It shows: *relative to the stated base*,
the grounding claim is added content, and it is exactly the content lost on
forgetting.

## 6. Consequences: what each equivalence notion cannot deliver

- **Automorphism invariance (N1)** cannot certify reality or recoverability:
  rigid bases trivialize it (§5), and even full covariance leaves the §4 binary.
  Never infer definability merely from covariance (ROADMAP check 2); the precise
  version: covariance ⟺ only *local* definability (Barrett Thm 1).
- **Definability (N2)** establishes redescription *on the stated base*. It does
  not establish metaphysical equivalence: §4 shows two definable, incompatible
  expansions; conversely a definable translation of a rival's `E` would defeat
  that rival's *distinctiveness* claim on that base, which is exactly what the
  translation argument (STRONGEST_VIEW O2) does to local fragmentalism's
  truth-conditions — while leaving the grounding dispute untouched. [THESIS,
  consistent with STRONGEST_VIEW's own concession]
- **Existence/uniqueness (N3)** is where ontological underdetermination lives:
  census results — two expansions (§4), three expansions (§5), zero expansions
  (project percolation non-extension for `p ∉ [0,1]`) — are the comparison
  instrument. Note the reversal: *failure* of existence (0 expansions) is
  sometimes a genuine exclusion result (the completion dilemma, ESSAY §4), while
  *multiplicity* is underdetermination, and *uniqueness* hands you definability
  (Beth). [PROVED here as bookkeeping; the project's own theorem is reviewed
  internally, not externally]
- **Category/Morita equivalence (N4)** delivers shared explicit content
  (common definitional extension) but transports nothing about existence or
  grounding clauses unless the *reconstrual* — which functor, which interpretation
  map — is stipulated and audited clause-by-clause. A representation
  transformation is not automatically an ontological equivalence (AGENTS.md;
  De Haro's interpretative constraints; manuscript's representation-equivalence
  caution in discriminators-audit §1). [THESIS]
- **Empirical equivalence (N5)** is scoped to a declared protocol class and is
  the project's central negative result (discriminators-audit: no screened
  protocol is an ontology discriminator; exclusivity premises missing). §4 adds
  a case where the two rivals agree even on *all* finite-precision records while
  disagreeing in `Δ`. [PROJECT + PROVED here, informal]
- **Metaphysical equivalence (N6)** has no accepted formal criterion. A
  defensible *candidate*: a translation under which every existence, grounding,
  and truth-policy clause of each rival maps to a theorem (definable equivalent)
  of the other, with the dependency direction preserved. Field 1973 (discovery
  depth only; primary not read) motivates definitional equivalence for
  ontological commitment; whether fundamentality/grounding disputes are
  substantive enough for N6 to be non-trivial is exactly STRONGEST_VIEW O2 and
  stays **[OPEN]**. This lane does not assume N6 collapses into N4 or N2.

**No universal theorem.** Nothing above states that all ontologies are
equivalent, that none are, or that any broad equivalence relation among
ontologies holds. Every verdict above is relative to a stated base, stated
clauses, and a stated protocol class.

## 7. Prior-art audit (definability, theoretical equivalence, surplus structure)

Full records with URLs, versions, and read depths: `sources.jsonl`. Summary of
what was established from primaries before the proposals above:

| Source | Locator verified | What was read here | Use |
|---|---|---|---|
| Zeeman 1964 | J. Math. Phys. 5(4):490–493, DOI 10.1063/1.1704140 | abstract + first page incl. theorem and Remarks 1–5 | §4 group premise; dim ≥ 3 |
| Barrett 2018 | Phil. Science, DOI 10.1086/699156; philpapers PDF | substantial full text: §1–§5, Props 1–3, Thms 1–3, Exs 1–6, SYM* | the E/S/I map of §3 |
| Winnie 1986 | cited by Barrett (Prop 1.10, 1.11); full locator unverified here | not read | inherited support for model-approach results |
| Hodges 2008 | cited by Barrett (Thm 6.6.4 Beth; Cor 10.5.2 Svenonius) | not read | inherited locators |
| Svenonius 1959 | original locator unverified here | not read | historical priority only |
| Semenov–Soprunov 2015 | arXiv:1301.2412v2; Logic J. IGPL, DOI 10.1093/jigpal/jzv038 | abstract | correct content of Svenonius' theorem |
| Mounoud 2014 | arXiv:1403.0182 | arXiv HTML: abstract, Theorem 1, proof strategy | generic rigidity (compact manifolds) |
| Malament 1977 | Noûs 11(3):293–300 (project R-F) | not read here; Barrett's gloss read | spacetime definability precedent |
| Clifton–Hogarth 1995 | Synthese 103:355–387 (project R-F) | not read here | null-line freedom (pp. 364–365, inherited) |
| Glymour 1977 | Noûs 11(3):227–251 (verified via Weatherall's abstract/notes) | not read | N2-based criterion of equivalence |
| Weatherall 2016 | Erkenntnis 81:1073–1091, DOI 10.1007/s10670-015-9783-5 | abstract + notes | N4 criterion; NGG equivalent to NG |
| Tsementzis 2017 | J. Symb. Logic, DOI 10.1017/jsl.2017.59; arXiv:1507.02302 | abstract | Morita ⟺ common definitional extension |
| Hudetz 2018 | Phil. Science, DOI 10.1086/701047 | title/venue only | lead: definable categorical equivalence |
| De Haro 2019 | Synthese, DOI 10.1007/s11229-019-02394-4 | abstract + intro fragment | interpretative constraints for equivalence |
| Dewar 2019 | BJPS 70(2), DOI 10.1093/bjps/axx021 | abstract | sophistication vs reduction; symmetry-as-isomorphism |
| North 2009 | J. Phil. cvi(2), Feb 2009 (jillnorth.org PDF) | opening lines only | structure-counting tradition |
| Redhead 1975 | Synthese 32:77–112, DOI 10.1007/BF00485113 | metadata/TOC level | surplus structure concept |
| Ismael–van Fraassen 2003 | CUP chapter, DOI 10.1017/cbo9780511535369.024 | abstract | symmetry as guide to superfluous structure |
| Field 1973 | J. Phil. 70(14):462–481, DOI 10.2307/2025110 | JSTOR/philpapers listings only | definitional equivalence & commitment (handle with care) |
| Correia–Rosenkranz 2020 | NDJFL, DOI 10.1215/00294527-2020-0001 | abstract | temporaryism as logics without presentness — nearest formal neighbor of CC |
| Sider 2001 | Four-Dimensionalism, OUP, DOI 10.1093/019924443x.001.0001 | book abstract | parsimony-argument context; exact section unverified |
| Barrett–Manchak 2024 | Philosophy of Physics 2(1):11, DOI 10.31389/pop.131 | abstract + §1 | same coordinates, different structure — base-relativity |
| Project anchors | STRONGEST_VIEW.md; discriminators-audit/RESULT.md; CLAIM_STATUS.md; ESSAY.md; EXPLANATORY_ROLE_TEST.md | full text | internal premises and scoping |

Nearest predecessors of this lane's deliverable, and what is not new here:

- Model-theoretic treatment of symmetries/definability: **Barrett 2018** (with
  Winnie, Beth, Svenonius). All logical results in §3 are theirs or inherited.
- Formalizing temporaryist ontologies as logics: **Correia–Rosenkranz 2020**
  (sound+complete logics for presentism and expansionism without presentness);
  **Fine 2005** and **Lipman 2023** standpoint frames `⟨D, W, R, v⟩` with
  `v(w) ⊆ D` (project R-F) are literally existence-expansions of a frame.
- Growth-order indeterminacy in causal sets: **Wüthrich–Callender 2017**;
  ancillarity: project records.

What this lane adds (narrowly): (i) the CC with residue reporting; (ii) the two
in-domain examples with exact domain assumptions and one machine-checked
certificate; (iii) the observation that the fragmentalist cone freedom collapses
to an exactly binary, unselectable choice under full causal covariance in the
flat category; (iv) the EDT test of §8. No priority claim beyond that.

## 8. The Expansion Divergence Test (EDT)

**[OURS: PROPOSAL]** Input: a rival contract stated per §2 (signature `Σ`,
theory `T_P`, added vocabulary `Δ_i` with axioms `A_i`, comparison group `G`,
protocol class). Output: a verdict matrix + a residue list.

- **T0 (base declaration).** State `Σ`, `T_P`, `G` exactly. Lanes using
  different bases do not transfer conclusions (Barrett–Manchak 2024: same
  privileged coordinates, different structure).
- **T1 (invariance audit).** Check `A_i` for `G`-equivariance (S1-type).
  Record vacuity if `G` is trivial. Never upgrade equivariance to definability
  or reality (§4, §5; Barrett Exs 5–6).
- **T2 (expansion census).** On each shared base model, count expansions of
  `T_P + A_i` up to expansion-isomorphism. `=0`: the rival's expansion fails to
  exist on this class (existence gate; where percolation-style exclusions live).
  `=1`: candidate implicit definability → go to T3. `≥2`: **underdetermined
  residue** = enumerate the claims whose truth varies across expansions (the §5
  procedure); these are the rival's added commitments relative to this base.
- **T3 (definability).** If unique, seek `Σ`-formulas defining each `Δ_i`
  symbol (E1), invoking Beth/Svenonius with the completeness caveat (use the
  elementary-embedding/isomorphism form, Barrett Thms 2–3, for incomplete `T_P`).
  Definable `Δ_i` ⟹ the rival's addition is a redescription *on this base*.
- **T4 (metaphysical audit).** If mutual translations exist with `Δ`-symbols
  mapped to definable equivalents *and* grounding/truth-policy clauses preserved
  clause-by-clause: record **metaphysical-equivalence candidate** (never a
  verdict). Otherwise record the exact untranslated clause as the locus of a
  genuine commitment.
- **T5 (empirical audit).** Apply discriminators-audit Lemma 1/2: are any
  `Δ`-symbols probabilistically active in the declared protocol class? Inert
  bridges ⟹ no likelihood separation possible at these realizations.

**Limitations (stated with the test, per the brief).**

1. **Base relativity.** All verdicts are relative to `Σ, T_P, G`. There is no
   absolute fact of "addition vs redescription" outside a stated base; changing
   the base can change the verdict (this is a feature for comparison, a limit on
   ontology claims).
2. **First-order proxy.** Definability here is FO. Philosophers may accept
   second-order, structural, or naturalness criteria (North 2009; Dewar 2019's
   critique of structure-counting) that outrun or run against FO verdicts, in
   both directions. Beth applies to theories; informal grounding talk must be
   formalized first, and the formalization choice can smuggle in the conclusion.
3. **Census cost.** T2 is a proof problem per model class. In the two examples
   it is elementary; nothing general is claimed, and curved-spacetime or
   infinite censuses may be hard or ill-posed.
4. **Grounding preservation is contested.** T4's "clause-by-clause preservation"
   presupposes a view of what grounding clauses must preserve (intimacy,
   direction, factivity — the Correia–Merlo 2024 lead in EXPLANATORY_ROLE_TEST
   §7, unread here). A rival may reject the audit's terms.
5. **Not an ontology discriminator.** EDT separates *content* relative to a
   base; it does not, by itself, select an ontology or refute underdetermination.
   T5 inherits the audit's exclusivity-premise gap.
6. **Spacetime-group audits are their own task.** For curved spacetimes the
   comparison group `Aut(M,g)` must be computed per class; Mounoud's genericity
   is for compact manifolds and does not by itself cover noncompact spacetimes.

## 9. On parsimony and default preference (independent of the coordinator's route)

The coordinator's EXPLANATORY_ROLE_TEST retracts any default preference and
replaces parsimony-counting with an explanatory-role test. The brief asks this
lane to develop its assessment independently. Independent route, same
neighborhood, narrower claim:

- Structure-counting (fewer primitives = less structure) presupposes a shared
  signature; rival contracts differ in `Δ` by hypothesis, and Barrett 2018's own
  finding is that the automorphism criterion SYM* has "a serious shortcoming"
  precisely because `S ↛ E`. Definability-based parsimony (Glymour) is argued by
  Weatherall 2016 to miss an important equivalence sense.
- Rigid bases make invariance-based counting vacuous (§5), and §4 shows a pair
  in which every counting convention treats the two rivals symmetrically (same
  signature size, both definable, both covariant) while they disagree.
- Therefore: **numerical parsimony across ontology pairs is not well-defined
  without a shared base and a defended counting convention; on shared bases it
  is symmetric in exactly the cases that matter.** Any remaining preference must
  come from the explanatory work the added clause does — which is the
  coordinator's test, reached here by a different, logic-first route.
  [THESIS, conditional on the cited sources' claims at the stated depths]

This is a negative, defensive conclusion; it asserts no positive preference.

## 10. Strongest contrary evidence and what would defeat this submission

- **Barrett 2018 is partly *pro*-symmetry:** Thm 1 (E2 ⟺ S1) and the Thms 2–3
  route show symmetries *are* a perfect guide to local/global definability in
  the right setting. A critic can say §4/§5 attack a strawman. Response: the
  examples do not contradict his theorems — they instantiate the exact pockets
  (incomplete contract theory; rigid base) where his own results say invariance
  underdetermines. If a reviewer shows the §4 proposition wrong (a third
  equivariant expansion, or a misapplication of Zeeman), Example 1 fails; the
  check would be a dilation-invariant proper subset of the punctured null
  boundary (impossible by the orbit argument) or an order automorphism outside
  Zeeman's group in dim ≥ 3.
- **A source stating the cone-binary collapse already.** The STRONGEST_VIEW R4
  says "the light cone is the only freedom" but does not (in the text read)
  state the exactly-two/covariance collapse; Clifton–Hogarth's null-line
  discussion (inherited) is adjacent. If the coordinator's Stein–GR manuscript
  or a source we did not screen contains the binary proposition, the example
  becomes an exposition, not a new derivation — bounded negative search
  recorded in AGENT_REPORT.md, no completeness claim.
- **Correia–Rosenkranz 2020** could undercut the CC's framing: if temporaryism
  is best formalized *without* an existence-expansion of a physical model, the
  CC is one instrument among several, not the natural home of the dispute. The
  CC's residue-reporting clause is designed to absorb this (record the rival's
  own formulation; do not force translations).
- **W–C-style gauge verdicts** could deny that Example 2's labelling is ever a
  commitment rather than gauge. Then Example 2 shows the *price of the stipulation*,
  not a loss — which is all it claims.
- **Priority:** if Lipman 2026 chs. 4/6 or Iaquinto–Torrengo ch. 4 (unread,
  priority leads in STRONGEST_VIEW) contain expansion-census-style comparisons,
  the CC should cite them as predecessors.

## 11. Status ledger

| Item | Status |
|---|---|
| E/S/I definability map (Beth, Svenonius, Barrett Thms 1–3, Winnie) | PROVED (source); locators above; Beth/Svenonius originals not read |
| Zeeman causality group, dim ≥ 3 | PROVED (source); statement + Remarks read |
| Mounoud generic rigidity (compact) | PROVED (source); noncompact spacetime analogue OPEN |
| Cone-binary proposition (§4) | PROVED here, on stated stipulations + Zeeman; flat category only |
| Empirical agreement of the §4 pair | OURS: PROPOSAL (informal, timelike finite-precision records) |
| Labelled-causet loss result (§5) | PROVED here; machine-checked certificate |
| Curved-spacetime extension of §4 | OPEN |
| Metaphysical equivalence criterion | OPEN; candidate stated (§6, §8 T4) |
| Whether fundamentality disputes are substantive (O2) | OPEN; not assumed either way |
| 1+1-dimensional census | OPEN (Zeeman Remark 2 shows the group is larger) |
| Percolation completion as N3-existence datum | PROJECT reviewed result, cited not extended |

## 12. For the other lanes (proposed next tasks)

1. **Rival-contracts lane:** run EDT T0–T2 on each of the four rival contracts
   (whole-history eternalism, preferred-slicing growing block, C&R
   spatiotemporaryism/bow tie, local fragmentalism) with base = marked globally
   hyperbolic spacetime + record algebra; report each rival's residue list.
   Note: the C&R contract will need their 2020 logics (or the chapters) read
   first; their existence-clauses are quantificational, not predicate-expansions.
2. **Classification lane:** use T2's census format as the output schema for
   existence assignments satisfying covariance + restriction + persistence on a
   stated Einstein–matter category; the §4 proposition is the flat, matter-free
   template of such a census.
3. **Coordinator reconciliation:** the §4 binary + P6/P6′ gives a clean
   either/or to put to the fragmentalist strongest view: choose the closed cone
   on a defended (signalling or closure) premise, or accept an undecidable
   binary that physics does not settle.
4. **Follow-up:** 1+1 and curved (FLRW) analogues of the census; the
   noncompact-spacetime genericity check; read Correia–Rosenkranz 2020 full text
   before using their logics as `T_P` in EDT.

## 13. Sources

All source records with URLs, versions, DOIs, read depths, and limits:
`sources.jsonl` (same directory). Verification commands and outputs:
AGENT_REPORT.md and `check_poset_expansion.py` (run log therein).
