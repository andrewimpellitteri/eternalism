# Independent red team: Unreal Is Not Open

Reviewed 2026-10-25. Source: `research/horizons/main.tex` at commit
`451c4d0`, SHA-256
`26f2d35cb19c0efbc49b0a07e2e30903e4664a49f5d42a1728fdb05da0250fdf`.
Line numbers below refer to that source. This report does not change the
concurrently authored manuscript. Previous reviews are evidence leads, not
independent certification.

## Verdict

**Revise before circulation.** The slicing theorem and standard-model geometric
calculations survived this assessment. A central interpretive inference does
not: the domain-of-dependence property assumed in the paper is sufficient for
determination inside Det(b), but does not make membership necessary for
law-relative determination. Negative conclusions about what the past cannot
fix therefore require a new hypothesis or narrower wording.

The positive conclusion that an unreal future can be fixed survives, conditional
on the becoming assumptions and the dynamics. The closed-dust calculation is a
useful illustration of that conclusion. This review does not certify exhaustive
novelty, realistic cosmology, or the companion Stein-GR proof.

## 1. Blocking: sufficient geometry is treated as necessary dynamics

**Locations:** definition and laws remark, lines 92–110; introductory question
72–73; philosophy 239–260; conclusion 311–319; corresponding abstract wording.

Let U=I_s^-(b). The assumed property is

> If every past-inextendible causal curve from x meets U, data on U fix the
> fields at x.

This gives Det(b) as a **guaranteed sufficient region**. It does not imply that
fields outside Det(b) admit different values in two solutions agreeing on U.
Calling Det membership “settled” by definition is legitimate, but does not
establish the ensuing claims about everything the selected laws actually fix.

### Explicit local, deterministic, nonstationary countermodel

Work on fixed Minkowski spacetime M=R×R³, with the prescribed unit timelike
flow u=∂t. Let two scalar fields satisfy

    u·∇Q = P,       u·∇P = 0.

Every smooth solution is

    Q(t,X) = A(X) + t B(X),       P(t,X) = B(X),

for arbitrary smooth spatial functions A and B. These are local, well-posed
first-order equations: their principal matrices are A⁰=identity and Aⁱ=0,
so their characteristics have zero spatial speed, inside the metric cones.
The model has infinitely many degrees of freedom and need not be stationary.
The flow is extra background structure; the paper does not forbid it in its
stated dynamics assumption. This is a test of that assumption, not a proposed
cosmological matter theory or an ontology inferred from a toy field.

It satisfies precisely the stated domain-of-dependence property. The past
vertical integral curve through x is one of the past-inextendible metric-causal
curves. If all such curves hit U, this one hits U at (s,X). There the data give
P(s,X)=B(X) and Q(s,X); the equations uniquely give Q and P at x. The argument
works for any data region U to which the paper's sufficient condition applies.

Now take b=(0,0). For **every** X and every target time t, select

    s = -1 - |t| - (|X₁|+|X₂|+|X₃|).

Then s<t and s<-|X|, so (s,X) lies in I_s^-(b). Consequently data on the
whole strict past of b determine A(X), B(X) for every X, and hence determine
the entire field solution on M, including Q and P at the timelike-future
event x=(1,0).

But x is outside the paper's geometric Det(b). For example, the past-directed
null ray γ(λ)=(1-λ,λ,0,0), λ≥0, is past-inextendible and never enters
I_s^-(b): its time coordinate exceeds minus its spatial radius by 1.
Thus even a timelike-future event can have all the model's field data fixed
while failing the geometric criterion. No superluminal propagation is involved.

The source of this effect is worth emphasizing: the input region is the
**entire unbounded chronological past**, not a single observer's practical
record. It contains earlier data on every vertical worldline. A speed bound
on possible influences supplies an upper bound on domains; it does not require
every permitted causal direction to carry independently variable information.

### Consequences for the manuscript

- “Nothing outside the observer's past [is fixed], whatever lies in that past”
  does not follow under the stated class of laws.
- Absence of a complete Cauchy surface inside I_s^-(b) does not show those data
  fail to determine future fields. A sufficient condition cannot be negated to
  obtain a necessary one.
- The geometric threshold changes with epoch in closed dust; an actual
  law-relative determined set need not first change at that threshold.
- A smooth field agreeing on an open region also agrees on its closure by
  continuity. Even the null-boundary distinction needs attention before claiming
  an exact characterization of actual field determination by this open set.

### Two defensible repair routes

**Minimal route:** retain the geometric definition and all its proved
calculations. Call it the *geometrically guaranteed determination region*.
State that membership supplies a sufficient guarantee for the assumed laws.
Replace negative physical conclusions with “not guaranteed by this geometric
criterion.” Keep the positive closed-dust result and distinguish it from
necessary conditions on prediction. Amend the abstract, question, philosophy
and conclusion consistently, not only the laws remark. Do not claim actual
openness changes with epoch merely because this sufficient region changes.

**Stronger route:** specify a solution class and observables, define x as fixed
when any two admissible solutions agreeing on U agree at x, and prove an exact
characterization. Necessity requires an actual pair of solutions for each
excluded x, with constraints, boundary regularity and permitted backgrounds
accounted for. Alternatively adopt an explicitly geometric definition of
“open,” while making clear its difference from dynamical or metaphysical
openness. The latter is a terminological choice, not a proof of necessity.

## 2. Mathematics that survived independent examination

### Slicing characterization (lines 122–143)

