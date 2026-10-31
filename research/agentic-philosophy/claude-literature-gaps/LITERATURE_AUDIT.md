# Philosophical literature blindspot audit

31 October 2026. Claude Code (Opus 5.5), at the user's request. A measured coverage audit
with a judged triage. Nothing listed here was read for this note, so every "bears on" is a
hypothesis. No novelty or ontology verdict. This supersedes the coverage part of
READING_GAPS.md, whose keyword tally was narrower.

## Result

**The blindspot is much larger than the metaontology one.** The project is strong in
philosophy of physics and in the narrow Correia–Rosenkranz debate. It has almost no contact
with mainstream analytic ontology, or with general philosophy of science. It uses the
concepts of those fields heavily without citing them.

| Measure | Value |
|---|---|
| SEP entries pulled | 100 |
| Works in their bibliographies | 9,140 |
| Authors cited in at least 5 entries, after removing common surnames | 309 |
| Of those, in 0 project files | 198 |
| In 1–3 files | 37 |
| In more than 3 | 74 |

Confirmed by `git grep` over all 1,228 tracked files: **0 files** for Quine, Carnap, Davidson,
van Inwagen, Schaffer, Rosen, Yablo, Simons, Thomasson, Steward, Koslicki, Dasgupta, Woodward,
Lipton, van Fraassen, Cartwright, Chisholm and Parfit. Armstrong and Hume: 1. Tooley: 1.

Concepts in use without their literatures:

| Term in project files | Files | Its main sources in the project |
|---|---|---|
| grounding | 112 | Schaffer, Rosen, Dasgupta: 0 |
| truthmaker | 32 | Armstrong: 1 |
| totality | 31 | Armstrong: 1 |
| causal process | 11 | Salmon, Woodward: 0; Dowe: 1 |
| ontological commitment | 11 | Quine: 0 |
| abductive selection (ROLE_OF_EXISTENCE.md) | central | "inference to the best explanation": 0; Lipton: 0 |
| "in progress" (pilot P2) | central | imperfective, telic, energeia: 0 |

## Triage against the project's actual failure points

Ranking is my judgment, not a score. The stated next question, from METAONTOLOGY_READ.md, is
which upper-bound principle deserves examination.

### Tier 1: bears directly on an open step

| Gap | Start with | Why it matters here |
|---|---|---|
| **Totality** | Armstrong, *A World of States of Affairs* (1997) and *Truth and Truthmakers* (2004); Molnar 2000; Mulligan, Simons and Smith 1984 | Read: see TOTALITY_READ.md. It states the debt and gives no reason to accept the bound. Forrest 2006 remains unread |
| **Causal process theory** | Salmon 1984; Dowe 2000; Russell 1912; Woodward 2003 | "Sustaining activity" and "causal production" are the project's central notions. These are the physical-process accounts of them. ROLE_OF_EXISTENCE.md asks for a deficit in production: this is that debate |
| **Aspect and process ontology** | Vendler; Kenny 1963; Dowty 1979; Parsons 1990; Galton 1984; Comrie 1976; Steward 1997 and 2013; Stout 2016 and 2018; Aristotle on *energeia* and *kinesis*, with Kosman 1984 | The pilot's P2 depends on what "in progress" means, and on what elapsed portion a token has. The imperfective paradox and the activity/accomplishment distinction study exactly this. Channel tokens look telic and the Kepler interaction atelic, which is the pilot's AC discovered from scratch |
| **Composition and life** | van Inwagen 1990; Thomson 1983; Wiggins; Baker 1997; Koslicki | The unity criterion, with a century of counterexamples the project has not tested |
| **Abduction and parsimony** | Lipton; Sober; van Fraassen 1980; Cartwright 1983; Ladyman and Ross 2007 | ROLE_OF_EXISTENCE.md's selection principle is an unsourced parsimony argument. Whether ideological simplicity bears on truth, and whether realism about a model's domain is warranted, is the representational bridge |
| **Grounding proper** | Schaffer 2010; Rosen 2010; Bennett, *Making Things Up*; Dasgupta | 112 files use the notion, mostly through Correia–Rosenkranz |

