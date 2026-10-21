# Easy event recognition, coherent erasure, and calibration

Coordinator derivation, 21 October 2026. Application of known event-filter
methods; no novelty claimed. Awaiting independent mathematical review.

## 1. Primary construction and scope

Frauca and Sorkin, arXiv:1610.02087v1, Section 5.2, Eqs. (42)–(46), construct
an equal superposition of the k history records in an event and project the
ancillas onto it. Their detector probability is the endpoint-summed quantum
measure divided by k; the conditioned system state retains the selected
histories' interference. Section 6.2.1, Eqs. (55)–(61), supplies a Fourier
implementation within the event subspace. These sections were read in full.

Chakraborti–Sorkin–Sinha, arXiv:2407.15702v3, Introduction, Sections 2.2 and 6,
and Section 4's event/detector relation, report an adapted photonic filter with
efficiency 1/2 instead of the earlier 1/3 for their event. The experiment is not
a causal-set instrument and does not license a universal efficiency bound for
arbitrary history representations. Neither paper's experimental data were
independently audited here.

## 2. Explicit finite instrument

Choose an orthonormal record basis |w>, w in {0,1}^n, and prepare

 |psi_n>=(q|0>+p|1>)^tensor n, p=(1+i)/2, q=(1-i)/2.

It is normalized since |p|^2+|q|^2=1; coefficients a_w obey sum_w a_w=1.
Define the rank-one scalar history measure mu(E)=|sum_{w in E}a_w|^2.
This is a finite coherent-register toy model, not causal-set percolation or
an implementation of its growth dynamics.

For m=|E|>0 let |chi_E>=sum_{w in E}|w>/sqrt(m) and Q_E=|chi_E><chi_E|.
The binary instrument has Kraus operators Q_E and I-Q_E. They satisfy
Q_E^dag Q_E+(I-Q_E)^dag(I-Q_E)=I. Its success probability is

 P_E=<psi_n|Q_E|psi_n>=mu(E)/m.

This is the one-output-sector specialization of the known filter construction.
It erases distinctions within E coherently: Q_E|psi>=(sum_E a)/sqrt(m)|chi_E>.
Membership-only projection onto span{|w>:w in E}, by contrast, gives
sum_E |a_w|^2 and retains which-history distinctions. Discarding records is not
a substitute for this coherent projection.

## 3. A small recognizer for a large witness event

For even n write k=number of ones. The phase of a_w is
exp(i*pi*(2k-n)/4). It lies on one of four coordinate rays. Let E_n include
precisely the positive-real and positive-imaginary rays. Membership requires
only k modulo four and known n modulo eight. A two-bit counter updated by
controlled modular increments recognizes it in n updates, retaining the
history input. This establishes a small recognition circuit, not a small
implementation of |chi_E><chi_E|. The counter must be uncomputed before
interference can be assessed if it would retain which-ray information.

Direct binomial summation gives, with x=2^(n/2-1),

 |E_n|=2^(n-1)+2^(n/2-1),
 sum_E a=(x+1)/2+i*x/2,
 mu(E_n)=((x+1)^2+x^2)/4,
 P_E=mu(E_n)/|E_n| -> 1/4.

Thus the event measure diverges exponentially while the detector probability
stays bounded and approaches 1/4. At n=20, mu=525313/4, m=524800 and
P=525313/2099200. The event-membership probability is instead 1025/2048.
Exact rational checks and a separate word-enumeration path agree through n=8;
compressed binomial evaluation reaches n=40 without enumerating 2^40 histories.

This gives a constructive answer to the last turn's question in this toy
model: the divergence does not itself produce unstable detector probabilities.
The calibration depends on event size. It also does not force the selected
large-measure event to be rare: its success rate tends to a quarter.

## 4. Sharp bound for a specified measurement task

Fix an m-element event and demand one state-independent detector effect Q on
the **full orthogonal record space** such that, for every normalized input a,

 <a|Q|a>=eta |sum_{w in E}a_w|^2.

By equality of quadratic forms, Q=eta |u_E><u_E|, where u_E=sum_E |w>.
As an effect Q must lie between 0 and I; its only nonzero eigenvalue is eta m.
Therefore eta<=1/m, and the projector above attains equality.
Multiple Kraus operators cannot improve this bound for the same probability
identity, because they define a single positive effect Q.

This is an elementary all-input bound, not a general optimality theorem for
history filters. In a dynamical history experiment not every orthogonal
record-state superposition is preparable with the fixed system dynamics.
The photonic 1/2 versus 1/3 improvement is therefore not contradicted.
Its exact relation to that experiment's allowed input space is not derived here.

More generally let the allowed preparations be **all** normalized vectors in
a known linear subspace K, with orthogonal projector Pi. Equality on those
states requires Pi Q Pi=eta |Pi u_E><Pi u_E|. Hence, when Pi u_E is nonzero,

 eta <= 1/||Pi u_E||^2.

The bound is attainable as an abstract effect by zero extension outside K.
If Pi u_E=0 the target response vanishes identically and eta is unidentifiable.
A non-linear preparation family cannot be replaced by its span without
justifying access to all superpositions in that span. If K is only one known
state, choosing eta to make the output certain is tautological and supplies
no independent measurement of an unknown measure.

## 5. What survives of the earlier resource argument

A *common* efficiency eta_n valid for every event at level n still satisfies
eta_n<=1/B_n^2, where B_n=max_E |a_n(E)|. That inequality is valid but makes a
much stronger calibration demand than the event-specific projector above.
For example, the Omega filter here has efficiency 2^(-n), whereas E_n has
1/|E_n|. Raw E_n counts do not need exponentially many independent trials to
estimate P_E to fixed relative precision. Recovering mu with fixed *absolute*
precision by rescaling those counts is a different estimation task.

For the estimator mu_hat=m*(successes/N), its exact variance is
m^2 P_E(1-P_E)/N. At fixed absolute RMSE delta, this particular estimator needs
N>=m^2 P_E(1-P_E)/delta^2. Relative RMSE instead needs
N>=(1-P_E)/(P_E delta_rel^2), which approaches 3/delta_rel^2.
Neither formula is a quantum-query lower bound. Collective or coherent
estimation, classical evaluation of a known formula, circuit synthesis and
calibration uncertainty are additional questions.

## Verdict and actual frontier

The generic filter and its 1/m probability factor are published. This toy
application clarifies why unbounded event amplitudes alone do not establish
unstable experimentally observed probabilities. Efficient event recognition
also does not establish efficient coherent measurement.

The sharper open research contract must fix: (i) a dynamically accessible
preparation family, (ii) event-dependent versus common calibration,
(iii) covariance and locality of access, (iv) absolute or relative estimation
error, and (v) the cost model for coherent erasure. Only after those choices
could the scalar non-extension obstruction yield a physical resource statement.
No global priority claim, general hardware lower bound, or temporal-ontology
conclusion is made. Full source-paper reconstruction outside the cited sections
and independent proof review remain unfinished.
