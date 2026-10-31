# Echo robustness: how narrowly the antipodal scalar identity depends on its field equation

Task `horizons-echo-robustness`, 25 October 2026. Worker submission for
independent review; not an accepted result and not a novelty claim.

## 0. Summary

The dispatch's Proposition (echo) says that in the closed dust model, the
conformally coupled massless scalar is determined on an antipodal echo of the
past, via the identity

$$\psi(\eta+\pi,-X)=-\psi(\eta,X)\qquad\text{for every smooth solution}\tag{E}$$

of the rescaled equation $\partial_\eta^2\psi=\Delta\psi-\psi$ on the unit
Einstein cylinder $\mathbb{R}\times S^3$ (Wald App.~D transformation; mode
argument in the dispatch). We perturb the field equation to
$\psi_{tt}=\Delta\psi-(1+\delta)\psi$ with constant $\delta\in\mathbb{R}$ and
ask for which $\delta$ identity (E) holds for **every** smooth solution with
**arbitrary** Cauchy data.

**Result.** (E) holds for all smooth solutions **iff $\delta=0$** (Theorem 2).
The exact degree-by-degree condition is $\omega_n^2=(n+1)^2+\delta>0$ and
$\omega_n\equiv n+1\pmod 2$, equivalently the integer lattice
$\delta=4k(n+1+k)$ with $(n+1)+2k>0$ (Theorem 1); every $\delta\neq0$ leaves
all sufficiently large degrees violating, with explicit single-mode failure
witnesses (Sec.~3; machine-checked in `check_modes.py`).

**Distinctions the task asked for.**

- *Geometry vs field.* The antipodal **refocusing of null cones** after
  conformal time $\pi$ and the **refocusing of singular supports** are
  $\delta$-independent causal-geometry facts (principal symbol unchanged).
  The **value echo** (E) is a fragile spectral resonance of the massless
  conformal scalar. In the Einstein static universe, determination from a
  past is complete ($F_{\mathcal L}(b)=M$) for **every** $\delta$, by
  slice-swallowing alone — no echo needed. The echo matters only on the dust
  strip before maximum expansion, and there it is destroyed by any
  $\delta\neq0$.
- *Loss of (E) $\neq$ loss of all nonlocal determination.* For every
  $\delta$, the spatial mean (degree-0 projection) of any solution vanishing
  on $I^-(b)$ vanishes identically: an integral, non-pointwise determination
  survives on the strip (Sec.~5.3).
- *ESU constant potential $\neq$ dust mass.* An ordinary massive scalar on
  closed dust rescales to the **time-dependent** potential
  $v(\eta)=1+m^2a(\eta)^2$, which is not $\pi$-periodic; the solution space
  is not even invariant under the echo map, so (E) fails a fortiori. No
  dust-mass conclusion is drawn from the constant-$\delta$ ESU analysis
  (Sec.~6).

**Verdict for the manuscript.** The echo proposition is maximally
field-equation-dependent: no constant-potential perturbation of the
conformal scalar preserves its mechanism. Whether any pointwise
determination beyond $J^-(b)$ survives on the strip at $\delta\neq0$ remains
open, as does the paper's own exactness question at $\delta=0$.

## 1. Setup and conventions

$\mathbb{R}\times S^3$ with product metric $-dt^2+d\Omega_3^2$ (unit Einstein
cylinder / static universe), $\Delta$ the positive-laplacian-sign convention
$\Delta=$ Laplace–Beltrami with $-\Delta Y_n=n(n+2)Y_n$ on degree-$n$
spherical harmonics. The field equation studied:

$$\psi_{tt}=\Delta\psi-(1+\delta)\psi,\qquad \delta\in\mathbb{R}\ \text{constant}.\tag{1}$$

