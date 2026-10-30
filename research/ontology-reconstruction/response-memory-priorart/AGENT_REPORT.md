# AGENT_REPORT — ontology-response-memory-priorart

Date: 2026-10-30. Branch: `agent/ontology-response-memory-priorart`.
Bounded prior-result challenge for the response-memory contract. Submission for
independent review; not an accepted completion and not a temporal-ontology verdict.

## Done and files

- Compared the three nearest primary works at hypothesis/result level, at the
  contracted locators, all read at full-text depth from fetched primary PDFs
  (details and exact versions in `sources.jsonl`, analysis in `RESULT.md`):
  - Salnikov–Satunin–Kirpichnikov–Fitkevich 2021, JHEP03(2021)143, App. A p. 15 (A.1)–(A.3);
  - Boyd–Chua 1985, IEEE Trans. Circuits Syst. CAS-32(11):1150–1161, §III, Thms 1–2,
    §8.1 Thm 5, §8.2 Thm 6, Conclusion;
  - Dong arXiv:1905.08620v1, abstract/intro/Theorem 1.1/§3.1–3.2 (Prop. 3.1, 3.3).
- Recorded the priority verdict: support claim (a) is **printed** (Salnikov (A.1),
  classical); norm claim (b) and fixed-window claim (c) have **no exact printed
  predecessor found** within stated search limits and are classified as **elementary
  consequences** (three-line derivation from the printed kernel + folklore
  kernel-norm identity + DLMF 10.7.3/10.17.3; full derivation in RESULT.md §3).
- Kernel normalization checked against (A.1): exact match, including 1/(4πr).
- Verified fading-memory realization invariance is Boyd–Chua Thm 6 (already known);
  not claimed as new anywhere in the outputs.
- Philosophical linkage checked at primary-access level: Brading 2013 law-constitutive
  present (Phil. Sci. 80(5):1101–1111, DOI 10.1086/673897); public PDF accessibility
  re-verified this run; the project's full-text record (`found-brading`) supplies the
  section locators (pp. 1103–1105). No novelty from the linkage alone.

Files written (all inside the owned directory):
- `research/ontology-reconstruction/response-memory-priorart/RESULT.md`
- `research/ontology-reconstruction/response-memory-priorart/sources.jsonl` (8 records:
  5 full-text/abstract-level, 2 discovery-depth print locators, 1 abstract-level)
- `research/ontology-reconstruction/response-memory-priorart/AGENT_REPORT.md` (this file)

## Search capability check (recorded per brief)

- `web-search-prime` (Z.ai MCP): **failed** — HTTP 429, code 1310 "Weekly/Monthly Limit
  Exhausted. Your limit will reset at 2026-11-17 10:00:29". First relevant test search
  did not execute.
- `serpapi_search`: **failed** — "Your account has run out of searches."
- `scholar_search`: **works** (openalex + arxiv); used for the capability test and the
  Brading check; relevance for the narrow norm question was low.
- `exa` `web_search_exa` / `web_fetch_exa`: **works**; used for two small query batches
  and all primary fetches. No claim in the outputs rests on a page that was not fetched.

## Source coverage

Three primaries at the contracted locators (full-text), two DLMF equation pages
(full-text), Brading 2013 (opening re-read; full-text record inherited from KB),
two print locators recorded at discovery depth only (Polyanin 2016; Gradshteyn–Ryzhik
2007 — paywalled, not accessed, no content claims made about them).
Search effort within budget: batch 1 = 3 queries (norm predecessor + locate the two
other primaries); batch 2 = 3 queries/fetches (norm predecessor re-check, Brading,
DLMF). Primary citation chasing followed Salnikov's references [48], [49].

## Verification commands and results

- `curl -sL` fetches to `/private/tmp/opencode/rm-priorart/`:
  `boyd_chua_1985.pdf` (1,373,846 B, web.stanford.edu/~boyd/papers/pdf/fading_volterra.pdf),
  `salnikov_2021.pdf` (1,841,900 B, link.springer.com/content/pdf/10.1007/JHEP03(2021)143.pdf),
  `dong_1905_08620v1.pdf` (239,343 B, arxiv.org/pdf/1905.08620v1). All three parsed as
  the correct papers and read directly.
- `python3 /private/tmp/opencode/rm-priorart/verify.py` — analytic-bound sanity check
  of the norm identity and ratio limit (J₁ by series ≤30, DLMF-10.17.3 asymptotic
  beyond; Simpson): C_* ≈ 1.536 on [0,200] with analytic tail bound ≤ 0.113;
  ratio ‖R_m−R₀‖/m ÷ C_* at r=1: 0.866 (m=0.5), 0.950 (0.2), 0.986 (0.1), 1.004 (0.05).
  Elapsed 0.06 s — within the hard ≤15 s / actual ≤10 s / total ≤30 s budget. No other
  computation was run; no numerical grids were used for any claim.
