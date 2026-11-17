# How much error can a growing past record tolerate?

*Coordinator follow-up, 17 November 2026. Internally checked derivation from a published energy estimate. Independent review and priority assessment remain open.*

The [exact-record argument](finite-records-and-possible-futures.md) leaves open what happens when even the field values we possess can be wrong. In the same free massive model, fix a nonzero future spatial average and an energy budget. There is an exact threshold for uniform recovery from noisy field values over successively longer past cones. It depends on how the total error grows with the duration of the record.

## The observation model and verdict

Let $w$ be a real solution of $(\partial_t^2-\Delta+m^2)w=0$ on all of $\mathbb R^{1+d}$, $m>0$, $d\ge1$, with conserved energy $E(w)\le B$ for a fixed $0<B<\infty$. Here $2E(w)=\int(|w_t|^2+|\nabla w|^2+m^2|w|^2)\,dx$. This can be the difference from a known reference history. Fix a nonzero real $g\in C_c^\infty(\mathbb R^d)$ and the future reading $F(w)=\int g(x)w(1,x)\,dx$.

For each $T>0$ the available datum is $y=w+n$ on $P_T=\{(t,x):-T<t<0,\ |x|<-t\}$. Only field values are observed. The additive error $n$ is arbitrary with spacetime norm $\|n\|_{L^2(P_T)}\le D(T)$. Uniform recovery means there are estimators $A_T$ for which the supremum of $|A_T(y)-F(w)|$ over these fields and errors tends to zero. Each duration defines one experiment. There is no probabilistic or independence assumption.

**Theorem.** Uniform recovery holds if and only if $D(T)/\sqrt T\to0$. In particular, a fixed total error budget is tolerable. A fixed positive allowance for root-mean-square spatial $L^2$ error per unit time permits a persistent ambiguity. The normalization averages over time only. Spatial errors are integrated over each whole cone section, without dividing by its volume.

## Recovery using a known test field

Solve the same free equation for $z$ with $z(1)=0$ and $z_t(1)=g$. Conservation gives $\|z_t(t)\|_2\le\|g\|_2$ and $\|z(t)\|_2\le\|g\|_2/m$. For every time $t$ the conserved pairing
$\langle w,z_t\rangle-\langle w_t,z\rangle$ equals $F(w)$ by its value at time one. Its derivative vanishes by the equations and spatial integration by parts. Smooth data give the calculation directly, and energy-norm continuity extends it to energy data.

Fix a nonnegative smooth $a$ compactly supported in $(1/2,1)$ with integral one. Let $\chi_T(t)=T^{-1}a(-t/T)$ and $K_T=2\chi_T z_t+\chi_T' z$. Averaging the pairing with $\chi_T$ and integrating the term containing $w_t$ by parts in time gives the exact identity

$$
F(w)=\int_{\mathbb R^{1+d}} K_T(t,x)w(t,x)\,dt\,dx .
$$

