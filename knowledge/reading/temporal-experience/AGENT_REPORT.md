# AGENT_REPORT.md — read-temporal-experience

Task: read the literature on temporal experience (GLM reading lane, authorized 2026-11-11).
Worktree: `/Users/andrew/eternalism/.worktrees/read-temporal-experience`, branch
`agent/read-temporal-experience`. Submission for independent review, not a final truth claim.

## Done / files

- `knowledge/reading/temporal-experience/READING.md` — five required sections: positions in
  defenders' terms, four canonical arguments reconstructed premise-by-premise plus the
  rate-of-passage objection, live open problems with progress conditions, repository-dependence
  section naming specific main.tex sections and three RESULT.md notes, ten ranked next reads.
- `knowledge/reading/temporal-experience/sources.jsonl` — 35 records, validated against the
  knowledge/README.md contract (required fields present on all; full-text fields present on all
  full-text records; depths restricted to the contract vocabulary).
- This file.

Committed only these three files. No board, runner, AGENTS.md or shared-seed edits. No subagents
launched.

## Search capability check

| Tool | Result |
|---|---|
| `web-search-prime` (Z.ai) | **FAILED** — MCP error -429, code 1310 "Weekly/Monthly Limit Exhausted", resets 2026-11-17 10:00:29 |
| `serpapi_search` | **FAILED** — "Your account has run out of searches" |
| `scholar_search` (OpenAlex) | **WORKED** — used for all bibliographic discovery |
| `exa` (`web_search_exa`, `web_fetch_exa`) | **WORKED** — used to locate and read open PDFs |
| Direct open-web fetches | Cambridge Core, PhilPapers, St Andrews repository, QUB portal, lapaul.org, ianbphillips.com, psychclassics.yorku.ca, plato.stanford.edu, jhaponline.org, apcz.umk.pl — all worked |
| Failed fetches | `philpapers.org/archive/PROPAP.pdf` timed out (Prosser "Passage and Perception" primary not read); `frontiersin.org` "Physical time within human time" CRAWL_NOT_FOUND (wrong URL, abandoned) |

## What was read, at what depth

Full-text (open copies fetched; "partial" noted honestly):

1. Paul, "Temporal Experience", *J. Phil.* 107(7) 2010: 333–359 — roughly first half; the
   antireductionist argument (1)–(5) at pp. 337–338 verbatim.
2. Phillips, "The Temporal Structure of Experience", *Subjective Time* (MIT Press 2014) ch. 7 —
   §§7.1–7.3; PSA, memory vs specious-present theories, the naïve view.
3. Prosser, "Rethinking the Specious Present" (Routledge 2017) — first half; taxonomy, Broad
   1923: 351 quoted, start of the dynamic snapshot theory.
4. Lee, "Explaining away temporal flow", *Inquiry* 2017 — abstract, intro, perceptual-evidence
   section; Perceptualism defined; objection to Prosser's mechanism.
5. Prosser, "Experience, Thought, and the Metaphysics of Time" (OUP 2013: 157–174) — intro and
   framing.
6. Prior, "Thank Goodness That's Over", *Philosophy* 34 (1959): 12–17 — the whole paper at fetch
   depth; the relief passage at p. 17 verbatim.
7. James, *Principles* ch. XV (1890) — opening (pp. 605–609); Clay's "specious present" verified.
8. Rashbrook, "Broad's Accounts of Temporal Experience", *JHAP* 1(5) 2012 — abstract and
   introduction; Thin-PSA/Overlap diagnosis.
9. SEP "Temporal Consciousness" (Dainton, rev. 2023-03-17) — §§1.1–1.4, 2.1–2.2 (secondary).
10. Bernáth & Inan, *Metaphysica* 24(2) 2023: 259–275 — abstract and introduction; two-route
    taxonomy of phenomenological arguments.
11. Hoerl & McCormack, *BBS* 42:e244 2018 — abstracts and framing.
12. Skow, "How fast does time pass?", *Phil. Studies* (online 2010) — abstract and introduction.
13. Gołosz, *Logic and Logical Philosophy* 32 (2023): 81–104 — §1 (secondary window onto
    Callender 2017; the book itself was **not accessed**).

