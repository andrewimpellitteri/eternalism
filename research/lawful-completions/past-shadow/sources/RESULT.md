# past-shadow-ltb-sources: RESULT — source audit for LTB embedding, Weyl formula, shell crossing and Einstein-dust well-posedness

Date: 2026-10-28. Worker: past-shadow-ltb-sources (branch `agent/past-shadow-ltb-sources`).
Scope: locate primary or standard-textbook statements with exact locators and read depths for
four claims. No locators are asserted that were not read from the cited source or its
publisher/metadata service. Items marked LEAD are discovery-level only.

## Search capability check

- `web-search-prime` MCP tool: FAILED once with quota error
  (`MCP error -429, code 1310, "Weekly/Monthly Limit Exhausted ... reset 2026-11-17"`),
  matching the coordinator note. Not retried.
- Fallbacks used and working: built-in `websearch`, `webfetch` (arXiv HTML / ar5iv / PMC /
  Springer / ADS abstract pages), `scholar_search` (openalex/crossref/arxiv metadata),
  `exa.web_fetch_exa` (successfully read the ADS full-text scan PDF of Hellaby–Lake 1985).

Read-depth labels follow knowledge/README.md: discovery, abstract, full-text, reproduced,
code-audited.

## Master table: claim → source → locator → depth → hypotheses

### Item 1 — LTB dust solution, simultaneous bang time, FLRW matching outside a comoving ball

| # | Claim | Source | Exact locator | Read depth | Exact hypotheses / content |
|---|-------|--------|---------------|-----------|----------------------------|
| 1.1 | LTB metric, R-equation, density, bang time, explicit η-parametric solutions | Krasiński & Hellaby 2002, Phys. Rev. D 65, 023501; arXiv:gr-qc/0106096 (ar5iv full text) | §2, eqs. (2.1)–(2.6); Λ=0 assumed for (2.4)–(2.6) | full-text | Metric ds²=dt²−R′²/(1+2E(r))dr²−R²dΩ² (2.1); Ṙ²=2E+2M/R+ΛR²/3 (2.2); κρ=2M′/(R²R′), κ=8πG/c⁴ (2.3); elliptic/parabolic/hyperbolic parametric solutions with t_B(r) (2.4)–(2.6). Dust, spherical symmetry, comoving coordinates. |
| 1.2 | FLRW models are the LTB subset with simultaneous bang time | same | §2, eqs. (2.7)–(2.8) | full-text | "The Friedmann models are contained in the Lemaître-Tolman class as the limit: t_B = const, \|E\|^{3/2}/M = const (2.7)"; standard radial coordinate when M = M₀r³, E = E₀r² (2.8). |
| 1.3 | Historical primaries for the LTB solution | Lemaître 1933, Ann. Soc. Sci. Bruxelles A53, 51; English translation "The Expanding Universe", Gen. Relativ. Gravit. 29, 641–680 (1997), DOI 10.1023/A:1018855621348; Tolman 1934, Proc. Natl. Acad. Sci. 20(3), 169–176, DOI 10.1073/pnas.20.3.169 (free scan PMC1076370); Bondi 1947, MNRAS 107, 410–425; reprinted Gen. Relativ. Gravit. 31, No. 11 (1999) | Bibliographic records verified on SpringerLink, PNAS/PMC, ADS (1933ASSB...53...51L, 1947MNRAS.107..410B), INSPIRE 1307207 | metadata verified; Tolman: abstract (intro/conclusion OCR read; scan equations are OCR-garbled); Lemaître/Bondi content: NOT read | None asserted from content. Cross-check: Hellaby & Lake 1985 §II(a) writes "The Tolman metric is (Lemaître 1933; Tolman 1934; Bondi 1947)" — full-text cross-reference read. |
| 1.4 | LTB hole matched to FLRW exterior at a comoving boundary; compensated ("Swiss-cheese") construction | Marra, Kolb, Matarrese, Riotto 2007, Phys. Rev. D 76, 123004; arXiv:0708.3622 (ar5iv full text) | §II eqs. (1), (5), (7)–(10); §II.2.1; Fig. 2 caption; §V.1 | full-text | EdS "cheese"; unified form ds²=−dt²+Y′²/W²dr²+Y²dΩ² (1); mass/mean density M(r)=4π∫ρY²Y′dr=(4π/3)Y³ρ̄ (5); matching conditions: at hole boundary ρ̄→ρ_FRW and W(r)→1, with density profile chosen "in order to match the flat FRW model at the boundary of the hole"; §V.1: profile chosen with ⟨δρ⟩=0 (compensation). Text: "This idea was first proposed by Einstein and Straus". Their §III.2 also displays Y′→0 shell-crossing formation in a specific profile (cautionary, not a general claim). |
| 1.5 | Einstein–Straus vacuole (Schwarzschild cavity in an expanding cosmos) as historical background | Einstein & Straus 1945, Rev. Mod. Phys. 17, 120–124, DOI 10.1103/RevModPhys.17.120; erratum Rev. Mod. Phys. 18, 148–149 (1946), DOI 10.1103/RevModPhys.18.148 | DOI/Crossref metadata only | discovery (LEAD) | Metadata verified via two independent published reference lists read at full-text level (Krasinski–Hellaby 2002; Marra et al. 2007 citation "einstein" [bib.bib2] and PRD 65 023501 reference list). Paper content not read. |
| 1.6 | LTB/FLRW compound-models lineage (LTB void + envelope + FLRW exterior) | Sussman 2010, Class. Quantum Grav. 27, 175001; arXiv:1005.0717 (ar5iv full text) | §1, paragraph citing refs [29]–[33] | full-text (quote) | "the void is an LTB region containing a center, matched at a fixed comoving radius to another LTB region (the 'envelope'), which in turn is matched to a FLRW 'exterior'." Author calls these configurations "artificial". |

