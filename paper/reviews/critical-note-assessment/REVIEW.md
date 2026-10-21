# Referee assessment: is the P1\*\*/Savitt critical note publishable?

Referee role: independent journal referee (subagent), assessing publishability of a
short critical note, not the truth of the metaphysics. Date: 2026-10-21.

Target claim assessed:

> Savitt's 2021 SEP objection to Brading's local present applies to Brading's 2015
> P1\*\* (a) and to the sentence "all we need is (a)"; the paper states the
> non-implication explicitly and maps the repair costs.

Materials read: `paper/main.tex` (working-tree version, 443 lines, ~3,360 words,
8 pages); `paper/reviews/p1-priority-audit/REVIEW.md`; `p1-logic-audit/REVIEW.md`;
`p1-source-audit/REVIEW.md`; `research/existence-form/TRILEMMA.md` and
`NOVELTY_AUDIT.md`; `paper/READINESS.md`. I re-read Savitt's SEP §3.3 live
(full text of the section; entry states "substantive revision Wed Oct 6, 2021",
so the dating the audits rely on is current and stable). I did **not** re-read
Brading 2013/2015 directly; I rely on the source audit's page-image checks and on
the quotations reproduced in `main.tex` and the three audits, which agree.

---

## 0. Verdict in one paragraph

