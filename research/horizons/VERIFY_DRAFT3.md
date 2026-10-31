# Referee check: "Unreal Is Not Open", draft 3

Scope: `research/horizons/main.tex` (draft 3) checked against
`coordinator-review/REVIEW.md`. Neither file was edited. Scripts are in the
session scratchpad: `verify3.py` (curvature and conformal covariance),
`echo.py` (harmonics and the antipodal identity), `trap.py` (a radial
causal-escape search). They were run with python3.11 and sympy 1.13.1.

## Verified

1. **Remark rem:laws.** Taking U = I⁻(b), which is open, the domain-of-dependence
   property gives Det(b) ⊆ F_L(b). In any spacetime J⁻(b) ⊆ cl I⁻(b), and
   global hyperbolicity makes J⁻(b) closed, so J⁻(b) = cl I⁻(b). Continuity
   then gives J⁻(b) ⊆ F_L(b), and the stated inclusion is correct. The flow
   example is also correct. Q = A + tB and P = B are the general solution. The
   past integral curve of u through x is a past-inextendible causal curve, and
   (Q, P) at any one of its points determine A(X) and B(X), so the law has the
   domain-of-dependence property. Every vertical line enters I⁻(b) once
   t < t_b − |X − Y|, so F_L(b) = M.
2. **Prop. prop:sharp.** The sympy check gives residual 0 for
   (□_g − R_g/6)(ψ/a) = a⁻³ □_η ψ with g = a(η)²η. The plane wave f(u) solves
   the flat wave equation when |k̂| = 1. On I⁻(b),
   u < −|Z−Y| − k̂·(Z−Y) ≤ 0, and at x, u = η_x − η_b + |X−Y| > 0. Conformal
   metrics have the same causal vectors, so they have the same causal curves.
   The slab is causally convex in Minkowski space because η is monotone along
   causal curves, so J⁻ in the slab is the Minkowski J⁻ intersected with the
   slab. The locator Wald 1984 Appendix D is correct as far as I know: the
   conformally invariant equation ∇ᵃ∇ₐφ − (n−2)/(4(n−1)) R φ = 0, with weight
   Ω^{(2−n)/2}, appears there. I did not check the equation number against the
   book.
3. **Prop. prop:echo.**
   - R(ESU) = 6 (sympy), so the equation is ψ_ηη = Δψ − ψ, with the sign correct.
     The sympy residual is 0 for the closed-dust covariance g = a²g_ESU.
   - The eigenvalues of Δ are −n(n+2); the check gives −3, −8, −15 and −24
     for n = 1 to 4. So the frequency is (n(n+2)+1)^{1/2} = n+1.
   - Degree-n harmonics are restrictions of homogeneous harmonic polynomials,
     so they have parity (−1)ⁿ. Each mode then picks up the factor
     (−1)ⁿ(−1)^{n+1} = −1 under A. sympy confirms ψ∘A + ψ = 0 for non-zonal
     modes with n = 1 to 4.
   - Extension to R×S³ follows from global well-posedness on the ESU.
   - The nonempty and disjoint claim is correct: J⁻(b) ⊂ {0 < η ≤ η_b}, so
     A(J⁻(b)) ⊂ {π < η ≤ η_b + π}, and A(η_b/2, Y) ∈ M. The echo is also disjoint
     from J⁻(b) itself.
   - trap.py found no evidence that the echo set fails to be exact. Radial
     causal curves escape the A-invariant zero set in every case tried. The
     open question in lines 307–309 is properly left open.
4. **Theorem, corollary, lemma and modal section.** These are sound.
   - The lemma parenthetical is fixed.
   - The rooted .2 correspondence (local Church–Rosser at b, which is
     equivalent to directedness of the generated subframe) is now correct.
   - "Failure of .2 … occurs with and without inflation" is fixed.
   - "Converse fails in two ways" has been replaced by "two geometric regimes",
     which is fixed.
   - The common-past criterion |X−Y| < η_x + η_y − 2η₋ is correct.

## REVIEW.md finding 1: mostly resolved

Det(b) is now explicitly a sufficient, "guaranteed" region. F_L(b) is
law-relative. The flow countermodel appears in the text with "the inclusion is
in general strict". Necessity is proved only where it holds, by Prop. sharp in
the flat models. Some summary sentences still overstate what is shown.

## Issues

### MUST-FIX

**M1. Conclusion, lines 407–409, and Intro Q1, lines 77–78.** The theorem
characterizes Det(b). That set is a lower bound on what every such law fixes,
not "what every local deterministic law fixes". Even in Minkowski spacetime,
every continuous law with the domain-of-dependence property fixes J⁻(b), which
is strictly larger than Det(b) = I⁻(b). The paper does not prove that the
intersection of F_L(b) over all such laws equals Det(b) ∪ J⁻(b) in general.

- Conclusion replacement: "What the causal structure guarantees — what every
  local deterministic law fixes in virtue of the domain-of-dependence property
  alone — is characterized by a slicing condition on Geroch's domain of
  prediction (Theorem 3); it is a lower bound on what any particular law fixes."
