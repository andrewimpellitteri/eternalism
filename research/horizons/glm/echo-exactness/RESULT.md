# Echo exactness: the fixed region of the conformal scalar on closed dust

Task `horizons-echo-exactness`. Frozen inputs:
`research/horizons/coordinator-review/dispatch-2026-10-25/main.tex` (draft 3,
SHA-256 `bbd59269…`) and `SOURCE.md`; leads: `coordinator-review/REVIEW.md`,
`coordinator-review/DRAFT3_FOLLOWUP.md`. All arguments below were
independently reconstructed for this task; the review documents were used as
pointers, not as certificates.

## 0. The question

Let $M=(0,2\pi)\times S^3$ with the closed dust metric
$g=a(\eta)^2(-d\eta^2+d\Omega_3^2)$, $a=\tfrac12 a_m(1-\cos\eta)$, and let
$\mathcal L$ be the smooth solutions on $M$ of the conformally coupled scalar
equation $\Box_g\phi-\tfrac16R\phi=0$. For $b=(\tau,Y)\in M$ with
$0<\tau\le\pi$, write $I^-_s(b)$ for the strict chronological past and, as in
the draft, $F_{\mathcal L}(b)=\{x:\text{any two solutions agreeing on }I^-_s(b)
\text{ agree at }x\}$. Draft 3, Proposition (echo), proves
$J^-(b)\cup(A(J^-(b))\cap M)\subseteq F_{\mathcal L}(b)$ with
$A(\eta,X)=(\eta+\pi,-X)$, and leaves open whether this is an equality. It is
not: the true fixed region is strictly larger, and we compute it exactly.

Write, for $x=(\eta,Z)\in M$, $d=d_{S^3}(Z,Y)$ and
$$u(x)=\eta+d,\qquad v(x)=\eta-d$$
(the two optical coordinates of the observer line $\{\eta\}\times\{Y\}$; note
$u\le\tau$ iff $x\in J^-(b)$, and $v\le\tau$ iff $x\in J^-(\hat b)$ where
$\hat b=A(b)=(\tau+\pi,-Y)$).

## 1. Result

**Theorem.** For every $b=(\tau,Y)\in M$ with $0<\tau\le\pi$,
$$F_{\mathcal L}(b)\;=\;M\cap\Big(\{u\le\tau\}\cup\{v\le\tau\}\cup
\{v\ge 2\pi-\tau\}\cup\{u\ge 2\pi-\tau\}\Big).$$
Equivalently, the unfixed region is the open "causal annulus"
$$M\setminus F_{\mathcal L}(b)=\{x\in M:\tau<u(x)<2\pi-\tau,\ \tau<v(x)<2\pi-\tau\},$$
which is nonempty if and only if $\tau<\pi$. In particular:

1. **The draft's conjectured exactness is false.** For $\tau<\pi$ the point
   $x_W=(2\pi-\tau/2,\,Y)$ satisfies $v=2\pi-\tau/2>\,2\pi-\tau$, so
   $x_W\in F_{\mathcal L}(b)$, while $u=v=2\pi-\tau/2>\tau$ excludes it from
   $J^-(b)\cup(J^-(\hat b)\cap M)$. The draft's under-propagation is real: its
   inclusion is strict for every $\tau<\pi$.
2. **Critical epoch $\tau=\pi$.** $F_{\mathcal L}(b)=M$: every pair of
   solutions agreeing on $I^-_s(b)$ agrees on all of $M$ (values and, since
   derivatives of solutions are solutions, all jets). At the same epoch
   $\mathrm{Det}(b)=I^-_s(b)$ (draft, Prop. dust, strict): *everything* is
   law-fixed at maximum expansion while *nothing beyond the strict past* is
   geometrically guaranteed. The coordinator's suggestion is realized: at
   $\tau=\pi$ continuity-in-the-solution-class (via the mechanisms below)
   determines all smooth data although the geometric guarantee stays minimal.
