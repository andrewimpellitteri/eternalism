# Repair log: point-by-point response to the coordinator findings

29 October 2026. Lane `ontology-bridges-repair`. Each item cites the finding
and states exactly what was changed, where, and on what evidence. Sections
refer to [RESULT.md](RESULT.md) unless noted. The predecessor submission
([RESULT.md of `ontology-bridge-premises`](../../bridges/RESULT.md) — a
final-layout link; the file itself sits in the preserved predecessor worktree
at pinned commit `c15901c3197044c557dc968ffd5e6851f61e283b`) is preserved
unmodified in
its own worktree; only relevant material was copied or adapted into this lane.

## 1. BATCH1_INITIAL_REVIEW §2, paragraph 1 — "Section 1.3 goes too far in saying physical supervenience cannot be stated neutrally"

**Finding.** One can stipulate a physical model as a representational reduct,
add a distinct existence predicate, and ask whether all admissible expansions
agree on the predicate. That is a substantive uniqueness premise, not formally
circular.

**Repair.** Accepted in full; the blanket claim is retracted. RESULT §1 now
states the neutral framework explicitly: representational reduct (§1.1),
separate existence predicate (§1.2), admissible class defined by structural
constraints A1–A4 with no use of concrete existence (§1.3), and the exact
premises SU (global supervenience, Kim-style) and UNIQ (uniqueness of the
existence function) with their logical relationship (§1.4). The finite
witnesses implement exactly this discipline: the program's docstring and
structure enforce that only predicates on representational labels are
computed (§7).

**Residual scope.** The one formulation that *is* logically circular —
defining "physical facts" as the tenseless-total inventory and concluding that
the tenseless-total inventory is the concrete one — is retained, but only as
one avoidable variant in the four-mode taxonomy (RESULT §2, table row 3); it
no longer carries a verdict about supervenience as such.

## 2. BATCH1_INITIAL_REVIEW §2, paragraph 2 — "Nor do the two alternatives E_all and E_past refute supervenience outright"

**Finding.** Each defines a different supervenience function within its own
model class; they show the shared structural requirements do not determine
which function is correct. A class admitting both violates uniqueness, while a
rival asserting supervenience may reject precisely that class. Repair the
verdict to "the physics considered here does not entail or uniquely specify
this bridge"; reserve "circular" for an argument that actually assumes its
desired existence conclusion.

**Repair.** RESULT §1.4–§1.5 is the point-by-point replacement:

- The repaired verdict sentence appears verbatim in §1.4.
- §1.5 states exactly what the coexistence refutes (the entailment of UNIQ by
  the shared constraints; the availability of a neutral selection theorem) and
  what it does not refute (SU itself — each one-expansion class satisfies it;
  either candidate individually; the rational permissibility of either rival).
- §3.3 repairs the charitable-rival treatment: the Stein-style and C&R rivals
  are now presented as rivals who accept supervenience *inside their own
  classes* and reject the plural class, not as parties refuted by the
  coexistence observation.
- The "class admitting both expansions violates uniqueness" structure is
  machine-checked: W1 counts 6 families under the shared constraints, and
  exactly 1 under each rival's added selector (RESULT §7).
- The question-begging direction is also flagged: using the coexistence
  observation *against a supervenience-asserting rival* assumes the plural
  admissibility the rival denies (RESULT §2, table row 4).

## 3. BATCH1_INITIAL_REVIEW §2, paragraph 3 — "the clipped-spacetime example establishes a failure of inference from matched past information to equal future lifetime" and no more

**Finding.** It does not by itself show that completeness has no observational
or predictive content under every protocol or comparison class.

**Repair.** Accepted; the overclaim is retracted and replaced by an exact
two-protocol statement (RESULT §4.2–§4.3):

- P1 (matched-past protocol, comparison class {clipped Minkowski, full
  Minkowski}, access strictly below the shorter lifetime): records identical,
  lifetimes differ — matched past records do not determine future lifetime.
  This is the reviewed sharpness example at its exact scope
  ([COMMON_EXTENSION_REPAIR](../../../lawful-completions/coordinator/COMMON_EXTENSION_REPAIR.md)).
- P2 (future-inclusive protocol, same class): the hypotheses differ in what a
  persisting observer records at durations ≥ T; completeness hypotheses have
  predictive content and are decidable, if at all, only in time.
- Discrete protocol surrogate W5 machine-checks the protocol logic (§7).
- Predecessor §2.5's "completeness is not a predictive or observable
  property" is retracted in so many words (RESULT §4.3, second bullet).

## 4. BATCH2_RUN_PLAN row 2 — "Reconstruct substantive noncircular supervenience and constitution bridges, preserve rival objections, defend one positive route with explicit defeaters"

**Repair.**

- Three bridges reconstructed with premises separated by category, primary
  support at recorded depths, charitable rival rejections, and one retained
  noncircular premise each: A′ (RESULT §3, retained: invariance + determinacy
  + UNIQ-as-claim), B′ (RESULT §4, retained: B′1 mathematics + B′2
  representation; B′3 isolated as a contestable noncircular philosophical
  premise), C′ (RESULT §5, restated as a methodological constraint with its
  exact scope, never a selector).
