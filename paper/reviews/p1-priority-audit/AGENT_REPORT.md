# Agent report: P1\*\* priority audit

Task: independent, bounded defeat search for the claim that the P1\*\*
coverage point is modestly novel. Date: 2026-10-21. Target commit `5a9ec90`.

Status: worker submission. Not a priority certificate. Not accepted until the
coordinator inspects it.

## Files changed

- `paper/reviews/p1-priority-audit/REVIEW.md` (new)
- `paper/reviews/p1-priority-audit/AGENT_REPORT.md` (new)

No other path was written, including `paper/main.tex`, the workboard, and
`research/existence-form/`. No commits, pushes, or agent launches.

Note: `git status` at the end of this run shows `paper/main.tex` as modified and
sibling directories `paper/reviews/p1-logic-audit/` and
`paper/reviews/p1-source-audit/` as untracked. None of that is this audit's
work; it belongs to concurrent sessions. This audit's only additions are the two
files listed above.

## Materials read in this audit

Local, read-only:

- `AGENTS.md`, `knowledge/NOVELTY.md`, `paper/main.tex` (all 428 lines),
  `paper/references.bib`, `paper/SOURCE_AUDIT.md`,
  `research/existence-form/NOVELTY_AUDIT.md`,
  `research/existence-form/TRILEMMA.md`,
  `paper/reviews/external-2/REVIEW.md`,
  `research/article-admissibility/primary-review/SOURCES.md`.

External, fetched and read (temporary copies under the approved temp dir, not
added to the repo):

| Source | Version / locator | Depth | Notes |
|---|---|---|---|
| Brading 2015, *SHPS-A* 50, 13–19 | public published-layout PDF; SHA-256 `7caceae74aebe28d1775561cd307dce50f912570eb1a7f9a709d70c699b08f6b` | full-text, pp. 15–19 | Hash **matches** `paper/SOURCE_AUDIT.md`; identity independently confirmed. Text extracted with a small PDFKit (Swift) helper because `pdftotext`/pypdf were unavailable |
| Brading 2013, *Phil. Sci.* 80, 1101–1111 | public PDF; SHA-256 `c93ca072e14c4fd0f1c638ff960db17847231479ec9bf168cf0d69f9644bb054` | full-text, pp. 1105, 1109–1110 | Hash **matches** the recorded value |
| Savitt, "Being and Becoming in Modern Physics", SEP | live entry + `fall2014`, `win2020`, `fall2023` archives | full-text §3.3; archive diff for dating | Main finding |
| Mason, "Temporal Perspectives, Probabilities, and Openness" | PhilSci-Archive 25374 preprint via Wayback `20250922154454`; SHA-256 `38312ca49099069e579f26195315e5a4115299b226e6c3a490294af9711ca780` | full-text (26 pp.) | Published *Synthese* version not read |
| Rovelli, "Neither Presentism nor Eternalism" | arXiv:1910.02474v2 | full-text | FoP 49 (2019) 1325–1335 |
| Wüthrich, "Demarcating presentism" | wuthrich.net 2010 preprint | full-text | No Brading citation |
| Balaguer 2026 ch. 11 | DOI 10.1093/9780197845745.003.0011, pp. 212–237 | **abstract only** (Crossref) | Body unread |
| SEP "Presentism" | rev. 12 Feb 2026 | selected full-text | No Brading citation |
| Crossref / OpenAlex / Semantic Scholar records | as of 2026-10-21 | discovery | Citation graphs |

## Search queries run

OpenAlex REST (works by DOI, `filter=cites:…`, `fulltext.search`, authors):

- work records for `10.1016/j.shpsa.2014.09.007` (W2005418088) and
  `10.1086/673897` (W2173391953)
- citing works for both
- fulltext searches: `"Brading" "P1"`, `"empirical presentism"`,
  `"present" "Minkowski" "Brading"` (relevance-sorted). These returned mostly
  noise; OpenAlex fulltext search behaves as a loose bag-of-words filter and is
  not reliable for phrase queries. Not treated as evidence.

Semantic Scholar Graph API:

- `citations` for both DOIs (returned 3 and 3 citing items respectively)
- paper record for Mason 2026 (no OA PDF, abstract elided)

Crossref REST:

- book chapters of Balaguer 2026 (`query.container-title`), abstracts retrieved
- Mason 2026 record
- *SHPS-A* 2015 volume-50 listing (Crossref `query.container-title`), to check
  for a same-issue reply to Brading. Volume 50 items: introduction pp. 1–3,
  "Why history matters to philosophy of physics" pp. 4–12, Brading pp. 13–19,
  and unrelated papers. No reply identified.
- Dorato / Wüthrich bibliographic probes

Web search (Google via SerpAPI):

- `"all we need is (a)" Brading`
- `"In order to avoid the block universe, all we need is"` (zero results)
- `"P1**" Brading presentism block universe`
- `Brading "empirical presentism" critique local present coverage`
- `"system-relative" existence presentism Brading`
- `Mason "Temporal Perspectives, Probabilities, and Openness" pdf`
- `"every dynamical system that has existed" Brading present`
- `Savitt "Presentism and Eternalism in Perspective" local present block`
- `"local presents" "block universe" presentist "every event"…`
- `presentism "union of" presents "the whole history" local present critique`

