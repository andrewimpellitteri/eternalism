"""Exhaustive finite controls for an extensional sufficiency contract.

The mathematical proof is in RESULT.md. These controls do not establish
metaphysical grounding, physical possibility, or the scalar PDE theorem.
"""
from itertools import product
import json


def constant_on_fibres(signature, valuation):
    return all(signature[i] != signature[j] or valuation[i] == valuation[j]
               for i in range(len(signature)) for j in range(len(signature)))


def admits_assignment(signature, valuation):
    labels = sorted(set(signature))
    return any(all(candidate[labels.index(g)] == v
                   for g, v in zip(signature, valuation))
               for candidate in product([False, True], repeat=len(labels)))


def main():
    examined = 0
    for signature in product(range(4), repeat=4):
        for valuation in product([False, True], repeat=4):
            assert constant_on_fibres(signature, valuation) == admits_assignment(
                signature, valuation)
            examined += 1

    # Four complete models: (past label, future outcome).
    models = list(product(range(2), repeat=2))
    past = [p for p, outcome in models]
    outcome = [bool(outcome) for p, outcome in models]
    enriched = list(range(len(models)))
    assert not admits_assignment(past, outcome)
    assert admits_assignment(enriched, outcome)

    # One future claim requires less discrimination than a separating
    # two-proposition language. This blocks a whole-history inference from
    # the mere existence of one bivalent future truth.
    target_one = [False, False, True, True]
    target_two = [False, True, False, True]
    signature_one = [0, 0, 1, 1]
    assert admits_assignment(signature_one, target_one)
    assert not admits_assignment(signature_one, target_two)
    print(json.dumps({
        "scope": "finite extensional controls, not metaphysical/PDE verification",
        "assignments_examined": examined,
        "constant_fibre_iff_assignment": True,
        "past_signature_insufficient_for_chosen_future_outcome": True,
        "enriched_signature_extensionally_sufficient": True,
        "one_proposition_need_not_select_whole_model": True,
    }, indent=2))


if __name__ == "__main__":
    main()
