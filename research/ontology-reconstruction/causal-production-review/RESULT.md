# Bounded review: causal production, law variation and temporal actuality

Reviewed candidate: `research/ontology-reconstruction/coordinator/causal-production/RESULT.md`, SHA-256 `18d6c514f239f451417860fe6dd331cd6e5c161c0438b0a7e6547789e76b522c`.

## Strongest objection first

The finite model is a sound witness to a narrow probability claim, but it does not answer Tooley’s central explanatory challenge. Its equation, `Y = Z OR (K AND X)`, stipulates that `X` is an upstream input, that `Z` is an independent background route, and that changing `K` changes the downstream rule while leaving the exogenous distribution fixed. This gives the model directed causal autonomy by construction. A finite measure over `K` settings then shows that ordinary probability permits Tooley’s C1/C3/C4 pattern without the proposed reverse C4* pattern. It does not establish that this probability measure is Tooley’s logical probability, that the stipulated direction is independently grounded, or that a static non-Humean account can explain why the law counterfactual preserves `X` rather than revising it. The coordinator mostly acknowledges these limits; the model must not be cited as a counterexample to Tooley’s full account.

The strongest source-faithful Tooley reply is more than “both events exist, so causal roles must be symmetric.” Tooley makes the probability postulates part of his characterization of causal laws, rejects probability-raising as unable to ground causal direction, and argues that in a static world the attempted derivation of C4 has an unjustified stability assumption while a parallel argument yields C4*. He then says temporal actuality-as-of-time explains why a law plus the already actual cause adds an effect, rather than deleting an earlier cause to accommodate an absent later effect. This is a proposed explanation of the postulates, not just a prediction-equivalent restatement. Any rival that grants real, directed governing relations has to explain why its law variation preserves the root facts and recomputes descendants, and why that account is at least as good an explanation as Tooley’s temporal-actuality account.

That rescue is serious, but it is not a demonstrated uniqueness result. Tooley’s inference depends on the bridge that the relevant cause/effect asymmetry in logical probability can be explained only by an asymmetry in what is actual as of a time, together with his characterization of causal laws and the claim that no acceptable alternative account supplies the needed asymmetry. A non-Humean rival can reject that bridge without denying causal direction or laws, but merely naming “governing dependence” does not discharge its explanatory burden. The coordinator is right to leave that comparison live.

## Probability audit

For the stated finite model, with independent binary `X,Z,K`, probabilities `p,q,r`, and `Y = Z OR (K AND X)`, the calculations check out:

- `Pr(X=1 | K=1)=p=Pr(X=1)` by independence, so the model’s C1 instance holds.
- Conditional on `X=0`, `Y=Z`, and independence of `Z` and `K` gives `Pr(Y=1 | X=0,K=1)=q=Pr(Y=1 | X=0)`, the stated C3 instance.
- `Pr(Y=1 | K=1)=p+(1-p)q`, which is C4 after substituting those instances into the ordinary total-probability decomposition.
- At `p=q=r=1/2`, `Pr(Y)=q+r p(1-q)=5/8`; thus `Pr(¬Y)=3/8`.
- `Pr(¬X ∧ Y)=(1-p)q=1/4`, so `Pr(¬X | Y)=(1/4)/(5/8)=2/5`. The displayed C4* right side is therefore `3/8+(5/8)(2/5)=5/8`, while `Pr(¬X | K=1)=1/2`. The proposed reverse identity fails in this stipulated measure even though the displayed C1 and C4 instances hold.

The second setting also checks: with `Pr(K=1)=1/2`, `Pr(X=1|K=0)=1/4`, `Pr(X=1|K=1)=3/4`, and `Z` independent with probability `1/2`, the mixture gives `Pr(X=1)=1/2` but `Pr(X=1|K=1)=3/4`; hence C1 fails. Assigning each history an inventory in which the `X` slot occurs first and persists does not change those probabilities. This correctly illustrates that within-history persistence does not entail cross-law invariance.

The proposition scopes should stay explicit. In the first calculation, conditioning on `K=1` is the model’s representation of conditioning on the law proposition; it is not a claim about an observer learning the law. The unconditioned comparison averages over the stipulated family of law settings. Observing `Y` and inferring whether `X` occurred is a different conditional question, and `K` is not an in-world random law subjected to intervention. In the second calculation, the failure is a failure of the chosen cross-law measure to satisfy C1; since C1 is one of Tooley’s defining requirements for the causal laws under discussion, it is not an example of a Tooley-law satisfying his account and then violating C1.

