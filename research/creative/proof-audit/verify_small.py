#!/usr/bin/env python3
"""Exact small-instance checks for CTP cylinder sums; standard library only.

Finite enumeration corroborates the identities but does not prove the all-k
bound.  The symmetric complex point is represented in Q(sqrt(2)).
"""

from fractions import Fraction
from itertools import combinations
from math import sqrt


def closures(n):
    """Return all distinct transitive closures of forward-edge masks."""
    pairs = list(combinations(range(n), 2))
    out = set()
    for mask in range(1 << len(pairs)):
        rel = [[False] * n for _ in range(n)]
        for bit, (i, j) in enumerate(pairs):
            if mask & (1 << bit):
                rel[i][j] = True
        for mid in range(n):
            for i in range(n):
                if rel[i][mid]:
                    for j in range(n):
                        rel[i][j] |= rel[mid][j]
        out.add(tuple(tuple(row) for row in rel))
    return out


def order_counts(rel):
    n = len(rel)
    relations = sum(rel[i][j] for i in range(n) for j in range(n))
    links = sum(
        rel[i][j] and not any(rel[i][m] and rel[m][j]
                              for m in range(i + 1, j))
        for i in range(n) for j in range(i + 1, n)
    )
    maxima = sum(not any(rel[i][j] for j in range(n)) for i in range(n))
    minima = sum(not any(rel[j][i] for j in range(n)) for i in range(n))
    return links, relations, maxima, minima


def edge_order_probabilities(n, r, s):
    """Aggregate exact Bernoulli-edge probabilities by resulting order."""
    pairs = list(combinations(range(n), 2))
    out = {}
    for mask in range(1 << len(pairs)):
        rel = [[False] * n for _ in range(n)]
        edge_count = 0
        for bit, (i, j) in enumerate(pairs):
            if mask & (1 << bit):
                rel[i][j] = True
                edge_count += 1
        for mid in range(n):
            for i in range(n):
                if rel[i][mid]:
                    for j in range(n):
                        rel[i][j] |= rel[mid][j]
        key = tuple(tuple(row) for row in rel)
        out[key] = out.get(key, Fraction(0)) + (
            r ** edge_count * s ** (len(pairs) - edge_count)
        )
    assert sum(out.values(), Fraction(0)) == 1
    return out


def level_sum(k, r, s):
    """Compute Z_k(r,s) over all labeled k-orders exactly."""
    total = Fraction(0)
    orders = closures(k)
    for key in orders:
        rel = [list(row) for row in key]
        links, relations, maxima, _minima = order_counts(rel)
        gap = k * (k - 1) // 2 - relations
        total += r ** (links + maxima) * s ** gap
    return total, len(orders)


def check_all_order_identity(k, r, s):
    z, order_count = level_sum(k, r, s)
    event = Fraction(0)
    for key, probability in edge_order_probabilities(k + 1, r, s).items():
        if all(key[i][k] for i in range(k)):
            event += probability
    exposure = Fraction(1)
    for j in range(1, k + 1):
        exposure *= 1 - s ** j
    assert z == event == exposure, (k, z, event, exposure)

    # Each k-order has exactly one two-cap extension and each such extension
    # is doubly principal; check cardinality and defining endpoint predicates.
    capped = 0
    for key in closures(k):
        rel = [list(row) for row in key]
        links, relations, maxima, _ = order_counts(rel)
        n = k + 2
        full = [[False] * n for _ in range(n)]
        for i in range(k):
            for j in range(k):
                full[i][j] = rel[i][j]
            full[i][k] = True
            full[i][k + 1] = True
        full[k][k + 1] = True
        assert all(full[i][n - 1] for i in range(n - 1))
        assert all(full[i][n - 2] for i in range(n - 2))
        full_links, full_relations, _full_maxima, _full_minima = order_counts(full)
        assert full_links == links + maxima + 1
        assert full_relations == relations + 2 * k + 1
        assert n * (n - 1) // 2 - full_relations == (
            k * (k - 1) // 2 - relations
        )
        capped += 1
    assert capped == order_count
    return z, exposure, order_count


