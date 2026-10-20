# Foundations full-text claim spot-check

I audited the seven sampling-frame entries assigned to `audit_lane="foundations"`:
three RC-2 contract anchors, two foundations-stratum draws, and the two required
primary attempts. Findings are recorded individually in `findings.jsonl`.
The sampling frame and frozen source-register copies were read as supplied; I
did not edit a source register, contract, or another lane.

## Results

Five entries are confirmed at the bounded statement/argument level, one has a
locator correction, and one primary text remains unreadable. No proof was
independently reproduced. The short excerpts in `findings.jsonl` are all under
20 words per source.

- `found-malament-1977`: the primary Noûs scan was accessible through a
  university-hosted reading archive. Sections 1–3, including Propositions 1–3,
  were read. The earlier abstract-only status is resolved; the proposition
  summary in the SEP is substantially right, while the primary distinguishes
  explicit definability from the weaker automorphism-invariance condition in
  Proposition 2. This supports RC-2's conditional simultaneity result, not an
  unconditional physical or ontological conclusion.
- `found-sarkar-stachel-1999`: the BU-hosted primary journal scan was readable in
  the browser. I checked its abstract, Section 2, and Section 3 Theorems 1–2.
  The recorded temporal-reflection critique and conditional uniqueness claims
  are supported. The assumptions field should name the separate conditions of
  Theorems 1 and 2, rather than grouping them generically.
- `found-sep-malament`: the Winter 2001 SEP archive is readable and its author,
  archive date, and Malament section were verified. It is a sound secondary
  summary, but the primary text is required for RC-2's primary-source support.
- `found-stein-1991`: Cambridge Core confirms the bibliographic record and
  abstract. The body was read from a Paperzz-hosted scan reproducing journal
  pagination, including pp. 148–150 in sequence. The accessible OCR's displayed
  theorem sentence lists reflexivity, transitivity, time-orientation-preserving
  invariance, and one past causal pair, then concludes exactly causal past. That
  isolated implication is false: universal R is a counterexample, and the
  reflexive chronological-past relation omits past-null pairs. The immediately
  preceding argument supplies two further contextual premises: all points in
  the causal past are R-related, and condition (iv) leaves some states unsettled
  at every point. It uses those premises with invariance/transitivity to exclude
  extra spacelike/future pairs. I could not compare the OCR with a printed-page
  image, so whether the theorem/context mismatch originates in print, OCR, or
  extraction remains unresolved. The sample's modest compatibility claim is
  supported; it does not establish physical indeterminism or objective passage.
  RC-2's stronger context-preserving formal characterization and premise
  necessity table remain project proof obligations, not results established by
  this spot-check.
- `aqft-fewster-verch-2012-kg`: the versioned arXiv HTML confirms the model and
  Theorem 4.3 claim. It is specifically the massless-current quotient; the
  dimensional exception is for disconnected-spacetime category `Loc` at
  dimension 2. The proposed topological-charge remedy is the authors' conjecture.
- `arrow-wallace-gravity-entropy-2009`: the arXiv v1 text supports the bounded
  matter-entropy/radiation claim. The frozen locator skips Section 7, where the
  specific material-entropy decrease and radiation compensation are stated;
  update the locator to include that section. This remains Wallace's bounded
  statistical-mechanical argument, not a universal entropy formula.
- `found-stein-1968`: the primary text remains inaccessible through the public
  routes tried. JSTOR's stable article page exposed metadata only. PhilArchive
  lists a public archived version, but its PDF endpoint returned HTTP 403.
  JSTOR issue contents and PhilPapers verify author, title, venue, pages, and
  DOI only. I did not use non-authoritative Scribd snippets as evidence.

## Contract impact and access status

RC-2's primary Malament dependency is now independently read and its prior
abstract-depth limitation is resolved for coordinator consideration. The SEP
entry remains secondary and is not a substitute. Sarkar–Stachel supports the
need to keep temporal-reflection invariance explicit as a premise; it does not
settle whether that premise is physically warranted. Stein 1991's surrounding
argument motivates a context-preserving causal-past result, but its displayed
OCR theorem sentence is false in isolation, and this spot-check does not prove
the reconstructed theorem or its premise-necessity table. The printed-page
status of the mismatch remains unresolved. The unread Stein 1968 record does not
directly underwrite the current RC-2 theorem statement, which principally cites
Stein 1991; any claim attributed specifically to Stein 1968 remains unsupported
until its primary text is read.
The two stratified papers have no direct `contract_ids` in the sampling frame.

Primary-read status is therefore resolved for Malament 1977 and Stein 1991; the
primary Stein 1968 attempt is documented as inaccessible after JSTOR and
PhilArchive attempts. Sarkar–Stachel's original article and Fewster–Verch's
versioned arXiv text were read. The SEP archive is verified as a secondary
record. Wallace's versioned arXiv text was read at the claim level.

All seven assigned records have entries in `findings.jsonl`. Work was limited
to the accessible text and the specific recorded claims. I did not audit full
proofs, reproduce calculations, or resolve the broader philosophical debates.
