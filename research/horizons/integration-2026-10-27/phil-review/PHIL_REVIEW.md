# Philosophical and source-scope review of the horizons integration

Reviewed file: `research/horizons/main.tex`, SHA-256
`fa438d7708a75601b9caff5fd18bcba4712a168c17aa1a5ddc6211383bdce2a3`.
This hash identifies the shared-checkout version read for this review. No
manuscript changes were made.

Comparison set: `research/horizons/native/bridge-recovery/REPLACEMENT.md`,
`research/horizons/native/bridge-recovery/CLAIM_MAP.md`, and
`research/horizons/native/source-recovery/SOURCE_GAPS.md`. Read depth for the
three internal notes and the relevant manuscript passages: full text. This is
a bounded philosophical/source-scope review, not an independent proof audit,
source reinspection, novelty assessment, or release-readiness judgment.

## Overall assessment

The integration is careful on the central distinction. It defines `real from`
as a fragment-relative premise, `guaranteed from` geometrically, and `fixed
from` relative to a specified solution class. It explicitly requires the
domain-of-dependence uniqueness property, and says that this is not inferred
from operational no-signalling (main.tex, around lines 130–151). The text also
preserves both the deterministic growing-block response and the eternalist
response (around lines 675–683), and does not claim that the physics chooses
between them. Its selected Earman disclosure and no-priority sentence
(around lines 314–319) are aligned with the source-recovery note.

I found no remaining substantive overclaim about ontic openness in the
philosophical section. Three small wording changes would make the strongest
scope limits harder to miss: avoid calling the result itself a “relativistic
form” of growing block; state the Cauchy-data determinism premise in the
second enumerated conclusion; and make the Earman disclosure explicitly say
that the pages were visually inspected and that Ellis–Sciama is known here
only through Earman's citation. The companion-theorem introduction is already
appropriately bounded to globally hyperbolic metric spacetimes and
preservation-and-reflection under causally convex isometric embeddings.

## Bounded replacement proposals

These are proposals for the coordinator to consider, not edits.

### 1. Growing block analogy (main.tex around lines 653–656)

Current wording: “This is the relativistic form of the growing block combined
with determinism”. The examples establish compatibility between fragment
unreality and law-relative fixing under named laws. Calling that the
relativistic form of a metaphysical view risks suggesting that the examples
derive or instantiate an ontology.

Suggested replacement:

> These examples illustrate a compatibility claim often made by deterministic
> growing-block views: an event may be absent from a standpoint's real fragment
> while its value is fixed relative to the stipulated laws and solution class.
> Rak\'ic's sea-fight case can be read in this way \citep{Rakic1997}: at most,
> the outcome is fixed from the observer, not real from her.

This preserves the named precedent and accurately presents the connection as
an interpretation of the result.

### 2. Determinism and Cauchy data (main.tex around lines 657–664)

Current wording begins: “Under deterministic laws the whole spacetime is fixed
by data on any Cauchy surface”. In context this is standard shorthand, but the
paper's own definition makes fixing relative to a solution class. A bare
determinism label can obscure the needed uniqueness of the Cauchy problem.

Suggested replacement for the first sentence of item 2:

> For a law and admissible solution class with unique evolution from Cauchy
> data, data on a Cauchy surface fix the solution throughout the spacetime;
> nevertheless, no single event's past contains a Cauchy surface in the flat,
> open, radiation or de Sitter models.

The following model-specific sentences can remain. This keeps determinism
distinct from the local domain-of-dependence premise and from observational
no-signalling.

### 3. Earman disclosure (main.tex around lines 314–319)

Current disclosure correctly says that selected Earman pages were checked,
Ellis and Sciama pp. 41–42 were not, the model-specific result may overlap,
and no priority claim is made. For exact provenance, I recommend replacing
the two sentences beginning “We have checked” with:

> We visually inspected Earman's selected pages 125–130; the cited
> Ellis–Sciama pages were not available for inspection here, and their result
> is known in this comparison only through Earman's citation and discussion.
> The model-specific characterization below may overlap with this prior work;
> we make no priority claim for it.

