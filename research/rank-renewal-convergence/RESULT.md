# Weighted convergence for rank-only post values: the obligation closes

Status: worker result, 2026-10-21, submitted for review. Task
`rank-renewal-convergence`. This document closes the **analytic** obligation
left open in `research/rank-renewal-followup/STATUS.md` and
`research/adversarial-review/coordinator/RENEWAL_OBSTRUCTION.md`, and thereby
confirms the *candidate* rank-only classification of
`research/adversarial-review/coordinator/RANK_FACTOR_NO_GO.md`.

It is a verification and write-up, not a new theorem, not a priority claim and
not a physical result. The measure-theoretic frame (the covariant posts algebra,
countable additivity, the laminar cover) is **imported** from
`research/creative/COVARIANT_RESULT.md`; I re-derive the rank-only part but do
not independently formalise countable additivity on that algebra.

Verdict: **(a)** — the needed weighted estimate is true and is proved below in
all three parameter regimes. Consequently the conditional obstruction is not
conditional on a missing estimate: in the stated measure-theoretic frame, for
`p∉[0,1]` and for `p=0` there is no normalized rank-only complex measure, and
`0<p≤1` is the exact existence range.

## 1. Setting and notation

Fix `p∈ℂ`, `q=1-p`, `a=|p|`, `b=|q|`, `t=a+b`. For a naturally labelled finite
order `C` of size `n`, let `L(C)` be the number of covers, `R(C)` the number of
strict comparable pairs, `h(C)=C(n,2)-R(C)`, and

```
A_p(C) = p^{L(C)} q^{h(C)} .
```

`N(H)` is the number of natural labellings of the unlabelled shape `H`
(labellings related by an automorphism identified once). `H` is *principal* if
it has a unique maximal element; *doubly principal* if it and its restriction to
the labels `<n-1` are principal. `D_H` is the covariant event of
`COVARIANT_RESULT.md`: infinitely many posts, and a post with exactly `n-1`
ancestors whose inclusive past is isomorphic to `H`. `ν` is a finite countably
additive complex measure on the posts algebra with `ν(P_∞)=1`.

**Rank-only rule.** There are finite complex numbers `κ_n` with

```
ν(D_H) = κ_n N(H) A_p(H)      for every principal H of size n.     (R)
```

Define the positive level sums, the next-post segment coefficients and the
bridge coefficients (all sums over *naturally labelled* orders, each labelling
once):

```
W_1 = 1,   W_n = Σ_{H principal, |H|=n} N(H)|A_p(H)|          (n≥2)
R_1 = p,   R_k = Σ_{T post-free, |T|=k-1} A_p(T) p^{M(T)+min(T)}   (k≥2)
K_k = the same sum with |A_p(T)| and |p| replaced by moduli
B_0 = 1,   B_1 = p,   B_m = Σ_{T any, |T|=m-1} A_p(T) p^{M(T)+min(T)}
```

with `M(T)`, `min(T)` the numbers of maximal and minimal elements. The
`k=1`/`m=1` terms are special: the empty-order expression would give `1`, but
the singleton segment has `min=1`, giving `p`. This is the convention already
recorded in `RENEWAL_OBSTRUCTION.md` and used by `check_weighted.py`.

**Renewal identity** (Lemma 0). `B_m = Σ_{k=1}^m R_k B_{m-k}` for `m≥1`;
equivalently `U(z)(1-R(z))=1` as formal power series. Proof: decompose a
principal segment at its first post after the specified old maximum. The
decomposition is an ordinal sum, cross covers are exactly the seam already in
`p^{min}`, and natural labels concatenate, so no interleaving multiplicity
appears. Finite exact corroboration: all `B_m` identities for `m=1..8` at
`p=0, 1/2, 3/2, 2, -1, (1+i)/2` (Section B of `check_weighted.py`); the earlier
`check_renewal_series.py` verifies degree five at five parameters.

## 2. The weighted obligation

`RENEWAL_OBSTRUCTION.md` states the obstruction under

```
|κ_n| ≤ C ρ^n   and   U, R absolutely convergent at ρ.             (old)
```

That formulation is the wrong coordinate, as Section 4 explains; the sharp form
is the weighted estimate

```
Σ_{j≥0} |B_j| / W_{n+j} < ∞ .                                      (6)
```

This is exactly condition (6) of `RANK_FACTOR_NO_GO.md`. It is a property of the
parameter `p` alone, not of `κ`.

### Lemma 1 (bridge bound)

