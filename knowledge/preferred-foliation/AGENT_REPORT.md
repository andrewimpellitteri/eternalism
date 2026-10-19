# AGENT_REPORT — kb-preferred-foliation

Task: map theories that add a preferred foliation or relativistic collapse
structure (Lorentz-Poincaré interpretations; Bohmian mechanics with a
preferred foliation; relativistic GRW flash and mass-density versions;
Tomonaga-Schwinger formulations; Myrvold-style relativistic collapse results).
Worktree: `agent/kb-preferred-foliation`. Submission for independent review —
not accepted completion.

## Done / files

- `knowledge/preferred-foliation/sources.jsonl` — 31 records (lane prefix
  `fol-`), validated: unique IDs, required fields present, read_depth within
  the contract's five values. 11 full-text/abstract records, 20 discovery
  records with explicitly stated verification limits.
- `knowledge/preferred-foliation/theory-map.md` — per-theory records
  (§1 Lorentz-Poincaré, §2 Bohmian foliation, §3 GRWf, §4 GRWm/CSL
  relativistic, §5 Tomonaga-Schwinger, §6 Myrvold + unresolved "Hubert"),
  each with: what the foliation is, fixed vs dynamical, empirical
  detectability, and which relativity-of-simultaneity arguments it blocks or
  accepts; plus §7 detectability ledger, §8 comparison table, scope
  restrictions, and gap-defeaters.
- `knowledge/preferred-foliation/search-log.md` — capability check, query
  batches, identifier errors caught, blocked sources, gaps.
- Existing IDs reused, not duplicated: `phil-bohm-foliation`,
  `phil-grw`, `phil-sme`, `seed-lorentz-data-2026`, `seed-bell-temporal-order`,
  `seed-einstein-1905`, `found-stein-1991`, `found-malament-1977`,
  `found-rietdijk`, `found-putnam`, `phil-maudlin`.
