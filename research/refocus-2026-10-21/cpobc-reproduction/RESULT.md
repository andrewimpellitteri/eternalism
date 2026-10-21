# CPOBC obstruction reproduction

Status: **reproduced, restricted 2×2 self-adjoint nonsingular obstruction** (2026-10-21). This reconstructs the self-adjoint commutativity argument in Xu, arXiv:2607.26672v1, Sec. 29.11, Eqs. (252)–(260), for the stated square-operator CPOBC identities. The final propagation from centrality of an antichain generator to all transition operators is imported from the source's central-generator lemma. This is not a reproduction of the full Theorem 29.12 and says nothing about non-self-adjoint or singular branches.

## Exact derivation

The reproduced argument uses the following necessary operator identities from the source: $[F,Q_n]=0$, where $F=Q_1(I-Q_1)$ (Eq. (253)); $[Q_1Q_2^{-1},Q_1^{-1}Q_2]=0$ (Eq. (258)); and, after defining $R=Q_2Q_1^{-1}$, $[R,Q_n]=0$ (the three-generator CPOBC relation following Eq. (259)). It also uses self-adjointness and nonsingularity of $Q_1,Q_2$, the two-element chain timid transition, and the two-precursor timid transitions.

First prove $[Q_1,Q_2]=0$. Put $A=Q_1$, $B=Q_2$. On any spectral subspace of $A(I-A)$, the spectrum of self-adjoint $A$ contains at most a complementary pair $q,1-q$. In a nontrivial pair block write

$$
A=\begin{pmatrix}qI&0\\0&(1-q)I\end{pmatrix},\qquad B=\begin{pmatrix}U&D\\D^*&V\end{pmatrix}.
$$

The second commutator identity gives $[AB^{-1},C]=0$, where $C=A^{-1}B$. Since $AB^{-1}=(ACA^{-1})^{-1}$, invertibility makes this equivalent to $[ACA^{-1},C]=0$. Finally $ACA^{-1}=BA^{-1}=C^*$, so this is $[C,C^*]=0$. Its upper diagonal block is exactly

$$
\big(q^{-2}-(1-q)^{-2}\big)DD^*.
$$

Invertibility excludes $q=0,1$. For $q\ne1/2$, the coefficient is nonzero, so positivity of $DD^*$ gives $D=0$; for $q=1/2$, $A$ is scalar on that block. Thus $[Q_1,Q_2]=0$. The script checks the coefficient with an exact rational mixed-block control $q=1/3,D=1$, where it equals $27/4\ne0$, and a diagonal commuting control.

Now $R=Q_2Q_1^{-1}$ is self-adjoint and commutes with $Q_1$, while $[R,Q_n]=0$. If a 2×2 $R$ has distinct eigenvalues, this last identity makes $Q_n$ diagonal in the common eigenbasis, hence $[Q_1,Q_n]=0$. This covers the distinct-$R$ case directly. If $R=rI$, the chain timid transition $T_2=I-R$ is nonsingular, so $r\ne1$. The remaining possibility is mixing between the complementary eigenvalues $q,1-q$ of $Q_1$, which is where the two-precursor condition is needed.

Xu's chain reduction gives $Q_2=Q_1R$, $T_2=I-R$, and the two-element-antichain timid transition $S=I-(2I-Q_1)R$, with $A_n^{(2)}=S Q_n Q_2^{-1}$ (Eqs. (259)–(260)). On a two-dimensional complementary-eigenvalue block, take

$$
Q_1=\begin{pmatrix}q&0\\0&1-q\end{pmatrix},\quad R=rI,\quad
Q_n=\begin{pmatrix}u&D\\\overline D&v\end{pmatrix}.
$$

Then $Q_2=\operatorname{diag}(qr,(1-q)r)$, $S=\operatorname{diag}(s_q,s_{1-q})$, where

$$
s_q=1-(2-q)r,\qquad s_{1-q}=1-(1+q)r.
$$

The off-diagonal entries of $A_n^{(2)}$ are

