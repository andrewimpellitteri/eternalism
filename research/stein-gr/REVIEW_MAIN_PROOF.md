# Adversarial review: proof of Theorem thm:main (research/stein-gr/main.tex)

Scope: Lemmas R, E, B, C, the construction of M', Lemmas D and F, eq:transfer, the proof of (a) and (b), and the use of Theorem thm:flat.
Read depth: full text of main.tex. I checked MS (gr-qc/0609119), Bernal-Sanchez (gr-qc/0512095) and Clifton-Hogarth (ch1995.txt) against the cited items. I did all verification by hand. No computation was run.

## Verdict: sound with fixable gaps

The architecture is correct: pass to a tubular chart, cut off to a flat auxiliary globally hyperbolic M', use (LC) on a self-determined region, then run the chain w -> x -> b -> v using (CB) and (T), then detour through a flat slab. I found no fatal conceptual error and no failure of the logic of (a) or (b). I found one construction as written that is inconsistent (F1) but is repaired by a one-line change. I found one citation applied outside its stated scope (F2). The remaining items are incomplete case analyses and unstated verifications.

## A. Errors that must be corrected (mechanical, but the text is wrong as written)

### F1. Tube cut-off is impossible as stated (Lemma B / "Constants and the auxiliary spacetime")

T_rho = {|t|<rho, s in (-1,L+1), |y|<rho} has the same s-range for every rho. The paper then asks chi = 1 on T_{2r} and supp chi inside T_{3r}.

- Closure of T_{2r} contains points with s = -1 and s = L+1. These are not in the open set T_{3r}. So chi = 1 on T_{2r} and supp chi inside T_{3r} cannot both hold.
- The same defect hits Lemma D(i). A boundary point of T_{2r} at the s-end has a vertical escape path that ends at the end of the curve. That end is not controlled by the cone estimate, and the point (0,-1,y) is not clearly outside B_0 within the controlled region.
- Independently, the constant r <= 1/2 allows 3r = 1.5 > 1, so even the t- and y-ranges can exceed the s-margin.

Repair: define T_rho = {|t|<rho, -rho<s<L+rho, |y|<rho}. Extend c to [-r_0, L+r_0] (or any fixed margin larger than 3r), and require r < min{r_0/3, ...}. With this:

- T_{2r} is relatively compact in T_{3r}, so chi exists and M' is fine.
- The vertical escape from an s-end point of dT_{2r} ends at s = -2r or L+2r. That is outside B_0, since B_0 has s in [-r/2, L+r/2]. So the s-ends of the tube, which you asked about, are handled by the vertical case.
- A lid point moving outward at speed mu/2 stays in T_{3r}: it needs |y| <= r/2 + mu r < 3r.
- Lemma F is unaffected. It only uses |y| >= 3.83r > 3r and |t| > 3r.

### F2. Bernal-Sanchez Thm 1.1 / Rem 4.14 are not stated for 0-dimensional H (Set-up)

BS Thm 1.1 is "H compact spacelike acausal m-submanifold with boundary". The convention in section 2 is that submanifolds are connected. Remark 4.14 only removes connectedness.

- A two-point set {x,b} is a 0-manifold. It is neither explicitly included nor excluded. The proof sketch (smoothing a hypersurface G_1 extending H) is dimension-agnostic, but I would not rely on it.
- The item cited is therefore not literally the item used.

Repair: let H = D_x union D_b, two small closed spacelike 3-discs through x and b.

- Take them so small that D_x union D_b is acausal. Spacelike separation is an open condition, and causal diamonds around x and b shrink to the points.
- Each disc is acausal in a small convex neighbourhood.
- This is exactly Thm 1.1 plus Rem 4.14 (non-connected H) as stated.
- Alternatively, cite the statement for general m after checking Sect. 4.

The paper uses only that a smooth spacelike Cauchy surface S contains x and b, and S is connected because M is.

## B. Gaps that do not affect truth but are not proved in the text

### G1. Lemma D(i): t(q) > 0 and the choice of q

"Every q in dT_{2r} with t(q)>0" is used for the crossing point of a past-directed curve from p in D^+. That t(q)>0 is not argued. It is true if q is chosen as follows:

