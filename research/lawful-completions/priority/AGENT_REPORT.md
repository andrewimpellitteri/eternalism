# AGENT_REPORT — lawful-completions-priority

28 October 2026. Worker submission for review (not accepted completion).
Worktree: /Users/andrew/eternalism/.worktrees/lawful-completions-priority,
branch agent/lawful-completions-priority.

## Task

Kill-test priority and scope of past-preserving Einstein completions: audit
primary Manchak 2008 (prediction / genuine prediction), observational
indistinguishability variants, fixed-matter / topology / nonisometric-future
constructions; find the strongest established result answering CONTRACT items
A and B; check cut-paste vs fixed Einstein–matter evolution and maximal GH
status; check prior theorem coverage for the spherical Vaidya/null-dust
baseline; deliver three closest predecessors at assumption level, minimal
candidate delta, and KILL/PASS/CONDITIONAL with falsifier.

## Done / files

- `research/lawful-completions/priority/RESULT.md` — main deliverable: primary
  audit with exact locators and read depths; A verdict **KILL** (Manchak 2008
  pp. 319–321 + Manchak 2009 p. 55, with any local field laws); B verdict
  **CONDITIONAL** (B-i blocked by CBG 1969; B-ii occupied by Taub–NUT / Gowdy /
  Bianchi IX / Costa et al. 2015 non-isometric extensions of shared MGHDs;
  surviving B-iii delta specified); cut-paste trap audit; Vaidya coverage check;
  candidate obstruction L1 and candidate lemma L2, each with falsifiers;
  access-gate register.
- `research/lawful-completions/priority/sources.jsonl` — 26 source records with
  required fields (id, title, url, checked_on, read_depth, kind, relevance,
  limits) plus version/DOI, locators, assumptions, conclusions, proof status,
  related IDs where full-text.
- `AGENT_REPORT.md` (root) — handback report (replaces prior lane's root file
  per handback convention).

## Search capability check (brief requirement)

- Z.ai MCP `web-search-prime` (`web_search_prime`): **FAILED** — MCP error -429,
  code 1310, "Weekly/Monthly Limit Exhausted", reset 2026-11-17 10:00:29.
- Fallback `serpapi_search`: **worked** (used for lead discovery).
- `webfetch`/`curl`: worked. Local PDF extraction: Swift + macOS PDFKit script
  (`/private/tmp/opencode/lcp/extract.swift`), same method as the horizons lane.

## Source coverage

Full-text read this run: Manchak 2008 (4 pp.), Manchak 2009 (8 pp.), Manchak
2016 (12 pp.), Geroch 1977 pp. 81–92 (noisy scan; 7-page LSE file), Doboszewski
2017 ch. 11 (20 pp.), Linford 2026 arXiv:2603.04159v3 (HTML, §§1–6.1), Manchak
2025 popular piece. Partial: Malament 1977 (p. 80 tail only — pp. 61–79 are an
ACCESS GATE), Doboszewski 2019 (abstract + §1), Linford §6.2. Abstract/snippet
or secondary-only: CBG 1969, Chruściel–Isenberg 1993, Costa et al. 2015,
Moncrief 1981, Misner–Taub 1969, Ringström 2009, Krasnikov 2009, Dafermos 2014,
Aboelhassan 2023 (embargoed), Burnett 1996, Sbierski 2021, Cinti–Fano 2021,
Lesourd 2021, Hogarth 1993, HE 1973, Manchak–Barrett 2023/2024. Queries run:
Manchak observational indistinguishability; Malament/Barrett–Manchak
Heraclitus; Timofeev / extendible MGHD / Vaidya; Christodoulou two-sided;
Cinti–Fano critique; plus citation chasing from the read papers' bibliographies
(primary source of the mathematical-GR leads).

## Verification commands and results

- `curl -sL -o … + file …` for each PDF (Manchak2008a.pdf: PDF 4 pages;
  GerochMalament1977.pdf: PDF 1.6, **7 pages** — decisive access fact;
  manchak2009.pdf: 8 pages; manchak2016.pdf; doboszewski2017.pdf: 16 pages;
  doboszewski2019.pdf: 19 pages; manchak2025_he.pdf).
- `qpdf --show-npages GerochMalament1977.pdf` → 7 (proves the Malament gap is in
  the file, not the extractor).
- `swift extract.swift <pdf>` (PDFKit) → text files in /private/tmp/opencode/lcp/
  (kept out of the repo; no large files committed).
- Statements of Manchak 2008 cross-checked against the project's own
  `research/horizons/PRIOR_WORK_CHECK.md` addendum (independent prior read):
  theorem wording at p. 319 and genuine-prediction content match.