3. **Timelike-future targets are fixed before $\pi$.** For every
   $\eta_x\in(2\pi-\tau,\,2\pi)$ the event $x=(\eta_x,Y)$ is timelike future
   of $b$ (as $0=\eta_x-\tau<d$ is false, i.e. $d=0<\eta_x-\tau$), lies
   outside $\mathrm{Det}(b)$ (strict for $\tau\le\pi$), and is fixed:
   $u(x)=\eta_x\ge 2\pi-\tau$. This answers DRAFT3_FOLLOWUP's request: field
   determination before maximum extension does reach genuinely future events;
   the pre-threshold echo points are not the whole story.
4. **Explicit epoch-dependent determination witness.** Same spacetime, same
   law, same target $x^*=(3\pi/2,Y)$: from $b_1=(2\pi/5,Y)$,
   $u=v=3\pi/2\in(\tau_1,\,2\pi-\tau_1)$, so $x^*\notin F_{\mathcal L}(b_1)$
   (an explicit separating pair is constructed below and realized
   numerically); from $b_2=(3\pi/4,Y)$, $3\pi/2\ge 2\pi-\tau_2=5\pi/4$, so
   $x^*\in F_{\mathcal L}(b_2)$. Both standpoints precede $x^*$ in time and
   both have $\mathrm{Det}(b_i)=I^-_s(b_i)$. Law-relative determination of one
   and the same future event therefore switches with the observer's epoch
   while the geometric guarantee does not move: the witness DRAFT3_FOLLOWUP
   asked for, as an explicit construction rather than an inference from
   $\mathrm{Det}$.

All statements concern value-fixing under the *smooth solution class of the
single scalar law* on this $M$; no claim is made about other fields, other
topologies, quantization, observation, or our universe.

## 2. Proof

### 2.1 Reduction to the Einstein cylinder

$\psi:=a\phi$ satisfies the fixed equation on the Einstein cylinder
$E=\mathbb R\times S^3$,
$$(\partial_\eta^2-\Delta_{S^3}+1)\,\psi=0,$$
i.e. degree-$n$ spherical harmonics (eigenvalue $-n(n+2)$) oscillate with
frequency $n+1$. Standard well-posedness from any interior slice
$\{\eta_1\}$ gives:

* **(E1) Extension.** Every smooth solution on $M$ extends uniquely to a
  smooth solution on $E$; conversely restrictions of smooth solutions on $E$
  exhaust $\mathcal L$. (The big-band slices carry no boundary condition; the
  class is exactly the unrestricted smooth solution class.)
* **(E2) Periodicity and echo.** Integer frequencies imply
  $\psi(\eta+2\pi,X)=\psi(\eta,X)$; and with $Y_n(-X)=(-1)^nY_n(X)$,
  $\psi(\eta+\pi,-X)=(-1)^{n+1}(-1)^n\psi(\eta,X)=-\psi(\eta,X)$. Hence
  $\psi\circ A=-\psi$ and $\psi\circ A^2=\psi$ for every solution. This is
  the draft's echo identity; we only use it, and its consequence
  $\psi|_{I^-_s(b)}=0\Rightarrow\psi|_{A(I^-_s(b))}=0$.

Cylindrical coordinates: null geodesics from $p=(\eta_1,P)$ refocus at
$A$-images; the light cone of $p$ in $E$ is
$C(p)=\{(\eta,X):\ \mathrm{fold}(|\eta-\eta_1|)=d_{S^3}(X,P)\}$, where
$\mathrm{fold}(t):=\arccos(\cos t)\in[0,\pi]$.

### 2.2 Trace lemma (Huygens/refocusing form of the Cauchy propagator)

**Lemma.** Let $\psi$ have Cauchy data $(f,g)=(\psi,\partial_\eta\psi)|_{\eta_
=\eta_1}$. Then for $\eta\ne\eta_1\ (\mathrm{mod}\ 2\pi)$, with
$\rho=\mathrm{fold}(|\eta-\eta_1|)\in(0,\pi)$ and
$\varepsilon=+1$ if $|\eta-\eta_1|<\pi$, $\varepsilon=-1$ otherwise,
$$\psi(\eta,X)=\frac{\varepsilon}{4\pi\sin\rho}\int_{\partial B(X,\rho)}
g\,d\sigma\;-\;\frac{1}{4\pi}\,\partial_t\Big|_{t=\rho'}\!\Big(\frac{1}{\sin t}
\int_{\partial B(X,t)} f\,d\sigma\Big)\cdot(\text{branch}),$$
where the $f$-term is the corresponding derivative-combination on the same
sphere. In particular:

* **(T1) Support.** If $\partial B(X,\rho)\cap\operatorname{supp}(g\ \text{and
  }f)=\emptyset$, then $\psi(\eta,X)=0$.
* **(T2) Nonvanishing.** If $f=0$ and $g\ge0$ is continuous, not identically
  $0$, with $P\in\partial B(X,\rho)\cap\operatorname{supp}g$ at which
  $g>0$, then $\psi(\eta,X)\ne0$ (the trace is the shell integral with
  strictly positive density $1/(4\pi\sin\rho)$ on the direct branch).

*Proof.* Mode expansion: $K_n(X,\cdot)=\tfrac{n+1}{2\pi^2}C_n^1(\cos
d(X,\cdot))$ is the reproducing kernel of degree $n$
($C_n^1(\cos d)=\sin((n+1)d)/\sin d$), and
$$\frac{\sin(t\Lambda)}{\Lambda}\delta_X
=\sum_n\frac{\sin((n+1)t)}{n+1}K_n(X,\cdot)
=\frac{1}{2\pi^2}\sum_{k\ge1}\sin(kt)\,C_{k-1}^1(\cos d(X,\cdot))
=\frac{1}{2\pi^2\sin d}\sum_{k\ge1}\sin(kt)\sin(kd),$$
with $d=d(X,\cdot)$. The distributional identity
$\sum_{k\ge1}\sin(kt)\sin(kd)=\tfrac{\pi}{2}\sum_{j\in\mathbb Z}
[\delta_{2\pi}(d-t-2\pi j)-\delta_{2\pi}(d+t-2\pi j)]$ exhibits the kernel as
a shell measure: pairing with $g$ and using co-areas
($G_g(d):=\int_{\partial B(X,d)}g\,d\sigma$, $\frac{G_g}{\sin t}$ smooth with
vanishing endpoints) gives $\psi=\frac{G_g(\rho)}{4\pi\sin\rho}$ with the
branch sign $\varepsilon$; the $f$-part is
$-\tfrac{1}{4\pi}\partial_t(G_f(t)/\sin t)$ at the same hit, from
$\cos(t\Lambda)\delta_X=-\tfrac{1}{2\pi^2\sin d}\sum_k k\cos(kt)\sin(kd)$ and
$\sum_k k\cos(kt)\sin(kd)=-\partial_t\sum_k\sin(kt)\sin(kd)$. Note the sign
$\varepsilon=-1$ on the reflected branch $t\in(\pi,2\pi)$: $\psi\circ A=-\psi$
in kernel form. (Nonzero constants were verified to machine precision:
`verify_echo_exactness.py` check 2, where the same mode sums match the exact
closed forms for Poisson data, $g$- and $f$-parts and the pole value
$\psi(t,P)=\sin t/D(t)$, at $\le1.1\times10^{-14}$.) $\square$

This lemma is the engine of both directions: fixed points are those where
*every* admissible shell misses, unfixed points are those a shell can be
made to hit while avoiding the constraint region.

### 2.3 Lower bound: the four regions are fixed

Let $\psi\in\mathcal L$ with $\psi|_U=0$, $U=I^-_s(b)$. By (E1) work on $E$
with the unique extension (still $\psi$, vanishing on $U$).