- Hand derivation (RESULT.md §3): substitution z = m√(s²−r²) and √(r²+z²/m²) ≥ z/m give
  ‖R_m−R₀‖ = (1/4π)∫₀^∞ |J₁(z)|/√(r²+z²/m²) dz ≤ C_*·m/(4π); ratio limit by dominated
  convergence; |J₁(u)| ≤ u/2 gives window error ≤ m²W/(8π). The L∞→L∞ norm of a
  translation-invariant convolution channel equals the kernel's L¹ mass (exact norm,
  not an estimate), the framework being Boyd–Chua Thm 5's bounded-measure class.

## Strongest contrary evidence (novelty defeaters found)

1. The support statement is printed: Salnikov et al. (A.1) contains the exact kernel
   with θ(t−t′−R) tail for all m>0 and attributes it to a 2016 handbook. Any claim of
   a "new support result" is defeated.
2. The norm statement is the kind of immediate corollary the contract's kill criterion
   names: given (A.1), any analyst computing the L¹ mass of the tail reaches the
   C_*·m/(4π) bound and the ratio limit in three lines; the O(m²) fixed-window behavior
   is already visible in their harmonic-source phase comparison (A.2)–(A.3).
3. The bounded-measure/convolution framework making the norm identity "folklore-level"
   is Boyd–Chua Thm 5(I); the support/norm contrast is structurally the same as their
   known point that FM is an I/O property while measure-level structure (e.g., atoms,
   support) is not. The joint contrast is therefore a repackaging, not a new theorem.
4. "Uniform mass estimates" for KG is an established research subject (Dong v1 and its
   lineage), so absence of the exact statement in three papers does not establish it
   is unprinted anywhere.

## Verdict summary

- Claim (a) exact support: **printed predecessor — not novel.**
- Claim (b) L∞→L∞ bound with constant C_*·m/(4π) and ratio limit: **no exact printed
  predecessor found within audit limits; classify as an elementary consequence.
  No mathematical novelty claim should be made.**
- Claim (c) O(m²) fixed-window: **elementary; consistent with Salnikov (A.2)–(A.3).**
- Support/norm contrast as a *use*: potentially unoccupied only as a downstream
  constitutive criterion (contract's "constitutive transport" continuation), which
  requires independently specified organizing structure; the mathematics alone carries
  no novelty.
- Philosophical linkage: Brading 2013 is the accessible prior framing; a response
  window is not an ontology by relabeling (contract concurs).

## Limitations

- `web-search-prime` and `serpapi_search` were quota-exhausted; discovery coverage
  relied on exa + scholar_search within two small batches. This is a bounded audit,
  not a systematic review.
- Polyanin (2016) and Gradshteyn–Ryzhik (2007) not accessed (paywalled print); their
  exact locators are recorded from Salnikov's bibliography. The single highest-value
  unchecked locus for an exact printed predecessor of the norm constant is the
  Polyanin retarded-solution section.
- Broader literature not reached within budget: treatises on hyperbolic fundamental
  solutions, massive-photon (Proca limit) literature, viscoelastic/damped-wave kernel
  literature. "Not found" therefore means "not found within stated limits", never
  "does not exist".
- Numerical values are sanity checks only: C_* bounded to ≈[1.54, 1.65]; the m=0.05
  ratio (1.004·C_*) sits within the few-per-mille accuracy of the leading asymptotic
  used for |J₁| beyond z=30 (the dominated-convergence approach is from below exactly,
  so the 0.4% overshoot is attributable to that approximation).
- Dong was audited in the exact v1 (2019-05-21) only; later published versions were
  not consulted (out of budget).

## Blockers

None blocking submission. Access limits (quota-exhausted search tools, paywalled print
handbooks) are recorded above rather than resolved by assumption.

## Proposed next tasks

1. Access Polyanin (2016) retarded-solution section and Gradshteyn–Ryzhik (2007) §6.6xx
   in print/library; look for the kernel statement and any |J₁|/z-type printed integral.
2. If the coordinator's benchmark proceeds, state it as a kernel-norm-identity
   corollary of (A.1) with the explicit "elementary consequence" label from RESULT.md,
   citing Salnikov et al. 2021 App. A + DLMF 10.7.3/10.17.3 + Boyd–Chua Thm 5 as
   framework; keep fading-memory realization invariance out of the contribution list.
3. Scope check of the two contract continuations (constitutive transport; robust
   temporal organization) against Brading 2013 and Savitt before any philosophical
   claim, with the requirement of an independently specified constitutive criterion.
4. Optional bounded follow-up audit: Proca-limit and damped-wave kernel literature for
   an analogous support/norm contrast statement (same kill criterion applies).
