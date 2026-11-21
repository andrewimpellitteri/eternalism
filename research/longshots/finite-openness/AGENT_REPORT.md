# Agent report: longshot-finite-openness

GLM headless worker, 2026-11-10. Task: test "the open future is a finite resource" in
ΛCDM; verify session numbers; find prior statements; check for any ontological
consequence in the literature; write a claim contract. Submission for review, not an
accepted result.

## Done / files

All inside `research/longshots/finite-openness/`:

- `RESULT.md` — six-part claim contract. **Verdict: negative on physical novelty; the
  volume-budget number is already published (Gott et al. 2005, factor 2.36); the
  ontological consequence is unclaimed but currently blocked by the measure objection.
  Session numbers verified.**
- `check_horizons.py` — stdlib-only verification (Simpson, singularity-free
  substitutions a = x², a = 1/x), with independent z-space route, resolution check,
  age/particle-horizon/z_eh anchors, and a Davis & Lineweaver-parameter recompute.
- `sources.jsonl` — 10 records under the knowledge/README.md contract, depths labelled
  (3 full-text partial, 5 abstract, 1 abstract screened-out, 1 discovery not-read).
- This report.

Not done: no workboard edits, no manuscript edits, no subagents, no installs, no
pushes. Owned paths respected.

## Search capability check

- `web-search-prime` (Z.ai): **failed** — MCP error -429, code 1310 "Weekly/Monthly
  Limit Exhausted", resets 2026-11-17 10:00 UTC. Reported as required by the brief.
- Fallbacks used and working: `exa.web_search_exa` (semantic search, worked), 
  `exa.web_fetch_exa` (primary-page fetch of arXiv/ar5iv pages, worked),
  `scholar_search` (OpenAlex backend, `openalex_key_loaded: true`, worked). All reads
  of primary sources went through fetches of arXiv/ar5iv pages; no source content is
  claimed beyond what was fetched.

## Source coverage (read depths in sources.jsonl)

- **Full-text (partial, via fetch):** Gott et al. astro-ph/0310571 (abstract + horizon
  sections with Eqs. 14–15), Davis & Lineweaver astro-ph/0310808 (abstract, Secs. 1–3,
  Fig. 1 caption, App. B samples), Loeb astro-ph/0107568v2 (abstract, Sec. I, start of
  II), Krauss & Scherrer 0704.0221v3 (intro + CMB passages).
- **Abstract:** Ellis 2015 EBU, Deng 2017, Stoica 2019 (screened out), Markkanen 2018,
  Huang 2026.
- **Discovery (not read):** Gibbons & Hawking 1977 — flagged for verification.
- Queries run (small batches): Loeb/galaxy-horizon; "growing block" + event
  horizon/cosmological constant (×3 phrasings); evolving block universe + de Sitter;
  presentism + event horizon; becoming-saturation-in-de-Sitter; Krauss-Scherrer ID
  resolution; Gibbons-Hawking locator. Citation chasing from D&L App. B (Rindler 1956,
  Harrison 1991) at excerpt level only.
- Error found and corrected: arXiv 0704.0229 is an unrelated mathematics paper
  (Mulmuley, geometric complexity theory); Krauss & Scherrer is **0704.0221**. My first
  fetch hit the wrong paper; the search result corrected the ID, and this is recorded
  in sources.jsonl.

## Verification commands and results

```
python3 research/longshots/finite-openness/check_horizons.py
```

- Session numbers **verified**: particle horizon 46.13 Gly (session 46.1), ultimate
  62.81 Gly (session 62.8), (χ_p/χ_∞)³ = 39.6 % ("about 40 %"), (χ_eh/χ_p)³ = 4.73 %
  (session 4.7 %). Exact reproduction requires radiation (Ω_r = 9.2×10⁻⁵) — the
  session evidently included it; matter-only gives 47.01/63.68/40.2 %/4.47 %, so the
  claims are robust at their stated precision.
- Independent z-integral route agrees to 6.8×10⁻¹⁵ relative; 2¹⁴ vs 2¹⁶ Simpson to
  5.9×10⁻¹⁵; age anchor 13.797 Gyr matches the published ~13.8 Gyr for these
  parameters; z_eh = 1.87 sits between Gott's z = 1.69 and D&L's "z ∼ 1.8" (parameter
  differences, consistent); recomputation with D&L's own parameters reproduces their
  quoted 46-Glyr particle horizon anchor.
- Honest note: two intermediate script bugs (a 1/H₀ constant and an endpoint-limit
  guard in the tail substitution) produced wrong interim outputs; both were caught by
  the cross-checks (age anchor and route disagreement) and fixed before any conclusion
  was drawn. The committed script is the corrected one.

## Strongest contrary evidence

1. **Already-known kill (decisive):** Gott et al. 2005 state the finite co-moving
   future visibility limit (4.50 R_H₀ = 19,000 Mpc) and the volume budget itself —
   "the number of galaxies we will eventually ever be able to see is only larger than
   number observable today by a factor of 2.36" — which is the session's "about 40 %"
   under WMAP-era parameters. D&L 2004 state the past-light-cone/event-horizon
   convergence in one line; Loeb 2002 and Krauss & Scherrer 2007 state the freezing and
   shrinking consequences. The physical claim is not new.
2. **Measure objection (blocks the ontological residue):** comoving slice-volume is the
   only natural measure under which openness is finite; arriving signals never
   terminate (frozen, exponentially redshifting images; eternal emission from sources
   inside the reachable ball), horizon thermodynamics keeps contributing, and the
   proper volume and spacetime 4-volume of the union of past cones diverge
   (integrand ~ a³ ∝ e^{3Ht}). Quantum gravity already occupies a different "finite
   per-observer budget" sense (de Sitter entropy bounds).
3. **Standpoint-relativity is marginal (our note):** pairwise differences between
   observers' ultimate balls are O((d/χ_∞)²) ≈ 10⁻⁹ in volume for galaxy-scale
   separations.

## Limitations

- No astropy/scipy (no installs allowed); verification is two independent
  stdlib-integration routes plus published anchors, not an independent codebase.
- Radiation model is the simple Ω_r = 9.2×10⁻⁵ fluid; no massive-neutrino transition.
- Journal locators for Gott et al., D&L, Krauss & Scherrer not verified against
  publishers (arXiv/ar5iv versions read); Gibbons & Hawking 1977 not read at all.
- Philosophical search covered two engines with ~8 query phrasings; PhilPapers' own
  site search was not queried directly. A systematic growing-block survey could still
  surface a stray paper; absence of a hit is search-bounded, not proof.
- Everything here was checked by one model family (same-model failure modes apply per
  AGENTS.md).

## Proposed next tasks

1. Cheap: close-form hypergeometric evaluation of the three flat-ΛCDM horizon
   integrals as an exactness certificate (mpmath), removing quadrature entirely.
2. A targeted PhilPapers/scopus-grade sweep of growing-block/presentism venues
   (2004–2026) for any Λ-horizon ontology remark, to convert "not found" into a
   stronger negative.
3. If the coordinator wants the ontological residue pursued at all: the live question
   is not cosmology but the bridge premise (becoming indexed to causal access) —
   better handled in the fixing-exchange lane, where openness already has a
   description-length measure (Prop. 3), than as a longshot cosmology claim.

## Blockers

None.
