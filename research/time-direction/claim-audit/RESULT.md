# Cross-lane consistency audit of the arrow claims

19 November 2026. Coordinator session (Claude Code, Opus 5.5). Not independently reviewed. The
check is [check_claim_audit.py](check_claim_audit.py): pure Python, fixed seeds, floating point
with a tolerance of 1e-9. A3′ is exact and can be checked by hand.

## Why

Each lane tested its own claim on its own models. Here, six claims from the
[consolidation](../consolidation/RESULT.md), [chance records](../../records-asymmetry/chance/RESULT.md)
and [macro bridge](../macro-bridge/RESULT.md) are restated as predicates, at the scope their prose
gives them. All six are then run on one shared corpus. The corpus adds worlds no lane used:
- kernels with zero entries;
- stationary processes that are not Markov (hidden-Markov images);
- coarse-grainings of permutation dynamics that are exactly time-reversal symmetric.

The idea comes from PhilBench's view-consistency test (philbench.com, read at discovery depth,
19 November). Its finding that capable models answer more consistently but no more correctly, and
that their answers flip under a prompt to ignore philosophers, is a warning for a project whose only
reviewer so far is one model family. A claim should survive models chosen by someone other than the
claimant.

## Results

| | Claim as worded | Corpus | Outcome |
|---|---|---|---|
| A1 | Consolidation claim 3: "A chance law can be described homogeneously in exactly one direction, the one leading away from a single boundary" | 400 positive and 400 zero-entry kernels on 3–4 states, sharp start, T = 6 | **Holds for positive kernels (0 exceptions). Fails as worded:** with zero entries the backward description is homogeneous over the whole run in 56 cases, and at some step while μ is still changing in 65. The lemma's converse needs positivity. *Corrected:* claim 3 now says "strictly positive kernel" |
| A2 | Table row, deterministic reversible: production direction "none, even with a boundary"; versus claim 5: production runs backward from an end boundary in a deterministic world | 300 random coarse-grainings of reversal-symmetric permutations (8–12 states), macro start boundary | No contradiction once the level is stated. At micro level homogeneity never picks a direction. At macro level: **neither 291, both 9, exactly one 0**. B3–B4's macro production direction depends on the macro process being exactly Markov |
| A3 | Claim 2: "A law arrow on its own leaves every amount of whole time slices mirror-symmetric", together with claim 6, that law arrows are label arrows | Stationary Markov (control), stationary hidden-Markov (4 states into 2), coarse-grained symmetric permutations, uniform measure; all time sets of {0..5} | **Fails outside Markov.** Control: gap ≤ 1e-15. Hidden Markov: gap in 147 of 200, up to 0.044 bits. Coarse-grained permutations: 65 of 200, up to 0.400 bits. No boundary is present in any of them |
| A3′ | Smallest case found | A 6-cycle (a rotation, which is reversal-symmetric) read through the cyclic word 2 0 0 1 1 1, at a uniformly random phase | (X₀, X₁, X₃) takes 6 distinct values: H = log₂6 = 2.585. The mirror set (X₁, X₃, X₄) takes 5: H = 2.252. Exhaustive search finds none with two labels up to 6 states and T ≤ 4 |
| A4 | Claims 1 and 6: if the reversal map preserves the coarse-graining, no macro arrow; if not, arrows can appear | 300 reversal-symmetric permutations, uniform measure, random partitions into 3 | **Holds.** Preserved: 149, worst asymmetry 2e-16. Not preserved: an arrow in 71 of 151, up to 0.5 bits |
| A5 | Chance records: "a reversible kernel gives no record arrow of any kind" | 100 reversible stationary kernels on a 2×3 product, both ordered pairs, lags 1 and 2; plus coarse-grained images | **Holds.** Worst record–forecast difference 1.5e-14. Coarse-grained images mirror (9e-16) |
| A6 | Claim 4: relative entropy to equilibrium never rises away from a boundary | 400 zero-entry kernels with a stationary π found | **Holds** (0 rises). This is the data-processing inequality |

## What changes

1. **Amounts are not boundary-only.** Under stationarity alone, the entropy of a contiguous stretch
   of times always equals that of its mirror. A pattern of times with gaps need not. That holds for
   any stationary process that is not Markov, including the coarse-grained images that claim 6 says
   are where arrows come from. So the consolidation's alignment of boundaries with amounts and of
   labels with values is wrong. A coarse-graining can give an amount arrow with no boundary at all:
   in A3′, how much a pattern of three times pins down depends on its orientation.
2. **What is left for boundaries**, within scope:
   - the relative-entropy gradient, which needs non-stationarity by definition;
   - the production direction for positive Markov descriptions.

   The second is narrower than it looked. Positivity is required (A1). Generic coarse descriptions of
   deterministic worlds give no production direction either way (A2).
3. **Claim 1 survives at macro level** (A4). This makes the label source precise: an arrow appears
   only when the reversal map fails to carry the coarse-graining to itself.

## For the ontologies

Growing-block and Maudlin-style production needed a production direction, and the consolidation said
only a boundary supplies one. That still holds, with less in it. Where the coarse description of a
reversible world is not Markov, the homogeneity criterion supplies *nothing*, even with a boundary.
A defender of production then has two options:
- choose descriptions that are Markov, so that a choice of labels joins the boundary as a premise;
- give up homogeneity as the mark of production.

On the other side, an opponent of passage cannot say that every amount arrow is a boundary effect.

## Limits

- Random corpora, 3 to 12 states, horizons of 4 to 6 steps. Counts are of these corpora only, not
  frequencies in physical systems.
- "Homogeneous" means equal one-step conditional laws. That is weaker than a Markov description for
  processes that are not Markov.
- A3 is elementary. Irreversibility of stationary non-Markov processes is known in general (not
  checked at source here). No priority is claimed.
- Each claim was restated as a predicate by this session, which is a judgment about what its prose
  says. A different reading of "amount" or "direction" could change A2 and A3.
- One model family wrote both the claims and this audit.