(i) $u\le\tau$ (i.e. $\overline U=J^-(b)$): continuity of $\psi$.
(ii) $v\le\tau$ ($=J^-(\hat b)\cap M$): by (E2) $\psi$ vanishes on the open
set $A(U)$, hence on $\overline{A(U)}=A(\overline U)=J^-(\hat b)$.
(iii) $v\ge2\pi-\tau$: by (E2)+periodicity $\psi$ vanishes on
$U+2\pi=\{(2\pi+s,Z):0<s<\tau,\ d(Z,Y)<\tau-s\}$. For $x\in M$ with
$v(x)>2\pi-\tau$ choose $s\in(0,\tau)$ with $v(x)>2\pi-\tau+2s$ and consider
the spacelike disk $\Sigma_s=\{2\pi+s\}\times B(Y,\tau-s)\subseteq U+2\pi$.
Every future-inextendible causal curve from $x$ crosses the slice $\{2\pi+s\}
$ inside $\overline B(X_x,\,2\pi+s-\eta_x)$, and
$d(X_x,Y)+2\pi+s-\eta_x<\tau-s$ is exactly $v(x)>2\pi-\tau+2s$; so the closed
cone-ball lies in the open disk: $x\in D^+(\Sigma_s)$. Since $\psi$ vanishes
on the open set $U+2\pi\supseteq\Sigma_s$, the data $(\psi,\partial_\eta\psi)
$ vanish on $\Sigma_s$, and uniqueness of the Cauchy problem on the
development of a spacelike disk (standard energy argument; no analyticity
used) gives $\psi(x)=0$. Points with $v=2\pi-\tau$ are added because
$F_{\mathcal L}(b)=\bigcap_{\psi\in\mathcal N}\psi^{-1}(0)$ is closed
($\mathcal N=\{\psi:\psi|_U=0\}$).
(iv) $u\ge2\pi-\tau$: identical, using the disks
$\{\pi+s\}\times B(-Y,\tau-s)\subseteq A(U)$ on which $\psi$ vanishes by
(ii); the cone containment condition reads $u(x)>2\pi-\tau+2s$.

(Note (iii) and (iv) are echo images of each other, as they must be since
$F_{\mathcal L}(b)=A(F_{\mathcal L}(b))$.)

### 2.4 Upper bound: separating solutions on the annulus

Let $x=(\eta_x,X_x)\in M$ with $\tau<u,v<2\pi-\tau$; write
$d_x=d(X_x,Y)$, $e=\mathrm{fold}(\eta_x)$. We construct $\psi\in\mathcal N$
with $\psi(x)>0$; then $(\psi,0)$ separates. Take data at slice
$\eta_1=-\psi_0\le0$ (a slice before the bang; admissible by (E1)) with
$f=0$ and $g\ge0$ a smooth bump supported in the cap $\bar B(P,\sigma)$,
$g(P)>0$, where $\sigma$ and the vertex are chosen as follows.

*Case $\eta_x\le\pi$.* Pick a margin $m>0$ with $m<\min(u-\tau,\ v-\tau,\
2\pi-\tau-u,\ \pi-\tau)$ (positive since $x$ is in the open annulus), then
$\psi_0>0$ so small that $\psi_0<\min(\pi-\tau-m,\ \pi-\eta_x,\ m)$ and
$2\psi_0<2\pi-\tau-m-u$; possible since $v<2\pi-\tau$ and $u<2\pi-\tau$ give
nonempty windows (compatibility of the two $\psi_0$-bounds is exactly
$u+v=2\eta_x\le2\pi$). Set
$$c:=\text{any value in }\big[\max(\psi_0+\tau+m,\ |d_x-\xi|),
\ \min(\pi,\ d_x+\xi,\ 2\pi-d_x-\xi-m)\big],\qquad \xi:=\eta_x+\psi_0.$$
The interval is nonempty: the lower bounds are $\psi_0+\tau+m\le d_x+\xi
\Leftrightarrow v\ge\tau+m$ ✓, and $\psi_0+\tau+m\le2\pi-d_x-\xi-m
\Leftrightarrow2\psi_0\le2\pi-\tau-2m-u$ ✓ by choice of $\psi_0$; the upper
bounds are positive for the same reason and $c\ge|d_x-\xi|$ holds by the
second chosen $\psi_0$-bound ($\psi_0\ge(v-\tau-m)/2$; take $\psi_0$ at the
midpoint of its window). Since $|d_x-c|\le\xi\le\min(c+d_x,2\pi-c-d_x)$,
some $P\in S^3$ has $d(P,Y)=c$, $d(P,X_x)=\xi$.

