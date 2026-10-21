# Frontier audit: event-filter efficiency versus growing variation

21 October 2026. Candidate direction, pending independent review and priority
search. The stability theorem in RESULT.md is known mathematics. The question
below asks what physically realizable instruments can do with its witnesses.

## New primary-source contact

Chakraborti, Sorkin and Sinha, *Measuring a Quantum Measure Exceeding Unity*,
arXiv:2407.15702v3 (14 September 2026), Quantum 10, 2215 (2026),
DOI 10.22331/q-2026-09-24-2215.
Primary URLs: https://arxiv.org/abs/2407.15702 and
https://arxiv.org/html/2407.15702v3 .
Read depth: abstract, Introduction, Section 2.2 and Section 6; not a complete
experimental-data audit. The text describes an ancilla filter with calibrated
detector probability equal to one-half the chosen event's quantum measure.
It also distinguishes direct detection from inferred quantum measure, and
limits what this demonstrates about what actually happened in a history.
No causal-set event-filter realization is established by this experiment.

## Conditional finite bound (coordinator derivation)

At resolution n, let a_n be the prescribed scalar event amplitude,
V_n its total variation, and B_n=max_E |a_n(E)| over all event unions.
Suppose a family of filters has a **common** nonnegative calibration eta_n,
with ordinary success probabilities

    P_n(success | E) = eta_n |a_n(E)|^2

for every E at this resolution. Probability bounded by one implies

    eta_n <= 1/B_n^2 <= pi^2/V_n^2.

This is a necessary condition, not a sufficient condition for realizing a
quantum instrument. It assumes the rank-one scalar quantum measure |a(E)|^2;
the photonic paper's endpoint-summed measure is more general. Its one-event
calibration does not assert this all-event, common-efficiency hypothesis.

If instead each filter has eta_{n,E}, only eta_{n,E}<=1/|a_n(E)|^2 follows.
That does not force low efficiency for every event. Comparing individual
filters requires their own calibration, cost and disturbance models.

For a common efficiency, the reference event Omega has a_n(Omega)=1, hence
success probability eta_n. Under N independent Bernoulli trials, the sample
mean's relative variance is exactly (1-eta_n)/(N eta_n). Requiring relative
mean-square error <= delta^2 therefore requires

    N >= (1/eta_n-1)/delta^2 >= (B_n^2-1)/delta^2.

This bound concerns that estimator and sampling protocol. It is not an
unrestricted quantum lower bound; coherent amplitude estimation, collective
measurements, event-dependent calibration and prior knowledge are outside it.
As V_n diverges, common calibration would make the elementary reference
measurement increasingly inefficient, even though large-measure events can
still have order-one detector probabilities.

## Exact diagnostic

For the binary example in check.py, at even n the optimal event union has
B_n^2=((2^(n/2-1)+1)^2+(2^(n/2-1))^2)/4.
At n=20 this is 525313/4. A common calibration must obey
eta_20<=4/525313. For delta=1/10 the above reference protocol requires at least
13,132,725 independent trials. This is an exact necessary bound for a
hypothetical all-event family, not an estimate for the published experiment.

## What would actually advance the project

1. Derive the admissible event family from a finite ancilla/system instrument,
   including its disturbance, calibration, and causal access constraints.
2. Test whether it contains the divergent-variation event witnesses, or a
   sequence with unbounded B_n despite operational restrictions.
3. Construct filters or prove an obstruction for the allowed family; distinguish
   common calibration from event-dependent calibration.
4. Compare with the general filter scheme cited by Chakraborti et al., and
   quantum estimation/postselection resource bounds. The present bounded
   search is insufficient for a novelty claim.

Kill criteria: the bound follows immediately from an already published filter
resource theorem; allowed events have uniformly bounded amplitudes; no
instrument realizes the assumed scalar amplitude rule; or covariant access
excludes every candidate witness. Any one shrinks or kills the proposal.

## Decision

Keep the exact stability result as supporting mathematics. Put substantive
research effort into the instrument/access/resource question above, while
continuing the independent Bell-causality and clock-formulation probes. A
mathematical obstruction alone cannot establish an experimental prediction or
a preferred temporal ontology.