$\delta=0$ is the conformally coupled massless scalar after rescaling
($\Box_{\tilde g}-\tfrac16\tilde R$ with $\tilde R=6$); $\delta\neq0$ is a
constant potential shift, equivalently an ESU Klein–Gordon mass $m^2=-\delta$
or a shifted conformal coupling. Solutions are smooth on all of
$\mathbb{R}\times S^3$; the Cauchy problem from any slice $t=t_0$ is
well-posed for every $\delta$ (linear wave equation with smooth
coefficients), so "arbitrary position/velocity data" is meaningful.

Standard facts used (all classical):

- (F1) $-\Delta$ on $S^3$ has eigenvalues $n(n+2)$, $n=0,1,2,\dots$, on the
  space $\mathcal{H}_n$ of degree-$n$ spherical harmonics, with
  $\dim\mathcal{H}_n=(n+1)(n+2)/2$; the restrictions of homogeneous harmonic
  polynomials of degree $n$. Locator: e.g. the appendix of the
  Einstein–Klein–Gordon paper [AHP2021], eqs. (111)–(113) (full-text,
  publisher excerpt).
- (F2) Antipodal parity: $Y_n\in\mathcal{H}_n\Rightarrow Y_n(-X)=(-1)^nY_n(X)$
  (restriction of an odd/even homogeneous polynomial).
- (F3) Well-posedness and finite propagation speed for (1) on the cylinder,
  for every $\delta$; unchanged principal symbol.

Every smooth solution of (1) has a convergent mode expansion
$\psi=\sum_n f_n(t)Y_n(X)$ (finished in $C^\infty$), where each $f_n$ solves
the ODE $f_n''=-\omega_n^2f_n$ with

$$\omega_n^2=(n+1)^2+\delta .\tag{2}$$

The echo map is $T\psi(t,X):=\psi(t+\pi,-X)$. For constant $\delta$ the
equation is invariant under $t\mapsto t+\pi$ and under $X\mapsto-X$
separately, hence $T$ maps solutions to solutions for **every** $\delta$;
the echo identity (E) is the stronger requirement that $T=-\,\mathrm{Id}$ on
the whole solution space. Identity (E) for all solutions is equivalent to

$$f_n(t+\pi)=(-1)^{n+1}f_n(t)\quad\text{for every }n,\ \text{every solution }f_n,\ \text{every }t.\tag{E$_n$}$$

(by (F2) and uniqueness of the mode expansion).

## 2. Theorem 1 (exact sector condition)

**Theorem 1.** Fix $n\ge0$ and $\delta\in\mathbb{R}$. The sector condition
(E$_n$) holds for all Cauchy data **iff** $\omega_n^2=(n+1)^2+\delta>0$ and
$\omega_n=(n+1)+2k$ for some $k\in\mathbb{Z}$; equivalently

$$\delta=4k(n+1+k)\ \ \text{for some }k\in\mathbb{Z}\ \text{with }(n+1)+2k>0.\tag{3}$$

*Proof.* The solution space of $f''=-\omega_n^2f$ is 2-dimensional and the
map $E_\pi\colon f\mapsto f(\cdot+\pi)$ is linear on it; (E$_n$) says
$E_\pi=(-1)^{n+1}\mathrm{Id}$.

*Case $\omega_n^2>0$.* In the phase basis $(\cos\omega_nt,\ \sin\omega_nt/\omega_n)$,
$E_\pi$ is the rotation by angle $\omega_n\pi$. A rotation is
$(-1)^{n+1}\mathrm{Id}$ iff $\omega_n\pi\equiv(n+1)\pi\pmod{2\pi}$, i.e.
$\omega_n=(n+1)+2k$, $k\in\mathbb{Z}$, with $\omega_n>0$ already
 presupposed. Squaring (2) gives (3). Conversely, if $\omega_n=(n+1)+2k$
then $\cos(\omega_n\pi)=(-1)^{n+1}$, $\sin(\omega_n\pi)=0$, and
$f(t+\pi)=(-1)^{n+1}f(t)$ for both basis solutions and hence all data.