No counterexample or proof gap found under the stated global hyperbolicity
and surjective Cauchy-time hypotheses. The compact inverse-limit argument
works even though coordinate-forgetting maps need not be onto: in the product
of compact K_c sets, the finite causal-chain conditions are closed and have
the finite intersection property. This supplies a compatible infinite chain.
Push-up ensures every joined segment avoids the open past. A Cauchy time
approaching its lower interval endpoint cannot have an endpoint inside M,
including when the interval endpoint is finite. The joins are locally finite
in the interior time range and give a causal curve after parametrization.

The corrected Cauchy-surface corollary also handles x on or below the surface;
the proof no longer presumes all targets lie above it.

### Product-model calculations

For the stated full R³, H³ and unit-S³ spatial geometries, the ball-containment
argument supports the formulas. On the sphere, an interval wider than π permits
Det(b)=M once η_b>η_-+π. At equality the strict chronological-past convention
still gives the smaller region. Closed dust has conformal interval (0,2π)
and maximum expansion at π; the strict inequality is correctly retained.
Einstein static, closed radiation, and global de Sitter have the stated
geometric behavior. These calculations are not a claim about every topology
of a spatially closed model or about observationally viable cosmology.

**Small correction, lines 170–171:** the parenthetical “always so on R³ and
H³” attached to d(X,Y)+r₁≤π is false as a numerical inequality. Say instead
that geodesic extension works without a π bound on these unbounded spaces;
only on S³ does the proof split at π. The lemma itself survives. State r₁≥0
and the intended radius range explicitly if not already understood.

## 3. Modal wording needs two corrections

**Lines 283–287:** on arbitrary reflexive transitive frames, .2 corresponds to
the local common-successor condition

    wRx and wRy imply some z with xRz and yRz.

It is not equivalent to global directedness of the entire frame. A disjoint
union of two reflexive singleton frames validates .2 but is not globally
directed. On the frame generated by a particular root b, validity of .2
**at b for all valuations** is equivalent to directedness of that generated
frame. With past accessibility the successors in this formulation are common
causal pasts. State this rooted version, which is what the subsequent argument
uses. This is a precision repair, not a refutation of the horizon example.

**Lines 293–295:** “the failure of .2, which holds on both sides of it” reads as
claiming .2 holds, contrary to the preceding paragraph. Say explicitly that
**failure** of .2 occurs with and without finite-conformal-duration inflation.

The finite-lower-conformal-endpoint common-past calculation and its counterpairs
inside every generated past are sound. Keep arbitrary valuations separate from
persistent truth assignments and from any claim that the exact logic of all
globally hyperbolic frames has been established. The current open-question
caveat is appropriate.

## 4. Philosophy and release gates

“Unreal,” “not fixed by a given law and data set,” “unknown to an observer,”
and “true on some but not all histories” are different predicates. The revised
Belnap caveat recognizes part of this. The necessary/sufficient gap above still
crosses the boundary between geometric sufficiency and law-relative fixing.

The text's “converse fails in two ways” also needs literal checking: where no
events beyond the fragment are geometrically settled, the converse has not
failed in that way. Say that standard examples exhibit two geometric regimes.
The positive counterexample to “unreal implies unfixed” is the closed model;
the open models do not establish an independent opposite direction under the
stated general dynamics assumption.

Before circulation:

1. Resolve finding 1 by one explicit route, including all summary claims.
2. Correct the modal-frame wording and the two small proof/prose errors.
3. Independently reread the revised abstract and conclusion against the actual
   hypotheses. Search for “nothing,” “exactly,” “fixed,” and “open” to catch
   residual stronger claims. Rebuild afterward.
4. Preserve attribution: the dust horizon threshold and Geroch's construction
   are prior work. Describe the slicing statement as the proposed contribution
   subject to a bounded priority audit, not a certified new open-problem solution.

These are circulation gates for this manuscript, not a guarantee that every
possible hole is closed. Expert review remains particularly valuable for the
scope of the proposed slicing refinement and for the bridge premises.

## 5. Source audit and limits

- **Geroch, “Prediction in General Relativity” (1977), §§2–3, printed pp.83–90:**
  selected full text read from the LSE scan, not a reproduction of every theorem.
  The Maxwell example in §2 is a uniqueness statement inside a domain of
  dependence; §3 introduces an explicitly geometric prediction region and the
  Einstein-universe example. It does not supply the missing converse for all
  local dynamics assumed here. Scan:
  https://personal.lse.ac.uk/robert49/ppb/pdf/GerochPredictnInGRMinnesVol81977.pdf
- **Grøn and Johannesen, arXiv:1103.4753v1 (24 March 2011), §2.2, equations
  (11)–(15) and the discussion following them:** selected full text checked.
  The dust particle horizon disappearing at maximum expansion is explicitly
  prior work, not a novelty of this paper. This confirms the manuscript's
  demotion of that fact to an example.
  https://arxiv.org/html/1103.4753v1
- **Manchak (2008):** bibliographic discovery and previous reviewers' reports
  only in this pass. The author's PDF timed out; no independent full-text or
  proof verification is claimed here. In particular, the exact observational
  verification impossibility statement still needs its hypotheses pinned to
  the original text. Do not upgrade an unavailable source to “checked.”
- The cited modal-logic textbook, Goldblatt's exact completeness theorem,
  Rakić's original argument, and the Lewis–van der Schaaf comparison were not
  independently reverified in full in this pass. The elementary frame repair
  above follows directly from Kripke semantics and does not depend on a claim
  to have read those proofs.

The accompanying exact-arithmetic check corroborates the explicit countermodel
and a modal negative control. It is not a computational proof of the general
slicing theorem, a model of our universe, or a literature-completeness test.
