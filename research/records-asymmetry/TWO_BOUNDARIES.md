# How much history survives two blank boundaries?

*18 November 2026. Coordinator analysis of [the footprint experiment, Result 10](RESULT.md). Proofs and finite checks below. No external review or priority claim.*

In the 12-site example, 256 rotor configurations survive the endpoint condition. They produce **two** visible walks. The entire displayed past and future are determined by the first step. This changes the interpretation of the equality of record scores. The footprint can indicate the same bit twice because the ensemble permits no further variation in the path.

The distinction can be made arbitrarily large. On the line, compare two reversible walkers with the same position increments (one site left or right), the same footprint update, and the same requirement of blank ground at both ends. At duration $T=4k$, the first walker retains exactly **one bit** of visible path entropy. For the second walker, visible path entropy divided by $T$ tends to **one bit per step**. In both, every footprint is exactly the parity of past arrivals and exactly the parity of remaining future arrivals at its site.

## What the boundary actually says

Start at position 0 with every footprint off. On arrival at $p_t$, toggle its footprint. Write $S_t$ for the set of lit sites. The run is accepted when $S_T=\varnothing$. Toggling is addition modulo two. Consequently, for each accepted walk and each site, the parity over steps $1,\ldots,t$ equals the parity over steps $t+1,\ldots,T$. This is a pointwise identity, independent of the path law or prior. It concerns the two complete intervals. It gives no equality for arbitrary shorter windows.

Let $N_T$ count distinct accepted *position sequences*, and let $h_T$ be the Shannon entropy, in bits, of the position sequence under the initial ensemble conditional on acceptance. Neither quantity counts unused hidden degrees of freedom. A trajectory of the closed machine is deterministic once its initial state is specified. The entropy here measures variation among admissible paths.

## Walker 1. The flipping scatterer

The initial heading is right. At a departure site the rotor either transmits or reflects the incoming heading, then flips its state. Initial rotors are independent fair bits. The step is invertible: remove the footprint at the arrival site, use the outgoing heading to locate the previous site, restore the rotor there, and recover the incoming heading.

**Classification.** On the integer line, the only positive accepted durations are $T=4k$. There are two accepted paths. In one, the first four arrivals are $1,2,1,2$, the next four are $3,4,3,4$, and so on. The other is its spatial reflection. Each has probability $2^{-(2k+1)}$ before conditioning. Hence acceptance has probability $2^{-2k}$ and $h_{4k}=1$. The classification carries over to a ring of length $L\ge3$ when $T<L$: a lifted path spans fewer than $L$ sites of displacement, so distinct sites on that path cannot coincide modulo $L$.