In particular the derivative in $K_T$ acts only on known quantities. Use $A_T(y)=\int_{P_T}K_T y$. Its noise amplification in the stated norm is bounded by
$$
\|K_T\|_{L^2(P_T)}\le
\frac{\|g\|_2}{\sqrt T}
\left(2\|a\|_2+\frac{\|a'\|_2}{mT}\right),
$$
by the slice bounds and the rescaling of $\chi_T$. The estimator needs only the older half of the record, throughout its expanding spatial sections.

The omitted exterior can be bounded from quantities depending only on $g,m,T$. Write
$$
H_T=\sup_{-T\le t\le -T/2}
\left(\int_{|x|\ge |t|}(|z_t(t,x)|^2+m^2|z(t,x)|^2)\,dx\right)^{1/2}.
$$
Yang's exterior-energy estimate applied to the finite-energy data of $z$ at time zero gives $H_T\to0$. The change $(t,x)\mapsto(mt,mx)$ reduces a positive mass to unit mass. Since $\|w(t)\|_2\le\sqrt{2B}/m$, spatial Cauchy–Schwarz followed by time integration gives
$$
|A_T(y)-F(w)|\le
\frac{\|g\|_2 D(T)}{\sqrt T}
\left(2\|a\|_2+\frac{\|a'\|_2}{mT}\right)
+\frac{\sqrt{2B}}m
\left(2\|a\|_1+\frac{\|a'\|_1}{mT}\right)H_T .
$$
This proves sufficiency, uniformly over the stated ball. No decay rate for $H_T$ is assumed. The exterior estimate was checked in the primary text at Remark 1.10, immediately after equation (1.32). The estimator and its bound are deductions here. [Yang, arXiv:2309.15282v1](https://arxiv.org/html/2309.15282v1#S1.SS2)

## Why the threshold is necessary

If $D(T)/\sqrt T$ fails to tend to zero, it is at least some $c>0$ along a sequence $T_j\to\infty$. Choose a single free solution $v$ with $v(1)=g$, $v_t(1)=0$. Then $F(v)=\|g\|_2^2>0$. Take $\lambda>0$ small enough that $E(\lambda v)\le B$ and $\lambda\sqrt{2E(v)}/m\le c$. Integration of the spatial energy bound yields
$$
\|\lambda v\|_{L^2(P_{T_j})}
\le \lambda\sqrt{2E(v)}\,\sqrt{T_j}/m\le D(T_j).
$$
At each of those durations the zero record is compatible with zero field and zero error, or with field $\lambda v$ and error $-\lambda v$ on the observed region. Their target readings differ by the same positive number $\lambda\|g\|_2^2$. Any estimator must err by at least half that difference on one case. This proves necessity even if nonlinear estimators are allowed.

## Which philosophical inference survives?

In this model the uncertainty that remains for a bounded observer can have two different explanations. Under fixed total noise and an energy bound, sufficiently extensive records determine a chosen later average to any specified accuracy. Under the second error allowance, a disturbance can stay within the error budget at every duration and conceal a fixed change in that average. The equations, field class, and target are identical in both comparisons. An inability to infer tomorrow's reading can therefore arise entirely from what counts as observational agreement. To use it as evidence of an objectively unsettled future one must independently exclude that explanation.

The result concerns a continuum of measurements over an expanding spatial region, adversarial errors, and one fixed spatial average. A single observer's instrument, point sampling, noise specified per unit spacetime volume, or a changed source defines a different problem. A useful check on the mass assumption is the massless equation in one space dimension. For a nonnegative profile concentrated near the origin and a suitable smooth bump $h$ supported near $1$, the finite-energy free wave $h(t+x)$ vanishes on the whole past cone while its time-one average is positive. Even perfect records then leave a fixed discrepancy. The [earlier noisy-record diagnostic](noisy-record-control/RESULT.md) addresses point readings on a different spacetime.

## How wide must the record be?

Duration alone can give a misleading picture of observational access. Keep $B>0$, the same compactly supported nonzero $g$, and a **fixed** total error allowance $D>0$. Replace each past spatial section at $t=-s$ by the ball $|x|<R(s)$ with a measurable radius $0\le R(s)\le s$. There are two different outcomes.

- **Asymptotically full width.** If $R(s)/s\to1$, the same estimator restricted to the observed balls recovers $F$ uniformly. This allows the missing outer shell to grow without bound, for example with thickness $\sqrt{s}$ for $s\ge1$.
- **A fixed fractional deficit.** If $R(s)\le\beta s$ eventually for some $0<\beta<1$, no estimator recovers $F$ uniformly. Even the entire infinite past record on these balls admits two fields giving precisely the same noisy data and different future readings. Their separation can depend on $\beta,g,B,D$ and may be very small.

*Proof of recovery.* Only the estimate of the omitted exterior changes. For any $0<c<1$, eventually $R(s)\ge cs$. By Yang's (1.32) with $r_0=0$, $r_1=c$, and conservation, the limiting energy of $z$ outside $|x|<cs$ is the energy in frequencies of group speed at least $c$. The boundaries have zero measure for energy data. For positive mass the group speed $|k|/\sqrt{m^2+|k|^2}$ is strictly below one at every finite frequency, so that spectral tail tends to zero as $c\uparrow1$. This bounds the limsup of the energy omitted by the actual balls by zero. The supremum on $T/2\le s\le T$ therefore tends to zero as well. The preceding noise bound applies without change. [Yang, Remark 1.10, equation (1.32)](https://arxiv.org/html/2309.15282v1#S1.SS2)

*Proof of failure.* A smooth compactly supported nonzero $g$ has a real-analytic Fourier transform that cannot vanish on the entire open set of group speeds greater than $\beta$. Choose a real, nonnegative, even smooth frequency cutoff $b$ compactly supported in that set with $\int b|\widehat g|^2>0$. Let $v$ have time-one displacement with Fourier transform $b\widehat g$ and zero time-one velocity. The field is real, smooth and of finite energy. Plancherel gives $F(v)>0$.

On the observed cone at large $s$, both Fourier phases $x\cdot k\pm(t-1)\sqrt{m^2+|k|^2}$ are nonstationary on the packet's frequency support. Indeed $|x|/|t-1|\le\beta$ there while that compact support has minimum group speed strictly greater than $\beta$. Divide the phase by $|t-1|$. Its gradient stays uniformly away from zero and all its higher derivatives stay bounded on the support. Repeated integration by parts in $k$ against the smooth compact amplitude gives $|v(-s,x)|\le C_N(1+s)^{-N}$ there for every $N$. Since the observed slice has volume $O(s^d)$, choosing $2N>d+1$ makes the squared field integrable over the entire observed past. Bounded times contribute finitely by the energy bound. This is the standard velocity-support estimate; the direct argument applies in every dimension. [Duell, arXiv:1603.07512v2, Lemma 6, three spatial dimensions](https://arxiv.org/pdf/1603.07512v2)

Scale the packet by a single positive constant until its energy is at most $B$ and its total observed norm over **all past times** is at most $D$. One admissible history is zero. Another is that scaled packet with its observed field canceled by a single admissible additive error. The two future readings remain separated for every duration, which proves failure. This construction relies on positive error allowance; exact uniqueness on a narrower cone is a separate question.

The distinction is physical even in a model with a unique free evolution from Cauchy data. A fast packet can approach today's neighborhood from a direction covered by the full past cone while leaving only a small integrated trace inside a narrower observing region. A compact spatial average can respond weakly to arbitrarily fast massive modes because its Fourier transform has no finite cutoff. The argument concerns the possibility of arbitrarily accurate recovery. It supplies no macroscopic lower bound on the hidden signal and no prediction about what a typical packet or a stochastic detector would do. Intermediate geometries with oscillating widths are outside the two cases.
