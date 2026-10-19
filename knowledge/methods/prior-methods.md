# Prior methods: AI-assisted physics, CAS agents, multi-agent autoformalization, semantic audit

Status: first-pass comparison, 2026-10-19. Evidence depths are in `sources.jsonl`
(`meth-*` records). Nine sources were read at full-text depth: three by the
lane worker (meth-cas-agents-2026, meth-tensor-agents-2026, meth-sw-lean-2026)
and six by a coordinator-launched subagent (AxQM, position paper, FERMIACC,
Diagrammatica, TPBench, Ax-Prover; the last two key sections only). Coordinator
re-verification covered repository facts and the figures cited in section 3, not
every sentence. The TNLean repository record stays at discovery depth. Nothing here has been reproduced; every claim below is the
source authors' claim at the stated depth, except where explicitly marked as
our design inference.

## 1. The compared workflows

| Workflow (source) | Shape | Verification model | Primary failure surface (authors' own reports) |
|---|---|---|---|
| Single LLM + CAS runtime on novel perturbation-theory problems; Claude Opus 4-6 driving a Maple REPL with expert-built contexts (meth-cas-agents-2026) | One agent, iterative REPL loop, 100-turn cap | Expert stage-wise pass/fail on 9 problems with known answers | Convention handling ("flat background" for cosmological evolution; the paper's exact wording on a Minkowski misreading was not confirmed); abandoned "too trivial" solutions; order reduction after forgetting Lagrange-multiplier constraints; an equivalence valid only if f″(χ)≠0; branch selection (branching noticed in all problems but one; the more complicated branch usually chosen, the simpler σ=0 branch once); instruction-only contexts cause decision paralysis |
| Multi-agent autoformalization: six specialized roles around a Lean blueprint, persistent memory, human strategic review (meth-tensor-agents-2026, meth-tnlean-repo) | Orchestrator + proof-writer + scout + simplifier + blueprint-sync + automated reviewer; parallel dispatch on disjoint files; scout-then-prove; review-repair capped at 5 cycles | Lean kernel for proofs; blueprint-vs-Lean and literature-vs-Lean semantic checks by reviewer agents (the paper does not report whether the automated reviewer flagged the two main incidents); six human blueprint-review rounds | Weakened statements (extra "doubly stochastic" hypothesis); finite statement replaced by asymptotic one; vacuous proofs from never-satisfied hypotheses named as a risk the reviewer checks for (no concrete incident reported); statements assuming structural data the intended theorem should derive (App. E.2); artificial D=0/N=0 cases excluded by adding D≥1, N≥1 (edge-case handling cost, not an error caught); blueprint-code drift; Lean heartbeat budget and model context limits. Stated bottleneck: "enforcing mathematical intent" |
| Named-postulate codification of a non-rigorous physics argument in Lean, with oracle and adversarial review (meth-sw-lean-2026) | Physics as predicates H0–H7 in theorem types; math-only `axiom` keyword; single dictionary from physical concepts to mathematical objects | `#print axioms` dependency report; numerical oracle (278 checks, 30–40 digits, separate engine); cross-model statement-level review; four-part transcription validation; independent physics routes to the prepotential agreeing (the paper's "physicist's triangle": weak-coupling perturbation theory, instanton expansion, exact curve periods) | Vacuous hypotheses (true by fiat); unsatisfiable hypotheses (R-symmetry order at rank 1); family-dependence traps (free coefficients fit anything at one scale); adversarial review found 3 statement-level gaps after 62 numerical checks passed; the oracle itself erred twice |
| Kernel-graded proof-synthesis benchmark over Nielsen–Chuang (meth-axqm-2026; see also form-axqm) | 1,019 tasks over 479 items (505 of 687 extracted items formalized); public sorry-stubbed statements, private solutions; independent and dependency-order regimes | Deterministic Lean kernel: compiles, no `sorry` in closure, no new axioms; the repository adds a statement-fingerprint check that a task's statement is untouched | The authors state that statement-level correspondence is not graded ("a statement can be vacuous, or quietly weaker than the claim in print, and still compile", Sec. 2) and rely on named human faithfulness review and dependency reuse, which they say does not guarantee correctness |
| Scaffolded hypothesis generation for particle theory (meth-fermiacc-2026) | Proposer-critic-patch loop (six critic axes) driving FeynRules/UFO, MadGraph, Pythia, Delphes, MadAnalysis | Deterministic tool and consistency checks; no known-answer benchmark; physics validation left to future work | UV-model-to-benchmark mapping not verified (Sec. 2.1 fn. 4); some proposals fail to reproduce the needed rate; about 7 single-shot proposals over 4 excesses, so "at scale" is not shown by reported counts |
| Tool-constrained symbolic computation in HEP (meth-diagrammatica-2026) | Agent emits compact human-auditable diagram specs; trusted backend computes exactly; two paths (NDA, exact FeynCalc); Claude Opus 4.6 in single curated sessions | Exhaustive enumeration within supported vertex families, checked by chiral-basis and NDA cross-checks and four PDG comparisons at 2–4%; not a graded known-answer catalog | Names the core problem directly: "correctness is governed by implicit mathematical conventions that are not encoded in a form that can be easily checked in the computational backend" |
| Position paper on language agents for physics (meth-language-agents-position-2026) | Argument, not system; no experiments; illustrative examples from late 2024 to early 2025; cautiously optimistic about specialized agents | Calls for verification frameworks; Sec. 4.3 critics should not see the generator's intermediate artifacts | Gaps claimed: physical intuition, constraint satisfaction, reliable reasoning; not fixable by prompting alone |

Not independently reviewed in this pass: the Douglas repository internals, the TNLean build, the HEPTAPOD log files, and AxQM's Lean statements beyond one sampled file. TPBench and Ax-Prover were read in key sections only.

## 2. Reusable code and artifacts (public)

| Artifact | License / state | Reuse for this project |
|---|---|---|
| TNLean + QICLean (Lean 4/Mathlib v4.35.0-rc3 pinned per README; 14,363 commits; Apache-2.0) | Research library in progress; sorries/axioms badges live; commit not pinned by us | Blueprint+checkdecls linkage pattern; released technique notes, distilled memory files, reviewer prompts (per paper) — candidate seeds for our own agent role prompts |
| TNLean `docs/paper-gaps/` convention (published at sirui-lu.com/TNLean/paper-gaps) | Live | Direct precedent for our required divergence register: every place a formal artifact says something different from its cited source, recorded, not hidden |
| leanblueprint / checkdecls toolchain | Open source | Mechanical check that every prose statement resolves to a declaration and every claimed proof exists — adopt for any Lean deliverable |
| TeXRA agent-definition YAMLs (paper App. H reproduces all five) | Released with TNLean | Drop-in starting points; must be adapted: our lanes are extraction/comparison tasks, not proof-writing |
| Douglas `mrdouglasny/seiberg-witten` (per paper; not inspected) | Companion to a working paper | Template for oracle suites (`validate_singcount.py` described in paper) and for `#print axioms` footprint reporting; inspect and pin before any reuse |
| AxQM benchmark + finite-dim QM library | Apache-2.0 plus NOTICE; statements on the `independent` (2ccf167e…) and `dependency-order` (233d4116…) branches, `main` (b14e4e10…) holds metadata; solutions private | Statements are usable without the solutions (sorry-stubbed, N&C text not reproduced). The ~3,500 supporting library definitions are unaudited, so a mis-defined primitive would corrupt dependent statements |
| HEPTAPOD (Diagrammatica code and logs) | GPL-3.0; HEAD 76e1a311… (2026-10-14, after the paper, not paper-pinned) | Convention-fixing tool design; session logs claimed by the paper, unverified |
| TPBench / Ax-Prover | TPBench: public problems at tpbench.org, private set on request, no official repo found. Ax-Prover: no paper-linked repo; `Axiomatic-AI/ax-prover-base` (AGPL-3.0) is a different paper's artifact | Numeric-answer checking only (TPBench); compile-plus-no-sorry grading with no statement check (Ax-Prover) |
| Hell–Thiele context recipe + stage rubric (paper Sec. 3.4–3.5, App. B) | Published text, no code repo named | Recipe: worked examples > abstract instructions; small representative sets > large ones; retarget examples at observed failures. Rubric: grade stages, allow correct-final-with-forgotten-subtlety to pass only when explicitly recorded |
| Diagrammatica known-answer catalog design | Abstract-level | Pattern: exhaustive small-theory catalog with limits, as clean items for a defect-injection evaluation |

## 3. Failure-mode taxonomy (consolidated, each anchored to a primary source)

1. **F1 Weakened/narrowed statement.** Formal artifact is provable and correct but
   weaker or more special than the source claim. Evidence: TNLean DS-gauge
   incident. Consequence for us: a Lean-checked "equivalence" between two
   descriptions of time may silently hold only for ideal clocks or one frame
   family.
2. **F2 Vacuous or unsatisfiable hypotheses.** Witnesses trivially exist or cannot
   exist. Evidence: Douglas H3/H5/H6 hardening. TNLean names vacuous
   proofs as a risk its reviewer checks for but reports no instance. Consequence: an assumption map can look satisfied while carrying
   no physics.
3. **F3 Nearby-statement substitution (finite/asymptotic).** Proving a related
   statement instead of the intended one. Evidence: TNLean asymptotic swap.
   Consequence: first-order-in-v/c or large-N checks standing in for exact
   claims.
4. **F4 Convention misreading.** Implicit conventions resolved wrongly and
   silently. Evidence: Hell–Thiele flat-background; Diagrammatica's motivating
   problem. Consequence: simultaneity conventions, sign of boost parameter, and
   clock-synchronization conventions are exactly this class in our subject.
5. **F5 Dropped constraints mid-derivation.** Evidence: Hell–Thiele forgotten
   Lagrange multipliers. Consequence: Page–Wootters-style conditionalizations
   that drop the constraint Hamiltonian.
6. **F6 Silent branch selection.** Evidence: Hell–Thiele multiple background
   branches (noticed in nearly all problems, so "silent" is our gloss). Consequence: choosing one simultaneity convention or one growth
   order without flagging alternatives.
7. **F7 Conditional equivalence used unconditionally.** Evidence: Hell–Thiele
   f″(χ)≠0 subtlety (the paper states the condition; "used unconditionally"
   is our gloss of the risk). Consequence: equivalence theorems (e.g., relational
   dynamics trinity results) whose hypotheses carry sector or clock-class
   restrictions.
8. **F8 Untraceable premises.** Equations or assumptions without provenance.
   Evidence: Douglas names hallucinated assumptions as AI's characteristic
   physics error; Hell–Thiele saw training-set knowledge enter uninvited.
9. **F9 Edge cases outside the physical domain.** Evidence: TNLean adds D≥1, N≥1 to exclude artificial Lean cases (App. B.5
    reports about 2,000 lines of Lean on them); a handling cost, not a caught error.
10. **F10 Review-loop pathologies.** Endless review on revision; self-review
    agreement as false confidence. Evidence: TNLean's 5-cycle cap and its
    incidents where the human supervisor flagged unintended versions of the
    statement (the paper does not report what the automated reviewer did); Douglas's separation of "is it proved?" from "does it
    say what the source says?" from "can the intended theorems be derived?".

### Documented evidence that agreement is not correctness

- Douglas: an axiom set passed 62 numerical checks and was still rejected by
  adversarial statement review (three gaps invisible to sampling). Two engines
  agreeing on values did not make the statement fit for purpose.
- TNLean: the human supervisor flagged the weakened DS-gauge theorem and the
  asymptotic substitution; the paper does not report whether the automated
  reviewer had flagged either.
- Hell–Thiele: a 1024-token thinking budget gave very little improvement, and
  a smaller representative example set beat a larger one; a single-model judge would share the misreading ("flat
  background").
- These are also the project's stated position (knowledge/NOVELTY.md): same-model
  agents share failure modes; different prompts do not create independent
  evidence.

## 4. Design conclusions for this project (our inference, from the above)

1. Adopt the Douglas separation as architecture: physical premises,
   mathematical definitions, and philosophical bridge premises are different
   record types with different audit duties; physics must never hide inside a
   mathematical definition or a prose summary.
2. Adopt the blueprint/link pattern mechanically (every equation and assumption
   resolves to a source ID + locator), because F1/F2/F8 are invisible to kernel
   checking and to prose review.
3. Keep a published divergence register per lane (TNLean paper-gaps pattern):
   disagreements between sources and divergences between our artifacts and
   their sources are outputs, not noise.
4. Require concrete falsifiers for every equivalence claim: which single named
   assumption, changed how, breaks it (needed for candidate A/D work and for
   the counterexample role).
5. Verification is layered and each layer is necessary-not-sufficient: kernel
   or CAS where available; independent numerical oracle; finite countermodels
   with stated bounds; statement-level adversarial review; human strategic
   review of intent. Agreement of any subset is recorded, never treated as
   proof of correspondence.
6. Cost/scale reality check: TNLean's authors report $20,206 recorded model-API cost for their library (arXiv:2607.07857, verified by coordinator; a figure from their project, not ours) and
   six human review rounds for one theorem's blueprint. Our lanes must assume
   review effort, not just generation effort, and scope pilots accordingly.

The handoff contract, role definitions, and audit procedure that follow from
these conclusions are in `handoff-contract.md`; the evaluation pilot is in
`pilot-design.md`.
