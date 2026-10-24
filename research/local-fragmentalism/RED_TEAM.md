# Red team: local fragmentalism

24 October 2026. Adversarial review of STRONGEST_VIEW.md (229-line version,
with O10/O11 and the Dieks route) and its backing paper
`research/stein-gr/main.tex` (13 pp., builds cleanly, second-review fixes
verified present: flat-data conclusion is now ℝ×Σ "not Minkowski in general;
e.g. Σ = T³" in Proposition 19; the Milne-wedge locality failure is proved
directly in Proposition 5; Gödel isolation is self-contained and honestly
scoped to morphisms into M; Wüthrich–Callender is softened to what is shown).

Every [PROVED] tag was checked against the paper's numbered results: Prop 4,
Prop 5, Thm 7, Thm 8, Thm 9, Prop 10, Prop 17, Prop 18 all exist and say what
the view claims. No mathematical errors found. The attacks below are
philosophical; none breaks a theorem. A previous red-team pass on the
computational artifacts (countermodel N(H) fix, coordination and gate probes)
is recorded in `research/redteam/math-audit/` and
`research/redteam/infra-redteam/`.

## A. The fragment is a growing block, not presentism (§1, table row 1)

F(b) ⊇ I⁻(b): the whole causal past is real from b. Presentism says the past
is unreal. So §1's "From every standpoint, presentism's picture holds" and
table row 1 misdescribe the view's own fragments. What holds from every
standpoint is a growing block with a pointed apex — §1's own next clause
("reality grows along each worldline") is growing-block talk. The paper's
Limits paragraph agrees: the theorem "does not decide between presentism, the
growing block and eternalism."

Note the tension this creates with O11: the fact that kills the presentism
claim (the timelike past is real from b) is exactly the fact that answers
Fine's space/time asymmetry objection. Keep O11's reply; fix §1 and row 1 to
"presentism's negative claim (the future is not real from a standpoint)" and
give the growing block its row honestly.

## B. Target 1 / O2: what "not real from b" adds, and what it does not

Extensionally, after R1, "not real from b" is exhausted by "not in b's chosen
causal past" (boundary rule aside). The residual content is threefold:

1. Quantifier discipline: no standpoint-free existentials.
2. Context-dependence: (LC) makes B a theory over the category GH, so the same
   b has different fragments in different spacetimes. The eternalist's "x
   exists" has no such dependence. This is real content.
3. A semantic thesis about what the debate was about.

The eternalist can accept R1–R8 in full as a theory of *determinacy* (Stein
1968 already gives "nothing outside J⁻(b) is settled for b" in Minkowski) and
add the unprefixed quantifier. Against that eternalist, the view's only unique
claim is that the unprefixed quantifier is illegitimate — which is Fine's
move, not a consequence of physics. Correct slogan: **relativity plus locality
derives the fragment geometry; nothing derives fragmentalism.** The paper
respects this limit; §1's "locality rules that out" rhetoric and the diagnosis
paragraph occasionally do not. Available defense, worth stating in the
document: the view's own meta-facts (the fragment structure) are invariant
causal geometry under P5, so the relativist reading is self-consistent — the
view replaces the absolute-existence question rather than answering it.

## C. O6 / target 6: upgrade "hostage" to a trilemma, and add the P5-correlations gap

The Dieks 2025 route (now cited) is real; radical perspectivalism is the
Everett-side escape. Make the full trilemma explicit: Everett keeps P3 (cost:
indexical outcomes — congenial, since standpoint-relative fragments mirror
self-location); Bohm needs a preferred foliation, i.e. R8's second horn, the
very move R8 taxes the presentist with; objective collapse makes spacelike
becoming real, Clifton–Hogarth fires, R1 dies. Sharper than O6 as stated:
under P3 + P5, **EPR correlations are not absolute facts.** A standpoint whose
past holds one wing cannot hold the correlation fact (P3), so by P5 it is not
standpoint-invariant. Dieks's perspectivalism answers the EPR side; the view
still owes an account of how invariant Born-rule statistics emerge from
fragment-relative correlation facts. That is a concrete open problem and
belongs in §6 as OPEN, not inside "hostage."

