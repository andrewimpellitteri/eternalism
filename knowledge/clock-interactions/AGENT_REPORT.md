# AGENT_REPORT: kb-clock-interactions

Run type: a Claude subagent (Opus) completed this lane after the OpenCode GLM worker
stopped on a provider quota. The work stayed inside the existing worktree and branch
`agent/kb-clock-interactions`. The submission goes to coordinator review and is not
accepted completion.

## Files changed

- `knowledge/clock-interactions/sources.jsonl`: 6 new lane-prefixed records. 3 are
  full-text, 2 abstract and 1 discovery.
- `knowledge/clock-interactions/rc1-neighbours.md`: per-paper table, verbatim findings with
  locators, verdict on the RC-1 case, bearing on RC-5, the refined narrowest case with
  defeaters, and what is unread.
- `knowledge/clock-interactions/sa_example3_check.py`: exact standard-library check of
  Smith-Ahmadi Sec. 4.3.
- `knowledge/clock-interactions/rijavec_backflow_check.py`: check of a consequence we draw
  from Rijavec Eq. (90). It is not the author's claim.
- `AGENT_REPORT.md` (this file).

Existing ids were reused rather than duplicated: `frontier-relational-trinity-2019v3` and
`frontier-smith-ahmadi-interacting-2019`. Their rereads are in `rc1-neighbours.md`, not as
copied jsonl records.

## Sources read and depth

| id | version read | depth |
|---|---|---|
| clockint-rijavec-pw-robustness-2023 | arXiv 2204.11740v3 HTML, all sections and appendices | full-text |
| frontier-smith-ahmadi-interacting-2019 (reused) | arXiv 1712.00081v3 HTML, all sections | full-text reread |
| clockint-mendes-quasi-ideal-2021 | arXiv 2107.11452v1 HTML, all sections and appendices | full-text |
| clockint-garmier-nonideal-qrf-2026 | arXiv 2512.19343v2 HTML, main text Secs. I-VI and App. I. App. F opening only. Apps. B-E, G, H and proofs not read | full-text (main text) |
| frontier-relational-trinity-2019v3 (reused) | arXiv 1912.00033v3 HTML: abstract, Secs. II.2, III.2.2, IV.1 (to Thm 1), V.1, V.2.1 (to Lemma 2), V.3, IX, App. A | interaction passages and conclusions, as the brief asked |
| clockint-periodic-clocks-2024 | arXiv 2409.06479v3: abstract plus Sec. II.2, Ex. 6 with footnote 11, located lines | abstract |
| clockint-singh-friedrich-2023 | arXiv 2304.01263v2 abstract | abstract |
| clockint-cafasso-tdit-2024 | Crossref metadata, arXiv title | discovery |

## Key findings, with locators

1. **Trinity 1912.00033v3.** Sec. II.2 states: "we assume that the clock and system do not
   interact." The equivalence is proved only "for clock Hamiltonians with non-degenerate and
   continuous spectrum" (Sec. V.3). Sec. III.2.3 adds "henceforth considering only
   noncompact clocks". Sec. IX names interactions "the most pressing generalization". The
   existing record slightly overstates discrete-spectrum coverage. A correction is
   proposed in `rc1-neighbours.md`, and that record was not edited.
2. **Periodic trinity 2409.06479v3 (abstract plus passages).** The trinity is extended to
   periodic clocks, finite-dimensional non-ideal two-level clocks included (Ex. 6). Sec.
   II.2 says: "we shall henceforth assume that no interactions between C and S are present."
3. **Smith-Ahmadi 1712.00081v3.** The kernel equation (Eq. 14) holds for general `H_int` in
   the PW picture only. Isometry is equivalent to a t-independent conditional inner product
   that the authors demand (Eqs. 11-12, 15, footnote 1). Ex. 3 (Eq. 24) uses a qubit
   periodic non-ideal clock with `[H_int,H_C] != 0`. Our check confirms
   `H_int Π_phys = 0`, so the example is degenerate. It also finds an apparent sign typo in
   Eq. (26) that does not affect the conclusion.
4. **Rijavec 2204.11740v3.** Interactions are restricted by Eqs. (47)-(48) to
   `[h,V]=0=[H,V]`, giving `V = X⊗h` (Eq. 51). The clock is ideal and its measurements are
   projective (footnote 7). His "Heisenberg picture" is a formal unitary, not the trinity's
   symmetry reduction. The `[V,h] != 0` case is left open (Sec. VII). A mixture over
   total-energy sectors gives a CPTP non-unitary system map (Eq. 70, footnote 21).
5. **Mendes et al. 2107.11452v1.** The clock is a finite-d quasi-ideal clock, only
   approximately covariant, and the interaction `-𝔾 H_S⊗H_C` commutes with `H_C`. The
   analysis is PW only and perturbative. The claimed "non-linear" equation (Eq. 33) gets
   its state dependence from the definition of V (Eq. 52). The derivation does not show
   that the map is non-linear (our reading).
6. **Garmier et al. 2512.19343v2.** The framework is kinematic only, with a product global
   action and no Hamiltonian-constraint dynamics. Non-ideal QRFs give superselection and a
   non-homomorphic relationalization map (Eq. 25). Finite Abelian groups, so Z_N, are
   covered kinematically (App. F). The only time-evolution remark in Sec. V is
   qualitative.

