# Repaired bridge arguments: supervenience, constitution, anchoring

29 October 2026. Lane: `ontology-bridges-repair` (repair of
[`ontology-bridge-premises`](../../bridges/RESULT.md) — the predecessor
submission, which integrates at that path; read this session from its
preserved worktree at pinned predecessor
commit `c15901c3197044c557dc968ffd5e6851f61e283b`, clean, READ ONLY). This is
a worker submission for coordinator review. It contains no
accepted theorem, no novelty claim, and no project ontology verdict. A repair
enters review; it does not accept itself and does not select a temporal
ontology. Point-by-point response to the coordinator findings:
[REPAIR_LOG.md](REPAIR_LOG.md). Source register: [sources.jsonl](sources.jsonl)
(schema per [knowledge/README](../../../../knowledge/README.md)).

## 0. Method, capability check, independence

- **Search capability check.** `scholar_search` **worked** (29 Oct 2026).
  Query 1 (Kim "Concepts of Supervenience" 1984) returned the exact Crossref
  records: *Philosophy and Phenomenological Research* 45(2), first page 153,
  DOI 10.2307/2107423; and Kim 1987 "'Strong' and 'Global' Supervenience
  Revisited", PPR 48(2), p. 315, DOI 10.2307/2107631. Query 2 (Malament 1977)
  returned Crossref metadata for *Noûs* 11(3), p. 293, DOI 10.2307/2214766,
  plus two contrary-scope papers recorded below. Primary fetch used
  `exa.web_fetch_exa` (Rynasiewicz 2001 PhilSci preprint, abstract + opening
  section read). `web-search-prime` **not used and not retried** (per brief).
  `serpapi_search` not needed and not tested this session.
- Small, relevant query batches and citation chasing only. Every source used
  below is registered with its exact version/locator and this session's honest
  read depth. Depths from the predecessor lane are reused **at their recorded
  depth and marked as project records**; this session did not re-read Putnam,
  Stein, Wüthrich–Callender, Pooley, Arageorgis, C&R or Brading in the
  original, and no claim below depends on a fresh reading of them.
- **Independence.** This lane assumes no unfinished conclusion of the other
  repair lanes (`ontology-equivalence-repair`, `ontology-rivals-repair`) or of
  the pending C¹,¹ axis reconstruction. Internal project results are cited at
  their recorded status (coordinator-reviewed sidecar / internal proof
  proposal / proposal), never as externally refereed results.

## 1. The repaired framework: neutral reduct, separate existence predicate, admissible class, exact premise

The coordinator's central correction is accepted: a physical representation of
future events does not by itself assume their concrete existence. What follows
is the framework the predecessor's §1.3 should have used.

### 1.1 Neutral physical reduct

A **physical reduct** is a structure `P = (M, g_ab, fields, b)` (continuum) or
its finite surrogate `P = (T, ≤, b₁,…,b_k)` (labels with an order relation and
marked standpoints). `P` is interpreted **representationally and only
representationally**: it is an adequate representation of the accessible
physical facts. Nothing in the interpretation of `P` asserts that the elements
of `M` (or `T`) concretely exist, and nothing asserts that they do not. This is
the same discipline as the coordinator's finite line in
[EXPLANATORY_ROLE_TEST §2](../../coordinator/EXPLANATORY_ROLE_TEST.md): labels
are comparison devices; including them in the metalanguage is not an
ontological assertion.

### 1.2 Separate existence predicate

An **existence assignment** on `P` is a function `E` taking each marked
standpoint `b` to a subset `E(b) ⊆ M` (resp. `⊆ T`), read as
"`x ∈ E(b)`" ≡ "`x` would be concrete from standpoint `b`" under that
candidate expansion. `E` is a *separate predicate* on top of `P`: the pair
`w = (P, E)` is an **expansion** (a candidate world). Different `E` on the same
`P` are different ontological readings of one and the same physical
representation.

### 1.3 Admissible class

Fix structural admissibility constraints on assignments, each a mathematical
property of `(P, E)`:

- **A1 (invariance/covariance).** For every automorphism `φ` of `P`:
  `φ[E(b)] = E(φ(b))`. Finite surrogate of "no privileged observers".
