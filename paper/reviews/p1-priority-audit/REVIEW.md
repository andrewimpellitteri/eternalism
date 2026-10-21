# Independent priority audit: Brading's P1\*\* (a) and the coverage point

Auditor role: independent priority auditor (subagent), not a referee of the
paper's philosophy. Date: 2026-10-21. Target: `paper/main.tex` at commit
`5a9ec90` ("Retarget article at Brading P1-double-prime"), and the novelty
assertion in `research/existence-form/NOVELTY_AUDIT.md` §"Verdict".

This is a bounded defeat search, not a priority certificate. It records what I
found, at what read depth, and where the search stopped. Absence of a hit is
evidence only about the venues and indexes actually queried; those are listed in
`AGENT_REPORT.md`.

---

## 1. The claim audited

`NOVELTY_AUDIT.md` (2026-10-21) asserts, as the paper's defensible contribution:

> The **P1\*\* coverage point** — that Brading's own (a) is local boundedness and
> does not exclude coverage, so "all we need is (a)" is insufficient — appears
> not to be stated in the prior work found.

The exact target sentence is Brading 2015, p. 17: "In order to avoid the block
universe, all we need is (a)." Clause (a) requires that each thing's present be
"less than the entire spatiotemporal evolution of the universe as represented in
Minkowski spacetime".

I audited four layers separately, because they have different status:

| Layer | Content | Verdict |
|---|---|---|
| L0 | `∀i U_i ⊊ W ⊬ ⋃i U_i ⊊ W` | Elementary; not novel, and the audit already says so. |
| L1 | Application to Brading 2013 (P1\*, local present) | **Published**: Savitt, SEP §3.3 (2021 revision). See §4. |
| L2 | Application to Brading 2015 P1\*\* (a) and "all we need is (a)" | Not found in any source read. Narrow survivor. |
| L3 | System-/frame-relative existence as a position | Not novel (Balaguer 2026; Mason 2026; Savitt 2006; Rovelli 2019). Audit already says so. |
| L4 | P/Q/N trilemma | Not novel as a frame: overlaps the "existence simpliciter"/trivialisation literature (Savitt 2006; Wüthrich 2010). Audit already concedes this. |

---

## 2. Bottom line

**The modest novelty claim as written is not sustained. A narrower version is.**

The audit's claim rests on the sentence "appears not to be stated in the prior
work found". That is false for L1 once Steven Savitt's SEP entry is included in
the prior work: §3.3 "Localizing Time" contains a published, editorially
reviewed, widely read critique of Brading's local present whose conclusion is the
paper's conclusion — the local present characterises a relativistic present, not
presentism — supported by the premise that every system, past, present and
future, has a sustaining region. That is the coverage argument in prose, aimed at
Brading 2013.

What survives is genuinely narrower: **no source read applies the point to
Brading's 2015 P1\*\* or to the sufficiency sentence "all we need is (a)"**, and
no source read gives the set-theoretic statement or the explicit coverage
premise (C). The paper's contribution is therefore a retargeting and
formalisation of a 2021 published objection against a 2015 sentence, plus a cost
analysis. That is a legitimate increment; it is not "an objection not stated in
the prior work".

A referee who knows the SEP entry can say: "Savitt made this point in 2021 about
the 2013 paper, and Brading's 2015 P1\*\* is the same condition restated; what is
new?" The paper currently has no answer, because it does not cite Savitt at all.
That is the single largest priority risk in the draft, larger than the ones the
second external review identified.

---

## 3. Prior-art table

Read depths follow `AGENTS.md`: discovery, abstract, full-text, reproduced,
code-audited. "Full-text (locator)" means I read the cited pages or section
myself in this audit; where I read only part, the part is named.