*Case $\omega_n=0$* (i.e. $\delta=-(n+1)^2$). Solutions $f=a+bt$;
$E_\pi$ is the unipotent $\begin{psmallmatrix}1&\pi\\0&1\end{psmallmatrix}$ in
the basis $(1,t)$, which is neither $+\mathrm{Id}$ nor $-\mathrm{Id}$
($\pi\neq0$). (E$_n$) fails (already $f(t)=t$ violates it).

*Case $\omega_n^2<0$.* Write $\mu=\sqrt{-\omega_n^2}>0$; solutions
$f=ae^{\mu t}+be^{-\mu t}$, and $E_\pi=\mathrm{diag}(e^{\mu\pi},e^{-\mu\pi})$.
Equality with $(-1)^{n+1}\mathrm{Id}$ forces $e^{\mu\pi}=(-1)^{n+1}$: for
even $n$ this demands $e^{\mu\pi}=-1$, impossible; for odd $n$ it demands
$e^{\mu\pi}=e^{-\mu\pi}=1$, i.e. $\mu=0$, excluded. ∎

Examples (exact, confirmed by integer scan in `check_modes.py`):
$\delta=8$ echoes in sector $0$ only ($\omega_0=3$); $\delta=12$ in sector
$1$ ($\omega_1=4$); $\delta=20$ in sector $3$; $\delta=-8$ in sector $2$
($\omega_2=1$); $\delta=-12$ in sector $3$ ($\omega_3=2$); $\delta=-4$ in
**no** sector ($k=-1,n=1$ gives $\omega_1=0$, excluded). Positive
sector-hits have $k\ge1$, $\delta\ge8$; negative ones $k\le-1$,
$n+1>2|k|$, $\delta=-4|k|(n+1-|k|)$.

## 3. Theorem 2 (sharp all-solution classification) and witnesses

**Theorem 2.** Identity (E) holds for every smooth solution of (1) iff
$\delta=0$.

*Proof.* ($\Leftarrow$) $\delta=0$: $\omega_n=n+1=(n+1)+2\cdot0$, so
Theorem 1 applies to every $n$ (this re-derives the dispatch's mode
argument).

($\Rightarrow$) Let $\delta\neq0$. Choose $n$ with
$n+1>\max\big(|\delta|/4,\sqrt{|\delta|}\big)$; then
$\omega_n^2\ge(n+1)^2-|\delta|>0$ and

$$\big|\omega_n-(n+1)\big|=\frac{|\delta|}{\omega_n+(n+1)}\le\frac{|\delta|}{2(n+1)}<2 .$$

If (E$_n$) held, Theorem 1 would give $\omega_n=(n+1)+2k$ with
$2|k|=\big|\omega_n-(n+1)\big|<2$, so $k=0$ and $\omega_n=n+1$, forcing
$\delta=0$ — contradiction. All but finitely many $n$ satisfy the hypothesis,
so **every** $\delta\neq0$ leaves infinitely many violating sectors. ∎

**Explicit failure witnesses** (single modes, generic data; the antipodal
parity makes no contribution at $t=0$, so the violation is visible already
there):

- $\delta=1$ ("$ (\Box-2)$", unit shift): the **spatially constant** mode
  $\psi=\sin(\sqrt5\,t)$ violates (E): $\psi(0,\cdot)=0$ but
  $\psi(\pi,\cdot)=\sin(\sqrt5\pi)\neq0$. Even the homogeneous sector fails
  for generic $\delta$.
- $\delta=8$: sector $n=0$ still echoes ($\omega_0=3$) but
  $\psi=\sin(2\sqrt3\,t)\,X^1$ (degree-1 harmonic $Y_1(X)=X^1$, the first
  coordinate of $S^3\subset\mathbb{R}^4$) violates (E):
  $\sin(2\sqrt3\,\pi)\neq0$. Shows the classification is sharp
  sector-by-sector, and that sector echoes do **not** add up to a pointwise
  identity (values at an event mix all degrees).
- $\delta=-8$: sector $n=2$ echoes ($\omega_2=1$) but the exponential mode
  $\psi=e^{\sqrt7\,t}Y_0$ violates (E): $e^{\sqrt7\pi}\neq-1$.