Avoidance: for $(\eta,Z)\in U$ the shell radius is
$\rho(\eta)=\mathrm{fold}(|\eta-\eta_1|)=\eta+\psi_0\le\pi$ (direct branch)
and $d(Z,P)\ge c-d(Z,Y)>c-\tau+\eta=\rho(\eta)+m$, so
$\partial B(Z,\rho)\cap\bar B(P,\sigma)=\emptyset$ as $\sigma<m$: by (T1)
$\psi|_U=0$. (Uniform margin; the growing refocused cone tracks the
shrinking ball exactly, which is why the bang epochs are the binding
constraints.) Hitting: $x$ lies on the cone, $\rho(\eta_x)=\xi$, and the
shell $\partial B(X_x,\xi)$ passes through $P$; by (T2) $\psi(x)>0$.

*Case $\eta_x=\pi$.* The same construction works with
$\psi_0=(\pi-d_x-\tau)/2$ (which the annulus hypothesis $\tau<u,v$ makes
positive when $d_x<\pi-\tau$); the two time-circle triangles close with
slack $2d_x$, and with $d_x=0$ the forced choice $c=\xi$ is still
non-tangent in the avoidance margin ($m=c-\psi_0-\tau>0$).

*Case $\eta_x>\pi$.* Reflect: apply the construction of the first case to
$\rho(x):=(2\pi-\eta_x,X_x)$, which is again in the open annulus
(the annulus is invariant under $\eta\mapsto2\pi-\eta$), and pull the
solution back by the isometric time-reversal $(\eta,Z)\mapsto(2\pi-\eta,Z)$,
under which the equation, the class $\mathcal L$, and $U$ (now based at the
closing bang copy $(2\pi-\tau,Y)$, the reflection of $b$) are preserved.
Equivalently use vertices $\eta_1=2\pi-\psi_0$ near the closing bang.

This proves $M\setminus F_{\mathcal L}(b)\subseteq$ the open annulus; with
§2.3 (and closedness of $F$ for the boundary strata) the theorem follows. $\square$

