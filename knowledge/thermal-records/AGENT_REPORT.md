# AGENT_REPORT: kb-thermal-records

**Provenance.** This is a Claude-subagent (Sonnet) completion of a lane whose OpenCode GLM worker died when the Z.ai usage limit was hit. It is not the GLM worker's own submission. It goes to review; it is not accepted completion.

## Files (all under knowledge/thermal-records/)
- sources.jsonl: 11 records (prefix tr-).
- comparison.md: flow/clock/arrow table, six-item contract for five anchors (Connes-Rovelli, modular theory/BW, Hersent 2025, records, PH), conflation list, predecessors and defeaters.
- AGENT_REPORT.md (this file; also the task's requested location was the report path, so it sits in the same directory).

## From the dead worker's log vs afresh
Log (events.jsonl, 102 lines): the worker read the project files and existing records, two WebSearch calls failed, a web-search-prime call worked once (output not preserved in a usable form), and it fetched pages: arXiv abs math-ph/0602036 (Halvorson-Mueger), abs and HTML v1 of 2502.12750 (Hersent, fetched twice), abs 2306.13774 (van Neerven-Portal), abs and HTML v1 of gr-qc/9406019. It read Hersent Secs. 3-5 directly and grepped the reference list (Matassa 2013 arXiv:1212.3462, Poulain-Wallet 2018 arXiv:1801.02715, Etesi 2024, Rovelli 1993a/b). It wrote no deliverables and never fetched any records/memory or Past-Hypothesis source. Its only planned analysis ("Hersent fully mapped") is a one-line note; I used it only as a pointer.
Afresh by me (2026-10-19): WebFetch of Connes-Rovelli HTML v1 and Hersent HTML v1 (through the tool's small-model summarizer, so not verbatim reading; equation numbers need spot-checking; last ~17k characters of Hersent HTML unread by me), Crossref lookups (BW 1976 DOI 10.1063/1.522898, Borchers 2000, HHW 1967, Rovelli 1993), arXiv abstracts for Martinetti-Rovelli, Rovelli "Forget time", Mlodinow-Brun. Mlodinow-Brun PDF fetch returned binary, so abstract depth only.

## Findings worth the coordinator's attention
- Existing record aqft-bisognano-wichmann-1976 has DOI 10.1063/1.522676 and title "...Hermitian scalar field. II"; Crossref resolves 10.1063/1.522898 to "On the duality condition for quantum fields", JMP 17, 303-321 (1976). I added tr-bisognano-wichmann-1976 instead of editing the other lane. The old record should be corrected by its owner.
- Existing phil-thermal-time and frontier-thermal-*-1994/2025 records are shallower than the tr- versions; I linked rather than duplicated IDs.
- I mistakenly guessed arXiv 1910.02970 as a Rovelli paper while exploring; it is an unrelated condensed-matter paper and was not used. A Rovelli "memory/relational" source was not located.

## Checks
`python3 /Users/andrew/eternalism/scripts/check_sources.py --online knowledge/thermal-records` from the worktree root: 11 records, 7 arXiv IDs, 6 DOI lookups, 0 errors, 0 warnings.

## Limitations and unresolved
- Search: WebSearch was loaded but I did not use it; discovery was by direct fetch of known identifiers, so coverage is not a literature search. The dead worker's search tool failed twice.
- Not read at all: Tomita-Takesaki original, Takesaki 1970, Borchers 2000, HHW 1967, Rovelli 1993a/b, BW 1976 body, Matassa, Poulain-Wallet, Etesi (all cited via others or metadata only). Records/memory depth is thin: Wolpert, Albert (Time and Chance), Reichenbach not fetched. Past-Hypothesis section reuses the Codex arrow-cosmology lane without re-reading it.
- Hersent's later versions and any citing/critical papers were not checked.
- Unresolved: any paper tying the Connes-Rovelli state choice to a PH macrostate; whether van Neerven-Portal's POVM makes modular time measurable beyond the examples.
- Nothing was committed; no git state-changing commands were run.
