# Agent report: kb-discriminators

Date: 2026-10-19  
Scope: proposed observational/experimental discriminators for temporal-ontology packages; public primary-source screen.  
Owned paths: `knowledge/discriminators/` only.

## Files changed

- `knowledge/discriminators/sources.jsonl` — 11 unique lane-prefixed records after adding a full-text numerical review of the 2026 LAGEOS PRL alongside the original abstract-level PRD record. Read depths: 6 full-text, 5 abstract. Records include exact publication/preprint versions, locators where read, model assumptions, status, dependencies, related project source IDs, and limits.
- `knowledge/discriminators/comparison-ledger.md` — anchor-model comparison contract and 8 proposal-level records spanning Brading, preferred-frame gravity, SME resonator/clock tests, Page–Wootters clocks, cold-atom entropic time, and quantum proper-time interferometry.
- `knowledge/discriminators/ownlane/AGENT_REPORT.md` — this handoff.

## Primary claim checks

1. Brading 2013 (plus abstract-level 2015 follow-up): the 2013 paper retains P2, special relativity as a complete account of spatiotemporal structure, while revising the epistemic-versus-ontological role of that account. Its law-constitutive present has no specified measurement protocol or quantitative signature. The separate 2015 abstract says empirical refutation would require resources beyond SR, but does not name a test. Existing shared record `found-brading` is linked rather than overwritten.
2. Lucchesi et al. 2026 LAGEOS: the APS abstract gives a summary scale |α1|~2×10^-5. The full PRL reports α1=(+2±3)×10^-5 (GEODYN II) and (+1±2)×10^-5 (SATAN), where ± is statistical 1σ, plus total systematic RSS σsys≈7.7×10^-6. These estimates are compatible with zero and must not be presented as a confidence-level upper bound. They constrain a coupled preferred-frame gravity package; they do not test an uncoupled hidden foliation.
3. Barontini 2026 cold-atom analog: inspected full arXiv v2, including Eqs. (1)–(6) and experiment discussion. Eq. (3) is signed, τ=(σ/kB)∫(dS/dφ)|dφ|, retaining sign of dS/dφ and not guaranteeing monotonicity. The paper reports monotonic ordering almost everywhere plus wiggles where dS and dφ change sign in coarse sampling. Bright-sector coarse-grained Shannon entropy is S=Ns; total mini-universe entropy is a distinct quantity, reported constant within experimental errors. Effective Schrödinger fit adds mean-field, mass-function, positive-branch and expansion assumptions. This is an operational analog/time-coordinate benchmark, not evidence that cosmological time or an ontology is emergent.

Additional positive package-level discriminator: Müller et al. 2007 rotating resonator comparison reports simultaneous limits at 10^-16 on five electron and eight photon SME coefficients. It demonstrates that physical Lorentz-violating packages are testable and can be excluded by data; it does not measure an ontological label.

## Checks and evidence

- Parsed every JSONL line with Python's standard JSON parser; confirmed 10 unique IDs and all required source-record fields.
- Checked in-scope file status; unrelated untracked `knowledge/aqft-locality/` and `knowledge/arrow-cosmology/` were left untouched.
- Read `AGENTS.md`, `README.md`, `knowledge/README.md`, `knowledge/NOVELTY.md`, the `kb-discriminators` brief, and existing frontier/foundations/methods source registers before writing.
- Public primary sources checked: Brading DOI/author-linked paper text; APS and arXiv pages for Barontini, Moreva, LAGEOS, SME clock comparisons, optical-cavity tests, and trapped-ion proper-time proposal; PMC full text for Loriani et al.; APS abstract for Foster & Jacobson. Full details and read-depth limits are in `sources.jsonl`.

## Limitations and unresolved questions

- Brading's full article was screened via indexed/author-linked text; no independent argument reconstruction. The 2015 follow-up remains abstract-level.
- Abstract-level records intentionally do not claim detailed equation/proof audit. The 2026 LAGEOS orbit reduction/systematics and Einstein-aether coupling-region conversion need full-paper/table audit before parameter-specific exclusions are stated.
- SME bounds are coefficient/model dependent; this lane avoids reporting a scalar “current bound” where results constrain correlated combinations. Update the broader coefficient inventory against current data tables before quantitative use.
- Barontini data were not independently reanalyzed or reproduced. Eq. (3) is signed and does not guarantee monotonicity; whether the reported ordering is robust under independent entropy/coarse-graining analysis and how the analog transfers to WDW models remain open checks.
- Proposed Loriani and Sorci clock signatures have not been reproduced here; Sorci's feasibility/systematics reside partly in supplemental protocol.
- Empirical equivalence claimed for a hidden foliation is limited to cases where stipulated dynamics and accessible records are unchanged. No general representation equivalence or gauge theorem is claimed.
- Bounded screening is not evidence of novelty or untreatability; forward citation checks and adversarial comparison with more recent experiments remain.

No board transition, commit, installation, or other lane edit was made. Submitted for coordinator review; not accepted as complete.