### Tier 2: matters for the comparison, not the first step

| Gap | Start with | Why |
|---|---|---|
| Ontological commitment | Quine 1948; Carnap 1950; Yablo; Thomasson; Hofweber | Part read now, through Sider and Meyer |
| Growing block and presentism proper | Tooley 1997; Hinchliff 1996; Bigelow 1996; Tallant 2013, 2018; Ingthorsson 2016; Emery 2017 | The rival positions are held mainly through one exchange. Tooley, the main growing-block book, is in 1 file |
| Modality and permanentism | Williamson 2013; Plantinga 1974; Linsky and Zalta 1994; Stalnaker | Maximal-world admissibility is a modal claim |
| Modes of being | McDaniel, on ontological pluralism | Dorato's pluralism and E_b's status |
| Persistence | Hawley 2001; Haslanger; Merricks; Parfit | Thin, and the unity lane needs it |
| Laws and their role | Mumford 2004; Tooley 1977; Lange; Loewer | Law-constitution is the Brading premise |
| Temporal experience | Dainton 2000; Prosser 2016; Phillips; Hoerl | ROLE_OF_EXISTENCE.md names experience as the hardest burden |
| Emergence and levels | Batterman; Kim; Machamer et al. 2000; Craver | Effective systems as candidate unities |
| Biological individuality | Godfrey-Smith; Dupré; Okasha; R. A. Wilson 1999 | Organizational closure, which the GLM lane started |

### Tier 3: worth a bounded look

- **Buddhist philosophy of time.** From memory, an Abhidharma dispute over whether past and
  future exist closely parallels this debate, and momentariness bears on process. Siderits
  2022 and Priest's work appear in the bibliographies. This is a lead to verify.
- **Whitehead, Bergson, Husserl.** Bergson and Whitehead have some mentions. Process
  metaphysics in the historical sense.
- **Tense semantics in linguistics** beyond aspect: Kamp, Kaplan, Ogihara.

### Not needed

Absence alone means nothing. Most of the 198 are irrelevant here: Searle, Descartes, Tye,
Churchland, Fodor, epistemology and philosophy of mind generally.

## What this implies

1. **Priority risk is larger than the novelty audits suggest.** They searched near each
   claim, in the project's own vocabulary. The pilot's width condition looks like the
   telic/atelic distinction, and "occurrence-presence" looks like a contested position in
   Stout and Steward. Other project distinctions may be rediscoveries. Each needs a check
   against the field that owns the concept.
2. **A rival the project has not met may be stronger.** The 'strongest rival' in each test
   was built largely from project reading.
3. **Reading all of this is not the plan.** One read per open step, each reporting what a
   rival must revise.

## Proposed order

1. **Totality.** Done: TOTALITY_READ.md.
2. **Aspect and process**, against P2, before anyone relies on it. PROCESS_EXPLANATION_TEST.md
   read selected Stout 1997 and Steward 2013, so this narrows to the imperfective and telic work.
3. **Causal process theory**, against the sustaining-activity criterion.
4. **Composition**, against the unity criterion.
5. **Abduction**, against ROLE_OF_EXISTENCE.md's selection principle.

## Limits

- I chose the 100 entries, so an area none of them touches stays invisible. SEP is also
  Anglophone and analytic in its coverage. 14 further entry addresses failed, including
  metaphilosophy and personal identity, and scientific explanation had no parsable list.
- The counts use surnames. I removed common ones, such as Smith and Williams, but collisions
  remain, and a hit may be a different person. Zero hits are reliable; positive hits are not.
- My list stopped at authors in 5 or more entries, so specialists may be missed. Time-specific
  authors with fewer entries were not systematically checked.
- The bibliography parser made errors, so specific citations here come from entries I could
  confirm or from memory. Verify each before citing it. Years may refer to one of several editions.
- 55 PDFs in the repo are not searched by these counts. A citation inside only a PDF is
  uncounted. Worktree-only material is also uncounted.
- Not citing a work does not show an argument is ignorant of it. The project may have reached
  some of these points independently.
