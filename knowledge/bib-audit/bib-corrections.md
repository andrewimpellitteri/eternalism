# Bibliographic audit — corrections and verification

Status: worker submission for independent review (task `kb-bib-repair`), 2026-10-19.
Scope: every record in `knowledge/*/sources.jsonl` and `knowledge/seed-sources.jsonl`
that is **not** an arXiv or DOI-verified item (books, JSTOR items, publisher pages,
catalog scans, code repositories, SEP pages), plus resolution of `found-prior-2009`
and a defensive Crossref spot-check of DOI-labeled records.

This file proposes changes only. No lane `sources.jsonl` file was edited.
Machine-readable proposals: `proposed-records.jsonl` (23 records with field-level
changes), `proposed-other-lane-fixes.jsonl` (2 out-of-scope repairs, proposals only).

## Search capability check

| Tool | Result |
| --- | --- |
| OpenCode `websearch` | **FAILED** — two attempts returned `Web search cancelled` (2nd retry confirmed). |
| MCP `web-search-prime.web_search_prime` (via Code Mode) | **WORKS** — first test query `Hawley "The Future of the Universe" growing block Mind` returned 9 results; used for Hawley identification, Penrose chapter pagination, and the PhilPapers-survey existence check. Hit a transient 429 rate limit once; retry after a pause succeeded. |
| `curl` / `webfetch` to public APIs | **WORKS** — Crossref, OpenAlex, Open Library, archive.org, GitHub API, SEP, Project Gutenberg, White Rose eprints, Scholars@Duke, AFP, fourmilab, INSPIRE. |

Session note: the agent harness restarted mid-run and the MCP tool catalog
changed around it (`web-search-prime` removed and re-added, `serpapi_search`
added; not used). All search results cited in this audit were obtained from the
`web-search-prime` tests logged above before the restart; every verification
rests on direct `curl`/`webfetch` responses against primary catalog endpoints,
which are reproduced in section F.

Search method: small targeted queries, citation chasing from authoritative
catalogs; no bulk downloads.

## Reading depth of this audit

Every verification below is **catalog/landing-page metadata level** (`discovery`
depth against catalogs). I did not read paywalled or blocked content, and I do not
re-derive the substantive claims of any source. Existing `read_depth` values in
records were left as the originating lanes claimed them; this audit verifies
bibliographic identity (author, title, venue, year, pages, identifiers), not
argument content.

---

## A. Correction table (records with field changes)

Evidence URL per change. `read_depth` values are unchanged except where noted.

### A.1 Broken or wrong identifiers (highest priority)

| Record id | Field | Old value | New value | Evidence URL |
| --- | --- | --- | --- | --- |
| `found-reichenbach` | url | `https://archive.org/details/directionoftime00reic` (item nonexistent; metadata API returns `{}`) | `https://archive.org/details/directionoftime0000reic` | https://archive.org/metadata/directionoftime0000reic |
| `found-reichenbach` | year | (absent) | `1956` (original; scan is 1971 UC Press printing, ISBN 9780520018396) | https://openlibrary.org/search.json?q=title%3A%22direction+of+time%22+author%3Areichenbach |
| `found-prior-2009` | whole record | "The Future of the Universe", Hawley, DOI 10.1093/mind/fzp077 | **CANNOT IDENTIFY — quarantine, do not cite** (see section C) | https://api.crossref.org/works/10.1093/mind/fzp077 |
| `aqft-bisognano-wichmann-1976` *(other lane — proposal only)* | url | `https://doi.org/10.1063/1.522676` (= Wong & Yeh, "Eigenvalues of the invariant operators of the orthogonal and unitary groups", JMP 16(6):1239–1243, 1975) | `https://doi.org/10.1063/1.522898` | https://api.crossref.org/works/10.1063/1.522898 |
| `aqft-bisognano-wichmann-1976` *(other lane)* | title | "On the duality condition for a Hermitian scalar field. II" | "On the duality condition for quantum fields" | https://api.crossref.org/works/10.1063/1.522898 |
| `aqft-bisognano-wichmann-1976` *(other lane)* | version | "J. Math. Phys. 17 (1976), 303-321; DOI locator not independently verified" | "J. Math. Phys. 17(3), 303-321 (1976); DOI 10.1063/1.522898" | https://api.crossref.org/works/10.1063/1.522898 |

