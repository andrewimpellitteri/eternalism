#!/usr/bin/env python3
"""Exact regression for the b=1 capped-bipartite lower bound correction."""
from fractions import Fraction as F
from itertools import product
from math import comb


def family_sum(m, a):
    # Enumerate all m x m Boolean matrices.  Each row gives a lower vertex's
    # neighbours in the upper antichain.  z is the number of empty rows.
    total = F(0)
    configs = 0
    for rows in product(range(1 << m), repeat=m):
        e = sum(row.bit_count() for row in rows)
        z = sum(row == 0 for row in rows)
        covers = e + m + z  # E links, B->cap links, empty-row A->cap links
        total += a ** covers
        configs += 1
    closed = a**m * (a + (1 + a)**m - 1)**m
    assert total == closed
    assert configs == 1 << (m * m)
    return total


def restricted_family_sum(m, a):
    # Restrict every lower row to nonempty; then covers are exactly |E|+m.
    total = F(0)
    for rows in product(range(1, 1 << m), repeat=m):
        e = sum(row.bit_count() for row in rows)
        total += a ** (e + m)
    closed = a**m * ((1 + a)**m - 1)**m
    assert total == closed
    return total


# p=(50+120i)/169 has |p|=10/13 and |1-p|=1 exactly.
a = F(10, 13)
actual_at_n3 = family_sum(1, a)
assert actual_at_n3 == 2 * a**2 == F(200, 169)
claimed_at_n3 = a * (1 + a)
assert claimed_at_n3 == F(230, 169)
assert actual_at_n3 < claimed_at_n3

for m in range(1, 5):
    full = family_sum(m, a)
    restricted = restricted_family_sum(m, a)
    # The full family includes the restricted family and both sums are exact.
    assert full >= restricted
    # Every fixed E gives a distinct naturally labelled principal order.
    print(f"m={m}: full={full}, restricted={restricted}")

# The corrected bounds grow quadratically-exponentially.  For these m,
# (1+a)^m + a - 1 >= (1+a)^m/2; verify without floating point.
for m in range(1, 20):
    assert (1 + a)**m + a - 1 >= (1 + a)**m / 2
print(f"counterexample: W_3 >= {actual_at_n3}; claimed bound = {claimed_at_n3}")
print("corrected exact family formula and restricted-family formula pass m=1..4")
