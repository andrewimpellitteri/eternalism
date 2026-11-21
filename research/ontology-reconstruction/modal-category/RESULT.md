# The modal category of existential openness: ω_t^ex, the nomological box, and three physical model categories

Task `ontology-modal-category-bridge`. 30 October 2026. Primary-source
reconstruction and model-category translation; no new PDE work, no novelty
claim, no ontology verdict. Strongest counterexample first, as the brief
requires.

Read depths: C&R ch. 7 read in full directly from the local primary PDF
(all 18 pages); C&R "Replies to Critics" §7 pp. 477–483 read in full from
the open-access Sciendo text; Sbierski arXiv:1309.7591v3 read at selected
sections (definitions and statement of Theorems 2.6–2.8, Lemmas 3.1/3.3);
Choquet-Bruhat–Geroch 1969 at abstract/discovery; Luk–Oh–Yang at abstract,
with its Theorem 1.7 known only through the project lane record. Full
records with limits are in `sources.jsonl`.

## 0. Strongest counterexample first

**The coordinator's open cut M_< does not instantiate C&R's existential
openness.** The brief asked me to check this, and it fails, in two
independent ways.

1. *No last moment.* C&R's own treatment of cessation assumes a last
   moment: "This grounding explanation presupposes that if time does not
   go on indefinitely, there is a last moment of time. This is not an
   entirely innocent assumption; however, note that it is compatible with
   time's being discrete, dense or continuous" (ch. 7, p. 111). M_< =
   {p ∈ M : T(p) < T_*} has no final event; its excluded boundary is not
   part of the model (coordinator MAXIMALITY_AND_EXISTENTIAL_OPENNESS.md
   §2 states this itself). So M_< cannot witness a clause whose own
   grounding story runs through a last moment, and C&R explicitly flag
   that assumption as load-bearing rather than innocent.
2. *Wrong modal category.* C&R's witnesses of existential openness are
   **complete alternative worlds in which later times never exist**:
   grade (III′) is "Now, ω^ex_now, but neither t nor any time later than
   t ever exists", grade (II′) keeps later times existing but empty
   (p. 116). In the Replies, the matching permanentist construction is
   likewise a complete world: "a world that is a perfect match of the
   actual world up to 2050 and then ceases to exist" (Replies §7, p. 481,
   quoting Torre 2021: 430, with C&R's remark that the match is
   location-based). Both sides of the source exchange use terminal-time
   complete worlds. Nobody in the exchange uses an open cut. M_< is a
   stage-like initial development of one physical history, not either
   rival's possible world.

Consequence: the same pointed causal past comparison in the smooth class
(open variation of finite future readings with J⁻(b) and incoming mass
fixed) does not show that C&R's (IND_ex) is instantiated by the physics.
It shows something else — that one *specific weaker database* (the
observer's causal past) underdetermines later readings while the full
databases do not. That separation is the positive content below.

## 1. The source clauses pinned (Done-when 1)

### 1.1 The worldstates of ch. 7 (pp. 113–116)

'(DET)' glosses determinism as "Always, ∀tG∀t′ (t ≺ t′ → the way the world
is up to t nomologically determines the way the world is up to t′)"
(p. 113); '(IND)' is its negation with "Sometimes, ∃tF∃t′" and a negated
determination claim. The vague phrase "the way the world is up to t" is a
nominalisation of 'At t, ω_t', where ω_t is "a description of what
actually is or used to be the case at t, where this description is in some
pertinent sense complete" (p. 114).

**The ban (p. 114).** ω_t must not contain clauses equivalent to 'Fφ' or
'Fnφ', nor clauses "ultimately reducible to clauses of the forms '¬Fφ' or
'¬Fnφ'". Their reason is anti-trivialization by example: if present facts
fix that event e will occur with determinable Φ in n units but not which
determinate Φ₁, "It would be cheating to try to restore cohergence of this
example with (DET) by conceiving 'ω_now' to entail '¬FnΦᵢ(e)', for each
determinate of Φ, Φᵢ, that is distinct from Φ₁." This is the source's own
anti-cheating principle; I use it in §4.

