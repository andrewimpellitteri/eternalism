# Adversarial audit: localized polar persistence

Date: 2026-10-30

Target: `research/lawful-completions/coordinator/LOCAL_POLAR_PERSISTENCE.md`

Scope: local radial H³ Picard construction, weak–strong uniqueness, common higher-order lifespan, and §5 continuation. The coefficient gain (A) and L²-to-H¹ difference estimate (B) are treated as hypotheses, as requested. I did not audit the exterior induction or constraint algebra.

## Finding

I found no counterexample to the local persistence conclusion under the stated assumptions (including radial invariance, local Lipschitz regularity of the given solution, finite-speed bound for `c`, and (A)–(B)). The nonlocality itself is controlled: at radius `R`, the radial constraint reads only input at radii at most `R`; (B) controls the derivative of the coefficient difference in the weak–strong estimate. A pointwise-nonlinearity theorem alone would not justify these steps, but the displayed estimates do.

Section 5 has the right continuation mechanism and does not need a sequence of restarts whose spatial losses accumulate. As written, however, the nested-cone argument is compressed at the key point: it does not quantify the relation among the inner restart ball, the target compact set, the uniform local lifespan, and the uniqueness-cone speed. Its sentence about fitting the speed-times-interval into the buffer can be made into a one-restart continuation lemma below. This is a proof-detail repair, not a counterexample or a new hypothesis beyond those already stated.

## Local construction and uniqueness audit

For the localized Picard step, write `d_n = ĉ[Uⁿ]−ĉ[Uⁿ⁻¹]` and `Zⁿ=Uⁿ−Uⁿ⁻¹`. Subtraction puts the principal term in divergence form with coefficient `ĉ[Uⁿ]`; the remaining forcing is

`Σ A_j (d_n ∂_j Uⁿ + (∂_j d_n) Uⁿ)`.

The common H³ bound gives a common W¹,∞ bound. Hypothesis (B) gives `||d_n||₂+||∇d_n||₂ ≤ C||Zⁿ||₂`; hence this forcing is bounded in L² by `C||Zⁿ||₂`. The symmetric L² estimate therefore yields a contraction on a short interval. The coefficient cutoff remains positive because `1+χ₁(c−1)=(1−χ₁)+χ₁c`, and the energy cutoff is nonnegative. The positive integral formula for `f` gives a uniform lower bound on the fixed cutoff support from the common L∞ bound. These facts close the stated base-norm iteration without requiring derivative closeness of the iterates.

The localized coefficient at points of `B_L` agrees with the original coefficient there: its radial integral samples only radii `≤R`, where `χ₀=χ₁=1`. Thus localization does not invalidate comparison on the intended interior ball.

For weak–strong uniqueness, subtraction with `D=U−V` gives principal coefficient `c[U]` and forcing `Σ A_j(d∂_jV+(∂_jd)V)`. On a cone whose boundary contracts faster than `sup c[U]`, the principal boundary flux is nonpositive. By (B), the forcing has L² norm at most `C||V||W¹,∞||D||₂`; the resulting Gronwall inequality with zero initial difference proves equality on the cone. The stated local Lipschitz regularity suffices for the weak Green identity (or a standard spatial mollification limit) because the principal coefficient is Lipschitz there. No values outside the comparison ball enter the radial coefficient at an interior point.

The common higher-order interval is also supported by the stated structure. For each fixed `k`, the frozen linear estimate has coefficients controlled by the common H³ bound, while the terms involving the frozen iterate's Hᵏ norm enter linearly. Taking the maximum over the first `N` iterates gives a Gronwall bound independent of `N`; then the limit inherits each fixed-order bound. The lifespan is selected at the H³ level and does not shrink with `k`. To make this fully formal, one should state the standard linear energy estimate for the cutoff equation at each integer order and pass to the limit weakly at that order; the note's interpolation convergence alone gives strong convergence below H³, not by itself strong H³ convergence. This is a regularity-passage detail and does not undermine the common-interval argument if the usual energy-solution construction is supplied.

## Explicit buffer lemma repairing §5

