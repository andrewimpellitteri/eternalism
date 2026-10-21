# Corrected comparison: three constraint conventions on a clock–qubit model

This is a finite-dimensional application of published constructions, not a new result. Units use \(\hbar=1\) and clock spacing \(\omega=1\). Energies below are dimensionless in these units. Calculations use Python's standard library only; spectral clustering tolerance is stated with the implementation.

## Shared kinematics

The clock is \(\mathbb C^3\), with energy basis \(|n\rangle\), \(n=0,1,2\), Hamiltonian \(H_C=\mathrm{diag}(0,1,2)\), and readings
\[
 |\tau_k\rangle=3^{-1/2}\sum_{n=0}^2e^{-2\pi i nk/3}|n\rangle,\qquad k\in\mathbb Z_3.
\]
The system is a qubit with \(H_S=(\epsilon/2)\sigma_z\), and the total Hamiltonian in formulation A is
\[
 H=H_C\otimes I+I\otimes H_S+gK\otimes\sigma_x.
\]
We use \(K_{rd}=|\tau_0\rangle\langle\tau_0|\) and \(K_{en}=|1\rangle\langle1|\). In particular, \([K_{en},H_C]=0\), while \([K_{rd},H_C]\ne0\). The shared readout is \(p(k)=\| (\langle\tau_k|\otimes I)\psi\|^2\); a normalized conditional vector, when \(p(k)>0\), is \(\sqrt3(\langle\tau_k|\otimes I)\psi\).

The cases \(\epsilon=1,2\), \(g=0,1/2\), and the resonant check \((\epsilon,g,K)=(2,\sqrt3,K_{en})\) are diagnostics, not a parameter survey. For \(K_{en}\), the spectrum is exactly
\[
 -\epsilon/2,\quad \epsilon/2,\quad 1\pm\sqrt{(\epsilon/2)^2+g^2},\quad 2-\epsilon/2,\quad 2+\epsilon/2.
\]
No full spectral classification is claimed for \(K_{rd}\).

## A. Hamiltonian-eigenvalue constraint

For each selected real \(\lambda\), the physical sector is \(V_\lambda=\ker(H-\lambda I)\). This formulation permits any eigenvalue; it imposes no lattice or periodicity condition. The comparison must name \(\lambda\). An eigenspace at one value cannot be compared to an invariant sector at another merely because their dimensions match.

## B. Step-invariance / history-state construction

Primary constructions: Boette–Rossignoli, arXiv:1806.00956v2, Sec. II, Eqs. (1)–(9), which defines a finite clock orbit with unitary steps and requires cyclic closure (text immediately before Eq. (2)); and Hausmann–Schmidhuber–Castro-Ruiz, arXiv:2308.10967v4, Sec. 5, Eqs. (24)–(27), with derivation in App. G, Eqs. (116)–(122). The latter uses an infinite, aperiodic clock index \(k\in\mathbb Z\); it does not require a finite wraparound. Read depth: full text at these constructions and locators, not a full-paper audit.

For the finite \(Z_3\) implementation, set
\[
 U=\sum_{t\in\mathbb Z_3}|\tau_t\rangle\langle\tau_{t-1}|\otimes U_{t,t-1},\qquad
 M=U_{0,2}U_{2,1}U_{1,0}.
\]
The fixed-vector equation \(U|\Psi\rangle=|\Psi\rangle\) has a mathematical solution space whether or not \(M=I\). Only when \(M=I\), equivalently \(U^3=I\), is this a representation of \(Z_3\) and the finite cyclic construction used by Boette–Rossignoli. When closure fails, report \(E_1(U)\), the monodromy, and wrap defect as diagnostics; do not label them a \(Z_3\) action or a closed finite history.

The code retains three explicitly different step conventions:

- B1 uses the same \(V=e^{-iH_St_1}e^{-ig t_1\sigma_x}\) on every step. Its closure is tested, not presumed.
- B2 places the kick on the step leaving \(\tau_0\), uses free steps elsewhere, and chooses the last step as \((U_{2,1}U_{1,0})^{-1}\). This is a closure-imposed kick convention of the type allowed by the finite construction.
- B3 uses the same first two steps as B2 and a free final step. It is a finite three-step diagnostic inspired by the local kick choice; the HSC construction itself has no wraparound.

These are choices of step unitaries, not derived translations of the single Hamiltonian \(H\). B2's compensating last step changes the step schedule. A same-model or physical equivalence claim requires an explicit intertwiner preserving the selected states and readout instrument; none is asserted here. At zero coupling, cumulative maps are compared with \(e^{-iH_St_k}\) as a known-limit check.

