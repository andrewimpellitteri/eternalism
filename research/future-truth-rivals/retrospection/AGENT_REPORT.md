# Agent report: retrospective and GR compatibility reviews

## Files in this lane

- `research/future-truth-rivals/retrospection/RESULT.md` — bounded MacFarlane (2003) clause reconstruction.
- `research/future-truth-rivals/retrospection/REVIEW_PAIRED.md` — independent audit of paired Contracts L/S and author self-assessment.
- `research/future-truth-rivals/retrospection/REVIEW_GR.md` — independent Placek Definition 15 / history-consequence proof review.
- `research/future-truth-rivals/retrospection/sources.jsonl` — source register, including author page and 2007 Garden preprint records.
- `research/future-truth-rivals/retrospection/AGENT_REPORT.md` — this report.

## Findings

The MacFarlane lane read selected original clauses and the sea-battle example in the 2003 published offprint. It distinguishes assessment-sensitive utterance truth from fixed-proposition persistence. The paired-contract review confirms Contract S is a current-assessment supervaluation over `C_b`, not MacFarlane's full double-context semantics; it flags that mapping the later PDE compatibility class to MacFarlane's branching histories remains unestablished. The paired contract explicitly treats its designated complete realization as a mathematical comparison parameter, not an ontic postulate.

The author-page record is corrected: the self-assessment note appears under entry 30 for “Truth in the Garden of Forking Paths,” and entry 41 lists the 2003 article. The linked author-hosted preprint is the 26-page version dated 28 January 2007. Its §1, printed pp. 1–2, gives the shortcomings the author attributes to the 2003 argument. This is recorded as MacFarlane's self-assessment, not as a refutation. The later chapter's full argument remains unread.

The Placek review checked the exact causal criterion and 1-Lipschitz endpoint proof. The core proof works on the stipulated cylinder, with immediate omitted case splits when the chain attains its infimum or supremum. A direct page-image check of printed p. 200 (`/private/tmp/eternalism-placek-def15.png`, rendered from `/private/tmp/eternalism-placek-2014.pdf`) resolves the Definition 15(2a) interval: it is `t_{>x} ∩ t_{<y}`. The earlier review's `≥x` correction was wrong; the RESULT.md's `≤x` transcription is the typo. The nonempty-chain convention remains unconfirmed in the printed Definition 15; if empty chains are admitted, clauses 2(b) and 2(c) fail in this open cylinder. Definition 17 then yields no splitting pairs, and Definitions 19–23 yield a unique g-history, conditional on the nonempty-chain convention. Coordinator integration will add the attained-endpoint case split to the GR result/report and keep the empty-chain qualification in synthesis. No atlas-level GR correspondence is claimed.

## Evidence and checks

- Read original Placek (2014) PDF: Definition 15(2a)–(c), Definition 17, Condition 18, Definitions 19–23; visually inspected printed p. 200 at the supplied local page-image path above.
- Verified MacFarlane's current Papers page and its linked `garden.pdf` author preprint; recorded exact versions and locators.
- Parsed every line in `sources.jsonl` as JSON and ran `git diff --check` on the owned retrospection directory.
- No board, manuscript, shared seed, runner, or files outside the lane were edited. No commits were made.

## Remaining gates

- Correia–Rosenkranz *Nothing To Come*, chapter 7, remains open and unread in full.
- MacFarlane's 2007/2008 revised chapter was checked only in §1; the complete revised argument remains unread.
- Placek's later topology, chart, generalized-manifold, and tangent-space construction remains outside the GR proof review.
