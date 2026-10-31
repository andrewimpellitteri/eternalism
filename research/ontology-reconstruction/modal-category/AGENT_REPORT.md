# AGENT_REPORT.md — ontology-modal-category-bridge

Task: map existential openness to explicit physical and metaphysical model
categories (reconstruct ω_t^ex and the nomological box from C&R ch. 7,
compare model categories with the same local field equations, deliver an
explicit translation or exact obstruction, with charitable rival, positive
bridge argument, and defeater).

## Search capability check (required at start)

- `web-search-prime` (`tools["web-search-prime"].web_search_prime`):
  **FAILED** — MCP error −429, code 1310 "Weekly/Monthly Limit Exhausted.
  Your limit will reset at 2026-11-17 10:00:29". Recorded per brief; not
  used for any result.
- `serpapi_search`: **FAILED** — "Your account has run out of searches."
- `scholar_search`: **WORKED** (openalex + arxiv + crossref). Used to pin
  Sbierski arXiv:1309.7591v3 and Choquet-Bruhat–Geroch 1969 (crossref).
- `exa` web_search/web_fetch: **WORKED**. Used to fetch the Sbierski ar5iv
  full text, the Luk–Oh–Yang abstract, and the open-access full text of
  C&R "Replies to Critics" (Sciendo PDF text), including the full §7
  pp. 477–482 passage.

No claim below rests on an unaccessed source; depths are per record.

## Done / files

Owned directory `research/ontology-reconstruction/modal-category/`:

- `RESULT.md` — the substantive deliverable. Strongest counterexample
  first (§0: the coordinator's open cut M_< does not instantiate C&R's
  openness clauses — no last moment, and both sides of the source
  exchange use terminal-time complete worlds, not cuts); §1 pins the
  ch. 7 worldstate and modality clauses with exact quotes and page
  locators (ω_t^loc/ω_t^ex definitions, the anti-trivialization ban,
  (DET_loc)/(DET_ex)/(IND_loc)/(IND_ex), grades (I′)–(III′), the □/⬨
  glosses and caveats) and the Replies §7 pp. 480–482 passage in full;
  §2 defines four categories (arbitrary smooth GHDs; MGHDs; the selected
  two-sided complete scattering class; complete worlds with terminal-time
  semantics); §3 answers the coordinator question — a same pointed causal
  past does **not** fix ω_t^ex (three-database separation table with
  distinct determination verdicts); §4 gives the translation and its
  obstruction (T-bridge as a separately stated premise; Cat0 trivializes
  the box; Cat1 uniqueness alone kills same-past later-existence
  variation; grade (II′) has no spacetime analogue — exact obstruction;
  grade (III′) splits into restriction / singular MGHD end / terminal-time
  world); §5 separates stage, open cut, and complete world with terminal
  time; §6 gives the positive bridge argument (P1 law-relativity from the
  source, P2 anti-trivialization from the source's own p. 114 principle,
  P3 canonicity of the MGHD) with its conditional conclusion; §7 the
  charitable rival (law-agnostic nomological space) stated at full
  strength plus what it costs and our defeater; §8 keeps ch. 7 worldstates
  distinct from ch. 9 point-profile B; §9 separation table; §10 defeat
  conditions and next tasks. C&R openness is **not** reclassified as
  purely metaphysical; the nomological reading is kept live and shown to
  exclude the openness claim within the selected class.
- `sources.jsonl` — 8 records, all knowledge/README contract fields
  present (validated by script). Full-text records carry version/DOI,
  locators, assumptions, conclusion, proof status, dependencies, related
  IDs, open questions, limits.
- `check_modal_witnesses.py` — finite rational time-line illustration of
  the witness bookkeeping (stdlib, 0.02 s): box holds for all pairs in
  complete models; fails on pairs straddling cuts; across all Cat0
  segments, (IND_ex)-style witnesses exist for 15/15 pairs; open cuts
  have no last moment. Labeled illustration, not a proof.

Root: this `AGENT_REPORT.md`.

## Verification commands and results

- `python3 research/ontology-reconstruction/modal-category/check_modal_witnesses.py`
  — exit 0, 0.02 s (hard limit 15 s / actual 10 s / total 30 s: pass).
  Output tabulates the per-category survey and the anti-trivialization
  witness as described above.
- JSONL contract validation (inline python): 8 records, all required and
  full-text fields present — pass.
