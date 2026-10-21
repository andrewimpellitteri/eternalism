#!/usr/bin/env python3
"""Exact checks for the manuscript's finite examples, not an ontology test."""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
import unittest


def enumerated_path_law():
    """Closed-form product for the declared three-time binary chain."""
    return {
        path: Q(1, 2)
        * Q(3 if path[0] == path[1] else 1, 4)
        * Q(3 if path[1] == path[2] else 1, 4)
        for path in product((0, 1), repeat=3)
    }


def sequential_path_law():
    """Separate implementation: iteratively extend weighted prefixes."""
    prefixes = {(0,): Q(1, 2), (1,): Q(1, 2)}
    for _ in range(2):
        extended = {}
        for prefix, weight in prefixes.items():
            extended[prefix + (prefix[-1],)] = weight * Q(3, 4)
            extended[prefix + (1 - prefix[-1],)] = weight * Q(1, 4)
        prefixes = extended
    return prefixes


def pushforward(law, record):
    result = defaultdict(Q)
    for path, weight in law.items():
        result[record(path)] += weight
    return dict(result)


def causal_law(kind, intervention=False):
    """A: X=Z,Y=X; B: X=Z,Y=Z. do(X=0) replaces only X's rule."""
    if kind not in {"A", "B"}:
        raise ValueError("unknown causal model")
    result = defaultdict(Q)
    for z in (0, 1):
        x = 0 if intervention else z
        y = x if kind == "A" else z
        result[(x, y)] += Q(1, 2)
    return dict(result)


class ManuscriptExamples(unittest.TestCase):
    def test_full_history_laws(self):
        formula, sequential = enumerated_path_law(), sequential_path_law()
        self.assertEqual(formula, sequential)
        self.assertEqual(len(formula), 8)
        self.assertEqual(sum(formula.values()), 1)
        self.assertEqual(formula[(0, 0, 0)], Q(9, 32))
        self.assertEqual(formula[(0, 1, 0)], Q(1, 32))

    def test_all_prefix_marginals(self):
        for length in range(1, 4):
            with self.subTest(length=length):
                a = pushforward(enumerated_path_law(), lambda p: p[:length])
                b = pushforward(sequential_path_law(), lambda p: p[:length])
                self.assertEqual(a, b)
                self.assertEqual(sum(a.values()), 1)

    def test_adaptive_revealed_prefix_protocol(self):
        # Read at time 1 if the time-0 bit was 0; otherwise read at time 2.
        def record(path):
            selected_time = 1 if path[0] == 0 else 2
            return path[0], selected_time, path[selected_time]

        a = pushforward(enumerated_path_law(), record)
        b = pushforward(sequential_path_law(), record)
        self.assertEqual(a, b)
        self.assertEqual(a[(0, 1, 0)], Q(3, 8))
        self.assertEqual(a[(1, 2, 1)], Q(5, 16))

    def test_same_passive_different_interventional_laws(self):
        self.assertEqual(causal_law("A"), causal_law("B"))
        self.assertEqual(causal_law("A", True), {(0, 0): Q(1)})
        self.assertEqual(causal_law("B", True), {(0, 0): Q(1, 2), (0, 1): Q(1, 2)})
        self.assertNotEqual(causal_law("A", True), causal_law("B", True))

    def test_two_system_four_event_coverage_model(self):
        """The paper's finite (a)+(b)-without-proper-union model."""
        world = {"a", "b", "c", "d"}
        history_1, present_1 = {"a", "b", "c"}, {"a", "b"}
        history_2, present_2 = {"b", "c", "d"}, {"c", "d"}
        self.assertTrue(present_1 < world)
        self.assertTrue(present_2 < world)
        self.assertTrue(present_1 < history_1)
        self.assertTrue(present_2 < history_2)
        self.assertEqual(present_1 | present_2, world)

    def test_pointwise_agreement_need_not_equal_marginal_evidence(self):
        # Identical conditional models with different priors over theta.
        probabilities = (Q(1, 4), Q(3, 4))
        first_prior, second_prior = (Q(3, 4), Q(1, 4)), (Q(1, 4), Q(3, 4))
        first = sum(p * w for p, w in zip(probabilities, first_prior))
        second = sum(p * w for p, w in zip(probabilities, second_prior))
        self.assertEqual(first, Q(3, 8))
        self.assertEqual(second, Q(5, 8))
        self.assertNotEqual(first, second)


if __name__ == "__main__":
    unittest.main(verbosity=2)
