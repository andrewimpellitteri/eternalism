# A creative research loop for this repository

22 October 2026. Implemented adaptation of inspected mathematics workflows;
not a claim that this harness improves discovery rates. One live pilot is
recorded in `pilot/`. Reuse `scripts/agents.py` for ownership and review.

## Change the object being searched

The existing playbook supplies provenance and adversarial review. Add a
generation phase where the LLM proposes mathematical objects, alternative
representations and discriminating experiments. Give it an obstruction and
a fixed question, rather than only asking for a proof of a favored sentence.
An idea can be worth retaining because it exposes the missing premise.

The search unit is a **candidate mechanism**. A new title or different prose
for the same construction is not a new mechanism. Start with three routes:
one representation change; one reversal/obstruction; one different observable
or auxiliary object. At most three active researchers including coordinator,
and two bounded rounds for this pilot. This is a small human-directed loop,
not a reproduction of an industrial automated search system.

## One round

1. **Freeze the question.** Write `QUESTION.md`: what must stay fixed, what may
   change, smallest useful result, and what would merely answer an easier
   question. Record physical and philosophical questions separately.
2. **Generate before selecting.** Ask independent proposers for genuinely
   different mechanisms and one cheap test each. They receive the question
   and evidence, without a coordinator's preferred answer. Assign disjoint
   files. A proposed bridge premise may be speculative if labelled as such.
3. **Test cheaply.** Check the first obstruction with exact computation,
   limiting cases, countermodels or source lookup. Preserve a failing idea
   and its specific failure; it can become a useful parent of a revised idea.
4. **Change one thing.** A child candidate records parents, the changed
   representation/assumption, and whether this changes the question. A changed
   question gets a new contract rather than borrowing the old verdict.
5. **Review a clean artifact.** Give the reviewer the frozen question, proposed
   statement, assumptions, proof/witness and sources. Omit the proposer's
   confidence, a preferred winner and private thinking traces. Reviewer outputs
   specific defects or uncertainty, not a vote for the most fluent narrative.
6. **Select using evidence.** Retain one mathematically checkable route and one
   structurally different unresolved route where useful. Stop a branch on its
   named kill. If every route fails, report the obstruction. Human/coordinator
   judgment chooses relevance; changing the scientific question needs visibility.

## Separate kinds of feedback

Record four gates per candidate, without combining them into a score:

| Gate | Useful evidence | What a pass does not establish |
| --- | --- | --- |
| Mathematical | Exact witness, analytic proof, counterexample, bounded computation | Source correspondence, physical implementability or novelty |
| Source/priority | A pinned primary statement and assumption-level comparison | Truth of an unexamined proof, absence of older literature |
| Physical access | Named state/preparation, instrument, symmetries, resources | That those resources exist in the causal-set model or a laboratory |
| Philosophical bridge | Explicit premise-to-conclusion argument and counterposition | A unique ontology selected by a mathematical representation |

Use `pass`, `fail`, `conditional` or `unknown` for a **named** test. `unknown`
is a useful result, not a low confidence pass. An LLM rubric about elegance or
novelty is a suggestion for inspection. It never substitutes for these gates.

## Creative moves to request explicitly

- Replace a difficult sum with a geometric, dual, variational or measure-theoretic
  representation; state what the map preserves and what it adds.
- Invent an auxiliary object whose existence would make the problem easy;
  test whether that object is actually available.
- Turn “can we distinguish?” into “what is the smallest access algebra that
  would permit distinction?” or prove an obstruction for the declared algebra.
- Find the invariant behind two apparently unrelated failed approaches;
  combine their useful fragments instead of restarting from a blank prompt.
- Ask for the strongest nearby statement the evidence really proves, then
  identify precisely how it differs from the intended question.
- Generate a toy model that breaks the argument and an edited-but-valid
  control that should survive. Retain both rather than training a critic to
  reject everything.

These are prompts for search operators, not claims of general LLM creativity.
The inspected sources and their evidence limits are in `RECENT_MATH.md`.

## Artifacts and reuse

`candidates.jsonl` preserves public claim summaries, ancestry, tests and
disposition. It is a bounded research archive, not the global workboard.
`loop.py validate` checks its structural consistency and contract hash;
`loop.py packet ID --role reviewer` produces an evidence index without
generator verdicts; `--role proposer` includes branch feedback for revision.
Reviewers must open the linked artifacts; the index is not self-contained
and does not conceal provenance inside those files. The tool does not evaluate
proofs, launch models, run arbitrary commands,
rank hypotheses, or approve a physical/philosophical claim.

Use the short prompts in `PROMPTS.md`, then existing claim/review/accept
commands. Keep a small interaction card: who supplied the question, who
proposed a mechanism, what was changed after failure, what was checked, and
what remains unknown. Store public outputs and substantive corrections, not
private chain-of-thought. Exact model family is recorded only when known;
fresh contexts from one family are not independent model-family evidence.

## Evaluate the workflow honestly

For a later comparison, fix one question, sources, model/call/time budget and
known-answer controls before comparing one-shot, critique-only and this loop.
Track distinct mechanisms tested, actual counterexamples, question drift,
source errors and reusable surviving lemmas. Do not count pages or agreement.
The present pilot is transparent and unblinded; it demonstrates execution and
finds technical boundaries, not a measured improvement over another method.
