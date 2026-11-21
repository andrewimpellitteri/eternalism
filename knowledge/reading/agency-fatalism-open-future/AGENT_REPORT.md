# AGENT_REPORT.md — read-agency-fatalism-open-future

11 November 2026. Worker submission for review; not an accepted completion. Branch
`agent/read-agency-fatalism-open-future`, worktree
`/Users/andrew/eternalism/.worktrees/read-agency-fatalism-open-future`.

## Done, and files

Task: read the literature on agency, fatalism and the open future and deliver
READING.md (five specified parts), sources.jsonl under the knowledge record contract,
and this report.

- `knowledge/reading/agency-fatalism-open-future/READING.md` — the reading note:
  positions with named defenders and sources; five canonical arguments reconstructed
  premise by premise with standard objections; open problems with progress criteria;
  a repository-dependence section naming exact sections of
  `research/what-the-past-can-fix/main.tex` (sec:truth, sec:direction, sec:revise,
  parts/fixing_guaranteed.tex) and of the notes (fixing-exchange, horizons-and-news,
  future-truth-rivals/coordinator, future-truth-grounding) with revisions proposed;
  ten ranked next reads.
- `knowledge/reading/agency-fatalism-open-future/sources.jsonl` — 13 records under the
  knowledge/README.md contract (required fields validated; read_depth constrained to
  the allowed vocabulary).
- `AGENT_REPORT.md` — this file.

Nothing outside the allowed paths was created or modified. The task brief was re-read
via `python3 scripts/agents.py brief read-agency-fatalism-open-future`; the board, the
runner, AGENTS.md and shared seed files were not edited. No subagents were launched,
nothing was pushed or merged, and no dependencies were installed.

## Search capability check

- `web-search-prime` (Z.ai): **failed** — MCP error -429, "Weekly/Monthly Limit
  Exhausted", resets 2026-11-17. Reported per brief instructions.
- `scholar_search` (Crossref/OpenAlex): **worked** — used to verify Thomason 1970
  bibliographic data (Theoria 36(3): 264-281; DOI).
- `exa` (`web_search_exa`, `web_fetch_exa`): **worked** — used for all primary-source
  discovery and extraction.
