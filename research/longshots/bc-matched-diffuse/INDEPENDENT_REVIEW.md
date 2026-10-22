# Independent adversarial review: diffuse matched-cylinder construction

22 October 2026. Scope: audit of `CLAIM_CONTRACT.md`, `RESULT.md`,
`PRIOR_WORK.md`, and the preceding matched-norms records. I reviewed the
analytic proof and ran the bounded finite checker with bytecode generation
disabled. I did not repeat the constructive search or re-audit the primary
sources in this pass; I checked their stated role and type assumptions against
the construction.

## Verdict

The completed `RESULT.md` proof survives the adversarial checks in scope. The
seed cancellation, all-stage Mobius bound, q-phase term in the row estimate,
L1(P0) extension, atomlessness, and minimum-only E2 increment are correct as
written. All displayed constants are sufficient; I found no substantive
mathematical defect. The statement is a scalar norm-only construction with
variation absolutely continuous with respect to the specified atomless
reference. The finite checker agrees with the analytic proof but remains
bounded evidence rather than an all-stage proof.

## Exact seed cancellation and norm matching

Write v_A=u, v_B=conjugate(u), where u=(3+4i)/5. At size two,

    w_A(chain)-w_B(chain) = 4/u - 4/conjugate(u) = -32i/5,

while the antichain and singleton weights agree. For an n-element C, the only
unequal proper-ideal weights are therefore the two-element chain ideals. If
c(C) counts those actual subsets, then

    sum_(P proper ideal C) (w_A(P)-w_B(P)) = (-32i/5)c(C).

The proposed h_C=-16c(C)/5 gives f_A(C)-f_B(C)=2i h_C=(-32i/5)c(C).
Subtracting the proper-ideal sums in the recursion proves
 w_A(C)=w_B(C) exactly for every n>=3. The multiplicity must be by actual
subsets, as specified; counting only ideal isomorphism types would break this
identity.

The bound c(C)<=n is valid: each two-element chain ideal has a unique upper
element y whose strict past is exactly its single lower element. Distinct such
ideals have distinct upper elements, so they inject into C. Thus |h_C|<=16n/5.
Since R_n=1000^n, |h_C|<R_n for n>=3, x_C is strictly positive, and
|f_A(C)|=|f_B(C)|=R_n. The q values are nonzero and have common magnitude
R_n^-1. Together with exact equality of later w values and matched seed
magnitudes, the path-product formula gives matched individual-cylinder
magnitudes at every depth. The construction is isomorphism invariant if the
induction explicitly notes that c(C) and the actual-ideal sum are invariant
under causet isomorphism.

The cancellation does not itself imply later w is nonzero. Nonvanishing is
separately supplied by the proposed comparison to positive w0 and a strict
bound |w-w0|<w0.

## Reference comparison and row bounds

The real reference has f0(C)=L^n and w0(C)=L^n(1-1/L)^m, m=|Max(C)|. Since
m<=n, w0(C)>=(L-1)^n=999^n. For n>=3 this exceeds

    H_n=L^2 n^2 + 4n 2^n.

The inequality holds at n=3, and each of 999^n/(L^2n^2) and
999^n/(4n2^n) increases thereafter; hence the sum of the two H_n terms is
also below 999^n at every n>=3.

For late parents, b(f(C)-f0(C))=|L^n-x_C|+|h_C|<=4n follows from the
explicit estimate:

    L^n-x_C = h_C^2/(L^n+x_C) <= (256/25)n^2/L^n,

and this plus 16n/5 is less than 4n for n>=3. For seed sizes, f(empty)=f0(empty);
at size one the discrepancy is L-2; at size two it is at most L^2+4 per
actual ideal. In the ideal-lattice Mobius inversion of
f(C)=sum_(P ideal C)w(P), the Mobius coefficient vanishes unless the
complement of P in C is an antichain. Bounding the surviving early terms by the number of one- and
two-element subsets, and the late terms by at most 2^n terms each of size
4n, gives the advertised H_n with room to spare. RESULT.md shows this
inversion and the early-term count; a recurrence bound that counts all
nested ideal chains instead would not justify H_n.

