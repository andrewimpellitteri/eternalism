# Expansion versus redescription: repaired examples and a source-quantified logical map

Lane: `ontology-equivalence-repair` (29 October 2026 repair batch).
Date: 29 October 2026. Sole worker. **Status: submission for independent
review; not an accepted result; selects no ontology.**

Repairs the five findings on the equivalence-lane submission of 29 October
(reviewed in
[../coordinator/BATCH1_INITIAL_REVIEW.md](../../coordinator/BATCH1_INITIAL_REVIEW.md),
§1) to the predecessor submission at commit
`d26520bf3b1580f8f2cb3345083db4a3518c7c92` (worktree
`ontology-expansion-equivalence`, read-only input; its checkout is clean and
was not modified). Point-by-point responses:
[REPAIR_LOG.md](REPAIR_LOG.md). Source records: [sources.jsonl](sources.jsonl).
Finite checks: [check_repairs.py](check_repairs.py) (standard library, exact
rational arithmetic, wall time 0.006 s). The predecessor's RESULT remains on
file at [../../equivalence/RESULT.md](../../equivalence/RESULT.md); only
relevant material is adapted here, and nothing in the predecessor lane was
changed.

Tags: **[PROVED (source)]** — established result, locator and read depth
given; **[PROVED here]** — derivation given in this document on stated
premises; **[EXACT-FINITE]** — complete finite check by enumeration;
**[WITNESS]** — explicit finite witnesses with exact arithmetic, illustrating
an analytically proved statement; **[OURS: PROPOSAL]** — our construction,
not a theorem about the world; **[OPEN]** — not established.

## 0. Answer in brief

1. **Causal-past definability corrected (Finding 1).** The predecessor
   displayed `J⁻(b) = {x : x ≪ b ∨ x = b}`, which is `I⁻(b) ∪ {b}` (when ≪ is
   chronological), not the causal past: it omits the nonzero null cone. The
   corrected definition in the chronological language is
   `J⁻(b) = {x : ∀y (b ≪ y → x ≪ y)}`, proved analytically in §2 below
   [PROVED here]. All downstream statements now use the corrected form.

2. **Cone census survives 1+1, with exact group and dimension assumptions
   (Finding 3).** The census of §3 needs only a subgroup of the comparison
   group, not Zeeman's classification: translations, orthochronous boosts,
   positive dilations and spatial reflection are ≪-preserving by direct
   computation, and their origin-stabilizer is transitive on the nonzero past
   null cone in every spacetime dimension ≥ 2. A larger group cannot create
   new invariant subsets of an already-transitive orbit, so the census is
   **exactly two expansions** in 1+1 as well. The predecessor's "in 1+1 the
   census fails" claim is retracted. The dimension assumption is reported
   exactly: n ≥ 1 spatial dimensions for the binary; in 0+1 the two
   candidates coincide. Zeeman 1964 is demoted to context: it identifies the
   automorphism group of the *causal* order in dimensions ≥ 3 and warns
   (Remark 2) that the group is larger in 1+1 — neither fact is used in the
   proof. [PROVED here; Zeeman first page read]

3. **Per-expansion definability vs uniform recovery separated (Finding 2).**
   For the rigid three-element poset, every element is parameter-free
   definable in the base language (displayed formulas), and each of the three
   chosen growth orders is parameter-free definable as a displayed pair
   formula. What fails is **uniform recovery**: no single base-language
   formula coincides with the growth order of all three expansions of the
   shared reduct, and (by the sourced Beth direction) the shared reduct plus
   the growth-order axioms does not explicitly define the labelling. The
   predecessor's "inexpressible in the base" rhetoric is withdrawn; the
   growth claim is *added, varying-across-expansions content*, and each
   instance of it is base-expressible. [PROVED here; EXACT-FINITE check]

4. **Causal boundedness distinguished from nonuniversality (Finding 4).**
   The clause `E_b ⊆ J⁻(b)` is a substantive exclusivity premise: it excludes
   eternalism, the bow tie, and other candidates before any theorem runs.
   The census classifies expansions *within* the bounded family; it does not
   and cannot select among temporal ontologies generally (§3.2, clause-wise
   exclusion table).

5. **Logical map source-quantified (Finding 5).** Barrett 2018 was
   independently inspected this run at full-text depth through an alternate
   access route (the coordinator's direct PhilPapers fetch returned 403; see
   §1). Every quantifier is pinned: structure-level E_A/S_A vs theory-level
   E1/E2/I1/S1/S2/S3; local vs global explicit definability; implicit
   definability; Beth's hypotheses; Svenonius' completeness hypothesis;
   existence vs uniqueness as a separate column (§5). Category equivalence is
   **not** identified with Morita equivalence: Weatherall's criteria, his
   model-category morphisms, Tsementzis' doctrine scope, Barrett–Halvorson's
   many-sorted Morita, and the Andréka–Madarász–Németi–Székely 2023
   concrete-isomorphic-but-definitionally-inequivalent examples are each
   recorded with their exact hypotheses (§5.3).