Abstract (via OpenAlex): Miller 2023 (*Ergo*), Bacharach 2022 (*Synthese*), Busch–Dubois–VanRullen
2009 (*J. Neurosci.*), Baumgarten–Schnitzler–Lange 2015 (*PNAS*), Peebles 2017 (*Manuscrito*).
Discovery (located/citation-verified, not read): Prosser "Passage and Perception" (*Noûs* 47(1)
2013: 69–84, verified via Deng 2013's reference list), Broad 1923 scans (archive.org), Williams
1951, Skow 2009, Maudlin 2007, Hare, Craig 2000, Schlesinger 1991, Cohen 1959 exchange
(bibliography verified via the *JSL* review, Kanger 1960), Tononi & Koch 2015 and Kent & Wittmann
2021 (as quoted in the SEP entry, locators unverified), Husserl/Brough (version discrepancy
flagged: 1990 in Paul fn. 1 vs 1991 in the repo's phenomenology note), Roselli 2018, Wilson 2022,
the retired SEP entry "The Experience and Perception of Time".

## Not accessed (stated explicitly)

Callender 2017 (paywalled; content used only secondhand via Gołosz and labelled so); Dainton 2000
(paywalled; via his own SEP entry and Prosser's taxonomy); Prosser 2016 (paywalled; via the 2013
chapter and Lee 2017); Husserl/Brough (paywalled); Broad 1923 full text (scan located but not
fetched — quotes held only at quoted-in-source depth); Price 1996 (**not read at all** in this
task; the repo's characterization of Price rests on the fixing-exchange note's own three-passage
depth); Skow 2015; SEP §8.2 "The Argument from Experience" (section title verified, content
unread); Bernáth & Inan's argument sections after the introduction.

## Verification commands and results

- JSONL contract validation: `python3` parse of all 35 lines, checking required fields, full-text
  fields, and depth vocabulary — passed after fixing one JSON syntax slip (stray paren in
  texp-003) and adding missing full-text fields to six records.
- Citation cross-checks that independently agreed: Paul's page header (J. Phil CVII(7), 333–359)
  matched Deng 2013's reference list (incl. DOI); Prior's page range 12–17 matched the *JSL*
  review listing of the Prior–Cohen exchange; James's Clay quote pages (608–609) matched between
  psychclassics (direct) and the SEP entry; Broad 1923: 351 verified as Prosser's quotation (not
  against Broad's scan).
- Repository claim check: `grep` over `research/what-the-past-can-fix/main.tex` confirms the
  bibliography contains no Dainton, Prosser, Paul, Prior, Husserl, James, Phillips or Lee — only
  Broad 1923 (growing block) and Callender 2000. This underpins READING.md §4.
- Quotation policy: quotations in READING.md are short phrases taken from fetched texts; every
  quotation sourced from another work's quotation is marked quoted-in-source.

## Strongest contrary evidence (against the deflationary reading I lean toward in §3.4 of READING.md)

- The antireductionist IBE is stated by Paul as dialectically strong when no reductionist
  explanation exists, and Maudlin/Skow/Hare/Craig/Schlesinger supply the motivating premises.
- Lee 2017: Prosser's sensitivity argument over-generalizes and lacks theory/observation
  conditions — the no-evidence conclusion is not yet properly derived.
- Bernáth & Inan 2023 argue the succession datum tells against eternalism itself, not just
  passage; Miller 2023 argues passage illusionism is wrong; Baumgarten 2015 and Busch 2009 give
  empirical discreteness results that cinematic/dynamist views can recruit.
- Gołosz 2022 answers Callender with dynamic multipresentism, showing the deflationary programme
  is contested on its own terms.

## Limitations

- All full-text reads are partial; none is a complete read of a book. No source was reproduced or
  code-audited. Depth labels in sources.jsonl reflect exactly this.
- Books by the four central authors (Dainton, Prosser 2016, Callender, Husserl) are paywalled;
  their positions are reconstructed from open chapters, the author's own SEP entry, and labelled
  secondary summaries — stated in every affected record.
- Price was not read; READING.md §4 flags the repo's Price claims as unverified by this task.
- Two locators (Kent & Wittmann 2021; Tononi & Koch 2015's exact publication) are recorded as
  unverified leads via the SEP entry, and READING.md instructs not to cite them until located.
- One worktree-local caveat: my section-4 judgments about main.tex are by a model from the same
  family as the paper's drafting assistants — not independent review.

## Proposed next tasks

1. Gated primary reads: Dainton 2000, Prosser 2016, Callender 2017, Broad 1933 vol. II (scans),
   Husserl/Brough — the five that would settle the positions READING.md states at reconstruction
   depth.
2. A short note connecting `research/time-direction/fixing-exchange/RESULT.md` Prop 3 (entropy
   imbalance) to Callender's functional explanation and Hoerl–McCormack's updating system — the
   synthesis READING.md §4 proposes.
3. Add experience-based candidate rows to the paper's §`sec:bounds` table (Paul-style IBE;
   Bernáth–Inan) and the cognitive-functional family to §`sec:direction`'s three-candidate list —
   coordinator decision.
4. Verify and locate Kent & Wittmann 2021 and Tononi & Koch 2015; read SEP §8.2.
5. Read Miller 2023 and Deng 2013 full texts (both open) to settle the live-passage-phenomenology
   taxonomy READING.md §3.1 sketches.
