# Independent replication vs. original: comparison

`replicate.py` was written from `SPEC.md` alone. I did not read `model.py`, `linalg.py`, `model_output.txt` or their git history until `replicate_output.txt` was finished and saved. The only file opened afterwards was `model_output.txt`, for this comparison. I did not read the original code at any point.

**Method (independent of Jacobi):** Householder tridiagonalisation of the complex Hermitian H, then Sturm-sequence bisection for the eigenvalues. Eigenvalues within 1e-7 of each other are grouped into one surface. Each eigenspace is the null space of H − λI, found by Gaussian elimination with complete pivoting (pivot tolerance 1e-8) and then Gram–Schmidt. For every surface, the code asserts that the nullity equals the Sturm multiplicity. All eigenpair residuals are ≤ 1.3e-15, and global orthonormality errors are ≤ 4.6e-15. Standard library only.

**Precision caveat:** `model_output.txt` prints most quantities to 4 or 6 decimals, so agreement can be checked only to that printed precision, not to 1e-6 everywhere. My values are given to 12 digits in `replicate_output.txt`.

Section numbers in `model_output.txt` do not follow the SPEC numbering. The mapping is given below.

| SPEC item | Quantity | Replication | Original (`model_output.txt` §) | Verdict |
|---|---|---|---|---|
| 1 | max\|[K,H_C]\|, K=\|τ0⟩⟨τ0\| | 0.666666666667 | 0.6667 (§1, §6) | agree |
| 1 | K=\|τ0⟩⟨τ1\|+h.c. | 0.666666666667 | 0.667 (§6) | agree |
| 1 | K=\|0⟩⟨1\|+h.c. | 1.000000000000 | 1.000 (§6) | agree |
| 1 | K=\|0⟩⟨0\| | 0 | "[K,H_C] = 0" (§7 header) | agree |
| 2 | g=0 surfaces | −0.5:1, 0.5:2, 1.5:2, 2.5:1 | same (§1) | agree |
| 2 | g=0.05 | −0.500509455580, 0.483131481082, 0.516452372701, 1.483547627299, 1.516868518918, 2.500509455580, all dim 1 | −0.5005, 0.4831, 0.5165, 1.4835, 1.5169, 2.5005, all dim 1 | agree (4 d.p.) |
| 2 | g=0.2 | −0.508197815471, 0.430463779248, 0.563001324189, 1.436998675811, 1.569536220752, 2.508197815471 | −0.5082, 0.4305, 0.5630, 1.4370, 1.5695, 2.5082 | agree (4 d.p.) |
| 2 | g=0.5 | −0.552732335304, 0.321093834410, 0.642077224496, 1.357922775504, 1.678906165590, 2.552732335304 | −0.5527, 0.3211, 0.6421, 1.3579, 1.6789, 2.5527 | agree (4 d.p.) |
| 2 | g=1.0 | −0.724957614404, 0.160904246276, 0.734595507592, 1.265404492408, 1.839095753724, 2.724957614404 | −0.7250, 0.1609, 0.7346, 1.2654, 1.8391, 2.7250 | agree (4 d.p.) |
| 3 | eig of P(K⊗σx)P on V_0.5 | ±0.333333333333 | ±0.333333 (§2) | agree |
| 3 | (λ(g)−0.5)/g at g=1e-3 | −0.333416617, +0.333249950 | −0.333417, 0.33325 | agree (6 d.p.); both differ from first order by 8.3e-5 = O(g), as expected |
| 4 | p(k), d=0 and d=0.1, g=0.2 (6 surfaces) | e.g. λ=−0.5082: 0.344431818339/0.327784090830×2; d=0.1: 0.341102272837/0.329448863581×2 (full table in output) | §4, all 6 rows | agree (4 d.p., every entry) |
| 4 | p(k), g=0.5 (6 surfaces) | e.g. λ=0.6421: 0.233470511940/0.383264744030×2; d=0.1: 0.263429358358/0.368285320821×2 | §4, all 6 rows | agree (4 d.p., every entry) |
| 4 | p(k), g=0.05 and g=1.0 | computed (see output) | not printed | no comparison |
| 5 | isometry defect, g=0.2 | 0.033295455017, 0.079626747263, 0.112922202280 (each twice, mirrored) | 0.033, 0.080, 0.113 | agree (3 d.p.) |
| 5 | isometry defect, g=0.5 | 0.205272993734, 0.094315470444, 0.299588464179 (mirrored) | 0.205, 0.094, 0.300 | agree (3 d.p.) |
| 5 | defect, g=0 all surfaces | 0 | 2.22e-16 on V_0.5 (§3) | agree (rounding) |
| 6 | max\|⟨G[X]⟩−⟨X⟩\|, g=0.5 | 1.67e-16 | 5.57e-17 (§5) | agree (both at rounding level) |
| 7a | defect on V_0.5, g=0 | 2.2e-16 | 2.22e-16 for each k | agree |
| 7a | p(k) for (B0+B1)/√2 | 1/3, 1/3, 1/3 (d=0 and d=0.1) | 0.333333 ×3 | agree |
| 7a | fidelity with e^{−iH_S t_k}ψ_S(0) | 1.000000000000 for every k | max infidelity 4.44e-16 | agree |
| 7b | K=\|0⟩⟨0\| spectra, g=0.2/0.5/1 | ±√(0.25+g²) = ±0.538516480713 / ±0.707106781187 / ±1.118033988750; 0.5 (dim 1); 1.5 (dim 2); 2.5 (dim 1) | ±0.5385 / ±0.7071 / ±1.1180; 0.5:1; 1.5:2; 2.5:1 | agree |
| 7b | p(k) | 1/3 each, all surfaces (dim-2 surface: full range over the surface is [1/3, 1/3]) | 0.333333 ×3 | agree |
| 7b | isometry defect | ≤ 4.4e-16 | ≤ 4.4e-16 | agree |
| — | max surface dim at g=.05,.2,.5,1 (other K) | τ0τ1+h.c.: [1,1,1,1]; \|0⟩⟨1\|+h.c.: [1,1,1,2] | same (§6) | agree |
| 8 | spectrum, K=\|0⟩⟨1\|+h.c., g=1 | −0.914213562373, −0.5, 1.5 (dim 2), 1.914213562373, 2.5 | 1.5 dim 2 (§8) | agree |
| 8 | eig A_k†A_k | k=0: 1, 1; k=1,2: 0.208712152522, 4.791287847478 | [1,1]; [0.208712, 4.791288] ×2 | agree |
| 8 | eig P†P of the propagators 0→1, 1→2, 2→0 | 0.208712152522, 4.791287847478 for each | same, 6 d.p. | agree |
| 8 | fraction of random pairs whose trace distance increases at some step | 2000/2000 (seed `random.Random(12345)`, complex Gaussian) | 200/200 (seed 1) | agree (different random draws, same result) |
| 8 | g=0.99 / 1.01 neighbour check | not computed (not in SPEC) | in §8 | no comparison |

