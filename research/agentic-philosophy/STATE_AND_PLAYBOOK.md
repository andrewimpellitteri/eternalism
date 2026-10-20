# Agentic philosophy: state of play and a swarm playbook

Status: 2026-10-20. A short working note, not a literature review. It records
what “agentic philosophy” currently means, the closest prior art, where agents
help, where they fail, and a concrete swarm design for producing something
new.

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

**Stage 0 — Human claim contract.** One page: exact question, proposed claim,
three nearest predecessors, delta, smallest example, falsifier, novelty kind.
No agent proceeds without it.

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

**Stage 5 — Selection gate.** A human decides: primary target, fallback, or
explicit no-selection. No agent votes, no weighted scores.

**Stage 6 — Independent replication.** Different model family, fresh context;
spot-check citations, proofs, code. Same-model agents share failure modes.

**Coordination:** a blackboard of claims (ID, assumptions, evidence, status),
disjoint file ownership, no agent edits the board. Max 2–3 rounds; debate without
a gate becomes noise.

## 6. Design rules

- Use 2–3 model families, not ten copies of one model.
- Roles over personas: cartographer, adversary, formalizer, auditor — not
  “Socrates” and “Hume”.
- Novelty = assumption-level delta + named defeater, not “this sounds new”.
- Preserve negative results; define kill criteria before work starts.
- Judge output by source-backed claims and reproducible checks, not word count
  or consensus.
- Human owns the question and the gate; agents own the middle.

## 7. A concrete first experiment

Pick one narrow question — e.g. *“which premise does the work in argument A,
and is there a countermodel when it is dropped?”* Run six agents for two weeks.
Deliver: a source map, three candidate claims, one countermodel or formal
kernel, and a one-page selection memo. Success is a defensible **no** or a
sharpened claim, not a paper.

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

## Bottom line

The realistic near-term contribution is **adversarial formal philosophy**:
agents compress the literature, attack claims, and check the mathematical
spine; humans choose the question, judge significance, and own the bridge
premises. A swarm is a better red team than a better philosopher.
