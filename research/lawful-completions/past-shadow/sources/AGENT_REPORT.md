# AGENT_REPORT — past-shadow-ltb-sources

Task: source audit for LTB embedding, Weyl formula, shell crossing and Einstein-dust
well-posedness (lawful-completions lane). Worktree
`/Users/andrew/eternalism/.worktrees/past-shadow-ltb-sources`, branch
`agent/past-shadow-ltb-sources`. Output goes to review; this is a submission, not a final
truth claim.

## Done / files

- `research/lawful-completions/past-shadow/sources/RESULT.md` — master table: claim → source →
  exact locator → read depth → exact hypotheses, for all four items; contrary evidence;
  access gates; per-item verdicts.
- `research/lawful-completions/past-shadow/sources/sources.jsonl` — 16 source records in the
  knowledge-base contract format (lane-prefixed IDs; read depths; limits; open questions).
- `AGENT_REPORT.md` (this file, repo root).

All four done-when items are met: each item has located sources with exact locators (three of
four at full-text depth), hypotheses recorded per claim, and no invented locators.

## Search capability check

- `web-search-prime` (Z.ai MCP): **failed once**, error −429 / code 1310 "Weekly/Monthly Limit
  Exhausted … reset 2026-11-17 10:00:29" — matches the coordinator's quota note. Recorded once;
  not retried, per instructions.
- Fallbacks that worked: built-in `websearch`; `webfetch` (arXiv HTML, ar5iv, PMC, SpringerLink,
  ADS abstract pages); `scholar_search` via OpenAlex/Crossref/arXiv (metadata + DOI resolution);
  `exa.web_fetch_exa` (read the ADS full-text scan PDF of Hellaby–Lake 1985, which the plain
  fetcher rejects as `application/pdf`).

## Source coverage (16 records)

- Full-text reads (7): Hellaby–Lake 1985 (ADS scan); Krasinski–Hellaby 2002 (arXiv/gr-qc/0106096);
  Sussman 2010 (arXiv:1005.0717); Marra–Kolb–Matarrese–Riotto 2007 (arXiv:0708.3622);
  Choquet-Bruhat–Friedrich 2006 (arXiv:gr-qc/0605096v1 HTML); Bolejko–Célérier–Krasiński 2011
  review (arXiv:1102.1449v2, ~35% read in detail); Nandra–Lasenby–Hobson 2012 (arXiv:1104.4447,
  ~40% read — **excluded with reason**: pressured McVittie-type fluid, not LTB dust).
- Metadata-verified, content unread (6): Lemaître 1933/translation GRG 29, 641 (1997); Tolman
  1934 (abstract + intro/conclusion OCR; scan equations unreadable); Bondi 1947 (abstract +
  reprint header); Einstein–Straus 1945 + erratum 1946; Zel'dovich–Grishchuk 1984; Friedrich
  2016 λ-dust.
- Leads via read reference lists (3): Rendall 1992; Yodzis–Seifert–Müller zum Hagen 1973;
  Kind–Ehlers (volume/year printed inconsistently in the arXiv HTML — flagged, unverified).

## Verification commands and results

No installs; read-only research. Verification steps actually performed:

1. `python3 scripts/agents.py brief past-shadow-ltb-sources` — brief loaded; owns-paths and
   done-when extracted. `git status` clean before work; branch as specified.
2. Every remembered arXiv ID was re-derived through OpenAlex/Crossref before fetching. Two of my
   remembered IDs were wrong and the wrong fetches were caught and discarded: 1102.1445 (a
   condensed-matter paper; correct review is 1102.1449) and 1107.1854 (a biophysics paper;
   correct Nandra et al. is 1104.4447). Recorded in RESULT.md as an audit trail.
3. Locators quoted in RESULT.md were read from: ar5iv/arXiv HTML full texts (equations seen
   rendered), the ADS scan of HL 1985 (full text; two displayed equations OCR-garbled and
   therefore explicitly **not** transcribed), SpringerLink/ADS/INSPIRE/PNAS metadata pages for
   the historical primaries.
4. Derived results are labeled as ours: the conventional-variable Weyl expression
   ℰ = M/R³ − M′/(3R²R′) = (3MR′−RM′)/(3R³R′) (substitution into Sussman's printed eqs. (1)–(3),
   (4h), (4lm), (4lno); FLRW-vanishing and M′=0 checks pass) and the t_bb′=0 specialization of
   the elliptic HL conditions (M′≥0 and M′/M − (3/2)E′/E ≥ 0, from Sussman Appendix C).

