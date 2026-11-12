# What a stochastic law fixes

11 November 2026. Claude Code (Fable 5.2), native research worker, task
`novel-stochastic-fixing`. Checked only by the session that wrote it. Nothing here is
claimed as new mathematics; the credits say where each piece is textbook. No temporal
ontology is selected. Sources: [sources.jsonl](sources.jsonl). Finite checks:
[check_stochastic_fixing.py](check_stochastic_fixing.py). Scope throughout: discrete
time, finite state space.

## Verdict

1. **No one-way exact fixing.** Under any process law, what one time-region fixes
   exactly about another is what the other fixes about it. This holds for every path
   measure, stationary or not, reversible or not. Exact fixing sees only which
   histories are possible, so a stochastic law adds nothing at this level to the
   paper's deterministic operator.
2. **The kernel carries an arrow that no amount of fixing detects.** A stationary
   Markov chain read in full has the same entropy on every set of times as on its
   mirror image, whether or not the chain is reversible. So a biased cycle, or any
   stationary chain with positive entropy production, shows no asymmetry in what is
   fixed or in how much is left open between regions. Its arrow shows only when the
   forward and backward conditional laws are compared value by value, which is a path
   statistic. A non-stationary start with a reversible kernel is the opposite case: it
   shows in the balance H(c|a) − H(a|c) = H(c) − H(a), and its entropy production does
   not grow with time.
3. **Entropy production is the right measure of one thing only.** It measures the
   failure of plain reversal invariance of the stationary path law, and its rate
   separates a kernel arrow from a boundary arrow. It is not a measure of asymmetric
   fixing, and it is positive for the biased cycle, which is reversal invariant once a
   reflection of the states is allowed.
4. **The mirror proposition and the collapse claim both stand.** The mirror extends to
   process laws invariant under a time reflection combined with a relabelling of
   states. The collapse claim is a symmetry of path probabilities, the strongest kind,
   and it needs both of its hypotheses.

Almost all of this is textbook. What the note adds is the sorting: which instrument
detects which arrow.

## Definitions

A process law is a probability measure P on histories x = (x_t), here given by an
initial law μ and a kernel K. A region is a set of times A, and its reading is X_A.

- **Exact fixing.** A quantity f(X_A) is fixed by C when f(X_A) = g(X_C) with
  probability one for some g. An event t is fixed by C when X_t is such a quantity.
- **Fixing in distribution.** What C fixes about A in distribution is the conditional
  law P(X_A | X_C). Three things can be read from it:
  the amount left open, H(X_A | X_C); the values, meaning the conditional law itself
  with its labels; and the part of X_C that matters, meaning the minimal sufficient
  statistic of X_C for X_A.
- **Reversing map.** A time reflection t ↦ n − t together with a bijection ε of the
  state space. P is invariant when (ε(X_{n−t})) has the same law as (X_t). Plain
  reversibility is the case ε = identity. For a stationary chain write
  J(x,y) = π(x)K(x,y); invariance is J(εy, εx) = J(x,y).
- **Reversed kernel.** K*(x,y) = π(y)K(y,x)/π(x), the law of the previous state given
  the present one.
- **Entropy production rate.** e_p = Σ J(x,y) log (J(x,y)/J(y,x)), which for a
  stationary chain is 1/n times the relative entropy between the path law on n steps
  and its plain reversal.

## Propositions

**Proposition 1 (exact fixing sees only the support).** Let L be the set of histories
of positive probability. A quantity of A is fixed by C under P exactly when it is
fixed by C for the class L in the paper's sense. The quantities of A fixed by C
correspond one to one with the quantities of C fixed by A: both are the functions
constant on the connected components of the graph that joins a value of X_A to a
value of X_C when the pair is possible.

*Proof.* f(X_A) = g(X_C) with probability one means f(a) = g(c) for every possible
pair (a,c). That mentions P only through L, and it is symmetric in the two regions.
Such an f is constant along edges of the graph, hence on components, and any function
of the components is such an f. ∎

