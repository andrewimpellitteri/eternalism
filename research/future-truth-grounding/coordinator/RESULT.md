# What a complete local ground would have to distinguish

27 October 2026. Coordinator derivation and source-lane synthesis. This is a
research contract, not a proof of a temporal ontology. The elementary
factorization results below are standard set-theoretic facts; no novelty
claim is made. Manuscripts remain unchanged.

## The substantive correction to the preliminary challenge

The most promising question is no longer simply whether unreal future
events can be mentioned truthfully. Existing growing-block semantics can
do that, and some explicitly allow unsettled statements to lack current
truth values. Nor does rejecting truthmaker maximalism automatically
reject every supervenience principle about truth.

The sharper comparison is: **which differences between possible complete
models must a theory's existing grounds distinguish if those grounds are
to determine the truth values it promises?** This can be checked before
claiming that the grounds explain, rather than merely encode, those truths.

Three separate questions must remain separate throughout:

1. Is a proposed base extensionally sufficient to determine truth values?
2. Does that base actually exist, with the stipulated content, from b?
3. Does it explain the truths in the proposed grounding sense?

Our mathematical tests primarily address the first. An affirmative answer
does not answer the other two; a negative answer refutes sufficiency of
that specific base under the chosen truth policy.

## 1. Exact sufficiency criterion

Fix a set Ω of admitted complete models, a fixed standpoint b, a common
reference convention and fixed laws. Let R_b(s) be the stipulated past data
of model s, and let G_b(s) be its proposed complete ground signature. Include
fixed-law information in G if laws are allowed to vary between models.
“Signature” just records sameness/difference of candidate grounds; no
assumption that grounds are computer-readable is intended.

Let Q be one fixed proposition with designated-model truth

    v_Q : Ω -> {0,1}.

There is a function f_Q assigning Q's truth from the ground signature,

    v_Q = f_Q ◦ G_b,

if and only if

    G_b(s)=G_b(t)  implies  v_Q(s)=v_Q(t).                 (1)

Proof: the forward implication is substitution. Conversely, for any g in
the image of G, define f_Q(g) as the common value of v_Q on that fibre.
Condition (1) makes this well-defined. The domain can be restricted to the
image of G, so no choice of values on uninstantiated signatures is needed.

This is exactly the extensional supervenience requirement used in the
preliminary obstruction. It asserts neither that every truth has a
truthmaker nor that such a factorization is a grounding explanation.
For example, G_b(s)=v_Q(s) always factors Q but merely redescribes its
truth. G_b(s)=s likewise encodes the whole model without establishing that
the whole model exists from b or explains itself.

### Strictly past-local candidate grounds

If G_b factors through the past restriction R_b, then two models agreeing
on that restriction necessarily have the same ground signature. Thus Q
can have a past-local outcome-matching bivalent assignment only if Q is
constant on every past-data fibre. Conversely, if Q is constant on those
fibres, its truth has an extensional assignment from R_b itself. Whether
R_b is an admissible complete ground is a further philosophical question.

This makes the logical burden precise. A same-past/different-outcome pair
disproves past-data sufficiency. It does not prove that all existing
grounds in the rival theory are the same. Primitive lawmakers, powers,
selection facts or other extra structure must be compared separately.

## 2. A lower bound on additional discrimination

Within one past-data fibre C, suppose Q takes both Boolean values. Any
enriched signature adequate for Q must split at least those Q-true and
Q-false members; it cannot remain constant on C. This is a necessary
distinction, not a count of physical bits or a demand for future entities.

For a family of propositions, signatures must distinguish any two models
that disagree on any member of that family. If the family separates all
models in C, an adequate signature must be injective on C, up to whatever
observational/gauge identification the language intentionally ignores.
It need not encode them inefficiently: a short seed together with laws
can determine an arbitrarily complicated development. Functional
sufficiency is not ontological commitment to the determined events.

For scalar field models on fixed M, the predicates

    Q_(x,q)(s)  iff  φ_s(x)>q,       q rational,

