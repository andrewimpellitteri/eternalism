# Second-pass report: trilemma revision at `0f09900`

Audit of `paper/main.tex` at commit `0f09900` (509 lines; compiled from a copy
to 9 pages, no unresolved references, no overfull boxes). This pass checks only
the five repairs requested; it does not re-audit the whole paper. Line numbers
are those of `0f09900`.

**Verdict.** Four of the five repairs are substantially adequate; the T1 repair
is adequate in form but its defence of T1b is not yet adequate to the text. The
note is close to publishable as a specialist note, but it still needs a short
revision: the trilemma’s exhaustiveness claim has a real gap (the “no present /
not a dynamical system” case), and horn (4) conflates two different exits. Those
are load-bearing for the central claim, so this is not yet copy-editing.

---

## 1. T1: internal premise, T1a/T1b separation

**Adequate in form; the defence of T1b is honest but incomplete.**

The paper now does what the first pass asked:

- It calls the “insofar as” a genuine conditional and says the identification is
  “a working premise of her argument, not a theorem” (l. 122–129).
- It states “This note therefore grants it” (l. 129) and repeats the grant in
  the abstract (l. 24–26) and §8 (l. 445–451).
- It separates the identification (T1a) from the claim that the universe is a
  genuine unity (T1b): l. 133–139 for the first, l. 153–163 for the second.
- It distinguishes scope from verdict: “Brading’s scope claim … gives the
  principle’s intended scope, not the verdict that the universe satisfies it”
  (l. 134–137). That is exactly the first-pass point.

The T1b defence uses the right texts: 2013 p. 1110 (“The dynamics grounds the
unity of what there is, both of the parts and of the whole (consisting of
interacting parts)”, l. 142–143), 2013 p. 1105 n. 3 (“the totality of existing
things”, “applies to all three”, l. 146–151), and the isolation/conservation
condition (2013 p. 1105; 2015 p. 16; l. 153–158). It also marks the inference as
an argument, not a quotation, and says “a reader may resist” (l. 159–161). That
is the right register.

**Residual weakness.** The p. 1110 quote has the qualifier “consisting of
interacting parts,” and the paper does not discuss it. The universe may contain
parts that never interact; if the “whole” whose unity the dynamics grounds is
the interacting whole, it may not be the material universe as a whole. The
paper’s answer is that the universe is “the limiting case of an isolated
system: there is no external interaction by definition” (l. 158–159). A referee
will say that is precisely the problem: isolation from external interactions is
vacuous for the universe, and a vacuous condition cannot ground a substantive
unity. The paper concedes that the premise is interpretive and makes the fourth
horn the fallback, which contains the damage. But it should either (i) argue
that the universe is an interacting whole (e.g. via gravity/cosmology), or
(ii) explicitly say the p. 1110 quote is not decisive and that T1b is a
reconstruction, not a textual verdict. As written, it says the texts “support
but do not compel” (l. 161–162), which is honest, but the “support” is weaker
than the section implies because the “interacting” qualifier is left untouched.

So: **adequate as a conditional premise, not yet adequate as a defence of the
text.** This is a residual weakness, not a fatal defect, because the trilemma is
explicitly conditional on T1b.

---

## 2. T4: the trilemma instead of `W`

**Substantially adequate; one exhaustiveness gap and one catch-all remain.**

The paper no longer asserts that the universe’s sustaining region is `W`. §3 is
now an explicit four-option structure:

- horn (1): `W` (l. 179–187);
- horn (2): proper global — Cauchy slice or thick slab (l. 189–202);
- horn (3): proper local patch (l. 204–214);
- horn (4): outside the domain (l. 216–222).

The “spatially global present **common to all systems**” qualifier is now quoted
and discussed: “The qualifier ‘common to all systems’ leaves room for a global
present for the universe alone … But the second clause rejects a spatially
global present without that qualifier. At a minimum, Brading owes an account of
why the universe’s global slice is not the global present she rejects”
(l. 194–202). That is exactly the first-pass repair.

“Local” is disambiguated: Brading’s sense is “any present that is a proper part
of the block,” while the paper uses the narrower sense “a proper region that is
not spatially global” (l. 173–177). The earlier equivocation is gone.

The conclusion is conditional: “P1\*\* cannot be both universal and satisfied by
the universe without an account of the universe’s sustaining region that
Brading does not supply” (l. 232–237). The note explicitly says it does not
claim that no such account can be given (l. 235–237; l. 453–465). Good.

