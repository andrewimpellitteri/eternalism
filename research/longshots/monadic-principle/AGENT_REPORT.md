# AGENT_REPORT — longshot-monadic-principle

10 November 2026. GLM (OpenCode headless) worker. Submission for review, not accepted
completion. Worktree `agent/longshot-monadic-principle`; owned paths only.

## Done

- Read the brief, AGENTS.md, README.md, knowledge/README.md, knowledge/NOVELTY.md, and
  the three project inputs (main.tex targets: `thm:char`, `cor:cauchy`, `thm:map`
  closed-dust rows, `cor:epoch`; both sibling RESULT.md files).
- Prior-work search and source checks for all four brief questions.
- Recomputed the conformal-time budget by hand (script + analytic cross-check); the
  session estimate was correct.
- Wrote the claim contract in the six-part NOVELTY.md form, sources.jsonl per the
  knowledge/README.md record contract, and this report.

## Files

- `research/longshots/monadic-principle/RESULT.md` — claim contract; verdict: the
  geometric core is already in the literature (negative on novelty), the law version is
  refuted for hot-BB-onward histories at all allowed Ω_k, surviving residue stated.
- `research/longshots/monadic-principle/compute_conformal.py` — stdlib-only budget
  script; reproduces the table in RESULT.md.
- `research/longshots/monadic-principle/sources.jsonl` — 19 records with read depths.
- `research/longshots/monadic-principle/AGENT_REPORT.md` — this file.

## Search capability check

- `web-search-prime`: **failed** — MCP error -429, code 1310, "Weekly/Monthly Limit
  Exhausted", resets 2026-11-17 10:00. Not available this session.
- Used instead: `exa.web_search_exa` and `exa.web_fetch_exa` (worked), `scholar_search`
  (worked, OpenAlex-backed). All claims in sources.jsonl state which page was actually
  fetched; nothing was read that could not be accessed.

## Source coverage (read depth)

- Full-text (partial): Manchak 2009 (page extraction: definition, conjecture, abstract);
  Penrose 1979 (Weyl-curvature excerpt); repo inputs.
- Abstract: Manchak 2008 (Springer), Norton 2009 (PhilSci PDF p. 1), Weinstein
  1004.1346 (arXiv abs; full text held by the sibling lane's record mm-weinstein-2011),
  Grøn–Johannesen, Bolotin–Tanatarov (highlights), Ellis–Maartens, Di Valentino et al.,
  Planck 2018, Wheeler–Feynman (Caltech record), Cornish et al., BGV, Smeenk–Wüthrich.
- Discovery: Geroch 1977, Malament 1977 (via Manchak/Norton text), Budic–Sachs (via
  Manchak 2008 reference list), Earman 1995 (via repo's page-check note).

## Answers to the four brief questions (details in RESULT.md)

1. **Named/studied?** Yes, in pieces, with a generic negative: Malament/Manchak
   observational indistinguishability (observable past never fixes the global model
   generically; "causally bizarre" I⁻(p)=M is the excluded extreme), Geroch prediction
   domains (compact-slice universes only; Einstein static Fig. 5), Manchak 2008
   (prediction ⇒ compact slice), Budic–Sachs, Earman pp. 125–130. The exact condition
   "every event's past contains a Cauchy surface" was not found stated as a named
   principle (defeat search).
2. **FLRW criterion and check:** wrap iff conformal time since the earliest slice
   exceeds π in curvature-radius units. Recomputed: η0 = 0.101 / 0.319 / 0.674 rad for
   Ω_k = −0.001 / −0.010 / −0.044; **the session estimate 0.10–0.67 was correct**.
   Cross-checks: analytic 14.2 Gpc / R_c gives 0.101 and 0.669; closed dust threshold
   η = π matches `prop:dust`. Closed de Sitter (width exactly π) fails for every event;
   closed dust wraps only after max expansion; Einstein-static/emergent pre-history
   satisfies it; closed inflation adds ~10⁻¹⁶ H₀⁻¹ of conformal time and rescues
   nothing. Rescue budget: pre-history must supply 2.5–3.0 rad ≈ 3.7–30× the whole
   observed conformal age; wrap without pre-history needs |Ω_k| ≈ 0.97.
3. **No-incoming-radiation?** Yes: as a law, the principle entails the per-event
   Sommerfeld/no-incoming condition — Weinstein's "lawlike time-asymmetry" (1004.1346,
   abstract verified) universalized over all events; massive finite-energy fields need
   no posit (sibling lane's theorem); Wheeler–Feynman is the time-symmetric absorber
   realization; Penrose's Weyl curvature hypothesis is the gravitational analogue at the
   past boundary.
4. **Refutation:** BAO+CMB flatness bounds (|Ω_k| ≲ 0.002 vs ≈0.97 needed; CMB-only
   closed value −0.044 still fails by ≈4.7×); null matched-circle searches (Cornish et
   al. 2004); a confirmed slow-roll primordial tensor spectrum would undercut the
   Einstein-static rescue; BGV past-incompleteness bars expanding pre-histories.

## Verification commands and results

```
cd research/longshots/monadic-principle && python3 compute_conformal.py
# eta0 0.101/0.319/0.674 rad; +future 0.137/0.432/0.908; |Ok| needed 0.97;
# cross-checks 0.101/0.669 rad — all match RESULT.md.
```

## Strongest contrary evidence

- Malament 1977 conjecture settled by Manchak 2009: the observable past fails to fix the
  global spacetime in every non-causally-bizarre model — the monadic condition is
  generically false in GR, so as a law it would be an extreme selection principle.
- The wrap threshold and the maximum-expansion horizon disappearance are known
  (Grøn–Johannesen 2011, Bolotin–Tanatarov 2013; repo `prop:dust` already states it).
- Weinstein 2011 already draws the lawlike-time-asymmetry moral for EM, so the
  philosophical move is not new.

## Limitations

- Geroch 1977 and Malament 1977 originals not read this session (depth: discovery via
  secondary text); no priority claim is made beyond what was verified.
- Planck Table 4 Ω_k row did not render in extraction; the −0.044/0.0007 values are the
  commonly published figures, labelled discovery-depth leads in sources.jsonl.
- The inflation conformal-time estimate uses standard background numbers, not a
  specific model; Di Valentino/Planck abstract extraction cut off before the numbers.
- Wheeler–Feynman and Penrose 1979 held at locator/excerpt depth only.
- Numerical integration is Simpson with 4×10⁵ steps; the analytic cross-check bounds
  any error well below the deficit factors (4.7–31) that matter.
- All review so far in this project is by same-family models; none of this is
  independent expert verification.

## Proposed next tasks

- A separate worker should read Geroch 1977 (sec. 3, Fig. 5) and Malament 1977 at
  source, upgrading the two discovery-depth records.
- A small task to verify the Planck Ω_k table values directly from the A&A HTML table.
- If the coordinator wants the residue pursued: formalize "total conformal past ≥ π" as
  a testable selection principle and survey emergent/cyclic model databases (COMPILE /
  debiased lensing analyses) for viable Ω_k + pre-history parameter space.
- Compile the matched-circles null results post-2004 (Planck-era topology searches) for
  the kill-condition section.
