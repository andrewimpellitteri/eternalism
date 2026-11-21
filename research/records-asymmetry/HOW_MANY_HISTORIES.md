# How many histories can the footprints distinguish?

*Coordinator follow-up, 18 November 2026. Exact finite counts and a sampling bound for the fair one-dimensional tape model. Internally checked. Priority and external review remain open.*

In [the two-boundary experiment](TWO_BOUNDARIES.md), a history is the sequence of walker positions. Let $B_T$ denote blank ground at times 0 and $T$, and let $W$ be the history. A noiseless record $R=f(W)$ splits the accepted histories into classes. Two histories in the same class give exactly the same record. Three counts answer different observer questions:

- Before looking, the number of possible record values is the number of distinguishable classes.
- After seeing $r$, the feasible histories are precisely the members of its class.
- With a specified probability law, the average information gained is $I(W;R\mid B_T)=H(R\mid B_T)$ bits. Here conditioning on $B_T$ always means the event holds. The effective number of equally probable classes is $2^{H(R\mid B_T)}$, which can be nonintegral. Jointly reading several marks requires their joint entropy; the chain rule credits each extra mark only with the information left after the previous marks are known.

## A photograph at eight steps

Take a fixed midpoint photograph at time 4 of the entire footprint pattern, excluding the walker. Use an unwrapped line and the stated initial ensembles. The rotor model admits two equiprobable mirror histories. In either history the ground is blank again at time 4. The midpoint photograph has one possible value and gives zero bits. At time 2 there are two equiprobable photographs, each identifying the whole route. A time-4 photograph including the walker's position also distinguishes both routes.

For the fair direction tape there are 32 equiprobable accepted histories. All six possible time-4 photographs and their class sizes are listed below. Coordinates give the sites where a footprint is on.

| Lit sites | Compatible histories |
|---|---:|
| none | 16 |
| $-2,0$ | 4 |
| $-1,1$ | 4 |
| $0,2$ | 4 |
| $-3,-1$ | 2 |
| $1,3$ | 2 |

Hence the ground photograph gives 2.125 of the 5 route bits, leaving 2.875 bits unresolved on average. Every possible photograph leaves multiple routes. Adding the current position gives 10 classes and 3.125 bits. A film of the ground at every step identifies all 32 routes: between consecutive frames exactly one site changes, revealing the arrival position. The quantitative difference arises even with noiseless, complete spatial coverage.

## How often must the ground be photographed?

Use the fair tape on the integer line, take $T$ through multiples of four, and fix in advance $m=m(T)$ distinct observation times in $1,\ldots,T$. Let $R$ be the ordered ground photographs. Two conclusions hold uniformly in their placement.

1. If $m=o(T)$, then $H(R\mid B_T)=o(T)$, even if each frame includes the walker. A vanishing fraction of steps photographed captures a vanishing fraction of route information.
2. For any schedule, $H(R\mid B_T)\ge m+\log_2\Pr(B_T)=m-o(T)$. Thus photographing a positive fraction of the steps retains a positive information rate even without the walker in frame. This lower bound concerns average information. Full reconstruction from a particular partial schedule is a different claim.

The [path count](TWO_BOUNDARIES.md#walker-2-a-reversible-walker-with-a-direction-tape) gives the common input $\Pr(B_T)=2^{-o(T)}$ and $H(W\mid B_T)=T-o(T)$. Here $o(T)$ denotes a quantity whose ratio to $T$ tends to zero. The proof exploits the one-dimensional fair path and this subexponential cost of conditioning. The rotor model has a different path law and a different cost.

*Upper bound.* Partition the steps up to the last photograph into $m$ intervals of lengths $\ell_i$. Write $M_i$ for the largest absolute displacement from the starting position within interval $i$. Before conditioning, a useful tail bound is
$$
\Pr\left(\sum_i M_i\ge\epsilon T\right)
\le [2(1+T/m)]^m \exp(-\epsilon^2T/2).
$$
Indeed, choose one partial sum and a sign in each interval to realize the maxima. There are at most $\prod_i 2(\ell_i+1)\le[2(1+T/m)]^m$ such choices. For any fixed choice the result is a sum of at most $T$ independent fair signs. Its exponential moment at $\lambda>0$ is bounded by $\exp(T\lambda^2/2)$ since $\cosh\lambda\le\exp(\lambda^2/2)$. Exponential Markov with $\lambda=\epsilon$ and a union bound give the inequality.

For $m=o(T)$ the prefactor has log $o(T)$. Dividing by $\Pr(B_T)$ therefore still gives a vanishing upper bound for each fixed $\epsilon>0$. As $\sum_i M_i\le T$, its conditional expectation is $o(T)$. Encode each interval by its radius $M_i$ in unary, a one-hot endpoint displacement in $[-M_i,M_i]$, and the $2M_i+1$ parity changes relative to its starting position. At most $5M_i+3$ bits suffice. Starting at the known origin and blank pattern, these prefix-decodable descriptions reconstruct all photographed positions and footprints. The entropy is at most their expected code length, hence $o(T)$. Empty schedules are immediate.

*Lower bound.* Fix a proposed sequence of $m$ photographs. Conditional on any complete past through the step immediately before a scheduled photograph, the two next directions yield different photographs: they toggle different sites. Before boundary conditioning at most half of the conditional probability can give the specified frame. Iterating over the observation times bounds the probability of the entire proposed sequence by $2^{-m}$. Conditioning can raise this to at most $2^{-m}/\Pr(B_T)$. Shannon entropy is at least minus the base-two log of the largest atom, proving the claim.

## Many possible patterns can still carry little information on average

Even a *single* midpoint ground photograph has exponentially many **possible** patterns along $T=16n$. Here is an explicit family. Walk right in $n$ blocks. From $p=3i$ choose one of the two five-step arrival lists
$$
(p+1,p,p+1,p+2,p+3),\qquad (p+1,p+2,p+1,p+2,p+3).
$$
Return directly from $3n$ to 0, reaching the midpoint at time $8n$. Each block choice can be read from the parity at its own site $3i+2$: the two options differ there and the return trip adds the same toggle to both. Repeat the entire closed half-path to cancel every lit site by $16n$. All $2^n$ choices therefore give distinct feasible photographs. This is a lower bound on the support size, with no claim of optimality. Combined with the upper bound, it shows why counting all logically possible marks and measuring how much a typical photograph tells us yield different answers under the same prior and boundaries.

For this archive the temporal inference is precise. A surviving mark warrants a definite claim about visit parity on both sides. Recovering the sequence of visits uses changes between marks across time. In a long run, arbitrarily many full-ground photographs can still leave almost all sequence information unresolved if their sampling density goes to zero. These are properties of a reversible parity recorder in one spatial dimension. A device that stores timestamps or an ordered log has a different record map.

The [exact checks](check_two_boundaries.py) verify the eight-step partitions, full-film decoding, finite examples of the support construction and the preconditioning atom bound for arbitrary schedules through eight steps. The asymptotic conclusions follow from the proofs. Even-visiting walks and lamp-configuration entropy have a prior literature; the usual switch–walk–switch model randomizes the switches, whereas this device always toggles on arrival. No priority is claimed for the sampling argument. [Even-visiting walks](https://arxiv.org/abs/cond-mat/0103549) · [Realizations of other lamp switching rules, Remark 3.4](https://www.tamuz.caltech.edu/papers/renyi.pdf)
