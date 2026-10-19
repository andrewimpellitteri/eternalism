# Search log — kb-preferred-foliation

Date: 2026-10-19. Worker: glm-kb-preferred-foliation (OpenCode GLM headless).

## Search capability check (required by brief)

- At task start: MCP servers: `tools.opencode.list_mcp_resources()` returned
  zero resources and zero templates — **no `web-search-prime` or other Z.ai
  research MCP tool was available at the initial check**.
- Built-in `websearch` tool: invoked twice ("Tumulka relativistic GRW …",
  "Mark Hubert relativistic collapse mass density ontology"); both calls
  failed with `{"error":{"type":"unknown","message":"Web search cancelled"}}`.
- Mid-run update: the `web-search-prime` MCP tool appeared in the Code Mode
  catalog and **worked** on three queries ("Hubert relativistic collapse
  theory foliation"; "Hubert collapse model quantum field theory paper";
  '"Mario Hubert" collapse relativity spacetime philosophy'). Note for
  consumers of its output: results arrive as a JSON-encoded string wrapping
  another JSON string (double parse required).
- Working substitutes used throughout (all public sources):
  - arXiv abs pages and arXiv search UI via HTTPS fetch (worked; one burst of
    `export.arxiv.org/api/query` calls hit HTTP 429, after which only the
    regular arxiv.org endpoints were used, spaced sequentially).
  - Crossref REST API (`api.crossref.org`) for DOI/metadata verification
    (worked; occasional 429 cleared by slower sequential requests with a
    `mailto` parameter).
  - DuckDuckGo HTML endpoint (`html.duckduckgo.com`) as a general web-search
    fallback (worked).
- Net conclusion for the report: search capability = degraded for the first
  phase (direct fetches only), fully functional after the mid-run appearance
  of `web-search-prime`. No source is claimed as read that was not actually
  fetched; search snippets were used only as leads and are labeled as such
  where they informed a record (see `fol-bedingham-modak-sudarsky-2016-bh`).

## Query batches (by theory family)

1. Relativistic GRW/flash: arXiv title search "Relativistic Version of the
   Ghirardi" → quant-ph/0406094; ar5iv full-text of quant-ph/0406094;
   Crossref 10.1007/s10955-006-9227-3, 10.1063/1.2219373; Crossref
   bibliographic "general argument against superluminal transmission" →
   BF02817189 (1980, not 1988 as first recalled).
2. Mass density / CSL: Crossref bibliographic "Models of wave-function
   collapse underlying theories and experimental tests" → DOI
   10.1103/RevModPhys.85.471 + arXiv search → 1204.4325; arXiv abs
   1003.2774, 1111.1425, 2506.07959; Crossref 10.1007/s10701-010-9510-7,
   10.1007/s10955-013-0814-9, 10.1103/PhysRevA.42.78.
3. Bohmian: arXiv title search "Hypersurface Bohm-Dirac models" →
   quant-ph/9801070 (confirms reused `phil-bohm-foliation`); arXiv title
   "Can Bohmian mechanics be made relativistic" → 1307.1714; ar5iv full
   texts of 1307.1714 and quant-ph/9801070; Crossref 10.1098/rspa.2013.0699,
   10.1103/PhysRevA.60.2729, 10.1088/0305-4470/38/4/R01; Cambridge Core
   contents page of Speakable 2nd ed. (chapter titles + page ranges).
4. Tomonaga-Schwinger / hypersurface collapse: Crossref 10.1143/PTP.1.27
   (403 at OUP landing), 10.1103/PhysRev.74.1439, 10.1103/PhysRevD.1.566,
   10.1103/PhysRevD.24.359; arXiv title "Born's rule for arbitrary Cauchy
   surfaces" → 1706.07074; Crossref 10.1007/s11005-019-01239-y.
5. Myrvold / "Hubert": Crossref bibliographic "peaceful coexistence collapse
   postulate relativity" → 10.1016/S1369-8486(02)00004-3; arXiv title
   "Relativistic Markovian dynamical collapse…" → 1709.03219; Crossref
   10.1103/PhysRevA.96.062116, 10.1017/9781108562218.003;
   `philpapers.org` search blocked (HTTP 403); arXiv author "Hubert, M" →
   only Mia Hubert (statistics); mario-hubert.com/publications fetched in
   full — no relativistic-collapse paper listed.
6. Lorentz-Poincaré: DDG for Poincaré 1906 (Springer DOI 10.1007/BF03013466
   verified via Crossref), Lorentz 1904 scans (JHU-hosted PDF located, not
   fetched), Routledge "Einstein, Relativity and Absolute Simultaneity"
   (landing 200, ISBN confirmed), Wiley Maudlin QLR (DDG → Wiley Online
   Books DOIs; Crossref 10.1002/9781444396973 = 3rd ed. 2011).
