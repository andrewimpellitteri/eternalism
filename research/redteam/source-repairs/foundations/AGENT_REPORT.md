# Foundations/discriminators source-repair report

Date: 2026-10-20. This native source-repair task edited only `knowledge/foundations/sources.jsonl`, `knowledge/discriminators/sources.jsonl`, and this report. Root owns board transitions and integration. The historical `before-records.jsonl`/`before-manifest.json`, accepted audit snapshots, proposed-record snapshots, shared seed, alias registry, and other source registers were not modified.

## Changes applied

- `found-sep-malament`: added author Allen I. Janis and exact archived edition metadata (Winter 2001; the archived entry reports original publication in 1998 and last modification 1999-06-30), with the audited Malament-theorem locator. Kept it explicitly secondary and preserved its earlier full-text reading provenance and missing-metadata state.
- `found-malament-1977`: upgraded the original abstract-only record to full-text based on the published Noûs/JSTOR scan, verified directly at `https://lps.elte.hu/gomori/reduction/readings/malament1977.pdf`. Added exact statement locators for Proposition 1 (p.296), Proposition 2 and argument (pp.297–299), and Proposition 3 (p.299), plus K/O definitions (pp.294–296). The record now distinguishes Prop. 2's disjunctive result (standard synchrony or universal) from the non-universal condition that selects standard synchrony, and separately records Prop. 3's K-only universal-relation result. The original abstract-only provenance and its SEP-derived/unchecked status remain in `reading_history`; the later primary read is separately attributed. This is not a proof reproduction or an unconditional conventionality/ontology result.
- `found-putnam`: reconciled the first-pass pp.240–242 shorthand with the second-pass foundations audit of pp.241–247. The record now identifies Principle III (observer-neutral reality transfer) as the stated bridge; separately records the later transitive-closure plus abundance-of-observers premise; and distinguishes both from geometric transitivity and from the future-contingent truth-value discussion. Both readers' scopes, the old partial-reading limitation, and its imprecise summary are retained in `reading_history`. No historical proposed-record file was changed.
- `found-brading` and `disc-brading-empirical-2013-full`: integrated the complete article-level read reported in the prior evidence task. The read copy is a public, 11-page PDF carrying the published *Philosophy of Science* pagination/imprint, checked against Duke and Cambridge publication metadata: `https://a7ad7762-bf80-40ab-9c06-f74d25597b55.filesusr.com/ugd/766654_811c433ef66645b68a25658f93370442.pdf`. Exact argument locators and the law-constitutive/system-sustaining proposal are captured. Both records explicitly state that the host is not the publisher and no publisher-file collation was done; no operational discriminator, empirical confirmation, or ontology selection is inferred. The previous abstract-level record and previous claimed author-linked-draft read are preserved separately. Different IDs remain separate; alias canonicalization is not performed here.
- `found-stein-1968` was left unchanged at discovery depth.
- `found-stein-1991` retains full-text depth and now records the distinction between the false isolated four-premise OCR sentence and the surrounding all-causal-past plus condition-(iv) context. The print/OCR/extraction mismatch remains unresolved pending a printed-page image; no error is attributed to Stein's published text. Prior reader scope and the second-pass OCR-context check are separately preserved.

Each edited record includes a `reading_history` entry pointing back to `research/redteam/source-repairs/before-records.jsonl` at snapshot revision `edfb80314fe7db51971cadf11f86690da3b71ac9`, along with old depth/version/scope and subsequent audited reading scope. The new source summaries remain limited to the cited primary/secondary text and do not settle philosophical bridge premises.

## Checks and hashes

The source payloads in the pre-edit manifest had hashes:

- `knowledge/foundations/sources.jsonl`: `192cb2c29847ab9a174f39e99654a8d8a4f6ba0f89b143df54a253d324105d2f`
- `knowledge/discriminators/sources.jsonl`: `bbc8749deb19e4a2e7f71540a1c034a6aaeb7168ab12d645b602704e556048b6`

After edits:

- `knowledge/foundations/sources.jsonl`: `525de88378fb037a4fa6bfd895f31e394423c6d9df790ea0a609c09a8ab5ea34`
- `knowledge/discriminators/sources.jsonl`: `fe88ed01506005770b1be800fe5dec53c22ae4d56ba356a0b106a30ec3c4f5c4`

`python3 scripts/check_sources.py --strict knowledge/foundations/sources.jsonl knowledge/discriminators/sources.jsonl` passed: 2 files, 25 records, 0 errors/warnings/info. JSONL parsing and required reading-history/snapshot-reference assertions passed for all six changed records; `found-stein-1968` remained unchanged.

A read-only global strict scan, `python3 scripts/check_sources.py --strict knowledge research`, returned 2 errors, 0 warnings: duplicate IDs `frontier-qrf-beyond-subsystems-2026` and `frontier-relativistic-trinity-2020v1` across `knowledge/frontier/sources.jsonl` and `knowledge/sector-conditioning/sources.jsonl`. These active, unassigned registers were not edited. The rest of that scan reported 24 files / 317 records.

## Limitations and unresolved decisions

- Malament's propositions were read from the published scan at statement/argument level; I did not independently reproduce the proofs or formalize them. The observer/causal-theory bridge remains philosophical and conditional.
- Putnam's summary follows the second-pass source audit. The reader name for both historical passes is not present in the artifact, so the provenance identifies those audits without inventing a person.
- Brading's copy matches published pagination and metadata but was not collated with a publisher-hosted file. The two distinct source IDs remain separate pending the coordinator's alias registry decision.
- Stein 1968 remains a discovery-only lead. Stein 1991's OCR theorem/context and printed-page caveat remain explicit.
- No accepted audit snapshot, historical proposed-record file, source alias registry, active literature lane, or task board state was changed. No commits were made.
