#!/usr/bin/env python3
"""Bounded exact checks for the stated memory family and error allocation."""
from fractions import Fraction
import json


def relation_from_mask(n, mask):
    a = n // 2
    pairs = [(i, j) for i in range(a) for j in range(a, n)]
    rel = {(i, j) for k, (i, j) in enumerate(pairs) if (mask >> k) & 1}
    return pairs, rel


def check_poset(n, rel):
    assert all(i != j for i, j in rel)
    assert all(not (j, i) in rel for i, j in rel)
    for i, j in rel:
        for k, ell in rel:
            if j == k:
                assert (i, ell) in rel


def main():
    counts = {}
    for n in range(2, 9):
        pairs, _ = relation_from_mask(n, 0)
        seen = set()
        for mask in range(1 << len(pairs)):
            pairs2, rel = relation_from_mask(n, mask)
            check_poset(n, rel)
            encoding = tuple(sorted(rel))
            assert encoding not in seen
            seen.add(encoding)
            assert pairs2 == pairs
        expected = 1 << ((n // 2) * (n - n // 2))
        assert len(seen) == expected
        counts[str(n)] = {"cross_edges": len(pairs), "distinct_posets": len(seen), "expected": expected}

    gap = Fraction(399999, 30000000)
    beta = gap / 8
    growth_each = [beta * Fraction(1, 2 ** (n - 1)) for n in range(3, 80)]
    growth_sum = sum(growth_each, Fraction(0))
    assert growth_sum == beta * (Fraction(1, 2) - Fraction(1, 2 ** 78))
    per_model = 4 * beta + 2 * growth_sum
    assert per_model < 5 * gap / 8
    assert per_model < gap
    retained = gap - per_model
    assert retained > 3 * gap / 8
    # For m identical per-step channel errors epsilon, this simple bound grows as 2m epsilon
    # when forward and reverse uses are both charged.
    eps = Fraction(1, 1000000)
    fixed_depths = {str(m): 2 * m * eps for m in (1, 10, 100, 1000)}
    out = {
        "bounded_poset_counts": counts,
        "gap": str(gap),
        "beta": str(beta),
        "per_model_error_bound_infinite_schedule": str(5 * gap / 8),
        "retained_gap_bound": str(3 * gap / 8),
        "growth_sum_below_beta_over_2": True,
        "fixed_per_stage_two_pass_error_examples": {k: str(v) for k, v in fixed_depths.items()},
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
