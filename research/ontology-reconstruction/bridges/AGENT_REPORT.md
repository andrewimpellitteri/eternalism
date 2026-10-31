# AGENT_REPORT — ontology-bridge-premises

29 October 2026. Worker submission for coordinator review. Task: adversarial
audit of ontology-selecting bridge premises. Branch: `agent/ontology-bridge-premises`.
No accepted theorem, no novelty claim, no ontology verdict is asserted.

## Done / files

- `research/ontology-reconstruction/bridges/RESULT.md` — the deliverable:
  three bridge arguments (physical supervenience of concrete existence;
  completeness/constitution; objective becoming requiring additional
  structure), each with numbered premises/conclusion, strongest independent
  primary-source defense, charitable rival rejection, circularity test,
  symmetry test (same demand on eternalism), and countermodel; an enforced
  distinctions section (dynamical sufficiency vs constitution; prediction vs
  existence; model domain vs concrete inventory; representational vs
  ontological completeness; empirical equivalence vs identity of ontology); and
  the selection section.
- `research/ontology-reconstruction/bridges/sources.jsonl` — 20 records in the
  knowledge/README schema (validated: all required fields, legal read_depth).
- This file (runner root).

**Verdict submitted:** all three strong bridges fail their selection purpose.
The one worth defending is the weakened, symmetric form of Bridge C — the
anchoring requirement (definable-from / invariant-under accepted structure of a
named category, or empirically manifested, or earned as primitive with an
independent explanatory role), applied symmetrically to every ontological
reading including eternalism's. It is a classification instrument, not an
ontological proof. Four explicit defeat conditions are stated (RESULT.md §5).

## Search capability check

- `scholar_search`: **worked** (test query on Malament/becoming; OpenAlex +
  arXiv + Crossref records returned). Used for bibliographic verification.
- `serpapi_search`: **failed** — "Your account has run out of searches." Not
  used further.
- `web-search-prime`: **not used** (quota exhausted until 2026-11-17; not
  retried, per brief).
- `exa` (`web_search_exa`, `web_fetch_exa`): **worked**; all primary pages
  below were fetched and inspected directly.

## Source coverage and read depths (details in sources.jsonl)

- Full-text or substantial-part reads this session: Putnam 1967 (pp. 240–247,
  full argument); Wüthrich–Callender arXiv:1502.00018**v1** pp. 1–13 (§§1–4;
  their final "novel global becoming" section not read); Pooley 2013 PhilSci
  preprint §§II–X (published version not collated; final section beyond X not
  read); Arageorgis 2016 (abstract, §§1–4, conclusion; full argument incl.
  condition [N] and completion-parasitism).
- Abstract-level: Malament 1977 (Noûs 11(3):293–300; abstract + UCI
  bibliography); Dieks 2005 preprint abstract; Rideout–Sorkin 2000 (PRD 61,
  024002; v3 abstract).
- Project records reused at recorded depth (not reopened): Stein 1991 print
  audit pp. 148–150 (SHA-256 in the audit); C&R chs. 7, 9 extraction;
  Brading 2013 pp. 1101–1111; brading-universe-frontier full-text notes;
  reviewed internal results (REPAIR_RESULT, COMMON_EXTENSION_REPAIR);
  coordinator proposals (EXPLANATORY_ROLE_TEST, ROLE_OF_EXISTENCE,
  PREMISE_STRESS_TEST); red-team SYNTHESIS; POINT_OF_DISAGREEMENT;
  BATCH2_INITIAL_REVIEW.
- Secondary only (quotes taken via Pooley/Arageorgis/W–C; not independently
  read): Skow 2009, Earman 2008, Maudlin 2007 ch. 4, Dieks 2006, Sorkin 2007,
  Dowker 2005/2014, Belnap 1992, Tooley 1997. Unverified locators are recorded
  as unknown, not invented.

## Verification commands and results

- `python3 -c "...json schema check..."` over sources.jsonl → "records OK"
  (required fields and read_depth enum enforced).
- `git status --short` before commit → only `research/ontology-reconstruction/
  bridges/` plus this root file untracked; nothing outside owned paths touched.
- Countermodels are inspectable on their face: the E_all/E_past stress test is
  elementary; the clipped-Minkowski example is the project's reviewed sharpness
  example; Stein's printed theorem is the project's page-verified audit.
