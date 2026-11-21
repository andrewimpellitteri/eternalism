# Worker report: read-thermodynamic-arrow

12 November 2026. GLM reading lane on branch `agent/read-thermodynamic-arrow`.
Submission for independent review, not a truth claim. No temporal ontology is selected.

## Done and files

- `knowledge/reading/thermodynamic-arrow/READING.md` — the required note, exactly the five
  specified parts: (1) nine main positions with named defenders and labelled sources;
  (2) five canonical arguments reconstructed premise by premise with primary sources and
  standard objections; (3) five live open problems with progress markers; (4) repository
  dependencies, naming precise lines and sections of
  `research/what-the-past-can-fix/main.tex` (§sec:direction, lines 526–577; abstract line 50;
  §sec:revise line 741), `research/time-direction/fixing-exchange/RESULT.md`, and the two
  horizons notes; (5) ten ranked primary sources with what each would settle.
- `knowledge/reading/thermodynamic-arrow/sources.jsonl` — 17 lane-prefixed records (`ta-`)
  under the knowledge/README.md contract; full-text records carry the extra fields,
  locators, versions/DOIs, and related IDs; abstract/discovery records carry explicit limits.
- This report.

## Search capability check

- `web-search-prime` (Z.ai): **failed** — first and only call returned MCP error −429,
  "Weekly/Monthly Limit Exhausted. Your limit will reset at 2026-11-17 10:00:29". Recorded
  here as the required test. All search fell back to `scholar_search` (OpenAlex/Crossref
  metadata; its arXiv sub-source returned HTTP 429 once) and `exa` `web_search_exa` /
  `web_fetch_exa` (worked throughout; PDF text extraction is lossy in places — noted per
  source). No global MCP configuration was changed.

## What was read, at what depth

**Full-text (open primaries):**
- Callender, "Thermodynamic Asymmetry in Time", SEP substantive revision 12 June 2026 —
  the whole entry read in slices; **secondary scaffolding**, labelled as such.
- Wallace, "The logic of the past hypothesis", PhilSci 8894 preprint (2011) — abstract,
  §§1, 4, 6 (Simple Past Hypothesis, classical), 7 (quantum; Past Law Hypothesis), references.
  Printed 2023 Harvard UP version not diffed.
- Price, "The Thermodynamic Arrow: Puzzles and Pseudo-puzzles", arXiv:physics/0402040v1 —
  §§1–2, one-asymmetry section, Gold-universe section, "Scepticism about the second law".
- North, "Time in Thermodynamics", PhilSci 8947 — full text via lossy extraction (citation
  numerals dropped); PH/statistical-postulate passages, law-status passage, gravitational
  entropy passage, Leeds passage. Quotes paraphrased only.
- Loewer, Interface Focus 2011 (10.1098/rsfs.2011.0072) — abstract and introduction.
- Chen, arXiv:2008.00611 (v3 confirmed 2026-08-07) — abstract, introduction, TOC, nomic-status
  and Weyl-curvature passages.

**Abstract/discovery (leads with limits stated):** Chen's body sections; Dorst 2023
(abstract only); Brown 2017 (abstract + fragments); Frisch 2010 (PhilSci 5204 — extraction
garbled, effectively abstract-level); Crutchfield–Ellison–Mahoney arXiv:0902.1209 (abstract +
Theorem 1); Carroll–Chen arXiv:hep-th/0410270 (abstract + introduction); Watanabe 1955
(metadata verified only); Price 1995 chapter, Price 1996 book, Albert 2000, Zeh 2007, and
Gold 1962 (metadata or secondary only).

**Reused existing repo records without re-reading** (labelled in READING.md):
`arrow-goldstein-boltzmann-2001`, `arrow-gtz-no-ph-2016`, `arrow-penrose-wch-1979`,
`arrow-wallace-gravity-entropy-2009`, `arrow-carroll-chen-2004`,
`arrow-earman-past-hypothesis-2006` (abstract), `phil-price-arrow` (abstract). The
Boltzmann/Loschmidt/Zermelo reconstruction rests on Callender SEP §2 (secondary) plus those
records.

## Not accessed

