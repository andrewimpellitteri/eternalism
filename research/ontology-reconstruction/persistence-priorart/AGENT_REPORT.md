# Agent report: ontology-persistence-priorart

30 October 2026. Headless GLM worker, isolated worktree
`/Users/andrew/eternalism/.worktrees/ontology-persistence-priorart`, branch
`agent/ontology-persistence-priorart`. Task: challenge the novelty of the
exact persistence censuses (n≥2 four-case; 1+1 sixteen-case with refinements)
against primary predecessors. This is a worker submission for coordinator
review — not accepted completion, not a novelty verdict.

## Done / files

* `research/ontology-reconstruction/persistence-priorart/RESULT.md` —
  premise/conclusion comparison with the nearest primary results;
  falsifier-oriented nearest-predecessor table (8 rows); point-by-point
  immediate-corollary test; the four required distinctions verified at
  source level; conservative verdicts (unresolved / immediate corollary per
  row); audit falsifiers; done/not-done ledger.
* `research/ontology-reconstruction/persistence-priorart/sources.jsonl` —
  16 records in the knowledge/README schema, lane prefix `pp-`, honest
  read-depth labels (2 discovery, 10 abstract, 3 full-text [one inherited,
  one fetched this session, one this session], 1 reproduced).
* `research/ontology-reconstruction/persistence-priorart/check_order_skeleton.py`
  — exact enumeration certificate (see checks below).
* `AGENT_REPORT.md` (repo root, authorized) — this report.

Headline findings:

1. **Bigaj 2008 located at full-text depth** (author-posted complete text of
   the Elsevier chapter, DOI 10.1016/S1871-1774(08)00012-0; project had it
   only at discovery depth via Thyssen p. 41). It prints: Stein's five
   requirements; the B-type relation's invariance and non-transitivity with
   universal transitive closure (Stein's saturation mechanism); the
   **cumulativity** condition (worldline-restricted transitivity); and
   **exactly two surviving becoming relations: R1 = "outside the future light
   cone of a, or a = b" (= census B) and R2 = "inside the past light cone of
   a" (= census J)** — under exhaustiveness + causal (null-inclusive)
   inclusion clauses + definability + non-universality. His footnote 3 also
   registers the CH chronological weakening (= census I) as a known variant.
2. Premise-level dispositions: Bigaj's pairs = census ∩ Bigaj premises
   ({J, B}) in n≥2 — immediate corollary of the census plus two one-line
   clause checks; the census is **not** a corollary of Bigaj (different
   inclusion axis, no exhaustiveness, F_t); CH 1995 Theorem 1 subsumes the
   census's transitivity row outright; the boundedness∧P_c row is the
   elementary collapse lemma; the 1+1 census repairs the scope of Bigaj's
   single-elsewhere dichotomy (null half-spaces satisfy all his weakened
   clauses in 1+1 without parity).
3. No printed equivalent of either full census found (55-title citation
   chase of CH 1995 + narrow queries). **Conservative verdicts: n≥2 census
   unresolved; 1+1 census unresolved (weaker coverage); several refinement
   rows immediate corollaries.** Not-found is nowhere treated as novelty
   evidence.

## Search capability check (required first action)

* `scholar_search` — **worked** (openalex backend; first call returned
  Savitt 2020 as top hit). Later calls hit arxiv HTTP 400 (one malformed
  query) and crossref HTTP 429 (rate limit).
* `exa.web_search_exa` / `exa.web_fetch_exa` — **worked**; these found and
  read the Bigaj author copy and the Thyssen 2019 open-access full text.
* Direct public APIs via fetch (OpenAlex works API, Crossref, Semantic
  Scholar citations endpoint, arXiv export API) — **worked**.
* `webfetch` on link.springer.com — blocked (CSP challenge); exa fetch used.
* `serpapi_search` — **failed** after the capability test ("Your account has
  run out of searches"); one attempted call, no results.
* `web-search-prime` — not used (quota exhausted per brief).

## Source coverage

* Full-text this session: Bigaj 2008 Section I through references (author web
  copy, complete but unpaginated); Thyssen 2019 open-access article
  (§§1–2, 5.1, 7–7.2, 8.1–8.2, 9 read; technical simultaneity sections
  skimmed).
* Full-text via inherited audits (primaries not reread, limits recorded):
  Clifton–Hogarth 1995 (knowledge/audits/clifton-hogarth/AGENT_REPORT.md);
  Stein 1991 (knowledge/foundations/audit.md).
* Abstract-level: Thyssen 2025, Thyssen RPM chapter, Müller 2019, Placek
  2019, Leininger 2020, Jhou 2017, Papadopoulos et al. 2018, Razniak 2025,
  Savitt 2020.
* Discovery: Godfrey-Smith 1979 (Crossref metadata verified: Philosophical
  Studies 36, 233–244, DOI 10.1007/bf00372628; body paywalled), Semantic
  Scholar citation-chase record.

## Verification commands and results

```sh
time perl -e 'alarm 15; exec @ARGV' python3 \
  research/ontology-reconstruction/persistence-priorart/check_order_skeleton.py
```

* PASS: n≥2 skeleton reproduces the 4 candidates {I, J, B, C} and all 10
  added-premise row counts (PERSISTENCE_CONVENTIONS §4).
* PASS: 1+1 skeleton reproduces all 16 patterns and every refinement count
  (P_c 9, F_c 9, P_c∧F_c 4, closed 4, closed∧F_c 1, transitive 12,
  trans∧closed 3, trans∧P_c 5, trans∧F_c 8, trans∧P_c∧F_c 3, reflection 4,
  mirror classes 10; fifth family (000|011) transitive and non-P_c).
* Wall time 0.05 s (hard timeout 15 s; total task compute ≈0.05 s, within the
  ≤30 s budget). Transitivity/closedness judgments enter as audit inputs from
  the printed witnesses (not re-derived): the script is a combinatorial
  certificate on the reviewed analytic reduction, not an enumeration proof of
  any continuous-domain census — no analytic claim was replaced by a grid.
* `python3 -c` schema check on sources.jsonl: 16 records, all required keys,
  depth labels valid.

## Strongest contrary evidence

* Bigaj 2008 (full text): two-case invariant classification {J, B} under
  cumulativity; B-relation invariance and non-transitivity already discussed;
  I printed as a known weakening. The census shares two candidates and the
  saturation mechanics.
* CH 1995 Theorem 1: subsumes the transitivity row {I, J}.
* The project itself previously misjudged Bigaj's accessibility (discovery
  only, "blocked") — a standing reminder that the unsearched remainder can
  move the disposition in either direction.

## Limitations

* Bigaj's author web copy carries no journal pagination; quoted definitions
  are cited by section/phrase and must be re-verified against the printed
  pp. 229–244. One OCR-garbled clause noted (transitivity counterexample
  prose); definitions unaffected. His "future light cone" phrase is read as
  the closed causal cone (giving R1 = B); the alternative reading would make
  R1 = C — flagged as an open question.
* OpenAlex reports 115 citing works for CH 1995; only the Semantic Scholar
  55-record set was chased. Godfrey-Smith 1979 body, Stein 1968, Aames 2022,
  Kügler 2020, Papadopoulos et al. 2018 body: unread. Non-English sources:
  abstract-level only. serpapi quota died mid-task; web-search-prime unused.
* Inherited CH/Stein depth relies on prior audits (their hashes/locators
  recorded); I did not reopen the primary scans.
* Every "no equivalent found" is a negative search result at the stated
  depths — never evidence of novelty.

## Blockers

None blocking submission. The only hard access blockers (paywalled
Springer/Elsevier bodies, JSTOR) are recorded as limits, not as completion.

## Proposed next tasks

1. Verify Bigaj 2008 quotations against the printed chapter pagination
   (pp. 229–244) and resolve the R1 = B vs C convention question.
2. Chase the OpenAlex 115-citing set of CH 1995 (worker with scholar access)
   and run the same premise-grid over Dorato 1996/2006 and the BST technical
   literature (Placek/Müller bodies).
3. Read Godfrey-Smith 1979 (library/campus access) for the cone-present
   candidate's exact region and premises; same for Stein 1968.
4. If the coordinator accepts the unresolved disposition, fold Bigaj 2008
   into the novelty-sprint claim contract as predecessor #1 and re-derive the
   census's residual delta (I and C admission via chronological-vs-causal +
   F_t, and the 1+1 no-parity family) as the only candidate novelty surface.
5. Optional: upgrade the skeleton check to a Lean-checked statement of the
   two census reductions (inputs as axioms) — small, and it would pin the
   "elementary corollary" analysis formally.
