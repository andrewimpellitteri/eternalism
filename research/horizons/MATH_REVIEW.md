# Referee report: "Horizons and Becoming" (research/horizons/main.tex, draft 25 Oct 2026)

Reviewer role: independent referee, mathematical relativity and modal logic.
Scope: every mathematical claim in main.tex, checked by my own derivation, plus
bibliographic spot checks. No project file other than this one was edited.

Read depth for sources I used:
- Minguzzi–Sánchez, gr-qc/0609119v3 (local text copy): full-text for the cited facts.
- Goldblatt 1980 (repo file `bf00370321.pdf`): full-text, pp. 219–220 only.
- Crossref and arXiv metadata: metadata only.
- Web search snippets: discovery only.

## Overall verdict

The core mathematics is correct. Theorem 1 (char) is proved soundly in both
directions. Lemma (balls), Propositions (conformal), (dust), (dot2) and (horizon)
are correct as stated, and the dust threshold at maximum expansion checks out.

Four statements need repair before circulation:
- the Cauchy corollary proves less than it states;
- one clause of Proposition (ds) is literally false;
- the Borde–Guth–Vilenkin (BGV) remark mischaracterizes the theorem;
- ".2 holding on a sub-domain" is not a well-defined modal claim.

The text also overstates novelty on the dust threshold: the vanishing of the
particle horizon at maximum expansion is classical cosmology. Several
abstract-level claims go further than the propositions prove. None of these
problems is fatal, and all can be repaired locally.

---

## MUST-FIX

### M1. The Corollary (cauchy) states more than its proof shows (lines 136–145)
The statement says "if I⁻(b) contains a Cauchy surface". The proof only treats a
level set S_c ⊆ I⁻(b), and an arbitrary Cauchy surface need not be a level set
of the chosen t. Proposition (dust) only uses the level-set case, but the
corollary as stated is unproved. It is true, though.

**Repair.** Keep the general statement and use the following direct proof. Let
S ⊆ I⁻(b) be Cauchy. Then M = I⁻(S) ∪ S ∪ I⁺(S) (MS2008, Def. 3.74 item 2).
- If x ∈ I⁻(S) ∪ S, then x ≤ s ≪ b for some s ∈ S, so x ∈ I⁻(b) by push-up.
- If x ∈ I⁺(S), extend any past-inextendible causal curve from x to an
  inextendible one. It meets S (Def. 3.74 item 3). It cannot meet S only to the
  future of x: then s′ ≪ x ≤ s for some s′, s ∈ S, which contradicts achronality.
  So the curve meets S ⊆ I⁻(b) in its past part.

The inner claim of the present proof (t(x) ≤ c implies x ∈ I⁻(b)) is correct.

### M2. Proposition (ds) contradicts the paper's own definitions (lines 339–355)
The paper defines G = ⋃_{s∈Γ} J⁻(s). For s = (η_s, N), J⁻(s) = {d(X,N) ≤ η_s − η}.
Since η_s < π/2 and the supremum is not attained,

  ⋃_s J⁻(s) = ⋃_s I⁻(s) = {d(X,N) < π/2 − η}.

So G is open and J⁻(Γ) has no null boundary inside it. The proof's own lemma
step shows that horizon points (d(X,N) + η = π/2) are not settled. Therefore:
- D = G exactly, not "up to its null boundary";
- M ∖ J⁻(Γ) = {d(X,N) ≥ π/2 − η} is closed, not open as stated, and contains
  the horizon.

**Repair.** State: "G = D = {d(X,N) < π/2 − η}, the shadow is
{d(X,N) ≥ π/2 − η}, and its interior {d(X,N) > π/2 − η} is nonempty."
Also replace η₋ in the proof by −π/2; η₋ is undefined in that context.

### M3. The BGV remark mischaracterizes the theorem (lines 291–295; conclusion 391–392)
BGV (PRL 90, 151301) show that a past-directed geodesic with positive averaged
expansion rate is past-incomplete. That is a statement about geodesic
incompleteness. It is not about whether conformal time is bounded below.

