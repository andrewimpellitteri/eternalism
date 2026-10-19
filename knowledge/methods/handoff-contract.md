# Specialist roles, handoff contract, and semantic-audit procedure

Status: design proposal, 2026-10-19, for this repository's agent workflow
(`scripts/agents.py` task board, GLM workers, isolated worktrees, reports
reviewed before acceptance). Grounded in `prior-methods.md`; every borrowed
mechanism cites its source record. This file proposes roles and artifacts only —
it launches nothing, and it does not modify the workboard.

## 1. Design requirements (from the audited failure modes)

- R1 Physics never hides: physical premises, mathematical definitions, and
  philosophical bridge premises are distinct record types with distinct audit
  duties (meth-sw-lean-2026 Sec. 2; project AGENTS.md research standards).
- R2 Every equation, assumption, and verdict carries provenance: source ID +
  exact locator + version. Untraceable items are defects, not style issues (F8).
- R3 Disagreements and failed attempts are first-class outputs, preserved in a
  divergence register (TNLean `docs/paper-gaps/` pattern; NOVELTY.md synthesis
  requirement).
- R4 Roles are separated by knowledge asymmetry, not just by prompt: the
  counterexample role must not receive the translator's rationale, or it will
  inherit and confirm the translator's blind spots (F1–F3 evidence).
- R5 No role may "accept" its own or a peer's output; acceptance is the
  coordinator's, after review (workboard contract).
- R6 Iteration loops have caps and no fresh-review-per-revision (TNLean App. D.3).

## 2. Specialist roles

Four specialist roles fit the existing one-task-one-worktree board. Each maps to
a workboard task with `owns` paths; each writes its lane's `sources.jsonl`
entries and an AGENT_REPORT.md per current practice.

### 2.1 Extractor (per source or per paper cluster)

- Input: one source (pinned version) from the seed or a lane's sources.jsonl,
  with a target read depth.
- Output: an extraction record — structured, quote-level, with fields defined in
  §3. Extracts equations verbatim with locators, names every assumption and
  classifies it (physical premise / mathematical definition / bridge premise /
  convention), records the paper's own stated limitations, disagreements with
  sibling sources, and failed attempts the authors report.
- Hard rules: no paraphrase from memory; anything not located in the text is
  recorded as an open question, never filled in; read depth is updated honestly
  (discovery → abstract → full-text) in the lane's sources.jsonl.
- Failure modes it prevents: F4, F8 at the entry point.

### 2.2 Translator (model-to-model or paper-to-model)

- Input: exactly two extraction records, or one extraction record plus one
  explicit target (a formal system such as a Lean signature, or a stated
  convention sheet and target notation for a single-source restatement). Never raw recollection; never
  another agent's summary in place of the extraction record.