| # | Source | Exact locator | Read depth | What it contains | Relation to the claim |
|---|---|---|---|---|---|
| P1 | **Steven Savitt, "Being and Becoming in Modern Physics", *Stanford Encyclopedia of Philosophy***, first publ. 2001, substantive revision 6 Oct 2021 | §3.3 "Localizing Time", <https://plato.stanford.edu/entries/spacetime-bebecome/#LocaTime> | **full-text** of §3.3 (whole section), plus archive comparison | See §4 below. Every system past/present/future has a sustaining region; therefore the account "is a characterization of a relativistic present, not relativistic presentism"; co-presence relation unspecified | **Decisive overlap with L1.** Same conclusion as the paper, for Brading 2013. Does not mention 2015, P1\*\*, (a), or set-theoretic union |
| P2 | **Lucy Mason, "Temporal Perspectives, Probabilities, and Openness"**, *Synthese* (2026), DOI 10.1007/s11229-026-05493-1 | PhilSci-Archive 25374 preprint, 26 pp., retrieved via Wayback snapshot 2025-09-22 | **full-text** (whole preprint, text-extracted; SHA-256 `38312ca4…`) | Uses Brading 2013 as "the most useful account of presentism"; level- and domain-relative existence; "facts about other levels are not necessarily included in what exists in any given perspective" (p. 18); notes presentness "is not transitive in this view" (p. 8) | **No P1\*\* coverage point.** Cites **Brading 2013 only**; the string "2015" does not occur in the preprint, so P1\*\* is not discussed. Strong prior art for L3/L4 |
| P3 | **Mark Balaguer, *How to Be a Presentist***, OUP 2026 | Ch. 11 "How to Make Presentism Consistent with Special Relativity", pp. 212–237, DOI 10.1093/9780197845745.003.0011 | **abstract** (Crossref, full abstract); body unread | R-presentism: (a) for any frame, all that exists is a 3-manifold; (b) no frame-independent fact which manifold is real; SR entails eternalism **or** R-presentism **or** a privileged frame | Prior art for L3. No indication of a Brading coverage critique in the abstract; **body unread — unresolved lead** |
| P4 | **Carlo Rovelli, "Neither Presentism nor Eternalism"**, *Foundations of Physics* 49 (2019) 1325–1335 | arXiv:1910.02474v2, §"The local present", closing pages | **full-text** | Local becoming "at every point of spacetime"; "The four-dimensional spacetime is only a cartography of the relations between these multiple local becomings" | Prior art for the **deflationary upshot** (local presents across the whole history are compatible with the 4-D ensemble). No Brading citation, no coverage framing |
| P5 | **Katherine Brading 2015**, *SHPS-A* 50, 13–19 | pp. 16–18, re-read in this audit from the public copy, SHA-256 `7caceae7…` (matches `paper/SOURCE_AUDIT.md`) | **full-text** (pp. 15–19) | P1\*\*, "all we need is (a)" (p. 17); "calls the ontology of a block universe into question" (p. 17); "Only if there are such can the version of presentism offered here survive" (p. 18); see §5 | **The target text**, not prior art. My read confirms the paper's quotations |
| P6 | **Katherine Brading 2013**, *Phil. Sci.* 80, 1101–1111 | pp. 1105 n. 3, 1109 nn. 6–7, 1110 | **full-text** (re-read this audit; SHA-256 `c93ca072…`) | Totality among the things the law-constitutive approach covers (n. 3); "made of things whose dynamically sustained regions of spacetime are much smaller than mine" (n. 6); no determinate inter-system relations (n. 7); interaction passage | Target text. Confirms the paper's n. 3 and n. 6 routes to (C) |
| P7 | **Savitt 2006, "Presentism and Eternalism in Perspective"**, in Dieks (ed.), *The Ontology of Spacetime* | cited via Mason 2026 (p. 1) and SEP *Presentism* bibliography | **discovery** (second-hand only; text not obtained) | Reported thesis: existence cannot be specified independently of a perspective; we must first fix the perspective, then ask what exists | Prior art for L3 (N-form) and for the Q-form/quantifier issue. **Unread — unresolved lead** |
| P8 | **Christian Wüthrich, "Demarcating presentism"** (2010 preprint) | <https://www.wuthrich.net/pub/WuthrichChristian2010Preprint_DemarcatingPresentism.pdf>, §2 | **full-text** | Reconstructs Savitt's trivialisation/"existence simpliciter" argument and replies to it; the presentism/eternalism distinction threatened by unrestricted quantification | Prior art for L4 (Q/N axis). **Does not cite Brading** (checked: no occurrence) |
| P9 | **SEP, "Presentism"** (first publ. 2018; substantive revision 12 Feb 2026) | opening definition; §on empirical basis | **full-text** (selected passages) | Presentism is "a view about what exists, absolutely and unrestrictedly" | Support for the paper's P/Q distinction. **No Brading citation** |
| P10 | OpenAlex / Semantic Scholar citation records for Brading 2013 (W2173391953) and 2015 (W2005418088) | as of 2026-10-21 | **discovery** | Brading 2015: 5 citing works in OpenAlex, 3 in Semantic Scholar; philosophical ones: Slavov, *Relational Passage of Time* (2022); Balaguer 2026 chapters; Mason 2026. Brading 2013: Balaguer 2026, Mason 2026, Raźniak 2023 (Polish) | No indexed critique of P1\*\*. Citation indexes under-cover humanities venues; weak negative evidence only |
| P11 | **Matias Slavov, *Relational Passage of Time*** (Routledge 2022) | DOI 10.4324/9781003224235 | **discovery** (OpenAlex citing record only) | Relational passage; cites Brading 2015 | No indication of a coverage critique. **Unread — unresolved lead** |
| P12 | **Maciej Raźniak, "Punktowa koncepcja teraźniejszości"**, *Edukacja Filozoficzna* (2023) | DOI 10.14394/edufil.2023.0002 | **discovery** | Polish-language; point-like conception of the present; cites Brading 2013 | Non-English lead not checked. **Unresolved** |

