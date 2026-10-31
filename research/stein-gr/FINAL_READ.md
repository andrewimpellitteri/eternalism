# Final consistency read of main.tex

25 October 2026. Whole-document read of `research/stein-gr/main.tex` (900 lines) against
INDEPENDENT_REVIEW / REVIEW_MAIN_PROOF / REVIEW_OTHER_RESULTS / SECOND_PASS_REVIEW (for
what was fixed), Minguzzi-Sanchez (MS) text and Clifton-Hogarth (CH) text. Depth: full-text
hand check of every proof; no recompilation. I could not check the Bernal-Sanchez citation
(Thm 1.1, Rem 4.14) against its text, only the logic of how it is used.

## Verdict

Ready for expert read after a short list of should-fix items. No must-fix mathematical
error found in Theorem main, Lemmas B-F, Theorem class/weyl, Prop reg, Cor worldline or
the causal-set proof. Two must-fix items are claim/proof mismatches in prose and one
definition clash; all are one-line repairs.

## A. Verification that earlier repairs are present and correct

- Strict vs reflexive chronology: framework defines I_s and I = I_s u Delta (l.139-145).
  Prop reg uses closure(I)=closure(I_s)=closure(J), Int J = I_s, B\Delta subset I_s, then
  (CB) (l.358-363): correct. Lemma D(iii) uses strict I_s diamonds (l.557-559): correct,
  and MS 2.16/2.17/2.31 citations match the MS text (2.31(i) push-up, 2.31(ii) horismos
  composition). Present and correct.
- Lemma D(ii): tau_0 <= tau_exit with equality included, tau_exit < tau_0 case with
  t>0 at exit, reverse inclusion via S as Cauchy surface (l.528-545). Correct; I traced the
  case split including the simultaneous-crossing case. The p in Sigma' case is
  handled before the stopping times.
- Gaussian coordinates: Phi({t=0}) subset S, t>0 in I^+(S), metric -dt^2+h_t, exactly eta
  on y=0, t=0 for all s in [-rho,L+rho] (Lemma B). Correct.
- T_rho s-range -rho<s<L+rho nested, closure(T_2r) in T_3r; constants order mu,lambda,eps
  -> rho_0,K -> r with 3r<rho_0, 6Kr<=eps, 8 lambda r<L (l.477-491). Lemma C algebra
  checked: both thresholds are exactly the stated ones; signature argument valid;
  convex interpolation preserves the bound. Correct.
- Escape paths: speed mu/2 over time 2r gives |y| in (r/2,3r) since mu>1/2 and mu<1.
  Correct. Flat arc: 10 r sin(pi/8) = 3.83 r > 3r, |t|>3r otherwise, slope 8r/L<1/lambda,
  endpoints w=(-4r,0), v=(4r,L) match t(s); chain w<<psi(x), psi(x) B psi(b), psi(b)<<v
  and, in (b), the reversed chain, are in the right direction. Correct.
- Bernal-Sanchez applied to the union of two small acausal discs with no causal curve
  between them (l.433-438): logic correct. Citation locator unchecked by me.
- Milne wedge argument in Prop nonlocal (l.224-229): correct (W = I^+(0) is open, causally
  convex, GH; tau_W finite = proper time; tau = infinity on Mink since past curves have
  unbounded length).
- Prop single: P o P argument and the J o P, P o J cases are correct.
- Godel convexity proof (l.675-679): correct (concatenation of timelike p->q, q->p).
- Wuthrich-Callender and Viglione claims are softened ("true on its own terms",
  "stricter", "akin to"). Present. The CS proof is correct (adjoining e < x only keeps I
  convex; I u {z} disjoint union).
- Cor worldline: proof is correct given the hypotheses; the worldline transitivity form
  matches CH p.363 text (a in B_lambda(b), b in B_lambda'(c) => a in B_lambda'(c)).
  Existence of inextendible timelike curves through each point, and extension of a
  timelike a->b curve, are fine.
- prop:dec flat-data argument: corrected for K=0 but see S2 below.
- Mechanical: every \ref/\eqref resolves; every \cite key has a \bibitem and vice versa;
  there are no hard-coded "Theorem N" references except to CH's own Theorems 1 and 2
  (correct). CH quote "no obvious way ... much less to extend Theorem 2" and "more
  difficult, though more interesting" match the CH text.

## B. Findings

### Must-fix

M1. Notation clash, l.140 vs Prop godel (l.671). The framework defines x<<y as
x in I^-(y) with x != y, but Prop godel writes "p << p for all p" for total viciousness.
Repair: define << as the strict relation (x in I_s^-(y), allowing x=y when a closed
timelike curve exists), and in Prop godel write p in I_s^-(p). Also state in the text
that "I_s subset I" and Delta subset I are used for reflexivity in totally vicious M.

M2. "Non-universal" is used (Thm class, Prop reg, Cor nopresent, l.255, 294, 316, 262) but
never defined. Repair: add after Theorem main: "Call B universal if B_M = U_M for every M;
by Theorem main this holds iff B_Mink = U (and then it holds for some M iff for all);
otherwise B is non-universal."

