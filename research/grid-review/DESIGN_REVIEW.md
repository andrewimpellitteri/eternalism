# Independent grid review

2026-10-19. Reviewed `grid/CONTRACT.md`, `grid/axes.json`, and
`scripts/grid.py` as present after snapshot `34f0357`. Later concurrent edits
may supersede these findings. This is an infrastructure/design review, not a
novelty audit. No core files, live result records, or GLM launches were changed.

## Immediate implementation findings

The read-only Luna runner reviewer independently inspected the same gates.
The coordinator reproduced the representative cases using in-memory mocks.
The following are regression requirements for `grid-regression-tests`; an
empty live result directory does not exercise them.

| Finding | Current mechanism | Required behavior |
|---|---|---|
| Invalid records can promote | `cells()` discards the problems returned by `results()` | Fail closed for affected cells; report errors rather than generating downstream tasks |
| Evidence shape is barely checked | Three empty predecessor objects and five empty queries pass length checks | Check required fields, types, allowed depths and meaningful nonempty values; content adequacy remains human review |
| Unknown/unassigned records promote | `adv` accepts any non-`A-` ID with `advance` | Validate canonical IDs and assignment/output ownership before promotion |
| Orphan or stale survivors expand | `s2` checks only an `A-` prefix and `survive` | Require the exact eligible parent claim/version and assigned independent review |
| Conflicting duplicates silently decide outcomes | `verdict()` chooses the most conservative label; `recs[0]` supplies the claim | Deduplicate identical copies; quarantine substantive conflicts for adjudication, preserving provenance |
| S2 can re-enter adversarial generation | Every non-`A-` advanced record is eligible | Enforce the declared finite stage graph, or explicitly specify recursion/termination |
| Invalid kill reasons suppress cells | Any truthy `kill_reason` passes | Enforce the enum and require an auditable reason; invalid kills are not coverage |

Minimal malformed record currently accepted by `contract_problems()`:

```json
{"cell":"S1-P01-B01","verdict":"advance","claim":"C","predecessors":[{},{},{}],"defeat_queries":["","","","",""],"smallest_instance":"x","bridge_premises":[]}
```

It omits `move`, `falsifier` and predecessor content. A validation pass must not
be described as evidence that its claim or citations are correct.

Additional robustness tests: non-object JSON, wrong field types, missing/unknown
IDs, repeated assignments, invalid batch sizes, dry-run no-write behavior and
concurrent coordinator reservations. Test concurrent append safety in isolated
temporary files, never by racing the real board. Reservation/append should be
one locked transaction if multiple coordinators may generate batches.

## Resolve contract choices before fixing expectations

1. **Stage verdicts:** the contract's general table lists `kill/hold/advance`,
   while adversary briefs use `kill/survive`. Document each stage separately.
2. **Expansion cardinality:** CONTRACT describes ontology × move; the runner
   and README currently use ontology only. Decide whether moves are an axis
   (54 cells per survivor) or a selected field (9); tests should follow that
   decision rather than silently choosing.
3. **Transfer direction:** 105 unordered family pairs are a defensible batch
   envelope, but a transfer claim must identify source → target. Neither both
   directions nor their equivalence follows from an unordered ID.
4. **Source-blind review:** independent discovery first is useful; after that,
   show the proposer evidence for source-correspondence checks. Permanent
   blindness is not a substitute for inspecting the actual predecessor.

## Scientific and philosophical gate improvements

- A family label must be instantiated as a model/version, domain, dynamics,
  symmetry/observer structure, boundary conditions and access protocol before
  substantive advancement. Record a baseline and one assumption perturbation.
- Require a precise predecessor-to-candidate delta and a non-corollary argument.
  Citation/search counts are minimum activity logs, not sufficient evidence.
  A critical unread paper means a source-check hold, not a negative finding.
- Separate passive record equivalence, intervention equivalence and ontological
  equivalence. Any map must preserve the declared objects and observables.
- An explicit bridge argument is eligible philosophy. Reject an unargued or
  circular leap, not every claim whose significance uses a philosophical
  premise. A conditional argument may still be known, trivial or unsound.
- Disambiguate B03 (determinism/settled truth/existing history), B05 (present
  versus unrestricted truthmakers), B10 (which equivalence?) and B11 (which
  openness?). P11's foliation status is model-dependent, not shared by every
  relativistic collapse or Tomonaga–Schwinger formulation.
- Pin axes content/version in each assignment and result. Record semantic
  duplicates at claim/domain/assumptions/access/delta level. Neither rephrasing
  nor agent agreement creates independent evidence or a new idea.
- Give broad cells a capped search/expansion budget. Provider/search failures
  are operational limitations, never evidence that a literature region is empty.

## Control-label audit

Independent advisory agents supplied useful control proposals, but their gold
labels also need checking. In particular, the proposed inference “presentism +
truthmaker maximalism + no abstract truthmakers implies no truthmaker for a past
truth” is **not valid from those premises alone**. A stipulated present concrete
record could be its truthmaker unless further premises rule that out. Whether
such records genuinely suffice is the philosophical issue, not something to
assume away in a supposedly independent gold label. Preserve this as a control
against accepting agent-generated labels by agreement.

See `controls.jsonl` for bounded calibration cases. They are synthetic except
where a repository predecessor is explicitly identified. They are not claims
of new results, and a control passing does not show research performance.
