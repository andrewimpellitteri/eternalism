# External review: temporal-ontology working draft

Received 2026-10-21. Reviewer read selected primary sources, not the entire
bibliography, and did not see the companion audit or calculation files. This is
a structured transcription of the reviewer report; the claims and examples are
preserved, wording is condensed.

## Verdict

**The central methodological claim survives. The paper, as an original research
contribution, largely does not.**

The main weakness is not spectacular nonsense. It is that the draft repeatedly
retreats from substantive claims until what remains is: state your assumptions,
distinguish different conclusions, and do not overgeneralise. Sensible — but the
manuscript has not demonstrated what its framework discovers that careful
argument reconstruction would otherwise miss.

There is also a concrete missing-premise problem in the Stein discussion.

## 1. The attempted repair of Stein’s theorem is insufficient

**Location:** §4, p. 5.

The draft says that adding the contextual non-universality condition to the
displayed hypotheses recovers the causal-past characterization. That does not
follow.

Consider

```
R(p,q)  iff  q = p or q in I^-(p),
```

where `I^-(p)` is the strict chronological past (past-directed timelike, not
null, separation). This relation is reflexive, transitive, invariant under
time-orientation-preserving automorphisms, instantiated by a past-pointing
related pair, and non-universal at every point. Yet it is not the causal-past
relation: it excludes distinct past-null-related events.

Stein’s prose supplies another assumption: every event in the causal past is
already definite. That stronger *causal-past inclusion* premise, not merely
non-universality, matters to recovering the conclusion.

Required repair: explicitly distinguish the displayed theorem,
non-universality, causal-past inclusion, and chronological-past inclusion.
This is especially damaging in a paper about making indispensable premises
explicit: the reconstruction omits an indispensable premise while presenting
itself as correcting a premise omission. This is a local problem in the
reconstruction, not grounds for declaring Stein’s entire argument defective.

## 2. The central thesis faces a weak–strong dilemma

**Locations:** §§1–3.

**Weak reading:** arguments should identify their assumptions and not claim
more than those assumptions establish. Correct, but what specifically has been
contributed to philosophy of time? Naming the assumptions `(P,O,B,A,S,E)` is
not itself an analytical result.

**Strong reading:** before physics can favor a temporal ontology, proponents
must specify an admissible physical realization, dynamics, probabilities,
operational interface, bridge principles, and comparison class. This is
controversial. Why should an explanatory or structural argument require the
same specification as an experimental likelihood comparison? An argument might
establish a serious structural cost without supplying a full physical
realization of every competitor.

The missing argument is not that explicitness is good. It is why this amount
and kind of explicitness is necessary for each kind of conclusion. A stronger
paper would distinguish what must be specified for a contradiction argument,
a likelihood comparison, an explanatory preference, and what can legitimately
remain open.

## 3. The paper asks about “favoring” but devotes its machinery to “excluding”

**Locations:** title, §§3–4, §7.

These are different questions:

1. Does relativity eliminate every admissible presentist realization?
2. Does relativity make eternalism more credible than presentism?

Failure to establish (1) does not substantially answer (2). Illustration:
`O_1` has one specified realization with `p(D)=1`; `O_2` has ten realizations
with equal prior weights, one with `p(D)=1` and nine with `p(D)=0`. Then
`p(D|O_1)=1`, `p(D|O_2)=0.1`, a Bayes factor of ten, although `O_2` retains a
perfectly compatible realization. Compatibility survives; evidential parity
does not.

The draft acknowledges this in §3.2, so this is a criticism of argumentative
emphasis, not a mathematical correction. The paper needs an actual account of
defeasible favoring, not mainly a catalogue of why decisive exclusion has not
occurred. A prior can reflect earlier physical evidence and explanatory
achievements; it need not be physics-free.

## 4. “Admissibility” contains almost the entire philosophical dispute

**Location:** §2.2, p. 3.

The conditions require fidelity to constitutive commitments, independent
motivation for added structure, consistent standards, and sensitivity to
alternative profiles. But the difficult disputes are exactly: which
commitments are constitutive; when a revision ceases to be presentism; what
makes a foliation independently motivated; how much explanatory work primitive
passage must do; when an alternative is reasonable rather than merely
imaginable.

The checklist relocates these questions rather than answering them. That is
not worthless, but organizing disputed judgments is not yet constraining them.

There is also an unresolved eligibility/discrimination problem. Background
evidence `D_0` establishes eligibility; discriminating evidence `D_1` compares
survivors. Filtering out unsuccessful realizations and then announcing that all
admissible survivors fit the evidence would obscure the evidential cost of the
filtering. The method does not yet prevent that. Preregistration is not a
substitute for justification: a criterion can be prejudicial before results are
inspected, and revising an ontology after a discovery need not be an
illegitimate rescue. An account of principled revision is needed.

