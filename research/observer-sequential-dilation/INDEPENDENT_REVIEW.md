# Independent review: observer sequential dilation

24 October 2026. Scope: mathematical consistency of `CLAIM_CONTRACT.md` and
`RESULT.md`, especially sequential heralding, reverse readout, outcome
conditioning, and finite/infinite claims. The named row-variation and matched-
pair bounds are treated as inputs; this review does not reproduce the original
matched-pair argument or audit the full physics literature.

## Verdict

No fatal algebraic error found in the central finite protocol, conditional on
the stated transition recursion, common moduli, unique-parent child labeling,
and the previously established all-depth bound `1 <= s(C) <= 1+zeta_n` with
`sum zeta_n = Z < 1/8`. The formulas consistently distinguish the success
probability of forward preparation from the additional reverse-readout filter.
The finite five-outcome law is normalized and nonnegative. This supports the
stated engineered finite-register construction, not physical availability of
its controls or an infinite-history detector.

One accounting boundary should remain explicit: `eta_N` is the probability per
trial *after the depth-three seed state has been prepared*. The fixed seed
preparation and the cost/accuracy of the transition-controlled unitary and its
inverse have no heralding probability in the model and are not included in the
rate. They are finite circuit resources, not free physical operations. This is
consistent with the RESULT's stated scope, but `eta_N > 1/3` must not be
presented as an end-to-end hardware rate or efficiency guarantee.

## Independent algebra checks

For a parent basis state, different parents have disjoint child supports by
unique last-birth deletion. Thus

`K_n^dag K_n |C> = (s(C)/B_n)|C>`.

The failure amplitude squared is `1-s(C)/B_n`, so the success and failure
effects sum to identity. For the target input, using `a(CP)=a(C)t(C,P)`,

`K_(j,n) psi_(j,n) = sqrt(V_(n+1)/(B_n V_n)) psi_(j,n+1)`.

The positive map has the same identity on `phi_n`. Multiplication over stages
therefore gives the stated exact all-success probability
`r_N=V_N/(V_3 b_N)` for these specified inputs. The pointwise upper bound on
`s(C)` is not the only relevant row fact: since the scalar transition row sums
to one, `s(C)=sum_P |t(C,P)| >= 1`. Thus
`K_n^dag K_n >= I/B_n`, and every normalized input to stage `n` has
conditional forward success at least `1/B_n`. Applying this at each
success-conditioned stage gives arbitrary-input all-forward success at least
`1/b_N >= exp(-Z)>7/8`. The exact target recursion is still needed for
`r_N=V_N/(V_3 b_N)` and the stated target-specific readout rates; the uniform
forward bound alone does not give those exact rates.

On the all-success branch, the positive forward map sends `phi_3` to
`sqrt(r_N) phi_N`. The adjoint of a retained unitary dilation, supplied with
the specified blank/success ancillas and tested for return to the seed, has
history effect `r_N |phi_N><phi_N|`. This factor is in addition to forward
success. For a diagonal event projector `P_a`, input `psi_(j,N)`, and
`nu_j(a)=sum_(C in a) a_j(C)`, the event/read-yes probability conditional on
successful preparation is

`r_N |nu_j(a)|^2/V_N^2`.

Multiplying by forward success `r_N` gives the unconditional probability
`r_N^2 |nu_j(a)|^2/V_N^2 = eta_N mu_(j,N)(a)`, where the predecessor defines
`mu_(j,N)(a)=|nu_j(a)|^2`. Thus
`eta_N=1/(V_3^2 b_N^2)` is correctly simplified. With
`V_3<3/2`, `b_N^2 <= exp(2Z)<exp(1/4)<4/3`, the strict lower bound
`eta_N>1/3` follows. It applies to baseline readout with no event split; an
inserted event test changes the total read-success probability.

For the binary event split, the five coarse outcomes are:

| Outcome | Probability |
|---|---|
| preparation fails (any forward failure flag) | `1-r_N` |
| preparation succeeds, `a`, read succeeds | `eta_N mu_j(a)` |
| preparation succeeds, `a`, read fails | `r_N sum_(C in a)|a_j(C)|/V_N - eta_N mu_j(a)` |
| preparation succeeds, `a^c`, read succeeds | `eta_N mu_j(a^c)` |
| preparation succeeds, `a^c`, read fails | `r_N sum_(C in a^c)|a_j(C)|/V_N - eta_N mu_j(a^c)` |

These sum to one because `sum_C |a_j(C)|=V_N` and
`mu_j(a)+mu_j(a^c)` is the total read-success numerator. Each read-fail term
is nonnegative: `|nu_j(a)| <= sum_(C in a)|a_j(C)| <= V_N` and `r_N<=1`
imply the read effect cannot exceed the event branch's probability. The
preparation-failure row is a coarse graining of all stage failure locations;
the result does not claim their stage-resolved distribution. For the event
omitted, `nu_j(X)=1`, so the all-success baseline probability is `eta_N`.
Conditioning on read success after the split yields
`mu_j(a)/(mu_j(a)+mu_j(a^c))`, not `mu_j(a)`.

