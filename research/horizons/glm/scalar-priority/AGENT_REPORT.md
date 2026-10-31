# AGENT_REPORT — horizons-scalar-priority

Date: 2026-10-25. Task: audit prior work and exact sources for scalar
sharpness (Prop sharp) and antipodal echo (Prop echo) in the frozen draft
`research/horizons/coordinator-review/dispatch-2026-10-25/main.tex`, plus
the slicing characterization (Thm char) and the Manchak 2008 appeals.
Status: **submission for independent review** — a worker output, not an
accepted completion and not a final truth claim.

## Done / files

Research outputs (owned path `research/horizons/glm/scalar-priority/`):

- `PRIOR_WORK.md` — claim-by-claim antecedent audit with exact locators,
  verdicts (supported / needs narrowing / unread), and safe replacement
  wordings for the Manchak paraphrases.
- `sources.jsonl` — 13 source records per the knowledge-base contract
  (read_depth, exact versions, locators, limits).
- `SEARCH_LOG.md` — capability check, all queries, retrieval outcomes,
  coverage gaps.
- `echo_mode_check.py` — bounded verification script (see below).

Handback file: this `AGENT_REPORT.md` at the worktree root (allowed per
runbook).

## Search capability check

- `web-search-prime` (Z.ai): **unavailable** — quota exhausted, error code
  1310, "Weekly/Monthly Limit Exhausted", resets 2026-11-17 10:00:29. One
  test query; no retry loops.
- Fallbacks that worked: `serpapi_search` (MCP) and the built-in
  `websearch`; both exercised successfully and recorded in SEARCH_LOG.md.
- The brief's "timed out" Manchak URL actually returned HTTP 200 on
  2026-10-25; Manchak 2008 was therefore read at **full-text** depth (the
  published version, Found. Phys. 38: 317–321) from the author's site.

## Source coverage (depth-labeled)

Full-text read: Manchak 2008 (all 4 pages); Geroch 1977 (LSE scan, printed
pp. 81–93); Grøn & Johannesen arXiv:1103.4753v1; Bolotin & Tanatarov
arXiv:1310.6329v3 (pp. 1–23 + refs); Harte & Drivas arXiv:1202.0540v3 (= PRD
85, 124039); Baskin & Mazzeo arXiv:1210.8053v1 (§1–2 + refs).
Discovery only (not accessed): Wald 1984 (**App. D locator UNVERIFIED**;
lending-restricted), Friedlander 1975, Günther 1988, Hogarth 1993, Rindler
1956 (ADS 504), Minguzzi–Sánchez 2008, Manchak survey (403).

## Key findings

1. **Prop sharp is an immediate composition of standard results.**
   Conformal reduction of the conformally coupled equation (standard;
   exact Wald locator unverified) + sharp domain of dependence of the wave
   equation (sufficiency verified full-text in Baskin–Mazzeo §2.1;
   traveling-wave sharpness is standard PDE folklore with no locator
   verified here). Per the NOVELTY.md reject gate: **needs narrowing — not
   a candidate for mathematical novelty**; value is expository at most.
2. **Prop echo: ingredients standard; nearest published neighbor found.**
   The geometric half (closed-dust particle horizon vanishing at maximum
   expansion; antipodal two-path imaging) is verified prior work (GJ §2.2
   eqs. (11)–(15), pp. 4, 6, 10; BT §1.4 problem 40, pp. 21–23, Fig. 1.10).
   The wave half sits one formulation from Harte & Drivas (2012): retarded
   Green functions in **all conformally flat spacetimes** flip sign
   (δ(σ) → −δ(σ)) at each perfect caustic — predicted by their Penrose-limit
   theory, with the ESU observation itself attributed there to a **private
   communication** (Casals, 2012), not a published computation. The mode
   parity behind the draft's proof (frequency n+1, antipodal parity (−1)ⁿ)
   is elementary and was computationally confirmed. **Verdict: needs
   narrowing / undetermined within bounded search** — no verbatim printed
   determination statement found, but the inaccessible QFT-in-curved-space
   literature leaves a residual risk that a printed antecedent exists.
   Recommended: cite Harte & Drivas as nearest neighbor; keep the
   DRAFT3_FOLLOWUP caveat that the pre-threshold echo is spacelike to b.
3. **Thm char: undetermined within bounded search; plausibly a new
   formulation.** Closest antecedent verified: Geroch's printed definition
   of P(q) and his equivalent achronal-surface form (printed p. 91). The
   targeted novelty search returned zero results. No priority claim.