separate real values at x: between any unequal real numbers lies a rational.
If all such predicates at all target points are included, equal valuations
imply equal target field configurations. A theory promising bivalent,
outcome-matching truth for this whole language, grounded in its signature,
therefore needs enough discriminative structure to determine that
configuration. One isolated future claim requires much less; do not infer
global-history selection from one truth value.

## 3. Direct application to the reviewed scalar model

Here Ω is ALL smooth real solutions of the same fixed linear equation on
the same closed-dust background. R_b is restriction to I^−(b). Because the
class is linear, a nonzero past-vanishing difference can be scaled and added
to any actual solution. At x outside the uniform fixing set F_m(b), the
attainable values over any actual-past fibre are all of R. Hence every
nonempty proper truth set of that one scalar value varies on that fibre.

Conditional on the internally reviewed positive-mass classification:

| Standpoint | Point-value fixing | Extensional consequence for this language |
|---|---|---|
| 0<τ_b<π | F_m(b)=J^−(b) | At each x outside J^−(b), no strictly past-local signature suffices for every nontrivial one-value predicate under outcome-matching bivalence |
| π≤τ_b<2π | F_m(b)=M | The past restriction determines the entire field solution; all its fixed-reference field propositions factor through that restriction |

The exact-threshold row follows from the reviewed sidecar, not from a new
proof here. This is an extensional sufficiency boundary. It supplies no
new account of what exists, why laws govern or whether truth must have
current grounds. All model members already use the same mathematical M.

Likewise, a common norm bound can make selected predicates constant in an
otherwise non-singleton class. The all-real conclusion uses unrestricted
scaling. Finite energy separately for each solution does not by itself
impose a common cap.

The interesting philosophical possibility is that a past-only ontology
could support all relevant future field truths at some standpoints but
not through the same *past-data sufficiency* policy at others. That is a
conditional challenge to a proposed policy, not an argument that truth
itself is born at maximum expansion or that all future claims are gappy.

## 4. What the three source/semantic lanes establish

### Strong growing-block reply

The growing-block lane checked Briggs–Forbes's selected supervaluation
clause and primitive-law framework in the original 2019 article. Their
chosen account gives indeterminate present values where feasible futures
disagree; it therefore declines the preliminary outcome-matching bivalence
premise for that case. Their lawmakers are not identified with a classical
causal-past field restriction. The local pair is consequently not a
refutation of this account. A stronger future comparison must supply an
actual relativistic realization of the account's grounds and feasibility.

### Truthmaking objection

The objections lane recovered Filomeno's author manuscript. Its challenge
to deriving truthmaker maximalism from ontology is relevant, but must not
be conflated with a refutation of (1). Maximalism, necessitation by a
particular maker, same-base supervenience and truthmaking at the utterance
time are different requirements. A bivalent growing-block rival may deny
current truthmaking or propose temporalized truthmaking. Our conditional
test must say which requirement it imposes and defend it independently.

### Stage-sensitive semantics

The tense/domain lane used Loss's original clauses to build a finite
counterexample: keeping today's quantifier domain fixed under a stage
shift prevents the quantifier from finding later-born objects. A domain
that tracks the evaluated stage repairs that specific failure. This is
semantic compatibility only, not an explanation of passage. A finite
terminal toy must not be claimed to validate perpetual-growth axioms.

A further dense-stage stress test matters for our own semantics: strictly
larger domains at later stages do not alone imply that each stage has an
entity which first exists there. The example

    D(t)=T(t)=(-∞,t) ∪ {0},        t<0,

has strictly increasing domains and a unique latest existing time 0, yet
every extant entity already appears at some earlier stage. An extension-
ordered past-function tree supplies multiple futures with these same
domains. It satisfies the displayed domain/time constraints while adding
new times below the fixed latest time. The detailed check is in
`../tense-domain/DENSE_STAGE_CHECK.md`.