## C. Finite-group action construction and its candidate on this model

The source anchor is Ludescher et al., arXiv:2607.24976v1, Sec. IV.1 and App. B.2, Example 32, Eqs. (58)–(60). Its finite Abelian example has an actual group action, an explicitly specified invariant/kernel sector, and frame seeds. The comparison includes a small implementation of its position-level Eqs. (58)–(59) as a construction check; it does not use that example to infer an arbitrary real-spectrum clock action. Read depth: full text at the named construction, not full-paper or code audit.

For the present Hamiltonian and a chosen scalar origin \(\lambda\), define the candidate generator
\[
 U_\lambda=\exp[-2\pi i(H-\lambda I)/3].
\]
This is a \(Z_3\) representation on the kinematic space iff \(U_\lambda^3=I\), equivalently every energy obeys \(E-\lambda\in\mathbb Z\). Some scalar origin exists iff all energy gaps are integers. The code prints both the selected-origin wrap defect and a numerical integer-gap residual; the latter is a finite diagnostic, not an exact classification, especially for \(K_{rd}\).

The fixed space can be computed even when closure fails, but then it is only \(\mathrm{Fix}(U_\lambda)\), not the physical space of a claimed finite-group action. In a valid action,
\[
 \mathrm{Fix}(U_\lambda)=\bigoplus_{j\in\mathbb Z}V_{\lambda+3j}.
\]
Thus aliases must be shown explicitly. A matched comparison uses the same \(\lambda\) in A and \(U_\lambda\); the excess fixed-space dimension is the alias multiplicity when closure holds.

For \(P_k=|\tau_k\rangle\langle\tau_k|\otimes I\), the actual local-readout covariance condition on a selected invariant input space \(V\) is
\[
 U_\lambda^k P_0|_V=P_k|_V.
\]
Commutation of \(H_{int}\) with \(H_C\otimes I\) alone is not this condition. We evaluate the seed orbit on a spanning basis of the selected fixed space and the readout factorization/completeness on superpositions. A decisive check is \(\epsilon=2,g=\sqrt3,K=K_{en},\lambda=1\): closure holds and \(V_1\) is two-dimensional, yet the interacting \(n=1\) block rotates spin and the local position seed fails to covary. Hence even a valid action and \([K_{en},H_C]=0\) do not suffice for this specified local seed.

## Matched-origin and zero-coupling checks

The principal matched cases are:

| \(\epsilon,g,K\) | selected \(\lambda\) | A: \(\dim V_\lambda\) | C: wrap / \(\dim\mathrm{Fix}(U_\lambda)\) | Reading/alias point |
|---|---:|---:|---|---|
| \(1,0,K_{rd}\) | \(1/2\) | 2 | closes / 2 | no alias; same selected sector |
| \(1,0,K_{rd}\) | \(-1/2\) | 1 | closes / 2 | \(V_{5/2}\) aliases into the fixed space |
| \(2,0,K_{en}\) | 1 | 2 | closes / 2 | no alias; matched sector |
| \(2,0,K_{en}\) | 0 | 1 | closes / 2 | \(V_3\) aliases with \(V_0\) |
| \(2,1/2,K_{en}\) | 1 | 2 | fails / 2 | nonclosing unitary diagnostic; same \(V_1\) appears in the fixed space, but no \(Z_3\) action |
| \(2,\sqrt3,K_{en}\) | 1 | 2 | closes / 2 | matched sector; local seed/readout covariance fails |
| \(2,\sqrt3,K_{en}\) | 0 | 0 | closes / 2 | \(V_3\) aliases; dimension agreement with another sector is not sector identity |

At \(g=0\), A's two-dimensional surfaces are \(\lambda=1/2,3/2\) for \(\epsilon=1\), and \(\lambda=1\) for \(\epsilon=2\). The scalar-origin-shifted cyclic candidates reproduce the selected sector at \(\lambda=1/2\) and \(\lambda=1\), respectively. The unshifted \(\lambda=0\) comparison for \(\epsilon=1\) is empty in both formulations and is not compared to A's half-integer sectors. B2 has a two-dimensional closed history space by construction and recovers the free conditional system evolution at zero coupling. B1/B3 are evaluated with their stated step schedules and must pass their own closure test before being called finite cyclic actions.

The tables do not identify the three mathematical constructions as one physical model. They compare dimensions and readouts under explicit conventions; dynamical/operational equivalence is not claimed without an intertwiner. Nothing here fixes a temporal ontology.
