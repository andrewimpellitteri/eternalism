# Agent report: empirical-discriminator-audit

Date: 2026-10-21. Worker: native research subagent (GPT-6 Luna lane), shared
checkout, task `empirical-discriminator-audit`, priority 8. Submission only; this
goes to coordinator review and is not accepted completion.

## Files changed

- `research/discriminators-audit/RESULT.md` (new) — audit, P/M/O/E/N/X
  classification, master table (21 candidates), decision-rule table, three
  protocols (one concrete, one equivalence-breaking, one schema), the
  no-discrimination argument, defeat search, source/read-depth ledger,
  limitations, open questions.
- `research/discriminators-audit/AGENT_REPORT.md` (new, this file).

No other file was written. `WORKBOARD.jsonl`, `WORKBOARD.md`, `scripts/`,
`AGENTS.md`, `paper/`, the knowledge registers and every other task directory
were read-only in this run. No commit, push, merge, reset, deploy or agent launch.
No dependency installs; no Python beyond the standard library (used only for a
Markdown table/ID integrity check).

## What was read

Project instructions and state: `AGENTS.md`, `README.md`,
`knowledge/README.md`, `knowledge/NOVELTY.md`, the task brief from
`scripts/agents.py brief empirical-discriminator-audit`, `paper/READINESS.md`,
`paper/main.tex` (full), `paper/README.md`, `paper/references.bib` (full),
`paper/SOURCE_AUDIT.md` (grep-level), `paper/reviews/revision-2/REVIEW.md`
(grep-level for LAGEOS and source limits), `research/conclusions/SYNTHESIS.md`
(§5–§8), `research/adversarial-review/AGENT_REPORT.md`,
`research/source-gates/AGENT_REPORT.md`,
`research/operational-stability/RESULT.md`,
`research/event-filter-resources/RESULT.md`,
`research/article-admissibility/PROTOCOL.md`.

Lane records used for the candidate set and inherited depths:
`knowledge/discriminators/comparison-ledger.md` and `sources.jsonl`;
`knowledge/preferred-foliation/theory-map.md` and `search-log.md`;
`knowledge/arrow-cosmology/comparison.md`;
`knowledge/causal-sets/comparison-candidate-A.md`;
`knowledge/thermal-records/comparison.md`;
`knowledge/defeat-search/candidate-A.md`;
`knowledge/clock-interactions/sources.jsonl`;
`knowledge/discriminators/ownlane/AGENT_REPORT.md` (coordinator review);
`knowledge/audits/stein-printed-pages` (via the source-gates report).

Primaries fetched by this audit (arXiv abstract pages, 14): 1009.3058, 1105.4531,
gr-qc/0311055, 2501.10588, astro-ph/0209274, 1412.4006, 0908.1832, 2411.17588,
1912.00033, 1710.00707, 2409.06479, 1910.02474, quant-ph/9903047, 1206.6578.
No primary PDF was downloaded or read; numerical values (LAGEOS $\alpha_1$,
systematic RSS) are inherited from the project's full-text records and
`paper/main.tex`, not re-read. This limitation is stated in RESULT.md §9–§10 and
must not be upgraded by this report.

## Method

1. Extract the manuscript's own admissibility conditions (i)–(iv), the three
   inferential burdens, and the two fixed admissibility profiles. Use them as the
   scoring frame rather than inventing a new one.
2. Build a candidate list only from sources with a real, checkable locator,
   including the families named in the brief plus three additions that are
   commonly proposed as "time tests" (GRB dispersion, delayed-choice eraser,
   indefinite causal order). Add the structural/definability results and the two
   philosophical proposals with no protocol so the category boundary is explicit.
3. Classify each as P (parameter constraint), M (model selection), O (ontology
   discriminator), E (equivalence/no-discrimination), N (no admissible protocol),
   or X (category crossing). Reserve O for M plus an independently defended
   exclusivity premise.
4. For each row, name the bridge premise the ontological inference would need and
   test whether a rival ontology can carry the same physical structure.
5. State decision rules: what observation changes the model verdict and what, if
   anything, changes the ontology verdict. Give one concrete protocol and its
   exact stopping point, one equivalence-breaking protocol, and the only schema
   that would change the underdetermination verdict.
6. Run a bounded defeat search on the audit's own conclusion.

## Findings

