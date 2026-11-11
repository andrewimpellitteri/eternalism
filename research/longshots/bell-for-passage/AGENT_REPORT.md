# AGENT_REPORT — longshot-bell-for-passage

Date: 2026-11-10. Worker submission for independent review; not accepted completion.
Claim status: **negative result** — the longshot idea (an inequality for objective passage as
such) fails on current sources; one conjunction (Horvat's PL ∧ IH plus settings independence)
is excluded, and B&I's Markovian datum is falsifiable only jointly with a detachable locality
premise.

## Done / files

All inside `research/longshots/bell-for-passage/` (the allowed output path):

- `RESULT.md` — one-page-plus claim contract in the six-part form of
  knowledge/NOVELTY.md: statement (T) of the excluded conjunction and the three-part escape
  argument; three predecessors compared at assumption/result level; what changes; smallest
  reproducible example; kill conditions; novelty separation. States the negative verdict
  plainly.
- `sources.jsonl` — 21 records, `bfp-` prefixed, knowledge/README.md contract; passes
  `scripts/check_sources.py` (0 errors).
- `toy_check.py` — smallest reproducible example, pure stdlib, all checks pass.
- `AGENT_REPORT.md` — this file.

No other files touched; no workboard, runner, AGENTS.md, or shared seed edits; no subagents
launched; nothing pushed or merged.

## Search capability check (required at start)

- `web-search-prime`: **failed** — MCP error 429, "Weekly/Monthly Limit Exhausted. Your limit
  will reset at 2026-11-17 10:00:29".
- `serpapi_search`: **failed** — "Your account has run out of searches."
- `scholar_search` (OpenAlex/arXiv/Crossref): **worked**; used throughout (found
  Horvat 2610.41944v1 on the arXiv index in the first test).
- `exa` (`web_search_exa`, `web_fetch_exa`): **worked**; used to read arXiv HTML full texts and
  abstracts, and for two semantic searches (experimental tests of temporal ontology; inequalities
  tied to passage).

So the report's coverage rests on scholar_search + exa + the project's existing records.

## What the task asked and what was found

1. **Horvat at source.** arXiv:2610.41944v1 (2026-10-30) read at full-text depth (native arXiv
   HTML, through §IX; final tail truncated by the fetch cap and marked unread in the record).
   It proves exactly: Prop. 1 deterministic Locality ⇒ Determinism; Prop. 2 Bell's Local
   Causality (LC) and Probabilistic Locality (PL) are logically independent (toy examples both
   directions); Prop. 3 PL ∧ Irrelevance-of-History (IH) ⇒ LC, by Eqs. (13)–(17). Premises:
   probabilistic world-theories on a globally hyperbolic foliated Lorentzian background,
   probabilities conditioned on complete events at an initial surface, and footnote 9's placing
   of the spacelike event on one slice. He concludes: keep PL, history is relevant. He never
   mentions temporal ontology, presentism, or Builes–Impagnatiello.
2. **No-go survey.** Covered Bell's local causality (project records, inherited depths),
   Leggett–Garg and temporal Bell inequalities (LG 1985 metadata verified via Crossref; Emary
   review; Clemente–Kofler: LG inequalities are not necessary-and-sufficient for macrorealism;
   Allen–Maroney–Gogioso stronger no-go), Conway–Kochen plus both published comments (Tumulka
   2007; Bassi–Ghirardi 2007: relativistic GRW not excluded), Gisin on real-number
   indeterminism and open time (Erkenntnis 2019; Synthese 2021, abstracts), Maudlin/Myrvold on
   relativistic collapse (project records; Myrvold 2017 PRA as the closest conjunction-shaped
   physics no-go), and explicit tests of presentism/growing block (closest found: Builes,
   "Look at the time!", forthcoming Analysis — observational-credence route, not physics; no
   physics-venue experimental proposal found).
3. **Weakest premises / impossibility.** Delivered as statement (T): becoming + Markovian
   Chance (IH) + Horvat's PL + settings independence ⇒ Bell LC ⇒ excluded; but becoming entails
   neither IH nor PL, each conjunct is independently detachable (foliation dynamics /
   history-relevant chances / superdeterminism), and ontologies of becoming are empirically
   equivalent by construction (DGTZ 2014 undetectable foliation — quote verified in HTML this
   date; Tumulka's Lorentz-invariant GRWf). Hence no inequality for passage as such; a no-go for
   a conjunction is not a no-go for a conjunct. This resolves audit point 6 for the conjectured
   Horvat transfer in the markovian-presentism lane (scoped, not endorsed as published).
4. **Project standard respected.** RESULT.md preserves empirical equivalence where it holds and
   keeps the conjunction/conjunct distinction explicit throughout.

## Verification commands and results

- `python3 research/longshots/bell-for-passage/toy_check.py` → `ALL CHECKS PASSED`
  (CHSH = 4 for PR statistics; slice marginals equal across present states while joint chances
  differ; history-averaged tables exactly equal the PR observables; settings-independent
  history prior).
- `python3 -c` JSONL validation → 21 records, all required fields present.
- `python3 scripts/check_sources.py` → "23 files, 360 records: 0 errors, 2 warnings" (the two
  warnings are pre-existing, in `knowledge/pw-critiques/sources.jsonl`, not this lane).
- Horvat HTML fetch cross-checked against the arXiv abstract page (author, version, date).

## Strongest contrary evidence

- Horvat's paper itself is the strongest potential "already known": his Prop. 3 + his §VII–VIII
  discussion already contain the conjunction moral and the history-relevance escape. RESULT.md
  flags this as an accepted residual-triviality risk; what is added is the verified transfer to
  temporal ontology, the escape taxonomy mapped onto passage theories, and the toy.
- Myrvold 2017 PRA shows Lorentz-invariant Markovian collapse needs nonstandard DOF — if one
  reads "nonstandard DOF" as the preferred present, part of the escape space narrows; but the
  conjunct survives by construction, which is (T)'s point.
- The unverified Zenodo lead (Nero 2026, "Temporal Bell Inequalities and Global Consistency in
  Modal Triplet Theory") is the strongest possible prior-art threat; unreachable this date.

## Limitations

- Both quota-limited search tools were down; scholar_search + exa only. Coverage is
  discovery-level for Conway–Kochen (abstract not fetched directly; characterised via the two
  comments and Scholarpedia) and for Weinert 2013 / Ellis–Goswami 2012 (abstracts, not recorded
  in sources.jsonl to keep the file short).
- The Horvat tail after §IX is unread (fetch cap); his Prop. 3 derivation steps were read line
  by line, but no proof was formalised or reproduced.
- Inherited depths (Builes–Impagnatiello, Wharton–Argaman, Tumulka 2006, DGTZ 2014, Myrvold
  2017, Maudlin, Bell collection, Moreva) were not upgraded; my own DGTZ-2014 read is the
  introduction excerpt only.
- The citation sweep for "already known" relies on the coordinator lane's six-citer sweep of
  B&I plus today's searches; it is not exhaustive. Horvat is too recent for indexed citers.
- Same-model review only; no outside reader (project-wide standing limit).

## Proposed next tasks

1. Resolve the Nero 2026 Zenodo lead (exact DOI/metadata, then abstract) — it gates the
   novelty section of RESULT.md.
2. Fetch Myrvold 2002 (PeacefulCoexistence.pdf) and the FWT primary at full-text depth; both
   are named in the brief and currently sit at discovery depth.
3. If any reviewer wants the conjunction result sharpened: formalise Horvat's Prop. 3
   assumptions in a finite counterexample checker, or a Lean encoding of the world-theory
   definitions, after auditing correspondence (AGENTS.md standard).
4. Forward-citation check on Horvat in ~2 months (once indexed) for applications of his Prop. 3
   to temporal ontology, which would demote RESULT.md's contribution to a citation.
