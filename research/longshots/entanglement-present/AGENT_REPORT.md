# AGENT_REPORT.md — longshot-entanglement-present

Date: 2026-11-10. Worker: GLM headless research agent. Status: **submission for independent
review — not accepted completion.** Worktree:
`/Users/andrew/eternalism/.worktrees/longshot-entanglement-present`, branch
`agent/longshot-entanglement-present`.

## Done / files

- `research/longshots/entanglement-present/RESULT.md` — claim contract in the six-part form of
  `knowledge/NOVELTY.md`, answering the brief's five questions. Verdict: no published state-defined
  thick present found; idea survives screening as a narrow conjecture; as an *objective*-present
  proposal it fails already, because the state-dependence Fewster–Verch force is constitutive.
- `research/longshots/entanglement-present/sources.jsonl` — 21 records under the
  `knowledge/README.md` contract, read depths labelled.
- `research/longshots/entanglement-present/check_twopoint_decay.py` — reproduction script for the
  massive-scalar two-point decay shape and threshold thicknesses (stdlib only, seconds to run).

## Search capability check

- `web-search-prime`: **FAILED** — MCP error -429, "Weekly/Monthly Limit Exhausted … will reset at
  2026-11-17". Recorded per brief instructions; this was the first search attempted.
- `serpapi_search`: **FAILED** — "Your account has run out of searches." (attempted later).
- `scholar_search` (openalex/arxiv/crossref/semanticscholar): **worked**, used throughout.
- `exa` `web_search_exa` / `web_fetch_exa`: **worked**, used for the Fewster–Verch and
  Hollands–Sanders arXiv pages, the Cardy PDF landing text, Ruelle 1962 (e-periodica), and the
  Ruelle bibliographic verification.

No sources were claimed as read beyond what these tools actually returned; read depths in
sources.jsonl are set accordingly.

## Source coverage

Covered at abstract depth: Fewster–Verch 2012 (1106.4785), Summers–Werner JMP 1987, Ruelle 1962,
Cardy 2013 (1304.7985), Agón–Cohen-Abbo–Schnitzer 2016 (1505.03757), Hollands–Sanders 2018
(1702.04924v3), Swingle 2010, Casini–Huerta 2009, Marletto–Vedral 2017, Rovelli "Forget time" 2009,
Dorato 2013, Slavov 2022, Marolf–Morrison–Srednicki 2013. Discovery leads: Page–Wootters and
Connes–Rovelli via internal lane records, Capurso 2023 (unrefereed OSF), Klich 2012, Davidson 1994
(Thomas–Wichmann trail), Xiang 2026. Project sources read full-text: the stein-gr local-clock note;
the pw-critiques map was consulted for lineage placement only.

Question coverage: (1) decay of vacuum correlations and region entanglement — Ruelle, Summers–Werner,
Cardy, ACS, Hollands–Sanders, Swingle; (2) Fewster–Verch implication — abstract verified, discussed
in RESULT §§1, 5; (3) present/becoming from entanglement or correlations — Page–Wootters, Rovelli,
Dorato, Slavov, Marletto–Vedral, plus targeted novelty searches; (4) massless/thermal/cosmological
thickness — Cardy power law, elementary Matsubara estimate, de Sitter lead; (5) strongest failure —
type-III measure ill-definedness plus no covariant state, RESULT §5.

## Verification commands and results

```
python3 research/longshots/entanglement-present/check_twopoint_decay.py
```
Output (this session): asymptotic constant 0.031747; `W(s)e^s s^{3/2}` = 0.030613 (s=3), 0.031028
(s=5), 0.031282 (s=8), 0.031430 (s=12) — converging to the asymptotic value, confirming
`W ~ c e^{-s} s^{-3/2}` for `m = 1`; thresholds `s_ε` = 3.70 (ε=10⁻²), 5.44 (10⁻³), 11.26 (10⁻⁶)
against reference `W(1)`.

```
python3 scripts/check_sources.py research/longshots/entanglement-present
```
Run after writing; result recorded below in "Checks run" if it passed, or fixed and re-run.

## Strongest contrary evidence

- Fewster–Verch (abstract): no covariant choice of preferred state — the proposal's `ω` is extra,
  world-relative structure; combined with Hollands–Sanders' corridor/mixed-state constraints, the
  "appreciably entangled" predicate is not canonically normalised. This is the core of the kill case,
  and RESULT.md concedes it: the construction yields at most one present per `(M, ω)` pair.
- Cardy's paper is CFT-scoped: it does **not** support exponential MI decay for massive fields; that
  load-bearing claim remains unverified (flagged in RESULT §4).
- Threshold freedom (`ε` and the reference scale) makes any thickness available — triviality risk,
  stated in RESULT §5.

## Limitations

- Web-search-prime and serpapi quotas were exhausted; coverage relied on scholar_search (openalex)
  and exa. Recent (last 90 days) work was not exhaustively swept.
- No full-text reads of any external primary paper this session; everything external is abstract or
  discovery depth. The Stein-gr lane's internal full-text record for 1106.4785v3 was relied on and is
  cited as such.
- The brief's expected "Fredenhagen" decay result for local algebras was **not located**; Ruelle 1962
  and the reproduced Bessel asymptotics carry the decay claim instead, and Davidson 1994 marks the
  Thomas–Wichmann trail for future audit.
- Ismael's specific texts could not be pinned to a source in this pass; her role in Q3 is answered at
  lineage level only.
- The two-point-function decay was reproduced numerically; no entanglement measure was computed
  (region MI for massive fields requires machinery beyond this lane's scope and run budget).

## Unresolved questions

1. Does mutual information between disjoint regions of a massive free field decay exponentially in
   the separation (rate `2m`)? Check Casini–Huerta 2022 notes and Klich 2012; else prove it.
2. Is there a covariantly defined, renormalised region entanglement measure (relative entanglement
   entropy) whose separation-dependent part can serve as the threshold quantity without reference-scale
   arbitrariness?
3. Does any physically motivated state (KMS at CMB temperature, de Sitter Bunch–Davies) give a
   mesoscopic or macroscopic selective thickness? CMB thermal length `~ β ≈ 10⁻³ m` is suggestive
   but the state choice is exactly what no covariant rule fixes.
4. Was the interpretive step (correlation decay as the present's thickness) already made in the
   Everettian branching or quantum-reference-frame literature? Un-searched in depth.

## Proposed next tasks

- Verify or refute exponential MI decay between massive disjoint regions at full-text depth
  (Casini–Huerta 2022; Klich 2012), and if absent, state and prove it for the free massive scalar
  (tractable: modular Hamiltonian of free fields is known).
- Audit the Thomas–Wichmann cluster-estimate line (Davidson 1994 trail) for a rigorous decay theorem
  between local algebras.
- Novelty defeat-search round 2: Everettian branching thickness, spacetime QRF papers, and any 2024–2026
  work citing Summers–Werner on vacuum structure and temporal ontology.

## Checks run

```
python3 research/longshots/entanglement-present/check_twopoint_decay.py
```
Passed: output matches the numbers quoted in RESULT.md §4 (script committed alongside).

```
python3 scripts/check_sources.py research/longshots/entanglement-present
```
`1 files, 21 records: 0 errors, 5 warnings` (warnings are non-http URLs for internal records and the
search-record entry, mirroring the sibling lane's project-source convention; after adding full-text
fields to `ep-stein-gr-local-clock` it re-ran clean of that warning).
