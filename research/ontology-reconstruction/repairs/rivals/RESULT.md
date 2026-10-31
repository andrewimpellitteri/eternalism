# Rivals repair: grounding-preservation, bounded collapse criterion, and the Bell audit

29 October 2026. Worker submission for independent review (task
`ontology-rivals-repair`). Not an accepted result, not an ontology
selection. It repairs the four-contract submission of task
`ontology-rival-contracts` at predecessor commit
`1fb23fdf6fb85de05b627b04b7bb648dd394c140`, under the shared
[reconstruction roadmap](../../ROADMAP.md), in response to
[`BATCH1_INITIAL_REVIEW.md`](../../coordinator/BATCH1_INITIAL_REVIEW.md)
section 3, per [`BATCH2_RUN_PLAN.md`](../../coordinator/BATCH2_RUN_PLAN.md).

Attribution tags:

- **[name, p. N]** — the named author's stated claim, with printed locator;
  depth per this run's register (`sources.jsonl`).
- **[PROVED (project)]** — a theorem of `research/stein-gr/main.tex`,
  internally reviewed, externally unaccepted; status per
  [`research/CLAIM_STATUS.md`](../../../CLAIM_STATUS.md).
- **[PROVED (bounded)]** — proved here, with scope limited exactly as
  stated (analytic proof in prose; mechanical witness check in
  [`checks/grounding_translation_check.py`](checks/grounding_translation_check.py)).
- **[PROPOSED]** — our proposal, explicitly not established.
- **[gate: …]** — an access limit recorded rather than papered over.
- **[ours]** — this lane's reconstruction.

Read-depth key per [`knowledge/README.md`](../../../../knowledge/README.md):
`discovery`, `abstract`, `full-text`, `reproduced`, `code-audited`.

## 0. What this repair does, in one paragraph

