# clock-three-picture

Claude session, 2026-10-21. Fallback probe for RC-1/RC-5 (contract in
`research/redteam/loadbearing-rereads/RC1.md` and `RC5.md`). This is at most a
worked application of known constructions. Nothing here is a novelty claim.

## Files

- `SPEC.md`: the model, conventions and quantities, fixed before replication.
- `linalg.py`: standard-library complex linear algebra (Jacobi eigensolver on the
  real embedding; residuals checked for every eigenvector).
- `model.py` → `model_output.txt`: all computations (sections 1–8).
- `independent/`: an independent re-implementation from SPEC.md only, and its
  comparison with `model_output.txt` (see "Independent check").
- `literature.md`: the defeater read (see "Prior work").

## Model

Z_3 clock (`H_C = diag(0,1,2)`, ideal readings `|τ_k⟩`), qubit `H_S = σ_z/2`,
`H_int = g K ⊗ σ_x`, default `K = |τ_0⟩⟨τ_0|` with `‖[K, H_C]‖ = 0.667`.
Physical states are unit vectors in one eigenspace ("surface") of the constraint
operator. Non-ideal covariant POVM with blur d = 0.1.

## Results

| # | Claim | Evidence (model_output.txt) |
|---|---|---|
| R1 | Dirac and Page–Wootters expectations coincide on physical states for any interaction: `⟨G[E_k⊗O]⟩ = ⟨E_k⊗O⟩` | Sec. 5: max difference 5.6e-17. It holds because physical states are exact eigenvectors in a finite model; a one-line identity, not a computation-specific fact. |
| R2 | The trinity can therefore fail only at normalization: reading probabilities `p(k)` and the isometry of `R(k)` | Sec. 3 (g = 0 control): p = 1/3, isometry defect 2e-16, conditional states evolve by `e^{−iH_S t_k}` (infidelity 4e-16). |
| R3 | In this model, the non-commuting K makes `p(k)` non-uniform and `R(k)` non-isometric; the commuting control does not. Not a general law (see Answer) | Sec. 4: e.g. g = 0.5, p_ideal = 0.40/0.30/0.30, defect 0.21; non-ideal readout has the same pattern, smoothed. Sec. 7: commuting K, p = 1/3 to 1e-6, defect ≤ 4e-16. |
| R4 | A generic non-commuting interaction splits every degenerate surface into one-dimensional ones | Sec. 1 and 6: all surfaces have dim 1 for g ∈ {0.05, 0.2, 0.5, 1} and three choices of K, except one level crossing. Known limit (Sec. 2): first-order splitting ±0.3333 g predicted, ±0.3334 g at g = 1e-3. |
| R5 | So on a single generic interacting surface there is no family of initial system states and no dynamical map; the four memory criteria are undefined, not failed | Follows from R4. |
| R6 | On the accidental two-dimensional surface (K = `|0⟩⟨1|`+h.c., g = 1 exactly; separate at 0.99 and 1.01), reduced maps are non-isometric and trace distance revives (forced by period-3 return) | Sec. 8: eigenvalues of `A_k†A_k` = 0.2087, 4.7913 for k = 1, 2; all three step propagators have the same; 200/200 random pairs show an increase. A periodic non-isometric family must revive. |

## Memory-criteria table

| Setting | Semigroup | CP-divisibility | Backflow | Process tensor |
|---|---|---|---|---|
| Uncoupled, covariant non-ideal POVM, single surface (RC5.md check) | fails only because Φ_0 = D ≠ id | holds (unitary propagators) | none | not computed |
| Commuting interaction, 2-d surface (Sec. 7) | holds: `A_1` unitary, `A_2 = A_1²`, `A_1³ = 1` (checked to 1e-15 at g = 0.2, 0.5, 1) | holds | none | not computed |
| Generic non-commuting interaction, single surface (R4) | undefined: no map | undefined | undefined | undefined |
| Accidental 2-d non-commuting surface (R6) | no (non-isometric, period 3) | linear unnormalized propagators are single-Kraus CP but not trace-non-increasing (gain 4.79), so not CPTP-divisible; normalized maps are non-linear | revival forced by periodicity; not backflow in the standard sense, since the normalized maps are nonlinear | not computed: needs a choice of multi-time clock-readout instrument |
| Stationary mixture over several surfaces (Rijavec-type, from `kb-clock-interactions`) | — | fails | yes, even with commuting coupling | not computed |

