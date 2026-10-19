# Coordinator review notes

Status: 2026-10-19. Metadata-level review only. It checks record structure and
identifier correspondence, not scientific claims. Lanes are not accepted by this note.

## kb-foundations, kb-formalization, kb-frontier (in review)

Checked programmatically (34 records across three lanes):
- Every record has the required contract fields (`id`, `title`, `url`,
  `checked_on`, `read_depth`, `kind`, `relevance`, `limits`); all `read_depth`
  values are in the allowed set; IDs are unique across lanes.
- All 19 arXiv URLs resolve through the arXiv API, and the recorded titles match.
- `full-text` records carry the extra fields (authors, version, locator,
  assumptions, conclusion, proof status, dependencies, related IDs, open questions).
  Lanes name the locator field differently (`locator`, `section_locator`); a
  downstream consumer must accept both.

Not checked: that any assumption, conclusion, or theorem locator matches its
source. Full-text records need spot-checks against the source before acceptance.

Discrepancies and gaps:
- `frontier/candidates.md` says "15 records"; `sources.jsonl` has 16.
- Formalization: Physlib and AxQM are not pinned to commits and nothing was
  built, so no reuse claim is supported yet.
- Foundations: Malament's primary paper and Stein 1968 were not read. Putnam was
  read only partially (pp. 240-242).
- Frontier: abstract-level only. No candidate has passed the novelty gate.
- Coverage is far under the 60-100 screened / 12-20 deep-anchor targets. The
  `theory-map` gate should treat these lanes as seed material, not a review.

## Spot-check: kb-foundations full-text records (2026-10-19)

Verified against Crossref:
- `found-stein-1991`: **DOI wrong.** Recorded 10.1086/289737; Crossref gives
  10.1086/289609 for Stein, Phil. Sci. 58(2), 147-167. Journal, volume, pages
  and year are correct.
- `found-maxwell-1993`: **pages wrong.** Recorded pp. 327-344; Crossref gives
  pp. 341-348 (Phil. Sci. 60(2), a "Discussion" piece, DOI 10.1086/289737, which
  is correct). The recorded locator "p.343" falls inside the true range, but the
  wrong page range casts doubt on how the text was accessed.

Not verifiable by the coordinator: the cited URLs (paperzz.com, philpapers.org)
return Cloudflare challenges or 403 to curl and WebFetch, so the p.159 (Stein)
and p.343 (Maxwell) claims and the `full-text` read depth could not be
independently confirmed. Until re-checked from an accessible copy, treat
`read_depth` for these two records as unconfirmed and the argument-map content
that rests on them as unaudited. Putnam (already marked partial) was not rechecked.

Recommendation: do not accept `kb-foundations` until the two bibliographic
fields are corrected and the page-level claims are confirmed from a copy a
reviewer can open.

## kb-agent-methods interim review (2026-10-19, worker still running)

Reviewed `prior-methods.md`, `handoff-contract.md`, `pilot-design.md` in the
worker's worktree. Not yet accepted; the worker has not submitted AGENT_REPORT.md.

Verified: 9 arXiv IDs resolve to recorded titles; TNLean license (Apache-2.0),
commit count (14,363), `docs/paper-gaps/` and the Douglas repo exist; AxQM
(1,019 tasks) and TNLean ("enforcing mathematical intent") abstract claims match.
Unverified (need full text): the ~$20k API cost, 278 oracle checks, "62 numerical
checks passed, 3 gaps found", six human review rounds, Hell-Thiele failure list.
"$20k" is the TNLean authors' reported cost, but is worded as if it were a
project cost; reword and mark unverified.

Handoff contract and audit procedure: sound and consistent with AGENTS.md
(bridge-premise rule, no self-acceptance, capped loops, knowledge asymmetry for
the counterexample role). No blocking problems found.

Pilot design defects to fix before the pilot is built:
1. Family A alone is called the minimum viable pilot, but D2 (missing assumption)
   exists only in Family B, while the pass criteria require D2 and recall >= 6/8.
   Family A has 7 classes, so it cannot pass as written.
2. Contamination is unlisted. Einstein 1905 and the Lorentz transformation are in
   every model's training data, so "known answers" may test recall, not
   extraction fidelity. Needs a less memorized source or an explicit limitation.
3. D3 is mislabeled F1. It states a claim for all frames while deriving it for
   one family, so the statement is stronger than its derivation. F1 in the
   taxonomy is a formal statement weaker than the source.
4. B2 predicts a symbolic check would pass D5. A first-order expansion presented
   as exact is algebraically false against the exact formula, so it would likely
   be caught. State it as a hypothesis, not a premise.