This is consistent with `SOURCE_GAPS.md`: Earman's original scanned pages were
visually inspected; the chapter pages by Ellis and Sciama remain unread.
It avoids turning the limited access into evidence about what Ellis and Sciama
did or did not establish.

## Scope checks requested

- **Companion theorem category and nontrivial branch:** The introduction says
  the companion classifies relations assigned uniformly to globally
  hyperbolic metric spacetimes, names chronological becoming and transitivity,
  and specifies preservation and reflection under causally convex isometric
  embeddings. It then confines the chronological-past/causal-past conclusion
  to the nontrivial branch. This matches the replacement contract. The
  accompanying sentence expressly says this is a metric-only requirement,
  not merely no-superluminal-signalling; it also acknowledges that clock- or
  foliation-preserving categories alter the assumptions. No further broad
  claim about all physically admissible spacetimes appears in this passage.
- **No-signalling versus uniqueness:** The definition of the
  domain-of-dependence property is a uniqueness condition on pairs of
  solutions agreeing on an open set; the manuscript explicitly disclaims
  inferring it from operational no-signalling. Preserve this distinction.
- **Growing block and eternalism:** The two replies are stated symmetrically.
  The growing-block reply may treat later addition as openness even when
  values were previously law-fixed; whether that suffices is left semantic
  and philosophical. The eternalist may accept the same fixing facts while
  affirming that all events exist. This captures the strongest responses in
  the bridge-recovery note.
- **Ontology, fixedness, and measurements:** The manuscript does not infer
  existence from fixing or openness from nonfixing. It identifies the
  background and solution class as inputs, and says practical prediction
  requires a measurement process, observable, error norm, and tolerance.
  The mass result concerns exact past agreement under a changed law; the norm
  estimate is conditional on the stated conformal-data norm. The separate
  noisy-record discussion and spectral-cutoff caveat prevent either from
  being presented as a detector or general stability theorem.
- **Persistence:** The logic remark explicitly distinguishes tenseless
  past-event valuations from centered claims such as “this event is present
  now,” and treats persistence as an additional constraint with separate
  logical consequences. This is the right limitation. Avoid adding an
  unqualified claim that the standpoint logic establishes persistence or
  objective passage.
- **Grounding:** The final limits paragraph presents fragmentalist grounding
  as a proposal requiring an independently defended explanatory asymmetry;
  it says no established truth-conditional or empirical consequence follows
  for the fixing relations. This matches the replacement contract and leaves
  room for the eternalist response.
- **Source scope:** Earman is cited for the checked Cauchy-surface exception,
  prediction discussion, and electromagnetic-constraint example. The text
  neither attributes a precise theorem to unread Ellis–Sciama pages nor says
  that Earman lacks the exact model-specific theorem. The no-priority language
  is appropriate. Wald is cited for a conformal identity, but this review did
  not inspect Wald; `SOURCE_GAPS.md` records that its locator is discovery-level
  in that recovery lane. This is a source-verification question, outside the
  philosophical wording changes proposed above.

## Limits and unresolved points

The shared checkout already contained changes to `main.tex` when inspected;
the hash above pins the exact reviewed bytes, but this review does not identify
which edits produced them. I did not rebuild the PDF, test mathematics, inspect
the external sources independently, or make any novelty or release-readiness
claim. If the coordinator wants to act on the three wording proposals, they
should recheck the current file and its hash first.

## Follow-up verification

On 2026-10-27 I rechecked the updated `research/horizons/main.tex`. Its final
SHA-256 for this follow-up is
`ff095411f7080b01cf5046ed127c4e73b188c0265e4445c524f0f79822734769`.
The growing-block sentence now presents compatibility as an illustration;
the determinism sentence expressly requires unique evolution from Cauchy
data; and the source disclosure says that selected original Earman pages were
checked while Ellis–Sciama pp. 41–42 remain unread and enter through Earman's
discussion. These match the bounded proposals, with source-method detail kept
concise in the manuscript.

I also verified the math-review clarifications in the follow-up: the mass
proposition fixes `a_m>0`, and the norm-bound application explicitly defines
`h_m` as the rescaled difference `a(\phi_1-\phi_2)`. The manuscript was not
edited during this verification. The hash pins the exact current source
checked; no proof, build, novelty, or release-readiness claim is made.
