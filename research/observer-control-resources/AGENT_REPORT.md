# Agent report: observer-control-resources

Claim: `native-control-resources`; shared checkout, owned path only.

## Changed paths

- `research/observer-control-resources/RESULT.md`
- `research/observer-control-resources/AGENT_REPORT.md`
- `research/observer-control-resources/check.py`
- `research/observer-control-resources/output.json`
- `research/observer-control-resources/sources.jsonl`

## Main result

For a faithful full orthogonal register holding all labelled N-element histories, an explicit family of height-two posets forces at least 2^floor(N²/4) distinct slots and floor(N²/4) qubits. This is not a bound for compressed or nonorthogonal observer encodings.

With G=399999/30000000 the accepted ideal single-trial gap, per-model whole-circuit diamond errors e_j satisfy gap_actual >= G-(e_A+e_B)/2. The stated summable allocation budgets each model at 5G/8, retaining a gap at least 3G/8 uniformly in depth. A fixed per-step error only makes the elementary worst-case accumulated bound grow with depth; it therefore fails to certify a persistent gap, without proving loss in every implementation.

## Evidence and checks

Primary-source metadata and read depths are in `sources.jsonl`. The literature comparison is explicitly limited: direct proofs provide the subset count and circuit-error telescope; the named papers are context, not proof substitutes. `check.py` is standard-library-only and bounded at N<=8. It checks all edge subsets for the poset axioms and injective relation encoding, exact counts, geometric series allocation, and detector-margin arithmetic. No external dependencies or broad run were used.

## Limitations and unresolved obligations

The resource model assumes a full orthogonal slot per labelled history. No claims extend to compressed, approximate, implicit, or label-quotiented encodings. The channel bounds assume each component has a supplied diamond-norm guarantee; no physical synthesis or noise model supplies one. Fixed error per stage has no uniform guarantee under this argument. Precursor enumeration, coefficient arithmetic/oracles, reversible workspace, gate count, fault tolerance, hardware rates, energy, locality, and physical access to the inverse circuit remain uncharged or unresolved. No novelty or temporal ontology claim is made.

## Coordinator integration

Planck's independent review and coordinator primary rereads confirm the
mathematical memory/error arguments. Source attribution was repaired: AKN
v1 supplies mixed-state circuit/diamond/telescope results, not a fault-tolerance
threshold theorem. KSW full-text review now has precise locators; KR is retained
only at discovery/context depth because no precise passage was preserved and
the coordinator could not access its DOI. Four fixed budgets are explicit;
summability is sufficient, not a universal necessity claim.
