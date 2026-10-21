# Independent analytic review: clock-action audit

**Scope.** I reviewed the six claims in `RESULT.md` directly. This is an analytic audit of the stated finite-dimensional model, not a source-priority or novelty review. No tests, result files, board entries, or other files were changed.

## Verdict

I find no mathematical refutation of the six claims, with the assumptions and domains stated in `RESULT.md`. The scalar-origin criterion, alias characterization, exact allowed-coupling set at \(\epsilon=2\), cyclic-domain criterion, local-reading counterexample, and Gram-matrix criterion all check out. The formulas use dimensionless energies in units where the exponent's phase period is one; restoring units rescales the integer-gap condition accordingly.

## Claim-by-claim checks

### 1. Scalar origin repair and fixed-space aliases

Diagonalizing \(H\) gives
\[
 U_\lambda^N=e^{-2\pi i(H-\lambda I)},
\]
so this equals identity exactly when every eigenvalue satisfies \(E-\lambda\in\mathbb Z\). A scalar \(\lambda\) exists iff every pairwise energy gap is an integer. This confirms the stated scalar-origin repair criterion. A scalar phase in \(U^N\) can be removed by shifting \(\lambda\); a nonscalar \(U^N\) cannot be removed by one scalar shift. This is a statement about the specified linear action on vectors; a ray-level/projective action is a separate question.

Independently of closure, \(U_\lambda\)'s eigenvalue is one exactly for \(E=\lambda+kN\), so
\[
 \operatorname{Fix}(U_\lambda)=\bigoplus_{k\in\mathbb Z}V_{\lambda+kN}.
\]
The fixed space equals \(V_\lambda\) exactly when no distinct occupied energy in that congruence class occurs. The stated examples check: at \(\epsilon=1,g=0,\lambda=-1/2\), energies \(-1/2\) and \(5/2\) alias; at \(\epsilon=2,g=0\), \(V_0\) aliases with \(V_3\), while \(V_1\) is a different two-dimensional fixed space. Width less than \(N\) suffices to rule out aliases, but is not necessary.

### 2. Exact allowed \(g\) classification at \(\epsilon=2\)

The untouched clock sectors have energies \(-1,1\) and \(1,3\). The interacting sector has \(1\pm s\), where \(s=\sqrt{1+g^2}\). Since \(-1\) is present, any valid common origin has integer fractional part; consequently both \(1+s\) and \(1-s\) must be integers, equivalent to \(s\in\mathbb Z\). Conversely, integer \(s\) makes every energy integral, so the unshifted action closes. Thus for real \(g\), the exact set is
\[
 g^2=k^2-1,\quad k=1,2,3,\ldots,
\]
including \(g=0\). At \(g=\sqrt3\), the spectrum is \(\{-1,-1,1,1,3,3\}\); at \(g=\sqrt8\), the energies are \(-2,-1,1,1,3,4\). For \(\lambda=-2\), the fixed space is \(V_{-2}\oplus V_1\oplus V_4\), of dimension \(1+2+1=4\), while the Dirac surface \(V_{-2}\) has dimension one. These checks support the claimed classification for this Hamiltonian only.

### 3. Minimal seed-output cyclic domain

Let \(W=\operatorname{span}\{U^kM_0v:k\in\mathbb Z,v\in V\}\). It is invariant under \(U\) and \(U^{-1}\). Since \(U^N\) commutes with every power of \(U\), \((U^N-I)M_0v=0\) for all \(v\in V\) implies \((U^N-I)=0\) on every generator of \(W\), hence on \(W\). Conversely, if \(U^N=I\) on \(W\), it holds on \(M_0V\subseteq W\). The iff criterion is therefore correct (including the vacuous zero-range case).

