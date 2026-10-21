"""Exact finite corroboration of U=1+RU, not an analytic convergence proof."""
from fractions import Fraction as F
from itertools import combinations
from check_boundaries import closure, stats, mul, power

ZERO = (F(0), F(0))
ONE = (F(1), F(0))


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def coefficients(p, limit=5):
    q = (1 - p[0], -p[1])
    B = [ONE, p]
    R = [ZERO, p]
    for k in range(2, limit + 1):
        n = k - 1
        pairs = list(combinations(range(n), 2))
        orders = {closure([e for j, e in enumerate(pairs) if mask >> j & 1], n)
                  for mask in range(1 << len(pairs))}
        bridge = first = ZERO
        for rel in orders:
            L, h = stats(rel, n)
            minima = sum(not any((j, i) in rel for j in range(i)) for i in range(n))
            maxima = sum(not any((i, j) in rel for j in range(i + 1, n)) for i in range(n))
            weight = mul(power(p, L + minima + maxima), power(q, h))
            bridge = add(bridge, weight)
            has_post = any(all(i == j or (min(i, j), max(i, j)) in rel
                               for j in range(n)) for i in range(n))
            if not has_post:
                first = add(first, weight)
        B.append(bridge)
        R.append(first)
    return B, R


def main():
    for p in ((F(0), F(0)), (F(1), F(0)), (F(1, 2), F(0)),
              (F(1, 2), F(1, 2)), (F(-1), F(0))):
        B, R = coefficients(p)
        for n in range(1, len(B)):
            convolution = ZERO
            for j in range(1, n + 1):
                convolution = add(convolution, mul(R[j], B[n-j]))
            assert B[n] == convolution, (p, n, B[n], convolution)
        if p == ZERO:
            assert all(v == ZERO for v in B[1:] + R[1:])
        print(f'p={p}: bridge/first-post renewal identity exact through degree 5')


if __name__ == '__main__':
    main()