The coordinator held three §7.3 claims of the predecessor open: (i) the
derivational criterion against translation ("translations do not map
derivations") is not a general reason; (ii) the "iff" collapse conditions
carry no necessity/sufficiency proof; (iii) the Bell-nonlocality exposure
argument inherits an unresolved premise and conflates signalling with
nonsignalling dependence, and loss of motivation with collapse into
eternalism. This repair concedes (i) exactly — definitional translations
*can* map derivations, and the concession is checked mechanically on a
bounded fragment — and relocates the dispute to the layer translations
need not carry: grounding atoms and their direction
(Proposition T, §3). It replaces the unproved iff with a bounded
criterion proved in both directions relative to an explicit
operationalization (Criterion V, §4), demoting the old clauses to
flagged premises. It separates Bell nonlocality, nonsignalling
dependence, controllable signalling, and event ontology (§5), shows why
neither reading of the Clifton–Hogarth maxim yields collapse into
eternalism without an extra premise, and exhibits three concrete repair
options for local fragmentalism under which the view survives with its
ontology distinct from eternalism (witness: event *s*, §5.4). The
developed E/F comparison (§6) then states the two grounding directions
explicitly on a shared physical model and reports the honest finding the
brief anticipates: **as currently stated, the opposite grounding
directions restate the ontological dispute; no independent explanatory
payoff is demonstrated on the shared model, and §6.4 isolates exactly
what a payoff would require.** The four contracts (§7), their primary
clauses, and their strongest escapes (§8) are retained; Correia–Rosenkranz
later grounding is preserved and now verified first-hand (Replies §8).
Nothing here selects a temporal ontology (§10).

Search capability check (brief-mandated): `scholar_search` (OpenAlex)
**worked** (hits: Storz 2023; Chalmers 2011; deRosset 2015);
`exa` search/fetch **worked** (Putnam 1967 scan, Bell 1987 PDF, Broad
1923 archive.org OCR, C&R *Replies* at Sciendo, Fine 2005 NYU PDF,
arXiv abs pages for Tumulka/Hensen/Brown–Timpson, Nobel 2022 release);
`web-search-prime` **not retried** per brief; `serpapi` not needed.
De Gruyter returned HTTP 405 for the *Replies*; the Sciendo open-access
copy was used instead. Details in [`AGENT_REPORT.md`](AGENT_REPORT.md).

---

## 1. Notation and the shared comparison instrument

$\le$ is the reflexive causal order ($J^{-}$) of a spacetime; $\ll$ the
chronological order ($I^{-}$); $J^{-}(b)$, $I^{-}(b)$ the causal and
chronological pasts of event $b$. A *becoming theory* is a relation
$B$ with $I^{-}(b)\subseteq B(b)\subseteq J^{-}(b)$ in every globally
hyperbolic spacetime, unless universal
[PROVED (project), `thm:main`, `thm:flat`; assumptions and off-shell
premise per the manuscript and STRONGEST_VIEW §6]. Causal sufficiency
(P6) is the clause "whatever lies on a causal curve to $b$ is real from
$b$"; with it, $B(b)=J^{-}(b)$ [PROVED (project), given P6].

**Witness model (finite, explicit).** The induced causal suborder of
1+1 Minkowski on four coordinates: $a=(-1,0)$, $b=(0,0)$, $c=(1,0)$,
$s=(0,2)$ (units $c=1$). Then $J^{-}(b)\cap\text{pts}=\{a,b\}$,
$I^{-}(b)\cap\text{pts}=\{a\}$, and $s$ is spacelike to $a,b,c$. This is
a restriction witness, not a full spacetime model; every use below is
bounded to it. [PROVED (bounded), checked in `checks/grounding_translation_check.py`.]

Languages: shared core $L_0$ = causal order atoms + detector predicates.
E-side expansion adds a unary existence predicate $N$ ("concretely
exists") with the **definitional clause** $E(b,x) :\leftrightarrow N(x)
\wedge x\le b$. F-side expansion adds a binary primitive $R(b,x)$ ("$x$
is real from $b$"), with P6 giving $R(b,x)\leftrightarrow x\le b$ on
models where the fragment is $J^{-}(b)$ — extensionally coincident with
the E-side definiens on the witness model. These are comparison
instruments; per the [ROADMAP model-contract constraint](../../ROADMAP.md),
neither presupposes that all represented events concretely exist, and
neither is forced on the rivals of §7.

---

## 2. What the coordinator found, and the two-layer picture

BATCH1_INITIAL_REVIEW §3 on the predecessor's §7.3(1): "A formal
translation can map derivations as well as theorems. A dispute about
explanatory priority or metaphysical grounding must therefore identify
the extra structure that the relevant translation fails to preserve;
'translations do not map derivations' is not a general reason."

**Concession.** The coordinator is right, and the point can be made
mechanical: a definitional extension has an induced P-transform, a map
on formulas under which every axiom instance maps to a theorem and
modus ponens commutes with the map — so *derivations* are mapped, not
only theorems. On the bounded fragment this was verified: 252 instances
of the two Hilbert axiom schemas all map to tautologies under $\sigma$
(replacement of $R$-atoms by their definiens), with modus ponens
demonstrated semantically. [PROVED (bounded).] The predecessor's
criterion (1) is retracted as stated.

**The two layers.** What a truth-preserving, derivation-preserving
translation fixes is the *truth layer*: which sentences hold in which
models, and which inferences are valid. The dispute the contracts
actually pose (STRONGEST_VIEW §1: "the view and eternalism agree on
every tenseless truth and every observation. They disagree about what is
fundamental") lives on a second layer: **grounding atoms** — ordered
facts $A \triangleleft B$ ("$A$ grounds $B$") — together with a
primitive-basis specification (which predicates are primitives, which
defined). Whether definitions give rise to grounding atoms at all is
itself a premise:

- **Premise D** [explicit premise, not a theorem]: a definitional clause
  yields the grounding atom "the definiens-conjunction grounds the
  definiendum's instantiation." (The neighborhood is the standard logic
  of ground, where grounding claims have formal systems with structural
  axioms such as asymmetry and transitivity [abstract-level: deRosset
  2015 abstract locating Fine 2012a; systems not audited this run —
  flagged, per brief, as an open audit].) A theory that rejects D
  carries its primitive-basis choice *without* grounding atoms.

The structural premises used below, stated as premises: **(A)**
asymmetry — no fact grounds itself; **(T)** transitivity of
$\triangleleft$. Both are standard in the ground-logic literature
(neighborhood record above) and are adopted here only as explicit,
individually contestable premises — they are not physics.

**What a translation must preserve (the repaired criterion 1).** For a
translation between E-side and F-side theories to count as a
*translation of the rival* rather than an elimination, it must preserve,
on each theory's own primitive basis: (1) truths over $L_0$; (2)
derivations (it can — conceded); (3) **grounding atoms with their
direction**, if the theory carries them (Premise D accepted); or, if D
is rejected, (3′) the **primitive-basis specification** — which
predicates are defined and which primitive. (3)/(3′) is exactly the
"proposed grounding or explanatory-priority structure" the coordinator
asked us to name; for explanatory-priority disputes it is the
"aspect of dependence being offered as the explanation" of
[EXPLANATORY_ROLE_TEST §4 step 3](../../coordinator/EXPLANATORY_ROLE_TEST.md).
Call a translation pair *grounding-faithful* when it satisfies (1)–(3).

---

## 3. Proposition T: truth and derivation preservation do not carry grounding

**Proposition T.** On the witness model of §1, with the definitional
clause, P6, and Premise D as stated:

- **(T1)** There exists a translation pair $(\sigma,\tau)$ — $\sigma$
  mapping $R(b,x)$ to $N(x)\wedge x\le b$, $\tau$ mapping $N(x)$ to
  "$x$ is real from some standpoint" ($\exists b'\,R(b',x)$) — that is
  truth-preserving, mutually inverse on the shared core, and
  derivation-preserving, regardless of any grounding premises.
  [PROVED (bounded): verified over 3,715 bounded sentences of the
  fragment — ground atoms, Boolean combinations to three connectives,
  and one monadic quantifier layer — plus the 252-instance
  derivation check.]

- **(T2)** Under Premise D together with **full basicness** for F —
  the STRONGEST_VIEW §1 clause that standpoint-relative reality is
  *basic*, i.e. no distinct fact grounds $R(b,x)$ — no
  grounding-faithful mutual translation pair exists. *Proof.* E's
  definitional grounding atom is
  $(N(x)\wedge x\le b)\triangleleft E(b,x)$; by faithfulness it must
  survive $\tau$, giving
  $(\exists b' R(b',x)\wedge x\le b)\triangleleft R(b,x)$ on the F side,
  where the ground is a distinct fact; full basicness denies exactly
  this. With (A), the two atom sets cannot both be preserved. ∎

- **(T3)** The obstruction is premise-relative, not unconditional. If F
  asserts only **L0-restricted basicness** (no *L0*-fact grounds
  $R(b,x)$), the transported ground $\exists b' R(b',x)\wedge x\le b$
  is not an L0-fact and no collision arises; and if Premise D is
  rejected, there are no grounding atoms to preserve at all. The flag
  dependence was verified mechanically: collision occurs exactly under
  (D, full basicness), not under (D, L0-restricted) nor under (¬D).
  [PROVED (bounded).]

