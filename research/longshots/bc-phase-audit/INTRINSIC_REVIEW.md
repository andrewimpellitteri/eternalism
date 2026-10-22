# Independent review: intrinsic event E2

Checked 2026-10-22. This review independently derives the count generating function and checks the event and measure arguments in `INTRINSIC_EVENT.md`. I have not repeated the finite causet enumeration or rational tail enclosure checker assigned to the coordinator.

## Derivation of the finite polynomial and tail product

For a birth into parent C, the new element is minimal exactly when its precursor is empty. Existing elements cannot acquire new predecessors, so for every finite stage

\[
M_N=1+\#\{\text{empty-precursor births through size }N\}.
\]

Here the initial singleton is size one; “three births” in the coordinator’s notation means the size-three causet after two transitions.

At size two the chain and antichain cylinders each have amplitude 1/2. For the chain parent, q(chain)=1/4 is the empty-precursor transition, giving amplitude 1/8 and increasing the minimum count from one to two. The sum of its nonempty-precursor transitions is 3/4 by MSR, giving total amplitude 3/8 at minimum count one. For the antichain parent, q(anti)=u/4 gives amplitude u/8 at count three. MSR makes the sum of its nonempty transitions 1-u/4; multiplied by the parent amplitude 1/2, this contributes (4-u)/8 at count two. Adding the two parent contributions yields

\[
G_3(z)=\frac38z+\frac{5-u}{8}z^2+\frac{u}{8}z^3
=z\left[\frac38+\frac{5-u}{8}z+\frac{u}{8}z^2\right].
\]

This uses complex amplitude addition and MSR, not a probability interpretation of the early transitions. It counts minimum number, not causet shapes.

At each parent size n≥3, the empty-precursor amplitude is q_n=10^{-n}, independent of the parent. The sum over every nonempty precursor is 1-q_n by MSR. All those nonempty births leave M unchanged; the empty one increments it. Therefore, after summing over all parent histories at a fixed minimum count, the next stage multiplies its generating polynomial by

\[
(1-q_n)+q_nz=1-10^{-n}+10^{-n}z.
\]

Iterating gives exactly

\[
G_N(z)=G_3(z)\prod_{n=3}^{N-1}(1-10^{-n}+10^{-n}z),
\]

where G_N is the pushforward of the size-N cylinder amplitudes by M_N. This step is valid even though individual transitions are complex: only the aggregate nonempty contribution is replaced by the MSR identity, and the empty contribution is the common scalar q_n. It does not claim that each individual later transition is a probability.

For the real reference process P0, the minimum-increment indicators after size three are independent Bernoulli variables with parameters 10^{-n}: conditional on any history at size n, their probability is the same 10^{-n}. Since \(\sum_{n\ge3}10^{-n}=1/900\), the total number K of later increments is finite P0-almost surely. Its PGF is the convergent product

\[
\mathbb E_{P_0}[z^K]=\prod_{n=3}^{\infty}(1-10^{-n}+10^{-n}z),\qquad |z|\le1.
\]

The non-atomic completion establishes \(\nu_u\ll P_0\) with an L1 density, for both u values. Hence K is finite |nu_u|-almost everywhere as well. The finite-stage functions z^{M_N} are bounded by one for |z|≤1 and converge pointwise on that full-measure set. Finiteness of |nu_u| permits dominated convergence for the complex integral. Thus the completed-history generating function is the stated product, and this limiting step does not require a conditionally convergent sum over paths. For z=0, the convention is harmless because M_N≥1 and all terms vanish.

## E2: invariance, measurability, and value

The finite-stage event \(\{M_K=2\}\) is a finite union of size-K cylinders. Because M_K is nondecreasing, the completed event is

\[
E_2=\{M_\infty=2\}=\bigcup_{N\ge1}\bigcap_{K\ge N}\{M_K=2\}.
\]