**ω_t^loc (p. 114).** "a complete description of all the entities actually
located at t, or at any time earlier than t, in terms of the natural –
non-Lucretian and non-Cambridge-like – properties and relations among them
that they actually instantiate at t or at any earlier time", plus totality
clauses "'and that's everything located at the present time'", unembedded
or embedded under 'P', 'H', or 'At t′' with t′ ≺ t.

**ω_t^ex (p. 115).** "a complete description of all the entities actually
existing at t, or at any time earlier than t, in terms of the natural –
non-Lucretian and non-Cambridge-like – properties and relations among them
that they actually instantiate at t or at any earlier time", plus totality
clauses "'and that's everything existing at the present time'" in the same
positions.

Two features matter for translation. First, ω_t^ex is **cumulative**:
"existing at t, or at any time earlier than t" — on GBT past things still
exist at t, so the cumulative and snapshot readings coincide for GBT but
not for presentism; this is exactly why C&R say presentists can take the
same openness only by opening the past too (p. 116). Second, ω_t^ex
contains a **totality clause at each embedded present**: the description
asserts that nothing exists beyond what it lists, at each time it covers.
It is a completion claim about inventory, made without any future-tensed
clause — which is precisely what lets the same ω_t^ex hold in worlds that
differ in what exists later.

### 1.2 The modality (pp. 114–115)

- (DET_loc): "Always, ∀tG∀t′ (t ≺ t′ → □(At t, ω^loc_t → At t′,
  ω^loc_t′)) where '□' encodes nomological necessity" (p. 114).
- (IND_loc): "Sometimes, ∃tF∃t′ (t ≺ t′ & ⬨(At t, ω^loc_t & ¬ At t′,
  ω^loc_t′))" (p. 115). The diamond ⬨ is not separately glossed; on the
  text's own terms it is naturally the dual nomological possibility
  operator. Note 7 (p. 113) supports the law-relative reading: (IND) is
  compatible with probabilistic laws, since "any non-zero probability at
  least requires nomological possibility".
- (DET_ex) / (IND_ex): the same forms with ω^ex (p. 115).

**Caveat recorded:** the 'At' operator's free-logic behaviour (truth of
'At t′, φ' when t′ fails to exist) belongs to the base system of chapters
1–5, which were not available; the extraction CLAUSES.md notes this too.
My reconstruction reads '¬At t′, ω^ex_t′' as the failure of the complete
description at t′, witnessed in grade (III′) by t′ not existing. The
subscript layout ω^loc/ω^ex is a reconstruction from line breaks
(CLAUSES.md header), consistent with the page images.

### 1.3 The grades (pp. 115–116)

Witnessing '⬨(Now, ω^ex_now & ¬At t, ω^ex_t)' with now ≺ t:

- (I′) "Now, ω^ex_now, but at t, some of the things actually located at t
  are located at t and have properties distinct from the ones they
  actually have at t" — same inventory, different future property
  instances.
- (II′) "Now, ω^ex_now, but while t, and times later than t, sometimes
  exists, always, for all times t′, such that either t = t′ or t ≺ t′, no
  entity distinct from t′ is ever located at t′" — bare time continues,
  empty of content. Note the grades are stated with 'located' in the
  counterfactual consequent even in the ^ex case; only the held-fixed
  worldstate differs between the ^loc and ^ex versions.
- (III′) "Now, ω^ex_now, but neither t nor any time later than t ever
  exists" — later times absent from the alternative world entirely.

Availability (p. 116): (I′) is unavailable on event-essentialist
eternalism; (II′) is "no option" for permanentists short of locating
everything at earlier times; (III′) is "no option" for permanentists
because for them now, t and all later times exist. "GBT is
unproblematically consistent with (I′) to (III′)"; openness as (IND_ex) of
grade (II′) or (III′) is "perfectly compatible with the bivalence of all
future-tensed statements, including future contingents". This is the
chapter's headline: existence-based openness without truth-value gaps.

### 1.4 The Replies §7 (pp. 477–483, read in full)

