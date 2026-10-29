# Repairing the observable-rigidity result without localized maximality

28 October 2026. Coordinator proof proposal; independent adversarial review requested. Uses Claude's geometric screening transport, not the unverified premise Lprime. No novelty claim.

## Exact replacement for the overstrong conclusion

Do not assert that the entire futures are onto-isometric. Instead: every matched geodesic proper-time reading agrees at every finite duration for which both readings are defined. Future existence duration, maximality and completeness are separate properties.

## Hypotheses

1. Smooth time-oriented globally hyperbolic spacetimes with marked b_i, same deterministic geometric field theory. W_i are the open potential realms in Claude SCREENING.md. An onto field-preserving isometry h:W_1->W_2 extends homeomorphically to b_1->b_2.
2. The geometric transport conclusion is proved: for Sigma_1 an earlier smooth Cauchy slice and K_1=Sigma_1 intersect W_1, K_2=h(K_1) is smooth spacelike acausal, and Jplus(b_i) subset Dplus_{M_i}(K_i). This is SCREENING.md Theorem3(a), independently inspected but still being adversarially checked by Claude's worker.
3. Standard domain-of-dependence geometry: N_i=D_{M_i}(K_i) are open globally hyperbolic developments of their induced data with K_i Cauchy. Use the full two-sided domain, with the usual convention making it open; K_i are open partial hypersurfaces. They need NOT be maximal developments or lie in global Cauchy surfaces of M_i.
4. The specified field theory has the common-GHD extension property for these smooth data: two GHDs of the same data embed into one common GHD, compatibly with the initial data and fields. For smooth vacuum Einstein equations this is Sbierski arXiv:1309.7591v3 Theorem2.7. For coupled theories cite or establish the corresponding theorem; do not infer it from determinism alone.
5. Launch tangents are matched by the local extension of h at b established below, or included through an equivalent smooth observer-germ condition.

## Common extension

The neighborhood isometry h identifies the induced metric, extrinsic curvature and matter Cauchy data on K_1,K_2. By hypothesis4 choose common GHD N with compatible time-oriented field-preserving isometric embeddings F_i:N_i->N. This requires neither N_i to be maximal nor any ambient M_i maximality. Disconnected initial-data components can be treated componentwise; retain the components connected to the marked future.

We must identify the marks in N; initial-surface compatibility alone is insufficient without this step.

Choose a timelike curve alpha from a point p of K_1 in Iminus(b_1) to b_1. Such a p exists by following a past-directed timelike curve from b_1 to Sigma_1. The curve minus its final endpoint lies in Iminus(b_1) subset W_1. Mark-extension and causal convexity imply h(Iminus(b_1))=Iminus(b_2), as proved in SCREENING.md step2.

Both alpha and h(alpha) lie in the respective Dplus(K_i). Here is the useful elementary domain lemma: if q in Dplus(K), p in K and p<<y<<q along a timelike curve, then y belongs to Dplus(K). Otherwise a past-inextendible curve from y avoiding K, concatenated with the y-to-q segment, would give a past curve from q avoiding K; the segment itself cannot meet K because K is acausal and lies strictly to the future of p on that segment. Apply this with q=b_i. Thus the entire comparison path is in the two developments and the realm overlap.

At p, initial-data compatibility gives F_1(p)=F_2(h(p)) and equality of their differentials on T_p K_1. The two isometric embeddings also take the future unit normal to the same future unit normal of the common image of K; hence their differentials agree in the remaining normal direction. Thus F_1 and F_2 composed with h have the same full first jet at p. On the connected component of N_1 intersect W_1 intersect h^{-1}(N_2) containing alpha, these are isometric immersions into the same N. Uniqueness of isometric immersions from one common first jet (Sbierski Lemma3.1) gives equality across that component. Consequently F_1(alpha(t))=F_2(h(alpha(t))). Taking its endpoint limit gives

                    F_1(b_1)=F_2(b_2).

Since F_i are open embeddings, their image intersection contains a neighborhood of that common point. Their transition isometry F_2^{-1} composed with F_1 is therefore defined near b_1 and extends h from the overlapping past. It supplies the smooth local extension needed to match launch tangents; do not claim an arbitrary separately chosen tangent is automatically preserved.

## Reading agreement

Let gamma_i be the future timelike geodesics launched with the matched unit tangents. Whenever their segments through T exist in M_i, the segments are in Jplus(b_i) subset N_i. The embedded curves F_i composed with gamma_i are geodesics in the SAME smooth N with identical initial point and tangent. Geodesic IVP uniqueness therefore makes them agree through the common interval, in particular at T. The embeddings preserve metric, curvature and specified matter fields, so every corresponding scalar reading at T agrees.

No onto comparison of Jplus(b_1) and Jplus(b_2), no maximality of D(K), and no common global slice containing K_2 are required for this conclusion.

## Stronger proof status, narrower scope

This replaces the disputed Lprime by a standard common-development theorem, whose vacuum version is explicitly sourced. It does not prove common survival time: if a geodesic exists to T in only one M_i, the above comparison makes no assertion at that T. Nor does it prove equality of all future topology, all possible observers or extension classes.

In vacuum the theorem is conditional only on the stated causal-geometric transport and standard domain geometry, which must still be checked at their exact hypotheses. In a coupled theory it additionally requires the applicable common-development theorem in the stated regularity; the low-regularity scalar scattering limit is not silently included.

