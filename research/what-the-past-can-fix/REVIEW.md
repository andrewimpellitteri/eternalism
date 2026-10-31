# Adversarial review of "What the Past Can Fix"

31 October 2026. Reviewer: Claude Code (Opus 5.5), at the coordinator's request. Target: `main.tex` and
`parts/` as they stood at 12:20 on this date. Same model family as most of the internal review, so this
is not an independent check. No novelty or ontology verdict. Theorems outside the checklist were not
re-proved. Lines are `main.tex` lines unless a part is named.

**Where to apply repairs.** `parts/` is generated. Repairs to `parts/becoming_*` go in
`research/stein-gr/main.tex`, repairs to `parts/fixing_*` go in `research/horizons/main.tex` (or as `swap`
calls in `assemble.py` when the text is specific to the unified paper). The Lemma F text in `parts/` is
identical to `stein-gr/main.tex`.

## Verdict

**No theorem failed.** Lemma F's new proof stands with small repairs. Every row of Theorem `thm:map`
checks. The defects are in the prose around the theorems, and two are false as written:

1. The abstract and introduction drop transitivity from the no-shared-present claim. The paper's own bow
   tie is then a counterexample.
2. "It does not depend on whether the future exists" contradicts the paper's own positions table.

Section `sec:revise` is the weakest section. Three of its nine items survive at reduced strength.

| # | Item | Verdict |
|---|---|---|
| 1 | Lemma F | CONFIRMED, with 3 small repairs |
| 1 | Remark `rem:lc` | REPAIR: true of part (a), incomplete for part (b) |
| 2 | `eq:chain`, Theorem `thm:map` rows | CONFIRMED |
| 2 | Reading of the rows | REPAIR: bridge unstated, one statement mis-scoped |
| 2 | Theorem `thm:same-past` | CONFIRMED against sources, 2 omissions |
| 2 | Lemma `lem:cones` | CONFIRMED |
| 2 | Theorem `thm:rigidity` | CONFIRMED. Marked-extension hypothesis is redundant |
| 2 | Proposition `prop:uncountable` | CONFIRMED |
| 2 | Theorem `thm:massive` | CONFIRMED, including the outline and m=0. Time variable wrong |
| 2 | Proposition `prop:sp`, realm section | CONFIRMED |
| 3 | Part IV | REPAIR: 5 regressions against REVIEW_TOTALITY.md |
| 3 | "every attempt" | REJECT as written |
| 3 | Proposition `prop:tetrad` | CONFIRMED as Loss's argument |
| 3 | Positions table | REPAIR: 4 rows |
| 4 | `sec:revise` | REPAIR. 1 knocked out, 5 narrowed, 3 survive |
| 5 | Integration | REPAIR: list below. No "companion paper" or "Section 8" remains |
| 5 | "It does not depend on whether the future exists" | REJECT as written |
| 6 | References | 3 wrong or truncated titles, 1 misattributed source, 3 attribution problems |

Checks run: every `\ref` and `\eqref` resolves, every citation has a `\bibitem`, and no `\bibitem` is
uncited (script over `main.tex` and `parts/`).

## 1. Lemma F (`parts/becoming_proofs.tex`, lines 264–313)

| Step | Check | Verdict |
|---|---|---|
| P,Q spacelike in M′ | g′-causal implies η_λ-causal. True. The hypothesis is redundant: any two points of H are η_λ-spacelike, since slope < 1/λ | CONFIRMED |
| H Cauchy | d(t−f(s))/dτ ≥ ṫ(1−λ abs f′) > 0 and t→±∞ along inextendible curves, so one crossing for g′ and for η | CONFIRMED |
| Boost | H={t=αs+β}. A boost alone gives {t̃=const}. A time translation is also needed when β≠0, and the first application has β=−4r | REPAIR (trivial) |
| W^± as halves of D_Mink | In Minkowski, J⁻(p)∩H=B̄(z,t̃), and straight segments reach every point. So W^+=D^+ | CONFIRMED |
| Balls above 2δ | **True only with a global condition.** "Small compared with the curvature radius" does not exclude self-approach. A long arc of large curvature radius can coil through a solid region, and then its δ-neighbourhood contains balls much larger than 2δ. With δ below the reach of the arc, the true bound is δ. In the two uses the arc is a planar graph, so nothing breaks | REPAIR |
| Compactness | Set W={z∈Σ″, abs t̃≤d(z)} with d(z)=dist(z,H∖Σ″), which is 1-Lipschitz. W is closed and bounded | CONFIRMED |
| Flat neighbourhood U | Needs abs t̃ and the tube radius small against the distance to T̄_{3r}. The boost changes distances by a bounded factor depending on abs f′<1/λ. "Small compared with" hides this constant | CONFIRMED, tighten |
| C(p) nesting | If q=(T′,z′)∈C(p), then B̄(z′,T′)⊂B̄(z,T) | CONFIRMED |
| W⁺⊂D⁺ | Open-closed argument on the first parameter leaving C(p). C(p)⊂U makes the curve η-causal, so it stays in C(p) up to the crossing | CONFIRMED |
| D⁺⊂W⁺ | p below H is excluded (no crossing). p on H gives p∈Σ″. First point q₁ of γ in the closed W⁺ exists, and the crossing lies at or after it, so points just before q₁ are above H and off W⁺ | CONFIRMED |
| C(q)⊂U | C(q) lies within about dist(q,q₁) of C(q₁)⊂W⁺, and W⁺ is compact in open U | CONFIRMED |
| Choice of q, straight segment | q∉W⁺ gives z′∈B̄(z,T)∖Σ″. The segment lies in C(q)⊂U so it is g′-causal. The H crossing is unique and off Σ″ | CONFIRMED |
| Time reversal | g′ is not time-symmetric, but the argument uses only g′=η on U and H Cauchy. Works with C⁻ | CONFIRMED |
| N″ formula | A closed ball of radius d(z) misses the open set H∖Σ″. Interior of W is abs t̃<d(z). Where z∉int Σ″, d=0 and the set is empty | CONFIRMED |
| Connected, contains P,Q | Retract t̃→0 onto int Σ″, which contains the connected open tube. P,Q lie at distance ≥δ from H∖Σ″ | CONFIRMED |
| Causal convexity, global hyperbolicity | Σ″ is acausal, so Lemma D(iii) transfers word for word. N″⊂U, so the identity is an isometry preserving both orientations | CONFIRMED |
| Applications | Arcs avoid T̄_{3r} (10 sin(π/8)≈3.83>3), slope 8r/L<1/λ, endpoints η_λ-spacelike | CONFIRMED |