- **A2 (self-inclusion).** `b ∈ E(b)`.
- **A3 (persistence).** `b ≤ c` implies `E(b) ⊆ E(c)`.
- **A4 (restriction).** `E(U, b) = U ∩ E(M, b)` over the named comparison
  category (causally convex open embeddings; initial segments in the finite
  surrogate).

Write `Adm(P)` for the set of assignments satisfying the named constraints.
`Adm(P)` is defined without any use of concrete existence.

### 1.4 The exact supervenience and uniqueness premises

**SU (global supervenience of the concrete on the physical).** For any two
admissible expansions `w = (P, E)`, `w' = (P', E')`: if there is a reduct
isomorphism `h : P → P'`, then for every marked standpoint `b` and event `x`:
`x ∈ E(b)` iff `h(x) ∈ E'(h(b))`. (This is the standard *global* supervenience
form; the taxonomy is Kim's — `bridgefix-kim-1984`, metadata only. No claim
about Kim's own views is made here.)

**UNIQ (uniqueness of the existence function).** For each reduct `P`:
`|Adm(P)| = 1` up to reduct isomorphism — all admissible expansions of `P`
agree on which events are concrete.

The relationship matters:

- SU is *trivially satisfied* inside any one-expansion class. A rival who
  asserts supervenience typically does so by admitting exactly one `E` — e.g.
  the eternalist's `E ≡ M`, or the growing-block theorist's foliation-indexed
  assignment. Such a rival **rejects precisely the plural class** in which both
  `E_all` and `E_past` live.
- UNIQ is the substantive content of "supervenience as a *theorem*": the
  claim that the named constraints force a single `E`. UNIQ entails SU; SU does
  not entail UNIQ (SU is compatible with each connected component of the
  admissible class having its own `E`, so long as admissibility itself fixes
  the component — the standard gap between global supervenience and
  *determinability* of the supervenient pattern by the base).
- Therefore the correct repaired verdict is: **the physics considered here
  (the reduct plus A1–A4) does not entail UNIQ, hence does not entail or
  uniquely specify the bridge.** "Circular" is reserved for the specific
  definition-exploiting formulation diagnosed in §2 below.

### 1.5 What `E_all` and `E_past` coexistence does and does not refute

Both `E_all(M,b) = M` and `E_past(M,b) = J⁻(b)` satisfy A1–A4 on time-oriented
globally hyperbolic spacetimes (coordinator,
[PREMISE_STRESS_TEST §1](../../coordinator/PREMISE_STRESS_TEST.md); finite
witness W1 below). Precisely:

**What their coexistence refutes:**

1. That covariance, persistence, self-inclusion and restriction compatibility
   *entail* UNIQ — the inference from "physics + structural cleanliness" to a
   unique concrete inventory fails (nonentailment; witness W1).
2. That any argument is a *neutral selection theorem* whose premises a
   C&R-style and a Stein-style rival both accept while forcing one outcome
   (the predecessor's §1.3 "neutral reading does no selecting" observation,
   retained with corrected scope).

**What their coexistence does not refute:**

1. **Supervenience itself (SU).** Each of `E_all` and `E_past` *individually
   supplies a different supervenience function within its own one-expansion
   class*. In the class `Adm ∪ {UNIV}` there is exactly one assignment and SU
   holds; in the class `Adm ∪ {DOWN, FUTEX}` there is exactly one assignment
   (the causal-past one) and SU holds there too. W1 machine-checks both
   counts. The two rivals disagree about *which* function is correct; they do
   not disagree about whether the concrete supervenes on the physical *within
   their own theory*.
2. **Either candidate individually.** That two readings are both admissible
   shows a *gap* in the constraints, not that both readings are correct or
   that "anything goes". If the predicate "concrete from b" has a determinate
   extension at all, at most one of `E_all`, `E_past` is correct — the
   coexistence result is silence, not parity.
3. **The rational permissibility of either rival.** A supervenience-asserting
   rival may reject the shared plural class precisely because it finds
   existence-pluralism unacceptable; that rejection is a substantive
   philosophical position (§6), not a formal error.

## 2. Four failure modes, defined and kept distinct

These are our stipulative definitions in the expansion framework (standard
informal usage noted; no citation is offered as authority for the
stipulations):

1. **Nonentailment.** Premises Γ, conclusion C: Γ ⊬ C — there is a model of
   `Γ ∧ ¬C`. A property of the *argument's validity-in-extension*, independent
   of anyone's dialectical situation.
2. **False premise.** Some `γ ∈ Γ` is false (under the intended reading).
   The argument may be perfectly valid; it fails because the world or the
   intended interpretation does not satisfy a premise.
3. **Question-begging inference.** The argument is valid and its premises
   perhaps true, but the argument cannot serve *as an argument for C* to a
   rational audience that doubts C, because justifying some premise requires
   already accepting C (or the denial of a rival's live alternative is assumed
   rather than argued). A dialectical/epistemic defect, relative to an
   audience, not a formal one.
4. **Logical circularity.** The derivation uses C itself, or a premise
   *definitionally contains* C — the "conclusion" is an immediate expansion of
   a definition. A structural property of the derivation.

Application to the bridges (details in §§3–5):

| Claim as originally stated | Mode | Exact diagnosis |
|---|---|---|
| A1–A4 ⊢ E_all (Putnam-style) | Nonentailment + one conjunct of a premise false | W1/W2: structural constraints admit 6 families; the Putnam R-premise needs "R is definable **and** slice-like"; in SR no filling satisfies both (Stein 1991, print-audited; Malament 1977 within his scope conditions) |
| A2 as originally phrased ("cannot be stated neutrally") | Mis-diagnosis, now retracted | SU/UNIQ over the explicit reduct+expansion pair is neutral (§1.4); only the variant where "physical facts" is *defined* as the tenseless-total inventory is logically circular — and that variant is avoidable, so no blanket circularity verdict |
| "The class admits two expansions, so supervenience is refuted" | Question-begging (if used against a supervenience-asserting rival) | It assumes exactly the admissibility pluralism the rival denies (§1.5); against a neutral audience it is a sound nonentailment witness |
| B3 constitution from P1+P2 (completeness/constitution bridge) | Nonentailment (protocol-scoped) | §4: matched past records do not determine future lifetime in the named comparison class; no all-protocol claim is made |
| "R = definable in tenseless structure, therefore primitive tensed facts are unreal" | Question-begging (against primitive-fact theories) | The anchoring demand, if stated as an ontological criterion rather than a methodological preference, assumes what the primitivist denies (§5, defeat condition 3) |
| "Completeness has no observational content" (predecessor §2.5) | Overgeneralized nonentailment | Retracted: protocol P2 distinguishes the models (§4.3) |

## 3. Bridge A′: standpoint-indexed physical supervenience

**Proposed bridge (repaired).** For a named smooth relativistic category and
its reducts `P`: the concrete-from-`b` inventory is invariant under reduct
automorphisms, and the admissible-expansion class is claimed (as a
philosophical premise, not a theorem) to satisfy UNIQ. The open question is
which `E` is uniquely admissible; the bridge itself is the claim that
existence attributions must be anchored and determinate — not the claim that
`E = M`.

- **A′1 (invariance).** A1 above. *Retained noncircular premise*: if two
  reducts are isomorphic as physical structures, their concrete inventories
  must correspond. Defense: a violation would individuate standpoints by
  something outside the physical representation — an empirically and
  structurally idle privilege (W2 shows this premise does real work: it
  excludes the privileged-standpoint family).
- **A′2 (determinacy).** For the actual standpoint, "concrete from b" has a
  determinate extension (minimal ontological seriousness, shared by all
  rivals that accept existence talk at all; a strict deflationist about
  existence rejects the question — record that, do not average it away).
- **A′3 (UNIQ as claim).** The admissible class contains exactly one
  assignment. *This is the exact supervenience premise at issue*, and it is a
  philosophical thesis about which constraints are genuinely admissible —
  not a consequence of physics (W1).

### 3.1 Strongest primary defense (depths as recorded)

Putnam 1967 (full text, predecessor lane's read, JSTOR-scan copy): premises
(1), i–iii at pp. 240–241, transitivity argument p. 243, "Morals and
Conclusions" p. 246 — the strongest historical form because it derives an
ontological conclusion from explicitly physical premises without parsimony or
model-domain reasoning. Stein 1991 (theorem p. 149, print-audited by the
project at pp. 148–150 with the prose conditions — non-universality (iv) and
causal-past inclusion — the audit supplies): within Minkowski spacetime the
only non-trivial invariant definiteness relation satisfying those conditions
is the causal past.

### 3.2 Why the Putnam argument fails, exactly

Putnam's R must be (i) physical, coordinate-independent, tenselessly
definable; (ii) transitive across observers ("no privileged observers", III);
(iii) slice-like — each observer's R-class is a full simultaneity slice — for
the transitive closure to cover the manifold. In SR, no relation satisfies
(i)–(iii) together: the invariant-definable candidates are causal (Stein's
theorem), and the causal past is not slice-like; the slice-like candidates
(frame simultaneity) are not invariant-definable without a physically
distinguished frame (Malament 1977 for equivalence-type simultaneity
relations, within his scope conditions; see §5.2 for the disputed
philosophical import). So the argument is **valid but unsound**: one conjunct
of the R-premise is false under every uniform filling. The failure mode is
*false premise + nonentailment*, not circularity. (Category relativity: in
nearly-FLRW cosmologies a matter-distinguished foliation exists, so conjunct
(i) *can* hold there — the argument's scope is category-relative; project
red-team lead, lead-level provenance,
[bridges-redteam-synthesis](sources.jsonl).)

### 3.3 Charitable rival rejections (retained, not dismissed)

- **Stein-style (standpoint-relative becoming).** Accepts A′1–A′3 with
  `E = J⁻(b)`: supervenience holds inside the one-expansion class; "special
  relativity is perfectly compatible (in general) with 'ontological
  probabilism'" (Stein 1991 p. 164, quoted via Pooley 2013 §X — secondary
  carrier, recorded).
- **C&R later-grounded bivalent** (project chapter extraction, chs. 7 and 9):
  accepts the physics and a supervenience thesis for *truth* on a different
  base — the fourfold division plus grounding, not the concrete inventory.
  Their (GR) p. 110 permits present future-directed truths with later
  explanatory grounds; their bow-tie existence (ch. 9 pp. 149–150) denies
  that existence-at is causally closed. Against the *repaired* A′3 they say:
  UNIQ fails because the admissible class genuinely contains several readings
  (they embrace one of them), and the disputed question is which — precisely
  the coordinator's point.
- **Brading system-relative** (project record, pp. 1101–1111): existence is
  relativized to dynamical systems; A′1 becomes system-relative invariance;
  the union of local presents can cover the history.

### 3.4 Repaired verdict (A′)

The physics considered here does not entail or uniquely specify the
supervenience bridge (W1). The retained, defensible, noncircular content:
A′1 (invariance) and A′2 (determinacy) — both rivals accept them; they have
real filtering power (W2) and no selection power among the invariant
candidates (W1). Which `E` is uniquely admissible is decided by philosophical
premises (§6), not by the formalism.

## 4. Bridge B′: representation completeness and the isolated constitution premise

**Proposed bridge (repaired).** Separate the established mathematics from the
philosophical premise:

- **B′1 (dynamical determination — mathematics).** Smooth vacuum Cauchy data
  admit a unique maximal development (Sbierski arXiv:1309.7591v3, Theorem 2.7,
  as sourced in the project's reviewed
  [REPAIR_RESULT](../../../lawful-completions/coordinator/REPAIR_RESULT.md);
  internal review status, not external refereeing).
- **B′2 (representational completeness).** The best theory's models of the
  actual world are (isomorphic to) maximal solutions. A claim about
  *representation* only.
- **B′3 (constitution — the isolated philosophical premise).** The concrete
  totality is constituted by the events of the maximal actual solution.
  Noncircular statement: a theory-constitutive realism about model content —
  whatever the best theory quantifies over in its models of actual systems is
  part of the concrete inventory. This is substantive, contestable, and does
  not assume which events exist; it is therefore *not* logically circular
  (§2). Its defense, if any, is abductive, not physical.

### 4.1 Strongest primary defense (depths as recorded)

Pooley 2013 preprint §II: the B-theory answers **yes** to "Is an exhaustive
catalogue of which events occur, and how they are temporally related, a
complete account of temporal reality?" — the cleanest statement of what B′3
adds to B′2. The sharpness example (below) shows the physical boundary of the
defense.

### 4.2 The clipped-Minkowski result, stated at its exact scope

Project-reviewed construction
([COMMON_EXTENSION_REPAIR](../../../lawful-completions/coordinator/COMMON_EXTENSION_REPAIR.md),
"Sharpness example"; internal review status): `M₁ =` Minkowski `\ J⁺(q)` (q
later than the mark b) is smooth, vacuum, globally hyperbolic, a **nonmaximal**
GHD of the *same* earlier Cauchy data as full Minkowski `M₂`; the potential
realms at b coincide; the central unit-speed geodesic ends at proper time T in
M₁ and continues indefinitely in M₂; all matched readings agree at every
duration both define (the reviewed readout-agreement result in
[REPAIR_RESULT](../../../lawful-completions/coordinator/REPAIR_RESULT.md)).

**Exact protocol statement (the repair):**

- **P1 (matched-past protocol).** Comparison class: {M₁, M₂} as above. Access
  window: records at durations strictly below the shorter lifetime. Result:
  records identical; lifetimes differ. Hence: **matched past records do not
  determine future lifetime** — a nonentailment *for this protocol and
  comparison class* (discrete surrogate W5 machine-checks the protocol
  logic).
- **P2 (future-inclusive protocol).** Same class; access includes durations at
  or beyond T. Result: the hypotheses "the world is M₁" and "the world is
  M₂" differ in what a persisting observer records at durations ≥ T (further
  readings vs. none — the model contains no such events; an actual observer
  who persists beyond T refutes `M₁`-as-complete-world). Hence completeness
  hypotheses **have predictive content**: they are decidable, if at all, only
  by future observation.

