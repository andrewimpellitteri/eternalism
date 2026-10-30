# Red-team review of RESULT.md

30 October 2026. Claude Code (Opus 5.5), adversarial reader. No novelty or
ontological claim. This is one reader's audit, not acceptance.

## Verdict

**Not broken.** I found no gap in the Theorem or in §§1–5, conditional on the
finite-control chain. The new argument does not use that chain beyond what the
notes state. §6 is REPAIRABLE: its conclusion is true, but it is proved for a
different function from the one the Theorem's cuts sample.

**Strongest problem.** The Theorem's cuts are at proper times: E(T)=m_-(t(T)),
where t(T) is each model's own axis coordinate. §6 instead fixes V↦m_- at equal
coordinate values of V. For the function E, §6's first step fails. Equal E gives
only

    Φ₁²(t₁(T))/(2λ₁) = Φ₂²(t₂(T))/(2λ₂),   λ_i=λ_i(t_i(T),t_i(T)),

not Φ₁²=Φ₂². The two conditions differ whenever the clocks differ. So the
"sharp limit" is not yet the limit of §1's own cut construction. The repair is
in item 6. It keeps the conclusion and strengthens it. No counterexample was
found.

## Depth and limits of this audit

Read in full: RESULT.md, C11_FINITE_CONTROL.md, CUBIC_TRACE.md, INCOMING_MASS.md,
COMPACTNESS_CONTINUITY_REPAIR.md, SMOOTH_FINITE_CONTROL.md, the board brief.
Read in part: SMOOTHNESS_BOOTSTRAP.md §§1–2 opening, DEGREE_ROUTE.md,
PHILOSOPHICAL_SCOPE.md. LOY itself was not reread,
so its estimates are project-note inputs here, at discovery depth for this
review. The excluded audit directories were not read. A separate reviewer owns
the chain; a failure there fails this result.

One computation: exact rational arithmetic on 800 random instances (N=1,2,3,5)
confirmed the printed inversion and determinant. The script is not in the
repository. It checks formulas on instances and proves nothing; the algebra in
item 4 is the argument.

## Point-by-point audit

### 1. §1 cut. VERIFIED

- Geometric: yes. m, r, γ and proper time are invariants, so E_j needs no gauge.
- ∂J⁻: C11 §4 gives v nondecreasing on future causal curves, so J⁻⊂{v≤v_j}. A
  point with v<v_j reaches γ(T_j) along u=const then v=v_j. So J⁻={v≤v_j}, and
  its boundary is N_j. The domain is the entire quotient u≤v.
- r→∞: r(u,v_j)≥(v_j−u)/3, from λ≥1/3 integrated from the axis.
- Direction: ν<0 and 1−μ≥1/2 give m_u≤0. So m increases as u→−∞, that is
  outward along N_j, as claimed. The limit exists by monotonicity.
- E_j=m_-(t_j) by definition of m_-, with no limit exchange.
- Note: E_j is fixed at each model's own t_j, not at a common V. The value
  m_-(T_j) is not fixed. RESULT does not claim it is.

### 2. §2 family. VERIFIED

- Supports: T_(j−1)+2δ<T_j−2δ gives each C_k a window of length above 2δ,
  disjoint from F_(k−1) and F_k. Also δ<(T₁−A)/4 gives T_N+δ<2T_N+1, so G is
  clear of F_N. F_k(T_j)=δ_kj and C_k(T_j)=G(T_j)=0 hold, with c_k,a_k⁻>0.
- √b_k is smooth on b_k≥b⁰_k/2, so the map into any C^m norm is smooth, hence
  C²-continuous, with common support and bounds on compact R.
- The L_j formulas are correct, including the half-pulse term a_j⁻.
- e⁰_j=Σ_(k≤j)b⁰_kc_k is positive and strictly increasing.
- A: every support lies above A+δ, so v<A is exactly flat. Since 0<A, the event
  b is in the wedge. C11 §4 applies unchanged.

### 3. §3 estimates. VERIFIED

- Cut: Cε²<δ keeps t_(n,j) in (T_j−δ,T_j+δ). The stated bound does not need
  this; global sup f² suffices.
