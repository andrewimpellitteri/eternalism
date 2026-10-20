# Cross-model semantic-audit pilot: protocol

2026-10-20, Claude coordinator. Stage 1 fixes the design in
`knowledge/methods/pilot-design.md`; Stage 2 is pre-registered here and was
committed **before** any auditor saw the items.

## Stage 1: the seven REVIEW_NOTES defects, point by point

`knowledge/REVIEW_NOTES.md` lists seven defects. The current `pilot-design.md`
was already revised after that review, so each is checked against the current
text, then fixed or carried here.

| # | Defect | Status in current `pilot-design.md` | Fix in this protocol |
|---|---|---|---|
| 1 | Pass criteria impossible: D2 only in Family B but required | **Fixed.** D2 is in the Family A minimum set (§4, synchronization assumptions), and every required class (D2, D8, D9, D11, D14) is in that set. Arithmetic: 10 classes × 3 instances = 30 defective, ≥15 clean; "≥7 of 10 classes at ≥2/3" is attainable. | None needed. |
| 2 | Contamination: Einstein 1905 is memorized | **Partly fixed.** Stated as a limitation, with a no-extraction condition to measure it. | Make the **primary** family less memorized: Family C (Stage 2 below) uses records of 2026 papers and real past record failures, which no model has memorized as "the answer". Keep Family A only as a contamination control. |
| 3 | D3 mislabelled F1 | **Fixed.** D3 is tagged F1′ (overclaim), a proposed extension. | None needed. |
| 4 | B2 predicted to pass D5 | **Fixed.** B2 is predicted to catch D5. | None needed. |
| 5 | One instance per class, so 2-of-3 runs measures stability | **Partly fixed.** Three instances per class, but they share one T0 and one injector. | In Family C, instances are real failures from **different lanes and papers**, so instances of one class are not edits of one artifact. Report per-class counts with n; no rates from n < 5. |
| 6 | Call budget 60–80 vs ~300 implied | **Fixed.** ≈800 full / ≈270 screening. | Stage 2 budget stated below (2 auditor sessions). |
| 7 | Same-family injector and auditor | **Partly fixed.** Cross-model is primary, but what a cross-model run adds is not pre-registered. | Pre-registered below: compare each auditor's detection on items produced by its own family against items from other families. A same-family blind spot shows up as lower detection on own-family items. Two auditors cannot establish independence. |

## Stage 2 (authorized by the user on 2026-10-20): Family C, record-metadata audit

**Items.** `items.jsonl`: 17 records, shuffled with seed 20261020 by
`build_stage2.py`. Each shows only title, authors, url and version. Labels are in
`labels.jsonl` and are not shown to auditors.

- 8 **defective**, all real past failures with documented ground truth:
  4 wrong identifiers (Stein 1968, Malament 1977, Deasy, Bisognano–Wichmann 1976),
  1 nonexistent source (the "Hawley 2009" record), 1 wrong venue and date
  (Lazarovici–Reichert), and 2 wrong authors (the "Kostelecký–Mewes" record; the
  Loriani record with 8 wrong given names, found while building this set).
- 9 **clean**, every field checked against Crossref or the arXiv listing on 2026-10-20.
- No paper appears twice, so an auditor cannot diff a defective version against a corrected one.

**Producer family per defective item.** GPT/Luna lanes produced R01, R02, R06 and
R14. The foundations baseline (R09, R10, R13, R15) has no recorded producer model.

**Auditors** (GLM is excluded: its quota was exhausted at 08:25 UTC):
- **GPT**: `codex exec`, one session over all 17 items, web access as configured.
- **Claude**: one general-purpose subagent session over all 17 items, with web access.

Both get the identical prompt in `auditor_prompt.md`. One session per auditor sees
all items. This departs from "one artifact per fresh context"; it is acceptable
here because each item is a different paper and no corrected twin is present.

**Mechanical baseline** (already run, `mechanical_baseline.txt`):
`check_sources.py --online` flags R06, R09, R10, R13 and R15 (5/5 identifier
defects), misses R01, R02 and R14, and flags no clean item.

**Scoring.**
- *Detection*: verdict `defect` on a defective item, naming at least one
  labelled field.
- *Field miss*: verdict `defect` on a defective item, naming only other fields.
  Reported separately; not a detection.
- *False flag*: verdict `defect` on a clean item.
- *Unverifiable*: reported separately; never counted as detection or false flag.

**Pre-registered criteria** (a smoke test; n is far too small for rates):
- An auditor **adds value over the mechanical check** if it detects ≥2 of the 3
  items the checker missed (R01, R02, R14) with ≤1 false flag among the 9 clean items.
- An auditor **fails as a gate** if it misses ≥3 of the 5 identifier defects the
  checker caught, or makes ≥2 false flags.
- Same-family comparison: report GPT's detection on the GPT-produced defective
  items (R01, R02, R06, R14) against Claude's on the same items. With n = 4 this
  can show a gross difference at most.

**Budget.** 2 auditor sessions, each with web lookups (about 17–50 fetches).
Actual usage is reported in AGENT_REPORT.md.