The deterministic obstruction also checks out under its stated restriction.
An isometry preserving each parent sector preserves that sector's norm,
whereas the target child distribution has parent mass proportional to
`|a(C)|s(C)`. On occupied parents this agrees with the current mass exactly
when `s(C)=V_(n+1)/V_n`; nonconstant row variation therefore obstructs this
prefix-preserving deterministic map. It says nothing about maps that mix
parents, alter the representation, or postselect. The converse for constant
rows follows by normalizing each row with `sqrt(|t|/s)` and retaining the
transition phase.

## Limits and falsifiers preserved

- The coefficient `sqrt(|t|/B_n)` is a square-root reweighting. It is not the
  raw-amplitude append map with coefficient `t`, and it does not alone simulate
  the scalar process under ordinary history-register Born measurements.
- Arbitrary-input all-forward success has the uniform lower bound `1/b_N`
  because both `s(C)>=1` and `s(C)<=B_n` hold. The exact value `r_N` and the
  readout probabilities remain target-state-specific. Neither bound is a
  runtime, gate-count, precision, locality, energy, or physical observer
  bound; full readout can still have zero probability for an arbitrary input
  orthogonal to `phi_N` (or an event-restricted vector orthogonal to it).
- The reverse step assumes retained coherent access to the full finite
  dilation, its ancillas/flags, and inverse controls. It is an added operational
  resource. It does not reverse cosmological dynamics.
- The finite event `F_N={M_N=2}` and its positive finite-protocol gap are not a
  finite implementation of the completed event `E2`. Convergence of the
  probabilities and positivity of their limit do not provide a finite
  completed-event detector or uniform resource bound.
- No full completed-history covariance follows. The finite-label symmetry,
  physical locality, and ontology claims remain outside this result.

The conservative gap transfer is accepted here only as the named prior bound:
`mu_(B,N)(F_N)-mu_(A,N)(F_N)>399999/10000000`. Multiplying by
`eta_N>1/3` gives the reported unconditional gap
`>399999/30000000`. I have not independently rederived that prior amplitude
estimate, per the assigned scope.

## New checker audit

I inspected and ran `check.py`; it returns `PASS` with 47 parent rows and 397
append columns over the 3-to-4 and 4-to-5 stages. The separate level
enumeration has 7, 40, and 357 histories at depths 3, 4, and 5. It checks
interval enclosures for row contractions, the forward vectors against the
total-variation target vectors, and the direct overlap of the unnormalized
positive-preparation bra with the unnormalized phase-preparation ket. That
overlap includes both forward and reverse losses. It also checks the five
coarse outcomes and the finite event gap at those depths. I independently
verified that both parents in its reported size-four row-variation witness
have nonzero inherited-model amplitudes, so the witness is on occupied
support. Their disjoint row intervals are approximately
`1.000000000002824903...` and `1.000000000023134584...`.

The latest checker sets `r_3` exactly to one and asserts the preparation
failure outcome is nonnegative, resolving the earlier interval-display
caveat. It imports the pre-existing matched-diffuse and matched-norms
interval/model helpers, rather than independently proving the model. It pins
their current content hashes; I also verified those hashes against files at
the reported predecessor commit `ffb48d5`. Thus the append traversal and
readout arithmetic are newly checked against pinned model data, while the
model recurrence, helper correctness, and analytic all-depth row bound remain
inherited assumptions. These finite checks do not replace the all-stage proof.

The prior checker-label issues are resolved. The constant-row control now
uses explicit MSR rows `(2,-1)` for both parents and checks the branch Born
masses against the total-variation child masses
`[1/3,1/6,1/3,1/6]`, including preservation of each parent mass. The
nonconstant-row toy labels its inputs as scalar amplitudes and correctly
derives the TV parent weights; its `2/3`, full `1/9`, and free-readout `1/6`
rates remain consistent. The nonsummable contrast is now explicitly the
analytic sequence `2^-N -> 0`, not a finite numerical proof.

The checker now reports a formal limiting baseline enclosure
`[0.422311087189961757, 0.422311764857235859]`. Its tail step is valid under
the analytic majorant: with `T_5=sum_(n>=5) zeta_n<1`,
`b_5 <= b_infinity <= b_5 exp(T_5) <= b_5/(1-T_5)`. Inverting the squared
bounds gives the reported enclosure for `eta_infinity`. This adds a limit
bound, not an infinite-depth circuit or a new proof of the inherited
all-depth zeta estimate.

The locality sidecar has also been repaired: it now states the total-variation
parent mass `|A(C)|/V`, derives child-sector mass using `s(C)`, and uses the
same MSR toy for its restricted obstruction and two-loss readout accounting.
It separately reports the actual occupied size-four row-variation witness;
the toy is no longer presented as a witness from the matched model. I found no
remaining raw-`|A|^2`/TV mismatch in the sidecar's obstruction argument.