Consequence, stated with its exact scope: **the existence of a
truth-preserving, derivation-preserving translation decides nothing
about the grounding layer** — neither that the dispute survives
translation (T2) nor that it dissolves (T3). What the translation test
does deliver is a *location map*: the dispute lives wholly in the
grounding atoms (under D) or in the primitive-basis specification
(under ¬D). Whether a non-V-verbal residue there is substantive is
§4–§6, not §3.

---

## 4. Criterion V: a bounded collapse criterion, proved both ways; the old iff demoted

**Operationalization V.** The E/F dispute is *V-verbal* iff there is a
mutual pair of translations that is truth-preserving, mutually inverse
on all claims, **and** grounding-faithful (§2(1)–(3); under ¬D,
"grounding-faithful" reads as primitive-basis-preserving in both
directions).

**Criterion V.** (i) *Sufficiency*: if such a pair exists, the dispute
is V-verbal — by construction, since V just is the existence of that
pair. (ii) *Necessity*: within operationalization V, non-V-verbalness
requires the failure of some faithfulness clause; by T1 the truth and
derivation clauses cannot fail (on the bounded fragment), so the
failure must lie in the grounding/primitive-basis clause — which T2
supplies under (D + full basicness). Both directions are proved
relative to V. [PROVED (bounded/analytic).] V's domain of application
is stated: it concerns the E/F pair on the shared core; it is not a
general definition of verbalness and imposes nothing on disputes
outside its scope.

**The old "iff" demoted.** The predecessor's three conditions — (a)
fundamentality deflationism, (b) "P6 as mere physics", (c) defined
existence — are reclassified:

- **(a)** is not a condition *on* the dispute but the metametaphysical
  premise that decides whether failing V matters. It is now carried
  explicitly as an open premise of the comparison (both STRONGEST_VIEW
  §7 item 1 and O2 say this; the neighborhood literature on verbal
  disputes is recorded at abstract depth [Chalmers 2011 abstract;
  body unread this run — gate]).
- **(b)** and **(c)** become the *antecedent clauses of the F-side
  repair options* analyzed in §5.4 (what F must grant for its own
  position to change), not conditions of an iff.
- Necessity for the old three-clause conjunction is **declined**, with
  the reason: proving it would require ruling out every other route by
  which the dispute could be verbal or non-verbal, which needs a global
  metametaphysical theory no bounded argument supplies. The
  predecessor's "iff" is therefore withdrawn as a claim and retained
  only as the [PROPOSED] sufficient package it in fact is.

**Countermodel (the point of §3–§4).** The witness model carries, at
once: a proved truth- and derivation-preserving mutual translation
(T1), and — under (D + full basicness) — proved grounding
non-faithfulness (T2). Truth-conditionally the two sides are
intertranslatable; grounding-wise they are incompatible. This is the
exact sense in which "same physics, different ontology" is more than a
slogan *provided* Premise D and full basicness hold — and nothing here
defends those premises; they are the dispute restated (§6.3).

---

## 5. The Bell audit: four notions separated, the collapse claim repaired

### 5.1 Four notions (brief-mandated separation)

| Notion | Content | Status this run | Sources (depth) |
|---|---|---|---|
| **Bell nonlocality** (violation of local causality: no local-realist model with free settings reproduces the correlations) | Empirically established | Established experimental physics | [Nobel 2022 citation, verified this run]; [Storz et al. 2023 abstract, Nature, verified]; [Hensen et al. 2015 arXiv abstract, verified; journal pages per publisher metadata, unverified] |
| **Nonsignalling dependence** (spacelike outcome dependence that cannot carry messages; margins independent of remote settings) | What the violations actually establish, under the standard decomposition into parameter vs outcome independence | Established *as classification*; the Jarrett/Shimony decomposition itself is metadata-verified only — its proofs NOT audited this run [gate] | Jarrett 1984, Noûs 18(4):569 [discovery: locator via Brown–Timpson reference list]; Shimony, "Controllable and Uncontrollable Non-Locality" [discovery: CUP 1993 reprint, pp. 130–139]; Brown–Timpson 2016 [abstract, verified] |
| **Controllable signalling** (usable superluminal message transmission) | Absent in all empirically adequate formulations | Established absence at observable level | [Tumulka 2006 abstract, verified: rGRWf "reproduces the quantum probabilities in all cases presently testable"]; Brown–Timpson abstract: Everett QM "free of action-at-a-distance" Lorentz-covariant [verified] |
| **Event ontology** (what the local beables are: flashes, particles-on-a-foliation, field values, none) | Interpretation-relative; determines whether "spacelike dependence at the level of events" exists at all | Open; theory-dependent | [Tumulka 2006 abstract, verified: primitive ontology = "a discrete set of space-time points" (flash events); STRONGEST_VIEW §8.1, project record] |

The separation matters because the O6-style argument slides from the
first row to the second to the fourth. The established physics (rows
1–3) is precisely the *uncontrollable* kind: correlations without
signalling. Bell's own verdict about hidden-frame ontology — "The facts
of physics do not oblige us to accept one philosophy rather than the
other" [Bell, pp. 77–78, verified this run] — applies unchanged here:
no interpretation, and no ontology of events, is selected by the
violations.

### 5.2 The maxim's two readings

The Clifton–Hogarth maxim — "if an event … can causally influence
$b$, that event must have become for $b$" [C&H, p. 364; lane full-text
record; **gate**: Springer paywall, wording not verified first-hand by
this run] — contains the phrase "contribute to bringing about," which
admits two readings **[ours; not attributed readings]**:

