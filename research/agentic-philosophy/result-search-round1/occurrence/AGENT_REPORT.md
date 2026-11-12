# Agent report: ontology-occurrence-warrant-search (Route A, occurrence)

31 October 2026. Isolated GLM worker submission, branch
`agent/ontology-occurrence-warrant-search`. Status: **submission for review**,
not accepted completion. Ancestry declared: targeted recovery attempt of the
failed pilot's P2 family (per RESULT_SEARCH.md); not a fresh discovery claim.

## Done and files

- `research/agentic-philosophy/result-search-round1/occurrence/CANDIDATE.md` —
  the candidate: exact inference (P1–P5 → C), three-predicate separation,
  strongest source-based rivals R1–R3 with named costs, second process case
  (sedimented fermentation), cheapest falsifier (R3 model check), nearest-
  three delta, referee-packet verdict (**not warranted yet**), and the one
  substantive revision with the original preserved.
- `research/agentic-philosophy/result-search-round1/occurrence/sources.jsonl` —
  8 records, strict schema: 3 full-text direct reads, 5 discovery/inherited
  leads with unresolved items marked.
- `research/agentic-philosophy/result-search-round1/occurrence/AGENT_REPORT.md`
  (this file, lane copy) and fresh runner-root `AGENT_REPORT.md` (handback).

## Search capability check

- `web-search-prime.web_search_prime`: **failed** — MCP error -429, code 1310,
  "Weekly/Monthly Limit Exhausted", resets 2026-11-17 10:00. One attempt only;
  no retries.
- `scholar_search`: **worked** (3 queries; OpenAlex hits for G&G 2024 incl. OA
  PDF link, and DOLCE journal/arXiv records).
- `exa.web_fetch_exa`: **worked** (Springer HTML full text, arXiv HTML).
- Direct fetch: `curl` + `qpdf` stream decode for the Brading 2015 PDF.

## Source coverage (read depth: direct unless noted)

1. **Guarino & Guizzardi 2024** (Synthese 203:104, DOI 10.1007/s11229-024-
   04505-2, open access) — selected §§2–3.1–3.2: flight example and "no
   longer present" clause; snowball accumulation; K definition (fn 11); A1,
   A5–A7, A8, A9–A10, A11–A12; V1'–V3' with fn 14–15; D5–D6; conclusions
   ("classic notion of events as perdurants"; "process manifestations
   accumulate"). This is the strongest rival, read directly, and it supplies
   both the accumulation axioms and the fn-11 clause that refutes the pilot's
   fused "concretely present" reading at the source.
2. **Brading 2015 §5, pp. 17–18** — public journal-layout copy; **SHA-256
   `7caceae74aebe28d1775561cd307dce50f912570eb1a7f9a709d70c699b08f6b`
   verified equal** to the primary register record. P1** (a)/(b) quoted in
   full; "the present is extended in time just as it is extended in space";
   p. 18 empirical concession. Used only for the Q-form "concrete-from-b"
   regimentation; no ontology attributed to her.
3. **DOLCE 2023** (arXiv:2308.01597v1) — selected presence/perdurance passage
   ("endurants are wholly present …; perdurants can be partially present"),
   background for the presence idiom.
4. Inherited depth, marked as such: Stout 2016 (Mind 125(497) 41–62, via G&G
   quotes), Stout 2003 ("The life of a process", via G&G attribution — the
   main inherited gap), Masolo et al. 2003 D18 p. 34 (via fn 11), Wasserman
   2021 (in-text only; identity unresolved), Correia & Rosenkranz 2018 (fn 15
   mention only).

## Verification commands and results

- `shasum -a 256 brading2015.pdf` → `7caceae7…bb054`-prefix match to the
  register (full string in sources.jsonl). Exact.
- `qpdf --qdf --object-streams=disable --decode-level=all` + small Python
  stream-text extraction → 196,284 chars; §5 passages located and quoted with
  ligature restoration (fi/fl dropped by the text layer, per the savitt-delta
  lane's convention). No installs used (qpdf was pre-installed).
- Exa fetch of the G&G Springer HTML → 83,448 chars; all quoted axioms,
  footnotes, and definitions located by substring and quoted verbatim above
  in the sources/CANDIDATE records.
- No numerical grids; no computation beyond text extraction. No dependencies
  installed; no board/coordinator/shared file touched.

## Result in one paragraph

Within the strongest source-based rival's own apparatus (G&G 2024: V1' +
A5–A7 + A9 + CEM + fn 11), the occurrence route's bridge splits into a dead
leg and a live leg: the pilot's fused "concretely present from b" is refuted
at source (constitution without presence is their explicit fn-11 clause), but
the split claim C — every elapsed constituting phase of an ongoing token is
concrete-from-b — follows conditionally from their own accumulation axioms
given two independently motivated premises (constitution factivity at the
standpoint, P4; parthood inheritance of concrete being, P5). The rival's only
genuine denial (R3, front-only deflation) pays named costs; the rival's
trivializing completion (R2, tenseless perdurance) grants C but drains it of
restrictive force — which is this project's known inclusion dispute, honestly
recorded as the reason no referee packet is warranted yet. The verdict on the
recovery attempt: the family's unsupported premise is not repeated; the
recovery produced a bounded two-leg correction plus a falsifiable model check.
If the coordinator judges C non-trivially supported, the family continues to
the R3 model-check; if C is judged trivialized by R2, the family stops per the
round's rules, retaining the correction.

## Strongest contrary evidence

- G&G's explicit neutrality (conclusions: "classic notion of events as
  perdurants"; fn 10: no commitment on future events) — the apparatus itself
  does not fix C; only P4+P5 do.
- The R3 front-only deflation (§3.1 "cognitively carved out of events") is a
  consistent denial path; the second case narrows but does not refute it.
- Grounding-objection family adjacency: the P5 intuition is near known
  presentist-truth-grounding debates; no primary text of that family was read
  this round; priority audit required before any external claim.

## Limitations

- Stout 2003/2016 and Wasserman 2021 not read at primary level (marked
  inherited; both are needed for any referee packet — the manifestation
  concept and the constitution notion's exact content).
- D18 2003 p. 34 (the clause fn 11 rejects) not fetched; recorded as lead.
- G&G's §§4–5 taxonomy and formal development beyond the quoted clauses not
  audited; no independent reconstruction of their system was attempted.
- Brading's 2013 k-system detail relied on register/prior-lane records, not
  re-audited here.
- One candidate, one route; the modal route was not audited (per brief).

## Proposed next tasks (for the coordinator)

1. R3 model-check task: write the front-only model explicitly against V1',
   A5–A7, A9, fn 11 and the four named costs (the candidate's falsifier §6).
   This is the cheapest decisive test for the whole occurrence family.
2. Primary reads: Stout 2003 (current life) and Wasserman 2021 (temporary
   constitution), before any packet; D18 p. 34 for the rejected clause.
3. Priority audit of the P5 inheritance intuition against the grounding-
   objection family (Bigelow 1996 onward), labeled discovery-depth first.
4. If C survives the model check: a narrow task asking whether C-under-R2 has
   any non-trivial reading distinct from the recorded inclusion dispute; if
   not, close the occurrence family with the correction retained.

## Blockers

None blocking submission. web-search-prime quota exhaustion (resets
2026-11-17) did not materially limit coverage; scholar_search, exa, and direct
fetches sufficed.
