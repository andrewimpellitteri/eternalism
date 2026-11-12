# AGENT_REPORT — screening-review

Task `screening-review`: adversarial review of `research/bowtie-horizons/SCREENING.md`
(Lemma 1, Theorem 2, Theorem 3 incl. premise L). Analytic review only, per brief.
Status: **submitted for coordinator review** (per AGENTS.md, not self-accepted).
Date: 2026-10-31.

## Done / files

- `research/bowtie-horizons-screening-review/RESULT.md` — per-item verdicts with
  reasons, explicit counterexamples, premise-L access gate, recommended repair.
- `research/bowtie-horizons-screening-review/sources.jsonl` — 8 source records
  with depths and limits (contract-compliant).
- `AGENT_REPORT.md` (this file, root).

Verdicts (details in RESULT.md): Lemma 1 CONFIRMED; Theorem 2 (⇐) CONFIRMED
(one gap filled); Theorem 2 (⇒) CONFIRMED only under the Bernal–Sánchez C⁰
Cauchy-hypersurface convention — ∂P is not acausal in general (explicit 1+1
counterexample); NEEDS-FIX = state the convention (alternative smooth-acausal
route needs an uncited avoidance lemma (A)). Theorem 3(a) steps 1–2 CONFIRMED;
step 3 CONFIRMED with a one-line citation fix (via J⁻(J⁺)=I⁻(I⁺)); step 4
CONFIRMED with three completions (tail ⊆ W via push-up; GH-closedness for the
past-endpoint claim; inner continuity of I⁻ proven for compact sets).
Theorem 3(b) conditional logic CONFIRMED (marking step Ψ(b₁)=b₂ verified via
the connected W₁-component through I⁻(b₁) ∩ {t₁ > −1}); premise (L′)
**REFUTED as literally stated** (definitional counterexample: S = hyperbola
t = √(1+x²) in 1+1 Minkowski has D(S) = {t ≥ √(1+x²)}, not an open spacetime;
S lies in no Cauchy hypersurface in either convention) and **not located** in
the literature in any corrected form; replacement premise (L″) (D-agreement)
proposed and shown sufficient; it too is unsourced — Theorem 3(b) stays
explicitly conditional. No counterexample found against Lemma 1, Theorem 2 (⇐),
any Theorem 3(a) step, or (b)'s conditional logic, despite targeted 1+1/2+1
conformal and quotient attempts.

## Search capability check

- `scholar_search` (Openalex): **worked**. Queries: "Sbierski maximal Cauchy
  development Einstein equations"; "\"partial Cauchy surface\" maximal
  globally hyperbolic development uniqueness"; "initial data hypersurface with
  boundary maximal development Einstein domain of dependence uniqueness";
  "Cauchy problem initial data on achronal hypersurface not Cauchy domain of
  dependence development uniqueness general relativity"; "Ringstrom Cauchy
  problem general relativity maximal globally hyperbolic development theorem";
  "\"Lorentzian length space\" maximal Cauchy development non-unique".
- Exa `web_search_exa` / `web_fetch_exa`: **worked**. Identified
  arXiv:1309.7591 (title, versions, Def. 2.1, Thms 2.6–2.8 via ar5iv fetch);
  Bernal–Sánchez gr-qc/0512095 (definition paragraph, Thms 1.1/1.2, Prop 3.6);
  CBG 1969 INSPIRE abstract; partial-surface sweeps (no hits on point).
- `web-search-prime`: **not called**, per brief (quota exhausted until
  2026-11-17); no retry attempted. `serpapi`: not needed after the above
  succeeded.

## Source coverage

Primary (premise L): Sbierski arXiv:1309.7591v3 (full-text, selective sections:
Def. 2.1–2.4, Thms 2.6–2.8, 3.4, gluing discussion) — the key finding is
Definition 2.1 condition 3 (GHD requires the data to embed as a Cauchy
surface), which excludes the partial-hypersurface premise. CBG 1969 (abstract,
INSPIRE). Bernal–Sánchez gr-qc/0512095 (full-text selective: convention,
Thm 1.1 compact-only, Thm 1.2, Prop 3.6, Example 3.4). Ringström 2009: **not
accessed** (access gate recorded in sources.jsonl); scope assessed via
Sbierski §1 and Ringström's 2015 CQG survey (abstract). Peripheral: Wong 2014,
Müller 2404.06428, Eperon–Reall–Sbierski 2019 (abstracts; screened out).
Project files read: AGENTS.md, knowledge/NOVELTY.md, knowledge/README.md,
research/bowtie-horizons/{RESULT,SCREENING}.md,
research/lawful-completions/coordinator/CLAUDE_SCREENING_REVIEW.md.

