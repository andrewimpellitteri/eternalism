# Whole-bow-tie matching is rigid in a deterministic globally hyperbolic theory

2026-10-28. Coordinator proof, awaiting independent review. General causal-geometric lemma plus an explicit Cauchy-uniqueness premise. Not a novelty claim.

## Geometric lemma

Let (M_i,g_i), i=1,2, be connected, smooth, time-oriented globally hyperbolic spacetimes, with marked events b_i. Set U_i=M_i\J^+(b_i), the OPEN exterior of the closed future cone. Suppose h:U_1 -> U_2 is a time-orientation-preserving onto isometry. Then U_1 contains a smooth spacelike Cauchy surface Sigma_1 of M_1, and Sigma_2=h(Sigma_1) is a Cauchy surface of M_2.

Proof of the first assertion: choose a Cauchy temporal function t on M_1 with t(b_1)=0. The slice t=-1 is Cauchy and is contained in U_1, since causal monotonicity forces t>=0 on J^+(b_1).

Both U_i are open past sets: y in U_i and x<=y imply x in U_i. Consequently a causal curve with endpoints in U_i remains in U_i, so acausality of Sigma_1 is preserved in the ambient M_2. Thus a causal curve meets Sigma_2 at most once.

Take any inextendible causal curve c in M_2 and any point q on it. Its past tail cannot remain forever in J^+(b_2). Otherwise, when q is in that set, the past tail is entirely imprisoned in the compact diamond J^+(b_2) intersect J^-(q), contradicting nonimprisonment in a strongly causal spacetime. Thus the tail enters U_2 and, because U_2 is a past set, stays there toward the past.

Pull that tail back by h. It is past-inextendible in M_1. Indeed, an extension would give a past endpoint p. If p is in U_1, h would extend the original tail, contradicting inextendibility. If p is outside U_1, then b_1<=p; the causal extension from p to any point x of the tail would imply b_1<=x, contrary to x in U_1. Hence there is no endpoint/extension in M_1. Since Sigma_1 is Cauchy, this past-inextendible tail, extended arbitrarily toward the future if necessary, meets Sigma_1. The future extension might cross Sigma_1 instead of the given tail unless the chosen endpoint lies to the future of Sigma_1. To eliminate that gap, use the full pulled-back curve in U_1: if it exits U_1 toward the future, its endpoint lies in J^+(b_1), which is strictly to the future of Sigma_1; it must therefore already have crossed Sigma_1. If it never exits and is future-inextendible in M_1, Cauchyness applies directly. If a finite future endpoint lies inside U_1, the original curve was extendible. These cases give an intersection on the original curve. Equivalently, the pulled-back past-inextendible tail eventually has t<-1, while its maximal U_1 continuation either reaches t>-1 or is future-inextendible and hence crosses t=-1. Therefore c meets Sigma_2. This proves Cauchyness.

## Dynamical corollary

Assume the same deterministic coupled field theory in both spacetimes, with fields preserved by h, and assume both are maximal globally hyperbolic developments in a regularity category with geometric Cauchy uniqueness. The neighborhood isometry around Sigma_1 identifies the full induced initial data, including extrinsic curvature and field normal derivatives. The geometric uniqueness theorem then makes their developments globally isometric as developments of those data.

If the whole existing-realm comparison also includes b_i and the observer tangent with a continuous smooth extension of h to those marks, the global isometry preserves those marks and hence every well-defined future geodesic proper-time reading. Matching the open U alone should not silently be called matching the marked event; include that boundary/germ requirement explicitly.

For the bow-tie realm E_i=M_i\(J^+(b_i)\{b_i}), a realm isometry that preserves its manifold structure, fields, time orientation and marked b restricts to the hypothesized onto isometry of U_i. Thus a same-whole-bow-tie/different-future counterexample cannot exist under these deterministic MGHD hypotheses. This is a rigidity result, not merely a failure to construct an example.

## Proof status and cautions

The geometric proof's Cauchyness argument must be reviewed carefully, especially continuations at the excluded boundary and inextendible tails. A simpler sufficient statement, requiring Sigma_1 and its image to be Cauchy explicitly, follows immediately from standard Cauchy uniqueness even if the stronger geometric lemma fails.

The dynamical premise is not inferred for every matter theory or regularity. The standard vacuum MGHD theorem supplies one instance; a coupled Einstein--scalar application requires its corresponding wellposedness/uniqueness theorem. Non-GH extensions beyond a Cauchy horizon, stochastic evolution, or insufficient field/normal data fall outside the corollary.

This does not establish current existence of future events. Mathematical determination by existing data and ontological existence are different claims. Nor does it show that the physical world is in this deterministic smooth class.