Note on 1.4: Marra et al. fix initial data at a common time t̄ with uniform H; the paper does
not claim t_B(r)=const in general, and their §III.2 profile develops shell crossings. Do not
cite it for a simultaneously-banging matched model.

### Item 2 — LTB Weyl scalar (Ψ₂ / electric Weyl part) in terms of M, R, R′

| # | Claim | Source | Exact locator | Read depth | Exact hypotheses / content |
|---|-------|--------|---------------|-----------|----------------------------|
| 2.1 | LTB electric-Weyl scalar given by the density fluctuation: ℰ = −m_q δ^(m) = −m_q′/(3R′/R), with m_q = M/R³ | Sussman 2010, CQG 27, 175001; arXiv:1005.0717 | §2 eqs. (1)–(3), (4h), (4lm), (4lno); Appendix F "Local scalar representation" (title verified; E_ab normalization displayed there not re-derived) | full-text | His conventions: metric ds²=−c²dt²+R′²/(1+E)dr²+R²dΩ² (1); Ṙ²=2M/R+E (2); 2M′=κρR²R′, κ=8πG/c² (3); quasi-local density m_q=M/R³ (4h); fluctuation δ^(m)=(A−A_q)/A_q with A=m (4lm); shear/electric-Weyl scalars Σ=−ℋ_qδ^(ℋ), ℰ=−m_qδ^(m) (4lno). Local density scalar m=κρ/6=M′/(3R²R′) follows from (3). |
| 2.2 | Conventional-variable form (OUR algebra from 2.1, labeled as derived) | substitution into printed equations of 2.1 | derivation; checks below | derived, unchecked by independent source | ℰ = m_q − m = M/R³ − M′/(3R²R′) = (3MR′ − RM′)/(3R³R′). Checks: FLRW (M=M₀r³, R=a(t)r) ⇒ ℰ=0 ✓; Schwarzschild-like region (M′=0) ⇒ ℰ=M/R³ ✓. Sign/factor conventions for the Newman–Penrose scalar "Ψ₂ = −M/R³" were NOT verified in any fetched primary; treated as an unverified lead. |
| 2.3 | Standard LTB summary with metric (15) and R-equation (16) | Bolejko, Célérier & Krasiński 2011, Class. Quantum Grav. 28, 164002; arXiv:1102.1449v2 (ar5iv full text) | §2(2.b), eqs. (15)–(16) | full-text | ds²=dt²−R′²/(1+2E)dr²−R²dΩ² (15); Ṙ²=2E+2M/R+ΛR²/3 (16). This review's fetched portion contains no Weyl-scalar equation (verified absence in the read text). |

