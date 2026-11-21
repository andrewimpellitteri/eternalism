# Can a primitive direction of time run against time's arrows?

18 November 2026. Coordinator session (Claude Code, Opus 5.5), at the user's request. This note has
not been independently reviewed: every review so far comes from one model family. It claims no
priority, because the lemma is elementary and is likely known as a fact about reversing Markov chains.
It selects no ontology. The check is in [check_m_arrows.py](check_m_arrows.py) and the sources are in
[sources.jsonl](sources.jsonl).

**Maudlin's book has not been read.** Every claim attributed to Maudlin below comes from Loewer's
reconstruction (`ma-loewer-two-accounts-2012`, author's draft) or Healey's review
(`ma-healey-ndpr-2008`).

## The standoff

Loewer compares two accounts:
- **Maudlin's:** laws are fundamental producers. A primitive arrow at each point (an M-arrow) tells
  the law which way to produce the next state (draft pp. 4–6). Chances are best read as propensities.
- **The Lewis–Albert Humean account:** the direction of time comes from the Mentaculus. That is
  deterministic dynamics, plus the Past Hypothesis, plus a uniform measure over that macrostate
  (pp. 12–15).

His central objection is that M-arrows do no work. They are not *sufficient*, because there are
worlds whose M-arrows point against the entropy gradient while knowledge and influence follow
entropy. They are not *necessary*, because a Humean duplicate with no M-arrows would show the same
arrows (pp. 24–25). Maudlin replies, as Loewer quotes him, that this begs the question: a
time-reversed duplicate is not physically like us at all. Loewer answers that the reply begs the
question just as much, and he calls the dispute a standoff (pp. 25–26).

Both sides argue about what duplicate worlds would be like. This note asks something narrower and
checkable. **In which classes of law can an M-arrow come apart from the arrows physics does show?**

## Result

| Class of law | Can a homogeneous producing law point against the gradient? | Effect on the standoff |
|---|---|---|
| Deterministic and reversible (finite permutation dynamics) | **Yes.** Read backwards, the dynamics is again homogeneous, the inverse permutation, from any initial law (check 2). | Loewer's sufficiency objection stands. Neither direction of the law is privileged ([ARROW_READ.md](../ARROW_READ.md) §1). |
| Stochastic Markov chains with a strictly positive kernel | **No**, unless the world is stationary. A homogeneous description exists in exactly one direction. In that direction, relative entropy to equilibrium does not increase (Lemma, checks 1 and 3). | Loewer's sufficiency objection fails for this class, except as a claim about improbable histories. |
| Stochastic, with a boundary distribution in the middle (a Janus world) | No single orientation is homogeneous on both sides. The homogeneous direction flips at the boundary, and on each side it agrees with the outward fall in relative entropy (check 4). | A single global M-arrow must make its law inhomogeneous on one side, or the arrows must vary by region. |

### Lemma

Take a stochastic matrix K with all entries strictly positive, and an initial distribution μ₀. Write
μₜ = μ₀Kᵗ. Read the same path measure backwards. Its step from t+1 to t has the kernel

  Rₜ(y, x) = μₜ(x) K(x, y) / μₜ₊₁(y).

**Then Rₜ = Rₜ₊₁ if and only if μₜ is stationary.**

*Proof.* Every μₜ₊₁ is strictly positive, because K is.
- *If μₜ(x) = 0 for some x* (possible only at t = 0): then Rₜ(·, x) = 0 while Rₜ₊₁(·, x) > 0, so
  the kernels differ. And μₜ ≠ μₜ₊₁, so μₜ is not stationary.
- *Otherwise:* since K(x, y) > 0, the equality Rₜ(y, x) = Rₜ₊₁(y, x) is equivalent to
  μₜ₊₁(x)/μₜ(x) = μₜ₊₂(y)/μₜ₊₁(y). The left side depends only on x and the right side only on y,
  so both equal one constant c. Summing μₜ₊₁ = c·μₜ over states gives c = 1. Hence μₜ₊₁ = μₜ.
  Conversely, stationarity makes every later kernel the same. ∎

**Corollary.** Over any window of length 2 or more, the backward description is homogeneous if and
only if μ₀ is stationary. Check 5 shows the boundary case: a rank-one kernel reaches stationarity in
one step and is homogeneous from then on. The forward direction is also the one in which D(μₜ‖π)
does not increase (data processing). When K is doubly stochastic, Shannon entropy does not decrease
in that direction.

### What the lemma does, given three bridge premises

The lemma is mathematics. It bears on the Maudlin dispute only through three premises, which are
philosophical and not physical:

- **(H) Homogeneity.** A producing law gives the same propensities at every time. It "engages the
  state" and nothing else (Loewer p. 23). If a law's propensities depend on the date, the boundary
  information has been written into the law.
- **(M) Markov.** The produced chances depend only on the present state.
- **(P) Propensity.** M-probabilities are the transition chances K, in the direction of production
  (Loewer p. 4).

Under H, M and P, take a non-stationary world in this class. Its M-direction is not free. It must be
the unique direction in which the path statistics are homogeneous. That direction runs away from the
boundary distribution, toward equilibrium. So an M-arrow reversed against the chance gradient, with
the same law, would describe a statistically different world. To that extent Maudlin's reply, that a
reversed duplicate is not like us, gets support that does not beg the question, in this class only.
The support is statistical. It says nothing about mental states.

The same fact works against him. **A direction that can be detected can also be defined.** A
Humean best system for such a mosaic would, on our judgment of simplicity, also choose the
homogeneous direction, because one homogeneous kernel is simpler than a sequence of date-dependent
kernels. This is a premise about best-system simplicity, not a theorem. So the M-direction and the
direction of the Humean laws coincide, and the mosaic fixes both. This gives a dilemma for the
primitivist:
- **Stochastic worlds:** the arrow shows up in the statistics, so it is available to the reductionist.
- **Deterministic worlds:** it does not show up, so Loewer's insufficiency objection stands.

On neither horn does any observable in these models need a *primitive*. Maudlin's actual thesis
survives, because it is explanatory: production explains the pattern, and the pattern does not
constitute production. But it cannot claim that the models' statistics need it.

### Begins at low entropy versus a block with an edge

This is the question put to this lane. In this class it gets an answer that depends on the law:

- **Stochastic, positive, homogeneous laws:** the two pictures disagree on the statistics. Take
  "begins with μ₀ at t = 0 and is produced forward" and "has an edge distribution at T and is
  produced backward". Both use homogeneous laws, and they assign different path measures unless the
  world is stationary. Where the boundary sits relative to the law's direction is a fact a long
  record could test.
- **Deterministic reversible laws:** they do not disagree. The same set of histories and the same
  conditioned measure can be read either way.

So "the world began and grows forward" adds content beyond "the world has an edge" only where the
laws are stochastic, under the bridge premises above. The growth-arrow lane found the same split for
causal-set growth ([growth-arrow/RESULT.md](../growth-arrow/RESULT.md)):
- **Generic sequential growth:** the law has a direction.
- **Transitive percolation:** reversal-invariant at every stage, so its beginning does all the work.

## What a rival has a reason to revise

- **Loewer, the sufficiency objection (pp. 24–25).** The claim that M-arrows can point against the
  entropy gradient needs a restriction:
  - to deterministic or otherwise reversible-homogeneous laws, or
  - to improbable histories, or
  - to M-laws whose propensities depend on time.

  For homogeneous positive Markov propensities, the typical histories cannot be anti-thermodynamic
  relative to the M-direction.
- **Maudlin, as reconstructed.** The petitio reply can be strengthened for stochastic laws, but only
  by making the arrow recoverable from statistics. Janus worlds are a further cost. A single
  orientation everywhere forces the producing law to be inhomogeneous on one side. Loewer's footnote 6
  reports that Maudlin allows different laws in different regions, so regional arrows may be open to
  him. Whether that fits his view is unread.
- **Growing-block appeals to production.** If production means homogeneous stochastic generation,
  the direction of growth can be detected in the statistics. If production is compatible with
  deterministic reversible laws, the direction of growth is invisible in the laws, and the earlier
  [mirror result](../ARROW_READ.md) applies.

## Limits

- **Scope of the models:** finite state spaces, discrete time, Markov laws, and strictly positive
  kernels. Kernels with zero entries between the two extremes are unclassified; only permutations
  were checked. Continuous-time, continuum or field-theoretic laws (GRW, for instance) are not
  covered. Any extension to them is a conjecture.
- **Which entropy.** The gradient here is the relative entropy of the chance distribution. It is not
  the Boltzmann entropy of an actual microstate, and it is not the records asymmetry. A single
  history can run against it with small probability, and that probability was not quantified.
- **Prior work.** The lemma is an elementary fact about reversed Markov chains. Dolev, Elitzur and
  Hemmo (abstract only) make a stronger, related claim: that indeterminism yields an arrow whatever the
  initial condition. Klimenko's Markov-bridge account (abstract only) is the nearest two-boundary
  precedent. Albert's GRW treatment, which Loewer reports in his footnote 26, has not been reread for
  this note. The application to Loewer's objection was not found in the search, but the search was
  short.
- **Attribution.** Maudlin is unread at first hand, and so is the published version of Loewer.
- **Bridge premises.** H, M and P are bridge premises. A primitivist may reject H by letting
  propensities depend on the epoch. That rejection is coherent, and it carries the cost named above.

## Open questions

1. Read Maudlin 2007 ch. 4 and Maudlin 2002 to check H and the regional-laws reading.
2. Classify kernels with zero entries, and find where homogeneity in both directions first becomes
   possible between permutations and positive kernels.
3. Bound the probability of anti-gradient histories in a long finite run. That bound is where
   Loewer's counterworlds have to live.
4. Connect this to the records lane. Does the homogeneous direction coincide with the direction in
   which records point, in the stochastic gadget models of [records-asymmetry](../../records-asymmetry/RESULT.md)?
