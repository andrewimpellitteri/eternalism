# Second-pass primary-source audit (2026-10-19)

Scope: four targets only—Stein's relativistic becoming argument, Putnam and
Rietdijk's inference, Malament's conditional simultaneity theorem and its
primary critique, and Brading's alternative presentism. Read depths below mean
what was actually inspected in this pass. This is not a systematic review.

## 1. Stein 1991: exact assumptions and result

Primary source: Howard Stein, “On Relativity Theory and Openness of the
Future,” *Philosophy of Science* 58 (1991), 147–167. Full text inspected via
the scanned article at the `sources.jsonl` URL.

At pp.148–149 Stein asks whether a relation `R(a,b)` (“the state at b is
already definite as of a”) can be defined from Einstein–Minkowski geometry
with four requirements: (i) the basic reference entity is a here-now point;
(ii) definiteness propagates transitively; (iii) a point is definite as of
itself; (iv) at every point some states remain unsettled. A time orientation
is stipulated. He provisionally treats spacetime geometry as conformal (no
distinguished spatiotemporal unit), and regards all points in the causal past
as definite, because they may influence the state at the point (pp.148–149).

The OCR transcription at p.150 prints a theorem with only reflexivity,
transitivity, time-orientation-preserving automorphism invariance, and existence
of one past-pointing causal pair. **That displayed statement is false if read
literally.** For example, universal `R` meets those listed conditions but is
not the causal-past relation. Also `R(a,b) := (a=b) or (b is strictly
timelike-past of a)` is reflexive, transitive, and invariant, and includes a
past-pointing timelike pair, but omits null-related past points. These are
elementary countermodels to the theorem as transcribed.

The preceding argument on pp.148–150 carries additional constraints: condition
(iv) says that for every a some points remain unsettled as of a (which excludes
universal `R`), and the physical interpretation of spacetime commits the
candidate relation to containing *all* of a's causal past (which excludes the
strictly-timelike-only relation). With these contextual assumptions, the
candidate is forced to be the causal past. Those missing hypotheses, or
equivalent null-inclusion/causal-closure and non-universality conditions, are
needed for a valid result. The web-accessible text is OCR, and I could not
inspect a page image of the printed theorem; therefore I cannot determine
whether the omission is in the published typography, the OCR/transcription, or
the way the theorem is excerpted from its immediately preceding context. Do
not attribute an error to Stein absent page-image verification.

Accordingly, the safe context-preserving reconstruction is: in a time-oriented
Minkowski model, suppose `R` is definable/invariant under the stated
automorphisms, reflexive and transitive, contains the entire causal past of
each point, and satisfies the open/unsettled condition (iv). Then no
spacelike or future pair can also be in `R`, for that would force `R` to be
universal; hence `R` is exactly the causal-past relation. Stein notes that
his no-distinguished-unit assumption can be removed with a modified geometric
argument (p.150). This characterization is narrower than “SR permits
objective passage”: it gives an invariant causal-past relation, not a theorem
that objective passage exists. Whether `R` represents “already
become/definite” remains a bridge choice. Stein explicitly says whether the
candidate is satisfactory cannot be settled by mathematics alone (p.150).

Stein's criticism of Maxwell is separate. At pp.151–152 he rejects an
unargued inference from mutual indefiniteness of spacelike events to
self-indefiniteness, and challenges treating an observer-relative
simultaneity hyperplane as one global spatial present. That criticism should
not be conflated with the theorem's proof assumptions.

## 2. Putnam and Rietdijk: premises, scope, and distinction from determinism

Primary Putnam source: “Time and Physical Geometry,” *Journal of Philosophy*
64 (1967), 240–247. Scanned text inspected across pp.241–247; particularly
pp.241–243 and 246–247.

Putnam's starting ontological thesis is (1): “all (and only) things that exist
now are real” (p.241). His principle III, explicitly called the principle
“There Are No Privileged Observers,” says: if all and only things in a
physical relation `R` to me-now are real and you-now is real, then all and
only things in the same relation `R` to you-now are real (pp.241–242). He
requires `R` to be a tenseless, coordinate-independent physical relation and
not accidentally selected by the initial realness extension (p.242). Under
SR, he applies observer-relative simultaneity and uses the overlap of
co-located me-now/you-now to transfer realness; an event future-relative to
me can thereby become real (pp.242–243). The paper's more general closure
argument explicitly invokes the *transitive closure* of the relation “y is
simultaneous with x in x's coordinate system” and assumes enough observers,
including physical systems/fields (pp.246–247).

Correction to first-pass shorthand: saying simply that “transitivity of equal
existence across overlapping presents” is Putnam's bridge premise is
imprecise. The stated bridge is principle III (observer neutrality), and
the broad extension uses transitive closure plus an abundance-of-observers
premise. Standard simultaneity's geometric transitivity is not the same
premise. The argument is not forced by Lorentz geometry alone; the physical
kinematics plus these claims about reality and observers do the work.

Putnam discusses the sea-fight and truth-value/determinateness separately
(pp.243–246), and argues that future contingents already have truth values.
That move is stronger than the ontological consequence and does not follow
from relativity of simultaneity without additional assumptions. In modern
terms, determinism (laws plus state fixing a unique history), truth-value
determinacy, future openness, and eternalism are distinct theses. Putnam's
paper argues for a block ontology and against his target indeterminism; this
does not make eternalism logically equivalent to determinism.

Rietdijk's primary paper, “A Rigorous Proof of Determinism Derived from the
Special Theory of Relativity,” *Philosophy of Science* 33 (1966), 341–344,
was not available as inspectable full text in this pass. Its publisher record
and abstract say that an event may already be past for a possible distant
observer at the moment that is “now” for us, then state a determinism
conclusion. Thus the argument's precise steps and bridge assumptions remain
unverified here; do not present the abstract's conclusion as a theorem proved
from SR alone. Stein's 1991 discussion at p.148 reports the essential
similarity to Putnam and says the argument is misapplied, but that is Stein's
assessment, not Rietdijk's text.