- Output: a translation map with required sections:
  1. Dictionary table: each physical concept → mathematical object → source
     locator (Douglas's dictionary pattern, meth-sw-lean-2026 Sec. 4.1).
  2. State space, dynamics, causal structure, clock construction — per the
     knowledge/README.md theory-comparison contract.
  3. The explicit map (equations), with each equation carrying its source side
     and target side.
  4. Preserved observables: what an observer with stated access can measure
     identically under the map, and what access conditions this assumes.
  5. NOT-preserved list: what the map drops, weakens, or reinterprets.
  6. Convention sheet: every sign, unit, synchronization, and branch choice,
     declared (Diagrammatica's convention-fixing idea; anti-F4/F6).
- Hard rules: the map must state domain restrictions (which clock class, which
  sector, which frame family — anti-F1/F7); it must not silently specialize
  (anti-F3); where the source is ambiguous, the map records both readings.
- Failure modes it prevents: F1, F3, F4, F6, F7 (by construction forcing them
  onto the record).

### 2.3 Counterexample agent (adversarial)

- Input: a redacted view of the translation map (per R4) with `statement`,
  `failed_attempts`, `divergences`, `open_questions` and each assumption's
  `falsifier` removed, plus the pinned sources if it needs to check a citation.
  It does not receive the translator's reasoning.
- Mandate: defeat the map by construction. Required probes, each producing
  either a concrete counterexample or a signed "no finding" entry:
  1. Vacuity probe (Douglas heuristic): for every existentially quantified
     hypothesis, attempt to satisfy the letter while defeating the intent;
     attempt to satisfy all hypotheses with a degenerate model (anti-F2).
  2. Scope probe: exhibit a legitimate member of the claimed domain where the
     map's equations fail or the source claim does not apply (anti-F1).
  3. Limit probe: take stated limits (v→c, N→∞, D→large, zero coupling) and
     test whether the map's claims survive or were only approximate (anti-F3).
  4. Convention probe: flip each declared convention and check the map's
     predictions change in the way the source says (anti-F4/F6).
  5. Edge probe: dimension-zero, single-site, one-clock, empty-branch cases
     (anti-F9).
  6. Falsifier check: does the map name the single assumption whose change
     breaks the equivalence? If not, that is itself a finding.
- Hard rules: any claimed counterexample states its domain bound explicitly
  (finite model ≠ general theorem — AGENTS.md research standards); findings
  cite the map item (dictionary row, equation number) they defeat.

### 2.4 Reviewer (independent semantic auditor)

- Input: the map, the counterexample report, the pinned sources, and the
  verification artifacts (kernel output, oracle logs, model files).
- Cannot be the translator or the extractor of the same item (R4/R5).
- Answers four separated questions per artifact (Douglas's separation):
  1. Provenance: does every equation/assumption trace to a source ID + locator
     at the stated read depth?
  2. Correspondence: does the artifact say what the source says — no weaker, no
     stronger, no nearby statement?
  3. Derivability: can the claimed downstream consequences actually be derived
     from the artifact as stated?
  4. Observable preservation: do the preserved-observable claims hold under the
     stated access conditions?
- Output: a verdict record with per-question status, evidence links, remaining
  risks, and an explicit list of what was NOT checked. One review round by
  default; at most one repair round with a re-review of the delta (cap: 2
  rounds, adapting TNLean's cycle cap to our smaller scale).

Human review stays strategic: the coordinator (or a human-flagged reviewer
agent whose output is itself reviewed) audits intent — which statement was
meant — mirroring the TNLean finding that intent enforcement, not proof
search, is the bottleneck.

## 3. Handoff contract (artifact schema)

Every handoff between roles is a file in the producing task's `owns` paths,
using a fixed field set. JSONL for records; Markdown wrappers allowed for
readability, with the JSONL as the source of truth. Required fields:

```json
{
  "artifact_id": "xlat-<lane>-<n>",
  "artifact_kind": "extraction | translation-map | counterexample-report | audit-verdict",
  "producer_role": "extractor | translator | counterexample | reviewer",
  "model": "provider/model-id of the producing run",
  "created_on": "YYYY-MM-DD",
  "source_ids": ["<lane-prefixed IDs from some sources.jsonl>"],
  "source_versions": [{"id": "...", "version": "arXiv vN / commit SHA / DOI", "read_depth": "..."}],
  "statement": "the claim or map in one paragraph",
  "dictionary": [{"concept": "...", "object": "...", "source_id": "...", "locator": "eq. (n) / Sec. n / theorem n"}],
  "equations": [{"id": "eq-1", "source_side": {"id": "...", "locator": "...", "tex": "..."}, "target_side": {"tex": "..."}, "map_conditions": "..."}],
  "assumptions": [{"id": "as-1", "text": "...", "kind": "physical-premise | mathematical-definition | bridge-premise | convention", "source_id": "...", "locator": "...", "status": "assumed | derived | contested", "falsifier": "what change breaks downstream claims"}],
  "observables": [{"name": "...", "access_conditions": "...", "preserved": true, "source_id": "...", "locator": "..."}],
  "not_preserved": ["..."],
  "conventions": [{"name": "...", "chosen": "...", "alternatives": "...", "source_id": "...", "locator": "..."}],
  "divergences": [{"from": "source | sibling-source | earlier-artifact", "source_ids": ["..."], "description": "..."}],
  "failed_attempts": [{"route": "...", "why_abandoned": "...", "evidence": "..."}],
  "open_questions": ["..."],
  "verification": {"kernel": "none | command + result", "numeric_oracle": "none | engine + tolerance + result", "countermodel": "none | domain bound + result", "depth_limitations": "..."},
  "labels": {"is_conjecture": true, "is_source_claim": true, "is_verified_here": false}
}
```

Contract rules:

- C1 `source_versions` is mandatory for every artifact; an artifact without
  pinned versions is rejected at review.
- C2 Each entry of `assumptions` must carry `kind`; a premise that assumes an
  ontology (eternalism/presentism, passage) must be `bridge-premise`, per
  AGENTS.md, and cannot be cited as if derived.
- C3 `failed_attempts` and `divergences` are append-only across revisions of an
  artifact; empty lists are allowed only with a stated search.
- C4 `labels.is_verified_here` is true only if `verification` names a check that
  actually ran, with its command and result recorded in the lane report.
- C5 Any unresolvable provenance (equation the extractor cannot locate) is kept
  and flagged, never silently dropped (anti-F8).
- C7 Findings (in counterexample reports and audit verdicts) cite the artifact
  item they concern, or for a missing item the expected locus, plus the source
  locator where it is used or required. Each finding carries a severity
  (`minor | major | blocking`).
- C8 Per-kind field subsets: `extraction` omits `equations.target_side` and
  `observables`; `translation-map` uses the full schema; `counterexample-report`
  adds `findings` (C7) and `domain_bound`; `audit-verdict` adds `statuses` (one
  per §2.4 question: `ok | defect | not-checked`), `remaining_risks`, and
  `not_checked`. A verdict is reduced to a flag when any status is `defect` at
  severity `major` or higher.
- C9 `provenance_flag` (`resolved | unresolved`) accompanies each equation and
  assumption; C5's "kept and flagged" means `unresolved`, not a missing field.
- C6 Handoffs never contain credentials, private repository content, or
  unrelated personal data (AGENTS.md).

## 4. Semantic-audit procedure (applied by the reviewer; used again at
acceptance by the coordinator)

Layered, cheapest first; each layer is necessary, none is sufficient
(meth-sw-lean-2026 Sec. 5 pattern):

1. **Freeze.** Pin source versions and any code commits; record toolchain
   versions if a build is involved.
2. **Provenance sweep.** Trace every equation, assumption, and quantitative
   claim to source ID + locator. Untraceable ⇒ defect (F8). This step is pure
   bookkeeping and catches hallucinated premises without any model call.
3. **Vacuity probe.** For each hypothesis: can a witness be reverse-engineered
   so the hypothesis is satisfied but does no work? Can all hypotheses be
   satisfied by one degenerate model? (F2.)
4. **Scope audit.** Compare formal statement strength against the source
   statement: added hypotheses, dropped hypotheses, asymptotic/finite
   substitution, edge cases silently included or excluded (F1, F3, F9).
5. **Convention audit.** Check the convention sheet is complete and each
   declared convention matches the source's; flip conventions and re-derive a
   known consequence as a spot check (F4, F6).
6. **Independent check where possible.** Kernel build with `#print axioms` (or
   equivalent dependency report) for Lean artifacts; separate-engine numerical
   oracle with anchor values for quantitative claims; finite countermodel with
   stated domain bounds for logical claims. Record engine, version, tolerance,
   and the fact that the oracle can itself be wrong (Douglas's oracle erred
   twice; anchors caught it).
7. **Statement-level adversarial pass.** The counterexample report is reviewed
   for soundness; the reviewer tries to find at least one new defect the
   counterexample agent missed, on a sample of items. Numerical or kernel
   agreement never substitutes for this pass (62-checks-passed-3-gaps-found
   evidence).
8. **Verdict.** The four separated questions (§2.4) answered with evidence;
   remaining risks listed; unchecked items named. No verdict of "correct" is
   issued, only statuses per question.

Escalation: defects of class F1–F3 found at audit go back to the translator
with the map, not a rewritten map from the reviewer; the repair is the
producer's. Two rounds maximum, then escalate to the coordinator with the
disagreement recorded in `divergences`.

## 5. What this procedure does not do

- It does not certify physical truth of premises; it localizes trust onto named
  items (meth-sw-lean-2026).
- It does not replace the novelty audit or the Lean correspondence audit
  (NOVELTY.md gates; knowledge/formalization/reuse-map.md audit design).
- It does not create independence between same-model agents: roles sharing a
  model share failure modes; role separation limits, not removes, correlated
  errors. Cross-model review is desirable where available and its absence is a
  recorded limitation.
