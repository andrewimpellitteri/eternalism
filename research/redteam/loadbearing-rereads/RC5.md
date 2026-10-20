# RC-5 reread: four memory criteria for clock-conditioned maps

Coordinator draft, 2026-10-20. Written before the parent task
`rt-loadbearing-rereads-rc` could be claimed, because RC-5's one blocking input
(`kb-relational-markov-audit`) was accepted first (merge 9a0dc93). Not a novelty
claim.

## Verdict: SHRINK

Remaining case, in one sentence: *a finite clock whose conditioned system maps
carry reading-dependent memory, which requires either a clock–system interaction
with `[H_int, H_C] ≠ 0` (shared with RC-1) or a non-covariant, degrading clock
POVM, with the multi-time instrument fixed before any criterion is computed.*

## What was re-read, and what it shows

**2606.08595v1 (Nandi–Petruccione), arXiv HTML fetched 2026-10-20.** Verbatim checks:

- Before Eq. (10): "Applying the clock instrument and tracing over the bath and
  clock sectors yields a covariant time-convolutionless master equation for the
  conditioned reduced state (see Supplemental Material)".
- After Eq. (7): "the normalized conditioned state evolves nonlinearly due to
  relational conditioning."
- Supplement Eq. (23): `Ê_α(x;τ) = F_σ(T̂(x) − τ(x)) B̂_α(x)`, inside the
  interaction density, Eq. (24). Eq. (31): `ρ_S^I[Σ;τ] = Tr_Ξ(ρ_tot^I[Σ])`, a
  plain partial trace.
- Supplement, after Eq. (46): "Equation (44) is generically non-Markovian because
  the conditioned state … depends on the causal history encoded in the dressed
  relational kernel."
- The full text never uses "divisib", "backflow" or "process tensor".
  "Semigroup" appears only as GKLS/Lindblad background and in citations.

So Eq. (10) establishes a second-order, kernel-shaped generator for the
subnormalized state and none of the four criteria. This confirms the lane's Q2
verdict. Classifying it is an audit output, not a result.

**General separations of the criteria (abstract depth, identifiers verified 2026-10-20):**

| Separation | Source | Status |
|---|---|---|
| CP-divisibility vs. distinguishability backflow | Chruściński, Kossakowski, Rivas, arXiv:1102.4318v2, PRA 83, 052128 (2011): "these two measures need not agree" | published |
| CP-divisibility vs. multi-time (process-tensor) memory | Milz, Kim, Pollock, Modi, arXiv:1901.05223v2, PRL 123, 040401 (2019): CP-divisible processes "can still involve non-Markovian temporal correlations" | published |
| Semigroup vs. CP-divisibility | project correspondence case 5 (Gaussian dephasing `exp(-t²/2)`) | standard |
| Review of backflow, CP-divisibility and process-tensor frameworks | Gangwar, Sen, arXiv:2603.28277v3 (2026) | abstract only; no clock or relational-time content in the abstract |

A generic model separating the criteria would be an application of these
results, so that part is killed as a result claim.

**Uncoupled finite clock (coordinator computation, `rc5_zn_check.py`).** Take a
Page–Wootters qubit with an uncoupled `Z_N` clock and any covariant,
non-ideal clock POVM `E_τ = Σ_t f(t−τ)|t⟩⟨t|`. Then:

- the conditioning weight is `1/N` for every input, so conditioning is linear;
- the conditioned map is `Φ_τ = U(τ) ∘ D`, with `D` a fixed dephasing;
- the propagator between readings is the unitary `U(τ₂−τ₁)`.

So the map family is CP-divisible with no backflow, and it fails the semigroup
law only because `Φ_0 = D ≠ id`.

**Premise (added after `kb-clock-interactions`, merged in bc4b109):** this holds
for a pure physical state on a single constraint surface. A stationary mixture
over several total-energy sectors gives backflow even with an interaction that
commutes with the clock. In Rijavec's model (2204.11740v3, Eq. 90 and footnote 21)
the trace distance is `|cos(θ/2)|` with θ linear in t; the lane checked this
numerically, and it is the lane's derivation, not Rijavec's claim. So the
remaining case should also fix the universe state to one constraint surface.
The lane also conjectures a mechanism for the interacting case: when
`[H_int, H_C] ≠ 0`, the reading probabilities need not be uniform, so
normalized conditioning becomes reading-dependent. The `Z_3` example should
compute those probabilities first. The script checks this exactly for N = 5, 8, 12
with four blurs. This kills the uncoupled, covariant version of the defeat
search's proposed sub-case: there is no memory to classify. It is a finite check
of one model plus a two-line derivation, and needs independent checking.

## Disagreements with the underlying lanes (unresolved, not averaged)

