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
- Known-answer lemmas, with locators checked against the 1923 translation
  (Part I, "Kinematical Part"; equations read from the page's image alt text,
  the German original and the equation images not viewed):
  - (A1) Lorentz transformation, standard configuration: Part I §3, final display
    (τ = β(t − vx/c²), ξ = β(x − vt), η = y, ζ = z, β = 1/√(1 − v²/c²)). Derived
    in the source from linearity ("homogeneity of space and time"), reciprocity
    φ(v)φ(−v) = 1 and symmetry φ(v) = φ(−v). These are additional premises a
    defect could target.
  - (A2) Present only as light-cone (null wave) invariance: Part I §3, spherical
    wave x²+y²+z² = c²t² ⇒ ξ²+η²+ζ² = c²τ², "after a simple calculation". The
    general interval invariance for non-null separations is **not stated in
    1905**; if the pilot needs it, it is a derived extension to be proved, not a
    source lemma.
  - (A3) Moving-clock dilation: Part I §4. The text gives the exact form
    τ = t√(1−v²/c²), "slow by 1 − √(1−v²/c²) seconds per second", and then
    "neglecting magnitudes of fourth and higher order" the approximation ½v²/c².
  - (A4) Order reversal for spacelike and preservation for timelike pairs is
    **not in the 1905 text** (no hits for spacelike, timelike, order, precede).
    Relativity of simultaneity is stated in §2 only. A4 is a corollary of the §3
    time equation Δτ = β(Δt − vΔx/c²). It is reclassified as a derived corollary
    the pilot must prove; a baseline "reproduction" of A4 from this source is not
    available, and no outside source for it has been verified here.
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

- E: one extraction record per source (role: extractor), full provenance. The
  extractor lists the assumptions the source actually uses, including implicit
  ones it can locate; defects may only remove or alter items present in E.
- T0: one translation map produced from E per `handoff-contract.md` §2.2, then
  **verified clean before the run** (symbolic check of equations plus sign-off by
  a second reader from a different model family or the coordinator). A flag on a
  verified-clean T0 is a false accusation; a flag on an unverified T0 would be
  ambiguous, so T0 is not used until verified.
- Defective variants, three instances per class at different loci, each
  injecting exactly one ground-truth defect. The three instances share one T0,
  one injector, and one model family, so they are **not independent samples**;
  they reduce locus-specific luck, not model-level correlation.
- Clean items, about two per defective item pair (target ratio ≥ 1:2 clean to
  defective, so a flag-everything auditor is exposed):
  - T0 itself;
  - edited-but-clean variants: cosmetic edits at the same loci by the same
    injector (rewording, renaming, reordering), so edit footprints are not a
    label;
  - a true bridge-premise control: an explicitly ontological premise (for
    example, eternalism or a privileged foliation) correctly typed
    `bridge-premise` and not used as derived (must not be flagged).
- Labels live in a separate manifest (`labels.jsonl`). Each defect has a
  written justification, source locator, and second-reader sign-off before the
  blind run; the injector's own description of its edit is not the authority.
- All artifacts pass through one formatter and are audited in a fresh, isolated
  context each, with no shared context that would let an auditor diff variants.
- Injector and auditor are from different model families wherever both families
  are available (AGENTS.md authorizes OpenCode GLM and native Luna runs); some
  injections are scripted or manual. Same-family runs are labeled as such in
  every report.

## 4. Defect suite

Classes are tagged with the taxonomy of `prior-methods.md` §3 where one applies.
Class F1′ (overclaim: a claim stronger than its derivation) is introduced here
and is not in that taxonomy; it is a proposed extension, not an anchored class.

### Tier 1 — generic translation defects

| ID | Injected defect (respecified) | Taxonomy | Label |
|---|---|---|---|
| D1 | Convention-sheet inconsistency: the boost-direction convention is declared in the sheet but the equations use the opposite one. A consistent global sign flip is a relabeling, not a defect, and is a clean control. | F4 (as sheet-versus-equation inconsistency) | `defect:convention-inconsistency` |
| D2 | Missing assumption: remove an assumption that E lists (Family A: Part I §1 states by definition that light takes equal time A→B and B→A, plus symmetry, transitivity and freedom from contradiction as assumptions, all of which E must list; note the §3 derivation uses speeds c−v and c+v in K, so removing isotropy changes the derivation, not only the definition. Family B: the constraint (H_S+H_C)\|Ψ⟩=0) while it is still used downstream | F5 | `defect:missing-assumption` |
| D3 | Overclaim: a lemma stated for all inertial frames but derived only for standard configuration. Valid only if the pinned derivation really is narrow; the lemma may be true more generally, so the defect is the derivation gap, not falsity | F1′ | `defect:overclaimed-scope` |
| D4 | Vacuous hypothesis: "synchronized" defined by a condition any two clocks satisfy | F2 | `defect:vacuous-hypothesis` |
| D5 | Truncation presented as exact: the source's own labelled approximation (Part I §4, ½v²/c² "neglecting magnitudes of fourth and higher order") restated as the exact dilation. (A "first order in v/c" version is ill-defined, since γ's first-order term is 1.) | F3 | `defect:truncation-as-exact` |
| D6 | Silent branch. The 1905 time-dilation derivation has no quadratic or two-branch choice. The only implicit selections are φ = +1 from φ² = 1 (§3, excluded without comment) and the positive root in β. D6 is available for Family A only if anchored at one of these and labeled implicit in the source; otherwise dropped | F6 | `defect:silent-branch` |
| D7 | Edge case: claim stated for 0 ≤ v without handling v = c. The source addresses v = c only through the §4 contraction remark ("For v = c all moving objects ... shrivel up into plane figures"; speeds above c "meaningless") and the §5 and §10 limits; |v| < c is an inherited, implicit domain, not a stated exclusion | F9 | `defect:edge-case` |
| D8 | Untraceable item: an equation inserted with no source ID or locator | F8 | `defect:untraceable` |

