# What is conserved between past and future

10 November 2026. Claude Code (Fable 5.2), at the user's request. Checked only by the
session that wrote it. The mathematics is elementary and is not claimed as new. No
temporal ontology is selected. Sources: [sources.jsonl](sources.jsonl). Finite checks:
[check_exchange.py](check_exchange.py).

The statements marked ★ are in the unified paper's direction-of-time section.

## The idea

The paper asks which *events* a base fixes, and that has asymmetric answers. Ask
instead which *quantities* one region fixes about another. A quantity of a region is a
function of the lawful history that depends only on the history there.

## 1. Reciprocity and balance ★

**Proposition 1 (reciprocity).** For any class of histories and any regions A and C,
the quantities of C fixed by A are the quantities of A fixed by C. Both are the
quantities common to the two regions.

This is immediate from the definition. Its use is to show where an asymmetry can
live: only in what each region leaves open about the other.

**Proposition 2 (linear form).** Let the class be a vector space V of fields, or a
translate of one, and let K_A be its members vanishing on A. Then the common quantities
are the functions on V/(K_A + K_C). The freedom left on C given A is K_A/(K_A ∩ K_C),
and the freedom left on A given C is K_C/(K_A ∩ K_C). In finite dimensions these differ
by dim V|_C − dim V|_A. In particular no single reading fixes another one way.

**Proposition 3 (probabilistic form).** For discrete readings a of A and c of C under
any probability measure on the histories, H(c | a) − H(a | c) = H(c) − H(a).

So the future is more open than the past, each given the other, by exactly the amount
by which its description carries more. An arrow of openness is an information
imbalance between the two bases.

## 2. The closed dust model has an arrow of exact fixing ★

By the paper's massive-field theorem and its mirror, for a massive linear field on the
closed dust model and a standpoint at conformal time τ:

| Standpoint | Past given future | Future given past |
|---|---|---|
| τ < π | Fixed entirely | Open |
| τ = π | Fixed | Fixed |
| τ > π | Open | Fixed entirely |

The paper had said that "under equal bases each side is as fixed or unfixed from the
other". That is false at a single standpoint in this model. The law contributes no
arrow. The model has one, because the future of an early event contains a Cauchy
surface and its past does not. It points toward the larger side and reverses at the
midpoint.

## 3. Stationary chance opens the past as much as the future

**Proposition 4.** For a stationary process of discrete states, the entropy of the next
n steps given the present equals that of the previous n steps given the present. For a
shift-invariant set of histories over a finite alphabet, the total number of lawful
n-step continuations equals the total number of lawful n-step prehistories.

So lawful indeterminism, when stationary, leaves the past as unsettled as the future.
A difference needs a non-stationary distribution, and by Proposition 3 it equals the
change in the entropy of the description.

**Scope.** Discrete states, or any finite resolution. With exact continuous states it
can fail: the doubling map is stationary, fixes the future from the exact present and
leaves 2ⁿ pasts. At every finite resolution the two sides agree again.

**Bearing on views that ground past truths in the present and the laws.** With
stationary chances such a view has a past exactly as open as its future. It gets a
more settled past only from a non-stationary posit such as a Past Hypothesis, and by
the entropy growth that posit supplies. A view that grounds the past's fixity in
something non-nomic is untouched.

## Credits

- **Albert**, *Time and Chance*, ch. 6, n. 11 (read): under deterministic,
  volume-preserving dynamics a constraint at one time constrains every other "to
  exactly the same degree", differing in form. That is Proposition 1 with zero
  imbalance. The paper now cites it.
- **Crutchfield, Ellison and Mahoney**, arXiv:0902.1209 (read): a stationary process
  is equally predictable in both time directions. Proposition 4 is theirs. They also
  define an asymmetry in the memory needed to predict, which survives stationarity and
  is not treated here.
- **Price**, *Time's Arrow* (three passages read): the fixed past and open future
  belong to the agent's perspective. He gives no measure of it.
- **Markosian**, "The Open Past" (not read): the qualitative open-past point.

What this note adds: the comparison of regions that carry unequal amounts, the closed
dust reading, and the use of Proposition 4 against nomic grounding of the past.

## Limits

- Propositions 1 to 4 are identities. The contribution is their use.
- Section 2 inherits the status of the paper's massive-field theorem and mirror.
- Section 3 assumes stationarity, which the actual universe lacks. It says what a view
  must add to stationarity.
- A first version centred on an exchange property for single events and on a contrast
  between matroid and antimatroid closures. Both were true and nearly empty, and were
  cut. The single-event statement survives as the last sentence of Proposition 2.
