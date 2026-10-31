# Repaired screening theorem and a fully specified field-determination consequence

28 October 2026. Coordinator revision alongside Claude's SCREENING.md. No edits to that active lane. The geometry is a standard-causality deduction; the field consequence is a corollary of standard hyperbolic uniqueness, not a novelty claim. Independent review requested.

## Definitions

Let (M,g) be a connected smooth time-oriented globally hyperbolic spacetime without boundary, with marked b. Let

 B_b=M minus (Jplus(b) minus {b}),
 P_b={b} union {x: not(b prec x), and there exists z with b prec z and x prec z},
 W_b=Iminus(Iplus(b)) minus Jplus(b).

Here prec is distinct causal precedence including null pairs. Then

 P_b=Jminus(Jplus(b)) minus (Jplus(b) minus {b}),
 P_b=W_b union {b}.

The second identity uses push-up: a common causal successor can be extended chronologically, and every nonmarked point of P_b is outside Jplus(b). In particular W_b is open. It is causally convex because Iminus(Iplus(b)) is a past set and Jplus(b) is a future set.

Define smooth screening for R subset B_b by requiring Jplus(b) subset Dplus(Sigma intersect R) for EVERY SMOOTH SPACELIKE Cauchy hypersurface Sigma disjoint from b's strict causal future. This fixes the convention; no null-containing topological Cauchy surface is needed.

## Theorem A: exact smooth screening

R smoothly screens b's future iff P_b subset R.

Sufficiency: a past-inextendible causal curve from z in Jplus(b) meets Sigma. Its intersection y lies in Jminus(Jplus(b)) and outside b's strict future, hence in P_b subset R. The intersection is on the past part of the curve: a future intersection would lie in the forbidden strict future of b, apart from the trivial z=b point. This proves the domain-of-dependence inclusion.

Necessity: take x in P_b and a future witness z in Jplus(b) with x<=z. We can choose a smooth spacelike Cauchy surface Sigma through x avoiding b's strict future:

- If x=b, take a Cauchy temporal level through b.
- If x strictly precedes b, take a Cauchy temporal level through x. Temporal monotonicity places Jplus(b) strictly above it.
- If x is spacelike to b, extend the finite acausal set {x,b} to a smooth spacelike Cauchy surface. Bernal--Sanchez Theorem1.1 and Remark4.14 supply this, or first use two small compact spacelike acausal disks and apply their disconnected extension. Acausality of a surface containing b excludes every strict future point of b.

Choose a past-directed causal curve from z through x, and continue it past-inextendibly. It meets the acausal Cauchy surface only at x. If x is absent from R this curve misses Sigma intersect R, so z is absent from Dplus(Sigma intersect R). Contradiction. This proves necessity without a C0-convention ambiguity.

## Theorem B: fixed-background field determination, with no localized MGHD premise

Fix a smooth scalar normally hyperbolic linear operator L on this SAME (M,g), for example the real Klein--Gordon operator with specified smooth mass/curvature-coupling potential. Let u,v be global smooth solutions of Lu=Lv=0. If they agree on W_b, they agree on all of Jplus(b). More generally it suffices that they agree on R and W_b subset closure(R), with closure in the fixed common spacetime. It is enough for R to be a countable dense subset of W_b.

Proof: continuity first gives w=u-v=0 on W_b in the more general case. Choose a Cauchy temporal function t with t(b)=0 and a smooth Cauchy slice Sigma={t=-1}. Let K=Sigma intersect W_b. Because W_b is open, w and its normal derivative vanish on K. Theorem A gives Jplus(b) subset Dplus(K), since Sigma intersect P_b=K. Domain-of-dependence uniqueness for a normally hyperbolic operator gives w=0 on Dplus(K), hence on Jplus(b).

One can formulate the uniqueness step on the globally hyperbolic domain D(K), with K its spacelike Cauchy surface, or use local uniqueness on compact causal diamonds and an exhaustion. No assertion that D(K) is a MAXIMAL development is needed: both w and zero already solve the SAME fixed-background equation on that domain. For a specified solution category, source the corresponding homogeneous uniqueness theorem; compactly supported global existence statements alone should not be confused with the arbitrary-solution local uniqueness used here.

The density clause proves explicitly that minimal geometric screening is not minimal physical data determination. A countable dense set is sufficient here only with exact values and known continuity on a fixed manifold. This is not a finite-precision inference procedure, a countable set of feasible measurements, or a minimal necessary data set.

## What this repairs and what it does not

Theorem A is the exact geometric result Claude was pursuing, now for unambiguously smooth spacelike slices. Theorem B is an actual dynamical implication in a named physical test-field class, rather than an unverified application of restricted-data MGHD maximality. It strengthens proof status while narrowing scope.

It does not compare different dynamical metrics or identify their futures. It does not establish the localized Lprime premise for Einstein--matter equations. The coupled-rigidity proposal remains separate and conditional. A dense common set in a fixed spacetime is not an abstract isometry-extension theorem for punctured or incomplete realms.

## Safe philosophical statement

The specified point-level causal-potential realm is exactly the minimal realm for a universal causal-curve interception property. It is also sufficient to fix future solutions of the stated homogeneous test-field theory. These are two distinct results. The surplus bow-tie points have no causal route to b's own future in this fixed geometry, so they are not required by THIS screening criterion. This does not rule out other global, modal, compositional or cross-standpoint motivations for including them.

Future determination in a specified equation does not establish existence of future events, and fixing the background geometry is a material limitation for the ontological application.
