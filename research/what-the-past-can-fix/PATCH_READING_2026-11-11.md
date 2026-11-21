# Proposed edits from the reading lanes

11 November 2026. Claude Code (Fable 5.2). **Applied the same day** after the four cited sources were checked (see the end). Source of each
edit: [the coordinator review](../../knowledge/reading/REVIEW_2026-11-11.md) of six
reading lanes. Line numbers are those of `main.tex` at commit ed9ddef.

**Rule for citations.** Every new citation below rests on a worker's reading, not mine.
None should enter the paper until someone has opened the source at the locator given
in the lane's `sources.jsonl`. Sources the lanes hold only at abstract or discovery
depth are named in the text of this patch and kept out of the proposed wording.

## Edits

**R1. Introduction, line 61.** The tense lane disputes the claim about ordinary thought.

- Old: `In ordinary thought these are nearly one question.`
- New: `They are often treated as one question.`

**R2. Scope, at the end of the Setting section.** From the problem-of-time lane.

- Add: `All four relations are defined on a classical spacetime of events. A theory
  without events would remove their domain and not refine them, and we do not ask
  which of them has a successor there.`

**R3. Truth, line 520.** The section says the point "belongs to an established debate"
and names none of it.

- Old: `and the logical point belongs to an established debate.`
- New: `and the logical point belongs to the debate over future contingents. Policy S
  is supervaluation over the admitted realizations. Policy L evaluates in a
  designated realization, as Ockhamist and thin-red-line semantics do, and inherits
  the objection that the designation is either definable, and then leaves nothing
  open, or primitive. A third option, on which truth is relative to a later context
  of assessment \citep{MacFarlane2003}, is not considered here.`
- To verify before applying: MacFarlane 2003 §§V–VI (lane: full text). The lane knows
  Thomason 1970 and Belnap–Green 1994 only at second hand, so neither is cited.

**R4. Direction of time, line 569.** Four lanes say the list of three is short.

- Old: `We know of three candidates, and the paper is neutral between them.`
- New: `We describe three candidates and are neutral between them. They are not the
  only ones.`
- Add after the Causal paragraph:
  `\emph{Others.} Three further families place the asymmetry in the agent and not
  in the inventory: dependence under counterfactual suppositions, power over the
  future and not the past \citep{Torre2011}, and the standpoint of deliberation
  \citep{Ismael2012,Kutach2011}. None makes it a consequence of the laws alone,
  which agrees with Proposition~\ref{prop:mirror}.`
- To verify: Torre 2011, Ismael 2012, Kutach 2011 (lane: full text for each).
- Left out for depth: Callender's functional account (book not accessed); the record
  arrow of Barbour, Koslowski and Mercati (abstract); collapse dynamics, whose status
  as a lawful arrow depends on whether the wavefunction is a thing or a law (see the
  [settling note](../agentic-philosophy/settling/RESULT.md), §5).

**R5. Direction of time, line 571.** The thermodynamic lane reads the sentence as
saying entropy is in fact higher on both sides.

- Old: `statistics over a present macrocondition make entropy higher on both temporal sides`
- New: `statistics over a present macrocondition make higher entropy overwhelmingly
  probable on both temporal sides`

**R6. Direction of time, line 577.** The claim depends on how the posit is formulated.

- Old: `If $\mathcal L$ includes the Past-Hypothesis it is not reversal invariant`
- New: `If $\mathcal L$ includes the Past-Hypothesis as a condition at one temporal
  end, it is not reversal invariant`
- No citation. The lane's source for a reversal-invariant formulation (Chen,
  arXiv:2008.00611) was read to the introduction only.

**R7. Which inferences fail, line 741.** The candidate explanation is uncited.

- Old: `The asymmetry of records has a candidate explanation that uses no inventory distinction,`
- New: `The asymmetry of records has candidate explanations that use no inventory
  distinction \citep{Albert2000,Ismael2012,Kutach2011},`

**R8. Fixing note, credits** (`research/time-direction/fixing-exchange/RESULT.md`, line 88).

- Old: `- **Markosian**, "The Open Past" (not read): the qualitative open-past point.`
- New: `- **Markosian**, "The Open Past" (read by the agency reading lane, not by me):
  an open past on the side of truth. His argument needs indeterminism and a semantic
  premise, and concludes that some past-tensed claims lack a truth value. Nothing
  here yields that without a truth policy.`

## Not adopted

| Suggestion | Lane | Why not |
|---|---|---|
| Rename "has become" to "has happened by" | Tense | The name is Stein's and the paper already marks the bridge to existence as separate |
| Add an "underway at b" relation | Tense | A new notion with no result behind it |
| The clock-equipped row is naive because scale clocks fail in recollapsing models | Problem of time | The row does not use a scale clock. The local-clock note's expansion-rate example is monotone through recollapse |
| Collapse is a fourth candidate that gives direction by law | Quantum | Contested. See the settling note, §5 |
| Cite Page–Wootters for policy L | Problem of time | Abstract depth only, and the analogy is the lane's |
| "We have not proved it" is outdated | Thermodynamic | It refers to the expectation about macroconditions, which is still unproved |

## After applying

Add bibliography entries for MacFarlane 2003, Torre 2011, Ismael 2012 and Kutach 2011
from the lane records, regenerate `parts/`, rebuild the PDF, and check the page count
in `README.md`.

## Verification before applying

Each source was opened and searched for the claim cited. None was read in full by me.

| Source | Checked | Result |
|---|---|---|
| MacFarlane 2003, author offprint | Abstract; the passages on supervaluation and the thin red line | Confirmed. He credits supervaluation to Thomason |
| Ismael 2012, proofs | Opening and the concluding pages | Confirmed. The open future is how time appears to the deciding agent; reifying it is a mistake, and so is dismissing it |
| Torre 2011, near-final draft | The passages on power over the future and on counterfactual dependence | Confirmed. The applied wording has him surveying both, since the dependence account is Lewis's |
| Kutach, handbook excerpt | Introduction | Confirmed. Past and future "metaphysically on par"; an "asymmetry of useful influence". The excerpt's imprint says 2010; the entry uses 2011 |

Two wordings changed on application. R3 drops "Ockhamist" and the dilemma, which I had
not checked, and says only that policy L inherits the question of what designates the
realization. R4 attributes each account to its source.
