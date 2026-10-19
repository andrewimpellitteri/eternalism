# Pilot design: defect-injection evaluation of the handoff/audit pipeline

Status: proposal only, 2026-10-19. This task launches no agents and runs no
paid jobs. The pilot needs a coordinator-created workboard task (suggested id
`pilot-semantic-audit`, `owns: research/pilot-semantic-audit/`, blocked by this
task) before any run. Everything below is specified so that a reviewer can
attack the design before it is built.

## 1. Question the pilot answers

Does the handoff contract + semantic-audit procedure of `handoff-contract.md`
catch seeded, ground-truth-labeled semantic defects in physics translations —
without flagging correct translations — at small scale?

Success is measured against labeled defects and clean items. Agent agreement,
review-round counts, and report fluency are recorded but are explicitly not
success metrics.

## 2. Target material (known answers exist in public sources)

Family A — 1905 kinematics (primary):

- Source: Einstein, "On the Electrodynamics of Moving Bodies", 1923 Methuen
  translation via fourmilab.ch (seed-einstein-1905). Read depth available:
  the station/clock synchronization argument and the kinematics section are
  public and short. Current seed depth is `discovery`; the pilot's extractor
  must first raise it to `full-text` and record locators.
- Known-answer lemmas: (A1) the Lorentz transformation for frames in standard
  configuration; (A2) invariance of the interval / speed of light under (A1);
  (A3) moving-clock time dilation with the standard convention; (A4) the
  two-clock simultaneity argument (order reversal possible for spacelike
  separation, preserved order for timelike).

Family B — Page–Wootters conditional dynamics (stretch; only if Family A
concludes early):

- Sources: the seed anchors seed-qrf-proper-times, seed-temporal-measurements,
  frontier-page-wootters-measurements-2023 (abstracts; full-text read required
  before use), plus the original Page–Wootters construction as cited by them.
- Known answer: with a history state satisfying the constraint (H_S + H_C)|Ψ⟩=0,
  clock-conditioned system probabilities follow the Schrödinger evolution
  induced by H_S. The exact statement must be extracted from the pinned source,
  not from memory; if the anchors disagree on idealizations, that disagreement
  is itself recorded in `divergences`.

Both families are finite, computable, and have known wrong answers — the
preconditions for adversarial evaluation.

## 3. Artifact set

For each family, the pilot builds:

- E: one extraction record per source (role: extractor), full provenance.
- T0: one correct translation map (the known-answer artifact), produced from E
  following `handoff-contract.md` §2.2.
- D1..D8, three instances per class (different loci, e.g. different equations
  or assumptions): defective variants of T0, each injecting exactly one ground-
  truth defect. Family A has seven classes (D2 in its Family A form), Family B
  eight. Instances of one class are independent samples; repeated runs of one
  artifact are not. Labels live in a separate manifest (`labels.jsonl`, produced by
  the defect injector role and not given to the auditor).

The same translator prompt produces T0 and all D-variants; the injector applies
defects by editing the artifact text (equations, assumption entries,
convention sheet), so translation-quality variance does not confound the
defect signal.

## 4. Defect suite (each anchored to the taxonomy in prior-methods.md §3)

| ID | Injected defect | Taxonomy | Manifest label |
|---|---|---|---|
| D1 | Sign flip in the boost parameter (or in ω for Family B), convention sheet left unchanged | F4 | `defect:sign-convention` |
| D2 | Missing assumption. Family A: omit the isotropy/reciprocity assumption from the clock-synchronization prescription while still using it downstream. Family B: drop the constraint (H_S+H_C)|Ψ⟩=0 from the conditioning prescription | F5 | `defect:missing-assumption` |
| D3 | Overclaim: A4 stated for all inertial frames, derived only for standard-configuration boosts along one axis (claim stronger than derivation; the inverse of F1's weakened formal statement, so tagged F1′) | F1′ | `defect:overclaimed-scope` |
| D4 | Vacuous hypothesis: "synchronized" defined by a condition any two clocks satisfy (e.g., an existential with no constraint) | F2 | `defect:vacuous-hypothesis` |
| D5 | First-order-in-v/c expansion presented as exact time dilation | F3 | `defect:approximation-as-exact` |
| D6 | Silent branch: take the positive root of the quadratic where two branches exist, alternatives unrecorded | F6 | `defect:silent-branch` |
| D7 | Edge case: claim stated for all relative speeds 0≤v without excluding v=c degenerate handling | F9 | `defect:edge-case` |
| D8 | Untraceable equation: one equation inserted with no source_id/locator (a plausible but non-cited form) | F8 | `defect:untraceable` |

Two clean controls round out the set: T0 itself, and T0 with one assumption
correctly re-classified from `physical-premise` to `bridge-premise` with the
same content (a legitimate editorial change that must not be flagged).

## 5. Evaluation protocol

1. Blind run: the audit pipeline (reviewer role per `handoff-contract.md` §4,
   with the counterexample role on D-variants) processes the shuffled artifact
   set. Labels withheld.
2. Scoring against the manifest:
   - Per-class detection recall: fraction of Dk artifacts flagged as defective,
     by class. Report per class, not only aggregate.
   - Localization accuracy: does the finding point at the defect's locus (the
     exact equation/assumption/convention entry)?
   - False-accusation rate on clean items (T0, re-classified T0): must be zero
     for a passing pilot; any hit is reported as a finding against the
     procedure, not buried.
   - Provenance completeness: fraction of findings that cite artifact item +
     source ID + locator.