**Remark `rem:lc`.** Line 34–35 of `parts/becoming_framework.tex` says reflection is used along N↪M and in
Lemma F. In part (a) that is right: x B_M b → x B_N b, and w B′ v → w B_{N″} v. In part (b) the directions
differ. Reflection runs along ψ|_N:N→M′ and N″↪𝕄, while N↪M is used forward. Proposition `prop:causets`
also uses reflection, since a verdict on a convex subset is read back from the larger causal set.

## 2. Unified content

**`eq:chain`.** Correct. Is⊂I⁻⊂B is (CB), and B⊂J⁻ is Theorem `thm:main`. J⁻⊂F and Det⊂F are Remark `rem:laws`. Is⊊B always, since b∈B(b). B(b) needs defining as
{x: x B_M b}, and three forms F_L(Is(b)), F_L(b), F(b) are used for one set.

**Rows of `thm:map`.** All checked against the cited results.

| Row | Basis | Verdict |
|---|---|---|
| 1 | `prop:conformal`, `prop:sharp` (a=1, R=0) | CONFIRMED |
| 2 | `rem:laws` gives F=M, `prop:conformal` gives Det. The proof cites only the first | CONFIRMED, cite both |
| 3 | `prop:dust` (τ≤π), `thm:diamonds` (0<τ<π) | CONFIRMED |
| 4 | Flow paragraph, including the boundary lines by continuity | CONFIRMED |
| 5 | `thm:massive` | CONFIRMED |
| 6, τ=π | Det=Is by `prop:dust` at equality. F=M: the trace of Is(b) is S³ minus the antipode, so smooth data vanish | CONFIRMED |
| 7 | Is(b) contains a Cauchy slice | CONFIRMED |

"Each inclusion beyond J⁻(b)" is loose: Is⊂Det is not beyond J⁻, and it too can be strict or equal.

**Reading beneath the table.** Facts correct. Three repairs. (a) "Unreal" needs the bridge: nothing in
Part II says what is unreal unless having become is read as being real. (b) Row four belongs in "rows two,
three and six", and rows one and two also show law-dependence. (c) The last clause is sound, but the
introduction's paraphrase (line 104–105, "an unbounded change of verdict can be a bounded change in
fields") is meaningless, since a verdict is binary, and it attributes `eq:hidden` to Theorem `thm:map`.

**Theorem `thm:same-past`.** Statement, quantifiers, profile, mass limit, regularity and four
qualifications match C11_FINITE_CONTROL.md §§1, 3–7, SMOOTH_FINITE_CONTROL.md §§1–3 and
FINITE_CONTROL_ACCEPTANCE.md. The linear normalization φ(t,0)=Φ(t) is right, since rφ=f(v)−f(u) gives
φ(t,0)=2f′(t) and Φ=2f′. Repairs:

- The profile must vanish on v<A, and the F_k must miss G. C11 §3 has this through its interval [A,B]. The
  paper states neither. x must also lie in a small ball, or β is undefined.
- u, v, r, m, t and t(b)=0 are used and never defined.
- External inputs are incomplete. SMOOTH_FINITE_CONTROL.md §2 records that LOY's past completeness is one
  sentence and the reversed proof was not written out. FINITE_CONTROL_ACCEPTANCE.md records that the
  compact-family extension is our deduction, not printed in LOY.
- Credit. PRIOR_WORK.md (`claude-central-history`) lists "past does not fix later readings" as known in
  general (Manchak 2008, Geroch 1977), and the paper does not credit that here. "It does not." (line 322)
  is unconditional while the theorem is conditional.
- Read depth. Carlotto–Schoen is abstract and summaries only, and Kehle–Unger a fetch summary. Neither is
  labelled.

**Lemma `lem:cones`.** Bound checks: −2/9+(8/3)/16=−1/18. Σ⊂W, W is an open past set, and the Cauchy-in-W
argument holds: an inextendible curve of W is ambient past-inextendible because W is a past set, and its
future end cannot lie below t=0. `t₀<min(0,A)` is just t₀<0, since A>0. The Cartesian chart is the C¹,¹
one, which REALM_CONTRAST_IN_SMOOTH_CLASS.md §1 addresses and the paper does not.

**W versus W_b.** Not inconsistent, but the paper never connects them. W_b=I⁻(I⁺(b))∖J⁺(b) (line 423) and
W=M∖J⁺(b) differ whenever b has a horizon. They agree in this class, because the first clause of
`lem:cones` gives I⁻(I⁺(b))=M. That clause is stated and never used for this. Also W is the bow tie minus
b, whereas W_b in general omits elsewhere points, so "On a fixed background this is immediate. Put W_b=…"
is a stronger sufficiency claim than the bow-tie one. The fixed-background claim itself is right: any
past-inextendible curve from J⁺(b) lies in I⁻(I⁺(b)) and leaves J⁺(b) before t(b).

