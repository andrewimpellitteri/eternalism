# Classification and ontology repairs: second initial review

29 October 2026. Coordinator inspection, not acceptance or full integration.
The C¹,¹ axis reconstruction remains separately pending independent review.

## Submissions inspected

* Classification: `3abcacb3b87283c0786fa5f572e7f85ae27b8481`.
* Bridge repair: `55cf9619c6a10288912aebe0845e520ab9d72099`.
* Rival repair: `948945fae2e6c3dc708547f07519ee8a2baca311`.

All three entered review after fresh committed outputs and clean checkouts.
The equivalence repair completed during this review at `5bb8c3a` and also
entered review with a clean committed handback. Its inspection is recorded
in §4 below. All four runs are now submitted; none is accepted here.

The three supplied checking programs rerun successfully in approximately
0.03, 0.33 and 0.04 seconds respectively. These are finite checks of their
encodings. They do not verify domain membership that was not encoded, the
scope of a category-wide claim, or the philosophical bridge premises.

## 1. Classification: two scope errors, one repaired witness

### The persistence witness must be inside the open slab

CM2 uses `x=(0,13/10)` in `M=(0,1)×R`. That event is outside M. The script
checks causal inequalities but never checks the required `0<t_x<1`.

The conclusion survives with the following exact interior replacement:

    s=(1/2,0), c=(3/4,0), x=(1/20,13/10), w=(19/20,9/20).

All points belong to M, s<c, s and x are spacelike, and w is a strict
causal common future of s and x. Thus x belongs to D(s). A common slab
future `(t,m)` of c and x would require

    t≥3/4+|m|,       t≥1/20+|m−13/10|,       t<1.

The first and third inequalities imply `|m|<1/4`; the second then implies
`t>1/20+13/10−1/4=11/10>1`, a contradiction. Hence x is absent from D(c).
The replacement's domain and witness inequalities were independently
checked with exact Fraction arithmetic. This repairs a numerical witness,
not a new persistence theorem or priority claim.

### H=B on an ambient object does not establish restriction compatibility

The mathematical statement

    M future-directed  =>  H_M(b)=B_M(b)

is sound under the stated causal hypotheses. The inference

    M future-directed  =>  H_U(b)=U∩H_M(b) for every Loc subobject U

does not follow: U need not be future-directed, and the first equality
says nothing about H_U. The script's success for the particular past-unbounded
U of CM1 is not a theorem about every subobject. The proposed C_Mink category
explicitly includes *all* causally convex open globally hyperbolic
subspacetimes, not only future-directed ones.

Indeed the worker's own CM4 gives a counterexample with full Minkowski
ambient, without changing its coordinates. Let

    M0=R^(1+1),       M1=(0,1)×R,
    p=(9/10,8/5),     q=(9/10,−1/10),
    U=M1∩(I⁻_M0(p)∪I⁻_M0(q)),
    b=(1/2,0),        x=(1/2,3/2).

U is open and a past set relative to the slab, hence causally convex there.
The slab is causally convex in M0, so U is causally convex in M0 as well.
Its two cones overlap for small positive times (`t<1/20`), so it is connected.
For U-points a≤d, the ambient diamond is contained in the slab and in the
past set below d; hence it lies in U and is compact. U is globally hyperbolic.
Thus both inclusions U→M1→M0 are admissible morphisms.

The CM4 inequalities show x∉H_U(b), while its explicit witnesses

    r=(1/10,7/20),       w=(97/100,6/5)

show x∈H_M1(b). These are also valid M0 witnesses, so x∈H_M0(b).
All these points are interior slab points; b,x,r belong to U and w does
not. The CM4 analytic exclusion is inspectable: for r'=(t,y)≤b with
`¬(r'<x)`, one gets y<3/4. A common future of x below q is impossible by
the spatial separation 8/5 versus available time 2/5. Below p it must have
spatial coordinate m in `(27/20,35/20)`; the constraints r'≤b and t>0
give `s>m−1/2`, whereas being below p gives the incompatible upper bound
`s<9/10−|m−8/5|`. This is a universal analytic exclusion, not a grid result.

Consequently **H fails restriction compatibility in the stated full-Minkowski
category too**. The earlier blanket retraction of that possibility is not
justified. What survives positively is restriction compatibility on a
category in which *both* objects of every morphism are future-directed:
there H=B at both ends, and the order-defined B restricts.

Also distinguish the reasons for H=B. A slab with infinite conformal past
and finite future is generally not future-directed; earlier coordinator
arguments for H=B in that case use arbitrarily early witness standpoints,
not D=B. Do not list it as an instance of the future-directed lemma.

