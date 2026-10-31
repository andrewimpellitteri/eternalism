# Independent review: bounded ambiguity and noisy records

Reviewed 27 October 2026 from the two current `RESULT.md` files and their derivation/check artifacts. This is a mathematical audit of the stated scope, not manuscript acceptance or a novelty judgment.

## Verdicts

| Result | Verdict | Safe scope |
|---|---|---|
| `research/horizons/bounded-ambiguity/RESULT.md` | **Survives, with explicit conditional premises** | For smooth solutions on the unit cylinder, spatially homogeneous smooth real `q`, and the stated conformal Cauchy-data norm, the pointwise difference bound and its application to every normalized hidden alternative are supported by the displayed mode and addition-kernel estimates. The fixing-set application additionally assumes the massless fixing classification and the smooth extension to the auxiliary `t=0` slice. |
| `research/horizons/noisy-record-control/RESULT.md` | **Survives within the stated observation model, with narrow interpretation** | The finite-band sequence has unit conformal energy, vanishing aggregate field-record norm, and diverging target point value. It establishes failure of a uniform point-evaluation error modulus for this solution ball and this record norm, including when records are taken over the full strip. It does not establish a causal-horizon instability or detector failure. |

## Audit of the quantitative upper bound

For each `k`, Volterra and Gronwall give `|C_{λ,k}| ≤ exp(|λ|Q/k)` and `|S_{λ,k}| ≤ exp(|λ|Q/k)/k`. Subtracting the free multipliers gives `|D_C,k| ≤ |λ|Q exp(|λ|Q/k)/k` and `|D_S,k| ≤ |λ|Q exp(|λ|Q/k)/k²`. In the position-data term, `Λf` contributes the additional `1/k`; both coefficient multipliers are therefore bounded by `B/k²`, where `B=|λ|Q exp(|λ|Q)`.

The S³ eigenspace at eigenvalue `k` has multiplicity `k²`, and the addition kernel is `k²/(2π²)`. Joint Cauchy–Schwarz over position and velocity coefficients therefore bounds the squared evaluation norm by

`sum_k k²/(2π²) · 2B²/k⁴ = B²/π² · sum_k 1/k² = B²/6`.

Thus the constant `1/√6` follows; with `f=0`, the squared sum halves and gives `1/√12`. The argument is valid for smooth data as written. The bounded evaluation functional can then extend to the completion in the stated data norm; this does not imply arbitrary finite-energy fields have point values.

The hidden-alternative step is valid conditional on the stated geometry and extension: exact vanishing on `I_s^-(b)` supplies zero traces at `t=0` on the open ball `B(Y,τ)` by smoothness; finite propagation for the free equation makes `h₀` vanish in the unperturbed past and at any target fixed by the unperturbed theory. Subtract `h₀` and apply the bound. The supremum ranges over all smooth admissible differences with `N≤1`, so the conclusion is an upper bound on all alternatives in that defined class. It is not an estimate for noisy past data.

The endpoint is auxiliary, not part of the physical open strip. Under the stated smooth `q` extending past the endpoints, smooth Cauchy data on any interior slice generate a unique smooth solution through the closed cylinder interval by the ordinary well-posed Cauchy evolution for this linear equation. Thus endpoint smoothness need not be separately imposed on the solution. The hidden-data traces at `t=0` follow from this extension and vanishing on the approaching open past; no endpoint data are independently prescribed.

For dust, direct integration confirms `Q(t)=(a_m²/4)(3t/2−2 sin t+sin(2t)/4)` and `Q(2π)=3πa_m²/4`. With `λ=m²`, the rescaled-field bound is `O(m²)` at fixed `t`; the physical field has the additional `1/a(t)` factor, so uniformity requires staying away from the singular endpoints. The matching lower order remains conditional on the separately reviewed mass-loss witness.

## Audit of the noisy-record construction

The zonal harmonic normalization is consistent with the unit S³ radial volume: `Z_k(r)=sin(kr)/(√(2π²) sin r)` has unit L² norm and `Z_k(Y)=k/√(2π²)`. For the finite sum, each mode contributes `1/K` to the conserved conformal energy after position and velocity terms are added. At the target, all cosine phases equal one and the sum is `√K/√(2π²)`. Spatial orthogonality gives `||ψ_K(t)||²₂=(1/K) sum  cos²(...)/k² ≤1/K²`; integrating over a full period gives exactly `(π/K)sum 1/k² ≤π/K²`. Since `P` is a subset of the full strip, its record norm also tends to zero. Therefore the claimed infinite supremum under every positive record tolerance follows by choosing `K` large enough while the target value grows.

