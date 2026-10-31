# Coordinator review: reject Lemma P's whole-past inference

28 October 2026. Reviewed worker submission in the isolated constraints
worktree, branch agent/lawful-completions-constraints. Submission remains
in review. The source inventory is useful at its stated reading depths;
this note does not independently certify the extracted gluing theorems.
The proposed Lemma P is not usable as written.

## 1. P1 does not preserve the entire causal past

The proof claims that preserving data on an open collar O of
Sigma∩J^-(b) implies J^-(b)⊂D(O). This is false even in Minkowski spacetime.
Set b=(0,0), Sigma={t=−1}, and O={t=−1, |x|<1+delta}, delta>0. O contains
the entire past-cone footprint (the closed unit ball) with an open collar.
Choose p=(−T,0), T>2+delta. Then p≪b. An outward future null ray from p
meets Sigma at radius T−1>1+delta and misses O. Thus p∉D^-(O); since p is
before Sigma, it is not in D^+(O) either. Consequently p∉D(O).

Knowing that every past-directed curve from b meets O gives b∈D^+(O).
It does not say that every future-directed curve from an earlier p meets O.
Following one curve from p toward b cannot control the other curves used
in the universal quantifier defining D^-(O). This is precisely the full-past
versus diamond trap in CONTRACT.md, and the footprint collar does not fix it.

## 2. P2 is incompatible with its future target

The target y=gamma_(b,u)(T), T>0, is timelike future of b. A past-inextendible
causal curve from y can follow gamma backward through b, then continue to
Sigma. Its crossing lies in Omega⊂O. Since Sigma is Cauchy, the curve crosses
Sigma once. The shell C⊂Sigma\cl(O) is therefore avoided by this curve.
Hence y∉D^+(C). This directly contradicts P2. Moving the observer over the
annulus does not remove the past curve through b.

The relevant possible placement for a perturbation is y∈J^+(C), meaning
that C can influence y, not y∈D^+(C), which requires every past curve to
meet C. Replacing D by J removes this inconsistency but supplies no new
control theorem or whole-past matching proof.

## 3. Coupled sources cannot be frozen during the metric solve

For scalar initial data with field value phi and normal derivative Pi,
mu=1/2(Pi²+|Dphi|_h²)+V(phi), and J involves Pi Dphi (up to convention).
Changing the spatial metric h changes mu and the geometric constraints.
A prescribed-source solve for the vacuum/general constraint map with
sources calculated using the OLD metric does not by itself solve the
coupled Einstein–scalar constraints for the NEW metric. One needs a coupled
implicit-function theorem (with its correct linearization and kernel), a
fixed-point argument, or a verified parametrization addressing this metric
dependence. The same 'verbatim' claim across scalar, Maxwell and Vlasov
requires model-specific checks; their matter constraints are different.

## 4. Propagation support is not pointwise nonvanishing

The claim that a retarded scalar Green kernel is nonzero at every timelike
separation is false in general: the massless wave equation in 3+1 Minkowski
spacetime has Huygens support on the null cone. A nonzero admissible
variation of a relational observable requires an actual response/control
argument, with the variation of the evaluation geodesic included. Conditional
nonzero derivative is sufficient once an exact matched family exists;
causal reachability alone is not sufficient.

## Integration verdict

Do not accept or cite Lemma P, its A/B conclusions, or its claimed coupled
localization composition. Preserve the source audit with exact access gates,
and replace the construction claim by these named missing steps. The broad
main target remains open; these failures neither prove impossibility nor
identify a new result. No worker file was changed by this coordinator review.