1. `knowledge/defeat-search/rc5-memory-criteria.md` lists among Eq. (10)'s
   assumptions that "conditioning on the clock reading acts as postselection with
   normalization (Eq. 7), so the normalized state evolves nonlinearly." The
   accepted audit, and this reread, find that the supplement's derivation of the
   kernel is a linear, trace-preserving map per τ, with no postselection. The
   nonlinearity is announced in the main text but never enters the derivation.
2. The same file proposes "a qubit system with a finite-dimensional clock …
   (Smith-Ahmadi qubit-clock class or a Page-Wootters construction with unitary
   clock-system interaction)" as the narrowest sub-case. This reread finds that
   without the interaction, and with a covariant POVM, the case is degenerate. The
   interaction is load-bearing, which moves the remainder into RC-1's region.
3. The audit lane says the linear-channel argument for the supplement holds
   because `F_σ(T̂−τ) B̂_α` is Hermitian. That also needs `F_σ` real-valued; the
   paper implies this but does not state it.

## Claim-contract draft (NOVELTY.md gate)

- **Question.** For a finite clock coupled to a qubit with `[H_int, H_C] ≠ 0`,
  under linear conditioning and a fixed multi-time clock-readout instrument, which
  of: semigroup failure, CP-indivisibility, trace-distance backflow, process-tensor
  memory, hold, and do any two come apart?
- **Nearest predecessors.**
  1. Chruściński–Kossakowski–Rivas 2011: (ii) vs (iii) separation, not clock-conditioned.
  2. Milz–Kim–Pollock–Modi 2019: (ii) vs (iv) separation, not clock-conditioned.
  3. `frontier-page-wootters-measurements-2023` and Smith–Ahmadi 1712.00081:
     clock-conditioned non-unitary maps with no criterion classification found
     (abstract or snippet only for Smith–Ahmadi). Gambini–Porto–Pullin, PRL 93,
     240401 (2004), the degrading-clock case, is unread here and must be read first.
- **Delta.** Applying the published separations to the interacting finite-clock
  map family, if no one has done so. A plausible outcome is "application, not
  novel", which is still a valid audit output.
- **Smallest example.** `Z_3` clock, qubit system, `H_int = g σ_x ⊗ K` with `K`
  a clock operator not commuting with `H_C` (e.g. a reading projector `|0⟩⟨0|`,
  which `H_C` does not commute with); compute `Φ_τ` exactly for τ ∈ Z_3.
  (A coupling like `σ_z ⊗ H_C` commutes with `H_C` and does not qualify.)
- **Falsifier.** A published computation of divisibility, backflow or
  process-tensor memory for an interacting Page–Wootters or Smith–Ahmadi clock;
  or a proof that linear conditioning with any finite covariant clock yields maps
  of the form `U ∘ D` even with interaction.
- **Novelty kind.** At most an application or classification of known criteria
  to a known map family. Not a new criterion, not an ontology result.

Not called novel or open. Wait for `kb-clock-interactions` (RC-1 neighbours)
before writing a final contract, because the interacting region is shared.

## Independent post-claim reread (2026-10-20)

The parent task was claimed after this draft. Re-fetched and re-read
2606.08595v1 (main text and supplement):

- **Eq. (10).** A covariant time-convolutionless integro-differential equation
  for `ρ̃_{S,τ}[Σ]`, with kernel
  `C^{(σ)}_{αβ}(x,y;τ) = χ_σ(x,y;τ) G_{αβ}(x,y)` (Eq. 11) and `O(g³)`.
  There is no map family, composition law or two-time instrument in the
  equation, so none of the four criteria is formulated. The text's own claim is
  at the generator level.
- **Supplement Eq. (23).** `Ê_α(x;τ) = F_σ(T̂(x) − τ(x)) B̂_α(x)`, a Hermitian
  composite environmental operator; Eq. (24) puts it inside the interaction
  density; Eq. (31) is the plain partial trace
  `ρ_S^I[Σ;τ] = Tr_Ξ(ρ_tot^I[Σ])`. This is the linear, trace-preserving per-τ
  map the audit describes, not the normalized nonlinear Eq. (7) of the main
  text.
- **Supplement after Eq. (46).** "Equation (44) is generically non-Markovian
  because the conditioned state at the spacetime point x depends on the causal
  history encoded in the dressed relational kernel." This is a statement about
  a kernel, not a divisibility/backflow/process-tensor test.
- The words "divisib", "backflow" and "process tensor" do not occur anywhere in
  the HTML; "postselect", "outcome" and "Kraus" do not occur. This supports the
  audit's Q2 verdict.
- The four-criterion separations listed above are published (Chruściński–
  Kossakowski–Rivas 2011; Milz et al. 2019); applying them to this map family
  would be an application, not a new criterion. The draft's SHRINK stands.

One correction to the audit's contrary-evidence note: the linear-channel
argument for the supplement needs `F_σ` to be real-valued, which the text
implies but does not state. This is a premise to record, not a refutation.
