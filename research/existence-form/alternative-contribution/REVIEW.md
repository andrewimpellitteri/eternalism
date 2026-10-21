# What is left after Savitt: alternative contributions in the Brading material

Research scout report. Date: 21 October 2026. Author: subagent, philosophical
research lane. Output restricted to this directory; no edits to `paper/`,
`WORKBOARD.jsonl`, or any other lane.

Question put to this report: Savitt (SEP, *Being and Becoming in Modern
Physics*, §3.3, revision of 6 October 2021) preempts the article's headline
objection. Does a genuinely different, defensible contribution remain in the
material, and if so which?

This is a bounded search and an argument assessment, not a priority
certificate. "Not found" below means not found in the channels listed in §2. It
is not evidence of absence.

---

## 1. Bottom line

**One candidate survives, and it is a short critical note, not the article the
project is currently writing.**

| # | Candidate | Novelty risk | Size | Verdict |
|---|---|---|---|---|
| C1 | Totality reductio: P1\*\* (a) is false of the universe as a whole | moderate | note (5–7k words) or one section | **recommend, rank 1** |
| C2 | Scale-generality: existence = unity is scale-free, so no unity criterion selects a present | high as a thesis, medium as a critique of Mason | section | **recommend, rank 2, only as C1's frame** |
| C3 | Constitution/eligibility distinction | high — and as stated it misreads Brading | section at most | **reject as stated** |
| C4 | P/Q/N form-of-existence trilemma | very high | paragraph | **reject as a contribution** |
| C5 | Deflationary/relational reading and its explanatory cost | very high | paragraph | **reject as a contribution** |
| C6 | Parity/favoring account for local presentism | high | paragraph | **reject as a contribution** |

The decisive finding is textual and it cuts against the project's own current
framing. Brading does not lack an eligibility principle: she states one —
existence is unity (2015, p. 16) — and it applies "all the way up to the
material universe as a whole". That identity, not a missing premise, is what
sinks P1\*\*. The surviving argument is therefore not "you need an extra
actuality premise" (the article's current verdict) but "your own principle
makes the universe a thing that exists, and P1\*\* cannot be true of it".

The article as it stands is weaker than the material allows and weaker than
Savitt: it defends a conditional non-implication, while the texts support an
internal inconsistency claim. That is the honest reason to change it, and it is
also the only reason a referee who knows Savitt will accept.

---

## 2. Search actually performed

### 2.1 Read at full text in this session

| Source | Version / locator | What was checked |
|---|---|---|
| Brading, "Presentism as an Empirical Hypothesis", *Phil. Sci.* 80 (2013) 1101–1111 | public published-layout PDF, SHA-256 `c93ca072…` (matches `paper/SOURCE_AUDIT.md`), 11 pp. | pp. 1102–1105 (solipsism, unity assumption), 1105 n. 3, 1109–1110 (sustaining region, defeat condition, empirical hedge) |
| Brading, "Physically Locating the Present", *SHPS-A* 50 (2015) 13–19 | public published-layout PDF, SHA-256 `7caceae7…`, 9 pp. | pp. 15–18 (unity across the board, aggregation/composition, P1\*, P1\*\*, "all we need is (a)", survival condition) |
| Savitt, SEP "Being and Becoming in Modern Physics" | live entry, §3.3 "Localizing Time", rev. 6 Oct 2021 | whole of §3.3 |
| SEP "Presentism" | live entry, rev. 12 Feb 2026 | §1, §3 (triviality argument), §8 (relativity) |
| Mason, "Temporal Perspectives, Probabilities, and Openness" | PhilSci-Archive 25374 PDF, full text | pp. 1–2, 6–9, 17–18 |
| Rovelli, "Neither Presentism nor Eternalism", *Found. Phys.* 49 (2019) 1325–1335 | arXiv:1910.02474v2 | §"The local present", §"Becoming", closing pages |
| Wüthrich, "Demarcating presentism" (2010 preprint) | wuthrich.net PDF, 6 pp. | §§1–2 (trivialization, "existence simpliciter") |