For `j≥0`, with `B_j` as above:

```
|B_j| ≤ [ Π_{d=1}^{j} (1 + b^{d/2}) ]^2          (0 < b ≤ 1)       (1a)
|B_j| ≤ 4^j b^{j(j+1)/2}                          (b ≥ 1)          (1b)
```

In particular, if `b<1` then `|B_j| ≤ C_b := [Π_{d=1}^{∞}(1+b^{d/2})]^2 < ∞`.

**Proof.** `B_j` is the percolation weight of the event `E_j` on vertices
`0,…,j` that *every non-initial column has an incoming edge and every
non-final row has an outgoing edge*. Indeed, given the order on `{1,…,j}` with
unique maximum, the edges from `0` to its minimal elements make `0` below
everything, the maximum is above everything, and all other edges from `0` are
redundant and sum to `p+q=1`; conversely reachability from `0` forces an
incoming edge at every `v≥1`, and dually for `j`. Inclusion–exclusion over bad
columns `I⊆{1,…,j}` and bad rows `J⊆{0,…,j-1}` gives

```
B_j = Σ_{I,J} (-1)^{|I|+|J|} q^{e(I,J)} ,
```

`e(I,J)` the number of edges into `I` or out of `J`; free edges sum to
`p+q=1`, so this is a polynomial identity valid for every complex `p`. Each edge
is counted at most twice, so

```
(Σ_{i∈I} deg(i) + Σ_{j∈J} deg(j))/2 ≤ e(I,J) ≤ Σ_{i∈I} deg(i) + Σ_{j∈J} deg(j).
```

Row degrees are `j,j-1,…,1` and column degrees are `1,…,j`. For `b≤1`,
`b^{e} ≤ b^{(Σdeg)/2}` and summing factorises into `Π_d(1+b^{d/2})` twice,
giving (1a); for `b≥1`, `b^e ≤ b^{Σdeg} ≤ b^{j(j+1)/2}` and there are `2^j`
row and `2^j` column choices, giving (1b). ∎

(1a) converges because `Σ_d b^{d/2}<∞` and `log(1+x) ≤ x`.

### Lemma 2 (level lower bounds)

For `n≥2`, with `a,b>0`:

```
(i)   W_n ≥ a t^{n-2} F_{n-2},   F_m = Π_{j=1}^{m}(1-s^j),  s=b/t   [two-cap]
(ii)  W_n ≥ a^{n-1} b^{C(n-1,2)}                                    [star]
(iii) when b=1 and m≥1:
      W_{2m+1} ≥ a^m (1+a)^{m^2},   W_{2m+2} ≥ a^{m+1}(1+a)^{m^2}   [bipartite]
```

`F_m ≥ c_s := Π_{j≥1}(1-s^j) > 0` for `0<s<1`.

**Proof.** (i) is the two-cap bijection of `research/creative/RESULT.md`
(full-text read): every doubly-principal order is `G⊕{u}⊕{v}` with `G`
arbitrary; the two caps contribute `a·a^{L(G)+M(G)}`, and the normalized
endpoint-connectivity sum equals `F_{n-2}`. Doubly-principal orders are
principal, hence `W_n ≥ V_n ≥ a t^{n-2}F_{n-2}`. I reproduce the *bookkeeping*
by exact finite evaluation, not the probability lemma.

(ii) The `(n-1)`-antichain capped once (a single maximum above it) is principal,
has `a^{n-1}` for its `n-1` covers and `b^{C(n-1,2)}` for its incomparable pairs,
and contributes at least once (in fact `n` times, once per choice of cap label).

(iii) At `b=1`, take a lower antichain `A_m`, an upper antichain `B_m`, arbitrary
edges `E⊆A_m×B_m`, and a universal maximum `z`. The order is principal. Its
covers number `|E|+m`, its incomparable pairs number `m²-|E|+2C(m,2)`, and
`b=1`, so `|A_p| = a^{|E|+m}`. Summing the `2^{m²}` edge choices gives
`a^m(1+a)^{m^2}`. Appending one further universal maximum to each such order
keeps it principal and multiplies `|A_p|` by `a`, giving the even case
`a^{m+1}(1+a)^{m^2}`. Hence, with `m=⌊(N-1)/2⌋`,

```
W_N ≥ min(1,a)^{m+1} (1+a)^{m^2} ≥ exp( ((N-2)/2)^2 log(1+a) - C N )
```

for a constant `C` depending on `a` only. ∎

### Theorem 1 (weighted estimate)

