# AGENT_REPORT — ontology-modal-density-search (Route B only)

Worker: ontology-modal-density-search (GLM-5.3-Flash, OpenCode headless). Date: 2026-10-31.
Branch: `agent/ontology-modal-density-search`, isolated worktree `/Users/andrew/eternalism/.worktrees/ontology-modal-density-search`.
Status: **worker submission for independent review — not accepted completion, not a novelty verdict.**

## 1. Files changed / delivered

Owned files only (committed individually; no `git add -A`):

- `research/agentic-philosophy/result-search-round1/modal-density/CANDIDATE.md` — the candidate: exact inference, dense-comb counterexample with full clause audit, scope separation, strongest rival, independently motivated premise (sparseness), second case (accumulation comb), nearest-three delta/gaps, falsifiers, referee-packet verdict, proposed next tasks.
- `research/agentic-philosophy/result-search-round1/modal-density/sources.jsonl` — 6 strict-contract records (full-text: Müller 2020, Belnap 2003 postprint, Müller 2005, BMP 2021 chs. 1–3+10; abstract: Placek; discovery: citation chase).
- `research/agentic-philosophy/result-search-round1/modal-density/AGENT_REPORT.md` — this report (lane copy).
- `AGENT_REPORT.md` (repo root) — runner handback (same content). Note: this replaced a prior task's root handback (`stein-gluing-audit`, 2026-10-25) that was present in the branch's base commit; that report is preserved verbatim in the base commit `cb64c0a` and was not modified there.

Nothing else was created or modified. No board, coordinator, shared, runner, manuscript, or seed files touched. No installs, no subagents, no pushes, no merges.

## 2. Search capability check (as required)

- Tested capability: `web-search-prime` MCP tool. **Failed** with MCP error -429 (weekly/monthly quota exhausted; provider reports reset 2026-11-17). Reported here per the brief; no pointless retries.
- Fell back to `scholar_search` (worked) and `exa` web search/fetch (worked) for the bounded novelty/erratum check and OA source retrieval. Two small targeted batches, then the primary citation chase (OpenAlex), per brief limits.

## 3. Source coverage

| Record | Source | Depth | Key locators |
|---|---|---|---|
| rsb-muller2020-dynamic | Müller 2020, *Foundations of Physics* 50:644–664, DOI 10.1007/s10701-019-00267-x (OA version of record) | full-text (21 pp.) | Def. 6 p. 657; fn. 23 (no Weiner) p. 657; featureless clause p. 661; Theorem 1 pp. 661–662; fn. 26; §2.3 p. 655; §5 p. 662 |
| rsb-belnap2003-postprint | Belnap, "Branching space-time" postprint, PhilSci-Archive p1003 (orig. Synthese 92:385–434) | full-text (51 pp.) | Postulates 2-1, 4-1, 6-1, 7-1, 13-1, 13-5, 13-6, 13-8; Facts 13-11/13-12, 13-15 |
| rsb-muller2005-probability | Müller 2005, *BJPS* 56(3):487–520, DOI 10.1093/bjps/axi132 | full-text | Postulate 4 (Weiner) p. 513 + fn. 13; Def. 5 (MFB) p. 493; Post. 1 p. 495; App. A pp. 516–518; App. B Def. 21 (BST+S) pp. 518–519 |
| rsb-bmp2021-monograph | Belnap–Müller–Placek, *Branching Space-Times*, OUP (© 2022; project shorthand BMP 2021), chs. 1–3, 10 | full-text (chs. read in full) | Def. 2.10 p. 40; Fact 3.17 p. 64; Def. 3.15 p. 62; Fact 10.1 pp. 356–357; Def. 10.4 p. 359; Theorem 10.1 + proof p. 359; Def. 10.9 p. 375; Preface p. xiii (ch. 10 "integrates material from Müller (2006, 2019)") |
| rsb-placek2021-present | Placek, "Past, present and future modally introduced", *Synthese* 198(4):3603–3624, DOI 10.1007/s11229-019-02302-w (online first 1 July 2019) | abstract | degenerate "single event" case = all-events-chancy regime (dual of the comb) |
| rsb-openalex-muller2020-citations | OpenAlex work W2949901278 (cited_by_count = 17, re-verified via API 2026-10-31) + BJPS citing list | discovery | no correction/erratum/prior comb statement found |

Bibliographic verification performed this pass (single HTTP lookups, well within budget): OpenAlex count (17), Crossref DOIs for Müller 2005 and Placek. One locator correction recorded: the CANDIDATE's "Placek 2019" follows the online-first year; the version of record is Placek **2021**, Synthese 198(4):3603–3624 (flagged in the record for the reviewer; CANDIDATE text preserved per one-revision rule).

