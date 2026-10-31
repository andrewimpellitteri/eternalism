# AGENT_REPORT — stein-priority-audit

25 October 2026. Worker submission for coordinator review; not accepted
completion.

## Done and files

Audited priority for the exact repaired claim of `research/stein-gr/main.tex`
(off-shell, category-wide becoming classification under local covariance,
with its satellites), compared it assumption-by-assumption with nearest
predecessors, ran capability-of-defeating searches, and delivered:

- `SEARCH_LOG.md` — capability check, all queries, citation sweeps, coverage
  and residual risks.
- `sources.jsonl` — 19 source records with exact versions, locators, honest
  read depths and limits (contract fields present).
- `VERDICT.md` — the bounded verdict: PURSUE — narrow, nearest-predecessor
  comparison table, falsifiers, and five directly usable manuscript fixes.

No file outside `research/stein-gr/tasks/priority-audit/` was created or
modified. `main.tex`, `DRAFT.md`, reviews, board, runner and shared registers
untouched. The `_sources/` subdirectory holds downloaded primary material
(PDF/HTML/JSON, ~7 MB) and is intentionally left untracked.

## Search capability check (required)

`web-search-prime` (Z.ai MCP) **failed** with HTTP-equivalent -429, code 1310,
"Weekly/Monthly Limit Exhausted … will reset at 2026-11-17 10:00:29", on an
on-topic test query. Fallbacks worked: built-in web search, `webfetch`,
OpenAlex API, arXiv HTML, and `curl` for open PDFs. Two PhilSci PDFs and all
PhilArchive/PhilPapers file downloads and Springer pages were blocked; those
sources are recorded at their honest read depths.

## Source coverage (headline; details in sources.jsonl)

- Full-text: Stein 1991 (21-pp. scan); Viglione 2026 PhilSci preprint (26 pp.);
  WC2017 2015-01-30 draft (= arXiv v1, 15 pp.); BFV 2003 definitions and
  category (arXiv HTML); Wüthrich 2023 CST handbook chapter (grep + sections);
  Manchak 2017 Stein-honor talk (text extraction); Savitt 2011/2020 CDLP
  §2 via search-engine rendering of the PhilSci PDF (verbatim CH Theorem 1
  p.365, Theorem 2 pp.371–372, Lemma p.364).
- Abstract/definition level: CH 1995 (paywalled primary; Savitt rendering
  secondary); Stein 1970a note; Stein 1970b Gödel paper (p.594 verbatim via
  Manchak); Savitt 2005; Aames 2022; Myrvold 2003; Dorato 2002; Müller 2019;
  FV 2012 (abstract + S1/S2 + Loc definition from ar5iv); Zalel 2023;
  Guo-Paycha-Zhang 2023 (screened out).
- Citation sweeps (OpenAlex, full title listings): CH1995 (115), Stein 1991
  (259), WC2017 (66) citing works, screened; shortlisted items read.

## Verification commands and results

- `git rev-parse HEAD` → `0c6d2c59c651c0d97edd9f769c8bb949d5f65c82`
  (branch `agent/stein-priority-audit`).
- `shasum -a 256 research/stein-gr/main.tex` →
  `7ccc1d37b521e4a25af54c28ffc067066243bd190da79125d922037c90345886`.
  Note: differs from the hash in `SECOND_PASS_REVIEW.md`
  (`33f4a667…`), i.e. the manuscript changed after that review; this audit
  pins the current text. I did not modify the manuscript.
- `python3 -c "import json;[json.loads(l) for l in open('sources.jsonl')]"` →
  parses, 18 records (run below before commit).
