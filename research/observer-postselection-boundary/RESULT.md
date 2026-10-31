# From scalar history data to an explicit, conditional observer model

22 October 2026. Standard pre/postselection and measure-theoretic constructions
applied to the project pair; no novelty or internal causal-set detector claim.
See [prior work](PRIOR_WORK.md) and [contract](CLAIM_CONTRACT.md).

## 1. The representation question comes first

A scalar measure nu with nu(X)=1 defines the strongly positive kernel

    D(E,F)=conj(nu(E)) nu(F).

This conjugation convention makes D the inner product of event vectors;
conjugating both conventions changes none of the diagonal values. Its
D-derived history Hilbert space is one-dimensional: a finite event-vector
combination is represented by sum_E c_E nu(E), and the null space is the
kernel of this map. This is not the L2 history register in the previous pilot.
In particular, event intersection generally does not descend to an operator
on the quotient. [HISTORY_HILBERT.md](HISTORY_HILBERT.md) derives the criterion.
One-dimensionality does not erase the different event-vector assignments or
prove physical indistinguishability of two models. It shows that the larger
readout algebra requires an auxiliary completion, not just this reconstruction.

## 2. An intrinsic auxiliary representation

Let lambda=|nu| be the finite total-variation measure, V=lambda(X), and
h=dnu/dlambda. Polar decomposition gives |h|=1 lambda-almost everywhere and
V>=|nu(X)|=1. On H=L2(lambda) set

    psi=h/sqrt(V),     phi=1/sqrt(V),     P_E=M_(1_E).

Both vectors have norm one. Without an arbitrary reference measure or an
extra L2(P0) bound,

    <phi,psi>=1/V,
    <phi,P_E psi>=nu(E)/V,
    nu(E)=<phi,P_E psi>/<phi,psi>.                  (1)

This is precisely a projector weak value in established pre/postselection
language. It is not a frequency. The baseline postselection onto phi has
probability p0=1/V^2. The P_E form a PVM. This specifies a larger mathematical
register with a preparation and a final filter; it does not derive the
preparation or filter from causal-set dynamics. The earlier L2(P0) proof
remains valid but is unnecessary for this different representation.

For the matched atomless pair lambda_A=lambda_B=lambda by the accepted
variation-data theorem. Hence phi, P_E, V and the entire apparatus below
are COMMON to both models; only the input phase h_j differs. This avoids
an apparatus that secretly knows which model was prepared.

## 3. A sharp success bound for this named realization task

Suppose normalized vectors psi,phi and a PVM P on the given measurable space
realize a fixed normalized complex measure as in (1), with c=<phi,psi>!=0.
For any finite measurable partition E_1,...,E_m,

    |c| sum_i |nu(E_i)|
      =sum_i |<P_i phi,P_i psi>|
      <=sum_i ||P_i phi|| ||P_i psi|| <=1.

Taking the supremum over partitions gives |c|V<=1, so

    p0=|c|^2 <=1/V^2.                              (2)

Section 2 attains equality, including for a non-atomic finite measure.
Thus it is the optimal baseline success probability among exactly these
normalized pure-state, common-PVM, matrix-element-ratio realizations. In
independent repeated baseline trials the expected attempts per success are
at least V^2 and the construction attains that number. This omits preparation,
control, event-recognition and precision costs. It is NOT a universal sample
complexity lower bound, or a claim that every measurement must postselect.
Nonpostselected weak-value estimation circuits are known (PRIOR_WORK.md).

## 4. Derive access from a specific pointer coupling

Take a binary event E and a memory initialized in |0>. Let a controlled unitary
preserve the history register and prepare unit memory vectors u_1 on E and
u_0 on its complement:

    U = P_E tensor U_1 + P_Ec tensor U_0,
    U_a |0> = u_a.

This is a well-defined mathematical unitary even if E is infinite-history
measurable; that fact alone gives no finite implementation. Tracing out the
history register BEFORE any coherent final filter gives

    rho_M = lambda(E)/V |u_1><u_1|
            +lambda(Ec)/V |u_0><u_0|.              (3)

All phase dependence has disappeared. For any memory effect F, its pulled-back
history effect is

    <u_1,F u_1>P_E + <u_0,F u_0>P_Ec,

so the accessible effects are derived from this coupling, rather than merely
stipulated diagonal. Orthogonal pointer states allow every effect in this
binary membership algebra. The same calculation works for any finite
partition. Multiple history-diagonal controls and memory-only feedback remain
block-controlled and cannot expose the phase when the history is discarded.
This is a specified record observer; it is not a theorem about all observers.
The two matched models therefore give identical memory-only statistics.

If the experiment also retains the history register and postselects it onto
phi, the unnormalized memory state instead is

    m_j = [nu_j(E)u_1 + nu_j(Ec)u_0]/V.             (4)

This extra coherent history effect is exactly the new resource. It is outside
the memory-only access model. Let u_0=|0>, u_1=c|0>+s|1>, real c,s with
c^2+s^2=1 and 0<=c<=1. Then

    P_j(final success)
      = [mu_j(E)+mu_j(Ec)
         +2c Re(conj(nu_j(E))nu_j(Ec))]/V^2.       (5)