The standard BGV example cuts against the text. Flat-slicing de Sitter,
ds² = (Hη)⁻²(−dη² + dx²) with η ∈ (−∞, 0), has η₋ = −∞. On this patch, by the
paper's own Proposition (horizon) with η₋ = −∞, every pair of events has a
common past. Yet the patch is BGV-incomplete: past null geodesics reach η → −∞
at finite affine parameter, since ∫ dη/η² < ∞.

So BGV does not make "η₋ = −∞" doubtful. What BGV implies is that an inflating
patch is extendible or singular. Whether .2 holds then depends on the extension,
and the paper does not analyze it. A side check: in global de Sitter, which
extends that patch, .2 fails at every event by the same ball computation on S³.

**Repair.** Replace the sentence with: ".2 fails for every pair-region reaching
back to a finite conformal past boundary. If inflation is past-eternal in the
flat slicing, .2 holds within the inflating patch, but BGV shows that this patch
is past-incomplete. The verdict then depends on the spacetime before the patch,
which BGV does not fix."
Then soften "even with inflation, our standpoint logic is S4 without .2" to a
conditional claim, both here and in the conclusion.

---

## SHOULD-FIX

### S1. ".2 holding on a sub-domain" is not a modal-logic statement (lines 289–295, 391–392, abstract 42–43)
Validity of .2 is a property of a frame or of a point-generated subframe.

Take the observed region U, roughly J⁻(b) ∩ {η ≥ η_ls}. U is not R-closed, so it
generates no subframe. Even on the restricted frame (U, R|U), .2 fails after
inflation: the common past of two CMB points lies at η < η_ls, outside U.

What inflation secures is a relativized confluence condition: for all x, y ∈ U
there is some z ∈ M with z ≤ x and z ≤ y.

**Repair.** Define this condition explicitly, for example "U is confluent in M",
and use that phrase wherever the text says .2 is restored or holds on a
sub-domain.

### S2. "The horizon problem is this failure" overstates the identity (abstract 41–43; lines 283–290)
By Proposition (horizon), .2 fails at our standpoint whenever η₋ is finite. That
failure persists after inflation, which solves the horizon problem. So the
horizon problem is the failure of confluence restricted to observed pairs (S1).
It is not the failure of .2 at b, which is strictly stronger.

**Repair.** Abstract: "the cosmological horizon problem is the failure of this
confluence for the observed pairs; inflation repairs it there but not, without
further assumptions, for .2 itself."

### S3. The horizon-problem inequality: the factor is right; tighten the wording (lines 284–288)
With η₋ = 0:
- our past cone meets η = η_ls in a closed ball of comoving radius η₀ − η_ls,
  so the maximal separation is 2(η₀ − η_ls);
- by Proposition (horizon), two such points have a common past iff the
  separation is < 2η_ls.

So all such pairs share a past iff η₀ < 2η_ls. With η₀/η_ls roughly 50 in ΛCDM
(my estimate, not checked against a source), the condition fails by a large
factor, as claimed.

"Have a common past only if 2(η₀−η_ls) < 2η_ls" reads as a claim about every
pair. Say instead: "all such pairs have a common past iff η₀ < 2η_ls."

Optionally add the inflationary requirement that follows from the same formula:
η₋ < 2η_ls − η₀. It is monotone, so it also covers all observed pairs at later η.

### S4. The abstract's claim "in big-bang cosmologies .2 fails at every standpoint" covers more than is proved (line 41)
Proposition (horizon) proves only the spatially flat case. The claim is true for
FLRW with Σ = R³, S³ or H³ and finite η₋, and the same proof works:
- on any complete length space, closed balls B̄(X,r₁) and B̄(Y,r₂) meet iff
  d(X,Y) ≤ r₁ + r₂;
- J⁻(b) ∩ S_c contains a pair at distance min(2(η_b − c), diam Σ), which exceeds
  2(c − η₋) for c near η₋.

(Check: in closed dust the common-past condition is d(X,Y) < η_x + η_y, and .2
fails at every event, including after maximum expansion.)

**Repair.** Generalize the proposition in this way, or say "spatially flat" in
the abstract.

### S5. Proposition (horizon) needlessly assumes η₊ = ∞ (line 265)
The proof never uses η₊. ΛCDM, the paper's motivating "our universe", has finite
η₊, so as stated the proposition excludes it.

**Repair.** State the proposition for (η₋, η₊) × R³. Keep η₊ = ∞ only for the
remark that every pair has a common future (line 303). That remark is correct
for the half-space: take η_z large. It fails for finite η₊.

