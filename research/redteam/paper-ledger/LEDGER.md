# Claim ledger: paper/main.tex (19 October 2026 draft)

2026-10-20, Claude coordinator. Read-only on `paper/` and `knowledge/`. Depth is
the best `read_depth` among knowledge records for the work; where records
disagree, all are listed. `SOURCE_AUDIT.md` is the paper's own ledger and is
compared, not replaced.

Flags: **A** traced to a full-text record · **B** rests on abstract or discovery
depth · **C** records conflict (depth or reading) · **D** no knowledge record ·
**E** own argument or elementary result (no source needed; checked for validity) ·
**F** wording stronger than its support.

| # | Lines | Claim | Cited | Record(s), depth | Flags | Note |
|---|---|---|---|---|---|---|
| 1 | 20–35 | Burden-of-proof framework; no priority, prediction or preferred ontology claimed | — | — | E | Hedged correctly. |
| 2 | 38–41 | No systematic review, proof-assistant check or novelty-audited result | — | — | E | True as of 2026-10-20. |
| 3 | 45–51 | Three routes: contradiction, prediction, explanation | — | — | E | |
| 4 | 53–59 | Typical mis-inferences (simultaneity → no passage; history → determinism; equivalence → no time) | — | — | E | Illustrative; no author named, so no attribution risk. |
| 5 | 65–66 | The field's breadth is "usefully represented by" the Oxford Handbook | Callender2011 | `phil-handbook` discovery | B | Fine for a breadth pointer. SOURCE_AUDIT says "publisher overview/contents"; the record says discovery. |
| 6 | 66–68 | Callender 2017 and Maudlin 2007 "warn against treating one account of passage as the neutral interpretation" | Callender2017, Maudlin2007 | `phil-callender`, `phil-maudlin` abstract | B, F | The warning is the paper's inference from their contrast, worded as if they issue it. Proposal: "their contrasting programs show that no single account…". |
| 7 | 70–79 | Thesis quote | — | — | E | |
| 8 | 85–89 | Working definitions of presentism, eternalism, growing block, spotlight | — | — | E | Stipulative, labelled schematic. |
| 9 | 89–92 | Direct defenses differ: Bourne, Correia–Rosenkranz, Cameron; replies not audited | Bourne2006, CorreiaRosenkranz2018, Cameron2015 | `phil-bourne`, `phil-growing-block`, `phil-cameron` abstract | B | Self-flagged in the text. |
| 10 | 94–100 | An eternalist can accept indeterminism; 4D spacetime does not entail worms; knowing "now" is not knowing a spotlight property | — | — | E | Standard distinctions, unsourced. Acceptable as working argument. |
| 11 | 103–105 | McTaggart "already differentiates temporal order, change, and A-determinations" | McTaggart1908 | `phil-mctaggart` discovery | B, C | SOURCE_AUDIT claims "selected public-domain transcription passages"; the record says discovery. Reconcile; the claim itself is standard. |
| 12 | 106 | Skow "distinguishes robust from less demanding senses of passage" | Skow2015 | `phil-skow` abstract | B | Plausible from the abstract; no locator. |
| 13 | 107 | "No result about clock rates alone establishes which sense is physically real." | — | — | E, F | A universal claim with no argument given. Proposal: add "by itself" reasoning (clock rates concern metric structure, not passage senses) or soften. |
| 14 | 111–129 | Package tuple `M=(P,O,B,A,S;E)`; likelihoods belong to realized packages | — | — | E | Bookkeeping, labelled as such. |
| 15 | 131–148 | Four admissibility conditions; burden allocation | — | — | E | READINESS item 4 says this defense still needs strengthening. |
| 16 | 154–168 | Exclusion of a conjunction is not exclusion of O | — | — | E | Valid propositional logic. |
| 17 | 172–192 | Equal likelihoods; pointwise vs marginal evidence; Bayes factor 1 under equal prior predictives | — | — | E | Correct; `check_records.py` tests the pointwise-vs-marginal case (passes 2026-10-20). |
| 18 | 196–203 | Representation equivalence needs domain, inner product, observable map, access | — | — | E | |
| 19 | 207–216 | Boost kinematics: `t' = −γvL/c²` | — | — | E | Checked by hand: correct. |
| 20 | 219–221 | Putnam invokes an observer-neutral reality-transfer principle; closure adds observer assumptions | Putnam1967 | `found-putnam` full-text (foundations; also a proposed variant in bib-audit) | A, C | SOURCE_AUDIT: the first-pass record describes a narrower reading and must be reconciled before submission. |
| 21 | 222–225 | Stein's event-relative account; the paper does not reproduce the theorem; the isolated OCR statement is "too weak"; printed formulation unverified | Stein1991 | `found-stein-1991` full-text (OCR) | A, C | `research-contracts.md` calls the isolated statement **false**, with two countermodels (correspondence cases 1–2). The paper's "too weak" is milder, so not an overstatement, but use one wording. The primary page image is unread. |
| 22 | 227–234 | Appending a preferred foliation without changing dynamics or access need not change predictions; coupling can make it observable | — | (now) `knowledge/discriminators/comparison-ledger.md`, accepted 2026-10-20 | E | Now traceable: LAGEOS α1 and Einstein-aether records give the coupled case. |
| 23 | 236–240 | Brading develops a presentist program disputing that simultaneity must provide the unity of what exists | Brading2013 | `found-brading` abstract; `seed-brading-presentism` abstract; `disc-brading-empirical-2013-full` full-text (author-linked draft, no argument reconstruction) | C | Three records at two depths for one paper (canonicalization). The discriminators lane's reading supports the paper's description. |
| 24 | 242–258 | Costs on both sides; schematic foliation and local-becoming replies | — | — | E | Self-labelled "not fully audited reconstructions". |
| 25 | 264–267 | The relational trinity relates three descriptions under hypotheses; non-interacting setup and clock conditions matter | HoehnSmithLock2019 | `frontier-relational-trinity-2019v3` full-text | A | |
| 26 | 267–269 | Interaction treatments exist (Smith–Ahmadi kernel equation); "add interactions" is not a generic gap | SmithAhmadi2019 | `frontier-smith-ahmadi-interacting-2019` full-text | A | Also supported by defeat search B. RC-1 reread pending. |
| 27 | 271–286 | Stationary constraint ≠ no change; conditional dynamics ≠ exhaustive temporal reality; nonunitary evolution ≠ open future | — | — | E | |
| 28 | 288–293 | Research task: boundary of a published equivalence; check interacting, periodic-clock, QRF literature first; none claimed | — | — | E | Depends on `kb-clock-interactions` (running). |
| 29 | 301–318 | Proposition and proof (pushforward change of variables) | — | — | E | Proof valid as stated. |
| 30 | 320–332 | Sequential vs pre-sampled Markov paths agree on prefix records under the stated access condition | — | — | E | Tested by `check_records.py` (`test_full_history_laws`). |
| 31 | 335–341 | `P(000) = 9/32`, `P(010) = 1/32` | — | — | E | Hand-checked and tested. |
| 32 | 343–349 | A sequential generator is not the growing block; a sampled path is not eternalism | — | — | E | |
| 33 | 351–357 | Same passive law, different `do(X=0)` law | — | — | E | Tested (`test_same_passive_different_interventional_laws`); also grid control 03. |
| 34 | 359–364 | Records cannot favor an implementation when measure and response kernels match; becoming needs a defended interpretation and comparison with histories / covariant growth | — | — | E | The comparison with CSG prior work (Rideout–Sorkin `W(C)P(C)`; RC-4) is not yet in the paper. |
| 35 | 368–405 | Five objections and replies | Callender2017, Skow2015 | abstract | B | Replies argue against unnamed positions. Low attribution risk, but no defender is quoted. |
| 36 | 407–412 | Record example is elementary, not the contribution | — | — | E | |
| 37 | 416–433 | Three possible contributions; novelty gate unmet | — | — | E | True as of 2026-10-20. |
| 38 | 434–435 | Existence of Cauchy slicings under global hyperbolicity is not uniqueness of a present | BernalSanchez2005 | **none** | D | No knowledge record; SOURCE_AUDIT says abstract and bibliographic record only. BS2005 gives smooth Cauchy time functions and the metric splitting; existence of topological Cauchy slicings is Geroch (1970). Proposal: add a source record and say "smooth". |
| 39 | 439–447 | Provisional conclusion | — | — | E | Restates the thesis; no new claim. |

## Bibliography orphans

- In `references.bib` but never cited: none.
- Cited but not in `references.bib`: none (14 keys each way).
- Cited with no knowledge source record: **BernalSanchez2005**.
- Cited with records that disagree on depth: **Brading2013** (abstract ×2, full-text ×1),
  **McTaggart1908** (record discovery vs SOURCE_AUDIT "selected passages"),
  **Callender2011** (record discovery vs SOURCE_AUDIT "overview/contents").
  Duplicate IDs `found-stein-1991` and `found-putnam` also appear in
  `knowledge/bib-audit/proposed-records.jsonl`. That belongs to
  `rt-source-canonicalization`, which the Codex session holds.
