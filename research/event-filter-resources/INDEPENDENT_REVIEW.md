# Independent mathematical review: record leakage claims

**Scope.** Independent review of `RECORD_LOSS.md` Sections 2–4, as requested. I did not edit the derivation, checker, builders, workboard, or other files. This is a mathematical audit, not a literature-priority search. Conclusions below concern the exact stated finite-dimensional models.

## Severity-ranked findings

### 1. No mathematical refutation found: exact positive-filter criterion is correct under its all-input model

Let the history register have basis \(|i\rangle\), and let the fixed channel be the pure-record Schur channel
\[
 C(\rho)_{ij}=G_{ij}\rho_{ij},\qquad G_{ij}=\langle e_j|e_i\rangle,\quad G_{ii}=1.
\]
For a binary success effect \(0\le Q\le I\), trace duality gives success probability \(\operatorname{Tr}(C^*(Q)\rho)\). With this convention, \((C^*Q)_{ij}=\overline{G_{ij}}Q_{ij}\). Equality of this probability to \(\eta\langle u_E|\rho|u_E\rangle\) for every density matrix is equivalent to the operator identity \(C^*(Q)=\eta |u_E\rangle\langle u_E|\); equality on all pure states already implies equality of Hermitian operators.

The diagonal equations give \(Q_{ii}=\eta\) on \(E\) and zero outside it. Positivity then forces every row and column outside \(E\) to vanish: for a positive matrix, \(|Q_{ij}|^2\le Q_{ii}Q_{jj}\). Within \(E\), the target off-diagonal entries require \(Q_{ij}=\eta/\overline{G_{ij}}\). The same 2-by-2 positivity inequality gives \(|G_{ij}|\ge1\), while normalized environment records imply \(|G_{ij}|\le1\). Thus equality is necessary for every pair in the event support. For unit vectors, equality in Cauchy–Schwarz is exactly parallelism of their rays. Conversely, if all these rays are parallel, the required restricted effect is \(\eta G_E\); it is positive with sole nonzero eigenvalue \(m\eta\), so it is an effect exactly when \(0<\eta\le1/m\). This proves the iff and the stated maximum efficiency.

The theorem depends essentially on: a fixed channel induced by normalized conditional environment kets; a binary success probability represented by one output effect; no access to the discarded environment; no input-dependent rescaling/calibration; and equality for every density operator on the full history register, including arbitrary coherent superpositions. It does not imply the same obstruction on a restricted preparation family: equality of expectation values need only hold on the real linear span of that family's states, which can be a strictly smaller operator space. Pre-channel encoding, correlated/reference-assisted inputs, environment measurement or erasure, and signed estimators are different tasks. Also, the target is the unnormalized quadratic form \(|u_E\rangle\langle u_E|\); interpreting it as a physical probability requires the efficiency factor, with \(\eta\le1/m\).

**Classification:** the proof is a short consequence of trace duality, positivity of effects, and equality in Cauchy–Schwarz. Those are generic established facts. The event-support formulation and its exact efficiency bound are a useful special-case packaging; this review does not establish priority or novelty.

### 2. No refutation found: the minimax operator-norm formula is correct for every stated boundary and dimension

Here is an independent reduction and derivation. For any effect \(Q\), the worst input probability discrepancy is
\[
 \sup_{\rho\ge0,\,\operatorname{Tr}\rho=1}
 |\operatorname{Tr}[(C_\gamma^*(Q)-P)\rho]|
 =\|C_\gamma^*(Q)-P\|_{\rm op},
\]
since the difference is Hermitian. The channel and \(P=|u\rangle\langle u|/m\) are invariant under basis permutations and complex conjugation. Averaging any feasible \(Q\) over these transformations preserves the effect constraint and cannot increase the convex operator-norm objective. The averaged matrix is real, has a common diagonal and common off-diagonal, hence is \(Q=aP+b(I-P)\), with \(0\le a,b\le1\).

Put \(c=(1-\gamma)/m\). Since \(C_\gamma^*(Q)=\gamma Q+(1-\gamma)\operatorname{diag}(Q)\), its eigenvalues along \(u\) and perpendicular to \(u\) are respectively
\[
 L= (\gamma+c)a+(m-1)c b,\qquad
 R= c a+(1-c)b.
\]
They lie in \([0,1]\), so the objective is \(\max(1-L,R)\). For \(\gamma>0\), increasing \(a\) by \(t\) and decreasing \(b\) by \(ct/(1-c)\), while feasible, holds \(R\) fixed and raises \(L\) by \(\gamma t/(1-c)>0\). Continue until either \(a=1\) or \(b=0\). If \(b=0\) occurs first, then with \(b=0\), \(L+R=(\gamma+2c)a\le1\) for all \(a\le1\), because \(m\ge2\) implies \(\gamma+2(1-\gamma)/m\le1\). Thus the objective there is \(1-L\), which decreases as \(a\) increases to 1. An optimum therefore exists at \(a=1\).