## Verification commands and results

Analytic line-by-line re-derivation (no installs). Plus one arithmetic sanity
script, run 2026-10-31, all assertions passing:

    python3 /private/tmp/opencode/screening_check.py
    # Lemma1 spot checks: True
    # dP piecewise description: OK   (boundary pieces of P = I^-(x) ∪ I^-(Σ_{-1}))
    # dP ncap J+(b) = empty: True
    # S acausal: True                (hyperbola t=√(1+x²))
    # inside point, all 3 past slopes meet S: True
    # below-S point, past null slope 1 avoids S: True
    # cone-riding timelike curve x=t+1−arctan(t)/2 avoids S: True (slope |x′|<1 verified)

A one-line follow-up re-verified null-relatedness of the ∂P pair
(−0.5, 0.5), (−0.25, 0.75) (the first run's third flag used a mis-written
two-directional conjunction; corrected to one-directional). No other
computation was needed; the hyperbola D(S) computation and the acausal-Σ ⊇ S
impossibility are proven analytically in RESULT.md §6.2.

## Strongest contrary evidence (to the draft)

1. **Theorem 2's test surface ∂P is genuinely non-acausal** — explicit null
   segments in 1+1 Minkowski (RESULT.md §2.2). Under an acausal/smooth reading
   of "Cauchy surface (C⁰ allowed)" the proof of the (⇒) direction fails, not
   merely needs polish. Fix is cheap (state the Bernal–Sánchez convention,
   which the coordinator's earlier review already anticipated).
2. **Premise (L′) is not just unverified — it is ill-formed**: the standard
   GHD definition (Sbierski Def. 2.1(3)) requires Cauchy embedding, and for the
   draft's own example surface D_M(S) is not a spacetime. The uniqueness clause
   additionally fails structurally for partial data (branching at the Cauchy
   horizon; Sbierski's "corresponding boundary points" mechanism). This turns
   the coordinator's Finding 2 into a refutation of the literal statement and
   motivates the (L″) replacement.
3. **Bernal–Sánchez Thm 1.1 is compact-only**, so the draft's first repair
   route (h(K₁) in a target Cauchy surface) is blocked at this generality —
   independently confirmed by my proof that the hyperbola lies in no Cauchy
   hypersurface of Minkowski in either convention (this also corrects a
   subtlety: the naive "every timelike curve crosses the hyperbola" claim is
   false — cone-riding timelike curves avoid it — so the convention question
   needed the sharper argument).

## Limitations

- Ringström 2009 not accessed (no library access): access gate, not a claim
  about its contents beyond secondary descriptions.
- The incomparability/no-maximal-element argument for partial data (§6.3) is a
  construction sketch; the smooth vacuum realization of the handle patch was
  not written out. The definitional refutation (§6.1–6.2) does not depend on it.
- (L″) is proposed, shown sufficient, and argued provable by standard
  local-uniqueness propagation; I did not write the full proof, and no source
  was found. Theorem 3(b) therefore remains conditional — consistent with the
  draft's own honest flagging, but now with a precise replacement.
- Search coverage is targeted, not exhaustive (six scholar queries + Exa
  sweeps); a printed (L′)/(L″) could exist outside the queried phrasings.
- All analytic verdicts are my own; per AGENTS.md this submission requires
  independent coordinator inspection. No novelty claim is made anywhere.

## Proposed next tasks

1. Write out (L″): "D-agreement for smooth spacelike acausal partial data",
   following Sbierski's gluing restricted to D(K); or find it in print
   (Ringström 2009 access would settle this quickly).
2. Prove or disprove avoidance lemma (A) (smooth spacelike Cauchy surface
   through x avoiding J⁺(b)∖{b}), which would give Theorem 2 under the
   smooth-acausal convention; 1+1 evidence is positive.
3. Investigate whether this specific h(K₁) (from Theorem 3 step 4's pull-back
   structure) must lie in a Cauchy surface of M₂ — a targeted route around (L″).
4. Apply the corrected statements to the classification table rows (H-rigidity
   without a matched slice remains open, as the draft says).
5. Update SCREENING.md's L23–L27 (convention) and L88–L103 ((L′) → (L″)) upon
   coordinator acceptance of this review.

## Blockers

None. (web-search-prime unavailable by design; Ringström book inaccessible —
both recorded as gates, neither blocks the deliverables.)
