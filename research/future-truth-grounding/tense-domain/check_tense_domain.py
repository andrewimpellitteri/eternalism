#!/usr/bin/env python3
"""Finite, dependency-free check of the tense-domain toy in RESULT.md.

Only growth stages are modeled. F_g quantifies over later stages; no within-
block F_t operator is present. Source labels identify Loss's reported
diagnosis/repair, not an independent reconstruction of the 2012 chapter.
"""

STAGES = ("s0", "s1", "s2")
DOMAINS = {
    "s0": frozenset({"a"}),
    "s1": frozenset({"a", "b"}),
    "s2": frozenset({"a", "b", "c"}),
}
INDEX = {stage: i for i, stage in enumerate(STAGES)}

SOURCE_FROZEN = (
    "Loss 2021, §3, PMC HTML lines 212–222: his diagnosis that the fixed-"
    "timeline quantifier misses stage growth (Loss's reconstruction of B&F)."
)
SOURCE_REPAIR = (
    "Loss 2021, §3, PMC HTML lines 223–241: stage/timeline shifts plus a "
    "timeline-sensitive quantifier (author's proposed repair)."
)
SOURCE_TERMINAL = (
    "Finite toy consequence only: RESULT.md model ends at s2; it does not "
    "represent Loss's assumed ongoing growth."
)


def later_stages(stage):
    """Return stages strictly later than stage on the toy's sole history."""
    return STAGES[INDEX[stage] + 1 :]


def past_exists(entity, stage):
    """Whether entity occurred in a domain at any earlier growth stage."""
    i = INDEX[stage]
    return any(entity in DOMAINS[earlier] for earlier in STAGES[:i])


def fresh_birth_formula(origin, mode):
    """Evaluate F_g (exists x not PastExists_g(x)) at origin.

    mode='shifting' uses the domain at each future evaluation stage.
    mode='frozen' keeps the quantifier domain at the origin stage.
    Return (truth, witness-or-None).
    """
    if mode not in {"shifting", "frozen"}:
        raise ValueError("mode must be 'shifting' or 'frozen'")
    for evaluation_stage in later_stages(origin):
        domain_stage = evaluation_stage if mode == "shifting" else origin
        for entity in sorted(DOMAINS[domain_stage]):
            if not past_exists(entity, evaluation_stage):
                return True, (evaluation_stage, entity)
    return False, None


def main():
    print("Finite growth-stage model:")
    for stage in STAGES:
        print(f"  {stage}: D={sorted(DOMAINS[stage])}")

    for mode, source in (("frozen", SOURCE_FROZEN), ("shifting", SOURCE_REPAIR)):
        truth, witness = fresh_birth_formula("s0", mode)
        print(f"\nAt s0, {mode} domain: F_g exists x not PastExists_g(x) = {truth}")
        print(f"  witness: {witness}")
        print(f"  source label: {source}")

    truth, witness = fresh_birth_formula("s2", "shifting")
    print(f"\nAt terminal s2, shifting domain: F_g exists x not PastExists_g(x) = {truth}")
    print(f"  witness: {witness}")
    print(f"  source label: {SOURCE_TERMINAL}")


if __name__ == "__main__":
    main()
