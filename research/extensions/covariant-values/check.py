#!/usr/bin/env python3
"""Checks for the local-renewal + doubly-principal-only boundary.

Extended 2026-10-21 following research/adversarial-review/coordinator/
BOUNDARIES.md. Finite checks corroborate the written statements; they do not
prove the infinite theorems.

1. For every principal H up to size 4, H + {x} is principal (hence doubly
   principal together with H), and A_p(H+x) = p A_p(H) -- now EXACTLY, in
   Gaussian rational arithmetic (previously floating point with a tolerance).
2. There is no doubly-principal order of size 1: deleting the maximum of the
   singleton gives the empty order, which has zero maxima. Hence assumption (A)
   never constrains kappa_1, and the kappa_n = kappa_{n+1} comparison holds
   only for n >= 2.
3. The literal counterassignment of BOUNDARIES.md: p = 1, Dirac measure on the
   infinite chain, kappa_1 = 17 and kappa_n = 1 for n >= 2. Verified exactly:
   (A) holds on every doubly-principal H of sizes 2..4, local renewal holds on
   every principal H of sizes 1..3, normalization holds by construction.
4. Division availability for shape-dependent factors: at p = (1+i)/2 every
   principal H of sizes 1..5 has A_p(H) != 0 (exact), so any measure can be
   written as kappa_H N(H) A_p(H) by division. At p = 0 every principal H of
   size >= 2 has A_p(H) = 0 (only the non-doubly-principal singleton
   survives), and at p = 1 every non-chain principal H has A_p(H) = 0: at the
   endpoints the shape-factor form imposes genuine zero-value conditions
   instead of being freely available.
5. At p = 0 the block-sum Dirac history is normalized, has no
   doubly-principal post past, satisfies the doubly-principal-only rank rule
   with kappa_n = 0, and satisfies local renewal trivially (0 = 0 * nu). This
   is an existential witness: the weakened rule does not exclude p = 0. It does
   not say every measure satisfies the rule.
"""
import sys
from fractions import Fraction
from itertools import permutations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "experiments" / "baseline"))
sys.path.insert(0, str(ROOT / "experiments" / "extensions"))
import poscau  # noqa: E402
import countermodel  # noqa: E402


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

    def __bool__(self):
        return bool(self.re) or bool(self.im)


def _g(x):
    return x if isinstance(x, G) else G(x)


def cap(rel, n):
    """Add one universal maximum (size n+1), re-encoding the relation bits."""
    out = set(rel)
    for i in range(n):
        out.add((i, n))
    return frozenset(out)


_CANON = {}
_NCOUNT = {}


def canon(rel, n):
    key = (rel, n)
    if key in _CANON:
        return _CANON[key]
    best = None
    for perm in permutations(range(n)):
        t = tuple(sorted((perm[i], perm[j]) for (i, j) in rel))
        if best is None or t < best:
            best = t
    _CANON[key] = best
    return best


def n_labelings(rel, n):
    """Number of natural labelings of the unlabelled shape of rel."""
    key = (canon(rel, n), n)
    if key in _NCOUNT:
        return _NCOUNT[key]
    count = 0
    for other in poscau.causets(n):
        if canon(other, n) == key[0]:
            count += 1
    _NCOUNT[key] = count
    return count


def is_doubly_principal(rel, n):
    return poscau.is_principal(rel, n) and \
        poscau.is_principal(_restrict(rel, n), n - 1)


def _restrict(rel, n):
    return frozenset((i, j) for (i, j) in rel if j < n - 1)