*Blocking step.* On reaching a fresh site facing outwards with a reflecting rotor one site behind, there are two possibilities. Transmission takes the walker directly to the next fresh site. Reflection sends it one site back, where it reflects, and it then transmits on returning to the frontier. Either way the next fresh site is reached with a reflecting rotor behind. Induction shows that no site two or more places behind this frontier will be revisited. This is the blocking mechanism of Grosfils and colleagues; their Theorem 1 and blocking argument were checked in the primary text. [Grosfils et al., “Propagation and organization in lattice random media,” §2](https://arxiv.org/pdf/cond-mat/9905168)

*First block.* Write $s=\pm1$ for the first step. If the rotor at $s$ reflects immediately, the walker returns to 0. For $s=+1$ the rotor at 0 now reflects it back to 1, which transmits it to 2. The blocking step leaves 0 with one arrival forever. For $s=-1$ the rotor at 0 now transmits it to $+1$ with a reflecting rotor behind; site $-1$ stays odd forever. Neither partial excursion becomes blank before blocking takes effect. Thus an accepted path must first go to $s,2s$. The rotor at $s$ now reflects. If the rotor at $2s$ transmits, the blocking step at $3s$ leaves $s$ odd forever. It must instead reflect, giving $s,2s,s,2s$. The ground is blank and the current rotor is set to transmit outwards.

*Continuation and count.* At the end of such a block let the current site be $j$. The next departure transmits to the fresh site $j+s$ and leaves the rotor at $j$ reflecting. An immediate return to $j$ leaves one unmatched arrival there once the walker advances to $j+2s$. Continuing first to $j+2s$ instead forces a bounce, just as in the first block. Thus four more steps are necessary and sufficient for another blank endpoint. This proves the classification by induction. The initial rotor at 0 selects the sign; the first rotor states at the $2k$ successive fresh sites must alternate transmit, reflect. These $2k+1$ fair bits are specified, and all other rotors are free.

## Walker 2. A reversible walker with a direction tape

Include independent fair signs $d_1,\ldots,d_T$ on a tape in the initial state. At step $i$ move by $d_i$ and toggle the arrival footprint. Given the tape and step index, subtracting that move and undoing the toggle inverts the step. Including a head index makes the tape protocol autonomous. The prior gives every path on the line probability $2^{-T}$, so $h_T=\log_2 N_T$ under acceptance. Only the steering dynamics and its preparation have changed.

**Entropy rate.** Along $T=4k$, $h_T/T\to1$. Thus exact endpoint blankness costs a sublinear number of bits of path entropy in this model. This is consistent with the literature on even-visiting random walks, which imposes a closely related global parity constraint and studies more refined asymptotics. The following elementary rate proof uses our convention of counting arrivals, including returns to 0. [Noh, Park, Kim and den Nijs, original paper, abstract checked](https://arxiv.org/abs/cond-mat/0103549)

For a direct example of fresh variation, in each four-step block independently choose the right excursion $(1,0,1,0)$ or the left excursion $(-1,0,-1,0)$. Each clears its marks and returns to the origin, so every concatenation satisfies both boundaries. This already gives at least one free choice per four steps. Enumerating all accepted tapes gives 4, 32, 304 and 3,152 paths at 4, 8, 12 and 16 steps. The rate theorem is stronger and does not rely on extrapolating those counts.

*Proof.* Fix $b\ge1$. Make half-paths of length $2k$ from $\lfloor k/b\rfloor$ blocks of length $2b$, each starting and ending at 0. Fill the even remainder with a fixed sequence of out-and-back steps. There are
$$
M=\binom{2b}{b}^{\lfloor k/b\rfloor}
$$
such half-paths, each confined to $[-b,b]$. Their footprint parity patterns occupy at most $2^{2b+1}$ classes. Concatenating two half-paths from the same class gives a distinct length-$4k$ path with blank final ground: both halves start at 0 and their toggles cancel. By Cauchy–Schwarz the number of ordered matching pairs is at least $M^2/2^{2b+1}$. Hence
$$
\liminf_{k\to\infty}\frac{\log_2 N_{4k}}{4k}
\ge \frac{\log_2\binom{2b}{b}}{2b}.
$$
The central binomial coefficient is at least $2^{2b}/(2b+1)$, so the right side approaches one as $b$ grows. There are at most $2^{4k}$ paths in total. The two bounds prove the limit. By sign symmetry the first step is fair among accepted paths; revealing it removes exactly one bit and leaves the rate unchanged. The rate makes no assertion about independent increments, local prediction accuracy, or the entropy of a thermodynamic macrostate.

## What the original numbers were measuring

For the original 12-site, eight-step rotor experiment the acceptance probability is $1/16$. Of the 4,096 initial rotor configurations, 128 produce each surviving path. With just the initial boundary the path has entropy 5 bits over 41 distinct paths. With both boundaries, every nonconstant binary measurement made solely from the positions and footprints carries the same branch bit, possibly with its labels reversed. Conditioning on the first position removes all remaining information in such measurements.

There are even two ways to obtain **the identical published-style score of 1/6 bit per site in each direction**. Let a local event be the parity of visits within the indicated window on either side of the observation time.

| Observation and window | Why the average is 1/6 bit past and 1/6 bit future |
|---|---|
| Time 3, two steps | At sites 2 and 10 the footprint equals both local event bits. All other footprints are constant. |
| Time 2, one step | Sites 2 and 10 each give one bit about the past window only. Sites 1 and 11 each give one bit about the future window only. All other footprints are constant. |

In the first row the same local marks serve both readings. In the second row opposite local directions cancel in the average. The word “only” refers to the visit at the **same site**. The entire walk is recoverable from the branch bit. Altering the final condition also matters: allowing at most two lit sites at the end gives 2,048 configurations and 14 paths with 3.625 bits of entropy. These counts are specific to the stated run.

## Consequence for the philosophy of records

A test for a temporal arrow should ask **how many independently variable events the marks can distinguish after the boundary assumptions have been imposed**. Ten accurate footprints that all decode one choice supply one bit about the walk. In the rotor example an outside reader who knows the ensemble and sees the first move can forecast the entire path without ever looking at the later footprints. Treating every later match as a fresh piece of evidence about the direction of time double counts that choice.

The tape comparison sets the limit on this diagnosis. Even with an extensive range of histories, a footprint can exactly represent parities on both temporal sides. What survives in both models is the boundary identity. The disappearance of almost all variation in the rotor histories is a separate consequence of the steering mechanism. Neither result decides whether a mark was causally produced by a particular event, which conditional interventions are physical, or whether the future exists. Stradis's fork account specifically concerns observable events and the triangulation of an event by several records. Corroboration requires knowing which agreements share a source of variation. This finite calculation tests that premise in the walker; it does not refute the account. [Stradis, “Present records of the Past Hypothesis,” discussion of the fork asymmetry](https://doi.org/10.1007/s11229-024-04643-7)

[The exact check](check_two_boundaries.py) compares both path laws by enumeration, checks the site-level truth tables, and includes a wraparound control. The earlier literature already contains the flipping-scatterer mechanism and the even-visiting constraint. Priority for the particular comparison and the conditional two-path classification has not been established.
