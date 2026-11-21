# Adversarial audit of three ontology-selecting bridge premises

29 October 2026. Lane: `ontology-bridge-premises` (independent; isolated worktree).
This is a worker submission for coordinator review. It contains no accepted
theorem, no novelty claim, and no project ontology verdict. Comparison contract
follows the [ROADMAP](../ROADMAP.md) model contract: a physical model
`P = (M, g_ab, fields, laws)` with marked standpoint(s) `b`, an ontological
expansion including an existence assignment `E(b,x) ⊆ M`, and explicit bridge
premises from `P` to `E`. The contract is a comparison instrument; nothing here
forces every rival into a point-subset ontology or reads existence off a model
domain.

## 0. Method, capability check, independence

- Search capability check: `scholar_search` **worked** (query "Malament causal
  theories of time and physical becoming", 29 Oct 2026; returned OpenAlex,
  arXiv, Crossref records). `serpapi_search` **failed**: "Your account has run
  out of searches." `web-search-prime` **not used** (quota exhausted until
  2026-11-17; not retried per brief). Primary pages were fetched with `exa`
  (`web_fetch_exa`) and inspected directly.
- Small query batches + citation chasing only. Every result used below was
  fetched at a stated depth; unknown locators are recorded as unknown.
- Independence: this lane assumes no conclusion of the other three new
  ontology workers. The two rejected batch-2 technical submissions
  ([BATCH2_INITIAL_REVIEW](../../lawful-completions/coordinator/BATCH2_INITIAL_REVIEW.md))
  are not relied on: neither the claimed finite-cone continuity closure nor the
  scalar geometric objection is used anywhere below.
- Project-internal results are cited at their recorded status: *reviewed*
  (internal research review, not external refereeing), *accepted sidecar*, or
  *proposal*. Lane records reused at their recorded depth (e.g. C&R chapter
  extraction, Stein print audit, Brading full text); these are marked "project
  record" in `sources.jsonl`.

## 1. Bridge A: physical supervenience of concrete existence

**Proposed bridge.** The inventory of concrete existence supervenes on the
physical, and the physical — in a relativistic world — is the tenseless
manifold plus fields; therefore all events of the actual manifold are real.

- **A1 (physics).** Special relativity holds: no observer-independent
  simultaneity structure exists beyond the metric; physical relations are
  coordinate-independent and tenselessly definable.
- **A2 (supervenience).** There cannot be two worlds agreeing in all physical
  facts while differing in which events are concretely real.
- **A3 (no privileged observers).** If all and only the things standing in a
  physical relation R to me-now are real, and you-now are also real, then all
  and only the things standing in R to you-now are real (R physical,
  coordinate-independent, tenselessly definable, non-accidental).
- **A4 (closure).** R's transitive closure applied across "enough observers"
  (all physical systems, any admissible frame) reaches every event.
- **AC (conclusion).** Every event of the actual manifold is real; the concrete
  inventory is the tenseless four-manifold (eternalism).

### 1.1 Strongest primary defense

Hilary Putnam, "Time and Physical Geometry", *Journal of Philosophy* 64(8)
(27 Apr. 1967), 240–247 (full text read; JSTOR-scan copy, weebly mirror).
Argument as printed:

- Opens with the "man on the street's" view: "(1) All (and only) things that
  exist now are real" (p. 240), with assumptions **i** ("I-now am real"),
  **ii** (another observer in relative motion is real), and **III** "There Are
  No Privileged Observers" (pp. 240–241), the latter stated tenselessly over
  "all things past, present, and future", with R restricted to physical,
  coordinate-independent, tenselessly definable relations.
- p. 243: with (2) "All things that exist now are real" plus Lorentz
  invariance of the laws, "the relation R must also hold between all the
  events on some one 'simultaneity-line' in any observer's coordinate system
  and that observer-at-the-appropriate-time"; transitivity then makes a
  future-for-me event X (present-for-you) real for me.
- p. 246 ("Morals and Conclusions"): "every thing and event in space-time
  bears the transitive closure of the above relation R to me, at least if
  there are enough observers" — all future and past things are real.
- Second argument (pp. 244–246): if future contingents lack truth values
  (Aristotle), then "Absolutely Future / Absolutely Present /
  Absolutely Simultaneous" become *definable* physical relations, contradicting
  relativity; the truth-for-me/truth-for-you escape is shown contradictory
  (footnote 1, pp. 244–245). Putnam's own summary: "Aristotle was wrong. At
  least he was wrong if Relativity is right" (p. 244).