The decisive passage, pp. 480–482: "Whether determinism and indeterminism
are time-symmetric crucially depends on how we understand the world states
whose sequence they concern" (p. 480). The location-based conception makes
both time-symmetric — C&R concede this to Torre. The alternative:
world states "constituted by what exists simpliciter at the time at which
those states themselves are located … World states can then be seen as
snapshots of what reality is like at the times at which they are located,
where, at each such time, reality comprises all that exists simpliciter at
that time" (p. 481). Then "as long as such world states form a distinctive
ontological category", GBT may combine existential indeterminism about the
future with existential determinism about the past: "That is, GBT may then
allow that reality as it is at a given time could end at that time, even
if it actually will grow to include more world states in the future,
whereas reality as it is at that time could not have begun at that time,
if it actually did not begin at that time. Neither presentism nor
permanentism can commit to both" (p. 481).

And the concession my brief flagged (p. 482): "Existential indeterminism
vindicates the asymmetry intuition, only if GBT is in fact true. Insisting
that it does consequently implies insisting that GBT is true … We do not
insist that GBT is true because we do not pretend to possess such an
argument. Consequently, we do not insist on the claim that existential
indeterminism vindicates the asymmetry intuition. A fortiori we do not beg
any question against permanentism."

The Replies' snapshot gloss and ch. 7's cumulative definition agree on
GBT (accretion makes "exists at t" include everything earlier), but they
are distinct formulations; I keep both pinned and do not merge them.

## 2. Three physical model categories with the same local field equations

Fix the vacuum or Einstein–massless-scalar Cauchy problem. Category
members are what a "possible complete history of this theory" could be.

