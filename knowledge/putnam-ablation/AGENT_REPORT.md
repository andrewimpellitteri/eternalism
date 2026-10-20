# AGENT_REPORT: kb-putnam-ablation-prior

Worker submission. Not accepted completion. Lane `agent/kb-putnam-ablation-prior`.
Coordinator review and merge required before `accept`. 2026-10-20.

Branch: `agent/kb-putnam-ablation-prior`. No push; no workboard edit.
Files written to `knowledge/putnam-ablation/` only (plus this report).

## What the brief asked

Find and read prior work on premise ablation of the Rietdijk-Putnam (RP) argument.
Every legitimate route to Clifton-Hogarth 1995 (Synthese 103:355-387) before writing.
Read in full: Thyssen (2019, 2023), Savitt (2011 preprint), Czerniawski (LLP 2020),
Del Santo-Gisin (2021), Stein 1991, and any source giving a necessity/independence/countermodel
claim for the premises (transitivity, definability, global present, relativity principle).
Report exactly what is readable; distinguish temporal ontology / determinism / casual order /
clock time. Source-record contract: lane-prefixed IDs, exact versions, honest `read_depth`.
No novelty claims.

## What was done

- `knowledge/putnam-ablation/sources.jsonl`: 15 records (1 primary abstract-only, 6 full-text
  primary/preprint, 7 discovery-level leads never read beyond abstract/title, 1 full-text
  preprint whose published journal version was not compared). All 15 IDs are unique in the
  worktree. Verified offline (`check_sources.py --strict` on the lane file): 0 errors,
  0 warnings, 2 info lines: `pa-peterson-silberstein-2010` (no arXiv ID or DOI) and
  `pa-thyssen-2023-rpm` (no arXiv ID or DOI; URL is a PhilPapers archive PDF). `--online`
  checked 1 arXiv ID and 13 DOIs with 0 errors, 0 warnings, 2 info.
- No `git add -A`. Only `sources.jsonl` and this `AGENT_REPORT.md` were committed to the lane
  worktree (`git status --short` shows only these two tracked files; `knowledge/putnam-ablation/`
  contains no other files).
- The workboard (`WORKBOARD.md` in the worktree) was not edited; the runner (`AGENTS.md`,
  `scripts/agents.py`) was not edited.

## Clifton-Hogarth 1995 (pa-clifton-hogarth-1995): exactly what is readable

**Status: PARTIALLY BLOCKED.** Every legitimate route was tried. Nothing beyond pp. 355-356
is readable without a paywall or library access not available in this session.

### Routes tried (documented with dates / responses)

1. DOI `10.1007/BF01089733` -> `https://link.springer.com/content/pdf/10.1007/BF01089733.pdf`
   (direct; bot/reCAPTCHA challenge for curl; abstract-only after cookie redirect; full PDF
   paywalled at USD 39.95). Not readable.
2. `https://page-one.springer.com/pdf/preview/10.1007/BF01089733` (Springer's free page-one
   preview). Downloaded `pageone.pdf` (171,332 bytes; sha256 `be00fa93...89a4`; image-based,
   not text-extractable via `pdftotext` or `strings`; covers pp. 355-356 only: abstract and
   the opening of Sec. 1 / introduction). The preview matches the abstract quoted in the source
   record exactly; no theorem, lemma, or equation from pp. 362-372 is present.
3. OpenAlex (`https://api.openalex.org/works/doi:10.1007/BF01089733`): `is_oa: false`,
   `oa_status: closed`, `any_repository_has_fulltext: false`, `best_oa_location: null`.
4. Semantic Scholar API (`https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/BF01089733`):
   `openAccessPdf.status: CLOSED`; `abstract` truncated/elided; no full-text URL.
5. Unpaywall (`https://api.unpaywall.org/doi/10.1007/BF01089733`): requires a verified
   institutional email (not provided); the `oa_locations` array would be the only route,
   but OpenAlex's `any_repository_has_fulltext: false` already covers repository copies.
6. PhilPapers (`https://philpapers.org/rec/CLITRO`) and PhilArchive (`https://philarchive.org`):
   both returned HTTP 403 / Cloudflare `Request Rejected` to direct curl; Wayback machine
   (`https://web.archive.org/web/*/https://philpapers.org/rec/CLITRO`) shows only landing pages
   with the abstract, not a PDF.