### S6. Theorem (char) assumes, without saying so, that t is onto R (lines 84, 109, 119)
If c lay outside t(M), then S_c = ∅ and the right-hand side would hold vacuously.
The proof also uses c_n → −∞.

Bernal–Sánchez do give t onto R. See MS2008 Thm 3.78, which gives the splitting
R × S with T the projection, and the remark after Def. 3.74 ("WLOG Cauchy
functions are onto").

The propositions, however, use η with a bounded range (η₋, η₊). The proof works
verbatim for any Cauchy temporal function if c ranges over t(M) and c_n → inf t.
The concatenated curve then has no past endpoint p, because t(p) = inf t would
not be attained.

**Repair.** Add "t: M → R onto (or: c ∈ t(M))". Note also that Set(b) does not
depend on the choice of t, which justifies using η.

### S7. The stated relation of Set(b) to Geroch's P(b) is inexact (lines 97–102)
In a globally hyperbolic spacetime, I⁻(x) ⊆ I⁻(b) iff x ∈ J⁻(b). Every
x ∈ J⁻(b) sends all its past timelike curves into I⁻(x) ⊆ I⁻(b). So the
timelike-curve version of Set(b) is exactly J⁻(b) ∪ P(b), not I⁻(b) ∪ P(b).

The causal version satisfies I⁻(b) ⊆ Set(b) ⊆ J⁻(b) ∪ P(b), and it can contain
points of ∂J⁻(b). In the Einstein static universe Set(b) = M includes b's past
null cone, which belongs to neither I⁻(b) nor P(b). I did not settle whether
P(b) ⊆ Set(b) in general. I found no counterexample: in the threshold case
η_b = η₋ + π, P(b) = ∅.

**Repair.** State the inclusions above instead of "Set(b) is I⁻(b) ∪ P(b)".

### S8. The dust threshold is a known cosmological fact under another name (lines 189–196, 227–228; prior-work notes)
Set(b) = M for η_b > η₋ + π holds exactly because I⁻(b) ⊇ S_c, that is, because
b's particle horizon has vanished. Cosmology texts already note that in closed
dust the particle horizon vanishes, and the whole universe becomes visible, at
maximum expansion (η = π), and that in closed radiation this happens only at the
crunch.

I saw this at discovery depth in Grøn & Johannesen, arXiv:1103.4753 (also
0911.3310), and in "A Thousand Problems in Cosmology: Horizons", arXiv:1310.6329.
Rindler 1956 likely discusses closed models too (not checked).

**Repair.** Cite these sources. Say that the geometric threshold is known, and
that what is new is its reading as a settledness transition through
Theorem (char). Revise "We have not found the dust threshold at maximum
expansion" accordingly.

### S9. "There, and only there, an eternalist and a standpoint-first ontology disagree" is conditional (abstract 46–47; §5)
The claim depends on three bridge premises:
- standpoints are exactly the events on matter worldlines;
- the laws carry only domain-of-dependence information;
- the standpoint-first ontology counts settled-but-unreal events (D ∖ G) as
  factual.

The last premise is itself contestable. In de Sitter D = G, but elsewhere
D ∖ G can be nonempty.

**Repair.** Add "under these premises" to the abstract, and state the D ∖ G
stipulation explicitly. This matches the project rule separating physical,
mathematical and bridge premises.

### S10. "Settled" versus "real" when F(b) = J⁻(b) (lines 102–106)
Under the companion's signal principle, F(b) = J⁻(b). But with the I⁻-based
definition, Set(b) ⊉ J⁻(b) in Minkowski: events on b's past null cone are real
from b without being "settled" from b. The text calls this a feature, but a
reader will see a mismatch with "settled ⊇ real".

**Repair.** Note this explicitly. Either define settledness relative to F(b), or
say why the open I⁻(b) is the right base. A good reason: the compactness in
Theorem (char) needs it, and the J⁻ version changes the characterization.

### S11. "Half of global de Sitter" needs a precise sense (lines 47–48, 357)
It can be made precise. The time-reversing isometry σ(η,X) = (−η, −X) maps
{d(X,N) < π/2 − η} onto {d(X,N) > π/2 − η}. So M = G ⊔ H ⊔ σ(G), where H is the
null horizon.

**Repair.** Say this. Two further remarks strengthen the proposition and could
be added:
- de Sitter isometries act transitively on timelike geodesics, so Γ may be
  taken at the pole without loss of generality;
- any inextendible causal curve in global de Sitter ends at a single point P of
  I⁺, since X(η) is 1-Lipschitz. So the same result, G = {d(X,P) < π/2 − η},
  holds for every single observer, accelerated or not.

---

## OPTIONAL

- **O1** (line 174). The parenthetical "(on S³ the bound η₊−η₋≤π keeps
  η_b−η_x<π)" suggests that the chronology criterion needs the bound. It does
  not: x ≪ b iff d(X,Y) < η_b − η_x holds on the full static product for any
  range. The bound is needed only so that r₂ = η_b − c ≤ π in the Lemma. Move
  the parenthetical there.
