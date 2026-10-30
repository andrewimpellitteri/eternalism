# AGENT_REPORT — lawful-axis-lift-review

29 October 2026. Red-team review of
`research/lawful-completions/coordinator/AXIS_C11_RECONSTRUCTION.md`.
Worker submission for coordinator review — not an accepted result, not a vote.

## Done and files

* Read AGENTS.md, README.md, knowledge/README.md, knowledge/NOVELTY.md, the
  task brief, and the full coordinator document under review.
* Independently verified or refuted every proof obligation of the coordinator's
  finite-order C^{1,1} axis reconstruction, at the L1 (pure analytic),
  L2 (source correspondence), L3 (interpretation) separation the brief demands.
* **Verdict: the analytic argument is correct as an L1 lemma after two required
  repairs; no fatal gap found after deliberate refutation attempts.**
  * REPAIR-N2 (semantic, load-bearing): the hypothesis list must include the
    SSESF equations r_uv = 2mνλ/[(1−μ)r²] and (rφ)_uv = r_uv φ. The parity
    identity φ_ρ(t,0)=0 is NOT derivable from the mass equations alone; a
    counterexample (φ = ρ, lifting to |x| ∉ C¹) demonstrates the gap. The two
    equations are verbatim LOY v1 (SSESF) equations — confirmed against the
    primary text — so the repair is trivial but must be made.
  * REPAIR-N3 (proof gap): the cross-axis Lipschitz claim for E_ij = D n_i n_j
    is asserted, not proved. A complete two-case proof (segment avoids axis ⇒
    fundamental theorem with |Hess| ≤ C; segment crosses axis ⇒ crude bound
    |∇E(x)|+|∇E(y)| ≤ C(|x|+|y|) ≤ 2C|x−y|) is supplied in RESULT.md §5/O12;
    it uses only |∇E| ≤ Cρ and bounded off-axis Hess.
  * REPAIR-N1 (cosmetic): "every term is O(r)" in coordinator §2 — the φ_va and
    λ_a terms are O(r²), the 2r·r_a term is O(r); conclusion unchanged.
* Files: `RESULT.md` (line-by-line verdict table O1–O19, objections, repairs,
  counterexample attempts, limitations), `sources.jsonl` (6 records, schema
  compliant), `verify_checks.py` (pure-stdlib check script), this report.

## Search capability check

* `scholar_search` (mcp, "all" source): **worked** — first query returned
  OpenAlex/arXiv/CrossRef results (used again for prior-work probes). This was
  the one required capability test.
* `exa` fetch (web_fetch_exa / ar5iv): **worked** — arxiv.org/html for the 2016
  LOY paper returned only a stub, so the primary text was fetched from
  ar5iv.labs.arxiv.org (partial, title page through §1.1).
* `serpapi_search`: available but not needed; not exercised.
* `web-search-prime`: not used, per brief instruction.

## Source coverage (see sources.jsonl for exact depths)

* LOY v1 (1605.03893): partial full-text — abstract, metric ansatz, (1.2),
  the full (SSESF) system, Theorem 1.1, (1.7)–(1.9), Remarks 1.2–1.3. Sections
  2–6 and Prop 3.18 NOT fetched: the §4 mixed-derivative/third-order axis
  assertion remains the coordinator's own open gate, and I could not close it.
* Kilgore v1 (2108.13377): abstract + intro only; §7 unread (brief designated
  it "if needed"; the reviewed proof uses no cone theorem, so the warning is
  respected).
* Minguzzi 2014 (1308.6675): abstract-level — anchors the geodesic-uniqueness
  verdict as known methodology for Lipschitz/C^{1,1} connections.
* LeFloch–Mardare 2007, Baumgarte–Rendall 1993: discovery-level context.
* Coordinator document: read in full.

## Verification commands and results

```
cd research/lawful-completions/axis-lift-review
time python3 verify_checks.py     # 14/14 pass, 0.04 s wall (budget 30 s)
```

Checks (all pass): parity algebra X_ρρ = X_tt − 4X_uv; exact μ_ab quotient
formula vs finite differences (rr, tr, tt) to 6 digits; m_a = O(r²) and
m_ab = O(r) axis behavior; E_xx first-derivative closed formula; |∇E| = O(ρ);
|Hess E| bounded off-axis; gradient Lipschitz across segment-crossing pairs
(sup ratio 2.51); Hess no-limit sharpness model (oscillates −2.2…+2.0, bounded);
Hadamard bound |(D_n−D)/ρ| ≤ sup|∂ρ(D_n−D)|; wave-equation-necessity checks
(φ=ρ fails, φ=f(t) passes). Hand proofs in RESULT.md are the primary evidence;
the script only corroborates formulas and models sharpness.

## Strongest contrary evidence / attempted refutations

1. **φ = ρ counterexample** — satisfies every listed coordinator hypothesis
   except the unstated (rφ)_uv equation, and lifts to |x| ∉ C¹. This shows the
   missing hypothesis is load-bearing (OBJ-1). It is a specification gap, not a
   mathematical error: the coordinator's own §3 silently used the equation, and
   it is verbatim in LOY.
2. **D = ρ²sin(log ρ) sharpness model** — satisfies all input-type bounds,
   lifts C^{1,1} with bounded but non-convergent Hessian; confirms finite
   orders cannot be relabelled C² (coordinator's own §6 example, verified).
   Attempted rougher variants to break C^{1,1} itself all fail — the two-case
   proof closes the door (they are excluded by |D| ≤ Cρ², |D_ρρ| ≤ C).
3. **Source-order risk** — LOY Theorem 1.1 (1.9) explicitly bounds only *pure*
   second derivatives of r and (rφ); mixed second derivatives of φ and third
   derivatives of r (including near-axis uniformity) rest on §4/Prop 3.18,
   which I did not read. If that gate fails, the input orders weaken and the
   lemma's hypotheses shrink; the L1 lemma itself still holds as stated.

## Limitations

* L2 depth limited as above (LOY §2–6, Kilgore §7 unread; labeled honestly in
  sources.jsonl). No claim here about what LOY's proofs actually deliver.
* Checks are finite-difference corroboration on model functions, not proofs;
  models satisfy input-type bounds, not the full field equations (that is the
  correct role for a sharpness model, and the analytic proofs are separate).
* Global statements (clock unboundedness on the full quotient, two-sided
  completeness class) are conditional on global inputs not audited here.
* No ontology selected; no smooth MGHD upgrade; no novelty/priority claim made
  (geodesic uniqueness in C^{1,1} is flagged as known methodology; the
  coordinator likewise claims no priority).

## Proposed next tasks

1. Source lane: verify LOY §4 + Prop 3.18 supply uniform mixed φ'' and third
   r-derivatives including the axis, and the global a ≥ 2/3 input (closes the
   conditional parts of O8/O17).
2. Coordinator: apply REPAIR-N1/N2/N3 to AXIS_C11_RECONSTRUCTION.md.
3. Optional: formal (Lean) encoding of the now-supplied two-case Lipschitz
   lemma, the only step whose written proof was missing.