`check_modes.py` re-derives (3) by exact integer arithmetic over a window of
$\delta$ and integrates the witness modes by RK4: echo residuals are
$\sim10^{-14}$ where Theorem 1 predicts echo and order-1 where it predicts
failure. That script is a bounded demonstration of the algebra above, not a
proof of any general statement.

## 4. What is geometry and what is field

**(4.1) Refocusing is $\delta$-independent; values are not.** The principal
symbol of (1) is $\delta$-independent, so characteristics — the null cones of
the cylinder — are the same for all $\delta$. On $\mathbb{R}\times S^3$ every
null geodesic from an event refocuses with all others at the spacetime
antipode $A(p)=(t+\pi,-p)$; this standard geometric fact is recorded, e.g.,
in [CGL2026, §1] ("spacetime antipodes"). By propagation of singularities
for (1), for every $\delta$ and every solution
$\operatorname{singsupp}\psi(t+\pi)=-\operatorname{singsupp}\psi(t)$: the
**cones and singularities echo for all $\delta$**. What Theorem 2 shows is
that the **values** echo only at $\delta=0$. In Huygens terms: the retarded
fundamental solution of (1) is supported on the cone only at the isolated
potential $c=1+((3-1)/2)^2K$ of the constant-curvature family — the
Belger–Schimming–Wünsch survey records that on odd-dimensional constant
curvature $K$ the modified wave equation $\partial_t^2+(\Delta+c)$ satisfies
Huygens' principle **only** for $c=((n-1)/2)^2K$ [BSW1997, §on constant
curvature, assertion (b)]; for the unit $S^3$, $c=1$, i.e. our $\delta=0$.
Any $\delta\neq0$ produces a tail inside the cone, and the tail is exactly
what destroys (E). The echo identity is the mode-side shadow of
tail-freedom. (Related discrete-resonance phenomenology: the de Sitter
Huygens mass values $m^2=(n^2-1)/4$ and "knot points" of [Youssef2023].)

**(4.2) In the ESU the echo is not needed for determination.** For
$b=(\eta_b,Y)$ on the full cylinder and any $c<\eta_b-\pi$, the slice of
$I^-(b)$ at time $c$ is the open ball of radius $\eta_b-c>\pi$, which is all
of $S^3$; so $I^-(b)$ contains a full Cauchy surface. Any two solutions
agreeing on $I^-(b)$ agree on that slice, hence everywhere. So
$F_{\mathcal L}(b)=M$ for the equation (1) **for every $\delta$** — and
indeed for every law with the dispatch's domain-of-dependence property. This
is the dispatch's $\mathrm{Det}(b)=M$ (its Prop.~dust, ESU case) plus its
general inclusion $\mathrm{Det}\cup J^-\subseteq F_{\mathcal L}$; the point
here is its $\delta$-independence: **geometric guarantee does not move when
the field equation changes.**

**(4.3) On the dust strip the echo was the field's entire extra
contribution.** In the closed dust strip $(0,2\pi)\times S^3$ with
$\eta_b<\pi$, $I^-(b)$ contains no Cauchy surface of the extended cylinder
(its slices are balls of radius $<\pi$), so geometry alone determines
nothing beyond $J^-(b)$ at the guaranteed level, and the dispatch's echo
proposition supplied field-level determination on $A(J^-(b))\cap M$. By
Theorem 2 the identity powering it holds only at $\delta=0$: **for every
nonzero constant potential shift the echo mechanism is gone.** Whether
$A(J^-(b))\cap M\subseteq F_{\mathcal L}(b)$ could still hold for some
$(b,\delta)$ by other means is left open; sector echoes at special $\delta$
(e.g. $\delta=8$, sector 0) do not restore it pointwise, since an event
value mixes all degrees. We did **not** prove the converse ($x\notin
J^-(b)\Rightarrow x\notin F(b)$) for any $\delta$, including $0$ — the
dispatch's exactness question stands.