## Answer to the probe (after the literature check)

- **Where the reductions first differ.** Not in expectation values (R1, an
  identity). In this model they differ at normalization as soon as the
  non-commuting K is switched on (R3). That is **model-specific**: published
  finite-dimensional examples have non-commuting interactions with unit-norm
  conditional states (Smith–Ahmadi 1712.00081 Sec. 4.3, where the interaction
  vanishes on the surface; Boette–Rossignoli 1806.00956 Sec. II; Ludescher et al.
  2607.24976 Example 32). The closest general statement is Cafasso et al.
  2407.00161v2 Sec. VI: the normalization "coefficient can only be constant in t
  if the constraint is of the type discussed in Sec. IV".
- **Whether a memory criterion separates.** With the constraint written as an
  eigenvalue equation for a generic interacting H, each surface is
  one-dimensional (R4), so there is no map to test (R5). This depends on the
  formulation. Written as invariance under one clock step (Boette–Rossignoli;
  Hausmann et al. 2308.10967 Sec. 5) or as a Z_n group action (Ludescher et al.),
  the physical space keeps its dimension with interactions. The non-interacting
  version of R4 is already in Chataignier et al. 2409.06479v3 ("H_phys can be at
  most one-dimensional ... and the relational theory is thus trivial"; Sec. II.2:
  interactions "unless fine-tuned" ruin periodicity).
- **R6 relabelled.** The revival on the accidental surface is forced by period-3
  return (A_3 = A_0) and shows only non-unitarity. Because the normalized maps are
  nonlinear and not CPTP, calling it information backflow or CP-indivisibility in
  the standard sense is not supported (Rijavec 2504.01579 Sec. II: this
  non-unitarity "is different from the non-unitary dynamics of open quantum
  systems"). The table entry is kept as "revival", not "backflow".

## Limits

- One model family: N = 3, a qubit, commensurate ε = ω, three choices of K, five
  couplings. Floating point with 1e-7 eigenvalue clustering; "dim 1" is numerical,
  confirmed against first-order perturbation theory, not proved.
- R4 is generic, not universal, and formulation-dependent (above).
- The relational observable used in R1 is the full average over all surfaces;
  the literature's is the twirl over one clock cycle (Chataignier et al. Eq. 66),
  a different object once there is an interaction. R1 is a trivial identity.
- The process-tensor criterion is not computed; it needs a definitional choice
  of multi-time readout.

## Independent check

`independent/` (Claude subagent, wrote its code from SPEC.md only, compared with
`model_output.txt` last): every printed quantity agrees, items 1–8, using a
different eigensolver (Householder tridiagonalization, Sturm bisection, null
spaces by Gaussian elimination; residuals ≤ 1.3e-15). Its caveats are accepted:
the 100% revival is forced by periodicity; `A_k` as specified does not depend on
the surface basis at all; the spec does not fix g and K for items 4–5 or the basis
for item 7.

## Prior work

`literature.md` (Claude subagent; 33 quotes checked by script against arXiv HTML;
the coordinator re-checked three: Chataignier et al. "can be at most
one-dimensional", Cafasso et al. "can only be constant in t", Boette–Rossignoli
"will contain S−T interaction terms"). Verdicts: F1 immediately implied
(Hausmann et al. App. F); F2 partly covered and, as unqualified wording, defeated
by three published examples; F3 partly covered (non-interacting version
published), formulation-dependent; F4 not found as stated, and its "backflow"
label rejected.

## Novelty verdict

**Application and known-result reduction only. Nothing here survives as a new
result.** The probe's useful output is negative and methodological:
- the RC-1/RC-5 "interacting finite clock" contract does not have a single
  well-posed answer; it depends on the constraint formulation (eigenvalue
  equation vs. step invariance vs. group action) and on fine-tuning;
- the RC-5 memory question needs a dynamical map, which a generic interacting
  eigenvalue-constraint model does not supply;
- any future work here must start from Cafasso et al., Boette–Rossignoli and
  Ludescher et al. Example 32, not from the trinity papers.
