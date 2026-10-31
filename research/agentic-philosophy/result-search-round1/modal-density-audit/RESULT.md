# Non-total is not non-dense: a counterexample to modal nontriviality

31 October 2026. Coordinator proof and repair of GLM submission
`7e58c31e449a19f7b6d66b4fb00247e8da466b5f`. The motivating rational comb was
specified in the coordinator's question card before the worker ran. This
note adds a parameterized calculation, repairs an offshoot calculation and
limits the claim to the journal's abstract order axioms. Priority is open.

**Result:** under the necessary nonempty-chain convention, the rational
comb satisfies Definition6 of Müller2019/2020, is not featureless, and has
identity co-presentness on one whole history. It therefore defeats that
paper's Theorem1 in its written hypothesis class. This is a result about
an abstract branching order, not a counterexample within a class of
physically realized relativistic manifolds.

More generally, in the comb family below, absence of a branching point
at some moments is insufficient: for the trunk to have any non-singleton
present, the branching set must fail to be **dense**. This exact statement
is restricted to this family. It is not a proposed universal BST repair.

## 1. Exact target and conventions

The primary [journal article](https://link.springer.com/article/10.1007/s10701-019-00267-x)
defines BST in Definition6 by density, absence of endpoints, chain infima,
history-relative chain suprema and prior choice. Histories are maximal
directed sets (Definition7). Co-presentness is equality of CC sets
(Definitions8–12). Its Theorem1 asserts non-identity and non-universality
on every history of a structure outside its two featureless cases.

All chain clauses here concern **nonempty** chains. Reading Definition6
as including the empty chain would require a greatest element as its
infimum, contradicting the no-maxima clause in every intended model.
The construction does not exploit that vacuity or present it as a separate
objection to the theorem.

## 2. A comb for any branch set D⊆ℝ

Use a real trunk and a disjoint real offshoot above each d∈D:

    W_D = ℝ_T ⊔ ⋃_{d∈D}(d,∞)_d.

Each copy has its usual strict real order. Across copies set

    t_T < r_d iff t≤d<r,

and make no other comparisons. A trunk event is never above an offshoot.
The possible histories are

    h_T=ℝ_T,
    h_d=(−∞,d]_T ⊔ (d,∞)_d,   d∈D.

These are exactly the maximal directed sets. Events on different offshoots
have no common upper bound. Nor do an offshoot event above d and a trunk
event above d. A directed set with an offshoot event is consequently
contained in that h_d; a trunk-only set is contained in h_T. Each listed
set is directed and cannot be enlarged. Every event belongs to one.

Each history is order-isomorphic to ℝ by its numerical coordinate. This
also establishes density, including at a branch join, and absence of both
maxima and minima. The declared comparisons give a strict partial order.

## 3. Every Definition6 clause holds

**Global infima.** A chain can use at most one offshoot. If it is trunk-only
and lower bounded, its real infimum α gives the global infimum α_T; an
offshoot cannot be a lower bound of a trunk event. If it has offshoot-d
events and any trunk event, its infimum is again a trunk event at the real
infimum of its coordinates. If it consists wholly of offshoot-d events,
let α be their real infimum. For α>d use α_d; for α=d use d_T. These are
greatest among all lower bounds in W_D. The case α>d does not require
the infimum to belong to the chain.

**History-relative suprema.** If a chain X⊆h is upper bounded in W_D, its
numerical coordinates are bounded above. For a trunk-only X, any global
offshoot upper bound above d already forces every coordinate of X to be
at most d. For X containing offshoot-d events, every upper bound must lie
on that offshoot. The real supremum β therefore supplies an event of h
via its order isomorphism with ℝ, and is the least upper bound within h.
No global least upper bound across incompatible histories is assumed.

**Prior choice for all chain cases.** Distinct histories meet in a trunk
segment with maximum m_T:

    h_T∩h_d=(−∞,d]_T,
    h_d∩h_e=(−∞,min(d,e)]_T,   d≠e.

Every event in either history difference is strictly above that maximum
in its own history. Thus m_T is strictly below every member of any
nonempty O⊆h₁\h₂ and is maximal in h₁∩h₂. This verifies the required
lower-bounded-chain version, indeed a stronger statement. When d<e,
h_e\h_d includes both (d,e]_T and the e-offshoot; neither part is omitted.

For common chains, history-relative suprema also coincide as trunk events
at or below m. Thus the order of such suprema is preserved across histories,
satisfying the Weiner condition as stated in Müller2005, Postulate4, p513.
The journal explicitly omits that extra postulate; adding it would not
exclude this comb. No larger original-postprint axiom audit is needed for
the present target or claimed here.

## 4. Compute the official co-presentness relation directly

The containing-history sets are

    H(t_T)={h_T}∪{h_d:d∈D,d≥t},
    H(r_d)={h_d}.

For each d∈D, histories at d_T have exactly two immediate outcome cells:

    B_d={h_T}∪{h_e:e∈D,e>d},     A_d={h_d}.

Different members of B_d are undivided at d_T; h_d splits from all of B_d
there. All and only the branch events d_T are choice points.

For a trunk event t_T, its outside histories are precisely h_d with d<t.
Each splits from every history in H(t_T) at d_T. Conversely splitting
from h_T forces any proposed cause-like locus to be that d_T. Hence

    cll(t_T)={d_T:d∈D,d<t},
    CC(t_T)={(d_T→B_d):d∈D,d<t}.

For an offshoot event r_q, the containing-history set is the singleton
{h_q}. Outside histories h_d with d<q split from it at d_T; h_T and
histories with branch later than q split from it at q_T. Therefore

    cll(r_q)={d_T:d∈D,d≤q},
    CC(r_q)={(d_T→B_d):d∈D,d<q} ∪ {(q_T→A_q)}.

The earlier continued transitions **must be included**. For example,
h₀ witnesses 0_T∈cll(r₁) when 0,1∈D and r>1. Definition8 requires an
outside-history witness, not splitting from every outside history. Both
the GLM handback and the first native review missed this quantifier;
the corrected formula leaves the trunk counterexample intact.

Consequences follow without invoking Fact4's general characterization:

1. For s<t, CC(s_T)=CC(t_T) iff D∩[s,t)=∅.
2. All events on a fixed offshoot share CC, including its departure
   transition, and cannot be co-present with a trunk event or another
   offshoot. The whole h_q still includes prebranch trunk points.
3. For D≠∅, each offshoot history has a nontrivial relation: its tail is
   a multi-event class, while q_T has no q-departure transition and hence
   belongs to a distinct class.
4. On h_T the relation is identity iff D is dense. It is universal iff
   D=∅. Thus for nonempty proper D, **all histories have a nontrivial
   relation exactly when D is not dense**.

## 5. The journal counterexample and a second case

Take D=ℚ. There are many histories, so featureless case(i) fails. The
trunk contains irrational non-choice events; every offshoot history also
has non-choice events. No history consists wholly of choice points, so
case(ii) fails irrespective of modal-correlation details. Nevertheless
every nonempty real interval contains a rational, and §4 gives identity
co-presentness on h_T. This contradicts Theorem1's universal conclusion.

Take instead D={1/n:n≥1}. Then all trunk times t≤0 have the same empty
CC set and form the class (−∞,0]. Each gap (1/(n+1),1/n] is another
multi-event class. This is a second exact calculation using the same
criterion. We claim no continuity or instability under “arbitrarily
small” changes: no metric on models or perturbation map has been supplied.

The distinction exposed is D≠ℝ versus non-density of D. A non-choice
moment need not have any interval of indeterministic quiet around it.
The literal weaker BT assertion that *somewhere* there is a multi-moment
present is not refuted by the rational comb: its offshoot tails supply
such presents. The target is the journal's every-history theorem.

## 6. Philosophical, later-literature and priority boundaries

This formal counterexample shows that the journal's stated assumptions
do not ensure an extended present along every history. It does not show
that indeterminism is physically dense, that sparseness is independently
established, or that no other modal construction can ground an extended
present. It does not establish eternalism, presentism or objective passage.
The comb has no incomparable-but-compatible event pairs and no demonstrated
higher-dimensional relativistic manifold representation.

The later Belnap–Müller–Placek monograph's Theorem10.1, printed p359,
uses **BST_NF**, not the journal's Definition6 class. Direct selected
reading of Definition3.15 and Fact3.17, pp62–64, confirms that BST_NF
admits no choice points, whereas this comb has them. Therefore this
construction does not refute that later theorem. We have not independently
audited the worker's proposed transformed NF example or a full repair
theorem. We do not call that later formulation a proven correction.

The scope difference is material to significance and priority. Bounded
search found no located correction of the journal statement; that is
not evidence of exhaustive coverage or of a new discovery. Earlier dense-
indeterminism literature and possible implicit corrections remain to audit.
The result is presently an internally checked correction candidate with
a complete proof in its bounded class. External communication and a
historical-originality claim are separate, unperformed steps.
