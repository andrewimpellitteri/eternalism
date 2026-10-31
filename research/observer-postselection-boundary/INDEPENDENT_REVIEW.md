# Independent review of the auxiliary observer theorem and instrument

Bounded review, 23 October 2026. This assesses the analytic theorem and
instrument in `RESULT.md`, and the finite domain actually checked by
`check.py`. It does not repeat the rank-one GNS derivation in
`HISTORY_HILBERT.md`, perform another source search, or claim physical
implementation.

## Disposition

The sharp baseline postselection bound, its total-variation attaining
construction, the common apparatus for the matched pair, and the four-outcome
instrument are mathematically correct under their stated assumptions. The
seed's identical success-conditioned event frequencies coexist with a
different joint event-and-success probability, as claimed. The completed
bound `V<16/7` yields the stated positive ideal joint-success gap. No
universal measurement or physical-cost lower bound follows, and `RESULT.md`
appropriately says so.

The finite within-isomorphism-class apparatus symmetry is also valid for the
declared finite register. It is not a proof of full natural-label gauge
covariance or an action on completed cosmological histories. The stated
completed-measure-preserving-bijection condition is a valid sufficient
condition, but remains an assumption awaiting an actual group action and
invariance proof.

I ran `python3 research/observer-postselection-boundary/check.py`; it passed.
The checker is an exact finite certificate for the seven-history auxiliary
register, not a check of the all-stage theorem or physical implementation.
The finite controls for strict and saturated cases check out.

## Sharp baseline postselection bound

For a realization with normalized `psi,phi`, a PVM `{P_i}` and
`c=<phi,psi> != 0`, the fixed normalized measure obeys
`c nu(E_i)=<P_i phi,P_i psi>` on each cell of any finite measurable
partition. Therefore

    |c| sum_i |nu(E_i)|
      <= sum_i ||P_i phi|| ||P_i psi||
      <= (sum_i ||P_i phi||^2)^(1/2)
         (sum_i ||P_i psi||^2)^(1/2) = 1.

Taking the partition supremum gives `|c| V<=1`, hence baseline success
`p0=|c|^2<=V^-2`. This uses precisely a normalized pure pre/postselected
pair, one common PVM representing the measure by a matrix-element ratio, and
the total variation over the same event sigma algebra.

For attainment, with `lambda=|nu|`, `V=lambda(X)`, and
`h=dnu/dlambda`, the vectors `psi=h/sqrt(V)` and `phi=1/sqrt(V)` in
`L2(lambda)` are normalized. Multiplication by `1_E` is a PVM and
`<phi,psi>=1/V`, `<phi,P_E psi>=nu(E)/V`; thus the ratio is the prescribed
measure and `p0=V^-2`. This works for finite non-atomic measures as well.
The independent-trial expected-attempt statement is just the geometric
waiting-time consequence for repeated identical baseline trials. It excludes
state preparation, control, event recognition and precision costs.

This is sharp only within the specified realization class. It is not a lower
bound on arbitrary estimation strategies, all circuits, or all observers.
Nonpostselected weak-value estimation changes the operational task and its
resources; the coordinator's explicit caveat prevents the postselection
bound from becoming a universal cost claim. I did not independently audit
the source register for that literature claim.

## Common apparatus, pointer trace, and four outcomes

The accepted variation-data equality gives a common finite measure
`lambda_A=lambda_B=lambda`, hence a common `V`, constant postselection vector
`phi`, and multiplication PVM. The model inputs differ only through their
polar phases `h_j`; the apparatus does not use a model label.

For the controlled unitary, the joint state before the final filter has
history branches `P_E psi_j tensor u_1` and `P_Ec psi_j tensor u_0`. Tracing
out history removes their cross term, leaving

    rho_M = lambda(E)/V |u_1><u_1|
            +lambda(Ec)/V |u_0><u_0|.

For a memory effect `F`, pulling it back through the coupling gives
`<u_1,F u_1>P_E + <u_0,F u_0>P_Ec`. These formulas confirm equality of all
memory-only statistics for the two models. They rely on tracing out the
history before any coherent final filter; retaining history and postselecting
is a different access model.

For the four Kraus operators, write `Q=|phi><phi|` and `P_a` for the event
PVM cells. Then

    K_(a,yes)^* K_(a,yes) + K_(a,no)^* K_(a,no)
       = P_a Q P_a + P_a(I-Q)P_a = P_a,

so summing over `a=E,E^c` gives identity. On input `psi_j`, the yes
probability is `|nu_j(a)|^2/V^2`; the no probability is
`lambda(a)/V-|nu_j(a)|^2/V^2`. The latter is nonnegative because
`|nu_j(a)|<=lambda(a)<=V`. Summing all four outcomes gives one.

For `F_3`, the amplitudes are `nu_A(E)=nu_A(Ec)=1/2` and
`nu_B(E)=1/2-i/5`, `nu_B(Ec)=1/2+i/5`. Thus both postselected conditional
event frequencies are `1/2`, although the joint `(E,yes)` probabilities
differ by `1/(25 V_3^2)`. This is the central success-conditioning warning:
discarding the success rate erases this difference. At orthogonal record
overlap `c=0`, total success is `1/(2V_3^2)` for A and
`(29/50)/V_3^2` for B, both below the no-record baseline `1/V_3^2`.
At `c=1` the pointer records no event and success returns to baseline.
The interpolating success difference `(2/25)(1-c)/V_3^2` has the correct
sign and endpoints. The four-outcome output retains the event and success
flags, so its ordinary probabilities are not confused with the nonadditive
quantity `|nu(E)|^2` alone.

