# Read-only review of methods, foundations, and discriminator repairs

Date: 2026-10-20. Reviewed current changes against the frozen `before-records.jsonl` snapshot and the cited source/audit evidence. No source records, audit snapshots, or other project files were changed by this review; only this report is owned here.

## Findings

No blocking factual or scope error found in the reviewed repairs.

- **Malament:** Independently checked the published-scan PDF linked by the new `found-malament-1977` record. Proposition 1 is on p. 296; Proposition 2 is stated on pp. 297–299 and concludes the candidate relation is standard synchrony **or universal**; non-universality selects synchrony. Proposition 3 on p. 299 is the separate K-only result: under its equivalence and nontriviality conditions, the relation is universal. The repaired record states these distinctions accurately, gives the right locators, retains full-text as a read of the primary scan without claiming proof reproduction, and keeps the conventionality/ontology bridge conditional.
- **Putnam:** `found-putnam` accurately replaces the first-pass imprecise transitivity shorthand with Principle III as the stated bridge, then separately identifies the later transitive-closure and observer-abundance step. `reading_history` preserves the partial first pass and the pp. 241–247 second pass, and the conclusion separates ontology from the future-contingent truth-value argument. These statements match `knowledge/foundations/audit.md` §§2 and the primary-page locators.
- **Brading:** `found-brading` and `disc-brading-empirical-2013-full` identify the 2013 law-constitutive proposal and its limits without claiming an operational discriminator or empirical confirmation. Both expressly state that the publicly hosted, journal-paginated copy was not collated with a publisher-hosted version of record. The older abstract/draft account is preserved separately in reading history. No 2015 follow-up claim is attributed to the 2013 article.
- **Stein:** `found-stein-1991` preserves the OCR/context distinction: the isolated four-condition p. 150 transcription is not accepted as a valid implication; the surrounding all-causal-past premise and condition (iv) are recorded; whether the apparent omission is print, OCR, or extraction remains unresolved without a printed-page image. The record attributes no typographical error to Stein and does not infer objective passage. `found-stein-1968` correctly remains discovery-only.
- **Methods:** The added CAS and tensor-network summaries stay within the papers' model/task scope and present outcomes as author reports. CAS outcome counts (five of nine for both 10ex and 3broad; seven of nine for 3tailored; three of nine for instruction) match the primary v1 results text. The tensor record retains the finite-length, positive-bond-dimension/nonempty-chain qualifications and explicitly states that Lean checks the formalized statement rather than paper-intent correspondence. SW-LEAN is consistently attributed to the paper: the record says the results/build/footprint were not independently reproduced, treats SU(2) genus-one results as conditional on H0–H7 and mathematical inputs, and separates the SU(N)/higher-genus skeleton. Ax-Prover's author list matches the exact v4 header; only metadata/related-benchmark details were rechecked, with its historical substantive reading boundary retained.

The methods record-level `reading_provenance` preserves each before-snapshot depth and version for all four changed IDs. The foundations/discriminators records preserve the prior depth and link to the frozen snapshot while separating later reading scopes. The small formatting normalization in Stein 1991's historical version text does not change the edition; the original record remains intact in the before snapshot.

## Verification and limits

Read-only checks performed:

```text
python3 scripts/check_sources.py --strict knowledge/methods/sources.jsonl knowledge/foundations/sources.jsonl knowledge/discriminators/sources.jsonl
3 files, 35 records: 0 errors, 0 warnings, 0 info

git diff --check -- <the three reviewed registers>
clean
```

For Malament, the public university-hosted PDF exposes a JSTOR reproduction with the journal cover/metadata; I checked the proposition statements and page locators, not the proof details. I did not independently rebuild any Lean project, rerun CAS experiments, reconstruct Putnam's argument formally, verify Brading's copy against the publisher PDF, or resolve Stein's printed-page/OCR mismatch. For SW-LEAN, an optional precision improvement would name the paper's two nonstandard covering/lift inputs and three logical axioms alongside H0–H7; the current record nevertheless labels the results as author-reported and states that exact transitive footprints were not rebuilt, so I do not treat this as a blocking overclaim.
