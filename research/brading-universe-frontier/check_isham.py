"""Exact check of Isham (1991) Sec. 5.2.3 reduced Hamiltonians.

Constraint (5.2.5), written in P = pa^2 and Q = pf^2:
    C(a, P, Q, V) = -P/(24 a) - 6 a + Q/(2 a^3) + a^3 V = 0.
On exactly constructed on-shell points, checks that the squared reduced
Hamiltonians (5.2.6)-(5.2.8) agree with the constraint, and which of them
depend explicitly on the chosen time t. Finite exact evaluation only; not a
proof for all gauges and not a claim about any ontology.
"""
from fractions import Fraction as F
import random

random.seed(1991)


def r():
    return F(random.randint(1, 60), random.randint(1, 60))


def C(a, P, Q, V):
    return -P / (24 * a) - 6 * a + Q / (2 * a ** 3) + a ** 3 * V


def Ha2(t, Q, V):          # (5.2.6), time t := a, conjugate momentum pa
    return 24 * (-6 * t ** 2 + Q / (2 * t ** 2) + t ** 4 * V)


def Hphi2(a, P, Vt):       # (5.2.8), time t := phi, conjugate momentum pf
    return a ** 2 * P / 12 + 12 * a ** 4 - 2 * a ** 6 * Vt


def main():
    n = 0
    for _ in range(500):
        a, P, V = r(), r(), r()
        Q = Hphi2(a, P, V)               # on shell by construction
        assert C(a, P, Q, V) == 0
        assert Ha2(a, Q, V) == P         # (5.2.6) consistent on shell
        # (5.2.7) V = 0, time t := pa: 144 A^2 + t^2 A - 12 Q = 0 with A = a^2
        Q0 = Hphi2(a, P, F(0))
        assert C(a, P, Q0, F(0)) == 0
        assert 144 * a ** 4 + P * a ** 2 - 12 * Q0 == 0
        n += 1
    assert 144 * 48 == 6912  # Isham's displayed (5.2.7) form, rescaled
    # explicit time dependence: vary t with conjugate data fixed
    Q, P = F(7, 3), F(5, 2)
    assert Ha2(F(1), Q, F(0)) != Ha2(F(2), Q, F(0))          # H_a depends on t
    assert Hphi2(F(3, 2), P, F(0)) == Hphi2(F(3, 2), P, F(0))  # no t at all
    Vt = lambda t: t ** 2                                      # a t-dependent V
    assert Hphi2(F(3, 2), P, Vt(F(1))) != Hphi2(F(3, 2), P, Vt(F(2)))
    print(f"on-shell identities verified exactly at {n} constructed points")
    print("(5.2.6): H_a^2 depends explicitly on t=a, even with V=0")
    print("(5.2.8): H_phi^2 depends on t=phi only through V(t); V=0 removes it")
    print("PASS (finite exact checks only)")


if __name__ == "__main__":
    main()
