# Local fragmentalism: the strongest version

24 October 2026. Position statement for red-teaming. Not reviewed. Claims are
tagged:

- **[PROVED]** a theorem in `research/stein-gr/main.tex` (two independent
  reviews, fixes applied; still needs a cross-model pass and an expert);
- **[CONDITIONAL]** follows from proved results plus a stated premise;
- **[THESIS]** a philosophical claim argued, not proved;
- **[OPEN]** not established.

Priority status (see PRIOR_WORK.md): Fine's relativistic fragments are
frame-times, not causal pasts (via Hofweber & Lange and Savitt, read in full);
Rovelli and Slavov are close in spirit but give no causal-past identification
or derivation. Fine 2006 (read in full) already allows
spacetime-location standpoints, each giving "its own reality" (p. 412), and
Lipman (2018, n. 1) notes single-event fragments after Stein. So the frame,
including event-indexing, is Fine's. What may be new is the *content* of the
fragments, fixed by a locality theorem as causal pasts (§3), the
classification of locally covariant standpoint frames (§2b), and the replies
below. Fine 2005 read (§§9–11): he rejects event standpoints on space/time
grounds (pp. 304–305) and calls event-perspectives "decidedly odd" without
argument (n. 36). Still unread: Lipman 2026 (chs. 4 and 6) and Iaquinto &
Torrengo 2022, ch. 4 "Relativity" (requested from the authors).

## 1. Thesis

Reality is fragmented by standpoints: what is real, present and past is a
matter of how things stand *from* an event. Relativity, together with a
locality principle, then fixes what each standpoint's fragment must be: its
causal past, undecided only at the light cone. There is no shared present, the
universe as a whole has no standpoint, and the totality of fragments is the
block. Presentists are right about how reality is from every standpoint;
eternalists are right that no standpoint is privileged and that the
standpoint-invariant facts are the tenseless causal geometry. Their dispute
looked unresolvable because both assumed a shared present, which locality
rules out.

## 2. The view: five principles

