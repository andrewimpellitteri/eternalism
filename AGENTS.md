# Agent instructions

## Read first

Read README.md, knowledge/README.md, knowledge/NOVELTY.md, and your task brief
from `python3 scripts/agents.py brief TASK`. WORKBOARD.jsonl defines tasks;
WORKBOARD.md is generated. This project has no preferred temporal ontology.

## Coordination

- The user authorized OpenCode GLM headless agents. Default to that workflow.
- The user also authorized native GPT-6 Luna research agents. For an assigned
  native run, the coordinator claims the task first and assigns disjoint output
  directories; stay in those paths. The coordinator handles board transitions.
  Native runs may use the shared checkout when worktrees are unavailable.
- Use `scripts/agents.py launch`; it claims a task before creating an isolated
  worktree. Never edit another task's worktree or overwrite another claim.
- Remain within the brief's `owns` paths. Read other files as needed.
- Agents do not edit the workboard, runner, AGENTS.md, or shared seed sources.
- Commit only the named files you own. Do not use `git add -A`.
- Do not push, merge, reset, deploy, or launch additional agents from a worker.
- Write AGENT_REPORT.md with files changed, evidence, checks, limitations, and
  unresolved questions. A worker submission goes to review; it is not accepted
  completion. The coordinator inspects and integrates it before `accept`.
- Claims do not expire automatically. Check the process and worktree before
  releasing a stopped or failed task; preserve its outputs.

## Research standards

- Prior work and novelty audit come before original-theory implementation.
- Use primary papers and original code. Preserve exact versions and locators
  when read. Never invent a theorem number, quotation, experiment, or citation.
- Label read depth: discovery, abstract, full-text, reproduced, or code-audited.
  An abstract is a lead, not verification of a proof or an open problem.
- Distinguish paper authors' claims, established results, and our conjectures.
- Distinguish temporal ontology, objective passage, determinism, causal order,
  clock time, and the thermodynamic arrow. These are not interchangeable.
- Separate physical premises, mathematical definitions, and philosophical bridge
  premises. A definition that already assumes eternalism/presentism cannot
  independently establish it.
- A Lean build checks the encoded statement. Audit correspondence to the paper,
  all nonstandard axioms, `sorry`, and transitive dependencies. No novelty claim
  follows merely from using Lean, LLMs, or a recent preprint.
- A finite countermodel or numerical search has its stated domain only. It is
  not a general theorem. A representation transformation is not automatically
  an ontological equivalence or a gauge symmetry.
- Synthesis must preserve incompatible assumptions and empirical equivalence.
  Agent votes, citation counts, and arbitrary weighted scores are not physics.
- No dependency installs or large runs from workers without a task that names
  them. No credentials, private repositories, or unrelated personal data in
  prompts. Research workers use public sources and project files only.

