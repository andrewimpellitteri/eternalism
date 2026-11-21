# CLAIM_MAP: what the covariance theorem does and does not say about locality and becoming

Task `stein-interpretation-audit`, 27 October 2026. Claim map only; the
manuscript was not edited. This submission goes to coordinator review; it is
not an accepted verdict.

## 0. Source pins

- Worktree: `agent/stein-interpretation-audit`, HEAD `e30a37294c8fabf0a1f7b22c17d854091729e633` (no new commits upstream during the run).
- Audited source: `research/stein-gr/main.tex`, SHA-256
  `88c6d07f29e72921e78aaa04bc74608723527324d918c2fbdec7935d86d0c1c7`, 947 lines.
  (This differs from the hash in `SECOND_PASS_REVIEW.md`; that review checked an
  earlier snapshot. All line numbers below refer to the current file.)
- Also pinned: `research/local-fragmentalism/STRONGEST_VIEW.md`
  (`f3d0d7b1…`), `research/local-fragmentalism/COORDINATOR_AUDIT.md`
  (`d79dbbb7…`).
- Note: the pre-existing root `AGENT_REPORT.md` in this worktree was the
  gluing-audit worker's report (commit `6a45026`); per this task's allowed
  outputs it is replaced by this task's report on this branch only. The
  original remains in history and on main.

## 1. Search capability check

- `web-search-prime` (Z.ai MCP): **failed** — quota exhausted, resets
  2026-11-17 (`-429`, code 1310). One test query attempted (Clifton–Hogarth).
- Fallback used: OpenCode built-in `websearch` + direct `webfetch` of arXiv,
  ar5iv and Springer/philsci pages. Both worked. No source is claimed as read
  beyond what was actually retrieved; paywalled or unfetched items are marked
  below.

## 2. Primary-source verification (new checks by this run)

