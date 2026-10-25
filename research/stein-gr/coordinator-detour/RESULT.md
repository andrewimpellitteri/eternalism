# Detour repair: independently checked replacement

25 October 2026. Coordinator follow-up to `tasks/gluing-audit/PROOF_AUDIT.md`,
especially finding F1. This is a disjoint integration proposal; it does not
edit the manuscript or change the gluing task's claim/review status.

## Outcome

Do not apply F1's proposed uniform vertical-descent repair as written.
Vertical descent works at lateral and longitudinal tube boundaries, but at
a positive-time lid point whose spatial projection is inside the initial
slab it reaches that slab. It therefore fails to construct a curve avoiding
the slab. This is a gap in the proposed repair, not a counterexample to
Lemma F or the main theorem.

The accompanying `REPLACEMENT.tex` replaces the distance-neighborhood and
distance-gradient sketch with a product tube in coordinates adapted to the
flat arc. This uses exactly the already-checked local geometry of Lemma D:
vertical escape at the sides, timelike sideways-and-downward escape at the
lid, and a two-ambient first-event argument. It also specifies end margins,
the common Cauchy surface and the required compact flat neighborhood.

## Exact negative control for the proposed review repair

In Minkowski coordinates (tau,s,y1,y2), let the initial slab be

    Sigma = {tau=0, -1/2 <= s <= L+1/2, |y| <= 1/2}.

The lid point q=(2,L/2,0,0) of the corresponding outer product tube is
outside the slab. Vertical descent from q ends at (0,L/2,0,0), inside Sigma.
Thus it does not avoid Sigma. This failure occurs even in exactly flat
geometry and has nothing to do with endpoint curvature.

By contrast choose mu=3/4 and tangent (d tau,d s,d y1,d y2)=(-1,0,3/8,0).
Its Minkowski squared norm is -55/64<0. Over coordinate duration 2 it
ends at |y|=3/4>1/2 while remaining within |y|<3. This is the lid escape
used in the replacement. At a longitudinal end s=-2 or L+2, vertical
descent already ends outside Sigma. These are analytic exact checks,
not a numerical verification of the infinite theorem.

F1's diagnosis of a spatial distance gradient as spacelike is also not a
complete objection to the original sketch: that gradient is spacelike on
the sides too, and can be combined with a time component. The actual
obligation is to specify a timelike escape curve that stays in the flat
patch and avoids the initial slab. The product-coordinate proof does so
without assumptions about smooth distance gradients at rounded end caps.

## Why the replacement fits the existing proof

1. Lemma F already establishes that H is Cauchy in both M' and Minkowski.
2. A Lorentz boost makes H horizontal. The two metrics coincide with eta
   on an open neighborhood of the compact arc in H. Extend the arc a little
   at both ends while retaining this property, and reparametrize by arclength.
3. Euclidean normal coordinates of the arc within H straighten it. The
   common spacetime metric in these coordinates is -d tau^2+h(s,y), with
   h(s,0) the identity. It need not have constant components away from the
   arc. Smoothness and compactness give the same fixed inner-cone bound as
   in Lemmas B/C on a sufficiently thin tube.
4. A product slab with transverse radius a/2 and longitudinal margins a/2
   lies strictly inside the product tube of radius 2a. The closure of the
   radius-3a tube lies in the common flat neighborhood.
5. Every relevant shell point has the required escape path. For a lid point
   at tau=2a whose projection is in the slab, outward transverse speed mu/2
   gives displacement mu*a>a/2 and endpoint radius at most a/2+mu*a<3a.
   Its coordinate speed is less than mu, hence timelike for the common metric.
6. The first-exit proof of Lemma D uses just these local bounds and a common
   initial surface that is Cauchy in both ambients. It does not require the
   metrics to coincide outside the tube, or the common coordinate metric
   to have constant coefficients. The t=0/exit tie must remain in the
   initial-surface branch, as in the corrected Lemma D.
7. Transfer, causal convexity, global hyperbolicity, connectedness, and
   inclusion of the two arc points now follow by the same verified domain
   argument. Orientation-preserving coordinates/boosts are available.

The source used in this follow-up still has the distance-gradient sketch
in the proof of Lemma F; that is the sole proposed replacement here.
No theorem statement or locality assumption changes.

## Imported source check closed

The gluing audit flags Bernal–Sanchez as unread. Theorem 1.1 of
arXiv:gr-qc/0512095v1 states the extension of a compact spacelike acausal
submanifold with boundary to a spacelike Cauchy hypersurface. Its discussion
explicitly points to Remark 4.14 for disconnected submanifolds. The current
set-up applies it to two small closed spacelike 3-discs, so it matches the
stated hypotheses. This does not rely on the earlier disputed 0-manifold
interpretation. Read depth: theorem statement and indicated discussion;
not a full independent audit of the smoothing proof.

Source: https://arxiv.org/html/gr-qc/0512095v1 .

## Limitations and disposition

This repairs a proof presentation using the existing Lemma D and its
established local estimates. It is not an independent proof of every
statement in that lemma, a novelty verdict, or an energy-condition extension.
The gluing report should not be accepted wholesale on the strength of its
"no blocking finding" summary: its F1 suggested replacement needs the
correction above. The eta_c family is not simply vestigial either: eta_mu
and eta_lambda are used in the domain comparisons, so deleting the family
definition as suggested in C1 would require preserving those definitions.

The main source is left untouched for the designated integration gate.

## Verification performed

The replacement proof was substituted into a temporary copy of the pinned
manuscript, leaving the shared source untouched. The Codex desktop LaTeX
compiler reported success; the assembled source has no duplicate labels or
unresolved internal references. Exact rational arithmetic confirms the
negative-control witness and the combined escape norm -55/64. Input hashes
and the build result are recorded in verification.json. These checks do not
replace the analytic localization argument above.