This is not exact agreement on `P`: the construction uses small nonzero records. It holds even with full-strip records and so does not isolate a horizon mechanism. The energy is a conformal data norm, and the observation norm records field amplitude only. The fixed-profile averaging estimate follows from `|<χ,ψ_K>|≤||χ||₂||ψ_K||₂≤||χ||₂/K`; it is specific to this sequence, not a general past-only observability theorem.

The finite-band statement is also sound: a finite sum of spatial eigenmodes with sinusoidal time factors is real analytic on the connected cylinder. Vanishing on a nonempty open `P` implies vanishing identically. For its finite-dimensional design map, a zero Gram quadratic form means the corresponding analytic solution vanishes on `P`, hence all coefficients vanish; therefore the exact Gram matrix is positive definite. The stated bound follows by Cauchy–Schwarz in the Gram norm. Its constant can deteriorate with the cutoff and region; no uniform estimate follows.

The physical-field measure calculation is correct. In four spacetime dimensions, `dVol_g=a(t)^4 dt dV_{S³}`, while `φ=ψ/a`; hence `|φ|² dVol_g=a(t)^2|ψ|² dt dV_{S³}`. The displayed `a²` is the combined weight after field rescaling, not the volume density alone. Since `a(t)≤a_m` on the strip, the record bound `||φ||²_{L²(P,dVol_g)}≤a_m²π/K²` follows directly from the unweighted full-strip estimate. No measure repair is needed.

## Strongest objection and minimal safe statements

The strongest objection is that the noisy-record note can be read as evidence that finite causal records fail to predict a future event. Its construction proves a narrower functional-analytic statement: point evaluation is unbounded on this unit conformal-energy ball relative to the selected field-amplitude L² record norm. It uses errors on the record region, not exact past agreement, and works over the entire spacetime strip. It says nothing by itself about realistic detector response, a stronger norm involving derivatives, a common ultraviolet cutoff, fixed spatial averages, or point prediction from a physically specified observation process.

Minimal manuscript-safe statements:

1. Under the assumptions above, changing the homogeneous potential from zero to `λq` changes the target values of normalized exact-past-compatible alternatives by at most `|λ|Q exp(|λ|Q)/√6` in the rescaled field. At fixed interior dust targets this is `O(m²)` for ordinary mass `m`; the physical field bound includes `1/a(t)`.
2. For the stated full-field L² record norm and unit conformal-energy solution ball, no uniform error modulus controls a point value: an explicit exact-solution sequence has record norm tending to zero and target value tending to infinity. This is distinct from exact-past fixing and from a detector or causal-horizon claim.
3. A fixed finite spatial spectral cutoff changes the admissible solution class and makes exact fixing from any nonempty open record region global by analyticity. It is not a neutral numerical approximation to the unrestricted smooth class.

No implication to eternalism, presentism, passage, determinism, or ontology follows.

## Review correction

My initial review incorrectly objected that the `a²` factor was not a standard volume density, overlooking the simultaneous field rescaling `φ=ψ/a`. Recomputing the product gives `a⁴·a⁻²=a²`, exactly as the result states. I withdraw that objection; the physical four-volume record calculation is correct. I also initially framed endpoint extension as an extra solution-side assumption. With smooth `q` extending past the endpoints, smooth Cauchy data on an interior slice yield smooth unique evolution through them, so separate endpoint smoothness of the solution is unnecessary. These corrections do not alter the original result files.

## Evidence and read depth

- Read the full current bounded-ambiguity derivation and control code; independently followed the displayed derivation. The citation to Baskin–Mazzeo is reported by its author as selected-section full-text reading, but I did not independently read that source in this lane. It is context, not support for the new estimate.
- Read the full current noisy-record derivation and control code; independently checked the harmonic normalization, phase sum, energy, record norm, and analytic Gram logic. The Curry course notes entry is reported as full-text reading by its author; I did not independently verify it and it is not needed for the explicit construction.
- The reference to the project’s massless three-diamond fixing theorem is a premise of the bounded-result application. This review did not independently re-prove or re-audit the manuscript theorem or its literature priority.
- No external source was read in this review; no priority or novelty claim is made.

## Bounded checks performed

Ran both existing standard-library control scripts from the shared checkout without editing their files. `check_bound.py` passed its exact constant-potential mode comparisons (`k=1,3,9`), zero-potential control, multiplicity checks (`n=0..9`), 24-mode dust comparisons and coarse/fine integration checks. `check_controls.py` passed radial norm/energy/record controls for bands `K=4,8,16,32` and the stated six-dimensional zonal Gram quadrature/refinement check. These are finite numerical controls; they do not prove the infinite-mode estimates, the analytic uniqueness theorem, or physical observability.