Given |w(P)-w0(P)|<=H_n for every induced P of size at most n, the row
distance for a size-n parent follows from

    sum_P |q(C)w(P)-L^-n w0(P)|
      <= L^-n sum_P |w(P)-w0(P)|
         + |q(C)-L^-n| sum_P w0(P).

There are at most 2^n ideals and sum over all ideals w0(P)=L^n. Also
|q(C)-L^-n|=|f(C)-L^n|/L^(2n)<=4n/L^(2n). These give

    zeta_n = L^2 n^2(2/L)^n + 4n(4/L)^n + 4n/L^n,

as stated. The three positive series sum to less than 0.073, hence less than
1/8. For the first series, its n=3 term is 0.072 and successive-term ratio
is at most 16/4500; the other two start below 7.68e-7 and 1.2e-8 and have
ratios at most 2/375 and 1/750 respectively. This is a simple exact-rational
geometric bound, not a numerical-tail extrapolation.

The nonzero conclusion then follows: |w(C)-w0(C)|<=H_n<999^n<=w0(C), so
w(C) cannot vanish. The factorization also gives all q nonzero. MSR holds by
the defining recursion, and scalar ratio BC follows algebraically from
t(C,P)=q(C)w(P), as in the predecessor example.

## Completion and E2 audit

Let P0 be the real transitive-percolation path measure with transitions
p0(C,P)=L^-n w0(P). Every transition is positive. For n>=1, a proper-ideal
transition is at most 1/L; the timid transition is
(1-1/L)^|Max(C)|<=1-1/L. Therefore every depth-N cylinder has probability
at most (1-1/L)^(N-1), which tends to zero. This proves no point atoms. Since
the labelled-history space is standard Borel, P0 is atomless as a measure,
not merely point-atom-free: any positive-measure atom must lie, modulo null
sets, in one cell of each nested finite cylinder partition; these cells
specify one history, contradicting the zero point-mass bound. Absence of point
masses alone would not settle atomlessness on an arbitrary measurable space.

At depth n let g_n be the complex density of the finite cylinder amplitude
measure relative to P0, constant on depth-n cylinders. The row estimate gives

    ||g_(n+1)-g_n||_L1(P0) <= V_n zeta_n,
    V_(n+1) <= V_n(1+zeta_n).

Using V_3<=2 and sum zeta_n<1/8 gives V_n<=2 exp(1/8)<16/7. Hence the L1
increments are summable and g_n converges in L1(P0) to a density g. For each
fixed cylinder, later finite-level densities integrate to its prescribed
amplitude by MSR; L1 convergence preserves that cylinder value. Thus
nu=g P0 is the desired finite complex-measure extension, and
|nu|=|g|P0 is atomless. RESULT.md states the density construction explicitly;
a row bound alone would not suffice as a measure-extension argument. The
proof establishes |nu| absolutely continuous with respect to P0; it does not
claim equivalence nu~P0 or a positive lower bound on |g|, and no such stronger
claim is needed for atomlessness.

For E2, write F_n={M_n=2}. Since M_n is nondecreasing,
1_Fn converges pointwise to 1_E2, where E2 means the completed history has
exactly two minima. At one birth, only an empty precursor changes the minimum
count. Summing the MSR rows over each parent gives the exact increment

    a_(j,n+1)-a_(j,n)
      = sum_(|C|=n) A_j(C)q_j(C)(1_(M(C)=1)-1_(M(C)=2)).

For parents already in the event, nonempty children retain the parent minima
count and MSR makes their sum the parent amplitude minus the gregarious
branch; for one-minimum parents the gregarious branch enters the event. Thus
the increment's absolute value is at most

    sum_(|C|=n) |A(C)| |q(C)w(empty)| = V_n/R_n.

Finite variation then identifies the limit of nu(F_n) with nu(E2), either by
dominated convergence against |nu| or continuity of the symmetric
differences. Consequently each completed E2 amplitude differs from its
stage-three value by at most

    eta = (16/7) sum_(n>=3) 1000^-n
        = 16/(7*1000^2*999) < 10^-8.

