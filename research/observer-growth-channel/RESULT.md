# A growth-derived observer channel, and what survives of the phase-aligned event

Sole-worker result, 21 October 2026. Finite-stage algebra and exact enumeration.
No novelty, priority, universal-observer or ontological claim is made.

## 0. Verdict in one paragraph

The arbitrary history-register observer of
`research/covariant-observer-witness/` is replaced by three algebras/channels
derived from an explicit causal-set growth model: a clock (chain) observer, a
bounded-region stem observer, and a complete covariant (isomorphism-class)
observer, plus the gauge-fixed growth-record algebra that the earlier note
implicitly used. Four separable findings follow. (i) The phase-aligned event
`E` is a function of the unlabelled causet: the amplitude and the phase are
constant on isomorphism classes. (ii) `E` is *recognised* only by observers with
access to all proper subcausets (`k*(n) = n-1` at every tested stage) and above
all by one that collects principal stems, for which there is a two-line proof;
cardinality-only and bounded-region observers cannot name it. (iii) The
*coherent* effect `T_E = |u_E><u_E|` is outside the adjoint image of every
record channel, at every stage, and is outside the image of the visibility-`γ`
class channel for every `γ < 1`; this is exact and does not depend on
enumeration. So no record-based covariant observer can measure the quantum
measure of `E`. (iv) The divergence itself *does* survive the label quotient, but
the quotient changes the number: the register sum is not a function of the class
amplitudes alone, and after the correct `√m_κ` reweighting the growth rate drops
(≈15× to ≈5.4× per stage in the tested range). No detector probability
diverges: the class-resolved probability is bounded near 0.24 and the
efficiency-limited filter probability decays to 0.09 by `n = 7`. The event
therefore survives quotienting, does not survive dephasing or record access,
and never yields a divergent probability.

## 1. What is being replaced, and the replacement contract

`research/covariant-observer-witness/RESULT.md` used two algebras on the level-`n`
history register: cardinality-only (trivial at fixed `n`) and
isomorphism-class. It conceded that `A_iso` "is not derived from a causal-set
observer, a local region, or a physical instrument". The brief asks for a
replacement with an explicit access model, an explicit relabelling-covariance
statement, and an exact verdict on the effect.

The replacement is a family indexed by *what a growth-internal observer can
read*. Every member is a channel `C_r(ρ) = Σ_a Tr(P_a ρ)|a><a|` induced by a
record map `r` on the labelled level, i.e. the standard "the observer learns the
value of `r` and nothing else" instrument. This is a model of **access**, stated
as mathematics; it is not derived from causal-set dynamics. Section 8 lists
exactly which premises are mathematical assumptions.

## 2. The growth model (all facts machine-checked)

A **labelled birth history** at stage `n` is a tuple
`C = (C[0],…,C[n-1])`, where `C[i] ⊆ {0,…,i-1}` is the causal past of the
element born at step `i` and must be a down-set of the prefix. These are
exactly the labelled causets whose labelling is a linear extension: the
reachable labelled states of a sequential-growth process. Call the set
`level_n`.

| `n` | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| `\|level_n\|` | 1 | 2 | 7 | 40 | 357 | 4824 | 96428 |
| isomorphism classes | 1 | 2 | 5 | 16 | 63 | 318 | 2045 |

The class counts equal the number of unlabelled posets (A000112) at every
stage; that is an independent check on both the enumeration and the
canonicalisation.

Complex percolation amplitude, the object used by the earlier finite
comparison:

```
A(C) = p^L q^h,      p = (1+i)/2,  q = (1-i)/2,
L = #covering pairs, h = #incomparable pairs.
```

**F1 (factorisation).** `A(C) = ∏_i p^{m(D_i)} q^{i-|D_i|}` where `D_i = C[i]`
and `m(D)` is the number of maximal elements of `D`. Those factors are the
transition amplitudes of the growth process itself, so `A` is a product of
growth-step amplitudes and is not merely a poset-level weight. Verified for
every history, `n ≤ 7`.

**F2 (normalisation).** `Σ_C A(C) = 1` and `Σ_C |A(C)|² = 1` exactly at every
stage `n ≤ 7`, in exact rational complex arithmetic. `|A(C)|²` is the
real-percolation probability of the labelled history, so the level is a
normalised family of labelled states.

