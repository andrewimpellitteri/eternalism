# Red-team review of REVERSAL_TEST.md and PILOT_REVIEW.md

31 October 2026. Claude Code (Opus 5.5), fresh context. This is the same model as the
author, so it is not an independent review. For coordinator inspection, not acceptance.
No novelty or ontology verdict.

## Verdict

**The Lemma is correct and trivial. The headline Claim does not follow from it and, as
stated, is false. It is REPAIRABLE only to a much smaller claim.** PILOT_REVIEW's main
findings hold. One finding is partly unfair, three need rewording, and one item in its
survivors list is too generous.

**Strongest problem.** The Lemma needs a Θ_b-invariant *model*. The Claim says "on
reversal-symmetric *physics*". These differ, and §4 concedes that no realistic sustainer
has the first. A neutral rule on a non-invariant model can return a one-sided window with
no orientation premise, and it can return the pilot's own window.

Counterexample. Take the damped channel q_t+cq_x=−γq with γ>0 and F>0, so
q=F(t−x/c)e^{−γx/c}. Let Θ_b be the note's PT reflection with γ→−γ, which "whatever
conjugation" allows. Rule N: among events on tokens crossing the slice t=b, keep those
whose amplitude is at least that token's amplitude at the crossing. N never mentions
past, elapsed or input. It is neutral, because Θ_b maps tokens to tokens and the slice to
itself and preserves amplitude, so the defining condition transports. For γ>0 N returns
exactly the pilot's set of in-progress portions. An inline check found 0 neutrality
mismatches and 0 differences from that set on a 1,080-point grid.

If the γ→−γ conjugation is refused, use a reversible micro-model instead. For any
Θ-even functional S, such as coarse-grained bath entropy, "keep the part of the token on
the lower-S side of b" is neutral by the same argument, under a T-symmetric law with no
conjugation. It is one-sided wherever S is monotone through b.

Three things follow.

- The Claim's second sentence is false. §1's "non-neutral premise or symmetric windows"
  is false too: a neutral rule on a non-invariant model is a third option, and it is
  what row 2 of §3 actually is.
- "That source, not the activity, does the asymmetric work" is false of this model. N
  reads the side off the token's own attenuation. That attenuation may trace to distant
  boundary conditions, but this separate reductive thesis is one §4 names and does not
  show. It also confuses the ultimate source with the proximate bearer.
- The same standard removes the width. τ=L/c is as contingent as the side, and benchmark
  §6 calls the duration a property of the input/output protocol and boundary
  configuration. If "input" is a choice for the side, it is a choice for the width.

**What survives.**

1. The Lemma, plus a corollary with more bite against the pilot's R1. If a neutral
   present P includes L on a Θ_b-fixed model, it also includes Θ_b L.
2. The finding against the pilot: in its lossless channel, at the mirror standpoint, no
   past-sided rule is neutral, so its one-sided window needs a stated source.
3. A smaller, sound claim: *fix Θ explicitly. A one-sided window at b requires a Θ-odd
   feature of the rule or of (m,b). A bridge must name that feature.* Where the feature
   is in the activity, as with attenuation or entropy production, the activity does fix
   a side, and the side and width share their contingency. "Width but not side" is not
   established.

## 1. Reversal-neutrality

- **Lemma: VERIFIED.** W(m,b)=W(Θ_b m,b)=Θ_b W(m,b).
- **The definition: REPAIRABLE.** It assumes no ontology, and the conditional spares the
  growing-block theorist, for whom a reflected block is not in 𝓜. It has two defects.
  "Whatever conjugation" is unconstrained: flipping γ makes any oriented law "invariant",
  so neutrality has no fixed meaning until Θ is named. And Θ_b m=m treats a reflected
  relabelled model as the same model. AGENTS.md warns that a representation transformation
  is not automatically an equivalence. Repair: name Θ, list what it conjugates, and state
  that Θ_b m=m is a premise.
