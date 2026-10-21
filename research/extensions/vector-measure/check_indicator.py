#!/usr/bin/env python3
"""Exact finite checks for the reviewed L^2(P_r) indicator counterexample.

Added 2026-10-21 following research/adversarial-review/coordinator/
VECTOR_COUNTERMODEL.md. The analytic statements (countable additivity,
semivariation one, infinite total variation for nonreal p on the circle
|p|^2+|1-p|^2 = 1) are proved there; this script only corroborates their
finite, exactly-checkable consequences at p = (1+i)/2 (so r = |p|^2 = 1/2):

1. Norm prescription: for every naturally labelled causet C at sizes 1..5,
   |A_p(C)|^2 = r^{L(C)} (1-r)^{binom(n,2)-R(C)} = 2^{-(L+e)} exactly, which is
   P_r(cyl C): the L^2 norm of the cylinder indicator equals the prescribed
   amplitude modulus.
2. Finite additivity of the Re/Im assignment mu(C) = (Re A_p(C), Im A_p(C))
   through level 5: sum of child amplitudes equals the parent amplitude exactly.
   This shows finite norm-matching assignments exist trivially; finite
   existence is not evidence for, or a step toward, an infinite extension.
3. Finite partition normalization: the level-n cylinder probabilities sum to
   one exactly, and the simple-function norm identity
   ||sum_j a_j 1_{E_j}||^2 = sum_j |a_j|^2 P(E_j) <= 1 holds exactly on that
   family, with equality attained at |a_j| = 1. Finite corroboration only: this
   is not the semivariation-one statement at infinity.
4. Level norm sums grow (numerically, from exact dyadic squares); divergence is
   the analytic two-cap bound, not a finite check.

Exact arithmetic: Gaussian rationals (a+bi with Fraction parts). No installs.
"""
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "experiments" / "baseline"))
import poscau  # noqa: E402


class G:
    """Gaussian rational a+bi; supports what poscau.amplitude needs."""

    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re = F(re)
        self.im = F(im)

    def __add__(self, o):
        o = _g(o)
        return G(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __sub__(self, o):
        o = _g(o)
        return G(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        o = _g(o)
        return G(o.re - self.re, o.im - self.im)

    def __mul__(self, o):
        o = _g(o)
        return G(self.re * o.re - self.im * o.im,
                 self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def __pow__(self, k):
        r = G(1)
        for _ in range(k):
            r = r * self
        return r

    def __eq__(self, o):
        o = _g(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def __repr__(self):
        return f"({self.re}+{self.im}i)"

    def norm2(self):
        return self.re * self.re + self.im * self.im


def _g(x):
    return x if isinstance(x, G) else G(x)


def main():
    p = G(F(1, 2), F(1, 2))          # p = (1+i)/2, r = |p|^2 = 1/2
    r = F(1, 2)
    q = 1 - p

    # 1. Norm prescription on every cylinder, exact.
    checks = 0
    counts = {}
    for n in range(1, 6):
        level = poscau.causets(n)
        counts[n] = len(level)
        for rel in level:
            L, R = poscau.stats(rel, n)
            e = n * (n - 1) // 2 - R
            a = poscau.amplitude(rel, n, p)
            assert a == p ** L * q ** e
            assert a.norm2() == r ** L * r ** e == F(1, 2) ** (L + e), (n, rel)
            checks += 1
    print(f"norm prescription ||mu(cyl C)||^2 = P_r(cyl C) = 2^-(L+e): "
          f"{checks} exact identities, sizes 1-5")

    # 2. Re/Im finite additivity through level 5 (exact).
    add_checks = 0
    frontier = [(frozenset(), 1)]
    while frontier:
        rel, n = frontier.pop()
        a = poscau.amplitude(rel, n, p)
        total = G(0)
        for child, _, _ in poscau.children(rel, n):
            total = total + poscau.amplitude(child, n + 1, p)
            if n + 1 < 5:
                frontier.append((child, n + 1))
        assert total == a, (n, rel)
        add_checks += 1
    print(f"Re/Im assignment finite additivity: {add_checks} exact node "
          f"identities through level 5")

    # 3. Finite partition normalization and the simple-function norm bound.
    for n in (3, 4, 5):
        probs = []
        for rel in poscau.causets(n):
            L, R = poscau.stats(rel, n)
            e = n * (n - 1) // 2 - R
            probs.append(F(1, 2) ** (L + e))
        assert sum(probs) == 1
        # alpha_j = +-1: indicators of disjoint sets are orthogonal, so
        # ||sum_j a_j 1_{E_j}||^2 = sum_j |a_j|^2 P_j = sum P_j = 1 (attained).
        # alpha_j = 1/2: norm^2 = (1/4) sum P_j = 1/4 <= 1.
        assert sum(F(1, 4) * pk for pk in probs) == F(1, 4)
    print("partition normalization sum P_j = 1 and simple-function norm "
          "bound <= 1: exact at levels 3,4,5")

    # 4. Level norm sums (numerical values of exact dyadic square roots).
    sums = {}
    for n in range(1, 6):
        total = 0.0
        for rel in poscau.causets(n):
            L, R = poscau.stats(rel, n)
            e = n * (n - 1) // 2 - R
            total += float(F(1, 2) ** ((L + e) / 2))
        sums[n] = total
    for n in range(2, 6):
        assert sums[n] > sums[n - 1]
    print("level norm sums (numerical): "
          + ", ".join(f"S_{n}={sums[n]:.6g} ({counts[n]} nodes)"
                      for n in range(1, 6)))
    print("growth corroborated numerically; divergence is the analytic "
          "two-cap bound (VECTOR_COUNTERMODEL.md), not a finite check")

    print("ALL CHECKS PASSED (exact where stated; finite corroboration only)")


if __name__ == "__main__":
    main()