Negative results worth recording: no work was found stating that the **union** of
system-presents may equal the world history, in connection with Brading or
otherwise, in any of the venues searched; and the exact sentence "In order to
avoid the block universe, all we need is (a)" returns no web hits outside the
Brading PDF itself.

---

## 4. The decisive precedent: Savitt, SEP §3.3 (2021 revision)

Savitt's §3.3 follows a paragraph on Stein with this passage (quoted from the
live entry; checked against the `fall2023` archive, which carries the same 6 Oct
2021 revision):

> Presents construed this way will typically be larger than a single point but
> will not necessarily exhaust all of Minkowski spacetime or fall afoul of the
> relativity of simultaneity. But this is a characterization of a relativistic
> present, not relativistic presentism. Presumably every dynamical system that
> has existed, does exist or will exist had, has or will have a region of
> whatever size is necessary to sustain it. Furthermore, it is unclear under
> what conditions two dynamical systems share a present. Even if they are
> intuitively spatially close, what sustains one may, or may not, sustain the
> other. While Brading's suggestion might be developed into a way to define a
> relativistic present, it may not help to define presentism in a relativistic
> context, as she intended.

Why this matters, point by point:

1. **Same conclusion as the paper.** "A characterization of a relativistic
   present, not relativistic presentism" is the paper's "does not secure a
   global existential restriction", stated in one sentence.
2. **It supplies the coverage premise.** The sentence beginning "Presumably
   every dynamical system that has existed, does exist or will exist…" is the
   paper's premise (C) argued in print: if every system in the history has a
   sustaining region, the family of regions is populated across the whole
   history, so nothing is excluded by being outside a local present. The paper
   currently says Brading "does not state (C) or its negation" and offers only a
   sketch (n. 3, n. 6). Savitt states the affirmative case.
3. **It anticipates the co-existence repair.** "It is unclear under what
   conditions two dynamical systems share a present" is the paper's §5 "Repair
   2: restrictions on coexistence", including its diagnosis that the physics does
   not supply the relation.
4. **Dating.** I checked archived versions: §3.3 and this passage are **absent**
   from the `fall2014` (rev. 13 Aug 2013) and `win2020` (rev. 21 Aug 2017)
   snapshots and present in the 6 Oct 2021 revision. First appearance: 2021.

Where Savitt is weaker than the paper, precisely:

- He targets **Brading 2013**, i.e. P1\* — the formulation Brading herself
  superseded in 2015 as not saving what the presentist hoped to save. He does
  not mention 2015, P1\*\*, clause (a), or the sufficiency sentence.