## 4. Verification methods

- **No computation was run.** All mathematical checks are symbolic hand proofs: maximal histories and containing-history sets of the comb; clause-by-clause audit against Müller 2020 Def. 6 and the Belnap 2003 postprint set; Weiner's postulate; historical connection; no-MFB (vacuous — the comb has no SLR pairs); featureless clause; direct computation of `cll(t) = ℚ∩(−∞,t)` and `CC(t)` from Def. 8, **not** via the paper's Fact 4 (no circularity).
- Executed checks were limited to: downloads and file-type checks of the OA PDFs (all confirmed PDFs); page-level PDF reads via the page-based `read` tool (no pdftotext/pypdf available in this environment); the bibliographic API lookups above.
- Computation budget respected trivially (no numerical grids; nothing approached the hard 15 s limit). The dense construction is handled by hand, not by a finite grid — per the brief's prohibition.
- Scope separation verified, not asserted: the BST_NF analogue of the comb *is* a BST_NF structure but every trunk event lies in a nontrivial choice set, so h_T is featureless under BMP 2021 Def. 10.4(ii) and Theorem 10.1 is not violated. Fact 3.17 (no choice points in BST_NF, p. 64) excludes the BST92 comb itself.

## 5. Core verdict (see CANDIDATE.md for the full argument)

The dense comb (trunk ℝ + one deterministic offshoot at each rational) satisfies every written clause of Müller 2020's Definition 6 plus Weiner's postulate, historical connection, and no-MFB; it is **not** featureless (irrational trunk events are not choice points; clause (i) fails — 1+ℵ₀ histories); direct CC computation gives `cll(t) = ℚ∩(−∞,t)` and `∼|h_T = identity`. **Theorem 1 (pp. 661–662) is false as stated** in its own written hypothesis class. Footnote 26's identity condition is shown incomplete (identity also results from dense-but-not-total chanciness). BT level: the §2.3 existential sentence survives; the "consecutive choice points" characterization is refuted.

**Scope boundaries (do not cross):** no counterexample claim against BST_NF (Theorem 10.1 survives via featurelessness); no claim against MBS/higher-dimensional relativistic spacetime; not a refutation of objective becoming; no breakthrough claim. The submitted claim is *corrective verification*: a short correction note is warranted; a full novelty packet is not.

## 6. Strongest contrary evidence encountered

The monograph rescope (BMP 2021 ch. 10, Theorem 10.1) is the strongest rival: the result is true as restated for BST_NF, and the comb cannot arise there (Fact 3.17). Answered in CANDIDATE.md §4: the 2019 journal statement remains the published claim, is false in its own hypothesis class, and was never flagged as false; the Preface (p. xiii) confirms ch. 10 was built from Müller (2006, 2019); the Theorem 10.1 proof's identity-triviality step ("only possible … in which each element of h is a member of an uncorrelated choice set", p. 359) is precisely where BST92 escapes. The BT-level §2.3 refutation has no BST_NF shelter at all.

## 7. Limitations

- The two riskiest clause checks (suprema-in-h at branch points; chain-PCP) were re-derived by hand by the same worker who proposed the candidate — independent re-audit is proposed task 1.
- Müller 2005's BST+S (Def. 21) admission of the comb is consistency-checked but not fully audited (CANDIDATE.md §11.4).
- Citation chase is discovery-level (titles/abstracts of 17 citing works); priority remains unknown.
- BMP 2021 chs. 4–9 not read; silent-rescope priority question unresolved.
- "Placek 2019" in the CANDIDATE is the online-first year; version of record is 2021 (recorded in sources.jsonl).

## 8. Unresolved questions / proposed next tasks

1. Independent re-audit of the two riskiest clause checks (suprema-in-h; chain PCP) by a reviewer who did not propose the candidate.
2. Decide whether the repaired theorem (non-featureless + sparseness + no-MFB) is provable in BST92, or admits a further MFB-based counterexample (space-like cause-like loci inside a choice-free stretch).
3. Author correspondence (or short note) on whether the 2019 statement's falsity under Def. 6 was known when Theorem 10.1 was rescored to BST_NF; priority resolution.
4. Optional: full audit of whether Müller 2005's BST+S genuinely admits the comb.

## 9. Handback

Submission goes to coordinator review; not self-accepted. All owned files are committed on `agent/ontology-modal-density-search`; no push, no merge.
