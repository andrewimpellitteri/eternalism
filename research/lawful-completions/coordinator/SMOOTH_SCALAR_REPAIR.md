# Corrected smooth Einstein–scalar common-development application

29 October 2026. Coordinator source check and correction of worker submission 779cc91. Ordinary smooth GR; distinct from the reduced low-regularity scattering construction. Bounded corollary under the existing screening-transport hypotheses. Independent review of this integration pending; no novelty or ontology claim.

## Preserve the useful source contribution

Ringstrom's author correction note, Existence of a Maximal Globally Hyperbolic Development, https://people.kth.se/~hansr/mghd.pdf, was downloaded and directly checked. SHA-256 7282fbc43d0b22eb26fb7344c4e241eb945ddcaf5853ad8a833224deeb72f155. It is an undated primary author note, not a new journal publication.

- PDF p.5, Definition 2.1: smooth initial data on an n-manifold, with induced metric, second fundamental form, scalar value and normal derivative; no completeness or compactness requirement is imposed there.
- PDF p.6, Theorem 2.4 and Definition 2.7: respectively a common SMALLER development and metric-and-scalar-preserving embeddings. The smaller development alone is insufficient for our application.
- PDF pp.13–15, Definition 6.1, Lemma 6.4, Definition 6.7, Lemma 6.10: build the common larger development, preserving the scalar along with the metric. Lemma 6.10 gives the larger GHD containing both provided the glued space is Hausdorff.
- PDF pp.24–25, Lemma 10.1: the glued common extension is Hausdorff. Together these supply the required containing-both form, with compatible initial-data embeddings.

Read depth: selected statements, the gluing definitions and Lemma 6.10 proof, plus the opening/structure of Lemma 10.1 proof. Not a line-by-line reproof of all causal-boundary machinery in sections 7–10. The note identifies its local existence/uniqueness inputs with the book's Theorems 14.2/14.3; the book's interior proof pages were NOT directly accessed by the coordinator.

For V=0 the note uses Ric(g)=d(varphi) tensor d(varphi) and wave_g varphi=0. Setting varphi=sqrt(2) phi gives our Ric(g)=2 dphi tensor dphi normalization. Thus the common larger-development result is field-preserving for the massless system at issue, after this explicit normalization change.

## Correct the geometric setup

Keep K_1=Sigma_1 intersect W_1 and K_2=h(K_1). Do NOT replace K_1 by the full Sigma_1 or assert that an earlier entire Cauchy slice lies in I^-(b_1). Achronality, spacelikeness and intrinsic boundarylessness pass through h; ambient acausality uses the separately verified causal convexity of W_i.

The worker demanded ambient closedness of K_2 and treated an open disk as an obstruction. That necessity claim is false. The open unit spatial ball at t=0 in Minkowski has the open causal domain |t|+||z||<1 and is Cauchy there. Ambient closedness is therefore not necessary for the domain property used here.

A directly checked source statement is Steinbauer, arXiv:2206.05939v2, 14 November 2022, section 3.4, immediately before Proposition 3.7: for any acausal topological hypersurface S, its causal Cauchy development D(S) is open and globally hyperbolic. Its preceding definition uses inextendible CAUSAL curves. This is a primary author's pedagogical survey of standard geometry, not the original proof. The statement is unnumbered; do not invent a theorem number.

The S-Cauchy property also has a short verification in this setting. A past-inextendible ambient causal curve from q in D^+(S) meets S by definition. Its segment before meeting S stays in D^+(S): if a point on the segment had a past continuation avoiding S, concatenate it with the remaining segment to q to contradict q's domain property. Acausality prevents the q-to-S segment from meeting S twice. Thus an intrinsic inextendible curve in the open D(S) cannot stop at a boundary before reaching S: the ambient extension segment to S remains in D(S). Apply the time-reversed argument from D^-(S). Every inextendible curve in D(S) meets S exactly once. Smooth S therefore supplies the required smooth Cauchy data.

A fully formal presentation should make the ambient causal-curve extension step explicit (a maximal extension in M of the given one-sided curve); it is the standard smooth causal-curve extension argument. No requirement that S extend to a global ambient Cauchy surface, be complete, or itself be closed in M is introduced.

The worker's alternative Lemma D is also unusable: its chosen w in I^+(b_2) is outside W_2, so h^(-1)(w) is undefined. No part of this correction relies on that lemma.

## Correct the matter matching explanation

An isometry of OPEN realms already matches the induced metric and extrinsic curvature on K. It is wrong to invoke stress-energy's failure to determine extrinsic curvature as the issue in this comparison.

The genuine matter requirement is h^*phi_2=phi_1 on W_1, in addition to metric isometry. Differentiating the field equality and using the matched future unit normals identifies both scalar Cauchy data. Matching only stress tensors leaves additive scalar shifts and sign choices unresolved. No identification across those different scalar data sets is asserted.

## Resulting bounded corollary

Assume the existing geometric screening transport: J^+(b_i) subset D^+(K_i), realm h with the stipulated homeomorphic mark extension, and the matched launch germ as in COMMON_EXTENSION_REPAIR.md. For smooth Einstein–massless-scalar models with field-preserving realm h, every matched geometric and scalar geodesic reading agrees at every finite proper duration defined in BOTH models.

Proof: the domain statement supplies ordinary open GHDs N_i=D(K_i) of their induced data. Keep the connected marked components exactly as in the earlier repair. The corrected Ringstrom common-extension construction embeds both into a common GHD, preserving the field. The earlier full-first-jet comparison along a timelike curve from K_1 to b_1 identifies the marks there. Geodesic IVP uniqueness then identifies matched curves through every common duration, and field-preserving embeddings identify their scalar readings.

This uses no localized maximality claim, no global closedness of K_i and no claimed extension of K_2 to an ambient global Cauchy surface. It does not imply equal survival duration. The constant-scalar clipped-Minkowski example retains the same sharpness. The stronger onto-future result still requires its explicit marked completeness premises.

## Disposition

Retain the worker's field-preserving source chain at its exact read depth. Reject its substitution of Sigma_1 for K_1, asserted closedness necessity, Lemma D, and extrinsic-curvature rationale. This corrects the purported new obstruction and supplies the smooth scalar extension of the bounded vacuum argument. It does not make the reduced LOY class smooth, and it should not be used to upgrade that class by analogy.