- Let sigma_1 be the first point of Sigma met by the curve.
- Let q be the last point of dPhi(T_{2r}) before sigma_1.
- Then after q the curve stays in the tube. There t is strictly increasing along future-directed causal curves, so t(q) > 0.
- Strictness holds because sigma_1 is not in dT_{2r}.
- The part of the curve from p to q misses Sigma by choice of sigma_1.

Also state the fact "t>0 implies the point is in I^+(S), t<0 implies it is in I^-(S)". This holds because Phi(t,p) lies on the normal geodesic from a point of S and S is acausal. It is not needed that S meets the tube only in {t=0}.

### G2. Lemma D(ii): incomplete case split

The split into "leaves T_{2r}" and "never leaves" is not exhaustive and not correct.

- A past-inextendible g'-curve may cross t=0 (outside Sigma') and then exit. The escape path there would start at t(q)<0, which is not the setting of the stated escape path.
- The correct split is by the first of {first crossing of t=0, first exit from T_{2r}}.
- The case "never leaves" is vacuous. Inside T_{2r}, t is bounded and the speed is bounded, so the image curve converges in the closed tube. A curve that converges in the closed tube would be extendible in M, and in M' because the closure is in the domain of Phi.
- So an inextendible curve must leave. It leaves either after crossing t=0 outside Sigma' (use that crossing) or before (then t>0 at the exit, and use the escape path).
- The reverse inclusion needs the same split in M, with the same remarks about extendibility.

### G3. Lemma D(iii): connectedness of N and interior statements need one more sentence

All the geometric content is correct. I checked the following.

