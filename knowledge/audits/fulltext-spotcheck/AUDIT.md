# Full-text claim spotcheck

Checked 2026-10-20. Twenty records already claiming full-text depth were spotchecked, plus the separately required Stein 1968 and Malament 1977 primaries: **22 records total**. Sixteen are confirmed at the inspected locator/statement level; three have claim or metadata overstatements, two need locator/edition metadata correction, and one primary remains unreadable. Confirmation does not mean a theorem was proved, a whole paper was audited, or novelty was established.

## Sampling and scope

The committed cutoff is `82f1547`. `sampling.py` reproduces `sampling-frame.json` from that revision, using seed `20261020`; 72 distinct knowledge IDs claim full-text depth at the cutoff. All ten explicitly named full-text contract/policy anchors were included. Eight specified lane strata each contributed one seeded draw. Three full-text causal-set IDs refer to the same papers as RC-4's shallow frontier IDs; they were included as explicit alias anchors, one already selected by the random draw. This avoids excluding RC-4 merely because its primary reads used different IDs. The two mandatory older-depth primaries are additional to the 20 full-text records.

The original seeded draws and frozen source-record payloads were preserved when the two additional aliases were added. Input SHA-256 hashes, candidate lists and exact selections are recorded. Claude integrated five relational-Markov records after this cutoff; those new records are outside this frozen sample and require their own source review. The frame is reproducible rather than a continuously changing population.

Three native agents read disjoint samples (7 clocks/methods, 7 foundations, 8 physics records); the coordinator checked completeness, metadata-conflict evidence, source hashes and the main conceptual hazards. The coordinator reopened the measurement-paper header, Malament's published scan, Stein 1991's OCR context, Hartle and Wüthrich–Callender to inspect important findings. Two sampled SEP entries are secondary texts: confirming their archived contents is not primary theorem verification.

## Source-by-source dispositions

Each evidence file contains the primary URL, exact edition, read scope, decisive quotation, locator and limitations. Quotes occur once in the lane evidence files; the index refers to them without duplicating them.

| Source ID | Verdict | Evidence | Proposal / remaining scope |
|---|---|---|---|
| `aqft-fewster-verch-2012-kg` | confirmed | [foundations/findings.jsonl:4](foundations/findings.jsonl) | Retain the recorded model/domain and author-report limitations; no proof or code reproduction. |
| `arrow-wallace-gravity-entropy-2009` | locator-wrong | [foundations/findings.jsonl:5](foundations/findings.jsonl) | Add Section 7 for the specific matter/radiation entropy claim. |
| `axrel-sep-bebecome-2021` | locator-wrong | [physics/findings.jsonl:1](physics/findings.jsonl) | Correct archive edition vs substantive-revision dates; retain secondary status. |
| `cs-madsen-2026-v1` | confirmed | [physics/findings.jsonl:2](physics/findings.jsonl) | Retain the recorded model/domain and author-report limitations; no proof or code reproduction. |
| `cs-rideout-sorkin-2000-v3` | confirmed | [physics/findings.jsonl:7](physics/findings.jsonl) | Retain the recorded model/domain and author-report limitations; no proof or code reproduction. |
| `cs-wuthrich-callender-2015-v1` | claim-overstated | [physics/findings.jsonl:8](physics/findings.jsonl) | Qualify population scarcity/Lorentz inference; retain the finite counterexample. |
| `fol-dgtz-2014-can-bohmian` | confirmed | [physics/findings.jsonl:4](physics/findings.jsonl) | Retain the recorded model/domain and author-report limitations; no proof or code reproduction. |
| `found-malament-1977` | confirmed | [foundations/findings.jsonl:7](foundations/findings.jsonl) | Primary body now read; propose full-text upgrade with exact proposition locators. |
| `found-sarkar-stachel-1999` | confirmed | [foundations/findings.jsonl:1](foundations/findings.jsonl) | Retain the recorded model/domain and author-report limitations; no proof or code reproduction. |
| `found-sep-malament` | confirmed | [foundations/findings.jsonl:2](foundations/findings.jsonl) | Supply Janis and archived edition metadata; retain secondary status. |
| `found-stein-1968` | unreadable | [foundations/findings.jsonl:6](foundations/findings.jsonl) | Keep discovery depth; no primary body obtained through attempted routes. |
| `found-stein-1991` | confirmed | [foundations/findings.jsonl:3](foundations/findings.jsonl) | Retain context/OCR caveat; the literal four-premise characterization is false in isolation. |
| `frontier-page-wootters-measurements-2023` | claim-overstated | [clocks-methods/findings.jsonl:1](clocks-methods/findings.jsonl) | Correct the frontier author/date fields; review the equal-depth canonical choice. |
| `frontier-qrf-beyond-subsystems-2026` | confirmed | [clocks-methods/findings.jsonl:2](clocks-methods/findings.jsonl) | Retain the recorded model/domain and author-report limitations; no proof or code reproduction. |
| `frontier-relational-trinity-2019v3` | confirmed | [clocks-methods/findings.jsonl:3](clocks-methods/findings.jsonl) | Retain the recorded model/domain and author-report limitations; no proof or code reproduction. |
| `frontier-relativistic-trinity-2020v1` | confirmed | [clocks-methods/findings.jsonl:4](clocks-methods/findings.jsonl) | Retain the recorded model/domain and author-report limitations; no proof or code reproduction. |
| `frontier-smith-ahmadi-interacting-2019` | confirmed | [clocks-methods/findings.jsonl:5](clocks-methods/findings.jsonl) | Retain the recorded model/domain and author-report limitations; no proof or code reproduction. |
| `gq-bs-2005-smooth-time` | confirmed | [physics/findings.jsonl:3](physics/findings.jsonl) | Retain the recorded model/domain and author-report limitations; no proof or code reproduction. |
| `meth-diagrammatica-2026` | confirmed | [clocks-methods/findings.jsonl:6](clocks-methods/findings.jsonl) | Retain the recorded model/domain and author-report limitations; no proof or code reproduction. |
| `meth-sw-lean-2026` | confirmed | [clocks-methods/findings.jsonl:7](clocks-methods/findings.jsonl) | Retain the recorded model/domain and author-report limitations; no proof or code reproduction. |
| `time-hartle-2005-now` | claim-overstated | [physics/findings.jsonl:6](physics/findings.jsonl) | Replace the objective-passage conclusion with the narrower IGUS/model claim. |
| `tr-hersent-2025` | confirmed | [physics/findings.jsonl:5](physics/findings.jsonl) | Retain the recorded model/domain and author-report limitations; no proof or code reproduction. |