6. **One corrected test (§6).** The Expansion Census and Recovery Audit
   (EDT-R), with its strongest limit stated: every verdict is indexed to
   declared base, clauses, group and protocol, and the declared clauses can
   themselves encode ontological commitments — the instrument exhibits
   underdetermination within a declared family; it cannot certify absolute
   equivalence or inequivalence of ontologies and cannot select one. No broad
   equivalence or novelty claim is made anywhere in this document.

## 1. Method, capability check, provenance

Read first: AGENTS.md, README.md, knowledge/README.md, knowledge/NOVELTY.md,
[../coordinator/BATCH1_INITIAL_REVIEW.md](../../coordinator/BATCH1_INITIAL_REVIEW.md),
[../coordinator/BATCH2_RUN_PLAN.md](../../coordinator/BATCH2_RUN_PLAN.md), and
the full predecessor submission (RESULT.md, check_poset_expansion.py,
sources.jsonl) at `../../equivalence/` in the preserved worktree at commit
`d26520bf3b1580f8f2cb3345083db4a3518c7c92`.

**Search capability check (start of session).** `scholar_search` (OpenAlex
backend) **worked** (first query: Barrett 2018 symmetries — returned the
paper plus the AMNS 2023 and Barrett–Manchak 2026 leads). `exa`
(`web_search_exa`, `web_fetch_exa`) **worked** and fetched primary pages.
Per the brief, `web-search-prime` was **not retried**. `serpapi_search` is
**quota-exhausted** ("Your account has run out of searches") — recorded, not
hidden. Access limits retained: the PhilPapers PDF
`philpapers.org/archive/BARWDS-3.pdf` rejected the coordinator's direct
fetch (403); in this run the same URL returned substantial full text through
the exa fetch pipeline, which is how Barrett 2018 was read (depth and
covered sections recorded in sources.jsonl). The Barrett–Manchak 2026
PhilSci PDF body was not extractable (only the abstract page), and no arXiv
copy exists; it is recorded at abstract depth only.

Prior art before claims; no source upgraded from abstract to proof; all
depths recorded per the knowledge-base contract in
[../../../knowledge/README.md](../../../../knowledge/README.md).

## 2. Finding 1 — the causal past in the chronological language

Throughout, M = ℝ^(1+n) is n+1-dimensional Minkowski space, signature
(−, +, …, +) with the time coordinate first, **time-oriented**; for
w ∈ M, Q(w) = w₀² − |w⃗|²; x ≪ y iff y − x is **timelike and future-directed**
(the chronological relation, x ≠ y); x ⪯ y iff x = y or y − x is causal
(timelike or null) and future-directed (the causal order); I⁻(b) = {x : x ≪ b};
J⁻(b) = {x : x ⪯ b}. All statements are Minkowski-domain statements; the
curved analogue is [OPEN] (§9).

The predecessor's §4 displayed `J⁻(b) = {x : x ≪ b ∨ x = b}`. With ≪
chronological that set is `I⁻(b) ∪ {b}` and omits every nonzero
past-null point — not the causal past. The coordinator's correction, with an
analytic proof:

**Lemma 1.** *On time-oriented Minkowski space (any dimension ≥ 2),*
`J⁻(b) = {x : ∀y (b ≪ y → x ≪ y)}`. *So the causal past is explicitly
definable in the chronological language {≪}, by one first-order formula with
parameter b.* [PROVED here]

*Proof.* (⊆) Let x ⪯ b and b ≪ y. If x = b this is trivial. Otherwise
w := b − x is causal future nonzero and u := y − b is timelike future.
Write y − x = u + w. By the reversed Cauchy–Schwarz inequality for a causal
nonzero w and timelike u with the same time orientation, ⟨u, w⟩ < 0; hence
Q(u + w) = Q(u) + 2⟨u, w⟩ + Q(w) < 0, and (u + w)⁰ = u⁰ + w⁰ > 0. So x ≪ y.
(For the record, the inequality used: applying an orthochronous Lorentz
transformation, u = αv with v = (1, 0, …, 0), α > 0, and then
⟨u, w⟩ = α⟨v, w⟩ = −α w⁰ < 0 because causal nonzero future w has w⁰ > 0.)
(⊇, contrapositive) Suppose x ⪯̸ b; put w := b − x. Take a future-directed
unit timelike v and consider y_ε = b + εv for ε > 0; then b ≪ y_ε. If x ≪ y_ε
held for every ε ∈ (0, 1], then Q(w + εv) = Q(w) + 2ε⟨w, v⟩ + ε²Q(v) < 0 and
(w + εv)⁰ > 0 throughout. Letting ε → 0⁺ gives Q(w) ≤ 0 and w⁰ ≥ 0, i.e. w
is causal future-directed, i.e. x ⪯ b — contradiction. Hence some ε has
b ≪ y_ε while x ̸≪ y_ε, so x fails the defining formula. ∎

Both uses of continuity above are limits of polynomials in ε; no analysis
beyond that is needed. Two consequences used later: (i) every ≪-preserving
bijection preserves ⪯ (⪯ is {≪}-definable), so Aut(M, ≪) ⊆ Aut(M, ⪯) — in
dimensions ≥ 3 the latter is Zeeman's causality group, giving context for how
large the comparison group can be, though the census below never needs the
identification; (ii) the undecided region between the two census candidates
of §3 is exactly N := J⁻(0) ∖ (I⁻(0) ∪ {0}), the **nonzero past null cone**.

