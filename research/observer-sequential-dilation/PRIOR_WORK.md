# Prior correspondence and the actual delta

24 October 2026. No novelty or exhaustive priority claim.

| Predecessor | Read depth / exact locator | What transfers and what does not |
| --- | --- | --- |
| Ozols, Roetteler, Roland, [Quantum rejection sampling, 1103.2774v3](https://arxiv.org/html/1103.2774v3), 8 September 2011 | Full text at Section 4.1, Eqs. (11)–(15), and Section 4.2 Eq. (16) | Controlled flag rotations reweight known amplitudes coherently; inverse preparation is a resource. We use unamplified heralding, not their optimal query theorem or an efficiency guarantee. |
| Gudder, [Causal set approach to discrete quantum gravity, 1204.5767v1](https://arxiv.org/html/1204.5767v1), 25 April 2012 | Full text at Section 5, Eq. (5.1), Theorem 5.1 and displayed proof | Sum-one transitions give amplitude products and consistent history functionals. Their normalization is not automatically the trace-one normalization of an orthogonal-register Born state. Their unlabelled-path/multiplicity presentation is not silently identified with our labelled precursor enumeration. |
| Project [coherent growth note](../event-filter-resources/COHERENT_GROWTH.md) | Project artifact inspected, existing analytic isometry criterion | Raw transition amplitudes can give isometric columns only with squared-row normalization. We change the encoding to square-root modulus times phase and charge heralding. This is an auxiliary simulator, not a new dynamics theorem for the scalar process. |
| Project [postselection boundary](../observer-postselection-boundary/RESULT.md) | Accepted analytic representation and reviewed finite instrument; predecessor commit ffb48d5 | Supplies the common variation-based phase state and positive reference state. The new task replaces arbitrary terminal-state preparation with finite transition operations and replaces its free final projector with a scaled reverse preparation. |

The contribution in this lane is the explicit combination of known dilation
and coherent reweighting with the matched pair's summable row bound. Its
forward and reverse losses telescope to a nonvanishing finite-protocol rate.
This is neither a new general rejection-sampling algorithm nor a verified
physical causal-set observer. Primary experiments, SDP optimality proofs,
hardware circuits and new gauge dynamics were not reproduced.

## Checking lineage

The finite checker reuses the reviewed dyadic interval arithmetic and actual
model transition evaluators from the matched-norms/diffuse lanes, pinned by
SHA256 and verified against commit ffb48d5. It independently assembles new
forward vectors and reverse readout contractions and compares them with
terminal target formulas; it is not an independent implementation of the
underlying causal-set recursion. Exact rational toy controls avoid that
shared dependency. Analytic all-depth claims use named prior inequalities,
not a 357-history extrapolation.