- The comparison D_{eta_lambda} subset D_{g'} subset D_{eta_mu} is the right way round. eta_c has null speed c, and mu<1<lambda.
- x and b lie in the relative interior, at distance r/2 from the complement of B_0, so they lie in int D_{eta_lambda}.
- A point (t,p) of int D with t != 0 has dist(p, B_0^c) > 0, so p is in int B_0.
- The vertical segment from (t,p) down to (0,p) lies in I^-(q) intersect I^+(Sigma'), which is an open subset of D^+. So it lies in int D. int B_0 is convex.

The paper should add the sentence: "I^-(q) intersect J^+(Sigma) is contained in D^+(Sigma) by acausality". The paper uses this inclusion already but only attributes it to "the other cases".

The proof of causal convexity of D(Sigma) in (iii) is correct. I checked the mixed case, the case D^+ with D^-, and the vacuous cases.

### G4. Lemma F is stated for a single detour but used twice, and its proof is a recipe

(b) uses a time-reversed detour from x'=(4r,0,0,0) to b'=(-4r,L,0,0). Lemma F states only (w,v).

Also, the proof says "repeat the argument of Lemma D" without checking the following:

- the thin slab Sigma'' around the curve must have its domain of dependence inside a neighbourhood U of Sigma'' that is disjoint from closure T_{3r}. This needs delta (width) small relative to dist(curve, closure T_{3r}) > 0, which is true but unstated;
- the escape path from the lid of U to H minus Sigma'' must be eta-timelike and, being in the flat region, g'-timelike. Tilting by slope a=8r/L is harmless since a < 1/lambda;
- H = {t = -4r + (8r/L)s} is Cauchy for g'. The proof is: t - f(s) is strictly increasing along causal curves, f(s)=-4r+(8r/L)s, and |Delta f| <= a lambda |Delta t| < |Delta t| because a lambda < 1. It is not stated; "spacelike and Cauchy for eta and for g'" is asserted only;
- N'' = int D(Sigma'') is connected, because it deformation-retracts along H-normal or vertical segments to the relative interior of a thickened embedded arc;
- w, v in the relative interior of Sigma'' means the slab extends past the arc's end points.

Repair: state Lemma F in the form "for any pair (p_-, p_+) and any graph hyperplane H with slope < 1/lambda that avoids closure T_{3r}", and add the above verifications. The numerical facts I checked are all correct:

- |t|<=3r implies s/L in [1/8,7/8];
- there |y| >= 10 r sin(pi/8) = 3.83r > 3r;
- hence the curve is at positive distance from closure T_{3r};
- w, v are g'-spacelike since L > 8 lambda r;
- w << psi(x) and psi(b) << v via vertical segments, which are eta_mu-timelike and so g'-timelike by Lemma C.

### G5. Lemma R: wording

- "V a convex normal neighbourhood that is causally convex in M" conflates two things. What is needed is a convex neighbourhood U, and a causally convex V inside U containing b. MS Prop 2.10 describes causal relations "in U regarded as a spacetime", and MS Rem 2.12 transfers them to V and then M. The conclusion q_eps << b_1 should be read in U, then in M.
- "the connecting vector stays future-directed" needs one line: exp_{q_eps}^{-1}(b_1) is continuous in eps. It tends to u, a non-zero future causal vector (u != 0 since b_1 != b), and timelike vectors near a non-zero future causal vector are future-directed.
- Also note b_1 != b because M is causal (no closed causal curves).
- The world-function claim is correct: nabla_q sigma at q=b equals -u, so d/d eps of 2 sigma equals -2 g(u,a). If g(u,u)=0 the expansion is negative for small eps>0; if g(u,u)<0 it is already negative. a spacelike with g(u,a)>0 exists for any non-zero u.
- q_eps is spacelike to b because 2 sigma(q_eps,b) = eps^2 g(a,a) > 0 (MS 2.10).

### G6. Lemma B: closed tube and the extension of c

- c is declared on [-1,L+1] with unit speed. An embedded extension of length 1 on each side may not exist (the arc might hit itself). Only some margin delta_0 > 0 is needed. Replace "1" by delta_0 and require 3r < delta_0.
- The first-order estimate ||Phi^*g - eta|| <= K(|t|+|y|) is right. It follows because at (t,y)=(0,0) the metric is exactly eta (g_tt=-1, g_ti=0 by Gaussian normal form, and the spatial block is the identity because (e_1,e_2,e_3) is h-orthonormal and sigma_*(d_s,d_y) = (e_1,e_2,e_3) on c).
- Orientation (n,e_1,e_2,e_3) positive makes Phi orientation-preserving, and d_t -> n makes it time-orientation-preserving.

## C. Items I checked and found correct

- **Lemma C.** The inequalities, the thresholds, the signature argument (a negative vector plus a 3-dimensional positive-definite subspace, and nondegeneracy from ||h - eta|| < 1) and the stability under convex combination are right. The orders of the constants (mu, lambda, epsilon first; then r from K) have no circularity.
- **M' globally hyperbolic.** The bound |d(s,y)/dt| < lambda together with monotonicity of t shows every inextendible causal curve meets each level of t exactly once; hence the levels are Cauchy surfaces and MS Thm 3.75 applies. The argument that t cannot have a finite limit uses completeness of R^4 (bounded spatial speed).
- **eq:transfer.** The chain via two morphisms N -> M and N -> M' is correct once Lemma D holds.
- **Lemma E.** The set of points spacelike to z is open because J^+(z) and J^-(z) are closed. "S open" and "complement open" are both correct; the connectedness argument is right. The R x S^3 example is correct: points spacelike to b=(0,p) satisfy |t|<d(p,.)<=pi, and to x=(3pi,p) they satisfy |t-3pi|<=pi, so none exist.
- **Part (a).** The chain w B psi(x), psi(x) B psi(b), psi(b) B v uses (CB) in the right direction (the earlier point is the one that has become). Transitivity gives w B' v, and Lemma F plus Theorem thm:flat give a spacelike pair in B_Mink, a contradiction. The J^+ case reduction via Lemma R is correct: e << x gives e B x, then x B b gives e B b by (T), and e is spacelike to b.
- **Part (b).** The reversed chain psi(x) << x', b' << psi(b), x' B' b' (universal on the flat detour), then (T) is correct. Combined with Lemma E and (T), it gives universality of B_M. The dichotomy at the end of thm:main follows.
- **Theorem thm:flat.**
  - CH Theorem 1's proof (pp. 365-367, text lines of ch1995.txt around Theorem 1) uses only b-preserving spatial rotations, boosts and translations. Case (1) uses a rotation and a boost about b and then translations. Case (2) uses a point e in I^-(a) spacelike to b. Case (3) uses the rotation, boost and translation action on the null cone.
  - Reflections are not used, and CH remark so at the end (the text near "Theorem 1 does not exploit the spatial reflection symmetry").
  - CH's formulation of definability is invariance of B under the full time-orientation-preserving metrical automorphisms, which includes reflections. The paper's use of the proper orthochronous subgroup is therefore a (valid) weakening of the hypothesis, and the argument of the proof uses only that subgroup. The paper's justification is correct but should say explicitly that this is a weakening whose adequacy rests on reading CH's proof, not on CH's statement.
  - CH's (reflexive) convention for I^- matches the paper's.
  - Automorphisms of Mink in GH: proper orthochronous Poincare maps are surjective isometric embeddings preserving orientation and time-orientation, so (LC) gives their invariance.

## D. Citation check

| Cited item | What it says | Use in paper | Status |
|---|---|---|---|
| MS Prop 2.10 | Causal relations in a convex neighbourhood U (regarded as a spacetime) are read from exp_p^{-1} | Lemma R | OK, but applies to U, not M (see G5) |
| MS Remark 2.12 | Causal convexity of V implies <=_U restricted to V equals <=_V; arbitrarily small causally convex V exist in convex U | Lemma R | OK |
| MS Prop 2.31 (i) | p<<r<=q implies p<<q | Lemma R, Lemma D(iii) | OK |
| MS Prop 2.17 | Closure/interior of J^+ and I^+ | not used in main proof | n/a |
| MS Def 3.63 | Definition of causal simplicity (causal and J^+(p), J^-(p) closed) | Lemma E ("global hyperbolicity implying causal simplicity") | Misattributed. The implication GH implies J^+(p), J^-(p) closed is MS Prop 3.71 (after Def 3.70); Def 3.63 only defines causal simplicity. Cite Def 3.70 + Prop 3.71 |
| MS Thm 3.75 | GH iff there is a Cauchy hypersurface | M' globally hyperbolic | OK |
| MS "Sect. 3.11" | Def 3.70: causal + compact J^+(p) intersect J^-(q) | Lemma D(iii) (N globally hyperbolic) | OK |
| MS Thm 2.30 / Prop 2.31 | Used in the other theorems, not in the main proof | | n/a |
| Bernal-Sanchez Thm 1.1 | Compact spacelike acausal m-submanifold with boundary extends to a spacelike Cauchy hypersurface | Set-up | Hypothesis does not literally cover a 0-dimensional set; see F2 |
| Bernal-Sanchez Rem 4.14 | Non-connected acausal H handled by summing the h_G for each component | Set-up | OK for several components of a positive-dimensional H |
| CH Theorem 1 (p. 365) | B definable and transitive and CB gives I^-, J^- or U | Theorem thm:flat | OK; rotations/boosts/translations only |

## E. Presentational points

- The quantifier order "fix mu, lambda, epsilon; then r (depending on K, which depends on c)" should be written once explicitly as an order of choices.
- "Phi(T_{2r})" and "T_{2r}" are used for both the open tube and its closure; separate the two where the boundary is used (Lemma D(i)).
- The sentence "The argument uses only that {t=0} lies in a Cauchy surface of each ambient spacetime" is true, but Lemma D(i) also uses that Phi is injective, so that points of {t=0} with (s,y) outside B_0 are not in Sigma. State this.
- Statement of Lemma F should list what is proved: acausality of the slab in M', D_{M'}(Sigma'') = D_Mink(Sigma'') and that this set lies in the flat region.

## F. Does (b) give universality?

Yes. For every spacelike pair in every M, (b) yields x B_M b by the chain through the flat detour. Lemma E then connects arbitrary points by finite spacelike chains, and (T) gives B_M = U_M. No further hypothesis on M beyond membership in GH is used. The only external input is B_Mink = U.

## G. Summary of required changes, in priority order

1. F1: shrink the s-range of T_rho with rho and require 3r < margin of c (the original inequality r <= 1/2 is wrong).
2. F2: apply Bernal-Sanchez to two small discs, or verify the 0-dimensional case.
3. G2, G1: repair the case split in Lemma D(i) and D(ii).
4. G4: state and verify the detour lemma in both orientations, including that D(Sigma'') avoids closure T_{3r}.
5. G5, G6, citation fixes (MS Def 3.63 -> Def 3.70/Prop 3.71).