Let `p∉[0,1]`. If `b<1` or `b=1`, (6) holds for every `n≥1`. If `b>1`, (6)
holds for every `n` with `a b^{n-2} > 4` (a nonempty tail, since `b>1`).

**Proof.** Since `p∉[0,1]` we have `t>1` (equality in the triangle inequality
`|p|+|1-p| ≥ 1` forces `p∈[0,1]` real), and `a>0` (as `p≠0`).

*Case `b<1`.* Lemma 1a: `|B_j| ≤ C_b`. Lemma 2(i): `W_{n+j} ≥ a t^{n+j-2}c_s`.
Hence the term is at most `(C_b t^{2-n}/(a c_s)) t^{-j}`, a geometric sequence.

*Case `b=1`.* Lemma 1b: `|B_j| ≤ 4^j`. Lemma 2(iii): with `N=n+j`,
`log W_N ≥ ((N-2)/2)² log(1+a) - C N`. The term is at most
`exp(N log 4 - ((N-2)/2)² log(1+a) + C N)` for `N=n+j`, which is summable in
`j` because `log(1+a)>0`.

*Case `b>1`.* Lemma 1b and Lemma 2(ii) with `N=n+j`:

```
|B_j| / W_{n+j}
 ≤ 4^j b^{j(j+1)/2} / ( a^{n+j-1} b^{(n+j-1)(n+j-2)/2} )
 = a^{-(n-1)} b^{-(n-1)(n-2)/2} · ( 4 / (a b^{n-2}) )^j .
```

The exponent identity is exact: the `b`-exponents are
`j(j+1)/2 - (n+j-1)(n+j-2)/2 = -(n-1)(n-2)/2 - j(n-2)`, and the `a`-exponents
are `-(n+j-1) = -(n-1)-j`. Choosing `n` with `a b^{n-2}>4` makes the ratio
`<1`. ∎

The estimates are far from sharp; only summability is used. `check_weighted.py`
verifies (exactly) the star and bipartite bounds for `n=2..7`, the two-cap bound
for `n=2..7` at seven parameters, the bridge bounds for `j=1..7`, and the
exponent identity for `j=0..40`.

## 3. From the estimate to vanishing values

### Proposition (vanishing, `p≠0`)

Assume (R), let `p≠0`, and suppose (6) holds for some `n≥1`. Then `κ_n=0`.

**Proof.** *Structural input 1 (attenuation).* Summing `|ν(D_H)|` over the
finitely many principal shapes of rank `m`,

```
W_m |κ_m| ≤ ‖ν‖_TV =: T .                                          (2)
```

*Structural input 2 (child partition).* For a principal `H` of size `n`, the
children `D_J` over next-post pasts `J` are disjoint, partition `D_H` (because
`D_H⊆P_∞`), and satisfy `N(J)=N(H)N(S)`, `A_p(J)=A_p(H)w(S)` for the ordinal
sum `J=H⊕S`. Across the finitely many `H` of rank `n` the families are disjoint.
Hence

```
W_n Σ_{k≥1} K_k |κ_{n+k}| ≤ T .                                    (3)
```

*Structural input 3 (recurrence).* Dividing `ν(D_H)=Σ_J ν(D_J)` by
`N(H)A_p(H)`, available at every rank via the chain `A_p=p^{n-1}`,

```
κ_n = Σ_{k≥1} R_k κ_{n+k} ,   absolutely convergent by (3).        (4)
```

Now multiply (4) at `n+j` by `B_j` and sum over `j≥0`. Absolute convergence
holds:

```
Σ_j |B_j| |κ_{n+j}| ≤ T Σ_j |B_j|/W_{n+j} < ∞                      (5)
Σ_{j,k} |B_j R_k κ_{n+j+k}| ≤ T Σ_j |B_j|/W_{n+j} < ∞ ,
```

the second by (3) at rank `n+j` and `|R_k|≤K_k`. Fubini and Lemma 0 give

```
Σ_j B_j κ_{n+j}
 = Σ_{m≥1} κ_{n+m} Σ_{j=0}^{m-1} B_j R_{m-j}
 = Σ_{m≥1} B_m κ_{n+m}
 = Σ_j B_j κ_{n+j} - κ_n ,
```

so `κ_n=0`. ∎

Note that this step never mentions `R(1)`, the radius of `R`, or divergence of
any complex series. Only (6) and the *positive* level sums `W` enter.

### Corollary 1 (no-go away from the classical interval)

