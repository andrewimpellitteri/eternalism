# Bounded audit: delayed feedback constitutive test

**Verdict:** The feedback test's algebra and causal-delay conditioning are correct as stated, for the specified bounded-signal model with fixed delays and \(0\le g<1\). The key limitation is constitutive: a decaying echo loop is causal integration and organizing feedback, but the equations do not establish that the loop is self-sustaining or that its remote causal ancestry constitutes one unity or a present.

## Algebra and physical conditioning

Let \(\tau=L/c>0\), return delay \(\sigma>0\), and \(\ell=\tau+\sigma\). Characteristics of the outgoing transport equation give \(z(t)=q(t-\tau,0)\). Substituting the delayed return at the inlet yields
\[
z(t)=f(t-\tau)+g z(t-\ell).
\]
The return term is delayed by its physical transit time; there is no instantaneous action from a spatial average to the inlet.

For bounded continuous \(f\), iteration gives
\[
z(t)=\sum_{n=0}^{\infty} g^n f(t-\tau-n\ell).
\]
The series converges uniformly since its tail is bounded by \(\|f\|_\infty\sum_{n>N}g^n\). It defines a bounded continuous solution with norm at most \(\|f\|_\infty/(1-g)\). If two bounded solutions differ by \(d\), then \(d(t)=g^N d(t-N\ell)\) after \(N\) iterations, hence \(|d(t)|\le g^N\|d\|_\infty\to0\); uniqueness follows. This includes \(g=0\). With zero path signals before a finite preparation time and \(f=0\) before preparation, only finitely many terms contribute at each fixed output time. As observation age increases, the largest contributing echo index increases, so finite preparation supplies no age-independent uniform lookback cutoff.

The external-injection-to-outlet impulse measure is
\[
h_g=\sum_{n\ge0}g^n\delta_{\tau+n\ell}.
\]
For \(g=0\) its support endpoint is \(\tau\); for every \(g>0\), distinct atoms occur at arbitrarily large lags. Since all coefficients are positive,
\[
\|R_g-R_0\|_{\infty\to\infty}
=\|h_g-h_0\|_{\rm TV}
=\sum_{n\ge1}g^n
=\frac{g}{1-g}.
\]
The total-variation identity applies on bounded continuous histories; unrestricted compact smooth inputs can approach the supremum. Thus the response change tends to zero with \(g\), despite the exact-support jump.

After the stated DC calibration, \(\widetilde h_g=(1-g)h_g\) has total mass one. Relative to \(h_0=\delta_\tau\), the difference has mass \(-g\) at \(\tau\) and positive mass \((1-g)g^n\) at each later atom. The supports are disjoint, so
\[
\|\widetilde h_g-h_0\|_{\rm TV}
=g+(1-g)\sum_{n\ge1}g^n
=2g.
\]
For \(T_n=\tau+n\ell\), the calibrated tail after that cutoff is
\[
\sum_{k\ge n+1}(1-g)g^k=g^{n+1}.
\]
These identities are correct. Calibration fixes constant-input gain, while the \(2g\) difference still measures a changed response shape; calibration does not make the systems equivalent.

The input distinction in the final section is also correct and consequential. If the total junction signal \(j(t)=q(t,0)\) is the prescribed input, then transport gives \(z(t)=j(t-\tau)\), independent of \(g\). The \(f\to z\) protocol instead prescribes external injection before feedback mixing. Holding \(j\) fixed as \(g\) changes generally requires changing \(f\); these are different boundary conditionings/interventions on the same apparatus, not two internal realizations preserving the same input-output protocol.

## Red-team scope

The loop supplies a concrete causal organization: an outlet signal returns after \(\sigma\), changes a later inlet signal, and yields repeated echoes separated by \(\ell\). With \(g<1\), each echo attenuates geometrically. Nothing in this recurrence proves autonomous self-sustenance: the model is explicitly driven by \(f\), and it includes no closed energy budget or criterion for persistence when external injection stops. Calling it “feedback” is warranted; treating it as a sufficient criterion for composite unity is an additional premise.

Likewise, unbounded causal ancestry is a property of the chosen \(f\to z\) response. It does not show that every earlier contributing injection remains constitutive of the current organized system. The present carrier fields may encode that ancestry, while a constitutive account may instead identify the current carriers, one circulation, or another physically grounded activity as the unity. Those proposals need independent criteria and tests. The alternative \(j\to z\) protocol further shows why system boundary and intervention choice need justification before response duration can act as an ontological selector.

No equation repair is needed. The coordinator identifies Julius O. Smith III's author-hosted “Feedback Comb Filters” section as a directly read antecedent; I rely on that inherited source check and make no novelty claim or independent literature claim.