### A.2 Titles to exact catalog form

| Record id | Field | Old value | New value | Evidence URL |
| --- | --- | --- | --- | --- |
| `found-maxwell-1993` | title | On Relativity Theory and Openness of the Future | Discussion: On Relativity Theory and Openness of the Future | https://api.crossref.org/works/10.1086/289737 |
| `found-deasy-2015` *(other lane — proposal only)* | title | The Moving Spotlight Theory of Time | The moving spotlight theory | https://api.crossref.org/works/10.1007/s11098-014-0398-5 |
| `phil-fine` | title | Modality and Tense: Philosophical Papers, especially Tense and Reality | Modality and Tense: Philosophical Papers ("Tense and Reality" is a paper within the collection, not part of the title) | https://openlibrary.org/search.json?title=Modality+and+Tense&author=Fine (ISBN 9780199278701) |

### A.3 URLs replaced with canonical identifiers

| Record id | Field | Old value | New value | Evidence URL |
| --- | --- | --- | --- | --- |
| `found-stein-1991` | url | `https://paperzz.com/doc/7354841/...` (third-party PDF aggregator) | `https://doi.org/10.1086/289609` | https://api.crossref.org/works/10.1086/289609 |
| `form-physlib-povm-code` | url | `.../blob/master/QuantumInfo/Measurements/POVM.lean` (mutable) | `.../blob/5bbbb30d08b8e151406a10affbc8a369b74b32c6/QuantumInfo/Measurements/POVM.lean` | https://api.github.com/repos/leanprover-community/physlib/commits?per_page=1 |
| `form-physlib-minkowski-code` | url | `.../blob/master/Physlib/Relativity/MinkowskiMatrix.lean` (mutable) | `.../blob/5bbbb30d08b8e151406a10affbc8a369b74b32c6/Physlib/Relativity/MinkowskiMatrix.lean` | https://api.github.com/repos/leanprover-community/physlib/commits?per_page=1 |

Caveat recorded on both pinned-file records: the pin (master HEAD, 2026-10-19T20:14Z)
is taken **after** the original read earlier that day; line locators must be re-diffed
before reuse.

### A.4 Missing bibliographic fields added

| Record id | Field | Old value | New value | Evidence URL |
| --- | --- | --- | --- | --- |
| `found-putnam` | version | (no DOI) | adds "JSTOR DOI 10.2307/2024493" (J. Phil. 64(8):240–247, 1967 confirmed) | https://api.crossref.org/works/10.2307/2024493 |
| `phil-shoemaker` | version | (absent) | "J. Phil. 66(12), 1969, pp.363–381; DOI 10.2307/2023892" | https://api.crossref.org/works/10.2307/2023892 + https://plato.stanford.edu/entries/time/ (bibliography) |
| `phil-lewis` | version | (absent) | "American Philosophical Quarterly 13, 1976, pp.145–152 (issue number not independently confirmed)" | https://plato.stanford.edu/entries/time-travel/ (bibliography: "Lewis, David, 1976, 'The paradoxes of time travel', American Philosophical Quarterly, 13: 145–52") |
| `found-sarkar-stachel-1999` | version | (no DOI) | adds "DOI 10.1086/392684" (PoS 66(2):208–220, 1999 confirmed) | https://api.crossref.org/works/10.1086/392684 |
| `found-sep-malament` | authors | (absent) | Allen I. Janis | https://plato.stanford.edu/archives/win2001/entries/spacetime-convensimul/ (footer: Copyright 1998, 1999, Allen I. Janis) |
| `found-broad-1923` | year | (absent) | 1923 (original; archive.org scan `scientificthough00broa` is the 1959 Littlefield, Adams reprint) | https://archive.org/metadata/scientificthough00broa + https://openlibrary.org/search.json?title=Scientific+Thought&author=Broad |
| `seed-brading-presentism` | year | (absent) | 2013 (Philosophy of Science 80(5):1101–1111, December 2013) | https://scholars.duke.edu/publication/1377437 + https://api.crossref.org/works/10.1086/673897 |
| `seed-brading-presentism` | version | (absent) | "Philosophy of Science 80(5), December 2013, pp.1101–1111; DOI 10.1086/673897; author Katherine A. Brading (Duke)" | https://scholars.duke.edu/publication/1377437 |
| `seed-isabelle-relativity` | version | (absent) | "In: Durand-Lose & Nagy (eds.), MCU 2015, Springer LNCS (ISSN 0302-9743)" | https://eprints.whiterose.ac.uk/id/eprint/86607/ |
| `form-afp-schutz-outline` | authors | (absent) | Richard Schmoetten; Jake Palmer; Jacques D. Fleuriot | https://www.isa-afp.org/entries/Schutz_Spacetime.html |
| `form-afp-schutz-outline` | title | "AFP Schutz_Spacetime current generated proof outline" | "Schutz' Independent Axioms for Minkowski Spacetime (AFP entry), current generated proof outline" | https://www.isa-afp.org/entries/Schutz_Spacetime.html |