## 5. The paper demands completed comparisons and supplies none

This is the central architectural problem.

| Case | What the manuscript establishes |
|---|---|
| Brading | A conditional comparison whose matched likelihoods are stipulated |
| Relativistic becoming | A classification under premises whose ontological authority remains unsettled |
| Preferred-frame tests | Constraints on physical signals, without an ontology discriminator |
| Quantum clocks | Scope restrictions on equivalence claims, without a temporal-ontology comparison |
| Finite records | Equal probabilities under assumed measure and response-kernel matching |
| Causal sets | Covariance and extension issues, without an embedded-record model |

The qualifications are honest, but the cumulative result is that the framework
never demonstrates its promised usefulness through a completed application. A
methodological paper need not settle eternalism versus presentism, but it
should do at least one of: expose a consequential mistake in a published
argument; show a proposed discriminator fails for a previously neglected
reason; establish a non-obvious equivalence or inequivalence; defend a disputed
bridge; or materially improve an explanatory comparison. The manuscript mostly
says what someone would need to do. Section 8 reads like the proposal for a
paper rather than its conclusion.

## 6. The Brading example threatens the ontology classification

**Location:** §2.2, pp. 3–4.

The paper begins with presentism as a restriction on unrestricted concrete
existence, then examines system-relative, potentially nontransitive presents
that can extend across a system’s entire history. Those are not obviously
instances of the same ontology. Brading changes the direction of explanation:
dynamically constituted unities determine what counts as present, rather than a
prior temporal present determining what exists. Her present can occupy an
extended spacetime region.

The key question is therefore not initially “Does this view have the same
likelihoods as eternalism?” but “What makes this a restriction on existence
rather than a different way of individuating persisting systems?”

The paper’s union objection is excellent:

```
U_i proper subset W for every i  does not imply  union_i U_i proper subset W.
```

Every system-present could be smaller than the universe’s history while their
union covers the entire history. That does not prove Brading’s view is
eternalism; it shows that local boundedness alone does not supply the advertised
global ontological difference. The draft identifies this and leaves it
unresolved. This is arguably the most philosophically substantial problem in the
manuscript.

Develop it: specify the domain of unrestricted quantification; whether
existence is system-relative; how overlapping presents interact; which events,
if any, are excluded; whether the exclusion follows from physics or an
additional actuality principle. Until then Brading is not a successful worked
example; she is a difficult test of whether the framework can identify its own
comparison targets.

## 7. The quantum calculation is underreported and one-dimensional

**Location:** §5, p. 7.

The source-level caution is justified: the trinity construction assumes a
noninteracting clock and system. But the paper’s own calculation is not
sufficiently specified: matrices, clock states/POVM, sampled couplings,
selected eigenvalues, reduction maps, inner product, and results are missing.
The reader cannot assess “for the tested choices.”

More importantly, the one-dimensional sectors make the nonisometry result much
less informative than it sounds. If `H_phys = span{|Psi>}` with `|Psi|=1` and
`R_t` is linear, then `R_t^dagger R_t = |v_t|^2 I` whenever `v_t != 0`, so
`V_t = R_t/|v_t|` is an isometry onto its one-dimensional image. This does not
erase unequal clock-reading probabilities; it shows that nonisometry on a
one-dimensional domain can be a scalar weighting, not a substantive obstruction
to transporting a family of physical states.

The draft admits the sectors do not support arbitrary initial qubit states, but
that admission sharply reduces what the example illuminates. To make it
informative, provide a nontrivial physical state family, a defended inner
product, and a comparison separating changes in sector dimension, clock
probabilities, state-dependent distortion, and failure of dynamical
equivalence. Otherwise cut it or present it explicitly as a failed diagnostic.

## 8. The record proposition assumes the difficult part

**Location:** §6.

Proposition 1 is correct, but it assumes matching probability measures under a
map and matching complete outcome kernels, then proves matching outcome
probabilities. That is useful bookkeeping; the disputed physical content is in
the hypotheses. The finite-path example models revealed data and an access
restriction, not a memory-bearing subsystem whose dynamics explains the
restriction. The draft acknowledges this, but acknowledgment prevents
overclaiming rather than supplying the missing achievement.