| Source | What was checked | Depth | Result |
|---|---|---|---|
| Brunetti–Fredenhagen–Verch 2003, CMP 237:31–68, arXiv:math-ph/0112041 | §2.1–2.3: category of spacetimes (called **Man**), Def. 2.1 | full text, §§1–2 | Morphisms are isometric embeddings with **causally convex image** (their condition (i)) preserving orientation and time-orientation (condition (ii)). This matches the manuscript's GH category exactly (main.tex L147–153). Caveats: (a) BFV name the category Man; the name "Loc" is Fewster–Verch's — the manuscript's "[§2]{BFV2003}, [§2.2]{FV2012}" locator is accurate. (b) BFV Remark (B) explicitly allows "more general objects … or endow these objects with additional structures" — primary-source support for the clock-equipped category as a legitimate BFV-style variation, not an ad hoc retreat. (c) BFV p. 2 note: "local" in the definition means *geometrically local*, "which shouldn't be confused with the meaning of locality in the sense of Einstein causality" — direct support for keeping (LC) separate from signalling/microcausality. |
| Fewster–Verch 2012, Ann. H. Poincaré 13:1613–1674, arXiv:1106.4785v3 | Abstract, §1, §2.1–2.3 | full text, §§1–2 | §2.2 Loc: isometric embeddings, causally convex image, orientation/time-orientation preserved — manuscript's category is exactly FV Loc. Important nuance for framing: FV's whole paper shows local covariance alone is only a *necessary* condition for a theory being "the same in all spacetimes" (SPASs); full locally covariant theories can fail SPASs (their §4). The manuscript's intro sentence (L96–99) uses local covariance as the hypothesis "used to say when a QFT is 'the same in all spacetimes'" — defensible as a gloss on the title/programme, but the audit-grade statement is: local covariance is the *necessary* condition; FV show it is not sufficient, and their diagonal-theory phenomenon (theories agreeing in one spacetime but not others) is exactly mirrored by the manuscript's residual null freedom (§3 below). |
| Wüthrich–Callender 2017, BJPS 68:907–925, arXiv:1502.00018v1 | Abstract, §1–§3, fn. 5 | full text (§§1–4) | Quote "The analogue of this theorem, however, is straightforwardly false in CST" is verbatim (§3); fn. 5 contains "could be a small proper part of a much larger causet" verbatim. WC's counterexample relation is causal order plus ⟨b,c⟩,⟨c,b⟩ on the d<b,c<a diamond — as the manuscript §6 describes. The current manuscript framing ("Their claim is true on its own terms; the present result uses a stronger, cross-structure hypothesis", L667–668) is correct; the earlier "contrary to a published claim" overclaim is gone. |
| Clifton–Hogarth 1995, Synthese 103:355–387 | Locators and statements | not read here; corroborated by two accepted project reads | The accepted audit `knowledge/audits/clifton-hogarth/` (full primary read, p. 360 reflexive convention, Lemma p. 364, Thm 1 pp. 365–367, Thm 2 pp. 371–375, §4 pp. 381–387) and `REVIEW_OTHER_RESULTS.md` (verbatim quote checks of pp. 360, 364–367, 385–386 against text extracts) jointly cover every CH locator the manuscript uses. No discrepancy found. The two CH quotes in the manuscript (L75–79, L80–81) were verified verbatim by REVIEW_OTHER_RESULTS, not by this run. |
| Stein 1991, Philos. Sci. 58:147–167 | Printed theorem | not read here; printed-page audit | `knowledge/audits/stein-printed-pages/PRINTED_VERIFICATION.md` (accepted): theorem on **p. 149**; hypotheses reflexive + transitive + invariance under time-orientation-preserving automorphisms + a past-related pair; contextual condition (iv) (some events unsettled) is used in the proof but omitted from the printed display, and causal-past definiteness comes from the prose, not the display. See finding F1 below. |
| Andersson–Galloway–Howard 1998, CQG 15:309–322, arXiv:gr-qc/9709084 | Definition 1.1, Theorem 1.2, Prop. 2.1–2.2 | full text, key sections | τ(q) := sup of lengths of past-directed causal curves — matches Prop 5's definition (L208–210). Regular τ ⇒ globally hyperbolic, τ strictly increasing along future causal curves. The manuscript's (CB) argument for B_τ needs only the general reverse-triangle inequality, not regularity; its proof (L219–229) is consistent with the AGH text. |
| Viglione 2026, Erkenntnis, doi:10.1007/s10670-026-01075-2 (open access; philsci-archive 28022) | Abstract, CCC statement, §4–5 argument | full text via retrieved excerpts (Springer fetch blocked; text recovered through search extraction; no page numbers) | Real paper, published online 2026-03-09. CCC verbatim: "The fact that two distinct events are in a certain temporal relation (e.g. simultaneity) is absolute only if it obtains independently from the fact that any distinct causally disconnected event e_x occurs." The current manuscript wording — "closely related to the locality intuition that Viglione defends informally" (L98–100) and "akin to Viglione's Causal Connection Condition … (which is stricter: (LC) allows dependence on spacelike events inside the convex region)" (L813–815) — is accurate and incorporates the earlier review's correction. Not overclaiming "precise version". Viglione's own target is metaphysical cosmic simultaneity; using him *against* the cosmic-time rival's absoluteness claim is a fair citation (see §5 below). |

Not independently checked in this run (status preserved, not upgraded):
Monton 2006 (quotes verified against the author's preprint by
REVIEW_OTHER_RESULTS); Rakić 1997 and Earman 2008 (read in full by the
local-fragmentalism lane per STRONGEST_VIEW priority note; no local audit);
Stein 1968 p. 18 "pluralistic solipsism" quotation (author-verified only);
Hawking–Ellis §4.3 locator (flagged unverified by REVIEW_OTHER_RESULTS and
still unverified).

## 3. The category premise: what "this is Loc" commits, and what it omits

The manuscript's category (L147–153) is BFV/FV Loc verbatim. Three premise
components should be kept distinct when defending it, because they have
different statuses:

