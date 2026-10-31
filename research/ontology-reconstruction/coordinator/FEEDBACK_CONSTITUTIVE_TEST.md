# Does greater dynamical integration require a longer present?

30 October 2026. A constructive philosophical test using standard transport
and feedback mathematics. The bounded native
[algebra/conditioning review](../response-memory-review/REVIEW_FEEDBACK.md)
is integrated, with primary provenance inherited from the coordinator.
No new filter theorem, established unity criterion
or temporal ontology is claimed. Primary antecedent: Julius O. Smith III,
*Physical Audio Signal Processing*, author-hosted “Feedback Comb Filters”
section: delayed feedback produces decaying repeated echoes. The present
continuous-time calculation is elementary and stated in full below.

## 1. Make the feedback physically causal

Use an outgoing transport path of length L, speed c and transit time τ=L/c.
The return path has transit time σ>0. If the endpoints are spatially
separated by L, choose its length/speed so that σ is compatible with that
separation and the signal-speed bound. There is no instantaneous action
from a spatial average back to the input. Both paths are ordinary directed
transport channels, with an externally driven mixing junction at the inlet.

Let q(t,x) be the outgoing signal and z(t)=q(t,L) the point outlet signal.
For attenuation 0≤g<1 and externally prescribed injection f(t), impose

    q_t+c q_x=0,
    q(t,0)=f(t)+g z(t−σ).

The delayed term is the signal that has physically traversed the return
path; writing it as a delay eliminates that path's field state. The
junction is a driven linear model, not a closed energy-budget theorem.
The physical apparatus fixes the delays and gain. Varying g varies the
coupling arrangement, not complete data of one fixed boundary-value problem.

With ℓ=τ+σ, the characteristic equation at the outlet is

    z(t)=f(t−τ)+g z(t−ℓ).

For bounded histories its unique bounded solution is

    z(t)=Σ_{n≥0} g^n f(t−τ−nℓ).

The series converges uniformly and has norm at most ||f||_∞/(1−g).
For uniqueness, iterate the homogeneous difference equation N times:
|δz(t)|≤g^N||δz||_∞→0. Equivalently start both paths with zero signals at
a finite preparation time and set f=0 earlier. Only finitely many terms
can then contribute to any specified output time.

## 2. The extent changes at arbitrarily weak feedback

For the specified external-input/outlet protocol the impulse measure is

    h_g=Σ_{n≥0}g^n δ_{τ+nℓ}.

At g=0 its exact lookback endpoint is τ. At every g>0 its support is
unbounded. For a finite preparation time this means there is no fixed
apparatus cutoff valid uniformly as the experiment gets older: increasingly
old injections can still produce nonzero echoes. It does not require a
physically infinite past.

All coefficients are positive, so

    ||R_g−R_0||_{∞→∞}=g/(1−g).

This is the total-variation norm identity, attainable as a supremum with
compact smooth inputs of unrestricted duration. The support jump can
therefore coexist with arbitrarily small changes in every bounded-input
response. No mass term or modification of the transport PDE is needed;
the physical change is the return-path coupling.

To remove a mere static-gain difference, also compare calibrated outputs
\widetilde R_g=(1−g)R_g, all with unit constant-input gain. Their measures
are probability measures, and, since the initial echo and the later echoes
have disjoint supports,

    ||\widetilde R_g−R_0||=g+(1−g)Σ_{n≥1}g^n=2g.

The exact support is still unbounded for every positive g. Calibration is
an explicitly chosen measurement convention, not an ontological equivalence
or gauge symmetry. For cutoff T_n=τ+nℓ, n≥0, the calibrated remote tail
has mass g^(n+1). This gives an exact, tolerance-dependent truncation rule.
For two unknown histories of amplitude≤U the uncertainty bound has the
additional factor 2 described in RESPONSE_MEMORY_BENCHMARK.md.

## 3. Why this is a sharper constitutive test

An independently intelligible candidate organizing feature is now present:
outgoing transport changes the returning signal, which changes the next
injection. For g>0 this is an active causal feedback cycle; at g=0 the
outlet no longer contributes through that path. This feature can be stated
without mentioning which times should be concrete. It is a candidate
aspect of organization, not a claim that every feedback filter is a
genuine composite unity or that an attenuating loop is self-sustaining.

Consider the specific proposed selector:

    a system's present contains all external-input times that can affect
    its current coordinating response.

For this selector, activating even weak recursive coordination replaces
a finite lookback by one without an age-independent finite bound. A
fixed physical cycle time ℓ still exists, and bounded-source responses
remain close as g→0. The selector must therefore explain why that exact
support jump should be a jump in concrete extent. Greater dynamical
integration does not automatically imply a sharply bounded thick present.

The strongest response is to reject the selector: remote causal ancestry
need not be a constitutive part of current organization. One circulation
or the current carrier fields might constitute the loop even though older
inputs affect their values. That is a substantive constitutive proposal,
not a contradiction exposed by the response calculation. It is precisely
the proposal the next test should develop. A cycle time is not by itself
proof that one whole cycle, uniquely anchored in one way, is its present.

## 4. A further distinction inside the same physical apparatus

If the chosen input is the *total junction signal* j(t)=q(t,0), rather
than the external injection f(t), the outgoing relation is simply

    z(t)=j(t−τ).

It has finite lookback τ for every g. The f-to-z and j-to-z questions are
different physical conditionings on the same apparatus. Holding j fixed
while changing feedback may require compensating changes in f. This is
not a neutral relabeling of an intervention or an ontology.

It follows that response duration is invariant under internal realizations
with fixed access but need not be invariant under changes of the chosen
system boundary or input variables. A constitutive account must justify
that boundary independently. Calling all predictive states equivalent
does not settle it; nor does calling the external-input history necessary.

## 5. The positive research question

Can current material carriers plus a physically identified coordination
cycle supply a constitutive ground that is distinct from both full causal
ancestry and mere predictive data? Specify what would cease to be one
system if the cycle were interrupted, while separating loss of unity
from a changed output value or a disabled detector. Preserve the underlying
transport laws and state exactly which boundary interventions are allowed.

If that criterion works, test whether it gives a finite physical process
extent independent of gain calibration and state representation. Then
compare a process-based existential interpretation with an event realist
who accepts the very same carriers and cycle. The result sought is a
distinctive constitutive explanation, not a new name for a memory window.
No one of those bridge steps is asserted as completed here.