**Theorem `thm:rigidity`.** Proof correct, including Σ₂ ambient Cauchy. W₁'s connectedness is used without
proof (REALM_CONTRAST §3 has it). The citation of CBG1969 needs care, see §6.

**Marked-extension hypothesis.** Right, and unnecessary. H extends h and h is onto W₂, so H(J⁺(b₁))=J⁺(b₂).
Hence J⁺(H(b₁))=J⁺(b₂), and H(b₁)=b₂ in a causal spacetime. So W alone marks b, which is slightly stronger
than the source. Only the launch germ and tangent are extra content. The germ is available because
J⁻(b)∖{b}⊂W.

**Scope comment.** The bow tie contains an early Cauchy slice in every globally hyperbolic spacetime, so its
future is fixed for any law with unique evolution, not just "in the class of Theorem `thm:rigidity`". The
theorem's content over Cauchy uniqueness is the two-spacetime transport. The paper should not call this
"the centre of the paper" (line 466).

**Proposition `prop:uncountable`.** Matches NONISOMETRY_LEMMA.md, including the sign reversal and locally
Lipschitz measure argument. CONFIRMED.

**Theorem `thm:massive`.** Statement and outline match RESULT.md Lemmas 1–4 and its theorem proof, and
REVIEW_STATUS.md accepts that exact scope. m=0 clause: RESULT.md says the second line holds "for every mass
(including zero)", and the proof is as in the outline. Repairs: the outline uses t, while the paper uses η
and τ, and τ is never said to be conformal time. Two headline theorems (`thm:massive`, `thm:same-past`) have
no proof in the paper, only "the project's reviewed note". A reader outside the repository has nothing to
check.

**Stale sentence.** The end of `parts/fixing_models.tex` leaves open whether a local law in the closed models
fixes no more than Det∪J⁻. Theorem `thm:massive` now answers this on closed dust for every τ≠π. At τ=π the
massive law does fix more.

**Proposition `prop:sp` and realms.** Match PERSISTENCE_CONVENTIONS.md §1, RIVAL_PROFILE_AND_REGULARITY_BRIDGE.md
§§1–3, DIAMETER_CLASSIFICATION.md and HORIZON_REVIEW.md. "Future-directed" is undefined, the "it" in line 507
reads as D rather than the spacetime, and "The horizon obstruction belongs to the class, not to the idea" is
obscure. Appendix `app:status` still says "Reviewed for n≥2 census", and the census is no longer in the paper.

## 3. Part IV

**Regressions against REVIEW_TOTALITY.md and TOTALITY_READ.md**

| Passage | Problem | Verdict |
|---|---|---|
| Line 570, "every attempt" | TOTALITY_READ §6 and REVIEW item 8 qualified exactly this claim, because the theorem derives an upper bound from a stipulated negative. Line 687 of the same section then calls Theorem `thm:main` "a real upper-bound derivation". "Physical organization" narrows it only if the theorem is not such an attempt, and the sentence does not say so. It is also a universal with no audit | REJECT |
| Lines 568–569, R_b as what "constitution" supplies | REVIEW §2 flagged this conflation. Constitution gives R⊂E_b for an activity region that may include events later than b, and R_b is different. Prop `prop:sp` gives only J⁻(b), not the bow-tie or slice R_b, so the sentence is false of two columns of its own table | REPAIR |
| Line 124–125, intro diagnostic | Drops "for stated candidates only", and turns "a thesis the event realist rejects" into "the thesis in dispute". REVIEW's three escapes then look refuted | REPAIR |
| Lines 56, 127, 728, 741 | REVIEW §7 and TOTALITY_READ's Result: no strongest rival gets a new reason to revise anything. "Must revise" in the abstract is stronger than anything those notes allow, and the growing-block item is Loss's own | REPAIR |
| Line 705, "the live routes" | The least-base route is our construction with an obvious defect (no net saving across stages, REVIEW §4). Tooley's analysis is unread. "Fall outside the sorting" is what was earned | REPAIR |
| Line 679 | Drops "given P2–P4" | REPAIR |
| Line 603 | Drops "could change the first row". "Does other work" is asserted from an abstract and one review | REPAIR |
| Line 681 | Cites Earman as if the principle were his. It is the reply he reports | REPAIR |
| Line 623–624 | Drops "not totality-form constitution claims or a presentist's present-tensed premises". REVIEW also says "tenseless to tensed" is "not quite" the point, since past-tensed truths widen the class | REPAIR |
| Line 614, "the materials for it were there" | With no priority audit, this reads as a soft priority claim | REPAIR |

Not reintroduced: the merger of Loss and Fine, the "indexed and acceptable to both sides" claim, the
relativistic collapse, and "the identification is mine". Lines 602–613 and 658–662 keep the repaired forms.

**Is the "every attempt" sentence consistent with the theorem discussion?** No, see the first row.

**Line 553–554.** Cites Wawer2021 as a source for the later-grounded view. PASSAGE_AND_EARLIER_TRUTH.md §1
says he challenges it.

**Proposition `prop:tetrad`.** CONFIRMED. With permanence and temporal necessitation, a truthmaker at b makes
p true at every later stage, contrary to growth. The hypothesis "which growth falsifies" supplies the later
stage. It is Loss's argument and the proof says so. Calling it a Proposition is acceptable. It fires only
through the rigid claim, as line 637 says.

**Positions table (lines 748–761).** Selected profiles, as stated, but four rows need repair.