**Cat0 — arbitrary smooth globally hyperbolic developments (GHDs).**
Sbierski's Definition 2.1 (arXiv:1309.7591v3): a time-oriented globally
hyperbolic solution with an embedding of the initial data making the
image a Cauchy surface. Every proper restriction of a solution to a past
set bounded by a Cauchy slice is again a member (the coordinator's M_< is
one; COMMON_EXTENSION_REPAIR.md gives the sharper Minkowski-minus-J⁺(q)
variant that keeps the stipulated whole potential realm). Any two members
of the same data have a common extension (Theorem 2.7, "Global
uniqueness": "Given two GHDs M and M′ of the same initial data, there
exists a GHD M̃ that is an extension of M and M′"). This category is
closed under deletion of the future.

**Cat1 — maximal developments (MGHDs).** Theorem 2.8 / Choquet-Bruhat–
Geroch 1969 (Commun. Math. Phys. 14(4), 329–335, DOI 10.1007/bf01645389):
for given initial data there exists a GHD extending every other GHD of
the same data, unique up to isometry. Maximality is a property of a
solution, selected by the theory's own completion rule; it is **not**
implied by the local equations, which hold on every Cat0 restriction
equally (coordinator MAXIMALITY §3; the actuality-maximality-review
AGENT_REPORT.md records the same correction). Members may still be
singular: an MGHD can be inextendible while geodesically incomplete.
Whether a given member ends is fixed by its initial data through the same
uniqueness — there is no second maximal world with the same past and a
different future extent.

**Cat2 — the selected two-sided complete scattering class.** The project's
compact-profile Einstein–scalar class, whose members are MGHDs that are
in addition two-sided causally geodesically complete. Primary anchor:
Luk–Oh–Yang, arXiv:1605.03893, whose abstract states solutions "causally
geodesically complete both to the past and to the future"; the project's
SCATTERING_PAIR.md reads their Theorem 1.7 and §2 as the existence source
(their normalisation Ric_ab = 2∂_aφ∂_bφ). I did not read the paper beyond
the abstract; theorem content is taken from the lane record at discovery
depth. In Cat2 every finite proper-time target of the central observer
exists as a scalar-evaluation event in every member (coordinator
REALM_CONTRAST_IN_SMOOTH_CLASS.md §4 records the corresponding
whole-realm rigidity).

**Cat3 — complete worlds with terminal-time semantics.** Time series with
a last moment and no field-failure: neither a GHD (the underlying
manifold would have boundary, outside Definition 2.1), nor an MGHD, nor
in the selected class. No member of Cat3 is produced, or ruled out, by
the Einstein–scalar equations; such a category needs its own boundary
principle (a termination law, or primitive cessation as a law-level
posit). C&R's grade (III′) witnesses, grade (II′) witnesses, and Torre's
permanentist cessation world are all naturally Cat3 objects. This
category has no existence/uniqueness theory in the project records; it is
named here to mark what a honest translation would have to supply.

The finite illustration `check_modal_witnesses.py` (stdlib, 0.02 s)
tabulates the witness bookkeeping across these categories on rational
time lines: one entity per time, db(t) the frozen cumulative description
with totality clause. It is an illustration of bookkeeping, not a proof.

## 3. The database separation (coordinator question answered)

The brief asks: does a same-past causal model fix ω_t^ex? **No.** Three
distinct comparison databases must not be conflated; each has its own
determination verdict in the smooth class:

| Database held fixed | Relativistic analogue | Verdict in the smooth class |
|---|---|---|
| ω_t^ex (cumulative block up to t) | the restricted development {T ≤ t}, containing the full slice {T = t} | determines everything later, in Cat1 and Cat2 (uniqueness of MGHD: the slice data admit one maximal development) |
| pointed causal past J⁻(b) (+ incoming mass) | the observer's past cone | does **not** determine later readings (conditional open-range result, REALM_CONTRAST §4 row 1; exterior radiation differs elsewhere) |
| whole bow-tie realm B(b) = M \ (J⁺(b) \ {b}), realm-matched with marked germ | open realm isometry | determines the entire development in the selected class (rigidity, REALM_CONTRAST §3) |

So: same pointed causal past is **not** the same complete existing realm;
and the failures the open-range result exhibits are failures of
*causal-access* determination, not of (DET_ex). If ω_t^ex is translated
cumulatively (block up to t), then the models compared in the open-range
result have **different** ω_t^ex at the reading time (their elsewheres
differ), so they do not witness (IND_ex) at all. Conversely, B(b)-matching
is stronger than ω^ex-block matching need be: it also matches
future-of-b-elsewhere data. Neither equals the other. Any argument that
moves from the J⁻(b) result to "the existence-based future is open" — or
from the rigidity result to "the existence-based future is closed" —
changes the database in mid-inference. Both inferences fail at this
bridge, as the coordinator's MAXIMALITY §6 anticipated; the clause-level
reason is now explicit: ω_t^ex is cumulative over all entities up to t,
while J⁻(b) and B(b) are standpoint-relative causal profiles.

## 4. The translation and its obstruction (Done-when 2)

### 4.1 The classical → relativistic bridge is an extra premise

Ch. 7's framework has a primitive linear time series with absolute
simultaneity; entities are located at times, and times are containers.
The Einstein–scalar class has none of that. A translation needs:

- **T-bridge.** Choose a global temporal function T (exists: every member
  is globally hyperbolic; canonical up to normalization in the selected
  class via the center-normalized construction, but a convention in
  general). Map "the world up to t" to the restricted development
  {T ≤ t}; map "entity existing at t" (GBT reading) to "event located in
  {T ≤ t}".
- **Container/content drop.** In spacetime the events are the basic
  particulars; there is no level at which a time exists while nothing is
  located at it. Every event carries metric and scalar values.

Without the T-bridge, (DET_ex) is not even formulable over the physical
class; with it, the verdicts below follow. I state the bridge as a
defended assumption, not a discovery: it preserves the classical
cumulative-database structure and adds a foliation-type choice, which is
precisely the kind of premise AGENTS.md requires to be separated from
mathematics.

### 4.2 Verdict per category

**Cat0: (DET_ex) false for every pair; the box is trivialized.** For any
t ≺ t′, take the actual M and the restriction M_< cut between T(t) and
T(t′). Both contain the same block up to t (so 'At t, ω_t^ex' holds in
both), and in M_< the atom at t′ fails (no such time). So □(ω_t^ex →
ω_t′^ex) fails for **every** t ≺ t′, regardless of the field equations.
Under Cat0 admissibility, (IND_ex) is witnessed for every future
statement whatever the laws — the finite check tabulates 15/15 pairs
across the cut family. This is C&R's own anti-cheating pattern (p. 114):
hidden future-negation clauses trivialize (DET); unrestricted
future-deletion in the possibility class trivializes □ the same way. A
"nomological necessity" operator that fails on every pair is not tracking
the laws. **So Cat0 cannot be the intended range of □ without bankrupting
the nomological reading.**

**Cat1: (DET_ex) true; no same-past pair differs in later existence.**
Suppose two Cat1 members share the block up to t. They share the Cauchy
data on {T = t}. By Theorem 2.7 both embed in a common GHD; by
maximality both are MGHDs of those data; by Choquet-Bruhat–Geroch
uniqueness they are isometric (Sbierski's Lemma 3.1, verified verbatim:
two isometric immersions agreeing at one point with equal differential
are equal, supplies the rigidity step once the first jets match).
Hence no two distinct Cat1 worlds share ω_t^ex while differing later —
whether a member ends is itself fixed by its past. Singular ends exist in
Cat1 across different data, but never as alternatives with the same
ω_t^ex: an "ending" is a nomologically fixed physical feature, not a
chosen modal branch. **So maximality + uniqueness alone — not
completeness — already kills the same-past existential-openness witness.**
Completeness (Cat2) adds only that no member ends at all. (Honesty note:
the re-slicing uniqueness invoked here is standard for smooth
developments; its coupled-scalar regularity category is the
lawful-completions lane's audited input and is not re-verified in this
task.)

**Cat2: (DET_ex) true, and grade (III′) has no witness even across
different data.** Every member is two-sided complete; "later existence
fails because reality stops" is excluded by class membership, not by a
per-model boundary event.

**Cat3: unavailable from the theory.** Terminal-time complete worlds are
not GHDs, MGHDs, or members of the selected class. Producing them needs a
boundary rule (a law-level termination principle, or primitive cessation)
plus new semantics. C&R never supply one in ch. 7 — ch. 7 does not
identify the laws at all — and the physics supplies none. Note the
source's own care on p. 111: the last-moment assumption "is not an
entirely innocent assumption".

### 4.3 Grade-level translation

- **(I′)** (same inventory, different future properties): under the
  T-bridge with the cumulative database, excluded in Cat1/Cat2 by the
  same uniqueness. The *conditional* open-range result exhibits (I′)-like
  variation only for the J⁻(b) database, which is not ω_t^ex (§3).
- **(II′)** (later times exist but empty): **no relativistic analogue.**
  Container/content structure is absent; an "empty time" is not
  expressible over events-with-fields. This is an exact obstruction, not
  a gap in effort: ch. 9's spatiotemporaryism (points as the basic
  particulars, (P1R)/(P2R)/(PO)/(BO), per CLAUSES.md and the coordinator
  point-profile record) likewise has no container level, so the
  strongest GBT-specific grade of ch. 7 cannot be carried into the
  relativistic debate by translation at all.