- The Putnam argument's failure is now diagnosed as valid-but-unsound (false
  conjunct of the R-premise) rather than circular (RESULT §3.2), with the
  FLRW category-relativity caveat retained.
- One positive route selected: standpoint-indexed supervenience (the Stein
  route), RESULT §6, with a four-step independent justification whose step 4
  (record-bearing explanatory tie-break) is the substantive retained premise,
  and four explicit defeaters — including one exact, project-internal defeater
  built on the coordinator-reviewed closed-dust mass classification
  (`F_m(b) = M` for `π ≤ τ < 2π`,
  [REVIEW_STATUS](../../../horizons/mass-classification/REVIEW_STATUS.md),
  accepted research scope, not externally refereed).
- The symmetric anchoring requirement is explicitly labeled a proposed
  methodological constraint, not a selection theorem (RESULT §5.1).

## 5. Brief bullets — remaining specific obligations

- **"Physical representation of future events does not by itself assume
  concrete future existence."** RESULT §1.1–§1.2 (reduct + separate
  predicate); the witnesses compute only predicates on labels.
- **"State a genuinely neutral physical reduct and separate existence
  predicate, an explicit admissible world/model class, and the exact
  supervenience/uniqueness premise."** RESULT §1.1–§1.4.
- **"Distinguish nonentailment, false premise, question-begging inference and
  logical circularity."** RESULT §2 (stipulative definitions + application
  table).
- **"E_all and E_past individually supply different functions; explain what
  their coexistence does and does not refute."** RESULT §1.5 (three refutes,
  three does-not-refutes).
- **"Repair the clipped-Minkowski overclaim."** RESULT §4.2–§4.3; item 3
  above.
- **"Reconstruct the strongest three bridge arguments with primary support
  and charitable rival rejections, retaining rather than dismissing a
  substantive noncircular premise when defensible."** RESULT §§3–5; retained
  premises flagged in each; the predecessor's anchor-inventory is preserved
  (all predecessor sources re-registered in
  [sources.jsonl](sources.jsonl) as project records at recorded depths).
- **"Select one best positive route … independent justification and what
  rival explanation would defeat it."** RESULT §6 (steps 1–4; defeaters 1–4;
  defeater 1 is exact and uses a reviewed internal result at its recorded
  status).
- **"A symmetric anchoring requirement is a proposed methodological
  constraint, not a selection theorem."** RESULT §5.1 (stated as such).
- **"Give at least one exact small model or premise table that distinguishes
  the rival readings without taking the model domain as already concrete."**
  RESULT §5.3 + §7 (W1–W4 premise tables; domain-as-concrete prohibition
  enforced in the program's design and docstring).
- **"Keep empirical access, ontological supervenience, grounding and
  dynamical determination separate."** RESULT §8 (four-way table), plus
  category labels on every premise in §§3–6.
- **Checking-program constraints** (explicit finite witnesses, standard
  library, bounded sizes, < 10 s per check / ≤ 15 s hard timeout / ≤ 30 s
  total; no dense-grid expansion): RESULT §7 (0.72 s; sizes ≤ 4 elements;
  enumeration ≤ 65 536 families; no timed-out search was rerun or enlarged —
  this lane never had one).

## 6. New contrary evidence incorporated (search yield)

The predecessor's Bridge C rested on Malament 1977 at abstract depth with no
scope caveats. This session's search surfaced and registered the contrary
primary literature on what the definability result establishes: Rynasiewicz
2001 (abstract + opening section read via exa) and Sarkar–Stachel 1999
(metadata only, honestly labeled). RESULT §5.2 now states the definability
results at their disputed philosophical import: they filter candidates within
a structure; they do not settle interpretive questions. Kim 1984/1987
(metadata) anchor the global-supervenience terminology used in §1.4.

## 7. What was intentionally not changed

- The predecessor's Bridge C taxonomy and cost accounting (Pooley §VII
  routes; Wüthrich–Callender dilemma) — retained with unchanged verdicts in
  kind, sharpened in scope (RESULT §5.4–§5.5).
- All predecessor source records and their depths — re-registered, not
  upgraded. No source moved from abstract to full-text by assertion; the only
  new above-abstract read this session is Rynasiewicz 2001 (partial).
- The predecessor's enforced-distinctions table (its §4) — subsumed and
  extended by RESULT §8.

## 8. Blockers and open items for the coordinator

1. The positive route's step-4 tie-break (record-bearing vs determination) is
   stated and motivated, not proven. Defeater 1 (RESULT §6.2) shows the two
   tie-breaks genuinely diverge on reviewed internal mathematics; choosing
   between them is a philosophical task this lane does not attempt to close.
2. The F_m mass-classification sidecar and the common-extension/sharpness
   results are used at their recorded *internal review* status; both remain
   pending external review, and any integration inherits that limit.
3. Kim 1984 is cited only for the taxonomy of supervenience forms at metadata
   depth; the formulation of SU/UNIQ is ours. A full-text check against Kim's
   exact definitions would be a cheap upgrade for the reviewer.
4. Malament 1977 remains unread in full in this lineage (two lanes now);
   Sarkar–Stachel 1999 is metadata-only. If the definability scope matters to
   integration, both should be read before any stronger claim is built on
   §5.2.
