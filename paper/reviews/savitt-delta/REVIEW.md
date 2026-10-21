# Savitt delta audit: does anything survive "a characterization of a relativistic present, not relativistic presentism"?

Independent source audit (subagent), not a referee's report on the paper's
philosophy. Date: 2026-10-21. Target: `paper/main.tex` as it stands in the
working tree (commit `268b22f` plus uncommitted edits), the priority audit at
`paper/reviews/p1-priority-audit/REVIEW.md`, the logic audit at
`paper/reviews/p1-logic-audit/REVIEW.md`, and the novelty verdict in
`research/existence-form/NOVELTY_AUDIT.md`.

The question is narrow: given Savitt's published objection, what is left that
the paper adds, and is it enough to publish as a standalone article.

**Answer in one line: the increment is a trivial extension, verging on a
restatement, and the standalone paper should be dropped.**

---

## 1. Sources and read depths

| Source | Locator | Read depth | Notes |
|---|---|---|---|
| Savitt, "Being and Becoming in Modern Physics", *SEP* | §3.3 "Localizing Time", <https://plato.stanford.edu/entries/spacetime-bebecome/#LocaTime>; first publ. 11 Jul 2001, substantive revision 6 Oct 2021 | **full-text** of §3.3 (all three Brading-touching paragraphs and the section's remainder) | Read live entry; every quotation below copied from it |
| Same, archived editions | `archives/{fall2014, spr2018, win2020, sum2021, fall2021, win2021, spr2022, fall2022, win2022, fall2023, win2024, fall2024, win2025, fall2026}` | **full-text** search of each for the section and the passage | Dating check in §2.4 |
| Same, rest of entry | bibliography; full-text keyword search | **discovery** (keyword search: "Brading", "2015", "exist", "suffic", "quantif", "domain") | Basis for the negative claims in §2.3; not an argument-level read of §1–§3.2 |
| Brading 2013, "Presentism as an Empirical Hypothesis" | *Phil. Sci.* 80, 1101–1111; public copy, SHA-256 `c93ca072e14c4fd0f1c638ff960db17847231479ec9bf168cf0d69f9644bb054` | **full-text** (11 pp.) | Hash matches `paper/SOURCE_AUDIT.md`; text extracted with macOS PDFKit |
| Brading 2015, "Physically Locating the Present" | *SHPS-A* 50, 13–19; public copy, SHA-256 `7caceae74aebe28d1775561cd307dce50f912570eb1a7f9a709d70c699b08f6b` | **full-text** (7 pp.) | Hash matches `paper/SOURCE_AUDIT.md`. The PDF's text layer drops the `fi`/`fl` ligatures ("signi cant", "speci c"); quotations below have them restored and are otherwise character-faithful |
| *SEP*, "Presentism" | rev. 12 Feb 2026 | **discovery** (keyword search) | Zero occurrences of "Brading"; zero of "local present". Not a second site of the objection |
| PhilPapers records for Brading 2013/2015 | — | **not read** | HTTP 403 (Cloudflare). Unresolved lead, as in the priority audit |
| SerpApi/Google queries | phrases `Brading "all we need is (a)"`, Savitt+Brading phrasings, reply/comment searches | **discovery** | Returned no relevant hit, but the queries were noisy and this is weak evidence; not relied on for any verdict |

Nothing below is quoted from a secondary summary. Where the priority or novelty
audit misquotes or under-quotes Savitt, I say so (§2.5).

---

## 2. What Savitt argues, exactly

### 2.1 The passage, verbatim

§3.3 begins with three paragraphs on Brading, then turns to Stein and Dieks.
The Brading material is the first two paragraphs. Verbatim, with the paragraph
break marked:

> Katherine Brading claimed that with proper attention to the history of
> physics one can find a satisfying version of presentism that does not require
> a global present. If one grounds the unity of objects in dynamical laws, as
> she, invoking DiSalle (2006), claims that Newton did, then she says the
> present can be viewed as "a spatiotemporal region of whatever size is
> necessary to sustain the dynamical system in question." (2013, 1109) Presents
> construed this way will typically be larger than a single point but will not
> necessarily exhaust all of Minkowski spacetime or fall afoul of the relativity
> of simultaneity.