For \(\epsilon=2,g=1/2,\lambda=1\), \(V_1=\operatorname{span}\{|0,\uparrow\rangle,|2,\downarrow\rangle\}\), and the stated Fourier clock seed maps it onto \(|\tau_0\rangle\otimes\mathbb C^2\). Its \(n=1\) clock component contains spin-up, which has nonzero overlap with both eigenvectors of the interacting block \(\sigma_z+\tfrac12\sigma_x\). The corresponding eigenvalues of \(U_1^3\) are \(e^{\mp i\pi\sqrt5}\ne1\). Thus \(U_1^3\) is not identity on the seed image, and restricting only the physical input to \(V_1\) does not repair this seed-orbit action.

### 4. Local reading covariance despite a commuting interaction

At \(\epsilon=2,g=\sqrt3,\lambda=1\), \(V_1\) contains \(|0,\uparrow\rangle\). With the normalized three-point Fourier clock, \(P_0|0,\uparrow\rangle=|\tau_0,\uparrow\rangle/\sqrt3\). In the \(n=1\) block, \(H-I=\sigma_z+\sqrt3\sigma_x\), whose square is \(4I\). Therefore the off-diagonal spin amplitude of \(U_1\) in that block is
\[
 -i\frac{\sqrt3}{2}\sin(4\pi/3)=i\frac34.
\]
The input clock component at \(n=1\) contributes another factor \(1/\sqrt3\), in addition to the initial \(1/\sqrt3\), so \(U_1P_0|0,\uparrow\rangle\) has a nonzero \(|1,\downarrow\rangle\) component of magnitude \(1/4\). By contrast, \(P_1|0,\uparrow\rangle\) has spin-up only. Hence \(U P_0|_{V_1}=P_1|_{V_1}\) fails. The interaction commutes with \(H_C\otimes I\) because it is supported on one clock eigenspace, but that commutation does not imply translation of the specified Fourier readings. This confirms the explicit counterexample.

### 5. Gram-matrix condition for conditioning

For \(R_k=\sqrt N(\langle\tau_k|\otimes I)J\), a map defined by \(T_k(R_0v)=R_kv\) is well-defined exactly when \(\ker R_0\subseteq\ker R_k\). Equality \(R_k^\dagger R_k=R_0^\dagger R_0\) gives equality of norms and inner products, hence equal kernels and a range-to-range isometry; it is onto \(\operatorname{ran}R_k\). Conversely, such an isometry forces equality of the Gram matrices. If \(R_0\) is invertible and input and system dimensions agree, \(T_k=R_kR_0^{-1}\) is unitary exactly under this condition. When the maps are rank-deficient, the condition only identifies an isometry on the accessible ranges and says nothing about a unitary action on inaccessible degrees of freedom.

Finally, \(\sum_kR_k^\dagger R_k=NI\) follows from completeness of the readings and isometry of \(J\). Thus if all \(R_k^\dagger R_k\) are equal, each equals \(I\). Conversely, \(R_k^\dagger R_k=I\) is exactly uniform probability \(1/N\) for reading \(k\) on every normalized physical input. The normalization factor \(\sqrt N\) in the definition of \(R_k\) is essential to this identity; the unscaled slice Gram matrices equal \(I/N\). The stated all-input and rank qualifications are appropriate.

## Limits

These verifications establish only the stated matrix identities and counterexamples for the specified Hamiltonian, seed, and clock readings. They do not establish correspondence to every construction in the cited papers or support any novelty or ontological conclusion.


## Review of the added finite checks and corrected alias count

I reread the current `RESULT.md` and inspected `check.py` and `output.txt`. The corrected \(g=\sqrt8,\lambda=-2\) multiplicity is right: \(V_{-2}\), \(V_1\), and \(V_4\) contribute dimensions 1, 2, and 1, respectively, so the fixed space has dimension 4. The reported block-exponential, seed-wrap, reading-covariance, and direct-reduction outputs are consistent with the analytic calculations above. They corroborate the finite examples; the exact spectral and Gram-matrix arguments remain the basis of this review. The script uses floating-point matrix exponentials for those checks, so its numerical pass does not itself prove the general claims.