3. Baselines, each run identically and blind:
   - B0 translator only (no audit): upper-bounds how many defects survive
     without the pipeline.
   - B1 single-model self-check (same model reviews its own artifact):
     expected weak on D3/D4/D5 per primary-source evidence; measures the
     uplift of role separation.
   - B2 kernel/oracle-only where applicable: for Family A, a symbolic check of
     the algebra. Hypothesis, not premise: it should pass D3 and D7 (the algebra
     is fine, the claim's scope or domain is wrong) and may well catch D5, since
     a first-order expansion differs from the exact formula. Report what it
     actually catches; the point is that compile-or-compute success ≠
     correspondence.
4. Repetition: 3 runs per artifact (different seeds/orderings) to measure
   stability. Per-class recall is computed over the three instances per class
   (first-run verdicts), and run-to-run flips are reported separately as an
   instability rate. Report ranges, not single numbers.

## 5.1 Pass criteria (decided before the run)

- Per-class recall ≥ 2/3 instances in at least 6 of the classes run (Family A:
  6 of 7; both families: 6 of 8 classes), including at minimum
  `missing-assumption` (D2) and `untraceable` (D8), the two classes that
  motivate the whole design. Instability (verdict flips across runs) is
  reported and counts against a class that is only intermittently detected.
- Zero false accusations on both clean controls across all runs.
- 100% provenance completeness on findings (C1/C5 of the contract).
- Any class detected in < 2/3 instances is listed with a diagnosis (missing probe,
  shared-model blindness, artifact ambiguity).

## 5.2 Anti-goals

- Agreement between roles/models is logged but never scored; a pipeline whose
  findings correlate with reviewer-translator agreement rather than with
  manifest labels has failed by this design.
- No metric rewards verbosity, confidence, or number of review rounds.

## 6. Scale and cost bounds (for the coordinator's go/no-go)

- Artifacts: Family A = 1 clean + 7 classes × 3 instances + 1 control = 23
  artifacts; Family B = 26. Family A alone is the minimum viable pilot.
- Model calls: per artifact per run ≈ 1 audit + 1 counterexample + 1 B1
  self-check (B0 and B2 need no extra audit call). Family A: 23 × 3 runs × 3 ≈
  210 calls; both families ≈ 450. Small context each, but the coordinator should
  approve the actual number, not the earlier smaller estimate. No Lean build required for
  Family A; Family B may use a ≤ 100-line numeric check (separate engine,
  anchors per Douglas practice) instead of a kernel build.
- Wall-clock: sized for one workboard task; no large runs, no dependency
  installs (Python standard library numeric check only, consistent with repo
  policy).

## 7. Known limitations of the design (stated up front)

- Contamination: Einstein 1905 and the Lorentz transformation are in every
  model's training data, so a model may reproduce the "known answer" from memory
  and the pilot would then test recall rather than fidelity to the extraction
  record. Mitigations to build in: auditors work only from the pinned extraction
  and artifact (no recollection-based pass); Family A translations use
  disguised notation and conventions (nonstandard symbols, c ≠ 1, rapidity
  parametrization) so memorized forms do not match; and Family B, which is less
  memorized, is not optional for any claim beyond "catches textbook defects".
- Cross-model run: pre-register that a run with auditor and injector from
  different model families is the intended follow-up; until then every report
  states that roles share a model family.

- Injected defects are synthetic; real translation failures are noisier and
  may combine classes. The suite bounds what the pilot can show: behavior on
  these classes only.
- Same-model roles share blind spots (NOVELTY.md; prior-methods §3): detection
  of F1/F2-class defects may be inflated by the injector using the same model
  family's blind spots as a template. Cross-model runs are desirable; if only
  one model is authorized, the limitation is recorded in every report.
- Family A is special relativity with unusually crisp known answers; passing
  there does not validate the pipeline on interpretive disputes (candidate A/D
  material), where "known answer" may not exist.
- Three runs are enough to expose gross instability, not to estimate rates
  precisely.

## 8. Proposed workboard entry (for the coordinator; not edited by this task)

```json
{"id":"pilot-semantic-audit","title":"Run the defect-injection pilot for the semantic-audit pipeline","priority":8,
 "blocked_by":["kb-agent-methods"],
 "owns":["research/pilot-semantic-audit/"],
 "brief":"Execute knowledge/methods/pilot-design.md on Family A (and Family B if time allows). Blind labels, baselines B0-B2, pass criteria as specified. No new dependencies.",
 "done_when":["Per-class detection table and confusion data committed","Clean-control false-accusation rate reported","Failures diagnosed per class","AGENT_REPORT.md records all runs, seeds, and model IDs"]}
```
