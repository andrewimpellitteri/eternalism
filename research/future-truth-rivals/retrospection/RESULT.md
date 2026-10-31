# Retrospective assessment of a future-tense utterance

Checked 27 October 2026. This is a bounded reconstruction of MacFarlane's
original clauses, not a full-paper validation or a theory of temporal ontology.

## Primary clauses inspected

John MacFarlane, “Future Contingents and Relative Truth,” *The Philosophical
Quarterly* 53(212) (July 2003), 321–336, DOI
[10.1111/1467-9213.00315](https://doi.org/10.1111/1467-9213.00315). I inspected
the author's 16-page offprint at
<https://johnmacfarlane.net/futcon-offprint.pdf>, including the original PDF
pages printed 322–332 (sections I–VI, selected passages). The inspected source
is the published 2003 offprint; publisher metadata confirms volume, issue, page
range, and DOI. The decisive semantic clauses are in §V, printed pp. 328–331.

The paper frames the problem using Jake's utterance at moment `m0` of “There
will be a sea battle tomorrow.” Histories `h1` and `h2` both pass through `m0`;
the battle occurs in `h1` and not in `h2`. MacFarlane explicitly says he does
not presuppose that objective indeterminism is true; he assumes only that talk
about the future would be coherent if it were true (§II, printed p. 323).

The original two-stage semantics is:

1. **Semantics proper:** evaluate the sentence at a point `(m,h)`. In the
   tensed language, `Will:φ` is true at `(m,h)` iff `φ` is true at some later
   moment on `h`; `Sett:φ` is true at `(m,h)` iff `φ` is true at `(m,h1)` for
   every history `h1` through `m` (§V, printed p. 329).
2. **Postsemantics:** evaluate an utterance-context `u` together with an
   assessment-context `a`. For double-time-reference postsemantics, `φ` is
   true (false) at `(u,a)` iff it is true (false) at every point `(m,h)` where
   `m` is the moment of `u`, `h` passes through `m`, and, if `a` is later than
   `m`, `h` also passes through the moment of `a` (§V, printed p. 330).

For Jake's utterance, MacFarlane gives the exact results (§V, printed p. 331):

| Utterance context | Assessment context | Result for the uttered sentence |
|---|---|---|
| `u=m0` | `a=m0` | Neither true nor false: both `(m0,h1)` and `(m0,h2)` remain relevant. |
| `u=m0` | `a=m1` on the battle history | True: only histories through both `m0` and `m1` remain relevant. |
| `u=m0` | `a=m2` on the no-battle history | False: only histories through both `m0` and `m2` remain relevant. |

The utterance is held fixed while its assessment changes. This is not the thin
red line: no unique continuation is marked as actual in the utterance context.
It is also not a three-valued assignment that simply changes with physical
time; assessment context is an explicit semantic parameter, and the truth
status at `m0` remains “neither” when assessed there.

## Correspondence with the project's persistence test

The coordinator's preliminary test fixes (i) one proposition `Q`, (ii) its
reference convention and laws, and (iii) a valuation `v_Q(s)` on complete
models. It asks whether equal proposed grounds force equal values of that same
`Q`. MacFarlane instead gives an utterance of a future-tense sentence a
two-context evaluation `V(φ,u,a)`, with a postsemantic range of points
depending on `a`.

The sea-battle case therefore supplies a **precise non-correspondence**, not a
counterexample to the fixed-`Q` criterion. At a fixed complete history, the
outcome proposition “a sea battle occurs at the named tomorrow” has a stable
value: true on `h1`, false on `h2`. MacFarlane's utterance-level result
additionally varies with `a`: at `m0` it is neither, and under later assessment
on the respective continuation it is true or false. To compare this account
with ground sufficiency, the signature and target valuation must preserve the
assessment parameter, or the comparison must explicitly project to a selected
assessment. Dropping `a` changes the target semantics; it does not show that
one fixed proposition changes truth value within a complete model.

Thus the exact example challenges an unconditional policy that assigns one
assessment-independent bivalent truth value to every future-tense utterance.
It does not challenge the weaker statement that a fixed proposition's value
factors through a sufficiently discriminating signature. A signature may
include the utterance context, assessment context, relevant histories, and
outcome facts; factorization then remains an extensional question. Such a
factorization alone says nothing about whether those facts exist at utterance
time or explain the truth in a grounding sense.

## Minimal semantic contract for a paired comparison

Use the following contract before testing truth/ground sufficiency:

- **Branching structure:** moments with a precedence relation and histories
  through each moment; the sea-battle toy has two histories sharing `m0` and
  diverging afterward. This is the paper's idealized branching-time setting,
  not yet a relativistic realization.
- **Utterance:** retain the actual speech act and its context `u=m0`; do not
  replace it with a new utterance in each alternative history.
- **At-point content:** interpret the future operator along a history, then
  evaluate the battle predicate at the relevant later point.
- **Assessment:** retain `a` as an independent parameter. The later-context
  postsemantic range consists of histories through both utterance and
  assessment moments; the present-context range includes every history
  through the utterance moment.
- **Truth status:** state whether truth is bivalent, gappy, or assessed-relative.
  For this example, reproduce the table above before applying any
  ground-sufficiency condition.
- **Ground question:** separately specify whether proposed grounds are indexed
  to utterance time, assessment time, or both, and whether they may include
  future outcome facts, laws, primitive selection facts, or the relevant
  histories. Do not infer a concrete growing-block ontology from the
  semantics.

## Source-backed alternatives and scope

MacFarlane's own proposal is double-context, assessment-sensitive utterance
truth under a branching-time semantics. A fixed-proposition comparison can be
run alongside it, but must remain a different target: hold the named event
and proposition fixed across complete models, then test whether the proposed
grounds distinguish models on which its value differs. An assessor-relative
extension can instead make `V(Q,u,a)` the target and require the proposed
signature to include or determine `a` and the relevant branch restriction.

The paper's semantic framework is neutral, by MacFarlane's account, about
whether objective indeterminism actually obtains and about whether any sentence
is assessment-sensitive; those are substantive choices in the application.
The sea-battle construction does not establish an open future in physics,
growing-block ontology, temporal passage, future-event nonexistence, or a
truthmaker theory. No physical model, formal proof audit, or later literature
survey was performed here. The author's current publications page notes that
he now regards the argument of this earlier paper as inadequate; that later
self-assessment is a lead for the coordinator's synthesis, not a refutation
established in this lane.