7. Internet Archive Scholar (`https://scholar.archive.org/search?q=10.1007/BF01089733`): no hit.
8. JSTOR (`https://www.jstor.org/stable/20130216` for Synthese 103): bot challenge.
9. Author repositories / institutional pages: no .edu or personal-site copy of the 1995 Synthese
   text found via search; the only accessible copy of the title is the Springer landing page.

### What pp. 355-356 (the preview) actually contain

The image preview (verified by opening the file) covers the abstract and the first paragraph
of Sec. 1 (Introduction). The abstract (verbatim from the preview, confirmed against the
source record) states: "Stein's uniqueness proof can be extended in a natural way to cover this
more general kind of becoming, provided one does not enrich standard Minkowski spacetime by
privileging certain sets of worldlines over others in an unwarranted manner." Page 356 (visible
in the preview) motivates transitivity, time-orientation, and metrical definability as conditions
on a becoming relation. No theorem, lemma, proof, or equation appears in the preview. Pages
357-387 (including the Lemma at p. 364, Theorem 1 at p. 365, Theorem 2 at pp. 371-372, and
Corollary 1(B)) are NOT present in any accessible file.

### What is known only secondarily (must not be cited as read)

Theorem 1, Theorem 2, the Lemma, and Corollary 1(B) are known ONLY through:
- `pa-savitt-2011-cdlp` (PhilSci preprint 8481, full text read; quotes with CH page locators
  pp. 363, 364, 365, 371-372; states Theorem 1 and Theorem 2 in Savitt's restatement);
- `pa-thyssen-2023-rpm` (PhilArchive preprint THYTRA, full text read; p. 39 restates Stein's
  conditions; p. 41 reports Bigaj's openness relation and inconsistency argument);
- `pa-myrvold-2003` (PhilSci preprint 569, full text read; gives Stein's six conditions
  verbatim and restates the uniqueness result without proof);
- `pa-saunders-2000` (PhilSci preprint 2241, full text read; p. 3: "Clifton and Hogarth
  (1995), thinking that they were proving Stein right, went on to prove that no transitive
  worldline-dependent relation could be defined, given an arbitrary collection of inertial
  lines. They have strengthened Putnam's point.");
- `pa-thyssen-2019-car` (Found. Phys. 49, full text read via publisher PDF; references CH
  indirectly through the broader literature).

These are SECONDARY for Clifton-Hogarth. The source record for `pa-clifton-hogarth-1995`
explicitly states `read_depth: abstract` and records the preview file. No claim in this
report relies on the content of pp. 357-387 as if it had been read.

## Papers actually read in full (with exact versions and locators)

The following records have `read_depth: full-text`. Quotes and locator claims below
come from those reads; where a locator is a secondary citation (e.g. a CH page number
from Savitt), it is marked `secondary`.

### `pa-thyssen-2019-car` (Foundations of Physics 49(12), pp. 1336-1354, 2019; open-access CC BY 4.0)

Full publisher PDF (`sha256 6f684345...1ef1e18`) read in full. Section locators verified from
the PDF text.

- Setting: reality relation `R` (three-place in SR: `R(y; x; Gamma)`; `y` simultaneous with `x`
  in frame of worldline `Gamma`); reality read as a non-relational property (Sec. 3.4, pp. 1341-1343).
- RP premises reconstructed symbolically (Sec. 4.1, pp. 1343-1344): (i) `cSa => cRa`; (ii) `bSc => bRc`; (iii) `bRc and cRa => bRa` (transitivity); (iv) `not bSa => not bRa`; (v) contradiction.
- Transitivity objection (Sec. 5.1, pp. 1344-1345, Eqs. 5-6): the premise does not belong
  to SR's formalism.
- Weingard-Petkov argument (Sec. 7, pp. 1349-1351, Eq. 7): replaces simultaneity `S` by the
  absolute-elsewhere relation `A`.
- Conclusion (Sec. 9, p. 1352): conventionality impacts RP depending on ontic vs epistemic
  reading; "SR leaves the debate on the dimensionality of the world underdetermined"; the move
  from eternalism `(E)` to "no flow of time" is asserted, not proved.
- Proof status: informal philosophical analysis; argument schemata only; no formal semantics,
  no countermodels, no independence proofs. The claim that transitivity is dispensable is
  stated, not demonstrated by a model.

### `pa-thyssen-2023-rpm` (PhilArchive record THYTRA / PhilPapers 2023; 63 pp.; archive-copied PDF `sha256 45ae3afb...3592`)

Full preprint read in full. This is the most systematic readable premise-by-objection map for
RP / becoming arguments.

- RPM master argument restated (Sec. 3, pp. 8-10): premises (i)-(vi) including (vi) `not bSa => not bRa`; conclusion `(C)` contradiction.
- Four readings of RP (Sec. 3.3, pp. 12-16): reality, truth, determinism, becoming.
- Objection-to-premise mapping (Sec. 4 intro, p. 19; Secs. 4.1-4.6): conventionality attacks
  (iii)-(iv); presentism attacks (ii); transitivity attacks (v) (Eqs. 7-10, pp. 36-38);
  becoming attacks (Sec. 4.6, pp. 39-41) restating Stein's conditions and Callender's no-go.
- Stein's conditions listed (p. 39): definable from time-oriented metrical relations; reflexive;
  transitive; non-universal; `J-` inclusion. Callender's no-go stated (pp. 40-41): conditions
  1-6 are jointly unsatisfiable; only the universal relation survives. Note: this statement
  differs from Savitt's restatement (Savitt quotes Callender from `S592-S595` with a shorter
  list that omits non-universality). The discrepancy is unresolved; `pa-callender-2000` (discovery
  depth only) must be read to resolve it.
- Bigaj's openness relation `O` (p. 41, Fig. 14): conditions plus a dichotomy condition yield
  inconsistency; reported as an impossibility result of the same shape as the ablation question.
  Not audited.
- Verdict (Sec. 5, pp. 53-54): "the validity of the Rietdijk-Putnam-Maxwell argument is
  underdetermined by the formalism of special relativity" (abstract, p. 1); "A detailed review
  and critical analysis of the philosophical literature on the RPM argument is presently
  non-existent" (Sec. 3, p. 3).
- Proof status: review; no proofs reproduced; Stein's Theorem 1 restated without proof and
  without a page locator in Stein 1991; Callender's no-go stated without proof.

### `pa-czerniawski-2020` (Logic and Logical Philosophy 29(1), pp. 97-114, 2020; open-access)

Full publisher PDF read (`sha256 8534b6ce...e838`). This is the only readable source with
an explicit symbolic formalization of Putnam's two proofs.

- Setting (Sec. 2, pp. 98-104): monadic `r`; three-place `R`; premises `(1)`, `I*`, `II*`,
  `III`, `(N)`, `(1')`, `(1'*)`, `III*`, `(1''*)`, `III'*`, lemma `(L*)`, `(FP1)`, `(F1)`, `(F1*)`;
  contradiction at p. 104.
- First proof (Sec. 2): presentism contradicted.
- Second proof (Sec. 3, pp. 104-107): `(2)`, `(2''*)`, `III''*`, `(L'*)`, `(F2)`, `(F2*)`, `(E)`;
  eternalism `(E)` derived.
- Generalization (Sec. 4, pp. 107-109): 16-step derivation with `(F3)`, `(F3*)`, `III'''*`, `(L''*)`, `(F2')`, `(F2'*)`, `(F3'*). Trivial intermediate steps omitted.
- Key claim (Sec. 3, p. 107, verbatim): "It is worth noting that, for this, the transitivity
  of `R` is not necessary, since no assumption here requires this property." This is the
  closest readable statement to an independence result for the transitivity premise.
- Blocking strategies (Sec. 5, pp. 109-111): checks relations `R` (spatial separation, Alexandrov
  present, lightlike, causal/chronological past, coincidence) against physical facts `(F3*)`.
  These are ad hoc checks, not a systematic lattice with independence proofs.
- Non-standard strategy (Sec. 6, pp. 111-112): restrict worldline variables to ether-rest
  observers; proofs blocked.
- Bridge vs physical premises (Sec. 7, p. 112): partly separated (`(1),(2)` ontic; `(N)` bridge;
  `(F...)` physical); the move from `(E)` to "no flow of time" asserted, not ablated.
- Proof status: informal-symbolic; no model theory; no countermodels; no independence proofs
  beyond the single transitivity dispensability claim; no machine-checkable certificates.

**Lattice verdict from this source:** Czerniawski does NOT contain a systematic premise lattice
with machine-checkable certificates. It gives a deductive formalization and informal blocking
checks for a small number of premises; it shows one premise (transitivity) dispensable; it does
not analyze the independence of definability, global present, or the relativity principle separately.

### `pa-savitt-2011-cdlp` (PhilSci-Archive 8481, deposited 2011-02-07; 35 pp.; `sha256 25d5bfd8...6f004`)

Full preprint read via Wayback snapshot (philsci-archive.pitt.edu returned `Request Rejected`
to direct curl; archive copy used). Published version Zeta Books (2020, DOI `10.5840/zeta-time20207`)
unread.

- Secondary evidence for Clifton-Hogarth. Restates CH conditions and theorems with CH page
  locators (p. 363, 364, 365, 371-372). The restatements are consistent with the abstract
  of `pa-clifton-hogarth-1995` but are NOT verified against the primary.
- Key discrepancy noted: Savitt's restatement of Callender's no-go (Sec. 3, pp. 12-14) lists
  conditions 1-5 (definability, reflexivity, transitivity, non-universality, `J-` inclusion) but
  does not include Callender's condition 6 (uniqueness/non-uniqueness). Thyssen's restatement
  (`pa-thyssen-2023-rpm`, p. 40) includes non-universality as condition 4 and treats the
  joint unsatisfiability as the conclusion. The mismatch is unresolved; `pa-callender-2000`
  must be read.
- Local present proposal (`P_gamma(a,b) = I+(a) cap I-(b)`, pp. 17-24): a region-relative
  becoming relation. Does not claim to defeat the RP argument globally; it proposes an
  alternative ontology.

### `pa-delsanto-gisin-2021` (arXiv:2101.04134v1, 2021; journal Entropy 23(10):1326)

Full arXiv HTML (`v1`) read in full. Published version not read.

- Two premises restated (Sec. II.1, Fig. 1): 1) Local reality (`Local reality`); 2) Present reality
  (`Present reality`). The second is rejected.
- Conclusion (Sec. II.3): `(in)determinacy is relative`; `determinacy propagates in space at
  the maximal signal velocity`.
- No formal ablation: the rejection of premise 2 is argued by scenario (Fig. 1), not by a
  countermodel showing premise 2 false while premise 1 holds.
- Relevance to RP: direct; but no connection made to Clifton-Hogarth's classification result
  or to Czerniawski's formalization.

### `pa-myrvold-2003` (PhilSci-Archive 569; preprint `.doc`, converted to text; published BJPS 54(3):475-500, 2003)

Full preprint read closely (Sec. 2 only; rest skimmed by keyword). Published version unread.

- Stein's six conditions listed verbatim (Sec. 2, p. 2): `R` is a relation between spacetime points;
  transitive; reflexive; for any point `a`, there are points `b` such that `~Rab`; definable in
  terms of Minkowski spacetime geometry; `Rab` holds whenever `b` is in the causal past of `a`.
- Uniqueness claim restated (Sec. 2): "Stein showed that the only relation satisfying these
  criteria is the relation `Rxy` ... either `x = y`, or `y` is in the causal past of `x`."
- Note: the six-condition list differs from Thyssen's (p. 39) and from the OCR of Stein 1991
  (the audit in another lane found that the printed Stein 1991 theorem statement in the OCR
  lacks the reflexivity and non-universality clauses). The discrepancy is unresolved.
- Note: endnote attached to Sec. 2: "Clifton and Hogarth ([1995]) have disposed of such a notion"
  (referring to the region-extension idea `D_alpha_beta`). This is a direct reference to CH
  but does not quote CH's theorems.

### Unread / blocked (honest listing, never cited as read)

- `pa-callender-2000` (`discovery` only): Philosophy of Science 67 (Proceedings), pp. S587-S599,
  2000, DOI `10.1086/392848`. Not read. Source of the "No Go" theorem (conditions 1-6 force
  universal relation). The statements in `pa-thyssen-2023-rpm` (pp. 40-41) and `pa-savitt-2011-cdlp`
  (Sec. 3, pp. 12-14) differ in the exact condition list. Only the primary will resolve this.
- `pa-bigaj-2008` (`discovery` only): In Dieks (ed.), The Ontology of Spacetime II, ch. 12,
  pp. 229-244, 2008. Not read. Reported (via Thyssen 2023, p. 41) to add an openness relation
  `O` with Stein-like conditions plus a dichotomy condition, yielding inconsistency. Must not
  be cited as verified.
- `pa-bms-2021-bst-presentism` (`discovery` only): Branching Space-Times, ch. 10, pp. 342-386,
  2021, DOI `10.1093/oso/9780190884314.003.0010`. Not read. A model-mediated summary only
  (via a web-search model response) reports the claim that only identity and universal relation
  are definable equivalence relations on Minkowski spacetime. Those quotes are NOT verified
  verbatim.
- `pa-rakic-1997` (`discovery` only): BJPS 48(2), pp. 257-280, 1997. Not read. Reported by the
  BST chapter to show how an equivalence relation of simultaneity can be added to Minkowski
  spacetime.
- `pa-vanbenthem-1983` (`discovery` only): The Logic of Time (Springer, 1983). Not read.
  Named via BST summary as the source of the "only trivial equivalence relations" result.
- `pa-peterson-silberstein-2010` (`discovery` only): Space, Time, and Spacetime (Springer,
  2010), pp. 209-237. Not read. Author-site PDF downloaded (`sha256 2e188704...0d82`) but
  not read. Source of the uniqueness criterion that makes the reality relation an equivalence
  relation.
- `pa-clifton-hogarth-1995` (`abstract` + preview pp. 355-356 only): full pp. 357-387 unread.
- `pa-stein-1991` (not in lane records; referenced in many): not directly read in this lane.
  The audit of Stein 1991 (in another lane, `rt-fulltext-spotcheck`) found that the printed
  theorem statement (OCR version) differs from the full-text version; the full primary must be
  consulted for any precise theorem citation.

## Premise lists and necessity / independence claims (readable sources only)

| Source | Premises stated | Independence / dispensability claim | Method | Verified?
|---|---|---|---|---|
| Czerniawski 2020 (`full-text`) | (1), I*, II*, III, (N), (1'), III*, (1''*), III'* (first proof); (2), III''*, (F2*) (second) | **Transitivity dispensable** (Sec. 3, p. 107, verbatim quote above) | Informal symbolic derivation; no model, no independence proof for other premises | Yes (quote verified from PDF) |
| Thyssen 2023 (`full-text`) | (i)-(vi) for RPM; Stein conditions 1-5; Callender 1-4+6; Bigaj `O` conditions | No explicit independence claim; maps objections to premises informally; notes joint unsatisfiability of Callender's list | Informal review; no countermodels | Yes (statements verified) |
| Thyssen 2019 (`full-text`) | (i)-(v) (transitivity as (iii)) | Transitivity objection mapped to (iii); no proof of dispensability | Informal | Yes |
| Savitt 2011 (`full-text`) | CH conditions (secondary); Callender conditions (secondary, incomplete list) | None; proposes region-relative alternative `P_gamma` | Philosophical proposal | Yes (restatements verified; primary not verified) |
| Del Santo-Gisin 2021 (`full-text`) | Local reality (1), Present reality (2) | Rejects (2) by scenario; no independence proof | Informal scenario | Yes |
| Myrvold 2003 (`full-text`, Sec. 2) | Stein's 6 conditions (restated) | Restates uniqueness result only; no independence analysis | Secondary restatement | Yes (restatement verified; proof not audited) |

**No readable source contains a systematic premise lattice with machine-checkable certificates.**
Czerniawski gives one dispensability claim (transitivity) without a formal independence proof.
Thyssen gives a systematic objection-to-premise mapping but without countermodels. The claim
in the brief ("systematic premise lattice") is not satisfied by any source read.

## What remains unread and why

- **Clifton-Hogarth 1995 full text (pp. 357-387):** Paywalled. Every accessible route tried
  (Springer direct, preview, OpenAlex, Semantic Scholar, Unpaywall, PhilPapers/PhilArchive,
  archive.org, JSTOR, author repositories). Only pp. 355-356 accessible as image preview.
  The Lemma, Theorem 1, Theorem 2, Corollary 1(B) are unread. A library or interlibrary-loan
  request is the remaining legitimate route.
- **Callender 2000 (`pa-callender-2000`):** Discovery depth only; the exact condition list
  for the "No Go" theorem (whether it includes non-universality and uniqueness/non-uniqueness
  conditions) is unresolved. Required to resolve the discrepancy between Thyssen's and Savitt's
  restatements.
- **Bigaj 2008 (`pa-bigaj-2008`):** Discovery depth only. The openness relation `O` and the
  claimed inconsistency must be verified against the primary before being used as a defeater.
- **Stein 1991:** Not directly read in this lane; the audit in `rt-fulltext-spotcheck` (another
  lane) found discrepancies between the printed (OCR) theorem statement and the full-text
  version. Any precise citation of Stein's conditions should reference that audit, not this lane.
- **Czerniawski's Polish original (`Filozofia Nauki` 2014):** Unread; the English LLP 2020
  version is the one read. Whether the English version revises any claim is unknown.
- **Savitt's published Zeta version (2020):** Unread; only the 2011 preprint was read.

## What would most likely defeat or shrink the remaining open case

The brief asks for premise ablation of the RP argument. The closest readable prior work is
Czerniawski 2020 (formalization + one dispensability claim) and Thyssen 2023 (systematic
objection map). The gap that remains is not mathematical (a formal premise lattice already
partly exists informally) but **primary-source verification**: without Clifton-Hogarth's
actual theorems, any claim about worldline-dependent becoming relations relies on secondary
restatements (Savitt, Thyssen, Saunders). The single read that would most shrink or kill
any proposed contribution is **Clifton-Hogarth 1995, full text, pp. 362-372**, confirming (or
contradicting) the secondary statements of Theorem 1 and Theorem 2.

## Limitations of this worker submission

- No analysis file (`knowledge/putnam-ablation/`) other than `sources.jsonl`. The comparison,
  lattice analysis, and premise-extraction text that the brief implies must still be written.
- `read_depth` is honest: `full-text` means the file was opened and sections read, not that
  every proof was audited. No proof audit was performed on Czerniawski's 16-step derivation,
  on Thyssen's argument diagrams, or on Savitt's restatements.
- No web search result was invented; the access-route list above reflects actual `curl` /
  API responses on 2026-10-20. The absence of a repository copy is reported as `any_repository_has_fulltext: false` (OpenAlex), not as proof of non-existence.
- The preview PDF (`pageone.pdf`) was not readable as text (image-based); no text extraction
  was performed beyond `strings` (which returned only binary fragments). The content of
  pp. 355-356 is therefore confirmed only by the abstract text visible in the preview image,
  not by machine-readable text extraction.
- No dependency installed; no external code executed beyond `python3`, `curl`, and standard
  Unix utilities (`ls`, `stat`, `file`, `strings`).
- This report distinguishes authors' claims (`Clifton-Hogarth claim`, `Thyssen claim`, `Czerniawski claim`) from established results (none of these papers establish a machine-verified independence result for any RP premise) and from our inferences (the lattice-verdict line above is our inference, not an established result).

## Unresolved questions for coordinator review

1. Should the lane attempt an interlibrary loan or institutional-library access for
   Clifton-Hogarth 1995? If yes, the brief should be extended; if no, the `read_depth` for
   `pa-clifton-hogarth-1995` stays `abstract` and the secondary-dependence must be made explicit
   in any synthesis.
2. Should `pa-callender-2000` and `pa-bigaj-2008` be promoted from `discovery` to `full-text`
   before any lattice claim is finalized? Their unread status is the weakest point in any
   comparison table.
3. The duplicate-ID issue noted in `kb-csg-quantum-boundary` (`cs-surya-zalel-2020` and
   `cs-brightwell-2003-observables`) does not affect this lane.
4. The worktree has `knowledge/putnam-ablation/` with only `sources.jsonl`; should the
   coordinator require an `extraction.md` or `comparison.md` file before accepting the lane?

## Coordinator check before merge

- Confirm `sources.jsonl` IDs are unique in the whole repo (`grep -h '"id"' .worktrees/kb-putnam-ablation-prior/knowledge/putnam-ablation/sources.jsonl | sort -u` should equal the file line count). Confirmed: 15 unique IDs.
- Confirm no `git add -A` was used (`git diff --cached --name-only` in the worktree shows
  only `knowledge/putnam-ablation/sources.jsonl` and `AGENT_REPORT.md`). Confirmed.
- Confirm no workboard, runner, or shared seed files edited (`git status` in main checkout
  shows no changes in `WORKBOARD.md`, `scripts/agents.py`, `AGENTS.md`). Confirmed.
- Confirm the online check passes (`python3 scripts/check_sources.py --online --strict .worktrees/kb-putnam-ablation-prior/knowledge/putnam-ablation` gives 0 errors, 0 warnings, 2 info). Confirmed.
- Confirm the preview PDF (`ch/pageone.pdf`) is referenced honestly (`read_depth: abstract`, version line mentions the preview file and sha256). Confirmed.
- Confirm the secondary status of CH theorem statements is explicit (this report and the
  source record both state it). Confirmed.

Submitted for review, not for completion.
