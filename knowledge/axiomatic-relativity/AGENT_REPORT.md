# AGENT_REPORT — kb-axiomatic-relativity

Worktree: `/Users/andrew/eternalism/.worktrees/kb-axiomatic-relativity`
Branch: `agent/kb-axiomatic-relativity`. Date: 2026-10-19.
Status: review submission, not accepted completion.

## Done / files

Task: read to full text Andréka et al. (arXiv:1105.0885), Besnard
(arXiv:1104.1263), and the Malament/Stein definability results they rely on;
extract axioms and exact theorem statements with hypotheses and locators;
state what the results do not show about temporal ontology; mark NOVELTY.md
candidate C against already-settled ablations.

Files changed (all inside allowed paths):

- `knowledge/axiomatic-relativity/sources.jsonl` — 17 new `axrel-*` records;
  validated JSONL (fields, depths, unique IDs). Existing IDs reused by
  reference, not duplicated (map in `knowledge/axiomatic-relativity/README.md`).
- `knowledge/axiomatic-relativity/axioms-and-theorems.md` — axiom systems
  (SpecRel, AccRel, GenRel language-by-language; Malament-line structures),
  exact theorem statements with locators and honest read-depth table,
  ontology non-implications.
- `knowledge/axiomatic-relativity/ablations-and-temporal-ontology.md` —
  settled-ablation tables (A1-A12 Malament line, B1-B7 Budapest FOL line),
  candidate-C marking with four unclaimed seams and their defeat-searches,
  ontology-separation checklist.
- `knowledge/axiomatic-relativity/README.md` — lane index, ID reuse map,
  identifier verification log.
- `AGENT_REPORT.md` — this file.

