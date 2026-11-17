# Can a bounded past settle a future reading?

*Coordinator research note, 17 November 2026. The cone estimate below is published. The deductions and philosophical interpretation have been checked in this session and await independent review.*

Two classes of massive fields allow exactly the same histories in every bounded spacetime region. They disagree about whether agreement on an event's entire past forces agreement tomorrow. There is a third possibility between exact determination and unrestricted openness. With a fixed energy budget, a sufficiently long finite record can exclude any specified discrepancy in a future spatial average, even when every finite record admits some discrepancy.

## The physical question

Work on all of Minkowski spacetime in $d\geq 1$ spatial dimensions, in units with light speed one. Take smooth real solutions of $L\phi=(\partial_t^2-\Delta+m^2)\phi=0$ with $m>0$. Compare two histories by subtracting their fields. Their difference $w$ solves the same equation. Its conserved energy is

$$
E(w)=\tfrac12\int_{\mathbb R^d}
\big(|\partial_t w|^2+|\nabla w|^2+m^2|w|^2\big)\,dx.
$$

This is the energy of the difference field. The argument permits either background field to have infinite energy. Let $P=\{(t,x):t<0,\ |x|<-t\}$ and $P_T=P\cap\{-T<t<0\}$. Agreement means equality of the fields throughout the indicated open set. A future reading will be a passive mathematical observable $F(w)=\int g(x)w(1,x)\,dx$ with a fixed smooth, compactly supported spatial profile $g$.

## What agrees locally and comes apart globally

**1. Every bounded field history has a finite-energy realization.** Given a bounded spacetime region $K$ and any smooth solution, choose a time slice earlier than $K$. A finite ball on that slice contains the entire causal footprint of $K$. Multiply both Cauchy data by a smooth compactly supported cutoff equal to one on a neighborhood of that ball. The resulting solution has finite energy and agrees exactly with the original on $K$ by finite propagation. This also works for any finite union of bounded regions. The realizing solution and its energy can depend on $K$.

**2. Agreement on the whole past fixes every finite-energy difference.** If $w$ vanishes on $P$, its energy on each negative time slice lies in $|x|\geq |t|$. Yang's exterior-energy estimate says that energy in $|x|>|t|$ tends to zero as $t\to-\infty$. The boundary sphere has zero spatial measure. Conservation therefore gives $E(w)=0$, hence $w=0$. This argument applies to energy-space solutions vanishing distributionally on $P$, using almost every negative time slice. Time reversal gives the same result for a future cone. Yang states the estimate for unit mass in every spatial dimension. The change of coordinates $(s,y)=(mt,mx)$ gives the result for every positive mass. Burnol gives the one-dimensional estimate. I checked both statements in the primary texts and rederived this corollary. [Yang, arXiv v1, Remark 1.10 immediately after (1.32)](https://arxiv.org/html/2309.15282v1#S1.SS2) · [Burnol, arXiv v4, Theorem 1, p. 2](https://arxiv.org/pdf/math/0509619)