The independent fixed-background result in SCREENING_REPAIRED.md is logically separate and avoids all geometric common-development machinery.

## Additional corollary: full future agreement under marked causal completeness

There is a clean stronger conclusion under an explicit additional geometric hypothesis, rather than Lprime. Suppose every future-directed causal geodesic launched at b_i is complete in M_i, for BOTH i. Then the same common-extension construction gives an onto isometry between Jplus(b_1) and Jplus(b_2), carrying the fields and the canonical marked germ.

Proof: every q_2 in Jplus(b_2) is joined to b_2 by a causal geodesic in a globally hyperbolic spacetime (a maximizing timelike geodesic for chronological separation; a null geodesic for null separation). Parametrize this segment affinely on a finite interval, and transport its initial tangent through the canonical local isometry at b. Completeness supplies the corresponding segment in M_1. Both segments lie in their screened futures, hence in N_i. Their embeddings into N have the same initial data, so uniqueness identifies their endpoints. Therefore F_2(Jplus(b_2)) is contained in F_1(Jplus(b_1)). Reverse the argument to obtain equality. The transition F_2^{-1} composed with F_1 is an isometry on an open overlap containing the future and restricts to the claimed onto map.

Only completeness of causal geodesics issuing from the marks is used, not geodesic completeness everywhere. Timelike completeness alone gives the corresponding equality of chronological futures; the null-boundary conclusion needs the causal/null version or an additional boundary argument. This corollary does not establish completeness from shared realm data, and cannot be used if one completion develops an incomplete geodesic. Its assumptions should never be dropped in a philosophical summary.

Thus there are three different strengths: common-duration readings with ordinary common-development uniqueness; onto chronological future with marked timelike completeness; onto causal future with marked causal completeness. None uses localized maximality of restricted data.

## Sharpness example: same potential realm, different survival in nonmaximal developments

Take full Minkowski M_2 of dimension at least two, b=(0,0), q=(T,0) with T>0. Let M_1=M_2 minus Jplus_{M_2}(q), with its induced metric, and retain the same b. M_1 is open, smooth and vacuum. It is a past set, and a constant-time slice before b is Cauchy in it: every inextendible causal curve has a past tail reaching that slice, while endpoints on the removed future boundary only truncate the future. Alternatively, causal diamonds between points of M_1 are the same compact Minkowski diamonds because the upper endpoint is outside Jplus(q). Hence M_1 is globally hyperbolic. It is a nonmaximal GHD of the same earlier Cauchy data.

Its potential realm W_1 is exactly W_2=Minkowski minus Jplus(b). Inclusion W_1 subset W_2 is immediate. Conversely every spacelike x=(t,z) relative to b shares a future with b on b's FUTURE NULL cone, which is outside Jplus(q). For r=|z|>|t|, the point

 z_*=(lambda,lambda z/r),  lambda=(r+t)/2,

is null-related to both b and x and lies outside Jplus(q), since its time minus spatial radius is zero<T. It is a distinct successor of both. Strict-past x shares the successor b (and a small timelike successor of b before q). Thus all nonfuture points other than b remain in W_1. The identity identifies both open potential realms and their marked germs.

Yet the central unit-speed geodesic in M_1 ends at proper time T at the missing q, while in M_2 it continues indefinitely. Finite readings at durations strictly less than T agree, as the repaired theorem predicts. This is a concrete counterexample to inferring equal survival or onto future isometry from realm matching plus common-extension uniqueness alone.

The example does NOT refute the stronger proposal restricted to ambient MGHDs: M_1 is expressly nonmaximal and extends into M_2. Its role is to prove the necessity of an additional extendibility/completeness restriction for the stronger conclusion. It also shows why the repaired finite-reading result, which requires no ambient maximality, has a strictly different scope.

## Domain/component verification to use at integration

Each K_i is a smooth embedded spacelike hypersurface WITHOUT boundary as an intrinsic manifold: K_1 is open in Sigma_1, and h transports that local hypersurface structure to K_2. It is acausal in the ambient spacetime by causal convexity of W_i and acausality of Sigma_1. The standard domain theorem for an acausal topological hypersurface without boundary says its full domain D(K_i) is open and globally hyperbolic, with K_i Cauchy. This is an ordinary domain-of-dependence result, not a restricted-data maximality claim. Do not apply it to a closed disk WITH its edge included; that is a different hypothesis.

For components, use Cauchy splitting D(K_i) homeomorphic to R times K_i componentwise. Let C_1 be the component of D(K_1) containing b_1 and let K_1^b=C_1 intersect K_1, its connected Cauchy component. Choose p and alpha in C_1 as above. Since h(alpha) runs from h(p) to b_2 inside D(K_2), h(p) lies in the component C_2 containing b_2. The connected set h(K_1^b) is precisely the corresponding connected component K_2^b of K_2, because h is a diffeomorphism of K_1 onto K_2. Thus the two marked components are developments of the SAME connected initial-data manifold; Sbierski's connectedness convention applies directly. Every Jplus(b_i) is contained in that marked component, since it is causally joined to b_i and is already a subset of D(K_i). No component needed to screen the marked future is discarded.

Initial data induced on K_i^b obey the vacuum constraints automatically because the ambient metrics obey the vacuum equations. Their Riemannian metrics need not be complete: the source initial-data definition requires a connected smooth Riemannian manifold with its constraint tensor, not completeness. This is another reason not to add unmentioned asymptotic/completeness assumptions to the common-extension theorem.