- **"A rule using no orientation is neutral": GAP for time-oriented Lorentzian models.**
  Suppose m includes an orientation τ. Under plain pushforward, "past side of b" is
  covariant and therefore *neutral*, but no model is fixed, since a reflection reverses
  τ, so the Lemma has no instance. Under pushforward composed with an orientation flip,
  symmetric models are fixed and "past side" is non-neutral, but only because orientation
  is treated as a conjugated label, which is what a primitive-direction theorist denies.
  Suppose instead m omits τ. Then a generic (M,g) has no reflection at all, and a rule on
  (M,g) can be one-sided, for example "the side of b nearer the initial singularity".
  "Should be neutral" also fails on its own terms: see the end-A rule in point 2.
- **"Past side fails neutrality": REPAIRABLE.** It holds only on the flip reading, and
  "past" must be fixed independently of m. "Unless its result is empty" should read
  "unless its result lies in the slice at b". A closed side can return the slice, and the
  pilot's window is closed at b.
- **"Exactly four options ... exhaustive": GAP.** The sentence announces four options and
  lists two. The table's rows are not all non-neutral premises: row 2 is a neutral rule on
  an asymmetric model, and row 3 is not a break under "whatever conjugation" (point 3).
  Also missing are a multi-valued W returning a symmetric pair of one-sided windows, as
  in spontaneous symmetry breaking, and a standpoint Θ does not fix. §4's "arbitrary
  selection" covers only a single-valued W. Repair: replace "exhaustive" with a
  classification of Θ-odd sources.

## 2. The channel witness

Rederived by hand. channel_check.py was read and rerun, and it passes.

- **PT map, inlet to reflected outlet, y reflected: VERIFIED.** Q=G(t−x/c) with
  G(w)=F(2b−τ−w), and y_Q(t)=y(2b−t).
- **Two-sided identity: VERIFIED, but it has less content than the note suggests.** It
  is the substitution g(t+s)=f(t+s−τ). Both forms name the same data, F on (t−τ,t). A
  future form also survives damping, as y=τ⁻¹∫₀^τ e^{γs}g(t+s)ds (checked numerically), so
  its existence needs only an invertible inlet-to-outlet map, not reversal symmetry.
  Only the flat kernel needs PT.
- **Palindromic condition: VERIFIED, but it fires at one b.** F(w)=F(2b−τ−w) makes the
  history Θ_b-invariant at that b only. An exact check gave invariance at b and not at
  b+1/3, unless F is constant. Elsewhere a neutral rule is unconstrained, except that it
  must mirror its output at 2b−b′. The note's "window" is a fact about one instant.
- **Token span: VERIFIED, but "as required" misleads.** The region t−x/c∈[b−τ,b] is
  Θ_b-invariant for *every* F. That is geometry, not the Lemma.
- **Bearing on "depends on exactly the input window": REPAIRABLE.** The identity does not
  contradict it. The pilot's claim is a response claim: vary f under a fixed law.
  Mathematically f and g are in bijection, so the response has an exact advanced mirror.
  What breaks the tie is which end can be set. Repair: say the identity removes the side
  from functional dependence, not from dependence as control.
- **A stronger witness the note missed.** For every x,
  y(t)=τ⁻¹∫_{x/c−τ}^{x/c} q(t+s,x)ds (exact check at four x). The inlet window is wholly
  past, the outlet window wholly future, the midpoint window centred. Side varies with
  probe position. So does width: a section moving at v has time-width τ/(1−v/c), and
  straight sections of the token region run from 0 (the slice) to 2τ (the long diagonal).
  Width τ is the fixed-probe case, and the neutral token region projects to 2τ in time, not
  τ. The invariant is the set of characteristics. The witness shows both width and side
  are section-relative, against §5's "physics supplies only the first".
- **PT versus T: it matters, and the note undersells it: REPAIRABLE.** T alone fixes every
  point of slice b but sends c→−c, so no c≠0 model is fixed and the Lemma has no instance.
  PT fixes models but fixes only the event (b,L/2) and the slice setwise. For an event
  standpoint elsewhere, Θ_b moves b. Repair: state W(Θm,Θb)=ΘW(m,b). Neutrality is also
  group-relative. Rule "events at end A on tokens in transit at b" has no temporal
  vocabulary, is T-neutral (exact check) and not PT-neutral, and is one-sided even on the
  palindromic model. So "no temporally oriented premise" must become "no Θ-odd premise".
  Given the end, its side comes from the sign of c, a feature of the transport itself.
