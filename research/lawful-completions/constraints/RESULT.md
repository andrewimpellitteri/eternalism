# Constraints lane: exact gluing results and a candidate past-preserving lemma

Lane: `constraints/` of `research/lawful-completions/`. Date: 2026-10-28.
Status: technical feasibility submission for review. Not a theorem of ours, not a
novelty claim. Sources: `sources.jsonl` (same directory); IDs below refer to it.

Verdict for the assigned subproblem ("spacelike/characteristic gluing,
coupled-matter realizability, charge/genericity restrictions; exact usable
theorem or named missing lemma"): **CONDITIONAL**. One usable conditional
construction (Lemma P) and three named missing steps (M1-M3), each with a
falsifier. Nothing here is PASS: the coupled-matter theorem itself is not in the
literature at our search depth, and the one load-bearing citation
(constraints-c05, Corvino-Schoen) was read only at secondary attribution this
run. Nothing here is KILL: no obstruction found blocks the construction.

## 1. Extracted primary results (exact hypotheses, conclusions)

All four brief leads were fetched at primary pages on 2026-10-28. Two were
deep-read partially (theorem statements verbatim); titles and claims of the
others are recorded at abstract depth. Note one correction to casual naming:
arXiv:1606.03078 is "Localized deformation for initial data sets with the
dominant energy condition" (Corvino-Huang, Calc. Var. PDE), not a "local gluing
of time-symmetric data" title.

### 1.1 Corvino-Huang 2020 (constraints-c04) - the DEC anchor (deep read)

Setting: initial data set (g,pi) (pi = momentum in the K - (tr K)g convention),
constraint map Phi(g,pi) = (2mu, J), DEC mu >= |J|. Modified operator
Phi^W_{(g,pi)}(gamma,tau) = Phi(gamma,tau) + (0, (1/2) gamma ._{g} (J+W))
absorbs the first-order metric change in the DEC inequality (their (1.1)
discussion shows why plain local surjectivity does not promote weak to strict
DEC).

- **Thm 1.1.** (g,pi) in C^{4,alpha} x C^{3,alpha}(Omega-bar), Omega compact
  with boundary; **no-kernel condition**: kernel of DPhi^0*_{(g,pi)} trivial on
  Omega. Then for small (psi,V) there are (h,w) with
  mu_bar - |J_bar|_{g_bar} >= mu - |J+V|_g + psi. Smooth output from smooth
  input (Thm 1.2, C^{k+4,alpha} framework, deformations in C_c^{k+2,alpha}).
- **Thm 1.3.** Interpolation gluing of two data sets CLOSE to a common
  (g0,pi0) across an annulus: DEC interpolates, inequality only.
- **Thm 1.4.** Asymptotic gluing to a member of an admissible family
  (Kerr; also non-vacuum Kerr-Newman) across B_{2R} \ B_R for R large, exact
  equality in B_R and outside B_{2R}, **without** any kernel assumption
  (finite-dimensional approximate kernel absorbed by the family), ADM energy
  raised: E_theta > E by controlled small epsilon.
- **Example 2.4 (key genericity fact).** At flat data (g_E, 0) the adjoint
  kernel is 10-dimensional (1 + x^i and translation/rotation fields).
  Proposition 2.1: kernel elements are real-analytic-type (ODE-along-geodesics
  rigidity), finite-dimensional, and cannot vanish on open sets.

Crucial negative remark (authors', sec. 1, after Thm 1.4): "our gluing results
do not fully recover the vacuum gluing results ... since we do not obtain
EQUALITY for the dominant energy condition." **This closes the DEC shortcut:**
DEC-inequality deformations do not, and are not claimed to, produce data of a
fixed matter model.

### 1.2 Czimek-Rodnianski 2022 (constraints-c03) - obstruction-free, vacuum (deep read, secs 1-2.6)

- **Thm 2.9 (main).** Null gluing near Minkowski with charge gaps satisfying
  Delta-E = C1*eps (strictly positive), |Delta-L| <= C2 eps^2,
  eps^{-1} Delta-E > C3(eps^{-1}|Delta-P| + eps^{-1}|Delta-G|), C3 above a
  universal constant. Output: null data matching S2 EXACTLY; S1 is PERTURBED
  (S1', with x1' - x1 = O(eps)-controlled).
- **Cor 2.13.** Spacelike corollary: asymptotically flat data (Def 2.12:
  g - e = O(r^-1), k = O(r^-2); NO Regge-Teitelboim parity needed, unlike
  Corvino-Schoen) glued to a CHOSEN Kerr (or Schwarzschild of any mass
  M > M0) across a far-out annulus A_[R,2R], under the same type of charge-gap
  conditions on ADM parameters.
- Regularity: authors' Sobolev-type X and high-frequency X^{h.f.} norms; the
  precise indices (their sec 2.2) were not read this run (access limit). The
  predecessor ACR II result is explicitly finite-regularity: C^{m+2}
  tangential, C^2 transversal (constraints-c02, abstract).

Read correctly, "obstruction-free" is **not unconditional**: the method uses
the nonlinearity to absorb the 10 charges at the price of a strictly positive
energy gap of order eps and dominance of E-gaps over P,G-gaps; it is
perturbative near Minkowski; and the target is a model family in the
asymptotic region, not an arbitrary prescribed interior deformation. Also,
matching on the seed side is only up to O(eps) on a perturbed sphere, so this
gluing cannot by itself preserve a specified past EXACTLY; exact matching is on
the opposite end.

### 1.3 ACR 2021 I and II (constraints-c01, constraints-c02) - abstract depth

Codimension-10 null gluing near Minkowski; 10-dim obstruction space of
gauge-invariant charges conserved by the linearized null constraints; charges
identified with ADM E, P, L, center of mass; angular-sector localization; no
decay loss. Vacuum only. Finite regularity in II (see above). Theorem-level
hypotheses not read this run.

### 1.4 Equality-type local surjectivity (constraints-c05/-c06/-c07) - secondary attribution

Corvino-Huang (c04, sec. 1) attributes, and describes exactly: "work of
Fischer and Marsden shows that the constraint map is locally surjective if the
kernel of the formal L2 adjoint of the linearized constraint operator is
trivial, a condition which Moncrief proves is equivalent to the absence of
spacetime Killing vector fields" (closed-manifold case), with the
compact-with-boundary localized versions due to Corvino (scalar curvature,
CMP 2000) and Corvino-Schoen (full constraint map, JDG 2006), and a systematic
weighted-space treatment by Chrusciel-Delay (Memoir). C04's own derivation of
the DEC difficulty starts from the equality solve
Phi(g+h, pi+w) = Phi(g,pi) + (2psi, V), i.e. surjectivity with prescribed
compact target shift and compactly supported solution.

**This is the load-bearing statement for our lemma and it was NOT read at
primary level this run.** Its exact form (support of (h,w) vs support of the
shift; spaces; validity at NON-vacuum base data (g,pi)) must be verified in
Corvino-Schoen 2006 and/or Chrusciel-Delay before Lemma P is used.

### 1.5 Coupled matter existence (constraints-c10) and new flexibility leads

Choquet-Bruhat-Isenberg-Pollack (CQG 2007): Einstein-scalar constraints via
conformal method on COMPACT manifolds; some existence subclasses unresolved.
No localization, no exterior matching.

Mao-Oh-Tao (arXiv:2308.13031v1, 2023, abstract depth): unit-scale-annulus
gluing via explicit solution operators with prescribed support; strengthens
Czimek-Rodnianski obstruction-free gluing by purely spacelike methods.
Oh-Luk-Mao-Tao, "An h-principle for general relativistic initial data sets"
(UCLA seminar talk, Oct 2026; discovery only, no manuscript located): a
Nash-Kuiper-type flexibility result generalizing the obstruction-free gluing
theorems. Both are vacuum; both are watch items for M1.

## 2. Candidate deliverable: a sufficient lemma for changing the relational future while preserving the observer past

### 2.1 The lemma (slice form)

Work in a coupled Einstein-matter system E with a well-posed Cauchy problem
(local existence and uniqueness in a stated smooth class). Canonical example:
Einstein-massless (or massive, potential V) scalar field, sources
(mu_phi, J_phi) determined by scalar data (phi0, phi1); the same structure
holds for Einstein-Vlasov (f free) and Einstein-Maxwell with free divergence-free
(E,B). Let (M, g, fields) be a smooth solution, Sigma a smooth spacelike Cauchy
surface, b in J^+(Sigma), u the unit future velocity at b, and
y = gamma_{(b,u)}(T) the relational evaluation point (before caustics), with
the same normalization conventions as the coordinator's model
(M, g, fields, b, u).

**Hypotheses.**

(P1) *Whole-past footprint fixed.* Let Omega := Sigma ∩ J^-(b) (closed in
Sigma). Choose open O with Omega ⊂ O ⊂ Sigma. This is the clause that answers
the contract's trap: an arbitrary Cauchy patch does not suffice; the fixed set
must contain the ENTIRE slice-crossing of the causal past, with an open collar.

(P2) *Causal shadow placement.* A compact shell C ⊂ Sigma \ cl(O) with
positive separation from cl(O), and y in D^+(C): every past-inextendible causal
curve from y meets C. (In flat-like geometry: the observer's future geodesic
must head out over the annulus; the change must be planted in the target's
causal shadow but outside the observer's.)

(P3) *Constraint step.* New matter data equal to the old outside C and
differing by a small (delta phi0, delta phi1) in C_c^inf(C); the induced source
shift (delta mu, delta J) is small and supported in C; AND at the base data the
kernel of DPhi^*_{(gamma,K)} is trivial on a neighbourhood of C (no local KIDs;
genericity - see M1 for what fails without it).

(P4) *Evolution class.* Maximal developments of the two data sets exist and are
unique in the stated class (Choquet-Bruhat-Lichnerowicz for Einstein-scalar).

**Conclusion.**

(i) The two maximal developments agree on D(O), hence on the closure of
I^-(b) together with b: the observer's ENTIRE causal past - geometry, matter,
and all records - is preserved as the same solution, not merely isometric and
not merely on an initial patch.

(ii) The new development differs from the old in every neighbourhood of y,
provided the first variation of the evaluated observable at y is nonzero; for
the scalar evaluation phi|_y (or its 1-jet) there exist admissible
(delta phi0, delta phi1) with nonzero retarded first variation at every
y in D^+(C) (linearized change = retarded Green integral over
J^-(y) ∩ C, nonzero at timelike separation), and by continuous dependence of
the solution map all sufficiently small nonzero amplitudes give
phi_new(y) != phi_old(y). Charges and the asymptotic end are preserved EXACTLY
because C is interior and the data are untouched on cl(O)^c ∪ C^c.

**Proof sketch and epistemic status.**

(a) (i) is elementary and standard: Sigma Cauchy implies every
past-inextendible causal curve from b meets Sigma in Omega ⊂ O, so
J^-(b) ∪ {b} ⊂ D(O); agreement of initial data on the open set O propagates to
D(O) by uniqueness (P4). This is the same domain-of-dependence logic the gluing
literature uses (c03 sec. 1: "the spacetime pieces are determined by the domain
of dependence property"). Not novel; stated here because it is exactly the
clause the contract flags as the trap.

(b) (P3) is the composition "matter data are free + constraint map locally
surjective with prescribed compactly supported source shift at kernel-free
data". For Einstein-scalar: choose (phi0+delta phi0, phi1+delta phi1); the
sources shift by small compactly supported (delta mu, delta J); apply the
Corvino-Schoen / Chrusciel-Delay local surjectivity (sec. 1.4) to get (h,w)
supp ⊂ C with the coupled constraints satisfied ON Sigma. The existence
theory for the coupled evolution is classical. **The composition as a packaged
coupled-matter localized gluing does not appear in the sources found**
(searches at the stated depth); it should be treated as an explicit
CONSTRUCTION whose citation base needs primary verification (1.4), not as a
literature result.

(c) (ii) uses differentiability/continuous dependence of the solution map in
the chosen norms. The single-point clause is genericity, not an unconditional
claim: a deformation could accidentally fix the value at one point while
changing the jet or nearby values. Falsifier: exhibit a nonzero compactly
supported data perturbation on C whose maximal development coincides with the
old solution on a neighbourhood of every y in D^+(C) (this would contradict
(a)-type uniqueness applied backwards, or show a flaw in the retarded
non-vanishing), or a violation of (i).

**What this gives the shared target.** Mapping to the coordinator's hierarchy:
- Lane A (one lawful pair, same past, different future): Lemma P with (P3) in
  vacuum is immediate from existing results; with coupled matter it is
  CONDITIONAL on (1.4) verification. Elementary per the contract; do not
  inflate.
- Lane B (fixed matter theory, common Cauchy topology, maximal developments,
  full-past matching justified): this is exactly (P1)+(P4): the whole-past
  matching is justified by D(O)-agreement, not by a Cauchy patch. The
  constraint realization in the FIXED matter theory is the (P3) composition -
  the part not in the literature.
- Lane C (local control of future observables with charges fixed, exact
  hypotheses): interior-annulus version keeps ADM charges exactly; exact
  hypotheses are (P1)-(P4) plus the smallness norms of the underlying
  surjectivity theorem. Genericity (P3) is the honest restriction; M1 below is
  the named missing step for removing it.
- Lane D: not pursued (contract: only after A-C feasibility and priority audit).

**Matter-model scope of (P3).** Scalar (free data), Vlasov (free distribution
f), Maxwell with free divergence-free (E,B): the composition goes through
verbatim in structure. Null dust does NOT have the same free-data structure on
a spacelike slice in any form I verified - the coordinator's Vaidya baseline
should stay separate (as the contract already assigns).

## 3. Named missing steps / obstructions, with falsifiers

**M1 (genericity at degenerate base data; interior annuli).** The equality-type
constraint step needs trivial kernel of DPhi^* on the deformation shell.
At flat data the kernel is 10-dimensional (c04 Ex. 2.4; KID interpretation via
Moncrief at vacuum). Czimek-Rodnianski (c03) remove charge obstructions using
the nonlinearity, but only: near Minkowski, in the asymptotic region, gluing to
a chosen model family, and with charge-gap conditions (Delta-E = C1*eps > 0
strictly). Mao-Oh-Tao (c08) sharpen this; the h-principle work (c09) may
generalize further. **Missing lemma:** obstruction-free localized deformation
with an arbitrary prescribed small compactly supported source shift on a
compact INTERIOR annulus, at (possibly flat or Kerr-like) base data.
Sharp form: does the nonlinear constraint map at flat data on a compact
annulus surject onto ALL small compactly supported shifts, or only onto those
orthogonal to the 10 kernel elements? Falsifier (for our use): a small shift
supported in a flat annulus provably admitting no exact solution (would fix the
range and confine Lemma P to generic shells); conversely a published theorem
surjecting onto all shifts would delete hypothesis (P3)'s kernel clause.
Either answer is informative for Lane C.

**M2 (characteristic/null gluing with coupled matter).** All located
characteristic gluing results (c01, c02, c03) are VACUUM. No published
codimension-finite or obstruction-free null gluing for Einstein-scalar, or any
fixed coupled matter model, was found at our search depth. Null constraint
systems with matter transport couple differently (the scalar's transport along
the null hypersurface changes the charge transport equations used by the
gluing), so this is a genuine gap, not an oversight. Falsifier: any published
theorem gluing two Einstein-scalar (or Einstein-matter) null data sets with
matter matched at both ends and constraint satisfaction along the glued null
hypersurface. If none exists, Lane C's null-side control in a fixed matter
theory has no toolkit yet.

**M3 (KID correspondence at non-vacuum data).** The kernel-of-DPhi^* =
spacetime KIDs equivalence (Moncrief) is attributed at vacuum data. At
Einstein-scalar (or general coupled) data, the corresponding statement
(matter-carrying KIDs of the coupled linearized system) is not stated in the
sources read. This matters only for interpreting (P3) geometrically; the
kernel-free hypothesis itself is well-defined regardless. Falsifier: a coupled
solution with trivial kernel but a genuine coupled KID, or vice versa.

## 4. Assumptions vs the shared target (no novelty inflation)

- The shared question's extension demand ("decide explicitly whether matching
  extends to b and J^-(b); do not infer from an open-past isometry without
  hypotheses") is met by Lemma P (P1): the matching hypothesis is explicit
  (open O containing the full Sigma ∩ J^-(b)) and the extension is a
  consequence of (P4), not assumed.
- Everything in section 2.1(a) is standard; the lane claims no novelty for it.
- The candidate NEW content is narrow: (1) the packaged coupled-matter
  composition (P3) - whose absence from the literature is a search-depth
  negative, not a proven gap; (2) the explicit whole-past formulation
  connecting gluing theorems to the pointed-observer target; (3) the precise
  accounting of what obstruction-free gluing does and does not give
  (charge-gap conditions; perturbative; exact on one end only).
- Vacuum Lane A/B feasibility does not need our composition: exact-equality
  deformations exist (Corvino 2000; Corvino-Schoen 2006; CH Thm 1.4 without
  kernel assumptions in the asymptotic regime; C-R Cor 2.13 obstruction-free
  with charge gaps). The DEC lane (c04) is NOT usable for fixed matter
  (authors' own equality remark) - this is the strongest contrary evidence
  found against the cheapest coupled shortcut.
- "Initial Cauchy-patch preservation is not whole-past preservation": honored.
  Lemma P's fixed set is the whole causal footprint with a collar; if Sigma ∩
  J^-(b) is non-compact (observer past reaching an end), O is non-compact and
  the constraint step moves to the asymptotic regime, where charge
  preservation is no longer automatic (CH Thm 1.4 raises E by construction;
  C-R Cor 2.13 REQUIRES Delta-E = C1 > 0). Past preservation + exact charge
  preservation + far-out change are in tension; interior annuli keep charges
  exactly but need (P3)/M1. This trade-off should inform the coordinator's
  full-past quantifier design.

## 5. Access limits and required verifications

1. constraints-c05 (Corvino-Schoen 2006) and constraints-c07 (Chrusciel-Delay
   Memoir): not read at primary level this run. Verify: exact localized
   surjectivity statement; whether stated at non-vacuum (g,pi); support and
   space of the solution vs the shift. Lemma P's (P3) is conditional on this.
2. constraints-c01/-c02 (ACR I/II): abstract depth only; theorem-level
   hypotheses and function spaces unread.
3. Publication status of c01, c02, c03, c08: arXiv v1 pages carry no
   journal-ref as accessed 2026-10-28; statuses unverified.
4. c09 (h-principle): talk abstract only; no manuscript located; cite as lead
   only.
5. Absence claims (no coupled-matter localized gluing; no null gluing with
   matter) are search-depth negatives (queries in AGENT_REPORT.md), not proofs
   of absence. Chrusciel-Delay's Memoir is the likeliest place where part of
   (P3) may already be written down.
6. The web-search-prime MCP server was quota-exhausted; searches used the
   SerpApi fallback (see AGENT_REPORT.md).

## 6. Proposed next tasks

1. Verify (P3)'s citation base: read Corvino-Schoen 2006 local surjectivity
   proposition and Chrusciel-Delay Memoir mapping theorems at primary level;
   decide whether the coupled composition is already implicit there.
2. Attack M1's sharp form: either construct an obstructed compactly supported
   shift on a flat annulus (projected-surjectivity pairing argument), or locate
  / prove an interior obstruction-free deformation theorem.
3. M2 feasibility: derive the linearized null constraint system with a scalar
   transport and count conserved charges (is the obstruction space still
   10-dimensional, or enlarged by matter flux terms?).
4. Coordinator coupling: with (P1)-(P4) in hand, check whether the baseline
   Vaidya construction already realizes Lane A/B (it may), and reserve the
   coupled-scalar realization for the genuinely new step.
