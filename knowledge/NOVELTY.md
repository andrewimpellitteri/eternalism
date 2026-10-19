# Novelty strategy

Status: research proposals, not discoveries. Updated 2026-10-19.

## What is already occupied

Logical axiom analysis of relativity predates this project: see
[Andréka et al.](https://arxiv.org/abs/1105.0885). Machine-assisted relativity
also predates it: see [Stannett](https://eprints.whiterose.ac.uk/id/eprint/86607/).
[Physlib](https://github.com/leanprover-community/physlib) already formalizes
physics in Lean. Recreating Lorentz transformations or a twin-paradox proof is
a useful baseline, not a novel research claim.

Assumption-sensitive simultaneity analysis also exists:
[Besnard](https://arxiv.org/abs/1104.1263) explicitly studies definability and
available observer structure. Philosophical counterpositions include
[Brading](https://scholars.duke.edu/publication/1377437) and
[Wüthrich and Callender](https://arxiv.org/abs/1502.00018).
"Relativity proves eternalism" is not a suitable starting axiom.

AI-assisted physics and multi-agent formalization are prior art too. See
[tensor-network autoformalization](https://arxiv.org/abs/2607.07857),
[physical axioms in a Seiberg–Witten formalization](https://arxiv.org/abs/2607.06379),
and [LLMs with a computer algebra runtime](https://arxiv.org/abs/2605.08212).
These are abstract-level leads here; their implementations need auditing.

## Candidate contributions

### A. Find the boundary of observational distinguishability

Question: in a carefully bounded family of models, can a physical observer's
records distinguish a growing history from a completed-history representation?
If not, which additional dynamics or access assumptions first make a difference?

Deliverable: an explicit mapping that preserves specified observables, a proof
under named assumptions, and counterexamples when essential assumptions change.
Include stochastic/branching histories; do not identify eternalism with
determinism. Do not declare all ontologies gauge equivalent.

Nearest precedents: covariant causal-set growth, relativistic becoming,
operational equivalence, and histories/relational formulations. A new translation
of familiar equations is insufficient. Reject this candidate if the result is
already an immediate corollary of a known equivalence or true by our definitions.

### B. Extend a recent quantum-clock result beyond its idealizations

Question: do two descriptions that agree for an ideal clock still agree for
interacting clocks, finite resolution, or restricted observer access?

Deliverable: reproduce a recent paper's smallest tractable model, extract the
exact assumptions, and derive a previously unreported correction, equivalence
boundary, or counterexample. Trace any consequence for ontology through explicit
bridge premises. Begin with finite-dimensional systems if they faithfully retain
the target effect; a toy model cannot establish the full field-theoretic claim.

Nearest precedents: [spacetime QRFs](https://arxiv.org/abs/2101.11628),
[temporal measurements](https://arxiv.org/abs/2308.10967), and their references
and subsequent work. Recent candidates are in the source seed; their results
are not yet verified. Search relational-time equivalence and imperfect-clock
literature before calling any extension open.

Concrete narrowing already found through Z.ai search: the
[relational trinity](https://arxiv.org/abs/1912.00033v3) explicitly encompasses
non-ideal clocks, and a [relativistic extension](https://arxiv.org/abs/2007.00580v1)
already exists. Thus "extend equivalence to non-ideal clocks" is too broad to
claim as a gap. Extract their exact hypotheses before selecting an interaction,
resolution, or observer-access case outside their scope.

### C. Search for minimal assumptions behind time arguments

Question: which combinations of symmetry, locality, definability, global
foliation, and ontological premises actually force a disputed conclusion?

Deliverable: a new classification theorem or a new countermodel, with an
assumption-dependency graph and checked certificates for selected results.
Finite model finding can propose examples; Lean or an appropriate proof system
can verify the precise mathematical statement.

Nearest precedents: axiomatic relativity, Malament/Stein, directed-time variants,
and Besnard. Automated axiom ablation alone is not new. Reject candidates that
only restate known independence results or confuse a finite bound with all models.

### D. Let synthesis produce a precise disagreement

Have theory specialists independently fill the same comparison contract. Ask
translation agents for explicit maps between models, and adversarial agents for
an observable or mathematical obstruction that breaks each map. Preserve
incommensurability when no defensible translation exists.

Deliverable: an unexpected bridge between two frameworks with a new derived
consequence, or a precise incompatibility/no-go result. A prose synthesis,
taxonomy, searchable corpus, or swarm consensus is useful infrastructure but
does not satisfy this project's substantive novelty goal by itself.

## Gate before original implementation

For each shortlisted candidate, write a one-page claim contract:

1. Exact question and proposed theorem, counterexample, or measurable prediction.
2. Three nearest predecessors and a comparison at assumption/result level.
3. What changes relative to those predecessors, and why it matters.
4. Smallest reproducible example and independent verification route.
5. What would show the claim is wrong, trivial, already known, or physically
   irrelevant. Include searches capable of defeating our novelty claim.
6. Explicit separation of mathematical novelty, formalization novelty, physical
   novelty, and philosophical consequence.

An independent reviewer who did not propose the candidate must challenge that
contract. Passing the gate selects a research target; it does not certify global
priority or truth. A formalization can be a valuable contribution if it discovers
a real gap or creates a reusable missing foundation, even without new physics.

## Agent organization

Start with three parallel literature lanes and queue the methods lane next.
Use fresh synthesis and criticism tasks after those outputs are integrated.
Expand by theory family, not by making many agents read everything. Return source
IDs, exact assumptions, equations, and falsifiers, not just prose summaries.
Same-model agents share failure modes: independently check source correspondence,
calculations, and proofs; different prompts do not create independent evidence.

Choose one narrow target after broad screening. Python explores and reproduces;
Lean verifies selected statements after checking correspondence. Keep proposed
results, failed searches, and accepted conclusions separately labeled throughout.

