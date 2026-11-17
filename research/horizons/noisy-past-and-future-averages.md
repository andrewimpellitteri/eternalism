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