**Remaining gap 1: the “no present / not a dynamical system” case.** The
trilemma assumes that if the universe is in the domain, it has a present with an
extent. At l. 167–169 the paper moves directly from “Grant the two premises” to
“What is the spatiotemporal extent of the universe’s present?” But Brading’s
present is the region needed to sustain a *dynamical system*. If the universe is
a genuine unity but not a dynamical system in the relevant sense — no
system/environment distinction, no external interactions, no parameter of
evolution — it may have no sustaining region at all. P1\*\* says every existing
thing exists only presently, but it does not follow that every existing thing
has a well-defined present extent; that is a further premise of Brading’s
account. The four horns do not include “in the domain but no present.” The
exhaustiveness claim at l. 224–226 (“either it is in the domain and its present
is `W`, proper global, or proper local; or it is not in the domain”) therefore
fails. This is the strongest remaining defect. Fix: add a horn (0) “the universe
has no present / is not a dynamical system” and say whether it is a version of
horn (4) or a distinct cost; or argue that P1\*\*’s “exists only presently”
guarantees a present for every thing in the domain.

**Remaining gap 2: horn (3) is a catch-all with a patch-only cost.** “Local” is
defined negatively as any proper region that is not spatially global
(l. 174–177). But the cost argument at l. 204–214 only covers “a local patch”
whose laws determine the rest. A proper non-global region need not be a patch:
it could be a disconnected union of patches, a past light cone, a region that is
spatially global in one direction but not another, or a region with holes. The
paper’s “four horns are exhaustive” is true by stipulation (every proper region
is either spatially global or not), but the claim that **each horn has a cost**
is not established for the whole of horn (3). Define the horns by the kind of
sustaining account (whole history / global data / local data / no domain) rather
than by region shape, or add a sub-case for “non-global, non-patch proper
region” and say why it collapses to the patch case or is unaccounted. This is
load-bearing for the “each has a cost” conclusion, though less so than gap 1.

---

## 3. The 2013/2015 criticism

**Adequate.** The reframing is exactly right.

- The section now says the 2013 condition “describes a different scenario”
  (l. 241), not “makes the same point in a different form.”
- It treats “for whatever system we try to consider” as a universal quantifier,
  says the “in other words” is valid in that direction but not an equivalence
  (l. 253–257). That is the correct logical point.
- It says “That is not a logical defect in a sufficient condition. It is a gap
  in the framing” (l. 262–263). That is the first-pass repair.
- It quotes “the crucial question” (2015 p. 18; l. 268–272) and “A great deal
  rests…” (2013 p. 1110; l. 275–277). Good.
- It distinguishes universal / universe-own-region / subsystem-only scenarios
  (l. 286–295) and says the empirical question decides (1) vs (3), not (2)
  (l. 297–298). The three-way distinction is the right one.

Minor: “Brading’s empirical question decides between (1) and (3)” (l. 297) is
slightly loose. The empirical question decides whether (1) holds (no genuine
subsystems) and whether (3) is available (subsystems, universe excluded). It
does not “decide between” them; (2) remains compatible with subsystems. The
next sentence says (2) is not decided, so the point is clear. No fix needed
beyond “decides whether (1) holds and whether (3) is available.”

---

## 4. The four-event model

**Adequate.** The model now states its assumptions explicitly:

- “the model is set-theoretic, not dynamical … It models the extensional shadow
  of (a) and (b)” (l. 349–351);
- “`less than` is an extent comparison, and `⊊` is a regimenting choice; it
  assumes containment” (l. 351–353);
- “the model uses a common event domain `W`” and 2013 n. 7 denies determinate
  ontological spatiotemporal relations (l. 353–362). It quotes n. 7 and says
  “the model therefore treats `W` as the common epistemic representation … If no
  common representation is allowed, the model is a result about the
  representation, not about the ontology” (l. 358–362).

It also calls the model “a burden-shift, not a refutation of Brading’s
dynamics” (l. 369–370). That is the right scope.

**Residual point.** The n. 7 caveat is stated only for the coverage model. The
trilemma’s horns (1)–(3) are also framed in terms of `W` and the “spatiotemporal
extent” of the universe’s present. If `W` is the epistemic representation, the
trilemma is a result about the representation, not the ontology. The paper
should either extend the n. 7 caveat to the trilemma (“the trilemma is stated in
the common epistemic frame”) or defend `W` as the common frame for the trilemma
too. This is a conceptual issue, not a defect in the model itself. A referee who
knows 2013 n. 7 will ask why the same caveat does not apply to horns (1)–(3).