- **(α) signalling-grade influence**: "contribute" = settle/signal —
  an influence that could make a difference to $b$'s being settled.
  Under (α), established Bell physics does not trigger P6's
  universalization: nonsignalling dependence is not influence, so
  $B(b)=J^{-}(b)$ stands and the fragments are untouched.
- **(β) any-dependence**: "contribute" = any fundamental-level
  dependence. Under (β), any spacelike-dependent dynamics (rGRWf-style
  flashes; foliation Bohmian mechanics) makes *everything* real from
  $b$ via maxim + transitivity — as STRONGEST_VIEW itself notes ("if
  non-signalling Bell dependence counted as 'contributing to bringing
  about $b$', the maxim plus transitivity would make everything real
  from $b$").

STRONGEST_VIEW P6 adopts the signalling form *because* it "is
restricted to signalling precisely so that this is a clear bet"; the
view's own text already contains the (α)/(β) choice. This repair's
audit conclusion: **the choice is an unresolved modal-interpretation
premise inherited from the maxim's wording, not something known
quantum theory settles.** Under the charitable reading (α) — the one
that matches the established uncontrollable character of the
correlations — the falsifier never fires on current physics.

### 5.3 Even under (β): revision, not collapse into eternalism

Grant (β) *and* an event-level spacelike-dependent fundamental
dynamics. Then P6 fails. What follows is **not** "the view collapses
into eternalism" (the phrasing of STRONGEST_VIEW §8 item 1 and O6,
which this repair flags as an overclaim in our own project record).
Three concrete repairs are available to the fragmentalist:

- **(F-a)** re-read the maxim as (α): keep P6 and
  $B(b)=J^{-}(b)$ intact. Cost: a interpretive bet about the maxim,
  not about quantum statistics — and the bet is the one the
  uncontrollable character of the established correlations favors.
- **(F-b)** drop causal sufficiency: the project's own classification
  leaves $I^{-}(b)\subseteq B(b)\subseteq J^{-}(b)$ for every globally
  hyperbolic spacetime [PROVED (project), `thm:main`]. Nontrivial
  fragments survive; e.g. the pointy option $B(b)=I^{-}(b)$ (Stein's
  domain, as recorded in the C&R-quoted definition) remains.
- **(F-c)** index fragments by whatever structure the new dynamics
  supplies (e.g. a Bohmian foliation): fragments become leaf-relative —
  a transition toward the standpoint-relative cousin of Contract G,
  still standpoint-basic, still not eternalism. (Note the scope
  correction: Tumulka's rGRWf is nonlocal and Bell-violating *without*
  a preferred slicing [abstract, verified] — so even collapse-type
  dynamics need not supply the foliation (F-c) presumes; and the
  2004/2006 model's non-interacting scope is recorded as unverified.)

**Witness that E ≠ F survives all three repairs** [PROVED (bounded),
checked]: on the witness model, under each repair option —
$F(b)=J^{-}(b)$, $F(b)=I^{-}(b)$, leaf-indexed — the event $s$ is
real-simpliciter (E inventory) yet unreal-from-$b$ (F fragment). The
ontologies remain distinct after the Bell premise is granted.

**The extra premise collapse into E would need**: that the fragments
have no remaining distinctive role — i.e., the conjunction of
predecessor-clause (a) (deflationism) with the denial of every *other*
F motivation (persistence-of-appearance answerability, standpoint
neutrality, Fine's n. 36 "more plausible way" programme [Fine n. 36,
verified this run]). Loss of one causal motivation (P6) or failure of
one constitutive bridge does not deliver that conjunction. The same
logical move is the one Correia–Rosenkranz themselves deploy against
Dorato–Hoefer's "only superficially distinct from eternalism" charge:
a currently-existing explanandum-fact does not imply a
currently-existing explanans-fact, and "some of the currently existing
facts … do so only courtesy of what will but may not yet exist"
[Replies, pp. 482–484, verified this run]. We cite their reply as the
published instance of the *form* of the move, not as an accepted
solution; whether it succeeds for C&R is the chapter lane's open
question.

### 5.4 Repaired exposure claim (predecessor criterion 2, narrowed)

What survives of the falsifier-exposure criterion, with exact scope:

- **F's grounding layer is dynamically exposed; the E inventory is
  not.** P6 is a grounding clause whose truth hangs on empirical
  dynamics (the maxim reads the dynamics as settling what became);
  a spacelike-dependent fundamental dynamics would force revision of
  the fragment content (§5.3). The E-side inventory clause, by
  contrast, is defined over whatever the complete physical history
  contains; no physics *prunes* it — revision changes its content, not
  its thesis.