**F3 (phase is a birth-order phase).** `arg A(C) = (L-h)π/4 (mod 2π)`, checked
via `2^{L+h}A(C)² = i^{L-h}` for every history. Hence the phase is a genuine
accumulated growth phase, not a relabelling artefact.

**F4 (total variation).** `V_n = Σ_C |A(C)| = 1.000, 1.414, 2.621, 6.048,
16.751, 54.227, 201.071` for `n = 1…7` (exact integer counts by `L+h`). This
diverges, consistent with the known non-extension of complex percolation
(Section 7, S3).

The event of interest, unchanged from the earlier note:

```
E = { C : (L(C) - h(C)) mod 8 ∈ {0,1} },
```

i.e. histories whose amplitude lies on the positive-real or positive-imaginary
ray. `E` is a proper, non-empty subset at every stage: sizes
1, 2, 13, 78, 1099, 24624 for `n = 2…7`.

## 3. Two structural identities that decide recognition

**Identity I1.** For every history and every stage,

```
L = Σ_x m(J^-(x)),        h = C(n,2) - Σ_x |J^-(x)|,
```

where `J^-(x)` is the principal past of `x` and `m(·)` counts maximal elements.
`Σ_x |J^-(x)|` counts comparable pairs; `Σ_x m(J^-(x))` counts covering pairs,
since `y` is maximal in `J^-(x)` exactly when `(y,x)` is a cover. Verified for
all histories, `n ≤ 7`.

Consequence: **`L-h`, hence `E`, is a function of the multiset of isomorphism
classes of the principal pasts `{[J^-(x)] : x ∈ C}`.** A partial stem is a
finite down-set that contains its own past (Brightwell–Dowker–Garcia–Henson–
Sorkin 2003, Sec. 3); the principal pasts `J^-(x)` are exactly the down-sets of
the form "past of one element", and every down-set is contained in at least one
of them. So
the phase-aligned event is measurable by a **covariant local-record
collection**: each element carries a label-free record of its own past, the
observer collects all records, and no global relation is read directly. This is
a genuine answer to "give a causal-set observable that resolves the phase" and
it is stronger than the earlier note, which only had the full class.

**Identity I2 (multiplicities).** Growth normalisation forces the covariance
question to be about multiplicities. With `m_κ = |level_n ∩ κ|` the class
multiplicity, `Σ_κ m_κ |A_κ|² = 1`. Three different amplitude sums over `E` are
therefore available and they are *not* equal:

| sum | definition | meaning |
|---|---|---|
| `S_reg` | `Σ_{C∈E} A(C) = Σ_κ m_κ A_κ` | labelled-register sum (the earlier note's `S_n`) |
| `S_unl` | `Σ_{κ∈E} A_κ` | naive push-forward of the amplitude to unlabelled causets |
| `S_orb` | `Σ_{κ∈E} √m_κ A_κ` | amplitude on the quotient with `P(κ)=|·|²` |

`S_reg ≠ S_unl` for every `n ≥ 4`, which is the precise sense in which **the
amplitude sum is not a function of the covariant data alone**: it depends on
`m_κ`, a count of labellings. `S_orb` is the only one of the three whose squared
modulus is a normalised probability assignment on classes, so it is the
correctly normalised covariant amplitude.

## 4. The observer algebras and their channels

Let `H_n = C^{level_n}` with basis `|C>`, and `ψ = Σ_C A(C)|C>` (unit norm by
F2). Write `u_E = Σ_{C∈E}|C>`, `T_E = |u_E><u_E|`, and
`Q_E = T_E/|E|`.

### (a) `A_card`: clock / worldline observer

*Derivation.* A chain is the causal-set analogue of a timelike worldline, and a
chain carries no order information beyond its own cardinality. An observer whose
only structure is its worldline therefore records `|W|` and nothing else; at
fixed stage `n` this is constant. (The "observer = chain of events" picture is
used in the causal-set literature; see Section 7, S6, discovery depth only.)
*Channel.* `r(C) = n`, one atom, `im(C_r*) = span{I}`. `T_E` is neither a
scalar nor diagonal, so `T_E ∉ im(C_r*)` and `E` is not measurable. Exact for
`n ≥ 2`.

### (b) `A_k`: bounded-region (stem) observer

*Derivation.* The observer inspects bounded patches of the causet — all partial
stems of at most `k` elements — and reports their isomorphism classes. The
covariant summary is the multiset of classes, no labels.
*Channel.* `r_k(C) = { [J] : J a down-set of C, 1 ≤ |J| ≤ k }`. The adjoint
image is `span{P_a}`, the commutative algebra of atom projectors.

### (c) `A_iso`: complete covariant observer

*Derivation.* A record is *covariant* iff it is independent of labelling. Any
label-independent record map on `level_n` is constant on isomorphism classes, so
`A_iso` — the algebra of functions of `[C]` — is the **maximal** covariant record
algebra at stage `n`. This is the finite-stage truncation of the standard
statement that covariant observables are label-invariant measurable sets
(Brightwell et al. 2003; Dowker–Surya 2006; Zalel 2023). Its instrument is the
class-pinching channel `Π(ρ) = Σ_κ Π_κ ρ Π_κ`.

### (d) `A_growth`: the gauge-fixed growth-record algebra

The diagonal algebra on `level_n`: the observer sees the full birth history,
including the birth order. This is what the earlier register comparison actually
used. It is **not** covariant: `S_n` does not act on `level_n` (only labelled
posets whose labelling is a linear extension are reachable), so no nontrivial
finite-stage cylinder is relabelling-invariant — the finite-stage counterpart of
Surya–Zalel 2020 Sec. 2. `A_iso` is the covariant shadow of `A_growth`.

### Covariance statement, stated exactly

1. `A(C)` depends only on the isomorphism class of `C` (`L`, `h` are order
   invariants). Verified on every class, `n ≤ 7`. This is condition (a) of
   Surya–Zalel 2020 Sec. 2.2 in the finite stage.
2. `E` is therefore a union of classes, and `ψ` has equal amplitude on
   relabelled copies of the same causet.
3. `S_n` does **not** act on `level_n`; "quotienting birth labels" is the map
   `level_n → Classes_n`, not a unitary group action. Any claim that a finite
   object "commutes with relabelling" must be read as "factors through `[C]`".
4. The earlier note's statement that the class-pinching channel "is covariant
   because permutations preserve classes" is correct as far as it goes, but it
   does not by itself say anything about `T_E`, which is not a function of
   `[C]` alone.

## 5. Results

### R1 — Recognition (exact finite enumeration)

| `n` | `k=0` (cardinality) | `k=1` | `k=2` | `k=3` | `k=4` | `k=5` | `k*=n-1` |
|---|---|---|---|---|---|---|---|
| 3 | no | no (2 mixed atoms) | **yes** (5 atoms = 5 classes) | — | — | — | 2 |
| 4 | no | no (3) | no (3) | **yes** (16 = 16) | — | — | 3 |
| 5 | no | no (4) | no (6) | no (8) | **yes** (63 = 63) | — | 4 |
| 6 | no | no (5) | no (14) | no (29) | no (27) | **yes** (318 = 318) | 5 |

"Mixed atoms" counts atoms of the `A_k` partition containing both a history in
`E` and one outside it; `k` recognises `E` iff that count is zero. At `k = n-1`
the atom count equals the class count, so `A_k = A_iso` exactly.

**Measured scaling: `k*(n) = n-1` at every tested stage `n = 3,4,5,6`.**
Recognising the phase event requires access to *all proper subcausets*, i.e.
essentially complete information. Example witnesses (same `k`-stem spectrum,
opposite `E` status, at `n = 4`, `k = 2`):

```
in E :  pasts=(0,0,0,7)  covers=[0<3, 1<3, 2<3]   L=3 h=3  (L-h)mod8=0
out  :  pasts=(0,0,0,3)  covers=[0<3, 1<3]        L=2 h=4  (L-h)mod8=6
```

By contrast, the principal-stem spectrum of Section 3 (Identity I1) *does*
determine `E`, with a two-line proof and no enumeration. So the recognition
threshold is real but not absolute: the phase is a function of the full
local-record collection. It is not a bounded-region observable.

### R2 — Adjoint image: the coherent effect is unreachable for every record channel

Two channel models must be separated, because they give different (and both
correct) statements.

**Model 1 — classical record output (the physically intended one).** The
observer learns the value of `r` and retains nothing else, so the accessible
system is a classical register:
`C_r(ρ) = Σ_a Tr(P_a ρ)|a><a|` with atom projectors `P_a` of the partition
induced by `r`. Then

```
C_r*(Q) = Σ_a Q_aa P_a  ∈  span{P_a},
```

a **commutative** algebra of projectors diagonal in the `|C>` basis. `T_E` has
`<C|T_E|C'> = 1 ≠ 0` for any two distinct `C, C' ∈ E`, so `T_E` is diagonal in
that basis only if `|E| = 1`. Hence `T_E ∉ im(C_r*)` for every event with at
least two histories, at every stage, for **every** record map — cardinality,
stem spectrum, isomorphism class, or anything else. This is the model to which
the `RECORD_LOSS.md` §1 criterion (`C*(Q) = ηT` solvable iff `T ∈ im C*`)
applies verbatim.

**Model 2 — non-demolition measurement that keeps the system.** The observer
dephases by `r` but retains the history register:
`C_r(ρ) = Σ_a P_a ρ P_a`, so `im(C_r*)` is the block-diagonal algebra of the
atom partition. Here `T_E ∈ im(C_r*)` iff no two histories of `E` lie in
different atoms. For `A_iso` that fails: `E` meets two or more classes at every
`n ≥ 3` (13 histories in 13 classes at `n = 4`), so `T_E` is still excluded. It
does *not* fail for the cardinality record (a single atom), but that channel is
the identity — an observer that measures nothing is not restricted, which is
vacuous rather than informative. Model 2 with a partial visibility `γ` is
quantified exactly in R3.

In both models, nothing in the argument uses enumeration: the exclusion is
structural. It is the precise sense in which the earlier comparison's observer
was not a physical observer — `T_E` needs cross-history coherence, which no
record instrument supplies.

What a record observer *can* do is measure the event's indicator. Its
probability is `P_cl(E) = Σ_{C∈E}|A(C)|²`, bounded:

| `n` | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|
| `P_cl(E)` | 0.5000 | 0.2500 | 0.2969 | 0.2422 | 0.2398 | 0.2406 |

Bounded, non-vanishing, apparently converging near 0.24. The quantum measure
`|S_reg|²` at the same stage is `0.5, 0.5, 3.20, 14.41, 150.70, 2293.32`. The
interference share `1 - P_cl/|S_reg|²` is

```
0.0000, 0.5000, 0.9073, 0.9832, 0.9984, 0.9999
```

so from `n = 4` on, **more than 90% and asymptotically essentially all of the
witness's magnitude is cross-class interference** — exactly the part no record
channel can see.

### R3 — Visibility theorem: any dephasing at all kills the effect

Let `Φ_γ = γ·id + (1-γ)·Π` with `Π` the class pinching and `0 ≤ γ ≤ 1` (a
legitimate CPTP convex combination interpolating "full coherence" and
"classical"). Suppose `Φ_γ*(Q) = η T_E` with `0 ≤ Q ≤ I`, `η > 0`.

Take two classes `κ1 ≠ κ2` met by `E`, and unit vectors
`e_i = Π_{κi}u_E/‖Π_{κi}u_E‖`. On `span{e_1,e_2}` the diagonal entries are
unchanged by `Π`, while the off-diagonal entry is multiplied by `γ`:

```
(Q')_ii = η w_i ,   (Q')_12 = η √(w_1 w_2) / γ ,
```

with `w_i = ‖Π_{κi}u_E‖²` (the multiplicity `m_κ` of that class). Positivity of
the compression `Q'` requires

```
det Q' = η² w_1 w_2 (1 - γ^{-2}) ≥ 0,
```

which for `γ < 1` and `η > 0` is strict-negative. Hence:

> **Exact realisation of the phase-aligned quantum measure requires visibility
> γ = 1 on every pair of isomorphism classes met by `E`.**

Checked exactly at `n = 5` on the two largest classes in `E`
(`m = 10, 8`): `det = 0` at `γ = 1` (`0.00`), `-1.62` at `γ = 0.99`, `-240` at
`γ = 0.5`. The threshold is not quantitative — it is exactly `γ = 1`. Any
leakage, any partial which-class record, any decoherence destroys it.

### R4 — What the label quotient actually does to the divergence

Because `A` is class-constant, the divergence is *not* a labelling artefact in
the naive sense: it survives the quotient. But the quotient is not innocent
either, because the register sum carries the labelling multiplicities:

| `n` | `\|S_reg\|²` | `\|S_unl\|²` | `\|S_orb\|²` |
|---|---|---|---|
| 2 | 0.500 | 0.500 | 0.500 |
| 3 | 0.500 | 0.500 | 0.500 |
| 4 | 3.203 | 0.453 | 1.114 |
| 5 | 14.406 | 0.778 | 3.068 |
| 6 | 150.703 | 1.882 | 14.257 |
| 7 | 2293.320 | 4.394 | 77.271 |

All three grow. `S_reg` grows by ≈15× at the last step; `S_orb`, the correctly
normalised quotient amplitude, by ≈5.4×; `S_unl` by ≈2.3×. The
register sum overstates the covariant magnitude by ≈30× at `n = 7`. So the
honest statement is: **the divergent variation survives quotienting birth
labels, at a reduced but still super-polynomial rate in the tested range.** The
earlier note's `|S_n|²` numbers are correct as register sums but are not the
covariant quantity; they differ from it by the labelling multiplicity.

### R5 — No probability diverges

Two accessible probabilities exist and both are bounded:

| `n` | `P_cl(E)` (record observer) | `\|S_reg\|²/\|E\|` (efficiency-limited filter) |
|---|---|---|
| 2 | 0.5000 | 0.5000 |
| 3 | 0.2500 | 0.2500 |
| 4 | 0.2969 | 0.2464 |
| 5 | 0.2422 | 0.1847 |
| 6 | 0.2398 | 0.1371 |
| 7 | 0.2406 | 0.0931 |

`P_cl` is non-vanishing (≈1/4) and bounded; the filter probability decays. The
divergence lives *only* in the amplitude functional, never in a detector
probability. This reproduces, on the growth model, the observation already
recorded for the binary register in `research/event-filter-resources/RESULT.md`
§3, now with an explicit covariance and channel argument.

### R6 — A covariant instrument does exist, at a stated price

`Q_E = |χ_E><χ_E|` with `χ_E = u_E/√|E|` is a rank-one projector and is
label-independent: it is built from the class-defined event and the
class-constant amplitude, so it factors through `[C]` in the sense of Section 4.3.
`{Q_E, I-Q_E}` is a valid instrument with
`P(success) = |S_reg|²/|E|`. Its resources:

- coherent quantum memory spanning `span{|C> : C ∈ E}`, dimension `|E|`
  (`1, 2, 13, 78, 1099, 24624` at `n = 1…7`; asymptotically a fixed fraction of
  `level_n`, so exponential in `n`);
- visibility exactly `γ = 1` on every class pair (R3);
- calibrated knowledge of the class predicate `(L-h) mod 8 ∈ {0,1}`, i.e. of
  `L` and `h` for the actual history — which by `k*(n) = n-1` requires the
  complete stem spectrum;
- the all-input efficiency bound `η ≤ 1/|E|` (from `research/
  event-filter-resources/RESULT.md` §4), which is what makes
  `P = |S_reg|²/|E|` rather than `|S_reg|²`.

So a covariant instrument exists, but it is *precisely* the arbitrary
history-register observer in covariant clothing: complete-history coherent
control, exponential memory, zero dephasing. Nothing about it is local, and
nothing about it is derived from growth beyond the amplitude.

## 6. Scaling and kill criteria

**K1 (channel kill, exact).** If the observer's accessible algebra is a record
algebra — cardinality, any bounded-region stem spectrum, the class algebra, or
any other — then `T_E` is outside the adjoint image (R2) and the quantum measure
of `E` is not measurable. This is unconditional and holds at every stage.

**K2 (coherence kill, exact).** If the class channel has visibility `γ < 1` on
any pair of classes met by `E`, no effect realises the quantum measure (R3).
The threshold is exactly 1, not approximate.

**K3 (recognition kill, finite).** A bounded-region observer with `k ≤ n-2`
cannot even name `E`: `k*(n) = n-1` for `n = 3,4,5,6`. If this scaling holds
for all `n` (unproved; see Section 9, item 2), then no bounded-size local region
recognises the phase, and the event is an essentially global observable.

**K4 (probability kill, exact).** Any accessible probability lies in `[0,1]`
(R5). If a proposed physical reading of "divergent variation" requires a
diverging detector probability, it is killed for every observer in this family.

**Survival criterion.** The divergence survives exactly when an instrument with
`γ = 1` on all classes and coherent access to `span(E)` is granted. Under that
grant, `|S_orb|²` grows (0.5 → 77.3 over `n = 4…7`), so the event is not a
finite-size artefact.

## 7. Priority audit

Read depths are labelled. No exhaustive priority search was performed; the
search tools available in this session were rate-limited, so the audit below is
built from the project's audited source records plus one arXiv metadata query.
No novelty claim is made.

| ID | work | locator | depth here | what it already contains | what this note adds |
|---|---|---|---|---|---|
| S1 | Brightwell, Dowker, Garcia, Henson, Sorkin, *"Observables" in causal set cosmology*, gr-qc/0210061v2, PRD 67 084031 | Sec. 2 (covariant event algebra, all relabellings gauge); Sec. 3 (stem sets, Thm 1) | abstract; inherited full-text record | covariant observables = label-invariant measurable sets; stem sets generate them up to measure zero | applies the level-`n` truncation and measures the access threshold `k*(n)` |
| S2 | Dowker, Surya, *Observables in extended percolation*, gr-qc/0504069v1 | whole paper | abstract; inherited full-text record | stem-set characterisation is complete in extended percolation | none |
| S3 | Surya, Zalel, *A criterion for covariance in complex sequential growth models*, 2003.11311v1 | Sec. 2 (no nontrivial finite-stage cylinder is covariant; condition (a)); Sec. 2.3 Thm 2.1 (bounded variation ⟺ extension); Sec. 3.3 (complex percolation extends only for `q ∈ [0,1]`) | abstract; inherited full-text record | the exact non-extension criterion; the phase model used here is known non-extending | confirms that the divergence computed here is the known non-extension, and separates "amplitude diverges" from "probability diverges" |
| S4 | Dowker, Johnston, Surya, *On extending the quantum measure*, 1007.2725v1 | Claims 1–2 and bounded-variation necessity | abstract; inherited full-text record | complex percolation is non-extending | none |
| S5 | Zalel, *Covariant Growth Dynamics*, 2302.10582v1 | whole chapter | abstract; inherited full-text record | labels as coordinates, covariance as label-invariance, covtree | none |
| S6 | Knuth, *Inferences about interactions* (1212.2332), and Knuth–Bahrenyi, *Special relativity from causal sets* (1005.4172) | abstracts | discovery only | "an observer can be represented by a chain of events" | supports the chain/clock derivation in §4(a); **not** verified beyond abstract |
| S7 | Frauca, Sorkin, 1610.02087v1 | Sec. 5.2, Eqs. (42)–(46) | abstract; inherited full-text record | the equal-superposition event filter and the `1/m` factor | the growth-derived covariance argument and the `γ=1` threshold |
| S8 | `research/event-filter-resources/RECORD_LOSS.md` §1 | — | project derivation, independently reviewed | `C*(Q)=ηT` solvability criterion; Schur-channel obstruction; minimax error | applied here to growth-derived record algebras |
| S9 | `research/operational-stability/RESULT.md` | Thm 1 (extension iff bounded variation), Thm 2 (single-event witness) | project derivation, read in full | divergence of variation = failure of uniform calibration stability = non-extension | used only to interpret `V_n`; not load-bearing |
| S10 | `research/covariant-observer-witness/RESULT.md` | whole note | project derivation, read in full | the `A_card`/`A_iso` comparison and `|S_n|²` values reproduced here as `|S_reg|²` | supplies the baseline; this note adds the third and fourth algebras, the prime-stem identity, the adjoint-image arguments, `γ=1`, `k*(n)=n-1`, and the `√m_κ` correction |

Nearest-predecessor comparison at assumption/result level:

- **S1/S2** give the *event algebra* of covariant observables. They do not give
  a channel, an adjoint image, an access threshold, or a statement about a
  coherent effect. Their covariant algebra is precisely `A_iso` here.
- **S3/S4** give the *measure* obstruction. They do not distinguish the
  amplitude functional from a detector probability, and they do not discuss
  observers.
- **S7/S8** give the *instrument* and the channel criterion in an abstract
  register, without any causal-set growth model.
- The combination — growth factorisation, the principal-stem identity, the
  adjoint-image no-go for record algebras, the exact `γ=1` threshold, and the
  `k*(n)=n-1` access table — is not something I found stated. That is a
  scoped-novelty estimate only; no priority search capable of defeating it was
  completed.

## 8. Mathematical access assumptions versus derived causal-set physics

**Derived from the growth model (checked, not assumed):** amplitude
factorisation (F1); the two normalisations (F2); the phase identity (F3); the
principal-stem formulas for `L` and `h` (I1); class-constancy of the amplitude
(F4/§4.1); the level and class counts.

**Mathematical access assumptions (not derived from causal-set physics):**

1. That an observer is described by a *record map* on `level_n` and nothing
   else. A real observer could have a non-commutative memory, correlated
   ancillas, or pre-channel access.
2. That the record is *covariant* (label-independent). This is the standard
   gauge premise (S1, S3, S5); it is a premise, not a theorem about observers.
3. `A_k`: that "bounded-region access" means the multiset of isomorphism
   classes of all partial stems of size `≤ k`. Other locality notions
   (interval-based, light-cone-based, poset-distance-based) would give different
   partitions and possibly a different threshold.
4. That the chain observer's record is only `|W|`. A chain observer in a
   *labelled* description does see its birth indices.
5. The efficiency bound `η ≤ 1/|E|` assumes all superpositions in the span are
   preparable (`RECORD_LOSS.md` §1, `RESULT.md` §4). A restricted dynamical
   preparation family can evade it.
6. `γ` is a *modelling* visibility, not computed from any decoherence model.

**Not claimed:** that any cosmological observer has access to the complete stem
spectrum; that `A_iso` is the "right" physical algebra; that the phase model is
the causal-set dynamics; that the finite-stage quotient equals the infinite
covariant algebra.

## 9. Limitations and unresolved questions

1. **Finite stage only.** Sums to `n = 7`; access thresholds and isomorphism
   brute-forcing to `n ≤ 6`/`5`. A finite-stage result has that domain only. In
   particular **divergence of `|S_orb|²` is not proved**: the tested ratios
   (2.8, 4.6, 5.4) suggest it, but five points are not a theorem.
2. **`k*(n) = n-1` is measured, not proved.** It holds at `n = 3,4,5,6`. A
   general proof would need, for each `n` and each `k ≤ n-2`, an explicit pair
   with equal `k`-stem spectra and `(L-h)` differing mod 8. The enumeration
   supplies such pairs at each tested stage but no uniform family.
3. **The finite-stage quotient is a truncation.** In the infinite growth model
   the covariant algebra is generated by stem sets (S1) and no nontrivial
   finite-stage cylinder is covariant (S3 Sec. 2). `A_iso` here is the stage-`n`
   truncation, not the infinite covariant algebra.
4. **The amplitude model is a known non-extending one.** At `p = (1+i)/2`,
   complex percolation has unbounded variation (S3 Sec. 3.3, S4), so in the
   infinite limit the quantum measure does not extend to the covariant
   σ-algebra at all. Then "the quantum measure of the phase-aligned covariant
   event" does not exist in the infinite model; only finite-stage sums do. This
   is the deepest limitation and it is a property of the model, not of the
   observer analysis.
5. **No observer dynamics.** Nothing here models how a record is physically
   written, how a region is selected, or what fixes `γ`.
6. **`A_p(C) = p^L q^h` is not a Bell-causal QSG dynamics.** It factorises over
   births and reproduces the percolation normalisation, but no Bell causality
   condition is imposed or checked. `research/csg-quantum/` records
   Srivastava–Surya 2603.25503 on implementing Bell causality in QSG; that is
   the natural place to look for a physically motivated amplitude.
7. **The event `E` is model-specific.** `(L-h) mod 8` is tied to `p` on the
   `|p| = |q|` circle. Other phases give other events; the general lesson (the
   quantum measure needs cross-class coherence, a record observer sees only the
   diagonal) is what transfers, not the specific event.
8. **No dynamical selection argument.** Even with `γ = 1` granted, nothing
   explains why a causet dynamics would grant it.

## 10. Reproduction

```
python3 research/observer-growth-channel/check.py        # ~33 s, 45 checks
python3 research/observer-growth-channel/check.py 6      # ~10 s, sums to n=6
```

`check.py` is standard library only, exact rational complex arithmetic, and
prints every asserted number. `sources.jsonl` records the source provenance at
the depths used.