- `shasum -a 256` on the local ch. 7/9 PDFs reproduces the prior lane's
  SHA-256 values exactly (94eb9c6f…, 60a8b4d0…) — primary-PDF identity
  confirmed before quoting.
- Direct primary reading this task: ch. 7 all 18 pages from the local
  PDF; Replies §7 pp. 477–482 from Sciendo OA text; Sbierski Defs
  2.1–2.4, Thms 2.6–2.8, Lemma 3.1/3.3 statements from the ar5iv render.
  The project's "Sbierski Lemma 3.1" and "Theorem 2.7" citations were
  verified verbatim against the source.

## Source coverage

Primary: C&R *Nothing To Come* ch. 7 (full-text, direct); C&R "Replies to
Critics" §7 (full-text, OA); Sbierski arXiv:1309.7591v3 (selected
sections, full-text); Choquet-Bruhat–Geroch 1969 (discovery, via crossref
+ Sbierski); Luk–Oh–Yang arXiv:1605.03893 (abstract; Theorem 1.7 only via
the project's SCATTERING_PAIR.md record). Project records: CLAUSES.md,
MAXIMALITY_AND_EXISTENTIAL_OPENNESS.md, NEXT_PHILOSOPHICAL_TESTS.md §1,
RIVAL_PROFILE_AND_REGULARITY_BRIDGE.md, PERSISTENCE_CONVENTIONS.md,
REALM_CONTRAST_IN_SMOOTH_CLASS.md, COMMON_EXTENSION_REPAIR.md,
SCATTERING_PAIR.md, actuality-maximality-review report. Chapter 9's own
PDF was not re-read this task; ch. 9 clauses rely on the two existing
full-text records (CLAUSES.md, coordinator point-profile record).

## Strongest contrary evidence (to my own conclusion)

1. C&R's p. 482 concession plus the unspecified laws of ch. 7 make the
   law-agnostic rival fully coherent: if □ ranges over whatever the
   actual laws permit and the actual laws are cessation-permitting, no
   Einstein–scalar theorem bears on (IND_ex) at all. My §6 conclusion is
   conditional on P1–P3, and P3 (canonicity) is an interpretation, as the
   actuality-maximality-review already insisted.
2. The Replies' "as long as such world states form a distinctive
   ontological category" (p. 481) is a substantive enabling condition I
   could not cash out over physical models; a successful cash-out would
   revive the rival from inside the source.
3. The T-bridge (global temporal function) is my addition, not C&R's;
   without it (DET_ex) is not formulable over GR, so the determinism
   verdict is formalization-relative.
4. Appendix 3 (translation manual) and chs. 1–5 were unread; the free-logic
   behaviour of 'At t′, φ' under non-existing t′ is reconstructed, not
   verified. If the manual treats the box differently, §6 needs revision.

## Limitations

- No new mathematics was proved; Cat1's uniqueness verdict uses
  established re-slicing facts whose coupled-scalar regularity category
  is the lawful-completions lane's audited input, not re-verified here.
- The finite check is an illustration of bookkeeping on rational time
  lines; it proves nothing about continuum categories.
- web-search-prime and serpapi were quota-dead; search coverage leaned on
  scholar_search + exa. No paywalled source was accessed; the Torre 2021
  commentary and Deng/Dorato–Hoefer/Wawer commentaries were read only as
  quoted inside the Replies.
- I did not launch subagents, edit coordination files, or touch anything
  outside the allowed paths.

## Proposed next tasks

1. Read *Nothing To Come* chs. 1–5 and Appendices 2–3 (removes the
   free-logic/At caveat and the □ gloss dependence; largest unread
   dependency of this reconstruction).
2. Cash out the Replies' "distinctive ontological category" condition for
   world states over physical models — the one move that would defeat the
   §7 defeater from inside the source.
3. Audit whether any Luk–Oh–Yang-lineage existence result covers
   boundary/terminal formulations (would make Cat3 internal to a physics
   comparison).
4. Apply §3's database table (ω-block vs J⁻(b) vs B(b)) to the
   constitutive-extent test in NEXT_PHILOSOPHICAL_TESTS §2.
5. Prior-art audit: existence-based indeterminism mapped to development
   categories, 2021–2026 (novelty question only; no claim is made here).

This report is a submission for independent review, not an accepted
completion.