## 5. Loss of the echo vs loss of all nonlocal determination

**(5.1) Symmetry survives; involution does not.** For every constant
$\delta$, $T\psi(t,X)=\psi(t+\pi,-X)$ maps solutions of (1) to solutions
(time-translation and antipodal isometry are symmetries). What fails at
$\delta\neq0$ is that $T$ acts as $-\mathrm{Id}$; $T^2$ is the $2\pi$
time shift, which is $\mathrm{Id}$ on solutions only at $\delta=0$ (all
frequencies integral). The echo is thus a resonance between the frequency
ladder $\{\omega_n\}$ and the antipodal parity, not a symmetry breakdown.

**(5.2) A $\delta$-free witness set.** Theorem 2's proof exhibits, for every
$\delta\neq0$, infinitely many degrees $n$ whose pure modes violate (E);
these give explicit solution pairs agreeing on no-set-in-particular but
failing the identity that the dispatch's determination argument consumes.

**(5.3) Integral determination survives every $\delta$.** Let $c_0(t)$ be
the spatial mean of a solution $\psi$ over $S^3$. Orthogonality of
$\mathcal{H}_0$ to $\mathcal{H}_n$, $n\ge1$, gives
$c_0''=-(1+\delta)c_0$: the mean solves a closed ODE. If $\psi$ vanishes on
$I^-(b)$, then $c_0$ vanishes on an open time interval (of length $\pi$ on
the cylinder; $(0,\eta_b)$ for the dust strip), hence $c_0\equiv0$ by ODE
uniqueness. So for **every** $\delta$: two solutions agreeing on $I^-(b)$
have equal spatial means everywhere. This is a genuine nonlocal
determination from the past — but global/integral, not pointwise, and it
does not put any specific event outside $J^-(b)$ into $F_{\mathcal L}(b)$
(non-mean modes can differ there; cf. the witnesses). It answers the task's
request to separate "loss of this particular echo identity" from "loss of
all nonlocal determination": at $\delta\neq0$ the echo dies, some
integral determination persists, and pointwise beyond-$J^-$ determination is
an open question (conjecturally none, per the localization considerations
in the working notes, but unproven here).

## 6. Ordinary mass on closed dust: a different model (kept separate)

For the massive conformally coupled scalar
$\Box_g\phi-\tfrac16R_g\phi+m^2\phi=0$ on closed dust
$g=a(\eta)^2(-d\eta^2+d\Omega_3^2)$, $a=\tfrac12a_m(1-\cos\eta)$, the
conformal transformation (same covariance identity as [Wald1984, App.~D],
cited by the dispatch) gives, for $\psi=a\phi$,

$$\psi_{\eta\eta}=\Delta\psi-v(\eta)\psi,\qquad v(\eta)=1+m^2a(\eta)^2,\tag{4}$$

a **time-dependent** potential — not the constant $1+\delta$ of (1).
Moreover $a(\eta+\pi)=\tfrac12a_m(1+\cos\eta)\neq a(\eta)$, so $v$ is
$2\pi$- but not $\pi$-periodic.

**Lemma.** For $\psi_{tt}=\Delta\psi-v(t)\psi$ with smooth $v$, the solution
space is invariant under $T\psi(t,X)=\psi(t+\pi,-X)$ iff
$v(t+\pi)=v(t)$ for all $t$.

*Proof.* Direct computation:
$L_t(T\psi)(t,X)=[v(t)-v(t+\pi)]\,\psi(t+\pi,-X)$, where
$L_t=\partial_t^2-\Delta+v(t)$. Cauchy data at the slice $t+\pi$ are
unrestricted, so $L_t(T\psi)\equiv0$ for all solutions iff the coefficient
vanishes pointwise. ∎