5. One instance per class run three times gives repeated measurements of one
   artifact, not three independent samples. The 2/3-runs criterion measures model
   stability on that artifact, not class recall. Add several instances per class.
6. Call budget (60-80) is below the stated design (about 20 artifacts x 3 runs x
   audit, counterexample and baselines, roughly 300).
7. Injector, translator and auditor are the same model family; the limitation is
   noted but the pilot should also pre-register what a cross-model run would add.

### kb-agent-methods submission check (2026-10-19)

Worker committed `d6f17ca` and wrote AGENT_REPORT.md, then `opencode` exited 1, so
the runner recorded `failed`. Work is complete; moved to `review` by hand, not accepted.

Figures now verified against arXiv HTML: TNLean $20,206 recorded API cost for the
whole library (about $5,548 for the FT-MPS theorem), six blueprint review rounds,
five-iteration review-repair cap, DS-gauge weakening and asymptotic-for-finite
substitution (2607.07857); 278 oracle checks, 62 passing checks then three
statement-level gaps, two oracle errors (2607.06379). The reworded "$20k" line
should still say it is the TNLean authors' figure.

Remaining: report says 2 full-text records but sources.jsonl has 3 (CAS, tensor,
Seiberg-Witten); prior-methods.md header counts are inconsistent. The seven pilot
design defects above are still open.

## Repo-wide DOI check (2026-10-19)

All 18 DOIs in every `sources.jsonl` were matched to Crossref titles. Four
foundations records failed; three were corrected in `23241bb`:
- `found-stein-1968`: 10.2307/2023910 returned 404; correct DOI 10.2307/2024512.
- `found-malament-1977`: 10.1111/j.1933-1592.1977.tb01280.x returned 404; correct 10.2307/2214766.
- `found-deasy-2015`: DOI resolved to an unrelated paper; the matching Deasy paper is
  Phil. Studies 172 (2014) 2073-2089, 10.1007/s11098-014-0398-5.
- `found-prior-2009`: left in place but flagged unverified; the DOI points elsewhere
  and Crossref has no Hawley paper by that title.
Together with the earlier Stein 1991 / Maxwell 1993 fixes, six of the 13 original
foundations records carried a wrong DOI, venue or pages. Treat worker-supplied
bibliographic fields as untrusted until checked: run the arXiv-title and Crossref-title
checks on every new lane before acceptance. The arXiv check covers only arXiv URLs;
books and JSTOR items without DOIs remain unchecked.

## theory-map early check (2026-10-19, worker still running)

First file: `research/theory-map/sources.jsonl`, 62 records (59 re-copied lane
records plus 3 new `map-*`), all parse, no duplicate IDs, required fields present,
no read depths raised. The worker branched before commit 23241bb, so its copies of
`found-stein-1968`, `found-malament-1977` and `found-deasy-2015` carry the old
wrong DOIs, and `found-prior-2009` still lacks the unverified flag.

Acceptance rule for this and every lane that re-copies records: the canonical
version of a lane record is the one in `knowledge/<lane>/sources.jsonl` on `main`.
Take the worker's version only for new IDs, and compare identifiers for the 3
`map-*` records (all abstract depth) with arXiv and Crossref before merging.

## Audit of knowledge/philosophy/sources.jsonl (Codex session's register), 2026-10-19

Independent Claude-subagent audit of all 36 records (Crossref for DOIs; arXiv abstract
pages for arXiv items, since the arXiv API was rate-limited; catalog, Open Library, SEP
and Gutenberg pages for books). Result: no WRONG identifier, author, title, year or
venue; no fabricated citation; no record claims more than abstract depth. This contrasts
with the foundations lane (6 of 13 records wrong). OUP, Springer, JSTOR, MIT Press and
the PhilPapers survey site were bot-blocked, so book records were confirmed through
Crossref chapter records and DOIs rather than publisher pages. Not mine to edit; items
for the owning session:

- `phil-survey`: the quoted PhilPapers 2020 figures (39.92% eternalism, 18.39%
  presentism, 17.03% growing block, 734 answers) could not be verified. Check against the
  survey results page before keeping them in PHILOSOPHY_OF_TIME.md section 1.
- `phil-kant`: the limits field says A30-32/B46-49 were checked, but the Gutenberg
  text (4280) has no A/B pagination. The pinpoint claim is unsupported by that edition.
- `phil-fine`: title should be "Modality and Tense: Philosophical Papers"; the added
  "especially Tense and Reality" is not part of the published title.