def qsqrt2_power(exponent):
    """Return (x,y) for 2^(exponent/2) = x + y*sqrt(2), exact in Q(sqrt2)."""
    if exponent % 2 == 0:
        power = exponent // 2
        return (Fraction(2**power) if power >= 0 else Fraction(1, 2**(-power)),
                Fraction(0))
    power = (exponent - 1) // 2
    return (Fraction(0), Fraction(2**power) if power >= 0
            else Fraction(1, 2**(-power)))


def symmetric_point_level(k):
    """Exact sum of |A| at p=(1+i)/2, where a=b=1/sqrt(2)."""
    total = (Fraction(0), Fraction(0))
    for key in closures(k):
        rel = [list(row) for row in key]
        links, relations, maxima, _ = order_counts(rel)
        gap = k * (k - 1) // 2 - relations
        exponent = links + maxima + gap + 1  # leading cap factor a included
        term = qsqrt2_power(-exponent)
        total = (total[0] + term[0], total[1] + term[1])
    return total


def check_principal_harris_route(r, s):
    """Check the earlier principal-only E∩F identity for small n."""
    for n in range(2, 6):
        k = n - 1
        event = Fraction(0)
        for key, probability in edge_order_probabilities(n, r, s).items():
            if all(key[0][j] for j in range(1, n)) and all(
                key[i][n - 1] for i in range(n - 1)
            ):
                event += probability
        seam_sum = Fraction(0)
        for key in closures(k):
            rel = [list(row) for row in key]
            if all(rel[i][k - 1] for i in range(k - 1)):
                links, relations, _maxima, minima = order_counts(rel)
                gap = k * (k - 1) // 2 - relations
                seam_sum += r ** (links + minima) * s ** gap
        assert event == seam_sum
        product = Fraction(1)
        for j in range(1, n):
            product *= 1 - s ** j
        assert product ** 2 <= event <= product


def check_post_cutoff(p, q):
    """Check finite post-future cylinder sums by enumerating precursor sets."""
    for n in range(1, 4):
        for future_count in range(4):
            accumulated = Fraction(1)
            formula = Fraction(1)
            for j in range(1, future_count + 1):
                existing = n + j - 1
                step_sum = Fraction(0)
                # The first j elements are the post and its already-required
                # future; a new birth is above the post iff its precursor set
                # intersects these j elements. Other precursor choices sum out.
                for mask in range(1 << existing):
                    if mask & ((1 << j) - 1):
                        size = mask.bit_count()
                        step_sum += p ** size * q ** (existing - size)
                assert step_sum == 1 - q ** j, (n, j, step_sum)
                accumulated *= step_sum
                formula *= 1 - q ** j
            assert accumulated == formula


def main():
    for r, s, label in [
        (Fraction(2, 5), Fraction(3, 5), "r=2/5,s=3/5"),
        (Fraction(1, 2), Fraction(1, 2), "symmetric normalized r=s=1/2"),
    ]:
        for k in range(5):
            z, exposure, count = check_all_order_identity(k, r, s)
            print(f"{label}; k={k}; orders={count}; Z=F_k={z}")

    for k in range(5):
        rational, radical = symmetric_point_level(k)
        value = float(rational) + float(radical) * sqrt(2)
        print(f"p=(1+i)/2; k={k}; exact level sum={rational}+({radical})sqrt(2); ~{value:.12f}")

    check_principal_harris_route(Fraction(2, 5), Fraction(3, 5))
    print("principal-only Harris route also passed for n=2..5")
    check_post_cutoff(Fraction(2, 5), Fraction(3, 5))
    print("finite post-future precursor sums passed through 3 future births")


if __name__ == "__main__":
    main()
