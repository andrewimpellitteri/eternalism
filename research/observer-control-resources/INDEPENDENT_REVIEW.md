# Independent review: observer control resources

24 October 2026. Scope: independent bounded audit of `RESULT.md` and
`check.py`, focused on the full-history memory count, finite circuit-error
accounting, and the stated primary-source correspondence. I did not edit the
worker result, checker, source register, or any other project file.

## Verdict

The central combinatorial bound and the finite error budget are correct under
the stated architecture and channel-error assumptions. The memory statement
is specifically about a register with mutually orthogonal slots for every
labelled history. The error claim is a sufficient worst-case guarantee for the
specified complete finite circuit, with each component error supplied in
diamond norm. It establishes neither a universal memory lower bound nor that
summability is necessary for every implementation.

One primary-source description needs repair: Aharonov–Kitaev–Nisan (AKN),
`quant-ph/9806029`, is not the cited fault-tolerance theorem. It develops the
mixed-state circuit model, trace and diamond metrics, and an `O(L ε)` circuit
error bound. Its introduction cites fault-tolerance results as prior work.
The project's elementary finite-circuit telescope remains a sound direct
argument, but the paper should be described for the results it actually
contains. There is also a version/read-depth bookkeeping mismatch for AKN and
KSW, detailed below.

## Independent mathematical audit

**Full-history memory.** Fix labelled floors `A` and `B` of sizes
`floor(N/2)` and `ceil(N/2)`. For each subset `S ⊆ A×B`, set the only strict
relations to the pairs in `S`. Every relation is irreflexive and asymmetric.
No two strict edges compose, since every edge ends in `B` and starts in `A`,
so transitivity holds. Distinct subsets give distinct labelled partial
orders, yielding

`2^(|A||B|) = 2^floor(N²/4)`

distinct histories. Mutually orthogonal basis slots for all such histories
therefore require dimension at least that large, or at least
`floor(N²/4)` qubits. The proof uses only this explicit family and does not
invoke an asymptotic enumeration theorem. It does not constrain compressed,
nonorthogonal, approximate, label-quotiented, or statistic-only encodings.
The injection and legal-poset checks are consistent with the described
natural-label architecture.

**Diamond norm and outcome total variation.** For two trace-preserving output
channels at diamond distance at most `e`, applying them to the same input
(including any reference system), then measuring and retaining a classical
outcome, gives output total-variation distance at most `e/2`: the trace
distance convention is one half the trace norm, and measurement is
contractive. The full output must retain failure outcomes for this direct
claim. A composition of CPTP components telescopes to at most the sum of
their component diamond distances, because the intervening channels have
diamond norm one. Thus for model errors `e_A,e_B`, the designated event
probability gap is bounded below by `G - (e_A+e_B)/2`.

**Summable two-pass schedule.** Put `β=G/8`. The intended fixed allocations
are four channel components per model, each at most `β`: seed preparation,
event instrument including its classical output, reverse seed-acceptance
test, and final classical readout. At each stage `n≥3`, budget `ε_n=β·2^-(n-1)`
separately to the forward growth dilation and its reverse use. The geometric
sum is `Σ ε_n=β/2`; both passes together cost at most `β`. Hence each model
has total error at most `4β+β=5G/8`. Substitution gives

`G - (5G/8 + 5G/8)/2 = 3G/8`.

This is a conservative sufficient schedule. The prose should make clear that
the four fixed components are individually budgeted; that is what the
checker’s `4 * beta` encodes. If the reverse acceptance and final readout are
intended as one combined component, the written component list and checker
should be reconciled, although the stated `5G/8` cap remains conservative.

For a unitary block, after aligning global phase if useful,
`||U(·)U† − V(·)V†||_diamond ≤ 2||U−V||_op`; so an operator-norm synthesis
error of at most half a component's channel budget suffices. An independently
implemented inverse needs its own budget unless it is exactly the adjoint of
the same approximate unitary, in which case the operator distance is the
same. This does not provide a synthesis method or a bound for noisy,
nonunitary components; those require direct channel-error guarantees.