**Not publishable as a short comment or note in its present framing.** It is not
a conference paper either: it has no empirical or formal result that would carry a
talk. The reason is not writing quality — the manuscript is careful, the
quotations are (after the current revision) mostly clean, and the boundary-drawing
is unusually honest. The reason is that the note's *increment* is
mis-specified. It is presented as "Savitt's objection, retargeted at the 2015
sentence", but Savitt's objection is *invariant* under the 2013→2015 change: his
objection is stated in a paragraph that already concedes the only thing (a) adds
("Presents construed this way will typically be larger than a single point but
will not necessarily exhaust all of Minkowski spacetime"). A referee who reads
both texts will conclude that the note has found a page number, not a problem. The
defensible contribution lies elsewhere — in the distinction between the
*uniqueness* objection Savitt actually makes and the *coverage* objection the
note actually needs, and in the fact that no condition of the same logical type as
(a) or (b) can supply what is missing. That is a real note, but it is a different
note, roughly 1.5× the length, aimed at a different venue, and it must abandon the
current thesis rather than defend it.

Realistic outcome if revised along §5 below: a specialist discussion note, maybe.
Realistic outcome as it stands: desk rejection or one round of
"interesting but insufficiently novel".

---

## 1. Is this publishable — comment, conference paper, or neither?

**Neither, as framed.**

As a *comment*, it fails the genre's central test: a comment must identify a claim
the target makes and show it is wrong in a way the author would not accept. Here
the target claim is one sentence — "In order to avoid the block universe, all we
need is (a)" — surrounded by two sentences that weaken it ("this calls the
ontology of a block universe into question"; "Only if there are such can the
version of presentism offered here survive", 2015, pp. 17–18). The manuscript
knows this: it now quotes the hedge and labels its own bridge "interpretive"
(l. 62–70). A comment that concedes up front that its verdict may need weakening
by a reader who prefers the author's own weaker wording is a comment that has
already lost the argument it is having.

As a *conference paper*, it has nothing to put on a slide. The formal content is
one two-line non-implication with a three-element model. The repair map is four
options in four paragraphs with no ranking criterion. Neither survives a
twenty-minute slot against a paper that presents a result.

As a *short note*, it is 3,360 words to make a point that fits in 800, and the
extra words are not load-bearing: the Stein paragraph, the Saunders/Pooley
section, the four-way "existence/presence/unity/endurance" taxonomy and the parity
verdict are scaffolding around a two-sentence argument. The proportion is wrong in
the way that invites the referee's standard line: "the author has written the
literature review for a paper they have not yet written."

There is one further, hard, non-philosophical obstacle: **the manuscript cites
neither Savitt nor Rovelli** (checked by grep over `main.tex` and
`references.bib`). The priority audit recommended Savitt as "mandatory, in the
introduction and in §4". The working tree still has no citation. A note whose
entire relation to prior work is "Savitt already said this, but about the earlier
formulation" cannot be submitted without citing Savitt; as it stands it would be
rejected on the first read for exactly the reason the project already knows.

---

## 2. The strongest rejection a referee would give

I give the rejection I would actually write, in descending order of force.

**(a) "Savitt already granted (a), so you have not extended his objection; you have
restated it."** This is the killer, and it is stronger than the priority audit's
version ("Savitt targets 2013, you target 2015"). Read Savitt's paragraph in
order. He first says the sustaining-region present is a genuine relativistic
present and *will not necessarily exhaust* Minkowski spacetime — that is (a), in
prose, before Brading wrote it. He then says every dynamical system past, present
or future has such a region, and that this characterises a present, not
presentism. So Savitt's argument is: *grant the per-item bound; the account still
fails to be presentism.* Brading's 2015 revision adds the per-item bound. Savitt's
objection therefore passes through the revision untouched — not "with more force"
(contra `NOVELTY_AUDIT.md` and the priority audit's §9), but *unchanged, because
it was conditional on the very clause added*. The note's headline is then a
non-event: "the 2015 revision does not answer an objection that already assumed
the revision's content."

**(b) "The conclusion is one Brading states herself as an open empirical
question."** Brading 2015, p. 18: the crucial question is whether there are
genuine subsystems smaller than the whole of spacetime, and "Only if there are
such can the version of presentism offered here survive." The note shows that (a)
does not settle this. Brading never said it did; she said it was the condition,
to be settled empirically. To make this a criticism rather than a restatement, the
note must show that (a) is the *wrong kind* of condition — that no empirical
answer to "are there smaller genuine subsystems?" could deliver the global
restriction. The manuscript gestures at this ("the physics does not supply it")
but does not argue it, so the referee sees a burden-shift dressed as a refutation.

**(c) "The formal core is not a result."** "∀i U_i ⊊ W does not imply ⋃U_i ⊊ W"
is true of any family of proper subsets with at least two members. The proof is a
three-element model. A referee will not accept that as the paper's stated
"contribution" (l. 434) even with the honest label "elementary set theory". The
non-implication is a *diagnostic device*, not a finding, and the note currently
puts it where a finding should be.

**(d) "The cost map is a list, not an argument."** Four options, no criterion of
adequacy, no exhaustiveness claim, and one of them (coexistence restrictions)
duplicates Savitt's own co-presence point ("it is unclear under what conditions
two dynamical systems share a present"), which the note does not acknowledge
because it does not cite Savitt. A referee who knows the SEP entry will read the
"repair 2" paragraph as Savitt's sentence with the citation removed.

**(e) "The bridge begs the question."** Treating "avoid the block universe" as
"exclude events from existence" is the premise on which everything rests, and the
manuscript says so. But then the conclusion is conditional on an interpretation
the target does not adopt, which is not how a comment should work: you refute the
target's claim, not a strengthened version of it that you have labelled as yours.

**(f) "The revisionary escape is conceded into victory."** Revisionary option 1
(system-relative existence) is said to "block the coverage objection by changing
the question". If the best repair is conceded to work, the note's conclusion
becomes "Brading's 2015 sentence, read one way, does not establish a thesis she
could get another way" — true, small, and not obviously worth a journal page.

**(g) Proportion and venue.** An eleven-year-old target with five indexed
citations, one sentence long, in a journal that has published no reply; no
engagement with the possibility that Brading would simply accept the conditional.
Referees weigh this.

None of these is an objection to the manuscript's honesty or its quotations. They
are objections to the *claim of contribution*.

---

## 3. What would make it a contribution

Ranked by value per unit of new work, and by whether it is available to this
project without new source archaeology.

**1. A new formal result — but the right one.** Not "local boundedness does not
imply proper union" (trivial, and already Savitt's concession in prose). The
stronger and *unoccupied* result is that **(a) together with (b) still does not
imply a proper union**:

> W = {a,b,c,d}; system 1 has history H₁ = {a,b,c} and present U₁ = {a,b};
> system 2 has history H₂ = {b,c,d} and present U₂ = {c,d}. Then U₁ ⊊ W and
> U₂ ⊊ W (a); U₁ ⊊ H₁ and U₂ ⊊ H₂ (b); and U₁ ∪ U₂ = W.

This matters because (b) is the obvious candidate no-coverage premise, and
nobody in the literature — Savitt included — checks whether it works. It does
not: (b) places events outside *their own* system's present, not outside *every*
present. Two lines, but it closes the defender's best move, and it converts the
note from "the obvious objection, retargeted" to "the obvious objection, plus the
obvious defence, closed". Add the general remark that follows: per-item properness
is coverage-neutral; excluding coverage requires either a joint size-and-cardinality
bound (unavailable from Brading, and physically arbitrary) or a *selection*
principle over systems. That general remark is the note's real theorem-shaped
content, and it is a claim about the *type* of condition needed, not about sets.

**2. A textual discovery — the two objections are different objections.** This is
the most valuable item and the least developed in the current draft. Savitt's
objection, read closely, is a **uniqueness** objection: many system-presents do
not make one present, and co-presence is undefined. The note's objection is a
**coverage** objection: many system-presents may jointly exhaust the history. These
come apart in both directions (presents can be many and not cover; presents can be
few and cover) and they have *different repairs*: uniqueness needs a co-presence
relation or a privileged system; coverage needs a principle of existence-conferral.
The priority audit conflates them — it reads Savitt's "every dynamical system has
a region" as "the coverage premise (C) argued in print", which Savitt's own
"will not necessarily exhaust" contradicts. Correcting that conflation is a
genuine, citable, small contribution, and it is exactly the sort of thing a
specialist venue will take: *the literature has been running two objections
together, and one of them is not answered by anything Brading says.*

**3. A new cost argument — eligibility versus unity.** The `TRILEMMA.md`
constitution/eligibility distinction is the only philosophically substantial idea
in the project, and the paper does not use it. Stated as an argument, not an
assertion: Brading's law-constitutive story explains what makes a system one thing
and how it persists; existence-conferral is a different relation (between a system
and events, or between a system and a domain), and no dynamical fact about unity
fixes which unities confer existence. That is *why* the missing premise is a
selection principle rather than a further bound, and *why* "add actuality" is not
ad hoc. This is the argument that turns burden-shift into diagnosis. It overlaps
Savitt 2006 and Wüthrich 2010 on unrestricted existence, so it must be presented
as a diagnosis of Brading specifically, not as a new meta-ontological thesis.

**4. No new application, and no synthesis for its own sake.** Synthesising
Savitt/Wüthrich/Mason/Balaguer into a "trilemma" would be an interesting survey
and an unpublishable one at this length; the project already concedes the frame is
not novel. Balaguer and Mason are better used as *evidence that the eligibility
route is live*, not as a synthesis target.

**Not sufficient on their own:** a better bibliography (necessary, not
sufficient); a sharper statement of the non-implication; a new name for the
objection.

---

## 4. Venues and formats

Bluntly: there is no venue where the current draft is a plausible accept, and the
realistic set after redesign is small and mid-tier.

- **SHPS-A (the target's own journal).** The only natural home for a discussion
  note on Brading 2015. But eleven years on, with no reply from Brading to
  engage, editors will likely prefer a paper that raises the general issue
  (local presents and the domain of existence) using Brading as the case. Do not
  pitch it as "a comment on p. 17".
- **Synthese / Philosophy of Science / BJPS.** All publish occasional discussion
  notes, all of them are replies in live disputes or carry a general lesson. A
  note on one sentence of a 2015 paper will not clear the desk. Low probability;
  not zero if the eligibility argument is strong and general.
- **Analysis / Thought.** Analysis takes ~3,000-word self-contained arguments
  with a sharp logical core. A version built on the (a)+(b) model and the
  type-of-condition claim could *almost* fit, but Analysis wants the argument, not
  the exegesis, and the exegesis is most of the evidence.
- **Journal for General Philosophy of Science; European Journal of Analytic
  Philosophy; Philosophia; Foundations of Physics.** Realistic. JGPS has a
  discussion format and tolerates careful negative notes on single arguments;
  Foundations of Physics is the best fit if the note is framed as being about the
  logic of local-present proposals rather than about Brading's text. Expect slow,
  low-visibility, and a real chance of "too exegetical".
- **Conference.** Not viable. A "comment" talk needs a controversy; there is
  none here.
- **Preprint (PhilSci-Archive) regardless.** It costs nothing and establishes
  the priority date for the (a)+(b) point, which is genuinely unoccupied.

Honest odds after full redesign: perhaps one specialist acceptance in three
attempts, in the 3,500–5,000 word range, over two years. Odds as currently
framed: near zero anywhere that matters.

---

## 5. Concrete outline of the strongest defensible note (~1,000 words of outline)

**Working title: "Two objections to Brading's local present, and why P1\*\* answers neither."**
Target length 3,800–4,200 words including notes. Everything below is stated as
the note's own claims, with the Savitt debt declared in the first two pages.

**§1. The texts (≈450 w).** Quote P1\*\* in full (2015, p. 17); quote "all we need
is (a)"; quote in the same breath the hedge ("calls the ontology of a block universe
into question") and the p. 18 survival condition. Then quote Savitt §3.3 (2021
revision) in full. State the thesis in one sentence: *the 2015 revision adds the
one clause Savitt's objection already concedes, so it cannot answer that
objection; and neither (a) nor (b) can supply the global restriction, because the
missing premise is a principle of existence-conferral, not a bound on the extent
of presents.* Declare immediately: the objection is Savitt's, published in 2021;
this note's contribution is the distinction in §2, the model in §3, and the
diagnosis in §4 — no more.

**§2. Savitt's objection is a uniqueness objection, not a coverage objection (≈750 w).**
Reconstruct the paragraph step by step and show that its structure is: *grant the
per-item bound → every system in the history has a present → so you have many
presents and no single present → co-presence is undefined.* Note the exact phrase
"will not necessarily exhaust all of Minkowski spacetime": that is (a)'s content,
conceded before (a) was written. Conclude that Savitt's objection is about the
*plurality* of presents, and that it is not the same as the coverage objection.
Then the payoff: the field (including the project's own priority audit) has read
Savitt as supplying the coverage premise; he does not, and his concession is
evidence against that reading. Two objections, two repairs: uniqueness → a
co-presence relation or a privileged system; coverage → a selection principle over
existence-conferring unities. Say plainly which one the note is about.

**§3. Neither (a) nor (b) excludes coverage (≈700 w).**
Proposition 1: local boundedness does not imply proper union (three-element
model; label it elementary and say why it is stated anyway — because the
sufficiency sentence needs exactly this). Proposition 2: **(a) and (b) together do
not imply proper union** — the four-element, two-system model in §3 above, with
(b)'s histories explicit. Explain why (b) is the natural no-coverage candidate and
why it fails: (b) puts events outside their *own* system's present, not outside
every present; a defender needs an event outside *all* presents, which neither
clause delivers. Add the general remark: per-item properness is coverage-neutral;
non-coverage requires a joint size-and-cardinality constraint or a selection
principle; Brading supplies neither, and the former is arbitrary in a way the
latter is not.

**§4. The missing premise is eligibility, not extent (≈1,000 w).**
This is the load-bearing section and must be argued, not asserted. (i) Unity is a
property of a system; existence-conferral is a relation between a system and
events; a law-constitutive account of the first does not determine the second.
(ii) Hence any further condition of the same form as (a)/(b) is the wrong type:
it constrains *how big* each present is, while the question is *which* presents
count. (iii) Run Brading's own totality note (2013, p. 1105 n. 3) as a clean
dilemma: if the totality is a genuine unity and its present is the whole history,
(a) is violated; if (a) holds of it, coverage holds; if the totality is not a
unity to which P1\*\* applies, then P1\*\*'s quantifier is restricted and the
event-domain question cannot even be posed. The current draft garbles this into
"internal pressure" — do it properly, one horn at a time. (iv) Answer the
"genuine-systemhood supplies the criterion" reply: genuine-systemhood is a unity
criterion, and the dilemma in (iii) shows it does not decide conferral.

**§5. Costs, ranked (≈550 w).** Three routes only, and rank them: (R1) an
eligibility/actuality premise — a metaphysical posit, not derivable from dynamics,
and it must include the further claim that the actual unity is not the maximal one
(the current draft omits this conjunct); (R2) a co-presence relation — answers the
uniqueness objection, not coverage, and risks reinstating a global present
(Saunders); (R3) frame- or perspective-relative existence (Balaguer, Mason) —
changes the subject, and then the disagreement with eternalism becomes verbal
(Savitt 2006; Wüthrich 2010). State that the routes are not interchangeable
because they deny different things. Concede primitive actuality as a coherent
position, not as a "cost" — the current wording begs the question against the
primitivist.

**§6. What this shows and what would defeat it (≈300 w).** Shows: (a) is
coverage-neutral; the 2015 revision does not answer Savitt's objection because it
adds only what that objection concedes; the needed premise is a selection
principle. Does not show: that Brading's actual family covers W; that presentism
fails. Falsifiers: a proof that no family of law-constituted presents can cover W;
a demonstration that (a)/(b) plus dynamical facts already yield a selection
principle; a reading of "all we need is (a)" on which the block is *not* the
thesis that every event is equally real.

**Do not include:** the parity verdict (unsupported and, per the logic audit,
self-contradictory); the Stein paragraph (source note, no work done); the
Saunders/Pooley survey (two paragraphs at most, in §5, as constraints on R2);
the four-way existence/presence/unity/endurance taxonomy (one sentence); the
interaction-passage discussion (a footnote); every self-addressed sentence
("The paper therefore withdraws…", "the contribution is…", "the accompanying
novelty audit").

**If the author will not make these changes**, the honest recommendation is to
abandon the standalone note and fold §2–§4 into the larger eligibility paper,
where the Brading case study is evidence rather than a claim to stand alone.

---

## 6. Checks performed and limits of this assessment

Checks: Savitt §3.3 read live on 2026-10-21 (entry revision date 6 Oct 2021
confirmed on the page); `main.tex` grepped for Savitt/Rovelli (absent); word count
computed (≈3,360); the current working-tree diff against `c4141d0` read to see
which audit items are already addressed. I did not re-read Brading 2013/2015 in
the original; my quotations are taken from `main.tex` and confirmed against the
source audit's page-image checks. I did not read Balaguer's or Mason's bodies, did
not check journal editorial policies on discussion notes, and did not search for a
further critique that would make even the redesigned note unoriginal. The
probability estimate in §4 is a judgement, not a measurement.