- No builds, installs, or large runs performed (none named in the brief).

## Compliance notes

- Independence: no assumption of other new workers' conclusions; neither
  rejected batch-2 submission is relied on anywhere (RESULT.md §0 records this
  explicitly); lane references resolved under `research/`.
- Selection argument is developed independently; relationship to the
  coordinator's EXPLANATORY_ROLE_TEST is recorded without adopting it as a
  premise (RESULT.md §5).
- No weighted ontology scores; the only taxonomy is qualitative and attached
  to named primary sources.
- No board, runner, shared seeds, or manuscripts touched; no child agents,
  pushes, or merges.

## Strongest contrary evidence found (against my own selection)

1. Maudlin-style primitivism (via Pooley fn. 6): if becoming is not modelled
   structure at all, "anchoring" misfires as a demand on physics and becomes a
   metaphysical preference; my reply (reclassification, not elimination) is
   stated but is a judgment call.
2. FLRW/CMB foliation lead (red-team §D): anchoring is category-relative, and
   in cosmological categories a shared now may cost nothing; this shrinks the
   bridge's selection power to near zero outside explicitly non-symmetric
   categories. Lead-level provenance only (not re-verified against primary
   texts this session).
3. W–C's CST results: Stein analogues are structure-dependent, so any
   definability-based norm inherits the fragility of the category choice.
4. The coordinator's domain-insensitivity example (EXPLANATORY_ROLE_TEST §2)
   shows weak distributed-grounding schemas are satisfied by all three simple
   domain policies — consistent with my negative verdicts on A and B, but it
   also shows how little any bridge can do without stronger grounding premises
   than anyone currently defends.

## Limitations

- Journal versions of Pooley 2013 and Wüthrich–Callender 2016 not collated;
  preprints used at stated versions. WC §§4.5–5 unread; Pooley's final section
  unread. Malament 1977 read at abstract level only — the frequently used
  "no privileged present" application is mine, via his verified simultaneity
  result and W–C's paraphrase of the conformal result (attribution left at
  their wording).
- The FLRW foliation point, Bell/rGRWf point, and all Skow/Earman/Maudlin/
  Tooley content are second-hand or lead-level here; a defensible version of
  this audit needs at least Earman 2008 and Maudlin 2007 ch. 4 read in full,
  plus a primary GR source for the FLRW distinguished-frame claim.
- The "anchoring requirement" is defended as a conditional methodological norm,
  not established as compulsory; its justification against primitive-fact
  theories is incomplete (that is defeat condition 3).
- Sources accessed are public; the Stein scan is a user-supplied local file
  whose verification record (not the file) is cited.

## Unresolved questions

1. Is there a neutral, non-circular statement of the supervenience base for
   Bridge A that both a later-grounded bivalent rival and a Stein-style rival
   could accept? (Probably not; a proof of impossibility would be valuable.)
2. Does the C&R bow-tie realm satisfy anchoring in curved spacetime, given the
   project's cylinder classification (potential realm ≠ bow tie when
   diam(S) > L)? A precise statement of what their realm choice costs in
   categories with horizons would sharpen the classification.
3. What exactly would count as "an explanandum only an unanchored addition
   explains"? The experience row remains unresolved in both coordinator notes;
   my defeat condition 1 depends on it.
4. Category-relativity of the anchoring norm: which physical category should be
   canonical for comparison — generic SR solutions, cosmological solutions, or
   the coupled Einstein–matter category the roadmap names?

## Proposed next tasks

1. Read Earman 2008 and Maudlin 2007 ch. 4 in full (primary) and re-run the
   Bridge C audit's rival-rejection section against them; collate Pooley 2013
   published pagination.
2. Formalize the anchoring classification as a small matrix: named physical
   category × rival contract (from the ontology-rival-contracts lane, when
   accepted) × anchoring status, with per-cell citations — input to Phase 2
   reconciliation, no scores.
3. Verify the FLRW/CMB distinguished-foliation claim against a primary GR text
   and promote or demote the red-team lead accordingly.
4. Test defeat condition 4: search for a physically serious category where an
   invariant, explanatory present exists (CST non-Hegelian escape routes,
   quantum reference frames) — the most direct way to break the W–C dilemma.