Minor: the abstract says the model “shows that … (a) and (b) do not imply a
proper union” (l. 39–40) without the “on the extensional reading” qualifier. The
body has it; the abstract should too.

---

## 5. “Scale-general”

**Adequate.** The section is now accurate:

- “Nor is the criterion literally scale-free” (l. 383–384).
- It quotes 2013 n. 3 in full, including “different principles of unity might be
  used for the different cases” and “applies to all three” (l. 384–389).
- It acknowledges the dynamical selection procedure: “as picked out by the
  dynamical laws” (2015 p. 18) and the isolation/conservation condition (2013
  p. 1105) (l. 391–396).
- It states the missing premise as “a guarantee that the procedure selects a
  proper subsystem rather than the maximal unity” (l. 396–401) and “a
  scale-selection guarantee, or an account of the maximal unity’s present”
  (l. 403–405). That is the first-pass repair.

Minor: “Scale-generality is enough to generate the trilemma” (l. 391) is a non
sequitur. The trilemma is generated by T1b (the universe is a candidate genuine
unity), not by scale-generality. Scale-generality explains why the criterion
does not by itself select a local scale; it is a diagnosis, not a premise. Say
“scale-generality explains why the trilemma is not resolved by the criterion
alone” rather than “enough to generate.” Not load-bearing.

---

## 6. Remaining load-bearing defects

1. **Horn (4) conflates two exits (l. 216–222, l. 162–163, l. 224–230).** The
   text says: “If the universe is not a genuine unity, or if ‘thing’ is a term
   of art for proper unities below the whole, then P1\*\* does not apply to it.
   This avoids the trilemma by restricting the quantifier. Its cost is the
   global claim.” Those are two different exits:
   - (4a) the universe is not a genuine unity. Under the granted identification,
     it is then not an existing thing, so P1\*\* does not apply because there is
     no thing to quantify over. The cost is not “the global claim”; it is that
     the universe does not exist.
   - (4b) the universe is a unity but “thing” is a term of art that excludes the
     totality. The cost is the restriction of the quantifier and the loss of the
     global claim.

   The paper also says at l. 162–163: “If the premise is rejected, the universe
   falls outside the domain, which is the fourth horn.” That is (4a), not (4b).
   The horn’s cost analysis only fits (4b). Split (4a)/(4b); the exhaustiveness
   claim at l. 224–230 and the conclusion at l. 484–490 depend on it.

2. **The “no present / not a dynamical system” case is missing (l. 167–169,
   l. 224–226).** As in §2 above. The trilemma assumes in-domain → has a
   present. Add horn (0) or argue the assumption. This is the most serious
   remaining gap in the exhaustiveness claim.

3. **Horn (3) is a catch-all with a patch-only cost (l. 173–177, l. 204–214).**
   As in §2 above. The cost argument does not cover every proper non-global
   region. Define the horns by kind of sustaining account, or add a sub-case.

4. **The n. 7 caveat is not extended to the trilemma (l. 354–362 vs
   l. 179–214).** If `W` is epistemic for the coverage model, it is epistemic for
   the trilemma too. Either extend the caveat or defend `W` as the common frame.

These are load-bearing for the central claim “the four horns are exhaustive and
each has a cost.” They are local fixes, not a structural rewrite.

---

## 7. Presentational issue: “trilemma” with four horns

The title and abstract call the result a “trilemma” (title l. 12; abstract
l. 34), but the text has four horns and says “The four horns are exhaustive”
(l. 224). A trilemma has three. Either call it a quadrilemma, or fold horn (4)
into the framing as “deny the antecedent” and reserve “trilemma” for the three
in-domain options. This is presentational, but a referee will notice, and it
makes the exhaustiveness claim look less deliberate than it is.

---

## 8. Publishability

**Still needs a short revision; after that, publishable as a specialist note.**
The five requested repairs are substantially in place: T1 is now an internal
premise, T4 is a conditional trilemma rather than an assertion of `W`, the
2013/2015 criticism is a framing gap rather than a logical defect, the
four-event model states its assumptions and addresses n. 7, and “scale-general”
replaces “scale-free” with the n. 3 qualification and the selection procedure.
The remaining defects are: horn (4)’s conflation, the missing “no present” horn,
the patch-only cost for horn (3), the unextended n. 7 caveat, and the abstract’s
“sufficiency sentence fails” (l. 41), which overstates the body’s “does not tell
us which horn holds” (l. 234–235). Fix those and the note is a defensible
specialist contribution. Do not expand it; the conditional trilemma is the right
size.
