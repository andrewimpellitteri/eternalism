# kb-putnam-ablation-prior — premise ablation of the Rietdijk–Putnam argument

Status: 2026-10-20. The automated run for this task failed on provider quota
(`.agent-runtime/runs/kb-putnam-ablation-prior/result.json`, exit 1, no
report). Its 15 source records were preserved. This report completes the lane
after the user supplied a scan of the one paper the lane could not obtain,
Clifton and Hogarth 1995; the scan was moved into
`knowledge/putnam-ablation/primary/`. No novelty claim is made.

## Files changed

- `knowledge/putnam-ablation/sources.jsonl` — 15 records (14 already present
  from the failed run; the Clifton–Hogarth record was upgraded from
  abstract/page-one to full-text, and open questions in the Savitt and
  Thyssen records were closed against the primary).
- `knowledge/putnam-ablation/primary/clifton-hogarth-1995.pdf` — user-supplied
  33-page scan, 2,834,611 bytes, sha256
  `1bcf93f94e5ff3252b154006b82c53e6462aa763e6d608525b630d100e8fa364`,
  OCR text layer, printed running heads p.355–387. Do not republish without
  checking provenance and redistribution rights.
- `knowledge/putnam-ablation/AGENT_REPORT.md` — this report.
- `knowledge/putnam-ablation/AGENT_REPORT.worker.md` — the failed run's preserved
  submission (commit 519056d), kept verbatim for provenance. Its Clifton–Hogarth
  status is superseded by the full-text read above.

## Readable / blocked status

| Source | Depth | Status |
|---|---|---|
| Clifton & Hogarth 1995, *Synthese* 103:355–387 | full-text | **Now readable.** User-supplied scan. Theorems, proofs and Secs. 3–4 read; publisher copy not compared. |
| Savitt 2011, *Chronogeometrical Determinism and the Local Present* | full-text | Read via Wayback copy of the PhilSci deposit (35 pp.). Secondary for CH and Callender. |
| Thyssen 2019, *Conventionality and Reality* | full-text | Publisher CC-BY PDF. Informal premise reconstruction. |
| Thyssen 2023, *The Rietdijk–Putnam–Maxwell Argument* | full-text | PhilArchive copy via Wayback. Informal objection-to-premise map. |
| Czerniawski 2020, *Time and Physical Geometry* | full-text | Publisher CC-BY-ND PDF. Symbolic reconstruction of Putnam's proofs. |
| Del Santo & Gisin 2021, *The relativity of indeterminacy* | full-text | arXiv HTML v1. Two-premise reconstruction; no formal model. |
| Myrvold 2003, *Relativistic Quantum Becoming* | full-text | PhilSci `.doc` via Wayback. Secondary statement of Stein's conditions. |
| Saunders 2000, *Tense and Indeterminateness* | full-text | PhilSci preprint via Wayback. Secondary paraphrase of CH. |
| Harrington 2008, *Special relativity and the future* | full-text | PhilSci preprint via Wayback. Secondary statement of "Stein's Theorem". |
| Callender 2000, *Shedding Light on Time* | discovery | **Blocked.** No OA copy found; content only via Savitt p.13 and Thyssen pp.40–41, whose statements differ. The No Go proof is unverified. |
| Bigaj 2008, *On Temporal Becoming, Relativity, and Quantum Mechanics* | discovery | **Blocked.** Closed access; known only from Thyssen p.41. |
| Rakić 1997; van Benthem 1983; Belnap–Müller–Placek 2021 ch.10; Peterson & Silberstein 2010 | discovery | **Unread leads.** van Benthem attribution comes from a model-mediated summary and is not verified. |
| Peacock 1992; Muller 1992; Stein 1991 (printed pages); Malament 1977 | not read here | CH discusses them; their primaries were not obtained. Stein 1991 exists in the repository only as OCR whose printed theorem wording is still unverified. |

## Premise table

Locators are to the read copies. "Necessity/independence" records what the
source actually proves, not what it motivates.

