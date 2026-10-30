# Root PDF relocation manifest

30 October 2026. All 36 loose PDFs in the repository root were moved into
the owning lanes' `sources/` directories (user-requested). Filenames were
kept unchanged so textual references remain findable; destinations follow
the referencing lane (or best content affinity where unreferenced). One
exact duplicate was deleted after checksum comparison.

| File | New home | Basis |
|---|---|---|
| 0034-4877%2871%2990024-3.pdf | research/where-openness-lives/sources/ | referenced in NOTE.md |
| 02698590802496680.pdf | research/local-fragmentalism/sources/ | PRIOR_WORK/NEW_PAPERS_CHECK refs |
| 0607380v1.pdf | research/brading-universe-frontier/sources/ | sources.jsonl ref |
| 0607380v1 (1).pdf | **deleted** | byte-identical to 0607380v1.pdf (md5 db705343…) |
| 1.1665157.pdf | research/stein-gr/sources/ | unreferenced; JMP classic, stein-gr affinity |
| 1.522874.pdf | research/stein-gr/sources/ | unreferenced; JMP classic, stein-gr affinity |
| 2024512.pdf ("On Einstein–Minkowski Space–Time") | research/bowtie-horizons-prior-art/becoming/sources/ | becoming sources.jsonl ref |
| 288328.pdf (Stein, Gödel time-structures) | research/stein-gr/sources/ | author affinity |
| 3-540-54978-1_11.pdf (Isham QG chapter) | research/brading-universe-frontier/sources/ | sources.jsonl ref |
| 9409001v1.pdf | research/brading-universe-frontier/sources/ | sources.jsonl ref |
| 978-3-030-15948-1_6.pdf | research/bowtie-horizons-prior-art/becoming/sources/ | becoming sources.jsonl ref |
| 978-3-319-78704-6_7.pdf (C&R ch. 7) | research/future-truth-rival-chapters/sources/ | review record; path field updated |
| 978-3-319-78704-6_9.pdf (C&R ch. 9) | research/ontology-reconstruction/coordinator/sources/ | SHA-256 recorded in RIVAL_PROFILE_AND_REGULARITY_BRIDGE.md; review path field updated |
| 978-94-007-1180-8_26.pdf (Petkov-vol. chapter on a present in Minkowski) | research/bowtie-horizons-prior-art/becoming/sources/ | content affinity |
| In Search of Cosmic Time.pdf | research/brading-universe-frontier/sources/ | sources.jsonl ref |
| S1871-1774%2806%2901007-2.pdf | research/bowtie-horizons-prior-art/becoming/sources/ | becoming sources.jsonl ref |
| S1871-1774%2806%2901008-4.pdf | research/bowtie-horizons-prior-art/becoming/sources/ | becoming sources.jsonl ref |
| WuthrichChristian2010PetkovColl_NoPresQG.pdf | research/local-fragmentalism/sources/ | redteam note refs |
| bf00370321.pdf (Diodorean modality) | research/local-fragmentalism/sources/ | PRIOR_WORK ref |
| bf00414289.pdf (Belnap, Branching space-time) | research/local-fragmentalism/sources/ | PRIOR_WORK ref |
| bf00708432.pdf (Relativity and the status of becoming) | research/local-fragmentalism/sources/ | PRIOR_WORK ref |
| bf01645389.pdf (Global aspects of the Cauchy problem) | research/stein-gr/sources/ | ENERGY_CONDITIONS.md ref |
| bjps%2F48.2.257.pdf | research/bowtie-horizons-prior-art/becoming/sources/ | becoming sources.jsonl ref |
| bjps%2F54.3.475.pdf | research/bowtie-horizons-prior-art/becoming/sources/ | becoming sources.jsonl ref |
| cpa.3160440305.pdf (Christodoulou, BH formation) | research/bowtie-horizons/sources/ | sources.jsonl ref |
| isham.pdf | research/brading-universe-frontier/sources/ | unreferenced companion of the 3-540 chapter (distinct file, kept) |
| j.shpsb.2015.02.001.pdf (thermodynamic arrow/cosmology, SHPMP 2015) | knowledge/arrow-cosmology/sources/ | content affinity |
| jdg%2F1090425530.pdf | research/stein-gr/sources/ | ENERGY_CONDITIONS.md ref |
| monist200588323.pdf (ontological insignificance, relativistic simultaneity) | research/bowtie-horizons-prior-art/becoming/sources/ | content affinity |
| presentism_and_qg_vp_3_dd.pdf | research/local-fragmentalism/sources/ | Viglione affinity |
| s00023-007-0341-9.pdf (AHP 2007, EM/GR) | research/stein-gr/sources/ | content affinity |
| s000230050006.pdf | research/stein-gr/sources/ | ENERGY_CONDITIONS.md ref |
| s10701-025-00844-3.pdf (Radical perspectivalism, FoPh 2025) | research/local-fragmentalism/sources/ | PRIOR_WORK/redteam refs |
| s11098-018-1178-4.pdf (fragmentalist interpretation of SR) | research/local-fragmentalism/sources/ | PRIOR_WORK/redteam refs |
| s11229-005-5515-8.pdf | research/local-fragmentalism/sources/ | PRIOR_WORK ref |
| s13194-022-00471-z.pdf (temporal becoming, causal diamonds, Gödel) | research/bowtie-horizons-prior-art/becoming/sources/ | content affinity |

Notes: filenames unchanged; no `local_file` fields referenced root paths
(the two absolute-path mentions in
`research/future-truth-rival-chapters/review/sources.jsonl` were updated).
SHA-256 values recorded in existing records remain valid (moves only).