### A.5 Version pins and notes added (code repositories)

| Record id | Field | Old value | New value | Evidence URL |
| --- | --- | --- | --- | --- |
| `form-physlib` | version | (absent) | master HEAD pinned `5bbbb30d08b8e151406a10affbc8a369b74b32c6`, Apache-2.0, push 2026-10-19T20:14Z | https://api.github.com/repos/leanprover-community/physlib |
| `seed-physlib` | version | (absent) | same pin as `form-physlib` | https://api.github.com/repos/leanprover-community/physlib |
| `form-axqm` | version | "main branch as viewed 2026-10-19; mutable; pin unavailable in page view" | main HEAD pinned `b14e4e1032d40f84b4fcaae26210daf916f9e468`, Apache-2.0, push 2026-09-03T20:41Z | https://api.github.com/repos/Axiomatic-AI/AxQM/commits?per_page=1 |
| `meth-tnlean-repo` | observed_state | "immutable commit SHA not captured in this pass" | appends HEAD pin `c1843ea4f348f69b02ca2fee43bbbbe6e9270077` (2026-10-19T19:02Z), Apache-2.0 confirmed | https://api.github.com/repos/LionSR/TNLean/commits?per_page=1 |

### A.6 Limits-field refinements (evidence-anchored)

| Record id | Field | Change | Evidence URL |
| --- | --- | --- | --- |
| `phil-survey` | limits | appended: `/survey/results/all` returns HTTP 403 to automated access on 2026-10-19 (unread); survey and temporal-ontology question page (`/survey/results/5182`) confirmed via search summary only | https://survey2020.philpeople.org/survey/results/5182 |
| `phil-kant` | limits | appended: Gutenberg #4280 is the J. M. D. Meiklejohn translation (B/2nd-edition text), confirmed from the page | https://www.gutenberg.org/cache/epub/4280/pg4280.html |
| `phil-dainton` | limits | appended: linked ISBN 9780415379298 = 2006 Routledge "International Library of Philosophy" reissue; original 2000 (ISBN 0415223822) — confirms the record's own caution | https://openlibrary.org/search.json?title=Stream+of+Consciousness&author=Dainton |

---

## B. Records verified with no changes needed (18)

All checked against the cited catalog/publisher/public page on 2026-10-19.