- `git status` / `git add` restricted to allowed paths (see below).

## Headline findings

1. **A is established, not open.** Manchak 2008's genuine-prediction theorem and
   its proof construct, for any point p off ∂J⁻(q), an inextendible partner
   containing an isometric copy of the closed past J⁻(q) whose future disagrees,
   and the paper states (p. 321) the construction survives ANY local conditions
   including Einstein's equation, Maxwell, and energy conditions. Lineage:
   Hawking–Ellis 1973 pp. 58–59 → Geroch 1977 pp. 89–90 → Malament 1977 →
   Manchak 2008/2009.
2. **B splits.** B-i (same data, two MGHDs) is impossible (CBG 1969). B-ii
   (shared MGHD + non-isometric inextendible extensions) is established in
   symmetric vacuum/electrovac cases (Taub–NUT; polarized Gowdy with countably
   many extensions; LRS Bianchi IX C²; Costa–Girão–Natário–Silva 2015,
   Einstein–Maxwell–scalar + Λ>0, generic C¹). The surviving B-iii delta
   (smooth, strongly causal, future-only, hole-free, non-vacuum well-posed
   matter, pointed relational observable) coincides with Doboszewski 2017
   §11.3.6's open question plus two strengthenings — a narrow, honest gap.
3. **Cut-paste check:** no audited cut-paste family retains a fixed global
   Einstein–matter evolution and maximal GH status; Geroch 1977 p. 85 already
   states Einstein's equation does not stop hole-cutting, and p. 86 that
   maximality is no substitute for hole-freeness; Linford 2026's IJC-glued dust
   clothesline is the best current cut-paste but leaves the clothesline seams
   unchecked and is not GH.
4. **Vaidya baseline:** extension analysis exists (Israel; Aboelhassan 2023,
   embargoed) but no OI/relational framing and no MGHD-non-uniqueness theorem
   found; existence of a baseline A-pair is near-trivial via a delayed ingoing
   shell outside J⁻(b), but my candidate obstruction L1 says the disagreement is
   always routed through the center-crossing event — so the baseline inherits
   the hard regularity/non-uniqueness machinery rather than trivializing it.
   (L1 is my conjecture-level analysis, with a stated falsifier.)

## Strongest contrary evidence

- Cinti & Fano 2021 (against weak OI; asymmetry objection) — located but NOT
  fully read (both public mirrors failed); must be read at review.
- Doboszewski 2017 §§11.3.4–5: known non-unique-extension pairs are symmetric,
  rare, and CTC-tainted beyond the horizon; compatible with Chruściel-style
  cosmic censorship. Any B-iii claim must argue non-artifactness.
- Linford 2026's own concession that his nemeses are physically unrealistic, and
  his unverified seam claims (IJC applied only to the OS worldtube).

## Limitations

- Malament 1977 pp. 61–79 unread (no public scan); the matter-field construction
  at pp. 74–76 that Manchak 2009 n. 12 relies on is unaudited. Do not quote
  Malament beyond p. 80 in any manuscript yet.
- All mathematical-GR primaries behind B-ii read only via Doboszewski's
  full-text survey (locators recorded in sources.jsonl); her summaries were not
  independently verified against the journals.
- Timofeev-style extendible-MGHD-in-null-dust claims: my searches did not locate
  a primary; may be misremembered in the brief's background. Recorded as an open
  locator task for the constraints lane rather than asserted.
- Christodoulou two-sided constructions: not audited in this lane (only the
  Dafermos 2014 abstract and survey traces).
- Linford 2026 is an unrefereed preprint; his §6.2, §7–8, appendices unread.
- No novelty claim is made anywhere; "not found" is labeled at stated search
  depth only.

## Unresolved questions / proposed next tasks

1. Obtain Malament 1977 pp. 61–80 and Cinti–Fano 2021 full text; audit the
   matter-field construction against the CONTRACT's observer-germ requirement.
2. Full-text read of Chruściel–Isenberg 1993 and Costa et al. 2015 extendibility
   statements; verify the "isometric but not via identity on the shared region"
   claim and strong-causality status of the extensions.
3. Constraints lane: locate primaries for non-unique/extendible MGHDs in null
   dust and scalar systems (Christodoulou two-sided; the Timofeev reference if
   it exists) and test them against L1/L2 falsifiers.
4. If B-iii survives review, write its claim contract against Doboszewski 2017
   §11.3.6 and the RESULT.md falsifier list; otherwise route to C/D.

## Compliance

Stayed in `research/lawful-completions/priority/` + root `AGENT_REPORT.md`; no
board/runner/manuscript/shared-seed edits; no installs; no large runs; no child
agents; commits limited to task-owned outputs plus the required root report.
