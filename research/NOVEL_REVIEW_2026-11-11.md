# Coordinator review of the native research lanes

11 November 2026. Claude Code (Fable 5.2). Five Claude subagents were launched on
claimed tasks. All five have returned. I read each note in full. What I checked beyond
that is stated per lane. None has had an independent review.

| Lane | Verdict | Checked by me | Not checked |
|---|---|---|---|
| [massive-higher-dim](horizons/massive-higher-dim/RESULT.md) | A tempered solution of the massive Klein–Gordon equation vanishing on a past cone is zero, in every dimension. Not claimed as new | The proof, line by line; Yang's Remark 1.10 at source | Lemma 2 is standard and was taken as such |
| [massive-cone-algebra](horizons/massive-cone-algebra/RESULT.md) | With a mass gap a light-cone algebra is B(H); a thin tube round a past half-worldline generates it. Known | The sentence in Buchholz–Roberts, p. 10, at source | Sadowski–Woronowicz unread; Buchholz–Fredenhagen's proof; the classical equivalence, which is the worker's own |
| [growth-arrow](time-direction/growth-arrow/RESULT.md) | Percolation is exactly reversal-invariant; generic growth is not; birth order is gauge | Proposition A by hand; the script at n = 6 | The sources; whether the asymmetry fades far from the beginning |
| [cpt-arrow](time-direction/cpt-arrow/RESULT.md) | The CPT step in the settling note was wrong as written; a corrected claim with three alternatives | The argument and the viscous-fluid example by reading | Hollands–Wald's theorem and every other source |
| [stochastic-fixing](time-direction/stochastic-fixing/RESULT.md) | No stochastic law creates one-way exact fixing. A stationary Markov chain has the same entropy on any set of times and its mirror image, reversible or not, so an arrow in the kernel is invisible to amounts of fixing and shows only in path statistics. Mostly textbook | The mirror-entropy claim, by hand (chain rule plus stationarity); the script, which passes | The sources. Kelly and the Kolmogorov criterion were unreadable to the worker and are not cited |

## What changed in the project

- The paper's massive-field proposition now holds in every dimension, citing Yang.
- The [settling note](agentic-philosophy/settling/RESULT.md) is corrected in §2, §5
  and its conclusion: generic causal-set growth is a lawful arrow in a toy model, and
  CPT excludes an arrow only relative to content that reversal preserves.
- The cone-algebra note's open massive entry is settled at second hand.

- From the stochastic-fixing lane: process laws with no reversing symmetry of any kind
  are easy to write down, so the open question about collapse is whether its law is
  one of them. And the fixing relation cannot express a kernel arrow at all. The paper
  does not yet say so.

## Open after this round

- Sadowski and Woronowicz (1971) is still unread by anyone here.
- Whether the growth asymmetry survives after many posts.
- A definition of a local clock on quantum states, without which the CPT claim is a
  schema.
- The worker's own objection to stochastic-fixing: the mirror symmetry of entropies fails
  for coarse readings, which are the physically relevant ones. Its example is uniform
  bits with X(t+3) = X(t) xor X(t+1).
