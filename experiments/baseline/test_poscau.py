#!/usr/bin/env python3
"""Unit checks for the independent (doubly-)reduced-poscau reproduction."""
from fractions import Fraction
import math
import unittest

import poscau

P = 0.5 + 0.5j
FORMULA = abs(P) + abs(1 - P) - 1


class CausetCounts(unittest.TestCase):
    def test_naturally_labelled_counts(self):
        self.assertEqual([len(poscau.causets(n)) for n in range(1, 6)],
                         [1, 2, 7, 40, 357])

    def test_additivity(self):
        for n in range(1, 5):
            for rel in poscau.causets(n):
                parent = poscau.amplitude(rel, n, P)
                total = sum(poscau.amplitude(c, n + 1, P)
                            for c, _, _ in poscau.children(rel, n))
                self.assertAlmostEqual(abs(total - parent), 0.0, places=12)


class Variation(unittest.TestCase):
    def test_real_probability_has_zero_zeta(self):
        for doubly in (False, True):
            table = poscau.level_table(4, 0.5, doubly)
            for n in table:
                for row in table[n]["nodes"]:
                    if row["zeta"] is not None:
                        self.assertAlmostEqual(row["zeta"], 0.0, places=12)

    def test_level_two_formula(self):
        for doubly in (False, True):
            table = poscau.level_table(2, P, doubly)
            vals = [r["zeta"] for r in table[2]["nodes"]
                    if r["zeta"] is not None and (not doubly or r["valency"] > 1)]
            self.assertAlmostEqual(min(vals), FORMULA, places=12)

    def test_fig_6_7_at_symmetric_point(self):
        for n in (2, 3, 4):
            red = poscau.level_table(n, P, False)[n]
            dbl = poscau.level_table(n, P, True)[n]
            self.assertAlmostEqual(red["zeta_min"], FORMULA, places=12)
            self.assertAlmostEqual(dbl["zeta_bar_min"], FORMULA, places=12)

    def test_valency_one_nodes_on_doubly_reduced_tree(self):
        # The paper's improved criterion exists because doubly-reduced poscau
        # has valency-1 nodes with zeta = 0 at every level > 1.
        table = poscau.level_table(4, P, True)
        for n in (2, 3, 4):
            self.assertTrue(any(r["valency"] == 1 and r["zeta"] == 0.0
                                for r in table[n]["nodes"]))


class FiniteCertificate(unittest.TestCase):
    def test_v5_v6_exact(self):
        expected = {5: (Fraction(3, 4), Fraction(3, 16)),
                    6: (Fraction(31, 32), Fraction(55, 64))}
        for n in (5, 6):
            a = Fraction(0)
            b = Fraction(0)
            for rel in poscau.causets(n):
                if not poscau.is_principal(rel, n):
                    continue
                parent = frozenset((i, j) for (i, j) in rel
                                   if i < n - 1 and j < n - 1)
                if not poscau.is_principal(parent, n - 1):
                    continue
                L, R = poscau.stats(rel, n)
                k = L + n * (n - 1) // 2 - R
                if k % 2 == 0:
                    a += Fraction(1, 2 ** (k // 2))
                else:
                    b += Fraction(1, 2 ** ((k + 1) // 2))
            self.assertEqual((a, b), expected[n])


if __name__ == "__main__":
    unittest.main()
