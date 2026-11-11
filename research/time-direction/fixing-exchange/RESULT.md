# What is conserved between past and future: reciprocity and the balance of openness

10 November 2026, second version the same day. Coordinator session (Claude Code,
Fable 5.2), at the user's request. Self-reviewed only: [REDTEAM.md](REDTEAM.md) records
the attack on the first version, what it removed, and what replaced it. The
mathematics is elementary and none of it is claimed as new mathematics. Proofs were
checked by hand, and [check_exchange.py](check_exchange.py) checks them on small finite
models. No temporal ontology is selected. Priority is not claimed (§9).

Target: §`sec:direction` of
[What the Past Can Fix](../../what-the-past-can-fix/main.tex), the open item in
[ARROW_DISPOSITION.md](../../ontology-reconstruction/coordinator/roadmap-audit-2026-10-31/ARROW_DISPOSITION.md),
and the "open past" thread of the
[Markovian-presentism lane](../../ontology-reconstruction/coordinator/markovian-presentism/RESULT.md).

## 0. The claim in one paragraph

The paper asks which events a base fixes. That question has asymmetric answers, and
the paper's sentence "under equal bases each side is as fixed or unfixed from the
other" is false at a single standpoint in the paper's own closed dust model. Ask
instead which *quantities* one region fixes about another. Then three things hold for
every class of histories, with no symmetry assumed:

1. **Reciprocity.** What region A fixes about region C is the same set of quantities
   as what C fixes about A.
2. **Balance.** The openness of C given A, minus the openness of A given C, equals the
   information in C minus the information in A.
3. **So an arrow of openness is an information imbalance between the two bases, and
   nothing else.** It has exactly four possible sources: the geometry of the bases, a
   many-to-one law, a selection of solutions, and a non-stationary chance
   distribution.

Two consequences are stated as results. In the closed dust model the past is fixed
and the future open at every standpoint before maximum expansion, and the reverse
after it, and the cause is the first source (§4). In a stationary world, lawful
indeterminism makes the past exactly as open as the future at every finite
resolution (§5). The second bears on any view that grounds past truths in the present
and the laws.

## 1. Setting

M is a set of events. A **class** 𝓛 is a set of functions on M (the lawful
histories). For a region A ⊆ M, a **quantity of A** is a function on 𝓛 whose value
depends only on the restriction of the history to A. Write Q(A) for the set of these.
The paper's fixing operator is

    F(A) = {x : the reading at x is in Q(A)}.

So F records which point readings A fixes. Q(A) records everything A fixes.

## 2. Reciprocity

**Definition.** A quantity of C is **fixed by A** if it is also a quantity of A.

**Proposition 1 (reciprocity).** For any class and any regions A and C, the quantities
of C fixed by A are the quantities of A fixed by C. Both are Q(A) ∩ Q(C).

*Proof.* The definition is symmetric. ∎

This is a tautology, and the point is that the question had been asked of the wrong
object. Its content appears when it is combined with what is *not* symmetric:

- F(A) ∩ C and F(C) ∩ A are sets of events and need not match in any sense. A point
  reading in C may lie in Q(A) ∩ Q(C) while the matching quantity of A is not a point
  reading.
- "A fixes everything about C" means Q(C) ⊆ Q(A). That is not symmetric. It says C
  is a coarsening of A.

**Proposition 2 (linear form).** Let 𝓛 be a vector space V of real functions, or a
translate of one. Let K_A be the members of V vanishing on A. Then

    Q(A) ∩ Q(C) = functions on V / (K_A + K_C),
    open(C | A) := the freedom left on C once A is given ≅ K_A / (K_A ∩ K_C),
    open(A | C) ≅ K_C / (K_A ∩ K_C).

*Proof.* A function on V is in Q(A) exactly when it is constant on cosets of K_A. A
function constant on cosets of K_A and of K_C is constant on cosets of K_A + K_C. The
freedom on C given A is the image of K_A under restriction to C, whose kernel is
K_A ∩ K_C. ∎

## 3. Balance

**Proposition 3 (balance, linear).** If the spaces are finite-dimensional,

    dim open(C | A) − dim open(A | C) = dim V|_C − dim V|_A.

*Proof.* The left side is dim K_A − dim K_C, and dim V|_A = dim V − dim K_A. ∎

**Proposition 4 (balance, probabilistic).** Let μ be a probability measure on 𝓛 and
let a, c be discrete readings of A and C with finite entropy. Then

    H(c | a) − H(a | c) = H(c) − H(a).

*Proof.* Both sides equal H(a, c) − H(a) − [H(a, c) − H(c)]. ∎

Proposition 4 is the chain rule of entropy and Proposition 3 is rank arithmetic. The
use made of them here is the reading: **the future is more open than the past, given
each other, by exactly the amount by which the future's description is longer.** The
shared part I(a; c), or dim V/(K_A + K_C), drops out of the difference.

**Corollary 5 (four sources).** An asymmetry of openness between A and C requires
info(C) ≠ info(A). For lawful histories that can arise only from:

| Source | What makes the two descriptions unequal | Example |
|---|---|---|
| Geometry of the bases | One base contains a Cauchy surface or more of one | §4 |
| A many-to-one law | Evolution of the chosen readings loses information one way | Relaxing macrodynamics; shocks |
| A selection of solutions | A boundary condition restricts one side more | A low-entropy past condition |
| Non-stationary chance | The entropy of the description changes in time | §5 |

A linear law with none of these has no asymmetry of openness at any pair of equal
bases. Time-reversal invariance is not needed for that conclusion, and the heat
equation satisfies it wherever backward uniqueness holds (standard classes; cited as
known, not checked here).

## 4. The closed dust model has an arrow of exact fixing, set by epoch

Take the paper's closed dust model and a massive linear field (m > 0), with
A = I⁻(b), C = I⁺(b) and τ the conformal time of b. For the massless conformal field
the fixed sets before the midpoint include the paper's extra diamonds, but they are
still not everything, so the table below is unchanged.

- Theorem `thm:massive`: F(A) = J⁻(b) for τ < π and F(A) = M for τ ≥ π.
- The reflection η ↦ 2π − η and Proposition `prop:mirror` give F(C) = M for τ ≤ π
  and F(C) = J⁺(b) for τ > π.

**Corollary 6.** In that model, with these linear fields:

| Standpoint | K_C | K_A | Past given future | Future given past |
|---|---|---|---|---|
| τ < π | 0 | ≠ 0 | Fixed entirely | Open |
| τ = π | 0 | 0 | Fixed | Fixed |
| τ > π | ≠ 0 | 0 | Open | Fixed entirely |

So at a single standpoint before maximum expansion, with one law and equal bases, the
past is fixed and the future is open in the exact sense of the paper's own operator.
After maximum expansion it is the reverse.

This is a reading of results the paper already has. The paper draws the opposite
moral from them: "exact fixing has no arrow of its own. Under equal bases each side is
as fixed or unfixed from the other." The first sentence is right about the *law* and
the second is wrong about the *model*. The corrected statement is Corollary 5: the
law contributes no arrow, and the model has one because the future cone of an early
event contains a Cauchy surface and its past cone does not. Balance says how large it
is: the whole of K_A.

This arrow has nothing to do with entropy. It points toward the temporally larger
side of the universe. It reverses at the midpoint. It exists in a universe whose law
and whose geometry are both time-symmetric.

## 5. Stationary chance: the past is as open as the future

Let (X_t) be a stationary stochastic process of discrete states. "Stationary" means
that the joint distribution of any block is unchanged by time translation. The
dynamics may be irreversible.

**Proposition 7.** For every n, H(X_1, …, X_n | X_0) = H(X_{−n}, …, X_{−1} | X_0).

*Proof.* Both equal H of a block of length n + 1 minus H(X_0). ∎

**Proposition 8 (possibilistic version).** Let 𝓛 be a time-translation-invariant set
of histories over a finite alphabet. The number of lawful length-n continuations,
summed over present states, equals the number of lawful length-n prehistories summed
over present states. Both are the number of lawful blocks of length n + 1.

So in a stationary world lawful indeterminism opens the past exactly as much as the
future. A fair coin tossed forever is the simplest case: the laws and the present
leave each past toss as unsettled as each future one. A difference appears only with
a non-stationary distribution, and then by Proposition 4 it equals the change in the
entropy of the description:

    H(X_{t+1} | X_t) − H(X_t | X_{t+1}) = H(X_{t+1}) − H(X_t).

**Scope.** The equality is for discrete states, hence for every finite coarse-graining
of a continuous state. With exact continuous states it can fail. The doubling map
x ↦ 2x mod 1 preserves Lebesgue measure, fixes the future from the exact present, and
leaves 2ⁿ pasts. At every finite resolution the two sides are again equal, at one bit
per step. So in a stationary world an arrow of exact fixing exists only as an
infinite-precision limit of a non-invertible law, where forward instability is being
counted as determination. This is the paper's distinction between exact fixing and
practical prediction, seen from the other side.

**Bearing on Nomic Presentism.** On that view a tensed claim is true because the
present state and the laws necessitate it. Markosian (1995) argued that the open
future has an open past as its price, and the Markovian-presentism lane records that
Builes concedes a possibly open past. Propositions 7 and 8 make that quantitative.
With stationary chances the view's past is open to exactly the degree its future is.
The view therefore gets a past more settled than its future only from a non-stationary
posit, and the amount it gets is the entropy growth that posit supplies. A Past
Hypothesis is such a posit. So the asymmetry of fixity on this view is not explained
by presentism or by the laws. It is the Past Hypothesis measured in bits. A defender
may accept that. It should be stated.

The same balance applies to the macroscopic case, with a caution about sign. If the
macrostate distribution spreads over time (branching, amplification, records), its
entropy grows and the future is the more open side. If macrodynamics relaxes many
macrostates to one, its entropy falls and the *past* is the more open side. The
entropy in the balance is that of the distribution over descriptions, not the
thermodynamic entropy of a macrostate.