This is a counterexample to treating the listed constraints as sufficient
for fresh existence at every stage. It is not an attack on an intended
append-at-the-edge interpretation, which may exclude this model. Our next
contract must state that extra requirement explicitly, including whether
timehood is an essential kind and when objects first enter the domain.

`FRESHNESS_REPAIR.md` gives a sufficient repair for an event-domain model:
make each domain the full principal past of an endpoint in one partial
order. Strictly nested principal pasts force the later endpoint to be
absent from every earlier domain, even with dense stage indices. This
does not impose a tree of incompatible stages or prove the proposed
domains actually exist.

The lane reports and their exact source locators are preserved in the
adjacent directories. Source claims and our arguments are distinct.

## 5. Relativistic transfer needs more care than anticipated

The coordinator's `../relativistic-branching/RESULT.md` provides two exact
tests. A travelling bump solves the deterministic 1+1 wave equation,
vanishes on b's whole strict past, and differs later. Thus our local-past
alternatives require no failure of Cauchy determinism.

Separately, the original branching-spacetime definition makes each history
upward directed. The full closed-dust M is not: simultaneous antipodal
events at τ=3π/2 would need a common future at τ≥2π, outside M. Therefore a
literal, order-isomorphic identification of each full dust solution with
one such history fails. This does not refute branching-spacetime theory;
it identifies a representation requirement for our specific cosmology.
The inference requires an onto identification; proper-subset embeddings
are not excluded. Placek's 2011 continuation-based semantics is a direct
prior-work lead for this already recognized GR/directedness problem; its
full construction is not checked in this round.
Placek's 2014 *Branching for General Relativists*, introduction p.192,
directly confirms the known limitation and proposes generalized histories.
The introduction was checked; the proposed repair still needs a specific
dust-model correspondence audit.

For now use a family of solutions and restriction maps as the neutral
formal baseline. A separate definition is needed if histories must cover
all of these finite-lifetime geometries. Adding an ideal future endpoint
or changing compatibility may be useful, but the resulting model must
show which causal and horizon facts it preserves.
A single adjoined final event also conflicts with the cited framework's
no-maximal-events condition, so it is not by itself a complete repair.

## 6. A focused next result and its failure conditions

The next substantive task is a comparison of TWO complete interpretation
contracts for the same neutral model:

* A bivalent, outcome-matching interpretation with explicitly identified
  grounds, their temporal status and a non-circular reason they suffice.
* A stage/domain interpretation that specifies which future statements
  are gappy, quantifier/tense shifts, retrospective reporting and what it
  means for its modal alternatives to be physically or metaphysically open.

Require both to accommodate the exact travelling-wave example, the
closed-dust lack of common futures, and the distinction between finite
energy and a uniform norm bound. A familiar preferred global foliation is
a legitimate rival addition; it must be stated as an extra physical or
philosophical premise, not quietly ruled out by a metric-only theorem.
The stage interpretation must also exclude or intentionally accommodate
the dense insertion counterexample; proper inclusion alone is insufficient
for the stronger fresh-at-each-stage axiom.

`TWO_ORDERS.md` supplies a neutral evaluation baseline with separate
causal-advance and past-agreement relations. It also exhibits a particularly
clear separation in the reviewed dust model: the proposed J^− event domain
can continue growing after the past-agreement classes have all become
singletons. Hypothetical ontological addition and resolution of field
alternatives are therefore distinct even inside one explicit construction.

Success means either a genuine obstruction under independently motivated
premises or a precise residual disagreement about grounds and passage.
If both simply decorate the same truth structure, report that limitation
and seek an explanatory discriminator. A translation, a factorization or
a vote among agents cannot establish metaphysical equivalence or choose
the better ontology.

## Acceptance scope

This round accepts bounded source reconstructions, explicit elementary
semantic/causal checks and the clarified research contract. It does not
accept a philosophical theory, priority claim, complete rival refutation,
new physics prediction or manuscript revision.
