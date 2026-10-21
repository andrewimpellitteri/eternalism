# Logic audit: *Local presents and the block*

Independent audit of `paper/main.tex` at commit `5a9ec90` (428 source lines;
compiled here to 8 pages, no unresolved references, no overfull boxes).
Auditor: subagent, philosophical logic lane. Date: 21 October 2026.

Scope: the argument, not the bibliography. Exact quotations were checked
against the full text of Brading 2013 (public copy, SHA-256 `c93ca072…`) and
Brading 2015 (copy, SHA-256 `7caceae7…`), both matching the project source
record; Clifton–Hogarth 1995 Theorem 1 was checked against the local scan.
Saunders and Pooley were **not** independently re-read (PhilSci-Archive
returned HTTP rejections); their use is assessed against the project's
recorded quotations at the depths that record states. Line numbers below are
those of the 428-line file at `5a9ec90`.

---

## 1. Verdict

**Needs revision.** The core move is sound: clause (a) is a per-thing bound on
the extent of each present, so it is a non-implication from (a) to a proper
union, and the paper now hits Brading's own stated sufficient condition rather
than a formulation she had abandoned. The retarget is real and the quotation
discipline is now good: P1\*\*, P1\*, the interaction passage, notes 3, 6 and 7,
and the p. 1109 present/defeat sentences all match the sources verbatim.

The paper nevertheless still states more than it has argued. Three defects are
load-bearing.