Tooley’s `Prob` is explicitly logical probability given restricted evidence (`C`: tautologies and information about causal laws), not empirical frequency, physical chance, or an intervention distribution. The toy measure is a legitimate finite probability measure over a selected family of complete valuations, with law settings represented by `K`; it establishes consistency only for that chosen sample space and weighting. It neither derives a logical probability measure from `C` nor proves that Tooley’s measure must admit the same weighting. The result correctly says this, and should retain that limitation wherever it states that the toy model “shows” or “defeats” something.

## Exact repair to the comparison

Recommended wording for the central result:

> This finite-measure construction is a consistency witness: ordinary probability over a stipulated family of law settings permits C1, C3 and C4 while the displayed C4* identity fails. The equation assigns an upstream role to `X` and holds its exogenous distribution fixed across the tested law change, so the construction does not independently ground that direction or reproduce Tooley’s logical-probability framework. It rebuts only the claim that C1/C4 algebraically entails C4* under ordinary probability. It does not rebut Tooley’s explanatory argument that temporal actuality grounds the relevant law-counterfactual asymmetry.

Recommended wording for the rival’s obligation:

> The non-Humean rival must supply a principled cross-law comparison: which facts or distributions remain fixed when the law changes, which may change, and why the directed governing relation licenses that partition. Persistence of actual events within each history does not establish this cross-history rule. Conversely, Tooley must establish that temporal actuality is needed for that rule, rather than one possible ground among non-temporal accounts of directed governance.

The candidate already contains most of these qualifications. The main correction is to make explicit, at the point of the finite result, that direction and invariance are stipulated by the structural equation and common exogenous distribution. Avoid saying that a “complete-history interpretation” alone supplies the rival’s explanation: it supplies an interpretation of the valuations, while the model’s directed equation supplies the asymmetry.

## Bounded verdict

The arithmetic and conditional identities are correct. The finite model establishes that ordinary probability does not force C4* from C1/C3/C4 in this selected model family. It does not establish a result about Tooley’s logical probability, a general impossibility theorem, or the comparative explanatory superiority of a block/non-temporal account. The altered-root model correctly separates persistence within each growing history from invariance across law variations. Tooley’s strongest surviving argument is an abductive and conditional challenge: if his characterization of causal laws and logical-probability postulates is accepted, can a static account explain their directional asymmetry as well as the growing account? The first unresolved premise is that temporal actuality is necessary, or uniquely adequate, as the ground of the cross-law invariance that supports C1/C4. This review supplies no general ontology verdict and does not refute Tooley’s full philosophical account.

## Source read and scope

Directly read selected passages from the supplied local extraction `/private/tmp/eternalism-tooley-1997.txt`: the definition and explanation of C1–C4 in §3.2, printed pp. 59–60 (extraction markers PDF pages 76–77); §4.5.1–4.5.3, printed pp. 104–111 (PDF pages 121–128); and §4.6.1 only, printed pp. 112–116 (PDF pages 129–133); §4.6.2 was not audited. Read depth for this review: selected full-text passages from the supplied extraction, not the whole book and not a check against the printed/PDF original. The cited statements above are paraphrases. The broader source-provenance audit remains with the coordinator.


## Addendum: upstream compatibility control

I read `research/ontology-reconstruction/coordinator/causal-production/LAW_VARIATION_TEST.md` for this bounded follow-up. Its upstream control is correctly labeled a compatibility control and explicitly disclaimed as a counterexample to Tooley’s specific downstream `X`-to-`Y` case. If the added law makes later `X` depend on earlier `Z`, holding `Z` fixed while changing `X` is exactly the causal-role pattern Tooley’s actuality-as-of-time account can also endorse: retain the antecedent that is actual at the relevant earlier stage and allow its downstream consequence to differ. Thus the control usefully shows that cross-law invariance must respect compatibility and causal role; by itself it does not favor the rival or show that Tooley’s rule is incomplete. Treat it as a shared boundary condition for comparing accounts, not evidence that a static account has explained the boundary.