- This is an asymmetry of **modal commitment profiles**, not of truth.
  It favors neither side by itself: the deflationist folds it into
  clause (a) ("exposure without truth-conditional residue is still
  verbal"); the substantivist counts it as content. It does, however,
  sharpen what F has staked: under (β)-type physics F revises, and the
  revision options (F-a)/(F-b)/(F-c) are concrete enough to be
  rationally choosable — which is the repaired content of "the bet is
  not idle" (STRONGEST_VIEW O6, kept with narrowed force).
- **Symmetry note (honest).** A *robust* eternalist (primitive block
  as fundamental structure) carries grounding atoms too
  ($N(x)\wedge x\le b\triangleleft E(b,x)$, Premise D) and is exposed
  to nothing physical — but pays instead the deflationist's
  challenge about primitive-basis disputes. The exposure asymmetry
  exists only between F and *deflationary* E; against robust E both
  sides are exposure-free and the dispute reduces to §6's grounding
  directions.

### 5.5 Inherited-premise audit list (all still open; none established here)

1. C&H maxim wording (p. 364) — **gate** (paywalled; lane record).
2. Reading (α) vs (β) of "contribute" — **ours**, unresolved.
3. rGRWf no-signalling proof and non-interacting scope — **abstract
   only**; body unaudited.
4. Jarrett/Shimony PI/OI decomposition — **metadata only**; proofs
   unaudited this run [gate].
5. "Bell-nonlocal at the level of events" (STRONGEST_VIEW §8.1) —
   interpretation-relative (event-ontology row); unresolved.
6. STRONGEST_VIEW §8.1/O6 "collapses into eternalism" — **overclaim,
   flagged**; replaced by §5.3's revision analysis. This is a
   correction to our own project record, proposed for the coordinator
   to carry into integration; this lane does not edit that file.

---

## 6. The developed pair: E vs F on the shared physical model

### 6.1 Why E and F are the strongest pair

E is the structure-minimal position (no added existence structure;
Putnam's own anti-foliation clause [Putnam, p. 246, verified this
run]); F is the only rival whose fragment content is fixed by the
shared physics theorems ($B(b)=J^{-}(b)$ given P6 [PROVED (project)])
while conceding empirical equivalence [STRONGEST_VIEW §6]. They are the
sharpest instance of "same physics, different ontology," and the only
pair for which the equivalence is already conceded by one side —
which is exactly what makes them the correct test for whether
anything substantive can survive translation. G and B differ from E in
inventory or extent, not merely in grounding direction.

### 6.2 The shared model and the two directions, stated as clauses

Analytic statement: Minkowski spacetime (or any globally hyperbolic
model), all sides accept the project's classification theorems, the
same records, horizons, and settledness behavior (R10), and no
observation distinguishes the sides [STRONGEST_VIEW §6, conceded].
Finite witness: §1's four-event suborder, with the E-side inventory
$\{a,b,c,s\}$ and the F-side fragment $F(b)=\{a,b\}$.

E-side clauses (whole-history eternalism):
- **E-inv.** $N(x)$ for every event of the complete history (witness:
  all four points).
- **E-def.** $E(b,x) :\leftrightarrow N(x)\wedge x\le b$ (restriction;
  no further fact of the form "$x$ is real from $b$").
- **E-ground** (under D): $(N(x)\wedge x\le b)\triangleleft E(b,x)$ —
  standpoint-relative facts are grounded *from the block side*.

F-side clauses (local fragmentalism, relativist core):
- **F-bas.** $R(b,x)$ is primitive and basic (full basicness; no
  distinct fact grounds it).
- **F-inv.** $R(b,b)$ always; $R(b,x)$ for $x\in J^{-}(b)$ (P6;
  witness: $\{a,b\}$).
- **F-ground** (P5): the tenseless geometry is the agreement of the
  standpoints — geometry facts are grounded *from the fragment side*:
  agreement-facts $\triangleleft$ causal-order facts.

### 6.3 The honest finding: the opposite directions restate the dispute

State the obvious, because it is the deliverable the brief asks for:
**as written, E-ground and F-ground are the ontological dispute
restated in grounding vocabulary.** The translation's failure to be
grounding-faithful (T2) is not an independent argument that the
dispute is substantive; it is the same claim said twice. The ¬D branch
is no better: the primitive-basis specification (E-def vs F-bas) is
the dispute restated definitionally. Either way, §3–§4's machinery
locates the dispute without advancing it.

**What an independent payoff would have to be** (per
[EXPLANATORY_ROLE_TEST §4](../../coordinator/EXPLANATORY_ROLE_TEST.md),
steps 1–3): an explanandum both sides recognize, where one side's
account requires its grounding direction — or its primitive basis —
and the other side cannot reproduce the *dependence aspect* without
adopting the disputed commitment. Two candidate explananda examined;
neither delivers:

1. **Truth-at-$b$ answerable to what exists from $b$** (the decisive
   open question flagged by the paired-contracts coordinator). E
   answers it deflationarily (truthmaker tenselessly exists), F
   fragment-internally. But on the shared model every putative
   witness of every true atom exists by the occurrence's own label —
   the coordinator's domain-insensitivity observation — so the
   answerability requirement, if accepted, is an extra
   contemporaneous-grounding premise, and if rejected, E's answer is
   fine. The explanandum distinguishes the premises, not the
   ontologies; adopting it would beg the question against E.
2. **Settledness behavior (R10)**: shared by both sides
   ([PROVED (project/here) per STRONGEST_VIEW]; in the witness
   nothing outside $F(b)$ is settled from $b$; in the Einstein static
   universe everything is). No payoff — the direction of grounding
   does no work in the derivation.
