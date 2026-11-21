# Causal production, law variation and temporal actuality

31 October 2026. Coordinator philosophical investigation; selected primary
reading, one worked objection and one recovery. No novelty or settled-ontology
claim. This does not revive the stopped occurrence-to-exhaustiveness family.

## 1. The argument we actually need to answer

Tooley's argument is not an analysis of causation as making a nonexistent
effect exist. His own backward-causation discussion rejects that shortcut.
The substantive route goes through causal laws and logical probability.

Direct source: *Time, Tense, and Causation* (1997), §§3.2.3.4, 4.4–4.6;
printed pp57–61, 101–117. The supplied PDF has printed-page offset +17.
The book is locally supplied and ignored by Git; its hash and exact reading
depth are recorded separately. These are paraphrases, not quotations.

Let L be the proposition that P is causally sufficient for Q, and let C
contain only tautologies or information about causal laws. Tooley's Prob is
logical probability on evidence, not a detector frequency, an intervention
operator or automatically a physical chance. The central conditions are:

    (C1) Pr(P | L,C) = Pr(P | C).
    (C3) Pr(Q | not-P,L,C) = Pr(Q | not-P,C).
    (C4) Pr(Q | L,C)
           = Pr(P | C) + Pr(not-P | C) Pr(Q | not-P,C).

C2 is the corresponding decomposition before using C3. Causal sufficiency,
the probability calculus, C1 and C3 yield C4. A mere biconditional connection
between P and Q does not decide which marginal should change when the law is
learned. The directional causal-law postulates are intended to decide it.

The argument has two stages (§4.5, pp103–111):

1. Familiar highly organized effects should not be treated as innumerable
   unexplained improbable accidents. Tooley argues that causal laws with these
   probability properties explain them, and so we have reason to accept such
   laws. This is an explanatory argument; its uniqueness claim needs defense.
2. In an equally real whole history, he argues, preserving the cause when a
   law is added has no better rationale than preserving the absence of the
   effect. In a growing world, the cause is already actual and the effect or
   its absence is not. Law plus what is actual generates what is added.
   This is offered as the needed explanation of C1/C4, not merely a new way
   to calculate their values.

There is a further selection step. Postulates I–VI (§4.6, pp112–116) connect
occurrence, causal priority/posteriority, simultaneity and transmission of
actuality/nonactuality. With an appropriate causal linking of times, they yield
the past-and-present inventory (§4.6.2, pp116–117). They are not all derived
just from the probability equations. The simultaneity clause also matters:
this is not already a theorem selecting a relativistic pointy realm.

The book's own actuality framework is more nuanced than “only what is now
concrete can be quantified over”. §§2.2.1–2.2.2, pp37–42 distinguish actuality
simpliciter and actuality as of a time, retain both primitives for this dynamic
account, and acknowledge a modest simplicity advantage to the static account,
other things equal. Thus the existence of a mathematical whole-history
representation is no objection by itself.

## 2. A source-faithful disagreement

The best rival grants substantial disputed resources for this test: real
directed causal relations, governing laws, modal dependence and explanations
that distinguish causes from effects. It need not accept a Humean reduction,
derive direction from entropy, or identify causation with correlation.

It denies this further claim:

> A directional difference in what can change when laws vary can be justified
> only by a directional difference in what is actual as of a time.

Call this the proposed bridge, not a premise Tooley states in exactly these
words. It isolates the necessity claim in §4.5.3. Equal actuality does not entail
equal causal roles, exchangeability under a prior, or equal resilience under
law changes. A root condition and a dependent outcome can both exist while
having different modal roles. Calling the dependent outcome actual does not
make it counterfactually indestructible: law counterfactuals compare different
worlds, rather than remove events from the actual world.

This reply alone is insufficient. It must say what the modal asymmetry amounts
to and why accepting it is preferable to the growing explanation. Simply
writing down a directed graph does not earn that account. The following small
model locates the burden more precisely.

## 3. A finite consistency check, with the probability limitation exposed

Let X,Z,K be independent binary variables, with probabilities p,q,r in (0,1).
K marks whether a proposed additional X-to-Y law is present. Define

    Y = Z OR (K AND X).

X is the potential cause, Z an independent background route, and Y the effect.
This is a stipulated family across alternative law settings, not a claim that
laws are literally switches in a laboratory. If K=1, X is sufficient for Y;
if X=0, the background route is unchanged. All valuations can be interpreted
as complete histories with both event slots. No varying existence predicate
is used to obtain the following identities:

    Pr(X=1 | K=1) = p = Pr(X=1),
    Pr(Y=1 | X=0,K=1) = q = Pr(Y=1 | X=0),
    Pr(Y=1 | K=1) = p + (1-p)q.

These reproduce the displayed C1/C3/C4 algebra for this one background context.
The equation assigns the directed input role to X; independence of K from X,Z
holds the exogenous distribution fixed across the tested law change. Those
features are assumptions of the comparison, not consequences of equal reality.
For p=q=r=1/2 the last value is 3/4. The unconditional Pr(Y=1) is 5/8, so
learning the law changes the effect marginal and leaves the cause marginal
unchanged. The putative reverse expression from §4.5.3, C4*, gives

    Pr(not-Y) + Pr(Y) Pr(not-X | Y) = 3/8 + (5/8)(2/5) = 5/8,