1. The verdict "Brading's 'all we need is (a)' is … insufficient as stated"
   (l. 395; abstract l. 25–27) silently converts Brading's aim — *avoid the
   block universe* — into *secure a global existential restriction*. She never
   equates these, and her own p. 17 sentence is about the weaker aim ("this
   calls the ontology of a block universe into question"). The bridge needs one
   argued paragraph, and it is missing (issue A1).
2. The coverage premise (C) is honestly introduced as a premise and honestly
   downgraded in one paragraph (l. 240–242), but the downgrade is not carried
   into the abstract, the conclusion or §6, and one of the two "textual routes"
   to (C) does not support coverage at all (issue A2).
3. §6's parity verdict is a global comparative claim about "presentism" and
   "the physics", derived from one formulation's local-boundedness point, with
   no comparison made, and its first sentence ("The conclusion is not that the
   evidence is silent") contradicts the verdict it introduces (issue A3).

None of these is fatal to the non-implication, which is correct and worth
publishing. Each fix is local (§1, §4.1, §6, §8, §7-Pooley, plus deletion of a
few authorial leftovers). With them, the paper is a defensible short negative
result. Without A1 and A3, a referee will say the verdict is a re-description
of Brading's aim plus a parity claim she never had to accept.

---

## 2. Findings on the assigned questions

**Q1. Is clause (a) correctly identified with local boundedness? Is (b)
correctly an extent/endurance claim?** Substantially yes, with two caveats.

- (a) reads "the spatiotemporal extent of the present for that thing is … (a)
  less than the entire spatiotemporal evolution of the universe as represented
  in Minkowski spacetime" (Brading 2015, p. 17, verified verbatim). The paper
  renders this as `∀i U_i ⊊ W` (l. 64–65, 204–208). Brading's own gloss on the
  same page supports the identification: such a present "is local, in being a
  spacetime region less than the extent of the entire 'block'". The
  identification is therefore better warranted than the paper shows — the
  gloss is not quoted. Two caveats: (i) "less than" is an extent comparison,
  and `⊊` assumes containment, so the formalisation is a (charitable)
  strengthening, not a transcription (C2); (ii) P1\*\* quantifies over
  *things*, the formalisation over *systems* (C2). Neither affects the
  non-implication's validity; both should be marked.
- (b) reads "less than the entire spatiotemporal evolution of that thing"
  (p. 17, verified). It is indeed a per-thing extent claim and not a domain
  claim, so the paper's core contrast survives. Calling it an
  "endurance/presence claim" (l. 120) is loose under the paper's own §2.2
  definition of endurance ("persistence of that unity through change", l. 115):
  (b) says nothing about persistence through change; it relates the present's
  extent to the thing's whole history (C3). Brading's own optionality remark is
  quoted accurately (l. 183–186).

**Q2. Does the coverage objection threaten (a), or only the claim that (a)
suffices for a global restriction? Is (C) argued, assumed, or honestly
downgraded?** It threatens only the sufficiency claim. The objection is a
non-implication: `∀i U_i ⊊ W ⊬ ⋃U_i ⊊ W`. It does not touch (a) itself, and it
does not show that Brading's actual family covers `W`. The paper says exactly
this at l. 231–242 ("exact as a non-implication and conditional as an
objection"), which is correct and is the right target, since Brading's sentence
is a sufficiency claim. So the answer to Q2 is: the objection is correctly
scoped in §4.1.

Coverage (C) is **stated as a premise, sketched, and not established**. The
status is honestly stated in l. 240–242 and dishonestly transcended at l. 25–27
and l. 392–396. The two "textual routes" (l. 244–259) do not do what the
sentence promises. Route 1 (n. 3, the totality) is the only route with real
force, and it is mis-described: on its first horn the totality's present *is*
`W`, which gives coverage directly; on its second horn P1\*\*'s universal
quantifier is empty. The paper flattens both into "internal pressure" and never
connects the horn to (C). Route 2 (n. 6) is not evidence for coverage: "things
whose dynamically sustained regions of spacetime are much smaller than mine …
come into and go out of existence on much shorter timescales than I do"
supports a plurality of nested, short-lived presents, not presents distributed
over all of `W`. The sentence "it is enough to show that (C) is not excluded by
Brading's premises" (l. 258–259) conflates "consistent with" with "supported
by", which is the same conflation the paragraph is trying to avoid.

**Q3. Does the conclusion follow? Is the parity verdict supported?** The
conclusion follows in its hedged form: "does not by itself secure" is exactly
what a non-implication plus a consistent covering family establishes (modulo
Q7's domain point). It does **not** follow in the form the abstract and
conclusion give it: "Brading's own stated sufficient condition does not secure
a global existential restriction" is fine as a claim about (a), but
"'all we need is (a)' is therefore insufficient as stated" is a claim about
Brading's sentence, and her sentence is about *avoiding the block universe*.
That she needs a *global restriction* to avoid the block is the paper's
interpretation, correct or not, and it is asserted rather than argued (A1).

The parity verdict is not supported. It is a global claim ("presentism over
eternalism"), it is not derived from any comparison (no evidence set, no
likelihood, no explanatory comparison is attempted in §6), it is not marked as
conditional on (C), and its universal "any advantage" is not established by an
enumeration of four repair options. The first sentence of §6 ("The conclusion
is not that the evidence is silent") is the negation of the verdict that
follows. Both were flagged in external-2 M8 and both remain.

**Q4. Are the repairs correctly separated? Maximal-interacting-unity handled
fairly? Primitive-actuality answered or conceded?** The separation is now
correct: restoring repairs 1–2 are distinguished from revisionary options 1–2
(l. 298–333), which fixes external-2's m8. The maximal-interacting-unity
candidate is engaged and not strawmanned: the paper names it as Brading's own
candidate (l. 306–310), runs two horns, and says "the cost is real". Two
defects: the paragraph contradicts itself ("the selection principle is not
derived from the physics or from dynamical unity alone", l. 305–306, versus "A
maximal-interacting-unity principle is a dynamical selection principle", l.
309–310), and the dichotomy ignores non-unique maximal unities (B6). The
primitive-actuality reply is **conceded** — formally satisfying `REFRAME.md`
§7's "answer or concede" obligation — but the concession is framed as a cost,
which is question-begging against the primitivist, and the reply as stated is
incomplete: even granting primitive actuality, one still needs that the actual
unity is not the maximal one (B5).

**Q5. Is system-relative existence really withdrawn? Does the interaction
passage do the work claimed?** The withdrawal is real in substance: the abstract
(no relativized reading), §1 (l. 71–77), §4.2 (l. 280–288), §5 (revisionary
option 1 assigned to Balaguer and Mason), and §6 make no relativized-existence
claim about Brading. Two residues: (i) the withdrawal is narrated as an
editorial act inside the argument ("The paper therefore withdraws the stronger
attribution", l. 287), which belongs in a response letter, not a paper (B1);
(ii) the passage is now asked to support "no event is excluded merely by lying
outside a local present" (l. 285–286), which is more than it says — its scope
is "whatever we interact with" and "the rest of that world", i.e. the
interacting world, not every event in `W`. The paper itself notes that "exists
relative to me" is *glossed by interaction* (l. 283–284), and that gloss makes
the co-presence reading (interaction links make the son present to me) at least
as natural; on that reading the passage says nothing about events outside every
present. The passage supports the weaker and still useful claim that Brading's
gloss treats things beyond one's own here-and-now as real, and it is in tension
with P1\*\*'s restriction rather than merely neutral about it (B2).

**Q6. Are Saunders and Pooley at their strongest? Is the "non-trivial"
qualifier marked? Does Pooley slide from existence to passage?** Saunders is
reconstructed at close to his strongest available form: the equivalence
requirement, the symmetry requirement, the Clifton–Hogarth trichotomy, the
public/uniqueness reason, and the two-horn mapping. The "non-trivial" qualifier
is explicitly marked as the paper's own strengthening (l. 365–367) — that is
correct and should be kept. The reconstruction has weakened on evidence: the
"public, non-provincial 'whole of reality'" reason (l. 374–376) now carries no
quotation and no locator, unlike external-2's version.

Pooley **still slides**, in a new form, and now inconsistently. The paragraph
says "she is not a candidate for Pooley's route" and two sentences later that
"Brading's local present supplies a deflationary one unless an actuality
premise is added" (l. 383–387). A deflationary *analysis of passage* is not
supplied by a local *present*; Brading says nothing about passage at all. And
"the coverage point is a precondition for any non-deflationary hard route" is
asserted, not shown: Pooley's hard route eschews a global Now and turns on the
open future, so it is not obvious that a point about the domain of existence is
a precondition for it (B3).

**Q7. Remaining overclaims, question-begging, category errors.** Overclaims:
§6 in full (A3); "no event is excluded merely by lying outside a local present"
(B2); "stronger than a catalogue" (l. 352); "this is the paper's real
conclusion" (l. 332–333 — addressed to a reviewer, not a reader). Question-
begging: calling primitive actuality a "cost" (B5); treating "avoid the block
universe" as equivalent to "exclude events from existence" (A1); treating the
tenseless event domain as the neutral frame without saying that a quantifier-
restriction reading of P1\*\* would make the coverage argument inexpressible
(B4). Category errors: "existence" is a *claim* in §2.2 (l. 109–110) and a
*predicate* in §5–§6 (C4); a present is a *region* and co-presence is a
*relation*, but §7 compares them ("A system-relative present is not an
equivalence relation … it is a region assigned to a system", l. 369–371) (C8).

---

## 3. Major issues

### A1. The verdict rests on an unstated bridge from "avoid the block" to "global existential restriction"

**Locations:** abstract l. 25–27; §1 l. 62–69; conclusion l. 392–396.

**Text of the target (verified, Brading 2015, p. 17):** "In order to avoid the
block universe, all we need is (a)." Earlier on the same page and in the same
section, her stated effect of the smaller-than-universe condition is: "if it
turns out that the size of the spatiotemporal region necessary to sustain a
particular dynamical system is less than the entire spatiotemporal history of
the universe, then this calls the ontology of a block universe into question."
The paper never quotes this second sentence and never argues that "calling the
ontology of a block universe into question" requires excluding events from
existence.

**Diagnosis.** The paper's non-implication is about (a) and coverage; its
headline verdict is about Brading's sentence; the two are joined only if
"avoiding the block universe" means "there is a global existential restriction
(not every event exists)". That identification is defensible — a block universe
just is one in which every event is equally real — but it is an interpretive
premise, and Brading's own wording is deliberately weaker. As written, a
defender can reply: "(a) does what I said — it locates a present smaller than
the universe's history and thereby blocks the inference to the block; I never
claimed it excludes events." The paper would then be attacking a claim its
target does not make, which is precisely the criticism external-2 made about
the previous draft, in a new place.

**Fix (choose one, preferably (i)).**
(i) Add a short bridge paragraph in §1 or §4.1: define the block universe as the
thesis that every event is equally real; quote Brading's "doesn't seem to save
anything that the presentist was hoping to save" (2015, p. 17) as the statement
of what presentism needs; argue that if every event belongs to some
system-present then, in aggregate, the entirety is present as of some system,
which is the outcome Brading says saves nothing. Then the verdict follows.
(ii) If the bridge cannot be defended, restate the verdict as "P1\*\* (a)
secures at most a present that is proper relative to the whole; it does not
secure the presentist restriction that motivated P1", and drop the claim that
Brading's sentence is false as stated.

Either way, quote the "calls the ontology of a block universe into question"
sentence so the reader sees the exact target.

### A2. (C) is asserted and sketched; the abstract and conclusion revert to the unqualified verdict

**Locations:** §4.1 l. 231–264; abstract l. 25–27; conclusion l. 392–396.

**Diagnosis.**
- The premise is named and its logical role is stated correctly (l. 234–242).
  That is a genuine improvement and should be kept.
- Route 1 (l. 246–251) is the only real route to (C): if the totality is a
  genuine unity, its sustaining region is `W`, so `⋃U_i = W`. The paper instead
  presents it as "internal pressure", which is true but weaker and misses that
  the first horn *establishes* coverage. The second horn ("the totality is not a
  thing to which (a) applies", l. 250) is not a route to (C) at all; it is an
  objection to P1\*\*'s quantifier.
- Route 2 (l. 253–259) does not support coverage. Note 6 gives nested, shorter-
  lived presents inside mine; nothing in it places presents in the far future or
  far past. "A plurality of nested, short-lived things whose presents populate
  the history" is the paper's inference, not Brading's text.
- "It is enough to show that (C) is not excluded by Brading's premises"
  (l. 258–259) is an equivocation: consistency of (C) with the premises is not
  support for (C), and the objection needs the latter.
- The self-addressed sentence at l. 262–264 ("The paper should not call the
  objection 'exact' …") is a leftover instruction, already satisfied at l. 241.
  It must be deleted (B1), and the earlier "exact as a non-implication" can
  stand.

**Fix.** Call the first horn by its name: a route to (C) conditional on the
totality being a law-constituted unity. Drop or downgrade route 2 to what it
supports ("Brading does not exclude a plurality of presents; that is
compatible with, but does not establish, coverage"). Delete l. 262–264 and
replace with one sentence: "Nothing in Brading's text establishes or excludes
(C); the objection is a burden-shift, and the burden is to show that the actual
family is proper." Then make the abstract and conclusion say the same thing:
"(a) does not, by itself, secure the restriction; whether the restriction holds
depends on a no-coverage premise Brading neither states nor argues."

### A3. The parity verdict is an unsupported global comparative claim, and §6 contradicts itself

**Locations:** §6 l. 342–355; tension with §1 l. 71–73.

**Diagnosis.**
- "On the P1\*\* (a) reading, the physics does not favor presentism over
  eternalism" (l. 347) is scoped to "the P1\*\* (a) reading" but its subject is
  "presentism". Nothing in the paper compares presentism and eternalism as
  total views; the paper's own conclusion (l. 71–73) explicitly says it does not
  claim that every presentism fails. The comparison actually made is:
  P1\*\*-with-coverage is empirically indistinguishable from eternalism at the
  level of events. That supports a claim about *that* formulation, not about
  "presentism".
- "Any advantage presentism can claim is purchased by an actuality or privilege
  premise the physics does not supply" (l. 347–349) is a universal claim. The
  paper enumerates four options (l. 298–340); it does not show that they
  exhaust the space. A preferred-foliation presentism, for instance, is a
  physical posit that the physics does not *supply* but does not obviously
  reduce to "actuality or privilege" in the paper's sense.
- The parity verdict is conditional on (C): if (C) fails, presentism and
  eternalism differ in the event domain, and Brading's p. 18 remark makes that
  an open empirical question. The section never says this.
- "The conclusion is not that the evidence is silent" (l. 344) denies exactly
  what a parity verdict asserts. "This is weaker than exclusion and stronger
  than a catalogue" (l. 352) is a self-assessment, not an argument; a
  conditional tie *is* a catalogue entry unless a comparison has been run.
- "A composite ontology can be favored without excluding every rival" (l.
  352–353) introduces "favored" without a standard of favoring; it is the
  residue of the earlier favoring material (REFRAME §6, external-2 M8) after
  the worked comparison was cut.

**Fix.** Either cut §6 to a single paragraph, or rewrite it as: "Within the
P1\*\* (a) route, and assuming the system-presents cover the history, the
physics supplies no difference between this presentism and eternalism: every
event is present to some system. Any difference must be carried by a premise
the physics does not supply (an actuality or privilege premise, or a
no-coverage claim). No comparison of the two ontologies as total views is
attempted here." Delete l. 344 and l. 352. If the global parity claim is
wanted, it must be argued from something like the trilemma's P/Q/N analysis
(`research/existence-form/TRILEMMA.md`), not asserted from one formulation.

---

## 4. Moderate issues

### B1. Editor-facing and self-referential text left in the manuscript

**Locations:** l. 262–264 ("The paper should not call …"); l. 287 ("The paper
therefore withdraws the stronger attribution"); l. 332–333 ("this is the
paper's real conclusion"); l. 421 ("depths stated in the review record");
l. 424 ("the accompanying novelty audit").

**Diagnosis.** These are addressed to the coordinator or the reviewer, not the
reader. They also document the revision rather than the position, which invites
the reading that the withdrawal and the "exact" downgrade are concessions to
referees. In a submitted article they are defects of register; in a review
cycle they are evidence that the de-drafting is incomplete.

**Fix.** Delete or convert. "The paper therefore withdraws the stronger
attribution" → "The passage does not establish a relativized existential
quantifier" (already said in the preceding sentence; delete). "This is the
paper's real conclusion" → state the conclusion. "review record" and
"accompanying novelty audit" → either give the reader-visible source or cut.
(External-2 m11/m12 flagged the same class; only partly fixed.)

### B2. The interaction passage is used beyond its scope

**Locations:** §4.2 l. 280–288.

**Diagnosis.** See Q5. The passage's scope is the interacting world, not `W`;
the paper's own interaction-gloss observation supports a co-presence reading
under which the son is inside the speaker's extended present, not outside every
present. On that reading the passage does not support "no event is excluded
merely by lying outside a local present".

**Fix.** Weaken to: "Brading's gloss treats things at a distance from one's own
here-and-now as real — 'the rest of that world is as real as we are' — which is
a single-domain claim about the world we interact with. It does not state, and
does not support, a restriction that excludes events; and read as a claim that
the son in London is real while outside my local present, it is in direct
tension with P1\*\*'s 'exists only presently'." The tension point strengthens the
negative verdict and costs nothing.

### B3. The Pooley paragraph slides from existence to passage and contradicts itself

**Locations:** §7 l. 378–388.

**Diagnosis.** "She is not a candidate for Pooley's route" (l. 383–384) and
"Brading's local present supplies a deflationary one unless an actuality
premise is added" (l. 386–387) cannot both be right. A local present is not an
analysis of passage. The "precondition" claim (l. 384–386) is asserted: Pooley's
hard route is about the open future and eschews a global Now, and no argument
shows that the domain-of-existence point bears on it.

**Fix.** Keep the concession and make it clean: "Pooley's question is about
objective passage; Brading's is about the extent of a present and the domain of
existence. Nothing in this paper bears on his route, and the coverage point does
not transfer to it. What can be said is only that a view which adds an actuality
premise would owe an account of how that premise relates to passage — which is
Pooley's question, not an answer to it." Delete "supplies a deflationary one".

### B4. Bearer-neutrality of the coverage point is asserted, not shown — and the argument depends on the event domain

**Locations:** §2.3 l. 124–133; §2.2 l. 118–122.

**Diagnosis.** The paper says it does not matter whether the bearers are events
or unities ("the coverage point concerns the extents, not the category of the
bearers"). That is not obvious, and in one direction it is false as stated: on
Brading's own "what exists (what is real) are the genuine unities" (2015,
p. 17), every unity has a present by P1\*\*, so no unity is ever excluded
regardless of coverage; the exclusion question only bites for *events*. The
coverage argument therefore is an argument about the event-domain rendering, and
it should say so. This is not a weakness — the unity reading makes the negative
result stronger, since P1\*\* then cannot restrict the domain of things at all —
but the current sentence hides the dependence instead of stating it.

**Fix.** Replace the last sentence of §2.3 with: "On the event reading, coverage
shows that no event is excluded. On the unity reading, P1\*\* cannot exclude
anything either: each unity has a present by definition, so every unity is
admitted. Either way the restriction fails; the event reading is used because
it is the only one in which the restriction can be stated at all." Also state
that the comparison is stated neither as tensed nor as tenseless existence, or
say explicitly that the argument uses a tenseless domain and why that does not
beg the question against a quantifier-restriction reading of P1\*\*.

### B5. The primitive-actuality reply is conceded, but its "cost" begs the question, and the reply is incomplete

**Locations:** §5 l. 335–340.

**Diagnosis.** "Its cost is that the physics does not supply it" is exactly what
the primitivist denies is a cost: on her view, actuality is not the kind of
thing physics supplies, so the absence is a category fact, not a deficit. The
paper's verdict line ("any advantage … purchased by an actuality or privilege
premise the physics does not supply") then reads as a criticism only to someone
who already requires a physical derivation. Additionally, the reply as stated
("the privileged system is simply the actual one") does not by itself avoid the
block: if the actual unity is the maximal one, its present is the whole history
and the view is the block. The primitivist needs a second conjunct — that the
actual unity is not the maximal unity — which is precisely the empirical
question Brading leaves open at p. 18.

**Fix.** Mark the concession explicitly: "This reply is not refuted here; it
shows that the verdict is conditional on the demand that physical
considerations adjudicate the matter." Add the second conjunct and its cost.
Then the verdict can say, without begging the question: "granting primitive
actuality, the view still needs a substantive claim about which unity is actual,
and that claim is not supplied by dynamical unity."

### B6. The maximal-interacting-unity paragraph contradicts itself and ignores non-unique maxima

**Locations:** §5 l. 303–312.

**Diagnosis.** "The selection principle is not derived from the physics or from
dynamical unity alone" (l. 305–306) versus "A maximal-interacting-unity
principle is a dynamical selection principle" (l. 309–310). The resolution the
paper needs is available: the *interaction* content is dynamical; the
*maximality* clause is a structural axiom, and it is the axiom that does the
selection. The dichotomy "if the maximal unity is selected … else independent
defense" also presumes a unique maximal unity; with several maximal interacting
components the principle selects a family, and the paper's conclusion ("its
present is the whole history") does not follow automatically. And "its present
is the whole history" is the paper's inference from the totality case, not
Brading's statement about maximal interacting unities; it should be labelled.

**Fix.** Distinguish dynamical content from the maximality axiom; note the
multiple-maxima case; cite p. 1109's defeat condition for the inference to `W`;
conclude only that the principle does not yield a proper union without an added
claim, which is the paper's real cost.

---

## 5. Minor issues

- **C1. The proof of the Proposition is not valid as stated** (l. 226–229).
  "Let `W` be a nonempty set and take two overlapping proper subsets whose union
  is `W`" fails for `|W| = 1`, and for `|W| = 2` only a disjoint cover exists, so
  the added "overlapping" is gratuitous. Fix: "take `W` with three points and
  the proper subsets `{a,b}`, `{b,c}`", and note that the model is
  set-theoretic, not a dynamical family.
- **C2. `⊊` is a regimenting step, not a transcription of "less than";
  and the quantifier runs over systems while P1\*\* runs over things**
  (l. 64–65, 126–130, 204–208). Say that the formalisation is the strongest
  natural reading of (a), so the non-implication holds a fortiori; and note that
  "every thing" includes things that are not dynamical systems, or say that on
  the law-constitutive identification things are unities with presents.
- **C3. The "(b) is an endurance claim" labelling is loose** (l. 118–122). (b)
  relates the present's extent to the thing's whole history; it says nothing
  about persistence through change as §2.2 defines endurance. Call it an
  extent-of-present claim. Optionally note the tension: (b) presupposes a
  thing-history longer than its present, which is odd for a formulation whose
  first clause says the thing exists only presently.
- **C4. §2.2 mixes categories** (l. 108–116): existence is given as a *claim*,
  presence as a relation, unity as a property, endurance as a process; and
  "existence" becomes a predicate ("exists-for-system-*i*") in §5. Define
  existence once as a domain-membership predicate and keep it.
- **C5. §5 repair 2's cost is the wrong cost** (l. 314–320): "the union of the
  family need not be a single present" is irrelevant to whether the union is a
  proper part of `W`. The real cost is that the maximal-family construction has
  no constraint that bounds the union, so it can still be `W`; say that.
- **C6. The Stein paragraph's role and antecedent are unclear** (l. 188–198):
  "The local-present strategy inherits this distinction" has no clear
  antecedent (the theorem/proof distinction, or the local/global definiteness
  distinction?). Add one clause stating what the section contributes to the
  coverage argument (it appears to contribute a source note only).
- **C7. Saunders's public-uniqueness reason lacks a quotation and locator**
  (l. 374–376); external-2 had it quoted at preprint p. 1. If the archive copy
  is unavailable, say "paraphrase" or cite the published S-page version.
- **C8. Region/relation category slip in the Saunders horn** (l. 369–371): a
  region is not a relation, and the relevant object for Saunders is the
  co-presence relation. Rewrite: "Brading assigns a region to each system and
  does not define a co-presence relation at all; so she neither satisfies
  Saunders's requirement nor claims to."
- **C9. The Q-form (quantifier-restriction) route is named in §8 but not costed
  in §5** (l. 300–301 versus l. 411–412). "Two repairs attempt to restore it"
  reads as an enumeration; the trilemma analysis identifies a third route —
  restrict the quantifier to the present — whose cost is a global present or
  privileged domain. Add it as a restoring repair with that cost, or say the
  list is not exhaustive and why.
- **C10. P1\* quotation wording** (l. 173–177): the quoted text "dependent on
  the dynamics" matches 2015, p. 17, not 2013, p. 1110 ("dependent on
  dynamics"). Both are cited. Cite the version quoted.
- **C11. Title/abstract**: "source-grounded negative result" is fine; but
  "does not exclude the family of system-presents covering the whole history"
  (l. 24–25) reads as if the paper excludes something. "does not exclude the
  case in which the system-presents cover the whole history" is clearer.

---

## 6. What is sound and should not be lost

- The non-implication and its scoping (l. 231–242). This is the paper's real
  contribution and it is correct.
- The retarget at P1\*\* and the quotation discipline. Every Brading quotation
  checked is verbatim; the one wording discrepancy is C10.
- The four-way distinction as a diagnostic device (despite C4).
- The separation of restoring repairs from revisionary options.
- The explicit "what would change the verdict" paragraph (l. 407–414); it is
  correctly stated and should survive the revision.
- The Saunders "non-trivial" marking. Keep it exactly as is.
- The non-claims in §1 and §8, and the refusal to claim novelty. These are
  correct and are what makes the paper's modesty credible.

---

## 7. Recommended revision order

1. A1 (bridge from "avoid the block" to the restriction) — this determines
   whether the headline verdict is true as stated.
2. A2 (state (C) once, promote the totality horn, delete the n. 6 route's
   overreach and the self-instruction) and propagate the hedge to the abstract
   and conclusion.
3. A3 (cut or scope §6; delete l. 344 and l. 352).
4. B1 (delete editor-facing text), B3 (Pooley), B2 (interaction passage),
   B5 (primitive actuality), B6 (maximal unity), B4 (domain).
5. C1–C11.

After 1–3 the paper's verdict is either supported or honestly weakened; after
4–5 it reads as a paper rather than a reply to referees.

---

## 8. Text checks performed

| Paper claim | Source | Result |
|---|---|---|
| P1\*\* full quotation (l. 50–57) | Brading 2015, p. 17 (full text, hash `7caceae7…`) | Verbatim |
| "In order to avoid the block universe, all we need is (a)" (l. 59–60) | Brading 2015, p. 17 | Verbatim |
| (b) optional; "should be included if we also deem it important…" (l. 183–186) | Brading 2015, p. 17 | Verbatim; paraphrase accurate |
| "doesn't seem to save anything that the presentist was hoping to save" (l. 181–182) | Brading 2015, p. 17 | Verbatim |
| "calls the ontology of a block universe into question" | Brading 2015, p. 17 | Present in source; **not used** in paper (A1) |
| P1/P2 (l. 86–88) | Brading 2013, p. 1101 | Verbatim |
| Present as sustaining region (l. 161–162) | Brading 2013, p. 1109 | Verbatim |
| Defeat condition (l. 166–168) | Brading 2013, p. 1109 | Verbatim |
| P1\* (l. 173–177) | 2013, p. 1110 / 2015, p. 17 | Accurate, but wording is 2015's (C10) |
| Interaction passage (l. 271–277) | Brading 2013, p. 1110 | Verbatim with ellipsis; scope over-read (B2) |
| n. 3 totality (l. 246–248) | Brading 2013, p. 1105 n. 3 | Verbatim |
| n. 6 smaller things (l. 253–255) | Brading 2013, p. 1109 n. 6 | Verbatim; inference to coverage not supported (A2) |
| n. 7 no determinate relations (l. 135–137) | Brading 2013, p. 1109 n. 7 | Verbatim |
| Stein theorem hypotheses (l. 189–196) | Project printed verification, p. 149 | Matches record |
| "non-trivial" as our strengthening (l. 365–367) | Saunders 2000, p. 3 via project record | Correctly marked |
| Clifton–Hogarth trichotomy (l. 368) | Local scan, Theorem 1, p. 365 | Confirmed: past chronological, past causal, universal |

No invented quotation was found. No formal error was found in the Proposition
itself (only its proof, C1). The compiled document is 8 pages with no
unresolved references and no overfull boxes; page count and pagination were not
otherwise inspected.