- Q1 replacement: "Which events are guaranteed from b, that is, fixed from what
  is real from b by every deterministic local law in virtue of causal structure
  alone (Theorem 3)?"

**M2. §5 item 3, lines 348–351, and abstract lines 46–48.** The paper says
"the answer to 'is the future open from here?' can differ between two events".
It has shown only that *guaranteedness* changes at maximum expansion, and line
308 leaves open what any law fixes before then. REVIEW.md explicitly said not
to infer epoch-dependence of openness from the sufficient region. Also, global
causal structure does not "change with cosmic epoch"; what changes is whether
b's past contains a Cauchy surface. There are two possible repairs.

- (a) Restrict the claim: "What is guaranteed from an event is decided by the
  causal structure, and in the closed dust model it changes with the event's
  epoch, so whether the future is guaranteed from here can differ between two
  events of one spacetime."
- (b) Keep the stronger claim and add an example that proves it. I checked
  this one. In closed dust take u = a⁻¹∂_η and the law of Remark rem:laws, so
  Q = A(X) + ηB(X). Every comoving line enters I⁻(b) iff d(X,Y) < η_b (for
  η_b ≤ π). Hence F_L(b) = (0,2π) × B̄(Y, η_b), which is not M when η_b < π
  and is M when η_b ≥ π. Suggested sentence: "Under the comoving-flow law of
  Remark 2, F_L(b) = (0,2π)×B̄(Y,η_b) ≠ M when η_b<π and F_L(b)=M afterwards, so
  for this law what is open from b does change with b's epoch."

For the abstract, replace "depends on global causal structure, which can change
with cosmic epoch" with "depends on the causal structure, whose verdict differs
between events of different epochs".

### SHOULD-FIX

**S1. Lines 280–281.** "Carries its value there exactly" is wrong. ψ = aφ
reappears with reversed sign: φ(A q) = −a(η_q)/a(η_q+π)·φ(q). Replacement:
"and the rescaled conformal scalar aφ reappears there with reversed sign."

**S2. §5 item 1, lines 332–335.** "For particular fields this happens more
widely" refers back to "unreal and guaranteed". The echo set is disjoint from
Det(b) (Prop. echo), and the flow law's extra events are not guaranteed either.
Replacement: "For particular fields, unreal events are fixed, though not
guaranteed, more widely: …"

**S3. Line 343, "is then exactly".** "Then" presents the result as following
from the absence of a Cauchy surface, which is the inference REVIEW.md
rejected. The result rests on Prop. sharp alone. Replacement: "For the
conformal scalar … what is fixed from b is exactly J⁻(b) (Proposition 7)."

**S4. Lines 351 and 416–417, "Relativity settles the first".** Relativity does
not fix the spacetime; Det(b) is settled given M. Replacement: "the causal
structure of the given spacetime settles the first; it does not settle the
second."

**S5. Manchak, lines 274–276 and 364–365.** REVIEW.md §5 records that Manchak
2008 was not read in full. Neither paraphrase ("requires a compact Cauchy
surface"; "cannot verify") has been pinned to the original text's hypotheses.
Check the source or soften to "compare Manchak's discussion of prediction
[Manchak2008]".

**S6. Abstract line 39, "the bound is attained".** The phrase does not say
which bound. Replacement: "the minimum Det(b) ∪ J⁻(b) = J⁻(b) that every
continuous such law must fix is attained".

### OPTIONAL

**O1. Line 125.** Replace "Their characteristics are the integral curves of u,
so…" with the direct argument: "(Q,P) at any point of an integral curve of u
determine them along it, and the past integral curve from x is
past-inextendible causal, so…".

**O2. Prop. sharp, lines 239–240.** Add "and the slab is causally convex in
Minkowski spacetime".

**O3. Prop. echo.**
- Write "agree on I⁻(b), hence by continuity on J⁻(b)".
- The nonempty and disjoint claim also holds at η_b = π, which would align it
  with line 308's "η_b ≤ π".
- Add "by global well-posedness" to the extension step.

**O4. Line 142, "the two differ at most on null boundaries".** This is
unproved. It is not even clear that a timelike-curve version of Det differs
from Det only on boundaries. Hedge: "we expect the two to differ at most on
null boundaries."

**O5. Line 271, "exactly the condition".** The literature places the horizon's
disappearance at η = π, but Det(b) = M holds only for η_b > π. Replacement:
"once the particle horizon has vanished (η_b > π), everything is guaranteed".

## Residual grep (abstract, intro, §5, conclusion)

I searched for "nothing", "exactly", "fixed", "open", "determined", "settles"
and "decides".

- Still overclaiming: lines 77, 343, 348–351, 407 and 416–417 (M1, M2, S3, S4).
- Acceptable: lines 38, 40, 325, 346, 356, 359, 376, 400 and 406. Each is
  scoped to "guaranteed", to Prop. sharp, or to a cited result.
