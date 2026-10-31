# Agent report: lawful-higher-regularity-audit

30 October 2026. Worker submission for independent review; coordinator owns
acceptance. Branch `agent/lawful-higher-regularity-audit`.

## Task

Check the higher-regularity literature (Kilgore 2108.13377, Luk–Oh
2108.13379, published LOY) against the two-sided Luk–Oh–Yang scattering
limits used by the lawful-completions chain: resolve the selected-full-text
vs abstract-level Kilgore scope tension, audit our compact smooth
incoming-profile family against every hypothesis (domain, initial surface,
derivative orders, axis parity, constants/vertex uniformity), check the
published LOY for the Prop 3.18 u-side sketches and the §4 k=0 display, and
give a precise bridge lemma or an explicit hypothesis obstruction.

## Deliverables

* `research/lawful-completions/higher-regularity-review/RESULT.md` — full
  audit: tension resolution, verbatim-anchored hypothesis loci, point-by-point
  obligation table, bridge-lemma statement and status, smooth
  common-development gate disposition, strongest counterexample.
* `research/lawful-completions/higher-regularity-review/sources.jsonl` — 4
  schema-compliant records with exact versions and TeX locators.
* `research/lawful-completions/higher-regularity-review/AGENT_REPORT.md` —
  done/files, search capability check, verification commands and results,
  limitations, unresolved questions, proposed next tasks.

## Headline findings

1. Footnote 1 of Kilgore v1 (TeX line 136) verbatim excludes direct control
   of the LOY past-null-infinity scattering spacetimes; the abstract-level
   suggestion is refuted at theorem-statement level: Theorem 3.1's data
   hypotheses (Definitions 2.5–2.6) fail for our family — under the literal
   I⁻ display for every cone (the scattering normalization
   `lim_{u→−∞}2∂_v(rφ)=Φ(v)≠0` violates it), and without a common bound for
   the translated C₁ weighted norm; constants are data-dependent, so no
   uniform all-order estimate follows.
2. The missing bridge lemma is not supplied by the literature. The in-project
   conditional supply remains the smoothness bootstrap chain at its stated
   finite-region scope, pending integrated review; it is not a Kilgore
   application and does not give Luk–Oh's (D1)–(D8) package.
3. Smooth common-development gate: stays conditional exactly as recorded in
   SMOOTH_FINITE_CONTROL; no unconditional source route; the Luk–Oh route has
   the additional, unverified (D2)–(D8) gap.
4. Published LOY (Ann. PDE 4:3, 2018, DOI 10.1007/s40818-017-0038-4):
   paywalled (303 → idp.springer.com; no OA copy on author pages). v1-only
   verbatim results recorded instead: u-side halves of Prop 3.18 are an
   explicitly labeled "Sketch of proof"; the §4 k=0 r-derivative display
   contradicts the λ=1/2 gauge. No corrections invented.

## Capability check and compute

`exa.web_search_exa` worked (recorded in lane report). Computational checks:
3 plain-Python verifications, 0.13 s total (caps: 10 s each / 30 s total);
they verify project-side algebra only, never replacing analytic proof.

## Not claimed

No new existence theorem, no bridge lemma, no smoothness or nonsmoothness
theorem, no novelty or temporal-ontology claim. Full limitations and
unresolved questions in the lane AGENT_REPORT.md.
