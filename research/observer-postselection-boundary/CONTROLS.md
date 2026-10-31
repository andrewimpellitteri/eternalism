# Observer-completion falsifiers and clean controls

Bounded sidecar control note. Scope: finite standard-form examples and exact
checks of the proposed postselection realization. This is not the coordinator's
derivation/checker, a literature review, or a causal-set detector construction.

## Bound: assumptions and sharpness control

Let a finite outcome PVM have atoms (P_i), and let normalized pre- and
postselected vectors (psi,phi) have nonzero overlap
(\alpha=\langle\phi|\psi\rangle). Define

\[
\nu_i=\frac{\langle\phi|P_i|\psi\rangle}{\alpha},\qquad
\sum_i\nu_i=1,\qquad V=\sum_i|\nu_i|.
\]

Then

\[
|\alpha|V=\sum_i|\langle\phi|P_i|\psi\rangle|
\leq\sum_i\|P_i\phi\|\,\|P_i\psi\|
\leq\Big(\sum_i\|P_i\phi\|^2\Big)^{1/2}
       \Big(\sum_i\|P_i\psi\|^2\Big)^{1/2}=1.
\]

Thus the success probability of the postselection *without an intervening
measurement* obeys (p=|\alpha|^2\leq V^{-2}). Equality is attained for any
finite normalized complex measure on its nonzero support in the auxiliary
space (L^2(|\nu|)). Write (h=d\nu/d|\nu|), so (|h|=1) almost everywhere,
and set

\[
\psi=h/\sqrt V,\qquad \phi=1/\sqrt V.
\]

Both vectors have unit norm; (
\langle\phi|P(E)|\psi\rangle=\nu(E)/V\), while
\(\langle\phi|\psi\rangle=\nu(\Omega)/V=1/V\). Their ratio is
\(\nu(E)\), and the success probability is (1/V^2\).

This verifies the candidate bound and equality construction under the stated
PVM and normalization assumptions. It does not imply that a scalar history
measure comes with this PVM, that the auxiliary space is the history Hilbert
space, or that (\nu(E)\) is a conditional detector probability. A key
convention to keep explicit is which success event is counted: the bound is
for final postselection without an intervening event measurement. An inserted
measurement generally changes that probability.

## Three invalid inferences and their valid counterparts

### 1. Weak value or squared measure treated as detector probability

**Invalid inference.** From (\nu(E)=\langle\phi|P_E|\psi\rangle/
\langle\phi|\psi\rangle\), infer that (\nu(E)\), or ( |\nu(E)|^2\), is the
conditional probability of obtaining detector outcome (E) after measuring
the PVM and then postselecting.

**Finite falsifier.** Take two PVM atoms and (\nu=(2,-1)\). This is normalized,
with (V=3). In the sharp construction, the unmeasured postselection success
probability is (1/9). The weak value of the first atom is 2 and its squared
modulus is 4, neither a probability. If the two-outcome PVM is actually
inserted, the successful joint amplitudes are (2/3) and (-1/3), so the
successful joint outcome probabilities are (4/9) and (1/9). The
postselection success probability after that measurement is (5/9), and the
conditional probability of the first result given successful postselection
is ( (4/9)/(5/9)=4/5\). It is neither 2 nor 4.

**Valid counterpart.** Treat (\nu(E)\) as a normalized transition-amplitude
ratio for the specified pre/postselection and PVM. For an intervening
projective measurement with one Kraus operator per result, compute joint
probabilities from ( |\langle\phi|P_i|\psi\rangle|^2\), then normalize by
their sum only when conditioning on successful postselection. That experiment
has a different success rate from the unmeasured postselection. Other
instruments require their own Kraus operators and probability calculation.

### 2. Pointer information assumed free of interference cost

**Invalid inference.** A pointer can learn which alternative occurred while
leaving the coherent postselection statistics unchanged.

**Finite falsifier.** Let (\nu=(1/2,1/2)\), so (V=1\), and use the sharp
construction (\psi=\phi=(1,1)/\sqrt2\). Without an inserted measurement,
postselection succeeds with probability 1 by coherent addition of the two
branch amplitudes. Couple a pointer to the two-atom PVM and leave orthogonal
which-branch records. The successful joint probabilities are (1/4,1/4\),
so postselection succeeds with probability (1/2\). The pointer has branch
information, while the cross-branch contribution to the postselection
probability is gone.

**Valid counterpart.** State the instrument and the coherence it preserves.
A pointer that distinguishes PVM sectors suppresses interference between
those sectors when its record is retained. A quantum-nondemolition pointer
for a *coarser* event can report that event and preserve coherence within its
eigenspaces; it need not reveal which alternative inside a sector. The
information/disturbance claim is therefore specific to the pointer coupling,
the recorded alternatives, and whether the pointer record is retained or
erased. It is not a universal ban on event information.

### 3. Auxiliary (L^2(|\nu|)) identified with the rank-one history Hilbert

**Invalid inference.** Because (L^2(|\nu|)) realizes the normalized measure
as a pre/postselected PVM matrix-element ratio, its dimension and event
projectors are automatically the intrinsic history Hilbert space and
operators supplied by the rank-one decoherence functional.

**Finite falsifier.** For (\nu=(1/2,1/2)\), the rank-one decoherence Gram
matrix on the two atoms is

\[
G_{ij}=\nu_i\overline{\nu_j}
 =\begin{pmatrix}1/4&1/4\\1/4&1/4\end{pmatrix},
\]

which has rank one. Its quotient history space is one-dimensional. In
contrast, (L^2(|\nu|)\cong\mathbb C^2\), and multiplication by the first
atom's indicator is the nontrivial projector \(\operatorname{diag}(1,0)\).
In the rank-one pre-quotient, the null vector \((1,-1)\) is sent by that
projector to \((1,0)\), which is not null. Therefore that event projector
does not descend to the quotient. The two spaces have different dimensions,
and the same event operator is not even well-defined on the quotient in this
example.

**Valid counterpart.** Call (L^2(|\nu|)\) an auxiliary realization or
dilation. The rank-one quotient and its operator algebra must be derived
separately. For any proposed event operator on a quotient, check the exact
descent condition: the operator must preserve the null subspace. The finite
example shows that a matrix-element realization alone does not establish
that condition.

## Mathematical defect check and limits

No defect was found in (p\leq1/V^2\) or its claimed (L^2(|\nu|)\) equality
case under the assumptions above: normalized finite complex measure, its
complete atomic PVM on the nonzero support, unit pre/postselected vectors,
nonzero overlap, and success defined as the unmeasured final postselection.
For (V=1\) the bound is the trivial (p\leq1\); for (V>1\) the finite
example ( (2,-1)\) saturates (1/9\). If the intended claim instead counts
success after an intervening event measurement, it is a different probability
and the stated bound does not follow by substituting the old overlap: the
instrument changes the state and success rate.

The checks above use exact rational arithmetic (standard-library
`fractions.Fraction`) for ( (2,-1)\), ( (1/2,1/2)\), the conditional
probability (4/5\), postselection rates (1/9\) and (5/9\), and the rank-one
Gram determinant. They are finite controls only. They do not establish an
operational completion for the atomless matched pair, a detector model, a
causal-set PVM, pointer nondemolition for that model, representation
covariance, or completed-causet observer physics. No primary-literature claim
or novelty claim is made in this sidecar.