Web search results were generally poor: the engine ignores quotes/asterisks and
returns commercial noise for "local presents"/"presents". I treated these as
weak negative evidence only.

arXiv API: title query for "Neither Presentism nor Eternalism" (found
arXiv:1910.02474). Abstract queries with `abs:` operators returned off-topic
results; abandoned.

Wayback CDX: `philsci-archive.pitt.edu/25374*`, `.../9936*`. Used to recover the
Mason preprint after the archive's WAF blocked direct access.

`web-search-prime` MCP tool: **quota exhausted** (429, resets 2026-11-17). Not
used.

## Access failures (recorded so they are not mistaken for absence of sources)

- **PhilPapers**: Cloudflare interstitial on every request (`/s/Brading`,
  record pages). Not searched. This is the most important gap: a short
  discussion note on Brading 2015 would most plausibly be indexed there.
- **PhilSci-Archive**: F5/TSPD JavaScript challenge on both landing and file
  URLs. Worked around via Wayback for item 25374 only.
- **SpringerLink**: bot challenge page; Mason's published version unread.
- **OUP Academic**: not attempted directly for the Balaguer body; Crossref
  abstracts used instead.
- **philarchive.org**: Cloudflare 403.
- **scholar.archive.org**: "Session Verification" page.
- **OpenAlex**: unauthenticated, shared daily budget; some queries returned 0.

## Main finding

Savitt's SEP entry, §3.3 "Localizing Time" (added in the substantive revision of
6 October 2021; absent from the 2013 and 2017 revisions), already argues that
Brading's dynamics-relative local present characterises "a relativistic
present, not relativistic presentism", on the premise that every dynamical
system that has existed, does exist or will exist has a sustaining region, and
raises the co-presence question. That is the substance of the paper's objection,
aimed at Brading 2013.

Consequence: the `NOVELTY_AUDIT.md` sentence "appears not to be stated in the
prior work found" is false for the 2013 formulation. The defensible residual
claim is only the application to Brading 2015 P1\*\* (a) and to "all we need is
(a)", which no source read states.

The audit's search design missed this because it did not search SEP entries.
`NOVELTY_AUDIT.md` lists Savitt (2009, 2011) only as a definer of local presents
and says he "do[es] not raise the union/coverage objection to Brading's (a)".
The second half is true of (a); the first half is not true of Savitt's SEP
entry.

## Checks performed

- File identity: SHA-256 of both Brading PDFs recomputed and matched against
  `paper/SOURCE_AUDIT.md`.
- Quotations: P1\*\*, "all we need is (a)", "calls the ontology of a block
  universe into question", p. 18 survival condition, p. 16 "all the way up to
  the material universe as a whole", p. 17 "what exists (what is real) are the
  genuine unities", 2013 nn. 3, 6, 7 and the interaction passage — all checked
  against extracted text in this audit.
- Extraction caveat: the PDFKit extraction drops `fi`/`fl` ligatures
  ("satis ed", " nd ourselves", "signi cant"). I did not quote any sentence
  containing such a ligature; those are paraphrased in `REVIEW.md`.
- Date-checked the SEP passage across four archive snapshots.
- Confirmed Mason's preprint does not contain the string "2015" and cites only
  Brading 2013.
- Confirmed Wüthrich 2010 and SEP "Presentism" do not cite Brading.

## Limits

- Bounded search; no priority certificate. Under-coverage of PhilPapers and of
  paywalled journal bodies means the L2 claim (no published application to
  P1\*\*) is "not found", not "does not exist".
- Unread: Balaguer 2026 body (highest-risk unread source), published Mason
  (*Synthese* 2026), Savitt 2006, Slavov 2022, Raźniak 2023, the *SHPS-A* vol.
  50 introduction, Savitt's 2009 and 2020 papers cited in the SEP.
- I did not assess whether the paper is right that (a) is insufficient; only
  what is already published.

## Unresolved leads worth the coordinator's attention

1. **Balaguer 2026, ch. 11 and the SR discussion elsewhere in the book.** If
   Balaguer says Brading's view does not restrict existence, the L2 increment
   may also be occupied. Needs the body text, not the abstract.
2. **Savitt 2006, "Presentism and Eternalism in Perspective".** Likely the
   earliest printed statement of the perspective-relative existence premise the
   paper's N-form relies on; currently cited only second-hand.
3. **PhilPapers citation list for Brading 2015.** Would settle whether a
   discussion note exists.
4. **Raźniak 2023 (Polish).** A point-like conception of the present citing
   Brading 2013; may contain a local-present critique not visible to English
   indexes.
5. **Same-issue commentary in *SHPS-A* vol. 50.** The Crossref listing shows no
   reply, but the issue's introduction (pp. 1–3) was not read.
6. **Callender 2017 "now patches"** and **Arthur 2019** local becoming: cited in
   Savitt's §3.3 as nearby views; not examined, because the audit's target is
   the Brading-specific claim.

## Recommendation to the coordinator

Do not record the P1\*\* coverage point as "not stated in the prior work found".
Record it as a narrow retargeting, cite Savitt's SEP §3.3 as the prior critique,
and rewrite the contribution sentence as in `REVIEW.md` §9. If the coordinator
wants the stronger priority claim, the Balaguer body and the PhilPapers graph
must be checked first; the present audit cannot support it.
