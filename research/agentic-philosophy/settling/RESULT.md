# Trying the three routes that could settle something

11 November 2026. Claude Code (Fable 5.2), at the user's request. Checked only by the
session that wrote it. An attempt on §5 of the [essay](../ESSAY_2026-11-11.md), which
named three developments that could break the stalemate. Two propositions here are
elementary and proved. The rest is argument. No temporal ontology is selected.
Sources: [sources.jsonl](sources.jsonl). Check: [collapse_reversal.py](collapse_reversal.py).

## Verdict

| Route | Outcome |
|---|---|
| A fundamental law that is not time-symmetric | **Contested for collapse, and narrowed to an exact target.** On Bedingham and Maroney's argument collapse does not qualify; Tumulka is reported to say his model does break the symmetry (§5). A lawful arrow needs a class of worlds with no time-reversing symmetry of any kind. A lawful *present* needs less, and can exist under ordinary symmetric laws |
| An argument from experience, agency or value | **Reduces to the first route or fails.** A present that makes a physical difference is a physical field and falls under the first route. One that makes none cannot be evidenced by a subject |
| A theory without spacetime | **Makes it harder, not easier.** The symmetric relations survive without spacetime. The one oriented relation does not |

So the essay was wrong on one point and too coarse on another. Both are corrected
there.

## 1. Collapse gives no lawful arrow

The essay said a collapse dynamics that heats matter would give every world a clock by
law. That is wrong.

**Proposition 1.** Take a finite-dimensional system with a time-reversal invariant
Hamiltonian and collapse operators that are self-adjoint and time-reversal invariant,
as the Gaussian localisations of GRW are. Let the record be the sequence of collapse
outcomes. If the initial state is maximally mixed, every record has the same
probability as its reversal.

*Proof.* The probability of a record is Tr(A ρ₀ A†), where A is the ordered product of
collapse operators and unitary steps. The reversed record has operator A′ = Θ A† Θ⁻¹,
with Θ the time-reversal operator. For ρ₀ proportional to the identity the two
probabilities are Tr(A A†) and Tr(A† A), which are equal. ∎

More generally Tr(A ρ₀ A†) = Tr(ρ₀ A† A). So a forward process with a chosen initial
state is the same thing as the reversed process started from the mixed state and
post-selected on that state at the other end. The asymmetry is exactly the asymmetry
of the boundary condition.

The script confirms it on a three-level toy: from the mixed state the largest
difference between a record's probability and its reversal's is 10⁻¹⁷, and from a pure
state the two distributions differ by one to two bits. The entropy of the averaged
state is constant from the mixed start and rises from the pure one, which is the
"heating".

**This is Bedingham and Maroney's thesis** (arXiv:1502.06830, read in full). They
argue it by simulation for a lattice model and for a continuous model, treat the energy
increase the same way, and conclude that any observed asymmetry is due to "the
asymmetric imposition of initial or final time boundary conditions". Proposition 1 is
an exact finite-dimensional case of what they conjecture.

Violation of time-reversal symmetry in the weak interaction does not help either: the
combined reversal with charge and parity is still a symmetry, and the paper's mirror
argument goes through with it.

## 2. A present and an arrow need different things

The essay ran together a lawful present and a lawful arrow. They separate.

**Proposition 2.** Let a class of worlds be closed under reversing the time
orientation. A local clock that does not depend on the orientation is constant along
every timelike curve.

*Proof.* If x precedes y in a world, the clock is no greater at x than at y. In the
reversed world y precedes x, the germs are the same apart from orientation, and so the
clock is no greater at y than at x. ∎

So on a reversal-invariant class every useful clock is odd under reversal. Such a clock
exists under ordinary laws. In Friedmann cosmologies the expansion rate of matter never
increases toward the future, given the energy conditions: this is the Raychaudhuri
equation, and for flat or open models it is the familiar statement that the Hubble rate
falls. Reverse the orientation and the expansion changes sign, and the statement holds
again. Unlike the density, the expansion is monotone through the whole of the closed
dust model, maximum expansion included.

What an odd clock gives and does not give:

- **Simultaneity, lawfully.** Its level sets do not depend on the orientation. So a
  shared present "by rule" is available under time-symmetric laws, on classes where
  the clock is monotone along all timelike curves. Homogeneous cosmologies are such a
  class. Realistic ones are approximately so, with the blur the essay describes.
- **No direction.** The clock increases toward whichever direction is called the
  future. It reads back the orientation it is given.

**So a lawful arrow needs the class of admissible worlds to break every time-reversing
symmetry.** For local, Lorentz-invariant quantum field theories the CPT theorem
supplies such a symmetry. On that basis an arrow is either a boundary condition, or it
needs a failure of locality or of Lorentz invariance. That is a precise target, and it
is the same failure that a primitive preferred foliation would be. I have not checked
how the CPT theorem's reversal acts on the classes used in the project's theorems, so
this last step is an argument and not a result.

