# Frontier search log

Checked 2026-10-19. Window definitions: last 90 days = 2026-07-21 through 2026-10-19 inclusive; past year = 2025-10-19 through 2026-10-19. Search used the configured Z.ai `web_search_prime` endpoint and targeted arXiv primary records. Search result summaries are discovery aids; source records distinguish abstract-level from discovery-only checks. No claim of systematic completeness.

## Queries and outcomes

| Date | Query focus | Outcome |
|---|---|---|
| 2026-10-19 | `site:arxiv.org quantum clocks relational time 2026 July OR August OR September` | Found QRF beyond subsystems (2607.24976; July 27), canonical clock sectors (2607.23852; July 26), and earlier March/May relational clock leads. The latter two July sources satisfy 90-day cutoff. |
| 2026-10-19 | `site:arxiv.org causal set becoming 2026 OR 2025 causal order growth` | Found causal-set embedding uniqueness (2607.05840; July 7, outside 90-day window), plus May horizon/geometry work and other less directly relevant results. No direct causal-set becoming paper in the exact window surfaced. |
| 2026-10-19 | `site:arxiv.org thermal time emergent spacetime 2026 2025` | Found noncommutative Minkowski thermal-time application (2502.12750), spin-glass exploration (2510.20902), and unrelated emergent-spacetime results. No clearly relevant thermal-time item in last 90 days found. |
| 2026-10-19 | `site:arxiv.org quantum reference frames indefinite causal order 2026 2025` | Found operational meaning of QRF (2607.03417; July 3, outside 90-day window), March time-delocalization work, and older QRF/ICO literature. Results mix causal-order representations with fixed-background time evolutions; these are not interchangeable. |
| 2026-10-19 | `site:arxiv.org/abs/ quantum clocks 2026 "Aug" OR "Sep"` | Surfaced time-of-arrival/ring clocks (2603.27311, revised Aug 21), but its relevance to foundational clock ontology is secondary; also metrology and Lorentz-violation papers excluded from this map. |
| 2026-10-19 | `site:arxiv.org/abs/ "thermal time" OR "emergent spacetime" 2025` | Returned several 2025 results. Kept thermal-time application and spin-glass title as leads; excluded cosmology framework and condensed-matter supersymmetry hits as not direct time-foundations evidence from metadata alone. |
| 2026-10-19 | `site:arxiv.org/abs/ "causal set" 2026 embedding` | Identified 2607.05840 and its abstract claim about well-conditioned embeddings. It is 14 days before the exact window, but within past year. |
| 2026-10-19 | `site:arxiv.org/abs/ "quantum reference frames" 2026` | Identified algebraic/non-subsystem, operational, correlation-geometry, local reference-field, and tetrad formulations. Kept the recent non-subsystem and operational papers; other hits are discovery leads for follow-up. |
| 2026-10-19 | Exact-title searches for `2607.24976`, `2607.05840`, `2607.03417`, `2607.23852`, `2608.16762`, `2606.08595`, `2603.08845`, and seed `1912.00033v3` | Verified some exact titles and abstract summaries, but search indexing did not return full text consistently. No equation, theorem, proof, or numerical result is claimed as read here. |

## Coverage and exclusions

Fifteen usable records are in `sources.jsonl`: causal-set growth/becoming and embedding; relational trinity, relativistic trinity, Page–Wootters measurements and spacetime QRF; newer QRF operational/non-subsystem directions; time-delocalization; one thermal-time deformation and one emergent-spacetime exploration; and a local-observer-clock lead. The 90-day window directly yielded two clearly relevant records (2607.24976 and 2607.23852) and one mathematical geometry result just outside it (2607.05840); 2608.16762 is also inside the window, but its abstract was not recovered. Counts indicate search coverage only.

Excluded or deferred: generic quantum-clock metrology, symmetry-breaking bounds, causal discovery/time-series papers, unrelated emergent-spacetime materials in condensed matter, and papers whose only known connection is a search snippet. “No result surfaced” is not evidence no result exists. Crossref/journal forward citation searches and full-text reference chasing remain undone.

## Search failures and caveats

The endpoint sometimes conflated publication/revision dates and returned results irrelevant to foundational time. The July 2026 hits were checked against the specified inclusive date boundary. Search snippets are not proof checks. No primary PDF was downloaded or locally reproduced; all physics claims below remain source claims as represented in abstracts/metadata.

## Second-pass primary-text audit (2026-10-19)

The coordinator reopened this lane for a bounded theorem/assumption pass. Versioned arXiv HTML was inspected for 1912.00033v3 (full relevant clock/trinity sections), 2007.00580v1 (quadratic-clock sectors and conditioning), 2607.24976v1 (Appendix B interaction and finite Abelian example), Smith–Ahmadi 1712.00081v3 (interaction kernel and conditional norm), and Rijavec 2204.11740v3 (interaction restrictions). Additional forward-citation searches from the Smith–Ahmadi journal record / QRF record identified:

| Lead | Status in this pass | Consequence for novelty |
|---|---|---|
| Rijavec, arXiv:2204.11740v3 / PRD 108, 063507 (2023), “Robustness…” | Full HTML consulted; extracted restricted interaction assumptions `[H+ h,V]=0` and `[h,V]=0` (Sec. V.1, Eqs. 47–48), but not all interaction solution equations. | Defeats broad claim that PW with interactions is untreated. It does not on its own establish interacting Trinity equivalence. |
| Chataignier, Höhn, Lock & Mele, arXiv:2409.06479 / NJP 28, 034504 (2026), “Relational dynamics with periodic clocks” | Abstract checked. Claims a periodic-clock relational trinity, partial group averaging and a revised PW conditional-probability rule for continuous-spectrum systems. | Strong falsifier for “periodic clocks lack trinity”; theorem details remain unread. |
| Mendes, Brito & Soares-Pinto, arXiv:2107.11452 / Universe 11, 308 (2025), “Non-linear equation… interaction and quasi-ideal clocks” | Abstract checked only. | Explicit interaction + non-ideal/quasi-ideal clock lead; no abstract-level claim treated as theorem audit. |
| De Vuyst, Höhn & Tsobanjan, arXiv:2507.14131 / Quantum 10, 2196 (2026), “On the relation between perspective-neutral, algebraic, and effective QRFs” | Abstract checked only. | Closely related to QRF-equivalence scope; limits any novelty claim about relating frame formalisms until full comparison. |

The exact trinity paper explicitly handles covariant clock POVMs and nonorthogonal clock states but assumes no clock-system interaction. The relativistic extension handles a quadratic clock with two frequency sectors separately and normalization tied to sector localization; do not extrapolate to arbitrary degenerate spectra or coherent cross-sector superpositions. The 2026 paper’s finite example is one concrete interaction, not a classification of all interactions. See `theorem-matrix.md` for exact assumptions, equations and the bounded candidate/falsifier.

Thermal-time/records leads were separately retained: Connes–Rovelli 1994 (state-dependent modular flow), Menicucci–Olson–Milburn 2011 (finite thermal clock and time scaling), Martinetti–Rovelli 2012 (bridge from modular flow to proper time), Chua 2024 (critical analysis of the modular-time interpretation), Milburn 2020 (thermodynamic model of clocks), and Hartle 2016 / Page 1993 (records and time-asymmetry interpretation). They are distinct lineages; none is evidence that records or modular flow establish objective passage. Some were only discovery/abstract and are labeled accordingly in the source records.

Bounded forward check: the new leads above were discovered through the cited primary records and bibliographic/search results, not an exhaustive citation graph. No absence claim about unresolved cases is warranted. No seed, board, or files outside `knowledge/frontier/` were changed.
