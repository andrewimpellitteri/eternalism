# Lane: axiomatic-relativity

Task: extract the axiom systems and definability/non-definability results
behind simultaneity and relativity (Andréka et al.; Besnard; Malament; Stein),
mark NOVELTY.md candidate C against them. Review submission, 2026-10-19.

## Files

- `sources.jsonl` — 17 new records, IDs prefixed `axrel-`. Validated: each
  line parses, all required fields present, `read_depth` in
  {discovery, abstract, full-text}, IDs unique.
- `axioms-and-theorems.md` — axiom list (SpecRel/AccRel/GenRel; the
  Malament-line structures), exact theorem statements with locators, reading
  depth per source, what the results do not show about temporal ontology.
- `ablations-and-temporal-ontology.md` — settled-ablation tables (Malament
  line A1-A12; Budapest FOL line B1-B7), candidate-C marking, seams with
  defeat-searches, ontology separation checklist.

## Reuse of existing source IDs (per knowledge/README.md contract)

No duplication: sources already registered in the knowledge base are
referenced by their existing IDs and NOT re-recorded here.

| Existing ID | Source | Note for coordinator |
|---|---|---|
| `seed-axiomatic-relativity` | arXiv:1105.0885 | read to full text this pass (arXiv HTML v1); its `read_depth: abstract` can be upgraded on acceptance |
| `seed-besnard-simultaneity` | arXiv:1104.1263 | read to full text (arXiv HTML v1; published DOI 10.1007/s10701-012-9649-5 verified) |
| `found-malament-1977` | Noûs 11(3):293-300 | read to full text this pass via public JSTOR scan (lps.elte.hu course mirror); DOI 10.2307/2214766 re-verified via Crossref; record can be upgraded from abstract; note the record's earlier Crossref fix was correct |
| `found-stein-1968` | J. Phil. 65(1):5-23 | UNREAD: philpapers 403, wayback capture of `STEOES.pdf` turned out to be a different document (filename collision), JSTOR/PDC paywalled; DOI 10.2307/2024512 re-verified via Crossref; content used only via secondary sources |
| `found-stein-1991`, `found-putnam`, `found-sarkar-stachel-1999`, `found-sep-malament`, `seed-einstein-1905`, `seed-isabelle-relativity`, `found-malament-1977` (dependencies) | foundations lane | used as recorded; no independent re-reading except where stated |
| — | Sarkar & Stachel 1999 | DOI 10.1086/392684 verified via Crossref this pass; the existing record lists no DOI and may add it on acceptance |

## Identifier verification log (2026-10-19)

Verified against arXiv landing pages or Crossref API (`api.crossref.org`)
before recording; no identifier in `sources.jsonl` or the analysis files is
unverified, and guesses are marked as such:

- arXiv:1105.0885v1 (landing page) — Andréka, Németi, Madarász, Székely;
  journal ref Hungarian Philosophical Review 2010/4, pp. 204-222.
- arXiv:1104.1263v1 (landing page) — Besnard; related DOI 10.1007/s10701-012-9649-5
  (also cross-checked at Semantic Scholar).
- DOI 10.2307/2214766 (Crossref) — Malament, Noûs 11(3), 1977-09, p. 293.
- DOI 10.2307/2024512 (Crossref) — Stein, J. Phil. 65(1), pp. 5-23, 1968.
- arXiv:gr-qc/0011050v1 (landing page) — Giulini; BJPS 52(4):651-670 (2001);
  DOI 10.1093/bjps/52.4.651 via Semantic Scholar record.
- arXiv:1202.6578v3 (landing page) — Mamone-Capria; Found. Phys. 42:1365-83
  (2012); related DOI 10.1007/s10701-012-9674-4.
- DOI 10.1093/bjps/axl019 (Crossref) — Ben-Yami 2006, BJPS 57:459-479.
  (An earlier lane-internal guess of `axl025` was wrong; corrected here.)
- DOI 10.1007/s10702-005-7539-1 (Crossref) — Hogarth 2005, FoPhL 18:491-497.
- DOI 10.1007/s10701-009-9328-3 (Crossref) — Grünbaum 2010, Found. Phys. 40:1285-1297.
- DOI 10.1063/1.1704140 (Crossref) — Zeeman 1964, J. Math. Phys. 5(4):490-493.
- DOI 10.1086/392920 (Crossref) — Rynasiewicz 2001, Phil. Sci. 68(3):S345-S357.
- DOI 10.1086/392684 (Crossref) — Sarkar & Stachel 1999, Phil. Sci. 66:208-220.
- DOI 10.1007/s10701-005-9041-9 (Crossref) — Madarász–Németi–Székely 2006,
  Found. Phys. 36:681-714.
- DOI 10.1007/s11229-011-9914-8 (Crossref) — "A logic road…", Synthese 186:633-649.
- DOI 10.1007/s10701-019-00306-7 (Crossref) — Ben-Yami 2019, Found. Phys. 49:1355-1364.
- DOI 10.1007/s11245-014-9237-8 (Crossref) — Ben-Yami 2014, Topoi 34:277-281.

Unverified locators (kept out of claims, flagged in records): Robb 1914
archive.org hint; Goldblatt Springer hint; Spirtes ProQuest hint; the 2019
Semantic Scholar item "Directed theories of time and the conventionality of
simultaneity" attributed to D. Malament (dead source URL, unverifiable
attribution — listed in AGENT_REPORT.md, not in sources.jsonl).
