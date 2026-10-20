# rt-loadbearing-rereads-rc — coordinator second read of RC-1…RC-5

Status: 2026-10-20. Claimed by `opencode-coordinator` because the GLM quota was
exhausted. This is a second-reader task, not another abstract search. The
deliverables are the five reread files in this directory plus this report. No
result here is called novel or open.

## Verdicts

| Contract | Verdict | One-sentence remainder |
|---|---|---|
| RC-1 interaction-dependent clocks | **SHRINK** | For a finite `Z_N` clock with a non-ideal covariant POVM, one constraint surface (pure physical state), and `[H_int,H_C] ≠ 0` acting non-trivially on the physical subspace, do the Dirac, Page–Wootters and relational-Heisenberg reductions agree? |
| RC-2 premise dependency (Stein/Malament) | **SHRINK** | A finite, machine-checked premise-necessity and non-interchangeability table, with a countermodel for each dropped premise and explicit bridge premises; the uniqueness theorem itself is Clifton–Hogarth's. |
| RC-3 sector-coherent conditioning | **SHRINK** | Whether sector-mixing operators commuting with the constraint (e.g. the clock reflection) are admissible physical observables, and if so what normalized probabilities a two-outcome reflection-refined POVM gives. |
| RC-4 record distinguishability in growth | **SHRINK** (classical finite-stage part **KILLED**) | In quantum sequential growth with norm-only covariance and path-dependent phases, do phases change the quantum measure of covariant events; and do non-extending complex models depend on the preferred ordering used for conditional convergence? |
| RC-5 four memory criteria | **SHRINK** | For a finite clock coupled to a qubit with `[H_int,H_C] ≠ 0`, under linear conditioning and a fixed multi-time instrument, which of semigroup failure, CP-indivisibility, backflow and process-tensor memory hold, and do any two come apart? |

No contract is KEEP. No contract is shown novel. RC-1 and RC-5 now share the
same smallest open object and have a combined contract in `RC1.md`.

## What was independently re-read

All pages were fetched as arXiv LaTeXML HTML on 2026-10-20; the Clifton–Hogarth
primary is the user-supplied printed scan with OCR layer. The per-file locators
and verbatim quotes are in the RC files; the decisive passages are:

**RC-1.**
- Rijavec 2204.11740v3, Eqs. (46)–(51): Eq. (47) `[H⊗I + I⊗h, V] = 0`; Eq. (48)
  `[I⊗h, V] = 0`; Eq. (51) `V = X⊗h`. Eq. (48) forces `V` to commute with the
  clock Hamiltonian, so `[H_int,H_C] ≠ 0` is outside the class. Sec. VII leaves
  the `t̂`-non-invariant interaction open.
- Smith–Ahmadi 1712.00081v3, Eq. (14) (PW-only modified Schrödinger equation),
  Eq. (15) (isometry condition), Example 3/ Eq. (24): `||[H_int,H_C]|| = 0.868`
  but `H_int|10> = H_int|01> = 0`; the null space is `span{|01>,|10>}`, so the
  example is degenerate. Eq. (26) has a sign typo (prints `e^{+iH_S t}`; the
  conditional state is `e^{-iH_S t}`).
- Garmier et al. 2512.19343v2: kinematic framework (global action, relational
  map, incoherent group averaging), superselection range in Sec. IV, only a
  qualitative time-evolution remark in Sec. V; finite Abelian groups covered
  kinematically, no Hamiltonian-constraint dynamics.
- Höhn–Smith–Lock 1912.00033v3: no clock–system interaction; non-degenerate
  continuous spectrum; noncompact clocks; interactions named the pressing
  generalization. Chataignier et al. 2409.06479v3: no interactions; they would
  ruin periodicity.
- Cafasso et al. 2407.00161v1 (the named falsifier): finite-dimensional
  Page–Wootters, but the interaction is inside the composite clock
  (time-dilation transfer); the system does not interact with the clock, and no
  three-picture comparison. Not a defeater.