3. **Later grounding**: available to E tenselessly (all existents
   exist), to B via (GR) [C&R, p. 110, chapter-lane record], and
   defended by C&R against the collapse charge [Replies §8, verified
   this run]. No payoff for the E/F direction dispute. (The Dyke
   exchange at [Replies, pp. 457–458, inspected this run] states the
   adjacent challenge — "existence itself doesn't cause anything" —
   and C&R's response; recorded, not resolved.)

So: **missing independent explanatory payoff, isolated.** A payoff
would require a third kind of explanandum where the grounding
direction enters the derivation of a recognized phenomenon — not of
its truth-conditions — and rivals can only mimic it by importing the
disputed primitive. Nothing found on the shared model does this. The
claim "no payoff yet" is itself a finding, negative and scoped.

### 6.4 Charitable rival responses, both directions

- **F's response to E-def** (repaired clause (c)): the fragmentalist
  grants the *extensional* adequacy of $E(b,x)=N(x)\wedge x\le b$
  while denying that definitional adequacy captures grounding —
  coextension is not same-fact (the standard move the ground-logic
  literature formalizes; neighborhood record at abstract depth).
  Under T3 this is exactly the ¬D/L0-restricted exit: the
  E-side "definition" does not touch F's basicness. E's charitable
  counter: the mirror move — F's "primitive" is just a predicate E
  declines to define, and primitiveness-claims are not physics. The
  exchange is symmetric; neither move is a win.
- **F's response to the Bell exposure** (§5.3): (F-a) with (α);
  C&R-pattern reply if collapse is charged.
- **E's response to Criterion V**: "your faithfulness clause is just
  my opponent's thesis" — granted, and that is §6.3's restatement
  finding, not an objection to V's boundedness.
- **The deflationist's response to all of it**: V's non-verbalness
  under (D + full basicness) still only shows the grounding layer is
  where a non-truth-conditional residue *would* live; whether
  non-truth-conditional residue is substantive is clause (a), which
  nobody in this repair settles.

### 6.5 The concrete translation/countermodel tests (all executed)

Program: [`checks/grounding_translation_check.py`](checks/grounding_translation_check.py)
(standard library; explicit witnesses; bounded; runtime 0.087 s;
cap 10 s per brief).

1. **Translation test.** $(\sigma,\tau)$ truth-preserving and mutually
   inverse over 3,715 bounded sentences; derivation-preservation via
   252 axiom-schema instances (P-transform) plus semantic MP. → PASS.
   Establishes T1 on the fragment; *not* a general-language result.
2. **Grounding countermodel test.** E-layer and F-layer grounding
   atoms each internally consistent (asymmetric transitive closure);
   jointly consistent absent faithfulness; collision occurs exactly
   under (D, full basicness) and not under (D, L0-restricted) or
   (¬D). → PASS. Establishes T2/T3 on the fragment.
3. **Post-Bell distinctness test.** Under all three §5.3 repair
   options, $s$ is E-real and F-unreal-from-$b$. → PASS. Establishes
   the §5.3 witness.

These checks verify bounded combinatorial claims stated above; they do
not verify the philosophical premises (D, basicness, (α)/(β)), which
remain argued or open.

---

## 7. The four contracts (retained; primary clauses and strengthened-position tags)

Ten-field frame per [ROADMAP](../../ROADMAP.md). Where the predecessor's
verification has been upgraded this run, the register marks it; the
clause texts are unchanged. Depths: this run unless marked inherited.

### E — whole-history eternalism (Putnam-anchored)

1. **Inventory** [Putnam, p. 246 — verified this run]: "all future
   things are real ('things' here includes 'events'), and likewise that
   all past things are real, even though they do not exist now."
2. **Standpoint** [Putnam, p. 241 — verified]: Principle III verbatim,
   with its three restricting clauses (tenseless language;
   coordinate-independence; no accidentality). Standpoints are
   locations.
3. **Existence** [Putnam, p. 246 — verified]: tenseless existence
   ("will exist, or has existed, or exists right now"); "the notion of
   being 'real' turns out to be coextensive with the tenseless notion
   of existence." Absolute, tenseless; no primitive $E(b,x)$.
4. **Persistence** not fixed by the anchor (four-dimensionalism or
   stage theory; Sider remains record-depth [gate]).
5. **Truth/grounds** bivalent, tenseless; the reality-transfer route
   via transitive closure and "enough observers" [p. 246 — verified] is
   Putnam's *argument*; the project's required check 1 (domain of a
   model ≠ existence) blocks it as an inference.
6. **Passage** not fundamental [Putnam, p. 247 — verified].
7. **Added structure** none; absolute simultaneity explicitly
   disallowed [p. 246 — verified].
8. **Determinism/openness**: independent (Putnam separates the
   determinateness argument, pp. 243–246; project ledger keeps them
   separate).
9. **Empirical commitments**: none beyond shared physics.
10. **Strongest objection**: reality-transfer ≠ existence (Stein 1991
    record [inherited full-text]; check 1); Principle III is a bridge
    premise, not physics.

### G — preferred-slicing growing block (Broad/Bell-anchored)

1. **Inventory** [Broad, p. 66 — verified this run]: reality of
   present and past; "the future is simply nothing at all."
2. **Standpoint**: objective present = leaf $\Sigma_\tau$ of a
   preferred slicing (our reconstruction; Broad discusses absolute
   order, not foliations).
3. **Existence** [Broad, pp. 66–67 — verified]: absolute,
   extent-indexed; "The sum total of existence is always increasing"
   and the later-than clause ("includes … together with something
   more") [p. 67 — verified].
4. **Persistence** [Broad, p. 66 — verified]: growing life-histories;
   "slices have been tacked on."
5. **Truth/grounds**: classical pairing gives future-contingent gaps
   [C&R, p. 102, chapter-lane record]; the bivalent later-grounds
   hybrid (Contract L) is [ours], distinct from the book's clauses
   [source-vs-ours distinction preserved].
6. **Passage** [Broad, pp. 67–68 — verified]: "Let us call the third
   kind of change Becoming"; the other changes depend on it.
7. **Added structure**: preferred slicing; realizations: Lorentzian
   rest frame [Bell, pp. 77–78 — verified this run], metric-defined
   cosmic time (near-FLRW; non-locality not added structure — red-team
   correction), dynamical foliation (Bohmian-type; abstract-depth
   lead).
8. **Determinism/openness**: open by non-existence; deterministic GBT
   coherent.
9. **Empirical**: none; Bell's own text: the frame is hidden, "the
   facts of physics do not oblige us to accept one philosophy rather
   than the other" [pp. 77–78 — verified].
10. **Strongest objection**: Earman 2008 "carving chips off the
    block" [abstract + lane §§5–7 record; **gate**: PDF absent here];
    edge epistemics; non-local leaf in generic GR.

### B — Correia–Rosenkranz bow-tie spatiotemporaryism

1. **Inventory** [C&R ch. 9, pp. 135–137 — chapter-lane record;
   **gate**]: spacetime points via the fourfold division.
2. **Standpoint** [pp. 145 — chapter-lane]: every point a standpoint;
   (A22R)/(A23R).
3. **Existence** [pp. 148–149 — chapter-lane]: primitive, point-relative,
   intransitive; pointy domain $E_b = J^{-}(b)$ = Stein's (as C&R note);
   bow domain $M\setminus(J^{+}(b)\setminus\{b\})$; "intransitivity of
   being" their accepted conclusion (pp. 155–156).
4. **Persistence**: limbs-objection motivation [pp. 151–152,
   chapter-lane].
5. **Truth/grounds — later grounding preserved, now verified**:
   chapter 7's requirement — "where φ is a sentence that is true now,
   it should hold that, sometimes, there are things such that φ is
   true now because those things exist then" [(GR)-family; C&R, p. 110
   chapter-lane; the Replies §8 restatement **verified this run at pp.
   482–483**], with the §8 distinction **verified this run**: the
   explanandum-fact (that Q is true now) currently exists while
   "the present truth of R does not imply that there currently exists
   a corresponding explanans-fact" [Replies, pp. 483–484].
   **[ours, strengthened position — distinct from source clauses]:**
   the bivalent Contract-L hybrid of the paired-contracts coordinator.
6. **Passage**: standpoint-relative becoming; edge not a point
   [p. 160, chapter-lane].
7. **Added structure**: none beyond causal division; the commitment is
   logical (intransitive existence-at).
8. **Determinism/openness**: (IND_ex) grades II′/III′ vs bivalence
   [pp. 115–116, chapter-lane].
9. **Empirical**: none.
10. **Strongest objection**: intransitivity cost; II′/III′
    unrepresentable over one fixed manifold [ours, per predecessor
    RESULT §5 — retained as our result, unreviewed]; our closed-dust
    fact against the (AR2) converse [ours, retained].

### F — local becoming / local fragmentalism (project's strongest view)

1. **Inventory**: events; fragments $F(b)$; with P6, $F(b)=J^{-}(b)$
   [PROVED (project), given P1–P6 and the off-shell premise].
2. **Standpoint** [Fine n. 36 — verified this run]: every event a
   standpoint; Fine's "more plausible way" clause first-hand; worldline
   restriction optional (Corollary 9).
3. **Existence**: standpoint-basic; absolute = agreement (P5).
4. **Persistence**: part-within-$J^{-}(b)$ ("the Sun now" conventional
   from $b$; O15).
5. **Truth/grounds**: settled-or-gap from $b$ (R10); settled ≠ real;
   no later grounding invoked (contrast B).
6. **Passage**: fragment growth along the time orientation; direction
   imported, conceded (O12).
7. **Added structure**: none given locality (P3w — the contested
   premise).
8. **Determinism/openness**: orthogonal (R10; O17).
9. **Empirical**: equivalence conceded [STRONGEST_VIEW §6]; falsifier
   list §8 — item 1 now repaired per §5.3 of this document (revision
   options, not collapse).
10. **Strongest objection**: O2 translation argument (five red-team
    groups) — now sharpened into §3–§4: the translation exists,
    preserves truths and derivations, and the dispute survives only on
    the grounding/primitive-basis layer; Bell falsifier — repaired
    per §5.

### Comparison matrix (updated rows only where the repair changes them)

| Field | E | G | B | F |
|---|---|---|---|---|
| Existence | absolute, tenseless [p. 246 ✓] | extent-indexed [Broad p. 67 ✓] | primitive point-relative, intransitive [ch. 9, gate] | standpoint-basic; absolute = agreement [ours] |
| Truth/grounds | bivalent tenseless | gaps classical; L-hybrid [ours] | bivalent with later grounds [(GR) + Replies §8 ✓] | settled-or-gap (R10) |
| Added structure | none; foliation forbidden [p. 246 ✓] | preferred slicing [Bell pp. 77–78 ✓] | none beyond causal division [gate] | none given locality |
| Empirical | none | none; frame hidden [Bell ✓] | none | none; equivalence conceded |
| Bell status | no exposure (inventory clause) | exposed via foliation dynamics; Bell's own neutrality clause [✓] | not exposed (clauses SR-true) | exposed via P6 under (β) only; three repairs; ≠ E survives [checked] |
| Key translation | E↔F pair proved truth+derivation-preserving [bounded ✓] | leaf-advancement ↦ block + indexical [contested] | @bE!y primitive vs reductionism (§6) | non-V-verbal under (D + full basicness) only [✓]; restatement finding §6.3 |

(✓ = clause verified first-hand this run; full matrix in the
predecessor submission at commit `1fb23fd` remains the base and is
incorporated by reference; only repaired rows are reprinted.)

---

## 8. Strongest rival escapes (updated for the repaired Bell status)

- **E**: (1) diagnose the rival primitive ($E(b,x)$ ill-defined, not
  false — Putnam's own opening diagnosis of "real"); (2) abduction from
  no-added-existence-structure — under-supported pending a cost metric
  (EXPLANATORY_ROLE_TEST §1); (3) defend Principle III independently —
  with Stein-1991's cost that automorphism-neutral standpoint-relative
  becoming also satisfies the neutrality.
- **G**: (1) scope to near-FLRW (metric-definable foliation: cost is
  non-locality, not added structure — contested premise, no begging);
  (2) Bell–Lorentz move, now first-hand verified [pp. 77–78]:
  unverifiable-in-principle ≠ unreal; (3) bivalent hybrid (Contract L,
  [ours]); (4) discrete realization via causal-set growth (Earman's own
  endpoint, lane record).
- **B**: (1) limbs/persistence motivation (chapter-lane); (2)
  determination gain on closed dust (bow domain determines all field
  values — [ours, predecessor §5, unreviewed]); (3) own the
  intransitivity; (4) later grounds [Replies §8, now verified] decline
  the contemporaneous-grounding premise.
- **F**: (1) fundamentality defense in its repaired form: the view
  stands or falls with the substantivity of primitive-basis/grounding
  disputes (O2) — §3–§4 give the sharper statement and the sharper
  refutation condition (V); (2) relativist core; (3) the signalling
  bet as modal content — **downgraded** per §5.4: exposure without
  collapse, three concrete repairs, no truth-conditional advantage;
  (4) worldline restriction (Corollary 9) at the recorded horizon cost.

---

## 9. What survives source checking vs what remains an access gate

| Item | Status after this run |
|---|---|
| Putnam pp. 240–247 clauses (E) | **Verified first-hand** (full-text) — survives |
| Broad pp. 66–68 clauses (G) | **Verified first-hand** (OCR; garbles noted) — survives |
| Bell pp. 77–78 clause (G) | **Verified first-hand** — survives |
| C&R Replies §8 pp. 482–485 (B later grounding; anti-collapse move; Bohmian concession p. 485) | **Verified first-hand** — survives; upgrades the inherited lane record |
| Fine n. 36 Sprigge clause + §11 region (F) | **Verified first-hand** — survives; pp. 304–305 asymmetry passage remains lane-record (FINE_READING.md) |
| stein-gr theorem statements/names | Verified present this run; proofs not re-audited [inherited status] |
| Stein 1968 wording | **Gate**: unread project-wide; quoted only via C&R p. 149 (itself chapter-lane) |
| Stein 1991 theorem p. 149 | **Gate**: foundations-lane record; not re-read |
| C&H maxim p. 364 | **Gate**: paywalled; lane record only |
| C&R NTC chs. 7/9 clauses | **Gate**: user-supplied PDFs, chapter-lane records (CLAUSES.md consulted); chs. 1–5, appendices unread project-wide |
| Earman 2008 §§5–7, p. 151 | **Gate**: lane full-text record (PRIOR_WORK.md present here); PDF absent |
| Ellis 2006 abstract clause | Inherited abstract record (predecessor verified twice); body still unread |
| Jarrett 1984 / Shimony controllability | **Gate**: metadata verified via Brown–Timpson reference list; arguments unaudited |
| rGRWf no-signalling proof, scope | Abstract verified; body unaudited |
| Chalmers 2011 verbal-dispute tests | Abstract only; not used as V's basis |

## 10. What does not follow; bridge-premise inventory; no selection

Nothing in this repair selects E, G, B, or F, and no result here is a
proof that physics selects a temporal ontology. The bridge premises are
inventoried per contract, each separately undefended at selection
grade: **E** — Principle III; real/tenseless-existence coextension.
**G** — Bell–Lorentz hidden frame; Broad's third change; slicing
realization choice. **B** — primitive E!; intransitivity acceptance;
(GR) grounding schema. **F** — P1–P6; the (α)/(β) maxim reading;
off-shell premise; substantivity of primitive-basis disputes. Plus the
cross-cutting premises of this repair: D, (A), (T), operationalization
V. Underdetermination remains the live research conclusion; a rigorous
argument for it is allowed output, and none is claimed here.

Scope limits of the bounded checks: 4-event induced suborder; bounded
sentence set; schema instances; standard library; 0.087 s. They verify
the stated bounded claims only; no dense search was run and none
timed out.

## 11. Proposed next tasks

1. **Bridge-premises lane / coordinator**: audit Premise D against the
   ground-logic literature (Fine 2012a; deRosset) and decide whether
   the grounding-atom layer or the ¬D primitive-basis layer is the
   official location of the dispute — this changes nothing in §7 but
   fixes which premise the next adversarial round attacks.
2. **Equivalence lane**: test Criterion V's faithfulness clause on the
   G-vs-E pair (where the translation must preserve the leaf-indexical
   structure) — the one place exposure (§5.4) and V can diverge
   concretely.
3. **Source acquisition (library, not installs)**: Stein 1968;
   C&H 1995 (maxim p. 364 first-hand); C&R appendices; Earman 2008 PDF;
   Jarrett 1984 (PI/OI definitions first-hand); Fine print pagination.
4. **Physical scout (scoped)**: whether any sanctioned collapse model
   combines event-level spacelike dependence *with* a preferred
   foliation (the (F-c) trigger) — currently only foliation-Bohmian
   does per the abstract-level records; rGRWf does not. Scope note
   only; no selection claim.
5. **Coordinator integration**: carry the STRONGEST_VIEW §8.1/O6
   "collapses into eternalism" correction (§5.3) into the project
   record at review; this lane does not edit that file.
