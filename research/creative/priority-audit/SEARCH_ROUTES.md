# Search route and index log

Checked 2026-10-19. This records a bounded discovery search, not an exhaustive
citation census or global priority certificate. Paper records and read depths
are in `sources.jsonl`.

## Forward-citation routes

- **INSPIRE-HEP**: query `refersto:recid:2609896` for arXiv:2212.01149. Four
  citing records were returned: arXiv:2310.17547, 2501.00139, 2603.25503, and
  2311.14881. The four titles are transcribed in `PRIORITY.md` and the source
  register; all four were screened at the depths recorded there.
  Query URL: <https://inspirehep.net/literature?q=refersto%3Arecid%3A2609896>.
- **OpenAlex**: DOI/arXiv work matching and citing-work filtering for
  arXiv:2212.01149 and 2003.11311. It returned three direct citations for
  2212.01149 (2310.17547, 2501.00139, 2603.25503), missing the 2023 survey
  returned by INSPIRE. For 2003.11311, it returned 28 records; not every citing
  record was individually read. This second route is a screen for potential
  leads, not an exhaustive review of all 28 papers.
  Search endpoint: <https://api.openalex.org/works?search=Observables%20for%20cyclic%20causal%20set%20cosmologies>.
- **Failed/unusable index routes**: Semantic Scholar citation endpoint returned
  HTTP 429. OpenCitations did not return a usable citing-work list (HTTP 400); Crossref
  did not yield a usable forward-citation list in this run. They are excluded
  from evidence. Google Scholar was not used as an index
  source.

## Independent discovery routes

- arXiv search/version pages and targeted queries for `"doubly-reduced poscau"`,
  `"doubly principal" causal set`, and `"complex transitive percolation"
  extension`.
- Fay Dowker and Stav Zalel author/publication records; recent arXiv submissions
  for causal-set measure-extension terms.
- Thesis/review search for complex percolation and extension terminology. The
  targeted thesis result was verified against its institutional repository
  record before adding it to `sources.jsonl`.

The closest hit remains Dowker–Zalel's own statement of the unresolved
valency-one contribution on the doubly-reduced tree. No separate source stating
the weighted-sum lower bound or the resulting all-parameter classification was
located. Searches did not exhaust all theses, books, repositories, languages,
unpublished notes, or alternative terminology.

## Separate covariant post-tail follow-up

The follow-up is recorded separately in `POST_TAIL_PRIORITY.md`; it was not part of the earlier labelled-algebra priority audit. Targeted queries checked combinations of `complex percolation`, `post`, `Euler product`, `future descendants`, `principal stems`, `conditional convergence`, and `infinite posts`, along with direct primary-source reads of arXiv:1007.2725v1, 1104.0997v2, and 0809.2258v2. Search-engine discovery routes included arXiv and general web queries; the source register records full-text depths and section locators for the sources that materially informed the comparison. No separate complex covariant all-principal common-factor theorem was located in this bounded follow-up.

The comparison corrects one possible ambiguity: Dowker–Johnston–Surya (2010) does not discuss posts in its conditional-convergence section. It discusses ordering-dependent conditional convergence generally and a probability-first complexification example for the originary event. Sorkin (2011) is the source that explicitly formulates the post event using principal stems and discusses events such as infinitely many posts. Bombelli–Seggev–Watson (2008) supplies the classical real-probability Euler factor for the future-post condition. These are adjacent ingredients, not verification or disproof of the new complex covariant theorem.
