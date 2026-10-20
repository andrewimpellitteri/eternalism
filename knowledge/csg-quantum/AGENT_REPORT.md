# AGENT_REPORT: kb-csg-quantum-boundary

This run was carried out by a Claude subagent (Opus) completing the GLM lane after the GLM worker
stopped on a provider quota. It is a worker submission for coordinator review, not accepted
completion. Date 2026-10-20. Branch `agent/kb-csg-quantum-boundary`.

## Files changed

- `knowledge/csg-quantum/sources.jsonl`: 23 records (16 full-text, 7 abstract).
- `knowledge/csg-quantum/extraction.md`: verbatim extraction with locators, RC-4 verdict, theory
  comparison table, category separation, corrections to the defeat-search notes, narrowest open
  cases, unread list.
- `AGENT_REPORT.md`: this file.

Nothing else was written. The workboard, runner, AGENTS.md and the main checkout were not touched.

## Sources read and depth

**Full-text, all from arxiv.org/html/<id>v<n>** (partial section coverage is stated in each
record's `limits`):

- Surya-Zalel 2003.11311v1 (reuses id `cs-surya-zalel-2020`)
- Brightwell et al. gr-qc/0210061v2 (reuses id `cs-brightwell-2003-observables`)
- Brightwell et al. gr-qc/0202097v1
- Dowker-Surya gr-qc/0504069v1
- Dowker-Johnston-Surya 1007.2725v1
- Srivastava-Surya 2603.25503v1
- Dowker-Imambaccus-Owens-Sorkin-Zalel 1910.07292v2
- Zalel 2302.10582v1
- Brightwell-Luczak 0901.0240v3 and 0901.0242v2 (Sec. 1 only)
- Bento-Dowker-Zalel 2109.10749v1
- Sorkin gr-qc/0703098v1
- Dowker 1405.3492v1 and 2209.07653v2
- Cohen-Cortês-Elitzur-Smolin 1902.05082v3
- Gudder 1405.0638v1 (Secs. 1-2)

**Abstract only:**

- Varadarajan-Rideout gr-qc/0504066
- Sorkin gr-qc/9401003
- Krugly 1106.6269
- Dowker-Zalel 2212.01149
- Zalel 2008.02607
- Ghazi-Tabatabai-Wallden 0901.3675
- Cortês-Smolin 1307.6167

## Key verbatim findings (full quotes and locators in extraction.md)

1. **The RC-4(a) property is published.** Brightwell-Luczak 0901.0240v3 Sec. 1: "They studied such
   processes with the property that, conditional on the causal set at some stage k being equal to
   some unlabeled k-element poset P, each linear extension of P is equally likely to have been the
   order in which the elements were generated. They called this property “general covariance.”"
   Theorem 4.2 gives the DLR-type characterization mu(E) = E_mu nu^k(E).
2. **There is no unique infinite analogue.** 0901.0242v2 Sec. 1: "depending on P, there may be one,
   many, or no order-invariant probability measures". 0901.0240v3 Example 4 and Sec. 7 give
   extremal mu_q for every q on two infinite chains. Our construction (extraction Sec. 3.A, needs
   independent check): DGC walks with identical covariant measure but different labelled measures,
   separated by a tail birth-order statistic.
3. **Non-DGC labelled dynamics are invisible in stem events as such.** 1910.07292v2 Sec. 5: "for
   every walk on labeled poscau – whether it satisfies Discrete General Covariance or not – there
   exists a covtree walk that produces the same measure on R(S)." Concrete non-DGC models are in
   2109.10749v1 Claim 3.5.
4. **Quantum extension.** Surya-Zalel Theorem 2.1 states that extension holds iff bounded variation.
   Theorem 3.1 and Claim 3.8 give the criteria. Sec. 2: "no event alpha in Z can be covariant
   unless alpha=Omega". DJS 1007.2725v1 Lemma 1 proves non-extension for non-real p. DJS Sec. 5:
   "the events in A are not themselves observables" and a proposed conditional convergence "with
   the conditionality determined by a preferred ordering of events".
5. **The phase loophole was flagged and set aside.** 2603.25503v1 Sec. 3.1 Note: "It is also
   possible to introduce a phase |c_n> = e^{i Phi}|c_n'> since this will leave the quantum measure
   invariant ... we do not consider this option henceforth." Sec. 4 repeats this for
   path-dependent phases.
6. **Observer access.** No formal observer or record model exists in any source. The nearest is
   gr-qc/0202097v1 Sec. 7: "this particular copy of S1 (the S1 that “we inhabit”)" might need "a
   logically independent concept of conditional probability". Other observer material is
   philosophical (Dowker 2209.07653v2 Secs. 4.3-4.6; Sorkin gr-qc/0703098v1 Sec. 5). In this
   literature "observable" means beable (gr-qc/0210061v2 Sec. 1; 2109.10749v1 footnote).

## Verdict on RC-4

The finite-stage classical part of RC-4(a) is killed and attributable to Brightwell-Luczak. Two
narrow cases remain, neither found treated:

- **(α)** A bridge-premise question: whether any embedded record can correspond to a non-covariant
  event, either stage-indexed or a tail statistic of birth order. This is the only route by which
  growth order could become "observable".
- **(β)** Two quantum questions:
  - norm-only-covariant QSG with path-dependent phases and an extending measure;
  - ordering-dependence of conditional-convergence prescriptions in non-extending complex models.

Section 8 of extraction.md lists the reads most likely to defeat each case.

## Checks run

- `python3 /Users/andrew/eternalism/scripts/check_sources.py --online <worktree>/knowledge/csg-quantum/sources.jsonl`
  gave: 1 file, 23 records, 23 arXiv IDs and 12 DOI lookups, 0 errors, 0 warnings.
- The same command with `--strict` gave 0 errors and 0 warnings.
- **Gudder DOI dropped.** The first online run gave one warning: the Gudder DOI 10.3390/axioms4010102
  resolves to a different published title ("A Model for the Universe that Begins to Resemble a
  Quantum Computer"). I removed it as an identifier of the text read and noted the discrepancy in
  the record.
- **Expected warnings from the combined check.** An offline run over the main `knowledge/` together
  with this file gives 0 errors. It gives the two expected WARNs: `cs-surya-zalel-2020` and
  `cs-brightwell-2003-observables` diverge in read_depth (discovery in
  `knowledge/causal-sets/sources.jsonl` on main, full-text here). These IDs were reused
  deliberately as instructed. The coordinator should make the full-text records canonical or
  merge them.
- No arXiv-issued 10.48550 DOIs are recorded.
- No dependency installs and no code runs beyond source fetching and the checker. The Sec. 3.A
  construction is a hand derivation with no numerical check.

## Limitations

- **Locators.** They are section, equation and theorem numbers from LaTeXML HTML renders. No PDF
  page numbers are given. Math inside quotes is simplified from alttext.
- **Versions.** Publisher versions behind recorded DOIs were not compared with the arXiv versions
  read.
- **Authors' results taken as claims.** Several long papers were read only in part (listed in
  each record). Srivastava-Surya's commutativity results and Brightwell-Luczak Sec. 8 proofs are
  taken as authors' claims.
- **Sec. 3.A and 3.C-3.D are ours.** They are labelled as such, are classical (3.A) or
  conjecture-level (3.D), and need an independent check. Whether any Bell-causal CSG model shows
  the infinite-limit non-sufficiency was not checked.
- **Web search** (WebSearch, arXiv listing and API, Crossref) worked. It is not a systematic
  search, so absence of an observer or record paper is "not found", not "does not exist".

## Unresolved questions

- Brightwell's unpublished notes on general covariance (cited by Sorkin gr-qc/0703098v1 [7]) are
  unread and probably not public.
- Sorkin-Surya "Constructing covariant observables in complex percolation" (cited as in
  preparation) was not found.
- Sorkin MSCS 2012 conditional-convergence paper: not read; arXiv ID not identified.
- Is the covariant sigma-algebra R countably generated? Zalel 2302.10582v1 Sec. 2.3 lists this as
  open.
- Does a quantum covtree walk exist in the literature (1910.07292v2 Sec. 5 (v))? Not searched
  beyond author listings.

## Coordinator review (2026-10-20)

- Checked verbatim against arXiv HTML fetched 2026-10-20: Brightwell–Luczak 0901.0240v3 Sec. 1 ("…each linear extension of P is equally likely to have been the order in which the elements were generated. They called this property 'general covariance.'"); covtree 1910.07292v2 Lemma 4.9 discussion ("whether it satisfies Discrete General Covariance or not – there exists a covtree walk that produces the same measure"); Bento–Dowker–Zalel 2109.10749v1 Alternating Transitive Percolation definition.
- Consequence for RC-4: the coordinator's finite-stage "birth order is ancillary" derivation (crosswalk, 2026-10-19) is Brightwell–Luczak's order-invariance property, already read as Rideout–Sorkin general covariance. Credit it to them.
- Not verified: the hand construction in extraction Sec. 3.A (q-family of DGC walks with equal covariant measures and different labelled measures). It is the lane's derivation and needs an independent check before it is used.
- Duplicate IDs `cs-surya-zalel-2020` and `cs-brightwell-2003-observables` now have records at two depths (discovery in causal-sets, full-text here); for rt-source-canonicalization.
- `check_sources.py --online`: 23 records, 0 errors.