- p error: |p_(n,j)−L_j|=∫ between T_j and t_(n,j) of f²≤sup f²·Cε². Correct.
  The N+1 row has zero error.
- Reading: ε⁻¹H−x_j=[ε⁻¹(H−εf(t))]+[f(t)−f(T_j)]=O(ε²). The b_k do not
  enter at order ε, since f(T_j)=x_j exactly.
- Compensator order: no ε term, since C_k vanishes near T_j. No ε² term: the LOY
  bound excludes it directly, and φ→−φ forbids it in any expansion (cross-check
  only). Compensators do enter at order ε³: the clock shift t−T=O(ε²) depends on
  them and feeds in as εx_jF_j′(T_j)(t−T). Thus "only at ε³" means no lower
  order, not no effect. Exactly, ∂_uλ≤0 gives λ≤½, so t_(n,j)≥T_j.
- Constants: f→R→C₀→LOY C→r→ε_*. Here r does not depend on ε, n or the target,
  so Cε²<r/2 is not circular.
- No new regime: C11's F_k already put radiation before later readings.

### 4. §4 degree. VERIFIED

Consecutive differences give, for 2≤j≤N,

    L_j−L_(j−1) = b_jc_j + x_(j−1)²(a_(j−1)−a_(j−1)⁻) + x_j²a_j⁻,

which is the printed formula with the index shift correct.

- j=1: b₁=(e₁−x₁²a₁⁻)/c₁.
- Row N+1, where "similarly" must drop the a_(N+1)⁻ term:
  b_(N+1)=(e_(N+1)−e_N−x_N²(a_N−a_N⁻))/c_(N+1).
- Jacobian: [I 0; ∂L/∂x T], T lower triangular with T_jk=c_k for k≤j, so the
  determinant is Π_(k≤N+1)c_k>0, independent of (x,b).
- Ball: "since … interior" is not the reason, but the claim holds. Y⁰ is the
  restriction of a polynomial shear, a diffeomorphism of R^(2N+1). So Y⁰(∂R) is
  the boundary of Y⁰(R). An explicit r: any r<ρ with
  (2r+2r²max_k a_k)/c_j<b⁰_j/2 for all j. An open B_r inside Y⁰(R) misses Y⁰(∂R)
  by injectivity, so points of the half ball are more than r/2 from it.
- Homotopy: on ∂R, |Y⁰+s(Y_n−Y⁰)−w|>r/2−Cε²>0. Degree 1 is the sign of the
  determinant. Y_n is only continuous, which is all degree needs.

### 5. §5 limit. VERIFIED

t_j is not moving in the step where the mass is computed. The limit solution is
selected first, which fixes t_j as a number. INCOMING_MASS then runs u→−∞ at that
fixed V. This is its primary statement, weaker than the V→∞ statement C11 uses.
Its uniformity is on a fixed interval, and t_j lies in the F_j window. The moving
cut enters only p_n, a profile integral, so no finite-cone mass is identified
with a boundary mass. p_(n,j)→∫^(t_j)f_*² uses t_(n,j)→t_j and uniform f_n→f_*.
Both hold along the subsequence. Since p_(n,j)=e_j for all n, the limit is
exactly e_j.

Remainders pass as C11 §6 requires: n→∞ at fixed (u,v), then u→−∞.

### 6. §6 confinement. REPAIRABLE

Correct as written, for fixed V: Φ₁²=Φ₂², and σ is locally constant. The step to
|φ₂|=|φ₁|+O(ε³) also holds. It does not use σ, and it should not: t₁ and t₂ can
lie on opposite sides of a zero of Φ₁ where σ changes, so a signed comparison
could fail. Use the modulus. |Φ₁|=|Φ₂| at every V, including zeros, and |Φ₁| is Cε-Lipschitz:

    |φ₂(T)| = |Φ₂(t₂)|+O(ε³) = |Φ₁(t₂)|+O(ε³) = |Φ₁(t₁)|+O(ε³) = |φ₁(T)|+O(ε³).