## 6. Single events: exchange (demoted from the first version)

**Proposition 9 (exchange).** Let 𝓛 be affine and y, z ∉ F(S). If y ∈ F(S ∪ {z}),
then z ∈ F(S ∪ {y}).

*Proof.* Let K be the differences vanishing on S. The evaluation δ_y is not zero on K
and vanishes on K ∩ ker δ_z, so δ_y = c δ_z on K with c ≠ 0. ∎

This is the one-dimensional case of Proposition 2. It is rarely non-vacuous: in a
field theory in more than 1+1 dimensions, adding one event to a base almost never
fixes another. It is kept because it shows cleanly when one-way fixing is impossible.

**Proposition 10 (one-way fixing).** z fixes y over S without y fixing z exactly when,
given the values on S, the reading at y is a function of the reading at z that is
somewhere non-injective. This never happens in an affine class. When it happens under
a measure with discrete readings, H(y | S) ≤ H(z | S).

**Example 11.** 𝓛 = {s F(u) + s² G(u)} with disjoint bumps F, G in u = t − x. Every
member solves the 1+1 wave equation. A reading on the support of F one-way fixes a
reading on the support of G, whichever comes first. A linear equation with a nonlinear
selection of solutions can therefore have one-way fixing in either time direction.

**Remark 12 (becoming).** The becoming closure cl_B(S) = ⋃ {x : x B s} is generated
by a relation between events, and with identity co-presence it satisfies
anti-exchange. F is not generated by any relation between events, since
F({s}) = {s} for the wave equation while F of a Cauchy surface is everything. This is
a structural difference between having become and being fixed. The first version
dressed it as "matroid against antimatroid"; the dressing added nothing, and no one
defends the identity it refutes.

## 7. What changes in the paper (not applied)

1. §`sec:direction`: replace "So exact fixing has no arrow of its own. Under equal
   bases each side is as fixed or unfixed from the other." Proposed: "The law
   contributes no arrow to exact fixing. A model can still have one. What one base
   fixes about another is always what the other fixes about it, and the two can differ
   only in what each leaves open, by exactly the difference in the information they
   contain."
2. Add Corollary 6 as a remark after the mirror proposition, since it is a reading of
   Theorem `thm:massive` and the mirror.
3. Replace "We expect exact fixing to change little" in the open-question paragraph by
   the balance: a Past Hypothesis changes the asymmetry of openness by the change it
   makes to the entropy of the two descriptions, and to exact fixing only where it
   makes a reading a non-injective function of another.
4. Markovian-presentism reply draft: add the stationary-symmetry point as a
   quantitative form of the open-past concession, with Markosian (1995) credited.

## 8. Limits and kill conditions

- Propositions 1, 3, 4, 7 and 8 are elementary identities. The contribution is their
  use, and a reader may judge that use to be the obvious one.
- "Information" needs a measure, a dimension count or a block count. In infinite
  dimensions Proposition 3 becomes the pair of isomorphisms in Proposition 2, and
  "more" means strict inclusion, as in §4.
- §4 inherits the status of Theorem `thm:massive` (accepted sidecar) and of the mirror
  proposition. It adds no analysis.
- §5 assumes stationarity, which the actual universe does not have. Its role is
  conditional: it identifies what a view must add to stationarity.
- Proposition 8 counts in total, not state by state. A particular state can have more
  continuations than prehistories.
- The Nomic Presentism paragraph relies on the lane's reading of Builes and
  Impagnatiello and on a search-snippet view of Markosian (1995). Neither was reread.
- Kill conditions: a reading of the paper's sentence on which it is true at one
  standpoint; a published statement that the asymmetry of nomic openness equals an
  entropy difference, applied to the fixity of the past; an error in the mirror step of
  §4.

## 9. Sources and search

Search, 10 November 2026: five web queries in total across both versions.

- Markosian, "The Open Past" (1995), PhilArchive record MARTOP-2. Snippet depth. The
  qualitative open-past point is his.
- Crutchfield, Ellison and Mahoney, "Time's Barbed Arrow", arXiv:0902.1209, and the
  companion arXiv:1107.2168. Snippet depth. The symmetry of past–future mutual
  information and of entropy rate for stationary processes is theirs and older. The
  nearest prior art for §5 as mathematics.
- Earman, *A Primer on Determinism* (1986). The distinction between futuristic and
  historical determinism is his. Not read; seen through a secondary source. §2's
  "A fixes everything about C" is that distinction for arbitrary regions.
- Dependence logic (arXiv:1208.5268, arXiv:1912.03252). Snippet depth. Nearest prior
  art for §6.
- Hodroj and co-authors on nomic openness. Snippet depth.
- No source was found that states the balance as the measure of the asymmetry of
  fixity, or that reads the closed dust epoch result as an arrow of fixing. The search
  was short, so this is weak evidence.
- Not done: no independent review, no outside reader, no reread of the paper's sources.
