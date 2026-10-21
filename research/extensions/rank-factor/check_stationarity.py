#!/usr/bin/env python3
"""Check S(H,m) = N(H)A(H) R_{m-n} on finite data.

Sections A-C use EXACT arithmetic (Fraction at p=1/2; Gaussian rationals at
p=(1+i)/2) and assert equality with zero tolerance. Section D is a numerical
diagnostic only.

Extended 2026-10-21 following research/adversarial-review/coordinator/
BOUNDARIES.md:
- B: at p=0 every R_k = 0 (R_1 = p = 0; for k>=2 each post-free T is nonempty
  with M(T), min(T) >= 1, so each term carries a positive power of p). Hence
  R(1) = 0 at p=0: the assertion "R(1)=1" holds for 0 < p <= 1, not p=0.
- C: the sum defining R_k (k>=2) runs over NATURALLY LABELLED post-free orders
  T of size k-1, each labelling counted once (poscau.causets); equivalently
  over unlabelled post-free shapes tau with multiplicity N(tau). Section C
  checks the two forms agree exactly.
- A: the identity S(H,m) = N(H)A(H)R_{m-n} is exactly the finite kernel
  identity; it is not evidence for countable additivity, normalization, or any
  infinite-rank existence or no-go claim.
"""
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import probe
import kernel_sequence7 as ks


class G:
    """Gaussian rational a+bi; supports what poscau.amplitude needs."""

    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re = Fraction(re)
        self.im = Fraction(im)

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


def _g(x):
    return x if isinstance(x, G) else G(x)


def section_a():
    print("A. exact kernel identity S(H,m) = N(H)A(H) R_{m-n}")
    for name, p in (("p=1/2", Fraction(1, 2)), ("p=(1+i)/2", G(1, 2))):
        data = probe.kernel(6, p)
        R = ks.R(7, p)
        checks = 0
        for cH, d in data.items():
            target = d["N"] * d["A"]
            if target == 0:
                continue
            for m, s in d["sums"].items():
                expected = R[m - d["n"]][0]
                assert s == expected * target, (name, d["n"], m)
                checks += 1
        print(f"  {name}: {checks} exact identities (zero tolerance): PASS")


def section_b():
    print("B. edge cases for R_k")
    for name, p in (("p=1/2", Fraction(1, 2)), ("p=(1+i)/2", G(1, 2))):
        R = ks.R(7, p)
        assert R[1][0] == p
    print("  R_1 = p exactly at p=1/2 and p=(1+i)/2: PASS")
    R0 = ks.R(7, 0)
    assert R0[1][0] == 0
    for k in range(2, 8):
        assert R0[k][0] == 0, k
    print("  at p=0: R_k = 0 for all k=1..7 (exact), so R(1)=0 there: "
          "the identity R(1)=1 excludes p=0")


def section_c():
    print("C. labelled T-sum equals shape-multiplicity sum (exact, p=1/2)")
    p = Fraction(1, 2)
    R = ks.R(7, p)
    for k in range(2, 8):
        size = k - 1
        shapes = {}
        for T in poscau_causets(size):
            if posts_nonempty(T, size):
                continue
            shapes.setdefault(probe.canon(T, size), T)
        total = 0
        for cform, T in shapes.items():
            ntau = probe.n_labelings(cform, size)
            m = len(ks_maxima(T, size))
            mn = len(ks_minima(T, size))
            total += ntau * poscau_amplitude(T, size, p) * (p ** m) * (p ** mn)
        assert total == R[k][0], (k, total, R[k][0])
    print("  R_2..R_7: labelled sum == sum over shapes with N(tau) "
          "multiplicity (exact): PASS")


def poscau_causets(n):
    import poscau
    return poscau.causets(n)


def poscau_amplitude(rel, n, p):
    import poscau
    return poscau.amplitude(rel, n, p)


def ks_maxima(rel, n):
    return ks.maxima(rel, n)


def ks_minima(rel, n):
    return ks.minima(rel, n)


def posts_nonempty(rel, n):
    return bool(ks.posts(rel, n))


def section_d():
    print("D. numerical diagnostic only (NOT an exact check, NOT evidence "
          "for existence or no-go)")
    p = 0.2 + 0.7j
    data = probe.kernel(6, p)
    R = ks.R(7, p)
    worst = 0.0
    checks = 0
    for cH, d in data.items():
        target = d["N"] * d["A"]
        if abs(target) < 1e-12:
            continue
        for m, s in d["sums"].items():
            err = abs(s / target - R[m - d["n"]][0])
            worst = max(worst, err)
            checks += 1
            if err > 1e-9:
                print(f"  mismatch n={d['n']} m={m} ratio={s / target} "
                      f"R={R[m - d['n']][0]}")
    print(f"  p=0.2+0.7j: checks={checks} max float error={worst:.3e}")


if __name__ == "__main__":
    section_a()
    section_b()
    section_c()
    section_d()
    print("EXACT SECTIONS PASSED; section D is a numerical diagnostic only")