| Row | Finding |
|---|---|
| Presentism | Unfair by omission. The answer depends on the spatial reading first: a Cauchy slice gives the clock row, a point gives almost nothing. By Corollary `cor:nopresent` an extended metric-only present must change category or drop transitivity, so the row is not free-standing. It also owes an upper bound |
| Pointy | Fair |
| Bow tie | **"Rejects transitivity" is accurate.** Failure: x∈E_b, y∈E_x, y∉E_b (PERSISTENCE_CONVENTIONS §4). Correia and Rosenkranz motivate rejecting (TR) in Replies §8 (`bowtie-horizons/RESULT.md`), and Dorato and Hoefer object on this ground. But the column misleads: the bow tie also owes an upper bound, and fixed is general, not class-specific |
| Standpoint relativism | Fair as a profile. J⁻(b) is not forced by relativism |
| Clock | **Wrong as stated.** The rule of `sec:becoming-rival` is T(x)≤T(b), so what has become is a sublevel set, and a level is the present. The level-only view is presentism. "If the slice is Cauchy" is vacuous, since T is a Cauchy temporal function |
| Event realism | Fair. Selection is owed only where completions are not unique, which should be said. Line 587 already says it |

## 4. Section `sec:revise`

Standard: BREAKTHROUGH_TEST.md §1 and §4 item 4. What would a knowledgeable opponent have a reason to revise,
and if the rival can retain everything, narrow or abandon.

| Item | Target real? | Result gives a reason? | Verdict |
|---|---|---|---|
| Stein, settledness | **No holder.** Repo records have "already definite as of", "unsettled", and all causal-past points definite because they may influence the state (pp.148–149). The record says the paper does not establish indeterminism, and that the relation's adequacy is left to interpretation (p.150). Nothing shows Stein means fixed by law. The phrase "fixed and definite" appears in no repo record, and a public-copy fetch returned only the title | Only against a nomic reading nobody is shown to hold. His theorem is untouched | **KNOCK OUT as a target.** Keep as a constraint on readers |
| Putnam | Real. Repo: pp.243–246 argue future contingents already have truth values, a step separate from the ontology. The claim that relativity settles it needs a page locator | First step: Section `sec:bounds` is about R_b⊂E_b, which is not Putnam's route. His bridge is Principle III, already explicit, and Theorem `thm:main` strengthens the conditional: a local transitive (CB) relation with one spacelike pair is universal. Second step: Section `sec:truth` is about growth, and PASSAGE §7 adds only that an inventory does not fix a truth policy. A block theorist adopts L at no cost | NARROW: state the policy. "At each step" fails |
| Unreality to openness | Generic, and the introduction says this has long been known | Exact GR models for a known point. Does not touch existence-based openness, which depends on the modal class (MAXIMALITY §§4, 7) | NARROW to law-relative openness in a fixed class |
| Openness to growth | Generic. Correia and Rosenkranz expressly refrain from arguing this way (MAXIMALITY §7) | The models differ in exterior data, so an indeterminist reply says this is not the openness meant | NARROW to past-relative nonfixing |
| Causal past as base | Real | Yes: a comparison must match the rival's realm. Bow-tie theorist must accept a fixed future under unique evolution. Holds for the argument, not new as physics | **SURVIVES** |
| Shared present | Real, and the strongest item | Yes, with (T) stated. Defenders retain everything by naming the rejected premise, but they must name it. Conditional on (LC), (CB), (T), off-shell | **SURVIVES, repaired** |
| Constitution to inventory | **The project's own candidate.** CONSTITUTIVE_GROUNDING_TEST.md disclaims any named reconstruction, and does not identify Brading's proposal with E_b=R | Defeats the displayed inference. "Closed as a deductive route" overreaches: that note says a further exhaustiveness principle could supply it | NARROW, label as ours |
| Growing-block maximalists | Real | Loss's reason, not ours. It fires through the rigid claim | SURVIVES, credited to Loss |
| Event realists as default | Thin. No event realist argues from R_b⊂E_b to H⊂E_b. The principle cited is our own, and ROLE_OF_EXISTENCE.md already withdrew the default | Selection debt is real only in non-unique classes, and "already in the project" (TOTALITY_READ §5) | NARROW to a debt, with the condition first |

**What survives by BREAKTHROUGH_TEST.md's standard.** Loss's item survives as true but gives no new reason, so it does not
count here. That leaves two listed items and one that is not listed, as revisions a knowledgeable opponent could be asked
for. None is priority-audited yet.

1. Anyone who holds that the loss of symmetry in general relativity frees a transitive metric-defined relation
   from Stein's constraint must name which of (LC), (CB) or the off-shell premise they reject.
2. Anyone who argues for or against a bow-tie view from past-relative nonfixing must change the base.
3. Anyone who reads causal limits on prediction as openness must add a law: `thm:map` separates them
   exactly in one model. Manchak and Earman partly anticipate this, as the paper says. This one is not on the
   current list, and should replace an item that fails.

None of the three is a philosophical advance on the ontology, and the paper claims none. "Breakthrough" is not
earned, and the paper does not use the word.

## 5. Integration

**Abstract, "It does not depend on whether the future exists."** Defensible only for a stipulated base: F_L(R)
is defined with no reference to existence. As written it is contradicted three times. The last column of the
positions table varies with the ontology. Line 479 says a bow-tie theorist has a future fixed by what exists
and a pointy theorist does not. Where E_b⊇future, fixed from what exists is trivial. Existence-based openness
(MAXIMALITY §7) also concerns whether the future occurs. REJECT as written.

**Other overclaims**