With a_A=1/2 and a_B=1/2-i/5, the gap is at least
1/25-(11/5)eta-2eta^2 > 399999/10000000. The sign and constants are
consistent. This bound uses the fact that only gregarious births change
minima; bounding by all non-timid row mass would be a different and much
weaker estimate.

## Remaining gates and limits

The analytic proof supplies the former proof obligations: it derives H_n by
Möbius inversion over subsets of Max(C), includes the q-phase contribution in
the row comparison, constructs Cauchy densities in L1(P0), preserves cylinder
values by MSR, and identifies the pointwise F_n limit with E2. A finite
checker can still provide useful bounded verification of early exact
cancellation, the actual chain-ideal count, interval radicands, and rational
inequalities, but cannot replace these all-stage arguments.

The new R_n changes cylinder magnitudes relative to the older atomic example,
as required by the variation-data theorem. This is a scalar norm-only model
with an engineered absolutely continuous completion relative to P0. It does
not establish detector probabilities, full decoherence-functional
covariance, physical realism, or a temporal-ontology consequence. Prior-work
comparison is appropriately cautious; this review finds no priority basis in
the contract, and the primary-source comparison was not independently
reopened here.

## Bounded checker and added path-atom check

I ran `PYTHONDONTWRITEBYTECODE=1 python3 research/longshots/bc-matched-diffuse/check.py`.
It passed. It checked direct labelled counts through five births, formal
recursive-versus-Mobius weight agreement and exact common later weights,
interval nonzero/norm/MSR/BC/row-distance checks through the stated finite
cutoffs, and the E2 flow and enclosures. It reported 407 nonzero transitions
and 1619 BC pair residual enclosures per model, the exact rational
Z=7715823102531768444113/106782186928294326375000, and completed gap
enclosure [0.039999999879874507, 0.039999999879885491]. These checks agree
with the analytic proof; they do not establish the all-stage identities,
completion, or atomlessness independently. The checker reads the predecessor
interval helper and reports its SHA256; no predecessor file was edited.

I also checked the added uniform path-modulus estimate. Direct substitution
gives zeta_4=0.000256004112, which is below 1/(2L)=0.0005. For n>=4 the three
positive terms in zeta_n each decrease: their successive ratios are at most
0.003125, 0.005, and 0.00125. Each actual transition then obeys
|t_j(C,P)|<=t0(C,P)+zeta_n<=999/1000+zeta_n<1999/2000. Along any fixed path,
the amplitude is consequently bounded by a finite prefix factor times a
geometrically decaying tail. Continuity from above for the finite complex
measure gives zero mass to each singleton history. This independently
confirms absence of point atoms. The stronger atomlessness conclusion still
uses the standard Borel path-space argument and |nu_j|<<P0; point-atom
absence alone would not imply atomlessness on an arbitrary measurable space.

## Source and originality boundary

The mathematical types and assumptions are clear in the proof: scalar complex
weights and transitions on naturally labelled finite-poset cylinders; a
closed, hence standard Borel, infinite-history space; finite complex
extensions with their total-variation measures; and a strictly positive real
transitive-percolation reference P0. The conclusion is |nu_j|<<P0, not
nu_j equivalent to P0. E2 is measurable on labelled histories and invariant
under completed order isomorphism. No claim is made about the unlabelled
quotient, operator-valued QBC, detector probabilities, or physical ontology.

`PRIOR_WORK.md` records exact primary versions and full-text locators for
Rideout–Sorkin gr-qc/9904062v3, Srivastava–Surya 2603.25503v1, and
Surya–Zalel 2003.11311v1, with limits on what was audited. Their stated roles
are consistent with the mathematical dependencies here: real transitive
percolation and factorization are established machinery; norm-only phase
freedom is expressly anticipated; and finite-variation extension methods
predate this example. I did not independently reopen those papers or conduct
another novelty search. Thus this review supports the construction's
mathematical validity within its stated scalar class, not originality or
priority. The exact matched-cylinder plus atomless-completion example may be
a distinct application, but any novelty claim remains unestablished pending
the coordinator's targeted predecessor comparison.
