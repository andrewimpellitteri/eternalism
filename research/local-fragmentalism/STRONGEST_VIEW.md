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
fragments, fixed by a locality theorem as causal pasts (§3), and the replies
below. Fine 2005 now read (§§9–11). Still unread: Lipman 2026 (chs. 4 and 6)
and Iaquinto & Torrengo 2022, ch. 4 "Relativity".

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

**P3. Locality.** Whether x is real from b's standpoint is settled by any
causally convex region containing x and b, by the same rule in every
spacetime. A standpoint is physical and local; no fact about b's fragment
turns on causally disconnected or distant structure. This is the "same theory
in all spacetimes" principle of locally covariant QFT and is akin to
Viglione's Causal Connection Condition. [THESIS, independently motivated]

**P4. Non-triviality.** Not everything is real from every standpoint. If it
were, there would be no becoming, only the block. [THESIS]

**P5. Invariance.** The absolute facts are those that hold from every
standpoint. [THESIS]

## 3. What follows

**R1. Fragments are causal pasts.** In every globally hyperbolic spacetime,
I^-(b) ⊆ F(b) ⊆ J^-(b). [PROVED: Theorems 7 and 8 of the paper, given P2–P4
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
[PROVED: Theorems 8–9 and Proposition 10.] The view's natural choice is
closed: whatever can causally influence b is real for b (Stein's "causal
becoming"). [THESIS]

**R5. The discrete case is exact.** In causal set theory, fragments are
exactly causal pasts, with no freedom. [PROVED: Proposition 17, using
non-manifoldlike posets.]

**R6. The universe has no standpoint.** The totality is not an event, so it
has no fragment and no present. The union of all fragments is the whole
spacetime. [CONDITIONAL on P1 restricting standpoints to events.] This turns
the "shape problem" of the Brading paper (`paper/main.tex`), which asks what
fixes the universe's present, from an objection into a prediction: nothing
does, because there is none.

**R7. In Gödel universes fragmentation collapses.** In totally vicious
spacetimes every fragment is everything, and the view coincides with
eternalism. Locality isolates such universes, so this does not reach ours.
[PROVED: Proposition 18; the "does not reach ours" part covers morphisms into
them only.]

**R8. A shared present costs locality or structure.** Any view with a shared,
extended present must either violate P3, using natural but non-local rules
such as cosmological time (Proposition 5), or add global structure such as a
preferred foliation or reference field (Monton's move). That inherits
Wüthrich's and Viglione's objections. [PROVED for the first horn; the second
is THESIS.]

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
objection. Reply: the view denies that there is a standpoint-free fact that
the future exists; the eternalist asserts it. Concession: the two are
empirically equivalent, and the difference lies in the status of
standpoint-free existence claims. The view's claim is that this is the *only*
remaining difference, and that it is the difference the debate was really
about.

**O3. "Locality begs the question against presentism."** It is motivated
independently: by locally covariant QFT, by Viglione's condition, and by the
fact that without it nothing at all is constrained (Proposition 4). Rejecting
it is coherent, but it means paying R8's costs.

**O4. "The off-shell premise."** Becoming is defined kinematically, as Stein's
and Clifton–Hogarth's are. Restricting it to physically reasonable spacetimes
is the open pocket problem. [OPEN]

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

**O9. "Fine already said this."** Possibly the frame; not, as far as we know,
the derivation. This must be audited before any novelty claim.

**O10. "Fragments must be coordinated somehow, and the coordination is brute"**
(Hofweber & Lange's objection to Fine, *Noûs* 2016: frame fragments leave the
Lorentz relations between fragments unexplained). Reply: local fragments are
not free-standing. They are coordinated by inclusion (F(b) ⊆ F(b') whenever
b ≤ b') and by a single shared causal geometry, which is itself the
standpoint-invariant content (P5). So the coordination is not brute; it is the
causal order. [THESIS; an advantage over frame fragmentalism, if it holds up.]

**O11. "Locational standpoints erase the difference between time and space."**
Fine's own objection, now read in full (Fine 2005, §10; self-archived
manuscript pp. 70–71, book pp. 304–305): "One of the primary motivations for
the presentist view is that it enables one to distinguish between space and
time. Temporal indexicality is metaphysically significant, while spatial
indexicality is not; there is an objective 'now', even though there is no
objective 'here'. However, once we adopt the locational view, this asymmetry
between space and time disappears." Fine concludes that the "frame-theoretic
form of nonstandard realism constitutes the only reasonable way of reconciling
presentism with SR" (ibid., manuscript p. 72).

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

Note: Fine (n. 31) identifies the world-line/location framework as "essentially
the framework of Clifton & Hogarth [95]", and (n. 32) distinguishes his relation
of standpoint-equivalence from Putnam's "y is real for x". The relation B of the
Stein paper is of Putnam's kind; under local fragmentalism no two distinct
events are equivalent standpoints (J^-(x) = J^-(y) forces x = y in GH
spacetimes), consistent with Fine's negative result about equivalences.

**O12. "Fragmentalist passage is anaemic: from the totality of fragments
nothing moves"** (Andreoletti's review of Iaquinto & Torrengo 2022, *Organon F*
32 (2025), §3: "from a global perspective, reality (the totality of fragments)
features no passage at all"). Reply: on this view there *is* no global
perspective (R6: the totality is not a standpoint), so the objection asks for
the view from a standpoint the view denies exists. Passage is the growth of
fragments along each worldline (R3), a standpoint-internal fact. The cost is
real, though: anyone who thinks passage must be visible "from outside" will
call this anaemic. [THESIS; a central red-team target alongside O2]

**O13. "Why not add an atemporal standpoint, as Lipman does?"** Lipman's
pluralist theory of time (*J. Phil.* 2023) reconciles the parties by positing
an atemporal standpoint from which the eternalist's picture is literally the
view, alongside temporal standpoints. That would answer O12 at once. Reply: an
atemporal standpoint is a standpoint of the totality, and R6 says the totality
has none; positing one reintroduces, at the level of standpoints, exactly the
non-local "view of the whole" that P3 excludes for becoming. Local
fragmentalism instead recovers the eternalist's truths as the facts invariant
across all standpoints (P5). This is a genuine choice point between the two
views, and the red team should press on it. [THESIS]

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
| Novelty against the fragmentalism literature | OPEN (unread) |

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
8. Priority: does Fine, or the fragmentalism-and-relativity literature,
   already contain R1–R3?