- **Fair witness: REPAIRABLE.** It is fair against the pilot's own model and is no evidence
  for the general Claim. It is lossless, tuned and not self-maintaining. The pilot's
  "sustainer" is also not neutral even here: its role test is cessation from b onward, and
  tokens are "injected". The mirror test is non-onset. Repair: use Θ-closed alternatives.
- **"Boundary-condition choice": REPAIRABLE.** Keep "boundary condition", drop "choice".
  Benchmark §6 has a physical drive at one end. That is an apparatus fact, not a
  modeller's option.

## 3. The dilemma table

- **Row 1, primitive orientation: REPAIRABLE.** It is fair if the primitive is external.
  It is not fair if direction is part of the activity, as with causal production or a
  Maudlin-style direction on which earlier states produce later ones. That theorist denies
  Θ_b m=m and denies "the activity contributes the width at most". Primitively directed
  causation and Maudlin both take this row, and an event-realist may too. Repair: split the
  row into external and constitutive primitives, and charge the second with lacking
  independent physical support, not with having the wrong source.
- **Row 2, "so it cannot favour an inventory": GAP. The inference is invalid.** A shared
  datum can favour whichever side explains it better. The project says so itself:
  BREAKTHROUGH_TEST §4 warns against confusing accommodation with "equal explanatory
  merit", and CONSTITUTIVE_GROUNDING_TEST says "Mere compatibility" does not establish it.
  A growing-block theorist may claim growth explains the direction. That places her in
  row 1, not row 2, since she denies the arrow is merely contingent. The proper reply is
  separate: growth alone supplies no entropy gradient, and Ellis and Drossel themselves
  attribute local arrows to a Past Condition. Repair: "Row 2 alone gives no preference; a
  preference needs a separate explanatory argument."
  Two smaller points. "Contingent" fails if the past condition is nomic, so say
  "non-dynamical". And contingency is no cost to a system-relative program. A side fixed
  by the system's own entropy production suits it. Row 2 is a repair for the bridge, not
  a defeat.
- **Row 3, T-violation: REPAIRABLE, dismissed too fast.** Under "whatever conjugation",
  CPT-symmetric T-violation is no break at all: Θ becomes CPT, and matter content makes
  models non-invariant. So known T-violation joins the neutral-rule class. Genuine
  law-level asymmetry is a different case, such as collapse. Albert proposed GRW as the
  ground of thermodynamic irreversibility, and Ellis and Drossel base passage on collapse
  and include biological arrows. Both are contested, but "unrelated to sustaining activity"
  needs an argument.
- **Row 4, "cannot support any view excluding the future at b": GAP as stated.** A
  symmetric window can be the slice {b}, of width zero, which excludes everything else. A
  bounded symmetric window excludes everything beyond its edges. Repair: "cannot support a
  view on which b is reality's leading edge."
- **Causal-order windows.** J⁻(b) uses the orientation, so it is non-neutral: row 1 if the
  orientation is primitive, row 2 if derived. The unoriented cone is neutral and two-sided.
  A diamond J⁺(p)∩J⁻(q) with p, q mirror images about b is neutral and bounded, so the
  literature already has a neutral relativistic window (point 6).

## 4. Who must revise

- **Constitutive-present theorist: VERIFIED for the pilot, REPAIRABLE as stated.** The
  quoted phrase is Attempt 1's. R1's "fixed by representation-invariant input/output
  physics" should be cited too. The pilot never argues its side, so the charge lands. But
  "revise" means "name the source". An apparatus fact is not a metaphysician's choice.
- **"Growing-block or presentist defender": GAP, presentism is misattributed.** Presentism
  treats past and future alike, needs no side, and has a neutral window in the slice. No
  source is cited for anyone holding the asymmetric-support position, and the pilot's R4c
  denies giving growth any support. Repair: drop presentism, or restrict to a
  past-trailing durational view if one is sourced.
- **"The event-realist retains everything": VERIFIED but one-sided.** The Lemma has no
  inventory content, so the slice presentist also retains everything. Singling out one
  party in the Claim, row 4 and this list tilts a project with no preferred ontology.
  State it for all parties.
