# Agentic philosophy: state of play and a swarm playbook

Status: updated 2026-10-22. A short working note, not a literature review. It records
what “agentic philosophy” currently means, the closest prior art, where agents
help, where they fail, and a concrete swarm design for producing something
new.

**30 October extension:** [What would count as a breakthrough?](BREAKTHROUGH_TEST.md)
separates useful output, historical originality, philosophical advance and AI
attribution. It applies an additional consequential-inference test to this
project's actual results and proposes one bounded ontology pilot. Six selected
primary readings are recorded. This is a methodological proposal, not evidence
that our workflow improves discovery rates or has produced a new ontology.

The implemented extension is [the creative-search protocol](creativity-loop/PROTOCOL.md),
with [recent mathematics examples](creativity-loop/RECENT_MATH.md) and an
[executed observer-access pilot](creativity-loop/pilot/RESULT.md). It adds
representation changes, auxiliary objects, and recombination to the audit loop.
The pilot demonstrates execution, not measured improvement over a baseline.

## 1. Two meanings

- **Philosophy *of* agentic AI:** agency, autonomy, responsibility, alignment.
  This is an established literature.
- **Agents *doing* philosophy:** much thinner. Most existing work is
  LLM-assisted philosophy, computational philosophy, or agentic science applied
  to philosophical material.

There is no mature benchmark for *philosophical novelty*. The closest work is
philosophical-reasoning/ethics benchmarking, conceptual-reasoning leaderboards,
and AI-science novelty evaluation. Benchmark competence is not philosophical
understanding; Millière’s 2026 survey is a useful corrective.

## 2. Prior art in six strands

