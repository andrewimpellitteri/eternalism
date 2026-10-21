"""Exact finite tests of the proposed c0 construction; infinite proof is separate."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from check_boundaries import closure, principal, stats


def restrict(rel, n):
    return frozenset((i, j) for i, j in rel if j < n)


def is_dp(rel, n):
    return principal(rel, n) and principal(restrict(rel, n - 1), n - 1)


def run(a, b, N=5):
    pairs = list(combinations(range(N), 2))
    counts = Counter(closure([e for j, e in enumerate(pairs) if mask >> j & 1], N)
                     for mask in range(1 << len(pairs)))
    leaf_prob = {C: F(count, 1 << len(pairs)) for C, count in counts.items()}
    cylinders = [(0, frozenset())]
    for n in range(2, N + 1):
        cylinders += [(n, C) for C in {restrict(D, n) for D in counts} if is_dp(C, n)]
    weights = []
    events = []
    for n, C in cylinders:
        L, h = stats(C, n)
        weights.append(a ** L * b ** h)
        events.append({D for D in counts if restrict(D, n) == C})
    for j, (n, D) in enumerate(cylinders):
        coords = []
        for i, event_C in enumerate(events):
            pc = sum(leaf_prob[C] for C in event_C)
            joint = sum(leaf_prob[C] for C in event_C & events[j])
            value = weights[i] * joint / pc
            assert 0 <= value <= weights[j]
            coords.append(value)
        assert max(coords) == weights[j] == coords[j]
    # A partition into all N-stage atoms is additive in every coordinate.
    for i, event_C in enumerate(events):
        pc = sum(leaf_prob[C] for C in event_C)
        atoms = [weights[i] * leaf_prob[D] / pc if D in event_C else F(0)
                 for D in counts]
        assert sum(atoms) == weights[i]
        assert abs(sum(v if j % 2 else -v for j, v in enumerate(atoms))) <= weights[i]
    print(f'a={a}, b={b}: {len(cylinders)} exact prescribed norms; conditional probabilities and partition bounds pass')


def chain_then_fork(n):
    # chain_n + A2 + {u} + {v}, size n+4, one incomparable pair.
    size = n + 4
    missing = (n, n + 1)
    return frozenset(e for e in combinations(range(size), 2) if e != missing)


def first_edge(n):
    # First n births are an antichain, next birth has precisely one parent.
    return frozenset({(0, n)})


def main():
    run(F(3, 5), F(4, 5))  # p=(9+12i)/25
    run(F(10, 13), F(1))  # p=(50+120i)/169: b=1 boundary
    witnesses = [(n + 4, chain_then_fork(n)) for n in range(1, 9)]
    for n, C in witnesses:
        assert is_dp(C, n)
        L, h = stats(C, n)
        assert h == 1 and L == n
        assert F(1) ** L * F(10, 13) ** h == F(10, 13)
    for j, (n, C) in enumerate(witnesses):
        for m, D in witnesses[j+1:]:
            assert restrict(D, n) != C  # pairwise disjoint cylinders
    # On b=1, all-cylinder prescription fails even though DP prescription exists.
    for n in range(1, 9):
        C = first_edge(n)
        L, h = stats(C, n + 1)
        assert L == 1 and F(10, 13) ** L * F(1) ** h == F(10, 13)
        for m in range(n+1, 9):
            assert restrict(first_edge(m), n + 1) != C
    print('Boundary disjoint families: constant-norm DP forks at a=1; all-cylinder first edges at b=1')


if __name__ == '__main__':
    main()
