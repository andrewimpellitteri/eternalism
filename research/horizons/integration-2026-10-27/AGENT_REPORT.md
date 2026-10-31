# Horizons draft 4: integration report

Task horizons-reviewed-integration; coordinator codex-horizons-integration.
27 October 2026. User explicitly authorized integration into the paper.

## Outcome

Integrated the independently reviewed ordinary physical mass result, the
norm-controlled O(m²) ambiguity estimate, and concise noisy-record and
finite-cutoff diagnostics into main.tex, with self-contained mathematical
arguments. The ordinary-mass theorem fixes a positive dust amplitude and
chooses the interior target before the small positive-mass interval. The
norm application explicitly uses h_m=a(phi_1-phi_2), all smooth differences
agreeing exactly on the strip-past, and the stated conformal-data budget.

The abstract, introduction, questions, philosophy and conclusion now reflect
those results. Prose separates exact fixing, records and ontic addition;
preserves strong growing-block and eternalist replies; scopes the companion
result to its metric-only/off-shell assumptions; and makes grounding and
appropriate persistence additional philosophical commitments. Selected original
Earman pages are credited; Ellis–Sciama and priority remain unresolved.

The existing title is retained, with date 27 October 2026 (draft 4). The
rebuilt horizons.pdf has 12 pages. CHANGE_MAP.md gives the correspondence to
the reviewed research sidecars and source disclosures.

## Validation and independent review

- Two successful final pdflatex passes after reviewer wording corrections.
  No undefined citations/references, duplicate source labels or overfull boxes.
  One pre-existing underfull bibliography line remains; it has no clipping.
- Seven existing theorem/corollary/proposition statements and their proof
  bodies were compared to baseline 1326b89 and remain byte-identical.
- A separate native mathematical reviewer compared the compressed new proofs
  against both reviewed derivations and found no introduced gap. Its minor
  suggestion to fix a_m>0 explicitly was applied. A rescaled-difference
  clarification was also checked in the final source.
- A separate native philosophy/source-scope reviewer checked the proposed
  replacements, assumptions and source-depth disclosures. Its growing-block
  compatibility wording and explicit Cauchy-uniqueness premise were applied.
  Both reviewers acknowledged final source SHA256
  ff095411f7080b01cf5046ed127c4e73b188c0265e4445c524f0f79822734769.
- All final PDF pages rendered and inspected as a 12-page contact sheet;
  affected proof pages 7–8 and record/philosophy pages 9–10 inspected at
  larger size. No clipped equations, overlapping text or broken references.
  Final contact sheet is layout-contact.png. PDF/source hashes and structural
  checks are in verification.json.
- The sidecar numerical implementations were not changed or needlessly
  rerun: this task checked mathematical and prose correspondence plus the
  actual built artifact. No dependency installs or large runs.

## Files changed

- research/horizons/main.tex
- research/horizons/horizons.pdf
- research/horizons/integration-2026-10-27/CHANGE_MAP.md
- research/horizons/integration-2026-10-27/verification.json
- research/horizons/integration-2026-10-27/layout-contact.png
- research/horizons/integration-2026-10-27/math-review/{MATH_REVIEW,AGENT_REPORT}.md
- research/horizons/integration-2026-10-27/phil-review/{PHIL_REVIEW,AGENT_REPORT}.md
- this report and coordinator workboard records

## Remaining limits

No complete massive fixing classification, uniform mass threshold, detector
stability, physical energy-budget interpretation, interacting/quantum theory
or backreaction result is asserted. No ontology follows from the formal
classification. The selected original Earman reading is not a whole-book
priority audit. Ellis–Sciama target pages remain unread and the recovery
lane did not directly verify Wald's scalar locator. Integration and a clean
build do not close source, originality or circulation gates.

The Stein-GR source, book materials, unrelated user PDFs and unrelated local
changes were preserved. No expert was contacted and no release was made.