### 2.2 Read at abstract or metadata depth only

| Source | Locator | Depth |
|---|---|---|
| Balaguer, *How to Be a Presentist* (OUP 2026) | Crossref abstracts for the whole book (ch. 1, 3, 4, 5, 7–14), incl. ch. 9 pp. 212–237, DOI 10.1093/9780197845745.003.0011; ch. 9 reference list | abstract + reference list. **Body not obtained.** |
| Savitt, "Chronogeometrical Determinism and the Local Present" (2020), DOI 10.5840/zeta-time20207 | OpenAlex abstract | abstract |
| Slavov, *Relational Passage of Time* (Routledge 2022) | OpenAlex abstract | abstract |
| Earman, "Reassessing the Prospects for a Growing Block Model of the Universe", *ISPS* 22 (2008) 135–164, DOI 10.1080/02698590802496680 | Crossref metadata | **discovery only; no abstract available** |
| Brading, "Explanation, Special Relativity, and Presentism" (2014), World Scientific, pp. 16–31 | Crossref metadata | **discovery only; no abstract** |

Saunders 2000 and Pooley 2013 are used only through the project's recorded
quotations (`research/strongest-opponents/RESULT.md`,
`paper/reviews/external-2/REVIEW.md`); I did not re-read them here.

### 2.3 Channels tried, and what failed

| Channel | Result |
|---|---|
| OpenAlex API | **worked**. Brading 2013 = 13 citing works, Brading 2015 = 5 citing works (same counts as `paper/reviews/p1-priority-audit/REVIEW.md`). No citing work is a critique of P1\*\* or of the totality. |
| Crossref API | **worked** (metadata, Balaguer chapter abstracts, Brading 2014 record). |
| PhilPapers | **blocked** (HTTP 403, Cloudflare). The venue most likely to hold a short discussion note on Brading 2015 remains unsearched. |
| Semantic Scholar API | **blocked** (HTTP 429). |
| Google Scholar session / scholar.archive.org | **blocked** (session verification page). |
| Google Books API | **returned empty result sets** for phrased queries; unusable. |
| Bing / DuckDuckGo HTML | **unusable**: returned unrelated commercial pages for every exact-phrase query, including `"empirical presentism" Brading`. |
| SerpApi | returned non-academic noise for all Brading queries. |
| `web-search-prime` MCP | **quota exhausted** (HTTP 429, resets 2026-11-17). |
| SEP entries | **worked**; the SEP *Presentism* entry (2026 revision) cites Brading nowhere, so Savitt's §3.3 remains the only SEP-level Brading critique. |

Consequence: the negative side of this report rests on two citation graphs and
two SEP entries, not on a full-text index of the philosophy literature. That is
a real limitation and it is carried into every novelty-risk rating below.

---

## 3. Candidate-by-candidate assessment

### C1 (was: "totality-as-unity tension"). The totality reductio

