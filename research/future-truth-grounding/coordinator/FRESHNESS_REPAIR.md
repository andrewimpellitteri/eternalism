# An explicit sufficient condition for fresh existence

27 October 2026. Elementary order-theoretic repair for our proposed
semantics. This is not a novelty claim or a verdict against Loss's intended
account. The adjacent dense-stage check shows why the formal condition
must be stated rather than inferred from domain inclusion alone.

## Principal-past condition

Let (W,≤) be a fixed partial order of possible event labels. For each
evaluation stage s choose an endpoint p_s and represent its event domain by
the entire principal past

    D_s = ↓p_s = {x in W : x≤p_s}.

Suppose stage precedence R implies proper domain inclusion:

    r R s  implies  D_r ⊊ D_s.

Then p_s is absent from EVERY R-earlier domain D_r. For if p_s∈D_r,
p_s≤p_r. Since p_r∈D_r⊆D_s, also p_r≤p_s. Antisymmetry gives p_r=p_s,
so the principal ideals are equal, contradicting strict inclusion.
Therefore p_s∈D_s is a fresh-existence witness at s on every stage-history
through s. The argument works on dense stage orders as well as discrete
ones; it needs no immediate predecessor and no linear global time.

Persistence also holds: x∈D_r and r R s imply x∈D_s. These are claims about
event-label domain membership. If the object language quantifies over
other entities as well, its typing and identity clauses must ensure that
event labels are legitimate stable witnesses; this lemma does not supply
a general ontology of persons, objects or properties.

## Relation to the dense insertion countermodel

In that model D_t=(-∞,t)∪{0} for t<0, ordered by the usual real order.
Although 0 is its latest member, D_t omits earlier labels between t and 0.
It is therefore not the full principal past of 0 in the union domain
(-∞,0]. This is exactly what the added condition excludes: an already
existing latest time cannot acquire previously missing earlier times.

The repair is stronger than bare domain growth. On a linear time order it
says each represented block is a complete prefix through its endpoint.
That fits the usual append-at-the-edge picture; it is not evidence that
the physical world actually has such a growing domain.

## Causal standpoint application and its limit

For a causal spacetime, set W=M with its causal order and p_s=b. Then the
proposed event domain J^−(b) is a principal ideal. Along b<c, these ideals
are strictly nested, and c is absent from every earlier domain. Thus this
particular event-relative interpretation has a fresh center at every
stage without relying on discrete births or a cosmic foliation.

But this is a standpoint poset, not automatically a tree of incompatible
possible growth stages. Two incomparable centers may both lie in a common
future center's past. The causal diamond in TWO_ORDERS.md shows why the
branching and causal orders must still be separated. This lemma repairs
freshness in one specified domain model; it does not provide branch
selection, a full tense language, truthmakers or an argument for passage.