- **Process-worm consequence: GAP, delete it.** Neutrality gives symmetry and nothing about
  extent, so the slice is equally "natural". A whole-token rule returns the same set for
  every b, so it is not a window. A whole token is generally not symmetric about b. The
  pilot's rejected alternative (c) already declined it. "Fits the event-realist's account"
  runs into BREAKTHROUGH_TEST §4: ability to recognize processes "does not earn event
  realism a default preference". The hedge does not remove the tilt.

## 5. The dissipative case

**Plainly: the Lemma is idle for every dissipative sustainer, and so for every realistic
self-maintaining system.** No flame or cell is Θ_b-invariant at any b. The note's vacuity
condition is met for that class. §4's "this changes which row applies. It does not defeat
the claim" is wrong for the headline. Row 2 is not a consequence of the Lemma. It is an
independent reductive premise, and §4's own exposure clause admits it would need showing.
§5's "absorbed, not refuted" should be withdrawn.

Even granting the reduction, the activity carries the side by a neutral rule, so "by
itself" survives only if "activity" excludes its own entropy production. Note also that a
steady flame's reservoir temperatures and concentrations are unchanged under reversal. The asymmetry lies in micro-correlations, so "reversed boundary conditions"
are not boundary conditions in the ordinary sense.

The Lemma is not idle for lossless sustainers. The note missed its best second case, the
pilot's Kepler pair. An eternal circular orbit is invariant under T composed with reflection
through the line of the pair at b, for *every* b. With no binding event the pilot's form
becomes (−∞,b], which is non-neutral at each standpoint. A real binding event, or
radiation, makes the model non-invariant again.

## 6. Priority

**Not simply Price's double standard. The Lemma is Curie's principle.** Norton's "Curie's
Lemma" has the same form: a symmetric cause under a symmetry-respecting map gives a
symmetric effect. He calls it a tautology, empty until instantiated, with all substance in
the mapping. That matches the note's "all the content lies in the definition". Roberts glosses
the idea as "if no asymmetry goes in, then no asymmetry comes out", and argues that the
state-to-state form fails for time reversal: a T-invariant state at t=0 has non-invariant
later states. That is the one-standpoint restriction of point 2. The Lemma escapes his
counterexample because it concerns whole models under a reflection, which is a point in
its favour. Castellani and Ismael reply that T is not a symmetry transformation in the
needed sense, and advise suspicion of reasoning with it like other symmetries. The note
reasons with it exactly that way.

Price supplies the diagnostic use, not the inference. Farr's distinction between
time-reversed models as distinct worlds and as causally unchanged is the live issue behind
Θ_b m=m. The nearest specific form is Curie's principle applied to a past-sided present,
with Price's charge attached. No source found applies this to sustaining activity. That
proves little: searches were few, and the Curie link was not in the note.

**Project record.** §5's "contains no such argument" needs a pointer. The redteam file
`research/local-fragmentalism/redteam/02_B_theory_deflationists.md` §5 already runs the
double-standard swap on J⁻(b): reversed orientation yields J⁺(b). It does not concern
sustaining activity, so the sentence is not strictly false.

**Specious present.** James's present is two-sided: "the practically cognized present is no
knife-edge, but a saddle-back", looking in two directions into time (1890, ch. XV, p. 609).
So symmetric thick presents are old, which undercuts row 4. Arthur's and Savitt's diamond is
a bounded interval between two events. Power's papers remain unread beyond abstracts. Whether
they treat reversal is unknown, so the note's "could be close" stands. No work joining time
reversal to process ontology was found, and two searches do not settle that.

## 7. PILOT_REVIEW.md against the pilot's text

Every quotation was checked and is accurate unless noted.

