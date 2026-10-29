# Coordinator review of Claude's screening addendum

28 October 2026. Read SCREENING.md and current RESULT.md in full; ran check.py. No edits to Claude-owned files, claims or commits. This is an independent analytic review; the separate screening-review worker is still pending.

## Overall disposition

Lemma 1 is correct. Theorem 2's set-theoretic screening result is credible and its construction works with the weak achronal Cauchy-surface convention; clarify that convention or use a smooth replacement. Theorem 3(a)'s causal-convexity, marked-past transport and endpoint argument look sound on inspection. Theorem 3(b) remains conditional on a genuinely unverified localization premise, with an additional applicability point below. Do not yet promote it to an established coupled-GR rigidity theorem.

## Finding 1: causal screening is not a necessary boundary for physical determination

SCREENING.md lines172--188 call this a dividing line inside the existing base and say 'the line falls at D_pot'. Theorem2 proves a line for the specially defined geometric screening predicate, not for physical determination in every smooth field theory.

Concrete test: remove one interior point x from the potential realm W, leaving R=W minus {x}. Smooth metric and matter data agreeing on R extend to agreement at x by continuity. If agreement on W suffices to determine the future under the proposed rigidity theorem's hypotheses, then agreement on R suffices too. Yet Theorem2's exact set-inclusion test can fail for R because a chosen causal curve intersects a chosen slice only at the missing point. No actual freedom to change a smooth field at that isolated point follows.

This is not a counterexample to Theorem2. It is a counterexample to reading its minimal SCREENING set as the minimal physically DETERMINING set. The last classification row already partly recognizes the distinction; the philosophical prose should preserve it too. Replace 'the dividing line exactly' with 'the geometric screening boundary; sufficient for physical determination under the additional uniqueness premises'.

For this puncture test use a fixed common spacetime/realm identification and an interior x; do not claim that every abstract isometry of punctured realms automatically extends. The point is already decisive for the information-base/minimal-data interpretation.

## Finding 2: Theorem3(b)'s localized premise has not yet been established or fully matched to its use

Lines88--95 explicitly mark L unverified. Lines130--134 then apply it to h(K1). Part(a) proves that h(K1) is a smooth acausal partial hypersurface and screens the marked future. It does not prove that it is an open subset of a GLOBAL Cauchy surface in M2, as L is presently formulated.

A general noncompact spacelike acausal partial hypersurface need not extend to a global Cauchy surface: in 1+1 Minkowski space, t=sqrt(1+x^2), x in R, is spacelike and acausal but not Cauchy, and cannot be enlarged to a Cauchy hypersurface while retaining that entire graph. Compact smooth extension results do not settle a noncompact h(K1). This is not a counterexample for this PARTICULAR h(K1); it identifies an inference that still needs proof or a stronger appropriately sourced localization theorem for partial hypersurfaces.

Two routes: prove h(K1) lies in an appropriate target Cauchy slice; or formulate/prove localization for these partial data without that requirement. In either case verify that D_M(K) is maximal as a development of the RESTRICTED data, not merely globally hyperbolic with K Cauchy. Ordinary full-data MGHD uniqueness alone is not a citation for that stronger sentence.

Until then, part(b) is an explicit conditional proposal. The classification must retain that condition, the coupled-matter category, and the observer-germ requirements.

## Finding 3: final philosophical universal is too strong

Lines203--207 conclude that no justification phrased in terms of the future can select the bow tie over potential. The demonstrated statement is narrower: points in the surplus have no causal route to b's OWN future, and are redundant for this screening criterion. Other causal-network, modal, composition or cross-standpoint principles have not been excluded. Similarly, the surplus beyond H lacks justification by THESE TWO specified potential rules, not by every possible causal or persistence principle.

The pointy row also supplies existential counterexamples in named classes, not a theorem that pointy realms fail to determine the future in every deterministic model/theory. Keep that quantifier explicit. The scattering pair still has its classical-axis regularity gate; the thin-shell Vaidya construction still has its stated matter/MGHD limits. Do not promote either to a finished smooth coupled theorem by citing its folder.

## Convention issue in Theorem2: fixable, not a refutation

The boundary of I^-(x) union I^-(Sigma_c) can contain null segments. Thus it is not acausal and may meet one inextendible causal curve more than once. It IS a Cauchy hypersurface under the achronal/every-inextendible-TIMELIKE-curve-once convention used by Bernal--Sanchez, which explicitly allows nonacausal Cauchy surfaces. The proof separately supplies the causal interception needed for screening and chooses a timelike continuation to avoid additional boundary intersections in its omitted-point witness. State the convention explicitly.

If the intended quantifier only ranges over smooth spacelike/acausal Cauchy surfaces, a repair is available. For x strictly before b choose a Cauchy temporal level through x. For x spacelike to b, extend the finite acausal set {x,b} to a smooth spacelike Cauchy surface using Bernal--Sanchez Theorem1.1 plus its disconnected-submanifold extension (Remark4.14). For x=b choose a smooth Cauchy surface through b. Such a surface avoids the strict future of b and the causal curve through x meets it only at x. Primary theorem checked selectively below; this is a proposed replacement argument, not an edit to the draft.

## Confirmed calculations and older limits

check.py reproduces the horizon thresholds, Vaidya radial closed form/integration and 360/360 sampled flat-slab checks. This is reproduction, not independent proof or cosmological parameter validation. Flat-slab threshold agrees algebraically with the independently reviewed coordinator formula. Vaidya's global solution/matter assumptions remain conditional. The restricted-body and fusion clauses are hypotheses, not a fully reconstructed author semantics; chapter9 expressly makes loc non-existence-entailing.

## Sources and depth

Bernal--Sanchez, arXiv:gr-qc/0512095v1 (15 Dec2005), full text selectively read: abstract, Theorem1.1, definitions in section2 and Remark4.14. https://arxiv.org/html/gr-qc/0512095 . It explicitly distinguishes nonacausal Cauchy surfaces and smooth spacelike extensions. This supports the convention clarification and finite-point smooth repair, not premiseL. Sbierski v3 clauses remain in the coordinator source register; they establish the vacuum full-data theorem, not the localized coupled statement now needed.

## Recommended status

- Accept Lemma1 and the screening characterization at its stated geometric scope, with the Cauchy convention clarified or the smooth proof substituted.
- Retain Theorem3(a) as a reviewed geometric argument, subject to the separately commissioned review; no counterexample identified in this inspection.
- Keep Theorem3(b) unaccepted pending premiseL and its target-slice applicability.
- Narrow the philosophical prose as above. This work sharpens the research question; it does not establish an ontology or a full new physical underdetermination boundary.