This is in the cylinder-generated sigma algebra. It is invariant under every relabeling/natural labeling of the completed causet because order isomorphisms preserve minimal elements. Thus the subset of labelled histories is a well-defined relabeling-invariant event. This set invariance does not imply that the entire labelled measure, vector measure, or decoherence functional is covariant.

Write

\[
b_0=\prod_{n\ge3}(1-10^{-n}),\qquad
s=\sum_{n\ge3}\frac{10^{-n}}{1-10^{-n}}
=\sum_{n\ge3}\frac1{10^n-1}.
\]

The tail probabilities of zero and exactly one minimum-increment are b0 and b1=b0s, respectively. To finish with exactly two minima, either the size-three count is already two and the tail has zero increments, or the size-three count is one and the tail has exactly one increment. Reading the z² coefficient therefore gives

\[
\nu_u(E_2)=\frac{(5-u)b_0+3b_1}{8}
=\frac{b_0}{8}(5+3s-u).
\]

The first term combines the size-three z² coefficient (5-u)/8 with b0; the second combines the z coefficient 3/8 with b1. This independently checks the coefficient selection.

For u=1, \(\nu_1(E_2)=b_0(4+3s)/8\), a positive real number. For \(u=(3+4i)/5\), the amplitude has nonzero imaginary part \(-b_0/10\). More strongly, with A=b0(5+3s)/8 and B=b0/8, \(\nu_u(E_2)=A-uB\) and \(\nu_1(E_2)=A-B\). Since |u|=1,

\[
\mu_u(E_2)-\mu_1(E_2)=|A-uB|^2-(A-B)^2=2AB(1-\operatorname{Re}u)
=\frac{b_0^2(5+3s)}{80}>0.
\]

Using s≥0 and \(b_0\ge1-\sum_{n\ge3}10^{-n}=899/900\), the claimed bound follows:

\[
\mu_u(E_2)-\mu_1(E_2)\ge\frac{(899/900)^2}{16}
=\frac{808201}{12960000}>0.
\]

The product lower bound follows first for finite products from \(\prod_i(1-p_i)\ge1-\sum_i p_i\), then by taking the limit. This is a strict difference in the rank-one quantum measures of the same intrinsic proposition under the two specified dynamics. The exact finite enumeration and sharpened rational interval enclosure remain with the coordinator, as assigned.

## What the difference does and does not refute

It refutes an equivalence between these two fixed models if the proposed equivalence identifies E2 as the same proposition and preserves its rank-one quantum-measure value. Such a map would have to send a single event to values that the calculation shows are unequal. The scalar amplitudes on E2 differ too, but their phase is not itself a probability. A map that reinterprets E2 as a different event, preserves only some smaller event family, or does not preserve \(\mu\) is outside this counterexample. It does not refute general equivalence claims between whole classes of norm-only and fully covariant models.

The result is not empirical distinguishability. \(\mu(E_2)=|\nu(E_2)|^2\) is a quantum-measure value, not automatically a Kolmogorov probability or detector frequency. For the binary partition \(\{E_2,E_2^c\}\), the rank-one decoherence functional has

\[
D(E_2,E_2^c)=\overline{\nu(E_2)}\,[1-\nu(E_2)],
\]

which is generally nonzero; the two alternatives are not thereby shown to be decoherent. No instrument, state-preparation protocol, readout, or rule connecting the event to observed records is supplied. A CPTP classical-record channel or another specified measurement model could change what is accessible. The calculation also does not establish a pure phase/gauge effect: u changes the antichain gregarious amplitude and other finite transition magnitudes, so these are two different dynamics with the same late schedule, not identical cylinder data related by a gauge map.

## Remaining assumptions and limits