**3. Some unrestricted smooth differences escape that conclusion.** Here is an explicit check of the [project's characteristic construction](massive-minkowski/RESULT.md). Use $u=t+x_1$, $v=t-x_1$, $a=m^2/4$, and set $j(z)=\sum_{k\geq0}(-a z)^k/(k!)^2$. Choose a nonzero nonnegative smooth $h$ supported compactly inside $(0,1)$. Set $w=0$ for $u\leq0$, and otherwise set

$$
w(u,v)=\int_0^u h(s)\,j\big((u-s)(v-1)\big)\,ds.
$$

This is smooth across $u=0$ since it vanishes in a neighborhood of that plane. The entire series gives $zj''+j'=-aj$. Differentiating first in $v$ and then in $u$ produces zero upper-endpoint term because of the factor $u-s$, so $w_{uv}=-aw$. Independence of the other spatial coordinates gives $Lw=0$ in every dimension. Throughout $P$ we have $u<0$. At $(t,x)=(1,0)$ we have $u=v=1$ and $w=\int h>0$. By continuity we can fix a nonnegative profile $g$ of integral one supported near the spatial origin with $F(w)>0$. Rescale $w$ to give $F(w)=1$. Part 2 now implies that its energy is infinite.

Apply part 1 to the union of $P_T$ and the support of this future reading. For every finite $T$ we obtain a smooth finite-energy difference that vanishes on $P_T$ and gives **the same unit discrepancy**. Part 2 rules out a single finite-energy difference that does this for every $T$. The observer's event and future reading stay fixed as the record extends backwards.

## The energy cost of keeping the same alternative alive

For that fixed reading, let $C(T)$ be the infimum of $E(w)$ among smooth free differences vanishing on $P_T$ with $F(w)=1$. Then

$$
C(T)<\infty \quad (0<T<\infty), \qquad
\lim_{T\to\infty}C(T)=+\infty .
$$

*Proof.* Finite cost follows from the cutoff construction. The admissible sets shrink as $T$ grows. If the costs stayed bounded, we could choose solutions $w_n$ vanishing on $P_n$, with unit reading and uniformly bounded energy. Their data at time zero have a weakly convergent subsequence in the energy Hilbert space $H^1\times L^2$. Call the solution from the limiting data $w$. Evaluation against the fixed profile at time one is a bounded linear functional of the data, since $|F(w)|\leq\|g\|_2\sqrt{2E(w)}/m$. Thus $F(w)=1$. For any smooth test function supported compactly inside $P$, pairing the evolving field with that spacetime test is also a bounded linear functional, by the same spatial bound integrated over its finite time support. The support lies in $P_n$ eventually, so the limiting pairing is zero. Hence $w$ vanishes on all of $P$. Part 2 forces $w=0$, contradicting $F(w)=1$.

In particular, fix an energy budget $B>0$ and a reading tolerance $\epsilon>0$. Once $C(T)>B/\epsilon^2$, any admissible difference with energy at most $B$ and exact agreement on $P_T$ has $|F(w)|<\epsilon$, by rescaling. Some nonzero discrepancy remains possible at every finite $T$, since the unit witness can be scaled down. No convergence rate follows from the compactness proof. Errors in the past record would require their own norm and estimate. The use of a spatial average makes the proof valid even in dimensions where point evaluation is unbounded on the energy space.

## What “could have differed” means here

**A free alternative and an intervention answer different questions.** I previously inferred a verdict about finite apparatus from the free-field theorem. That inference fails. If two source histories $J_1,J_2$ differ, the difference obeys $Lw=J_2-J_1$. For an exact control, take a smooth compact spacetime bump $b$ near the future reading with $F(b)\ne0$ and support disjoint from $P$. The source $Lb$ with zero data before the bump produces $b$, of finite energy on every slice, with the whole past unchanged. This construction allows a prescribed external source. A concrete apparatus calls for its own coupled dynamics.

**What the result establishes about time.** The verdict changes when we vary which complete free fields count as alternatives, even though their sets of bounded field histories agree. Within one finite-energy comparison class, a second distinction appears. Every finite stretch leaves an exact alternative, while extending that stretch defeats any fixed observable discrepancy at a fixed energy budget. Thus a claim that tomorrow is “open” needs to say what may vary, which past is held fixed, and whether arbitrarily small differences count. The same cone uniqueness holds in both time directions. To infer that the past *produces* the future requires a premise assigning a direction to that dependence. To infer that the future *exists now* requires a premise connecting uniqueness among alternatives to existence. Neither premise enters these proofs.

A global restriction could have independent physical justification. Agreement here concerns sets of possible bounded field histories. Probabilities, interventions, and competing cosmologies require additional structure. Weinstein's discussion of incoming radiation and prediction in Maxwell theory is a philosophical precedent for asking which restrictions give past data their force (abstract checked for this note). The energy estimate and the compactness reasoning have established mathematical antecedents. Priority for this combination or its philosophical use remains unassessed. [Weinstein, arXiv v2](https://arxiv.org/abs/1004.1346v2)
