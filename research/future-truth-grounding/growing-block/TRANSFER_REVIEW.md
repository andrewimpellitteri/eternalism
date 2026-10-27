# Transfer review: wave and closed-dust examples against BST

**Scope and source.** Independent bounded check of the coordinator's `relativistic-branching/RESULT.md`. I checked the algebra/order arguments and the original publisher PDF of N. Belnap, T. Müller, and T. Placek, “New Foundations for Branching Space-Times,” *Studia Logica* 109 (2021), 239–284 (published online 2020), DOI 10.1007/s11225-020-09905-2, especially Definition 1 and Definition 2, pp. 243–244, and the explanation on pp. 244–245. The publisher's original PDF is https://link.springer.com/content/pdf/10.1007/s11225-020-09905-2.pdf. This is a targeted definition check, not an audit of the paper's translation theorems.

## Analytic wave example

The example is correct as stated. For (\phi_1(t,z)=f(t-z)),

\[
(\partial_t^2-\partial_z^2)\phi_1=f''(t-z)-f''(t-z)=0.
\]

For every point of the strict chronological past of (b=(0,0)), (t<-|z|), which implies (t-z<0) (for (z<0), use (t-z<t+|z|<0); for (z\ge0), it is immediate). Since (f) is supported in ((1,2)), both fields vanish on all of (I^-(b)). At (x=(3/2,0)), the second field is (f(3/2)>0). On the slice (t=-1), its nonzero data occur for (-3<z<-2); the data are smooth and compactly supported, hence have finite standard wave energy. This is compatible with uniqueness from complete Cauchy data: the two solutions have different data on that Cauchy slice, despite agreeing on (I^-(b)).

The result therefore supports the narrow mathematical point that deterministic Cauchy evolution does not imply uniqueness from restriction to one event's entire strict causal past. It does not establish that these solution alternatives are ontologically open, or that they are branches in BST. The coordinator's caveat on that distinction is appropriate.

## Closed dust: no common future

The proof is valid for the specified spacetime and causal order. With conformal metric
\[
g=a(\tau)^2(-d\tau^2+d\Omega_3^2),\qquad 0<\tau<2\pi,
\]
positive conformal scaling preserves causal curves. A future causal curve from ((\tau_0,Y)) to ((\sigma,Z)) must satisfy (d_{S^3}(Y,Z)\le\sigma-\tau_0): the spatial path length cannot exceed the elapsed conformal time. For simultaneous antipodes (Y,-Y) at (	au_0=3\pi/2), a common future ((\sigma,Z)) would therefore imply
\[
\pi=d(Y,-Y)\le d(Y,Z)+d(Z,-Y)\le2(\sigma-3\pi/2).
\]
But every event in (M) has (sigma<2\pi), making the right side strictly less than (pi). Thus no common causal-future event exists in (M). The same argument works for any (	au_0\ge3\pi/2) still inside the spacetime; at the endpoint itself there are no events.

The inference to BST is valid under the stated literal transfer contract. Original Definition 1 (p. 243) calls (D\subseteq W) upward directed iff every pair (x,y\in D) has a common upper bound (z\in D). Original Definition 2 (pp. 243–244), item 2, defines a history as a set maximal with respect to directedness. Consequently every history is directed. If the whole event set and causal precedence order of this dust spacetime were order-isomorphic **onto** a BST history, the two antipodal events would have a common upper-bound event in that history; surjectivity and order preservation would map it back to a common causal-future event in (M), contrary to the inequality. This proves that the entire (M), with this order, cannot be represented as one history by an onto order isomorphism.

A useful precision: this does not rule out an order embedding of (M) as a proper subset of a larger history, because the larger history could contain an upper bound outside the image. Nor does it rule out regional or otherwise altered representations. The coordinator's phrase “identified order-isomorphically with one history” should be read in the onto, full-event-set sense; making that explicit prevents the argument from being overstated.

## Limits and a repair caveat

The finding is a failure of one literal structure-preserving transfer, not a contradiction in BST or a physical claim of indeterminism. The source itself distinguishes a single spacetime's physical evolution from BST's modal structure for alternative spacetimes (Introduction, pp. 241–242), and says BST92 is not itself a theory of physics (p. 241). Nothing here entails that BST is impossible or that the dust model is physically indeterministic.

One proposed repair in the coordinator result needs a qualification: adjoining only an ideal final event as a common upper bound may restore pairwise directedness, but it introduces a maximal element. Definition 2, item 3, expressly requires that (W) have no maximal elements (p. 244). So that single addition does not by itself produce a model satisfying the cited common-BST definition. A more elaborate extension might avoid maximality, but would require a newly specified order and representation contract.

**Verdict:** both mathematical examples check out. The dust argument establishes the narrow no-onto-order-isomorphism result. Keep its target explicit (the complete event set with its physical causal precedence identified with one BST history), and do not generalize it to BST's consistency, viability, or physical indeterminism.
