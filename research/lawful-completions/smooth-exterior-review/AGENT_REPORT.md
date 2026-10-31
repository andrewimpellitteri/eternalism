# Exterior Goursat induction audit

**Verdict: the exterior all-order induction is valid under the stated common incoming-profile norms and reduced low-order bounds.** I found no counterexample to the displayed first-order system or to the claimed uniformity in the receding lower characteristic. This verifies the exterior regularity step conditionally; it does not verify the other bootstrap steps or certify the full smoothness repair.

## Scope and exact files

Reviewed `research/lawful-completions/coordinator/SMOOTHNESS_BOOTSTRAP.md`, §1, against `research/lawful-completions/coordinator/C11_FINITE_CONTROL.md`, especially §§3–6, and the project instructions/brief. Changed only this file: `research/lawful-completions/smooth-exterior-review/AGENT_REPORT.md`. No external sources were used, so no `sources.jsonl` was needed. No code or numerical grid was used.

## Induction and uniform constants

On each strip `u_n ≤ u ≤ u_* < A`, `A ≤ v ≤ V`, the assumed bounds give `r ≥ c(A−u)`, `f ≥ 1/2`, and `λ ≥ 1/3`; for estimating the vector field and its derivatives, `c` can be taken as the stated `1/3`. The data `Y(u,A)` vanish except for the fixed `ν=-1/2`; integrating `Y_v=G` over the finite v interval bounds `h,p,m` uniformly, while the assumed low-order bounds control `ν,λ,q`. In particular the mass flux gives `m=O(ε²(V−A))` on this finite strip; no estimate proportional to an unbounded exterior radius is needed.

The vector field is

`F=(2mνλ/(fr²), 2mνλp/(fr³))`, with `r=(v−u)/2+h` and `f=1−2m/r`.

Every derivative of `F` in its state variables and explicit `v` dependence is bounded by `C_k(A−u)⁻²`: the least-decaying term is `r⁻²`; differentiating `r⁻¹` or `r⁻²` in `r` only adds inverse powers. Factors from differentiating `f⁻¹` are controlled by `f≥1/2`, bounded `m`, and `r` bounded below. Derivatives of `G` are uniformly bounded on the same state range; its mass component has only the bounded denominator `λ` and the displayed square. Constants can depend on the strip endpoint `u_*`, `A,V`, fixed low-order bounds and the common profile norm at the order in question, but not on `u_n`.

For `k≥1`, `∂_v^kY=∂_v^{k−1}G` is bounded from the already established X,Y v-derivatives through order `k−1`. Differentiating `X_u=F` k times in v gives a linear equation in `∂_v^kX`, with coefficient `F_X` and forcing consisting of lower X derivatives and the now-known `∂_v^kY`. The coefficient and forcing are bounded by `C_k(A−u)⁻²`. The boundary value is the kth derivative of `(1/2,Φ_n/2)`, uniformly bounded by the common profile norm. Gronwall therefore costs at most `exp(C_k/(A−u_*))`, independently of `u_n`; the displayed integral estimate is correct. Then `Y_v^k` follows from `G`. The term `F_Y Y_v^k` is indeed known at this stage, so there is no circular top-order dependency.

Mixed derivatives close in the stated order. Assuming u derivatives through order j−1, `∂_u^j X=∂_u^{j−1}F` is determined. The differentiated equation for `∂_u^jY` is a finite-v linear ODE with bounded `G_Y`, known `X` forcing and lower-order terms; its data vanish at `v=A`, since `Y(u,A)` is constant in u. Finite-interval Gronwall closes that order. Differentiating these identities in v then gives all mixed orders. Constants may grow with derivative order, which is sufficient for C∞ and is not claimed to be uniform in k.

## Continuation, limit, and slice scope

For each fixed finite approximant, local smooth characteristic/Goursat existence away from `r=0` is applicable to this smooth rational system. On any closed substrip with `u≤u_*<A`, the low-order bounds keep the solution in the regular region `r>0`, `f>0`, `λ>0`; the derivative estimates prevent higher derivatives from becoming unbounded before reaching the strip boundary. This is the required continuation mechanism. It does not use an axis estimate or divide by r at the center.

On each compact subset of `u<A, v≥A`, the estimates are uniform in n at every fixed derivative order. Diagonal Arzelà–Ascoli yields a smooth selected limit there. The subsequence has the same previously selected C¹/C² limit by uniqueness of uniform compact limits, so the smooth limit is the already selected reduced solution, with the derivative identities inherited by convergence. For `v<A`, the flat-wedge identity supplies smoothness; choosing `A` strictly before the common support gives an open overlap. Thus the exterior step establishes smoothness on the entire early region `t<A` (and on `u<A` wherever covered by the stated two regions), including the center via the flat wedge.

This supplies smooth data on a slice `t=t_c<A` when combined with the flat wedge and the project’s low-regularity global slice geometry. The exterior induction alone proves neither that the slice is complete nor the later polar-coordinate/axis regularity argument. The draft’s “smooth early complete Cauchy surface” conclusion is therefore correctly conditional on its §2 coordinate/global-slice claims; it should not be presented as a consequence of §1 alone.

## Repairs and strongest residual

No repair to the exterior induction is required. For maximum precision, the proof can state explicitly that the k-th forcing uses `Y_v^k` after it has been bounded from `G` and orders `<k`, and that finite-approximant continuation is on closed substrips `u≤u_*<A`, with the positive `r,f,λ` margins supplied by the low-order estimates. These are clarifications of dependencies already present, not a detected gap.

Strongest residual: the task brief requires the common profile derivative norms and the reduced low-order bounds uniformly in n; the exterior calculation consumes those inputs but does not rederive them from the incoming family. The local smooth Goursat theorem is also invoked at the level of standard local theory rather than independently proved here. If either input fails for the actual finite approximants, this audit does not repair it. Neither residual yields a counterexample within the stated hypotheses.

**Checks:** algebraic dependency audit of F and G; induction-order audit; integral bound `∫_{u_n}^{u_*}(A−s)⁻²ds ≤ 1/(A−u_*)`; limit identification and slice-scope audit. No computational check was necessary.