Let `K` be a target closed ball `B_R`, and let `τ` be a proposed finite smoothness endpoint. Suppose the solution is already known smooth and equal to the given Lipschitz solution on a shrinking outer cone up to `τ`, and that the H³ energy estimate gives a uniform bound on an inner cone with limiting radius at `τ` strictly larger than `R`. Let `C` exceed the known speed bound on the relevant time slab. Choose `η>0` and a fixed restart radius `r` so that

`R + 2η < r < lim_{t↑τ} L_inner(t)`.

The estimates on the outer smooth cone bound `||U(t)||_{H³(B_r)}` uniformly for `t<τ` sufficiently near `τ`. Extend `U(t)|_{B_r}` to whole-space H³ data with extension norm bounded uniformly in `t` (the radii are fixed). The H³ local construction then supplies a lifespan `h₀>0` independent of `t`, since the extended data norms and cutoff radii are uniformly bounded. Put

`h = min(h₀/2, η/(2C))`.

Choose a restart time `t₁<τ` with `τ−t₁<h/2`. The restarted smooth solution exists through `t₁+h`, hence beyond `τ`. Weak–strong uniqueness identifies it with the given solution on the cone from `B_r` contracting at speed `C`; throughout this interval its radius is at least `r−Ch > R+η`. It therefore extends smoothness on a neighborhood of `B_R` across `τ`.

Only one restart is used to cross a proposed endpoint. The fixed positive gap between `B_R` and the limiting inner-cone radius pays for the contraction during that restart. No loss is charged at each earlier local existence interval: those intervals are patched by uniqueness into the already existing smooth solution, and the argument is invoked only at a hypothetical finite endpoint. For a finite time slab and a prescribed compact set, first choose the original outer cone with enough radius that its contracting boundary stays strictly outside the target plus this restart margin. The finite speed bound permits that choice. The same construction works backward in time with reversed time orientation.

This supplies the missing quantitative justification for the intended §5 conclusion. It also clarifies which radius carries the H³ bound: it must be an inner cone still strictly larger than the target at the candidate endpoint, while the given solution's Lipschitz and coefficient bounds are available on a larger comparison cone.

## Assumptions versus conclusions

**Inputs, not derived here:** (A) and (B); local Lipschitz distributional solution on all space; radial scalar/vector structure; positive lower bound for `f` on relevant compact regions; finite upper bound for `c`; smooth initial data on the relevant initial balls; standard linear symmetric-hyperbolic energy estimates and bounded Sobolev extension operators.

**Derived conditional conclusions:** localized radial H³ Picard existence and L² uniqueness; weak–strong identification on shrinking inner cones; persistence of every fixed finite Sobolev order on the common H³ interval; and continuation across any finite interior endpoint with a strictly positive spatial buffer. Therefore the target finite-region smoothness conclusion follows conditionally from the listed inputs.

**Remaining presentational work in the source note:** state the explicit one-restart buffer lemma (or equivalent inequalities) and spell out the H³ energy-solution passage. Neither issue yields a counterexample under the hypotheses, but both should be explicit in a proof intended to establish the theorem rather than outline its standard steps.

## Repair disposition (2026-10-30)

Checked only the two incorporated repairs. **Both close the identified proof details under the stated hypotheses.** In §5, `R+2η<r`, `h≤η/(2C₀)`, and `τ−T₁<h/2` ensure the restarted comparison cone remains strictly beyond `B_R` and the restarted solution extends past `τ`; this is a single endpoint restart, so there is no accumulating boundary loss. This uses `C₀` as a speed bound on the entire restart comparison interval, including its short portion past `τ`, which is available on a compact slab around an interior endpoint.

The H³ passage is also adequate: weak H³ continuity gives weak L² continuity of each `D^αU`; the commuted equation has an L¹-in-time L² source, and the spatial Friedrichs commutator tends to zero for the Lipschitz principal coefficient. The resulting norm continuity plus weak continuity yields strong continuity for each derivative and hence in H³. It does not rely on strong H³ convergence of the Picard iterates. No further issue was found in these two repairs; no broader reaudit was performed.