The value of CM4 is therefore retained and sharpened in scope. Its
philosophical implication is conditional: a historical-potential ontology
must defend ambient dependence if it wants this H rule. Restriction
compatibility is itself a substantive bridge premise, not a neutral
criterion that automatically defeats that ontology.

## 2. Bridge repair: retain the concession, correct the direction of fixing

The repaired distinction between nonentailment and circularity is useful.
A neutral physical reduct and additional existence predicate can be stated;
supervenience then makes a substantive, contestable uniqueness claim. The
E_all/E_past alternatives do not by themselves refute either rival's own
single-expansion model class.

However §6.2 misuses the internally reviewed closed-dust result
`F_m(b)=M`. The definition in horizons/main.tex, §“Guaranteed from an event”,
is: **agreement on the specified whole open past of b forces agreement at
x**, for every pair of solutions in the fixed class. Thus F_m(b)=M says
that those past data determine the field throughout M. It does not say
that all of M is needed to determine facts at b, nor that future events
ground present facts. The worker's proposed defeater reverses this arrow.

One can separately propose the bridge
“everything determined from b is concrete from b”; together with F_m(b)=M
it would imply E(b)=M. But that is a different philosophical premise from
“things which determine present facts are concrete”, and still needs an
independent defense. Neither bridge is a consequence of the field equation.

The positive causal-past route also still owes the null-boundary and
elsewhere exclusions their exact assumptions. Record access, nomological
fixation, causal grounding and concrete existence remain different notions.
The finite enumeration is a bounded consistency exercise, not the missing
argument from records to an inventory of concrete entities.

## 3. Rival repair: a genuine concession, with the philosophical work open

The worker withdraws the claim that translations cannot map derivations,
demotes its unsupported collapse criterion, distinguishes nonsignalling
dependence from controllable signalling, and no longer infers eternalism
from loss of one motivation for fragmentalism. Those corrections address
the initial findings in kind; full source/translation correspondence still
needs review before integration.

Its clearest philosophical conclusion is deliberately negative: opposite
grounding directions currently restate the disagreement, without a
demonstrated independent explanatory payoff. The proposed obstruction to a
grounding-faithful translation uses explicit extra premises, including
definitions-as-grounds and full basicness of standpoint reality. Finite
checks can expose their inconsistency under a stipulated translation; they
cannot establish those metaphysical premises or the significance of the
resulting difference.

This locates the next serious question: identify an independently motivated
explanandum for which a changing or standpoint-relative concrete inventory
does indispensable explanatory work, and show why the best rival cannot
replicate it. If no such case survives, report that limitation instead of
awarding either view a default victory.

## 4. Equivalence repair: main concessions retained, two new textual errors

The revised finite example now distinguishes individual definability from
uniform recovery, and the two-case null-cone argument no longer relies on
the false 1+1 exception. Those are the right repairs in kind. The general
source-quantified logical map still needs coordinator source review rather
than acceptance on the worker's assertion.

Two errors remain in RESULT §§2–3:

* **Quadratic-form sign mismatch.** The text defines `Q(w)=w0²−|w_space|²`,
  which is positive on nonzero timelike vectors. Its proof then uses the
  negative-signature inner product, expands Q with the opposite cross-term
  sign, and asserts Q<0 for timelike vectors. The lemma itself is true, but
  that proof must use one convention consistently. A direct repair is to
  define `q(w)=−w0²+|w_space|²=⟨w,w⟩` and retain the displayed negative
  timelike inequalities and inner-product expansion. Alternatively reverse
  the signs in the proof while retaining its original Q definition. The
  finite program uses the positive-timelike convention; passing that check
  does not validate the incompatible textual inequalities.
* **Wrong bow-tie row.** Section 3.2 labels `I⁻(b)∪I⁺(b)∪{b}` as the
  bow tie. In this project's stated comparison the bow tie is
  `B(b)=M\(J⁺(b)\{b})`, including spacelike elsewhere and excluding
  the strict causal future. The bounded-family condition still excludes
  it, but because of its spacelike members, not future-timelike members.
  Repair the row before using it in a charitable rival comparison.

These are concrete correspondence repairs, not refutations of the corrected
finite definability example or the conditional null-cone census.

## Status and next review

No submission accepted at this checkpoint. Preserve all raw branches and
worker checkouts. Carry the corrected domain witness, the two-object
restriction condition, and the direction of fixation into the revised
premise-by-rival matrix. Review the equivalence handback when complete.
The technical axis proof needs its own independent mathematical audit.