- Key source-to-manuscript correspondence checks actually performed:
  - BFV's Man morphism conditions (i) causal convexity, (ii) orientation and
    time-orientation preservation — quoted from arXiv HTML — match the
    manuscript's (LC) morphisms (plus explicit openness, standard in the
    later Loc literature).
  - CH Theorem 1 trichotomy and page locators match the manuscript's
    thm:flat citation.
  - WC2017 §3 counterexample relation R and footnote 5 wording match the
    manuscript's quotes.
  - Stein 1991 Theorem wording (p.149) matches the manuscript's
    characterization of Stein's proof as symmetry-only.
  - Stein 1970 "deformation question" resolved to the Phil. Sci. 37 Gödel
    paper p.594 (Manchak's citation "1970, 594"), not the J.Phil. note.

## Strongest contrary evidence found

1. **Fewster–Verch 2012 principle S2 (SPASs)** — "if two locally covariant
   theories are subtheories and isomorphic in one spacetime, they are
   isomorphic in all" — is structurally the same cross-spacetime propagation
   schema as thm:main, with a proven failure/rescue analysis. It concerns
   theory isomorphisms, not event relations, and the manuscript's mechanism
   differs; but it is prior art for the *schema*, and the manuscript does not
   cite or distinguish it. Recorded as the nearest mathematical neighbor
   (VERDICT §2.4, fix 1).
2. **The flat shared-present collapse** (Saunders 2002; Callender 2000;
   Savitt CDLP §2): two distinct co-present events force universality — the
   flat antecedent of cor:nopresent. The corollary's cross-spacetime form is
   immediate from thm:main; its philosophical content is not new. Manuscript
   fix 3.
3. **CH pp. 385–386 remain primary-unverified.** If the closing section
   proposes (rather than laments the absence of) a locality-based extension,
   the manuscript's framing needs revision (though the theorem would stand).
4. Nothing in 440 screened citing works (2015–2026) states a cross-spacetime
   becoming-classification; the 2023 CST handbook chapter explicitly still
   lacks the embedding-based analogue. This is absence-of-evidence from
   substantial, targeted coverage — corroborative, not certifying.

## Limitations

- `web-search-prime` unavailable; public-search fallbacks used throughout.
- Paywalled/inaccessible primaries not read: CH 1995 pages (incl. the
  quoted 385–386 passage), Stein 1968 full text, Stein 1970b full text,
  Savitt 2005/2009/2015, Dieks 2006, Dorato 2002/2011, FV 2012 body,
  published BJPS WC2017. All are recorded with their true read depths.
- Title-level citation screening cannot exclude a mislabeled theorem;
  abstracts were checked only for shortlisted items.
- No mathematics-database (zbMATH/MathSciNet) query was possible; the
  "natural operations on Lorentzian manifolds" thread was searched once
  (negative) and is flagged as residual risk in SEARCH_LOG and VERDICT §4.
- Priority confidence is bounded by the coverage above; per project
  standards, citation counts and keyword absence were not treated as
  evidence of novelty.

## Proposed next tasks

1. `stein-manuscript-fixes` (editor): apply VERDICT §5 — FV S2 comparison,
   Stein 1970b citation, cor:nopresent attribution, prior-work caveat, and
   verify CH pp. 385–386 quotes against the primary (a human with Springer
  /JSTOR access can do this in minutes).
2. One-shot library check (human, institutional access): CH 1995 pp.
   365–367 and 385–386; Stein 1970b pp. 589–601; FV 2012 full text.
3. Optional bounded math search: "natural relations/operators on Loc or on
   categories of spacetimes" in zbMATH/MathSciNet vocabulary, to close
   residual risk 2 in SEARCH_LOG.
4. No change needed to the causet/null-boundary/rigidity lanes' scopes; this
   audit's prop:causets finding (no prior convex-embedding Stein theorem,
   including in the 2023 survey) feeds the `stein-causet-audit` lane's
   "published weaker claim" comparison directly.

## Unresolved questions

- Exact wording and argumentative force of CH 1995 pp. 385–386.
- Whether FV 2012's body contains any relation-valued functor statement
  (body unread).
- Whether the published BJPS WC2017 differs materially from the 2015 draft.
- Whether a preorder-valued natural functor is classified somewhere in the
  natural-operations mathematics literature under different vocabulary.