- He does not state the non-implication, does not use a union, and does not say
  the presents *cover* the history; he says they "will not necessarily exhaust"
  spacetime and that each system has one. A defender could read the first
  sentence as conceding that the presents may fail to cover.
- He does not distinguish the domains Brading might be read as quantifying over
  (things/unities vs events), which the paper does.

So: the *objection* is published; the *target* (2015 P1\*\* (a)), the *formal
statement*, and the *cost analysis* are the increment. That is what the paper
may claim, and no more.

---

## 5. Independent textual checks on the target (additions the draft should use)

Re-reading Brading 2015 pp. 15–19 against the paper turned up four passages that
bear directly on the argument and are not all in `main.tex`:

1. **p. 17, the hedge that a referee will use against the paper:** "then this
   calls the ontology of a block universe into question." In the one sentence
   where Brading states what local boundedness achieves, she says *calls into
   question*, not *excludes*. The paper's attack is on "all we need is (a)",
   which *is* a sufficiency claim, so the attack stands — but the paper must
   quote the hedge too, or it will be read as attacking a stronger claim than
   the surrounding text makes.
2. **p. 18, the survival condition:** "the crucial question would remain of
   whether there are genuine subsystems of the world, as picked out by the
   dynamical laws, that are smaller in spatiotemporal extent than the entirety
   of spacetime. Only if there are such can the version of presentism offered
   here survive." This is condition (a) again, offered as the survival
   condition. It is a second site for the objection and strengthens the paper's
   claim that (a) is Brading's own stated sufficient condition.
3. **p. 17, non-transitivity:** being present "is not transitive among systems
   and their subsystems." This is the nearest thing in Brading to a constraint
   on how presents combine. It blocks *composing* presents into one global
   present; it does **not** block their union from being the history. The paper
   should say this explicitly, since a defender will offer non-transitivity as
   an answer.
4. **p. 18, (a) is empirical:** Brading says it is an empirical matter, depending
   on the dynamics, whether (a) and (b) hold in the actual world (the extracted
   PDF drops the `fi`/`fl` ligatures in this sentence, so I paraphrase rather
   than quote). This cuts both ways: (a) cannot secure the restriction a priori,
   which supports the paper; but coverage (C) is equally an empirical question,
   which lets Brading reply that the paper's objection is not a refutation of her
   position but a statement that the empirical question is open. The paper's
   existing "burden-shift" concession is the right response and should be tied to
   this sentence.

Also confirmed at p. 16: the law-constitutive principle "applies all the way up
to the material universe as a whole", and at p. 17: "what exists (what is real)
are the genuine unities" — both as the second review reports.

---

## 6. Verdict on the modest novelty claim

| Question | Answer |
|---|---|
| Is L0 (non-implication) novel? | No. Elementary, as the audit says. |
| Is the application to Brading's local present novel? | **No.** Savitt, SEP §3.3 (2021) states the conclusion and the coverage-style premise against Brading 2013. |
| Is the application to P1\*\* (a) and "all we need is (a)" novel? | **Not found in any source read.** This is the only surviving increment. It is an extension of Savitt's published objection to a later, stronger formulation by the same author. |
| Is "system-/frame-relative existence" novel? | No (Balaguer 2026; Mason 2026; Savitt 2006; Rovelli 2019). |
| Is the P/Q/N trilemma novel? | No as a frame; it overlaps the existence-simpliciter/trivialisation debate (Savitt 2006; Wüthrich 2010) and the domain/level point (Mason 2026). |
| Does the paper currently acknowledge the nearest prior critique? | **No.** `main.tex` cites neither Savitt nor Rovelli. |

**Recommended verdict statement for the audit record:**

> The P1\*\* coverage point is a **narrow retargeting of a published objection**.
> Savitt (SEP, "Being and Becoming in Modern Physics", §3.3, revision of
> 6 October 2021) already argues that Brading's local present characterises a
> relativistic present rather than presentism, on the ground that every system in
> the history has a sustaining region, and already raises the co-presence
> question. What is not published, as far as this bounded search reaches, is the
> application of that objection to Brading's 2015 P1\*\* (a) and to her
> sufficiency sentence "all we need is (a)", together with the set-theoretic
> statement of the non-implication and the explicit coverage premise. The
> contribution should be described in exactly those terms, and the paper must
> cite Savitt as the source of the objection's core.

