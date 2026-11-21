# Agent report: causal production review

## Files changed

- `research/ontology-reconstruction/causal-production-review/RESULT.md`
- `research/ontology-reconstruction/causal-production-review/AGENT_REPORT.md`

No other project files were changed. No Git mutations, installs, or additional agents were used.

## Evidence and checks

- Read `AGENTS.md`, `README.md`, `knowledge/README.md`, `knowledge/NOVELTY.md`, and the output of `python3 scripts/agents.py brief ontology-causal-production-review`.
- Audited `research/ontology-reconstruction/coordinator/causal-production/RESULT.md`; reviewed candidate SHA-256: `18d6c514f239f451417860fe6dd331cd6e5c161c0438b0a7e6547789e76b522c`.
- Independently recomputed the finite-model marginals, conditionals, C1/C3/C4 instances, reverse C4* value, and the separate C1-failure example by hand; all displayed arithmetic checks.
- Read selected passages directly in `/private/tmp/eternalism-tooley-1997.txt`: §3.2 (printed pp. 59–60), §4.5.1–4.5.3 (pp. 104–111), and §4.6.1 only (printed pp. 112–116; PDF pages 129–133); §4.6.2 was not audited. This is selected full-text reading from an extraction, not a whole-book audit or collation against the original pages. No external research was conducted.

## Strongest finding

The toy model validly rebuts only a bare ordinary-probability entailment from C1/C3/C4 to C4*. Its structural equation and shared exogenous distribution already stipulate directed downstream dependence and cross-law root invariance. It therefore does not answer Tooley’s source-faithful explanatory claim that temporal actuality grounds the law-counterfactual asymmetry. The result acknowledges most of this; make the model’s built-in direction/invariance explicit wherever its finding is stated.

## Limitations and unresolved question

The audit does not settle whether Tooley’s temporal-actuality explanation is uniquely adequate, whether an independently defended non-Humean account of directed governance can explain the cross-law comparison equally well, or how the supplied extraction matches the original book pages. In the follow-up, I read `research/ontology-reconstruction/coordinator/causal-production/LAW_VARIATION_TEST.md` only. Its upstream compatibility control is consistent with the stated causal-role boundary, but both the growing account and a directed-governance rival can preserve the earlier antecedent and revise the later dependent state; the control alone does not adjudicate between them. The coordinator’s broader source provenance and substantive law-variation comparison remain outstanding.
