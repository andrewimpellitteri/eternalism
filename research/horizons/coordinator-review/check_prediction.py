"""Bounded controls for REVIEW.md; the general arguments are analytical."""
from fractions import Fraction as F
from itertools import product
import json


def fields(t, xyz):
    a = 2 + xyz[0] ** 2 - xyz[1] + 3 * xyz[2]
    b = 1 + xyz[0] - 2 * xyz[1] ** 2 + xyz[2]
    return a + t * b, b


def in_strict_past(t, xyz):
    return t < 0 and t * t > sum(v * v for v in xyz)


def box(relation, valuation, w):
    return all(v in valuation for v in relation[w])


def diamond(relation, valuation, w):
    return any(v in valuation for v in relation[w])


def dot_two_valid(relation):
    worlds = tuple(relation)
    for bits in product((False, True), repeat=len(worlds)):
        valuation = {w for w, bit in zip(worlds, bits) if bit}
        boxed = {w for w in worlds if box(relation, valuation, w)}
        diamonded = {w for w in worlds if diamond(relation, valuation, w)}
        for w in worlds:
            if diamond(relation, boxed, w) and not box(relation, diamonded, w):
                return False
    return True


def run():
    checked = 0
    for t, x, y, z in product(map(F, (-3, -1, 0, 1, 4)), repeat=4):
        xyz = (x, y, z)
        s = -1 - abs(t) - sum(map(abs, xyz))
        assert s < t and in_strict_past(s, xyz)
        qs, ps = fields(s, xyz)
        qt, pt = fields(t, xyz)
        assert (qs + (t - s) * ps, ps) == (qt, pt)
        checked += 1
    # Positive control: a timelike future target is fixed by past data.
    assert fields(F(1), (F(0),) * 3) == (F(3), F(1))
    assert not in_strict_past(F(1), (F(0),) * 3)
    # Negative geometric control: this entire null ray avoids the strict past.
    # Analytically t+r=1 for all lambda>=0; samples detect sign mistakes.
    for lam in map(F, (0, 1, 2, 10, 1000)):
        assert not in_strict_past(1 - lam, (lam, F(0), F(0)))
    # .2 is locally valid on disjoint singletons despite no global direction.
    disjoint = {0: {0}, 1: {1}}
    assert dot_two_valid(disjoint)
    assert not (disjoint[0] & disjoint[1])
    # Negative control: a root with two terminal incomparable successors fails .2.
    fork = {0: {0, 1, 2}, 1: {1}, 2: {2}}
    assert not dot_two_valid(fork)
    return {
        "status": "pass",
        "exact_field_recovery_cases": checked,
        "field_law": "dQ/dt=P; dP/dt=0 on fixed Minkowski background",
        "controls": ["future target", "null escape ray", "disjoint .2-valid frame", "fork .2-invalid frame"],
        "scope": "bounded exact controls; analytical universal arguments in REVIEW.md",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