If `p∉[0,1]` and `p≠0`, no finite countably additive complex `ν` on the posts
algebra satisfies `ν(P_∞)=1` and (R) for all principal `H`.

**Proof.** Theorem 1 gives (6) on a tail (all `n` when `b≤1`, `n≥n0` when
`b>1`). The Proposition gives `κ_n=0` there. Then (4) propagates zero downward:
for `m=n0-1,…,1` the right side vanishes identically because all its indices
exceed `n0-1` and (3) makes it absolutely convergent. So every `κ_n=0`, every
`ν(D_H)=0`. The `D_H` are a countable laminar family covering `P_∞` (every
infinite-post history has a post of rank `≥2`, hence lies in some `D_H`); finite
unions are finite disjoint unions of zero-valued sets, and continuity from below
gives `ν(P_∞)=0`, contradicting `ν(P_∞)=1`. ∎

### Corollary 2 (`p=0`)

At `p=0`, every principal `H` of size `≥2` has `L≥1` (its maximum covers
something), so `A_0(H)=0` and (R) forces `ν(D_H)=0` for all such `H` without
using any `κ_n`. Those `D_H` alone cover `P_∞` (take the *second* post, whose
inclusive past has size `≥2`), so the same laminar/continuity argument gives
`ν(P_∞)=0`. Hence no normalized rank-only measure at `p=0`.

This is the exact place where the `p=0` division failure is bypassed: the
recurrence (4) is *not* derivable at `p=0`, but the no-go does not need it. The
singleton `κ_1` is irrelevant, because the rank-`≥2` cover already exhausts
`P_∞`.

### Corollary 3 (existence range)

Under the measure-theoretic setup of `COVARIANT_RESULT.md` (finite countably
additive complex measure on the posts algebra, `ν(P_∞)=1`) with the rank-only
all-principal rule (R), a normalized rank-only measure exists **iff** `0<p≤1`.
Sufficiency is the classical construction (`κ_n=c(1-p)`, `κ=1` at `p=1`);
necessity is Corollaries 1 and 2.

This is precisely the candidate statement of `RANK_FACTOR_NO_GO.md`. What this
task adds is that the disputed step — the weighted convergence (6) — is proved,
not assumed.

## 4. Why "the decay radius of κ" was the wrong coordinate

`RENEWAL_OBSTRUCTION.md` asks for `|κ_n|≤Cρ^n` together with absolute
convergence of `U` and `R` at `ρ`. Three separate remarks:

1. `|κ_n|≤Cρ^n` holds automatically for `ρ=ρ_κ:=limsup|κ_n|^{1/n}`, and (2)
   plus Lemma 2 gives `ρ_κ ≤ 1/t` when `b<1`.
2. But absolute convergence of `R` at `1/t` is not available in general. At
   `p=3/2` the positive segment sums `K_k` are
   `1.5, 0, 2.53, 7.12, 37.1, 208, 1346` for `k=1..7` (exact), i.e. growing much
   faster than `t^k=2^k`. So `Σ K_k ρ^k` may diverge below `1/t`.
3. For `b≥1` the situation is worse: for `k≥3`, `K_k ≥ b^{C(k-1,2)} a^{2k-2}`
   (take the post-free antichain `T` of size `k-1`), so `Σ K_k ρ^k = ∞` for **every**
   `ρ>0` when `b>1`. The "common absolute-convergence domain" of `U` and `R` is
   then `{0}`, and the geometric-`λ` obstruction is vacuous there. Whether the
   *complex* series `R(z)` cancels enough to have positive radius is open and is
   not needed.

So the obligation is not "does `R` converge at `ρ_κ`" but "does the bridge
weighted by the level sums converge", (6). The bridge `B_j` and the next-post
sums `K_k` behave completely differently: at `p=3/2`, `|B_j| ≤ 2.25` for
`j≤7` while `K_7=1346`. That is why (6) closes where the radius formulation does
not.

## 5. Exact finite checks

`python3 research/rank-renewal-convergence/check_weighted.py` (standard library
only, about 50 s, no installs). All assertions have zero tolerance.