| Record id | Verified against | Result |
| --- | --- | --- |
| `arrow-penrose-wch-1979` | INSPIRE-HEP + Open Library | Chapter 12, pp. 581–638, in *General Relativity: An Einstein Centenary Survey* (eds. Hawking & Israel, CUP 1979, ISBN 9780521222853); LSE scan live (HTTP 200, 4.0 MB). Record's version/locators correct. Evidence: https://inspirehep.net/literature/159041 |
| `form-physlib-mstate-code` | GitHub API | Pinned SHA 67d742760382efce9419feefa348902aab797a07 exists (committer date 2026-09-07). Evidence: https://api.github.com/repos/leanprover-community/physlib/commits/67d742760382efce9419feefa348902aab797a07 |
| `phil-handbook` | Open Library | *Oxford Handbook of Philosophy of Time*, ed. Callender, OUP 2011, ISBN 9780199298204 |
| `phil-callender` | Open Library | *What Makes Time Special?*, OUP 2017 |
| `phil-maudlin` | Open Library | *The Metaphysics Within Physics*, OUP 2007, ISBN 9780199218219 |
| `phil-mellor` | Open Library | *Real Time II*, Routledge 1998; URL ISBN 9780415097819 matches |
| `phil-bourne` | Open Library | *A Future for Presentism*, Clarendon/OUP 2006 |
| `phil-growing-block` | Crossref (book DOI) | *Nothing To Come*, Correia & Rosenkranz, Springer 2018, book DOI 10.1007/978-3-319-78704-6, ISBN 9783319787039 |
| `phil-cameron` | Open Library | *The Moving Spotlight*, OUP 2015, ISBN 9780198713296 |
| `phil-skow` | Open Library | *Objective Becoming*, OUP 2015 |
| `phil-sider` | Open Library | *Four-Dimensionalism*, OUP 2001, ISBN 9780199244430 |
| `phil-horwich` | Open Library | *Asymmetries in Time*, MIT Press 1987; URL ISBN 9780262580885 (paperback) matches |
| `phil-husserl` | Open Library | *On the Phenomenology of the Consciousness of Internal Time (1893–1917)*, Kluwer 1991, ISBN 9780792308911 (URL ISBN matches); record's Brough-translation note consistent |
| `phil-james` | page fetch | psychclassics.yorku.ca page = "James (1890) Chapter 15", chapter XV heading and "specious present" content present |
| `phil-bergson` | page fetch | Gutenberg #56852 = *Time and Free Will*, Pogson translation, 1910, chapter II present |
| `phil-sep-time` | page fetch | Substantive revision Dec 4, 2025 — matches the record's stated revision date |
| `phil-sep-parts` | page fetch | First published Feb 1, 2004; substantive revision May 5, 2020 (record claimed no date) |
| `phil-sep-present` | page fetch | First published Jan 22, 2018; substantive revision Feb 12, 2026 (record claimed no date) |
| `seed-einstein-1905` | page fetch | fourmilab page live: "On the Electrodynamics of Moving Bodies By A. Einstein June 30, 1905" |

## C. `found-prior-2009`: the intended source cannot be identified

The record claims: Katherine Hawley, "The Future of the Universe", Mind 2009,
DOI 10.1093/mind/fzp077. Verified facts:

1. **The DOI points elsewhere.** Crossref: 10.1093/mind/fzp077 = J. Fernandez,
   review of Hurlburt & Schwitzgebel, *Describing Inner Experience?*,
   *Mind* 118(471):840–843, 2009. Evidence: https://api.crossref.org/works/10.1093/mind/fzp077
2. **No Hawley paper by that title exists.** OpenAlex holds the complete
   bibliography of philosopher Katherine Hawley (author id A5018607675;
   96 works, 1995–2021, fetched in full). No title resembles "The Future of the
   Universe". Her only Mind-2009 item is "Identity and Indiscernibility",
   *Mind* 118(469):101–119, DOI 10.1093/mind/fzn153 (verified via Crossref), which
   is about identity/indiscernibility, not time. Evidence:
   https://api.openalex.org/works?filter=author.id:A5018607675&per-page=100
3. **The title exists only for other authors/fields.** OpenAlex title search
   returns physics/astronomy items (Dicus, Letaw, Teplitz & Doran,
   *Scientific American* 1983; Adams & Laughlin 1998; Meadows 2008; Hawking 1991;
   Pasachoff 1979), none by Katherine Hawley.
