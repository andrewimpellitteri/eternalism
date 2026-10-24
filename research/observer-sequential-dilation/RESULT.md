# Transition-by-transition preparation and readout with bounded heralding loss

24 October 2026. An engineered finite history-register completion, using
standard controlled rotations and reversible dilations. Not an internal
causal-set observer, hardware implementation, novelty or ontology claim.
[Contract](CLAIM_CONTRACT.md) records predecessors and kill conditions.

## 1. The fixed target and the deterministic obstruction

For each finite labelled history C of size n let a_j(C) be its scalar
amplitude. Transitions t_j(C,P) append one maximal birth with past ideal P;
write CP for that child. Deleting the last birth recovers a unique parent.
For the matched pair all corresponding |a_j(C)| and |t_j(C,P)| agree.
Use common values

    V_n=sum_C |a_j(C)|,
    s(C)=sum_P |t_j(C,P)|,
    psi_(j,n)(C)=sqrt(|a_j(C)|/V_n) phase(a_j(C)),
    phi_n(C)=sqrt(|a_j(C)|/V_n).

The scalar row sum is one, so s(C)>=1. The target next-state weight of the
children of C is |a(C)|s(C)/V_(n+1), while its current weight is |a(C)|/V_n.
A prefix-preserving deterministic isometry maps each parent into a unit vector
in its own child sector and preserves these sector probabilities. Therefore
it can produce the target on an occupied parent only if

    s(C)=V_(n+1)/V_n.

Nonconstant s(C) on occupied parents obstructs this restricted deterministic
preparation. Conversely if the row variations are constant on the support,
normalized phase-weighted branching supplies the target. This is not a no-go
for arbitrary unitaries that mix parent sectors or change the representation.

## 2. A heralded step from finite transition data

The accepted construction supplies a uniform analytic row bound, for n>=3,

    1<=s(C)<=B_n=1+zeta_n,
    sum_(n>=3) zeta_n=Z<1/8.

Define the rectangular success Kraus map

    K_(j,n)|C> = sum_P sqrt(|t_j(C,P)|/B_n)
                       phase(t_j(C,P)) |CP>.

Disjoint child supports give K* K=diag(s(C)/B_n)<=I. The failure map

    F_n|C>=sqrt(1-s(C)/B_n)|C>

into a flagged copy of the parent register makes (K,F) an isometry. It has a
finite unitary extension with blank ancillas. A constructive implementation
first rotates a success flag with amplitude sqrt(s(C)/B_n), then on success
prepares the normalized child vector with coefficients
sqrt(|t|/s(C)) phase(t). Computing s(C) means summing over finite actual
precursor subsets, including multiplicities. There is no claim that this
computation or its controlled rotation is efficient or spatially local.

K_(j,n) psi_(j,n) = sqrt(p_n) psi_(j,n+1), where

    p_n=V_(n+1)/(B_n V_n).

A common positive map K_(+,n), dropping transition phases but retaining their
moduli, evolves phi_n with the same success probability. It is the SAME
positive preparation/readout apparatus for A and B. Only the phase-bearing
forward preparation differs. Do not replace K by raw t: the Born register
encoding uses sqrt modulus times phase and reproduces the scalar process
only through the specified later readout.

## 3. Accumulated success is bounded away from zero

Prepare the fixed seven-history seed psi_(j,3) by a finite unitary, and phi_3
by a common finite unitary as specified in the predecessor circuit note.
Let

    b_N=product_(n=3..N-1) B_n,
    r_N=product_(n=3..N-1) p_n=V_N/(V_3 b_N).

The probability of all forward preparation flags succeeding is r_N.
Since V_N>=V_3 and b_N<=exp(Z),

    1>=r_N>=exp(-Z)>7/8                         (N>=3).

In fact the forward survival lower bound holds for every normalized register
input: scalar MSR gives s(C)>=1, hence K* K>=I/B_n. Composing the
steps gives all-forward-success probability at least 1/b_N>7/8. The exact
r_N formula and terminal target identity use the particular preparations
above. The readout can have zero probability on other inputs; its >1/3
baseline bound is specific to the prescribed phase states.

This includes failed trials rather than silently renormalizing each step.
The depth-three seed is a fixed preparation resource, not an asymptotically
free arbitrary final-state oracle. No amplitude amplification is used.
Uniform success is not uniform runtime: the number of growth steps, register
size, arithmetic and precision costs still increase with N.

## 4. Readout using the reverse positive preparation

Let M_(+,N)=K_(+,N-1)...K_(+,3), so

    M_(+,N) phi_3 = sqrt(r_N) phi_N.