So zero sets cause no failure and clock differences are handled. Three repairs:

(a) **Proper-time function.** Add the case E₁=E₂ on T. Since t′(T)=1/(2λ),

    E′(T)=Φ²(t(T))/(4·2λ),   2λ=1+O(ε²).

So |Φ₁(t₁(T))|=|Φ₂(t₂(T))|(1+O(ε²)), and the same conclusion follows. In both
cases |φ(γ(T_j))|=2√D+O(ε³), with D=m_-′(T_j) or E′(T_j). The centres therefore
come from the mass function alone, with no reference model.

(b) **"The class" is undefined.** Take selected limits of compact smooth profiles
with flat wedge v<A and LOY smallness ε̃=C₀ε, including |Φ′|≤ε̃. CUBIC_TRACE says
the trace bound passes to any compact limit, so no uniqueness at past null
infinity is needed. "As functions of V" also needs its normalization stated: v=t
on the flat wedge and λ→½ as u→−∞. §1's "no coordinate" does not cover V.

(c) **Exact form of "2^N points".** The count is right with "at most". Stated
precisely, for any pair ||y₂,j|−|y₁,j||≤Cε³, so

    y₂ ∈ ∪_σ Π_j [σ_j|y₁,j|−Cε³, σ_j|y₁,j|+Cε³].

That is at most 2^N boxes of side 2Cε³. If |y₁,j|≤Cε³ the two factors merge and
the sign of reading j is undetermined, so components can be fewer. This is the
only qualification at small Φ(T_j). The conclusion is stronger than stated: a
ball of radius above Cε³ is impossible, not merely one of radius ~ε. The bound is
attained in the family: x→σx keeps Φ² exactly, and readings separate when
|x_k|≫ε². It can be strict in the C¹ class: a sign cannot flip across a simple
zero.

### 7. Hidden dependencies

- Differentiability in parameters: none used. Y⁰ is smooth; Y_n is continuous.
  §6 differentiates m_- in V only, by the fundamental theorem of calculus.
- Target dependence: r and ε_* have none. Roots and subsequences do, as flagged.
  No continuous selection is claimed.
- Chain use: no use beyond the notes. CUBIC_TRACE item 2 names an F_k-plus-tail
  family, but the estimate derived above it needs only the LOY hypotheses, which
  hold with C₀ε. VERIFIED.
- **Smoothness line in §5: REPAIRABLE (scope).** The Theorem cites only C11 inputs
  and names no category, yet §5 asserts smoothness. That needs the separate
  chain of SMOOTH_FINITE_CONTROL.md, including its external inputs. The proof
  appears family-independent: it uses all-order profile norms and A strictly
  before the supports. But §3 of that note speaks of C11's families and lists
  incoming mass, not prefix masses. State the category as a separate conditional
  clause, and add that r, m and N_j are geometric under the C¹,¹ atlas change, so
  each E_j is preserved.

## Smaller corrections

- §7 bullet 3 is false as literally read. The mass between adjacent cuts is
  E_j−E_(j−1), which is fixed. Say "any proper subinterval that meets a varying
  pulse".
- §7 bullet 2 understates the result. Every positive strictly increasing vector
  is an e⁰, with b⁰_k=(e⁰_k−e⁰_(k−1))/c_k. Only r and ε_* depend on it.
- "Sharp limit" overstates §6. It contrasts finite cut lists with all cuts at
  fixed ε. The same construction appears to extend to any finite cut list with
  list-dependent r and ε_*; I did not write this out. No threshold is proved, and
  the quantifier order ∀list∃ε_* must not be exchanged.
- RESULT cites no primary source or read depth directly, and the brief's
  AGENT_REPORT.md and sources.jsonl do not exist. This is acceptable for a
  candidate note, not for task completion.

## Unresolved

- The whole chain: uniform cubic trace, finite-cone continuity, varying-profile
  compactness, the mass identity and the LOY estimates, all unreviewed here.
- Structure below ε³ at fixed m_-. With infinitely many zero-separated bumps,
  σ has infinitely many choices, and RESULT rightly claims nothing there.
