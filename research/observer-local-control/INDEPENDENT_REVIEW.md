# Independent review: new actual witness and local branch-mass bound

24 October 2026. Scope is limited to the coordinator-added actual same-past
witness and the fixed-past branch-mass result in `RESULT.md`, plus the
corresponding new checks. I did not edit `RESULT.md`, `check.py`, sources, or
the workboard, and I make no broader literature or theory assessment.

## Verdict

Both additions are correct under their stated finite-register and access
assumptions. The actual pair has the same observer past and stage but different
validity of precursor mask 2, so the conditional global precursor states have
different support. The local branch-mass identity follows from
`t(C,P)=q(C)w(P)` and the past being a down-set. For a fixed-size past, the
probability of success while retaining only precursors inside that past
decays exponentially with the number of external spectators.

These conclusions concern a controller whose complete accessible record is
the stipulated observer record and whose output is a fixed global
precursor-register alphabet. They do not exclude a physical interaction in
which an environment carries spectator information, nor do they establish a
no-go for reduced local observables, alternative couplings, or differently
normalized instruments.

## Same-past actual witness

For `C=(0,0,1)` and `D=(0,1,1)`, observer `o=2` has closed past
`R={0,2}` in both histories, with induced relation `0<2`. At stage `n=3`,
the stipulated finite memory and observer record therefore coincide. In `C`,
vertex 1 is unrelated and `{1}` (mask 2) is an ideal. In `D`, `0<1`, so
`{1}` without 0 is not an ideal. The actual transition in the first context
has nonzero magnitude `L^-3`; the corresponding coordinate in the second
context is zero. Normalizing each transition row cannot remove this support
difference, and phases cannot turn a zero coordinate into a nonzero one.
Thus one record-only controller cannot reproduce both conditional states in
the common output basis.

The check reports the conditional Born mass at mask 2 in the first context as
`[0.000000000999999993, 0.000000000999999994]` for each model, and exactly
zero in the second. This is a conditional row coordinate, not the absolute
success probability of the global heralded step. The support argument alone
is enough for the access obstruction; equal global herald rates are not
required for this actual witness.

The common output alphabet is substantive. It lets both global rows be viewed
as vectors in one Hilbert space, with invalid coordinates padded by zero. If
each context instead has a distinct output space or the global precursor
register is traced out, this particular vector-equality criterion no longer
directly applies to the resulting reduced experiment. Likewise, if a memory
state or other accessible system is correlated with the spectator and differs
between `C` and `D`, the two cases are not the same record under that enlarged
access rule.

This proves a failure of factorization through the declared record for the
specified global output. A physical environment can hold or acquire
information about the spectator and mediate context-dependent joint dynamics
without the observer explicitly querying the global history. Such a mechanism
is outside the record-only control model; the witness does not rule it out.
To make a physical locality claim one would need to specify the system and
environment tensor factors or observable algebras, their initial correlations,
the allowed couplings, and which reduced output is required to match.

## Fixed-past branch-mass result

Let `R` be a down-set of `C` with `k=|R|`, and retain only global precursor
ideals `P⊆R`. The squared norm of that part of the original success column is

`p_local(C,R) = Σ_(P⊆R) |t(C,P)|/B_n = L^-n W_j(R)/B_n`.

The equality uses `|q(C)|=L^-n`. Because `R` is a down-set, its subsets that
are ideals of `C` are exactly the ideals of its induced order. For `k≥3`,
applying the same row rule to that induced history gives
`W_j(R)=L^k s_j(R)` and `1≤s_j(R)≤B_k`. Therefore

`p_local(C,R)=L^(k-n) s_j(R)/B_n ≤ L^(k-n) B_k/B_n < (9/8)L^(k-n)`.

The last strict inequality uses `B_n≥1` and `B_k<9/8`. Hence any unbounded
size deficit `n-k` forces these retained-branch probabilities to zero. In
particular, at fixed `k=3`, the exact checker enclosures are about `0.932835`
at `n=3`, `9.99744×10^-4` at `n=4`, and `9.99999×10^-7` at `n=5`.
Conversely, for `k≥3`, a bounded deficit gives a positive uniform lower bound
from `s_j(R)≥1` and `B_n<9/8`; the finite seed cases `k<3` require their
corresponding positive seed-row constants. Thus the stated boundary is
correct for this family and this retained part of the original instrument.

The probability is joint: it includes both the original global herald
success and the retained-precursor event. If one conditions on retaining a
precursor in `R`, the normalized conditional output state can remain
well-defined even as this joint probability tends to zero. But renormalizing
that restricted map into a new local heralded operation changes its success
amplitude, calibration, or both; it is not the same instrument as the original
global Kraus map. The vanishing branch mass therefore does not imply that all
conditional local experiments become unusable, and the conditional experiment
does not inherit the original global success guarantee.

For arbitrary coherent input supported on parents with the same past-size
cap, unique last-birth deletion gives disjoint child supports. The restricted
success effect is consequently diagonal in the parent basis, so coherence
cannot raise its largest branch probability above the maximum diagonal value.
This extension still assumes the same global register and the same restriction
to precursor subsets of each parent’s declared past; it is not a theorem about
arbitrary local instruments.

## Bounded verification and limits

I ran `python3 research/observer-local-control/check.py`; it returned
`PASS`. The finite checks verify the same observer record for the two
size-three contexts, validity versus invalidity of mask 2, nonzero versus zero
conditional coordinate, equality of the restricted normalized rows up to the
parent phase, and the branch-mass identity for the spectator family
`R=(0,0,3)` at `n=3,4,5` in both models. The returned masses match the formula
above.

This is a bounded check against the imported matched-model interval helpers,
whose source files are content-pinned by SHA-256 in the checker. It does not
independently prove those helpers, the transition recursion, or the all-depth
row bound. The general branch-mass decay follows from the displayed analytic
identity and row bounds, not from the three spectator samples.

The review supports only the declared record-only control obstruction and
the restricted-branch probability bound. It does not establish physical
locality or its impossibility, an observer-independent no-go, universal
necessity of a growing past, a hardware efficiency statement, or a temporal
ontology conclusion.
