# Agent report: creative-covariant-stopping

## Outcome

The stopping-time and hidden-record hypotheses were defeated by prior work or direct consequences. A third route produced an exact extension theorem: the complex transitive-percolation premeasure on doubly-principal labeled cylinders extends to a finite complex measure on the generated sigma-algebra iff p is in [0,1]. For p outside that interval, comparison with real transitive-percolation orders and positive association gives a finite doubly-principal block family with total seam weight above one; repeated concatenation makes total variation unbounded. Restriction then excludes extension on the larger labeled reduced-poscau algebra. Dowker–Zalel (arXiv:2212.01149v2, §§III.4 and V) pose this question and report inconclusive/numerical criteria. The proof is exact; global novelty priority is unverified.

The result concerns the labeled doubly-principal cylinder sigma-algebra \(\widetilde{\mathcal R}_p\), where the subscript p is the authors' notation for the posts algebra. It does not rule out a complex measure defined only on its covariant intersection \(\widetilde{\mathcal R}_p\cap\mathcal R\). It is a measure-extension theorem, not an observer-instrument result, a full decoherence-functional result, or an ontology result.

## Files written

- `claim-and-defeat.md`: two failed hypotheses, the all-parameter proof, finite certificates, six-part novelty contract, primary prior-art comparisons, defeaters, and interpretation limits.
- `exact_checks.py`: standard-library exact rational checks for the CSG stopping witness and HMM record non-Markov example.
- `reduced_poscau_obstruction.py`: independent exhaustive enumeration of all 1024 forward relation masks on five labels; verifies the principal-order histograms and exact weight inequalities.
- `principal5_certificate.csv`: 40 explicit naturally labelled principal orders with relation masks and link, minimum, relation, and exponent counts.
- `sources.jsonl`: versioned source records with assumptions, conclusions, dependencies, open questions, and locators.

## Evidence and checks

- Read the project instructions, task brief, README files, novelty standard, and integrated causal-set/novelty-audit material. The worktree-local task-table query refused because its table predates this task; the task brief was read in the main checkout.
- Read the relevant sections of Rideout–Sorkin gr-qc/9904062v3, Brightwell et al. gr-qc/0210061v2, Brightwell–Luczak arXiv:0901.0240v3, Dowker et al. arXiv:1910.07292v2, Dowker–Zalel arXiv:2212.01149v2, Dowker–Johnston–Surya arXiv:1007.2725v1, and Surya–Zalel arXiv:2003.11311v1. The fixed-causet Brightwell–Luczak companion and Kemeny–Snell were discovery/abstract-level only and are not used in the theorem.
- The five-element exhaustive script returned 40 principal orders with bivariate histogram `{(5,0):1,(6,1):3,(6,2):6,(6,3):4,(6,4):3,(7,3):7,(7,4):8,(7,5):6,(8,2):1,(8,6):1}`. It writes all 40 relation sets to the CSV certificate. Coordinator/reviewers independently reproduced the histogram using different enumeration methods.
- At p=(1+i)/2, the script verifies \(r_5=105/128+9/(8\sqrt2)\) and the capped block weight \(W=9/16+105/(128\sqrt2)>71/64>1\). For general p outside [0,1], the proof gives \(Z_k(a,b)\ge t^k c_s^2\), with \(c_s=\prod_{j\ge1}(1-s^j)>0\); therefore a finite k has capped weight above one. The all-parameter argument was independently checked by the coordinator and two native reviewers, including endpoint-probability identities on small real DAGs.
- `exact_checks.py` also passed: finite stopping probabilities are 2/3 and 1/3 for the three-element example, and HMM record probabilities are 15/28, 7/12, and 9/16.
- `python3 scripts/check_sources.py research/creative/covariant-stopping` returned `1 files, 7 records: 0 errors, 0 warnings, 0 info`. The final isolated-worktree online rerun, `python3 scripts/check_sources.py --online research/creative/covariant-stopping`, returned `1 files, 7 records; 6 arXiv IDs and 2 DOI lookups checked: 0 errors, 0 warnings, 1 info`. A coordinator-side run separately reported 8 unreachable-source warnings; the exact rerun here resolved them. The cited arXiv versions and locators were also checked in browser sources.

## Limitations

- Global novelty priority remains unverified. Targeted search found no later proof, but Dowker–Zalel is a close prior-art defeater and their conjecture covers the same broader conclusion.
- The all-p theorem covers the labeled posts/doubly-principal cylinder sigma-algebra and the larger labeled reduced-poscau algebra. It does not establish existence or nonexistence on the covariant intersection alone.
- The HMM recorder remains an ordinary hidden Markov illustration; no nontrivial marked Bell-causal growth model was built.
- No temporal-ontology, passage, determinism, clock-time, thermodynamic-arrow, or general quantum-gravity conclusion follows.