whereas Pr(not-X | K=1)=1/2. Thus ordinary probability and a complete-history
interpretation do not force C4* alongside C1/C4. The joint distribution already
distinguishes their roles. Statistical learning of X from Y, which may be
mutual, remains a different issue from learning the law K.

**Limits are decisive.** This is a finite probability measure stipulated over
a selected model family. It is not Tooley's canonical logical probability over
all relevant metaphysical possibilities, does not justify that measure from
tautological evidence, and does not prove the postulates for every permitted C
or every causal law. It is not a reduction or full analysis of actual causation.
It defeats a proposed *bare algebraic* impossibility argument, not the author's
complete explanatory or logical-probability argument. A non-Humean rival may
interpret the direction as real, but that interpretation remains a proposal.

The [bounded native audit](../../causal-production-review/RESULT.md) independently
checks these calculations and requires the stipulated direction/invariance
qualification at this exact point. It does not certify the complete
logical-probability or explanatory argument.

The construction uses familiar modular dependence and finite probability.
Tooley's own §§4.1 and 4.5 already pose the law-variation problem. Structural
causal modelling is a nearest prior, not our invention; the Pearl source
found here was inspected only at abstract/discovery depth. No novelty is
claimed for the model or the cause/effect-versus-correlation distinction.

## 4. Why growth alone does not supply the missing probability premise

Keep the same slots and equation, but allow

    Pr(X=1 | K=0)=1/4,
    Pr(X=1 | K=1)=3/4,
    Pr(K=1)=1/2.

Take Z independently with probability 1/2. Then Pr(X=1)=1/2, while
Pr(X=1 | K=1)=3/4, so C1 fails. Each selected history can still be assigned
a growing inventory that includes X's slot first and Y's slot later; causes
are actual before effects and past slots persist. That inventory assignment
does not change the probabilities.

This does not describe a Tooley causal law satisfying his definition: C1 is
precisely one of its intended conditions. Nor does it refute his full growing
account, which also invokes governance. It demonstrates only that the bare
inventory pattern leaves cross-law root probabilities unconstrained.
In particular, persistence within each growing history does not by itself
establish the cross-world rule that a root fact remains unchanged when a law
varies. The latter needs a modal comparison rule in either interpretation.

## 5. One recovery: actuality grounds the modal comparison

The stronger growing reply is that actuality is not merely an extra label on
an otherwise complete stochastic history. What is already actual constrains
how the world can develop. That is precisely why the cause, rather than the
absence of a future effect, should be held fixed in the law counterfactual.
Treating the rival as needing only the same numerical predictions misses the
explanatory ambition. The present argument must answer that ambition.

There are two questions to separate:

1. **Within a given lawful history:** what has happened is not subsequently
   erased as the world develops. This is the growing theorist's persistence
   claim, not the claim that a cause could not have failed to happen.
2. **Across alternative laws/histories:** the chosen cause distribution, or
   individual causal background, stays fixed while the downstream mechanism
   changes. This is the comparison needed for the probability/law argument.

The first does not entail the second. All the candidate worlds may grow,
while disagreeing about which cause occurred or about its probability, as
§4 makes explicit. An additional principle must specify which actual facts
are held fixed under the relevant law change, and why that comparison is
privileged. Tooley's §4.1 motivates preserving earlier history up to forced
divergence; his §4.5 proposes actuality as its rationale. That is an argument
to assess, not a missing sentence we can dismiss as a fallacy.

The equally serious rival instead takes directed causal autonomy or governing
dependence as the reason to preserve the root and recompute its descendants.
It must justify autonomy and the permitted law change. It is not enough to
choose a factorization of an observed distribution, because a distribution can
have multiple factorizations. With genuine directional causal structure as
part of its account, however, equal reality supplies no further argument that
the rival's modal comparison must be symmetric. The growing account has not
yet shown why its actuality basis is uniquely adequate, and the rival has not
yet shown its own basis superior in every respect.

**Disposition of this recovery:** retain a live explanatory dispute over the
ground of modal asymmetry. Reject the inference that equal reality alone
precludes it, and reject an appeal to bare growth as sufficient for C1.
The finite consistency check supplies no overall ontology ranking.

## 6. What changes philosophically, and the next serious test

Our previous project framing was incomplete. A growing theorist can offer an
argument for an upper bound through an account of causal laws, not only add
an arbitrary “that's all” clause after a constitutive lower bound. The task is
to evaluate that account's necessity and explanatory merit. Conversely, a
failure to derive inventory from a process's parts does not address this route.

The useful next question is more specific than whether a block can “produce”:

> What warrants holding a cause or its prior distribution invariant when a
> causal law is added, and does primitive temporal actuality provide a better
> ground for that invariance than a real directed governing relation?

This is not a newly discovered philosophical problem; it is the source's own
law-counterfactual challenge made explicit for our comparison. One next test
should use a concrete pair of non-Humean accounts, rather than a Humean foil,
and include cases where the changed law constrains the proposed root as well
as its descendants. Neither account may simply assume every desired law
change leaves that root possible. A claimed logical-probability result must
also state the admissible evidence class and justify its measure, not substitute
an empirical conditional or an intervention probability.

The 2024 and 2025/26 Tooley treatments were found at abstract depth only and
could alter the strongest current formulation. Mellor's 1998 review was found
but its full text could not be fetched; no objection from it is reported as
read. These are real source gates on a broader verdict. This selected reading
closes the earlier “causal argument unread” gap for the specified 1997 passages,
not for the entire book or its subsequent literature. No outside expert has
reviewed this investigation.
