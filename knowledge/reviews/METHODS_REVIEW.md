# Methods lane: independent review and execution gate

Date: 2026-10-19. Coordinator record; no merge, acceptance, or paid run is
performed by this file. Reviewed survey outputs are infrastructure, not a new
physics result or evidence for a temporal ontology.

## Reviewed snapshots and acceptance boundary

GLM submitted `d6f17ca` on `agent/kb-agent-methods`. Two fresh native
`gpt-6-luna` reviewers (high reasoning) independently inspected the clean
worker snapshot `29f92eccbc4444974664b0667f757caa5c55a12b`:

- `luna_pilot_math_review`: mathematical/physical ground truth and scope.
- `luna_pilot_eval_review`: blinding, measurements, controls, and experimental
  validity.

Their prompts were separate, but their shared model is a correlated-error risk;
their agreement is not evidence of mathematical truth. The coordinator checked
the source-depth tally directly: 10 records, comprising 3 full-text, 4 abstract,
and 3 discovery. No source study has been independently reproduced here.

The worker branch then advanced to `9c66b80488061f250d74bd7ec4ac116fd90c16f0`.
The coordinator inspected its diff: it narrows claims in `prior-methods.md`,
including distinguishing reported incidents from hypothetical risks and not
asserting unreported automated-review failures. That is useful correction, not
a new pilot evaluation. The pilot and handoff findings below still apply.

Recommendation: integrate the methods lane as a bounded prior-work survey and
design proposal, preserving these limitations. Do not interpret task acceptance
as pilot readiness, a complete query-driven literature sweep, or a novelty
certificate. Only mark the board task done after actual reviewed integration.
The Z.ai search limitation remains recorded; direct primary-source fetches and
citation chasing do not replace the missing search-led sweep.

## Required before pilot execution

References below use `knowledge/methods/pilot-design.md` at `29f92ec` in the
worker branch. These are review findings, not edits to another coordinator's
worktree.

1. **Fix the artifact denominator.** Lines 56–60 and 138–142 describe seven
   Family A classes, yet the table at 70–79 lists D1–D8 with an A-specific D2.
   State which classes actually run. Eight classes with three instances and two
   controls give 26 artifacts per family, not 23. Three calls per item across
   three runs would give 234 calls for one such family, before preparation,
   repairs, and tool calls. A smaller pilot is preferable before a large run.
2. **Blind processing, not only labels.** Lines 87–89 route only D-variants to
   the counterexample role. Gold status must not determine processing. Give
   every item the same route, tools, and budget; use opaque IDs; hide class
   names, mutation diffs, filenames, and the private label manifest. Freeze the
   manifest before evaluation. Do not give both members of an obvious pair to
   an auditor in the same context.
3. **Independently adjudicate gold labels.** T0 and mutations at 53–66 are not
   correct merely because an extractor/translator/injector produced them.
   Before evaluation, verify T0 against pinned source loci, each proposed
   mutation's intended single defect, its exact locus, and its witness. Keep
   ambiguous items out of the scored set rather than forcing binary labels.
4. **Replace or validate the reclassification control.** Lines 81–83 call
   physical-premise → bridge-premise reclassification an editorial change.
   Classification can change the inferential role. A truly harmless control
   could consistently rename a bound variable or reorder independent fields;
   its semantic invariance must be checked. Include varied clean items, not
   only two near-copies of one T0. Zero errors on two distinct clean items is
   not evidence of a generally low false-positive rate.
5. **Make mathematical defects item-specific.** D6 needs an actual equation
   and proof that the omitted root is still admissible under the stated
   orientation/continuity/domain assumptions. D1 must freeze coordinate roles;
   D3 must distinguish an incomplete derivation from a false claim; D4 must
   name a downstream inference that needs the removed content; D7 must make
   inclusion of the singular speed explicit rather than rely on an implicit
   notion of an inertial boost. D2 must remove a specific sourced condition,
   not conflate isotropy, reciprocity, and synchronization conventions.
6. **Specify Family B's actual model.** Lines 40–47 do not define a finite
   known-answer problem. Pin the clock, Hamiltonians, time states, admissible
   history states, normalization, and observables. A generic conditional-
   dynamics statement is not a finite model by itself. If approximated, name
   the approximation and its error target. Do not claim exact continuous-time
   ideal-clock behavior from an unspecified finite discretization.
7. **Freeze scoring and comparison claims.** Lines 112–127 score first-run
   recall but also say instability counts against a class without a decision
   rule. Choose an explicit item/class rule and report repeats as nested
   measurements, not independent samples. B1 vs the pipeline changes prompts,
   access, and calls as well as roles; without matched controls it tests a
   bundled workflow, not the causal benefit of role separation. Clarify B0 as
   a no-audit reference rather than an unspecified model baseline.

## Handoff-contract cautions

- The instruction to find *the single assumption* breaking each map
  (`handoff-contract.md:86–87`) is too restrictive. Some failures depend on
  combinations; some assumptions are redundant. Record tested sets and bounds;
  allow “not established,” rather than manufacture a unique falsifier.
- `#print axioms` (`:182–187`) reports declared axiom dependencies. Audit the
  theorem's full type, premise parameters, and referenced definitions as well:
  a physical postulate passed as a theorem hypothesis need not appear as an
  axiom constant. A clean dependency report does not establish physical
  correspondence. See the [Lean validation reference](https://lean-lang.org/doc/reference/latest/ValidatingProofs/).
- A source locator being present is a mechanical property; its supporting the
  attached equation is not pure bookkeeping. Keep provenance completeness
  separate from source entailment and from mathematical validity.

## Safe next work

Prepare a small readiness package first: independently checked gold pairs,
opaque public items, a private frozen manifest, uniform audit routing, precise
verdict schema, and a strictly bounded call budget. Existing sanity checks in
`knowledge/checks/` may seed it, but their mathematical truth labels must not be
mistaken for source-correspondence labels. No LLM performance result exists yet.

Theory-map synthesis may use the methods survey once it is integrated, while
keeping pilot execution and substantive novelty as separate gates. A failed
synthetic pilot would constrain this workflow; it would not refute a theory of
time.