This is the strongest primary defense because it derives the ontological
conclusion from explicitly physical premises (Lorentz invariance, definability,
transitivity, observer symmetry) without invoking parsimony or the model domain
as such.

### 1.2 Charitable rival rejection

- **Stein's rejection (strongest).** Howard Stein, "On Relativity Theory and
  Openness of the Future", *Philosophy of Science* 58(2) (1991), 147–167, DOI
  10.1086/289609. Project print audit
  ([PRINTED_VERIFICATION](../../../knowledge/audits/stein-printed-pages/PRINTED_VERIFICATION.md),
  pp. 148–150, JSTOR scan, SHA-256 recorded): the theorem on **p. 149** shows
  that a reflexive, transitive, time-orientation-preserving-automorphism
  invariant relation R holding of a past-pointing pair coincides with the
  past-pointing (causal) relation — subject to the prose-supplied conditions
  the display omits: non-universality (iv) and causal-past inclusion (timelike
  *or null*). The audit also gives an explicit countermodel (reflexive
  chronological-past relation) showing the display alone is insufficient.
  Applied to Putnam: A3–A4 do not force R to be slice-like; with
  R = "in the causal past of", you-now ∈ J⁻(me-now) implies
  J⁻(you-now) ⊆ J⁻(me-now), so III is satisfied and no future event becomes
  real. Stein's own moral (quoted in Pooley 2013 preprint, §X, from Stein 1991
  p. 164): "special relativity is perfectly compatible (in general) with
  'ontological probabilism'". So the same physics licenses standpoint-relative
  becoming; the argument selects nothing without a further premise that R must
  be transitive **and** slice-like.
- **Later-grounded bivalent rival.** Correia & Rosenkranz, *Nothing To Come*
  (project full-text extraction
  [CLAUSES.md](../../future-truth-rival-chapters/CLAUSES.md): ch. 7 pp. 99–116,
  ch. 9 pp. 135–161 read; appendices not read): their grounding requirement
  (GR) (p. 110) permits "a statement about the future be true now whose present
  truth is sometimes in the future explained by what exists then, while there
  exists now nothing that would explain its present truth". Putnam's argument
  never touches the distinction between being real and being true; A2's
  "physical facts" can be granted tenselessly while existence remains
  stage-restricted (their ch. 9 fourfold structure, p. 135, includes a bow-tie
  existence option (BO) on the same structure the eternalist uses).
- **System-relative rival.** Brading 2013 (project full text,
  [brading-existence/RESULT.md](../../brading-existence/RESULT.md), pp.
  1101–1111): P1* assigns each thing the present of its own dynamical system;
  the union of local presents can cover the history, so no event is excluded.
  Relativized existence satisfies the physics without AC.

### 1.3 Circularity test

A2 cannot be stated neutrally. If the supervenience base is "all physical
facts", enumerated tenselessly, it already includes the future events whose
existence is in question: A2 presumes the eternalist inventory. If the base is
"the present physical state", A2 presumes presentism. The neutral reading
("existence differences require physical differences") is satisfied by any
definable assignment, including E(b,x) = [x ∈ J⁻(b)] and the bow-tie, and so
does no selecting. The brief's standard is met exactly: a definition that
already assumes an ontology cannot establish it.

### 1.4 Symmetry test (same demand on eternalism)