Finite illustration [WITNESS]: check_repairs.py Part B1 evaluates the
displayed formula, with exact rational arithmetic, on six sampled point kinds
(timelike past, both null rays, spacelike, future, deep past) against the
analytic causal past; agreement is exact on all six. This illustrates Lemma 1;
it is not its proof.

## 3. Repaired Example 1 — the cone census, with exact assumptions

### 3.1 Setting and clauses

Base structure P = (M, ≪), Minkowski space, base language L = {≪}; no
metric, frame, or observer in the base. Comparison group G ⊆ Aut(M, ≪) — see
§3.4 for exactly which G the theorem needs. An expansion is a relation
E ⊆ M × M, written E_b = {x : E(b, x)}, satisfying:

1. chronological inclusion: I⁻(b) ⊆ E_b;
2. **causal boundedness:** E_b ⊆ J⁻(b);
3. self-realization: b ∈ E_b;
4. persistence: b ⪯ b′ ⟹ E_b ⊆ E_{b′};
5. covariance: σ(E_b) = E_{σ(b)} for every σ ∈ G.

Clauses (1)–(4) are stipulations [OURS: PROPOSAL], carried over unchanged
from the predecessor and modeled on the project's fragmentalist premises
(inclusion ≈ P2, boundedness ≈ the Stein-style non-universality premise,
persistence ≈ P5 of STRONGEST_VIEW, inherited project records — depths not
re-verified this run). The presentist's {b} and the eternalist's M are both
*outside* the contract — see §3.2 for exactly which clause excludes which.

### 3.2 Causal boundedness is an exclusivity premise, not "nonuniversality"

The clause-wise exclusion table (each row a direct evaluation of the clauses
[PROVED here]):

| candidate ontology clause (E_b) | excluded by | surviving clause(s) violated |
|---|---|---|
| {b} (presentist-style) | (1) | timelike-past points exist for n ≥ 1 |
| M (eternalist) | (2) | contains spacelike/future points |
| I⁻(b) ∪ I⁺(b) ∪ {b} (bow tie) | (2) | future timelike cone outside J⁻(b) |
| J⁻(b) ∖ {b} | (3) | standpoint unreal |
| I⁻(b) ∪ {b} (interior candidate) | — | survives |
| J⁻(b) (closed-cone candidate) | — | survives |

So **causal boundedness pre-selects the family**: assuming (2) already rules
out eternalism, the bow tie, and everything unbounded, before any census is
run. What the census then shows is *residual freedom within the bounded
family* — a binary the base cannot settle. The resulting "nonuniversality"
claim is therefore only this: among expansions satisfying (1)–(5), the base
underdetermines the choice. It is **not** a claim that the base cannot
distinguish temporal ontologies generally, and the census cannot select
between the two survivors. Any synthesis must carry both halves of this
distinction (response to Finding 4).

### 3.3 Proposition (census)

**Proposition 2.** *Let n ≥ 1 (spacetime dimension ≥ 2) and let G be any
group of ≪-preserving bijections of M containing translations, positive
dilations, spatial reflection and the orthochronous Lorentz group (in
particular, G = Aut(M, ≪) itself, whatever its exact extent). Then the
expansions E satisfying clauses (1)–(5) are exactly two: the interior
candidate E_int(b) = I⁻(b) ∪ {b} and the closed-cone candidate E_cl(b) =
J⁻(b). For n = 0 there is exactly one such expansion, since J⁻(b) =
I⁻(b) ∪ {b}.* [PROVED here]

*Proof.* Translations lie in G and E_{b+c} = τ_c(E_b) by (5) with σ = τ_c,
so E_b = E₀ + b; the census is decided by E₀. By (1), (2), (3),
I⁻(0) ∪ {0} ⊆ E₀ ⊆ J⁻(0); by Lemma 1 the undecided region is exactly
N = J⁻(0) ∖ (I⁻(0) ∪ {0}), the nonzero past null cone. Stabilizer elements
(positive dilations x ↦ λx; orthochronous Lorentz maps; in n = 1, boosts and
the spatial reflection (t, x) ↦ (t, −x)) fix 0 and preserve ≪ by direct
computation, so (5) makes E₀ invariant under each of them. The stabilizer is
transitive on N: in n ≥ 2, the rotations in SO(1, n)⁺ are transitive on
past-null directions (the celestial sphere S^(n−1), n − 1 ≥ 1) and dilations
scale the radius; in n = 1, N has two rays {λ(−1, ±1) : λ > 0}, the boost
u = t + x ↦ e^θ u, w = t − x ↦ e^(−θ) w moves along a ray with arbitrary
radius (θ ∈ ℝ gives all λ), and the reflection exchanges the two rays. Hence
E₀ ∩ N is an invariant subset of a single orbit: E₀ ∩ N = ∅ or N, giving
E₀ = I⁻(0) ∪ {0} or J⁻(0). Both candidates are relations of ≪ — E_int is
{x ≪ b}, E_cl is the Lemma 1 formula — so both are invariant under *every*
≪-preserving bijection, whatever G is, and both satisfy (1)–(3); for (4),
⪯-transitivity gives J⁻(b) ⊆ J⁻(b′), and x ≪ b, b ⪯ b′ gives x ≪ b′ by the
⊆-direction of Lemma 1's proof, so I⁻(b) ∪ {b} ⊆ I⁻(b′) ∪ {b′}. For n = 0
there are no nonzero null vectors, so N = ∅ and the candidates coincide. ∎