| Line | Text | Problem |
|---|---|---|
| 40–41, 94–95 | Local metric relation, no shared present | **False.** B={(x,b): x∉J⁺(b)∖{b}} is local by causal convexity, contains I⁻, is non-universal and has extended co-presence. It fails only (T). This is the paper's bow tie |
| 53, 121–122 | "The physics supplies lower bounds" | Prop `prop:sp` says no field equation enters. Constitution needs a granted premise. AGENTS.md requires these be kept apart |
| 78 | GR "determines the second exactly" | Exact only in the models treated. `thm:same-past` is target by target and conditional. Lines 774–775 repeat this |
| 79–80 | "It does not determine the third or the fourth" | The body supports only that nothing here does, and the sort is for stated candidates |
| 153 | Det is "what every local deterministic law fixes" | **False literally.** On Minkowski every such continuous law fixes J⁻(b), while Det=Is |
| 38 | "We separate them with theorems" | Truth is separated by a restricted counterinterpretation |
| 86–88 | Stein's theorem | Omits the conditions that PRINTED_VERIFICATION.md says the display needs, and the chronological case |
| 322 | "It does not." | Conditional result stated flat |
| 466 | "The centre of the paper" | The moral is linear and PRIOR_WORK.md advises treating the result as routine until a specialist says otherwise |
| 710 | "The most promising physical route" | An unargued judgement |
| 713 | "Closed as a deductive route" | See §4 |

**Forward references and leftovers**

- `parts/becoming_prior.tex:31`: "remark quoted in Section `sec:intro`". The remark is not there. It follows
  Corollary `cor:worldline`.
- `parts/becoming_energy.tex:9, 38–47`: "M′ above", "as above", "w, v and the detour", T_{2r}, D(Σ). All are
  defined later, in the appendix. Leftovers of the old order.
- Line 419: "In the notation of Section `sec:bounds`". E_b is set up in `sec:realms`.
- Line 676: "P2 below" is a label from STRONGEST_VIEW.md, undefined here, and it clashes with (P2R) on line 702.
- Line 167: "Earlier work in this programme" has no citation.
- Appendix: "Stout 2016 unread" has no referent. `thm:map`, `lem:cones`, `prop:uncountable`, `prop:mass`,
  `sec:truth` and `sec:maximal` have no status entry though line 130 promises "each". Broad and McCall are
  cited but unread, and the read-depth row omits them.
- Duplication: main.tex lines 193–197 repeat "The idea" at `parts/becoming_proofs.tex:66–70`. The trilemma
  appears three times.

**Notation clashes.** None changes a result. The ones worth fixing:

| Symbol | Uses | Fix |
|---|---|---|
| E | Horismos E⁻, realm E_b, incoming mass E | Mass 𝓔 or m_∞ in Part III |
| H | Hyperplane (Lemma F), isometry (`thm:rigidity`), history, H_n | Isometry Ψ. History stays H |
| R | Relation (`prop:single`), base (Setting), R_b, region R, frame | Base S, keep R and R_b distinct as above |
| U | 𝒰, launch vector, U_b, neighbourhoods | Launch vector n |
| B | Relation, unindexed B(b), B_{M,λ}(b), balls, constant in `prop:norm` | Define B(b) once. `\B` macro is unused |
| F | F_L(b), F_L(Is(b)), F_L(R), F(b), F_m, profiles F_k, metric coefficient F | Define F_L(R), set F_L(b):=F_L(Is(b)). F_L(R) is promised in Setting and never defined |
| τ, η, t | Conformal time as τ, η_b and t | Say τ=η_b. Use η in the outline |
| W | Milne wedge, W^±, W_b, W | Tolerable once W_b=W is stated |
| A, T | Antipodal map and cutoff, 2π and clock | Tolerable |

Reflexive versus strict is handled correctly throughout. `E⁺` is used in the proofs and never defined. The
paper's E⁻ excludes b, MS's contains it, and `thm:weyl`'s "x≠b" is redundant.

**Abstract and introduction versus body.** Otherwise delivered: every technical sentence of the abstract has a
theorem behind it, with its condition stated.

## 6. References

Checked against repo source records and, where marked, by fetch (31 October).

| Entry | Finding |
|---|---|
| Brading2015 | **Title truncated.** Fetched: "Physically locating the present: A case of reading physics as a contribution to philosophy" |
| Tooley2010 | **Title truncated.** Fetched: "Time, Truth, Actuality, and Causation: On the Impossibility of Divine Foreknowledge" |
| Kehrberger2021 | **Title truncated.** Fetched: "The Case Against Smooth Null Infinity I: Heuristics and Counter-Examples". "In print": the regularity is a remark in that paper, citing Christodoulou 1993 and LOY |
| GronJohannesen2011 | Subtitle missing. Fetched: "III: Universe models with positive spatial curvature" |
| Ringstrom2009 | **Misattributed use.** The common larger development comes from Ringström's author correction note, "Existence of a Maximal Globally Hyperbolic Development" (SMOOTH_SCALAR_REPAIR.md). Its interior book pages were not accessed. Add the note as its own entry |
| CBG1969 | Vacuum theorem. REALM_CONTRAST §3 says no vacuum-to-matter analogy is used, and the citation on line 461 should say the scalar case rests on the note |
| Wawer2021 | Entry right. Attribution wrong on line 554 |
| Broad1923 | Line 69 cites an unread source for growing block plus deterministic laws, which is our conjunction |
| Earman2008 | Line 681: reported reply, not his principle |
| McCall1994 | Read only through Earman and Tooley. Line 589 cites it directly |
| Bigelow | Named on line 601 with no reference. Add one or attribute through MacBride2024 |
| Incomplete | Deng2017, Colyvan1998, Wawer2021, GLS2018, CheynePigden2006, CarlottoSchoen2016, Muller2019 lack volume or pages. BS2006 lacks its journal. Fill from publishers |

Confirmed by fetch: Minguzzi2015 (title), vdSchaaf2026 (Marco Lewis, Nesta van der Schaaf; some repo records
misname the author as "T. van der Schaaf"), MSS2025, BolotinTanatarov2013, Arthur2019, Loss2022, Aames2022,
Viglione2026, Lipman2023. The remaining entries
look right from repo records and were not fetched.

