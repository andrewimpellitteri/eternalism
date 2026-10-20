# Selection decision ledger — 2026-10-20

Gate: `rt-selection-decision-gate`. Inputs: the independent novelty audit
(`research/novelty-audit/AGENT_REPORT.md`), the five load-bearing rereads
(`research/redteam/loadbearing-rereads/RC1–RC5.md`), the audited
complex-percolation candidate (`research/creative/CLAIM_CONTRACT.md`,
`RESULT.md`, `COVARIANT_RESULT.md`, and the three `ctp-*` audit reports), and
the theory-map contracts. No score, vote or weighted composite is used.
Selection is not a priority certificate.

## Decision

**Primary target: the labelled doubly-principal scalar complex-measure
classification** for complex transitive percolation (the `RESULT.md` theorem
draft).

**Fallback target: RC-1**, the finite `Z_N` clock with a non-ideal covariant
POVM and a clock–system interaction with `[H_int,H_C] ≠ 0`, testing agreement of
the Dirac, Page–Wootters and relational-Heisenberg reductions on one constraint
surface.

**Not selected, and archived as dead or conditional:** see the ledger below.

## Why the primary

1. It is the only candidate with a **complete theorem draft** and an
   **independent fresh proof audit** that found no falsifier
   (`research/creative/proof-audit/AUDIT.md`), plus an exact finite certificate
   (`verify_small.py`) and a second proof route.
2. Its direct predecessor **explicitly leaves the exact question open**.
   Dowker–Zalel 2212.01149v2, Sec. V (read in the priority audit and re-checked
   here): their application to Complex Transitive Percolation on
   doubly-reduced poscau "is inconclusive"; they cannot prove extension because
   `ζ ≥ |p|+|1-p|-1`, and cannot rule it out because level-`n` nodes with
   valency 1 make `ζ_n^min = 0`; the valency-one sum "in future it could be
   computed using techniques similar to those used to obtain the probability of
   a post [17]."
3. The candidate supplies exactly that missing lower bound. The prior-work
   delta is therefore not a broad framework claim; it is a named open case in a
   named paper. This is the strongest evidence in the whole pool.
4. It is reproducible at small finite order without new dependencies, and its
   finite certificate is already checkable by a second route.

The counterweight is recorded first in `AGENT_REPORT.md`: the estimate may be a
short corollary of Dowker–Zalel's criterion, external mathematical acceptance
and global priority are unverified, and the physical/ontological relevance is
nil without a bridge model.

## Why the fallback

RC-1 is the only temporal-clock contract with a clear, bounded operational
question and no read source closing it. It is not primary because the
novelty audit found the class underspecified, and the closest neighbours
(Ludescher 2607.24976, Hausmann 2308.10967) were not read at the exact
three-picture scope. It is a legitimate fallback: small, reproducible, and
squarely about clock time rather than causal-set measure theory.

## Ledger