4. **The draft's Manchak paraphrase needs correction.** Manchak's Theorem 1
   (p. 319) concludes "(M,g) admits a **compact, spacelike slice**" (slice =
   closed achronal set without edge, fn. 9) — *not* "a compact Cauchy
   surface" — under the hypothesis that some timelike-future event lies in
   the Geroch-style domain of prediction (achronal closed spacelike S ⊆
   J⁻(q)). Safe replacement wording supplied in PRIOR_WORK.md §2.5. The
   verification-impossibility paraphrase is supported in substance by
   Manchak's genuine-prediction Theorem 2 (P(q) ⊆ ∂J⁻(q), pp. 320–321),
   with wording narrowed. Also recorded: Geroch's printed p. 92
   closed-universe claim was shown false (Manchak fn. 8 → Hogarth 1993,
   unread); the manuscript should not lean on that page.
5. **Geroch attributions in the draft verified**: Einstein-static
   prediction example is Geroch's (printed p. 89 text; Fig. 5 on p. 91);
   the draft's "Relation to Geroch" paragraph matches the printed
   definition.

## Verification commands and results

```
# frozen input integrity
shasum -a 256 research/horizons/coordinator-review/dispatch-2026-10-25/main.tex
# → bbd592692f26484d6a13591d07989709ed32205ae250d36ebb88e15c4bc84bbe  (matches SOURCE.md)

# HTTP checks (representative)
curl -sL -o manchak_ippigr.pdf -w "%{http_code} %{size_download}" \
  https://sites.socsci.uci.edu/~jmanchak/ippigr.pdf     # → 200 226543
curl -sL -o geroch1977.pdf -w "%{http_code} %{size_download}" \
  https://personal.lse.ac.uk/robert49/ppb/pdf/GerochPredictnInGRMinnesVol81977.pdf  # → 200 1748381

# bounded spectral check of the echo mode algebra (stdlib only)
python3 research/horizons/glm/scalar-priority/echo_mode_check.py
# → PASS for n = 0..10: Laplace eigenvalue -n(n+2) consistent, frequency omega = n+1,
#   antipodal parity (-1)^n, and psi(eta+pi,-X) = -psi(eta,X) on explicit harmonic
#   polynomial modes; final line "ALL PASS"
```

The Python check verifies the standard spectral facts on explicit degree-n
harmonic modes (bounded scope). It is **not** a general proof of the
smooth-solution statement and carries no priority or novelty weight.

## Strongest contrary evidence

- Harte & Drivas p. 17 (Huygens failure: retarded Green functions
  generically have inside-cone support, citing Friedlander 1975 and Günther
  1988) shows the ESU/closed-FLRW wave-propagation lore is tail-dominated;
  the echo must be read as a value-determination statement, not a sharp-
  signal statement. No contradiction with the draft, but a required framing.
- The ESU sign-flip observation rests on a private communication inside
  Harte & Drivas — there is no published ESU Green-function computation
  confirming it in the sources read; the conformally-flat generality claim
  is the published part.
- REVIEW.md's sufficient-vs-necessary objection is consistent with Geroch
  §2's own explicit remark that determination statements "depend on the
  type of matter or fields considered" (printed pp. 84–85) — supporting
  the frozen draft's solution-class repair rather than the earlier framing.
- Residual novelty risk for Prop echo from literature I could not access
  (QFT-in-curved-space textbooks; Casals et al. Green-function papers).

## Limitations

- Wald 1984 App. D locator remains **unverified** (lending-restricted);
  manuscript should pin it from a physical copy or equation-precise citing
  source before relying on the exact citation.
- Hogarth 1993, Rindler 1956, Friedlander 1975, Günther 1988,
  Minguzzi–Sánchez 2008 unread; their content is recorded only at
  discovery depth via verified citing sources.
- The "closed universe as a lens" paper I initially suspected could not be
  confirmed and is deliberately not cited anywhere in my outputs.
- Bounded search only: the empty novelty searches are informative but not
  exhaustive; no global novelty, physical-realism, or ontology claim is
  made or supported by this audit.

## Proposed next tasks

1. Pin the Wald App. D equation numbers (or swap to a verified reference).
2. Retrieve Hogarth 1993 pp. 726–727 (counterexample to Geroch p. 92).
3. Library-access pass over Birrell & Davies / Parker & Toms and the
   Casals–Dolan–Ottewill–Wardell papers for any printed ESU/closed-FLRW
   mode-parity or antipodal-echo statement (likeliest home of a verbatim
   antecedent).
4. PhilPapers/PhilSci/MathSciNet pass on "domain of prediction"
   reformulations to firm up the Thm-char novelty question.
5. Optional bounded numerical illustration: retarded Green function sign
   flip on an ESU conformal slab vs. the Harte–Drivas prediction.
