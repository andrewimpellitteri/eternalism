# Audit: finite-family common-subsequence selection

**Disposition: PASS with stated domain and gauge qualifications.** The coordinator's claim is correct as an existential statement for any finite family of admissible profiles, provided profiles being matched agree on the full pre-tail interval, all finite-cone approximants use the same sequence of vertices and the same null-coordinate normalization, and local domain-of-dependence uniqueness is applied on the truncated pre-tail triangles. Global uniqueness from past null infinity is unnecessary. This constructs a compatible finite collection of limits; it does not define a canonical solution for each profile.

## Argument checked against the source

Luk–Oh–Yang §2.1, equations (2.4)–(2.5), prescribe λ⁻¹∂_v(rφ)=Φ and λ=1/2 on (C_{u_0}), with the regular-axis conditions (r=m=0) and (u=v) on Γ. Their local characteristic theorem gives uniqueness for these data. The constraints determine the remaining cone variables from the same profile and vertex normalization. In particular, the cone values of (r,\phi,m) up to (v<V) depend only on Φ restricted to ([u_0,V)).

For profiles Φ and Ψ agreeing on (v<V), the finite-cone solutions with the same (u_n\to-\infty) therefore agree on

\[
T_{n,V}=\{(u,v):u_n\le u\le v<V\}.
\]

The paper states local uniqueness for a full outgoing-cone datum, rather than spelling out this truncated-domain version. The needed inference is the ordinary local domain-of-dependence consequence: points in (T_{n,V}) have their past on the initial cone at (v\le v_{point}<V), so data at (v\ge V) cannot enter. It can also be obtained by applying the local uniqueness argument on successive bounded characteristic triangles. The regular axis is part of the boundary data and must be included; dropping it would leave the reflected spherical solution underdetermined.

Section 4, printed pp.27–29, starts with an arbitrary sequence (u_n\to-\infty), obtains bounds uniform in (n), and extracts a subsequence converging on every compact subset of (Q). For a finite list of profiles, extract successively for each profile, always from the subsequence retained so far. Each profile's estimates give precompactness along every subsequence; finiteness means the last subsequence works for the entire list. Equivalently, diagonalize over a countable compact exhaustion of (Q) and the finite profile index. Since each matched pair's approximants already agree on (T_{n,V}), its two limits agree on every compact subset of (Q\cap\{v<V\}). No uniqueness of the limiting global solution is used.

The conclusion is existential: choose these joint-subsequence limits as the members of the finite family. A separately selected limit for each profile could lie on a different subsequence and need not match. Nor does joint extraction imply equality between limits whose early profiles differ; it preserves equality only for profiles whose incoming data agree throughout the compared pre-tail interval.

## Gauge, domain, and observer qualifications

- **One synchronized gauge is essential.** The reduced system has the reparameterization freedom ((u,v)\mapsto(U(u),V(v))), noted in §2.1, Remark 2.2. Use the same numerical (u_n), the same (v)-label on every cone, λ=1/2 there, and the same (u=v) identification on the axis for every profile. If the profiles are translated or each limit is independently regauged, equality as functions of ((u,v)) no longer follows. A common gauge is a construction choice, not a new physical identification.
- **Only compact subsets are covered at a time.** Every compact (K\subset Q\cap\{v<V\}) lies in (T_{n,V}) for all sufficiently large (n), but the whole unbounded wedge is not one compact set. The diagonal exhaustion is what gives equality at every finite point. Keep readings strictly inside (v<V); equality at the boundary (v=V) is not implied when the profiles can differ there or after it.
- **The common region is a characteristic domain, not all of the past of every point by assertion.** The causal-coordinate monotonicity and local uniqueness give the triangular region above. Do not extend matching to a larger domain that has past characteristics meeting (v\ge V), or to a maximal-development region not represented in (Q).
- **Central clocks require metric reconstruction regularity.** The limits in §4 have (r^{(n)}\to r) in (C^2), (m^{(n)}\to m) in (C^1), and the stated scalar derivative convergence on compact sets. With the common gauge and the source's regular-axis reconstruction, λ=∂_vr, ν=∂_ur, and Ω²=−4νλ/(1−2m/r) agree on the matched wedge. This yields the same central proper-time element and the same scalar/curvature readings there. A claim about arbitrary observer geodesics also needs the corresponding regularity for uniqueness of the geodesic initial-value problem. These conclusions require staying in the regular region where (1-2m/r>0).
- **Finite families only.** For each fixed finite list, all source bounds are available profile by profile and successive extraction suffices. This gives no continuous, differentiable, or uncountable profile selection, and no response-rank result.

## Implication for the energy-lane claim

For any finite collection of early profiles and their late-tail variants, group variants by their shared early profile. Within each group, the common-subsequence argument selects solutions with exactly matching pre-tail fields. If every tail begins after (V), all members of that group share the same geometry and relational readings on compact subsets of (v<V), while their finite-cone incoming-energy values may differ according to the tail. The square-amplitude formula can then match those charges algebraically. It does not by itself identify the finite-cone charge with the mass of the selected global limit, prove ADM equality, or guarantee that different early profiles produce prescribed distinct readings.

## Falsifiers and scope

The argument would fail if the finite-cone approximants were not built from the same (u_n) and gauge; if the profiles differed somewhere below (V); if local characteristic uniqueness failed on the regular-axis triangles; if the compactness bounds were unavailable for one member of the finite list; or if reconstruction lost the regularity needed for the requested observer reading. None of these is a global-scattering-uniqueness requirement. Source check: arXiv:1605.03893v1, §2.1 and Remark 2.2, printed pp.7–8; §4 finite-cone sequence and compactness, printed pp.27–29. Read depth: full-text selective audit of those loci, not a reproof of their local existence or compactness estimates.