| Check | Result |
|---|---|
| A1 labelled sums = shape sums with `N(shape)` | exact, `n=1..5`, `p=1/2` |
| A2 `N(H⊕S)=N(H)N(S)` | exact, 71 shape pairs, `|H|+|S|≤5` |
| B renewal `B_m=Σ R_kB_{m-k}` | exact, `m=1..8`, six parameters |
| C `W_n ≥` star; `V_n ≥` two-cap | exact, `n=2..7`, seven parameters |
| C bipartite `b=1` bound | exact, `n=3..7`, `p=2` |
| D `B_j` = inclusion–exclusion | exact, `j≤7` (five real `p`), `j≤6` at `(1+i)/2` |
| D `B_j` = brute-force reachability percolation | exact, `j≤4`, five real `p`; `j=5` at `p=1/2` |
| D bridge bounds (1a)/(1b) | exact, `j=1..7` |
| E exponent identity | exact, `j=0..40` |
| H child sum `Σ_J A_p(J)=A_p(H)R_{m-n}` | exact, 426 identities per parameter, `n<m≤7`, four parameters |
| F endpoints | `A_0(H)=0` for principal `|H|≥2`; `A_1=δ_chain` |
| G `K_k` vs `R_k` | diagnostic only |

Exact values worth recording (all from the script):

```
p=(1+i)/2:  W_2..W_7 = √2/2, 1/2+√2/4, 3/8+3√2/4, 55/32+31√2/32,
                       29/8+809√2/256, 12711/1024+18249√2/2048
            V_2..V_7 = √2/2, 1/2, 1/4+√2/4, 3/4+3√2/16, 31/32+55√2/64,
                       809/256+29√2/16
p=2:        W_2..W_7 = 2, 8, 64, 960, 25856, 1209856
p=-1:       W_2..W_7 = 1, 3, 25, 555, 31937, 4671747
p=5/2:      W_2..W_7 = 2.5, 15.625, 255.86, 10580.44, 1073094.27,
                       260705496.71
```

Concrete instances of (6) obtained from the proven majorants:

```
p=-1:   n0=5,  Σ_{j≥0}|B_j|/W_{5+j} ≤ (1/64)·2        = 1/32
p=5/2:  n0=4,  Σ ≤ 2.5^{-3}1.5^{-3}/(1-4/(2.5·1.5²)) ≈ 0.0657
p=-1/2: n0=8,  Σ ≤ 0.5^{-7}1.5^{-21}/(1-4/(0.5·1.5⁶)) ≈ 0.0862
```

At `p=-1` the *actual* first three ratios are `1/555`, `1/31937`, `1/4671747`
against the majorant `1/64`, `1/128`, `1/256`; the bound is loose but valid.

The finite checks corroborate the bookkeeping. They are not the proof; the proof
is Section 2–3. In particular no root of a truncated polynomial is used
anywhere. `research/extensions/rank-factor/AGENT_REPORT.md` correctly warns that
such roots are meaningless, and Section 4 gives a structural reason: for `b≥1`
the absolute series diverges everywhere, so truncations are being evaluated
outside any reliable radius.

## 6. Audits requested by the brief

**Natural-label multiplicities.** The sums defining `R_k`, `K_k`, `B_j`, `W_n`
run over naturally labelled orders, each labelling once; equivalently over
shapes with multiplicity `N(shape)`. Both forms are checked exactly (A1), as is
the ordinal-sum multiplicity `N(H⊕S)=N(H)N(S)` (A2) on which the child partition
and `R_k` depend. `D_H` is indexed by the *unlabelled* shape, and a post's
inclusive past determines its shape, so distinct shapes at one rank are
disjoint: two posts with the same number of ancestors coincide because
`x<y ⇒ incpast(x) ⊊ incpast(y)`. This is what makes (2) a sum of disjoint
events and not an overcount.

**`p=0` division failure.** `N(H)A_0(H)=0` for every principal `H` of size
`≥2`, so the recurrence (4) cannot be obtained there. The no-go does not use
(4) at `p=0`; it uses `A_0(H)=0` and the laminar cover. Verified exactly.

**Endpoints.** `p=0`: excluded (Corollary 2). `p=1`: allowed; the Dirac measure
on the chain gives `κ_n=1` and `A_1=δ_{chain}` exactly. `p∈(0,1)`: allowed,
classical; here `t=1` and `F_m` does not decay, which is exactly why the
argument of Theorem 1 fails — the no-go must not, and does not, apply there.
`κ_1` is fixed by `ν(D_singleton)` and then by (4) at `n=1`; it is killed last
in the nonclassical case.

**Total variation versus the complex series.** The positive sums `K_k` grow
(6.9·10⁶ at `k=7`, `p=2`) while `|R_7|=256`, so cancellation between complex
terms is real and large. The withdrawn inference in
`research/extensions/rank-factor/AGENT_REPORT.md` — that total-variation
divergence implies divergence of the complex scalar series — remains
unjustified, and nothing here restores it. The no-go is proved through (6) and
the *positive* level sums, so it is independent of that question. Likewise the
result neither asserts nor needs convergence or divergence of `R(1)`.