Eternalism's own reading — every represented event of the model is concrete —
is an interpretation of the formalism, not an entailment of it
([ROLE_OF_EXISTENCE](../coordinator/ROLE_OF_EXISTENCE.md) correction, §1:
"treating every actual-history representation as concrete is itself a realist
commitment"). Supervenience is satisfied by every candidate assignment; the
demand that binds the growing block (no existence difference without physical
difference) binds eternalism equally at the level of *which reading of the same
manifold is correct*.

### 1.5 Countermodel

[PREMISE_STRESS_TEST](../coordinator/PREMISE_STRESS_TEST.md) §1 (internal,
elementary, inspectable): on time-oriented globally hyperbolic M with marked b,
both `E_all(M,b) = M` and `E_past(M,b) = J⁻(b)` are invariant under
time-orientation-preserving isometries, contain b, are monotone in b, and
satisfy the restriction equality `E(U,b) = U ∩ E(M,b)` for causally convex open
embeddings (for E_past, by causal convexity). Covariance, persistence,
self-inclusion, closedness and restriction compatibility thus do not separate
the two simplest rivals; excluding E_all requires adding nonuniversality or
future exclusion — i.e., putting the conclusion into the premises. A second
countermodel: same-causal-past lawful solutions with different future readings
([PHILOSOPHICAL_SCOPE](../../lawful-completions/coordinator/PHILOSOPHICAL_SCOPE.md))
show that even the "accessible physical base" is not fixed without choosing an
ontology for the elsewhere.

### 1.6 Verdict (A)

**Strong form fails.** A1–A4 yield at most: no invariant slice-like R exists in
SR — a constraint on candidate *relations* (cf. Malament's definability
result below), not a proof that the concrete is the whole manifold. The
supervenience premise is circular as a selector; the no-privileged-observers
premise is satisfiable by standpoint-relative becoming. **Weak surviving core:**
existence assignments must be anchored in physical and observer structure
(standpoint-indexed supervenience). This core is shared by all defensible
rivals and has no selection power by itself.

## 2. Bridge B: completeness / constitution

**Proposed bridge.** The concrete totality is constituted by all events of the
maximal actual solution of the laws; hence a physically complete world already
contains its future as concrete, and lawful production of future events is
constitution by one reality rather than mere prediction.

- **B1 (physics).** The initial-value problem is well posed: appropriate Cauchy
  data admit a unique maximal development; physical completeness of a world is
  being an inextendible solution of the laws.
- **B2 (theory).** The best theory's model of the actual world quantifies over
  every event of the manifold and treats the whole solution as the world
  (B-theoretic "exhaustive catalogue" completeness).
- **B3 (constitution).** The concrete existing totality *is constituted by* the
  events of that maximal actual solution — not merely fixed dynamically by
  earlier stages of it.
- **BC (conclusion).** Future events of the actual solution are concrete;
  dynamical sufficiency of the future from earlier data is constitution by one
  complete reality, not mere prediction of what will exist.

### 2.1 Strongest primary defense

- **Theory-side.** Oliver Pooley, "Relativity, the Open Future, and the Passage
  of Time", *Proceedings of the the Aristotelian Society* 113(3) (2013)
  (preprint read; published version not collated), §II: the B theory is
  characterized by answering **yes** to "Is an exhaustive catalogue of which
  events occur, and how they are temporally related, a complete account of
  temporal reality?" — with the tenseless description "holding once and for
  all, from no temporal point of view". This is the cleanest statement of the
  completeness claim the constitution bridge needs: the tenseless catalogue is
  *all of temporal reality*, and everything in it is concrete in the same
  sense.
- **Physics-side.** Maximality is the accepted home of the deterministic
  initial-value problem in GR; project reviewed results explicitly rest on the
  ordinary common-GHD extension theorem for smooth vacuum data
  ([REPAIR_RESULT](../../lawful-completions/coordinator/REPAIR_RESULT.md),
  citing Sbierski arXiv:1309.7591v3 Theorem 2.7). On the growing-block side,
  Earman 2008 is quoted (Arageorgis 2016, p. 37, full text read) speculating
  that causal-set growth "promises to transmute Becoming from a piece of
  speculative metaphysics to one of naturalized metaphysics" (Earman 2008,
  159) — a programme-level bet that the dynamics itself constitutes the
  growing concrete realm.