- `phil-mellor`: the Routledge URL slug is a placeholder; use the canonical page.
- `phil-lewis`: only reprints found by Crossref; the 1976 Am. Philos. Q. venue and pages
  are not recorded and the JSTOR id was not confirmed. `phil-shoemaker`: the JSTOR link
  was not fetched; the DOI 10.2307/2023892 is assumed to be the same item.
- `phil-dainton`: 2000 first edition not confirmed by catalog (the record flags this).
- PHILOSOPHY_OF_TIME.md cites some works by name with no register id (Rietdijk, the
  hole argument, Bell-type constraints, section 16 sketches). Section 16 labels its
  sketches unaudited. Ten attributed claims were spot-checked against abstracts and
  none was misattributed; Fine, Braddon-Mitchell, Prior, Perry and Maudlin claims were
  not checked.

## kb-ico-qrf and theory-map acceptance (2026-10-19)

Both lanes finished ("Task complete") and exited 1, so the runner marked them `failed`;
the board was corrected by hand with `review` then `accept`. Reports were moved into
each lane's owned directory (the accept scope check allows only `owns` paths).

theory-map: IDs resolve, scope ok, stale copies of four foundations records replaced by
the corrected canonical versions, all 19 connections status-tagged, five contracts.
See `knowledge/defeat-search/contracts-crosswalk.md` for missing closest predecessors.

kb-ico-qrf: 18 records. All five DOI records and the Quantum 9, 1616 (2025) and Nat.
Commun. 3, 1092 (2012) citations match Crossref. Four claims on arXiv 2603.08845 (frame-
change map preserves probabilities, Eq. 25 constraint, footnote 3 on the thermodynamic
arrow, the Discussion statement that clocks "do not disagree that the order of operations
is indefinite") were checked against the paper's HTML and match. The worker's "frame-
invariant" phrasing is its own gloss and is labeled as such. The lane re-records three
frontier IDs (2211.15685, 2603.08845, 2607.03417) at full-text depth where the frontier
lane has discovery or abstract; the deeper ico-qrf record supersedes them. The anchor E
numbers (separable bound 3/4, quantum value (2+sqrt2)/4) are correct.

Runner note: after a relaunch, `result.json` from the first attempt persists and makes a
live worker display as `failed`; check the process, not the status column.

## Read-only identifier check of the Codex lanes in review (2026-10-19)

kb-aqft-locality (9 records), kb-arrow-cosmology (10), kb-discriminators (11): all 30
records parse; 29 of 30 DOI-bearing records match Crossref titles (arXiv items not
re-checked, the arXiv API being rate-limited). One failure, in the lane's own words
already flagged as unverified:
- `aqft-bisognano-wichmann-1976`: DOI 10.1063/1.522676 resolves to an unrelated paper,
  and the title "On the duality condition for a Hermitian scalar field. II" is wrong. The
  1976 paper is "On the duality condition for quantum fields", J. Math. Phys. 17, 303-321,
  DOI 10.1063/1.522898 (the 1975 paper "...for a Hermitian scalar field" is 10.1063/1.522605,
  J. Math. Phys. 16, 985-1007). Left unedited: it belongs to the Codex session's lane.
Substance of these lanes (full-text claims) not reviewed here.

## kb-time-interpretations acceptance (2026-10-19)

29 records, no wrong DOIs (12 matched to Crossref), arXiv IDs and titles match; the
lane's `time-zampeli-2026` label is the journal-publication year of a 2022 preprint
(arXiv 2205.15893). Checked by hand: the ABL probability rule is stated correctly, and the
Hartle "Physics of Now" quote ("Past, present, and future are not properties of four-
dimensional spacetime but notions describing how individual IGUSes process information")
appears verbatim in the arXiv abstract. The lane keeps determinism, passage, causal order,
clock time and the memory arrow separate and flags "future is fixed" as ambiguous between
boundary condition, deterministic dynamics and block reality. The eight full-text anchors
were not individually re-read by the coordinator; the 1964 ABL original was not obtained
(APS 403), which the lane records.

## kb-preferred-foliation acceptance (2026-10-19)

31 records (2 full-text, 12 abstract, 17 discovery). All 17 DOI records match Crossref;
all 12 arXiv records match their abstract-page titles, including a days-old October 2026
preprint (2610.10980). The report states search tooling status honestly (unavailable at
start, restored mid-run, used for three rounds). The map keeps preferred frame, passage,
determinism, causal order, clock time and the arrow separate, labels each claim as
established, advocate claim or our note, and presents the neo-Lorentzian response to
Rietdijk-Putnam as denial of a bridge premise, not a refutation. Two full-text anchors and
the discovery-depth items were not re-read by the coordinator.