## 3. Experience, agency and value

Suppose a present, or a growth of what exists, that is not fixed by the physical
contents of the world. Either it makes a difference to some physical quantity or it
makes none.

- If it makes a difference, it is a physical field. It then belongs to the physics, it
  changes the class of admissible worlds, and whether it yields a present or an arrow is
  decided by the criteria above. This is the first route.
- If it makes none, two worlds differing only in it contain subjects in the same
  physical states, with the same memories, reports and reasons. Nothing in a subject's
  experience can then be evidence for it.

The second horn is, I believe, the known objection of Braddon-Mitchell and of Prosser.
I state it from memory and have not read either. What the project adds is the first
horn made exact: a present that does anything is a clock, and the conditions for
clocks are now known. The reading lanes on experience, agency and value should say
whether some argument escapes the dilemma. I do not see one.

## 4. Without spacetime

The fixing note's setting uses a set, a class of histories on it and subsets. No
causal or metric structure enters. So reciprocity and the balance of openness survive
in any theory that still has subsystems and correlations between them. "Has become"
does not survive, because it is defined from the causal order, and it is the only one
of the four relations with an orientation built in.

A timeless global state, as in the Wheeler–DeWitt and Page–Wootters approaches, is
stationary by construction. By the stationary result, no asymmetry of openness between
clock readings follows from such a state as such. It would have to come from a special
condition on the state, which is a boundary condition under another name.

So removing spacetime removes the oriented relation and keeps the symmetric ones. That
does not help a primitive. This section is the least secure: I have not read the
problem-of-time literature, and the reading lane on it is running.

## 5. What the reading lanes say against this

Added the same day, after six of ten reading lanes returned. They are worker
submissions; I spot-checked scope and two abstracts, not their sources.

- **Against §1.** The quantum lane reports that Tumulka's relativistic flash model
  (arXiv:quant-ph/0406094) lists time-reversal invariance as broken, and reads this as
  a lawful direction with no boundary condition. The abstract does not say it, and I
  have not read the body. If Tumulka says so, the literature holds two positions:
  the law as written is asymmetric (Tumulka), and the flash distribution it produces
  is symmetric apart from boundary conditions (Bedingham and Maroney). Proposition 1
  supports the second in finite dimensions only. So §1 is one side of a live
  dispute and not a closed question. The same lane names causal-set sequential
  growth as a second lawful direction, at abstract depth.
- **For §2.** Barbour, Koslowski and Mercati (2014, abstract depth in the lane) get
  an arrow from a time-symmetric law with no special initial condition: typical
  solutions have one past and two futures. That is an orientation-independent
  quantity that is not monotone, pointing away from a midpoint both ways. It is the
  pattern of Proposition 2, and of the closed dust model. The problem-of-time lane
  also records that scale-factor clocks fail to be monotone in recollapsing models,
  which is why §2 uses the expansion rate and not the size.
- **For §3.** The experience lane read Prosser (2013): no mental representation of
  objective tensed features is possible whether or not they exist, so experience is
  no evidence for passage. Lee (2017) accepts the conclusion and disputes the
  mechanism. So the second horn is in print as recalled. One attempted escape is
  listed, Bernáth and Inan's transcendental argument (2023, introduction read by the
  lane). The agency lane finds no account on which the asymmetry of openness forces
  a primitive; Ismael and Kutach place it in the deliberating agent.
- **Against §4's confidence.** The problem-of-time lane agrees that "has become"
  loses its domain without events. It adds two things I missed: Gryb and Thébault
  deny that the frozen equation should be imposed at all, and the thermal time
  hypothesis makes time depend on the state. Both would change §4.

## What is left that could settle anything

1. A fundamental law with no time-reversing symmetry at all, and with a quantity that
   is monotone along timelike curves. Tests of CPT and Lorentz invariance bear on it.
2. An argument from experience, agency or value that escapes the dilemma of §3.
3. Nothing else that I can see.

On present knowledge the stalemate is stable, and the reason is now specific: every
route to a primitive present or arrow runs through physics of a kind that current
theories exclude by symmetry.

## Limits

- Proposition 1 is finite-dimensional. GRW has no normalisable mixed state, and the
  statement there is Bedingham and Maroney's, not mine.
- Proposition 2 is about clocks in the sense of the local-clock note, with all its
  limits.
- The expansion clock is monotone along all timelike curves only in homogeneous
  models. In general it is monotone along the matter flow alone.
- The CPT step is unchecked. The dilemma in §3 is recalled, not read by me.
- §1 conflicts with a reported statement of Tumulka's that I have not read.
