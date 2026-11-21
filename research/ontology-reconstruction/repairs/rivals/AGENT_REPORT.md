# AGENT_REPORT.md — ontology-rivals-repair

29 October 2026. Worker report and authorized runner handback for the
task `ontology-rivals-repair` (branch
`agent/ontology-rivals-repair`, worktree
`/Users/andrew/eternalism/.worktrees/ontology-rivals-repair`).
This is a submission for independent review; it is not an accepted
result and selects no temporal ontology.

## Done and files

Repaired the grounding and translation test for the four temporal-rival
contracts in response to
[`research/ontology-reconstruction/coordinator/BATCH1_INITIAL_REVIEW.md`](../../coordinator/BATCH1_INITIAL_REVIEW.md)
§3, per
[`BATCH2_RUN_PLAN.md`](../../coordinator/BATCH2_RUN_PLAN.md).
Predecessor submission read at its exact commit
(`1fb23fdf6fb85de05b627b04b7bb648dd394c140` in the
`ontology-rival-contracts` worktree) and preserved untouched.

Files (all committed, no `git add -A`):

- `research/ontology-reconstruction/repairs/rivals/RESULT.md` —
  self-contained repaired result: translation-layer analysis
  (Proposition T), bounded collapse criterion V, four-notion Bell
  separation, E/F grounding comparison with restatement finding,
  retained four contracts, gates table.
- `research/ontology-reconstruction/repairs/rivals/REPAIR_LOG.md` —
  point-by-point response to the coordinator findings and brief
  obligations.
- `research/ontology-reconstruction/repairs/rivals/sources.jsonl` —
  24 records, schema-checked (unique IDs, required fields, valid
  depths).
- `research/ontology-reconstruction/repairs/rivals/checks/grounding_translation_check.py`
  — bounded witness-check program (standard library).
- `AGENT_REPORT.md` (this file) — runner handback.

## Search capability check (brief-mandated)

- `scholar_search` (OpenAlex): **worked**. Used for metadata discovery
  (Storz 2023 Nature record; Chalmers 2011; deRosset 2015).
- `exa` search + fetch: **worked**. Primary fetches succeeded: Putnam
  1967 JSTOR-scan PDF (full text); Bell 1987 "How to teach special
  relativity" PDF (pp. 77–78 verified); Broad 1923 archive.org djvu.txt
  (pp. 66–68 verified); Correia–Rosenkranz *Replies to Critics* at
  Sciendo (open access, §8 pp. 482–485 verified verbatim); Fine 2005
  NYU accessible PDF (n. 36 verified); arXiv abs pages (Tumulka
  quant-ph/0406094; Hensen 1508.05949; Brown–Timpson 1501.03521);
  nobelprize.org 2022 press release.
- `web-search-prime`: **not retried**, per brief.
- `serpapi`: not needed.
- One fetch failure recorded: De Gruyter returned HTTP 405 for the
  *Replies*; the Sciendo open-access copy of the same DOI was used.

## Source coverage

24 register records. Full-text verified first-hand this run: Putnam
1967; Bell 1987 (key passage); Broad 1923 (key passages, OCR);
C&R Replies §8; Fine 2005 (n. 36 + §11 region). Abstract-level
verified: Nobel 2022; Storz 2023; Hensen 2015; Tumulka 2006;
Brown–Timpson 2016; Chalmers 2011; deRosset 2015. Metadata/discovery:
Jarrett 1984; Shimony reprint (locators verified via the Brown–Timpson
reference list). Inherited gates (not re-read, recorded per item):
Stein 1968 (unread project-wide), Stein 1991 (foundations-lane
record), Clifton–Hogarth 1995 maxim p. 364 (paywalled), C&R NTC
chs. 7/9 (chapter-lane user PDFs), Earman 2008 §§5–7 (lane record;
PDF absent), Ellis 2006 body, C&R appendices, Sider/Mellor record
depth. Full item-by-item table: `.../repairs/rivals/RESULT.md` §9.

## Verification commands and results

```sh
time python3 research/ontology-reconstruction/repairs/rivals/checks/grounding_translation_check.py
```

Output: all five check groups PASS — (1) witness suborder of 1+1
Minkowski (J⁻(b)={a,b}, I⁻(b)={a}, s isolated); (2) translation pair
σ/τ truth-preserving and mutually inverse over 3,715 bounded
sentences; (3) 252 propositional axiom instances mapped to tautologies
(P-transform) plus semantic MP; (4) grounding layers consistent per
flag combination — collision exactly under (Premise D, full
basicness), none under L0-restricted basicness or ¬D; (5) post-Bell
distinctness witnesses across three fragment-repair options. Runtime
0.087 s (cap 10 s; total computation this task ≈ 0.1 s; no dense
searches run).