A stronger elementary construction is available. For a finite controlled
process `X_{t+1}=f_t(X_t,A_t,U_t)` with independent inputs `U_t` and actions
depending only on available records, compare (i) drawing each `U_t` when needed
with (ii) drawing all `U_t` in advance but keeping unused inputs inaccessible.
With the same update functions and policy, these generate the same record
distributions under adaptive interventions, not just passive observation. The
contrast is sequential randomness versus presampled causal response structure.
This is not offered as novel; it shows how quickly the example can be
strengthened and how little either version establishes about temporal ontology.
The real problem is to justify access restrictions physically and connect them
to genuinely different ontological commitments.

## 9. The sophisticated physics adds breadth without argumentative force

**Preferred-frame effects.** The LAGEOS estimates are accurately reproduced.
But their numerical precision does almost no work: the conclusion is unchanged
whether the bound improves. A preferred timelike vector field is not
automatically a preferred foliation; hypersurface orthogonality is an
additional restriction central to the Einstein-aether/foliation relationship.
The prose should make that transition carefully.

**Causal sets.** The finite-cylinder covariance issue is genuinely technical
and the cited source establishes the relevant obstruction for that algebra. But
the paper lacks the argument connecting covariant event structure to physically
available records and then to a particular temporal ontology. The draft openly
says these bridges are missing. So why is the material part of the main
argument rather than a future-work paragraph? The draft is broadest exactly
where it is least complete.

## 10. The paper is not fighting the strongest opponents

The paper rebuts inferences such as “no invariant simultaneity, therefore no
passage,” “stationary constraint, therefore no change,” and “same records,
therefore same ontology.” Those are worth rejecting, but a research
contribution needs to identify who makes the relevant inference, in what form,
and why their strongest defence fails.

Saunders frames the relativity conflict in terms of the theory’s deficiency as
a description of the reality demanded by presentism: a structural-completeness
challenge, not merely an unnoticed leap from a coordinate transformation.
Pooley distinguishes easy compatibility strategies from attempts to take both
relativity and robust passage seriously. These identify the argument to
confront: why should preserving bare compatibility count for much when the
price may be abandoning the explanatory integration that makes the physical
theory attractive? The current answer — explanatory comparisons are legitimate,
and the verdict remains open — is permission to conduct the debate, not
participation in it.

## What survives

- Rejecting a conjunction does not automatically reject each conjunct.
- Equal likelihoods over specified protocols provide no likelihood-based
  discrimination within that domain.
- Representation equivalence does not automatically establish metaphysical
  identity.
- A representation of complete histories does not, merely by being complete,
  establish determinism.
- Operational access cannot simply be ignored when comparing implementations.

The manuscript expressly rejects the opposite positions (physics is irrelevant;
every ontology is rescuable; empirical equivalence entails ontological
identity). The surviving problem is that its strongest claims are mostly sound
but modest, while its potentially substantial claims remain incomplete.

## What the reviewer would rebuild

**Best option: a focused paper about one existence bridge.** Focus on Brading,
local presents, and unrestricted existence. Sharper question: under what
conditions does a physically defined local present constitute a restriction on
what exists, rather than merely a division of an eternalist history into
dynamical unities?

Suggested structure: define the ontological contrast precisely; reconstruct
Brading charitably (separate dynamical unity, endurance, presentness,
existence); formulate the coverage problem; examine possible repairs
(system-relative existence, privileged actual systems, restrictions on which
local presents coexist, revised presentism); assess costs; draw a limited but
substantive conclusion. A candidate conclusion: dynamical individuation alone
is insufficient to establish the intended existential restriction.

**Alternative: keep the methodological paper but make it demonstrate
something.** Reduce §§1–3 to the minimum; choose one published inference;
reconstruct its strongest version; identify the exact bridge; show how
alternative defensible bridges change the conclusion; deliver an actual
comparative judgment. Allow the outcome to be “physics defeasibly favors this
package, although it does not exclude every rival realization.”

## What to cut now

| Material | Action |
|---|---|
| Stein paragraph | Repair the missing-premise reconstruction |
| Quantum numerical example | Remove unless fully specified and diagnostically meaningful |
| Elementary record proposition | Compress to a short illustration or appendix |
| Causal-set discussion | Remove unless made the central case |
| Detailed LAGEOS numbers | Compress |
| Repeated audit/novelty disclaimers | Consolidate into one status note |

## Bottom line

This is currently a careful research prospectus dressed as a research paper.
Its caution is largely justified and its organization is useful, but it spends
too much effort showing that conclusions require further work and too little
doing that work. The repair is not more qualifications, more citations, or
another toy model. It is to choose one disputed bridge, defend or defeat it, and
accept the risk of reaching a substantive conclusion.
