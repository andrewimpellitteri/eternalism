# Screening review: owner handoff and correction

31 October 2026. Addressed to `claude-native-bowtie`, the recorded holder of
`bowtie-horizon-rationale` and owner of `research/bowtie-horizons/`.
This persistent repository handoff implements the user's request to route
the finding. No direct chat message was sent: the app could not read the
candidate chats to establish which one belongs to this holder.

## Action for the bow-tie notes

Keep Theorem 3(b) of [SCREENING.md](../../bowtie-horizons/SCREENING.md)
conditional. The handed-back `screening-review` claims that its premise (L′)
is refuted, but the offered refutation is incorrect. Do not promote that
finding to the accepted ledger, and do not treat the proposed (L″) as proved.

Original review: branch `agent/screening-review`, commit
`ef924b1f38591ef19d0a9996664b986115844ad7`,
`research/bowtie-horizons-screening-review/RESULT.md`, §§6.1–6.5.
It remains in review; this handoff does not accept the full submission.
The worker's files and claim are preserved unchanged.

## The specific error in the claimed refutation

In 1+1 Minkowski space let

    S = {(t,x): t = sqrt(1+x²)}.
    a = t-x,  c = t+x.

Then S is `a>0, c>0, ac=1`. The review correctly identifies
`D⁺(S) = {a>0, c>0, ac>=1}`, but wrongly asserts `D⁻(S)=S`.
In fact, under the usual causal-curve definition of domain of dependence,

    D⁻(S) = {a>0, c>0, ac<=1},
    D(S)  = {a>0, c>0} = I⁺((0,0)).

Here is a direct proof of the missing part. Along a future causal curve,
both a and c are nondecreasing. Starting from a,c>0, they remain bounded
below by positive constants. A future-inextendible causal curve in full
Minkowski space has t tending to infinity: if t had a finite upper endpoint,
the causal speed bound would give a finite spatial limit and an extension.
Thus a+c tends to infinity and ac tends to infinity. Starting with ac<1,
continuity forces a crossing of ac=1. Every such curve therefore meets S.
For a point outside the positive quadrant, a future null ray keeping a
nonpositive coordinate fixed misses S. For a point with a,c>0 and ac>1,
every future causal continuation has product still greater than one, so
misses S. Including S itself proves the D⁻ formula.

For completeness, the D⁺ formula follows by reversing the argument. A
past-inextendible causal curve from ac>1 in the positive quadrant crosses
t=0 in full Minkowski space, and hence crosses S first. From ac<1 in that
quadrant, past causal continuations cannot increase either null coordinate
and cannot reach S; outside the quadrant, a past null ray retaining a
nonpositive coordinate also avoids S.

The full domain is **open**, contrary to the review's claimed closed region.
Although S is not Cauchy in ambient Minkowski space, it is Cauchy in this
domain. For the latter claim, an inextendible causal curve in the quadrant
has product tending to zero at its past end and infinity at its future end;
the product is strictly increasing along any nonconstant causal segment.
It therefore crosses S exactly once. This is an analytic calculation, not
a numerical counterexample search. It does not by itself prove (L′).

## What the primary source does and does not establish here

Sbierski [arXiv:1309.7591v3](https://arxiv.org/html/1309.7591v3),
Definition 2.1(3), requires the data surface to be Cauchy **in its
development**. Theorems 2.6–2.8 give local/common development and maximal
development statements in that framework. These selected statements were
checked directly; their proofs were not reconstructed for this handoff.

Being non-Cauchy in an ambient spacetime does not by itself prevent a surface
from being Cauchy in its own domain of dependence. Thus §6.1's inference
from partial/ambient data to definitional exclusion is also insufficient.
The actual open question is whether the relevant domains are maximal
developments, or whether a weaker domain-agreement theorem suffices under
the exact hypotheses of SCREENING.md. The hyperbola is no refutation of
either assertion. This source check supplies neither a proof of that
localization nor a general counterexample.

The source's maximality theorem is not itself a printed statement of the
required localization. A rigorous next step must either prove/supply the
localization for the particular matched hypersurfaces, or use an established
common-development route under additional stated assumptions. Retain the
existing [reviewed vacuum repair](COMMON_EXTENSION_REPAIR.md) at its own
scope rather than replacing it with the new submission's unproved (L″).

Any replacement premise must match full induced Cauchy data, including
extrinsic curvature and the relevant matter normal derivatives, or retain
the ambient isometry germ already available from h:W₁→W₂. Intrinsic slice
geometry and scalar values alone are not the Cauchy-data contract. The
original SCREENING.md germ is stronger than that abbreviated reading of
the worker's proposed (L″).

## Remaining handback

The reviewer separately raises a C⁰ Cauchy-surface convention issue in
Theorem 2: an achronal boundary can contain null segments and need not be
acausal. That finding is not disposed of by the hyperbola correction; it
still needs its own source/proof inspection before adopting the whole
review. No universal claim of literature absence follows from the worker's
bounded searches. Theorem 3(b), novelty and philosophical consequences
retain their existing gates.
