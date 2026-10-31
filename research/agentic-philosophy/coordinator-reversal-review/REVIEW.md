# Coordinator review of Claude's reversal conclusions

31 October 2026. Reviewed the revised notes and their same-model red-team,
not just the initial headline. Claude withdrew that headline during this
inspection. Exact inspected file hashes are in `INSPECTED.json`. This is a
bounded argument and calculation audit, not acceptance of a temporal ontology.

**Verdict:** the withdrawal is warranted. Retain the conditional symmetry
lemma, channel identities and most criticisms of the GLM pilot. Narrow the
remaining claim against the pilot, reject the alleged forced choice in R4a,
and leave application priority open. The reviewer's own broad claims about
all realistic sustainers are not established.

## 1. What the symmetry argument actually proves

Let z=(m,b) specify the model and standpoint. Fix a transformation Θ on both
inputs and output sets, and a single-valued rule W satisfying

    W(Θz)=ΘW(z).

If Θz=z, substitution gives W(z)=ΘW(z). Hence E⊆W(z) also implies
ΘE⊆W(z). Both statements are correct. A nonempty result confined to the
slice at b can be symmetric; the obstruction concerns a strictly past-sided
extent containing a point outside that slice. Symmetry fixes neither its
width nor the entire process as its extension.

Closure of the solution class under Θ does not imply Θz=z for a particular
solution. Thus the original passage from reversal-symmetric laws to a
symmetric window was invalid. A neutral rule on an asymmetric model can
return an asymmetric set. Also, an equivariant probability law or set of
alternatives need not have a symmetric individual outcome. These are
different claims from the single-valued lemma.