> But this is a characterization of a relativistic present, not relativistic
> presentism. Presumably every dynamical system that has existed, does exist or
> will exist had, has or will have a region of whatever size is necessary to
> sustain it. Furthermore, it is unclear under what conditions two dynamical
> systems share a present. Even if they are intuitively spatially close, what
> sustains one may, or may not, sustain the other. While Brading's suggestion
> might be developed into a way to define a relativistic present, it may not
> help to define presentism in a relativistic context, as she intended.

(Savitt, *SEP*, §3.3, revision of 6 Oct 2021. The only Brading locator in the
entry is "2013, 1109"; the entry's bibliography lists Brading 2013 only.)

### 2.2 The argument, reconstructed

1. **Target.** Brading's claim that a dynamics-relative, non-global present
   yields a satisfying presentism (attributed to Brading 2013, p. 1109).
2. **Concession.** Such presents are extended but need not be the whole of
   Minkowski spacetime, and they do not require a hyperplane of simultaneity.
3. **Thesis.** Therefore the construction is "a characterization of a
   relativistic present, not relativistic presentism."
4. **Ground 1 (population).** Every dynamical system — past, present or future —
   has a sustaining region. So the family of such regions is not sparse; it is
   populated across the whole history.
5. **Ground 2 (co-presence).** It is indefinite when two systems share a
   present, so the construction does not even supply an inter-system relation.
6. **Upshot (hedged).** It "might be developed into a way to define a
   relativistic present" but "may not help to define presentism in a
   relativistic context, as she intended."

The logical shape is: *local boundedness is granted, and presentism is still not
obtained, because (i) every system has such a region and (ii) co-presence is
undefined.* That is the coverage objection plus the co-existence objection,
stated in prose, with the sufficiency of local boundedness denied.

Further confirmation that Savitt classes Brading's present as a *present
definition*: three paragraphs later he writes, "It is also possible to have less
geometrically well-defined shapes as relativistic presents, as with Brading's
presents above and Callender's '*now* patches.' (2017, 2016)". Brading's local
present is thereafter one item on a list of candidate relativistic presents.

### 2.3 What Savitt does not say

Checked by full-text search of the live entry:

- **No Brading 2015.** "Brading" occurs four times in the entry: the two
  occurrences in §3.3 quoted above, one anaphoric "Brading's presents above",
  one in the bibliography (`Brading, K. 2013`). The bibliography has **no**
  Brading 2015 entry, and the entry's four occurrences of "2015" are all
  Dorato–Wittman and Savitt 2009/2020. The 2015 paper is invisible to the entry.
- **No P1, P1\*, P1\*\*, clause (a) or (b), and no "In order to avoid the block
  universe, all we need is (a)."** "P1" does not occur in §3.3.
- **No "sufficient"/"suffices".** The word does not occur in §3.3; the verdict
  is "not relativistic presentism" and "may not help to define presentism",
  which is a denial of helpfulness rather than an analysis of a sufficiency
  claim. He never locates a sentence in Brading that asserts sufficiency.
- **No unions, no coverage vocabulary, no countermodel.** "union" and "cover"
  do not occur in §3.3. His ground is a *population* claim about systems, not a
  set-theoretic claim about the union of presents. He never says the presents'
  aggregate may equal the history, and he never says local boundedness is
  consistent with coverage.
- **No domain regimentation.** "domain" and "quantif-" do not occur in §3.3. He
  does not distinguish things/unities from events as bearers, does not say what
  "exists" ranges over, and does not raise the tensed/tenseless question.
- **No cost map.** No actuality premise, no privileged foliation, no
  relativized existence, no repair menu. (The co-presence remark is a diagnosis,
  not a costed repair.)
- **No engagement with Brading's own empirical hedge or defeat condition.** He
  does not discuss 2013 p. 1109's "if the only dynamical system ... is this
  entirety ... this version of presentism is defeated", nor 2015 p. 18's
  "empirical matter" concession.
- **No claim that Brading is refuted.** The conclusion is doubly hedged
  ("might", "may not").

### 2.4 Dating (my own check, independent of the priority audit)

The section header "3.3 Localizing Time" and the whole passage are **absent**
from `fall2014` (rev. 13 Aug 2013), `spr2018`, `win2020`, `sum2021` and
`fall2021` (all rev. 21 Aug 2017). They are **present, identically worded**, in
`win2021` (rev. 6 Oct 2021) through `fall2026` and in the live entry. First
appearance: the 6 October 2021 revision. There is no earlier SEP edition of this
objection, and no later revision has softened or expanded it.

### 2.5 Quotation fidelity in the two audits

- The priority audit's block quote is a faithful concatenation, but it silently
  merges the end of Savitt's first paragraph with the opening of his second
  ("…relativity of simultaneity. But this is a characterization…"). There is a
  paragraph break there; a block quote should mark it.
- `research/existence-form/NOVELTY_AUDIT.md` quotes the premise-bearing
  sentences but **omits the one sentence that states the conclusion** ("But this
  is a characterization of a relativistic present, not relativistic
  presentism"). That omission makes the overlap look smaller than it is: the
  audit quotes Savitt's ground and drops his verdict.
- Neither audit records that Savitt's ground is *already* the paper's premise
  (C) in the affirmative, nor that Brading 2015 is absent from Savitt's
  bibliography. Both matter for §3 below.

---

## 3. Is the increment genuine, a restatement, or a trivial extension?

### 3.1 The burden

An increment is genuine only if it supplies at least one of: a premise the prior
argument lacks and needs; an inference the prior argument does not make; a
target whose content differs in a way the prior argument cannot reach; a
consequence or cost the prior argument does not draw; or a correction of the
prior argument. Formal restatement of published prose is not, by itself, any of
these.

### 3.2 Test 1: does P1\*\* (a) differ from what Savitt attacks?

The paper's case for a retarget rests on P1\*\* being a *later, stronger*
formulation. The Brading texts do not support that description.

- Brading 2013, p. 1109: "the spatiotemporal extent of the sufficient dynamical
  ground of a given unity might turn out to be much, much smaller than the
  abstract spatiotemporal structure within which the evolution of that unity is
  completely described, or it might be the size of the block universe. This is
  an empirical matter, something to be settled by the progress of science."
- Brading 2013, p. 1110: "So let us begin from the position that there are
  genuine subsystems. This means that the size of the spatiotemporal region
  required to sustain the system is less than the entire block universe, and so
  the present is (at least in the first instance) local, not global."
- Brading 2015, p. 17 (P1\*\* (a)): "less than the entire spatiotemporal
  evolution of the universe as represented in Minkowski spacetime."

P1\*\* (a) is the 2010-page assumption of 2013 ("less than the entire block
universe … local, not global") promoted to a clause of P1\*\* and quantified
over "each and every thing that exists." The substantive content — *each
thing's present is a proper part of the block* — is already in 2013, in the
sentence Savitt cites (p. 1109) and in the sentence that follows it (p. 1110).
The 2015 text adds explicitness and a universal quantifier, not a new
condition. So Savitt's target and the paper's target are the same condition in
two typographic settings.

The only genuine textual difference is that 2013 left the size open as an
empirical disjunction while 2015 makes smaller-than-the-block a requirement —
and Brading immediately re-opens it at p. 18 ("it is an empirical matter
dependent on the details of the dynamics whether conditions (a) and (b) are
satisfied in this, the actual world"). On either edition, then, (a) is an
empirical claim about actual systems, which is exactly what Savitt grants in
"Presumably every dynamical system … had, has or will have a region."

**Result: the retarget does not change the argument's target-content. It
changes the citation.**

### 3.3 Test 2: is the coverage premise the paper's addition?

The paper's second claimed increment is stating (C) explicitly, on the ground
that "Brading does not state (C) or its negation" (`main.tex`, §4.1). That is
true of Brading. It is false of the prior literature: Savitt states (C)
affirmatively, in the sentence the priority audit correctly identifies as the
coverage premise — every dynamical system, past, present and future, has a
sustaining region. The paper cannot present (C) as an unnoticed premise; the
nearest published critique asserts it as its own ground.

Worse for the paper's framing, Savitt's use of (C) is *stronger* than the
paper's. Savitt grants the population premise and concludes that presentism
still does not follow. The paper instead says: (a) does not entail coverage, and
*if* (C) fails the objection is only a burden-shift. So the paper quarrels about
a premise its predecessor gives away, and reaches a weaker conclusion than the
predecessor's. That is not an increment; it is a hedge on someone else's
argument.

### 3.4 Test 3: the sufficiency sentence

This is the one item Savitt does not quote. Does attacking it add anything?

"In order to avoid the block universe, all we need is (a)" (Brading 2015,
p. 17) says that local boundedness suffices for the anti-block aim. Savitt's
verdict — "a characterization of a relativistic present, not relativistic
presentism", and "it may not help to define presentism in a relativistic
context, as she intended" — denies precisely that local boundedness delivers
what Brading intended it to deliver. The 2015 sentence is a one-line statement
of the aim Savitt is already rejecting. Pointing out that the aim is stated in
one sentence in 2015 is a service to readers; it is not a new argument.

The paper's own apparatus does not close the gap either. The logic audit (A1)
found that the step from "avoid the block" to "secure a global existential
restriction" is an interpretive bridge the paper asserts; the paper now states
it as a bridge and offers the reader permission to weaken the verdict. An
argument that needs a bridge, applied to a sentence its predecessor already
rejected on the same ground, is not a new result.

### 3.5 Test 4: what is left — formalisation and domain

Two residues remain, and neither carries publication weight.

- **The non-implication and its countermodel.** `∀i U_i ⊊ W ⊬ ⋃U_i ⊊ W` with
  `W={a,b,c}`, `{a,b}`, `{b,c}`. The novelty audit already concedes this is
  elementary. It formalises Savitt's prose; it does not extend it. It also
  cannot bear the paper's headline, because the headline is about Brading's
  sentence, and the formal fact is about (a) alone (logic audit A1).
- **The event/unity domain dilemma.** Savitt quantifies over dynamical systems
  without fixing whether systems are the bearers of existence or the regions in
  which events exist. On a tenseless event reading, coverage defeats exclusion;
  on the unity reading, every unity has a present by construction and P1\*\*
  excludes nothing; on a tensed reading, presence needs a global now, which is
  what Brading rejects. This is a real observation and it is not in Savitt. But
  it is a clarification of the scope of the objection, and the paper currently
  hides it (logic audit B4) rather than using it — and used properly it weakens
  the paper's own formulation, since it shows the coverage argument is
  expressible only on a reading Brading may reject.

### 3.6 Verdict on question 2

**Trivial extension, verging on restatement.**

Not a verbatim restatement: Savitt never quotes "all we need is (a)", never
mentions 2015, never formalises, never distinguishes domains. But the argument
is the same argument, with the same premise and the same conclusion, applied to
the same condition under a later citation. A referee who knows the SEP entry —
the most-read reference work in the field, revised in 2021, stable for five
years — will read the paper as a citation note on Savitt, and the paper's
current 8-page frame (with a parity verdict the logic audit found unsupported)
makes that reading worse, not better.

---

## 4. Is there a defensible publication delta?

**No delta that supports a standalone article.**

The strongest surviving formulation is a *note-level* residue: the 2013→2015
change in Brading's own text, plus the bearer-domain dilemma. Set out at maximum
strength, it reads as follows. This is the best the material can do; it is
offered so the coordinator can judge it, not because I think it clears a
journal's threshold.

> **Delta statement (maximum defensible form).** Savitt (2021) established that
> Brading's dynamics-relative present is "a characterization of a relativistic
> present, not relativistic presentism", on the ground that every dynamical
> system in the history has a sustaining region. The addition offered here is
> not that objection, and does not compete with it. It is a claim about
> Brading's later statement of the same position. In 2013 the size of a
> sustaining region was left as an empirical disjunction — it "might turn out to
> be much, much smaller … or it might be the size of the block universe"
> (p. 1109) — and the local reading was introduced as a starting position ("let
> us begin from the position that there are genuine subsystems", p. 1110). In
> 2015 that starting position becomes a universal clause, P1\*\* (a), and is
> asserted in one sentence to be sufficient: "In order to avoid the block
> universe, all we need is (a)" (p. 17). Once (a) is a clause rather than a
> starting position, it predicates an extent of each bearer; it does not
> restrict a domain of existence, and whether it excludes anything depends on
> which domain the bearers populate. Under event-bearers, Savitt's conclusion
> follows, but only from a coverage premise he assumes ("Presumably …") and
> Brading neither states nor denies, so the conclusion is conditional on an
> unsurveyed empirical claim about the distribution of sustaining regions across
> the history. Under unity-bearers, P1\*\* admits every unity by construction and
> excludes nothing, so the coverage question cannot be posed at all. The point
> not in Savitt is this dilemma about the bearer domain, and its consequence
> that "all we need is (a)" fails for opposite reasons on its two horns: with
> event-bearers it needs a coverage premise, with unity-bearers it needs nothing
> because it excludes nothing. The non-implication, the countermodel and the
> cost map are expository aids to this point, not independent results.

Assessment of that paragraph, honestly:

- Its first three sentences are a literature correction (Brading 2015 exists,
  Savitt did not cite it). Corrections of this kind belong in a footnote to a
  survey, not in an article.
- Its middle is Savitt restated with the conditioning made explicit. Making a
  predecessor's premise explicit is a comment on the predecessor, and comment
  papers must show that the target argument fails or has an unnoticed bad
  consequence; here the consequence is that Savitt's conclusion should be
  hedged — which Savitt already does ("Presumably", "may not help").
- Its last substantive sentence (the domain dilemma) is the only candidate
  result, and it is a scope clarification, of the kind that belongs in a
  section of a larger paper on the quantifier-restriction route (the P/Q/N
  material in `research/existence-form/TRILEMMA.md`), where it can be connected
  to Wüthrich and Mason rather than standing alone.
- Nothing in it is a formal result, a new premise, or a new consequence for
  Brading that Savitt does not already draw.

A journal would receive it as: "Savitt 2021 made this objection; Brading 2015
restated the same condition; the objection applies; here is a formal version."
That is the profile of a rejected submission, and the risk is asymmetric — the
paper currently does not cite Savitt at all, so submitting it in anything like
its present form invites a priority complaint rather than a revise-and-resubmit.

---

## 5. Recommendation

1. **Drop the standalone paper.** The objection is Savitt's, the target is the
   same condition under a later citation, and the paper's distinctive additions
   (formalisation, cost map) are either elementary or defective.
2. **Do not attempt to salvage it by adding Savitt citations.** A paper whose
   abstract reads "Savitt argued X about Brading 2013; we show X also applies to
   Brading 2015" has no contribution sentence a referee will accept, and the
   paper's §6 parity verdict does not survive independent of the priority
   problem (logic audit A3).
3. **Preserve the material** as (a) a paragraph in any future paper on the
   quantifier-restriction / form-of-existence route, where the event/unity
   dilemma does real work, and (b) a short entry in the knowledge base
   recording Savitt §3.3 as the published home of the objection, with the 2021
   revision date and the fact that Brading 2015 is absent from its
   bibliography. `research/existence-form/NOVELTY_AUDIT.md` already records the
   first half of this; it should also record the omitted verdict sentence
   (§2.5 above).
4. **If a coordinator overrides this and keeps a paper**, two changes are
   mandatory and neither is sufficient: cite Savitt in the first paragraph with
   the 2021 revision and quote the verdict sentence, and describe the
   contribution in the comparative form of §4 above rather than as a coverage
   point. The present draft does neither: `main.tex` and `references.bib`
   contain zero occurrences of "Savitt" and zero of "Rovelli".

---

## 6. What this audit does not establish

- It does not establish that no one has applied Savitt's objection to Brading
  2015. PhilPapers was unreachable (HTTP 403) and general web queries were
  noisy; both are the venues most likely to hold a short note. Absence of a hit
  is evidence only about what I could read.
- It does not assess the truth of Savitt's objection or of Brading's position.
  It assesses what is published and what the paper adds to it.
- It does not audit the paper's other sections except where they bear on the
  priority question; the logic audit covers those.
- It does not collate either Brading PDF against the publisher's version; both
  copies match the hashes in `paper/SOURCE_AUDIT.md`.