## Ranked required repairs

**1. Restore transitivity to the no-shared-present claim.** It is false as stated.

Line 40–41: replace `a local relation defined from the metric alone admits no shared present` with
> a transitive local relation of becoming defined from the metric alone admits no shared present

Lines 94–95: replace the sentence beginning `For relations defined from the metric alone` with
> For transitive relations that contain the chronological past and are defined from the metric alone, locality, a
> shared present and non-trivial becoming cannot all be had (Corollary~\ref{cor:nopresent}). Without transitivity
> they can: the bow tie of Section~\ref{sec:rigidity} has all three.

`parts/becoming_phil.tex`: replace `for relations of becoming defined from the metric alone` with
> for becoming theories, which are transitive by definition, defined from the metric alone

and replace `Defenders of a shared now reject locality on $\GH$ or change the category` with
> Defenders of a shared now reject locality on $\GH$, reject transitivity or change the category

**2. Replace the abstract's independence claim.** Lines 51–52:
> So whether the future is open depends on which base is held fixed and on the law. Given a base and a law, the
> answer is the same whatever one says about whether the future exists. If the base is taken to be what exists from
> an event, the answer varies with the ontology.

**3. Repair line 568–571.**
> Let $R_b$ be what a restricted view counts as concrete from $b$, and $H$ the represented history. Constitution
> gives $R\subseteq E_b$ for an activity region $R$, which may include events later than $b$
> (Section~\ref{sec:process}). Persistence gives $\Jm(b)\subseteq E_b$ (Proposition~\ref{prop:sp}). A restricted view
> adds $R_b\subseteq E_b$. These are lower bounds, and every argument from physical organization that we have
> examined stops at one. Theorem~\ref{thm:main} gives an upper bound only by amplifying an assumed failure of
> universality, as discussed below. A lower bound cannot settle the matter, because $R_b\subseteq E_b$ is compatible
> with both $E_b=R_b$ and $E_b=H$.

**4. Stop calling the lower bounds physics.** Line 53:
> Stated bridges about constitution and persistence supply lower bounds on what is concrete from an event.

Line 121–122: replace `The physics gives lower bounds.` with
> Stated bridges from the physics give lower bounds.

Line 56: replace `We sort the stated candidates, and record what each party must revise.` with
> We sort the stated candidates, and record which inferences fail.

Line 124–125: replace from `The useful result` to `in dispute.` with
> The useful result is a diagnostic for these candidates: an index on ``concrete from $b$'' is either defined, and then
> trivial and shared, or primitive, and then a thesis the event realist rejects. Three candidates need support of a
> different kind.

**5. Replace the list in `sec:revise`** (lines 728–744), and the title with "Which inferences fail". Line 127: replace `records what each
party has a reason to revise` with `records which inferences fail`.
> The results license no ontology, but they do bear on particular inferences. None of what follows is claimed as new.
> \begin{description}
> \item[Metric-only shared presents.] Corollary~\ref{cor:nopresent}. A transitive relation containing the chronological
> past and defined from the metric alone has no shared present if it is local. Its defenders must name the premise
> they reject: locality on $\GH$, transitivity, the off-shell premise, or the category.
> \item[The causal past as a base for every rival.] Theorem~\ref{thm:rigidity}. A comparison must match the rival's
> realm. A past-agreement counterexample does not reach a bow-tie view, whose realm contains a Cauchy slice.
> \item[Causal limits on prediction read as openness.] Theorem~\ref{thm:map}. What is guaranteed does not bound what a
> law fixes, as \citet{Manchak2008} and \citet{Earman1995} partly anticipate.
> \item[Growing-block maximalists.] Proposition~\ref{prop:tetrad}. This is Loss's argument, and it fires through the
> rigid claim.
> \item[Unreality to law-relative openness.] Theorem~\ref{thm:map}, on the reading of having become as being real. The
> distinction is old; the models are exact. Openness of existence is untouched, since it concerns the modal class
> (Section~\ref{sec:maximal}).
> \item[Past-relative nonfixing to growth.] Theorem~\ref{thm:same-past} holds for an eternalist, since each model is one
> whole spacetime with its own exterior data. It is no evidence against indeterminist growth, and we know of no one who
> argues this way from it.
> \item[Reality to truth.] \citet[pp.~243--246]{Putnam1967} argues that future contingents already have truth values.
> That step needs a policy connecting outcomes to earlier truth (Section~\ref{sec:truth}). A block theorist can adopt
> the policy at no cost to the inventory, so the reason is to state it.
> \item[Constitution to inventory.] Section~\ref{sec:process}, against the argument as we reconstructed it.
> \item[Event realism as a default.] Where completions are not unique, the selection of $H$ is a debt. A selection
> principle preferring fewer primitives \citep{ProjectRole} needs a defence of its own.
> \end{description}
> One reading of \citet[pp.~148--149]{Stein1991} is also excluded. If ``definite'' and ``unsettled'' meant fixed by law,
> the relation would not be $\Jm$, since Theorem~\ref{thm:map} has $F=M$ in several rows with $B$ inside the causal past.
> Nothing we have read shows that Stein intends that reading, and his theorem does not need it.

**6. Correct the stale open question.** End of `parts/fixing_models.tex`, via `assemble.py`:
> Theorem~\ref{thm:massive} shows that on closed dust a local law can fix exactly $\Det(b)\cup J^-(b)$ for every $\tau\neq\pi$.
> Whether some local law does so at $\tau=\pi$, or in other closed models, we leave open.

