# Does an unfinished process give growth an explanatory advantage?

31 October 2026. One comparative argument and one revision. This tests a
claimed explanatory advantage of a growing inventory over event realism;
it does not resume the retired constitution-to-exhaustiveness argument.
Coordinator construction with the separate bounded review below.
No new temporal ontology or historical originality is claimed.

## 1. The argument to test, and the relevant predecessor

Candidate argument:

1. A concrete operation is already occurring before its successful completion.
2. It can be slowed or interrupted without that erasing its earlier activity.
3. A process ontology can explain this by treating the operation as ongoing.
4. An event-realist account must identify it with its complete actual sequence
   of events, which could not have had different parts.
5. Therefore a growing ontology explains concrete process unity better.

Premise 4 combines three different commitments: a concrete event inventory,
reduction of a process to an aggregate, and essential membership of that
aggregate. An event realist need not accept the latter two. Moreover, a
process ontology need not have a growing inventory.

There is an exact prior warning. Stout's [1997 paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0202BDBD1098B0926F1F7FD85E876785/S0031819100056631a.pdf/div-class-title-processes-div.pdf),
printed pp22–23, says that interruption does not defeat a structured-stage
account whose identity is independent of its precise constituents. He then
offers a separate persistence argument. Steward's
[2013 author manuscript](https://www.researchgate.net/publication/269622255_Processes_Continuants_and_Individuals),
§6, manuscript pp32–35 and n18, develops form-based modal robustness while
retaining temporal parts, and makes the essentialist treatment of events
explicit. These are competing philosophical proposals, not settled premises.
Their inventory implications are not established by the passages read.

Our test is a concrete application of this known alternative. The distinction
between a process and its completed history is not a new project discovery.

## 2. An operation with an actual organizing mechanism

Use an ideal feedback-controlled liquid-filling device. A start signal at
t=0 latches an execution on. The level sensor compares the liquid height h
with the physically stored target h=1; reaching it closes the inlet. A cancel
signal also closes the inlet and ends the execution. The tank can hold more
than one unit: reaching one is the controller's target, not a capacity limit.

Let q(t)>=0 be a locally piecewise-continuous available inlet rate, with
local integrability required explicitly. Let cancellation time
C belong to [0,infinity], with C=infinity meaning no finite cancellation,
and set a(t)=1 for t<C and 0 afterwards. Normalize the initial height to zero.
Then

    Q(t) = integral_0^t a(s)q(s) ds,
    h(t) = min(Q(t),1),
    actual inlet flow = a(t)q(t) 1_{h(t)<1}  almost everywhere.

The ideal switching model is intentional; no smooth relativistic matter
realization is asserted. These equations describe the sensor/valve feedback,
not an observer's ability to reconstruct a trajectory from data.

Set T=inf{t>=0: Q(t)>=1}, with inf(empty)=infinity. A finite T is successful
completion provided it occurs before cancellation. For a simultaneous
completion/cancellation, record target attainment as well as cancellation;
this convention has no effect on the examples or integrals. The execution
is active for t<min(T,C). A zero-rate stall need not count as current liquid flow; controller
execution and flow activity are different predicates. The examples below
have positive flow until the stated stopping event.

Fix b=1/4. For all examples q=1 before 1/2, so the controller has started,
the valve is open and h(b)=1/4, with actual positive flow. There are three
admitted later input protocols:

| Protocol | Input after 1/2 | Cancellation | Outcome |
|---|---|---|---|
| A | q=1 | Never | Target reached at t=1 |
| B | q=1/2 | Never | Target reached at t=3/2 |
| C | q=1 | At t=1/2 | Execution ends with h=1/2; target never reached |

More generally, if q=r>0 after 1/2 and there is no cancellation,

    T(r) = 1/2 + 1/(2r),
    dT/dr = -1/(2r²).

These follow by solving 1/2+r(T-1/2)=1. Under cancellation at 1/2, Q and h
stay at 1/2, proving the noncompletion. The family is deterministic with its
full input protocol specified. Future external inputs differ; this is not a
same-complete-Cauchy-data example or an indeterminism result.

## 3. What unifies this operation, and what is still a premise

The candidate participation rule is physical and restricted:

> Stages belong to this execution when their inlet activity is controlled by
> the same enabled execution latch, level comparison and actuator path
> originating in the marked start, until completion or cancellation. A new
> start/reset begins a different execution.

Changing inlet pressure changes delivery rate and duration without changing
that control organization. This offers a reason to compare A and B as
alternative executions of the same initiated task. It is not just reuse of
a token name: the latch and feedback path causally organize the flow.

Across alternative worlds/protocols, the rule supplies a proposed counterpart
criterion. Calling the counterparts numerically the same metaphysical
individual requires a further identity principle. Neither the equation for
h nor an experiment settles strict transworld identity. This comparison
does not assume that all real processes are controller-governed, or that the
controller and its surroundings form a uniquely fundamental unity.

The explanandum is deliberately narrower than those claims: why the active
operation already has a material realization at b, how the control path
selects its participating flow, and how that execution responds to the
specified rate/cancellation interventions. It does not assume that every
temporally extended part is concrete from b.

## 4. A stronger event-realist replacement

An event realist can admit every actual occurrence and regard the operation
as the causally organized execution, with the participation and counterpart
rule above. Its actual realization includes the flow that actually occurs;
its identity/role across permitted interventions is not defined by retaining
every member of that actual realization.

This account explains the target using the start, material latch, sensor,
stored target, actuator coupling and flow law. It explains the timing change
by the integral, cancellation by the valve's causal control, and the continued
organization under rate changes by the unchanged feedback path. It does not
need to deny any future event's concreteness from b. Nor does it infer that
the later success must already have occurred by b.

The growing account can use the same mechanism. At b its inventory admits
the already actual start and current realization. It describes the future
operation tensedly; it need not quantify currently over future concrete
constituents. The proposal that the process is ongoing is compatible with
that inventory. No future-grounding requirement is imposed to explain the
current material latch or current flow.

This is a pair of restricted explanatory accounts, not a construction of
two complete rival metaphysics or a reconstruction of C&R's whole theory.
Both must still defend their interpretation of concrete existence. Within
this contract, the distinctive inventory policies do no additional work in
explaining the operation's physical organization or input dependence.

This replacement is stronger than matching one actual output history: for
every admitted nonnegative locally piecewise-continuous q and single cancellation
time, the integral, participation rule and causal control path are retained.
Thus the timing and interruption dependence are retained too. We have not
shown that causal sufficiency exhausts all metaphysical constitution.

## 5. One revision: distinguish explanation of the whole from listing its parts

The advocate can revise premise 4: listing each event, even with its local
cause, may not explain why those events make one operation. The event realist
therefore owes an account of organization, not merely a concrete inventory.
This is a fair demand. The replacement above answers it with the actual
control mechanism and an explicit participation rule; it does not answer
by saying that the future is determined from a state.

An open-loop replay makes the distinction concrete. Replace the sensor
feedback by a timed valve that closes at t=1:

    h_replay(t) = integral_0^min(t,1) a(s)q(s) ds.

For q=1 and no cancellation, feedback and replay have exactly the same liquid
height and inlet-flow history. Under protocol B, feedback reaches one at
t=3/2, while replay stops at t=1 with h_replay=3/4. A matching actual output
trace therefore does not supply the same organizing explanation. The devices'
internal control architectures differ: this is not a pair with all physical
events/fields fixed. Both inventory interpretations can recognize that
physical difference and preserve the intervention contrast.

This gives the revision a substantive answer: organized causal roles add
explanatory content beyond a list of outputs. It supplies no exclusive role
for a growing concrete inventory. The proposed organizing rule remains a
bounded operational criterion, rather than a complete metaphysics of unity.

## 6. What the interruption argument actually excludes

A limited modal lemma makes the failed identification exact. Assume:

1. P is literally the same process in two admitted worlds;
2. P is identical to a rigidly designated aggregate F;
3. every actual member of F is essential to F whenever F exists;
4. in the second world P exists without one of those members.

These are inconsistent, using the ordinary necessary-identity treatment of
rigid designators. The conclusion is that the package cannot stand. Giving
up essential membership, adopting counterparts instead of strict identity,
or denying that the process is this aggregate are distinct responses. The
lemma does not exclude temporal parts, event realism or all aggregate
accounts. It does not select a growing inventory. This is familiar modal
reasoning, not a new theorem; Steward n18 is particularly relevant.

Likewise, an entire process's being active at b does not imply that every
temporal part of its realization is present or concrete from b. Calling it
the whole operation can concern the subject whose state is active. Neither
side gets the disputed all-parts inventory inference from that wording.
Steward already identifies this particular happening/presence slide in §3,
manuscript pp15–16. This is a direct predecessor of the project's criticism
of the occurrence-presence bridge, not a new philosophical distinction.

## 7. Disposition and the changed philosophical target

The initial explanatory argument fails at premise 4 and at the transfer from
process ontology to inventory growth. The one revision correctly demands an
organizing explanation; the feedback construction supplies a rival answer
with the input dependence preserved. No exclusive advantage for either
inventory has been established for this explanandum. This is a completed
bounded comparison, not a verdict that the complete theories explain equally
well or that all ontologies are equivalent.

The positive content is a requirement on the process account: an account of
organization and of which alterations preserve the process, with its actual
physical support specified. Treating a process as merely a rigid actual
event collection is inadequate under the stated robustness principle.
Temporal inventory and this mode of process individuation are different
questions. The primary literature already contains the conceptual distinction;
our controlled example is an application, not a priority claim.

The next potentially discriminating premise concerns the status of the
organizing form: whether its constitutive role is fixed by the physical
mechanism and laws, or whether a further grounding/identity fact is needed.
If the latter, a rival must explain why that fact requires its temporal
inventory. This is a changed question, not another attempt to obtain an
exhaustive concrete present from the process's extent.

Sources/read depth are in `process-explanation-sources.jsonl`. The
[bounded independent review](../../agentic-philosophy/process-explanation-review/RESULT.md)
checks the equations, intervention comparison, counterpart/identity scope
and conditional modal lemma. The coordinator inspected its findings and
made the input/completion conventions explicit. Its source provenance is
inherited; the primary readings above are the coordinator's own. Acceptance
is limited to this comparison and the failed exclusive-advantage argument,
not complete explanatory parity or metaphysical sufficiency of the proposed
unity criterion. See PROCESS_EXPLANATION_REPORT.md for the disposition.