**RC-2.**
- Clifton–Hogarth 1995: p.361 implicit definability as automorphism invariance;
  p.362 chronological `I⁻ ⊆ B` (not Stein's `J⁻`); p.364 Lemma; p.365 Theorem 1
  trichotomy `I⁻`, `J⁻`, `U`; p.367 Corollaries 1(A)/(B); pp.371–372 Theorem 2;
  p.376 Corollary 2; pp.376–380 privileged-worldline countermodels.
- No premise-necessity theorem: only time-orientation and the
  no-privileged-worldlines condition receive countermodel evidence. Transitivity
  and worldline transitivity are motivated, not ablated.

**RC-3.**
- HSL 2007.00580v1: sector coherence "is not physically accessible"; external
  reference frame "seems unsuitable here" and lifting would violate gauge
  invariance; footnote 14 contains only the example, while the "no
  superselection" clause is main text.
- Hosseini–Lock 2604.00092v1: physical expectation values insensitive to
  σ-coherence; naive map non-invertible and not state-independently
  normalizable; maps "must be defined sector-wise" and are partial isometries;
  Appendix A Eq. (42) isometry iff. Free particle, no detector/finite
  resolution/interaction.

**RC-4.**
- Brightwell–Luczak 0901.0240v3 Sec. 1: order-invariance / general covariance;
  Theorem 4.2 DLR characterization. This is Rideout–Sorkin's property,
  characterized by Brightwell–Luczak. The finite-stage classical part is killed.
- Surya–Zalel 2003.11311v1 Thm 2.1 (bounded variation iff extension), Thm 3.1,
  Claim 3.8, "no event α∈Z can be covariant unless α=Ω".
- Covtree 1910.07292v2 Sec. 5: every labelled walk, DGC or not, has a covtree
  walk with the same covariant measure.
- Srivastava–Surya 2603.25503v1: path-dependent phases leave the quantum measure
  invariant and are explicitly set aside; outlook leaves them to future work.
- Dowker–Johnston–Surya 1007.2725v1: non-extending complex models would need a
  conditional convergence fixed by a preferred ordering; uniqueness is not
  established.

**RC-5.**
- Nandi–Petruccione 2606.08595v1 Eq. (10): second-order TCL equation with memory
  kernel, no map family or composition law. Supplement Eq. (23) gated
  environmental operator, Eq. (24) interaction density, Eq. (31) plain partial
  trace, after Eq. (46) "generically non-Markovian" kernel statement. The words
  divisibility, backflow and process tensor never occur. The four criteria are
  not tested; their generic separations are published.

## Disagreements with the underlying lanes (explicit, unresolved)

1. **RC-1 / `kb-clock-interactions`:** the lane's record may overstate
   `frontier-relational-trinity-2019v3`'s discrete-spectrum coverage; correction
   left to source canonicalization. The lane reads Mendes et al. 2107.11452 as
   not demonstrating the claimed non-linearity; not re-checked here.
2. **RC-1 / Smith–Ahmadi:** the lane calls Eq. (26) a sign typo; this reread
   confirms the sign mismatch but not the published-version comparison (the
   arXiv v3 is what was read).
3. **RC-2 / `kb-putnam-ablation-prior`:** before the scan, the lane knew CH's
   theorems only via Savitt. The primary confirms Savitt's candidate list and
   CH's chronological premise; Thyssen fn51 and Saunders p.3 are too strong.
4. **RC-3 / defeat search:** the earlier note called the external-reference
   sentence "cut off" and named the external-phase-reference case as the
   remainder. The sentence is complete and argues against that route. The
   footnote-14 attribution was also wrong in the first draft; corrected.
5. **RC-3 / lane reading of 2409.06479 Example 14:** the lane reads it as
   counting sector-mixing operators among Dirac observables. The coordinator
   review already flagged that the example's opening does not say this; it
   remains unresolved and load-bearing for the reflection conjecture.
6. **RC-4 / defeat notes:** the finite-stage ancillarity was presented as a
   coordinator derivation needing checking. It is published (Rideout–Sorkin;
   Brightwell–Luczak characterization) and should be credited.
7. **RC-4 / source IDs:** `cs-surya-zalel-2020` and
   `cs-brightwell-2003-observables` exist at discovery and full-text depth in
   different lanes; canonicalization is still owed.
8. **RC-5 / audit lane:** the defeat note says conditioning acts as
   postselection with normalization and the state evolves nonlinearly. The
   supplement's derivation is a linear trace-preserving per-τ map; the
   nonlinearity is announced in the main text but does not enter the derivation.
   Also, the linear-channel argument needs `F_σ` real-valued, which the paper
   implies but does not state.
9. **RC-5 / `kb-clock-interactions`:** the lane's Rijavec backflow derivation
   uses a stationary mixture over energy sectors; it is the lane's derivation,
   not Rijavec's claim, and was only numerically spot-checked.

## Surviving claim contracts (NOVELTY.md gate)

- **RC-1 + RC-5 combined** — in `RC1.md`, with RC-1's `Z_3`/`Z_N` model and
  RC-5's criteria. Nearest predecessors, delta, smallest example, falsifier and
  novelty kind are listed there. Read Cafasso et al. at full text before any
  computation is presented as new; this reread only read its abstract and
  Secs. I–II.
- **RC-2** — in `RC2.md`. Formalization/bridge-separation target; the
  uniqueness theorem is not new. Read Besnard and Andréka full text first.
- **RC-3** — in `RC3.md`, marked **conditional**: read Marolf gr-qc/9508015 and
  Bartlett–Rudolph–Spekkens at full text before writing the final contract. The
  reflection-refined POVM is the lane's unchecked conjecture.
- **RC-4** — in `RC4.md`. At most a small computation in a known framework; the
  phase option is explicitly set aside by the named predecessor.

No contract is written for a KILL verdict. No one-page draft calls a sliver
novel or open.

## Checks run

- `python3 scripts/check_sources.py --strict knowledge/putnam-ablation` and
  `--online`: 15 records, 0 errors.
- `python3 scripts/check_sources.py --online knowledge/clock-interactions
  knowledge/sector-conditioning knowledge/csg-quantum
  knowledge/relational-markov`: lane records revalidated (lane reports already
  record their own counts; no errors).
- `python3 -I knowledge/clock-interactions/sa_example3_check.py` reproduced:
  commutator norm 0.868; `H_int` annihilates the physical span; conditional
  state matches `e^{-iH_S t}`.
- `python3 -I research/redteam/loadbearing-rereads/rc5_zn_check.py` (existing
  coordinator script) is a finite check of the uncoupled clock; not re-run as a
  proof.
- `python3 -m unittest discover -s tests`: 88 tests pass (run before the
  rereads; no code was changed here).

## Limitations

- HTML-only reads of arXiv versions; no PDF or published-version comparison for
  the quantum-clock, QSG and CSG papers. The Clifton–Hogarth read is a scan with
  OCR symbol garbling.
- Lane reports were inputs; only the passages listed above were independently
  re-read. Garmier's appendices, Chataignier et al.'s appendices, Mendes et al.,
  Bento–Dowker–Zalel 2109.10749, Marolf gr-qc/9508015, BRS RMP 79, Callender
  2000, Bigaj 2008, Stein 1991 printed pages, and Malament 1977 remain unread.
- The finite checks (Smith–Ahmadi, Rijavec backflow, `Z_N` uncoupled clock) are
  one-model checks, not theorems.
- No search was run for this task beyond the named papers; absence of a hit is
  not evidence of absence.

## Unresolved questions

1. Does Callender 2000 already give the RC-2 necessity table? Does Bigaj 2008
   give the independence result?
2. Is the RC-3 reflection-refined POVM admissible and normalizable, or excluded
   by the relational-Dirac-observable algebra? Marolf is the likeliest
   defeater.
3. Does the RC-4 phase option change any covariant quantum measure, or is it
   inert by construction? Does the preferred-order conditional convergence
   change predictions in non-extending complex models?
4. Is there a published computation of RC-1's three reductions or RC-5's four
   criteria for an interacting finite clock? Cafasso et al. is the closest known
   neighbour and does not do this.
5. Do the unresolved lane disagreements above change any verdict if the
   unread sources are read? The verdicts are version- and passage-specific.