**Verdict on RC-1.** No paper read here answers the case of a finite-dimensional Z_N clock
with a non-ideal covariant POVM, `[H_int,H_C] != 0` and three-picture agreement, or a
strict superset of it. The papers that compare pictures assume no interaction. The papers
with interactions are PW-only, or use commuting interactions, or give one degenerate
example. This is a finding about these papers only, not a novelty claim. Refined case and
defeaters are in `rc1-neighbours.md`.

**Bearing on RC-5.** The sentence in RC5.md that reading-dependent memory "requires
either `[H_int, H_C] ≠ 0` … or a non-covariant, degrading clock POVM" needs a stated
premise: a single constraint surface. Rijavec's commuting-interaction model with a
stationary mixture over two total-energy sectors gives a trace distance of `|cos(θ/2)|`,
with θ linear in t. That is backflow, so the family is not CP-divisible. This is our
derivation from Eq. (90) and was checked numerically. Smith-Ahmadi's t-independence
demand is the place where `[H_int,H_C] != 0` could make normalized conditioning
reading-dependent. That is a conjecture, not a paper's claim.

## Checks run

- `python3 scripts/check_sources.py --online --strict knowledge/clock-interactions`
  (worktree): "1 files, 6 records; 6 arXiv IDs and 3 DOI lookups checked: 0 errors, 0
  warnings, 0 info". The first run, before `text_url` was added for 2407.00161, checked 5
  arXiv IDs with 0 errors.
- Offline check over the whole worktree `knowledge/`: 13 files, 229 records, 0 errors.
  The 17 warnings and 1 info come from other lanes' files, and none involve `clockint-*`
  ids.
- The reused records `frontier-relational-trinity-2019v3` and
  `frontier-smith-ahmadi-interacting-2019` were copied to a scratch file and checked
  online: 2 arXiv IDs and 1 DOI, 0 errors.
- No arXiv-issued 10.48550 DOI is recorded.
- Crossref was queried directly to confirm the journal metadata of 10.1103/PhysRevD.108.063507,
  10.1088/1367-2630/ae46d0 and 10.1103/PhysRevD.110.106014.
- `python3 -I knowledge/clock-interactions/sa_example3_check.py`: commutator norm 0.868,
  `H_int|10> = H_int|01> = 0`, the null space is `span{|01>,|10>}`, and the conditional
  state matches `exp(-iH_S t)` to 0.0 while differing from `exp(+iH_S t)`.
- `python3 -I knowledge/clock-interactions/rijavec_backflow_check.py`: the state is
  maximally mixed at θ=π, `D(θ) = |cos(θ/2)|` on 41 grid points, and D increases 20 times.
  This is a check of one model, not a theorem.

## Web search

WebSearch worked. Three queries were run, two standard and one extended, aimed at
interacting-clock trinity follow-ups. None found a paper treating the RC-1 case. They
surfaced 2409.06479, 2407.00161 and 2604.21805 (clock ambiguity, not read). Fetching
arxiv.org HTML and abs pages with curl worked. No page was blocked or paywalled.

## Limitations

- Garmier et al. appendix proofs, trinity App. C proofs and most of 2409.06479 are unread.
- Two general web searches are not a forward-citation audit.
- Both scripts check single worked models.
- Mendes et al. has a second record, `pw-mendes-nonlinear-pw-2021` (abstract), in the
  unaccepted `kb-pw-critiques` worktree. The coordinator should merge the ids.
- The identification of trinity ref. [84] with 2409.06479 rests on authors and topic only.

## Unresolved questions

1. Does 2409.06479 cover Z_N (discrete-reading) covariant POVMs, and does it say anything
   about interactions beyond Sec. II.2?
2. What interaction class and pictures do Cafasso et al. (2407.00161) and Paiva et al.
   (Commun. Phys. 5, 2022) treat?
3. For a Z_3 clock with `H_int = g σ_x ⊗ |0><0|` on a single constraint surface, is the
   clock-reading marginal of physical states uniform? If it is not, which inner product
   makes the PW map isometric, and is it still equal to the group-averaging inner product?
4. Should RC5.md state the single-constraint-surface premise explicitly, given Rijavec's
   mixed-sector route to backflow?

## Coordinator review (2026-10-20)

- Quotes checked verbatim against arXiv HTML fetched 2026-10-20: 1912.00033v3 ("we assume that the clock and system do not interact"; "the most pressing generalization"; "henceforth considering only noncompact clocks"; "non-degenerate and continuous spectrum"); 1712.00081v3 footnote 1 ("may severely reduce the size of the physical Hilbert space"); 2204.11740v3 Sec. VII ("I leave this problem open for future investigations"); 2409.06479v3 ("we shall henceforth assume that no interactions between C and S are present"; also, earlier, "this would typically also ruin the periodicity of the clock").
- Re-ran `sa_example3_check.py` (commutator norm 0.868; `H_int` annihilates the physical span) and `rijavec_backflow_check.py` (trace distance |cos(θ/2)|, 20 increases on 41 points). Both reproduce.
- `check_sources.py --online`: 6 records, 0 errors.
- Accepted point for RC-5: the uncoupled-clock "no memory" result needs a single constraint surface (pure physical state). A stationary mixture over energy sectors gives backflow even with a commuting interaction. RC5.md is updated accordingly.
- Not re-checked: Mendes et al. and Garmier et al. readings; the claimed Eq. (26) sign typo in Smith–Ahmadi.
