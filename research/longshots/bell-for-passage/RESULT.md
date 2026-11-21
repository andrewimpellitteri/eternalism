# Bell-type theorems for objective passage: a negative result with one excluded conjunction

7-line summary below; claim contract per knowledge/NOVELTY.md. Lane: `longshots/bell-for-passage`,
10 November 2026. Horvat arXiv:2610.41944v1 was read at source (full HTML text); depths in
[sources.jsonl](sources.jsonl). This consolidates, and where marked verifies, the conjectured
Horvat transfer in
[markovian-presentism RESULT.md §5](../../ontology-reconstruction/coordinator/markovian-presentism/RESULT.md)
under its [audit](../../ontology-reconstruction/coordinator/markovian-presentism/AUDIT_2026-11-08.md)
point 6. No novelty claim is made; a negative result is the deliverable.

## 1. Exact question and proposed statement

Question. Is there an inequality or no-go theorem that every theory with objective becoming, or
with chances governed by the present state alone, must satisfy, and that experiment or
established physics could violate?

Proposed statement (negative, plus one excluded conjunction):

**(T)** Let a theory posit objective becoming with a global order ≺, chances Ch governed by the
≺-complete present state (Builes–Impagnatiello's Markovian Chance; Horvat's Irrelevance of
History, IH), Horvat's Probabilistic Locality (PL), and settings independence. Then Bell's Local
Causality holds (Horvat, Prop. 3), so Bell experiments exclude this conjunction. But (a) becoming
alone entails neither IH nor PL — Horvat's Prop. 2 exhibits their logical independence from
anything ontological, and his framework never mentions passage; (b) each remaining conjunct is
independently detachable: deny PL → preferred-foliation dynamics (relativistic Bohmian mechanics
carries "a hidden, empirically undetectable, notion of absolute simultaneity", DGTZ 2014 intro);
deny IH → history-relevant chances (Horvat §§VII–VIII; Wharton–Argaman's locally-mediated models;
GRWf flash chances); deny settings independence → superdeterminism; (c) any two theories agreeing
on all observable statistics can carry different ontologies of becoming (DGTZ 2014 foliation
undetectability; Tumulka's Lorentz-invariant GRWf). Therefore no inequality bears on objective
passage *as such*: inequalities exclude conjunctions containing it, at most. A no-go for a
conjunction is not a no-go for a conjunct.

Corollary for the repo. B&I's "precise datum" (Markovianism*) is falsifiable only jointly with a
locality-type premise; discovering non-Markovianity (their fn. 20) cannot, by itself, falsify
Nomic Presentism, because IH-detachment (history relevance) absorbs any Bell violation without
touching the ontology.

## 2. Three nearest predecessors, compared at assumption and result level

1. **Horvat, arXiv:2610.41944v1 (2026-10-30) — full text.** Assumptions: probabilistic
   world-theories (Defs. 1–3) on a globally hyperbolic foliated Lorentzian background; no
   ontology of passage; footnote 9 places the spacelike event on one slice with the screen.
   Results: Prop. 1 (deterministic Locality ⇒ Determinism); Prop. 2 (Bell's Local Causality and
   PL are logically independent, each direction by toy example); Prop. 3 (PL ∧ IH ⇒ Local
   Causality, via his Eqs. 13–17). He keeps PL as "relativity's lesson" and rejects IH: history
   is relevant. He draws no conclusion about passage, presentism, or B&I.
2. **Builes–Impagnatiello 2022 + repo adaptation.** Assumptions: Nomic/non-Humean presentism
   plus governance-from-the-present (the repo's §4 repair); Bayesian confirmation. Authors'
   result: Markovianism* confirms NHP. The repo's §5 transfer (Markovian Chance + probabilistic
   locality ⇒ Bell LC, falsified for GRWf) was a conjecture, "not formalised". This task read
   Horvat at source: the transfer holds, but only as conjunction-exclusion; Horvat's IH is
   exactly "governance from the present" stated cross-world, and his footnote 10 already makes
   the repo's O2 point.
3. **Wharton–Argaman, Rev. Mod. Phys. 92, 021002 (2020) — project record, full text.**
   Assumptions: QM-agreeing models; Local Causality decomposed into no-future-input-dependence
   (NFID), λ-independence, continuous action. Result: relaxing NFID yields locally-mediated,
   empirically adequate models with no retro-signalling. Horvat's IH is NFID in world-theory
   vocabulary; the escape space for passage theories coincides with their taxonomy. They also
   target no temporal ontology.

Auxiliary line: Leggett–Garg 1985 and the macrorealism literature (Emary–Lambert–Nori 2014
review; Clemente–Kofler 2016: LG inequalities are not necessary-and-sufficient for macrorealism,
no-signalling-in-time is the fine condition; Allen–Maroney–Gogioso 2017 ontological-models no-go).
These test macrorealism — definite values at all times, an assumption *open-future* presentism
denies — so they do not test passage either. Conway–Kochen (2006) excludes only deterministic
responses given free settings; the published comments (Tumulka 2007; Bassi–Ghirardi 2007) show it
does not touch relativistic stochastic collapse. Gisin (Erkenntnis 2019; Synthese 2021) ties
indeterminism to open time but derives no inequality. Myrvold 2017 PRA is the closest physics
no-go with the same shape: Lorentz-invariant + Markovian + standard degrees of freedom is
impossible for collapse dynamics — again a conjunction, again escapable by a foliation-like
nonstandard DOF.

## 3. What changes relative to these, and why it matters

Nothing in physics changes. The added content: (i) the repo's conjectural Horvat transfer is now
source-verified and correctly scoped to the conjunction (audit point 6 resolved for this lane);
(ii) the premise-dependency map shows every escape route for a passage theorist, so "Bell
falsifies Markovian presentism" is blocked as an overclaim; (iii) it shows the longshot's target
inequality cannot exist without a bridge premise that independently carries the empirical risk,
which is precisely where B&I's argument and its critics (Lettie, Ryoo, Howarth) actually trade.
It preserves empirical equivalence where it holds and is consistent with the paper's Limits
paragraph (Bell-type dependence is not signalling).

## 4. Smallest reproducible example and independent check

`toy_check.py` (pure stdlib, fractions; run `python3 toy_check.py`; passed 2026-11-10). It
exhibits: PR observable statistics (CHSH = 4); theory T_M whose chances are governed by the
complete present state alone (IH intact) yet are nonlocal — two present states agree on every
single-site slice distribution but differ on joint chances, so Local Causality fails and, by
Prop. 3, PL fails (the preferred-foliation escape); and theory T_H, a history-relevant twin whose
conditional chances at one site differ across two settings-independent histories (Ch(a=+1|e,x=0,
h1)=1 vs 0) but whose history-averaged statistics equal the PR observables exactly. So the
inequality separates neither ontology nor "governance from the present" alone. Independent
check: a reviewer recomputes the tables, and compares T_H against Horvat's §VII–VIII red-cube
discussion and his footnote 12 (multiple histories to one present, time-symmetric
indeterminism), and T_M against his Prop. 2 counterexample.

## 5. Kill conditions

- **Wrong:** a derivation of an inequality from passage alone, or from Markovian Chance without
  PL. Searched (scholar: OpenAlex/arXiv/Crossref; exa semantic): none found; Horvat's Prop. 2 is
  a counterexample to the second, but a proof would kill (T)(a). A detectable-foliation theorem
  or experiment would kill (T)(c); collapse-model bounds (Vinante 2017; Donadi 2021, project
  records) constrain dynamics, not ontology.
- **Already known:** any publication applying the conjunction moral explicitly to presentism,
  growing block, or the moving spotlight. B&I's six indexed citers (Lettie, Ryoo, Howarth,
  Mariani, Olsen, per the coordinator's sweep) do not; Horvat is too recent for indexed citers.
  **Unresolved lead:** Nero (2026, Zenodo), "Temporal Bell Inequalities and Global Consistency in
  Modal Triplet Theory" — surfaced in search; metadata unreachable today (DOI fetch failed,
  identifier truncated in search output). Resolve before relying on this contract's novelty
  section.
- **Trivial:** if the contract reduces to "Horvat Prop. 3 + audit point 6" verbatim. Accepted
  residual risk; the additions are the verified transfer, the escape taxonomy mapped onto
  passage theories, and the toy.
- **Physically irrelevant:** if all passage theories of interest already accept history
  relevance (then the corollary for B&I's fn. 20 still bites, but nothing new is excluded).

## 6. Kinds of novelty kept apart

Mathematical novelty: none claimed; the only theorem invoked is Horvat's Prop. 3 (his). Physical
novelty: none; every empirical statement is standard. Formalization novelty: none; the toy
illustrates, and does not formalize, his framework. Philosophical content: a source-verified
premise-dependency map and a testability boundary for temporal ontology — a synthesis
deliverable under NOVELTY.md's standard, to be entered as "conditional consolidation", not as a
discovery or a new prediction.

**Verdict.** The longshot idea — an inequality for objective passage itself — fails on current
sources: by construction (empirical equivalence of ontological addenda) and by locality of the
failure (conjunctions only). What survives is the scoped conjunction result and the observation
that B&I's datum is falsifiable only jointly with a detachable locality premise.