### Item 3 — Hellaby–Lake 1985 no-shell-crossing conditions; specialization to t_B′=0 with elliptic E<0

| # | Claim | Source | Exact locator | Read depth | Exact hypotheses / content |
|---|-------|--------|---------------|-----------|----------------------------|
| 3.1 | Necessary and sufficient no-shell-crossing conditions in Tolman models | Hellaby & Lake 1985, Astrophys. J. 290, 381–387, DOI 10.1086/162995; erratum ApJ 300, 461 (1986), DOI 10.1086/163822 (erratum metadata only, not read) | §II eqs. (2.1)–(2.31), Table 1; §IV | full-text (ADS scan PDF; displayed equations partially OCR-garbled) | Tolman metric (2.1) ds²=−dt²+r′²/(1+f)dR²+r²dΩ²; arbitrary functions a(R) (bang time), f(R) (energy), F(R) (mass ∝); density 8πρ=F′/(r²r′) (2.5, OCR). Elliptic (f<0), r′>0: a′<0 (2.25a); bound relating a′ to πF(−f)^{−3/2} and q′/q (2.25b — OCR garbled, NOT quoted here); F′>0 (2.25c); "the second one ensures that the time of recollapse increases with R, wherever r′ is positive". Hyperbolic (f>0): a′<0 (2.29); f′>0 (2.30); F>0 and F′>0 (2.31) — "sufficient as well as necessary". Regular maximum: F′=0 (2.7), f′=0 (2.8), a′=0 (2.9) at the same R (surface layer present; mass 2r(1+f)^{1/2}). Table 1 allows at most two of a′=0, f′=0, F′=0 at r′=0 loci. §IV quote: "Previously (Hellaby and Lake 1984), we concluded that physically reasonable Tolman models must have a simultaneous bang, i.e., a′ = 0 everywhere. This result is entirely compatible with the above conditions." Also: the commonly quoted conditions (r′>0, F′>0) "are actually too restrictive". |
| 3.2 | HL conditions restated in conventional M, E, t_bb variables | Sussman 2010, CQG 27, 175001; arXiv:1005.0717 | Appendix C, displayed conditions (unnumbered in ar5iv render) + §2 eqs. (1)–(3) | full-text | Parabolic & hyperbolic (expanding): R′>0 ⇔ {M′≥0, E′≥0, t_bb′≤0}. Elliptic: ±R′>0 ⇔ ±M′≥0, ±t_bb′≤0, ±[M′/M − (3/2)E′/E + c·t_bb′·\|E\|^{3/2}/(2πM)] ≥ 0. "The equal sign holds only at symmetry centers and at values of r where R′=0." CAUTION: Sussman's E is defined by Ṙ²=2M/R+E (his E = 2× the E of Krasiński–Hellaby/most LTB literature). |
| 3.3 | Specialization to simultaneous bang time, elliptic region (OUR derivation from 3.2) | derived from 3.2 by setting t_bb′=0 | derivation | derived, arithmetic check below | Expanding elliptic branch (sign +): conditions reduce to M′≥0 and M′/M − (3/2)E′/E ≥ 0 (plus the equality clause at centers/R′=0 loci). In HL 1985 variables the same specialization is consistent with §IV's simultaneous-bang remark quoted in 3.1: a′=0 is the boundary case of a′<0, with r′>0 then controlled by F′>0 away from regular maxima. |
| 3.4 | Simultaneous-bang models: HL conditions reduced to sign conditions and consequences | Sussman 2010 | §10.1 "Models with a simultaneous big bang", eqs. (4lnq…a),(4lnq…b) and the two displayed reductions (ar5iv labels); narrative below them | full-text | t_bb=t₀=const; elliptic: c(t_i−t₀)=Z_e(x_i)/y_i, δ_i^(m)=(β₁/α₁)δ_i^(k) with 0<β₁/α₁<1; HL conditions reduce to δ_i^(m)>−1 and δ_i^(m)−(3/2)δ_i^(k)>0 (elliptic); δ_i^(m)>−1, δ_i^(k)>−2/3 (hyperbolic). Consequence (elliptic, quoted): "there are no density and spatial curvature profile inversions, and (as opposed to the hyperbolic case) density void profiles are not possible in regular configurations." |
| 3.5 | Citation-chain cross-check and bang-time sign intuition | Krasiński & Hellaby 2002, PRD 65, 023501; arXiv:gr-qc/0106096 | §3.4 paragraph "Another serious possibility …" citing [7]; reference list [7]; appendix remark on t_{B,M}>0 | full-text | "The conditions on E(M) & t_B(M) for avoiding them [7] must also be checked." [7] = "C Hellaby, K. Lake, Astrophys. J. 290, 381 (1985) [+ erratum: Astrophys. J. 300, 461 (1985)]". Appendix remark (quote): "Strictly speaking, an increasing t_B, t_{B,M}>0, creates a shell crossing, but for such a slight variation in t_B, the shell crossing occurs very early on…" |