- **Distinction honored.** The bridge is explicitly *not* the claim that
  present data dynamically produce the future. Project reviewed results show
  exactly how the two come apart: equality of causal-potential realms fixes
  common-duration geometric readings under ordinary common-development
  uniqueness (REPAIR_RESULT; CLAIM_STATUS row "Equal potential realms fix
  common-duration geometric readings | Reviewed vacuum repair") without
  settling that the fixed events exist ("One cannot infer that … the future
  exists", REPAIR_RESULT §Philosophical consequence).

### 2.2 Charitable rival rejection

- **Later-grounded bivalent rival (strongest).** C&R (project extraction,
  ch. 7): truth of a future contingent is compatible with "there exists now
  nothing that would explain its present truth" (p. 110); openness is defined
  via (IND_ex) of grades (II′)/(III′) — possible failure of later times to
  exist or to contain entities — and is "perfectly compatible with the
  bivalence of all future-tensed statements" (p. 116). For this rival the
  completed model is a *representation* whose complete domain is not a concrete
  inventory; B3 is simply denied while all physics is granted. (Status: the
  authors' position, per the project's chapter/reply audit; ch. 7's own
  grounding of generalizations is conceded "a problem for everyone", p. 111
  n. 5.)
- **The completion-parasitism argument.** Arageorgis 2016 (full text read;
  *Belgrade Philosophical Annual* XXIX, DOI 10.5937/bpa1629033a, Conclusion):
  CSG dynamics "cannot be defined with mathematical consistency but in the
  limit of infinite time 'when' causal set growth 'has reached
  completion'… this makes the growing block imagery the CSP aspires to flesh
  out within physics parasitic on a block universe view". Mathematical
  completeness of the representation (the probability space over completed
  causal sets) is forced by the formalism and cannot be read back as
  ontological completeness of a growing world.
- **Model class relativity.** The project's sharpness example
  ([COMMON_EXTENSION_REPAIR](../../lawful-completions/coordinator/COMMON_EXTENSION_REPAIR.md),
  "Sharpness example", reviewed): M₁ = Minkowski minus J⁺(q) is smooth, vacuum,
  globally hyperbolic, and a nonmaximal GHD of *the same* earlier Cauchy data
  as full Minkowski M₂. Observable physics on the common region is identical;
  whether "the world" contains the events beyond q's future is not fixed by
  any data or by B1's uniqueness (both are admissible developments).
- **Brading's universe case.** Brading 2013 p. 1109 (project full text): if the
  only genuine system is the entire universe, "this version of presentism is
  defeated and the block universe triumphs" — but the project's universe-case
  work ([brading-universe-frontier/IDEAS.md](../../brading-universe-frontier/IDEAS.md),
  full-text reads of Wüthrich 2010, Monton 2005, Isham 1991 pp. 192–202,
  Thiemann 2006, Bamonti–Thébault 2025) shows the dilemma is real on both
  sides: at the totality the physics (Hamiltonian constraint, clock choice)
  does not hand either rival a free completeness-of-existence result. The
  completeness bridge cannot be won at the universe scale by pointing at the
  model.

### 2.3 Circularity test

"Maximal **actual** solution" contains the contested word. Inextendibility is
relative to an admissible solution class (the clipped spacetime is extendible
in the larger class; a development maximal in one category need not be in
another), and which class counts as "physical" is fixed using exactly the
ontological intuitions the bridge was supposed to settle. B2 also inherits the
eternalist reading: "the theory's model of the actual world" is the completed
manifold only if the model's domain is read as concrete inventory — the point
the model contract forbids assuming ([ROADMAP](../ROADMAP.md), Required checks
1: "Eternalism is not inferred from the domain of a spacetime model").

### 2.4 Symmetry test (same demand on eternalism)

Eternalism must justify the step from "the model contains all events" to "the
model's events are concrete", by the same abductive standard applied to the
rival's realm choices. [EXPLANATORY_ROLE_TEST](../coordinator/EXPLANATORY_ROLE_TEST.md)
(§1 correction, §6) makes this explicit: the directness of treating all actual
occurrences as concrete is a characterization, not a justification; calling
view A's domain "reality" and view B's a "representation" is not an argument
unless an explanatory difference is demonstrated. Parsimony alone is excluded
by the brief and by ROLE_OF_EXISTENCE §2 (no numerical measure of theoretical
cost has been supplied; none should be invented).

### 2.5 Countermodel

The clipped-Minkowski pair (§2.2, project reviewed) is a direct countermodel to
B3-as-entailment: same initial data, same laws, same local physics and common
readings up to any duration both define; two admissible solutions, one maximal,
one not. If constitution followed from physical completeness, exactly one of
the two could be "the concrete world", but nothing observable distinguishes
them — completeness is not a predictive or observable property. A second
countermodel at the level of *realms*: on a complete conformal cylinder with
finite duration L and diam(S) > L, the historical potential realm is a proper
subset of the bow tie at every standpoint (project reviewed cylinder
classification, [CLAIM_STATUS](../../CLAIM_STATUS.md) row; exact statement in
DIAMETER_CLASSIFICATION.md) — so even "the whole model" and "what is fixed for
a standpoint" come apart inside a single complete solution, and B3's
identification of constitution with the model domain loses its grip on
what grounds what.

### 2.6 Verdict (B)

**Fails as an ontological proof.** Dynamical sufficiency (well-posedness,
uniqueness, common-development agreement) is established mathematics; the
identification of the maximal solution's inventory with the concrete totality
is a further philosophical premise, circular if stated via "actual", and
rejected on principled grounds by the strongest rival. **Weak surviving core:**
the completed solution is the shared representational framework every rival
must interpret; bridge premises assign existence *on* it, they are not derived
from it. (C&R themselves encode their bow-tie view on the same completed
structure, ch. 9.)

## 3. Bridge C: objective becoming requires additional structure

**Proposed bridge (two-edged selector).** Whether objective becoming is
physically grounded depends on whether its structure is anchored in the
accepted physics; if not, it is an additional posit needing independent
defense — and symmetrically, no ontology (eternalism included) is read off the
formalism.

- **C1 (physics).** The accepted structure of a relativistic world is
  (M, g_ab, matter) with its causal order; in generic SR/GR solutions there is
  no physically distinguished global slice.
- **C2 (anchoring).** A candidate ontological relation or property is
  physically anchored iff it is definable from (or invariant under the
  automorphisms of) the accepted structure of the named comparison category,
  or empirically manifested, or defended as a primitive with an independent
  explanatory role rivals lack.
- **C3 (taxonomy).** Objective becoming is either (i) standpoint-relative and
  definable (Stein-type), (ii) constituted by event succession (deflationary),
  or (iii) an addition: preferred foliation, actuality property, growth
  dynamics, or primitive tensed facts.
- **C4 (norm).** Interpretive additions that are neither anchored nor
  independently explained are not warranted *by physics*; they may still be
  warranted metaphysically, at stated cost.
- **CC (conclusion).** Physics by itself supports only (i)-type or (ii)-type
  becoming; (iii)-type becoming is an extra posit; and, symmetrically, the
  eternalist's blanket concretization of the manifold is likewise an
  interpretation (definable but explanatorily unearned).

### 3.1 Strongest primary defense

- **Stein 1991** (print-verified theorem, p. 149, with the audit's contextual
  corrections): within Minkowski spacetime, the only non-trivial invariant
  definiteness relation is the causal past. Becoming of type (i) is *definable*
  from accepted structure — no addition. Corollary: any slice-like or global
  becoming structure is not definable from the metric-causal structure of SR;
  as a physical anchor it would be an addition.
- **Malament 1977**, "Causal Theories of Time and the Conventionality of
  Simultaneity", *Noûs* 11(3) (Sept. 1977), 293–300, DOI 10.2307/2214766
  (abstract read; full text not read this session): "In a straightforward
  sense, the relative simultaneity relation of special relativity is uniquely
  definable from the causal connectibility relation" — standard simultaneity
  is the only nontrivial equivalence-type simultaneity relation invariant under
  causal automorphisms. There is no observer-independent slice-like present
  definable from SR causal structure; a preferred present is an addition in
  this category. (Wüthrich–Callender v1 p. 2 attribute to "Malament 1977" the
  related result that the causal ordering determines the geometry up to a
  conformal factor; I did not verify which 1977 paper carries that wording and
  leave the attribution at their paraphrase.)
- **The dilemma, made rigorous.** Wüthrich & Callender, "What becomes of a
  causal set", arXiv:1502.00018v1 (30 Jan. 2015; BJPS 2016, DOI
  10.1093/bjps/axv040); v1 pp. 1–13 read (§§1–4): "any identification of a
  present in special relativity either answers to the presentist's explanatory
  request or is compatible with the structure of Minkowski spacetime, but not
  both" (p. 5); invariant identifications (a point, the past light cone) are
  explanatorily thin ("the big bang counts, counterintuitively, as 'now'");
  explanatory identifications (a foliation) violate invariance. In causal-set
  kinematics the Stein analogue **fails** (their Figure-1 counterexample
  causet: a reflexive, transitive, automorphism-invariant, non-universal R may
  include spacelike "non-Hegelian" pairs), but the escape collapses: large
  non-Hegelian subsets require lattice-regular causets, which would violate
  Lorentz symmetry and are empirically constrained (pp. 8–9). "In sum, rather
  than escape the dilemma, it seems CST embraces it and even makes it
  rigorous" (p. 9).
- **The preferred-foliation route's cost.** Pooley 2013 (preprint, §VII): the
  three routes for passage + relativity are deflation, preferred global Nows,
  or no-global-Now non-standard views. On the preferred-now route: either the
  metric "systematically misrepresents" real distances (neo-Lorentzian), or a
  foliation is "simply superadd[ed]", in which case metric temporal distance
  "is no longer a measure of the passage of time" and co-occurring events sit
  at no temporal distance from earlier events — "the resulting view may not be
  incoherent, but it is very strange indeed" (§VII). This is a primary-source
  statement of C4's cost accounting for one whole family.
- **An attempted physical becoming.** Rideout & Sorkin, "A Classical Sequential
  Growth Dynamics for Causal Sets", *Phys. Rev. D* 61, 024002 (2000);
  arXiv:gr-qc/9904062 (abstract of v3, 2004, read): growth dynamics derived
  from causality conditions and discrete general covariance — becoming built
  into the dynamics rather than added to a completed structure (their quoted
  gloss: the process is "not… happening 'in time' but rather as 'constituting
  time'", as quoted in W–C v1 p. 11 and Arageorgis p. 40). This is the
  strongest case that a (iii)-type posit can be *internal* to physics; see
  3.2–3.3 for why it does not close the bridge.

### 3.2 Charitable rival rejection

- **Primitivist (Maudlin).** Becoming is not structure *in the model* at all;
  it is a fundamental feature of the world the model represents (Pooley 2013
  fn. 6: Maudlin is "a realist (and primitivist) about the passage of time";
  Pooley adds "I do not claim to understand Maudlin's view"). The "addition"
  charge then rests on assuming every real feature must be modelled structure.
  *Our response:* granted — and then C4 does not refute the view; it reclassifies
  it: becoming is not physics-supported but must be defended metaphysically,
  which is what the primitivist in any case claims. The bridge's honest output
  is the classification, not an elimination.
- **Deflationist (Dieks/Savitt).** Becoming = the successive happening of
  events; nothing is added (Dieks 2005 preprint abstract read: becoming "as
  something purely local"; his 2006 formulation quoted via Pooley §II and
  Arageorgis p. 51: "Becoming is just the successive happening of events along
  a timelike world line"). *Our response:* CC accepts (ii) as physically
  kosher; the live question is whether it answers the A-theorist's explanatory
  request — Pooley (§II) relays Earman's verdict that it is a "thin and
  yawn-inducing" sense of passage (Earman 2008, 159), and W–C's dilemma says
  the request and the invariance cannot both be satisfied. The dispute
  survives inside the bridge rather than being settled by it.
- **Foliation presentist in FLRW (project red-team lead).** In nearly-FLRW
  cosmologies the matter distribution (e.g. the CMB rest frame) defines a
  canonical foliation, so a shared now "may cost no *added* structure, only
  non-locality" ([redteam/SYNTHESIS](../../local-fragmentalism/redteam/SYNTHESIS.md)
  §D; lead-level provenance, not re-verified against primary GR texts in this
  session). *Our response:* correct and important: anchoring is
  category-relative. The bridge must name its comparison category (ROADMAP
  model contract) and then still owes a further premise: why does this
  physically distinguished foliation carry concrete existence rather than
  merely being a convenient frame? The red-team's own answer stands: what
  fails is not the physics but the extra identification.
- **Moving spotlight / primitive tense (Skow 2009; Cameron).** Primitive tense
  operators or an actuality property are the addition, defended via temporal
  experience (Skow's relativistic generalization uses "Minkowski
  superspacetime", reported and criticized in Pooley §IX; Skow's official
  story in primitive tense operators, quoted at Pooley §IV from Skow 2009
  pp. 666–675). *Our response:* this is a legitimate defense route under C2's
  third clause (independent explanatory role); whether experience actually
  supplies that role is the unresolved burden both
  [ROLE_OF_EXISTENCE](../coordinator/ROLE_OF_EXISTENCE.md) §8 and
  EXPLANATORY_ROLE_TEST §5 identify. The bridge cannot settle it; it can only
  locate it.
- **CSG defender (Dowker/Sorkin).** Growth is inside the dynamics, so nothing
  is "added". *Our response:* the W–C and Arageorgis results show the price:
  the covariant probability space lives on completed causal sets (growth
  parasitic on the block, Arageorgis Conclusion), the covariant σ-algebra of
  physically meaningful questions excludes labeling-facts (Arageorgis §3),
  and no physically significant proposition's truth supervenes on the
  already-become part in the growing-block sense (his condition [N], §4).
  So the CSG route relocates rather than removes the bridge premise.

### 3.3 Circularity test

"Additional structure" is relative to a prior identification of "accepted
physics". Causal-set theory builds growth into its dynamics, converting a
(iii)-type posit into a (i)-type definable relation within its own category;
conversely, declaring the standard formalism "complete without becoming"
already encodes the B-theoretic reading. The bridge is therefore sound only as
a *conditional on a named physical category* — which the ROADMAP model contract
in any case requires. Stated category-relative, the circularity is contained:
within a fixed category, definability and invariance are mathematics, and the
cost accounting (W–C dilemma, Pooley's dilemma for preferred foliations) is
explicit.

### 3.4 Symmetry test (same demand on eternalism)

The eternalist's existence assignment E_all(b) = M is definable and invariant —
it passes C2's anchoring clause at zero physical cost. But C2/C4 apply to
interpretations, not only to additions: reading *all* model events as concrete
is an interpretation (ROLE_OF_EXISTENCE correction), and the eternalist owes
the same explanatory accounting: what does the blanket concretization explain
that standpoint-relative assignments cannot? Under the coordinator's
explanatory-role test (§5, rows "Future truth", "Passage/experience") nothing
so far established — completion results, screening, common-extension agreement
— does that explanatory work for the eternalist. Symmetrically, nothing does it
for the growing block or fragmentalist either; the ledger records exactly this
([CLAIM_STATUS](../../CLAIM_STATUS.md): "Physics here selects eternalism, GBT
or fragmentalism | Not established").

### 3.5 Countermodels

1. **Minkowski + Stein relation:** objective (standpoint-indexed) becoming with
   no additional physical structure — refutes the strong reading "objective
   becoming requires additional physical structure" (only *global or slice-like*
   becoming requires addition).
2. **CMB/FLRW foliation:** a physically distinguished global foliation with no
   new fields — refutes generalizing Malament-style definability to "no
   privileged present anywhere"; anchoring is category-relative.
3. **Moving spotlight:** an empirically idle primitive actuality property —
   refutes the verificationist supplement "whatever is real makes an empirical
   difference"; empirical idleness is a cost to be argued, not an impossibility
   proof.
4. **W–C counterexample causet (Figure 1):** Stein's theorem analogue fails on
   discrete kinematics; invariant non-causal definiteness relations exist.
   Definability results are theorems about a structure, not metaphysical
   necessities; the anchoring clause must be proven per category, not presumed.

### 3.6 Verdict (C)

**Both strong directions fail.** "Physics forbids objective becoming"
(Putnam/Rietdijk-style) fails via Stein-type definable becoming; "physics
contains no becoming and therefore none is real" fails via the category
mistake (physics does not entail any existence reading) and via the legitimate
primitivist route. What survives is a **two-sided conditional selector**: the
anchoring requirement C2+C4, applied symmetrically to every ontological reading
of a named physical category. It yields a classification of rivals by what
their existence assignments cost, not a winner.

## 4. Enforced distinctions

| Distinction | Established content (status) | What it is not |
|---|---|---|
| Dynamical sufficiency vs constitution | Equality of causal-potential realms fixes common-duration geometric readings under ordinary common-GHD extension (project reviewed; REPAIR_RESULT) | Not: the fixed future events thereby exist, or are *constituted by* the past realm |
| Prediction vs existence | Same-causal-past solutions with different futures; nonfactorization from (past, mass) data (project conditional/conditional-not-accepted; PHILOSOPHICAL_SCOPE) | Not: indeterminism, branching, or non-existence of the future |
| Model domain vs concrete inventory | E_all and E_past both covariant, persistent, restriction-compatible (PREMISE_STRESS_TEST §1); "Eternalism is not inferred from the domain of a spacetime model" (ROADMAP check 1) | Not: any reading of the manifold is forced by the formalism |
| Representation completeness vs ontological completeness | CSG probability space defined only on completed causal sets (Arageorgis 2016, reviewed here at full-text depth) | Not: the growing world therefore *is* completed, or eternalism true |
| Empirical equivalence vs identity of ontology | All rivals share all predictions in the audited categories; no discriminator without an independently defended exclusivity premise (CURRENT_SYNTHESIS §2) | Not: the ontologies are identical, nor that the question is verbal |

## 5. Selection: the one bridge worth defending

All three strong bridges fail their selection purpose. The one worth defending
is the **weakened, symmetric form of Bridge C: the anchoring requirement** —

> Given a named physical category and an agreed explanandum, an ontological
> reading of the models (existence assignment, becoming structure, or their
> denial) is warranted by physics only if its distinctive structure is anchored:
> definable from or invariant under the accepted structure of that category,
> empirically manifested, or independently defended as primitive with an
> explanatory role that rival readings cannot replicate without changing an
> independently motivated commitment.

**Why this one.** Bridge A's supervenience and Bridge B's constitution are
circular in exactly the place the anchoring requirement makes explicit (which
physical structure counts, and which reading of it counts as concrete). Bridge
C's dilemma-version is the only one of the three whose strongest defenses and
strongest rejections (Stein, Malament, Wüthrich–Callender, Pooley) *agree* on
the operative norm while disputing its application — which is what a defensible
bridge premise should look like. It is a classification instrument, not an
ontological proof; within a category it sorts readings by what their structure
costs.

**What it yields here (proposed classification, not a verdict).** Within smooth
relativistic categories with no distinguished foliation: eternalism's E_all and
Stein-type local becoming are anchored (definable) at zero physical cost;
C&R's bow-tie is anchored within their fourfold structure (ch. 9 uses only the
fourfold division, p. 135); preferred-foliation presentism is anchored only in
categories with a distinguished foliation (FLRW-like) and an addition
otherwise, with the costs Pooley details; moving-spotlight actuality and
Tooley-style primitive tensed facts are additions whose defense must come from
experience or grounding theory, not physics; CSG becoming is dynamics-internal
but completion-parasitic in its covariant formulation. No assignment is
selected among the anchored ones; that is the honest outcome, consistent with
the ledger's "not established".

**What could defeat it.**

1. **An explanandum only an unanchored addition explains.** If a precisely
   characterized feature of temporal experience (or of grounding) is shown to
   require, e.g., primitive actuality — with the explanatory link established,
   not asserted — the third clause of C2 admits it and the "idle addition"
   charge lapses for that category. (Defeater already live: ROLE_OF_EXISTENCE
   §8; EXPLANATORY_ROLE_TEST §5 row 3.)
2. **An anchoring failure with an independently forced view.** Bell-type
   nonlocal dynamics (e.g. a Tumulka rGRWf-style event ontology with a
   nonlocal law and no foliation; red-team §D, lead-level) would show that
   well-motivated objective structure need be neither definable nor local; the
   requirement's first clause would then be too strong and must be weakened to
   "anchored or independently motivated".
3. **A proof that the requirement begs the question.** If primitive-fact
   theories (Tooley-style) are coherent and fundamental, then demanding
   definability in tenseless structure precisely assumes what they deny; the
   requirement would need independent justification as a methodological norm
   (which ROLE_OF_EXISTENCE §2 attempts for a different norm) or be abandoned
   as a mere prejudice.
4. **A category where the dilemma collapses.** W–C's CST kinematics shows
   Stein analogues are structure-dependent; a physically serious category in
   which an invariant, explanatory present exists would defeat the dilemma's
   generality (their non-Hegelian escape fails only via regularity→Lorentz
   violation, an empirical premise).

**Relations to coordinator work (independence preserved).** The anchoring
requirement is not the coordinator's explanatory-role test: that test audits
*specific claimed advantages* by replacement; this audits the *anchoring of the
ontological structure itself* by definability, invariance, or earned
primitiveness, in the tradition of Stein's own constraints and Pooley's
"properly relativistic" requirement. The two are compatible and complementary;
the coordinator may reconcile or reject either. No novelty is claimed for the
norm; the contribution of this lane is the symmetric audit of all three bridges
and the explicit defeat conditions.

## 6. What would change each verdict

- **A:** A neutral, non-circular formulation of the supervenience base (one a
  C&R-style rival and a Stein-style rival both accept) that still excludes
  standpoint-relative assignments would revive A. Alternatively, a proof that
  no coherent standpoint-relative semantics exists (no known result suggests
  this; MacFarlane-style assessment semantics and fragmentalist programs point
  the other way).
- **B:** A physical criterion for worldhood that is observable or lawful —
  e.g. a uniqueness theorem for the *concrete* realm from the best theory's
  data — would connect B1 to B3 non-circularly. Conversely, an accepted
  physical theory whose standard models are essentially non-maximal (with
  extendibility carrying observable content) would undermine the maximality
  premise itself.
- **C:** See §5 defeat conditions 1–4. Additionally: an empirical
  discriminator between any two anchored readings would change everything —
  the ledger records that none is known.

## 7. Source and depth summary

Full records in `sources.jsonl` (schema per
[knowledge/README](../../../knowledge/README.md)). Primary full-text or
substantial-part reads this session: Putnam 1967; Wüthrich–Callender v1 §§1–4;
Pooley 2013 preprint §§II–X; Arageorgis 2016 (abstract, §§1–4, conclusion).
Abstract-level: Malament 1977; Dieks 2005; Rideout–Sorkin 2000 (v3 abstract).
Project records reused at recorded depth: Stein 1991 pp. 148–150 (print
audit); C&R chs. 7, 9 (chapter extraction); Brading 2013 pp. 1101–1111;
brading-universe-frontier full-text reads. Quotations from Skow 2009, Earman
2008, Maudlin 2007, Dieks 2006, Sorkin 2007, Dowker 2005/2014 and Belnap 1992
are taken via the Pooley/Arageorgis/W–C texts and marked as secondary; those
works were not independently read this session and their locators are recorded
as unknown where unverified. serpapi unavailable; web-search-prime not used.