$$
(A_n^{(2)})_{12}=\frac{s_qD}{(1-q)r},\qquad
(A_n^{(2)})_{21}=\frac{s_{1-q}\overline D}{qr}.
$$

Self-adjointness therefore requires

$$
\big(qs_q-(1-q)s_{1-q}\big)D=0,
\quad qs_q-(1-q)s_{1-q}=(2q-1)(1-r).
$$

This is exactly Eq. (260)'s coefficient, obtained directly from the displayed transition matrices. Nonsingularity requires $q(1-q)\ne0$, $r\ne0$, $1-r\ne0$, $s_qs_{1-q}\ne0$, and $\det Q_n\ne0$ on this block. If $q\ne1/2$, those conditions force $D=0$. At $q=1/2$, the two $Q_1$ eigenvalues coincide, so this is not mixing between distinct eigenvalues. Thus $Q_1$ commutes with every antichain generator $Q_n$. The conclusion that this central antichain generator forces the **full transition algebra** to be commutative uses Xu's cited central-generator lemma; that propagation lemma is imported, not re-proved here.

The proof uses operator self-adjointness and the operator CPOBC transition relations. It does not replace vector-measure covariance with norm covariance or insert a path-dependent phase.

## Exact controls and run

`check.py` uses only Python's standard-library `Fraction` and exact 2×2 matrix operations. It also compares exact polynomial coefficient maps for $qs_q-(1-q)s_{1-q}=(2q-1)(1-r)$. `check-output.txt` is the saved output.

- **Positive commuting control:** $q=1/3,r=1/2,Q_n=\operatorname{diag}(2,3)$. Exact determinants are $\det Q_1=2/9$, $\det Q_2=1/18$, $\det Q_n=6$, $\det T_2=1/4$, $\det S=1/18$, $\det A_n^{(2)}=6$. The transition is self-adjoint and $[Q_1,Q_n]=0$.
- **Rejected noncommuting candidate:** same $q,r$, $Q_n=\left(\begin{smallmatrix}2&1\\1&3\end{smallmatrix}\right)$. All listed determinants remain nonzero ($\det Q_n=\det A_n^{(2)}=5$), but $A_n^{(2)}=\left(\begin{smallmatrix}2&1/2\\2&3\end{smallmatrix}\right)$ is not self-adjoint; the exact obstruction coefficient is $-1/6$.
- **Rejected singular control:** same $q,Q_n$, but $r=1$. The mixing candidate produces a self-adjoint $A_n^{(2)}$, while $\det T_2=0$ and the coefficient vanishes. This is the excluded singular chain-timid-transition boundary, illustrating why $r\ne1$ is essential.
- **Singular $Q_1$ control:** $q=0$ gives $\det Q_1=0$, so $Q_1^{-1}$ is unavailable and the calculation rejects it before applying the obstruction.
- **Complementary-block identity control:** at $q=1/3$ with $D=1$, the exact upper-block commutator is $27/4$; with diagonal $B$, it vanishes.
- **Simple-$R$ control:** distinct rational eigenvalues of $R$ force $[R,Q_n]=0$ to set the off-diagonal of $Q_n$ to zero.
- **Distinct noncomplementary-spectrum control:** for $Q_1=\operatorname{diag}(1/3,1/4)$, the eigenvalues of $F=Q_1(I-Q_1)$ are $2/9$ and $3/16$; the mixed test matrix gives $[F,Q_n]_{12}=5/144\ne0$.

Run: `python3 research/refocus-2026-10-21/cpobc-reproduction/check.py` — **PASS**, exact rational arithmetic. No timeout or numerical tolerance is involved.

## Feasibility of the remaining first-simple-spectrum chart

Xu's normalized chart is

$$
Q_1=\begin{pmatrix}a&1\\q&d\end{pmatrix},\qquad
Q_2=hQ_1,\qquad R_3=\operatorname{diag}(1,x),\qquad R_4=\operatorname{diag}(1,y).
$$