## D. Target 3: P3 equivocates between law-locality and fact-locality

As written, P3 ("no fact about b's fragment turns on causally disconnected or
distant structure") is refuted as a general physical principle by
Aharonov–Bohm: the interference fact at b is settled by flux in the excluded
region — global holonomy, in no causally convex region with b. LCQFT's actual
principle is law-locality (local algebras, local dynamics). R1 needs only
becoming-fact locality; the formal (LC) is fine and correctly rules out
holonomy-sensitive becoming. But the metaphysical justification is analogy,
not independence, and Viglione's CCC is a condition on becoming relations, not
an independent physical principle. Reword P3: "whether x has become for b is
settled only by local structure."

## E. Target 5: R6 is a framework limit, not a prediction

(LC) quantifies over points; B is a point-relation from the start, so the
universe was never a candidate standpoint. R6 is conditional on
standpoints-are-events in a strong sense: Brading can reject that ontology at
exactly the price Monton pays for a foliation. The strongest available defense
is not in the document: a standpoint must bear the "real-from" relation; (LC)
makes that relation local; so only spacetime locations can bear it. That is a
derivation-shaped argument, but it is physicalism about perspectives and
should be a tagged premise, not silently assumed.

## F. Target 4: transitivity is answered, but it costs Fine-membership

Frame-hopping dissolves: once R1 is in place, "real for" is fragment
inclusion, not perspective-mixing, and monotonicity is a theorem (verified by
hand through both the chronological and horismotic cases, via the MS 2.31
facts and (NC); note the paper states neither R2 nor R3 — the corollary
environment is declared and never used. Add them; two lines each). The cost:
Fine's fragments are compatibility classes, not inclusion-ordered; co-real
closure is what he denies. Local fragmentalism's fragments form a causal
tree — structurally alien to Fine's frame/compatibility fragments (PRIOR_WORK
now confirms the textual side: Fine's fragments are frame-times). That
ordering is simultaneously the novelty claim (it is what answers Hofweber–Lange
in O10: coordination by inclusion is not brute) and the reason a Fine-ist can
deny the view is fragmentalism at all. Say this openly; it is the view's
identity question.

## G. Remaining targets

- Target 2: yes — the relativist reading vindicates each side by
  relativizing what each side asserted unrelativized. "Resolves the divide"
  should read "replaces the question" (see B).
- Target 7: the closed choice (J⁻) has an unused argument — explanatory
  closure: under I⁻, b's present state is causally explained by events (the
  emission of incoming light) that are unreal from b. Use it. Prop 10 vs
  Thm 9 shows regularity, not locality, picks the endpoint; say so plainly.
- Target 8 / priority: PRIOR_WORK.md has done the sweep; this review
  independently agrees with its verdict — Fine's fragments are frame-based,
  and no checked source derives causal-past fragments from a locality theorem
  across spacetimes. Remaining unread risks are the three PRIOR_WORK lists:
  Fine 2005 pp. 304–305 in direct text, the 2026 *Standpoints* chapter,
  Iaquinto–Torrengo's SR chapter.

## Fixes

1. §1 and table row 1: replace "presentism's picture" with the pointed
   growing block; keep the future-unreality vindication (A).
2. R1's tag: (CB) + Theorem 7 gives R1; Theorem 8 backs R4, not R1.
3. Add the two corollaries (trivial co-presence; growth) to the paper so the
   [PROVED corollary] tags point at stated results.
4. P3 rewording (D).
5. O6: add the trilemma and the P5-correlations open problem (C).
6. O11: once Fine 2005 pp. 304–305 is read directly, note that the reply and
   fix A trade on the same fact (past real from b) — the view answers Fine's
   asymmetry demand and abandons presentism's picture in one move; present
   that as one honest package.

## Scope

Read: STRONGEST_VIEW.md (current version), PRIOR_WORK.md, the full paper, and
the cited proof sections. Spot-checked the main theorem's differential
geometry (lemmas R, E, B, C, D, F read; not independently re-derived line by
line). Unverified: any claim here that rests on memory of the Fine/Lipman/
Iaquinto literature rather than the recorded read depths in PRIOR_WORK.md.