### Tier 2 — time-specific defects (none of these is a mechanical check)

| ID | Injected defect | Why it matters here |
|---|---|---|
| D9 | A bridge premise presented as physical or derived (for example, "relativity of simultaneity implies all events are equally real" stated as a consequence) | AGENTS.md: a definition assuming eternalism cannot establish it; contract C2 |
| D10 | Causal order conflated with temporal ontology or objective passage | AGENTS.md distinction |
| D11 | Hidden global foliation or preferred frame ("the present") inside the synchronization prescription | The standard hidden premise in Rietdijk–Putnam-style arguments |
| D12 | Coordinate time swapped for proper time (t ↔ τ) in the dilation statement | Clock time vs coordinate time |
| D13 | A synchronization convention treated as a physical fact | Conventionality of simultaneity |
| D14 | An observable-preserving map restated as "ontologically equivalent" or "gauge" | AGENTS.md: a representation transformation is not automatically an ontological equivalence |
| D15 | A premise typed with the wrong `kind` (for example a bridge premise labeled physical) | Contract R1/C2. This replaces the earlier "reclassified control", which would have been a defect, not a clean item |

D10–D15 depend on a source passage that supports them; a class is dropped for a
family if its pinned source gives no honest locus. Disguised notation (nonstandard
symbols, c ≠ 1, rapidity) is a representation change: it never changes an item's
label, and "preserves observables" is never scored as ontological equivalence.

**Minimum viable pilot (Family A):** D1, D2, D3, D4, D5, D7, D8 plus D9, D11,
D14 (and D6 if the source supports it) = 10 classes, 30 defective artifacts,
at least 15 clean artifacts, about 45 total. Preconditions, each to be pinned
with a locator before the run: A1 and A3 are source lemmas (§3, §4); A2 only as
null-cone invariance; A4 is not a source lemma and is excluded from the
known-answer set unless proved by the pilot or cited to a verified outside
source; D6 needs an anchored implicit selection or is dropped; and each defect
removes or alters something present in E.

## 5. Evaluation protocol

1. Blind run: the audit pipeline (reviewer role, with the counterexample role,
   per `handoff-contract.md` §4) processes the shuffled set, one artifact per
   fresh context. Labels withheld.
2. **Detection** is defined, not assumed: a finding of severity ≥ major whose
   cited artifact item matches the manifest locus. A flag at the wrong locus is
   a miss for that defect and, if the item is clean, a false accusation. The
   verdict statuses of the contract (§4) map to "flagged" if any per-question
   status is `defect` at severity ≥ major.
3. Scoring: per-class instance recall; locus-match rate; false-accusation rate on
   clean items with an exact 95% upper bound; finding provenance (below);
   instability (verdict flips across the 3 runs).
4. **Finding provenance** means each finding cites the artifact item it concerns
   (or, for a missing item such as D2 and D8, the expected locus) plus the
   source locator where it is used or required. This is separate from contract
   C1/C5 (artifact-level provenance). For D2 and D8 the "source locator" is the
   expected one and is not required to exist.
5. Baselines, each run blind with identical scoring:
   - Null-1: flag-everything. Null-2: random flagging at the defect base rate.
     These bound what an uninformative auditor scores (flag-all gets full recall
     and is exposed only by clean items, hence the ≥ 1:2 clean ratio).
   - B1′: one model call, same checklist as the pipeline. B1″: same number of
     calls as the pipeline, same model, no role separation. Together they isolate
     role separation from checklist content and call count.
   - B2: schema/lint plus symbolic algebra check, no model. Pre-stated prediction:
     it catches D1 (sheet vs equations), D5, D7, D8 and nothing of D3, D4,
     D9–D15. Report what it actually catches; the lint-only share of the
     pipeline's detections is reported separately so the semantic contribution is
     visible.
   - No-extraction condition: the auditor sees the artifact without E. Its
     detection of D1/D5/D12 measures detection from memorized physics, which
     bounds contamination.