**7. Positions table.** Replace four rows.
> Presentism & Present only, however spatially read & Denies persistence; owes an upper bound & Depends on the spatial
> reading and the law: as the clock row for a Cauchy slice; past-grounding owed\\
> Bow-tie growing block & Past and elsewhere & Rejects transitivity of existence-at; owes an upper bound & Fixed wherever
> the law has unique evolution, since the realm contains a Cauchy slice\\
> Clock-equipped view & $\{T\le T(b)\}$, with a level of $T$ as present & Changes the category & Fixed if the law has unique
> Cauchy evolution\\
> Event realism & $H$ & Owes a lower bound, and selection where completions are not unique & Yes, trivially, and that says
> nothing about law\\

**8. Setting and thesis.** Line 153, middle column:
> what the causal structure guarantees from $\Is(b)$, fixed by every law with the domain-of-dependence property

Lines 78–80: replace from `It determines` to `either.` with
> It makes the second a mathematical question, once a law and a comparison are named, and we answer it exactly in the
> models treated. Nothing here determines the third or the fourth, and the first two do not determine them.

Line 154: replace `what a law class fixes from agreement on a base $R$` with
> $x\in F_{\mathcal L}(R)$ if any two solutions agreeing on $R$ agree at $x$; $F_{\mathcal L}(b):=F_{\mathcal L}(\Is(b))$

**9. Lemma F and Remark `rem:lc`.** In `research/stein-gr/main.tex`. Replace `A Lorentz boost (an isometry of $\eta$) makes
$H$ horizontal:` with
> A boost along $s$ followed by a time translation, an isometry of $\eta$ preserving time orientation, makes $H$ horizontal:

Replace from `Take $\delta$ small` to `on which $g'=\eta$.` with
> As $\delta\downarrow0$ the sets $\Sigma''$ decrease to the extended arc, which is compact with empty interior in $H$. So
> the largest radius $h(\delta)$ of a closed ball in $\Sigma''$ tends to $0$: a limit of balls of radius bounded below would
> lie in the arc. Take $\delta$ with $\delta+h(\delta)$ small compared with the $(\tilde t,z)$-distance from the extended arc
> to $\overline{T_{3r}}$. Every point of $W=W^+\cup W^-$ has $z\in\Sigma''$ and $|\tilde t|\le h(\delta)$, so $W$ is compact and
> has an open neighbourhood $U$ on which $g'=\eta$.

Replace `Extend $\kappa$ slightly past $P$ and $Q$` with
> Extend $\kappa$ slightly past $P$ and $Q$ inside $H$, keeping it embedded and off $\overline{T_{3r}}$,

In Remark `rem:lc`, replace `uses it along $N\hookrightarrow M$ and in Lemma~\ref{lem:F}` with
> uses it along $N\hookrightarrow M$ and $N''\hookrightarrow M'$ in part (a), and along $\psi|_N:N\to M'$ and
> $N''\hookrightarrow\Mink$ in part (b)

**10. Part IV attributions.** Line 553–554: replace `\citep{CR2018,Wawer2021}` with
> \citep{CR2018}, which \citet{Wawer2021} challenges

Line 69: replace the sentence with
> A growing block in Broad's sense \citep{Broad1923}, with deterministic laws added, has an unreal future that is settled.

Line 681: replace the first cell with
> No fact selects a completion, the reply Earman reports \citep[pp.~144, 154, 159]{Earman2008}

Line 679: replace the last cell with
> The same bound as Theorem~\ref{thm:main}, given the bridge and non-universality

Line 603–604: replace from `does other work` to `abstract.` with
> appears to do other work, but we have not read it beyond its abstract and one review, and it could change the first row
> of the table below.

Line 705: replace `and they are the live routes for a restricted view` with
> and they fall outside this sorting

Line 614: replace `, but the materials for it were there` with
> . No priority audit has been run

Line 624–625: replace `It is a form of the familiar point that tenseless premises do not yield tensed conclusions, and it says` with
> It does not cover totality-form constitution claims or a presentist's present-tensed premises. It is close to the familiar
> point that tenseless premises do not yield tensed conclusions, and it says

Line 713: replace `is closed as a deductive route, and adding examples will not reopen it` with
> is closed as a deductive route unless a further exhaustiveness premise is supplied, and adding examples will not supply it

Line 710: replace `The most promising physical route to a restricted inventory runs` with
> One physical route to a restricted inventory runs

**11. Theorem `thm:same-past`.** Lines 325–328: replace from `Choose incoming` through `$2T_N+1$.` with
> Use double null coordinates $(u,v)$ with $t=(u+v)/2$ and $b$ at $t=0$ on the center; $r$ is the area radius and $m$ the
> Hawking mass. Choose incoming characteristic data at past null infinity from a compact family: fix $0<A<T_1$, smooth $F_k$
> with disjoint supports about $T_k$ inside $(A,2T_N+1)$ and $F_k(T_j)=\delta_{kj}$, and a smooth nonzero $G$ supported after
> $2T_N+1$. Take $x$ in a small closed ball on which $\beta$ below is smooth and positive.

This follows C11 §4, where $v=t+\rho$ and $u=t-\rho$. Line 356, after `sketched in the source.`, add
> The past half of their completeness theorem is stated in one sentence, and the extension to our compact family is our
> deduction from their uniform bounds.

Line 388, before `That is the expected mechanism`, add
> That a past need not fix later readings is known in general \citep{Geroch1977,Manchak2008}.

Line 322: replace `It does not.` with
> Subject to the inputs below, it does not.

Line 466: replace `The contrast is the centre of the paper. In one physical class` with
> In one physical class

**12. Theorem `thm:map`.** Line 281–282: replace from `Each row` to `equality.` with
> Each row below holds, and each of $\Jm(b)\subseteq F$, $\Is(b)\subseteq\Det(b)$ and $\Det(b)\subseteq F$ can be strict or an
> equality. Here $B(b)=\{x:x\,B_M\,b\}$ and $F=F_{\mathcal L}(\Is(b))$.

