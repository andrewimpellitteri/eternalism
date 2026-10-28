# Same-past data, actual outcomes, and representative choice

27 October 2026. Bounded algebraic result for the future-rival-selection task. This is a conditional mathematical distinction, not a claim about which solution is actual or a novelty claim.

## Contract

Let Ω be a nonempty family of admitted solutions, let R: Ω → P be the stipulated past-data map, and let q: Ω → Y be an outcome (for example, the field value at a fixed target event). A past-local enrichment has the form

    K(s) = k(R(s)).

Thus K(s)=K(t) whenever R(s)=R(t). Call K outcome-sufficient when there is a map h with q=h∘K. The exact criterion is

    K outcome-sufficient  iff  K(s)=K(t) implies q(s)=q(t).

In particular, no enrichment of the displayed past-local form can be outcome-sufficient if q varies on an R-fibre. Equivalently, a universal past-local outcome rule σ satisfying q(s)=σ(R(s)) for every admitted s exists exactly when q is constant on every R-fibre. This follows directly: necessity is substitution; for sufficiency define σ(r) to be the common q-value on R⁻¹(r), for r in im(R).

This is a no-go for universal outcome matching from the stipulated past data. It does not say that no actual outcome exists, that the past lacks every possible ground, or that one actual model cannot be selected by an extra fact. A selector that matches the actual model only after adding such a fact is no longer determined by R alone.

## Representative is not actuality

A representative section is a map ρ: im(R) → Ω satisfying R(ρ(r))=r. It selects one compatible model per past-data value. It need not satisfy ρ(R(s))=s for every s in a non-singleton fibre; that latter condition is impossible, since its left side is identical for any two models in the fibre. Where sections exist, they give conventions or model representatives, not a proof that the selected representative is the actual solution. Set-theoretic choice can supply a section for a family of nonempty fibres, but supplies no reason to identify its values with actuality.

For the homogeneous linear scalar equation in the task, Ω is a vector space of smooth solutions and R is restriction to the stipulated past. The zero-past fibre is W=ker(R), a vector subspace. If a target evaluation q(v)=v(x) is nonzero on W, choose w∈W with w(x)≠0. For every c∈ℝ, v_c=(c/w(x))w lies in W and q(v_c)=c. Hence the outcome ranges over all ℝ on that fibre. Every past-local K is constant there and cannot reproduce q. More generally, take any base solution v₀ in a nonempty fibre r. Its compatible family is v₀+w for w∈W; if evaluation is nonzero on W, the target values on that fibre again range over ℝ, since w(x) ranges over ℝ. The base solution may be zero (in particular, in the zero-past fibre); it need not be nonzero. This uses unrestricted smooth solutions and linearity; it need not survive a restricted admissible class or a common bound that makes the relevant outcome constant.

## What the symmetry argument does and does not prove

Use the minimal example Ω=W=ℝ, with past map R(v)=0 and outcome q(v)=v. Sign reversal S(v)=−v preserves the zero-past fibre and the equation class. The representative 0 is fixed by S. Therefore sign symmetry alone does not forbid a symmetry-compatible representative choice. It also does not make q past-determined: q(1)≠q(−1), while R(1)=R(−1).

Translations T_u(v)=v+u, u∈W, also preserve this zero-past fibre and act transitively and freely on it. If this entire translation group is stipulated as a symmetry, an equivariant point selector over the fixed past value would have to return a point v fixed by every T_u. For any nonzero u, v+u≠v, so no such fixed point exists. This is an exact no-equivariant-selector result for that group action. It is not a no-choice result: the non-equivariant convention ρ(0)=0 exists. Nor does the algebra show that translations are physical symmetries once extra structure, boundary conditions, a norm, or additional grounds are included.

The ambient linear solution space distinguishes its zero solution; that permits the zero-past convention and defeats the claim that residual symmetry by itself always blocks a canonical choice. On a nonzero affine fibre, an origin is not supplied by the affine structure alone. A chosen norm and closed-fibre conditions, for example, can sometimes select a unique least-norm representative by projection. Such added structure can make a representative canonical relative to that structure, while leaving open whether it is actual. Conversely, a free transitive translation action has no equivariant selected point. The correct conclusion depends on the declared group action and allowed structure, not on the word “symmetry” by itself.

## Scope and source access

No external source clause was needed for this elementary set-theoretic and linear-algebraic subtask; no external primary source was accessed. The exact solution-class premise and task-local target are taken from the assigned brief and the coordinator's `RESULT.md` §§1 and 3. Those project files are research inputs, not independent source verification. The conditional PDE application above does not re-prove the coordinator's past-fibre classification. In its stated all-smooth linear class, it only applies the affine-fibre argument to that premise.
