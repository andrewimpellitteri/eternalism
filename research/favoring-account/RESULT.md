# Defeasible favoring without exclusion

Sole-worker analysis, 2026-10-21. Core input for the reframed article
(`paper/REFRAME.md`), responding to the external review's point that the draft
asks about "favoring" while devoting its machinery to "excluding."

## The distinction

Two questions are different:

1. **Exclusion:** does the physics eliminate every admissible realization of
   ontology `O`?
2. **Favoring:** does the physics make `O` more credible than a rival `O'`?

Failure to establish (1) does not answer (2). A package can retain a compatible
realization and still be less favored than a rival, because the rival's
realizations fit the evidence better or are better supported by independent
considerations.

The reviewer's example makes the point exactly. Let `O_1` have one specified
realization with `p(D|O_1)=1`. Let `O_2` have ten independently specified
realizations with equal prior weights; one gives `p(D|r)=1`, nine give `0`.
Then

```
p(D|O_1)=1,   p(D|O_2)=0.1,   BF_{12}=10.
```

`O_2` retains a perfectly compatible realization, but the evidence favors
`O_1` by a factor of ten. Compatibility survives; evidential parity does not.

## A composite-hypothesis account

Treat an ontology as a **composite hypothesis**:

- a class `R_O` of admissible realizations (models, bridges, auxiliary
  structures);
- a prior `p(r|O)` over those realizations;
- a likelihood `p(D|r)` for the discriminating evidence;
- the marginal likelihood `p(D|O)=sum_r p(D|r)p(r|O)`.

A Bayes factor `p(D|O_1)/p(D|O_2)` is a comparative favoring measure. It is
defeasible: it depends on the realization class, the prior and the likelihood,
and it can be overturned by new evidence or by showing that the prior was
arbitrary.

This is not a new statistical theory. It is a discipline for stating what a
favoring claim is doing. The alternative — comparing only the best realization
of each ontology — can favor an ontology by ignoring its other admissible
realizations; comparing only the worst can penalize it unfairly. The composite
treatment makes the choice explicit.

## What justifies the prior?

The hard part is `p(r|O)`. It should not be chosen after seeing the verdict.
It can be constrained by:

1. **Earlier physical evidence** that bears on the realization, independently
   of `D`.
2. **Explanatory achievements** that the ontology's proponents claim for the
   realization, assessed by a criterion stated in advance.
3. **Symmetry or invariance** considerations that make some realizations
   equivalent or equally weighted.
4. **Simplicity/parsimony**, if it is independently motivated and applied
   symmetrically to rivals.
5. **Explicit ignorance**: a uniform prior over a stated finite class, with the
   class justified.

If none of these is available, the prior is stipulated. A stipulated prior can
still yield a conditional verdict — "given this prior, `O_1` is favored" — but
it is not evidence for `O_1` simpliciter. The paper must label it as such.

This is where the reviewer's "priors can reflect earlier physical evidence"
point bites. A prior is not automatically physics-free; it can encode earlier
results. But it must be stated and defended, not hidden in the choice of
realization.

## Favoring versus exclusion

A favoring verdict has the form:

> Given comparison class `C`, admissible realizations `R_O`, priors `p(r|O)`
> justified by `J`, and evidence `D`, ontology `O_1` is favored over `O_2` by
> factor `B`; this does not exclude `O_2`, and it is defeated if `J` or `R_O`
> is shown to be arbitrary.

An exclusion verdict has the form:

> Every admissible realization of `O_2` is inconsistent with `D` (or with the
> physics), so `O_2` is excluded from `C`.

The first is weaker and more achievable. It is also what the article's title
promises. The paper should be willing to reach it.

## Application: Brading

Brading's system-relative present can be treated as a composite hypothesis:
realizations differ in which systems are genuine, what their sustaining regions
are, and how presence relates to existence. The coverage objection shows that
one prominent realization — local boundedness without an actuality premise —
may be behaviorally indistinguishable from an eternalist history with local
presents. If so, the presentist composite either:

- includes the eternalist-like realization, in which case the likelihood
  comparison does not favor presentism over eternalism; or
- excludes it by an actuality/privilege premise, in which case the prior over
  realizations must justify that exclusion.

Either way, the favoring verdict depends on the realization class and the
prior. The paper can say: under the system-relative realization, the evidence
does not favor presentism over eternalism; under a privileged-actuality
realization, it may, but the privilege premise is doing the work. That is a
substantive comparative verdict, not a catalogue.

## Application: LAGEOS

A preferred-frame bound changes the likelihood of an Einstein-aether model
relative to GR. It does not by itself change the likelihood of an ontology,
because the ontology-to-model map is not specified. To get an ontological
favoring verdict, one needs a prior over ontology-realization classes that
links presentism/eternalism to aether/GR. The bound can then favor a package
conditionally. Without that link, the correct verdict is "parameter constraint,
no ontological discrimination" — which is what the discriminator audit found.

## The paper's use

The reframed paper can use this account in its conclusion:

> Physics may defeasibly favor a package without excluding its rival. The
> verdict is conditional on the realization class and the prior; it is not a
> proof of ontology, and it is not nothing.

This is the positive payoff the external reviewer asked for. It also keeps the
paper honest: a favoring verdict is not an exclusion, and a failure to exclude
is not a failure to favor.

## Limits

- The account does not settle which prior is correct. It requires the prior to
  be stated and independently constrained; where it is not, the verdict is
  conditional.
- It does not make ontology comparison quantitative in practice; the
  likelihoods are often qualitative. The Bayes-factor form is a discipline, not
  a claim that the numbers are available.
- It does not by itself supply the exclusivity premise the discriminator audit
  found missing; it explains how a favoring verdict can proceed without one,
  at the cost of conditionality.
- No new empirical prediction or ontology selection.
