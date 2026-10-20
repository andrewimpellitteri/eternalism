# Worker report: kb-arrow-cosmology

## Files changed

- `knowledge/arrow-cosmology/sources.jsonl` — 10 unique lane-prefixed source records: 6 full-text, 4 abstract-level. Includes standard Boltzmann/PH argument, Penrose WCH, Earman and Wallace objections, central-time and Newtonian-gravity alternatives, Boltzmann-brain/observer typicality, and a BABAR microscopic T-violation result.
- `knowledge/arrow-cosmology/comparison.md` — premise-to-conclusion table, model/version comparison, limits, nearest predecessors, and novelty falsifiers.

## Evidence and research depth

Primary source pages/full texts were inspected for Goldstein (2001), Goldstein-Tumulka-Zanghì (2016, arXiv v3), Penrose (1979 chapter scan), Lazarovici-Reichert (2018 arXiv text), and Dyson-Kleban-Susskind (2002 arXiv v3). Targeted argument extractions are recorded in the source entries, including: GTZ's discussion of two-sided entropy increase, non-normalizable measures, and the distinction between theoretical typicality and evidence-based inference; Penrose's own caveat that the Weyl/entropy correspondence was qualitative and the hypothesis vague; and Lazarovici-Reichert's separation of the entropic and relational gravitational arrows, plus their self-location/Boltzmann-brain problem for bounded-entropy fluctuation cosmologies.

## Bibliographic correction and subsequent review pass

An independent review caught an authorship error in the first version: arXiv:1203.3382 was incorrectly attributed to S. A. Goode and J. Wainwright. The original arXiv v4 record identifies Ovidiu-Cristinel Stoica as sole author, with v4 dated 2013-09-04 and the cited Annals of Physics 338 (2013), pp. 186-194, DOI 10.1016/j.aop.2013.08.002. The source ID and all comparison references are corrected to arrow-stoica-wch-2013. Metadata was checked against the original arXiv record; read depth remains abstract because no theorem/proof audit was done.

Wallace (2009/2010) was initially screened at abstract depth by the original worker. In a subsequent reviewer pass, primary arXiv HTML sections 2-4 and 8-10 were read, and the source record was upgraded to full-text with that provenance explicit. This adds the nuance that Wallace distinguishes gravity's changes to material dynamics/macrostates from entropy of gravitational field degrees of freedom; in his account collapse may lower matter entropy while heat/radiation transfer raises total entropy. He also contests an overly restrictive interpretation of Earman without claiming to solve the Past Hypothesis. No calculation was independently reproduced.

Four additional leads remain abstract-level only: Stoica's conditional quasi-regular singularity result, Earman's objection to a well-defined/sufficient cosmological Boltzmann entropy, original Carroll-Chen proposal, and BABAR's neutral-B T violation result. Claims are limited accordingly; no theorem/proof or experiment audit is represented as completed.

## Checks

- Read `AGENTS.md`, `README.md`, `knowledge/README.md`, `knowledge/NOVELTY.md`, and the brief from `python3 scripts/agents.py brief kb-arrow-cosmology` before editing.
- Checked existing `knowledge/frontier/`, `knowledge/foundations/`, and `knowledge/methods/`; reused their contextual distinctions and did not edit or duplicate their source registers.
- Source JSON schema and unique IDs were parsed/validated after the bibliographic correction; no general test suite was run.
- No dependencies installed; no board/runner/seed/shared files changed; no commit made.

## Limitations and unresolved questions

- Search was targeted, not systematic. No backward/forward citation audit, exhaustive scan of Boltzmann-brain measure proposals, or modern cosmological-data review was performed.
- Earman's argument remains abstract-level here; his detailed models need full-text reading before reliance on specifics. Wallace was upgraded to full-text for Secs. 2-4 and 8-10 only (see above).
- No current experimental bound or numerical entropy of the universe is asserted. The BABAR result is confined to microscopic neutral-B transitions and cannot be substituted for a thermodynamic arrow.
- WCH has no accepted, general gravitational entropy functional established by this lane. The cited later vanishing-Weyl result is only an abstract lead and conditional on a mathematical singularity class.
- The Newtonian N-body typicality model is not relativistic cosmology; reported simulations were not reproduced. Central-time typicality depends on measure and observer-conditioning choices.
- Nothing in the screened arguments entails temporal ontology, objective passage, determinism, or causal order. That separation is explicit in the comparison contract.

## Novelty status

No novelty claim. Nearest predecessors are enumerated in `comparison.md`. Any new formal or physical claim would need a broader search and independent challenge; candidate falsifiers are listed there.

## Coordinator review (2026-10-20)

- Verified on arXiv: GTZ arXiv:1602.05601v3 (2016-07-06), Phys. Rev. D 94, 023520; Goldstein cond-mat/0105242 has only v1 (2001-05-11), Lecture Notes in Physics 574.
- Corrected the Lazarovici–Reichert venue. The record named SHPS B 69 (2020), pp. 1-10, which no source supports; the paper appeared in the 2020 World Scientific volume *Statistical Mechanics and Scientific Explanation*. Also fixed the v2 date (2019-01-10, not 2018).
- Fixed the limitations bullet that still called Wallace abstract-level after the upgrade.
- Versioned the Goldstein URL. The checker's `\bv\d+\b` test misses old-style IDs such as `cond-mat/0105242v1`; that is a checker gap for rt-citation-gate-hardening, not a record defect.