| Strand | Representative work | Relevance |
|---|---|---|
| Computational philosophy | [SEP: Computational Philosophy](https://plato.stanford.edu/entries/computational-philosophy/) | Pre-LLM baseline: models, simulations, formal methods. |
| LLMs as philosophers | [Millière, *The Philosophy of Language Models* (2026)](https://compass.onlinelibrary.wiley.com/doi/10.1111/phc3.70095); [APA blog (2024)](https://blog.apaonline.org/2024/11/28/large-language-models-llms-are-often-poor-philosophers-but-these-shortcomings-make-them-more-useful-for-teaching-not-less/) | Capability and failure modes; teaching is a stronger use case than discovery. |
| Multi-agent debate | [Du et al. 2023](https://arxiv.org/abs/2305.14325); [Irving et al. 2018](https://arxiv.org/abs/1805.00899); [2026 survey](https://arxiv.org/html/2607.26212v1) | Improves factuality/robustness; does not create a question or guarantee truth. |
| Agentic science | [Google AI co-scientist (2025)](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/); [Robin (Nature 2026)](https://www.nature.com/articles/s41586-026-10652-y); [AI Scientist (Nature 2026)](https://www.nature.com/articles/s41586-026-10265-5) | Closest architecture prior art: generate → debate → evolve/tournament → review. |
| Novelty evaluation | [RINoBench (2026)](https://arxiv.org/abs/2603.10303); [NovBench](https://informationmatters.org/2026/04/can-ai-really-understand-scientific-novelty-insights-from-a-new-benchmark/); [“Instability of LLM-Based Novelty Evaluation” (2026)](https://arxiv.org/html/2610.02022v1) | LLM novelty judges are brittle; novelty needs literature-grounded, assumption-level comparison. |
| Formal philosophy | [Tao on Lean reliability and AI (2026)](https://terrytao.wordpress.com/2026/10/09/what-mathematicians-should-know-about-the-lean-theorem-proverquestions-of-reliability-and-ai/) | Lean checks the encoded statement, not its meaning or physical relevance. |

Adjacent philosophical work includes conceptual engineering with LLMs
([bias/prototype paper, 2024](https://link.springer.com/article/10.1007/s11098-024-02273-w)),
LLM “silicon sampling” in experimental philosophy, and the now-standard critique
that fluent text is not understanding.

## 3. Where agents add value

- **Cartography:** positions, premises, locators, read depth, disagreements.
- **Defeater-first prior art:** three closest predecessors before drafting.
- **Countermodel/consistency search:** finite models, exact certificates.
- **Translation:** map one framework’s assumptions onto another’s.
- **Generative search:** invent auxiliary objects, change representations, and
  attack strategic intermediate lemmas. Preserve different mechanisms.
- **Recombination:** turn a failed route’s missing hypothesis into a bounded
  child question; preserve the failed inference.
- **Adversarial review:** different model family, fresh context.
- **Drafting and teaching:** summaries, objections, examples, exposition.

## 4. Where they fail

- Choosing a question worth asking.
- Judging novelty against a literature they have not fully read.
- Distinguishing a mathematical result from a physical or ontological one.
- Resisting consensus, sycophancy, and stylistic confidence.
- Citation accuracy; “abstract-as-proof”; formalization theater.
- Turning more agents into more of the same idea.

## 5. A swarm that makes sense

**Stage 0 — Authorized question contract.** One page: exact question, nearest
predecessors, smallest example, kill conditions, and evidence sought. The
coordinator can supply it within the user-authorized scope. A candidate claim
can emerge during search; do not require a preferred answer.

**Generative round — Distinct mechanisms.** Produce bounded alternatives:
representation change, auxiliary object, or inverted question. Run cheap
discriminating tests and preserve failures. Each child changes one named
mechanism or assumption. Return here when an audit reveals a productive
missing hypothesis; use the linked protocol to retain ancestry and evidence.

**Stage 1 — Cartographers.** Read primary texts; source records with locators
and honest depth. Reuse IDs; no abstract-as-proof.

**Stage 2 — Adversaries.** Each tries to kill the claim: closest predecessor,
countermodel, equivocation, bridge-premise failure. Report the strongest
defeater first.

**Stage 3 — Formalizers.** Lean/exact models only for the mathematical spine.
Light, pinned, no giant libraries; finite kernels are often enough. No `sorry`,
no opaque axioms; audit correspondence.

**Stage 4 — Bridge auditor.** Separate mathematical, physical, and philosophical
premises. A definition that assumes eternalism cannot establish it.

**Stage 5 — Selection gate.** The coordinator retains supported results within
the authorized scope and presents consequential premise choices to the user.
Keep mathematical, source, physical, and philosophical gates separate.
No agent votes, no weighted ontology scores.

**Stage 6 — Independent replication.** Different model family, fresh context;
spot-check citations, proofs, code. Same-model agents share failure modes.

**Coordination:** a blackboard of claims (ID, assumptions, evidence, status),
disjoint file ownership, no agent edits the board. Max 2–3 rounds; debate without
a gate becomes noise.

## 6. Design rules

- Prefer model-family diversity when available; fresh contexts in one family
  provide bounded review, not independent model-family replication.
- Roles over personas: cartographer, adversary, formalizer, auditor — not
  “Socrates” and “Hume”.
- Novelty = assumption-level delta + named defeater, not “this sounds new”.
- Preserve negative results; define kill criteria before work starts.
- Judge output by source-backed claims and reproducible checks, not word count
  or consensus.
- Human owns the question and the gate; agents own the middle.

## 7. An executed bounded pilot

The [observer-access pilot](creativity-loop/pilot/RESULT.md) used a coordinator,
a fresh-context proposer, and a separate reviewer. Three live mechanisms were
considered: Hilbert representation, finite-memory stopping, and invariant event
access. A false L1-to-L2 shortcut was a seeded control, not a spontaneous
failed discovery. The actual densities admit an L2 bound supporting a
conditional readout result; no physical instrument or ontology follows.

The local helper validates ancestry and question-file hashes and emits review
packets without proposer verdicts. It does not judge proofs or launch models.
The methods defect-injection benchmark remains a proposal. A matched-budget
comparison against one-shot and critique-only search would be needed to claim
better performance.

## 8. Lessons from this repository

- The **selection gate** is the right template: a human decision among bounded
  contracts, with explicit kills and a fallback, beats a popular vote.
- **Light formal checks** (exact finite certificates, a no-mathlib Lean kernel)
  catch bookkeeping errors and keep the correspondence honest. They do not make
  a result new.
- **Prior art is the bottleneck.** The current project’s strongest selected
  result may be a short corollary of its direct predecessor; only a targeted
  priority audit can decide that.
- **Do not formalize ontology.** Formalize the mathematical spine and the
  bridge premises separately; the philosophical work is usually in the premise,
  not the proof.

## 9. Working aim

Use agents both to generate mathematical objects and to challenge them. Exact
checks guide search where available; source correspondence, physical access,
significance, and bridge premises require separate judgments. Preserve a
useful conditional result when its grander interpretation fails.