### Item 4 — Local well-posedness of the Einstein-dust (pressureless Einstein–Euler) Cauchy problem

| # | Claim | Source | Exact locator | Read depth | Exact hypotheses / content |
|---|-------|--------|---------------|-----------|---------------------------|
| 4.1 | Local existence + uniqueness for Einstein–dust; isolated bodies | Choquet-Bruhat & Friedrich 2006, "Motion of isolated bodies", Class. Quantum Grav. 23, 5941–5950, DOI 10.1088/0264-9381/23/20/015; arXiv:gr-qc/0605096v1 (arXiv HTML full text) | Abstract; §2 eqs. (2.1)–(2.8); Theorem 2.1; Corollary 2.2; §2.3; Theorem 2.3; Remark 2.4; Corollary 2.5 | full-text | System: T_ab=r u_a u_b (2.1); u^αu_α=−1 (2.2); ∇_αT^{αβ}=0 ⇒ geodesic motion (2.4) + continuity ∇_α(ru^α)=0 (2.5); R_ab=r(u_a u_b + g_ab/(n−1)) (2.6). Theorem 2.1 (n+1 dims): data ḡ∈M_s, k̄∈H_{s−1}, v̄∈H_{s−1}, r̄∈H_{s−2}, s>n/2+2, ‖v̄‖_ḡ<1 ⇒ unique local wave-gauge solution g∈L_s(T), u∈U_{s−1}(T), r∈E_{s−2}(T); hyperbolic Leray system, causal while g Lorentzian and u timelike. Corollary 2.2: constraint-satisfying data ⇒ solution of the full Einstein-dust system; globally hyperbolic; unique up to isometry in the maximal globally hyperbolic class if s>n/2+3. Theorem 2.3 (r̄≥0, ω̄=supp(r̄)): physical solution determined by (ḡ,k̄,r̄) on M and v̄ on ω only, independent of the extension of v̄. Corollary 2.5: local geometric uniqueness. Limitation (§2.3, Remark 2.4): caustic formation (∇u blow-up, "physical phenomena like shell crossings", citing Yodzis–Seifert–Müller zum Hagen 1973) can end the evolution; lifetime can depend on the extension of v̄ off supp(r̄). |
| 4.2 | Citation verification for "Choquet-Bruhat and Friedrich 2006" | this task (verification note) | — | verification | A 2006 joint Choquet-Bruhat–Friedrich paper exists with the content the brief expected (Einstein-dust Cauchy well-posedness), but its title is "Motion of isolated bodies", CQG 23, 5941–5950. Crossref/arXiv/INSPIRE searches found no separate 2006 C. R. Acad. Sci. note titled "Cauchy problem for the Einstein-dust system" by these authors. Treat the short-title form in the task brief as a paraphrase, not a citable title. |
| 4.3 | Related leads (metadata only, not read) | (a) H. Friedrich, "Sharp asymptotics for Einstein-λ-dust flows", Commun. Math. Phys. 350, 803–844 (2016), DOI 10.1007/s00220-016-2716-6 (Crossref). (b) H. Friedrich, "Evolution equations for gravitating ideal fluid bodies in general relativity", Phys. Rev. D 57, 2317–2322 (1998) — printed as ref [4] of 4.1. (c) A. D. Rendall, J. Math. Phys. 33, 1047–1053 (1992) — ref [7] of 4.1. (d) S. Dain & G. Nagy, Phys. Rev. D 65, 084020 (2002) — ref [2]. (e) Kind & Ehlers — ref [5] of 4.1; NOTE: the arXiv HTML prints "Class. Quantum Grav. 18 (1993) 2123–2136", an internally inconsistent volume/year; actual data unverified. (f) Yodzis, Seifert & Müller zum Hagen, Commun. Math. Phys. 34, 135–148 (1973) — ref [8]. (g) Choquet-Bruhat, General Relativity and the Einstein Equations (OUP 2008), "Local Cauchy Problem" chapter pp. 142–178 (Crossref). | — | discovery (LEADS) | Cited only as leads from the read reference list of 4.1 or from Crossref; no content assertions. |