| Finding | Verdict | Note |
|---|---|---|
| 1. Side from "elapsed" | Correct, REPAIRABLE | The gloss is in P2's defense (§3 item 2), not P2. "Tensed" is wrong: "earlier than b" is oriented but tenseless, and AGENTS.md requires that distinction. "The temporal asymmetry in dispute" overstates: the CTR accepts earlier and later, and what is disputed is inventory. Against R1's "at least", a side excludes nothing, so use the corollary under What survives |
| 2. Lower bound and width | Correct in substance, REPAIRABLE | R1's question is printed as "why is S's present this wide?", and R4b says "has this width". Those need an upper bound, which P3⁻ lacks. A lower bound answers only "why at least τ?", so R1's first sentence is safe. "Contradict" is too strong: this is an unearned presupposition, not an inconsistency. Better evidence was missed: R3 keeps "determinate widths ... (channel: yes)" |
| 3. Explanandum | Correct, fair | The pilot's own §4 verdict says the CTR can retain everything. R4b withdraws that without saying so |
| 4. R2 equivocation | Correct | §4(i) does slide from present-for-S to concrete as of b. An unnoticed consequence: on the local reading the retraction of P3-backward was unforced, so finding 2's upper bound could return. It would return only as a restriction of the word "present", which is the pilot's rejected alternative (b). Findings 2 and 4 should be stated together |
| 5. "Trivially" | Correct | |
| 6. AC and level | Mostly correct | The f≡0 point and the b+τ point are right; the pilot's "no carriage is in progress" is false until b+τ. "The Kepler interaction can be described with propagation tokens" is unsupported: the Newtonian pair has none, so that is a different, retarded model, not a redescription |
| 7. P1 analytic | Partly unfair | The pilot calls only "operative at the assessment time" analytic. P1 also says unity "consists in" the activity's being operative, which is not analytic. So "says only" misdescribes it. The pilot uses the restriction to leave other grounds free, not to carry C&R's warning |

Over-generous: "the free-particle witness [is] correct". Its §9 first use is fine, but
the "Invalid test" use is not. A free particle has no A, so G2 fails and nothing separates
G2 from P2. And P2 as printed covers any "process token in progress at b", not only
sustainers, so "P2 does not apply" needs a restriction the pilot never states.

Missed by both: W_b is not a time strip. The union of in-progress portions is a triangle
with corners (b−τ,0), (b,0), (b,L). The strip contains completed-token events: (b−τ/2,L) lies
on a token that exited at b−τ/2. "Width τ" is a time projection, and holds as a local
duration only at the inlet.

## Read depth and limits

Computations ran inline in under 10 seconds. Rule N's neutrality has a one-line analytic
argument, and the grid check is confirmation. Exact checks are at sample points only. All
domains are the stated models.

| Source | Depth this session |
|---|---|
| REVERSAL_TEST, PILOT_REVIEW, pilot RESULT.md (ccb40b5), PILOT_QUESTION, CONSTITUTIVE_GROUNDING_TEST, BREAKTHROUGH_TEST, benchmark §§6–8 | full-text |
| channel_check.py | code-audited, rerun |
| Norton, "Curie's Truism", Philosophy of Science 83(5), 2016, journal layout | full-text §§1–3 start; rest unread |
| Roberts, "The Simple Failure of Curie's Principle", preprint 6 Aug 2012; published 80(4), 2013, 579–592, not collated | full-text §§1–4.2 start |
| Castellani and Ismael, "Which Curie's Principle?", 83(5), 2016, preprint | abstract, start of §4.2 |
| Ellis and Drossel, "Emergence of time", arXiv:1911.04772v3 | abstract, selected excerpts |
| James 1890, Principles, ch. XV p. 609, psychclassics copy | passage, via fetch summary |
| Farr, BJPS 71(1), 2020, DOI 10.1093/bjps/axx025 | abstract |
| Power 2012, Erkenntnis 77(1) 121–132; Power 2016, chapter | abstract, via search summary |
| Price 1996; Maudlin 2007 ch. 4 (chapter attribution from one secondary source); Earman on time direction; Albert 2000 ch. 7 on GRW; Arthur 2006 and Savitt on diamonds | discovery only; Arthur's project register records full-text by an earlier worker, inherited |
| Earman 2004; Ismael 1997; Dainton; Dupré and Nicholson | discovery, or cited through others; not read |

Not done: no primary reread of Brading, Brown–Pooley or C&R, so nothing here concerns their
positions. The pilot's cited precedents were not checked. Whether any published durational
view is past-trailing was not determined. The attribution of positions to Maudlin, Albert,
Earman and Price rests on summaries and should be verified before external use.
