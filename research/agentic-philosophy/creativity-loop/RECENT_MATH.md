# What recent LLM mathematics suggests for creative research

Checked 22 October 2026. Selected primary-method passages and a released
interaction were inspected; experiments and proofs were not reproduced here.
These sources support design choices, not a measured benefit for philosophy.

| Primary example | Concrete move / evidence inspected | Transfer to this repo (our inference) |
| --- | --- | --- |
| [Aletheia, 2602.10177v2](https://arxiv.org/html/2602.10177v2), Sections 2–4 | Separates generator, verifier and reviser in natural language, with abstention. The authors report both useful strategy suggestions and many failures or unintended interpretations. Their significance taxonomy is separate from autonomy. | Ask for strategies as well as sublemmas; review a clean submitted statement; preserve “not solved”. Check intended question separately from formal validity. |
| [Lee–Seo, 2602.02450v2](https://arxiv.org/html/2602.02450v2), Section 3.1 and AI-contribution passages | A difficult inequality is recast through a dual set and log-convex geometry. The authors identify agent input and subsequent human proof work. A linked Lean artifact is reported, not built or audited here. | Explicitly ask for a new auxiliary object or representation that makes a hard obstruction tractable. Keep useful statements even if the initial proof needs repair. |
| [Released Lee–Seo interaction](https://raw.githubusercontent.com/google-deepmind/superhuman/refs/heads/main/aletheia/LeeSeo26/LeeSeo26.tex), second user prompt / “Surface Geometry” / “The Dual Set” | Inspected public prompt/output passages actually introduce a surface and supporting-plane dual. These are released final outputs, not a complete experimental log; correctness was not independently established. Mutable main snapshot, no commit pin obtained. | A concrete example of an object-changing search move. Preserve public claims and corrections; do not pretend to possess or need private model thinking traces. |
| [AlphaEvolve, 2506.13131v1](https://arxiv.org/html/2506.13131v1), Sections 2.1–2.5, discussion | Searches programs, constructors or search algorithms; keeps evaluated candidates and diverse lineages; uses increasingly costly checks. Automated evaluability is an explicit limitation. | Retain several mechanisms and useful failures. Apply exact evaluators to mathematical subclaims, with separate unresolved physical and philosophical gates. No ontology “fitness score”. |
| [Matrix-exponent follow-up, 2608.16884v1](https://arxiv.org/html/2608.16884v1), Sections 3–4 | Human reformulation makes a larger optimization accessible; AlphaEvolve refines its algorithm and starts from parent solutions. The reported bound is separately certified using rational arithmetic. Code release was described as forthcoming in the inspected version. | Search the formulation and the solver; reuse partial progress; separate exploratory numerical evidence from the final certificate. Report the actual human/coordinator contribution. |
| [FunSearch, primary announcement](https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/), 14 December 2023 | Earlier LLM/program/evaluator/database loop. | Predecessor, not a 2026 discovery or a new architecture we invented. |

One timely perspective is Francesco Maggi's [18 October 2026 guest essay](https://terrytao.wordpress.com/2026/10/18/will-it-be-a-golden-age-or-a-dark-age-for-mathematics-and-science/)
on Tao's blog. It argues for preserving human understanding and independent
scientific activity. It is an opinion contribution by Maggi, not an empirical
capability evaluation authored by Tao.

## What “creativity” means operationally here

The useful observable behaviors are changing representation, inventing an
auxiliary object, importing a relevant technique, proposing a strategic lemma,
and recombining tested fragments. None establishes subjective creativity or
reliable autonomous research. The distinction matters: a system can produce a
valuable new route while still requiring specialist work on validity and
importance. Polished novelty narratives are not evidence.

Our existing playbook already has source audits, claim contracts, countermodels
and semantic checks. The addition is a bounded **generate → test → transform
→ retain/recombine** loop before final selection, exercised on a live question.
Success can be a sharper obstruction or one missing physical premise.

## Philosophy and physics have several different checking surfaces

Some subclaims are as checkable as mathematics: consistency, normalization,
invariance, countermodels, limits and conservation laws. Citation fidelity
can be checked against an exact passage. Whether a proposed instrument is
physically available is another question. Whether physical equivalence implies
ontological equivalence is an explicit philosophical argument. Keep these
surfaces separate and allow unknown outcomes; do not turn them into a single
reward signal. This is our proposed adaptation, not a result established by
the cited systems.

The live pilot is not an evaluation of LLM creativity or an ablation against
the old workflow. It uses a coordinator and two native sidecars, including a
fresh-context proposer. They are not demonstrated independent model families.
It is an auditable example of using the capabilities differently.