M3. Cor nopresent / trilemma (l.260-270, 768-774) overreach by an unstated bridge premise.
The corollary shows that mutual becoming (x B b and b B x) forces x=b. The trilemma
reads this as "locality, a shared extended present, and non-trivial becoming cannot all be
had", which silently identifies "shared present" with co-presence in this sense. A rival
view (present = events neither of which has become for the other, or Stein's
"definite for" read differently) is not touched. Repair: in the trilemma paragraph insert
"if a shared present is understood as a set of events each of which has become for each
other (the sense in which Stein's dilemma is posed)". Also verify or drop the claim that
"Stein's 'pluralistic' reading already suggested point-like presents" (l.771-773): nothing in
the project files cited supports it; attribute to a specific page or remove.

### Should-fix

S1. Prop godel / Godel paragraph (l.668-696) vs abstract. The abstract says Godel-type
universes "constrain nothing here". But transmission out of a Godel universe would run along
morphisms FROM it; Prop godel is about morphisms INTO it, and the text concedes "we have
not shown that no morphisms lead out". The sentence "does not transmit anything out of
totally vicious ones by morphisms into them" is also garbled. A one-line fix closes the gap:
an open totally vicious subset of a causal spacetime is impossible (it contains closed
timelike curves), so no morphism leads from a totally vicious spacetime into any causal, in
particular any globally hyperbolic, spacetime. Add this as a second clause of Prop godel,
rewrite the garbled sentence, and keep "here" in the abstract = globally hyperbolic. Without
this, soften the abstract to "isolates ... for transmission into causal spacetimes".

S2. Prop dec proof (l.704-724) proves less than the statement says. The statement is for
any Cauchy surface with a flat neighbourhood; the proof assumes the data (Sigma,h,0), i.e.
K=0. That suffices for M' (the slices t=c with c<-3r are totally geodesic) but not for the
general statement (e.g. a flat slice with K != 0 inside Minkowski). Repair: either restrict
the statement to "flat neighbourhood of a totally geodesic Cauchy surface", or replace the
Choquet-Bruhat-Geroch paragraph with: after G=0 the metric is vacuum, the Riemann tensor
satisfies a linear homogeneous wave system (box R = R*R) with zero Cauchy data on the flat
neighbourhood, hence R=0 on D(Sigma)=M. This is also shorter and avoids the claim about the
static development R x Sigma. Note also that "vacuum" here means G=0 so Ric=0, Lambda=0.

S3. Abstract and l.109-112 / 784-793: "relations determined by causal structure alone".
The Weyl relation depends on the conformal class, not on the bare causal relation. These
are equivalent only via Malament-type reconstruction theorems (distinguishing spacetimes),
which the paper does not cite. Repair: say "determined by conformal structure alone" (as
Thm weyl already does), or cite Malament 1977 / Hawking-King-McCarthy.

S4. Notation clash: h denotes the induced metric on S (set-up, Lemma B, sigma) and also an
arbitrary 4-metric in Lemma C (l.465-472). Repair: rename Lemma C's metric to k (or g_*),
and the induced metric to h_S.

S5. l.329-330 states MS Thm 2.30 as "a causal curve that is not an unbroken lightlike
pregeodesic can be deformed to a timelike curve". MS 2.30(i) says "not a maximizing
lightlike curve". The use in Thm weyl is valid (a causal curve between horismotic points is
by definition not deformable, hence maximizing, hence a geodesic by 2.30(ii)), but cite both
parts correctly.

S6. Intro bullet on energy conditions (l.123-126) says the key construction is "provably
unavailable". Prop dec shows only that this specific M' is not in GH_DEC unless g is flat on
T_2r; the Pocket problem is about alternative constructions. Repair: "the specific
auxiliary spacetime is provably unavailable".

### Optional

O1. Date: title says 24 October, review files 25 October; harmonise if needed.
O2. l.203-206: "the dust-cosmology ordering by scalar curvature ... is a symmetric instance"
is cryptic; either give one sentence or drop it (not used later).
O3. Theorem class: "On Mink, N is empty or all of E^-" is deduced from Theorem flat; say
"by Theorem flat, since B_Mink in {I, J}".
O4. l.726-731 "no pocket can be inserted" should read "no such pocket can lie in the domain
of dependence of unmodified vacuum data".
O5. l.746: "Thin shells will not suffice in general" is a heuristic; flag as such.
O6. Prop nonlocal: "B relates spacelike pairs in every spacetime where tau is finite" holds
because every spacetime has spacelike pairs and B is total on tau-comparable points; one
phrase would make that visible.
O7. Add one sentence in the framework that the becoming relation B_M(x,b) direction
"x has become for b" is used consistently, including in the Cor nopresent proof.

## C. Cross-reference and numbering check

All 29 labels resolve; unused labels are section labels only. No prose reference to a
numbered theorem of this paper. Theorem~1/2 mentions refer to CH. MS proposition numbers
(2.10, 2.12, 2.16, 2.17, 2.30, 2.31, 3.68(iii), 3.70, 3.71, 3.75) exist in the MS text with
the content cited (3.68(iii) is "J^+ closed in MxM"; 3.71 gives closed J^pm(p)).
