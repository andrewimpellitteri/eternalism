# Agent report: tense-domain semantic investigation

## Files changed

- `research/future-truth-grounding/tense-domain/RESULT.md`
- `research/future-truth-grounding/tense-domain/sources.jsonl`
- `research/future-truth-grounding/tense-domain/AGENT_REPORT.md`
- `research/future-truth-grounding/tense-domain/check_tense_domain.py`

## Evidence and decisive finding

Read Loss's original PMC HTML, selected full text: §§2.2–2.3 and §3, including the growth-domain clause, stage-relative tense clauses, quantifier-troubles diagnosis, shifting-timeline repair, and conclusion. Exact HTML line locators and bibliographic version are in the lane source record and result. The full-text record now includes `dependencies`, `related_source_ids`, and `open_questions`.

The finite three-stage model uses only growth stages and `F_g`; it has no within-block `F_t`. A frozen quantifier over the initial domain cannot witness a fresh entity at a later stage, so `F_g ∃x ¬PastExists_g(x)` is false in the toy; letting the quantifier range over the evaluated later stage's domain makes it true. At terminal stage `s2`, the formula is false even with a shifting domain because there is no later stage. This explicitly blocks any claim that the finite toy validates perpetual growth. The script labels the frozen and shifting cases with the relevant Loss passages and labels the terminal case as a toy-only consequence.

## Checks

Ran `python3 research/future-truth-grounding/tense-domain/check_tense_domain.py`; output confirms frozen=false at `s0`, shifting=true with witness `(s1,b)`, and terminal shifting=false at `s2`. Parsed the source JSONL and checked the three required fields. The source-labeled counterexample is explicitly attributed to Loss's diagnosis/reconstruction, not presented as an independent full audit of Briggs–Forbes.

## Coordinator synthesis fidelity

Read `research/future-truth-grounding/coordinator/RESULT.md`, §4 “Stage-sensitive semantics.” Its synthesis is faithful to this lane: it describes the frozen-domain failure and stage-sensitive repair as semantic compatibility, not an explanation of passage, and explicitly cautions that a finite terminal toy does not validate perpetual-growth axioms. The updated result now states the terminal-stage limitation and makes clear that it contains only `F_g`, with no within-block `F_t`. I found no substantive mismatch requiring a coordinator-file edit.

## Dense-stage stress test

Added `DENSE_STAGE_CHECK.md` after checking Loss's original clauses at PMC HTML lines 149–182 and footnote 17. The time-indexed dense model satisfies (D), (T1)–(T3), time-domain inclusion, and multiple futures via an extension-ordered past-function tree. Every extant entity is already present at an earlier stage, so the displayed assumptions do not entail (GB1), (GB3), or (GB6); (GB2), (GB4), and (GB5) hold. The model relies on adding new times below a constant latest time; this meets the listed formal clauses but may violate the intended append-at-the-edge reading. The result is recorded as a conditional underspecification, not a paper-error claim. A first-existence witness is an exact repair; strict latest-time advance is sufficient in the one-sorted `D=T` model, while the separate-sort case needs a freshness link.

## Coordinator freshness repair review

Reviewed `research/future-truth-grounding/coordinator/FRESHNESS_REPAIR.md` and its causal/branching qualification in `TWO_ORDERS.md`. The principal-ideal proof is valid: if `D_s=↓p_s`, `D_r⊊D_s`, and `p_s∈D_r`, then `p_s≤p_r`; since `p_r∈D_r⊆D_s`, also `p_r≤p_s`; antisymmetry forces equality and hence equal principal ideals, contradicting strict inclusion. Therefore `p_s` is absent from every R-earlier domain and witnesses fresh existence. The condition excludes the dense insertion model because its domains omit portions below the constant endpoint and are not full principal ideals. For a language with non-event objects, the report correctly requires a typing/identity bridge before the event-label witness establishes the desired existential claim.

The causal application is sound as a separate event-relative proposal: in a causal partial order, `J⁻(b)=↓b` and a strict causal successor `c` is absent from `J⁻(b)` while belonging to `J⁻(c)`. This does not make causal advance the branching-stage relation. As `TWO_ORDERS.md` illustrates with the Minkowski diamond, incomparable spacelike events may both belong to one spacetime and share a future; a tree of incompatible histories cannot represent that compatibility without extra structure. The repair establishes a fresh center in the proposed causal-past domain, not a branch-selection account or an argument for passage. This clarifies the dense-stage result: full-prefix domains match the append-at-the-edge interpretation and exclude retroactive insertion, so the countermodel is no attack on Loss's intended account.

## Limitations and unresolved questions

- This is selected full-text source reading, not a complete audit of Loss or the Briggs–Forbes 2012 chapter.
- It does not establish that the toy domain condition is metaphysical generation, or that stage semantics is ontologically correct.
- It leaves supertruth across branches, future-contingent truth values, retrospective reports, names under nonexistence, and relativistic partial orders untreated.
- The toy's `PastExists_g` is an explicit stage-history predicate. It should not be read as an analysis of within-block pastness or as a solution to the full two-dimensional tense semantics.
- Loss's displayed (D), (T1)–(T3) do not themselves state the principal-ideal/full-prefix condition; the coordinator's repair supplies it as an explicit sufficient condition aligned with the intended append-at-the-edge interpretation.