**Disagreements:** none.

## Notes and SPEC ambiguities

1. **Items 4 and 5: K and g are not specified.** SPEC does not say which g (or which K) the p(k) and isometry-defect values are for. The original prints them only for g = 0.2 and 0.5 with the default K. I computed them for every g in item 2. Only g = 0.2 and 0.5 could be compared.
2. **Item 5: the defect on a multi-dimensional surface depends on the basis.** The "largest absolute entry" of 3B†(Π_k⊗1)B − 1 changes under a unitary change of B. The spectral norm of the same matrix does not, so I report both. Every dim > 1 surface that appears here has this matrix equal to 0 (up to rounding), so the choice does not matter in practice.
3. **Item 7a: B_0 and B_1 are not specified.** For these quantities the choice does not matter. On V_0.5 at g = 0, 3B†(Π_k⊗1)B = 1, p(k) = 1/3 and the fidelity is 1 for every unitary choice of basis. I confirmed this with a randomly rotated basis (see output). SPEC 7 also asks for the "surface dimensions" of the commuting control; these are printed in the output.
4. **Item 8: A_k does not depend on the basis at all.** The brief expected A_k to depend on the surface basis through a similarity transform. As SPEC defines it, A_k = R(k)|_V (R(0)|_V)^{-1} maps the system space ℂ² to ℂ². Changing B → BU cancels, so A_k itself is basis-independent (given V) and its entries are printed. A_k†A_k and every propagator have eigenvalues (5 ± √21)/2. |det| = 1 throughout. The 1.5 surface is span{(|0↑⟩+|1↓⟩)/√2, |2↓⟩}, which I checked by hand.
5. **Item 8: the 100% increase fraction is forced once D_k is not constant.** Because A_3 = A_0, the trace-distance sequence returns to its starting value. So any pair whose D_k varies must increase at some step. The 100% figure therefore shows only that the propagators are non-unitary (not unitary up to a scale) for generic pairs. It does not show anything stronger.
6. **Item 6 is an algebraic identity here.** When ψ lies in a single surface, ⟨ψ|P_λ X P_λ|ψ⟩ = ⟨ψ|X|ψ⟩ exactly. Its numerical check confirms that the implementations are consistent, not any physical claim.
7. **Not compared at 1e-6.** Agreement at the 1e-6 tolerance could not be checked for values the original prints to only 3–4 decimals: the spectra, p(k) and the defects. The replication's 12-digit values are available if the original is re-run with more digits.