Retain coherent access to a finite unitary dilation of this preparation.
Running its adjoint with blank flags and accepting the original seed state
and all success/blank flags implements the history-space effect

    r_N |phi_N><phi_N|.

The adjoint success branch is NOT an unscaled projector onto phi_N. The
original seed test can be implemented by reversing its fixed preparation.
Dilation flags or work registers must be coherently uncomputed or tested;
classical sampling access does not supply the inverse circuit. If forward
heralds were measured, on the all-success branch they are known fixed values
and can be reset; their success probability is still charged in r_N.

If a binary event a in {E,E^c} is measured before this reverse readout,
conditional on successful preparation the joint event/readout probability is

    r_N |sum_(C in a) a_j(C)|^2/V_N^2.

Including forward preparation success, the unconditional probability per
seed trial is

    P_j(prep yes, a, read yes) = eta_N mu_(j,N)(a),
    eta_N=r_N^2/V_N^2=1/(V_3^2 b_N^2).           (1)

Thus both forward AND reverse losses have been counted. Ignoring either
would inflate the claimed detector rate. There is no terminal arbitrary
state-preparation oracle; readout reuses inverse access to the common
transition-controlled dilation, an explicit extra physical resource.

A complete output law is

    P(prep no) = 1-r_N,
    P_j(prep yes,a,read yes) = eta_N mu_(j,N)(a),
    P_j(prep yes,a,read no)
       =r_N sum_(C in a)|a_j(C)|/V_N - eta_N mu_(j,N)(a).

All terms are nonnegative and sum to one: the read effect is r_N times a
projector, bounded by identity. If the event test is omitted, scalar MSR
gives mu(X)=1, so the full baseline success is eta_N. If the event test is
performed, total read success changes with the event partition. Conditioning
on read success gives mu(E)/(mu(E)+mu(Ec)), as in the predecessor; it is not
mu(E). Forward-preparation flags have model-independent probabilities here.

## 5. A uniform rate and a formal limiting distinction

The exact seed has

    V_3=(25+sqrt(265)+2sqrt(65))/40 <3/2.

Since b_N^2<=exp(2Z)<exp(1/4)<4/3,

    eta_N>1/3                                      (all finite N>=3).

The last exponential comparison follows termwise from the geometric series.
This is a lower bound on the BASELINE full success probability for this ideal
finite protocol, not a universal efficiency bound for observers or all events.
The read-success probability for an inserted event test has its own law above.

For F_N={M_N=2}, the previous gregarious-birth tail bound implies the finite
amplitudes stay within tau=16/[7 L^2(L-1)] of their depth-three centers for
all N>=3, and converge to the completed E2 amplitudes. Consequently the same
previously proved conservative gap applies at every such finite N and in the
limit:

    mu_(B,N)(F_N)-mu_(A,N)(F_N)>399999/10000000.

The unconditional (prep yes,F_N,read yes) output gap is therefore

    >399999/30000000.

A certified finite-product/tail calculation bounds the formal limiting
baseline eta_infinity between 0.422311087189961757 and
0.422311764857235859. It uses b_5<=b_infinity<=b_5/(1-T_5), where
T_5=sum_(n>=5)zeta_n<1; the upper comparison follows from
product(1+zeta)<=exp(T_5)<=1/(1-T_5). This is a probability
bound in the ideal model, not a timing, cost or hardware estimate.

The products b_N converge and V_N increases to finite V, so the displayed
finite protocol probabilities have limits. This does not implement a circuit
of infinitely many gates, decide E2 exactly in finite time, or bound the
physical resources needed for a completed-history projector. F_N is a finite
prefix event, not a completed-relabeling-invariant event. No new completed
cosmological symmetry action has been supplied.

## 6. What bottleneck moved

The earlier global terminal-state oracle is replaced by transition-controlled
preparation and its inverse. Summable row excess suffices to keep heralding
losses finite in this encoding. The remaining physical resource is reversible
coherent access to a labelled history register and its precursor-controlled
couplings, including the readout inverse. These operations are not derived as
local matter dynamics on a causal set. A cheap herald probability does not
make the operation cheap, local, covariant, or physically available.

The finite register has different unconditioned decoherence data from the
original rank-one scalar history process. Equation (1) reconstructs its
specified finite event values through a changed measurement. The construction
neither proves scalar phase freedom is empirically observable nor rules it out.
The [locality audit](LOCALITY_AUDIT.md) and independent review preserve this
boundary. No temporal ontology, objective passage, or priority conclusion follows.