Earman 2006 SHPMP 37:399–430 (paywalled; his position is reconstructed only from Callender
SEP §3.1 and Chen 2023's summary, and READING.md says not to quote its wording); Albert,
*Time and Chance*; Price, *Time's Arrow and Archimedes' Point*; Zeh's book; Reichenbach 1956;
Gold 1962 (locator never verified — no record written for it); Winsberg 2004; Frisch 2005;
Frisch–Pietsch 2016; Wallace's printed 2023 chapter; Dorst and Brown at body depth.

## Verification commands and results

- `python3 scripts/check_sources.py` → `24 files, 377 records: 0 errors, 2 warnings` — the
  two warnings are pre-existing in `knowledge/pw-critiques/` (untouched, another lane's);
  my one warning (Chen record missing exact arXiv version) was fixed by pinning v3
  (2026-08-07), re-checked clean.
- `git status --short` → only `?? knowledge/reading/` plus (after writing) `AGENT_REPORT.md`;
  nothing else modified; `git log` shows the board-seed commit as HEAD before my commit.
- Version checks done online: Wallace preprint (deposited 10 Nov 2011) and its Harvard UP
  DOI 10.4159/9780674287716-004 (Crossref, via scholar_search); Chen chapter DOIs
  10.2307/j.ctv32nxzc6.10 / 10.4159/9780674287716-008 and arXiv v3 (fetched); Earman 2006
  DOI 10.1016/j.shpsb.2006.03.002; Price 1995 DOI 10.1017/cbo9780511622861.005; Zeh 2007
  DOI 10.1007/978-3-540-68001-7; CEM DOI 10.1103/PhysRevLett.103.094101; Loewer DOI
  10.1098/rsfs.2011.0072; Watanabe Rev. Mod. Phys. 27, 179 (1955).

## Special question — answer recorded in READING.md §4

The fixing note's claims decompose as: (i) the conditional-entropy identity is a textbook
identity — right, elementary; (ii) "stationary chance opens the past as much as the future"
is Watanabe's framework (metadata-level) and CEM's stated theorem (abstract-level; CEM was
already credited by the note); (iii) "a Past Hypothesis supplies the imbalance" is the
standard Albert–Loewer Mentaculus doctrine — but no named defender states "openness =
conditional-entropy imbalance between bases"; Albert measures the epistemic arrow, CEM
measures stored memory (crypticity, which survives stationarity and is the rival measure),
and Wallace denies the PH is even an entropy-supplying posit. Verdict: said in skeleton,
not in packaging; right only as a stipulated, partition-relative measure.

## Strongest contrary evidence found

- Price 2004's double standard (read): explaining a past low-entropy condition while
  dismissing a future one is unwarranted; the puzzle becomes cosmological.
- Earman 2006 (secondary only): the PH may be ill-formed in GR — "not even false".
- Wallace 2011 (read): the PH is not an entropy constraint but a probability distribution —
  this cuts against main.tex's and the fixing note's phrasings.
- Dorst 2023 (abstract): modern best-system accounts may render the PH otiose.
- Frisch 2010 (abstract-level): PH-in-best-system must also licence special-science laws.
- Brown 2017 (abstract + fragments): the role of objective probability in both Albert's and
  Wallace's accounts is obscure.

## Limitations

- `web-search-prime` unavailable; coverage rests on scholar_search + exa, so recall may be
  narrower than the brief's ideal (no systematic citation-chasing beyond two hops).
- exa PDF extraction was lossy for North (numerals dropped) and effectively unusable for
  Frisch 2010; both are flagged, and no wording-level claims rest on them.
- Albert 2000 and Price 1996 page references in main.tex (pp. 96; 113–116; 121–122 n. 11;
  pp. 81ff; 132–133) remain unverified by anyone in this lane; READING.md flags them.
- The ΛCDM transfer of the closed-dust fixing corollary in READING.md §4 is explicitly
  marked as conjecture-by-transfer, not proved.
- One published-page diff (Wallace 2011 preprint vs 2023 printing) not done.
- All review is same-family model review; nothing here is expert review.

## Proposed next tasks

1. Verify the Albert/Price page citations in main.tex against physical copies
   (needs user-gated sources per PARITY_MAP.md).
2. Full-text read of Earman 2006 (license or library access) and a diff of Wallace's 2011
   preprint against the 2023 printing.
3. A companion note transferring the mirror/balance propositions to flat ΛCDM with a
   particle horizon (the READING.md §4 conjecture), checked against the horizons lane.
4. Draft the concrete revision of main.tex §sec:direction's Albert sentence and the
   fixing note's "Bearing" paragraph per READING.md §4, for coordinator review.
5. When `web-search-prime` resets (17 Nov), run a supplementary sweep for any named
   defender of the "openness = information imbalance" thesis, to close the novelty check.