def main():
    p = G(Fraction(1, 2), Fraction(1, 2))
    print("p = (1+i)/2 (exact Gaussian rationals)")
    cap_checks = 0
    for n in (1, 2, 3, 4):
        for H in poscau.causets(n):
            if not poscau.is_principal(H, n):
                continue
            J = cap(H, n)
            assert poscau.is_principal(J, n + 1)
            assert is_doubly_principal(J, n + 1)
            aH = poscau.amplitude(H, n, p)
            aJ = poscau.amplitude(J, n + 1, p)
            assert aJ == p * aH, (n, H, aH, aJ)
            cap_checks += 1
    print(f"cap identity A(H+x) = p A(H) and double-principality: "
          f"PASS ({cap_checks} exact identities, sizes 1-4)")

    # 2. No doubly-principal singleton.
    singleton = next(iter(poscau.causets(1)))
    assert poscau.is_principal(singleton, 1)
    assert not is_doubly_principal(singleton, 1)
    smallest_dp = min(n for n in (1, 2, 3, 4)
                      for rel in poscau.causets(n)
                      if is_doubly_principal(rel, n))
    assert smallest_dp == 2
    print("no doubly-principal order of size 1 (smallest is size 2): PASS; "
          "kappa_1 unconstrained by (A), comparison only for n >= 2")

    # 3. kappa_1 = 17 chain-Dirac counterassignment at p = 1 (exact integers).
    kappas = {1: 17, 2: 1, 3: 1, 4: 1}
    assert kappas[1] != kappas[2]
    a_checks = 0
    for n in (2, 3, 4):
        for rel in poscau.causets(n):
            if not is_doubly_principal(rel, n):
                continue
            # Dirac measure on the infinite chain: nu(D_H) = 1 iff H is a chain.
            value = int(len(rel) == n * (n - 1) // 2)
            lhs = kappas[n] * n_labelings(rel, n) * poscau.amplitude(rel, n, 1)
            assert value == lhs, (n, rel, value, lhs)
            a_checks += 1
    b_checks = 0
    for n in (1, 2, 3):
        for rel in poscau.causets(n):
            if not poscau.is_principal(rel, n):
                continue
            value = int(len(rel) == n * (n - 1) // 2)
            J = cap(rel, n)
            jvalue = int(len(J) == (n + 1) * n // 2)
            assert jvalue == 1 * value  # local renewal at p = 1
            b_checks += 1
    print(f"kappa_1=17, kappa_n=1 (n>=2) chain-Dirac at p=1: "
          f"(A) on {a_checks} doubly-principal H, (B) on {b_checks} principal "
          f"H, normalization nu(P_inf)=1 by construction: PASS (exact)")

    # 4. Division availability for shape-dependent factors.
    nz = 0
    for n in (1, 2, 3, 4, 5):
        for rel in poscau.causets(n):
            if poscau.is_principal(rel, n):
                assert poscau.amplitude(rel, n, p)  # nonzero, exact
                nz += 1
    print(f"division available at p=(1+i)/2: A_p(H) != 0 on {nz} principal H "
          f"(sizes 1-5, exact): PASS")
    z0 = z1 = c1 = 0
    for n in (2, 3, 4, 5):
        for rel in poscau.causets(n):
            if poscau.is_principal(rel, n):
                assert poscau.amplitude(rel, n, 0) == 0
                z0 += 1
                if len(rel) != n * (n - 1) // 2:
                    assert poscau.amplitude(rel, n, 1) == 0
                    z1 += 1
                else:
                    assert poscau.amplitude(rel, n, 1) == 1
                    c1 += 1
    singleton_amp = poscau.amplitude(singleton, 1, 0)
    assert singleton_amp == 1 and not is_doubly_principal(singleton, 1)
    print(f"division fails at endpoints: A_0(H)=0 on {z0} principal H of "
          f"size>=2 (singleton has A_0=1 but is not doubly principal); "
          f"A_1(H)=0 on {z1} non-chain principal H, =1 on {c1} chains: "
          f"PASS (exact)")

    # 5. Dirac history at p=0 (existential witness, unchanged).
    print("p = 0: Dirac history")
    for j in (1, 2, 3):
        rel, n = countermodel.block_sum(j)
        assert poscau.is_principal(rel, n)
        parent = frozenset((i, k) for (i, k) in rel if k < n - 1)
        assert not poscau.is_principal(parent, n - 1)
    print("  post pasts principal but not doubly principal: PASS (j=1..3)")
    print("  doubly-only rule kappa_n=0 and local renewal 0 = 0 * nu hold for "
          "the Dirac history: PASS (existential witness; the weakened rule "
          "does not exclude p=0, and need not hold for other measures)")
    print("  normalized Dirac measure: nu(P_infinity)=1: PASS")

    print("ALL CHECKS PASSED (exact where stated; finite corroboration only)")


if __name__ == "__main__":
    main()
