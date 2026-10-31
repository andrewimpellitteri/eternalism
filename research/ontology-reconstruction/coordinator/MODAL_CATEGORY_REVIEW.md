# Modal-category submission: useful source work, bridge not accepted

30 October 2026. Coordinator review of isolated GLM commit `5ddb63d`,
task `ontology-modal-category-bridge`, based on `1d1102a`. The clean
submission and its root report remain preserved in that worktree/branch.
It is **in review**, not integrated or accepted. This note supersedes
any inference that a clean worker exit validates the conclusions.

## 1. The anti-trivialization argument fails

RESULT.md §§4.2 and 6 infer that admitting arbitrary regular cuts makes
the nomological box trivial or unable to track laws, and therefore that
a nontrivial box requires a maximal-world range. That inference is invalid.
Failure to determine every complete future state does not make the
necessity operator trivial, nor does it remove every dynamical constraint.

A simple counterexample to that inference uses an ODE, not a full C&R
semantics. Admit one history on R and histories on (−∞,τ), τ>0, each
satisfying x'=0 with x(0)=0. Interpret the test description D_t as including
the existence of time-label t and the cumulative x=0 data through t.
Let the box quantify over these admitted histories.

For any 0≤t<t′, a cut with t<τ<t′ matches D_t and lacks D_t′. Thus D_t
does not necessitate D_t′ for any such pair. Nevertheless every admitted
history satisfies the nonvacuous local constraint x'=0, and every included
point has x=0. Existence of label 1 is contingent across the histories.
The box has both valid and invalid contents; it is not a trivial operator.
This example does not defend these cuts as physically complete worlds.
It disproves the purported inference from universal full-state prediction
failure to modal triviality. Maximal-world admissibility needs its own
argument, as MAXIMALITY_AND_EXISTENTIAL_OPENNESS.md already maintains.

The worker's source attribution also reverses the p114 example's role.
Direct rereading of the user-provided chapter7 PDF, printedp114, confirms
that the authors bar future information from being inserted into the
held-fixed present description so as to restore determinism artificially.
They do not there supply a rule banning cessation alternatives from the
range of nomological possibility. The worker's P2 is not a consequence of
that passage. Its §6 bridge must be withdrawn in the submitted form.

## 2. A geometric inclusion corrects the database table

Let T be a temporal function on a time-oriented spacetime, b a mark,
t=T(b), and define

    C_t = {x : T(x)≤t},
    B_b = M \ (J⁺(b) \ {b}).

Then C_t⊆B_b. For if x∈C_t lay in J⁺(b)\{b}, strict increase of T on
nonconstant future causal curves would imply T(x)>T(b), a contradiction.
No field equation or maximality is used in this inclusion.

In Minkowski spacetime with T the inertial time and b=(0,0), the inclusion
is proper: x=(1,2,0,0) has T(x)>0 and is spacelike to b, hence belongs to
B_b but not C_0. This also illustrates why the point's causal past does
not coincide with either region.

Consequently the worker's §§3 and 8 assertion that the cumulative region
and bow tie are incomparable is false **under its own translation with
t=T(b)**. If the time and standpoint are not paired that way, a different
comparison has been chosen and must be stated. Region inclusion also does
not automatically show that an arbitrary realm isometry preserves a
separately chosen T; matching contracts and data identifications remain
necessary. The accepted smooth-class Cauchy-transport argument handles
its stated geometric matching contract, not a full source semantics.

## 3. Empty continuation is not terminal time

Direct rereading of printedpp115–116 distinguishes:

* gradeII′: later times exist but have no located entities other than
  themselves;
* gradeIII′: the specified later time and all still later times never
  exist.

The worker repeatedly puts both grades into its terminal-time Cat3.
That is incorrect: empty continued time is not a final included time.
In addition, the p111 last-moment assumption supports a particular
grounding explanation of negative future truths. It does not, without
further semantic argument, establish that every model of the gradeIII′
modal clause has a last included point. An open cut does not reproduce
that last-moment grounding story. The stronger claim that the grade
itself can never be interpreted by an open cut is not established here.

A singular end of a smooth MGHD also need not supply a last spacetime
event. Geodesic incompleteness, a final included moment and an externally
stipulated terminal boundary are different structures. A finite maximal
proper-time duration cannot simply be identified with the source's
terminal-time account.

The worker's assertion that gradeII′ has no relativistic analogue is too
strong. A bare events-and-fields encoding may not represent a distinct
time-container ontology. That is a limit of the encoding, not a theorem
excluding every carrier/content interpretation or every relativistic
empty-content proposal. Vacuum or vanishing scalar field is not by itself
the source's claim that only time entities are located there. A translation
must say which entities count; chapter9 was not directly reread by this
worker, and its full semantic reconstruction is not supplied.

## 4. What survives, under explicit bridges

The useful work is the separation of complete existence descriptions,
causal-past data and realm matching, together with the exact nomological
gloss and grades. A charitable physical encoding can add:

1. A chosen temporal function and paired standpoint, t=T(b).
2. A rule associating the source description with complete field and
   inventory data on C_t, including a full Cauchy slice.
3. A category of complete physical histories and field-preserving
   identifications of data and evaluation marks.

These are bridges, not clauses recovered from the field equations. Under
them, smooth MGHD uniqueness makes full Cauchy-data matching determine
the maximal development. In the selected complete scattering subclass,
the required central proper-time sample events also exist. Arbitrary
regular cuts are outside that subclass. This is a conditional physical
comparison, not a correspondence theorem for full ω_ex semantics.

The physical inputs do not select an ontological inventory. A maximal
mathematical history can support a growing interpretation. Source
existential alternatives may involve different existence-at expansions
of represented physics rather than deleted spacetime events; §8 of
CONSTITUTION_IS_NOT_PREDICTION.md explains why those operations must be
kept separate. Likewise, a center-normalized coordinate construction
must not be called a unique canonical temporal function without a
separate uniqueness argument.

## 5. Source depth and disposition

The worker reports whole chapter7 reading, selected Sbierski definitions
and theorem statements, selected primary Replies reading, and only
abstract/inherited LOY scope. These are its reports of access, not an
upgrade of coordinator reading. For the corrections above the coordinator
directly reread chapter7 printedpp111,114–116 using the supplied primary
PDF; earlier selected Replies reading remains as recorded. No source
quotation is needed for the two elementary counterarguments.

The finite script cannot resolve these objections: sampled time labels
cannot establish a continuum's last-point structure, and a finite table
of failed complete-state predictions cannot certify the anti-triviality
bridge. No new numerical test was run.

Required repair before acceptance: withdraw P2 and the resulting forced
maximality inference; correct cumulative/bow-tie inclusion; separate
empty continuation, absent later times and last-moment grounding; narrow
the claimed relativistic no-analogue result; preserve the full source-
to-physics translation gate. The submission's source extraction is useful,
but its proposed positive bridge is not accepted. Its unchanged original
and report remain recoverable at `5ddb63d`; no shared root report or
worker-owned output has been overwritten.
