# Calibrating specification burdens

Sole-worker analysis, 2026-10-21. Core input for the reframed article
(`paper/REFRAME.md`), responding to the external review's weak/strong dilemma.

## The problem

The draft says two things that pull apart.

- **Weak reading:** arguments should state their assumptions and not claim more
  than those assumptions establish. Nearly everyone accepts this; it is not yet
  a contribution to philosophy of time.
- **Strong reading:** before physics can favor a temporal ontology, proponents
  must specify an admissible realization, dynamics, probabilities, an
  operational interface, bridge principles and a comparison class. This is
  controversial: why should a structural or explanatory argument carry the same
  specification burden as an experimental likelihood comparison?

The draft oscillates between the two. The fix is not to repeat that assumptions
matter. It is to calibrate the burden to the **inference type**. Different
conclusions require different things to be specified; a single checklist
imposes the strongest burden everywhere and makes explanatory arguments look
defective by construction.

## Four inference types and what they require

| Inference | What must be specified | What may remain open | Failure mode |
|---|---|---|---|
| **Contradiction / exclusion** | The premises, the target claim, the logical form, and the relevance of each premise. A model or countermodel if the argument is semantic. | A full dynamics for every rival; empirical likelihoods; auxiliary motivations not used in the derivation. | Attacking a conjunction and concluding each conjunct fails; using a premise that assumes the conclusion. |
| **Likelihood comparison** | A common protocol, models with likelihoods, a prior over models/realizations (or an explicit marginalization), and a decision rule. | Realizations that are not in the comparison class, provided their exclusion is stated and justified. | Filtering out unsuccessful realizations and then reporting that all survivors fit; comparing models without a common protocol. |
| **Explanatory preference** | The explanatory virtue, the comparison class, the rival's best version, and what would count against the preference. | A complete physical realization of every rival; a quantitative likelihood. | Using an unstated virtue; choosing the virtue after seeing the verdict; treating a cost as a refutation. |
| **Admissibility judgment** | The ontology's constitutive commitments, permitted auxiliary changes, the eligibility evidence, and the rule for when a realization is excluded. | The full space of rivals; the final ontology verdict. | Relocating the disputed judgment into the checklist; treating preregistration as justification. |

This table is the calibration. It says: a contradiction argument needs logical
relevance, not a full dynamics; a likelihood comparison needs a protocol and
priors, not a complete metaphysics; an explanatory preference needs a defended
virtue and a comparison, not a complete rival realization; an admissibility
judgment needs constitutive commitments and a revision rule, not a verdict on
every rival.

## The weak/strong dilemma resolved

The strong reading is defensible only for the inference that actually carries
the evidential weight. If the paper claims that physics **favors** an ontology,
it owes a likelihood comparison or an explanatory comparison with a stated
virtue. If it claims that a package is **inadmissible**, it owes the
constitutive commitments and the exclusion rule. If it claims a **contradiction**,
it owes the premises and the logical form. It does not owe all four at once.

The paper's thesis should therefore be stated conditionally:

> When a physical result is used to favor or exclude a temporal ontology, the
> bridge and the realization class must be specified to the degree required by
> the inference being made — no more, and no less.

This is stronger than the weak reading (it imposes a real burden) and weaker
than the blanket strong reading (it does not demand a full realization for every
argument). It also explains why the article's case studies have different
shapes: Brading's existence bridge is an admissibility/explanatory argument;
LAGEOS is a parameter constraint; the clock example is a model-selection
diagnostic; the record example is a likelihood bookkeeping exercise.

## Eligibility versus discrimination

A separate distinction is needed:

- **Background evidence `D_0`** establishes which packages are eligible: they
  are consistent with known physics, have a defined dynamics and interface, and
  do not contradict established results.
- **Discriminating evidence `D_1`** compares the eligible survivors.

Filtering on `D_0` is legitimate, but it changes the evidential base. If a
package is excluded because it fails background evidence, the comparison among
survivors is not a comparison with the excluded package. The paper must report
the cost of the filter, not announce that all admissible survivors fit `D_1`.
Otherwise the argument commits a selection effect: the evidence that eliminated
the rivals disappears from the final likelihood.

A simple rule: state `D_0`, the filter, and the resulting comparison class
before computing `D_1`. If the filter is contested, report the comparison under
both the filtered and unfiltered classes.

## Preregistration is not justification

Preregistering a criterion prevents some post hoc moves, but it does not make
the criterion neutral. A criterion can be prejudicial before any result is
inspected. Conversely, revising an ontology after a physical discovery need not
be an illegitimate rescue: it can be a principled response to new evidence.

A principled revision should state:

1. what changed (the physical result, the auxiliary, the bridge);
2. why the change is licensed by the ontology's constitutive commitments, not
   merely convenient;
3. what else the change would affect;
4. whether the revised package still deserves the ontology's name;
5. what evidence would have counted against the revision.

Without (1)-(5), "revision" is indistinguishable from saving the phenomenon by
redescription.

## Application: Brading

Brading's case is an **admissibility/explanatory** argument, not a likelihood
comparison. The relevant burden is:

- state the constitutive commitments (law-constituted unity; system-relative
  present; P1*);
- state the eligibility condition (genuine subsystems exist; their sustaining
  regions are proper parts);
- state the bridge from presence to existence;
- state what would defeat the view (the universe is the only system).

The coverage objection shows that the bridge from presence to global existence
is missing. That is a legitimate admissibility criticism: it does not demand a
full likelihood model of every rival, only the missing premise. The reviewer's
point that the draft over-demanded specification is correct; the calibrated
burden is enough to make the criticism bite.

## Application: preferred-frame tests

LAGEOS is a **parameter constraint** on a named gravity model, with a
model-selection comparison against GR. It is not an admissibility or likelihood
comparison between ontologies. The calibrated burden is:

- specify the model and the parameter;
- specify the signal and the dataset;
- state the comparison class (GR vs Einstein-aether);
- do not claim an ontology verdict without an exclusivity bridge.

The draft's numerical detail is therefore not doing ontological work; the
correct treatment is a compressed parameter-constraint paragraph, not a central
case.

## Verdict

The weak/strong dilemma is resolved by replacing a uniform checklist with a
**burden table keyed to inference type**. The paper's methodological claim
survives in the conditional form: specify what the inference requires, and do
not pretend that a stronger demand is neutral. The claim is not that
specification is optional; it is that the required specification is
inference-relative.

This is a contribution to the paper's framework, not a new general theory of
evidence. Its test is whether it changes a verdict in the Brading case (it does:
the missing bridge is exposed without demanding a full rival dynamics) and in
the LAGEOS case (it does: the parameter bound is compressed and denied an
ontological verdict).

## Limits

- The table is a proposal, not a derived theorem. Its adequacy is judged by
  whether it handles the cases without begging the question.
- It does not settle which explanatory virtues are legitimate; it requires them
  to be stated and defended.
- It does not provide a decision rule for every disagreement about
  admissibility; it makes the disagreement inspectable.
- No empirical or ontological verdict follows from the calibration alone.