The general symmetry-inheritance argument is already present in Norton's
[Curie's Truism](https://sites.pitt.edu/~jdnorton/papers/Curie_truism_final.pdf),
especially §2 and the opening of §3. This is not a new general theorem.
Whether this particular application has a published predecessor remains
unsettled; a small unsuccessful search cannot establish either novelty or
its absence. Norton's broader verdict on causal metaphysics is his argument,
not something this review independently proves.

## 2. A field-history symmetry is not yet a symmetry of the experiment

For the lossless channel, Θ(t,x)=(2b−t,L−x) preserves the transport equation.
A source F palindromic about b−τ/2 makes the resulting scalar field history
fixed by Θ. This verifies the stated field calculation.

But Θ exchanges the two ends. A model with a controllable inlet at x=0,
passive outlet at x=L and specified access to interventions contains more
than this field. Its role assignments have not been shown to be fixed.
Equality of scalar histories does not establish that premise. The corrected
notes' finding that the pilot's one-sided rule fails neutrality at a mirror
standpoint is therefore conditional on using the reduced, unlabelled model,
or on separately proving a symmetry of the full contract. The pilot cannot
be required to erase a physical drive assignment merely to satisfy this
test. Its occurrence-to-presence inference remains disputed either way.

Likewise “one-sided output requires a Θ-odd feature” is safe as shorthand
for the contrapositive of the lemma, with Θ, its domain, single-valuedness
and fixed standpoint specified. It is not a classification of every physical
arrow or every account of presence.

This also prevents misusing Roberts's time-reversal counterexample.
His [2012 preprint](https://jamesowenweatherall.com/SCPPRG/RobertsBryan2012Man_Curie.pdf),
§2, concerns preservation of **instantaneous states** during evolution;
the lemma here concerns a **whole model** and its assigned set. Time reversal
relates forward and backward evolution, rather than generally commuting
with evolution for a fixed positive duration. The counterexample does not
invalidate the displayed lemma. Castellani and Ismael's
[§4.2 reply](https://www.jenanni.com/papers/WhichCurie'sPrinciple.pdf)
disputes the relevant meaning of time-reversal symmetry; this is a genuine
interpretive disagreement, not a settled objection to the algebra above.

## 3. The channel identities and attenuation witness survive

For c,L>0, τ=L/c, q(t,x)=F(t−x/c), and g(t)=F(t−τ), substitution gives

    y(t) = τ⁻¹∫₀^τ F(t−u)du
         = τ⁻¹∫₀^τ g(t+s)ds
         = τ⁻¹∫_(x/c−τ)^(x/c) q(t+s,x)ds,  0≤x≤L.

These identities hold for locally integrable F. The inlet form uses earlier
values and the outlet form later values of the same complete solution.
Neither permits independently changing the future outlet while holding
its required earlier inlet fixed. The fixed-probe witness is correct;
changing probe or section changes the observation contract. It does not
remove the determinate transit time of the original fixed apparatus.
The moving-section formula in REVIEW needs |1−v/c| in its denominator,
v≠c, and endpoints inside the channel before it describes a full section.

The closed region of complete tokens crossing t=b is

    B = {(t,x): 0≤x≤L, b−τ≤t−x/c≤b}.

Its time projection is [b−τ,b+τ]. Its elapsed portion B∩{t≤b} is the
triangle with vertices (b−τ,0),(b,0),(b,L), with time projection [b−τ,b].
The projection is not the region. Boundary conventions for in-progress
tokens must be specified separately; this closure calculation settles no
ontological issue about endpoints.

The reviewer's damped example is analytically valid under its stated family.
For γ>0 and F(s)>0, a characteristic token labelled s has amplitude
F(s)e^(−γ(t−s)). On that token its amplitude is at least the amplitude at
the crossing time b exactly when t≤b. Under PT, Q(t,x)=q(2b−t,L−x)
solves the equation with γ′=−γ; token incidence and the amplitude comparison
are preserved. Thus this neutral rule selects elapsed portions on the
attenuating member and future portions on the amplifying member.

This is a statement about a family admitting both signs of γ, not reversal
invariance of the fixed positive-damping theory or a demonstrated microscopic
model of a cell. No grid is needed for this proof. More generally, a
time-reversal-even observable strictly monotone through b prevents a history
from being reflection-fixed there. That conditional fact does not prove
the reviewer's universal claim about every realistic self-maintaining system.

Claude's exact-rational checker was code-audited and run successfully. It
checks quartic inputs at finitely many points; the substitutions and chain
rule above carry the general claims. The reviewer reports further inline
grids whose code was not supplied; they are not adopted as reproduced evidence.

## 4. The pilot criticism holds, with one substantive exception

Claude correctly identifies the pilot's inclusion/exact-width mismatch,
the slide from present-for-S to concrete inventory, the delayed cessation
after switching off the source, and the unsupported transfer from Newtonian
Kepler interaction to propagating tokens. The repaired withdrawal of the
“P1 is empty” criticism is also warranted. Our earlier
[pilot review](../PILOT_REVIEW.md) independently records the main failures.

But the final PILOT_REVIEW still calls R4a a fair challenge requiring an
instantaneous-stage theorist to accept P2 or deflate genuine sustaining
unity. That forced choice is unproved. A rival may treat the process and
its diachronic constitution as real while denying that all its elapsed
phases are concretely present together from b. The pilot has not derived
a contradiction in that combination. Arguing that such a combination
misclassifies processes requires an independent defense of P2; it cannot
function as a conceded cost of rejecting P2. This remains the occurrence
worker's source-based question, not a result already won against that rival.

The Kepler example also supports the narrower claim that a periodic solution
alone does not select a unique operative window. It proves no universal
restriction to completion-structured activities. Neither review should
promote the pilot's limited countermodels into a theorem excluding every
system-relative exhaustiveness principle.

## Disposition

Retain a correspondence test: identify the entity, full physical contract,
transformation and disputed presence predicate before drawing a metaphysical
consequence. Withdraw the general width-without-side thesis. Keep the
pilot-specific mirror objection conditional and the occurrence-to-presence
premise open. None of these checks gives eternalism, presentism or a growing
block an automatic explanatory preference. A referee packet for a new
ontology argument is not warranted by this candidate.