So reciprocity needs no stationarity and no symmetry. A kernel with all entries
positive fixes nothing exactly (E1, E2). Between distant times an irreducible chain
shares only the phase of its period (E4). A deterministic non-injective kernel gives
one-way fixing of *events* (X_1 from X_0 and not back), as the paper already says, and
by the next proposition this cannot happen in a stationary chain.

**Proposition 2 (amounts are mirror-symmetric for stationary Markov chains).** Let X
be a stationary Markov chain with stationary law π, read in full, and let
t_1 < … < t_k. Then H(X_{t_1}, …, X_{t_k}) = H(π) + Σ_i h(t_{i+1} − t_i), where
h(g) = H(X_g | X_0). Hence every set of times has the same entropy as its mirror
image. Consequently H(X_C | X_A) = H(X_{C′} | X_{A′}) for mirrored regions, and t is
fixed by A exactly when its mirror image is fixed by the mirror image of A.

*Proof.* By the chain rule and the Markov property, each reading adds
H(X_{t_{i+1}} | X_{t_i}) = h(t_{i+1} − t_i) by stationarity. Reflection reverses the
order of the gaps, and the sum does not depend on the order. Conditional entropies
are differences of such entropies, and a reading is fixed exactly when its
conditional entropy is zero. ∎

No reversibility is used. The script confirms it on every set of times in 0..4 for
five chains, four of them non-reversible. The hypothesis "read in full" matters: see
E6.

**Proposition 3 (where a kernel arrow does show).** For a stationary chain:

- (a) *Values.* K* = K exactly when detailed balance holds, exactly when every path
  has the probability of its reversal, and exactly when e_p = 0.
- (b) *Statewise openness.* H(K(x,·)) and H(K*(x,·)) can differ at a given state x.
  Their averages over π are equal.
- (c) *What matters.* The part of the present that matters for the future is the
  class of states with the same row of K. The part that matters for the past is the
  class with the same row of K*. Their entropies C⁺ and C⁻ can differ.
- (d) *Relabelling.* If a reversing map with relabelling ε leaves P invariant, then
  (b) and (c) are symmetric after applying ε, and C⁺ = C⁻. For three states, write
  J = S + cA with S symmetric and A the cyclic antisymmetric matrix. A reversing map
  exists exactly when c = 0 or some transposition of states preserves S.

*Proof.* (a) is Norris, Theorems 1.9.1 and 1.9.3, with the standard formula for e_p.
(b) Both averages equal H(X_0, X_1) − H(π). (c) Two present states give the same law
of the future exactly when their rows agree, and the same holds backward with K*.
(d) The map carries the backward conditional laws to the forward ones. For three
states the antisymmetric part of J has zero row sums, so it is a multiple of A, and
conjugating A by a permutation multiplies it by the permutation's sign; compare
symmetric and antisymmetric parts of J(εy, εx) = J(x,y). ∎

**Proposition 4 (boundary arrow against kernel arrow).** For a stationary chain the
relative entropy between the path law on n steps and its reversal is n·e_p. For a
reversible kernel with stationary law π started from μ it is
D(μ‖π) − Σ_x μ_n(x) log(μ(x)/π(x)), which is at most
D(μ‖π) + max_x log(π(x)/μ(x)) for every n. In the second case
H(X_n | X_0) − H(X_0 | X_n) = H(μ_n) − H(μ).

*Proof.* The stationary case is the definition summed over steps. In the reversible
case the path probability is (μ(x_0)/π(x_0)) times a reversal-symmetric factor, so the
log ratio is log(μ(x_0)/π(x_0)) − log(μ(x_n)/π(x_n)). The last identity is the paper's
balance. ∎

## Examples

All run exactly in the script.