This lane treats the diagonal $R_3,R_4$ form as a **restricted chart/ansatz**; it has not established that it follows from a general gauge or simultaneous-reduction argument. Within this ansatz, retain the first-simple-spectrum condition $x\ne1$, as well as $x,y\ne0$ for invertibility. The six displayed scalar parameters are $(a,d,q,h,x,y)$, and the two-element chain requires $h\ne0,1$. Explicit necessary determinant exclusions include

$$
\det Q_1=ad-q\ne0,\qquad \det(I-Q_1)=(1-a)(1-d)-q\ne0,
$$

plus every determinant of the generated stage-three and later transition operators. Saturate by the complete transition determinant product, not just these displayed factors. On the trace-balanced slice $d=a$ only, $q-a^2=-\det Q_1$; in the general chart the determinant is $ad-q$.

The source gives a scale estimate on the restricted trace-balanced slice $d=a,x=-1$: substitution into twelve determinant-cleared stage-three residuals yields factor $(y-1)(q-a^2)$; after separating $y=1$ and removing the singular $q-a^2=0$ boundary, the remaining equations split into the $E_1,E_2$ pieces reported in Eq. (257), and next-stage equations exclude them. The authors explicitly report that eliminating $d-a$ and $x+1$ from their full saturated first-simple-spectrum ideal did not yield a finite characteristic-zero certificate (Sec. 29.11 proof).

**Concrete next method:** first establish the normalized $Q_1$ chart for the intended representation class, but do not assume the diagonal $R_3,R_4$ form without proving it. For the restricted ansatz, regenerate the twelve stage-three residuals from the finite transition catalog; use fraction-free denominator clearing; saturate by the full product of required transition determinants, $ad-q$, $(1-a)(1-d)-q$, $h$, $1-h$, $x$, $y$, and the simple-spectrum factor $x-1$ (or retain $x\ne1$ as an inequation). Then split only on factors certified by the residual ideal, starting with $y-1$, $d-a$, and $x+1$. Run modular Gröbner/elimination over several good primes, reconstruct rational basis elements, and verify each proposed basis by exact reduction over $\mathbb Q$. If that stalls, use triangular decomposition/regular chains and report the inequations explicitly. No SymPy, Singular, Sage, Mathematica, or Wolfram executable was installed; dependencies were not installed, and the larger chart computation was not attempted.

**Feasibility judgment:** a bounded stage-three elimination is plausible once the residual list and determinant product are available, because the published restricted slice reduces to low-degree factors. A global characteristic-zero certificate is uncertain: Xu reports a prior attempt did not find one, and the six-variable saturation plus proof of the diagonal ansatz are additional burdens. Treat modular output as a lead until exact rational verification succeeds. Kill or narrow this restricted target if (i) the residual catalog cannot be independently regenerated from the transition rules, (ii) every apparent component is removed by required determinant saturation, or (iii) survivors lie only on excluded boundaries such as $x=1$, $ad-q=0$, $(1-a)(1-d)-q=0$, $h=0,1$, or $xy=0$. The condition $q-a^2=0$ is a kill criterion only after restricting to $d=a$. If all regular components disappear, report only an exclusion for this restricted chart/ansatz, not a general 2×2 theorem. A surviving regular component requires checking the next antichain stage before any existence claim.

## Source and companion-certificate audit

Primary version PDFs are retained beside this report. SHA-256 hashes:

- Srivastava–Surya, arXiv:2603.25503v1: `545c2c1a6a0ad046bcb41612a0d108030601992ccc9e3c9d472dec3d92cc89aa`.
- Xu, arXiv:2607.26672v1: `206e0e286aea66c857a31ef9b58140bacee6be0912569fc9962aa47a688d0fd2`.

The Xu manuscript cites a companion manuscript as supporting material for its larger triangular and chart calculations, but I did not locate a public companion certificate or code artifact in the source record/indexed search. The reproduced local block calculations above are reconstructed directly and do not rely on that companion. The Srivastava–Surya appendix is a second primary candidate; its Pauli assignment and invertibility conditions were inspected, but its longer Appendix calculation was not counted as independently reproduced here.