- **O2** (Lemma, 150–164). The lemma is correct, including the edge cases X = Y,
  r₁ ≥ π, and d + r₁ = π. In the last case the extended geodesic has length π
  and is still minimizing, ending at −Y. In the propositions r₂ = η_b − c may be
  ≤ 0, giving an empty open ball. The lemma remains true there, but say
  "r₁ ≥ 0, r₂ ∈ R".
- **O3** (line 352). The phrase "applies with an open past set" is correct. The
  proof uses only that U is open (so K_c is compact) and that J⁻(U) ⊆ U (push-up
  for the segments). Every open U with I⁻(U) = U satisfies the second condition.
  State this as "Theorem (char) holds for any open past set U in place of I⁻(b)"
  and cite it in Proposition (ds).
- **O4** (lines 93–96). Theorem (char) supplies the physics bridge: if
  J⁻(x) ∩ S_c ⊆ I⁻(b), then x ∈ D⁺(S_c ∩ I⁻(b)), an open piece of a Cauchy
  surface. That is the hypothesis under which hyperbolic PDE uniqueness applies.
  Say so.
- **O5** (line 242). .2 corresponds to Church–Rosser convergence on all frames
  (it is a Sahlqvist formula), and locally at a point. The restriction to
  reflexive transitive frames is unnecessary. Add a BdRV locator. Goldblatt
  (pp. 219–220, read) also states S4.2 for 2D and 3D Minkowski, and states that
  restricting to timelike signals changes nothing.
- **O6** (lines 81–84). Add MS2008 locators:
  - push-up: the statement before Prop. 2.17, refined in Prop. 2.31;
  - J⁺ closed: Remark 3.66(2) and Thm 3.69;
  - J±(K) ∩ S compact: Def. 3.74 item 4;
  - splitting: Thm 3.78.
- **O7** (lines 223–225). Per the prior-work notes, Geroch stated the
  compact-slice claim as a corollary. Hogarth 1993 showed it false as stated,
  and Manchak proved a corrected version. "Conjectured" may misdescribe this.
  Align with Manchak's footnote 8 and cite Hogarth 1993.
- **O8** (line 382). A Schwarzschild–de Sitter spacetime with compact slices
  needs a second mass (its global structure is periodic). "The same horizon
  structure appears" holds qualitatively, but the size of the shadow changes.
- **O9** (line 182). Proposition (conformal) also covers open FLRW (Σ = H³): the
  Lemma holds on any complete, uniquely geodesic, geodesically complete space.
- **O10** (lines 318, 369). Check that Earman 2008 actually makes the
  "fragments cover M and fix the geometry" point and discusses observational
  indistinguishability. I did not verify either.
- **O11.** The proofs of Theorem (char) are otherwise airtight. Checked points:
  - K_c is compact (closed subset of the compact J⁻(x) ∩ S_c);
  - P_n is closed in a compact product because ≤ is closed;
  - P_n is nonempty by the crossing-plus-push-up argument;
  - the inverse limit of nonempty compact Hausdorff spaces is nonempty, and the
    bonding maps need not be surjective;
  - the infinite concatenation is locally finite on [0,∞), so it is a
    continuous, locally Lipschitz causal curve;
  - it has no past endpoint because t → −∞ along it;
  - each segment avoids I⁻(b) by push-up;
  - c < t(x) is necessary (for c > t(x) the condition is vacuous) and sufficient.