4. **`web-search-prime` and DuckDuckGo HTML found no Hawley item** matching the
   title or a growing-block paper by that name.

**Resolution:** the intended source cannot be identified. Proposed handling
(in `proposed-records.jsonl`): quarantine the record — title prefixed
"UNIDENTIFIED — record quarantined", limits field carries the full evidence
trail and a do-not-cite instruction — pending a foundations-lane decision to
retire it or replace it with a deliberately chosen, verified source.

Nearest verified candidates if the lane wants the same relevance ("asymmetry
between past and future and growing-block intuitions"), clearly labeled:

- **Hawley, "Metaphysics and Relativity"**, in *The Routledge Companion to
  Metaphysics*, DOI 10.4324/9780203879306.ch47 (verified in Crossref as an
  existing Hawley chapter). *Conjecture only* that this survey chapter was the
  intended target; its content was not read in this audit.
- **Braddon-Mitchell, "How do we know it is now now?"**, *Analysis* 64(3):199–203,
  2004 — already in the KB as `phil-latest` (DOI verified this audit), and it is
  the canonical latest-edge/growing-block epistemic objection.
- Smolin, *Time Reborn: From the Crisis in Physics to the Future of the
  Universe* (2013) surfaced in search summaries because its subtitle contains
  the phrase; treated as an unexamined lead, **not** a candidate repair.

## D. Records that could not be verified (blocked or inaccessible)

Per the contract, a blocked or paywalled page is recorded as **unread**, never as read.

| Record id | Blocker | What was / was not verified |
| --- | --- | --- |
| `found-prior-2009` | Intended source does not exist as cited | Negative verification only (section C); record quarantined |
| `phil-survey` | `survey2020.philpeople.org/survey/results/all` → HTTP 403 to automated access | Survey existence + temporal-ontology sub-page confirmed via search summary; results page **unread** |
| `found-putnam` (JSTOR landing) | www.jstor.org returns a JavaScript client challenge to curl | Bibliographic data verified via Crossref 10.2307/2024493; JSTOR page **unread** |
| `phil-shoemaker` (JSTOR landing) | same challenge | Verified via Crossref 10.2307/2023892 + SEP bibliography; JSTOR page **unread** |
| `phil-lewis` (JSTOR landing) | same challenge; DOI 10.2307/20009616 not registered; PhilPapers → Cloudflare 403 | Verified via SEP time-travel bibliography (vol 13: 145–52); JSTOR page **unread**; issue number unconfirmed |
| 7 OUP book pages (`phil-handbook`, `phil-callender`, `phil-maudlin`, `phil-bourne`, `phil-cameron`, `phil-skow`, `phil-fine`, `phil-sider`) | academic.oup.com → HTTP 403 | Bibliographic data verified via Open Library; OUP pages **unread** (records cite OUP URLs; URLs kept, evidence recorded) |
| `phil-growing-block` Springer page | link.springer.com → JS client challenge | Book verified via Crossref book DOI; Springer page **unread** |
| `phil-husserl` Springer page | same challenge | Book verified via Open Library (Kluwer 1991, ISBN match); page **unread** |
| `phil-horwich` MIT Press page | mitpress.mit.edu → HTTP 403 | Book verified via Open Library; MIT page **unread** |
| `found-stein-1991` (paperzz copy) | third-party aggregator not re-fetched in this audit | Bibliography verified via Crossref 10.1086/289609; the aggregator copy previously read by the foundations lane was **not** re-inspected |
| `phil-maxwell`/`found-maxwell-1993` (philpapers.org/archive PDF) | philpapers.org → Cloudflare 403 on metadata pages | Bibliography verified via Crossref 10.1086/289737; the archive PDF was not re-fetched |
| Google Books API | Anonymous quota exhausted (HTTP 429) | Open Library used instead; no impact |

## E. Defensive Crossref spot-check of DOI-labeled records (out of scope, findings only)

The brief warns that earlier lanes had wrong DOIs, so all 19 additional DOI
records were probed against `api.crossref.org`. Results:

- **Wrong DOI found (1):** `aqft-bisognano-wichmann-1976` — repair proposed in
  section A.1 / `proposed-other-lane-fixes.jsonl`.
- **Title drift found (1):** `found-deasy-2015` — section A.2.
- **Verified correct (17):** `aqft-haag-kastler-1964` (JMP 5:848–861, 1964),
  `aqft-reeh-schlieder-1961` (Nuovo Cimento 22:1051–1068, 1961),
  `aqft-tomita-takesaki-1970` (LNMS, 1970), `aqft-bisognano-wichmann-1975`
  (JMP 16(4):985–1007, 1975), `arrow-earman-past-hypothesis-2006`
  (SHPS-B 37:399–430, 2006), `disc-brading-empirical-2013-full` (PoS
  80(5):1101–1111, 2013), `disc-brading-locating-present-2015-full`
  (SHPS-A 50:13–19, 2015), `disc-foster-jacobson-einstein-aether-2006` (PRD 73,
  2006), `disc-lageos-alpha1-2026` (PRD 114, 2026), `disc-herrmann-cavity-2007`
  (PRL 99, 2007), `disc-sorci-proper-time-ionclock-2026` (PRL 136, 2026),
  `disc-loriani-clock-interferometry-2019` (Sci. Adv. 5, 2019),
  `disc-lageos-prl-constraint-2026` (PRL 137, 2026), `found-stein-1968`
  (J. Phil. 65(1):5–23, 1968), `found-malament-1977` (Noûs 11(3):293–, 1977),
  `found-rietdijk` (PoS 33(4):341–344, 1966), `found-brading` (= 10.1086/673897,
  same work as `disc-brading-empirical-2013-full`, cross-lane duplicate by design),
  `phil-mctaggart` (Mind XVII:457–474, 1908), `phil-prior` (Philosophy 34:12–17,
  1959), `phil-perry` (Noûs 13(1), 1979), `phil-belnap` (Synthese 92:385–434,
  1992), `phil-everett` (Rev. Mod. Phys. 29:454–462, 1957), `phil-grw` (PRD
  34:470–491, 1986). A transient Crossref failure on `10.1093/analys/64.3.199`
  was re-checked via title search and confirmed valid (`phil-latest`,
  Analysis 64(3):199–203, 2004).

Note on duplicates: `found-brading` (foundations) and
`disc-brading-empirical-2013-full` (discriminators) cite the same DOI across
lanes. Each lane's file is its own register, so this is legal under the
contract; flagged here so synthesis dedupes by DOI.

## F. Log of queries and endpoints (reproducibility)

- Crossref: `/works/{doi}` for 28 DOIs; `/works?query.*` for Bisognano–Wichmann,
  Braddon-Mitchell, Sarkar–Stachel.
- OpenAlex: `/authors?search=Katherine Hawley`; `/works?filter=author.id:A5018607675`
  (full, 96 works); `/works?filter=title.search:"The Future of the Universe"`;
  Lewis and Shoemaker title searches.
- Open Library: `/search.json` for 15 books (title+author), fields incl. ISBN,
  publisher, first_publish_year.
- archive.org: `/metadata/{id}` ×3 (one empty → repair), `/advancedsearch.php` for Reichenbach items.
- GitHub API (unauthenticated): `/repos/{repo}` and `/repos/{repo}/commits?per_page=1`
  for physlib, AxQM, TNLean; `/commits/{sha}` to confirm the pre-existing pin.
- Page fetches: 5 SEP pages (3 current, 1 archived, 1 time-travel for the Lewis
  citation), Gutenberg ×2 (one required `--compressed`), psychclassics, fourmilab,
  White Rose eprint, Scholars@Duke, AFP entry, INSPIRE (via search summary), Penrose
  scan (HTTP 200 size check only).
- web-search-prime: 4 queries (Hawley ×2 — one rate-limited and retried,
  Penrose pagination, PhilPapers survey).
- DuckDuckGo HTML endpoint: 1 query (Hawley) — usable fallback, no relevant hits.