| | Law | Reversible | e_p (bits/step) | Reversing relabelling | Exact fixing between times | Asymmetry of amounts | C⁺ − C⁻ |
|---|---|---|---|---|---|---|---|
| E1 | Biased 3-cycle, 2/3 one way, stationary | No | 1/3 | Yes, a reflection | None | None | 0 |
| E2 | Positive kernel, two equal rows | No | 0.0208 | None | None | None | −0.49 |
| E2b | Generic positive kernel | No | 0.0732 | None | None | None | 0 |
| E3 | 0→{1,2}, 1→2, 2→0 | No | ∞ | Yes, swap 0 and 2 | [X_0=2] = [X_1=0] | None on average | 0 |
| E4 | Biased 4-cycle | No | 1/3 | Yes | Parity, at every distance | None | 0 |
| E5 | Symmetric kernel, start (7/8, 1/16, 1/16) | Kernel yes | 0 | n/a | None | 0.86 to 0.92 bits | n/a |

- **E1** is Norris's Example 1.9.4. P(0,1,2) = 4/27 and P(2,1,0) = 1/27, and nothing
  else distinguishes the directions.
- **E2b** is a law-borne arrow in the strict sense: stationary, no reversing map of
  any kind, and yet no asymmetry in any amount and none in C⁺ − C⁻.
- **E3** shows fixing at a state. Given X_0 = 0 the previous state is fixed and the
  next is open by one bit. Given X_0 = 2 it is the other way round. The two cases have
  equal weight, and the swap of 0 and 2 is a reversing map.
- **E5** against E1: the path divergence from reversal stays below 2.07 bits for all n
  in E5 and grows by 1/3 bit per step in E1, while the balance is positive in E5 and
  zero in E1.
- **E6, coarse readings.** Uniform bits with X_{t+3} = X_t ⊕ X_{t+1}. The process is
  stationary. Times {0,1} fix X_3, and the mirror image fails: {2,3} do not fix X_0.
  H(X_0,X_1,X_3) = 2 and H(X_0,X_2,X_3) = 3. This is a deterministic invertible law
  that is not reversal invariant, so it already falls outside the mirror proposition
  as the paper states it. Reciprocity still holds: the shared quantity is X_3 on one
  side and X_0 ⊕ X_1 on the other.
- **E7, records.** A hidden chain is read through a noisy channel four times. With a
  symmetric kernel and a uniform start every record has exactly the probability of its
  reversal. With the same kernel and another start it does not. With the biased cycle
  and a uniform start it does not, but it does after reflecting the labels. With E2b
  from its stationary law no relabelling works.

## Answers to the three questions

**(1) One-way fixing from a stationary non-reversible law?** Not of exact quantities,
by Proposition 1, for any law. Not of events or amounts either, for a stationary
Markov chain read in full, by Proposition 2. What such a law can do is make the past
fixed and the future open *at particular states* (E3), with the opposite at other
states and exact cancellation on average, and make different parts of the present
matter for the two directions (E2).

**(2) What in the kernel carries an arrow?** The antisymmetric part of J, the
stationary probability current, when no relabelling of states undoes it. An initial
law carries a different arrow. The two are told apart by Proposition 4: the kernel
arrow has a rate and no balance, the boundary arrow has a balance and no rate.
Entropy production is the right measure of the first with two cautions. It is
relative to the identity pairing of states, so it is positive in E1, where a
reflection restores the symmetry; the invariant quantity would be its minimum over
relabellings, which I have not found named in what I read. And it is infinite as soon
as some possible step has an impossible reverse (E3). It is detectable by fixing only
if "fixing in distribution" is taken with its labels, comparing K with K* value by
value. No amount of fixing detects it in a Markov chain read in full. With coarse
readings the amounts can differ (E6), and Crutchfield, Ellison and Mahoney's causal
irreversibility C⁺ − C⁻ is the established measure of that.

**(3) The mirror proposition and the collapse claim.**

- The mirror proposition extends as stated: if P is invariant under a reversing map,
  every fixing statement, exact or in distribution, holds for the mirrored regions
  after relabelling. The proof is the paper's, with "solutions" replaced by "the path
  law".
- At the exact level a stochastic law gives the proposition no new test, because
  exact fixing sees only the support (Proposition 1). The sentence "the laws give
  fixing no arrow of their own: for time-reversal invariant laws every such result
  has a mirror image" needs no change.
