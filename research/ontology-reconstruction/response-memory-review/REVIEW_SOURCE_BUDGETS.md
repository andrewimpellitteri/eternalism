# Bounded audit: source-budget hierarchy

**Verdict:** The §3a exponents, constants, and endpoint distinction are correct for the difference kernel at fixed \(r>0\), on the stated compact smooth source class with the peak output norm. The bounds are analytic consequences of the kernel; they impose no common duration, bandwidth, or peak constraint.

For conjugate exponents \(1/p+1/q=1\), \(1\le p<\infty\), the difference response has kernel
\[
k_m(s)=-\mathbf 1_{s\ge r}\frac{mJ_1(m\sqrt{s^2-r^2})}{4\pi\sqrt{s^2-r^2}}.
\]
For \(q>1\), Hölder duality gives the \(L^q\)-source to peak-output norm \(\|k_m\|_p\). Smooth compact inputs attain its supremum in the limiting sense: for finite \(q\), they approximate the \(L^q\) dual extremizer; for \(q=\infty\), bounded smooth approximations to the sign of the reversed kernel suffice. With \(z=m\sqrt{s^2-r^2}\),
\[
\|k_m\|_p^p
=\frac{m^{2p-1}}{(4\pi)^p}
\int_0^\infty
\frac{|J_1(z)|^p z^{1-p}}{\sqrt{z^2+(mr)^2}}\,dz.
\]
The integral is dominated by \((|J_1(z)|/z)^p\), which is integrable: \(J_1(z)/z\to1/2\) at zero and is \(O(z^{-3/2})\) at infinity. Thus, for each fixed \(r>0\),
\[
\lim_{m\downarrow0}
\frac{\|k_m\|_p}{m^{2-1/p}}
=\frac{C_p}{4\pi},
\qquad
C_p=\left(\int_0^\infty(|J_1(z)|/z)^p\,dz\right)^{1/p}.
\]
Since \(2-1/p=1+1/q\), this matches the benchmark's \(m^{1+1/q}\) rate, including \(q=\infty,p=1\). The bound before taking the limit is uniform in \(r\); the sharp asymptotic is only asserted at fixed \(r\).

The endpoint \(q=1,p=\infty\) is separate. Here \(\|k_m\|_\infty=(m^2/(4\pi))\operatorname*{ess\,sup}_{z>0}|J_1(z)|/z\). The stated Poisson integral gives
\[
J_1(z)=\frac{z}{\pi}\int_0^\pi\cos(z\cos\theta)\sin^2\theta\,d\theta,
\]
so \(|J_1(z)|\le z/2\). The ratio tends to \(1/2\) as \(z\downarrow0\), making its essential supremum \(1/2\), and hence \(\|k_m\|_\infty=m^2/(8\pi)\). Compact smooth \(L^1\)-normalized pulses concentrated near the cone lag approach this peak norm; their peak amplitudes and bandwidths cannot be bounded uniformly.

The light-cone delta cancels in \(R_m-R_0\), which is why these finite-\(q\) peak-output difference norms exist. Each individual point-source response retains the delta and is not a bounded \(L^q\to L^\infty\) map for finite \(q\). The difference estimate therefore says nothing by itself about boundedness of either individual point response. Likewise, an \(L^2\) budget on prescribed source amplitude is not a field-energy bound; that would require source work and detector-coupling physics. No fixed duration, bandwidth, or common peak constraint is present. No correction to §3a is needed.

The coordinator identifies NIST DLMF 10.9.4 as the source of the Poisson integral and reports the standard norm argument as elementary. This review did not independently retrieve DLMF and makes no novelty or prior-art claim.

## Added physical energy budget (§3b)

The energy estimate also checks out for the stated forced Klein–Gordon experiment. Multiplying the equation by \(\partial_t\phi_m\), integrating by parts, and using finite propagation with zero pre-source data gives
\[
E_m'(t)=f(t)\int a\,\partial_t\phi_m\,dx.
\]
Since \(\|\partial_t\phi_m\|_2\le\sqrt{2E_m}\), regularizing \(\sqrt{E_m}\) as the benchmark describes and integrating from zero energy yields
\[
\sqrt{E_m(t)}\le \frac{\|a\|_2\|f\|_1}{\sqrt2},
\]
uniformly in time and \(m\ge0\). The pointwise tail bound follows from \(|J_1(z)|\le z/2\):
\[
|k_m(s)|=\frac{m^2}{4\pi}\frac{|J_1(z)|}{z}\le\frac{m^2}{8\pi}.
\]
The mass-independent direct atom cancels in the difference. Integrating the remaining kernel against the fixed spatial weights gives
\[
\|Y_m-Y_0\|_\infty\le
\frac{m^2\|a\|_1\|b\|_1\|f\|_1}{8\pi}.
\]
Thus the stated sufficient condition \(\|f\|_1\le\sqrt{2E_{\max}}/\|a\|_2\), for \(\|a\|_2>0\), implies both the common field-energy upper bound and the displayed readout bound. This does not equate the actual energies for different masses, include energy spent by the source apparatus, model gravitational backreaction, or establish that the input condition is necessary. It is a physical upper budget for this prescribed-source experiment only.
