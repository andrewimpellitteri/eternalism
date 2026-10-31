# Priority-audit search log — cross-spacetime becoming classifications

25 October 2026. Lane: `stein-priority-audit`. Source manuscript pinned at
commit `0c6d2c5` (`main.tex` SHA-256
`7ccc1d37b521e4a25af54c28ffc067066243bd190da79125d922037c90345886`; note this
differs from the hash pinned by `SECOND_PASS_REVIEW.md` — the manuscript was
edited after that review; the theorem statements audited here are the current
ones).

## Search capability check (required at start)

- `web-search-prime` (Z.ai MCP): **FAILED** —
  `MCP error -429: {"error":{"code":"1310","message":"Weekly/Monthly Limit
  Exhausted. Your limit will reset at 2026-11-17 10:00:29"}}`. Test query was
  on-topic ("Stein theorem becoming curved spacetime Clifton Hogarth
  extension"). Recorded as unavailable for the whole run.
- Fallbacks used and working: built-in web search (Serper-based), `webfetch`
  for public pages, public APIs (OpenAlex, arXiv), `curl` for open PDFs.
  Semantic Scholar API returned HTTP 429 on first use; OpenAlex used instead.
  PhilPapers/PhilArchive direct file downloads returned 403;
  PhilSci-Archive rejected two direct PDF fetches (bot check) while serving
  two others. Springer link blocked both curl and webfetch (bot challenge).

## Queries run (grouped, with purpose)

1. `Clifton Hogarth definability objective becoming Minkowski extension curved
   spacetime theorem` — capability/anchor verification. Found CH abstract,
   PhilPapers abstract, SEP entry, Savitt CDLP (philsci 8481), WC2017 PDF.
2. `Stein theorem becoming curved spacetime Clifton Hogarth extension` —
   the capability test (rate-limited before results).
3. `Viglione "Not-so-absolute cosmic simultaneity" Erkenntnis 2026` — located
   OA versions (Springer, PhilSci 28022, air.unimi.it, COSMOS project page).
4. `"Clifton" "Hogarth" "definability of objective becoming" pdf Synthese
   1995` — hunt for open full text: not found (JSTOR/Springer only).
5. `becoming relation "globally hyperbolic" transitive theorem curved spacetime
   Stein extension` — defeating search; found nothing theorem-like; surfaced
   domain-theory results (Martin-type bicontinuous poset results) and
   Sorkin-Woolgar causal order — adjacent mathematics, no becoming
   classification.
6. `"no obvious way to extend Theorem 1 beyond Minkowski spacetime"` — exact
   phrase hunt for a verbatim secondary quote of CH pp.385-386: no hit; the
   passage remains primary-unverified (see limitations).
7. `Stein 1970 "A Note on Time and Relativity Theory" pdf Gödel cosmological
   deformation` — located the full J.Phil. note (strangebeautiful.com) and,
   through Manchak 2017, resolved that the deformation question is in Stein's
   other 1970 paper (Phil. Sci. 37:589-601, p.594).
8. `Stein "paradoxical time-structures of Gödel" 1970 pdf Philosophy of
   Science` — abstract + Cambridge listing; paywalled.
9. `Zalel "covariant growth dynamics" causal set arXiv` — arXiv:2302.10582;
   screened (label-invariance of growth measures; not relations).
10. `natural transformation causal relation category of spacetimes "locally
    covariant" order classification` — confirmed the Loc category details and
    found the nearest structural precedent (FV 2012 S1/S2, SPASs property;
    Fewster-Verch 1201.3295 endomorphism classification). No preorder
    classification anywhere in this literature.
11. `causal set "Stein's theorem" "order embedding" OR "convex" becoming
    relation theorem locally finite posets` — only WC2017/ar5iv mirrors and
    survey restatements; no convex-embedding Stein theorem.
12. `"Clifton and Hogarth" "Theorem 1" becoming "universal relation" invariant
    under isometries statement` — surfaced Savitt CDLP full text (verbatim CH
    Lemma p.364, Theorem 1 p.365, Theorem 2 pp.371-372) and Dorato 2002.
13. `Stein "On Einstein-Minkowski Space-Time" 1968 philarchive pdf` — PhilArchive
    record exists (rec/STEOES, 2,065 downloads) but file downloads 403; content
    approach via Stein 1991 (full text), SEP notes quoting Stein 1968 p.14
    ("those events, and only those, have already become ... in the topological
    closure of the past of a"), and WC2017's statement summary.

## Citation chasing

- OpenAlex `cites:` sweeps, all citing works retrieved and title-screened:
  CH1995 (115), Stein 1991 (259), WC2017 (66). Shortlisted items were checked
  at abstract or deeper level (see `sources.jsonl`). Full JSON retained
  locally in `_sources/cites-*.json` (untracked).
- Reference-chasing backward: WC2017's own framing of the shared-present
  collapse (Callender 2000; Wüthrich 2013; Saunders 2002 via Savitt CDLP and
  Viglione's reference list).

## Coverage assessment

Searched: Stein/CH lineage and all citing literature (through Oct 2026);
locally covariant QFT (BFV; FV; spin-statistics reformulations; qft.org
renderings); causal-set becoming (WC2017; Wüthrich 2023 handbook chapter;
Zalel 2023; Rideout-Sorkin lineage references); time-machine/deformation
program (Stein 1970b question via Manchak 2017); Viglione 2026 and recent
philosophy of cosmic simultaneity; Aames 2022; Savitt 2005/2020; Dorato
2002; Myrvold 2003; Müller 2019.

Not fully covered (residual risk, ordered by estimated threat):

1. CH1995 primary pages 365-367 and especially 385-386 (paywalled; exact
   wording of the "no obvious way" remark unverified; if that final section
   proposes a locality-based extension as the answer, the manuscript's
   *diagnosis* would be anticipated, though not its theorem).
2. "Natural operations on Lorentzian manifolds" mathematics (natural tensor
  /operators literature): searched only via the natural-transformation query;
   a classification of natural *binary relations* on Loc could exist there
   under different vocabulary (e.g. "natural relation", "invariant relation
   on the category of spacetimes").
3. Fewster-Verch 2012 full text beyond S1/S2 (60 pp.) — only abstract +
   introduction rendering read.
4. Stein 1968 full text (PhilArchive blocked; secondary quotes only).
5. Savitt 2005, Savitt 2009/2015, Dieks 2006, Dorato 2011, Earman 2008 full
   texts (abstracts/secondary renderings only).
6. Published BJPS version of WC2017 vs the 2015 draft read here.
7. Anything published in the last weeks (no preprint-server alert scan;
   OpenAlex and search coverage is inherently a few days behind).