### 4.3 Repaired verdict (B′) — overclaim retracted

- Established (project-reviewed, internal): P1-protocol nonentailment —
  matched past records do not fix future lifetime in this comparison class.
- **Retracted:** "completeness is not a predictive or observable property"
  (predecessor §2.5). That was an all-protocol claim; P2 distinguishes the
  models. The corrected statement: *completeness has no retrodictive content
  from matched past records in this class; whatever content it has is
  predictive and in-time.*
- B′1–B′2 are established (as mathematics and as representation); B′3 does
  not follow from them (that is the P1 nonentailment); B′3 is not circular as
  stated but is a further philosophical commitment whose rival rejection —
  C&R's later-grounding (ch. 7, (GR) p. 110: present truth, later grounds)
  and Arageorgis's completion-parasitism (the covariant CSG probability
  space lives on completed causal sets) — are principled, source-faithful
  rejections that grant all of B′1–B′2.

## 5. Bridge C′: anchoring as a methodological constraint, with its exact scope

### 5.1 The constraint (proposal, not a selector)

Given a named physical category and an agreed explanandum, an ontological
reading is *anchored* iff its distinctive structure is (i) definable from or
invariant under the accepted structure of that category, or (ii) empirically
manifested, or (iii) independently defended as primitive with an explanatory
role rivals cannot replicate without changing an independently motivated
commitment. Applied symmetrically to all readings, it yields a *cost
classification*, never a winner: "A symmetric anchoring requirement is a
proposed methodological constraint, not a selection theorem."

