# Why the higher-order cone theorem does not automatically upgrade our limit

30 October 2026. Selected primary-source scope audit and coordinator
calculation; not a full proof audit or a smoothness impossibility theorem.

## Primary reading resolves the abstract-level tension

Kilgore, [arXiv:2108.13377v1](https://arxiv.org/html/2108.13377v1), 30 August
2021, introduction footnote 1, explicitly distinguishes cone-future models
from LOY's past-null-infinity scattering models and does not directly
control the latter. Definition 2.5 specifies weighted characteristic-data
regularity; Definition 2.6 supplies a local-scattering condition. Theorem
3.1 assumes this regularity and scattering class. These selected statements
were reread directly. The full induction and its constants were not audited.

Thus the earlier selected-full-text source-register warning is supported;
the later abstract-based suggestion of immediate applicability is not.
This does not say our compact profiles cannot ultimately yield smooth
solutions. It says that this particular global theorem cannot be applied
unchanged without checking its extra hypotheses and their uniformity.

## A concrete uniformity obstruction for the actual approximation sequence

Definition 2.5's outgoing-cone norm includes, already at derivative level
zero, a finite constant A bounding v^ω |∂_v(rφ)| on C₁, with ω≥2 in
Theorem 3.1. Translate our cone u=u_n to that normalization by

    ū=u−u_n+1,       v̄=v−u_n+1.

Then the initial cone is C₁ and ∂_(v̄)(rφ)=Φ_(ε,x)(v)/2. Fix a point v_*
inside the common compensating tail G where G(v_*)≠0. The finite-control
family has β(x)≥β_min>0 and all F_k vanish there. Consequently every
admissible outgoing data bound A_n must obey

    A_n ≥ (v_*−u_n+1)^ω εβ_min|G(v_*)|/2  → ∞.

This is an exact lower bound on a source hypothesis norm, valid for
arbitrary choices x_n in the compact parameter ball at any fixed ε>0.
It is not a numerical observation, nor an inference from lack of decay
of the original compact profile. Each individual translated data set has
a finite weighted norm; there is no common bound for the sequence.

The divergence is caused by moving the cone vertex while the physical
pulse stays at fixed advanced coordinate. It is not by itself divergence
of local geometric derivatives in the original physical chart. Decay
weights evaluated far from the translated origin could cancel some of
the growing constants if one proved the appropriate quantitative
dependence. We have not audited such a cancellation. In particular this
calculation does **not** prove that the C¹,¹ limit fails to be C² or smooth.

It does rule out treating "compact smooth profile" as a ready-made uniform
weighted-data hypothesis for this translated sequence. The null-infinity
claim must supply a localized or suitably weighted estimate, not simply
quote an all-order theorem for fixed cone data.

Shrinking the profile amplitude with n would change the target problem:
the displayed lower bound would require ε_n→0 to retain a common A, and
then E_n=ε_n²β₀²||G||²₂/4→0. That would not preserve the fixed positive
incoming mass or the nonzero reading ball of the finite-control theorem.

## Exact remaining lemma

For each compact physical quotient set K and each derivative order k,
prove a bound on the normalized finite-cone solutions of the form

    sup_n ||r_n, r_nφ_n, φ_n||_(required orders on K) ≤ C_(K,k),

uniform over the compact profile family, with the axis parity identities
and enough derivative reserve for the Cartesian division/lifting step.
Alternatively prove a regularity theorem directly for the selected
past-null-infinity solution. A fixed-data future stability theorem does
not supply either statement just by changing its name to "global".

Status: the direct-applicability question is answered negatively at the
stated source scope; the stronger smoothness bridge remains open. The
finite-order C¹,¹ argument and candidate scalar-readout theorem do not
require this upgrade. No novelty claim is made for the norm calculation.