## 7. Scope, what is not claimed, and falsifiers

Not claimed:

- No physical, ontological or interpretive consequence. `κ_n` and `ν` are
  measure-theoretic compatibility data inside a model.
- No priority or novelty claim. The ingredients are renewal inversion,
  inclusion–exclusion and variation; the candidate statement and the three-case
  strategy are the coordinator's, and this note is the review of that strategy.
- No classification of shape-dependent values, DP-only rules, non-normalized
  measures, or Banach/Hilbert norm-prescription problems. In particular the
  `L²` indicator construction in `coordinator/VECTOR_COUNTERMODEL.md` prescribes
  `|A_p(C)|`, not `A_p(C)`, and is untouched. Finite-dimensional vector
  measures remain excluded there by finite total variation.
- No general theorem about arbitrary causal-set measures: the value rule (R) is
  a strong dynamical axiom, and dropping it (e.g. to doubly-principal-only)
  restores countermodels.

What would defeat the result:

1. A normalized rank-only complex measure at some `p∉[0,1]`. By Theorem 1 and
   the Proposition it would have to violate (2), (3) or (4); each is a direct
   consequence of countable additivity and the ordinal-sum factorization.
2. An error in Lemma 1's identification of `B_j` with the endpoint-percolation
   event. The identification is checked exactly against the independent
   bridge sum for `j≤7`, against inclusion–exclusion for `j≤7`, and against
   brute-force reachability percolation for `j≤4` (five real parameters) and
   `j=5` at `p=1/2`.
3. An error in Lemma 2(i)'s two-cap bound, which is imported from
   `creative/RESULT.md` and only corroborated here. This is the one imported
   inequality that carries real weight in the `b<1` case; it was separately
   audited in `creative/proof-audit/`, which I did not re-read.
4. A failure of laminarity or of the cover `∪_H D_H = P_∞`. Both are argued in
   `COVARIANT_RESULT.md` (full-text read) and are not independently formalised
   here.

Changes that would *evade* the no-go: allow shape-dependent `κ_H` (for
`p∉{0,1}` every finite `ν` can then be written in that form by division, so the
restriction disappears), drop normalization, or restrict the value rule to
doubly-principal pasts (the Dirac countermodel of `COVARIANT_RESULT.md`). Within
the stated rule no extra hypothesis is needed: (6) is proved unconditionally for
`p∉[0,1]`.

## 8. Read depth of sources

| Source | Depth |
|---|---|
| `AGENTS.md`, `README.md`, `knowledge/NOVELTY.md`, task brief | full text |
| `research/rank-renewal-followup/STATUS.md`, `AGENT_REPORT.md` | full text |
| `research/adversarial-review/coordinator/RENEWAL_OBSTRUCTION.md` | full text |
| `research/adversarial-review/coordinator/RANK_FACTOR_NO_GO.md` | full text |
| `research/adversarial-review/coordinator/BOUNDARIES.md` | full text |
| `research/adversarial-review/coordinator/REVIEW_HISTORY.md` | full text |
| `research/adversarial-review/coordinator/VECTOR_COUNTERMODEL.md` | full text |
| `research/adversarial-review/coordinator/check_renewal_series.py` and `check_boundaries.py` | code-audited |
| `research/creative/COVARIANT_RESULT.md`, `creative/RESULT.md` | full text |
| `research/extensions/rank-factor/AGENT_REPORT.md` | full text |
| `research/extensions/rank-factor/check_stationarity.py`, `kernel_sequence7.py`, `probe.py` | code-audited |
| `research/extensions/covariant-values/AGENT_REPORT.md` | full text |
| `experiments/baseline/poscau.py` | code-audited (not imported by my script) |

No external papers were consulted for this task; the analytic content is
elementary and self-contained apart from the imported two-cap bound.
`research/creative/proof-audit/` was **not** read (listed as a residual risk
above). `coordinator/BANACH_NORM_BOUNDARY.md` and
`coordinator/HILBERT_NORM_BOUNDARY.md` were not read; the scope statement above
only says norm-prescription problems are outside this result.

## 9. Reproduce

```
python3 research/rank-renewal-convergence/check_weighted.py
```

Standard library only; about 50 s; exact arithmetic (`Fraction`, Gaussian
rationals, `Q(√2)`); no network, no installs, no board edits.