## Contract impacts

- **RC-1:** the clock sources support restricted uncoupled equivalence, an interacting kernel construction, and a specific frame-dependent model. The continuous QRF example is outside that paper's rigorous finite-dimensional framework; use the bounded finite analogue for any implementation. No necessary/sufficient classification or priority result was verified here.
- **RC-2:** Malament's original propositions are now readable, removing the earlier primary-access gap for that paper. Its uniqueness conclusion remains conditional on the selected causal/observer/definability framework. Stein 1968 remains unread; Stein 1991 is a separate source. The first worker extraction repeated the false isolated OCR theorem statement; the coordinator rejected it using the existing universal-relation and chronological-past countermodels. The corrected finding keeps the surrounding full-causal-past and unsettled-state conditions explicit and leaves the proposed premise-dependency proof as project work. No error is attributed to Stein's printed text without a page-image comparison.
- **RC-3:** the relativistic source supports sectorwise equivalence and inaccessibility of sector coherence for its relational Dirac observables. A broader no-go for arbitrary instruments or external references is not established by this check.
- **RC-4:** the same-paper aliases supply actual full-text checks of the CSG model and becoming discussion instead of relying on older abstract labels. Growth-compatible becoming remains interpretive; the population genericity claim requires qualification. Madsen's reconstruction statement does not adjudicate becoming or record access. No new growing-vs-completed-history equivalence was derived.
- **RC-5:** the checked measurement model supplies specific finite-clock nonlocal/nonunitary behavior. That alone does not classify semigroup failure, divisibility, backflow and multi-time memory. The separate relational-Markov audit integrated by Claude must be assessed on its own evidence.

## Access and verification limits

Malament was read from a university-hosted scan of the published article: https://lps.elte.hu/gomori/reduction/readings/malament1977.pdf. Stein 1968 remained inaccessible after the documented JSTOR/DOI and PhilArchive attempts; metadata and snippets were not promoted to a primary reading. Detailed routes are in the foundations report. Neither source's register was edited.

The primary measurement-paper header at https://arxiv.org/html/2308.10967v1 supports the ico-qrf author/date fields and contradicts those fields in the frontier copy. Canonicalization records this as an unresolved source-owner decision, with a specific primary-backed correction proposal. This audit also narrows the Hartle attribution: a subjective-time model is not a proof about objective passage or temporal ontology.

The observed confirmation count is **16/22** (16/21 among sources whose relevant body text was available), a descriptive audit outcome only. The sample combines mandatory anchors and stratified draws and is not a population-wide error-rate estimate. Different prompts/agents do not make source claims true; the useful evidence is the inspected source text and explicit counterexamples. No Lean build, code audit, experimental reproduction, priority certification or ontology selection occurred.

`verification.json` records exact coverage, reproduction and source-hash checks. All 22 IDs occur exactly once in the evidence; every readable item has a locator and short quote (maximum 18 words/source). Proposals remain separate from source registers for owner/coordinator application.