Independent justification of the constraint as a norm (defeasible): it is the
 operative norm on which the Putnam → Stein → Malament → Wüthrich–Callender
progression actually converged — the participants dispute its application,
not its standing; and it blocks special pleading by binding the eternalist's
blanket concretization as tightly as the rival's additions
([ROLE_OF_EXISTENCE](../../coordinator/ROLE_OF_EXISTENCE.md) correction, §1).
Its limitation: it presumes that unearned primitives are costly, which a
primitive-fact theorist denies (defeat condition 3 below).

### 5.2 The definability corpus at its exact scope

- Stein 1991 (print-audited, pp. 148–150): the only non-trivial invariant
  definiteness relation satisfying the stated conditions in Minkowski
  spacetime is the causal past.
- Malament 1977 (*Noûs* 11(3), 293–300, DOI 10.2307/2214766; metadata
  confirmed this session via Crossref; abstract known from the predecessor
  record at abstract depth; full text **not** read this session): standard
  simultaneity is uniquely definable from causal connectibility — for
  equivalence-type simultaneity relations, within his scope conditions.
  **Scope caveat (new this session):** the step from this definability result
  to "simultaneity is non-conventional" is disputed in the primary
  literature — Rynasiewicz 2001 (PhilSci-Archive 293; this session read
  abstract + opening section) examines concrete alternatives and calls the
  inference into question; Sarkar & Stachel 1999 (*Philosophy of Science*
  66(2), 208–220, DOI 10.1086/392684; metadata only) directly contest what
  Malament proved. Definability filters candidates within a structure; it
  does not by itself settle interpretive questions.
