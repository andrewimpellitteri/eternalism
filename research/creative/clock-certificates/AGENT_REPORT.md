# Agent report — creative clock certificates

## Files changed

- `research/creative/clock-certificates/claim-contract.md`
- `research/creative/clock-certificates/addendum-dowker-zalel.md`
- `research/creative/clock-certificates/addendum-general-p.md`
- `research/creative/clock-certificates/AGENT_REPORT.md`

## Result

For the initial clock probe, I considered four hypotheses: an
interaction/autonomy no-go, failure of the trinity for non-ideal finite clocks,
an autonomy/information-leakage tradeoff, and a frame-switching recovery echo.
The first has a bounded finite counterexample in Ludescher et al.,
arXiv:2607.24976v1, Example 32, with n=3 and K=1. Its interaction does not
commute with the local clock generator P1, yet the non-local center-of-mass
instrument yields a fixed effective generator; the local particle-clock
reduction is step-dependent. The broad non-ideal-clock trinity conjecture is
preempted by the 2019 and 2024 trinity papers under their stated assumptions.
Broad frame-switching reversibility is already treated by operational QRF,
extra-particle, and perspective-neutral work.

For that initial clock probe, no new theorem or counterexample is claimed. Its
only unselected lead is a clock-specific quantitative relation between
autonomy defect and complementary-channel information leakage. The claim
contract states the requirements needed to make it precise and QEC criteria
that could show it is a repackaging.

Two later independent skeptic addenda audit a separate CTP measure-extension
candidate. The fixed-parameter addendum checks the capped principal-block
construction for p=(1+i)/2, including a small independent exact enumeration of
the 40 principal five-element gadgets. The general-parameter addendum checks
the normalized-modulus argument: a real Bernoulli transitive-percolation
connectivity event, Harris's inequality, and finite-block growth imply a
proposed non-extension result for every p outside [0,1] on
tilde R_p. These are mathematical proof audits, not formalized proofs or
accepted novelty claims. Both addenda withhold conclusions about the covariant
intersection R_p.

## Evidence and checks

- Read project guidance and the initial task brief. Read the integrated
  novelty audit, source manifest/search log, and relevant clock defeat-search
  notes.
- Opened primary arXiv texts for 2409.06479v3, 2607.24976v1, 1912.00033v3,
  and 1712.00081v3. Checked the assumptions, exact finite Example 32 equations,
  and the non-ideal clock/trinity claims at their section/equation locators.
- Checked primary-source abstracts and selected article text for
  1709.04471v3, 2207.13707v2, 2303.14002, 2110.13199, and 2508.09540; their
  read depths and theorem-audit limits are marked in the claim contract.
- For the fixed-parameter CTP audit, a small standard-library exhaustive check
  over 64 relation masks on four ordered labels reproduced the principal-gadget
  exponent histogram. No dependencies or large runs were used.
- For the general-parameter CTP audit, the labeled-order probability identity,
  connected-Hasse-graph exponent bound, Harris lower bound, and repeated-block
  argument were checked analytically. They were not encoded in a proof
  assistant or tested by a second implementation.
- No tests were added or run. The initial clock probe involved no code and no
  independent proof reproduction; that statement does not apply to the later
  mathematical audits above.

## Limitations and unresolved questions

- No systematic forward-citation search was done. Recent sources and all
  supplements are not exhausted.
- The clock H3 autonomy/leakage direction remains underspecified until the
  instrument, noise channel, reachable domain, observable algebra, and distance
  are fixed. It must be compared exactly against complementary-channel and
  approximate Knill–Laflamme criteria before any finite calculation.
- The finite clock counterexample defeats only the broad autonomy impossibility
  claim. Example 32's interaction commutes with the global translation part of
  the constraint, although it fails to commute with the local clock generator
  P1. It does not settle arbitrary noncommuting constraints or instruments.
- The CTP addenda depend on matching the intended extension problem to the
  prescribed amplitudes on all doubly-principal cylinder generators. The
  general argument addresses tilde R_p only, not its covariant intersection
  R_p; novelty and priority remain unverified.
- No ontological consequence is supported.
