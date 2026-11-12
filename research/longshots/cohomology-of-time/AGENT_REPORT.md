# AGENT_REPORT — longshot-cohomology-of-time

10 November 2026. GLM worker, one task, one worktree. Submission for independent review.

## Done and files

- Read the shared docs (AGENTS.md, README.md, knowledge/README.md, knowledge/NOVELTY.md),
  the task brief (`python3 scripts/agents.py brief longshot-cohomology-of-time`), and the
  seed note `research/stein-gr/local-clock/RESULT.md`.
- Read the Fewster–Verch cohomology remark and wedge-connectedness at source, and the
  Sanders paper it cites, at source. Surveyed later work on cohomology of/on spacetime
  categories (Becker–Schenkel–Szabo; Ruzzi line).
- Stated the simplest precise cohomology candidate for the germ-precedence preorder and
  computed it for the two toy classes; verdict: **relabelling**, lane closed per the
  brief's question (4).
- Files (all inside the owned directory):
  - `research/longshots/cohomology-of-time/RESULT.md` — claim contract, six-part form.
  - `research/longshots/cohomology-of-time/sources.jsonl` — 5 source records.
  - `research/longshots/cohomology-of-time/AGENT_REPORT.md` — this file.

## Search capability check

- `web-search-prime` (Z.ai): **failed** — MCP error -429, code 1310, "Weekly/Monthly
  Limit Exhausted. Your limit will reset at 2026-11-17 10:00:29". Tested once at start
  with a relevant query; recorded here; not used further.
- `scholar_search` (openalex/arxiv/crossref): **worked**; used for all source discovery.
- `webfetch` (ar5iv.labs.arxiv.org, arxiv.org/abs): **worked**; used to read primary
  texts. One wrong arXiv ID guess (1004.4819) was caught at fetch and corrected via
  scholar_search to 0911.1304; no invented citation entered the records.

## Source coverage and read depths

- lc-coh-fv2012 (Fewster–Verch, arXiv:1106.4785v3 / AHP 13 (2012) 1613–1674):
  full-text via ar5iv; the conjecture sentence is in §1 (not §2.3 as the brief said);
  §2.3 Props 2.4/2.6 give the Cauchy-wedge connectedness; footnote 5 already builds
  monotone ℕ-valued functions on the spacetime category (object-level ancestor of
  "clocks").
- lc-coh-sanders2010 (Sanders, arXiv:0911.1304v2 / RMP 22 (2010) 381–430): full-text
  §1–§3.4; Theorem 3.15 classifies Dirac-structure freedoms by H¹(SSpac, ℤ₂) of the
  nerve; Remark 3.16 expects nonabelian cohomology for general freedoms.
- lc-coh-bss2017 (Becker–Schenkel–Szabo, arXiv:1406.1514 / RMP 2017): full-text
  abstract–§3; differential cohomology *on* Loc^m for gauge/gerbe freedoms.
- lc-coh-ruzzi2005, lc-coh-rrv2012: abstract depth only (labelled as such).
- Negative searches (2026-11-10, scholar/openalex + arxiv): no source found applying
  cohomology to germ preorders, becoming relations, or local clocks.

## Verification commands and results

Full ar5iv texts were saved by the fetch tool and grepped rather than trusted from
memory; representative checks:

```bash
grep -n -i "cohomolog" <saved FV text>
#   -> line 345/347: conjecture sentence + Sanders pointer; line 3167: §6.2 eta remark
grep -n "Sanders" <saved FV text>; sed -n 4600,4660p <saved FV text>
#   -> ref [48] = Sanders, The locally covariant dirac field, Rev. Math. Phys. 22, 381-430 (2010)
grep -n -i "cohomolog\|Stiefel" <saved Sanders text>
sed -n 1860,2075p <saved Sanders text>
#   -> §3.4 nerve cohomology, Theorem 3.15, Remark 3.16; refs [33] Roberts-Ruzzi, [38] Segal
```

arXiv versions confirmed on abstract pages: 1106.4785v3 (v1 23 Jun 2011, v3 8 May 2012);
0911.1304v2. No computation scripts were needed; all constructions in RESULT.md are
on-paper and labelled conditional where they are unverified.

## Strongest contrary evidence

- The FV/Sanders/BSS line shows cohomology of spacetime categories *is* fruitful — so a
  blanket "cohomology of Loc is empty" claim would be wrong; the honest negative is
  narrower: the mechanism needs non-rigid coefficient objects, which clock targets lack.
- FV's footnote-5 monotone χ functions mean any claim that "monotone structures on Loc
  are new" would be false; this lane claims nothing of the sort.
- Sanders and Ruzzi lines (poset cohomology over causally ordered regions) are the
  closest family to the germ-preorder idea; if any of it has been applied to germs by
  later authors, the negative result would need re-checking. Searches did not find that.

## Limitations

- Lemma T/T′ (transplant constructions) use two standard facts flagged for verification
  at source (split-form Gaussian normal coordinates; GH of ℝ × Σ with −dt² + complete h,
  via FV Prop 2.1's own citation) and a smooth-interpolation step not written out in
  full. Computation A is conditional on them; the relabelling verdict is not.
- The dust-FLRW scalar-curvature decrease (trace identity R = 8πGρ, ρ ∝ a⁻³) is used as
  textbook knowledge and was not verified against a specific source.
- The ball-extremal certificates were not checked against the curvature-monotonicity /
  generic-condition literature; they may have cousins there.
- BSS read via ar5iv; version number and page range not pinned from the journal site.
- Same-model review only: this work has not been checked by anyone else.

## Unresolved questions

- Does the mixed-sign case of Lemma T′ hold (does every class-B germ chain-connect to
  the flat germ through one-sign intermediates)? Affects π₀(P(B)) = 1, not the verdict.
- Whether the note's Theorem 4 survives independent review (its own limits mention a
  repaired error and a sketched gluing argument in the connected category).

## Proposed next tasks

1. Verify (F1)/(F2) and the FLRW trace identity at source (small reading task).
2. Search the singularity-theorem/generic-condition literature for curvature-monotone
   conditions matching the ball-extremal certificates (would settle the only novelty
   increment found).
3. Optional: formalize "thin category with initial object ⇒ contractible nerve" in Lean
   as a reusable certificate for no-local-clock checks on discretized classes.