- **(III′)** (later times never exist): three different realizations that
  the classical operator does not distinguish, corresponding to §2's
  categories — (a) a nonmaximal restriction (Cat0: deletion of the future
  from a mathematical model, no physics content), (b) a singular end of
  the MGHD (Cat1: a physical feature of the solution, nomologically fixed
  by the past, absent in the selected class), (c) a terminal-time world
  (Cat3: needs a boundary principle the theory lacks). **(IND_ex) of
  grade (III′) is therefore three different claims; none of them is
  delivered by the smoothness/MGHD results, and only (a) is delivered by
  anything in our toolkit — which is exactly why (a) must not be presented
  as instantiating the claim.**

## 5. Stage, open cut, and complete world with terminal time

Three objects that must never be merged:

1. **A stage**: an interpretation of one complete history. On a growing
   reading, the concrete inventory at t is {T ≤ t} within the one actual
   development M. No modal claim is made; M is neither truncated nor
   competed with. MAXIMALITY §5 is right that this is consistent with
   accepting maximal mathematical histories; nothing here selects a
   temporal ontology.
2. **An open cut**: a nonmaximal development M_< of the same initial
   data, with no last moment. It is a model of the theory in Cat0 and
   nothing more. It is not a stage (a stage lives inside a complete
   history; the cut is a different, smaller model), and it is not a
   world of the rival's modal space (§0).
