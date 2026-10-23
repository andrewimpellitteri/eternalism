# Explicit finite register implementation and resource ledger

This implements the stated auxiliary instrument for the actual depth-three
seed. It is an ordinary quantum-register construction, not an internal
causal-set observer. No hardware run or compiler synthesis is claimed.

Embed the seven histories in a three-qubit register H; the eighth basis state
has zero preparation amplitude. Use this ordered basis:

| Code | A amplitude | B amplitude | Event F3? |
| --- | --- | --- | --- |
| (0,0,0) | (3+4i)/40 | (3+4i)/40 | no |
| (0,0,1) | (3+4i)/40 | (3+4i)/40 | yes |
| (0,0,2) | (3+4i)/40 | (3+4i)/40 | yes |
| (0,0,3) | (11-12i)/40 | (11-12i)/40 | yes |
| (0,1,0) | (3+4i)/40 | (3-4i)/40 | yes |
| (0,1,1) | (3+4i)/40 | (3-4i)/40 | no |
| (0,1,3) | (7-4i)/20 | (7+4i)/20 | no |

Let w_i be the common amplitude modulus and V3=sum_i w_i. Define the common
positive vector phi_i=sqrt(w_i/V3) and choose a unitary W with W|000>=phi
(any orthonormal completion supplies one). The model-dependent diagonal phase
gate Z_j has entries a_(j,i)/w_i on the seven supported states and 1 on the
unused state. Its input psi_j=Z_j phi has unit norm. This phase oracle is a
PREPARATION assumption: the history measure alone does not give a laboratory
Hamiltonian that applies it.

1. Prepare H in phi using W and apply Z_j. Start event and success qubits in 0.
2. Coherently compute F3(H) into the event qubit, leaving H unchanged.
3. Apply W-adjoint on H, coherently toggle the success qubit iff H=000,
   and restore H with W. This implements the binary phi projector test.
4. Read both qubits. Keeping H until this test is essential. Tracing H out
   earlier leaves equal record statistics and removes access to this test.

The four retained-H Kraus operators are Q_phi P_a and (I-Q_phi)P_a,
so the four probabilities are exactly Eq. (6) of RESULT.md. If H is discarded,
a finer computational measurement followed by coarse-graining its outcomes
has the same output probabilities, but need not produce the same retained-H
instrument. A known arithmetic answer or a model-dependent output coin is not
this common apparatus.

The memory-only event frequency is common to the models. The joint
(event=yes, success=yes) gap is approximately 0.01942252585. The baseline
success is approximately 0.48556314631, but that baseline refers to omitting
the event measurement. With the event test the success rates are respectively
(1/2)/V3^2 and (29/50)/V3^2; after conditioning on success, both event
frequencies equal 1/2. The exact checker verifies these distinct quantities.

## Added resources and unresolved physics

The construction uses coherent storage of all seven alternatives, controlled
phase preparation, reversible event computation, and a final coherent filter.
There is no resource-scaling or locality result for larger histories. Arbitrary
finite-dimensional unitaries exist mathematically; their realization by a
causal-set observer is an additional question. Covariance of the final
instrument under the declared finite representative-permutation group does
not prove that each gate is in an available symmetry-constrained gate set.
The input B is not invariant under that group. A physical superselection or
preparation restriction could therefore exclude the proposed inputs even
where the mathematical apparatus is covariant. Full completed-history
relabeling covariance remains open.
