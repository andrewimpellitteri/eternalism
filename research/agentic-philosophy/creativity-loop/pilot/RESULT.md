# Creative-search pilot: what changed and what survived

22 October 2026. This is an executed, unblinded research pilot, not a benchmark
or an originality claim. The [frozen question](QUESTION.md) concerns observer
access to the existing matched atomless scalar growth models.

## Result

A representation change exposes a useful boundary. For these particular
models, their densities relative to the common reference P0 are square
integrable. Normalizing them as Hilbert-space vectors gives identical outcome
probabilities for every multiplication-effect readout. A specified coherent
projector instead distinguishes the pair. Its probability is

    p_j(E)=|nu_j(E)|^2/[K P0(E)],

not the unnormalized quantum-measure value. The [analytic derivation](STATE_READOUT.md)
includes the extra L2 bound; [independent review](../INDEPENDENT_REVIEW.md)
checks the denominators, convergence, reference dependence and scope.

This constructs a conditional mathematical measurement model. It does not
supply a physical preparation or causal-set detector, prove full instrument
covariance, or establish a temporal ontology. Selecting the reference measure
and accessible effects remains additional structure requiring justification.

## Search outcomes

| Route | Cheap test / obstruction | Disposition |
| --- | --- | --- |
| Seeded L1-to-L2 shortcut | An integrable density need not be square integrable. | Refuted control; never claimed as a discovery. |
| Actual density-to-state representation | Relative transition bounds yield bounded L2 martingale norms. | Retained with an analytic proof for this pair. |
| Finite-memory stopping | A finite prefix with two minima permits both a future third minimum and no further minima. | Exact finite certification blocked; stopped operational statistic needs an instrument. |
| Invariant event predicates | Completed minima count is intrinsic; finite-prefix invariance does not imply completed covariance. | Membership alone does not deliver coherent access. |
| Recombine representation and access algebra | Multiplication effects agree; coherent Q_E differs. | Conditional mathematical result; physical realization unresolved. |

There are three live mechanisms here, not five independent discoveries. The
seeded control and the recombination are recorded as such. Finite stopping and
event-language proposals are preserved in [REFORMULATIONS.md](REFORMULATIONS.md),
including their strongest kills; neither is promoted to an implemented observer.

The [exact finite checker](check_access.py) reconstructs the seven depth-three
histories and their nonuniform reference weights. It independently expands
coherent cross terms, verifies common normalization and equal diagonal
probabilities, and confirms that dephasing removes the distinction. It also
checks clean conjugation and continuation controls. Its [captured output](output.json)
is a finite certificate; the infinite-level result relies on the analytic
proof, not extrapolation from these seven histories. Four transparent paired
[negative controls](NEGATIVE_CONTROLS.md) guard nearby semantic errors; they
are not a blinded defect-detection score.

## What was implemented

The [protocol](../PROTOCOL.md) adds generate → test → transform → retain or
recombine to the existing source/bridge audits. [Prompts](../PROMPTS.md)
request mechanisms and auxiliary objects, rather than more opinions about the
same claim. The [candidate archive](../candidates.jsonl) retains parent-child
relationships, failed tests, evidence paths and four separate gates. Verdicts
are reviewer judgments supported by artifacts, not automatic truth labels.

From the repository root:

```sh
python3 research/agentic-philosophy/creativity-loop/loop.py validate
python3 research/agentic-philosophy/creativity-loop/loop.py check
python3 research/agentic-philosophy/creativity-loop/loop.py packet readout-algebra-split --role reviewer
```

The helper validates structure and detects question-file changes. It emits a
review index without proposer verdicts or confidence; reviewers must open the
linked evidence files. Those artifacts can
still reveal provenance, so this is not blind review. It never selects a
scientific winner, executes archive-supplied commands or launches models.

## Interaction and evidence limits

The coordinator inspected primary-method passages from recent mathematics,
proposed the L2 representation, derived its bound, wrote the checker and
integrated the results. A fresh-context native proposer supplied the stopping
and invariant-event alternatives. A separate native reviewer supplied paired
controls and checked the proof and protocol, with its precise review depth
recorded in its report. All worked under disjoint file ownership. These are
not demonstrated independent model families. Public artifacts preserve claims,
checks and corrections; private model thinking traces are neither collected
nor needed.

The archive is retrospective. There was no randomized allocation, matched
one-shot baseline, blind scoring, cost accounting or performance ablation.
This establishes that the workflow ran and produced a checkable result; it
does not establish improved discovery rate. Standard mathematical ingredients
and the pre-existing phase gap mean novelty remains unestablished.

## Hardest useful next question

Derive an accessible-effect algebra from a specified causal-set observer or
instrument model, instead of stipulating one. A productive continuation must
justify preparation, reference choice, allowed coherent operations and
completed-history covariance together, or prove an obstruction for a clearly
declared class. Another unconstrained phase-gap example would not resolve
this physical bottleneck. This question is a future task, not a result of
the current pilot.