- **No candidate is O.** Twenty-one candidates: 5 primary parameter constraints,
  7 primary model-selection tests, 2 equivalence results, 4 primary category
  crossings, 4 with no admissible protocol. D1 is counted in both the parameter
  and model-selection groups; D17 carries a secondary category-crossing use.
- **Strongest candidate:** D1, coupled preferred frame / LAGEOS $\alpha_1$. It has
  a named model with the disputed structure coupled, real precision data, and a
  specified signal. It still fails because a block/eternalist package can carry
  the same aether field. It is also weaker than usually presented: the two values
  are software-package analyses of the same satellite programme rather than two
  independent experiments, and aether regions with vanishing $\alpha_1$ exist, so
  even a null is a slice constraint rather than a model exclusion.
- **Runner-up:** D11, causal-set growth. It is the only place where a
  growth-vs-completed difference is even definable, and the current result is a
  proved equivalence for covariant records. Its escape route (stage-relative
  access) is an access assumption that a block can also host.
- **Positive equivalence results** (D5 relational clocks, D11 causal-set growth)
  are the rows that most directly support underdetermination; both are scoped to
  declared model classes.
- **Structural result (bookkeeping, not new):** a likelihood gap between
  ontologies requires an exclusivity premise, because bridge premises are
  normally probabilistically inert. Every candidate's discriminating structure
  is a coupling, an access restriction, or a probability-law change; in each case
  the rival ontology has an admissible realization carrying it.
- **What would change the verdict:** Protocol C, i.e. a defended demonstration
  that one ontology's constitutive commitments entail a coupled structure and the
  rival's forbid it. No such demonstration exists in the screened literature.

## Evidence and checks

- Every row has an exact locator (journal/volume/page or arXiv ID plus section,
  equation or table where the claim depends on one). Locators for inherited
  records are the versions recorded in the project lanes; they were not silently
  upgraded.
- 14 primaries were metadata-verified today. Where an abstract is the only thing
  read, the row says so and the claim attributed to the paper is confined to what
  the abstract states (e.g. D10's "do not differ significantly" is a direct
  abstract quotation).
- Numeric claims are limited to LAGEOS values already used in `paper/main.tex`
  and checked by the revision-2 review, with the review's caveats preserved.
- Markdown structure check (standard-library Python): all five tables have
  consistent pipe counts; 21 unique IDs, each appearing once per table.
- No computational or physical result is claimed. RESULT.md §6 is explicitly
  labelled bookkeeping on the manuscript's definitions.

## Search capability and failures (recorded, not hidden)

- `serpapi_search` (Google) worked for all queries.
- `web-search-prime` (Z.ai MCP) failed with `MCP error -429`
  "Weekly/Monthly Limit Exhausted. Your limit will reset at 2026-11-17 10:00:29".
  This is a tool-quota failure, not a research finding.
- `philarchive.org` returned HTTP 403 (Cloudflare challenge). A preprint titled
  "Quantum Physics Prefers the Present" is therefore a snippet-level lead only
  and is used for no verdict.
- General web search is poor for philosophy-of-physics primary literature; the
  audit relies on the project's existing full-text lanes for the substance and
  treats its own web search as a bounded defeat check only.

## Limitations

- No primary PDF read by this audit; the classification inherits lane depths.
- The LAGEOS orbit reduction, systematics and PRL body were not re-audited; the
  revision-2 review's caveat stands.
- The audit covers the manuscript's schematic ontology families, not a full
  taxonomy of hybrid or deflationary views.
- The "exclusivity" result is a framework consequence, not a novel theorem, and
  it depends on the probabilistic-inertness assumption (P2), which is stated and
  scoped rather than proved.
- The defeat search is bounded and its negative result is not proof of absence.

## Unresolved questions

1. Is there a published calculation of frame-dependent collapse rates, and do
   existing bounds constrain it? This is the most promising route to a genuine
   model-selection test with a foliation signature, and it is still not an O.
2. What is the current observational status of everpresent $\Lambda$? Not covered
   by `knowledge/causal-sets`; needs a dedicated read.
3. Can the definability results be turned into an exclusion argument whose
   premises a presentist must accept? Separate task.
4. Does any actual ontology carry an exclusivity commitment, stated as
   constitutive and independently motivated? The audit found none.
5. The blocked "quantum physics prefers the present" preprint should be read
   before anyone claims the literature is uniformly on the underdetermination
   side.

## Coordination notes

- Stayed within `research/discriminators-audit/`.
- No workboard transition requested; the coordinator owns board state.
- This is a submission for review, not accepted completion.