The baseline c=1 leaves no event record and has probability 1/V^2. A record
with c<1 changes interference. “History-preserving” in the basis is therefore
not “preserves the original decoherence functional.” Coherent postselection
plus a record can discriminate; record output by itself cannot.

## 5. A complete finite measurement and its four outcomes

For orthogonal records (c=0), measure the event membership, then postselect
onto phi. The joint instrument has Kraus operators

    K_(a,yes)=|phi><phi| P_a,
    K_(a,no)=(I-|phi><phi|) P_a,    a in {E,Ec}.

Their adjoint products sum to I. With input psi_j the outcome probabilities are

    P_j(a,yes) = mu_j(a)/V^2,
    P_j(a,no)  = lambda(a)/V - mu_j(a)/V^2.        (6)

Nonnegativity follows from |nu(a)|<=lambda(a)<=V, and all four sum to one.
The event and success outputs are ordinary probabilities in this augmented
register experiment. There is no weak-coupling approximation here.

The conditional probability after retaining only success trials is instead

    P_j(E | success, event test performed)
      = mu_j(E)/[mu_j(E)+mu_j(Ec)].                 (7)

It is generally NOT mu_j(E). The total success rate in this experiment is
[mu_j(E)+mu_j(Ec)]/V^2, not the baseline 1/V^2. This difference is the
measurement disturbance and must not be normalized away or hidden as loss.

## 6. Actual finite seed and completed pair

At depth three the seven amplitudes have common total variation

    V_3=(25+sqrt(265)+2sqrt(65))/40.

For F_3={M_3=2}, nu_A(F_3)=1/2 and nu_B(F_3)=1/2-i/5.
Complement amplitudes are 1/2 and 1/2+i/5. Thus

    mu_A(F_3)=mu_A(F_3c)=1/4,
    mu_B(F_3)=mu_B(F_3c)=29/100.

The common apparatus (6) distinguishes the models: the joint (E,yes) gap is
1/(25 V_3^2). Yet both success-conditioned E frequencies in (7) equal 1/2!
Discarding the success/failure rate discards this particular distinction.
For the partial pointer in (5), the total-success difference is

    P_B(success)-P_A(success) = (2/25)(1-c)/V_3^2.

This tends to zero as the event record is turned off. Memory-only outcomes
remain equal for every c. The checker verifies these identities by an
independent exact pointer-state expansion, as well as the full instrument.

For the completed pair V_N increases to V<16/7. Therefore the ideal
completed-register realization has optimal BASELINE success

    p0*=1/V^2 >49/256.

Its completed intrinsic E2 joint-success probability difference in (6) obeys

    [mu_B(E2)-mu_A(E2)]/V^2
      > (399999/10000000)(49/256) >0.

This is a lower bound in a stated auxiliary model, not a laboratory or
cosmological prediction. Finite approximant probabilities converge because
V_N->V and nu_j({M_N=2})->nu_j(E2). Neither numerical convergence nor a
positive abstract success rate bounds the physical cost of coherent access
to an infinite-history event. The finite prefix is not a completed covariant
predicate. Full operator/DF covariance of the pair was never assumed.

## 7. Symmetry: what the instrument actually respects

At finite depth three, define the auxiliary register group that permutes
representatives inside each finite-poset isomorphism class. This is a declared
finite register symmetry, not the full natural-label gauge structure. The
weights |a_C| agree within each class; hence phi has equal coefficients inside
each class and is fixed by these permutations. F_3 is a union of classes,
so P_F3 also commutes with the group. Consequently Q_phi and both products
in every K_(a,b) commute with the group: the full four-outcome instrument is
covariant with invariant outcome labels. Model B need not be an invariant
input state. Covariance of the apparatus does not force input invariance.

For completed histories the sufficient condition is stronger and explicit:
a specified group of measurable bijections must preserve lambda, and the
event E must be invariant. Its pullback unitaries on L2(lambda) then fix phi
and commute with P_E, so this same instrument is covariant. We have not
constructed that group action or proved lambda invariant under cosmological
natural relabelings. Cylinder norm covariance by itself is not such a proof.
The E2 predicate is intrinsic, but that does not settle the missing action,
preparation or physical control. This conditional result separates apparatus
covariance from the unproved full physical symmetry claim.

## 8. What has and has not advanced

We have a common, explicit apparatus with all outcomes and a sharp success
bound for its baseline pre/postselection representation; a record-only
observer algebra derived from a unitary; and a precise reason this is extra
structure beyond the D-derived Hilbert space. Known ingredients are being
applied, not claimed new. [CONTROLS.md](CONTROLS.md) and the independent
review record falsifiers and scope restrictions.

The unresolved physical step is now concrete: supply growth-system-plus-memory
dynamics that prepares these phase states, maintains the coherent history
register, implements its final filter, and respects completed-history
relabeling symmetry. Existence of an ordinary register circuit does not supply
such dynamics. Conversely, this gap does not prove no internal observer can
exist. No temporal ontology or direction of objective passage is selected.
