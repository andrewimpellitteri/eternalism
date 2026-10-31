# Red-team audit: response-memory benchmark

**Verdict:** I found no material error in the benchmark's stated kernel, norm, asymptotic, transport, or restricted realization deductions. Its mathematical conclusions survive with the stated domains and qualifications. The strongest risk is a philosophical overreading: a response-support cutoff is an input/output property of a specified apparatus, not by itself a thick present, and an instantaneous predictive state need not constitute the process it encodes.

## Analytic checks

1. **Kernel and normalization.** The benchmark's retarded (3+1)-dimensional Klein–Gordon kernel has the direct atom (\delta_r/(4\pi r)) and interior tail (-mJ_1(m\sqrt{s^2-r^2})/(4\pi\sqrt{s^2-r^2})\). The tail quotient tends to (m^2/2) at the cone, so (k_m(r+)=-m^2/(8\pi)). This is consistent with the stated sign and normalization. The provenance is inherited from the coordinator's citation to Salnikov et al., Appendix A (A.1), printed p. 15; I did not independently retrieve the paper.

2. **Exact support.** For (m>0), the tail is real analytic on (s>r) and is not identically zero on any final interval; the large-argument Bessel oscillations also exhibit arbitrarily late nonzero values. Thus its support is unbounded. Given any proposed finite cutoff, a compact smooth input bump can be placed at lags beyond it inside an interval where the kernel has one sign, producing a nonzero output. For (m=0), only the atom at (r) remains, so the benchmark's upper support endpoint (H=r) follows from its definition. This endpoint does not imply a filled interval of sampled past times.

3. **Convolution norm and mass bound.** For a finite signed regular Borel measure, convolution on bounded continuous inputs with the supremum norm has operator norm equal to total variation. The upper bound is the variation inequality. For the lower bound, regularity lets bounded sign data be approximated in (L^1(|h|)) by bounded continuous functions; smooth compactly supported approximants are available on the real line. The same argument applies to the tail difference, whose atom cancels. With (z=m\sqrt{s^2-r^2}),
   \[
   s=\frac{\sqrt{z^2+(mr)^2}}{m},\qquad ds=\frac{z\,dz}{m\sqrt{z^2+(mr)^2}},
   \]
   so
   \[
   D_r(m)=\frac{m}{4\pi}\int_0^\infty\frac{|J_1(z)|}{\sqrt{z^2+(mr)^2}}\,dz.
   \]
   The inequality follows from \(\sqrt{z^2+(mr)^2}\ge z\). Since \(J_1(z)/z\to1/2\) at zero and \(|J_1(z)|/z=O(z^{-3/2})\) at infinity, \(C_*\) is finite and positive. For fixed (r>0), dominated convergence with majorant \(|J_1(z)|/z\) gives the stated sharp positive limit. It is an absolute gain bound uniform in (r), not a relative bound uniform in (r).

4. **Finite-window order versus all-history order.** On fixed \([r,T]\), the small-argument expansion gives \(k_m(s)=-m^2/(8\pi)+O(m^4(s^2-r^2))\), uniformly on that interval. For sufficiently small (m) the tail has one sign there, and integration gives \(m^2(T-r)/(8\pi)+O_{r,T}(m^4)\). In contrast, the full variation is asymptotic to a positive constant times (m). The difference is the nonuniformity of the growing lag domain, not a contradiction. The admitted input class places no common duration bound, and no fixed-energy or bandwidth inference follows.

5. **Tolerance, truncation, and the factor of two.** For the specified zero remote-input truncation, the operator error is exactly \(|h|((T,\infty))\), by the same convolution norm identity. If two inputs each have norm at most (U) and agree on the retained recent interval, their difference on the omitted part is bounded by (2U), yielding the stated (2U|h|((T,\infty))\). This factor is appropriate for uncertainty between two histories; comparison of one history with zero remote input has only the single-history bound. Integrability of the massive tail makes every positive-tolerance cutoff finite, and the global mass bound makes (T=r) sufficient when (mC_*/(4\pi)\le\delta\). The claimed discontinuity warning for the minimizing cutoff is appropriate.

6. **Spatial smearing and late-time support.** The pointwise operator bound integrates against nonnegative weights to give the (AB) bound. On the compact separation range, expanding \(\sqrt{s^2-r^2}=s+O(s^{-1})\) and the Bessel asymptotic gives a leading coefficient proportional to the total weight (AB>0\), with an (O_{m,a,b}(s^{-5/2})) remainder uniform in separation. Late cosine peaks therefore prevent compact support. Positivity and nonzero total weights matter: this argument does not establish the claim for signed or specially filtered weights. The remainder is for fixed (m>0), and gives no uniform-in-(m) late-time estimate.

7. **Transport window.** The boundary-driven characteristic solution is \(q(t,x)=f(t-x/c)\) after the initial interior data have exited. Setting \(\tau=L/c\) and averaging over (x\) gives the uniform positive kernel \(\tau^{-1}\mathbf 1_{[0,\tau]}\). Its support endpoint, tail variation, and tolerance cutoff are as stated (with endpoint values immaterial for this absolutely continuous kernel). Its full field is a Markov state while its measured input/output response samples a filled interval. These are compatible claims about distinct descriptions.

8. **Response invariance and LTI scope.** If two finite lag measures agree on all compact smooth inputs, evaluating the output at a fixed time shows their difference annihilates all reflected compact smooth test functions; hence they agree as distributions and as measures. Support and variation-tail error are invariant under realizations that preserve the specified input, output, clock, and gain. For finite-dimensional time-invariant state-space response (Ce^{As}B), analyticity on (s>0) means vanishing beyond a finite positive cutoff forces vanishing throughout (s>0). This excludes nonzero finite-cutoff dynamic impulse responses in that realization class; it does not cover delays or distributed transport. A feedthrough atom is separate.

## Scope and repairs

The benchmark already makes the crucial distinctions: changing (m) changes the operator; the source and detector define the operational channel; an exact support endpoint need not be filled; transport duration is not a universal property of every observable; and equal input/output behavior does not prove ontological identity. Preserve those qualifications when summarizing it. In particular:

- Do not infer a thick present from the massive tail or from the transport kernel alone. The former is a point-channel response with an integrable oscillatory tail; the latter is a positive filled window for a selected protocol.
- Do not infer that instantaneous predictive sufficiency makes the represented process unreal or instantaneous. The transport field state encodes the boundary history while the measured response extends over (\tau\).
- Do not treat mass variation as two states of one fixed operator with the same complete Cauchy data, or use the (m\to0\) estimate as a fixed-energy or universal practical-detectability result.
- Keep input/output equivalence narrower than ontological equivalence. It fixes the measured response under specified access, not hidden carriers or internal organization.

No repairs to the benchmark's equations were required. This audit supports its elementary derivations only; it is not a novelty result, a broad prior-art review, or an independent source verification.
