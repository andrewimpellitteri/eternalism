# Triage of the rescued results against the paper

31 October 2026. Claude Code (Opus 5.5). This asks one question of each of the 33 rescued tasks in
the [review queue](../REVIEW_QUEUE.md): does it contradict or weaken something the paper claims?
It accepts nothing, and the board is unchanged. It is the same model family as the paper's assistant,
so it is not independent review.

Corrected the same evening. The first version missed coordinator reviews of three tasks, and it
miscounted the script repairs. The [coordinator's handoff](../lawful-completions/coordinator/central-history-audit/CLEANUP_HANDOFF.md)
raised most of these points, and the tables below now reflect them.

## Outcome

No theorem or proposition in the paper changed. One worker theorem is false, one attribution was
missing, and one script needed two repairs.

| Finding | Effect |
|---|---|
| `horizons-echo-exactness`: the stated fixed set is false | None on the paper, which proves the correct set. Result marked refuted |
| `screening-review`: its refutation of (L′) is wrong, as the owner handoff shows | None on the paper, which does not use (L′). Result marked |
| `ontology-persistence-priorart`: Bigaj 2008 has the same pair of realms | **Citation added** to Section `sec:realms` |
| `horizons-perturbation-referee`: its numerical control failed | Two script bugs, not a problem with `prop:mass`. Corrected copy passes |
| `stein-null-boundary-audit`: left a script and no report | Script passes. Status table updated |

## The refuted theorem

The worker's theorem counts a point as fixed if either optical coordinate lands in the fixed band.
The truth needs both. Step 2.3(ii) treats the echo of the past as all of `J⁻(b̂)`, but the echo holds
only after η = π, and step (iv) has the matching fault.

Exact zonal solutions settle it. On the unit S³, `ψ(η,r) = [G(η+r) − G(η−r)] / sin r` solves the
rescaled equation for every smooth 2π-periodic `G`. Choosing `G` to vanish on `[−τ, τ]` makes `ψ` vanish
on the past of `b`. At τ = 1, on a grid of 79,401 points, `ψ` is nonzero at 52,266 points the worker calls
fixed and at none inside the paper's diamonds. See [refutation_check.py](../horizons/glm/echo-exactness/refutation_check.py).

The worker's own script passes because it tests the comoving line, where the two sets agree. Its
claims on that line stand. A passing script here said nothing about the region where the theorem fails.

## The referee script

[check_referee_control.py](../horizons/glm/perturbation-referee/check_referee_control.py) is kept as
handed back. It has two bugs: RK4 stages 2–4 used the intermediate position as the velocity, and the
constant-δ section stepped the dust potential. Its comparison with π·h(Y) also assumed that two
sums truncate alike, and they do not.

[The corrected copy](../horizons/glm/perturbation-referee/check_referee_control_corrected.py) passes.
The stepper matches a closed form to about 2×10⁻⁹. That closed form and the spectral value both converge
to the exact π·h(Y) = 0.1172648, with the closed-form error falling from 3×10⁻⁵ at 48 modes to 6×10⁻⁹
at 384. The stepper also matches the operator identity for `w(T)` to about 10⁻¹⁰. At δ = −10⁻⁴ the sign
test fails at 96 modes because the truncation residual of 1.6×10⁻⁵ exceeds the signal of 1.2×10⁻⁵,
which is why the script asserts signs only at |δ| ≥ 10⁻³.

## All 33 tasks

Depth: **full** means the whole result was read. **Verdict** means the summary or verdict sections, or
a coordinator review of them. Depth is what this triage read, not what the worker read.

### Contains an error, now marked (2)

| Task | Depth | Disposition |
|---|---|---|
| `horizons-echo-exactness` | Full to step 2.3 | Refuted above |
| `screening-review` | Verdict | (L′) refutation wrong. Its other confirmations stand as worker claims |

### Rejected in part by the coordinator; the paper does not use the rejected part (15)

| Task | Depth | What was rejected | Paper |
|---|---|---|---|
| `lawful-completions-constraints` | Verdict | Lemma P's whole-past inference | Not used |
| `lawful-completions-priority` | Verdict | The kill verdicts for the exact target | Keeps Manchak and Geroch as known prior |
| `lawful-finite-cone-continuity` | Verdict | Theorem 2's false Grönwall step | Uses the [replacement proof](../lawful-completions/coordinator/COMPACTNESS_CONTINUITY_REPAIR.md), [accepted at finite-control scope](../lawful-completions/coordinator/FINITE_CONTROL_ACCEPTANCE.md). No uniform continuity is used |
| `lawful-central-history-review` | Verdict, plus [the audit](../lawful-completions/coordinator/central-history-audit/RESULT.md) §1 | Its assembly and smooth-input objections. The worker confused the fixed point with the smoothed profile. I checked that algebra | Unaffected: `thm:same-past` is finite. The whole-history theorem is not accepted either |
| `lawful-scalar-common-extension` | Verdict | The geometric audit | `thm:rigidity` works inside its class, where Σ is Cauchy by `lem:cones` |
| `ontology-modal-category-bridge` | Verdict | The anti-trivialization argument | Treats maximality as a choice, not a theorem |
| `ontology-constitutive-extent-test` | Verdict | The reconstruction dilemma | Not used |
| `ontology-constitutive-bridge-pilot` | Scope section, plus [the review](../agentic-philosophy/PILOT_REVIEW.md) | Premise P2 and the cessation test | Not used |
| `ontology-natural-assignments` | Verdict | Two scope errors and the census table | `prop:sp` has the corrected form |
| `ontology-equivalence-repair` | Verdict | Two textual errors and the same table | Not used |
| `ontology-bridges-repair` | Verdict | Reversed direction of fixing in §6.2 | Not used |
| `ontology-rivals-repair` | Verdict | Corrections kept, review still owed | Not used |
| `ontology-rival-contracts` | Heading only | Superseded by its repair | Not used directly |
| `ontology-bridge-premises` | Heading only | Superseded by its repair | Not used directly |
| `ontology-expansion-equivalence` | Verdict | Wrong `J⁻` definition; superseded by its repair | Not used directly |

### Supports the paper or leaves it unchanged (10)

| Task | Depth | Note |
|---|---|---|
| `stein-priority-audit` | Full | Its five suggested fixes are in the paper or the Stein source, apart from the printed Clifton–Hogarth pages |
| `stein-core-repairs` | Report | Both findings already repaired |
| `stein-interpretation-audit` | Heads and end | The mathematics survives. Wording repairs are in the paper |
| `stein-null-boundary-audit` | Script run | Passes. Status table updated |
| `horizons-echo-robustness` | Summary | Agrees with `prop:mass`. Its open question is closed by `thm:massive` |
| `horizons-perturbation-referee` | Full | Independent derivation agrees with `prop:mass`, with the limits it states |
| `horizons-scalar-priority` | Verdict | The paper uses Manchak's corrected theorem and not Geroch's printed claim |
| `ontology-null-refinements-review` | Verdict | The census verifies under its premises |
| `lawful-higher-regularity-audit` | Verdict | Kilgore does not upgrade the family. The paper does not use that route |
| `ontology-modal-density-search` | Via [the review](../agentic-philosophy/result-search-round1/modal-density-audit/WORKER_REVIEW.md) | The comb survives, with its offshoot calculation repaired. The paper's modal comb rests on that repaired form |

### Attribution (1)

| Task | Depth | Disposition |
|---|---|---|
| `ontology-persistence-priorart` | Verdict | Bigaj cited. The citation was checked against Crossref, which lists no author. The extraction is the worker's: printed pages are unverified, and the audit's own falsifier 2 asks whether "future light cone" means the timelike interior. Check the printed chapter before submission |

### No bearing on the paper's claims (5)

| Task | Depth | Note |
|---|---|---|
| `ontology-coordination-unity` | Summary | Operational contrast, no constitutive licence |
| `ontology-cycle-recovery-test` | Summary | Fits the paper's closed deductive route |
| `ontology-occurrence-warrant-search` | Via round disposition | The family stopped |
| `past-shadow-ltb-sources` | Verdict | Source locators for a lane the paper does not use |
| `prior-art-becoming` | Verdict table | No full predecessor at the depth read. Absence is not evidence of novelty |

## Scripts

All 16 rescued scripts were run with a 45-second limit. Fifteen passed and the referee script failed as
described. Most check only their own encodings, so a pass says little, as the echo case shows.

## Preservation and source records

The coordinator's [preservation audit](../lawful-completions/coordinator/central-history-audit/RESCUE_AUDIT.json)
compared 116 committed file occurrences across the 33 tasks. It found 112 identical, and four that
differ only in Markdown link destinations, which are the link repairs made during the rescue. That
comparison is bounded and does not cover every ignored file in every worktree.

`check_sources.py --strict` reports three errors in the `screening-review` register and one in the
`finite-cone-continuity` register, all missing fields or versions. The default run does not report
them. They are schema errors, not findings about the results, and they stay as handed back.

## Not done

- No rescued task is accepted, and only the coordinator-level reading above was done on most of them.
- Tasks marked verdict or heading depth could hold further errors that this triage did not see.
- The whole-history theorem remains unaccepted. It matters only if the paper ever claims whole
  central histories.
- The other tasks without sign-off, and their coordinator notes, were not triaged here.