"Modestly novel" survives only in this comparative form. It should not be
defended as "the coverage point is not in the prior work".

---

## 7. What the paper must cite

1. **Savitt, SEP, "Being and Becoming in Modern Physics", §3.3** — mandatory,
   in the introduction and in §4, with the 2021 revision date. State the
   difference: Savitt targets P1\*/2013; the paper targets P1\*\* (a)/2015; and
   Savitt's premise "every dynamical system that has existed, does exist or will
   exist…" is the closest published statement of the coverage premise.
2. **Rovelli 2019** — for the deflationary upshot: local becoming at every point
   plus a 4-D ensemble as "cartography". The paper's "revisionary option 2"
   currently reads as if it were the paper's own diagnosis; it is Rovelli's
   published position (and, per Mason, Savitt's).
3. **Savitt 2006** (at least as cited in Mason 2026 and the SEP *Presentism*
   bibliography) — for the "no existence simpliciter without a perspective"
   point that underwrites the N-form.
4. **Mason 2026 and Balaguer 2026** — already cited; keep the existing
   concession. Add that Mason cites Brading 2013 only, so her view neither
   states nor answers the P1\*\* point; that is a reason to cite her as a nearby
   position, not as a rival to the paper's claim.
5. **SEP, "Presentism"** — for "presentism is a view about what exists,
   absolutely and unrestrictedly"; it supports the P/Q distinction the paper
   relies on.

## 8. What the paper must not claim or imply

1. That the objection is new, or "not stated in the prior work", or that no one
   has criticised Brading's local present as failing to be presentist. Savitt
   has, in the most-read reference work in the field.
2. That Brading nowhere acknowledges the difficulty. Her p. 17 hedge ("calls the
   ontology of a block universe into question") and her p. 18 survival condition
   show she treats (a) as an open empirical matter; the paper's point is that
   (a) is the *wrong kind* of condition, not that she ignored the issue.
3. That system-/frame-relative existence, local becoming, or the
   "revised presentism is eternalism with a local label" diagnosis is new.
4. That the "exact" objection is exact. The second external review already
   flags this; the Savitt passage makes the point sharper, because Savitt's own
   phrasing ("will not necessarily exhaust") concedes the gap rather than
   closing it. The non-implication is exact; coverage is a premise.
5. That the P/Q/N trilemma is a discovery. Present it as a diagnostic that
   organises Savitt/Wüthrich/Mason material.

## 9. Suggested replacement for the contribution sentence

> Brading's 2015 P1\*\* replaces P1\* with a stronger anti-block condition and
> asserts that clause (a) suffices. Savitt has argued, against the 2013
> formulation, that a dynamics-relative present characterises a relativistic
> present rather than presentism, because every system in the history has a
> sustaining region. This paper shows that the same objection applies with more
> force to the 2015 formulation: (a) is local boundedness, local boundedness does
> not imply that the union of system-presents is proper, and Brading states
> neither the coverage premise nor its negation. The contribution is the
> retargeting, the formal statement, and the cost analysis — not the objection
> itself.

## 10. Limits of this audit

- I did not read the body of Balaguer 2026, the published *Synthese* version of
  Mason, Savitt 2006, Slavov 2022, or the Polish Raźniak 2023. Any of them could
  contain the P1\*\* application or a union statement. Balaguer is the most
  likely, because his chapter is the one place a presentist author engages
  Brading at book length in the same period.
- PhilPapers was unreachable (Cloudflare). PhilPapers is the venue most likely
  to hold a short discussion note on Brading 2015 that OpenAlex and Semantic
  Scholar do not index. This is the main structural gap in the search.
- Google web search returned no hits for the two Brading phrases outside the
  PDFs themselves, but Google does not index most paywalled journal bodies, so
  this is weak evidence.
- I did not enumerate the full contents of *SHPS-A* vol. 50 beyond the Crossref
  listing; the issue appears to contain no reply to Brading, but I did not read
  its introduction or the other papers.
- This audit says nothing about whether the paper's argument is *correct*. It
  says what is already published and what is not.