Headline outcomes (for the coordinator's cross-lane review):

1. Four target papers read to full text: 1105.0885v1, 1104.1263v1, and —
   beyond the abstract-level state they were in — Malament 1977 (public JSTOR
   scan) and Giulini 2001; plus Mamone-Capria 2012 full text as the key later
   systematic source. Stein 1968 remained inaccessible (see Blockers);
   grounded in two full-text-read secondary sources instead.
2. The candidate-C ablation space for Minkowski simultaneity is substantially
   occupied: the literature already settles symmetry-vs-directedness of the
   causal primitive, time-reflection, dilations, worldline-vs-frame,
   chronology, clock, global-vs-local data, soundness criteria, and a
   systematic automorphism-group classification (with published corrections
   of predecessors). Four seams are recorded as unverified leads with explicit
   defeat-searches; no gap is claimed.
3. Two identifier corrections for cross-lane use: Ben-Yami 2006 DOI is
   10.1093/bjps/axl019 (not axl025 as an earlier internal note guessed);
   Sarkar–Stachel 1999 DOI is 10.1086/392684 (missing from the existing
   foundations record).

## Search capability check (required by brief)

- `web-search-prime` MCP: NOT AVAILABLE at session start.
  `tools.opencode.list_mcp_resources()` returned empty resources/templates,
  and no such tool existed in the Code Mode catalog. The brief's fallback was
  used: public web tools + citation chasing.
- Built-in `websearch`: FAILED 3× ("Web search cancelled") — recorded as
  unavailable, not worked around silently.
- Alternative public APIs used for discovery/verification: arXiv abs/HTML
  pages, Crossref REST (`api.crossref.org/works…`), Semantic Scholar graph
  API, Unpaywall, Wayback availability API. All worked (Crossref and
  Semantic Scholar rate-limited occasionally; retried with spacing).
- `web-search-prime` BECAME AVAILABLE mid-session (tool-catalog update) and
  was then tested successfully on a task-relevant query ("directed theories
  of time conventionality of simultaneity Malament"). It returned usable
  results, including the public Malament 1977 PDF mirrors that enabled the
  full-text read. Both facts (initial absence, later success) are recorded
  here for the capability audit the brief requested.

## Source coverage

Full-text read (primary): arXiv:1105.0885v1 (HTML), arXiv:1104.1263v1 (HTML),
Malament 1977 pp. 293-300 (JSTOR scan at lps.elte.hu, fetched and text-
extracted), arXiv:gr-qc/0011050v1 (Giulini, HTML), arXiv:1202.6578v3
(Mamone-Capria, HTML).
Full-text read (secondary): SEP "Conventionality of Simultaneity" (2018
revision + "Further Discussion" supplement), SEP "Being and Becoming in
Modern Physics" (2021 revision).
Abstract/discovery level: Zeeman 1964 (Crossref abstract), Ben-Yami 2006,
Hogarth 2005, Grünbaum 2010, Rynasiewicz 2001, MNS 2006, "logic road" 2012,
Ben-Yami 2019, Ben-Yami 2014, Spirtes 1981, Robb 1914, Goldblatt 2004,
Andréka et al. 2002 report (dead URL).
Unread despite attempts: Stein 1968 (see Blockers).
Deliberately out of scope this pass: the Budapest school's deeper corpus
(2002 report unreachable; Handbook chapter, Székely thesis, Studia Logica
papers paywalled or unlocated), Winnie 1970a/b, Minguzzi 2002, preferred-
foliation phenomenology (covered by knowledge/discriminators lane).

## Verification commands and results

- arXiv landing pages fetched for 1105.0885, 1104.1263, 1202.6578,
  gr-qc/0011050: titles, authors, versions (v1/v3), journal refs confirmed.
- Crossref API queried for each DOI listed in
  `knowledge/axiomatic-relativity/README.md` (§ Identifier verification log):
  all returned matching title/container/volume/pages. Representative command
  shape: `GET https://api.crossref.org/works/10.2307/2214766` → Noûs 11(3),
  1977-09, p. 293; `GET …/works?query.bibliographic=Ben-Yami+Causality+and+
  Temporal+Order+in+Special+Relativity` → DOI 10.1093/bjps/axl019.
- JSONL validation run:

```sh
python3 - <<'EOF'
import json
seen=set()
req=["id","title","url","checked_on","read_depth","kind","relevance","limits"]
for i,line in enumerate(open("knowledge/axiomatic-relativity/sources.jsonl"),1):
    d=json.loads(line); assert not [k for k in req if k not in d], (i)
    assert d["read_depth"] in {"discovery","abstract","full-text","reproduced","code-audited"}
    assert d["id"] not in seen; seen.add(d["id"])
print("OK", len(seen))
EOF
# → OK 17
```

- Malament PDF integrity: `curl -sL -o … && file malament1977b.pdf` →
  "PDF document, version 1.6", 9 pages, JSTOR cover sheet with correct
  citation (Noûs 11(3) Sep 1977, pp. 293-300) and matching first page text;
  text layer extracted with macOS PDFKit via `osascript -l JavaScript`
  (no packages installed).
- Negative verification (important): the Semantic Scholar "green OA" link
  for Stein 1968 (`philpapers.org/archive/STEOES.pdf`, via web.archive.org)
  was fetched and its text extracted — it is a 4-page student essay on
  Russell, not Stein. Stein 1968 stays recorded as UNREAD; no theorem was
  quoted from it as verified.

## Strongest contrary evidence (to the readings this lane relies on)

- Mamone-Capria 2012 documents *corrections* to Giulini 2001's Thm 2 and
  Thm 5 (everywhere-dense subgroups of ℝ missed) and an error in an unnamed
  paper's Thm 2 (his fn 6 re P-invariance); any use of Giulini's
  classifications must cite the corrected forms.
- Giulini 2001 (§5) identifies a genuine proof gap in Sarkar–Stachel 1999
  (classes of a G-invariant partition need not be G-invariant sets), while
  agreeing with their critique of time-reflection invariance; Besnard 2011
  additionally shows their half-cone definitions presuppose a time
  orientation beyond κ. So "Malament's theorem refuted" and "theorem
  unquestionable" are both wrong; the theorem holds exactly under its stated
  invariance group.
- Against reading Malament's theorem as anti-conventionalist: Janis's
  per-observer latitude argument (SEP Sec. 3), Grünbaum 2010, and
  Mamone-Capria 2012 §4 ("does not cut in the debate") — three independent
  positions; plus Malament's own Sec. 1 framing (conditional on the causal
  theory of time's criterion).
- Besnard Thm 5.1 is itself contrary evidence to the privileged status of
  standard synchrony: with only locally accessible data, Σ_X is not even
  definable-as-invariant. Any synthesis must keep A1 and A8 in tension
  rather than averaging them.

## Limitations

- Stein 1968 not read; its theorem is recorded only as reported by SEP and
  found-stein-1991, flagged as unaudited in every location it appears.
- Besnard's results are single-source here (no independent re-derivation in
  the corpus); proofs were read, not reproduced. Same for the Budapest
  theorems, whose deeper proofs live in inaccessible cited works.
- The Budapest ablation table (B1-B7) covers only the 19-page intro paper;
  the school's full ablation corpus was not reachable, so B-list completeness
  is NOT claimed.
- `web-search-prime` was unavailable for most of the session; coverage of
  post-2012 literature relied on Crossref/Semantic-Scholar/APA queries and
  reference chasing, not systematic search. A dedicated forward-citation
  sweep on Besnard 2012 (Found. Phys.) and on Ben-Yami 2006 is still missing.
- No Lean/Isabelle artifacts inspected (out of this lane's scope; methods
  lane owns formalization).

## Proposed next tasks

1. Forward-citation sweep (defeat-search) on Besnard 2011/2012, Ben-Yami
   2006, Giulini 2001, Mamone-Capria 2012 for 2012-2026 ablation results —
   would confirm or kill seams S1-S4 in ablations-and-temporal-ontology.md.
2. Obtain and audit Stein 1968 (library/JSTOR access needed) and, if
   candidate C advances, Robb 1914/1936 vs symmetric-κ axiom sets.
3. Extract the precise GenRel/AccRel axiom texts from the Synthese "logic
   road" paper and Székely thesis (needed before any Lean encoding).
4. Resolve the unverified Semantic Scholar lead "Directed theories of time
   and the conventionality of simultaneity" (attributed to D. Malament,
   2019; dead URL) — if it is a Malament manuscript, it directly touches
   candidate C.
5. Audit the Cont-independence countermodels (B5) if any formalization claim
   is contemplated.

## Blockers

- Stein 1968: JSTOR and PDC paywalled; philpapers 403 (bot wall, also for
  reader proxies); the only public "OA" copy is a filename collision
  (different document). Recorded as unread rather than read.
- Andréka et al. 2002 report: renyi.hu URL 404; no verified mirror found
  before scope cutoff.
- Hogarth 2005, Grünbaum 2010, Rynasiewicz 2001, Ben-Yami 2006/2014/2019:
  paywalled; recorded at abstract/discovery depth with secondary-derived
  content explicitly marked.
- Occasional Crossref/Semantic Scholar 429 rate limits; worked around by
  spacing queries; no query was left unverified because of this.

Committed files: only the five paths listed under Done/files.
No workboard, runner, AGENTS.md, or other lane's files touched. No
dependencies installed; no subagents launched; nothing pushed or merged.