**Why earlier attempts stall.** Any single-vertex bump that hits $x$ needs
time-circle distances $(\psi_0,\xi,e)$ to be circularly consistent and the
spatial triangle $(c,\xi;d_x)$ to close, with the avoidance constraint
$|c-\psi_0|\ge\tau$; summing the two triangle inequalities gives
$\tau\le|c-\psi_0|\le d_x+e$, i.e. $u=\eta_x+d_x\ge\tau$ — the annulus
condition is *exactly* the boundary of feasibility of the method, and the
four fixed regions are exactly where every admissible cone is blocked
(annulus complement) or where the constraint region itself is hit. This is
also why naive constructions with vertices inside $(0,\tau)$ work only for
$\tau\le\pi/2$ (they then graze $A(U)$'s antipodal refocus), and why
vertices must be taken just outside the bang slices for $\tau>\pi/2$.

## 3. What the numerics verify (and what they cannot)

`verify_echo_exactness.py` (stdlib only; output in `verify_output.txt`):

1. Echo identity $\psi(t+\pi,\pi-d)=-\psi(t,d)$: residual $2.7\times10^{-15}$
   (mode-wise exact; a check of the mode machine, not new mathematics).
2. Mode sums vs. exact closed forms for Poisson data (both $f$- and $g$-parts,
   all branches, plus pole value): $\le1.1\times10^{-14}$. This verifies the
   trace lemma's kernel structure (shell support, refocusing, branch sign) in
   the regime where a closed form exists.
3. Separation witness: for $b_1=(2\pi/5,Y)$ and the annulus target
   $x_0=(\tau+0.9,Y)$ (timelike future of $b_1$), the constructed admissible
   bump (support radius $0.15<$ margin $0.42$) gives
   $|\psi|\le2.4\times10^{-3}$ on sampled $U$-points vs.
   $\psi(x_0)=+0.650$, and $\psi(x_W)=4.3\times10^{-4}$ at
   $x_W=(2\pi-\tfrac12,Y)$ — a point outside $J^-(b_1)\cup J^-(\hat b)$
   where the theorem forces vanishing.
4. b2-control: the $b_2=(3\pi/4,Y)$-admissible solution gives
   $\psi(x')=+3.99$ at its own annulus target but $\psi(x^*)=1.3\times10^{-3}$
   at $x^*=(3\pi/2,Y)$, which the theorem places in $F_{\mathcal L}(b_2)$.
5. Geometry: the four-region membership of all witness points; $\tau=\pi$
   covers a $40\times40$ grid with no point outside the union; the annulus
   contains 288/1560 grid points at $\tau=2\pi/5$.

Limits: the projections use $n\le1500$ modes, so "vanishing" values are
truncation/Gibbs-limited ($10^{-3}$–$10^{-4}$), not exact zeros; the checks
corroborate the analytic lemma and constructions on their bounded domain and
are not proofs of the global theorem. The theorem's proof in §2 is analytic
and complete on its stated scope.

## 4. Scope, and what remains open

* **Class-dependence.** Everything is for $\mathcal L$ = smooth solutions of
  the one conformal scalar. The draft's residual question — whether *some*
  local law with domain-of-dependence fixes no more than
  $\mathrm{Det}(b)\cup J^-(b)$ in the closed models — is untouched (REVIEW's
  flow-law counterexample shows the intersection over laws can jump outside
  any single $F_{\mathcal L}$). Our result sharpens the *upper* side of that
  question: in the closed dust model even the *lower* envelope over "natural
  geometric fields" can be much larger than the geometric guarantee.
* **Interpretive guards.** "Fixed" = solution-agreement (informational,
  nomological, given $M$), not Belnap settledness, not epistemic prediction
  (Manchak), not ontological fixation of the future, and not a claim about
  realistic cosmology (deterministic classical scalar on a recollapsing
  closed universe). The $\tau=\pi$ "everything fixed" statement is about the
  idealized model's solution class.
* **Jets vs values.** The theorem fixes values; since $\partial_{\eta}\psi$
  and spatial derivatives of solutions are again solutions, all first (hence
  all) jets at points of $F_{\mathcal L}(b)$ are fixed as well. What is *not*
  fixed outside the development of a data region is the restriction of
  solutions to slices as Cauchy data — the fixed-region statement and a
  full-Cauchy-data statement must not be conflated (REVIEW's warning,
  honored here by construction: the constraint region is the open
  $I^-_s(b)$, and only pointwise consequences at $F$-points are claimed).
* **Open.** (a) The exact $F_{\mathcal L}$ for the *other* standard models
  (closed radiation, de Sitter, antipodal-quotient variants) — the same
  machinery applies wherever the solution class has an exact finite-order
  echo; closed radiation has frequency $\sqrt{n(n+2)}$ (non-integer, no
  periodization), so new behavior is expected. (b) The minimal
  $\bigcap_\mathcal L$ over a natural field menu. (c) Whether some local law
  attains the geometric bound in the closed models. (d) A Lean formalization
  of the trace lemma's distributional core is possible but was out of scope
  here (no builds/installs permitted for this task).

## 5. Source notes (details in `sources.jsonl`)

Primary mathematics done here is self-contained (mode sums + elementary
spherical geometry + standard Cauchy uniqueness). External checks made:
draft 3 (frozen) read full-text; REVIEW.md and DRAFT3_FOLLOWUP.md read
full-text as leads; Nolan arXiv:gr-qc/9703031v1 (CQG 14 (1997) 1295–1308)
read at abstract level — confirms Green-function structure
$\Sigma\delta(\Omega)+V\Theta(-\Omega)$ language and that minimal scalars in
cosmological spacetimes tail, consistent with our use of the conformal
coupling; the classical Huygens classification program (Carminati–McLenaghan
IHP series; Wünsch; Günther; Friedlander) located at discovery/bibliographic
level: conformally invariant scalar wave equations satisfy Huygens' principle
on (locally) conformally flat spacetimes, matching our trace lemma on the
conformally flat cylinder. Draft's other citations (Wald App. D; HE; Geroch
1977; MS2008; Grøn–Johannesen; Bolotin–Tanatarov; Manchak) were taken over
from the draft and coordinator review with their stated depths, not
re-verified here except where used above.