For a fixed positive stage error, this telescoping estimate grows with the
number of forward and reverse stages, so it cannot certify a depth-independent
positive gap. That is a limitation of this worst-case estimate, not proof that
every fixed-error implementation loses the gap. No universal necessity of
summability is established.

## Bounded checker

I ran `python3 research/observer-control-resources/check.py`; it completed
successfully. The output checks all cross-edge subsets through `N=8`, the
distinct-relation counts, exact rational allocation sums, and the claimed
margin. For example, at `N=8` it checks all 65,536 subsets and obtains 65,536
distinct posets. The code verifies finite combinatorics and arithmetic; the
general family argument and channel telescope are analytical proofs in the
text, not results established by enumerating these finite cases.

The checker’s finite growth schedule ends at stage 79, while its assertions
compare the exact finite sum to the geometric-series bound. This is a valid
bounded arithmetic check, not a numerical simulation of infinitely many
stages. The schedule’s infinite bound follows from the geometric series
directly.

## Primary-source correspondence and read depth

- **AKN.** The requested `https://arxiv.org/abs/quant-ph/9806029v2` URL did
  not resolve in the browser. The official arXiv record and linked PDF that I
  could inspect identify the accessible paper as `quant-ph/9806029v1`; I
  therefore independently read the **full text of v1**, not v2. In the PDF,
  the abstract and introduction describe mixed-state circuit equivalence and
  the probabilistic-subroutine problem (pp. 1–3); the paper defines trace and
  diamond metrics and proves gate/circuit error bounds in Sec. 5, including
  Theorems 3 and 4 (PDF pp. 15–19). The introduction explicitly says
  fault-tolerant computation results already exist and cites them; it does not
  present a fault-tolerance threshold theorem. The source register says
  `v2`, `abstract`, while the worker result calls it an established
  fault-tolerant computation result. Correct the description to the results
  above, and verify the claimed v2 locator or change the version to the
  actually checked one. The AKN error framework is relevant precedent; it is
  not evidence of fault tolerance for this observer circuit.

- **KSW.** I independently read the **full text of arXiv:0710.2495v1** at
  the registered exact version. The paper proves continuity relations between
  completely positive maps in cb norm and their Stinespring dilations in
  operator norm; see Theorem 1, Sec. 2, and Theorem 2 for general range
  algebras. This is relevant context for distinguishing channel and dilation
  distances, but the observer result does not use the KSW theorem to prove its
  finite composition estimate. The worker's source register labels KSW
  `abstract`, while its `RESULT.md` says “full text.” The latter matches my
  independent reading; update the source record and give the theorem locator
  if the coordinator adopts this reading depth.

- **Kleitman–Rothschild.** Its role as context is represented accurately:
  the explicit subset injection above proves the claimed bound without their
  asymptotic enumeration result. No theorem from that paper is needed for
  this review.

Primary links: [AKN official arXiv record](https://arxiv.org/abs/quant-ph/9806029),
[AKN accessible v1 full text](https://arxiv.org/pdf/quant-ph/9806029),
[KSW v1 full text](https://arxiv.org/pdf/0710.2495v1), and
[Kleitman–Rothschild](https://doi.org/10.1090/S0002-9947-1975-0369090-9).

## Limits preserved

The accounting still assumes a complete finite CPTP implementation model and
specified component error bounds. It does not charge or bound precursor
enumeration, arithmetic and coefficient loading, reversible history updates,
gate count, synthesis cost, fault-tolerance overhead, energy, locality,
calibration, latency, or physical access to the inverse circuit. Exact
algebraic controls in the ideal finite model do not imply a finite universal
gate compilation or an efficient oracle. The review supplies no hardware
rate, universal complexity bound, or temporal-ontology conclusion.
