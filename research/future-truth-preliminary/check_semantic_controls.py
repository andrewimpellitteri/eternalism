"""Small countermodels, not a proof of the PDE or a metaphysical result."""
from itertools import product
import json


def settled(values):
    assert values, "An admissible completion class must be nonempty"
    return "true" if all(values) else "false" if not any(values) else "open"


def main():
    checks = {}
    rain = [True, False]
    checks["history_truth_is_not_settlement"] = settled(rain) == "open"
    checks["excluded_middle_supertrue_without_either_disjunct"] = (
        settled([p or not p for p in rain]) == "true"
        and settled(rain) == settled([not p for p in rain]) == "open"
    )
    checks["nonfixed_value_can_have_settled_sign"] = (
        len(set([1, 2])) > 1 and settled([v > 0 for v in [1, 2]]) == "true"
    )
    diagonal = [(q, q) for q in [-2, -1, 0, 1, 2]]
    checks["varying_coordinates_need_not_vary_relation"] = (
        len({a for a, _ in diagonal}) > 1
        and len({b for _, b in diagonal}) > 1
        and settled([a == b for a, b in diagonal]) == "true"
    )
    # Test all subsets of a four-world space and all refinements of one
    # equivalence class. This checks the finite set-theoretic persistence
    # statement, not persistence of indexical content or ontology.
    worlds = set(range(4))
    subsets = [set(i for i, yes in enumerate(bits) if yes)
               for bits in product([False, True], repeat=4)]
    checks["fixed_proposition_settlement_persists_under_refinement"] = all(
        not (small <= large and large <= proposition) or small <= proposition
        for small in subsets if small
        for large in subsets if large
        for proposition in subsets
    )
    # Two models have identical proposed complete grounds. Outcome matching
    # forces opposite truth values, so no Boolean assignment also supervenes
    # on those grounds. This checks the logical skeleton of A+B+C only.
    outcomes = [True, False]
    permitted = [assignment for assignment in product([False, True], repeat=2)
                 if assignment[0] == assignment[1]
                 and list(assignment) == outcomes]
    checks["same_grounds_outcome_matching_obstruction"] = not permitted
    # Contrast unrestricted scaling (proved in the note) with a common bound.
    reference, bound, threshold = 2, 0.5, 0
    checks["bounded_ambiguity_can_preserve_threshold"] = (
        reference - bound > threshold
        and settled([reference + d > threshold for d in [-bound, 0, bound]]) == "true"
    )
    checks["empty_class_guard"] = False
    try:
        settled([])
    except AssertionError:
        checks["empty_class_guard"] = True
    assert all(checks.values()), checks
    print(json.dumps({"scope": "finite illustrative semantic controls only",
                      "checks": checks}, indent=2))


if __name__ == "__main__":
    main()