6. Repetition: three runs per artifact to measure stability. A defect counts as
   detected if flagged with locus match in at least 2 of the 3 runs.

## 5.1 Pass criteria (decided before the run; this is a smoke test)

The pilot can show gross failure or gross success on these classes. It cannot
certify the pipeline: n is small, instances are correlated, and zero false
accusations in about 15 clean items only bounds the rate below roughly 18% at
95%. Reports use the word "smoke test", never "validation".

- At least 7 of the 10 minimum-viable classes have ≥ 2 of 3 instances detected,
  and every required class (D2, D8, D9, D11, D14) does.
- No major false accusation on T0 or the true bridge-premise control in any
  run; the overall clean false-accusation point rate is ≤ 1/15, reported with
  its upper bound.
- Pooled instance recall beats both B1′ and B1″ by at least 20 percentage
  points. A pipeline that does no better than a single checklist call fails,
  whatever its absolute recall.
- Finding provenance as defined in §5 item 4: 100% of findings.
- Any class below threshold is listed with a diagnosis (missing probe, shared-
  model blindness, artifact ambiguity, ambiguous label).

## 5.2 Anti-goals

- Agreement between roles/models is logged but never scored. A pipeline whose
  findings correlate with reviewer–translator agreement rather than manifest
  labels has failed by this design.
- No metric rewards verbosity, confidence, or number of review rounds.
- No verdict of "ontologically equivalent" is ever scored as correct; D14 tests
  that the auditor refuses it.

## 6. Scale, cost, and who drives it

- Artifacts: about 45 (Family A minimum viable set).
- Model calls: pipeline ≈ 2 per artifact per run (audit + counterexample),
  B1′ 1, B1″ matched to the pipeline, no-extraction condition 1. Full design:
  45 artifacts × 3 runs × roughly 6 calls ≈ 800. A screening version (one run of
  everything, repeats only for artifacts flagged or missed) is ≈ 270. The
  coordinator chooses the version and the number before any launch.
- No Lean build for Family A. A Family B numeric check, if used, is a short
  standard-library Python script.
- **Driver:** a coordinator-run, scripted standard-library driver issues the
  role calls and records model IDs and seeds. A worker agent does not launch the
  role agents itself (AGENTS.md: workers do not launch agents).
- Claims are scoped to Family A. Family B is a stretch; its anchors are
  abstract-depth and must be read in full before any Family B result is reported.

## 7. Known limitations of the design (stated up front)

- Contamination: Einstein 1905 and the Lorentz transformation are in every
  model's training data, so a model may reproduce the "known answer" from memory.
  Disguised notation helps but does not enforce extraction-only reasoning; the
  no-extraction condition (§5) measures how much detection survives without E,
  and that number is reported beside every result. Family A can only support
  claims of the form "catches textbook-physics defects"; it says nothing about
  less-memorized or interpretive material.
- Cross-model injection and auditing is the primary design (§3), not a
  follow-up. A run where both roles share a model family is labeled as such.

- Injected defects are synthetic; real translation failures are noisier and
  may combine classes. The suite bounds what the pilot can show: behavior on
  these classes only.
- Same-model roles share blind spots (NOVELTY.md; prior-methods §3): an LLM
  injector may produce defects shaped like what an LLM auditor already
  recognizes. Cross-family injection and some scripted or manual injections are
  the mitigation, not a cure.
- Ground-truth labels are the weakest link: several defects (D1, D3, D5, D13)
  are physically arguable unless pinned to a source locator and signed off by a
  second reader. A disputed label is excluded and reported, not scored.
- Family A is special relativity with unusually crisp known answers; passing
  there does not validate the pipeline on interpretive disputes (candidate A/D
  material), where "known answer" may not exist.
- Three runs are enough to expose gross instability, not to estimate rates.
  With 3 instances and a 2-of-3 threshold, a class whose true detection
  probability is 0.5 passes half the time; results are reported as intervals.

## 8. Proposed workboard entry (for the coordinator; not edited by this task)

```json
{"id":"pilot-semantic-audit","title":"Run the defect-injection pilot for the semantic-audit pipeline","priority":8,
 "blocked_by":["kb-agent-methods"],
 "owns":["research/pilot-semantic-audit/"],
 "brief":"Execute knowledge/methods/pilot-design.md on Family A only: verify T0 and all labels first, then run the blind audit with null baselines, B1prime, B1double-prime, B2 and the no-extraction condition via a coordinator-run stdlib driver. Pass criteria as specified; report as a smoke test. No new dependencies.",
 "done_when":["Per-class detection table and confusion data committed","Clean-item false-accusation rate with upper bound reported","Label justifications and second-reader sign-offs committed before the blind run","Failures diagnosed per class","AGENT_REPORT.md records all runs, seeds, and model IDs"]}
```
