# Agent report: ctp-priority-audit

## Files changed

- `research/creative/priority-audit/PRIORITY.md` — independent, bounded priority and literature audit, including the exact target scope, a checked direct weighted-sum obstruction, citation-index coverage, screened-work depths, and limits.
- `research/creative/priority-audit/sources.jsonl` — source register with primary URLs, locators, read depths, findings, and limits.
- `research/creative/priority-audit/SEARCH_ROUTES.md` — citation-index, failed-route, and independent discovery log.

## Findings

The closest direct prior is Dowker–Zalel, *Observables for cyclic causal set cosmologies*, arXiv:2212.01149v2 (last revised 2023-07-17, per arXiv history). Its Sec. V supplies a finite-level variation criterion for the doubly-reduced tree, but leaves the valency-one contribution (the sum over doubly-principal causets) unresolved and says it could be computed in future work. The coordinator's all-parameter result follows from a direct estimate of that contribution: every doubly-principal size-\(k+2\) order is \(G\oplus\{u\}\oplus\{v\}\), and the absolute amplitude sum is at least

\[
|p|(|p|+|1-p|)^k\prod_{j\ge1}\left(1-\left(\frac{|1-p|}{|p|+|1-p|}\right)^j\right),
\]

which diverges for \(p\notin[0,1]\). The calculation is an elementary strengthening/application of the paper's criterion. I located no prior publication of this estimate or the exact labelled doubly-principal classification, so the novelty is best framed as a specific weighted-sum estimate and application of that criterion. The full-cylinder nonextension theorem does not imply the result on the smaller algebra. No statement is made about the covariant intersection.

## Evidence and checks

- Read Dowker–Zalel v2 at full-text depth in Secs. III.3–III.4 and V; checked the generator algebra, open extension question, and valency-one passage.
- Read Dowker–Johnston–Surya (2010) Sec. 4 and Surya–Zalel (2020) Secs. 2.3, 3.1–3.3 at full-text depth. They establish nearby full-algebra nonextension and bounded-variation criteria, not this smaller generator-algebra result.
- Checked forward-citing works through INSPIRE-HEP (four direct citing works) and OpenAlex (three direct citing works); screened the returned works at depths recorded in the source register. Also checked targeted arXiv/author records and recent work.
- Screened 2026-07-29 arXiv:2607.26672 full text at Sec. 29.7; its measure discussion is for positive scalar CSG laws. Screened arXiv:2603.25503v1 (2026-03-26) in abstract/introduction/reference context; it concerns operator Bell causality. No journal date is claimed.
- Checked exact combinatorial exponents and the probability identity: given order \(G\), the final label is above all earlier labels iff it links to all maximal elements of \(G\). Reverse exposure gives the Euler product. The product is strictly positive for \(0<s<1\); finite disjoint generator families with unbounded absolute sums contradict finite total variation.
- JSONL parse check and whitespace/diff check only; no project test suite is relevant to this literature task.

## Limitations and unresolved questions

This is not an exhaustive priority certification. Semantic Scholar returned HTTP 429; OpenCitations did not provide a usable citing list (HTTP 400). OpenAlex did not return the 2023 review found by INSPIRE; the 28 citing records for Surya–Zalel were not each full-text screened. Theses, books, non-English repositories, unpublished notes, and all possible alternate terminology were not exhausted. The direct calculation appears to close the precise open case named by Dowker–Zalel, but whether it is best characterized as a new result or a short corollary of their variation criterion remains an editorial novelty judgment. No author was contacted.

## Separate covariant post-tail follow-up

Added `POST_TAIL_PRIORITY.md` and two primary-paper records in `sources.jsonl` after the separate target in `research/creative/COVARIANT_RESULT.md` was supplied. The target explicitly assumes a normalized finite complex measure on pure covariant `R_p`, `ν(P∞)=1`, and a common finite factor for every principal H. The bounded search found the classical real-probability Euler factor in Bombelli–Seggev–Watson (2008), DJS's general conditional-convergence/probability-first proposals (2010), and Sorkin's post-event/principal-stem and evenly-convergent framework (2011). No source located states the target complex all-principal common-factor classification. Priority remains unresolved; classical post probabilities may make some factor calculations immediate under suitable hypotheses, but that does not itself establish the target measure theorem. DJS 2010 does not mention posts in the conditional-convergence discussion; Sorkin 2011 is the post-specific comparison. This follow-up is separate and does not retroactively expand the earlier labelled-algebra audit.

## Follow-up files and checks

- `research/creative/priority-audit/POST_TAIL_PRIORITY.md` — separate bounded priority note for the covariant post-tail result.
- `research/creative/priority-audit/sources.jsonl` — added Sorkin (2011) and Bombelli–Seggev–Watson (2008) full-text records; refined DJS (2010) locator and scope.
- `research/creative/priority-audit/SEARCH_ROUTES.md` — recorded targeted query families and the distinction between adjacent sources.
- `research/creative/priority-audit/AGENT_REPORT.md` — this report.
- Validation: `python3 scripts/check_sources.py research/creative/priority-audit/sources.jsonl` reports 13 records, 0 errors, 0 warnings, 0 info.