**P1. Standpoints.** For each event b there is a fragment F(b): the totality
of facts as they stand from b. Facts within a fragment are jointly coherent;
facts from different fragments need not be (Fine's non-standard realism).
[THESIS] A weaker, relativist reading ("facts obtain relative to standpoints,
and all standpoints are on a par") is available; the theorems below do not
depend on choosing.

**P2. Becoming is reality-from-a-standpoint.** "x has become for b" means
"x is real in F(b)". This relation is
- transitive: what is real for something real for b is real for b;
- chronologically inclusive: what lies in b's chronological past is real for
  b (Clifton and Hogarth derive this from worldline becoming and worldline
  transitivity).
[THESIS]

Why transitivity is not an extra assumption: read "x is real from b" as "x
has happened by b". If y has happened by b, and x had happened by y, then x
has happened by b; transitivity is part of what "having happened by" means.
Clifton and Hogarth's worldline transitivity says the same thing for
observers: two observers who meet agree on what has happened (pp. 362–363).
Denying it means that something can have happened by an event that has
happened by b without having happened by b, which is not a coherent notion of
becoming.

**P3. Locality.** Whether x is real from b's standpoint is settled by any
causally convex region containing x and b, by the same rule in every
spacetime. A standpoint is physical and local; no fact about b's fragment
turns on causally disconnected or distant structure. This is the "same theory
in all spacetimes" principle of locally covariant QFT and is akin to
Viglione's Causal Connection Condition. [THESIS, independently motivated]

What the theorem actually uses is weaker (checked against every appeal to
(LC) in the Stein paper): **(P3w)** one rule for every spacetime; invariance
under isometries; and, whenever a thin compact acausal slab Σ contains x and b
in its interior, the verdict on (x, b) depends only on int D(Σ) with its
geometry. D(Σ) is exactly the region whose physics is fixed by data on Σ. So
P3w says that *facts about what has happened supervene on the physics of any
region that determines the two events*. A physicalist about becoming can
hardly reject this. Someone who does reject it holds that whether x has
happened by b turns on goings-on outside every region that physically
determines x and b.

**P4. Non-triviality.** Not everything is real from every standpoint. If it
were, there would be no becoming, only the block. [THESIS]

**P5. Invariance.** The absolute facts are those that hold from every
standpoint. [THESIS]

**P6. Causal sufficiency.** Whatever can causally influence b is real from b.
This is Clifton and Hogarth's own maxim: "if an event ... can causally
influence b, that event must have become for b. Otherwise, how could an
unsettled, unreal, event for b possibly contribute to bringing about an event
that is settled for b, namely, b itself?" (1995, p. 364). Events on b's past
light cone can influence b by light signals, so P6 gives J^-(b) ⊆ F(b).
[THESIS] (Clifton and Hogarth also record a competing intuition, that null
lines might be ontologically on a par, and they suggest that intuition may be
the one to give up, ibid. pp. 364–365. Local fragmentalism gives it up.)

**P6′. Limit closure (an independent route to the same result).** Being real from b does not switch off at a limit: if
events x_n converge to x and each x_n is real from b, then x is real from b.
That is, each fragment F(b) is a closed set. (This pointwise closedness is
weaker than closedness of B_M in M×M, but it suffices: F(b) then contains the
closure of I^-(b), which is J^-(b) in globally hyperbolic spacetimes, so the
argument of Proposition 12 (Regularity) goes through.) This expresses that reality from a
standpoint has no gaps at its own boundary, and it agrees with Stein's
principle that whatever can causally influence b has become for b. [THESIS]

**P7. Extended standpoints (optional).** A region R may also count as a
standpoint, with fragment F(R) = ⋃_{b∈R} F(b). [THESIS; the view is stated
with and without it below]

## 2b. The formal frame

Lipman's standpoint logic (*J. Phil.* 2023, read in full) works with models
⟨D, W, R, v⟩: W ⊆ D are the standpoints, "w1Rw2 represents the claim that,
from the standpoint of w1, w2 is a standpoint", R is reflexive, v(w) ⊆ D
"represents entities that exist from the perspective of w", and "if w1Rw2 then
w2 ∈ v(w1)". Local fragmentalism is the following class of such models, one
for every globally hyperbolic spacetime M:

- D = W = the events of M (with P7, also its regions);
- v(b) = F(b), the events real from b;
- R(b, x) iff x ∈ v(b): from b, x is a standpoint just when it exists from b.

Lipman's constraint and the reflexivity of R hold by construction (b ∈ F(b)).
P2 adds transitivity of R and chronological inclusion; P3 says the assignment
M ↦ (W, R, v) is locally covariant. The Stein-GR theorem is then a
**classification of locally covariant standpoint frames**: every such family
that is non-universal on Minkowski spacetime has I^-(b) ⊆ v(b) ⊆ J^-(b) in
every spacetime, and with P6, v(b) = J^-(b) exactly. [PROVED, given the
identification; the identification itself is THESIS] This puts the physics
in the metaphysicians' own formalism, and it says what Lipman's framework
leaves open: which frames relativity permits.

## 3. What follows

**R1. Fragments are causal pasts.** In every globally hyperbolic spacetime,
I^-(b) ⊆ F(b) ⊆ J^-(b). [PROVED: Theorems 7 and 10 (main theorem; classification) of the paper, given P2–P4
as the axioms (CB), (T), (LC) and non-universality, plus the off-shell premise.]

**R2. There is no shared present.** Co-presence (each real for the other) is
trivial: from b, b alone is present. [PROVED corollary of R1: x ≤ b and
b ≤ x force x = b in causal spacetimes.] This is Stein's "pluralistic extreme
solipsism", now in every curved spacetime, and it is not solipsism about
reality: the whole causal past is real from b.

**R3. Fragments grow.** If b ≤ b', then F(b) ⊆ F(b'): along any worldline,
reality accrues. Becoming is real and directed. [PROVED from R1.]

**R4. The light cone is the only freedom.** Which lightlike-separated events
are real for b is not fixed. A rule may even let curvature along the light ray
decide. Requiring F(b) to be closed gives J^-(b), open gives I^-(b).
[PROVED: Theorems 10–11 and Proposition 12.] With P6 the freedom closes:
R1 gives F(b) ⊆ J^-(b) and P6 gives J^-(b) ⊆ F(b), so F(b) = J^-(b) exactly,
in every globally hyperbolic spacetime, with no dependence on curvature.
P6′ gives the same result by a topological route (Proposition 12). Two
independent principles, one causal and one topological, agree, which makes
the choice of J^- over I^- principled rather than chosen to exclude the
Weyl-gated rules. [PROVED given P6 or P6′] The view is thereby fully
determined: there is no remaining parameter.

**R5. The discrete case is exact.** In causal set theory, fragments are
exactly causal pasts, with no freedom. [PROVED: Proposition 19 (causal sets), using
non-manifoldlike posets.]

**R6. The universe has no present.** Without P7, the totality is not an
event and has no standpoint at all. With P7, the totality is a standpoint, and
its fragment is F(M) = ⋃_b J^-(b) = M: *the view from the whole is the block.*
Either way it has no present, since co-presence is defined among events and is
trivial (R2). [PROVED given P7's definition] This turns the "shape problem" of
the Brading paper (`paper/main.tex`), which asks what fixes the universe's
present, from an objection into a prediction: nothing does, because there is
none.

**R6′. The eternalist's standpoint is derived, not posited.** With P7, the
atemporal standpoint of Lipman's pluralist theory of time is recovered as the
totality's fragment, without adding a primitive atemporal standpoint. The
block is not an alternative to the fragments; it is their union, seen from
the whole. [PROVED given P7]

**R7. In Gödel universes fragmentation collapses.** In totally vicious
spacetimes every fragment is everything, and the view coincides with
eternalism. Locality isolates such universes, so this does not reach ours.
[PROVED: Proposition 20 (Gödel isolation); the "does not reach ours" part covers morphisms into
them only.]

**R8. A shared present costs locality or structure.** Any view with a shared,
extended present must either violate P3, using natural but non-local rules
such as cosmological time (Proposition 5), or add global structure such as a
preferred foliation or reference field (Monton's move). That inherits
Wüthrich's and Viglione's objections. [PROVED for the first horn; the second
is THESIS.]

**R9. Uniqueness.** Among views on which (i) reality is standpoint-relative
with events as standpoints, (ii) becoming is transitive and includes the
chronological past, (iii) the rule is local in the sense of P3w, (iv) becoming
is non-trivial, and (v) potential causes are real, there is exactly one: F(b)
= J^-(b). [PROVED given (i)–(v) and the off-shell premise of O4] Local fragmentalism is not one option among
many; it is what is left once those five commitments are made.

## 4. Why this resolves the divide

| Intuition | Where it is vindicated |
|---|---|
| The present is metaphysically special (presentism) | From every standpoint, its own present is the apex of reality; the future is not real from there (R1, R2) |
| Becoming is real and directed (growing block) | Fragments grow along worldlines (R3) |
| No moment is privileged (eternalism) | No standpoint is privileged (P1, P5) |
| Reality is the four-dimensional block (eternalism) | The union of fragments is the spacetime; the invariant facts are its causal geometry (P5, R6) |
| Relativity's lesson: no global now | There is no shared present at all (R2), and no foliation is used |
| Physics is tenseless | Tense lives in fragments; the laws state invariant facts |

**The diagnosis.** Three things cannot all hold together: locality, a shared
extended present, and non-trivial becoming [PROVED as R1/R2]. Presentists
kept the shared present; eternalists, seeing that relativity forbids it,
gave up becoming. Local fragmentalism keeps locality and becoming and gives up
only the *shared* present. That is the one element relativity has already
taken away.

## 5. Strongest replies to the obvious objections

**O1. "Fragmentalism is incoherent or too costly."** P1's relativist reading
avoids Fine's non-standard realism and still yields R1–R8. The red-team
question is whether the relativist reading still deserves the name
"resolution".

**O2. "This is eternalism with tensed vocabulary."** This is the deepest
objection. In the frame of §2b the disagreement becomes exact. The eternalist
holds that there is a single standpoint, or a privileged one, from which every
event exists. The presentist holds that only event standpoints exist and that
the future exists from none of them. Local fragmentalism (with P7) holds that
both kinds of standpoint exist: from every event, its future does not exist
(v(b) = J^-(b)); from the whole, everything does (v(M) = M). So each side is
right about the standpoints it recognizes and wrong to deny the other's. That
is a statable thesis about which standpoints exist and what they contain, not
a relabelling. It is also not "anything goes": the theorem fixes what each
event standpoint contains. Concession: the parties remain empirically
equivalent, and someone who denies that standpoints are part of reality at
all will see no difference.

**O3. "Locality begs the question against presentism."** It is motivated
independently: by locally covariant QFT, by Viglione's condition, and by the
fact that without it nothing at all is constrained (Proposition 4). Rejecting
it is coherent, but it means paying R8's costs.

**O4. "The off-shell premise."** Becoming is defined kinematically, as Stein's
and Clifton–Hogarth's are. The premise that one rule governs every
geometrically possible spacetime is a local cousin of Gödel's own modal
premise, that whether time lapses should not depend on "the particular way in
which matter and its motion are arranged in the world". Anyone who presses
Gödel's argument is committed to something stronger. The view needs only the
local version, which cannot reach out of Gödel universes (R7). Restricting
the rule to physically reasonable spacetimes is the open pocket problem;
energy conditions make it genuinely harder, not routinely true
(`research/stein-gr/ENERGY_CONDITIONS.md`). [OPEN]

**O5. "Transitivity and chronological inclusion are contestable"** (Sklar;
Clifton–Hogarth's own discussion). Drop either and Stein-type results
fail: anything goes. The view adopts them openly as what objective becoming
means.

**O6. "Quantum nonlocality."** Clifton and Hogarth argue that spacelike
causation would force universal becoming. The view inherits this. If
collapse is real and nonlocal, fragments may be forced to grow, possibly to
everything, which is eternalism. The view is hostage to quantum foundations,
and says so. But there is a live route out: Dieks's radical perspectivalism
(Found. Phys. 2025) gives a local, Lorentz-covariant account of EPR in which
perspectives "remain" independent "even when they make causal contact". Local
fragmentalism fits naturally with such no-collapse, perspectival readings.
[OPEN]

**O7. "Experience presents an extended now."** The specious present is a
duration along a worldline (the Arthur–Savitt diamond read as an experiential
window), not a co-reality class. Diamonds are not fragments.

**O8. "Denying the universe a present is a cost."** Only for views, like
Brading's, that need a present for the totality. Here it is a prediction (R6).

**O9. "Fine already said this."** Fine has the frame, including event
standpoints (2006, pp. 411–412). He rejects them on space/time grounds
(2005, pp. 304–305; see O11) and dismisses event-perspectives as "decidedly
odd" without argument (2005, n. 36). He never says what an event's reality
contains. The derivation (R1, §2b) and the general-relativistic reply to his
objection (O11b) are, as far as the sources read go, new. Lipman 2026 and
Iaquinto & Torrengo ch. 4 remain unread.

**O10. "Fragments must be coordinated somehow, and the coordination is brute"**
(Hofweber & Lange's objection to Fine, *Noûs* 2016: frame fragments leave the
Lorentz relations between fragments unexplained). Reply: local fragments are
not free-standing. They are coordinated by inclusion (F(b) ⊆ F(b') whenever
b ≤ b') and by a single shared causal geometry, which is itself the
standpoint-invariant content (P5). So the coordination is not brute; it is the
causal order. [THESIS; an advantage over frame fragmentalism, if it holds up.]

**O11. "Locational standpoints erase the difference between time and space."**
Fine's own objection, now read in full (Fine 2005, §10; self-archived
manuscript pp. 70–71, book pp. 304–305 on the anchor below): "One of the primary motivations for
the presentist view is that it enables one to distinguish between space and
time. Temporal indexicality is metaphysically significant, while spatial
indexicality is not; there is an objective 'now', even though there is no
objective 'here'. However, once we adopt the locational view, this asymmetry
between space and time disappears." Fine concludes that the "frame-theoretic
form of nonstandard realism constitutes the only reasonable way of reconciling
presentism with SR" (ibid., manuscript p. 72, book p. 306).

Reply, in two parts.
(a) Concession: on local fragmentalism the fragment of b is centred on b, so
"here" is as objective as "now"; Fine's asymmetry is *not* restored. What the
view gives instead is a different, structural asymmetry: displacement to the
future enlarges a fragment (F(b) ⊆ F(b') for b ≤ b'), while spatial displacement
yields fragments neither of which contains the other. Time is the direction in
which reality accrues; space is not. Whether that is enough for a tense
realist is a fair red-team question.
(b) The general-relativistic reply, which is the stronger one. Fine's argument
for frame fragments rests on special relativity having global inertial frames
("SR embodies enough of an asymmetry between space and time ...; one can simply
take ... temporal indexicality to be relativity to a frame-time pair"). A
generic curved spacetime has no global inertial frames. Frame-time standpoints
then require a foliation or reference field, which is added global structure
or, without it, non-locality (R8; Proposition 5 of the Stein paper). So in
general relativity Fine's preferred option is no longer free, and the
locational option is the only local one left. The Stein-GR theorem then fixes
what its fragments contain. [THESIS; (b) is the view's main contribution
relative to Fine]

(c) Fine's other remark on event standpoints is a dismissal without
argument. Footnote 36 (ms. p. 79, ≈ book pp. 310–311) reports Sprigge's view that
"every event must be present from its own point of view, and as it really is",
and continues: "the notion of each event having its own 'perspective' on
reality is decidedly odd; and I assume that there must be some more plausible
way in which one might accommodate the universal presentness of events within
our overall conception of what is real." Local fragmentalism is a candidate for
that "more plausible way": it says what an event's perspective contains (its
causal past, R1), and why that content is forced (locality). [THESIS]

Page numbers: the self-archived manuscript is reflowed, so there is no
constant offset to the book; see PAGE_MAP.md (ten anchors). Interpolated: the
asymmetry objection is book ≈ pp. 304–305 (ms. 69–71), matching Lipman's
report; the chauvinism argument ≈ pp. 301–302 (ms. 65); footnote 36 ≈ pp.
310–311 (ms. 79). Spot-check the print edition before quoting.

Note: Fine (n. 31) identifies the world-line/location framework as "essentially
the framework of Clifton & Hogarth [95]", and (n. 32) distinguishes his relation
of standpoint-equivalence from Putnam's "y is real for x". The relation B of the
Stein paper is of Putnam's kind; under local fragmentalism no two distinct
events are equivalent standpoints (J^-(x) = J^-(y) forces x = y in GH
spacetimes), consistent with Fine's negative result about equivalences.

**O12. "Fragmentalist passage is anaemic: from the totality of fragments
nothing moves"** (Andreoletti's review of Iaquinto & Torrengo 2022, *Organon F*
32 (2025), §3: "from a global perspective, reality (the totality of fragments)
features no passage at all"). Reply: passage is the growth of fragments along each worldline (R3), a
standpoint-internal fact. With P7, the view from the whole is the block
(R6′), and the block is indeed static: that is the eternalist's truth, and
the view grants it. What the objection wants is passage visible *from the
whole*. The view's answer is that passage is not the kind of fact that
obtains from the whole, just as "here" is not a fact from nowhere. The cost
remains for anyone who thinks real passage must be standpoint-independent.
[THESIS; a central red-team target alongside O2]

**O13. "Why not add an atemporal standpoint, as Lipman does?"** Lipman's
pluralist theory of time (*J. Phil.* 2023) reconciles the parties by positing
an atemporal standpoint from which the eternalist's picture is literally the
view, alongside temporal standpoints. That would answer O12 at once. Reply: with P7 we have it, and derived rather than posited. The totality's
fragment is the union of the event fragments, which is the block (R6′). So
local fragmentalism contains Lipman's atemporal standpoint as a consequence and
adds what his framework leaves open, namely what the temporal (here: event)
standpoints contain, fixed by physics (§2b). Without P7 the view instead
recovers the eternalist's truths as the facts invariant across all standpoints
(P5). [THESIS; P7 is the stronger version]

## 6. What is proved versus assumed

| Item | Status |
|---|---|
| Fragment = causal past up to the null boundary, in every GH spacetime | PROVED, given (LC), (T), (CB), non-universality and the off-shell premise |
| Trivial co-presence; fragment growth | PROVED corollaries |
| Null-boundary classification; regularity | PROVED |
| Causal sets, exact | PROVED (non-manifoldlike posets used) |
| Gödel isolation | PROVED (morphisms into M only) |
| Reading "has become" as "real from b" | THESIS (the bridge premise) |
| Fragmentalism or relativism about facts | THESIS |
| Locality as a metaphysical requirement | THESIS (independently motivated) |
| On-shell / energy-condition version | OPEN |
| Compatibility with quantum nonlocality | OPEN |
| Exact fragment F(b) = J^-(b) | PROVED given P6 (causal) or P6′ (topological) |
| Uniqueness among local standpoint views (R9) | PROVED given (i)–(v) and the off-shell premise |
| Locality needed only in the weak form P3w | CHECKED against every use of (LC) |
| Classification of locally covariant standpoint frames (§2b) | PROVED given the identification |
| View from the whole = block (R6′) | PROVED given P7 |
| Novelty against the fragmentalism literature | PARTLY CHECKED (Fine 2005/2006, Lipman 2018/2023, Hofweber–Lange, Savitt; Lipman 2026 and Iaquinto–Torrengo ch. 4 unread) |

## 7. Where to aim the red team

1. Is O2 fatal? Is there any content in "not real from b" beyond "not in b's
   causal past"?
2. Does the relativist reading of P1 dissolve the presentist's core claim
   rather than vindicate it?
3. Is P3 (locality) really independent of the conclusion, or does it smuggle
   in eternalist assumptions about which structure is fundamental?
4. P2's transitivity across standpoints: why should what is real for y, when y
   is real for b, be real for b? (Sklar-style worries; frame-hopping.)
5. R6: is "the universe has no standpoint" principled, or an ad hoc escape
   from Brading's problem?
6. O6: does quantum nonlocality collapse the view into eternalism?
7. Is the null-boundary choice (R4) a problem? A view whose fragments can
   depend on Weyl curvature at the light cone looks unprincipled unless
   regularity is motivated.
8. Priority: do Lipman 2026 (chs. 4, 6) or Iaquinto & Torrengo (ch. 4)
   already contain R1–R3 or §2b?
9. P6 rests on causal influence along light rays. Is a light-like influence
   enough for "having happened by", or should only timelike connections
   count (which would give I^-)?
11. P3w: can a defender of a shared present reject supervenience on domains
    of dependence without rejecting physicalism about becoming?
10. With P7, is the view just Lipman's pluralism with physics added? If so, is
    that a defect or the point?

## 8. Where the view sticks its neck out

These would count against it:

1. **A physically privileged foliation.** If physics turned out to have a
   preferred global time (a dynamical preferred frame, as in some quantum
   gravity proposals), P3's motivation would weaken and a shared present
   would come back on the table.
2. **Real nonlocal collapse.** If quantum state reduction is a physical,
   nonlocal process, Clifton and Hogarth's argument pushes fragments toward
   everything (O6). The view needs no-collapse or local readings.
3. **Locally definable spacelike co-reality.** Any well-motivated local
   relation of co-presence between spacelike-separated events would refute
   the view's premises, since R2 says there is none.
4. **Closed timelike curves in our universe.** In totally vicious regions
   fragments are everything (R7). A universe with such regions would make the
   view coincide with eternalism there.

None of these is currently supported, but each is the kind of physical result
that could tell against the view.