6b. `web-search-prime` round (mid-run): "Hubert relativistic collapse theory
   foliation" → surfaced Bedingham-Modak-Sudarsky PRD 94:045009 (DOI
   Crossref-verified; added as discovery), Piccione arXiv:2610.10980 (abs
   page fetched; added as abstract), Allori 2022 philarchive lead, Snoke
   2023 philsci-21770 lead, and the open PDF of Myrvold's 2019 chapter on
   core.ac.uk (PDF fetch unsupported; still unread). Two further Hubert
   queries and one on frame-dependent collapse-rate tests produced no new
   primary sources; the CMB-frame results were generic and are not recorded.
7. Detectability: arXiv search "LISA Pathfinder collapse" → 1611.09776 and
   2411.17588 (2025 update, recorded as lead only); arXiv title "Underground
   test of gravity-related wave function collapse" → 2111.13490; Crossref
   10.1103/PhysRevLett.119.110401, 10.1038/s41567-020-1008-4,
   10.1103/PhysRevD.94.124036.
8. Secondary: SEP "Collapse Theories" entry fetched (authors Ghirardi &
   Bassi; first published 2002, revised 2025-09-30).

## Identifier errors caught by verification (would have entered the record otherwise)

- quant-ph/0406097 ≠ Tumulka's relativistic GRW — that ID is Eakins &
  Jaroszkiewicz, "Counterfactual errors and state reduction in relativistic
  quantum physics". Correct ID: quant-ph/0406094.
- arXiv 1204.4632 ≠ Bassi et al. RMP 2013 — that ID is a µSR paper. Correct:
  1204.4325.
- Bedingham 2011 DOI recalled as 10.1007/s10701-010-9424-1 — wrong. Correct:
  10.1007/s10701-010-9510-7.
- "Can Bohmian mechanics be made relativistic?" authorship recalled as
  Dürr-Goldstein-Tumulka-Zanghì — wrong: includes Travis Norsen, not Tumulka.
- Myrvold 2002 title recalled as "…is the collapse paradigm compatible with
  relativity?" (Quo Vadis chapter) — the SHPMP paper is "…is the collapse
  postulate incompatible with relativity?".
- GRW no-superluminal argument recalled as 1988 Foundations of Physics —
  actually 1980, Lettere al Nuovo Cimento 27:293-298.
- Balashov-Janssen pages recalled 327-350 — Crossref: 327-346.
- "Hubert-style" assumed to be Mark Hubert — no such arXiv/Crossref author
  with relativistic-collapse work located; nearest is Mario Hubert (see map
  §6 unresolved item).
- Tumulka "Collapse and Relativity" pages recalled 155-170 — Crossref:
  340-351.

## Blocked / unread sources (recorded as unread, never as read)

- OUP/J-Stage landing for Tomonaga 1946: HTTP 403.
- PhilPapers search pages: HTTP 403 (bot block).
- philsci-archive.pitt.edu eprint page 14718: "Request Rejected".
- Myrvold 2002 PDF (publish.uwo.ca): located; PDF fetch unsupported → unread.
- Balashov-Janssen, Myrvold 2019 chapter, Maudlin QLR, Craig-Smith volume,
  GRW 1980, GPR 1990, Hellwig-Kraus, Aharonov-Albert, Tomonaga, Schwinger,
  Lorentz 1904, Poincaré 1906: metadata verified; texts not accessed (see
  `read_depth: discovery` in sources.jsonl).

## Known gaps / next search passes

- Bell's ch. 9 and ch. 19 texts (Speakable) — needed for any direct quotation
  of the Lorentzian viewpoint or the QFT-beables frame statement.
- Full texts of Myrvold 2002 and Myrvold 2017 (proof scope conditions); the
  Myrvold 2019 chapter is available at core.ac.uk/download/pdf/157868389.pdf
  (PDF fetch unsupported here — unread).
- Hellwig-Kraus acausality discussion and Aharonov-Albert 1981 argument at
  first hand.
- Interacting relativistic collapse: partially addressed by the Piccione 2026
  preprint (abstract-level) and the Bedingham-Modak-Sudarsky 2016 application
  (discovery); both need full-text passes. Allori 2022 (flash ontology and
  hyperboloid proper-time foliation; philarchive ALLWII-5) and Snoke 2023
  (philsci-21770) are located leads not yet recorded as source records.
- Preferred-frame dependence in collapse phenomenology: no primary source on
  frame-dependent collapse-rate tests surfaced in the `web-search-prime`
  round; the 2025 LISA update (Phys. Rev. A 111, L020203, arXiv:2411.17588)
  remains a lead.