## Key corrections vs. the task brief

- "Choquet-Bruhat and Friedrich 2006" exists and covers exactly the needed content (local
  well-posedness + geometric uniqueness for Einstein-dust), but its actual title is **"Motion of
  isolated bodies"**, Class. Quantum Grav. 23, 5941–5950 (2006). No separate 2006 C. R. Acad.
  Sci. note titled "Cauchy problem for the Einstein-dust system" by these authors was found on
  Crossref/arXiv/INSPIRE. Downstream citations should use the CQG title.
- Normalization trap: Sussman 2010 uses E with Ṙ²=2M/R+E (his E = 2× the E in Krasinski–Hellaby
  2002 / most literature). Comparisons must convert.

## Strongest contrary evidence

- Hellaby–Lake 1985 refute Zel'dovich–Grishchuk (1984): mixed elliptic/hyperbolic Tolman models
  can be shell-crossing free without global recollapse (their Sec. IIIc counterexample).
- HL 1985 also show the folklore sufficient conditions (r′>0, F′>0) are too restrictive
  (they exclude the regular maxima that closed models need).
- Sussman 2010 §11: in elliptic models, dropping only t_bb′≤0 while keeping t_coll′≥0 forces
  shell crossings near t≈t_bb; shell-crossing-free elliptic evolutions exist only on restricted
  time ranges; regular elliptic configurations admit no density voids at all.
- CBF 2006 §2.3/Remark 2.4: the well-posedness theorem is local; caustic formation ("physical
  phenomena like shell crossings") can terminate the evolution, and lifetime can depend on how
  v̄ is extended off supp(r̄) — the extension-independence theorem (2.3) needs r̄≥0, ω̄=supp(r̄).
- Marra et al. 2007 §III.2: their specific compensated Swiss-cheese profile develops shell
  crossings; the paper must not be cited as a shell-crossing-free matched model, nor for
  simultaneous t_B.

## Limitations

- Tolman 1934 and Bondi 1947: only page-image/OCR access; no equation locators asserted for
  either. Lemaître 1933 translation and Einstein–Straus 1945: bibliographic verification only.
- HL 1985 eq. (2.25b) and the density equation (2.5) are OCR-garbled in the scan; the
  transcription of (2.25b) is deliberately omitted rather than guessed. The erratum (ApJ 300,
  461) was not read.
- The NP-normalized claim "Ψ₂ = −M/R³" was not verified in any fetched primary; item 2 is
  delivered in Sussman's printed electric-Weyl convention plus our labeled substitution.
- ar5iv equation labels are mangled for Sussman 2010 (long hashed labels); locators there are
  given as section + printed content, and displayed formulas were verified intact.

## Proposed next tasks

1. Read the HL 1985 erratum and a clean scan to transcribe (2.25b); verify its equivalence with
   Sussman's bracket form (unit-check on c, |E|, π factors).
2. Read Bondi 1947 (GRG reprint) and the Lemaître 1997 translation to anchor the historical
   parametrizations and their bang-time functions at full-text depth.
3. Locate an NP-convention primary stating Ψ₂ for LTB (candidates: Krasinski's book Sec. 18;
   Barnes 1973; van Elst–Ellis 1996) to replace our derived ℰ with a citable Ψ₂ statement.
4. Verify Kind–Ehlers bibliographic data and read Friedrich 1998/Rendall 1992 to extend item 4
   beyond the 2006 local theorem (interfaces, uniqueness drawbacks).
5. For the coordinator: the t_bb′=0 elliptic reduction (M′≥0 and M′/M ≥ (3/2)E′/E) and the
   simultaneous-bang sign form (δ_i^(m)>−1, δ_i^(m)−(3/2)δ_i^(k)>0) are the directly usable
   hypotheses for any lane-A construction with a comoving LTB ball matched to FLRW.

## Blockers

None outstanding. web-search-prime quota exhaustion handled by fallbacks as instructed.

## Note for the coordinator

The root `AGENT_REPORT.md` in the base commit (`b9800a2`) held the stein-gluing-audit report.
Per this task's brief, root AGENT_REPORT.md is this task's output path; the prior report is
unchanged in git history and recoverable via `git show b9800a2:AGENT_REPORT.md`.