- The limit uses the previously established finite countably additive complex measure \(\nu_u\), finite total variation, and absolute continuity with respect to the real-percolation reference P0. Both u choices must satisfy the nonzero-transition and L1-completion proof. The recorded early inverse weights are nonzero; the PERCOLATION_TAIL bounds dominate the u=1 perturbation as well as the complex case.
- The reference process is used to control the tail and its minimum-count law. It is not substituted for \(\nu_u\) on early cylinders. The tail factors are positive because the late q_n are real and shape independent.
- Countably many unions/intersections establish sigma-algebra measurability, not a finite-time measurement procedure. Relabeling invariance of E2 is a property of the event set, not a proof of full covariance for complex cylinder amplitudes or off-diagonal D values.
- This review checks the symbolic generating-function and measure-limit logic. It does not independently enumerate finite causets, reproduce the coordinator’s exact rational enclosure, or audit an external source. No claim about instruments, physical probability, ontology, or a pure gauge transformation follows.

## Fixed-cylinder-norm defeat check

I independently checked the narrowing in `FIXED_DATA_CHECK.md`. For the size-three V poset, whose size-two parent is the antichain, the full-precursor weight is

\[
w_u(\text{anti}_2)=\frac4u-3,
\]

so its transition amplitude after the size-two cylinder of amplitude 1/2 is

\[
A_u(V)=\frac12\frac{u}{4}\left(\frac4u-3\right)=\frac{4-3u}{8},\qquad
c_u=|A_u(V)|^2=\frac{25-24\operatorname{Re}u}{64}
\]

for \(|u|=1\). Thus, within this fixed one-parameter family, equality of all finite cylinder norms implies equality of c, hence equality of \(\operatorname{Re}u\). Two unit-circle points with the same real part are u and \(\bar u\) (coincident when u is real). This uses the assumption that every other parameter, especially the real late schedule, stays fixed.

Under u↦\(\bar u\), all q values conjugate, and the recursion for w uses only reciprocal and finite sums, so induction gives \(w_{\bar u}(C)=\overline{w_u(C)}\) for every finite C. Then every transition and finite path amplitude conjugates. In the stated non-atomic completion, the reference cylinder probabilities are real, so the finite-level densities conjugate. Conjugation is continuous in L1(P0), and uniqueness of the L1 limit gives \(g_{\bar u}=\bar g_u\) almost everywhere and \(\nu_{\bar u}(E)=\overline{\nu_u(E)}\) for every completed measurable event E. Therefore \(\mu_{\bar u}(E)=\mu_u(E)\) for every such E. This is an analytic all-events statement for the rank-one diagonal quantum measure, not merely the coordinator’s finite check. It does not show equality of D off the diagonal: the decoherence functionals are complex conjugates, and their imaginary off-diagonal terms can differ.

For the selected values, \(c_{(3+4i)/5}=53/320\), \(c_1=1/64\), and \(c_u-c_1=3/20\). With A and B as defined above,

\[
\mu_u(E_2)-\mu_1(E_2)=2AB(1-\operatorname{Re}u)
=\frac{16AB}{3}\,[c_u-c_1].
\]

The coefficient follows because \(1-\operatorname{Re}u=2/5\) and \(c_u-c_1=3/20\). Thus the E2 gap versus u=1 is already determined by this finite cylinder magnitude within the fixed family; it is not additional phase-only rank-one-\(\mu\) predictive content. The conjugate pair has the same c and indeed the same rank-one \(\mu\) on every completed event.

The broader completion estimate also checks with the coarser stated constant: \(b(4/u-100)\le106\) for |u|=1, so

\[
b(w(C)-w_0(C))\le 8n+106\binom n2\le53n^2.
\]

For n≥3, \(9^n>53n^2\) (true at n=3, and the ratio \(9(n/(n+1))^2\) exceeds one thereafter), so the nonzero-weight lower-bound argument still applies. The corresponding row-distance majorant \(53n^2/5^n\) is summable. This preserves the nonzero-transition and L1-completion argument for the whole unit-circle family. The comparison remains limited: equal rank-one \(\mu\) under conjugation is not equality of decoherence functionals or a claim of identical outcomes for arbitrary coherent controls or instruments. No empirical reading of c or E2 follows absent a specified measurement model.