## Contrary evidence and cautions found while reading

- Hellaby & Lake 1985 explicitly contradict Zel'dovich & Grishchuk (1984): a closed hybrid
  model (elliptic–hyperbolic–elliptic) can be shell-crossing free without global recollapse
  (§IIIc model, §IV). Zel'dovich & Grishchuk 1984, MNRAS 207, 23P — metadata via HL's reference
  list only (LEAD).
- HL 1985: the frequently quoted sufficient conditions (r′>0, F′>0) are "too restrictive" —
  they exclude regular maxima needed in closed models.
- Sussman 2010 §11: for elliptic models, dropping t_bb′≤0 while keeping t_coll′≥0 produces
  shell crossings near t≈t_bb for all r; shell-crossing-free evolutions can exist only on
  restricted time ranges. Elliptic regular configurations forbid density voids entirely.
- Sussman 2010 §10.3: an elliptic region enclosing a parabolic or hyperbolic region containing
  a center is incompatible with the HL conditions (citing Bonnor, CQG 2, 781–790 [47]).
- Normalization trap recorded: E in Sussman 2010 = 2E in Krasiński–Hellaby 2002 (metrics
  (1) vs (2.1)). Comparisons across these papers must convert.
- My own memory of two arXiv IDs was wrong and caught by fetching: 1102.1445 and 1107.1854 are
  unrelated papers; correct IDs are 1102.1449 (Bolejko–Célérier–Krasiński review) and
  1104.4447 (Nandra–Lasenby–Hobson). Nandra et al. 2012 (MNRAS 422, 2931) was fetched and is a
  pressured-fluid McVittie-type spacetime, NOT LTB dust — excluded as a source for item 2.

## Access gates

- ADS/PDF and APS pages are not readable by the plain fetcher (content-type blocked);
  exa fetch handled the ADS scan. Tolman 1934 exists only as scanned page images on PMC; its
  equations could not be transcribed reliably (OCR garbled), so no equation locators are
  asserted for Tolman.
- Hellaby–Lake erratum (ApJ 300, 461) and Zel'dovich–Grishchuk 1984 not read (metadata only).
- Bondi 1947 full text exists behind a third-party PDF; its displayed equations were seen only
  through search-engine OCR excerpts and are treated as unverified. Only bibliographic facts
  for Bondi are asserted.

## Verdict per item

| Item | Status |
|------|--------|
| 1. LTB + simultaneous bang + FLRW matching | LOCATED (modern full-text anchors 1.1–1.2, 1.4, 1.6; primaries at metadata depth 1.3, 1.5) |
| 2. Weyl scalar in M, R, R′ | LOCATED at full-text level in Sussman's conventions (2.1); conventional-variable form is OUR derived algebra (2.2); NP Ψ₂ normalization left as lead |
| 3. Hellaby–Lake conditions, t_B′=0 elliptic specialization | LOCATED (3.1 full-text; 3.2 full-text restatement; 3.3 derived; 3.4 full-text simultaneous-bang case) |
| 4. Einstein-dust local well-posedness | LOCATED AND VERIFIED (4.1 full-text; brief's citation paraphrase corrected in 4.2) |
