# AGENT_REPORT.md — read-quantum-theory-and-time

11 November 2026. GLM reading lane, headless run (resumed once after an interruption; state
recovered from the worktree, no work lost). Submission for independent review, not a final truth
claim. No temporal ontology is selected.

## Done and files

- Read the required project files: AGENTS.md, README.md, knowledge/README.md,
  knowledge/NOVELTY.md, research/PARITY_MAP.md, the task brief, and the four flagged notes
  (research/time-direction/fixing-exchange/RESULT.md, research/stein-gr/local-clock/RESULT.md,
  research/horizons/horizons-and-news/RESULT.md, research/horizons/cone-algebras/RESULT.md).
- Read research/what-the-past-can-fix/main.tex in full (all 907 lines: Introduction, Part I
  premises (LC)/(T)/(CB) via parts/becoming_framework.tex and becoming_phil.tex, Parts II–IV,
  sec:direction, sec:truth, sec:revise, sec:defeat, Appendix status table, bibliography), and
  grepped it for quantum content (quantum, GRW, Bell, Everett, collapse, foliat): the paper's
  only quantum anchors are the AQFT category (BFV2003, FV2012) and the citations Bigaj 2008,
  Monton 2006, Savitt 2009, Saunders 2002.
- Wrote `knowledge/reading/quantum-theory-and-time/READING.md` (2,243 words ≈ 3 pages) with
  exactly the five required parts: positions, canonical arguments, open problems, what the
  repository must revise, ten next sources ranked. It answers the special question: GRW-family
  collapse laws single out a *direction* lawfully (time-reversal non-invariance is in the law,
  no boundary condition; Tumulka 2006 lists it among rGRWf's symmetries); no interpretation read
  derives a *present* from its laws — foliation-collapse adds one as extra structure, and the
  bridge from foliation to existence is philosophical.
- Wrote `knowledge/reading/quantum-theory-and-time/sources.jsonl` (22 records) under the
  knowledge/README.md contract.
- Committed exactly: READING.md, sources.jsonl, this AGENT_REPORT.md.

## Search capability check

- `web-search-prime` (MCP): **FAILED** — HTTP 429, "Weekly/Monthly Limit Exhausted", resets
  2026-11-17. Reported as unavailable per instructions; not used for any recorded source.
- `scholar_search` (OpenAlex): **WORKED** — used to verify Wharton–Argaman RMP (arXiv:1906.04313),
  Rideout–Sorkin (gr-qc/9904062), Kastner 1999, and to correct two citation errors before they
  entered the record (an invented arXiv ID for Wharton–Argaman was caught this way: 1905.04831 is
  an unrelated mathematics paper; Rideout–Sorkin is 9904062, not 9904028).
- `exa` web_search / web_fetch: **WORKED** — used for all full-text extraction.
- APS journals page: **WORKED** — verified ABL 1964 (Phys. Rev. 134, B1410) and read its abstract.

## What was read, at what depth

Full-text (partial, via open web extraction; per-record `limits` say which sections):

- Tumulka 2006, rGRWf (arXiv:quant-ph/0406094v2; JSP 125:821–840) — abstract, §1, §2.1–2.2.
- Myrvold, "Lessons of Bell's Theorem" (PhilSci-Archive 12382) — §§1, 2, 5, 6.1, 7, start of 8.
- Saunders, "How Relativity Contradicts Presentism" (author PDF; RIPS 50 (2002) 277–292) — §§1–3.
- Saunders & Wallace, "Branching and Uncertainty" (BJPS 59 (2008)) — abstract, §2.
- Price 2012 (arXiv:1002.0906v3; SHPMP 43:75–83) — abstract, §1, §2.1.
- Wharton & Argaman 2020 (arXiv:1906.04313v3; RMP 92, 021002) — abstract, §I.
- Wüthrich 2013 (arXiv:1207.1490v1) — abstract, §§1–3.
- Bedingham et al. 2014 (arXiv:1111.1425v4; JSP 154:623–631) — abstract, §§I–II.
- Barandes 2026 (arXiv:2602.07402v1) — abstract, §1.
- SEP (secondary): Bell's Theorem (rev. 2024-01-25; §8.2 and preamble), Collapse Theories
  (rev. 2025-09-30; preamble, §§1–2), Everettian QM (rev. 2023-06-20; §§1–2).

Abstract: Wilson 2020 (OUP page), Ismael 2022 (publisher page), Rideout–Sorkin 2000 (OpenAlex),
Kastner 1999 (OpenAlex), ABL 1964 (APS abstract; locator verified).

Discovery (not read; access paths recorded in each record's `limits`): Maudlin,
*Quantum Non-Locality and Relativity* (book inaccessible; reconstructed from SEP §8.2 and an NDPR
review, flagged as a placeholder in READING.md), Bell 1964, Bell 1987, Norsen 2009.

Could not access: Maudlin's book (gated), Wallace's *The Emergent Multiverse* (gated; the only
found copy was on a dubious mirror and was deliberately not used), Wilson's book (abstract only),
Ismael's full text (paywalled), ABL's body (paywalled). No credentials or private repositories
were read; no packages installed.

## Verification commands and results

- `python3 scripts/check_sources.py knowledge/reading/quantum-theory-and-time` → 22 records,
  0 errors, 0 warnings.
- `python3 scripts/check_sources.py --online knowledge/reading/quantum-theory-and-time` →
  8 arXiv IDs and 11 DOIs checked: 0 errors, 0 warnings (identifiers resolve and match recorded
  titles). Fixed on the way: two wrong arXiv IDs caught before commit (see above), ABL locator
  confirmed against APS, arXiv versions pinned (1906.04313v3, 2602.07402v1, plus versions already
  known for Tumulka/Bedingham/Price/Wüthrich).
- `python3 scripts/check_links.py` → 0 broken links.
- `python3 -m unittest discover -s tests` → OK.
- No `sorry`-style or formal claims are involved; nothing here is a proof claim.

## Source coverage and gaps

Covered: Bell/relativity (Myrvold full, Maudlin placeholder), collapse (GRW recall via Tumulka,
flash and matter-density ontologies, foliation question), Everett (Saunders–Wallace, Wilson
abstract), retrocausal/time-symmetric (Price, Wharton–Argaman, ABL, Barandes), presentism/growing
block (Saunders 2002, Wüthrich taxonomy), and one lawful-growth pointer (Rideout–Sorkin).

Gaps by the brief's own list: GRW 1986 and Bell's papers read only at second hand; Wallace and
Wilson at placeholder depth; the Everett open-future question beyond Saunders–Wallace §2
(their §3–4 unread); Wüthrich's collapse-foliation evaluation unread beyond the taxonomy; the
repo's existing Page–Wootters lane not duplicated (out of scope per PARITY_MAP).

## Strongest contrary evidence recorded

- Barandes 2026: the ABL rule is symmetric under reverse orderings, not time symmetry, and
  rests on a single-system/ensemble category error; post-selection manufactures artifacts.
  ABL's own abstract (read) already carries the asymmetry in an ensemble postulate, which
  supports Barandes's direction if not his diagnosis.
- Norsen 2009 (via Myrvold, discovery depth): vigorous skepticism that stochastic theories can
  violate Bell locality without unacceptable nonlocality.
- Wüthrich 2013: presentist uses of collapse-foliation physics survive, in his assessment, only
  in "metaphysically repugnant" forms.
- Price 2012's own scope limits: Everettians and Bohmians escape his time-symmetry→retrocausality
  argument entirely.

## Limitations

- All "full-text" reads are partial web extractions; per-record `limits` name what was and was
  not read. No proof in any read source was re-derived; several proofs (Tumulka §§3–8,
  Bedingham §§III–V) were not read.
- One-interviewer risk: all extraction went through one tool family (exa) plus APS pages; a
  fetch artifact could have truncated mid-document (checked by hand where quotations were drawn).
- Myrvold's printed chapter pages, Saunders–Wallace page range, Bell 1964/1987 venues, Norsen's
  venue: unverified, and recorded as such in sources.jsonl rather than guessed.
- Maudlin's position in READING.md part 1 is a reconstruction from secondary sources and is
  labelled as such; it should not be cited further until the book is read.
- The READING.md section 4 judgments about the repository are this worker's readings, made under
  the standing limitation that all review so far in this project is same-family model review.

## Proposed next tasks

1. Read Maudlin, *Quantum Non-Locality and Relativity* (gated; user-supplied) and replace the
   placeholder reconstruction in READING.md part 1.
2. A worker lane extending the paper's F_L fixing framework to stochastic process laws, with
   rGRWf as the first case (READING.md part 4, second bullet, names the exact open question in
   main.tex sec:direction it would answer).
3. Read GRW 1986 and Bell 1987 directly; verify the two quotations READING.md carries at second
   hand ("a galaxy of such events"; the Lorentz-invariance remark).
4. Read Wallace 2012 chs. on branching/probability and Wilson 2020, then reconsider main.tex
   sec:truth's policy space against branch-relative truth.
5. A short note testing whether a becoming relation defined from rGRWf flashes fails (LC) on the
   GH category while remaining Lorentz-invariant — READING.md part 4, first bullet, flags this as
   the quantum occupant of the paper's conceded rival horn.