At \(a=1\), balancing the decreasing error \(1-L\) and increasing error \(R\) gives
\[
 b=\frac{(m-2)c}{1+(m-2)c},\qquad
 \min\max(1-L,R)=\frac{(m-1)c}{1+(m-2)c}
 =\frac{(m-1)(1-\gamma)}{m+(m-2)(1-\gamma)}.
\]
The balance point is feasible for all \(m\ge2\) and \(0\le\gamma\le1\). At \(\gamma=0\), the channel output is diagonal for every input effect; \(Q=I/2\) gives error \(1/2\), and no diagonal output effect can do better: its expectation on \(|u/\sqrt m\rangle\) is the mean diagonal value \(d\), and a Fourier-phase unit vector orthogonal to \(|u\rangle\) has the same expectation. Its worst error is therefore at least \(\max(1-d,d)\), minimized at \(d=1/2\). The displayed formula is then \(1/2\). At \(\gamma=1\), \(Q=P\) gives zero, agreeing with the formula. At \(m=2\), it reduces to \((1-\gamma)/2\), attained by \(Q=P\). Thus the boundaries and all dimensions requested check out.

Assumptions: finite-dimensional record space; the specific real scalar dephasing channel with fixed \(0\le\gamma\le1\); a single binary output effect; target exactly the normalized uniform rank-one projector; worst-case probability error over all density matrices; and observer access only after this channel. Changing the target, channel, access model, allowed instrument, or preparation domain changes the optimization. The script's grid is corroboration only; the symmetry reduction and affine minimization above supply the proof.

**Classification:** symmetrization/convexity and a two-variable linear minimax calculation are standard techniques. The closed form for this particular channel-target pair is a special-case result. No priority judgment follows from this derivation; a source search would be needed to call the formula new.

### 3. No refutation found: Fisher-information bound holds for locally unbiased estimation in the stated commuting product family

For \(0<r\le1\), the family \(\rho_x=(I+rxX)/2\), \(-1<x<1\), is diagonal in the fixed \(X\) basis. The \(N\)-copy state is diagonal in the product basis with probabilities
\[
 p_x(s_1,\ldots,s_N)=\prod_{k=1}^N\frac{1+r x s_k}{2},\quad s_k\in\{-1,+1\}.
\]
Any collective POVM has outcome probabilities obtained by applying a parameter-independent stochastic kernel to this classical label distribution: its kernel entries are the POVM's diagonal matrix elements in that basis. Classical Fisher information cannot increase under this processing. The label Fisher information is additive and equals \(N r^2/(1-r^2x^2)\). Therefore every regular locally unbiased estimator of \(\theta(x)=(1+x)/2\) obeys the scalar Cramér–Rao bound
\[
 \operatorname{Var}_x(\widehat\theta)\ge
 \frac{(d\theta/dx)^2}{I_N(x)}
 =\frac{1-r^2x^2}{4Nr^2}.
\]
Measuring \(X\) on each copy and using \(Y=(1+s/r)/2\) has mean \(\theta(x)\) and exactly this variance, so equality is attained. At \(x=0\), local unbiasedness gives RMSE squared equal to variance at that point; RMSE at most \(\delta\) therefore requires \(N\ge1/(4\delta^2r^2)\). For \(r=\gamma^n\), this yields the stated exponential expression. If \(r=1\), the same expressions remain valid for interior \(x\); the problem's intended leakage regime has \(0<r<1\).

Hidden assumptions: the unknown scalar \(x\) is common to all copies; the supplied state is exactly \(\rho_x^{\otimes N}\); the measurement is a parameter-independent POVM on those outputs (collective POVMs are included); there is no pre-leakage coherent access, environment access, or extra reference correlated with \(x\); and unbiasedness is local at the point where the bound is asserted, with the usual differentiability/finite-variance conditions for Cramér–Rao. This does not bound biased estimators, a global minimax risk, different input encodings or preparation families, or general history models. The rescaled single-shot estimator may fall outside \([0,1]\); it is a signed statistical estimator, not a positive event filter.

**Classification:** additivity of Fisher information for product samples, classical data processing, and the Cramér–Rao inequality are generic known results. The application to this commuting qubit family and its saturating estimator is elementary. The factor \(\gamma^{-2n}\) is valid for the stated experiment, not a general physical resource theorem. No novelty or priority claim is supported here.

## Overall verdict

All three statements withstand this review under their explicit models. I found no counterexample to the Schur-channel iff, the minimax formula (including \(\gamma=0,1\) and \(m=2\)), or the local Fisher-information lower bound for arbitrary collective POVMs on independent outputs. The most important qualification is domain scope: exact filtering is an all-input positive-effect claim; the minimax result is channel- and target-specific; and the sample cost is a local unbiased-estimation result for one commuting product family. Any broader physical or novelty conclusion needs separate assumptions and literature work.