---

## Item-by-item verification summary

1. **Theorem (char).** Correct in both directions; see O11. Needs t onto R or
   c ∈ t(M) (S6).
2. **Corollary (cauchy).** The level-set case is correct, including "t(x) ≤ c
   implies x ∈ I⁻(b)". The general Cauchy-surface case is unproved but true;
   M1 gives the fix.
3. **Lemma (balls).** Correct on R³ and on S³ with r₂ ≤ π, including all edge
   cases.
4. **Proposition (conformal).** Correct, and the settled set is conformally
   invariant. Two models check out:
   - closed radiation: a'' = −a gives a = a₀ sin η on (0, π), a range of π;
   - global de Sitter: a = 1/cos η on (−π/2, π/2), a range of π.
5. **Proposition (dust).** Correct.
   - Closed dust: a = (a_m/2)(1 − cos η) on (0, 2π), with maximum at η = π.
   - At exactly η_b = π, Set(b) = I⁻(b).
   - Einstein static: Set = M, which duplicates Geroch Fig. 5.
   - Novelty: S8.
6. **Section 4.**
   - The .2-directedness correspondence is correct (O5).
   - Proposition (dot2) is correct.
   - The common-past criterion |X−Y| < η_x + η_y − 2η₋ is correct; strictness
     comes from the supremum over c > η₋.
   - .2 fails at every event, and holds when η₋ = −∞.
   - The factor in the horizon inequality is correct (S3).
   - BGV is mischaracterized (M3).
   - Common future for every pair is correct in the half-space only (S5).
7. **Proposition (ds).** ⋃I⁻(s) = {d < π/2 − η} is correct, and its boundary is
   the Gibbons–Hawking event horizon (the past cone of Γ's endpoint on I⁺).
   - The generalization of Theorem (char) is correct (O3).
   - The statement's wording is wrong (M2).
   - "Half" is right in the isometric sense (S11).
8. **Overclaims.** In the abstract and conclusion: S1, S2, S4, S9, and the
   conditionality in M3. Also, "nothing outside an event's causal past is
   settled" is true but weaker than proved: nothing outside the chronological
   past is settled.
9. **Bibliography.**
   - Verified through Crossref metadata:
     - BGV, PRL 90 (2003) 151301;
     - Bernal–Sánchez, CMP 257 (2005) 43–50;
     - Goldblatt, Studia Logica 39 (1980) 219–236, DOI 10.1007/BF00370321;
       content also read, pp. 219–220;
     - Gibbons–Hawking, PRD 15 (1977) 2738–2751;
     - Guth, PRD 23 (1981) 347–356;
     - Rindler, MNRAS 116 (1956) 662–677, DOI 10.1093/mnras/116.6.662;
       reprinted in GRG 34 (2002) 133–153;
     - Earman, ISPS 22 (2008) 135–164;
     - Clifton–Hogarth, Synthese 103 (1995) 355–387;
     - Stein, J. Phil. 65 (1968) 5–23;
     - Stein, Phil. Sci. 58 (1991) 147–167;
     - Manchak, Found. Phys. 38 (2008) 317–321.
   - Verified through arXiv metadata:
     - MS2008 pp. 299–358 (journal-ref);
     - Lewis & van der Schaaf, arXiv:2601.14029v2. The authors are Marco Lewis
       and Nesta van der Schaaf; the prior-work notes name only van der Schaaf.
       Published in Proc. AiML 2026, EPTCS 447, pp. 584–602; add this;
     - Lesourd, arXiv:2101.08324v1, title and author.
   - Not verified:
     - Geroch pp. 81–93 and Malament pp. 61–80. These are only consistent with
       the project's scan, in which Malament's tail precedes Geroch at p. 81.
     - BdRV and HE1973. These are standard books; their details are correct to
       my knowledge, but no locator is given.

Sources (discovery level, for S8):
- [Grøn & Johannesen, arXiv:1103.4753](https://arxiv.org/pdf/1103.4753)
- [Grøn & Johannesen, arXiv:0911.3310](https://arxiv.org/pdf/0911.3310)
- [A Thousand Problems in Cosmology: Horizons, arXiv:1310.6329](https://arxiv.org/pdf/1310.6329)