## Completed variation and scope of the cost statement

For the completed pair, `V_N` increases to `V<16/7`; this gives
`1/V^2>49/256`. Combining it with the prior completed-event estimate
`mu_B(E2)-mu_A(E2)>399999/10000000` gives the reported ideal joint-success
gap lower bound `19599951/2560000000`. This is a bound for the constructed
auxiliary pre/postselection model and common variation measure. It is not a
bound on the physical cost of preparing the phase state, maintaining a
coherent history register, deciding `E2`, or implementing its projector.
Finite-approximant convergence does not supply those resources.

The completed-event claim uses the already established finite countably
additive extensions, common variation, and E2 tail bound. The new finite
checker does not re-prove those all-stage facts. Neither a positive abstract
success probability nor finite-level certificates establish a cosmological
or laboratory instrument.

## Symmetry audit

At depth three, the group declared in `RESULT.md` consists of permutations
among representatives of each same finite isomorphism class. The checker
enumerates all seven histories, computes canonical edge sets under all six
vertex permutations, and verifies equal atomic variation weights and constant
`F_3` membership within every class. In the normalized atomic basis these
equal weights make the constant postselection vector invariant. Since
`F_3` is class-invariant, `P_F3` commutes with this group; consequently
`Q_phi`, the two event projections, and their four Kraus products commute as
well. The checker also verifies a B-model amplitude mismatch between two
representatives in one class, consistent with a covariant apparatus and a
noninvariant input state.

This is a genuine finite auxiliary-register symmetry result. The group is
defined on representative slots, not derived as the full natural-label gauge
action. For completed histories, any measurable bijection preserving
`lambda` and leaving `E` invariant induces a unitary fixing `phi` and
commuting with `P_E`; the stated covariance conclusion follows. No such
cosmological group action or preservation of `lambda` is constructed here.
Cylinder-norm covariance alone would not establish it.

## Checker audit and signed control

The exact checker independently reconstructs the seven allowed depth-three
mask histories and the seed amplitudes. It represents
`Q(sqrt(265),sqrt(65))` with rational coefficients, checks the total variation
and its square, four-outcome positivity/normalization, common record-only
statistics, conditional `1/2`, and partial pointer overlaps `0,3/5,1`. It
checks the finite representative-permutation invariants and the null-vector
intersection failure. Its decimal outputs are now outward-rounded 12-place
intervals, while comparisons use exact rational/algebraic arithmetic. The
reported completed gap bound is obtained from the supplied analytic `V` and
E2 bounds, not from enumerating the completion.

The signed control uses `nu=(2,-1)`, so `V=3`, baseline success is `1/9`,
and the event-test-plus-filter success outcomes are `4/9` and `1/9`. Thus
the checker assertion

    assert F(4,9)+F(1,9)!=F(1,9)

compares the correct total disturbed success `5/9` with the baseline `1/9`.
It is valid; the bare right-hand constant is somewhat opaque, but there is no
scale error or control defect.

More broadly, the finite script verifies four-outcome normalization for the
two seed inputs and a concrete symmetry check, while the operator identity
for every input and the sharp partition bound are established by the general
algebraic proofs above. It has no all-stage enumeration, no constructed
completed relabeling action, and no physical preparation/cost test. I did not
re-audit `PRIOR_WORK.md` or its primary-source locators. The pre/postselection
construction is a known mathematical representation applied here; no
priority, empirical, or temporal-ontology conclusion follows.

## Explicit finite circuit and resource boundary

I also inspected `CIRCUIT.md`. Its three-qubit history register has seven
supported basis states and one unused state. The listed A/B amplitudes have
the same modulus at each history, so the common vector
`phi_i=sqrt(w_i/V_3)` is normalized and each diagonal entry `a_(j,i)/w_i`
has unit modulus. Thus `Z_j phi` prepares the stated model input, conditional
on access to this model-dependent phase oracle. Any unitary completion of
`W|000>=phi` exists in this finite-dimensional space; conjugating the
zero-basis projector by `W` gives `Q_phi`. The sequence `W^*`, coherent
zero-test into the success qubit, then `W` therefore implements the claimed
binary projector instrument without measuring or discarding the history
register. Computing `F_3` into a separate event qubit preserves that test.

This construction is an exact finite circuit specification, not a gate-level
synthesis, resource scaling result, available gate-set proof, or hardware
demonstration. In particular, the history measure does not derive a physical
Hamiltonian or preparation procedure for `Z_j`; the model-dependent phase
preparation is an explicit assumption. Tracing out the history before the
coherent filter removes the interference needed for the success test, while
measuring a finer history PVM and coarse-graining can reproduce probabilities
without reproducing the retained-history instrument. The reported baseline
success omits the event test; after the event test the model-specific success
rates are `(1/2)/V_3^2` and `(29/50)/V_3^2`, with equal success-conditioned
event frequencies. These are distinct operational quantities, and none
supports an empirical or hardware claim by itself.