| Contract / candidate | Disposition | Kill/archive reason (traceable read) |
|---|---|---|
| Primary: labelled doubly-principal classification | **SELECTED** | Direct predecessor leaves the exact valency-one/doubly-principal question open (Dowker–Zalel v2 Sec. V); independent proof audit found no falsifier; exact finite certificate exists. Priority and external acceptance remain unresolved. |
| Conditional covariant common-tail-factor theorem | **CONDITIONAL, not selected** | Requires an added common factor `ν(D_H)=κN(H)A_p(H)` for **all principal** post pasts plus cyclic normalization (`COVARIANT_RESULT.md`, `covariant-boundary/BOUNDARY.md`); not a consequence of covariance; the doubly-principal-only weakened rule has a Dirac counterexample. Keep as a follow-up, not the target. |
| RC-1 interaction-dependent clocks | **FALLBACK** | No read source closes the finite `Z_N`, non-ideal covariant POVM, `[H_int,H_C] ≠ 0`, three-picture case: HSL 1912.00033 and 2409.06479 assume no interaction; Smith–Ahmadi 1712.00081 is PW-only and its Example 3 is degenerate; Rijavec 2204.11740 restricts to `V = X⊗h`; Garmier 2512.19343 is kinematic. Lost to primary on mathematical concreteness and because the novelty audit calls the class underspecified. |
| RC-2 premise-dependency classification | **KILLED as a new-theorem claim; formalization-only archived** | Clifton–Hogarth 1995 p.365 gives the uniqueness trichotomy under implicit definability + transitivity + `I⁻ ⊆ B`; p.376 Corollary 2 gives the Malament-type no-go; pp.376–380 give countermodels for privileged worldlines. No premise-necessity table exists, but a finite enumeration table is a formalization, and formalization prior art was not searched. Reopen only as a formalization task with a repository search. |
| RC-3 sector-coherent conditioning no-go | **KILLED as stated** | HSL 2007.00580 after Eq. (33): sector coherence "is not physically accessible" and superpositions/mixtures are indistinguishable; the external-frame route is argued to violate gauge invariance. Hosseini–Lock 2604.00092 gives the normalization obstruction and sector-wise partial-isometry remedy. Only the lane's reflection-refined POVM conjecture remains, unchecked and possibly excluded by the observable algebra. |
| RC-4 classical record distinguishability | **KILLED** | Rideout–Sorkin general covariance; Brightwell–Luczak 0901.0240v3 Sec. 1 states the order-invariance/linear-extension property, Theorem 4.2 gives the DLR characterization. The finite-stage birth-order result is published, not a new derivation. |
| RC-4 quantum phase / ordering remainders | **ARCHIVED, small computation** | Srivastava–Surya 2603.25503 explicitly sets the path-dependent phase option aside; Dowker–Johnston–Surya 1007.2725 asks for a preferred-ordering conditional convergence and its uniqueness. Both are at most small computations in a known framework; no ontology consequence without a bridge premise. |
| RC-5 generic four-criterion separation | **KILLED as a result claim** | The separations are published: Chruściński–Kossakowski–Rivas 2011 (CP-divisibility vs backflow), Milz et al. 2019 (CP-divisibility vs process-tensor memory). Nandi–Petruccione 2606.08595 Eq. (10) is a second-order TCL kernel statement, not a map family, and tests none of the four criteria. Only an application to RC-1's model remains. |
| RC-5 application to the RC-1 model | **MERGED INTO RC-1 FALLBACK** | The interacting finite-clock map family is shared; the combined contract is in `loadbearing-rereads/RC1.md`. No separate target. |
| Broad candidates A, B, C | **KILLED as stated; archived** | Novelty audit and `STATUS_2026-10-19.md`: A's classical covariant-growth core is occupied; B is substantially occupied by 2308.10967 and the clock literature; C's simultaneity side is occupied by Malament/Besnard, and the RPM side by Clifton–Hogarth/Czerniawski/Thyssen. |
| Creative clock certificates / clock memory / covariant stopping | **NOT SELECTED** | Derived finite checks and a covariant stopping boundary, but each reduces to a known instrument or stopping result at the read depths; the selection gate receives the complex-percolation candidate as the strongest creative output. No selection here. |

## What is explicitly killed so it stops consuming lanes

- RC-2 "new classification theorem" framing (keep only formalization).
- RC-3 no-go as a novel result (keep only the conditional reflection
  conjecture, and only if Marolf/BRT do not exclude it).
- RC-4 classical finite-stage distinguishability (published).
- RC-5 generic criterion-separation result (published).
- Broad A/B/C as standalone targets (occupied).

## Re-run triggers

- Primary: reopen the gate if (a) Dowker–Zalel or a citing work already proves
  the same prescribed-value estimate, (b) an external referee finds a gap in
  `RESULT.md`, or (c) the finite certificate contradicts the analytic bound.
- Fallback: reopen RC-1 if Ludescher et al. 2607.24976 or a forward citation
  already computes the same three-picture comparison for a non-commuting
  finite-clock interaction.
- RC-2: reopen only with a formalization-prior-art search and a full-text
  Callender 2000/Bigaj 2008 read.
- RC-3: reopen only after Marolf gr-qc/9508015 and BRS RMP 79 are read and the
  reflection POVM is checked.