Register validation:

```sh
python3 -c "import json;[json.loads(l) for l in open('research/ontology-reconstruction/repairs/rivals/sources.jsonl')]"
# OK 24 records, unique IDs, schema fields present
```

First-hand quote verifications this run (locators recorded in
`sources.jsonl`): Putnam p. 241 Principle III and p. 246
coextension/Lorentz clauses; Bell pp. 77–78 aether/neutrality passage;
Broad pp. 66–68 growth and Becoming passages; Replies pp. 482–485
later-grounding defense and anti-collapse reply; Fine n. 36 Sprigge
clause.

## Strongest contrary evidence

1. **The deflationist can grant everything here and still call the
   residual grounding layer verbal by fiat.** Criterion V proves
   non-verbalness only relative to operationalization V plus the
   substantive premises (D, full basicness); it does not refute the
   deflationist — by design, the repair *locates* the premise instead.
2. **The restatement finding cuts against the predecessor's own
   §7.3**: the repaired analysis shows the translation test cannot
   independently vindicate local fragmentalism; what remains is a
   premise location map. Anyone expecting the repair to strengthen F's
   case should read RESULT §6.3 as the negative result it is.
3. **rGRWf's abstract** (verified) shows a collapse dynamics can be
   Bell-violating and nonlocal *without* a preferred slicing —
   weakening the assumption that event-level spacelike dependence
   automatically supplies the foliation that repair option (F-c)
   needs, and complicating the mapping from dynamics to ontology.
4. **Anticipation risk (unaudited)**: the neighborhood of
   ground-theoretic equivalence and verbal-dispute literature
   (Fine 2012a systems; Chalmers 2011 tests; deRosset) may contain a
   published version of the "faithfulness" point or a superior
   operationalization; those bodies were not audited this run
   (abstract/metadata only), so no novelty claim is made for
   Proposition T or Criterion V.

## Limitations

- Gates retained and itemized (RESULT §9): Stein 1968/1991, C&H 1995,
  C&R NTC chapters, Earman 2008 PDF, Fine print pagination, Ellis 2006
  body, Jarrett/Shimony arguments, rGRWf body. No source was upgraded
  beyond its checked depth.
- Proposition T and Criterion V are proved on a bounded fragment with
  an explicit finite witness; they are not general-language theorems,
  and the checking program verifies only the stated bounded claims.
- The philosophical premises (Premise D, asymmetry/transitivity,
  full vs L0-restricted basicness, the maxim readings (α)/(β),
  operationalization V) are stated as premises; none is defended as
  physics or established as metaphysics.
- The four contracts remain reconstructions for review; clause
  attributions resting on chapter-lane records (C&R chs.) and other
  lane records stay at their recorded depths.
- No proof that physics selects a temporal ontology is offered or
  implied; the bridge-premise inventory (RESULT §10) is explicitly
  undefended at selection grade.

## Proposed next tasks

1. Coordinator/bridges: audit Premise D against the ground-logic
   literature and fix the official location of the dispute
   (grounding-atom layer vs primitive-basis layer).
2. Equivalence lane: test Criterion V's faithfulness clause on the
   G-vs-E pair (leaf-indexical structure) — where exposure and V can
   diverge.
3. Source acquisition via library/ILL: Stein 1968; Clifton–Hogarth
   1995; C&R appendices 2–3; Earman 2008 PDF; Jarrett 1984.
4. Scoped physical scout: which sanctioned dynamics combine
   event-level spacelike dependence with a preferred foliation
   (the (F-c) trigger); scope note only.
5. Coordinator integration: carry the STRONGEST_VIEW §8 item 1 / O6
   "collapses into eternalism" phrasing correction (RESULT §5.3/§5.5)
   into the project record at review.

## Handback

Note for the runner: the committed root `AGENT_REPORT.md` at this
branch's HEAD was a stale handback from the earlier `stein-gluing-audit`
lane (25 October); its canonical deliverable
`research/stein-gr/tasks/gluing-audit/PROOF_AUDIT.md` is intact in this
worktree and the old root text remains in branch history for archiving
before integration, per the batch-1 review instruction.

Work complete within the brief's scope; owned outputs staged for
commit; the predecessor worktree and its commit are untouched; no
coordination files, board, runner, shared seeds, or other lanes were
modified; no subagents were launched; nothing was pushed, merged, or
deployed. This report is the authorized runner handback; the
submission now passes to coordinator review.