## 3. Malament: conditional result and its boundaries

Primary Malament source: David Malament, “Causal Theories of Time and the
Conventionality of Simultaneity,” *Noûs* 11 (1977), 293–300. The primary
article could not be accessed in this pass. The following exact-condition
summary is therefore **not independently verified against Malament's own
pages**; it is checked against the authors' primary critique, Sarkar and
Stachel (1999), and the archived SEP exposition. Malament's paper remains
`abstract` depth.

Sarkar and Stachel's primary paper, “Did Malament Prove the Non-Conventionality
of Simultaneity in the Special Theory of Relativity?” (1999), pp.208–220,
section 2, states Malament's framework in detail: causal connectibility `κ`
(events can be connected by a signal in either direction), an inertial
observer's full worldline, and a candidate simultaneity relation defined
from those. Their presentation lists conditions including equivalence,
nontriviality, cross-worldline related events, and invariance under causal
automorphisms preserving the observer worldline; it then identifies temporal
reflection invariance as the premise that excludes forward/backward null-cone
alternatives. The archived SEP statement gives a closely related abbreviated
condition list (definability from `κ,O`, equivalence, non-universality and a
cross-worldline related pair) and says the result is standard synchrony.

The safe claim is conditional: in the specified Minkowski/observer/causal
definability framework, with the stipulated invariance and simultaneity
conditions, Einstein synchrony is unique. This is neither uniqueness of
metaphysical presentness nor evidence for eternalism. Sarkar and Stachel
argue that temporal-reflection invariance is physically unwarranted; dropping
it admits future- or past-null-cone definitions, and what remains distinctive
about Einstein synchrony is its independence from observer position within an
inertial frame. This critique does not by itself vindicate every
conventionalist account. Exact formalization should wait for the original
Malament text and the full Sarkar–Stachel proof, not rely on SEP shorthand.

## 4. Brading: a serious alternative, but not a demonstrated measurement

Primary source: Katherine Brading, “Presentism as an Empirical Hypothesis,”
*Philosophy of Science* 80 (2013), 1101–1111. The primary PDF was located;
search-indexed text was inspected for the introduction (p.1101), the
discussion around p.1104, and the epistemic-unity discussion around p.1110.
The complete PDF text was not continuously audited, so the record remains
`abstract` depth and this is a selective text check, not a full-text audit.

Brading begins with (P1) “all and only things that exist now are real” and
(P2) SR is a complete account of spacetime structure (p.1101). The familiar
conflict appears if spacetime/simultaneity is assumed to supply the
ontological unity of everything real. Her alternative rejects that shared
assumption: she proposes using unity grounded in physical laws (via a
law-constitutive approach drawn from Newton) rather than a preferred global
simultaneity foliation. She expressly rejects adding a preferred foliation
(p.1104), and recasts spacetime as an *epistemic* principle of unity—a
framework for organizing inferences to remote/unobserved events—rather than
the ontological ground of what exists (around p.1110). She labels the view an
empirical hypothesis compatible with SR and not yet falsified, while admitting
that it needs substantial elaboration.

This is a substantive reply to the blanket inference “SR rules out any
presentism,” and it blocks an easy dismissal based only on lack of absolute
simultaneity. But the inspected text does not provide a concrete quantitative
prediction or an experimental protocol that distinguishes her ontology from
eternalism. “Empirical hypothesis” here is a programmatic and theory-choice
claim, not evidence of a confirmed empirical distinction. Her proposal also
does not, in these passages, establish an objective passage variable. It is
not a growing-block defense, so the stronger growing-block debate and
epistemic objection remain an unfilled target.

## Audit of the first-pass report/map

- **Corrected:** The web OCR's isolated statement of Stein's theorem at p.150
  omits assumptions needed for validity. Universal `R` and reflexive
  chronological past are counterexamples to the isolated wording. The proof's
  surrounding context supplies (iv) and inclusion of the full causal past;
  whether the omission is in print or OCR remains unverified. The valid
  context-preserving result characterizes causal past, not objective passage.
- **Confirmed, with scope added:** SR's relativity of simultaneity alone does
  not choose a privileged global present.
- **Corrected:** Putnam's key bridge is stated as observer-neutral principle
  III; the paper's broader conclusion also uses transitive closure and
  “enough observers.” It is not merely geometric transitivity of synchrony.
- **Narrowed/unverified:** Malament's result is conditional and stronger than
  “causal geometry determines simultaneity” in ordinary language. Primary
  proof not accessed; the exact conditions in this audit are relayed through
  primary critics and a secondary summary. His result does not settle ontology.
- **Narrowed:** Brading offers a live conceptual/empirical research program
  that rejects spacetime as ontological unity, but the inspected text supplies
  no concrete discriminating observation. The earlier report overstated this
  as a testable variant without making that limitation clear.
- **Still unverified:** Rietdijk's proof steps, strongest presentist models
  beyond Brading, and a robust growing-block response (including its
  epistemic-location challenge) require primary full-text audit.

## Remaining scientific bottleneck

The key bottleneck is a sharply specified, empirically articulated bridge
from a physical structure (causal cones, foliation, law-governed dynamics, or
records) to ontological status or objective passage. Existing kinematics
constrains simultaneity and causal access, but the inspected arguments do not
show that those observables distinguish eternalism, local becoming, or
law-constitutive presentism. A computational contribution must first define
model classes, observables and allowed bridge rules without building the
desired ontology into the definitions.
