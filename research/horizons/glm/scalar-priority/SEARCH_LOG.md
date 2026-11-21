# Search log — horizons-scalar-priority

Date: 2026-10-25. Worker: GLM headless research agent.

## Capability check (required at start)

| Tool | Result |
|---|---|
| `web-search-prime` (Z.ai MCP) | **FAILED**: MCP error -429, code 1310, "Weekly/Monthly Limit Exhausted. Your limit will reset at 2026-11-17 10:00:29". One test query only ("Manchak Is Prediction Possible in General Relativity Foundations of Physics 2008"); no retry loops per brief. |
| `serpapi_search` (MCP) | **WORKED** — used as primary search fallback for all subsequent queries. |
| built-in `websearch` | **WORKED** — one confirmation query for the Manchak retrieval targets. |
| direct `fetch`/`curl` of public primary URLs | **WORKED** — used for PDFs and APIs. |

## Successful retrievals

| Target | URL | HTTP | Depth |
|---|---|---|---|
| Manchak 2008 (author copy, published version) | sites.socsci.uci.edu/~jmanchak/ippigr.pdf | 200, 226,543 B, 4 pages | full-text read |
| Manchak 2008 (PhilSci preprint backup) | philsci-archive.pitt.edu/archive/00003836/01/NoPredGR.pdf | 200, 137,245 B | downloaded, not compared |
| Geroch 1977 (LSE scan) | personal.lse.ac.uk/robert49/ppb/pdf/GerochPredictnInGRMinnesVol81977.pdf | 200, 1,748,381 B | full-text read (printed pp. 81–93) |
| Grøn & Johannesen v1 | arxiv.org/pdf/1103.4753v1 | 200, 308,368 B | full-text read |
| Bolotin & Tanatarov v3 | arxiv.org/pdf/1310.6329 | 200, 2,305,678 B | pp. 1–23 + refs read |
| Harte & Drivas v3 | arxiv.org/pdf/1202.0540v3 | 200, 1,289,118 B | full-text read |
| Baskin & Mazzeo v1 | arxiv.org/pdf/1210.8053 | 200, 267,367 B | §1–2 + refs read |
| archive.org metadata (Wald item) | archive.org/metadata/generalrelativit0000wald | 200 | discovery only |
| archive.org metadata (ost-physics-genrel) | archive.org/metadata/ost-physics-genrel | 200 | discovery only (identified as Crowell, not Wald) |

## Failed retrievals (recorded, not retried in loops)

| Target | URL | Result |
|---|---|---|
| Rindler 1956 ADS scan | articles.adsabs.harvard.edu/pdf/1956MNRAS..116..662R | HTTP 504; unread |
| Manchak "Global Spacetime Structure" survey | core.ac.uk/download/pdf/148349200.pdf | HTTP 403; unread |
| Wald search-inside | ia601907.us.archive.org/fulltext/inside.php?...generalrelativit0000wald... | "Item not available" (lending-restricted); App. D locator unverified |
| ADS alternate for Rindler | (deferred) | not pursued after 504, per bounded-search policy |

## Search queries (serpapi / built-in websearch / arXiv API)

1. `Manchak "Is Prediction Possible in General Relativity" Foundations of Physics 2008` — found Springer, PhilSci, Semantic Scholar; led to working author PDF. ✔
2. `"Huygens principle" "Einstein static universe" wave equation` — found Harte–Drivas PRD 85, 124039 (caustics paper), plus a "strong wave tails" lead. ✔
3. `Wald "Appendix D" conformal transformations scalar field "conformally invariant"` — two citing-source leads only (p. 445 note; "contains some useful..."); no equation-level quote. ◐
4. `wave equation "Einstein static universe" spherical harmonics frequency n+1 modes` — unproductive. ✘
5. `Gott 1980 MNRAS closed universe gravitational lens antipode focus` — unproductive (generic results). ✘
6. `"Einstein static universe" scalar Green function tail support light cone` — weak hits only. ◐
7. `"Caustics and wave propagation in curved spacetimes" arXiv` — confirmed arXiv:1202.0540 (Harte & Drivas). ✔
8. `"domain of dependence" sharpness wave equation "plane wave" sharp finite propagation speed` — found arXiv:1210.8053 (Baskin–Mazzeo). ✔
9. `"domain of prediction" Geroch characterization "Cauchy time function" OR slicing` — **zero results** (relevant negative for Thm-char novelty search). ✘ (empty = informative)
10. `Hogarth "Predicting the future in relativistic spacetimes" 1993 pdf` — bibliographic confirmation only; no accessible full text. ◐
11. `"closed universe" lens focusing antipode Rindler Gott general relativity cosmology` — unproductive; the remembered "closed universe as a lens" paper was NOT confirmed and is not cited anywhere in my outputs. ✘
12. built-in `websearch`: `Manchak "Is Prediction Possible in General Relativity" 2008 pdf` — confirmed PhilSci/author copies. ✔
13. arXiv API `all:"Einstein static universe" AND all:"mode functions"` — empty. ✘
14. archive.org advancedsearch: `creator:(Wald) AND title:("general relativity")` — found the lending-restricted item. ◐

## Coverage assessment

- **Strong**: prediction/prior-work line — Geroch 1977 and Manchak 2008 read in full at primary locators; closed-model horizon line — Grøn & Johannesen and Bolotin & Tanatarov read at the cited locators.
- **Moderate**: wave-propagation line — Harte & Drivas (conformally flat caustic sign flip; Huygens failure) and Baskin & Mazzeo (domain of dependence) full text.
- **Thin / gaps**: copyrighted books (Wald App. D — locator unverified; Friedlander; Günther; Birrell & Davies; Parker & Toms); Hogarth 1993 pp. 726–727; Rindler 1956; Manchak's survey. An ESU mode-parity or "antipodal echo" statement could plausibly exist in the inaccessible QFT-in-curved-space literature; the bounded search could not rule it out (recorded in PRIOR_WORK.md §2.2).