The proof uses **only** that G contains the displayed subgroup. Zeeman 1964
is not a premise of the proposition. His theorem (abstract: "Causality is
represented by a partial ordering on Minkowski space, and the group of all
automorphisms that preserve this partial ordering is shown to be generated by
the inhomogeneous Lorentz group and dilatations") identifies Aut(M, ⪯) in
dimensions ≥ 3, and his Remark 2 states the identification "depends
essentially upon space being more than 1-dimensional": in 1 space dimension
"the causality group would be much larger than G" (first page read; proof
body not audited). Two things follow for this example: the dim ≥ 3
identification is context for how large the comparison group can be, and the
1+1 group's largeness is harmless — a larger group imposes more constraints,
and the two candidates are invariant under *all* ≪-preserving maps since they
are {≪}-definable. This is the coordinator's orbit point: a larger group
cannot create additional invariant subsets of an already-transitive orbit.

Finite illustration [WITNESS]: Parts B2–B4 of check_repairs.py verify, with
exact rational arithmetic, that sampled boosts/dilations/reflection preserve
≪ on sampled pairs, keep the sampled null cone null, walk the ray and swap
rays, and leave both candidates invariant on a closed witness set. These are
witnesses; the transitivity and invariance statements are the analytic proof
above.

### 3.4 The exact group and dimension assumptions (response to Finding 3)

| comparison group G (stabilizer of 0 acting on N) | n ≥ 2 (dim ≥ 3) | n = 1 (1+1) | n = 0 |
|---|---|---|---|
| any G ⊇ ⟨translations, orthochronous Lorentz, dilations⟩, reflection allowed | 2 expansions | 2 expansions | 1 |
| G = Aut(M, ≪), full chronological-automorphism group | 2 | 2 (unproven predecessor claim "census fails" **retracted**) | 1 |
| reflection-free variant (proper orthochronous stabilizer only) | 2 (SO⁺ already transitive on S^(n−1), n−1 ≥ 1) | **4** (the two null rays are separate orbits; each can be included independently; each such E₀ satisfies (1)–(5)) | 1 |

So the honest statement of the dimension sensitivity is: the **binary** needs
a group whose origin-stabilizer is transitive on the nonzero null cone. The
full chronological-automorphism group has that property in every dimension
≥ 2 (it always contains spatial reflection); a restricted group that excludes
reflection keeps the binary for n ≥ 2 but splits it 2×2 in 1+1. And the
binary itself needs n ≥ 1: with no spatial dimension there is no null region
and one expansion. All rows [PROVED here]; the 1+1 four-expansion row is the
direct orbit computation of the proof.

### 3.5 Logical-map application (structure level vs theory level)

With the Barrett 2018 notions pinned in §5: both candidates are **explicitly
definable in the base structure** (E_int by `x ≪ b`; E_cl by the Lemma 1
formula with parameter b) — so structure-level definability and invariance
coexist here with no gap. The contract theory T′ = (base axioms) ∪ {(1)–(4)
written in L ∪ {E}} has two expansions over one and the same {≪}-reduct
differing on E, so I1 fails; by Beth (E1 ⟺ I1) there is no formula of L such
that T′ ⊢ E ↔ φ — **global (uniform) explicit definability of "the E fixed by
the contract" fails** even though each realization of E is individually,
uniformly definable. The sentence "some nonzero-null point is E-real from b"
(expressible in L ∪ {E}, using the Lemma 1 formula) is true on E_cl and false
on E_int, so T′ is incomplete — exactly the pocket where Svenonius' theorem
requires its completeness hypothesis and S1 does not lift to E1 (the same
pattern as Barrett's Example 6). Underdetermination at theory level and
definability of each instance coexist. [PROVED here on the sourced map]

### 3.6 Empirical note (informal, unchanged in status)

The two expansions agree on every timelike record at finite precision (they
differ exactly on N); this remains an informal [OURS: PROPOSAL] argument
assuming timelike records and finite timing precision — not a theorem.

## 4. Repaired Example 2 — per-expansion definability vs uniform recovery

Base P = ({a, b, c}, <) with a < b, c isolated; base language L = {<}.
Expansions: growth labellings ℓ : P → {0, 1, 2}, bijective, respecting a < b.
Three exist (EXACT-FINITE, check A2): ℓ₁ = (a,b,c) ↦ (0,1,2), ℓ₂ = (0,2,1),
ℓ₃ = (1,2,0). Each adds the growth-order relation R_ℓ = {(x, y) : ℓ(x) < ℓ(y)}
to the shared reduct (P, <).

### 4.1 Element definitions (response to Finding 2, part 1)

Each element is **parameter-free definable** in L (displayed; each evaluated
exhaustively in check A3):

- φ_a(x) := ∃y (x < y) — "x has a strict successor" — extension {a};
- φ_b(x) := ∃y (y < x) — "x has a strict predecessor" — extension {b};
- φ_c(x) := ¬∃y (x < y ∨ y < x) — "x is isolated" — extension {c}.

So the base is not merely rigid (Aut(P) trivial, check A1) but **pointwise
definable**. Rigidity makes invariance vacuous (every relation is invariant);
pointwise definability is the stronger property that makes *every* expansion
relation definable — the predecessor only noted the former.

### 4.2 Each chosen linear order is definable (part 2)

For expansion i and stage k let ρ_{i,k}(x) be "x is the element whose stage is
k", spelled out as the corresponding disjunct of φ_a/φ_b/φ_c. Then each growth
order is defined by the parameter-free pair formula

  δ_i(x, y) := ⋁_{k < k′} ( ρ_{i,k}(x) ∧ ρ_{i,k′}(y) ),

and check A4 evaluates each δ_i on all 9 pairs and confirms extension = R_i
exactly. So **per-expansion definability holds**: each of the three chosen
linear orders is an explicit base-language definition. The predecessor's
suggestion that the base language cannot state the growth claims is wrong at
the per-instance level, as the coordinator observed.

### 4.3 Uniform recovery fails — exactly (part 3)

The three growth relations are pairwise distinct (check A5: R₁ =
{(a,b),(a,c),(b,c)}, R₂ = {(a,b),(a,c),(c,b)}, R₃ = {(a,b),(c,a),(c,b)}), and
the semantic census of all 2⁹ = 512 binary relations on P contains exactly
three strict linear extensions of <, namely R₁, R₂, R₃ (check A5). Since a
formula of L has one extension on the fixed structure P, no single L-formula
coincides with the growth order of all three expansions: **uniform recovery
over the expansion family fails** — exact, finite, no syntax enumeration
needed.

Theory-level restatement on the sourced map: the shared reduct with axioms
"R is a linear extension of <" has three expansions over one reduct, so I1
fails; by Beth, no formula δ with the theory ⊢ δ ↔ R: **no uniform explicit
definition of the growth order relative to the shared axioms.** The test
sentence "c became real before b" (stage(c) < stage(b)) is FALSE on ℓ₁, TRUE
on ℓ₂, ℓ₃ (check A6): the shared reduct is one fixed structure, every base
sentence has a fixed truth value on it, and this claim's value varies across
the three expansions, so no base sentence co-varies with it. [All PROVED
here; EXACT-FINITE]

### 4.4 Scope guard

The correct summary is: the growth claim is **added content whose truth varies
across expansions of the shared base; each instance of it is base-definable;
no single base definition recovers all three uniformly.** Not claimed:
absolute "inexpressibility" of growth talk in the tenseless base; not claimed:
anything about growth realism's correctness, gauge status, or physics (the
three-element domain is a toy; the empirical-inertness discussion of the
predecessor §5 is inherited project context, not re-verified here).

## 5. The logical map with pinned quantifiers (response to Finding 5)

### 5.1 Two levels, kept separate

| level | objects quantified over | conditions |
|---|---|---|
| structure (fixed A, Barrett's "model approach") | the single structure A | E_A: some Σ-formula φ has φ^A = r^A. S_A: every automorphism h of the reduct A∣Σ preserves r^A. |
| theory (T, Barrett's "theory approach") | all models of T | E1: one Σ-formula φ with T ⊨ ∀x(r ↔ φ) — **uniform across models**. E2: each model M of T individually defines r^M (formula may vary with M). I1: models with the same Σ-reduct agree on r. S1: r^M invariant under Aut(M∣Σ) for each model M. S2/S3: r^M transported along elementary embeddings / isomorphisms between reducts of models. |

A fixed-model verdict never entails a theory-level one: Example 5 of Barrett
(rigid structure, non-definable invariant subset) blocks S_A ⟹ E_A, and
Example 6 (one-element models, r unconstrained) blocks S1 ⟹ E1.

### 5.2 Exact statements pinned this run (Barrett 2018, full text read this run)

Independently inspected this run via the exa fetch of the PhilPapers PDF
(access route and limits in §1 and sources.jsonl); the predecessor's locators
were confirmed:

- Prop 1: E_A ⟹ S_A (automorphisms preserve Σ-formula extensions).
- Prop 2: E_A ⟺ S_B for every Σ∪{r}-structure B **elementarily equivalent**
  to A (Winnie 1986, Prop 1.10; per Barrett's footnote 8, Winnie's Prop 1.11
  gives E_A ⟺ S_A for the restricted class of "lucid" structures).
- Example 5: Σ = {c₀, c₁, …}; countable structure with identity-only
  automorphism group; r an extension given by a counting argument
  (uncountably many subsets, countably many formulas); S_A holds vacuously,
  E_A fails.
- E1 ⟹ E2 always; Example 6 (Σ = ∅, exactly-one-thing models, r free): E2
  holds, I1 fails — E2 ↛ E1 and S1 ↛ E1 (Prop 3 + Example 6 continued).
- **Beth** (as cited to Hodges 2008, Thm 6.6.4): E1 ⟺ I1.
- **Svenonius** (as cited to Hodges 2008, Cor 10.5.2): **if T is complete**,
  E1 ⟺ S1 — the completeness hypothesis is load-bearing; Barrett: most
  theories are not complete.
- **Theorem 1: E2 ⟺ S1** (proof goes through Prop 2 and elementary
  equivalence). Prop 3: E1 ⟹ S1 (so I1 ⟹ S1 via Beth). **Theorem 2: E1 ⟺ S2**;
  **Theorem 3: E1 ⟺ S3**.
- SYM*: "X has more structure than Y if the automorphism group of X is a
  proper subset of the automorphism group of Y" — Barrett's own "serious
  shortcoming": S_A ↛ E_A, so SYM* fails on the rigid pair (A, A∣Σ).
- Corollary 1 (his): the forgetful functor Π : Mod(T⁺) → Mod(T) forgets
  structure iff E1 fails of T⁺; Π is full iff S2.
- On Morita, Barrett explicitly **sets it aside**: "how much stronger 'Morita
  equivalence' — the many-sorted analogue of definitional equivalence — is
  than categorical equivalence", deferring to Barrett–Halvorson 2016 (RSL
  9(3): 556–582; not read this run).
- One-line reading: **invariance is a perfect guide to local (per-model)
  definability; global/uniform definability is captured only by implicit
  definability (Beth), by elementary-embedding or isomorphism invariance
  (Thms 2–3), or by invariance for complete theories (Svenonius).**

Hypotheses of Beth/Svenonius as available here: first-order logic; Beth used
at the (E1 ⟺ I1) form; Svenonius only with T complete. Hodges 2008 and
Svenonius 1959 were **not read** — locators inherited from Barrett and
predecessor, marked as such.

### 5.3 Category equivalence ≠ Morita equivalence — exact hypotheses

The brief forbids asserting "category equivalence = Morita equivalence"
without exact hypotheses. Pinned:

- **Weatherall 2016** (arXiv:1411.5757v3 full text read this run): Criterion
  1 (Glymour's, definability-based with unique covariant definability
  between models); Criterion 1′: isomorphism of categories of models
  **preserving empirical content**; Criterion 2: **equivalence** of categories
  of models preserving empirical content. His footnote: "the category of
  models of a theory T has models of T as objects and elementary embeddings
  as arrows" — but in the applications he builds *specific* categories with
  specific arrows (e.g. isometries preserving the Faraday tensor, or
  preserving gauge-transformed potentials), and his Prop 5.2 is an
  isomorphism while Prop 5.5 is only an equivalence — the morphism choice is
  load-bearing. His text states that even in first-order logic, isomorphism
  between categories of models is strictly weaker than definitional
  equivalence.
- **Tsementzis 2017** (abstract read): Morita equivalence "in the sense of
  Johnstone" is characterized syntactically as **common definitional
  extension** (Barrett–Halvorson's notion) "for cartesian, regular, coherent,
  geometric and first-order theories" — i.e. the identification holds within
  that doctrine scope, for equivalence of categories of models "naturally in
  any Grothendieck topos", not for arbitrary categories with arbitrary
  morphisms. [Abstract-level: the body theorem is not audited here.]
- **Barrett–Halvorson 2016** (RSL 9(3):556–582; **not read**; locator via
  Barrett 2018's references): Morita equivalence as many-sorted analogue of
  definitional equivalence — [discovery-depth lead].
- **Andréka, Madarász, Németi, Székely 2023** (arXiv:2211.14232v2, abstract
  read): first-order theories are definitionally equivalent iff there is a
  bijection between their model classes preserving isomorphisms and
  ultraproducts (their Thm 2); and they exhibit **uncountably many pairs of
  definitionally inequivalent theories whose model categories are concretely
  isomorphic** via bijections preserving ultraproducts up to isomorphism —
  the sharpest available warning that categorical data alone do not deliver
  definitional/Morita equivalence. [Abstract-level; settle conjectures of
  Barrett/Glymour/Halvorson per abstract.]

So the corrected column in any comparison: a claim of "same models up to
equivalence" must specify (i) which category (objects and **morphisms**),
(ii) which logic/doctrine, (iii) isomorphism vs equivalence of categories,
(iv) what is preserved (empirical content? clauses?). Only inside the
Johnstone-Morita + doctrine scope does common-definitional-extension follow
(Tsementzis); outside it, concrete isomorphisms exist without definitional
equivalence (AMNS 2023). [PROVED (source) at the stated depths]

### 5.4 Existence vs uniqueness (kept as its own column)

Existence of an expansion (census = 0 vs ≥ 1) and uniqueness up to
expansion-isomorphism (census = 1 vs ≥ 2) are separate questions, both
separate from definability: zero expansions = the rival's clauses are
unsatisfiable on the base class; one = candidate implicit definability (Beth
applies); several over one reduct = I1 fails = no uniform definition. The
cone example is a ≥ 2 case where every candidate is nonetheless definable;
the predecessor's percolation citation remains a project-internal
existence-failure datum, cited not extended.

## 6. One corrected test — Expansion Census and Recovery Audit (EDT-R), and its strongest limit

[OURS: PROPOSAL] Input: declared base (Σ, T_P), comparison group G, added
vocabulary Δ with clauses A_i, protocol class. Output: a verdict matrix, not
a single bit.

- **T0 Base declaration.** State Σ, T_P, G, and the protocol class. Lanes on
  different bases do not transfer verdicts.
- **T1 Invariance audit, two tiers.** Structure tier: which candidate
  Δ-extensions are G-invariant; if Aut is trivial, record that invariance is
  vacuous and check **pointwise definability** separately (it, not rigidity,
  decides whether expansion relations can be displayed). Theory tier:
  invariance under automorphisms (S1), elementary embeddings (S2),
  isomorphisms (S3) of models of T — never conflate tiers; S_A ↛ E_A and
  S1 ↛ E1 have pinned counterexamples (§5.2).
- **T2 Census.** Count expansions of T_P + A over a shared reduct, up to
  expansion-isomorphism. 0 = existence failure; ≥ 2 over one reduct = I1
  failure witnessed (list the witnessing pairs of expansions); 1 = candidate
  implicit definability.
- **T3 Recovery audit, three separate verdicts.** (i) Per-expansion explicit
  definability: display formulas (E2/local; in finite or pointwise-definable
  settings these can be displayed outright). (ii) Uniform/global definability
  (E1): only via I1 by Beth; invoke Svenonius only after stating that T is
  complete. (iii) Residue list: sentences whose truth varies across the
  census — the rival's added commitments relative to this base (recovered
  per instance, not uniformly).
- **T4 Preservation audit.** Any equivalence claim must declare the category
  (objects and morphisms), the logic/doctrine, isomorphism vs equivalence,
  and what is preserved (empirical content; existence/grounding/truth-policy
  clauses clause-by-clause). Without that, "category equivalence" licenses no
  ontological reading (§5.3).
- **T5 Empirical audit.** Inert vs active Δ in the declared protocol class;
  inert Δ ⟹ no likelihood separation at these realizations (project
  discriminators-audit lemmas inherited, not re-verified).

**Strongest limit (stated with the test).** Every verdict of EDT-R is indexed
to the declared base, clause set, group and protocol — and those declarations
can themselves encode substantive commitments: clause (2) of §3 excluded
eternalism before any census ran, and a protocol declaration can make added
structure inert by fiat. The audit can therefore exhibit
underdetermination-within-a-declared-family and separate per-instance from
uniform recoverability; it cannot certify absolute equivalence or inequivalence
of ontologies, cannot select an ontology, and its "added vs redescription"
verdicts are not base-invariant. That is the limit; no broader claim is made
for the instrument.

## 7. Prior-art audit

New records this run (full details in [sources.jsonl](sources.jsonl)):

| source | depth this run | use |
|---|---|---|
| Barrett 2018, Phil. Science, DOI 10.1086/699156 | full text (substantial portions incl. proofs, via exa fetch of the PhilPapers PDF; coordinator's direct fetch 403) | §5.2 quantifiers; Examples 5–6; SYM*; Corollary 1; Morita set-aside |
| Zeeman 1964, J. Math. Phys. 5(4):490–493, DOI 10.1063/1.1704140 | first page (abstract, theorem, Remarks 1–4) | context only: causal-order group, dim ≥ 3; Remark 2 quote; **not a census premise** |
| Weatherall 2016, arXiv:1411.5757v3 | full text (arXiv HTML, ~66k chars; criteria, EM and NG/NGG category constructions, footnotes) | §5.3 criteria 1/1′/2 and morphism choices |
| Andréka–Madarász–Németi–Székely 2023, arXiv:2211.14232v2, RSL DOI 10.1017/S1755020323000242 | abstract | §5.3 concrete-isomorphic ↛ definitionally equivalent |
| Tsementzis 2017, arXiv:1507.02302v1, JSL DOI 10.1017/jsl.2017.59 | abstract | §5.3 Johnstone-Morita ⟺ common definitional extension, doctrine scope |
| Semenov–Soprunov 2015, arXiv:1301.2412v2, Logic J. IGPL 23(6):966–975 | abstract | Svenonius content: permutations of elementary extensions |
| Barrett–Manchak 2026, PhilSci-Archive 30643 | abstract only (PDF body not extractable; no arXiv copy) | current lead: implicit-definability hierarchy in GR; "symmetry perfect guide" special cases — nearest current neighbor of §5; **to be read in full before any use** |
| Barrett–Halvorson 2016, RSL 9(3):556–582 | discovery (locator via Barrett's references) | §5.3 Morita lead |
| Minguzzi–Sánchez 2008, arXiv:gr-qc/0609119 | abstract (lead) | causal-hierarchy reference; the composition facts in Lemma 1 are proved here analytically, not cited from it |
| O. C. Stoica 2016, arXiv:1504.03265 | abstract (lead) | adjacent: reconstructing causal/chronological structure from the horismos relation |

Inherited from the predecessor at their recorded depths (not re-verified):
Winnie 1986, Hodges 2008, Svenonius 1959, Mounoud 2014, Malament 1977,
Clifton–Hogarth 1995, Glymour 1977, De Haro 2019, Dewar 2019, North 2009,
Redhead 1975, Ismael–van Fraassen 2003, Field 1973, Correia–Rosenkranz 2020,
Sider 2001, Barrett–Manchak 2024, Wüthrich–Callender 2017, Rideout–Sorkin
2000, Brightwell–Luczak 2011, Lipman 2023, Fine 2005, Swanson–Halvorson 2012,
and the project records (STRONGEST_VIEW, discriminators-audit,
CLAIM_STATUS, EXPLANATORY_ROLE_TEST, lawful-completions review) — see the
predecessor's sources.jsonl at
[../../equivalence/sources.jsonl](../../equivalence/sources.jsonl).

Not new here (novelty honesty): the definability/invariance map is Barrett
2018's (with Winnie, Beth, Svenonius); the causal-order-from-chronology
formula is the coordinator's correction and is a standard-type observation;
Zeeman and Mounoud are cited results. The repaired lane's contribution
remains, at most: the two in-domain examples with exact assumptions, the
per-expansion/uniform-recovery distinction with an exact finite certificate,
and the corrected test — all submitted for review, none asserted as an
established novelty.

## 8. Strongest contrary evidence

- **Barrett 2018 is partly pro-symmetry:** Thm 1 (E2 ⟺ S1) and Thms 2–3 show
  symmetries are a perfect guide to local — and (via embeddings/isomorphisms,
  or completeness) global — definability. If a reviewer shows the cone census
  wrong (a third ≪-preserving candidate expansion, or a stabilizer not
  transitive on N), Example 1 fails; the check would be an invariant proper
  subset of the nonzero null cone under the displayed subgroup (impossible by
  the orbit computation) or a ≪-preserving bijection not covered by the
  analytic preservation checks.
- **The Lemma 1 formula is folkloric.** If a source states causal-past
  definability from chronology explicitly (candidate places: causal-hierarchy
  surveys, definability-in-spacetime literature), §2 becomes an exposition of
  a known fact — the proof here would still stand, the claim to derivation
  novelty would not. Bounded negative search recorded in AGENT_REPORT.md; no
  completeness claim for the search.
- **BM2026** may already contain the quantifier map of §5 in GR form; until it
  is read in full, §5 claims no priority over it.
- **Wüthrich–Callender-style gauge verdicts** on growth orders would make
  §4's lost claim a price willingly paid rather than a loss — §4 claims only
  what the stipulation costs, nothing about the stipulation's correctness.
- **Restricted-group defenses:** a rival who restricts G to exclude
  reflection loses the binary in 1+1 (four expansions, §3.4) — which *strengthens*
  underdetermination rather than rescuing uniqueness; noted so the census is
  not oversold as group-independent.

## 9. Status ledger

| item | status |
|---|---|
| Lemma 1 (causal past definable in {≪}, Minkowski, analytic proof) | PROVED here; curved analogue OPEN |
| Cone census, n ≥ 1, G ⊇ displayed subgroup (incl. G = Aut(M,≪), 1+1) | PROVED here (supersedes predecessor's "1+1 fails") |
| No-reflection 1+1 variant (4 expansions); 0+1 (1 expansion) | PROVED here |
| Zeeman role in the example | demoted to context; first page read; proof not audited |
| Poset: pointwise definability + per-expansion definability | PROVED here; EXACT-FINITE |
| Poset: failure of uniform recovery (fixed base + Beth at theory level) | PROVED here; EXACT-FINITE |
| Clause-wise exclusions (boundedness vs nonuniversality) | PROVED here (direct clause evaluation) |
| Barrett 2018 quantifier map (Props 1–3, Thms 1–3, Exs 5–6, SYM*) | PROVED (source), full text this run; Hodges/Svenonius originals not read |
| Category equivalence vs Morita hypotheses | PROVED (source) at abstract/full-text depths as recorded; Barrett–Halvorson 2016 not read |
| Curved-spacetime census and noncompact genericity | OPEN |
| Empirical agreement of the cone pair | OURS: PROPOSAL, informal |
| Any ontology selection, or broad equivalence/novelty claim | NOT MADE (out of scope for this lane) |

## 10. Sources and verification

All records: [sources.jsonl](sources.jsonl) (schema per
[../../../knowledge/README.md](../../../../knowledge/README.md), lane prefix
`eqr-`). Verification: `python3 check_repairs.py` — all checks pass, wall
time 0.006 s (log reproduced in AGENT_REPORT.md). Predecessor worktree
verified clean at `d26520bf3b1580f8f2cb3345083db4a3518c7c92` before work
began and untouched after. Point-by-point repair responses:
[REPAIR_LOG.md](REPAIR_LOG.md). Runner handback: AGENT_REPORT.md at the
repository root.