Line 308: replace `Being unreal from $b$ does not imply being open:` with
> Reading having become as being real, being unreal from $b$ does not imply being open:

Line 309–310: replace `rows two, three and six` with
> rows two to four and six

Line 104–105: replace `and an unbounded change of verdict can be a bounded change in fields` with
> and an exact verdict can flip while the hidden fields change by $O(m^2)$ in a stated norm (equation~\eqref{eq:hidden})

**13. Theorem `thm:rigidity`.** Insert after the proof of Lemma `lem:cones`:
> Since every two events share a chronological future, $W_b=W$ in this class, and $W$ is the bow tie minus $b$.

Line 423, after the definition of $W_b$, add
> In general $W_b$ is smaller than the bow tie, which is why the sufficiency below is the stronger claim.

Lines 449–450: replace `of metric and scalar, extending continuously to send $b_1$ to $b_2$.` with
> of metric and scalar.

Lines 462–463: replace `and the continuous extension gives $H(b_1)=b_2$.` with
> so $H$ carries $\Jp(b_1)=M_1\setminus W_1$ onto $\Jp(b_2)$. Thus $\Jp(H(b_1))=\Jp(b_2)$, and $H(b_1)=b_2$ since $M_2$ is causal.

This is optional. The stated theorem is correct as it is.

Line 461: replace `\citep{CBG1969,Ringstrom2009}` with
> \citep{CBG1969,Ringstrom2009}, in the scalar form of \citet{RingstromNote}

Lemma `lem:cones`, line 433: replace `$t_0<\min(0,A)$` with `$t_0<0$`, and line 438: add "in the $C^{1,1}$ reconstruction chart, whose
causal curves are those of the smooth representative" after `global Cartesian coordinates`.

**14. Integration.**

- `parts/becoming_prior.tex:31`: replace `quoted in Section~\ref{sec:intro}` with `quoted after Corollary~\ref{cor:worldline}`.
- `parts/becoming_energy.tex:9`: replace `$M'$ above` with `the spacetime $M'$ of Appendix~\ref{sec:proofs}`. Line 47: replace `$\Sigma$ as
  above` with `$\Sigma$ as in Lemma~\ref{lem:D}`. Line 38: replace `near $w$, $v$ and the detour` with `near the points $w$, $v$ and the
  detour of the proof of Theorem~\ref{thm:main}`.
- Line 419: replace `Section~\ref{sec:bounds}` with `Section~\ref{sec:realms}`.
- Lines 676, 689: replace `via P2 below` with `via the reality bridge`, and `at a bridge P2, which reads` with `at a bridge, which reads`.
- Line 167–170: cite the causal-set example or delete the two sentences from `Earlier work`.
- `parts/fixing_mass` and line 245: add `Write $\tau=\eta_b$ for conformal time.` before Proposition `prop:mass`. Line 253: replace `\psi_{tt}` and
  `V(t)` with `\psi_{\eta\eta}` and `V(\eta)`.
- Lines 86–88: replace the first sentence of the paragraph with
  > Stein's theorem, with its contextual conditions, says that in Minkowski spacetime a transitive, symmetry-invariant relation of
  > becoming that contains the causal past and leaves something unsettled is the causal past \citep{Stein1968,Stein1991}. Clifton and
  > Hogarth give the form whose alternatives are the chronological past, the causal past and the universal relation \citep{CH1995}.
- Line 505–511: replace `this is persistent exactly when it is future-directed` with `this is persistent exactly when every pair of
  events has a common strict causal future`, and `The horizon obstruction belongs to the class, not to the idea.` with `Whether a horizon
  obstructs the criterion depends on the class.`
- Appendix: replace `Reviewed for $n\ge2$ census; cylinder classification reviewed` with `Proposition~\ref{prop:sp} elementary; horizon lemma and
  cylinder classification reviewed`. Delete `Stout 2016 unread`. Add rows for `thm:map`, `lem:cones`, `prop:uncountable`, `prop:mass`,
  Sections `sec:truth` and `sec:maximal`. Add Broad and McCall to the reports-only row, and Carlotto--Schoen and Kehle--Unger as read
  at summary depth. Update the Lemma F entry.
- Put the proofs of Theorems `thm:massive` and `thm:same-past` somewhere a reader can check them. An appendix or a public note both
  serve. Until then they are claims with outlines.

**15. References.** Correct Brading2015, Tooley2010, Kehrberger2021 and GronJohannesen2011 as in §6. Add:
> \bibitem[Ringström(n.d.)]{RingstromNote} H. Ringström, Existence of a maximal globally hyperbolic development, author note,
> \url{https://people.kth.se/~hansr/mghd.pdf}.

Add a Bigelow reference or attribute through MacBride2024. Line 589: replace `on McCall's view \citep{McCall1994}` with `on McCall's view
as reported by \citet{Earman2008}`. Add the missing volumes and pages from publishers, not from memory.

## Is this one paper?

Yes, with a defensible single thesis, once the abstract's independence sentence is repaired: what has become, what is fixed,
what exists and what is true are different relations, and each result shows one gap with its conditions. Parts I to III are
a tight argument: Theorem `thm:map` and the realm contrast connect them, and `eq:chain` is the real unifying object. Part IV is
looser, a bounded survey at report depth attached by the question "what would reach existence?", and it adds no theorem of its
own beyond Loss's. The negative half of the thesis is supported by countermodels to stated inferences and a sort of stated
candidates, not by a theorem, and should be worded that way. The weakest section is `sec:revise`: it restates inferences few
hold, against targets partly of the project's own making, and its strongest item was mis-stated. Cut to the three surviving
items, or the list in repair 5, it stops overselling the paper. The next weakest point is structural: two theorems named in the
abstract are proved outside the paper.
