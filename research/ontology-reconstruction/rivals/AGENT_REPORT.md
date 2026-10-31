# AGENT_REPORT — ontology-rival-contracts

29 October 2026 (resumed run; worktree was clean at start, no prior
partial outputs existed, so the task was completed in this run).
Worker submission for independent review — not accepted completion.

## Done / files

- `research/ontology-reconstruction/rivals/RESULT.md` — four
  source-anchored model contracts (E eternalism, G preferred-slicing
  GBT, B C&R bow-tie spatiotemporaryism, F local becoming/fragmentalism)
  on the ROADMAP ten-field template; a comparison matrix; the developed
  physics-agreement pair (E vs F) with three precise non-collapse
  criteria and explicit collapse conditions; strongest escape routes
  from the project's existing objections for each contract; gates and
  proposed next tasks.
- `research/ontology-reconstruction/rivals/sources.jsonl` — 15 source
  records in the knowledge/README schema (validated by script); access
  gates recorded rather than filled.
- This root report (only other file written; no other paths touched).

Done-when checklist: four charitable source-backed contracts (§2–5);
physics agreement vs ontological disagreement separated (§7.1–7.2);
strongest rival replies retained (§7.3–7.4, §8).

## Search capability check (required)

- `scholar_search` (OpenAlex): **worked** — used for C&R-related
  metadata (Dorato–Hoefer critique located; not fetched, already
  covered by lane records).
- `exa` (`web_search_exa`, `web_fetch_exa`): **worked** — Putnam PDF
  text, Bell PDF text, Broad archive item, Ellis abstract, Earman
  abstract/metadata, Clifton–Hogarth metadata.
- `web-search-prime`: **not retried** — quota exhausted until
  2026-11-17 per brief; no calls made.
- `serpapi_search`: not needed this run.
- No MCP configuration changes; no installs.

## Source coverage (this run's depths)

| Source | Depth this run | Route |
|---|---|---|
| Putnam 1967, J. Phil. 64(8) | full-text | publicly posted scan via exa; locators pp. 240–247 |
| Broad 1923, Scientific Thought | full-text of key passage (pp. 66–68) | archive.org djvu.txt OCR, downloaded and grepped locally |
| Bell, "How to teach special relativity" (1987 reprint) | full-text of opening/closing sections | publicly hosted PDF via exa; printed p. 77 header confirmed |
| Ellis 2006 (arXiv:gr-qc/0605049v5) | abstract | arXiv abs + ar5iv (body not extractable this run) — gated |
| Earman 2008 | abstract | OpenAlex/exa — §§5–7 rest on local-fragmentalism lane's full-text record (PDF not in worktree) — gated |
| C&R, Nothing To Come chs. 7, 9 | full-text (via chapter lane; files re-verified in worktree) | user-supplied PDFs, SHA-256 in chapter-lane register — chs. 1–5, App. 2–3 gated |
| C&R, Replies §8 | full-text (via coordinator lane record) | not fetched this run |
| Stein 1991 | full-text (via foundations record; page images inspected there) | not re-read |
| Stein 1968 | discovery/gate | unread; only C&R's p. 149 quotation used |
| Clifton–Hogarth 1995 | abstract/gate | paywalled; maxim quote rests on fragmentalism lane's full-text read |
| Fine 2005 | full-text (via fragmentalism lane record; PDF not in worktree) — gated | lane page-map caveats retained |
| stein-gr main.tex | full-text (in worktree) | theorem statements quoted from the file at commit 8b93418 |
| Project records (STRONGEST_VIEW, PAIRED_CONTRACTS, EXPLANATORY_ROLE_TEST, chapter CLAUSES/RESULT) | full-text | read in this worktree |

## Verification commands and results

- `git status`/`git log` at start: clean tree at commit 8b93418; branch
  `agent/ontology-rival-contracts`; owned output dir absent (fresh run).
- Broad passage located and verified:
  `curl` archive.org djvu.txt → `grep -n "becoming"` → `sed -n
  '2900,2990p' | tr -s ' '`: the pp. 66–68 clauses ("accepts the
  reality of the present and the past …", "The sum total of existence
  is always increasing …", "Let us call the third kind of change
  Becoming") found verbatim after OCR whitespace normalization;
  independently matches the SEP transcription (two-source check).
- Putnam text: exa fetch of the posted scan; thesis (1), Principle III,
  and the pp. 246–247 conclusions extracted with OCR-spacing
  normalization; consistent with `knowledge/foundations` full-text
  audit (independent check).
- Bell text: exa extraction; Lorentz "real rest … aether" clause at
  printed p. 77 confirmed by page header.
- Ellis: abstract clause verified identically on arxiv.org/abs and
  ar5iv (two fetches). Body fetch attempted twice (ar5iv, arxiv PDF) —
  failed to return body text; recorded as gate, no body quotes used.
- stein-gr theorems: `sed -n '/begin{theorem}/,/end{theorem}/p'` on
  `research/stein-gr/main.tex`; quoted statements match the manuscript.
- sources.jsonl validated: `python3` schema check — 15 records, all
  required fields present, depths within the allowed vocabulary.

## Strongest contrary evidence encountered (recorded, not buried)

1. **Ellis 2006 v5 explicitly rejects preferred surfaces** — the
   nearest physics growth-view is worldline-based, not slicing-based.
   Contract G is therefore anchored on Broad+Bell(+cosmic-time
   scoping), and Ellis is recorded as a neighbouring variant, not
   support.
2. **Earman 2008**: no non-cheating Broad-type model constructions;
   G's escape routes must carry this (RESULT §8, item G).
3. **The red-team translation argument** (five groups): E-vs-F
   collapse pressure; answered by criteria, not dismissed (RESULT
   §7.3), with the honest limit that the collapse conditions
   (a)–(c) are substantive positions someone may accept.
4. **Coordinator EXPLANATORY_ROLE_TEST**: defeats parsimony defaults
   and package-consistency shortcuts; my falsifier-exposure criterion
   is independent of it and the possible divergence is flagged as an
   open question rather than resolved.
5. **BATCH2_INITIAL_REVIEW**: not relied on; the two rejected technical
   submissions are unused here (brief instruction respected).

## Limitations

- Access gates as listed in sources.jsonl: Stein 1968, C&H 1995,
  Fine 2005 PDF (not in worktree), Earman 2008 PDF (not in worktree),
  Ellis body, C&R chs. 1–5 and Appendices 2–3, Sider/Mellor depth.
- Quotes resting on other lanes' full-text reads are labelled as such;
  I did not re-open the user-supplied C&R PDFs (not present in this
  worktree; the lane's extraction files are).
- RESULT §7.3 criteria are [ours] — proposals for review, not
  established results; §7.4's formal claim is conditional on unread
  appendices.
- No physics was computed; no runs beyond text retrieval/grep; no
  dependencies installed; no coordination files touched.

## Proposed next tasks

See RESULT §10: equivalence lane to attack the three collapse
criteria; bridge-premises lane on Principle III and the Bell–Lorentz
hidden-frame premise; source acquisition (ILL) for the gated items;
SME Lorentz-violation scout for G's foliation; coordinator
reconciliation of this matrix with the natural-assignments lane.

## Blockers

None outstanding for this task's scope. The gated items require
library/ILL access outside a worker run.