- Direct `curl` (public pages): **worked** — used for Markosian's papers index, Ismael's
  papers index, Belnap's PhilSci PDF, the SEP compatibilism entry, and PhilArchive
  metadata (PhilArchive's own PDF endpoint now sits behind a Cloudflare challenge; the
  Kutach excerpt text was obtained through exa's extraction of the same item).

## Source coverage, with depths

Primary, full-text (the named sections read directly from openly accessible copies):

1. Aristotle, *On Interpretation* ch. 9 (Edghill trans., MIT Classics) — whole chapter.
2. Belnap, "Branching space-time" — PhilSci-Archive postprint (11 Feb 2003), read in
   full (51 pp. incl. appendix). Limits: postprint, not the 1992 Synthese text; the
   author's own quoting restriction is recorded in sources.jsonl.
3. MacFarlane, "Future Contingents and Relative Truth" — author offprint, §§I-VI read
   closely (§VII not read to the end).
4. Markosian, "The Open Past" (1995) — author PDF, read in full.
5. Markosian, "The Truth About the Past and the Future" (2013) — author PDF, §§1-6 read
   (some objection/reply sections only in part).
6. van Inwagen, "The Incompatibility of Free Will and Determinism" (1975) — LSE-hosted
   copy, all four parts read.
7. Barnes & Cameron, "The Open Future: Bivalence, Determinism and Ontology" — author
   PDF, §§0, 2, 3a read; middle of §1 skimmed; publication venue not verified from the
   file.
8. Ismael, "Decision and the Open Future" (2012) — author PDF, whole chapter.
9. Kutach, "The Asymmetry of Influence" — Oxford Handbook excerpt via PhilArchive;
   excerpt read (the excerpt itself omits three sections).
10. Torre, "The Open Future" (2011) — PhilArchive near-final draft, §§1-5 read.

Secondary, full-text or selected: SEP "Future Contingents" (Øhrstrøm & Hasle, rev.
2024) — whole entry; SEP "Compatibilism" (rev. 2024) — selected sections (§1.1-1.3,
3.1-3.2, 4.1.2-4.1.3). Entry authorship of the latter was not verified and is left
unnamed in the record.

Discovery only: Thomason, "Indeterminist time and truth-value gaps" (1970) — Wiley
paywall; metadata verified via Crossref/Wiley, content attributed through the labelled
secondary sources. This is the main coverage gap; it is ranked first in READING.md's
next-reads list.

Not accessed and not claimed: Prior 1967, Belnap/Green 1994, Belnap/Perloff/Xu 2001,
Tooley 1997, Lewis 1981/1987, van Inwagen 1983, MacFarlane 2014, Kutach 2013, Ismael
2016, Łukasiewicz, Wawer 2021, Correia–Rosenkranz 2018 (the latter two are cited by
main.tex but belong to other lanes' reading). All positions attributed to them in
READING.md are labelled as known via the read sources, mostly Torre 2011 and the SEP
entries.

## Verification commands and results

- `python3 scripts/agents.py brief read-agency-fatalism-open-future` — brief matches
  the assignment; output paths respected.
- JSONL contract check (python json.loads per line; required fields; read_depth
  vocabulary) — result: `OK`, 13 records parse, no missing fields, no invalid depths.
- `grep -n '\section|\subsection' research/what-the-past-can-fix/main.tex` and targeted
  reads of lines 506-578 and 733-748 — used to locate sec:truth, sec:direction,
  sec:revise exactly as cited in READING.md part 4.
- Cross-checks against the repository's own records:
  - main.tex line 834 (Belnap 1992 bibliography entry) and
    parts/fixing_guaranteed.tex lines 39-41 ("Neither notion is Belnap's") were
    verified against the BST-92 postprint (Def 3-2; Fact 8-3) — the paper's
    non-identification is correct, and Fact 13-15 was found as an additional
    connection.
  - main.tex's Albert quotation (pp. 121-122, n. 11) matches the fixing-exchange
    note's credit (ch. 6, n. 11).
  - research/future-truth-rivals/retrospection/REVIEW_PAIRED.md's reading of
    MacFarlane 2003 §V (double time references; Contract S is not his full view) was
    independently confirmed against the offprint.
  - research/time-direction/fixing-exchange/RESULT.md's "Markosian, 'The Open Past'
    (not read)" credit line was checked against the now-read paper: the note's
    characterization understates a structural difference (truth-side vs fixing-side),
    and READING.md part 4 proposes the exact revision.
- No test suite run was required or appropriate for this reading lane; the repository's
  own checks were not modified.

## Strongest contrary evidence found

- Markosian 1995: the only non-question-begging defence of an open future (nomic
  indeterminism + tensed correspondence truth) forces an open past. This presses on any
  repo claim that the past's fixity is grounded in nomic openness alone, and it is the
  same pressure the fixing-exchange note's Proposition 4 exerts from the fixing side —
  with the important difference (recorded in READING.md) that Markosian's conclusion is
  semantic and needs TCT, which the note's identity does not supply.
- Barnes & Cameron 2011: openness is compatible with bivalence, determinism and
  eternalism. This blunts any inference from the repo's openness/fixing results to
  ontology — a restriction the paper itself already states ("No temporal ontology is
  selected", sec:revise), so the evidence supports rather than contradicts the paper's
  stated caution.
- van Inwagen 1975: determinism (base-plus-laws entailment) plus the transfer
  principles yields incompatibilism. The repo's "fixing" relation is exactly his
  determinism notion; the paper nowhere engages the consequence-argument literature,
  so if Parts II-III's fixing results are ever read as bearing on agency, the
  transfer-premise debate is where that would be contested.
- Torre 2011 (citing Lewis 1986b) and Markosian 1995: indeterminism alone does not
  deliver the asymmetry, since time-symmetric laws give multiple pasts too. This
  confirms the paper's mirror proposition rather than opposing it, but it also shows
  the paper's three-candidate list is incomplete (counterfactual-dependence,
  power-over, deliberative/pragmatic accounts missing).

## Limitations

- web-search-prime was rate-limited; discovery relied on exa + Crossref + curl. No
  credentials or private sources were used; everything read is public.
- Thomason 1970 unread (paywalled). Prior 1967 and all books listed above unread; all
  attributions to them are second-hand and labelled.
- Two SEP entries are secondary scaffolding; page numbers they give for paywalled
  primaries were recorded on their authority, not verified.
- Belnap 1992 was read in postprint form, which the author flags as not quotable as if
  original; Synthese pagination not verified.
- Barnes & Cameron's §1 middle (the precisification machinery for bivalence
  compatibility) was skimmed, not read clause by clause; their publication venue was
  not verified from the author PDF.
- Kutach's excerpt omits three sections; the "ensing" framework proper (his 2013 book)
  is unread, so READING.md's characterization of his view rests on the excerpt only.
- Quotations in READING.md are at most short phrases and are attributed through the
  source where the wording was seen (e.g. Lewis p. 38 and Tooley pp. 44-45 as quoted in
  Torre's draft); no quotation or page number was invented.
- Same-family review caveat applies (AGENTS.md): all review so far in this project is
  by models from one family; this submission has not been independently checked.

## Proposed next tasks

1. A gated read of Thomason 1970 (paywalled; needs library access or a supplied copy):
   would settle the exact supervaluationist clauses and the substitution problem that
   any policy-S formulation in main.tex must answer.
2. A follow-up lane on Prior 1967 (chs. on the Ockhamist and Peircean systems) plus
   Belnap & Green 1994: would give the L-policy genealogy and the TRL dilemma primary
   depth, and support the READING.md part-4 revision of sec:truth.
3. A worker task to apply the proposed revisions: widen sec:direction's candidate list
   (Lewis; Torre/Ismael/Kutach), add the established-debate citations to sec:truth,
   qualify the fixing-exchange note's Markosian credit line, and consider citing BST-92
   Fact 13-15 beside the pointed/slice-base distinction. Each is a small, checkable
   edit; none changes any theorem.
4. A comparison task: state the repo's balance/exchange results (reciprocity, entropy
   identity, Prop 4) as a column in the asymmetry-source table of READING.md part 3,
   with one paragraph per literature account saying which fixing-side result it must
   respect. This is the lane where the repository can contribute, per PARITY_MAP's
   parity test 5.
5. Markosian 2013's route semantics vs the repo's relativistic branching results
   (relativistic-branching lane, closed-dust model): test whether routes survive
   replacement of the branching line by GR structure. Owner: a future-truth lane
   familiar with the Placek/BMP definitions.
