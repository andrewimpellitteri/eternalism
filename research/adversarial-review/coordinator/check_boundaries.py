"""Independent exact finite corroboration; the infinite proof is in VECTOR_COUNTERMODEL.md."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations


def closure(edges, n):
    rel = set(edges)
    for k in range(n):
        for i in range(k):
            for j in range(k + 1, n):
                if (i, k) in rel and (k, j) in rel:
                    rel.add((i, j))
    return frozenset(rel)


def principal(rel, n):
    return sum(not any((i, j) in rel for j in range(i + 1, n))
               for i in range(n)) == 1


def stats(rel, n):
    covers = sum(not any((i, k) in rel and (k, j) in rel for k in range(i + 1, j))
                 for i, j in rel)
    return covers, n * (n - 1) // 2 - len(rel)


def mul(z, w):
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def power(z, n):
    out = F(1), F(0)
    for _ in range(n):
        out = mul(out, z)
    return out


def main():
    total = 0
    for n in range(1, 6):
        pairs = list(combinations(range(n), 2))
        counts = Counter(closure([e for i, e in enumerate(pairs) if mask >> i & 1], n)
                         for mask in range(1 << len(pairs)))
        assert sum(counts.values()) == 1 << len(pairs)
        for rel, count in counts.items():
            L, h = stats(rel, n)
            amplitude = mul(power((F(1, 2), F(1, 2)), L),
                            power((F(1, 2), F(-1, 2)), h))
            squared_norm = sum(x * x for x in amplitude)
            probability = F(count, 1 << len(pairs))
            assert probability == F(1, 2) ** (L + h) == squared_norm
            total += 1
        # On this finite partition, disjoint indicators are orthogonal.
        # Unit-modulus coefficients give norm squared sum(probability) = 1.
        assert sum(F(count, 1 << len(pairs)) for count in counts.values()) == 1
        print(f'n={n}: {len(counts)} cylinder identities and partition normalization exact')
    # The singleton is principal, but not doubly principal: its deletion is empty.
    assert principal(frozenset(), 1)
    assert not principal(frozenset(), 0)
    kappas = {1: 17, **{n: 1 for n in range(2, 7)}}
    for n in range(1, 6):
        pairs = list(combinations(range(n), 2))
        orders = {closure([e for i, e in enumerate(pairs) if mask >> i & 1], n)
                  for mask in range(1 << len(pairs))}
        for rel in orders:
            L, h = stats(rel, n)
            value = int(len(rel) == len(pairs))  # Dirac at the infinite chain, p=1
            amplitude = int(h == 0)
            if principal(rel, n):
                capped = rel | frozenset((i, n) for i in range(n))
                capvalue = int(len(capped) == (n + 1) * n // 2)
                assert capvalue == value  # local renewal at p=1
            previous = frozenset((i, j) for i, j in rel if j < n - 1)
            if principal(rel, n) and principal(previous, n - 1):
                # At p=1 nonchains have zero amplitude irrespective of N(H).
                assert value == kappas[n] * amplitude
    assert kappas[1] != kappas[2]
    print(f'{total} exact cylinder identities; singleton kappa_1 counterassignment verified')


if __name__ == '__main__':
    main()