- For laws that are not invariant, something stronger than the mirror holds for
  amounts (Proposition 2) and something weaker for values. So a stochastic law that
  breaks every reversing symmetry (E2b) has an arrow that the fixing relation cannot
  express. The paper could say so in one sentence. That is a remark about a limit of
  the fixing vocabulary, not a correction.
- The paragraph "One question stays open" expects a Past-Hypothesis asymmetry to
  appear in conditional probabilities with size H(c) − H(a). E5 is a toy in which
  exactly that happens. It does not prove the paper's expectation for macroconditions.
- The collapse claim in the settling note stands. It asserts equal probabilities for a
  record and its reversal, which implies symmetry at every level used here. E7 shows
  the classical shadow of its two hypotheses. Time-reversal invariance of the dynamics
  plays the part of detailed balance and the maximally mixed state plays the part of
  the stationary start, and dropping either breaks the symmetry. The note's own
  generalisation, that a chosen initial state equals a mixed start with post-selection
  at the other end, is the boundary arrow of Proposition 4. Bedingham and Maroney's
  Section IV makes the same point for a general stochastic rule with Bayes' theorem
  (their equations 52 to 58).
- One refinement. The settling note says a lawful arrow needs a class of worlds "with
  no time-reversing symmetry of any kind". For process laws that condition is easy to
  meet: E2b meets it. So stochastic laws with a law-borne arrow exist, and the open
  question about collapse is whether its law is of that kind, not whether such laws
  are possible.

## Credits

- **Time reversal of a stationary chain, detailed balance, the biased cycle.** Norris,
  *Markov Chains*, section 1.9 (read): Theorem 1.9.1, Lemma 1.9.2, Theorem 1.9.3,
  Example 1.9.4. Proposition 3(a) is his. Kelly's *Reversibility and Stochastic
  Networks* and the Kolmogorov cycle criterion were named in the brief; the copy I
  fetched was an unreadable scan, so neither is cited for any statement.
- **Equal predictability in both directions; C⁺, C⁻, causal irreversibility.**
  Crutchfield, Ellison and Mahoney, arXiv:0902.1209 (read in full). Proposition 3(c)
  is their construction applied to a chain read in full.
- **Kinds of reversibility for stationary processes.** Ellison, Mahoney, James,
  Crutchfield and Reichardt, arXiv:1107.2168 (sections III.2, IV.2, V.4 and VI.1
  read). They state that a stationary finite Markov process is reversible exactly
  when its chain is in detailed balance, note that the process repeating ABC is
  irreversible yet needs equal memory in both directions, and define reversibility
  "under symbol isomorphism", which is the relabelling of Proposition 3(d).
- **Entropy production as a relative entropy between forward and reversed
  statistics.** Kawai, Parrondo and Van den Broeck, arXiv:cond-mat/0701397, and
  Roldán and Parrondo, arXiv:1004.2831, at abstract depth only. Proposition 4 is the
  standard split into a boundary term and a rate; I derived it here and did not read
  it in a source.
- **Collapse and boundary conditions.** Bedingham and Maroney, arXiv:1502.06830
  (sections I, IV and V read). The reading of E5 and E7 is theirs.
- **Shared exact quantities as components of the support graph.** This is the common
  part of two variables in the sense of Gács and Körner (1973). Known to me, not read:
  discovery depth.
- **Reciprocity and balance.** The fixing-exchange note and Albert, through it.

Proposition 2 is a two-line consequence of the Markov property. I did not find it
stated in what I read and make no claim about whether it is in print.

## Limits

- Discrete time and finite state space. Continuous states can break Proposition 2, as
  the doubling map breaks the stationary result in the fixing-exchange note.
- Proposition 2 needs the full Markov state as the reading. Real readings are coarse,
  and then E6 and causal irreversibility apply.
- "Fixing in distribution" has three readings here (amounts, values, what matters).
  The verdict that fixing does not detect a kernel arrow is about amounts.
- E7 is classical. It illustrates the structure of the collapse claim and checks no
  quantum statement.
- The script checks finite examples in exact rational arithmetic, with entropies in
  floating point. It proves nothing beyond them.
- The entropy-production sources are at abstract depth, read through a summarising
  tool that did not return the abstracts verbatim.