3. **A complete world with terminal time**: a Cat3 object with final
   included boundary semantics. Both C&R's grades (II′)/(III′) and
   Torre's permanentist match live here, as informal modal claims. The
   physics neither supplies nor excludes the category; excluding it from
   a comparison is a stipulation of maximal-world admissibility plus
   class choice, defended as such in §6.

The actuality-maximality-review demanded exactly this separation; §2–§4
make it clause-exact.

## 6. The positive bridge argument, with its assumptions separated (Done-when 3)

**Bridge claim:** when a determinism formula like (DET_ex) is evaluated
over a physical theory's possibility space, the box ranges over the
theory's admissible complete histories; for the Einstein–scalar theory
the only canonical candidate for that range is the MGHD category (Cat1),
or the selected complete subclass (Cat2) when class-specific completeness
is stipulated.

- **P1 (law-relativity, from the source).** '□' encodes nomological
  necessity (p. 114); n. 7 extends the framework to probabilistic laws.
  So the box's range is fixed by the laws.
- **P2 (anti-trivialization, from the source's own principle).** p. 114
  bans clauses that would make (DET) fail trivially. Admitting open cuts
  as complete histories makes □ fail on every pair (§4.2 Cat0), which is
  trivialization of exactly the source's kind. So a nontrivial nomological
  box requires a range closed under the theory's own completion rule.
- **P3 (canonicity, from the mathematics).** The MGHD is the theory's own
  canonical completion of given data (Choquet-Bruhat–Geroch; Sbierski's
  construction; his introduction: the MGHD "defines the object whose
  properties one needs to understand" for the global Cauchy problem).
  Choosing it is an interpretation of the theory — the actuality-review
  is right that it is not a theorem — but it is the only candidate the
  theory itself supplies, and every alternative range is either
  trivializing (Cat0) or extra-theoretic (Cat3).

**Conclusion (conditional):** under P1–P3 and the T-bridge, (DET_ex) is
true and (IND_ex) false in the Einstein–scalar class. Existence-based
openness is nomologically excluded there; it survives only as (i) broader
metaphysical possibility (against the p. 114 gloss), (ii) a different
law-class with a termination principle (Cat3, unstated in ch. 7), or
(iii) a stage-interpretation of one history (§5.1, no modal claim). Each
route needs its own argument; none is delivered by the physics, and
none is refuted by the physics either. **This is a translation result
with separately defended premises, not a physical theorem and not a
refutation of C&R.**

Accepting maximal mathematical histories is still not eternalism, and
model maximality is still not entailed by local equations (both recorded
in MAXIMALITY §§3, 5 and preserved here).

## 7. The charitable rival, stated as strongly as possible

**Rival reading (law-agnostic nomological space).** Ch. 7 never says which
laws hold. The rival reads □ as ranging over alternatives admitted by the
actual laws, whatever they are, and maintains that the actual laws could
be cessation-permitting: reality's ending at a time is nomologically
possible without any field-level boundary event — a primitive
law-level posit, of the same standing as other unfounded law facts. On
this reading, every verdict of §4 is beside the point: the Einstein–scalar
class is a class of *some* law, and the rival's openness claim was never
about that law. The rival can add that C&R's p. 482 concession shows they
claim no physical vindication anyway.

**What this rival preserves:** coherence of (IND_ex) with bivalence
(ch. 7's actual result); the asymmetry mechanism (existence-accumulation
makes the past fixed and the future open, pp. 481–482); immunity from all
Cat0–Cat2 results.

**What it costs (our defeater):** the possibility space is stipulated,
not derived. If the laws are not specified, (DET_ex)/(IND_ex) have no
determinate content until a law-class is named; once the rival names one
that permits regular cessation, that principle is an additional modal
commitment that the argument for openness must own explicitly — it cannot
be read off growth or off the equations. And per the source's own
concession (p. 482), the rival cannot claim that this openness vindicates
the asymmetry intuition without an independent argument for GBT. So the
rival keeps a coherent possibility and loses any claim that the physics
explains or evidences it: a possibility permitted by an ontology is not
yet a phenomenon explained by it (MAXIMALITY §7, which this task confirms
at clause level). Our analysis is defeasible in turn: a source-supplied,
independently motivated physical end rule compatible with the stipulated
theory (MAXIMALITY §9's first defeat condition), or a demonstrated
reading of ch. 7's □ as explicitly metaphysical, would defeat P1/P3 and
with them §6's conditional conclusion. The T-bridge would be defeated by
a source-faithful covariant reformulation of the cumulative worldstate
that needs no temporal function; I did not find one in ch. 7 or ch. 9
(the latter's fourfold structure is a different, standpoint-relative
database, §3).

## 8. Chapter 7 worldstates vs chapter 9 point profiles (no smuggling)

ω_t^ex is **not** the bow-tie realm B(b). They differ in structure:

- ω_t^ex is a description attached to a time on a linear series,
  cumulative over all entities up to that time, with totality clauses —
  a classical, foliation-shaped database.
- B(b) is a standpoint-relative causal profile: M \ (J⁺(b) \ {b}),
  defined from causal structure alone (coordinator
  RIVAL_PROFILE_AND_REGULARITY_BRIDGE.md §2), containing b's elsewhere
  and past but excluding its strict causal future.

Neither contains the other in general; their determination powers differ
(§3). Identifying them — or "imposing the chapter-9 bow-tie realm on the
classical chapter-7 world-state definition", as the brief forbids — would
silently convert a bivalence-era determinism formula into a relativistic
existence claim without the needed bridge. Ch. 9's own framework replaces
rather than instantiates ch. 7's worldstates: its operators are point-based,
its existence profile is B-type or J-type, and (as §4.3 records) it cannot
express grade (II′). The classical and relativistic openness debates are
genuinely different problems; the missing correspondence between ch. 7's
nomological operator and any physical category is now located precisely:
it lies in the T-bridge (§4.1) and in the admissibility stipulation (§6),
and it has no ch. 9 shortcut.

## 9. Separation table: physical theorem vs philosophical bridge

| Statement | Status |
|---|---|
| Same pointed causal past (+ incoming mass) does not fix later readings | conditional physical result, project record; database ≠ ω_t^ex |
| Whole-realm matching fixes the development in the selected class | physical-mathematical rigidity, project record |
| MGHD existence/uniqueness for given data | established mathematics (CB-Geroch 1969; Sbierski 1309.7591v3 Thms 2.7–2.8) |
| Cat0 admissibility trivializes the nomological box | theorem-shaped observation at translation level; finite illustration run; depends on T-bridge |
| Cat1 uniqueness kills same-past later-existence variation | corollary of established uniqueness + T-bridge |
| (II′) has no spacetime analogue | structural fact about the two ontologies |
| Maximal-world admissibility as the range of □ | philosophical bridge premise (P1–P3), defended, not proved |
| Existence-based openness survives only as stipulated possibility | conditional philosophical conclusion of §6 + §7 |
| GBT is true/false; the future exists/does not | not asserted; no ontology selected |

## 10. Defeat conditions and proposed next tasks

This analysis weakens if: a covariant, foliation-free reading of the
cumulative worldstate is supplied (defeats the T-bridge); a motivated
termination principle is shown to be part of some named physical theory's
standard formulation (makes Cat3 internal to a physics comparison); or a
source text shows ch. 7's □ explicitly ranges over metaphysical
possibility (overturns P1; note Appendix 3's translation manual was
unread and could bear on this). Conversely it strengthens if the
Replies' "distinctive ontological category" clause for world states
(p. 481) is given a non-question-begging instance over physical models —
no worker in this round has attempted that.

Next tasks, smallest first: (1) read *Nothing To Come* ch. 1–5 and
Appendices 2–3 to remove the free-logic/At caveat (§1.2) — the single
largest unread dependency of this reconstruction; (2) audit whether
any Luk–Oh–Yang-class existence result covers scalar boundary "no-boundary"
formulations that could act as a Cat3 analogue; (3) apply §3's
database table to the constitutive-extent test (NEXT_PHILOSOPHICAL_TESTS
§2), which currently uses "predictively sufficient" regions without the
ω-block/causal-profile distinction; (4) prior-art audit on
existence-based indeterminism in philosophy of physics journals since
2021 (Torre 2021 and replies exist; whether anyone maps existential
indeterminism to development categories — I found no such mapping in this
round's searches — is a novelty question, not a claim).