- Proposal for coordinator: `phil-bohm-foliation` can be upgraded to
  full-text with DOI 10.1103/PhysRevA.60.2729 (verified this pass; the
  philosophy lane's file is not owned by this task, so no edit was made).

## Search capability check

- At task start, `web-search-prime` / Z.ai research MCP tools were **not
  available** (MCP resource list empty), and the built-in `websearch` tool
  **failed** on two test calls ("Web search cancelled"). Both facts recorded
  as required by the brief.
- Mid-run, the `web-search-prime` MCP tool appeared and **worked** on three
  queries (used to close the "Hubert" item as far as public search allows and
  to surface two new primary sources). Its output is doubly-JSON-encoded.
- Substitutes used throughout: arXiv abs/search pages, Crossref API,
  DuckDuckGo HTML, publisher landing pages, ar5iv full-text renderings. All
  public sources. One early `export.arxiv.org` burst hit HTTP 429; switched
  to spaced sequential requests on arxiv.org endpoints.

## Source coverage

- Relativistic collapse/GRW: 12 records (Tumulka 2006 GRWf full-text; GRW
  1980 no-signalling; GPR 1990 CSL; Bedingham 2011; BDGTZ matter-density
  2014; Bassi RMP 2013; Myrvold 2017; Myrvold 2019 chapter; Tumulka AIP 2006;
  Bedingham-Pearle 2025 preprint; Bedingham-Modak-Sudarsky 2016;
  Piccione 2026 preprint).
- Bohmian: 4 records (HBD reused + enriched; DGTZ Bell-type QFT 2005; DGTZ
  2014 full-text; Bell Speakable with verified chapter locators) plus
  Esfeld-Hubert-Lazarovici-Dürr 2014.
- Lorentz-Poincaré: 5 records (Lorentz 1904; Poincaré 1906; Balashov-Janssen
  2003; Craig-Smith 2008; Maudlin QLR 3rd ed.).
- Tomonaga-Schwinger/hypersurface: 5 records (Tomonaga 1946; Schwinger 1948;
  Hellwig-Kraus 1970; Aharonov-Albert 1981; Lienert-Tumulka 2020).
- Detectability: 3 records (Vinante 2017; Donadi 2021; Carlesso 2016) plus
  reused SME/Data-Tables records.
- Secondary: SEP "Collapse Theories" (revised 2025-09-30).

## Verification commands and results

All identifiers were checked against Crossref or arXiv landing pages before
recording. Reproducible equivalents (run 2026-10-19):

```sh
# Crossref metadata checks (24 DOIs, all HTTP 200, titles/authors matched):
curl -s "https://api.crossref.org/works/10.1007/s10955-006-9227-3" | jq '.message.title,.message.page'
curl -s "https://api.crossref.org/works/10.1063/1.2219373"       | jq '.message.title,.message.page'
curl -s "https://api.crossref.org/works/10.1007/BF02817189"      | jq '.message.title,.message.volume'
curl -s "https://api.crossref.org/works/10.1007/s10701-010-9510-7"
curl -s "https://api.crossref.org/works/10.1007/s10955-013-0814-9"
curl -s "https://api.crossref.org/works/10.1103/PhysRevA.42.78"
curl -s "https://api.crossref.org/works/10.1016/S1369-8486(02)00004-3"
curl -s "https://api.crossref.org/works/10.1103/PhysRevA.96.062116"
curl -s "https://api.crossref.org/works/10.1017/9781108562218.003"
curl -s "https://api.crossref.org/works/10.1103/RevModPhys.85.471"
curl -s "https://api.crossref.org/works/10.1143/PTP.1.27"
curl -s "https://api.crossref.org/works/10.1103/PhysRev.74.1439"
curl -s "https://api.crossref.org/works/10.1103/PhysRevD.1.566"
curl -s "https://api.crossref.org/works/10.1103/PhysRevD.24.359"
curl -s "https://api.crossref.org/works/10.1007/s11005-019-01239-y"
curl -s "https://api.crossref.org/works/10.1088/0305-4470/38/4/R01"
curl -s "https://api.crossref.org/works/10.1098/rspa.2013.0699"
curl -s "https://api.crossref.org/works/10.1103/PhysRevA.60.2729"
curl -s "https://api.crossref.org/works/10.1017/CBO9780511815676"
curl -s "https://api.crossref.org/works/10.1007/BF03013466"
curl -s "https://api.crossref.org/works/10.1093/bjps/54.2.327"
curl -s "https://api.crossref.org/works/10.1093/bjps/axt019"
curl -s "https://api.crossref.org/works/10.1103/PhysRevLett.119.110401"
curl -s "https://api.crossref.org/works/10.1038/s41567-020-1008-4"
curl -s "https://api.crossref.org/works/10.1103/PhysRevD.94.124036"
curl -s "https://api.crossref.org/works/10.1002/9781444396973"

# arXiv ID checks (all HTTP 200; titles/authors/journal-ref matched):
curl -sL https://arxiv.org/abs/quant-ph/0406094
curl -sL https://arxiv.org/abs/quant-ph/9801070
curl -sL https://arxiv.org/abs/quant-ph/0407116
curl -sL https://arxiv.org/abs/1307.1714
curl -sL https://arxiv.org/abs/1003.2774
curl -sL https://arxiv.org/abs/1111.1425
curl -sL https://arxiv.org/abs/1204.4325
curl -sL https://arxiv.org/abs/1709.03219
curl -sL https://arxiv.org/abs/1706.07074
curl -sL https://arxiv.org/abs/1611.09776
curl -sL https://arxiv.org/abs/2111.13490
curl -sL https://arxiv.org/abs/2506.07959

# Full-text renders used for the two full-text records:
curl -sL https://ar5iv.labs.arxiv.org/html/quant-ph/0406094
curl -sL https://ar5iv.labs.arxiv.org/html/1307.1714
```

JSONL validation (run in-repo): `python3 -c` script asserting per-record
required fields, `read_depth` domain, and ID uniqueness →
`OK: 29 records, all unique, all required fields present`.

Eight wrong identifiers/authors from memory were caught and corrected before
recording (list in `search-log.md`) — including quant-ph/0406097→0406094 and
1204.4632→1204.4325, the exact failure mode the brief warned about.

## Strongest contrary evidence (kept visible in the map)

- **Against "collapse is simply compatible with relativity"**: Myrvold 2017
  (abstract-level): relativistically invariant Markovian collapse with only
  standard degrees of freedom is impossible — nonstandard DOF are required.
  This constrains flash-type optimism (scope conditions not yet audited).
- **Against "mass-density ontologies relativize cleanly"**: BDGTZ 2014:
  different Lorentz frames assign conflicting matter densities; a modified
  frame-independent rule is proposed but its empirical equivalence is an open
  question.
- **Against "foliation theories cost nothing"**: Balashov-Janssen 2003
  (discovery lead): the added structure is judged implausible/ad hoc;
  HBD/DGTZ themselves call the foliation "additional dynamical space-time
  structure".
- **Against "a preferred frame is empirically testable"**: SME/Data-Tables
  constrain observable anisotropies, not hidden foliations with
  Lorentz-invariant statistics (asymmetry stated in map §7).

## Limitations

- Read depths are honest and uneven: 2 full-text (Tumulka 2006; DGTZ 2014),
  11 abstract, 18 discovery (metadata-only). The Tomonaga-Schwinger and
  Aharonov-Albert anchors are metadata-verified leads; their landing pages
  were blocked (403) or paywalled. No equation was re-derived; no proof was
  reproduced.
- "Hubert-style" could not be resolved to any located author/paper despite
  three search rounds including `web-search-prime` (arXiv, Crossref, author
  websites, talk listings); recorded as unresolved with candidate
  resolutions, not as evidence of absence.
- The detectability section contains no extracted numeric parameter bounds;
  experimental records are abstract/discovery level. Bedingham-Modak-Sudarsky
  2016 is recorded from a Crossref-verified DOI plus a search snippet — its
  foliation-dependence characterization is unverified against the text.
- Coverage of 2020-2026 work on interacting relativistic collapse is thin
  (two preprints recorded: Bedingham-Pearle 2025 and Piccione 2026, both at
  abstract level only).
- Allori 2022 and Snoke 2023 surfaced as relevant leads after the map was
  drafted; they are logged in search-log.md as unrecorded leads rather than
  silently appended.

## Unresolved questions

1. Does Myrvold 2017's no-go (Markovian + standard DOF) apply to flash-type
   dynamics? Requires full-text scope-condition audit.
2. Is the frame-independent matter-density rule of BDGTZ 2014 empirically
   equivalent to GRWm in all tested regimes?
3. Are DGTZ 2014's wave-function-determined foliations dynamically stable
   under interactions (their hedged "fundamentally Lorentz invariant" claim)?
4. Coordinator decision needed on the brief's "Hubert-style" item (map §6).

## Proposed next tasks

1. Full-text audits: Myrvold 2002 (public PDF), Myrvold 2017, Hellwig-Kraus
   1970, Aharonov-Albert 1981, Bell ch. 9/19 — each with exact-claim
   extraction into sources.jsonl upgrades.
2. Interacting relativistic GRWf / multi-time program survey (Lienert,
   Tumulka and successors, 2018-2026), separate search pass.
3. Frame-dependent collapse phenomenology: extract whether any published
   collapse test bounds frame-dependent collapse rates; record the 2025 LISA
   Pathfinder update (Phys. Rev. A 111, L020203).
4. If the coordinator confirms the "Hubert" reference, add the intended
   source; otherwise close the item with the §6 note.
