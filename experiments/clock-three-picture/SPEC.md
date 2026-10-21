# Z_3 clock + qubit model: specification

This file fixes the model so the numbers can be reproduced without the original
code. Everything is finite-dimensional; units with ħ = 1.

## Spaces and operators

- Total space `C ⊗ S`, clock first. Clock `C = ℂ³` with energy basis `|n⟩`,
  n = 0, 1, 2. System `S = ℂ²` with basis `|↑⟩, |↓⟩`.
- `H_C = diag(0, 1, 2)` (ω = 1). `H_S = (ε/2) σ_z = diag(+ε/2, −ε/2)`, with ε = 1.
- Ideal clock readings: `|τ_k⟩ = 3^{-1/2} Σ_n e^{−i n t_k} |n⟩`, `t_k = 2πk/3`,
  k = 0, 1, 2. They are orthonormal and `e^{−i H_C t_1}|τ_k⟩ = |τ_{k+1}⟩`.
- Interaction `H_int = g K ⊗ σ_x`. Default `K = |τ_0⟩⟨τ_0|`. Other K used:
  `|τ_0⟩⟨τ_1| + |τ_1⟩⟨τ_0|`; `|0⟩⟨1| + |1⟩⟨0|` (energy basis); and the commuting
  control `|0⟩⟨0|` (energy basis).
- Constraint operator `H = H_C ⊗ 1 + 1 ⊗ H_S + H_int`. A **constraint surface** is
  an eigenspace `V_λ` of H (eigenvalues equal within 1e-7 are one surface). A
  physical state is a unit vector in one `V_λ`.

## Quantities

1. `‖[K, H_C]‖`: the largest absolute matrix entry of the commutator.
2. For g ∈ {0, 0.05, 0.2, 0.5, 1.0}: every eigenvalue λ of H and dim `V_λ`.
3. Known limit: the first-order splitting of the g = 0 surface at λ = 0.5 is given
   by the eigenvalues of `P (K ⊗ σ_x) P` on that surface (P its projector);
   compare with `(λ(g) − 0.5)/g` at g = 1e-3.
4. Non-ideal covariant POVM: `E_k = Σ_j f((j − k) mod 3) |τ_j⟩⟨τ_j|` with
   `f = (1 − 2d, d, d)`; d = 0 is ideal, d = 0.1 non-ideal.
   Reading probabilities `p(k) = ⟨ψ| E_k ⊗ 1 |ψ⟩` for ψ spanning a one-dimensional `V_λ`.
5. Page–Wootters reduction `R(k) = √3 (⟨τ_k| ⊗ 1)`. Isometry defect on `V_λ` with
   orthonormal basis B: the largest absolute entry of `3 B† (|τ_k⟩⟨τ_k| ⊗ 1) B − 1`,
   maximized over k.
6. Twirl identity: with `G[X] = Σ_λ P_λ X P_λ`, compare `⟨ψ|G[X]|ψ⟩` and
   `⟨ψ|X|ψ⟩` for `X = E_k ⊗ O` (d = 0.1), `O = [[0.5, 0.3−0.2i], [0.3+0.2i, −0.5]]`,
   over all surfaces at g = 0.5.
7. Controls: at g = 0 on `V_0.5`, isometry defect, `p(k)` for the state
   `(B_0 + B_1)/√2`, and fidelity of the conditional system state
   `∝ (⟨τ_k| ⊗ 1)ψ` with `e^{−i H_S t_k}` applied to the k = 0 state. Commuting
   control K = `|0⟩⟨0|` at g ∈ {0.2, 0.5, 1}: `p(k)`, isometry defect, surface
   dimensions.
8. Accidental surface: K = `|0⟩⟨1| + h.c.` at g = 1 has a two-dimensional surface
   (λ = 1.5). On it, `A_k = R(k) R(0)^{-1}` (2×2), `A_k† A_k`, the propagators
   `A_{k+1} A_k^{-1}` (k mod 3) and their `P† P`, and the trace distance between
   normalized `A_k u`, `A_k v` for random unit u, v over k = 0, 1, 2, 3 (≡ 0).