| Source | Setting | Premises as stated | Necessity / independence claim | Locator |
|---|---|---|---|---|
| Clifton & Hogarth 1995 (CH) | time-oriented Minkowski `(R^4, η, T)` | Thm 1: `B` implicitly definable from time-oriented metrical relations; `B` transitive; `I⁻ ⊆ B` (chronological becoming). Thm 2 adds worldline becoming `I⁻(b)∩λ ⊆ B_λ(b)`, worldline transitivity, meshing, and definability from `η, T, λ`. | **No premise-necessity/independence theorem.** Cor. 1(A): dropping `T` leaves only `U` (p.367). Sec. 3: dropping the "no privileged worldlines" condition yields countermodels — standard-simultaneity families and past-null-cone families satisfy Thm 2's premises but escape its conclusion (pp.376–380). Causal `J⁻ ⊆ B` is deliberately weakened to `I⁻ ⊆ B`, not proved necessary (pp.362–365). | Thm 1 p.365; Thm 2 pp.371–372; Cor. 1 p.367; Cor. 2 p.376 |
| Savitt 2011 | pre-relativistic review + local present | Restates CH: definable + transitive + chronological becoming; reports Callender's conditions plus non-uniqueness `NU`. Own proposal: region-relative present `P_γ(a,b)=I⁺(a)∩I⁻(b)`. | Reports Callender's No Go as: definable + transitive + `J⁻ ⊆ B` + `NU` ⇒ `U` (p.13); gives no proof. Calls the definability of further interval structure "open" (p.24). | pp.6–14, 16–24 |
| Thyssen 2019 | RPM/Weingard–Petkov argument schemata | RPM: `(i) cSa`; `(ii) bSc`; `(iii) cSa ⇒ cRa`; `(iv) bSc ⇒ bRc`; `(v) bRc ∧ cRa ⇒ bRa`; `(vi) ¬bSa ⇒ ¬bRa`; `(v)` is transitivity of "is real for". | Argues transitivity does not belong to SR's formalism (Sec. 5.1) and that conventionality attacks different premises under ontic vs epistemic readings (Secs. 5.2–5.3); concludes SR leaves the debate underdetermined (Sec. 9). Informal only; no countermodels or independence proofs. | pp.1341–1352 |
| Thyssen 2023 | RPM premises `(i)–(vi)` and objections | Same six premises; maps conventionality, presentism, transitivity and becoming objections onto them. Lists Stein's conditions including `J⁻` inclusion and non-universality. | Informal objection-to-premise map, not a lattice. **fn51 is wrong**: it says chronological inclusion would reduce CH's theorem to `I⁻` alone; CH p.365 leaves `I⁻`, `J⁻` or `U`. | pp.8–10, 19–41, fn51 |
| Czerniawski 2020 | symbolic reconstruction of Putnam's proofs | Reality predicate `r`; three-place frame-relative `R(y,x,α)`; premises `I*`, `(1''*)`/`(2''*)`, `III*`-style transitivity; physical "facts" `F*` asserted in SR. | **One explicit dispensability claim:** "for this, the transitivity of `R` is not necessary, since no assumption here requires this property" (p.107). Blocking strategies are informal; no model theory, countermodels or machine check. `R` is not CH's `B`. | pp.98–114, esp. p.107 |
| Del Santo & Gisin 2021 | truth-value (in)determinacy | `P1` relativity principle / finite information density; `Local reality`; `Present reality` (observers at relative rest share truth values for present events). | Rejects `Present reality` as the failing premise (Sec. II.1); informal scenario, no formal ablation. | Sec. I–III |
| Myrvold 2003 | Stein's conditions restated | `R` between spacetime points; transitive; reflexive; non-universal; definable from Minkowski geometry; holds for all `b` in the causal past of `a`. | Cites Stein's uniqueness result without proof; notes CH "disposed of" a worldline notion. Secondary. | Sec. 2 |
| Saunders 2000 | presentism and the "equivalence relation" requirement | Presentism needs an invariant definable equivalence relation (symmetric + transitive). | Claims CH "went on to prove that no transitive worldline-dependent relation could be defined" (p.3). **Too strong:** CH Thm 2 leaves `I⁻`, `J⁻` and `U`. Secondary. | pp.1–3 |
| Harrington 2008 | Stein's theorem and point present | "Only reflexive, transitive and Lorentz-invariant relations are the trivial, universal, past timelike and past causal relations." | Cites without proof. The printed statement omits future-directed relations; that is our observation, not a claim about Stein's text. Secondary. | Sec. 2, p.4 |
| Callender 2000 | No Go | Reportedly: definable + transitive + `J⁻ ⊆ B` + non-uniqueness `NU` ⇒ `U`. | **Unverified.** Savitt's and Thyssen's statements differ (Thyssen's condition list is jointly unsatisfiable as printed); whether Callender proves it is unknown. | via Savitt p.13; Thyssen pp.40–41 |
| Bigaj 2008 | openness relation `O` | Reportedly Stein-like conditions plus a dichotomy condition, deriving inconsistency. | **Unverified**, known only from Thyssen p.41. | — |

## What the Clifton–Hogarth primary establishes

1. **The theorem is a uniqueness/trichotomy result, not a premise lattice.**
   Theorem 1 (p.365, OCR-normalized):

   > "Consider an absolute, wordline-independent [sic] becoming relation in
   > time-oriented Minkowski spacetime. If this becoming relation is objective,
   > in that it is (implicitly) definable from time-oriented metrical relations
   > and is transitive, and if this relation satisfies chronological becoming,
   > then it can only be the relation of past chronological connectibility, or
   > the relation of past causal connectibility, or the universal relation."

   Theorem 2 (pp.371–372) extends the same trichotomy to every `B_λ`, given
   worldline becoming, worldline transitivity, and definability from `η, T, λ`.

2. **"Definable" means implicit definability as invariance under
   time-orientation-preserving metrical automorphisms** (p.361), not
   first-order or constructive definability. Any machine-checked version must
   encode this as a preservation/commutation condition on the relation, or the
   correspondence to the paper is lost.

3. **The premise is chronological, not causal, becoming.** CH replace Stein's
   `J⁻ ⊆ B` by `I⁻ ⊆ B`; the Lemma (p.364) derives chronological becoming from
   worldline becoming plus worldline transitivity, and the authors explicitly
   decline to endorse causal becoming because of the null-cone/coreality
   tangle (pp.364–365). This resolves the secondary disagreement: Savitt is
   right that CH's candidates are `I⁻`, `J⁻`, `U`; Thyssen's fn51 is not.

4. **The paper contains real independence-style evidence for two conditions
   only.** Dropping time-orientation leaves `U` (Cor. 1(A), p.367). Dropping
   the ban on privileged worldlines yields countermodels: a family of parallel
   inertial worldlines with standard-simultaneity planes, and a single
   noninertial worldline with past null cones, satisfy the Theorem 2 premises
   and escape the conclusion (pp.376–378); Peacock's and Muller's proposals are
   analyzed the same way (pp.378–380). Transitivity, worldline transitivity and
   worldline becoming are argued as constitutive of objectivity, not proved
   necessary by countermodel.

5. **Corollary 2 is a usable no-go for worldline-dependent equivalence
   relations** (p.376): reflexive `{R_λ}` satisfying worldline transitivity are
   each definable from `η, T, λ` iff they define an absolute `R` definable from
   `η, T`; combined with Malament's Proposition 3, this blocks recovering an
   absolute simultaneity relation by letting each observer use their own
   worldline, unless worldline transitivity is violated.

6. **The technical lemma is a candidate for later formal checking** (no
   novelty claim): CH assert that the subgroup of automorphisms preserving some
   timelike worldline generates the full Poincaré group, and say they could not
   find this in the literature (p.371; constructions pp.373–375). A Lean or
   computer-algebra check of that generation claim, plus the Theorem 2
   reduction, is a well-bounded formalization target. It would certify CH's
   proof, not create new physics.

## Lattice verdict

**No systematic premise lattice with machine-checkable necessity or
independence certificates was found in anything read here.** The closest
items are:

- CH: one uniqueness theorem with motivated premises and countermodels only for
  time-orientation and privileged worldlines.
- Czerniawski: symbolic derivations plus one informal dispensability remark
  about transitivity for a different relation.
- Thyssen 2019/2023: premise-by-premise reconstructions and an
  objection-to-premise map, but no models and no proofs of independence.
- Savitt: reports Callender's No Go without a proof; his own region-relative
  proposal is a replacement, not an ablation.

This does **not** establish that such a lattice is absent from the literature.
Callender 2000 and Bigaj 2008 are exactly the kind of source that could contain
the missing necessity/independence result, and both are unread. The repository's
existing axiomatic-relativity and Besnard material also already covers
assumption-sensitive simultaneity. The narrowest honest statement is: in the
readable sources, no formal assumption-dependency graph for the RPM argument
with checked certificates exists; what remains unread could defeat that.

What would most likely defeat a "new lattice" claim:

1. Callender's No Go proof (if it already gives premise-level necessity).
2. Bigaj's `O`-relation inconsistency argument.
3. A formalization of RPM premises in an existing relativity logic (Andréka et
   al., SpecRel) or Besnard's definability work.
4. A source that already treats the RPM premises as an explicit algebraic
   lattice rather than an informal argument map.

## Checks run

- `python3 scripts/check_sources.py --strict knowledge/putnam-ablation`
  — 15 records, 0 errors, 0 warnings, 0 info.
- `python3 scripts/check_sources.py --online --strict knowledge/putnam-ablation`
  — 1 arXiv ID and 13 DOI lookups, 0 errors, 0 warnings, 2 info.
- `shasum -a 256` on the scan; 33 pages confirmed with PDFKit; OCR text
  extracted and read for pp.355–387. Theorem numbers, page numbers and running
  heads checked against the scan.
- No live web search was used to complete this lane; identifiers were resolved
  online by the source checker against arXiv and Crossref.

## Limitations

- The CH text is a user-supplied scan with an OCR layer. OCR garbles symbols
  (`Bx` for `B_λ`, `J-~(b)` for `J+(b)` on p.365, `wordline` for worldline);
  readings above were taken with that in mind. The publisher's online version
  was not compared.
- Theorem proofs were read but not independently reproduced. No Lean/Coq
  certificate exists for CH, the group-generation claim, or Corollary 2.
- The CH scan's provenance and redistribution rights are not established.
- No general-relativistic or quantum extension is assessed here; CH themselves
  only sketch those directions (pp.384–386).
- The failed worker's records were not re-read against every primary; the
  records for Savitt, Thyssen, Czerniawski, Myrvold, Saunders and Harrington
  were spot-checked only where they bear on CH.

## Unresolved questions

- Does Callender 2000 actually prove the No Go, and with which exact premise
  list? Does it already supply the necessity result that would make a new
  lattice redundant?
- What is Bigaj's `O` condition, and is his inconsistency result an independent
  premise ablation?
- Can the CH group-generation claim be checked in all dimensions, and does the
  Theorem 2 reduction mechanize cleanly?
- How does CH's implicit definability relate to first-order definability in
  the relativity logics already catalogued in this repository?
- Stein 1991's printed theorem wording is still unverified (the repository has
  only OCR). CH quote Stein at pp.148 and 155–62; a readable Stein scan would
  settle the remaining RC-2/source-gate question.
- Peacock 1992 and Muller 1992 remain unread; CH's countermodel analysis of
  them is the best available secondary account.

## Narrowest unaddressed case (not a novelty claim)

Within the readable literature: an explicit, model-theoretic assumption
dependency graph for the RPM argument, distinguishing definability, transitivity,
chronological vs causal inclusion, time-orientation, and privileged-worldline
structure, with countermodels for each dropped premise and a machine-checked
certificate for at least the finite-dimensional core. CH supplies the uniqueness
theorem and two countermodel families; Czerniawski supplies one dispensability
remark; Thyssen supplies the informal map. No read source combines them.
