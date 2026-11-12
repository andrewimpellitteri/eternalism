# Independent bounded audit: finite prefix-mass control

31 October 2026. This is an independent reading of the coordinator's proposed
finite-dimensional construction, not an accepted project result, a source-paper
reproof, or independent external expertise. I read the assigned project inputs
and coordinator proof/audit documents. I did not consult external sources.

## Verdict

I found no invalid inference in the specified chain from the partial-pulse
chart through the simultaneous degree step and the conversion to actual global
boundary masses, provided the explicitly inherited finite-cone estimates,
compactness/uniqueness, proper-axis clock, and global mass-recovery inputs apply
uniformly to this compact smooth profile family as the cited project notes say.
The construction is algebraically consistent and the scaling of both errors is
sufficient for degree. This is a bounded conditional acceptance of that chain,
not an independent certification of its named PDE/source or regularity inputs.

## Audit of the construction

For disjoint supports, the prefix through `T_j` contains each earlier `F_i`
in full, the left portion of `F_j`, and `G_1,...,G_j`. Thus its quarter-norm
increment from prefix `j-1` to prefix `j` is

    (B_(j-1) x_(j-1)^2 + A_j x_j^2 + C_j beta_j^2)/4
    = p_j - p_(j-1).

Here `B_(j-1)` is the *right* portion of the preceding pulse and `A_j` is the
*left* portion of the current pulse. In particular, the formula neither omits
the partial current pulse nor counts its right portion too early. With
`x_0=0`, `B_0=0`, `A_(N+1)=0`, and `p_(N+1)=1`, the same calculation gives
all prefix identities and the total quarter-norm exactly one. The final
`G_(N+1)` is the remaining positive total-mass compensator; it is not an
additional unconstrained root variable.

The stated compact chart has positive radicands. On the radius-`rho` ball,
`p_j-p_(j-1) >= delta-2 rho >= delta/2`, so four times this increment is at
least `2 delta`. The subtracted pulse terms are at most
`rho^2 (B_(j-1)+A_j) <= delta`; hence each radicand is at least `delta`.
This also covers the first and final increments under the endpoint conventions.
The positive roots are smooth on a neighborhood of the closed ball and remain
bounded away from zero. The fixed finite schedule permits disjoint smooth
supports in the stated order, with every support after a common positive `A`.

At the actual finite-cone endpoint, the clock estimate gives
`|t_n(T_j)-T_j|=O(epsilon^2)` on the fixed readout window. Since
`Phi=epsilon f` and the family has a common sup norm, moving the upper endpoint
changes the quarter-integral by at most
`(epsilon^2/4) ||f||_infinity^2 |t_n(T_j)-T_j|=O(epsilon^4)`.
This estimate does not require the moving endpoint to stay within a support
interval. Combining it with the exact coordinate-cut identity gives
`Q_(n,j)=epsilon^2 p_j+O(epsilon^4)`. The cited cubic trace estimate, together
with the same clock shift and a uniform profile derivative bound, gives
`H_(n,j)=epsilon x_j+O(epsilon^3)`.

There are `2N` variables `(x,p-alpha)` and `2N` constraints: `N` readings and
`N` prefix masses. After scaling, the map is uniformly within `O(epsilon^2)`
of the identity on the compact ball. On its boundary, the homotopy to the
identity minus `(w,0)` avoids zero when `|w|<rho/2` and the uniform error is
less than `rho/2`. Its degree is therefore one. Continuity is required only
for each fixed finite-cone map; the cited compactness-plus-characteristic
uniqueness argument supplies that, while no differentiable or globally
selected scattering map is used. The degree roots can be chosen separately
for each cone, and compactness then selects a convergent subsequence.

The boundary-mass conversion uses the right order of operations as stated:
first select the global limit and pass its fixed-profile radiation and
finite-`V` mass-flux identities; then take `u` to minus infinity at each fixed
`V`. For that selected model, `V=t_*(T_j)` is a fixed number, even though it
varies between models. This yields the actual geometric cut value
`P_j=(1/4) integral_{-infinity}^{t_*(T_j)} Phi_*^2`. The total follows only
afterward by taking `V` to infinity. I see no exchange of a moving-cone limit
with the global boundary limit in this argument. The cut is geometric relative
to the specified spherical structure and marked central observer; the result
is not local detector energy or ADM mass.

## Exact scope and remaining gates

The conclusion is conditional on the imported source/PDE estimates and their
uniformity for this profile family, finite-cone continuity and compactness in
the cited solution class, the central proper-time reconstruction, and the
uniform finite-`V` global mass-recovery argument. I have not reread the primary
PDE source, independently reproduced those estimates, or audited the smooth
category/completeness/MGHD bridge. Those remain inherited gates, not established
by this sidecar. The geometric interpretation also uses the stipulated
spherical symmetry and marked observer to identify the radial null cut.

The chart requires strictly positive mass increments
`0<alpha_1<...<alpha_N<1`; zero or saturated increments are outside this
argument. Constants and the allowed target radius depend on the finite sample
schedule, fractions, and chosen basis. No dense-cut or whole-prefix-function
control, uniform-in-`N` bound, local energy or ADM equality, common full Cauchy
data, novelty/priority claim, or temporal-ontology conclusion follows.

This reading is independent of the coordinator's derivation in the limited
sense that I checked the displayed algebra, inequalities, quantifiers, and
limit order directly against the project inputs. It is not independent
external expertise: it is an internal model-based review, and the named
external mathematical inputs remain black boxes here.