1. **Metric-only naturality (forward preservation).** One rule B assigned to
   every GH spacetime, compatible with every morphism. This is the QFT
   functoriality analogue and the source of all the theorems' transfer steps.
2. **Reflection (the biconditional).** (LC) as stated (L160–161) requires
   x B_M b **iff** ψx B_{M'} ψb. QFT functoriality gives only the forward
   embedding; the reflection direction is the substantive claim that the
   verdict is *determined by* every causally convex region containing the
   pair — the manuscript's own gloss at L172–174. Nothing in QFT practice
   forces reflection (FV's SPASs analysis exists precisely because forward
   embeddings need not be isomorphisms). Defending (LC) therefore requires
   defending determination-by-regions, not merely naturality.
3. **Off-shell universality.** Objects are all GH metrics (Remark 1,
   L176–184). The manuscript flags this honestly, and §8 correctly treats the
   energy-conditioned transfer as an open problem with a stated sufficient
   condition (the earlier "reduces to an open gluing problem" overclaim is
   repaired to "sufficient condition" phrasing, L749–758).

Suggested replacement wording (optional, no mathematical change), L96–99:
"The right replacement is local covariance in the sense of locally covariant
quantum field theory — in Brunetti–Fredenhagen–Verch's and Fewster–Verch's
sense: one rule of becoming for all globally hyperbolic spacetimes, preserved
and reflected under isometric embeddings of causally convex regions. In that
literature this condition is necessary, though not by itself sufficient, for a
theory to be 'the same in all spacetimes'; whether the becoming rule is 'the
same theory' in the stronger sense is exactly the freedom left open at the
light cone (Theorem 7)." This turns a potential confusion into a
correspondence: the residual null freedom N (Thm 7) behaves like FV's
diagonal/pathological theories — locally covariant families that agree on
Minkowski (B = I^- there for every non-universal B) yet differ on curved
spacetimes (e.g. the Weyl-gated N of Thm 8). That is an observation of this
audit, not a manuscript claim.

## 4. The false-dichotomy test: the strongest clock-equipped rival

Target passages: abstract "generic spacetimes have no symmetries" framing
(L40–44); §1 bullet (L113–117); §9 "unless they give up locality or enrich
the spacetime structure itself" (L777–785) and "the price is locality alone"
(L783–785). The current text already concedes the added-structure horn ("the
category, and with it the notion of an isometric embedding, has changed",
L781–783), but two framing residues remain: (i) "give up locality" is still
listed as the rival's first option as if it were forced; (ii) "the price is
locality alone" describes the FLRW cosmic-time rule only *relative to the
all-GH category*, which is precisely what the rival rejects.

**The rival, precisely.** Define the category GH_T ("clock-equipped
spacetimes"):

- Objects: pairs (M, T) with M ∈ GH and T: M → ℝ a smooth temporal function
  (each level a spacelike Cauchy hypersurface).
- Morphisms ψ: (M, T) → (M', T'): morphisms of GH (isometric embeddings,
  causally convex image, orientation/time-orientation preserving) such that
  T'∘ψ = T. Composition and identities are immediate, so this is a category.

The cosmic-time becoming rule: B_{(M,T)}(x, b) :iff T(x) ≤ T(b).

- (T): transitivity of ≤ on ℝ. Holds.
- (CB): if x ∈ I^-(b) then x ≤ b, so T(x) ≤ T(b) (T increases along future
  causal curves). Holds.
- Non-universality: distinct events on one level {T = c} are spacelike and
  B-related both ways. Holds. Co-presence is exactly "same clock level" — a
  shared, extended present.
- (LC): for ψ: (M,T) → (M',T'), x B_M b iff T(x) ≤ T(b) iff
  T'(ψx) ≤ T'(ψb) iff ψx B_{M'} ψb. Holds — and note that only clock
  preservation is used; causal convexity is not even needed for this
  transfer. Milne's wedge into Minkowski — the very embedding that refutes
  the rule on GH (Prop 5) — is not a morphism here, because Minkowski admits
  no finite clock matching τ_W. The category restriction bites exactly where
  the (LC) failure was detected.
- Non-vacuity of morphisms: in FLRW, each slab {a < τ < b} between
  cosmological-time levels is open, causally convex and globally
  hyperbolic, and the inclusion preserves τ. The category has a rich
  morphism stock exactly where the rival wants to work.

**What follows.** On GH_T, locality (relative to clock-preserving
embeddings), a shared present and non-trivial becoming are jointly
consistent. The manuscript's trilemma is a theorem about the *metric-only*
category, not about categories with extra temporal structure. So the honest
statement of the rival's position is:

> The cosmic-time theorist need not abandon locality. She rejects one premise
> of the theorem: off-shell universality over the metric-only category. On
> her category the rule is as local as (LC) demands; what she gives up is
> (i) generality — no verdicts in spacetimes admitting no such clock
> (stationary and spatially compact models, e.g. the Einstein static
> universe), and (ii) the theorem's uniqueness pressure — the classification
> of Theorem 7 no longer applies, so her rule is one among many on the
> restricted category, not selected by locality.

**What the clock costs, split in two cases** (the manuscript's §9 already
distinguishes these; make the cost accounting explicit):

- Metric-definable clock (cosmological time in big-bang FLRW, AGH):
  *nothing physical is added*; τ is a function of the metric (sup of past
  causal lengths). The price is purely the domain restriction and loss of
  off-shell universality.
- Non-metric clock (a preferred foliation or reference field): structure is
  added, and Viglione's CCC then applies against the *absoluteness* claim:
  on a privileged foliation, whether two events are co-present depends on
  global foliation properties — facts about causally disconnected events —
  so a cosmic-time presentist who also claims absoluteness is exposed to
  Viglione's 2026 inconsistency argument, while a claimant who drops
  absoluteness owes an account of what the clock structure is for.

**Defensible replacement wording** (§9, L777–785, replacing "unless they give
up locality or enrich … the cost is the added structure. … the price is
locality alone"):

> …unless they change the category: enrich the structure carried by each
> spacetime with a preferred clock or foliation, with embeddings that
> preserve it, so that becoming is local relative to the richer structure
> (in effect Monton's move). The theorem then does not apply, because the
> notion of a morphism has changed. Where a canonical clock is already
> definable from the metric, as cosmological time is in big-bang
> cosmologies, no structure is added; the price is instead the loss of
> off-shell universality — no verdicts where the clock fails to exist, and
> no uniqueness theorem on the restricted category. Rejecting locality on
> the metric-only category remains a third, distinct option — the option of
> global, cosmological becoming — with the costs discussed above.

What survives: the theorem, the corollaries, Prop 5 (as a statement about the
GH category, which is what it is stated and proved for), and the trilemma *as
a trilemma for metric-only becoming relations*. Nothing mathematical
changes.

## 5. Transitivity, persistence, and the three "reachability" notions

**Transitivity is a substantive premise.** The manuscript inherits (T) and
(CB) from CH's framework (L158–164) and notes CH derive (CB) from worldline
becoming + worldline transitivity (L167–171). Two audit points:

1. The lexical defence ("transitivity is part of what 'having happened by'
   means", STRONGEST_VIEW P2) motivates but does not prove the formal axiom,
   which quantifies over all pairs and, in the worldline form (Cor 9,
   L275–287), over *all* inextendible timelike curves — an idealization
   stronger than "observers who meet agree" (CH p. 363, verified in the CH
   audit). Defenders who restrict standpoints to actual observer worldlines
   (an option STRONGEST_VIEW O16 records) get the same corollary but owe the
   cross-worldline composition principle as an extra premise.
2. What transitivity does **not** deliver: causal monotonicity of fragments.
   COORDINATOR_AUDIT §2's counterexample (N gated on positive scalar
   curvature at the target, with the conformally flat metric
   a(η)=2+sin η) satisfies (LC), (T), (CB) and non-universality, yet has
   x ∈ F(b), b ≤ c, x ∉ F(c). Transitivity yields F(b) ⊆ F(c) only along
   *becoming* steps b B c (hence along strict chronology, via (CB)), not
   along arbitrary causal steps including the null boundary. Any prose that
   says fragments "grow along the time orientation" without a P6/P6′-style
   extra assumption overstates the theorem. The manuscript itself makes no
   such claim (checked: §9 and the abstract do not assert causal
   monotonicity); the defect is confined to STRONGEST_VIEW R3, already
   flagged by COORDINATOR_AUDIT. Proposed replacement wording if the bridge
   literature is quoted: "Fragments grow along becoming: if b has become for
   c, everything real from b is real from c. Growth along every causal step
   needs an additional premise — causal sufficiency (P6) or limit closure
   (P6′) — each with its own costs."

**Persistence restricted to tenseless past-event facts.** STRONGEST_VIEW P5
as stated ("every fact that holds from b holds from b'") conflicts with R2
(b alone is present from b): the centred tensed truth "b is present" cannot
persist to b' ≫ b. COORDINATOR_AUDIT finding 1. Repair for any bridge
passage: persistence holds for *tenseless past-event facts* ("x has happened
by b" type truths, and the tenseless geometry they determine); centred
tensed claims ("b is present now-from-b") do not persist and are handled by
a separate tense-shift clause. Do not assert that the same present-tense
formula persists.

**Null metric reachability vs actual signalling vs Bell dependence.** Three
distinct notions; the manuscript's closing paragraph (L826–832) gestures at
the distinction but compresses it:

1. **Metric reachability**: x ∈ J^-(b) — pure causal geometry; what (CB),
   (T) and (LC) constrain. No dynamical content.
2. **Signalling**: the operational ability to carry a controllable,
   readout-able influence to b. In relativity, signalling access is bounded
   by J^-; the converse ("everything in J^-(b) could in principle signal")
   is an idealization about controllability, not a theorem. CH's maxim,
   read as P6-signalling, promotes J^-(b) ⊆ F(b) on this basis.
3. **Bell dependence**: spacelike correlations without signalling (and, in
   collapse theories, spacelike influences that do not enable signalling).
   Bell-type dependence does not violate the antecedent of
   P6-as-signalling; it challenges the stronger premise that *all*
   ontological or dynamical dependence on spacelike events requires their
   reality-from-b (COORDINATOR_AUDIT finding 3, with Tumulka's
   no-signalling nonlocal rGRW as the existence proof, arXiv:2002.00482v2,
   abstract-level).

Proposed replacement wording (§9 last paragraph, L827–832):

> Clifton and Hogarth's maxim — whatever can causally influence an event has
> become for it (p. 364) — must be read with care. Read as a claim about
> signalling, it puts J^-(b) into B_M and is exactly the causal-sufficiency
> premise. Bell-type *dependence* on spacelike events is not signalling, and
> by itself is no counterexample to the signalling reading; what it
> challenges is the stronger thought that any dynamical dependence on an
> event requires that event to have become. If the fundamental dynamics
> lets spacelike events contribute to bringing an event about — as in
> collapse or flash theories — the stronger reading forces universal
> becoming, and Theorem 6 then applies. A non-trivial local becoming theory
> therefore presupposes that such contribution is restricted to the causal
> past; that is a substantive bet about the dynamics, not a theorem of
> relativity.

## 6. Kinematic restriction vs theorem about admissible universes or ontology

The manuscript's own separations are largely in place and were verified in
the current text: the off-shell remark (L176–184); §8's sufficient-condition
framing of the pocket problem (L749–758) with the "provably unavailable"
claim scoped to the specific auxiliary spacetime (L123–126); the Limits
paragraph's "The theorem concerns relations of becoming, not ontology"
(L819–820). Two attribution refinements remain:

- **F1 (abstract, L31–33).** "Stein proved that … a transitive relation …
  that makes some past event definite for an event, must be the causal past
  or degenerate." Per the accepted printed-page audit: the printed theorem
  (p. 149) has reflexive+transitive+invariance+a-past-pair hypotheses; the
  *conclusion* "Rxy iff xy is a past-pointing vector" (i.e. exactly the
  causal past, no "degenerate" alternative) requires the contextual
  condition (iv) — some events unsettled — which is stated above the
  display and used in the proof but omitted from the display itself, plus
  causal-past definiteness from the prose. The trichotomy (including the
  degenerate alternative) is Clifton–Hogarth's. Suggested replacement:
  "Stein proved that in Minkowski spacetime a reflexive, transitive relation
  of becoming that is invariant under the time-orientation-preserving
  symmetries, makes some past event definite for an event, and leaves some
  events unsettled, must be the past causal connectibility relation.
  Clifton and Hogarth weakened the definiteness assumption to the
  chronological past and showed the options are then the chronological
  past, the causal past, or the universal relation …". Status: presentational;
  what survives is unaffected.
- **F2 (L63–64).** "Stein's theorem is the strongest positive result in the
  debate over relativistic becoming" — a value judgement flagged by the
  predecessor review and still present. Suggested: "the central positive
  result". Cosmetic.
- **F3 (L40–41, 85–86).** "generic spacetimes have no symmetries" is used
  twice without a citation or an existential fallback. Minimal repair:
  "there are open dense sets of … spacetimes with trivial isometry group
  [cite], and in any case some globally hyperbolic spacetimes have none, so
  the single-spacetime statement is simply false (Proposition 4)". The
  proposition only needs existence. Minor.
- **F4 (L211–212).** "invariant under all isometries and under the morphisms
  of GH that are onto" — onto-morphism invariance is redundant (onto
  morphisms are isometries); say "isometries". Cosmetic.

## 7. The standpoint interpretation: what it adds beyond eternalist causal restriction

Question from the 2026-10-27 coordinator update (GitHub gate #9). Scope
note: the manuscript itself is ontology-neutral (§9 Limits); the standpoint
layer lives in `STRONGEST_VIEW.md`. The two documents make claims of
different strength and must not be averaged.

What the theorems give any party: for every non-universal relation satisfying
(LC), (T), (CB), the fragment of b lies between I^-(b) and J^-(b) in every GH
spacetime (Thm 6); with causal sufficiency or limit closure it is exactly
J^-(b). An eternalist can and should accept this as the content of "what has
happened by b": it is a conditional classification of relations, useful
independently of ontology.

What the standpoint interpretation adds *over* the eternalist's restricted
quantifier ("x has happened by b" = "x ∈ J^-(b)"):

1. A grounding direction: standpoint-relative reality is basic; the tenseless
   geometry is recovered as the agreement of standpoints (P5, repaired
   version) rather than posited.
2. An answer to "why these fragments and not others": physics fixes them —
   the locality premise plus non-triviality pins the fragments up to the
   null boundary, instead of the eternalist stipulating the restriction.
3. A classification of the opposition: any rival with a shared present in
   the mutual-becoming sense must either violate locality on the metric-only
   category or change the category (§4 above) — a cost accounting, not a
   refutation.

What it does not add: no tenseless truth changes (truth-conditional
equivalence with eternalism is conceded in STRONGEST_VIEW); no observable
changes; and "settled" is kept separate from "real" (R10), which is what
makes the view compatible with deterministic futures inside a fragment-free
region.

**Defensible bridge passage (proposed, concise).**

> On any relation of becoming that is transitive, includes the
> chronological past, is local in the sense of one rule for all spacetimes
> preserved and reflected on causally convex regions, and is not universal,
> the fragment of an event b — what has become for b — lies within b's
> causal past and contains its chronological past; with causal sufficiency
> or limit closure it is exactly the causal past. Tenseless past-event facts
> persist to later standpoints; centred tensed truths, such as "b is
> present", do not, and are handled by the semantics of the indexical. The
> theorem is neutral between reading the fragment as the fundamental unit of
> reality (the standpoint interpretation) and reading it as the content of a
> restricted quantifier over one block; what it fixes is the fragment
> itself, whichever side of that dispute is fundamental.

**Strongest unresolved objection.** The interpretive gain is currently
untestable and rests on an undecided dispute. Truth-conditionally, the
standpoint view and the eternalist restriction agree on everything tenseless
(conceded), and no agreed criterion exists for when a grounding asymmetry is
explanatory rather than a redescription (STRONGEST_VIEW O2, Sider vs the
deflationists). Moreover the formal bridge is not yet statable with full
precision: the persistence axiom needs the tenseless/centred restriction of
§5, fragment growth along causal steps needs P6 or P6′ (each with
independent costs — Bell-compatibility for the causal-sufficiency route,
arbitrariness for the closure route), and the object language with
completion semantics for future-tensed claims is still owed (STRONGEST_VIEW
§7.4). Until those are supplied, the theorem constrains the fragments but
does not yet favour the interpretation over its empirically and
truth-conditionally equivalent eternalist restriction; the preference is
explanatory at best. This is the objection to state in the paper if the
bridge is asserted; the conditional mathematics needs none of it.

**Empirical equivalence vs grounding/explanatory preference — three levels
kept apart.** (i) Fragmentalism vs eternalism: truth-conditional *and*
empirical equivalence conceded; the dispute is grounding only. (ii)
Cosmic-time rule vs causal-past rule: not truth-conditionally equivalent on
becoming claims (the whole past clock level has "happened" for the former,
only J^-(b) for the latter), but empirically equivalent — no observable
distinguishes verdicts about spacelike events — and both preserve the same
tenseless causal geometry. Choosing between them is a matter of which
grounding structure one accepts, under the respective costs of §4.
(iii) Under Bell-nonlocal event dynamics the causal-past fragment itself can
collapse to the universal relation: there empirical neutrality ends and the
dynamics decides.

## 8. Resolved-review inventory (verified in the current source; do not re-open)

Confirmed repaired in `main.tex` at the pinned hash, with the repair visible
at the stated places: strict/reflexive convention and MS topological facts
(L140–145, §4 preamble); Lemma D(ii) simultaneous-crossing case (L534–551);
Weyl theorem's causally-convex flat set and "conformal structure" wording
(L307–316); Weyl/MS 2.30 citations (L327–336, 357–360); WC framing "true on
its own terms" (L654–668) with the off-shell causet flag (L667–670); Gödel
outgoing-morphism argument (L689–691) and modal-step reframing (L695–703);
DEC proposition restricted to totally geodesic Cauchy surface with the
Minguzzi-2015 route and the non-Minkowski maximal development fix
(L713–741); pocket problem as a stated sufficient condition (L749–758);
non-universality defined (L259–261); trilemma scoped to mutual-becoming
presents (L787–799); Viglione wording (L98–100, L813–815). The gluing-audit
F1 Lemma F repair was implemented by the coordinator in REPLACEMENT form;
the current Lemma F (L583–609) matches the replacement's product-tube
approach.

## 9. What survives

Everything mathematical in the abstract, introduction and philosophical
sections, as conditioned: (a) the classification theorem as a statement
about the metric-only category, with (LC) understood as naturality plus
reflection plus off-shell universality; (b) the corollaries, including the
mutual-becoming reading of "no shared present"; (c) the causal-set result as
a stronger-hypothesis theorem that does not contradict WC; (d) the Gödel
isolation as a fact about morphism absence; (e) the energy-condition
section as an open, sufficient-condition programme. The philosophical
sections survive with the wording repairs of §4, §5 and §6 above. The
standpoint interpretation is best presented, if at all, exactly as in §7's
bridge passage, with the strongest objection stated alongside it.