**Exact thesis.** P1\*\* is not merely insufficient for the presentist
restriction; it is **false of the universe as a whole**, on Brading's own
premises. Reconstruction (mine; the inference is not Brading's):

1. *Existence is unity.* The principle of ontological unity "applies across the
   board to simple things, composite systems, and component parts of those
   systems, and … all the way up to the material universe as a whole. Insofar as
   what exists is what is one, the law-constitutive approach to unity is a
   metaphysical thesis about what exists." (2015, p. 16)
2. *The universe is therefore a thing that exists* — indeed the paradigm case:
   "By aggregation I mean 'If the world contains a multiplicity of genuine
   unities, how do they together form a whole, rather than being merely a
   collection?' The members must stand in relations to one another, and those
   relations must be necessary and sufficient for the collection to form a
   unity." (2015, p. 16; and 2013, p. 1105 n. 3: the approach "applies to all
   three", including "the totality of existing things").
3. *P1\*\* is universal.* "For each and every thing that exists, that thing
   exists only presently, where for each thing the spatiotemporal extent of the
   present for that thing is … (a) less than the entire spatiotemporal evolution
   of the universe as represented in Minkowski spacetime" (2015, p. 17).
4. *A present is a sustaining region.* "The present is a spatiotemporal region
   of whatever size is necessary to sustain the dynamical system in question"
   (2013, p. 1109; 2015, p. 17: "whatever size is needed to sustain the
   dynamical system in question").
5. *What sustains the universe?* By (2), the universe's unity is constituted by
   the relations among all its members. Its sustaining region must therefore
   contain those relations. Its members are everything in the material
   universe, i.e. things spread throughout the history. So the region needed is
   the entire spatiotemporal evolution, `W`.
6. Hence the extent of the universe's present is not less than `W`: **(a) is
   false of the universe**, so P1\*\*, which quantifies over every existing
   thing, is false.

The alternatives are all closed by Brading's own text:

- *The universe's present is a proper but spatially total subregion of `W`* (a
  "global now", or the Cauchy slice that an initial-value reading of "needed to
  sustain" would deliver). Excluded at 2015, p. 17: "the idea of a spatially
  global present common to all systems is not preserved in this version of
  presentism, but the rejection of a spatially global present is one of the
  central lessons of special relativity".
- *The universe's present is a point or a local region.* That is the position
  Brading calls Stein's "peculiarly extreme (but pluralistic!) form of
  solipsism" (2013, p. 1102, quoting Stein 1968, p. 18) and says her view
  avoids (2013, pp. 1103, 1109–1110).
- *The universe is not a thing that exists.* Contradicts (1)–(2).

**Why this is not the article as written.** `paper/main.tex` §4.1 already runs
a two-horn version, but only as "the strongest route to (C)" — a route to the
*coverage premise*, which the paper then declines to assert. The reductio does
not need (C) at all. It does not need any claim about the family of
subsystem-presents, and it does not depend on Savitt's premise that "every
dynamical system that has existed, does exist or will exist" has a region —
which is exactly the premise a presentist will reject as question-begging.

**Exact target in the target.** Brading's own defeat condition conflates two
different situations:

> It might turn out that, for whatever system we try to consider, the size of
> the spatiotemporal region necessary to sustain it is the entire history of the
> universe … In other words, the only dynamical system that there is, is this
> entirety, and there are no genuine subsystems of the universe. If that turns
> out to be the case, then this version of presentism is defeated and the block
> universe triumphs. (2013, p. 1109)

and, in 2015, the survival condition: "Only if there are such [genuine
subsystems smaller than the entirety of spacetime] can the version of
presentism offered here survive" (p. 18). The reductio shows that the
antecedent of the first sentence is satisfied by the universe alone, whether or
not subsystems exist; so the survival condition of 2015, p. 18 is not
sufficient. "All we need is (a)" (2015, p. 17) is not a sufficient condition
for avoiding the block; for one existing thing it cannot be satisfied at all.

**Closest prior art.**

| Source | Locator | Relation |
|---|---|---|
| Savitt, SEP §3.3 | rev. 6 Oct 2021 | Conclusion: the local present "is a characterization of a relativistic present, not relativistic presentism", because "every dynamical system that has existed, does exist or will exist had, has or will have a region". **Different premise (semantic/characterization), different conclusion (not presentism).** Says nothing about the totality, P1\*\*, or existence = unity. |
| Brading 2015 | pp. 16–18 | Supplies every premise. p. 17 concedes that a system's needed region "might turn out to be the entire spatiotemporal history of the universe"; she treats this as a possibility about a system, not as an entailment for the totality. |
| Brading 2013 | pp. 1109–1110 | The conflation between "region = whole history" and "no genuine subsystems". This is the sentence the reductio attacks. |
| `paper/main.tex` §4.1 | current draft | Compressed two-horn version as a route to (C); not the inconsistency. |
| Mason 2025/2026 | preprint pp. 7–8, 17–18 | Level- and domain-relative existence. Adjacent, not the same: she accepts level-plural existence as a feature. |
| Rovelli 2019 | §"Becoming" | Local becomings at every point plus a 4-D "cartography" — the *positive* picture the reductio says Brading's principle produces. Prior art for the upshot, not for the inconsistency. |
| Balaguer 2026 | ch. 9 abstract | R-presentism; does not address Brading's totality clause in the abstract or in the ch. 9 reference list (which cites Brading 2013 only). **Body unread.** |

**Novelty risk: moderate.** Two reasons to be honest about it. First, every
premise is Brading's, and the inference is one step from (1) to (6); a referee
may say "she already says at p. 17 that the needed region might be the whole
history, and at p. 16 that it applies to the universe as a whole; you have
joined two sentences". Second, Savitt's premise, applied to the universe as a
dynamical system, gives a nearby result. What is not in either is the claim
that the joint is an *inconsistency* and that the p. 18 survival condition is
therefore the wrong condition. That is an argumentative contribution, not a
discovery. It should be sold as such.

**What would defeat it.** Any one of these:

1. A defensible reading on which the universe's sustaining region is a proper,
   spatially *local* region, without ad hoc stipulation. (I could not construct
   one: the universe is not local, and the only principled proper candidate —
   an initial-data slice — is spatially global.)
2. Evidence that Brading does not treat the material universe as a thing that
   exists, i.e. that the 2015 p. 16 identity is rhetorical. The unread 2014
   chapter (World Scientific, pp. 16–31) is the place to check.
3. A published statement of the same inconsistency. None found in two citation
   graphs and two SEP entries; PhilPapers and Scholar were unavailable, so this
   remains the live risk.
4. A demonstration that "exists only presently" is satisfiable by the universe
   when its present is `W` — i.e. that labelling the whole block "the present"
   does save what the presentist wanted. Brading denies this in her own words
   (2015, p. 17), so this route is closed to her, though not to a revisionary
   descendant.

**Size.** Short critical note (5,000–7,000 words): one target, one four-premise
reconstruction, one dilemma, one consequence for the empirical-question
framing. Alternatively a section that replaces `main.tex` §4.1. It is **not**
enough for the full article the project is drafting, and padding it with the
existing trilemma, repairs and parity material would re-import the preempted
content.

---

### C2. Scale-generality: existence = unity is a criterion that cannot select a present

**Exact thesis.** The problem with local presentism is not that it lacks an
eligibility principle, but that its eligibility principle is **scale-free**.
Brading's criterion — what exists is what is one — applies at every level
(simple, composite, part, totality). A criterion that makes something exist by
making it one cannot select *which* scale's unities are existence-conferring,
because it confers existence on all of them, including the maximal one. So any
local presentism must add a scale-selection principle (actuality of some
systems, a privileged frame, or a preferred level). Each such principle is a
global or relativizing structure, so local presentism is either relativized
existence (N-form) or a privileged structure.

**Closest prior art.** Brading 2015, p. 16 (the identity, and the
multiplicity/aggregation/composition triad, which *is* the scale question);
Mason, preprint pp. 17–18 (existence is level-relative — she treats this as the
solution, which is precisely the disagreement); Balaguer 2026, ch. 9 (frame
relativity as the solution); Wüthrich 2010, §2 (the "existence simpliciter"
challenge); Savitt 2006 (via Mason p. 1 and Wüthrich §2).

**Novelty risk: high as a general thesis.** The scale/level point is Mason's
central move and the frame/domain point is Balaguer's and Savitt's. The only
unoccupied version is a *criticism of Mason*: that level-relativity is not
local presentism but relativized existence, so her view concedes the point. That
is a different paper, and it requires the published *Synthese* version (DOI
10.1007/s11229-026-05493-1), which was not read here.

**What would defeat it.** A published argument that unity criteria are
scale-selecting; or Mason's published text already distinguishing
level-relative existence from relativized existence in a way that survives the
objection.

**Size.** Section. Use it as C1's general moral ("too generous, not too thin"),
not as a second paper.

---

### C3. Constitution versus eligibility

**Exact thesis (as in `TRILEMMA.md`).** Brading's law-constitutive account
explains unity and persistence, not ontological eligibility; no amount of
law-constitutive detail says which unities' presents confer existence; the
missing premise is an eligibility principle, not an "actuality patch".

**Status: as stated it misreads the target, and it should not be published in
this form.** Brading states the eligibility principle explicitly: "Insofar as
what exists is what is one, the law-constitutive approach to unity is a
metaphysical thesis about what exists" (2015, p. 16). Existence is not left
unaccounted for; it is identified with unity. The TRILEMMA's claim that "no
amount of law-constitutive detail bridges that categorial gap" is therefore
false of Brading: she bridges it by identity. A referee who has read p. 16 will
use this to reject the diagnosis.

The distinction can be saved only in the C2 form (the criterion is too
general, not missing), and C2 has the prior-art problem above.

**Closest prior art.** Brading 2015, p. 16 (the identity itself); the general
grounding literature on grounds of unity versus grounds of existence (not
searched here); Mason pp. 17–18; Wüthrich §2.

**Novelty risk: high**, both for the general distinction and for the
attribution.

**What would defeat it.** Already defeated as an attribution by p. 16. As a
general thesis it would need a case where a unity criterion is genuinely silent
about existence; Brading is not that case.

**Size.** At most a paragraph, and only in the reversed (C2) form.

---

### C4. The P/Q/N form-of-existence trilemma

**Exact thesis.** P-form (predicate presentism) yields the coverage problem;
Q-form (quantifier-restricted presentism) needs a global present or privileged
domain; N-form (no common domain) makes the debate relational.

**Closest prior art — this is heavily occupied.**

- SEP *Presentism* §3 (rev. 2026) states the triviality argument with exactly
  three readings of "exist": (P1) "only present things *exist now*" (trivial),
  (P2) "…*have existed*, *exist now*, or *will exist*" (false), (P3)
  "…exist *simpliciter*" (false, or collapses into P2), with the literature
  listed (Merricks, Zimmerman, Sider 1999/2006, Crisp 2004, Ludlow 2004, Meyer
  2005/2013, Savitt 2006, Stoneham 2009, Deasy 2019b "The Triviality Argument
  against Presentism", and others). The P/Q axis is this argument.
- Wüthrich 2010, §2: reconstructs Savitt's "existence simpliciter" and the
  unrestricted-quantification problem directly.
- Mason, preprint pp. 1–2 and 17–18: "There is no 'existence simpliciter' that
  can be specified absolutely, what exists depends on one's perspective"; and
  she attributes the "specify the domain first" point to Savitt and Rovelli as
  an existing diagnosis of a major flaw in the debate.
- Balaguer 2026, ch. 3 "Against Trivialism" (pp. 37–47) and ch. 5
  "Anti-Metaphysicalism" (pp. 85–100): non-factualism as a live option.

**Novelty risk: very high.** The trilemma is the triviality argument plus
Savitt/Rovelli/Mason. Nothing in it is ours.

**What would defeat it.** Already defeated as a novelty claim by the above.
Its only defensible use is as a labelled framework paragraph that cites these
sources and claims nothing.

**Size.** A paragraph in a related-work section, if kept at all. It cannot be
the article's spine, and the article must not present it as a discovery
(`paper/reviews/p1-priority-audit/REVIEW.md` §8.5 already says this).

---

### C5. The deflationary/relational reading of local presents and its explanatory cost

**Exact thesis.** Read as a local present, Brading's notion is deflationary: it
is a relativistic present with no global Now, and it buys consistency at the
cost of not taking passage seriously.

**Closest prior art.** Rovelli 2019 is explicit and stronger than the article
can claim: the candidate local presents "show that the common usage of 'present'
and 'simultaneous' is not in contradiction with relativity … **None of them
deserves to be charged with ontological weight**" (§"The local present",
2019, 1330–31); and "The four-dimensional spacetime is only a cartography of the
relations between these multiple local becomings" (§"Becoming"). Savitt
SEP §3.3 reaches the same characterization verdict about Brading. Pooley 2013's
route (1) — "a deflationary analysis of passage compatible with the block
universe" — is the same charge at the level of passage. Mason 2026 and Slavov
2022 defend relational/local passage as a positive view.

**Novelty risk: very high.** Rovelli states the deflationary reading *and*
refuses ontological weight for local presents; that is the whole content of the
"cost" claim, and it is his position, not an objection to it.

**What would defeat it.** Nothing needed; it is already published. The article
must cite Rovelli 2019 (as the audit says) and must not present "revisionary
option 2" as its own diagnosis.

**Size.** Paragraph. Keep the citation, drop the framing.

---

### C6. A positive account of parity/favoring for local presentism

**Exact thesis.** Comparing ontologies as composite hypotheses over realization
classes with stated priors and likelihoods yields a defeasible favoring verdict;
for Brading's local presentism the verdict is parity unless an actuality premise
is added.

**Closest prior art.** Balaguer 2026, ch. 9: "we don't have any good reason to
favor eternalism over R-presentism" (Crossref abstract, pp. 212–237) — a parity
verdict already argued at book length for a relativized presentism, and ch. 5
offers a stronger meta-position (non-factualism or "scientism"). SEP
*Presentism* §8 rehearses the standard "undermining versus counterargument"
framing (Hawley 2006; Balashov–Janssen 2003; Callender 2008) that any favoring
claim for presentism must negotiate. The Bayes-factor-over-a-composite-
hypothesis machinery is standard model averaging, not a philosophical result.

**Novelty risk: high.** And the section does not in fact deliver a verdict: as
both external-2 (M8) and the logic audit (A3) say, it delivers a tie dressed as
a verdict.

**What would defeat it.** Already defeated as a contribution. The honest version
is one sentence: within the P1\*\* route the physics supplies no difference
between this presentism and eternalism; any difference is carried by a premise
the physics does not supply.

**Size.** One paragraph, or cut.

---

## 4. What actually remains: the argument in its best form

This is the candidate I recommend. It is stated here as a proposal, not as an
established result, and every premise is sourced to a page I read this session.

> **(T1)** Brading holds that existence is unity and that the principle applies
> to the material universe as a whole (2015, p. 16; 2013, p. 1105 n. 3).
> **(T2)** The present of a thing is the region necessary to sustain it
> (2013, p. 1109; 2015, p. 17).
> **(T3)** P1\*\* requires, for every existing thing, that this region be less
> than the entire history of the universe (2015, p. 17).
> **(T4)** The region necessary to sustain the universe as a whole is the
> entire history: the universe's unity is constituted by the relations among
> its members (2015, p. 16), and its members are spread through the history.
> **(C)** Therefore P1\*\* (a) is false of the universe — or the universe's
> present is a spatially global present, which Brading rejects (2015, p. 17),
> or a point, which she calls solipsism (2013, pp. 1102–1103), or the universe
> is not a thing that exists, contradicting (T1).
> **(Corollary)** Brading's defeat condition (2013, pp. 1109–1110) and her
> survival condition (2015, p. 18) are mis-stated: the block follows from the
> universe's own present whether or not genuine subsystems exist, so the
> empirical question she poses is not the question on which her view turns.

**Relation to Savitt.** Savitt's verdict ("a characterization of a relativistic
present, not relativistic presentism") and this reductio are compatible and
mutually supporting: Savitt gives the semantic verdict, T1–C gives the
metaphysical reason internal to Brading's system. The note can say so, which is
also the answer to the referee question "what is new relative to Savitt?".

**Relation to the current draft.** `main.tex` §4.1 contains a compressed
version used as a route to (C). The note's increment over the draft is:
(i) the p. 16 identity as the warrant that the totality *is* a thing that
exists (the draft only says "if the totality is a genuine unity");
(ii) the target sentence at 2013, pp. 1109–1110, where the conflation actually
occurs;
(iii) the conclusion *inconsistency*, not *route to a premise*;
(iv) the fourth horn (point present → solipsism).

**Weak joints, in order of danger.**

1. (T4). "Necessary to sustain" is Brading's phrase and she never fixes its
   extension. An initial-value reading ("the data that determine the history")
   yields a Cauchy slice — still spatially global, so still horn 2, not an
   escape. A *minimality* reading could in principle yield something smaller
   for the universe, but no principled candidate exists, and any candidate that
   omits the universe's members omits what the universe is.
2. (T1). "Insofar as what exists is what is one" is a conditional in Brading's
   sentence. The note must either treat it as her operative premise (defensible:
   it introduces the whole metaphysics) or argue that the surrounding text
   commits her to it. This is the premise to stress-test first.
3. The genre. As a full article this is thin; as a note it is right-sized.

---

## 5. Recommendation

**Rank 1 — C1, the totality reductio.** It is the only candidate that (a) is not
Savitt's, (b) is not Rovelli's/Mason's/Balaguer's, (c) turns the article's
conditional burden-shift into an argument a referee must answer, and (d) uses
only texts I have read at full text with verified hashes. Novelty risk is
moderate and should be stated as such: the contribution is the identification of
an inconsistency, not the discovery of a new objection family.

**Rank 2 — C2, scale-generality, as C1's frame only.** State it in one
paragraph: the criterion that makes the universe exist is the same criterion
that makes molecules exist, and a criterion that cannot discriminate scales
cannot yield a local ontology. Do not build a second paper on it without the
published Mason text.

**Reject as contributions: C3 (as stated), C4, C5, C6.** Each is either
preempted (C4 by the SEP triviality argument and Mason/Savitt/Rovelli; C5 by
Rovelli 2019; C6 by Balaguer ch. 9) or misreads the target (C3 by 2015, p. 16).
Nothing is gained by retaining them as the article's spine.

### Decisive next step (one, bounded)

Write the reconstruction above (T1–T4) as a **single page** with the exact
quotations and page numbers, then attack premise (T1) and (T4) in that order:

- (T1) test: does the 2015 p. 16 sentence commit Brading to the identity, or is
  "insofar as" a hedge she could withdraw? Check the unread 2014 chapter
  (*Explanation, Special Relativity, and Presentism*, pp. 16–31) and Brading
  2011 (*Three principles of unity in Newton*) before writing.
- (T4) test: try to construct a reading on which the universe's sustaining
  region is proper *and* local *and* not ad hoc. If one is found, C1 collapses
  to the existing conditional verdict and the Brading paper should be dropped
  rather than published as a re-derivation of Savitt.

If both survive, the deliverable is a note, not the current article; if either
fails, the honest outcome is that no paper-sized contribution remains in this
material.

---

## 6. Claims the current paper must stop making

Collected here because they bear on which contribution is defensible:

1. That Brading's account supplies no existence criterion (2015, p. 16 supplies
   one).
2. That the coverage objection is the paper's contribution (Savitt 2021; and
   Rovelli 2019 states the positive local-becoming-plus-4-D picture).
3. That the P/Q/N trilemma is a discovery (SEP *Presentism* §3; Wüthrich 2010
   §2; Mason pp. 1–2, 17–18).
4. That the deflationary upshot or the parity verdict is the paper's own
   (Rovelli 2019; Balaguer 2026 ch. 9).
5. That "all we need is (a)" fails only conditionally, when the totality clause
   makes (a) false of one existing thing.

---

## 7. Limits

- Bounded search: two citation graphs, two SEP entries, seven full texts. No
  full-text philosophy index was reachable (PhilPapers, Scholar, Google Books
  all failed; see §2.3). Absence of a prior statement of the totality reductio
  is therefore weak evidence.
- Balaguer 2026 is the single most likely place for an unread critique of
  Brading's totality clause, and only abstracts were obtainable.
- Brading 2014 and Brading 2011 are unread and could contain either a restatement
  or a retraction of the 2015 p. 16 identity.
- The reductio is my reconstruction. It is not Brading's claim, not Savitt's,
  and it has not been independently reviewed.
- This report makes no claim about whether eternalism is true, and none about
  which of presentism/eternalism the physics favors.