Hence for $m\neq0$ on closed dust, $T$ is not even a symmetry of (4): there
are solutions whose echo translate is not a solution, and (E) fails a
fortiori. (Even the doubled, $2\pi$ echo $\psi(\eta+2\pi,X)=\psi(\eta,X)$
for all solutions is a Floquet condition that should fail generically for
$m\neq0$; we did not verify this and make no claim.) **No physical
dust-mass result follows from the ESU constant-$\delta$ analysis**; the two
models share only the conformal frame, and the robustness conclusions differ
in kind: constant shifts kill the value echo while preserving the equation
symmetry; the dust mass breaks the symmetry itself.

## 7. Answer to the framing question

The interesting claim — determination of an antipodal echo of one's past by
a field, before the geometric threshold — is a **special conformal
recurrence**, not a stable consequence of causal geometry. Causal geometry
stably gives: (i) cone/singularity refocusing (all $\delta$), (ii) complete
determination from the past once slices are swallowed (ESU and post-threshold
dust, all $\delta$, indeed all domain-of-dependence laws). The value echo on
the pre-threshold strip is carried by exactly one member of the
constant-potential family, $\delta=0$, in agreement with the Huygens
rigidity recorded in the prior literature: the massless conformal scalar is
the isolated tail-free (Huygens) equation of its family on constant
curvature.

## 8. Scope, prior work, and limits

- **What is proved here:** Theorems 1–2 and the Lemma of §6, with complete
  elementary proofs; the witnesses of §3; the $\delta$-independence claims
  of §4.2 and §5.3. All are short mode-algebra arguments using classical
  facts (F1)–(F3).
- **What is not claimed:** novelty of the algebra (frequency-ladder/parity
  arguments are standard; the Huygens literature anticipates the isolation
  of $\delta=0$ in a stronger, operator-theoretic form); exactness of
  $F_{\mathcal L}(b)$ for any $\delta$; any statement about our universe,
  about realistic matter, or about temporal ontology; anything global about
  Huygens theory beyond the cited survey's recorded results.
- **Search capability check:** the task-assigned Z.ai `web-search-prime`
  tool returned HTTP 429 / code 1310 "Weekly/Monthly Limit Exhausted"
  (resets 2026-11-17) on first use; it was **not** available. The standard
  OpenCode web search and direct public fetches were used instead. Coverage
  is accordingly narrower: no systematic citation-chasing beyond the leads
  below was performed, and quota was not retried in loops.
- **Prior work read (depths honest, details in `sources.jsonl`):**
  dispatch `main.tex` + `SOURCE.md` (frozen snapshot; full-text);
  `REVIEW.md` and `DRAFT3_FOLLOWUP.md` (full-text leads); Belger–Schimming–
  Wünsch survey (selected sections via publisher excerpt — the
  constant-curvature Huygens classification used above); Günther's
  monograph (bibliographic discovery only; scan TOC); Berest–Veselov
  (abstract); Youssef, de Sitter Huygens (abstract + selected §3);
  conformal-boundary-rigidity preprint for the spacetime-antipode refocusing
  statement (abstract + selected §1); Einstein–Klein–Gordon ESU mode
  structure (selected sections incl. harmonics appendix); tails context
  (EPJC 2017, abstract). Geroch 1977, Grøn–Johannesen 2011 and Manchak 2008
  were taken from the coordinator review's audit, not re-read here.
- **Open questions:** (a) exact $F_{\mathcal L}(b)$ on the dust strip for
  $\delta=0$ and for each $\delta\neq0$ (the dispatch's question, now
  parameterized); (b) whether the $\pi$-shifted echo fails for the
  time-dependent dust-mass potential in the stronger sense that *no*
  all-solutions affine echo $A(J^-(b))\subseteq F(b)$ exists for $m\neq0$;
  (c) Floquet genericity of the $2\pi$-recurrence failure in (4); (d) an
  independent check of the BSW survey's constant-curvature statement against
  Günther's monograph (we relied on the survey excerpt).

## Files

- `RESULT.md` — this document.
- `sources.jsonl` — source register with depths and limits.
- `check_modes.py` — bounded stdlib verification (integer sector scan; RK4
  echo residuals). Run: `python3 check_modes.py`.
