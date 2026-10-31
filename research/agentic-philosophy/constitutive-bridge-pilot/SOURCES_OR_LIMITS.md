# Sources and limits — constitutive-bridge pilot

31 October 2026. Task `ontology-constitutive-bridge-pilot`. Worker:
GLM-5.3-Flash via OpenCode, isolated worktree
`ontology-constitutive-bridge-pilot`.

## 1. Search capability check (required, recorded)

| Tool (server) | Query | Result |
|---|---|---|
| `web-search-prime` | "Brading law-constitutive present presentism criticism" | **FAILED** — MCP error -429, code 1310, "Weekly/Monthly Limit Exhausted", resets 2026-11-17 10:00 |
| `serpapi_search` | "Dainton specious present extended present physical systems duration experience temporality" | **FAILED** — "Your account has run out of searches." |
| `exa` `web_search_exa` | semantic query for existing sustaining-activity/extended-system-present arguments | **WORKED** — 8 results |
| `scholar_search` | "process ontology" presence present extended ongoing processes temporal | **WORKED** — openalex/arxiv/crossref results |

Per the brief: web-search-prime was tested first and did not work; available
public tools (exa, scholar_search) were used instead. Two of four search
tools were quota-exhausted; coverage was correspondingly narrow (see §4).

One follow-up batch fetch (2 URLs) was used to inspect the one result that
looked like a potential close precedent before extracting any conclusion,
per the search-summaries-are-leads rule.

## 2. Inherited sources (not read by this worker; depth = inherited)

These control the nearest-precedent comparisons in RESULT.md §8. Depths,
locators, and hashes are recorded by the primary reviewer lane
(`research/article-admissibility/primary-review/SOURCES.md`) and the
coordinator (`WEAK_COUPLING_AND_TEMPORAL_EXTENT.md` §1,
`PILOT_QUESTION.md`). I did not open these files this session.

| id | Source | Inherited depth | Key locators used |
|---|---|---|---|
| brading-2013 | Brading, "Presentism as an Empirical Hypothesis", *Philosophy of Science* 80(5): 1101–1111 (2013) | full-text (reviewer); all 11 pages | §§4–6, pp. 1104–1108 |
| brading-2015 | Brading, "Physically Locating the Present", *SHPSA* 50: 13–19 (2015), DOI 10.1016/j.shpsa.2014.09.007 | full-text (reviewer); §5 pp. 17–18 reread directly by coordinator | §5, printed pp. 17–18; p. 18 concession |
| brown-pooley-2004 | Brown & Pooley, "Minkowski Space-Time: A Glorious Non-Entity", arXiv physics/0403088v1 (2004; 2006 chapter 67–89 not collated) | full-text arXiv HTML (reviewer) | §§3–5 |
| balashov-janssen-2003 | Balashov & Janssen, "Presentism and Relativity", philsci-archive 525 preprint (30 pp.) | full-text preprint (reviewer) | §§9–11, archive pp. 17–24 |
| response-benchmark | `RESPONSE_MEMORY_BENCHMARK.md` (coordinator, 2026-10-30): transport channel §6, representation-invariance §7 | project internal, audited | §§6–7 |
| weak-coupling | `WEAK_COUPLING_AND_TEMPORAL_EXTENT.md` (coordinator, 2026-10-30) | project internal, audited | §§1, 5, 7 |
| constitution-note | `CONSTITUTION_IS_NOT_PREDICTION.md` (coordinator, 2026-10-30) | project internal | §§1–3, 7–8 |
| submission-review | `CONSTITUTIVE_SUBMISSION_REVIEW.md` (coordinator, 2026-10-30) | project internal | §§1–3 |
| explanatory-role-test | `EXPLANATORY_ROLE_TEST.md` (coordinator, 2026-10-29) | project internal | §§2–3 |
| pilot-question | `PILOT_QUESTION.md` (coordinator, 2026-10-31) | task brief | all |

Marking rule: no inherited reading was upgraded. Statements attributed to
Brading, Brown–Pooley, or Balashov–Janssen in RESULT.md rest on the
inherited register, not on my inspection; if the register is wrong, the
comparison is wrong.

## 3. Direct external reads this session (also in sources.jsonl)

1. **Müller 2019** — Springer landing page + abstract, open access.
   *Abstract depth.* Nearest formal precedent for an extended dynamic
   present; grounded in indeterministic modal correlation, not sustaining
   activity. Full branching-space-times formalism NOT read.
2. **"The Coherence Threshold"** (philarchive PORTCT-17) — page text
   (~first sections). *Discovery depth.* Unrefereed; no author, version, or
   date visible on the fetched page; "proof of interiority" claim not
   audited and not relied on.
3. **Guarino & Guizzardi 2024**, Synthese — search-result abstract only.
   *Discovery depth.*
4. **Esser 2026**, Synthese — search-result abstract only. *Discovery depth.*

## 4. Limits of the search

- One small batch only (4 queries; 2 failed on quota), as the brief allows.
  No systematic Brading-citation chase was possible with the working tools.
- I did not verify whether any published follow-up develops Brading 2013/2015
  into a positive sustaining-window argument. Müller 2019 and the
  coherence-threshold preprint are the closest items found; a fuller
  priority audit needs working search access (retry after 2026-11-17) and
  should include: Brading's citation forward, SoS/branching-time "present"
  literature, Seibt's process presence work, and Dainton's specious-present
  line (the serpapi query that failed targeted this last item).
- No paywalled full texts were read; no credentials or private sources used.

## 5. Limits of the argument itself

- Conditional on the pilot's stipulated common ground (sustaining unity
  granted). It does not advance the constitutive step.
- P2's defense is by deflation-cost against that stipulation plus a category
  argument; it is not an independent proof, and a perdurantist who accepts
  the deflation exits the common ground rather than being refuted.
- The physical case is one idealized apparatus (boundary-driven transport
  channel, point-like idealizations inherited from the benchmark); no claim
  about field-theoretic or quantum settings.
- The Kepler pair discussion is qualitative; no orbital mechanics was
  computed (none needed).
- Compute: none beyond file/git operations; within the stated bounds
  (hard ≤ 15 s, actual ≤ 10 s, total ≤ 30 s — trivially satisfied).

## 6. Verification performed

- `git status`/`git log` before and after commit; only owned paths staged by
  explicit path (`git add` of the lane directory and root AGENT_REPORT.md;
  no `git add -A`).
- `sources.jsonl` schema check: every line parsed as JSON and required keys
  (`id`, `title`, `url`, `checked_on`, `read_depth`, `kind`, `relevance`,
  `limits`) verified via python3 json parsing (stdlib only, no install).