- Wüthrich–Callender arXiv:1502.00018v1 §§1–4 (predecessor read; journal
  version DOI 10.1093/bjps/axv040 not collated): the invariance/explanatory
  dilemma, and the category-relativity of Stein analogues (their Figure-1
  counterexample causet).

### 5.3 Machine witnesses: category-relativity even at 3–4 elements

The finite witnesses in [§7](#7-machine-checked-finite-witnesses) give the
premise table that distinguishes the rival readings on representational
labels:

- **W1 (3-chain).** Shared constraints A1–A4: **6** admissible families,
  including both `E_all` and `E_past`. Adding UNIV: exactly 1 (E_all). Adding
  DOWN+FUTEX: exactly 1 (E_past). Each selector is coextensive with its
  conclusion under the constraints — the precise sense in which selecting by
  that selector alone is selection by fiat.
- **W2 (2-antichain, two standpoints).** Invariance A1 excludes the
  privileged-standpoint family (the finite surrogate of "no privileged
  observers") but leaves 2 invariant families. A1 does real work; it does not
  select an ontology.
- **W3 (4-diamond, co-present incomparables).** A1–A4 + DOWN + FUTEX +
  **TRANS** admit **both** the causal-past family and the bow-tie analogue
  (elsewhere included). Transitivity does no filtering work here: on
  categories with co-present incomparables, adding transitivity would not
  defeat the bow-tie rival.
- **W4 (chain + isolated point).** Same constraint set admits both families;
  here the *uniform* bow-tie analogue violates TRANS and is filtered. But a
  partial-elsewhere hybrid survives TRANS even here. **Whether transitivity
  filters the bow-tie reading is category-relative** — the finite analogue of
  the Wüthrich–Callender Figure-1 lesson, and a warning against any
  category-independent "transitivity defeats C&R" claim.

### 5.4 Charitable rival rejections (retained from the predecessor, verdicts unchanged in kind, sharpened in scope)

Primitivist (Maudlin, via Pooley fn. 6 — secondary): C′ reclassifies rather
than eliminates. Deflationist (Dieks): accepted as type-(ii) becoming; the
explanatory-sufficiency dispute survives inside the constraint. FLRW
foliation: anchoring is category-relative; the extra identification of the
distinguished foliation with concrete existence remains to be defended. CSG
growth: dynamics-internal but completion-parasitic (Arageorgis 2016,
conclusion). Moving spotlight / primitive tense: legitimate defense route
under clause (iii); whether experience supplies the role is the open burden
([ROLE_OF_EXISTENCE §8](../../coordinator/ROLE_OF_EXISTENCE.md)).

### 5.5 Repaired verdict (C′)

Both strong directions fail (physics forbids becoming / physics contains no
becoming): the first via Stein-type definable indexed becoming, the second via
the category mistake plus the legitimate primitivist route. What survives is
the two-sided conditional constraint of §5.1 plus the exact scope results of
§5.2–§5.3. It classifies; it does not select.

## 6. The one best positive route: standpoint-indexed supervenience (the Stein route)

**Selected route (proposal for review — selects no project ontology).**
Within a named smooth relativistic category with no distinguished foliation,
defend:

> For each standpoint `b`, the concrete realm is `E(b) = J⁻(b)`; existence is
> standpoint-indexed; there is no absolute concrete inventory. The existence
> predicate is determinate, invariant, and anchored in the accepted causal
> structure.

### 6.1 Independent justification (each step philosophical; physics only constrains)

1. **Invariance (A′1).** Existence attributions must be automorphism-invariant
   (§3, W2: this premise does real filtering work and both rivals accept it).
2. **Determinacy (A′2).** The predicate has a determinate extension per
   standpoint.
3. **Anchoring preference (C′ constraint).** Among determinate invariant
   assignments, prefer one definable from accepted structure at no added
   physical cost. In SR, Stein's theorem (print-audited) identifies exactly
   one non-trivial candidate: `J⁻(b)`.
4. **Explanatory tie-break (the genuinely positive premise).** The
   concrete-from-`b` realm is the region that can bear records of, and grounds
   for, present facts at `b`. Two defensible data favor the causal cut over
   its rivals: the reality of the past (a pure present-analogue `E(b) = {b}`
   loses it), and the record asymmetry (present records bear on the past, never
   on the future). The bow-tie rival must say why *coexistence*, rather than
   record-bearing, grounds concreteness for otherwise cut-off elsewhere
   events; the eternalist must say what the blanket inclusion of the future
   explains that the record-bearing realm does not.

This route retains a substantive noncircular premise the predecessor deferred:
the explanatory tie-break in step 4, stated and defended rather than dismissed.

### 6.2 Explicit defeaters (what rival explanations would defeat it)

1. **Determination-outruns-past (exact, project-internal reviewed).** A rival
   who adds the grounding premise "concrete-from-b ⊇ whatever determines
   present physical facts at b" defeats the causal cut wherever determination
   uses the whole model: on the coordinator-reviewed closed-dust mass
   classification, `F_m(b) = M` for `π ≤ τ < 2π` (all smooth real conformally
   coupled scalar solutions, every physical `m > 0`;
   [REVIEW_STATUS](../../../horizons/mass-classification/REVIEW_STATUS.md),
   accepted research scope, not externally refereed), the determining realm is
   the entire manifold, so that rival forces `E(b) = M` there. The route
   survives only if the record-bearing tie-break (step 4) is preferred to the
   determination tie-break — that preference is the exact live dispute, not
   something this lane settles.
2. **Coexistence/bow-tie.** If incoming-radiation or coexistence explanations
   require the elsewhere to be concrete, the causal cut is arbitrary; C&R's
   intransitive being (ch. 9 pp. 154–156) is the coherent fallback. W3 shows
   the route's defender cannot answer by TRANS alone: on co-present
   incomparables, transitivity filters nothing.
3. **Experience/growth.** If an independently characterized feature of
   temporal experience is shown — with the explanatory link established, not
   asserted — to require global growth, the indexed view pays the "thin and
   yawn-inducing" cost (Earman's verdict via Pooley §II, secondary).
4. **Non-indexed collapse.** If standpoint-indexed existence cannot be stated
   without collapsing into absolute existence (e.g., if assessment-relative
   semantics of the MacFarlane type proved unstateable — his preprint's
   status per ROLE_OF_EXISTENCE §9), the route fails wholesale.

Empirical equivalence: the route is defended as compatible with all shared
predictions; no discriminator between it and the rivals is claimed, consistent
with the ledger row "Physics here selects eternalism, GBT or fragmentalism —
Not established"
([CLAIM_STATUS](../../../CLAIM_STATUS.md), row inspected this session).

## 7. Machine-checked finite witnesses

Program: [checks/expansion_enum.py](checks/expansion_enum.py). Standard
library only; reduct sizes ≤ 4 elements; full enumeration ≤ 2^(4·4) = 65 536
candidate families per reduct; **0.72 s total** on this machine (bounds: 10 s
per check, 15 s hard timeout, 30 s total — met with margin). All labels are
representational; no witness treats a model domain as concrete (enforced by
the docstring and the code's structure: only predicates on labels are
computed).

Verification command and result:

```sh
python3 checks/expansion_enum.py
# All checks passed in 0.724 s (bound: 10 s per check / 30 s total).
```

Outputs (verbatim summaries):

- W1: shared {A1..A4} families on the 3-chain: **6**, including all@all and
  past@past; +UNIV → 1 (E_all); +DOWN+FUTEX → 1 (E_past).
- W2: privileged family {E(x)={x}, E(y)={x,y}} excluded by A1; 2 invariant
  families remain ({x}/{y} and all/all).
- W3: on the 4-diamond, {A1..A4, DOWN, FUTEX, TRANS} = 2 families: causal-past
  and bow-tie; transitivity separates nothing.
- W4: on chain+isolated, {A1..A4, DOWN, FUTEX} = 9 families; +TRANS = 8: the
  uniform bow-tie analogue is filtered, a partial-elsewhere hybrid survives.
- W5: protocol surrogate — matched records ≤ cutoff: identical; lifetimes
  differ (4 vs 6); post-cutoff records differ ([4] vs [4,5,6]).

## 8. The four-way separation (enforced throughout)

| Category | What it is | Where it appears here | What it is not |
|---|---|---|---|
| Empirical access | Observer records under a named protocol and comparison class (P1/P2; W5) | §4.2 | Not ontology: access asymmetries fix no existence assignment without a further premise |
| Dynamical determination | Well-posed IVP, unique maximal development, determining realms F_m (B′1; sharpness example; mass sidecar) | §4, §6.2 | Not existence, not grounding: "determines the reading at b" ≠ "is concrete from b" |
| Ontological supervenience | SU/UNIQ over the explicit expansion class (§1.4; W1) | §§1, 3 | Not a physical theorem; not refuted by assignment-pluralism (§1.5) |
| Grounding | Truth-at-b and its grounds, possibly later (C&R (GR); the tie-break in §6.1 step 4) | §§4.3, 6 | Not access, not determination: later-grounded truth is a distinct base; no present-ground demand may be smuggled in ([POINT_OF_DISAGREEMENT](../../../future-truth-rivals/coordinator/POINT_OF_DISAGREEMENT.md)) |

## 9. What would change each verdict

- **§1 framework:** a proof that some independently motivated constraint set
  forces UNIQ without embedding an existence conclusion would turn the gap
  into a theorem; none is known and W1 shows the obvious candidates fail.
- **A′:** a neutral constraint set accepted by every rival that forces a
  unique E would revive a selection version of A′. W2's lesson is that such
  premises must bind beyond invariance.
- **B′:** a physically admissible, essentially nonmaximal standard-model class
  (extendibility carrying predictive content that maximality lacks) would
  weaken B′2 as representation; conversely, an in-time falsification of all
  clipped completions in a real observational setting would give B′3 its
  first non-abductive support. Neither is known here.
- **C′ / route:** the four defeaters of §6.2; additionally, a demonstrated
  physical discriminator between any two anchored readings would change
  everything (none is known; ledger row cited in §6).

## 10. Source and depth summary

Full records: [sources.jsonl](sources.jsonl). Fresh this session (search +
fetch, stated depths): Kim 1984/1987 (Crossref metadata, discovery), Malament
1977 (Crossref metadata, discovery), Rynasiewicz 2001 (abstract + opening
section via exa fetch), Sarkar–Stachel 1999 (Crossref metadata, discovery).
Reused at the predecessor lane's recorded depths and marked as project
records (not re-read): Putnam 1967 (full-text), Stein 1991 (print audit
pp. 148–150), Wüthrich–Callender v1 §§1–4, Pooley 2013 preprint, Arageorgis
2016, C&R chapter extraction, Brading 2013 project record, Dieks 2005
(abstract), Rideout–Sorkin 2000 (abstract). Project-internal documents read in
full this session: coordinator review, run plan, ROADMAP,
PREMISE_STRESS_TEST, ROLE_OF_EXISTENCE, EXPLANATORY_ROLE_TEST,
POINT_OF_DISAGREEMENT, COMMON_EXTENSION_REPAIR, REPAIR_RESULT, mass-
classification REVIEW_STATUS, CURRENT_SYNTHESIS, CLAIM_STATUS (cited row),
predecessor RESULT.md and sources.jsonl. Quotations from Skow, Earman,
Maudlin, Dieks 2006 remain secondary (via Pooley/Arageorgis), as in the
predecessor register.
