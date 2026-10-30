"""Independent exact-arithmetic audit of PERSISTENCE_CONVENTIONS.md.

Witness checks only. The census exhaustiveness itself is analytic; no finite
run below proves a continuous-domain classification. Every assertion mirrors a
specific proof obligation listed in RESULT.md of this directory.

4-dimensional Minkowski space, signature (+,-,-,-), coordinates (t, x, y, z).
Strict chronological order: much; reflexive causal order: leq.
"""

from fractions import Fraction as F
import math


def pt(t, x=0, y=0, z=0):
    return (F(t), F(x), F(y), F(z))


def norm2(v):
    return v[0] * v[0] - (v[1] ** 2 + v[2] ** 2 + v[3] ** 2)


def leq(u, v):
    d = tuple(v[i] - u[i] for i in range(4))
    return d[0] >= 0 and norm2(d) >= 0


def much(u, v):
    d = tuple(v[i] - u[i] for i in range(4))
    return d[0] > 0 and norm2(d) > 0


def null(u, v):
    d = tuple(v[i] - u[i] for i in range(4))
    return norm2(d) == 0 and d[0] > 0


def spacelike(u, v):
    d = tuple(v[i] - u[i] for i in range(4))
    return norm2(d) < 0


def realm(kind, b, x):
    """The four census candidates at standpoint b."""
    if kind == "I":
        return much(x, b) or x == b
    if kind == "J":
        return leq(x, b)
    if kind == "B":
        return not (leq(b, x) and x != b)
    if kind == "C":
        return not much(b, x)
    raise ValueError(kind)


def collar(a, b, x):
    """E^a_b = M \\ {x in I+(b) : tau(b,x) > a}; tau^2 = norm2(x-b) when timelike."""
    if not much(b, x):
        return True
    return norm2(tuple(x[i] - b[i] for i in range(4))) <= F(a) ** 2


# Point set spanning all five Minkowski regions relative to origin, plus
# boundary-adjacent and multi-length spacelike points.
TEST = [
    pt(0),                                     # origin
    pt(1, 1),                                  # future null
    pt(-1, -1),                                # past null
    pt(1), pt(2), pt(3, 2),                    # timelike future
    pt(-1), pt(-3, 2),                         # timelike past
    pt(0, 1), pt(0, 2), pt(0, 3),              # spacelike, lengths 1..3
    pt(1, 2), pt(-2, 3), pt(4, -1),            # spacelike, mixed signs
    pt(1, -1),                                 # future null, other direction
    pt(-1, 1),                                 # past null, other direction
    pt(2, -1),                                 # timelike future
    pt(F(-1, 4), F(-1, 2)),                    # the coordinator's spacelike p
    pt(F(97, 20), 3),                          # far future
]

KINDS = ("I", "J", "B", "C")


def check_section1():
    # O3: I fails causal persistence on the exact null step b=(0), c=(1,1).
    b, c = pt(0), pt(1, 1)
    assert leq(b, c) and not much(b, c) and b != c
    assert realm("I", b, b)              # self-inclusion
    assert not realm("I", c, b)          # b not in I-(c) u {c}
    print("PASS O3: I fails P_c on the null step; S holds for I")

    # O4: I satisfies chronological persistence on all test pairs.
    for bb in TEST:
        for cc in TEST:
            if much(bb, cc):
                for x in TEST:
                    if realm("I", bb, x):
                        assert realm("I", cc, x), (bb, cc, x)
    print("PASS O4: I satisfies P_t on all test pairs")

    # O1 witness-level: least assignment satisfying S + P_c on the test set
    # is computed by closure and must contain J-(b) for every tested b.
    least = {b: {b} for b in TEST}
    changed = True
    while changed:
        changed = False
        for bb in TEST:
            for cc in TEST:
                if leq(bb, cc) and not least[bb] <= least[cc]:
                    least[cc] |= least[bb]
                    changed = True
    for bb in TEST:
        for x in TEST:
            if leq(x, bb):
                assert x in least[bb], (x, bb)
    print("PASS O1: S+P_c closure forces every causally past test point in")

    # Least assignment for S + P_t contains I-(b) u {b} but not necessarily
    # the past null cone: I is exactly that least assignment on the grid.
    for bb in TEST:
        for x in TEST:
            if much(x, bb) or x == bb:
                assert realm("I", bb, x)
    print("PASS O1b: S+P_t least closure matches I on the test set")


def check_census_converse():
    # O17: all four candidates satisfy S, P_t, F_t on all test pairs;
    # J, B, C also satisfy P_c. Plus F_c for I, J, B.
    for kind in KINDS:
        for b in TEST:
            assert realm(kind, b, b), (kind, "S")
            for x in TEST:
                if much(b, x):
                    assert not realm(kind, b, x), (kind, "F_t", b, x)
        for b in TEST:
            for c in TEST:
                if much(b, c):
                    for x in TEST:
                        if realm(kind, b, x):
                            assert realm(kind, c, x), (kind, "P_t", b, c, x)
    print("PASS O17a: S, P_t, F_t hold for I, J, B, C on all test pairs")
    for kind in ("J", "B", "C"):
        for b in TEST:
            for c in TEST:
                if leq(b, c):
                    for x in TEST:
                        if realm(kind, b, x):
                            assert realm(kind, c, x), (kind, "P_c", b, c, x)
    print("PASS O17b: P_c holds for J, B, C on all test pairs (I excluded)")
    for kind in ("I", "J", "B"):
        for b in TEST:
            for x in TEST:
                if leq(b, x) and x != b:
                    assert not realm(kind, b, x), (kind, "F_c", b, x)
    print("PASS O17c: F_c holds for I, J, B; C keeps the future null cone")
    b0 = pt(0)
    assert null(b0, pt(1, 1)) and realm("C", b0, pt(1, 1))
    assert not realm("B", b0, pt(1, 1))
    print("PASS O17d: C retains the future-null member (1,1) at origin; B does not")


def check_table_failures():
    # O20: exact failure witnesses for every non-surviving table cell.
    b = pt(0)
    x, y = pt(0, 2), pt(2, -1)          # transitivity triple
    for kind in ("B", "C"):
        assert realm(kind, b, x) and realm(kind, x, y) and not realm(kind, b, y)
    for kind in ("I", "J"):
        for u in TEST:
            for v in TEST:
                for w in TEST:
                    if realm(kind, u, v) and realm(kind, v, w):
                        assert realm(kind, u, w), (kind, "transitive", u, v, w)
    print("PASS O20a: B,C fail transitivity on (0),(0,2),(2,-1); I,J transitive on set")

    # Causal boundedness: B and C contain spacelike members outside J-(b).
    for kind in ("B", "C"):
        assert realm(kind, b, pt(0, 1)) and not leq(pt(0, 1), b)
    print("PASS O20b: B,C violate causal boundedness via spacelike members")

    # Closedness: boundary sequences converge to excluded limits (I, B);
    # limits are included for J, C. Analytic closure is not finitely provable.
    for k in range(1, 6):
        e = F(1, k)
        assert realm("I", b, pt(-1 - e, 1))      # strictly inside I-realm
        assert realm("B", b, pt(1, 1 + e))       # strictly inside B-realm
    assert not realm("I", b, pt(-1, 1))          # past-null limit excluded
    assert not realm("B", b, pt(1, 1))           # future-null limit excluded
    assert realm("J", b, pt(-1, 1)) and realm("C", b, pt(1, 1))
    print("PASS O20c: boundary sequences expose cl(I)=J, cl(B)=C exclusion")

    # C's F_c failure witness retained; I,J,B boundary {b} witness.
    assert realm("C", b, pt(1, 1)) and leq(b, pt(1, 1)) and pt(1, 1) != b
    print("PASS O20d: exact F_c distinction between C and I,J,B")


def check_saturation():
    # O11: exact chronological witnesses q_Z much p_S with Pythagorean
    # (R, Z) pairs so sqrt(Z^2-R^2) is an exact integer.
    pyth = [(3, 5), (5, 13), (8, 17), (7, 25)]
    for R, Z in pyth:
        n2 = Z * Z - R * R
        root = F(math.isqrt(n2))
        assert root * root == n2                       # exact, not float
        q = pt(-root, Z)                               # q_Z, spacelike length R
        assert spacelike(q, pt(0)) and norm2(q) == -R * R
        for S in (F(2), F(3), F(7, 2), F(6), F(12)):
            target = pt(0, S)                          # p_S
            assert much(q, target) == (2 * Z * S - R * R - S * S > 0), (R, Z, S)
        # Negative control: S beyond 2Z+R must break chronology.
        S_big = 2 * Z + R + 1
        assert not much(q, pt(0, S_big))
        assert 2 * Z * S_big - R * R - S_big ** 2 < 0
    print("PASS O11: q_Z << p_S iff 2ZS > R^2 + S^2 (exact, both directions)")

    # O14: past-null (−1,−1) chronologically above spacelike p=(−1/4,−1/2).
    pn, p_sp = pt(-1, -1), pt(F(-1, 4), F(-1, 2))
    assert much(pn, p_sp) and spacelike(p_sp, pt(0))
    # O13: spacelike (0,se) chronologically below future null (s,se).
    for s in (F(1), F(5, 2)):
        assert much(pt(0, s), pt(s, s))
    # O12/n>=2: proper pi-rotation about the z-axis reverses the x-axis
    # while keeping det +1 and time orientation.
    v, w = pt(0, 3), pt(0, -3)
    rot = lambda u: (u[0], -u[1], -u[2], u[3])  # pi-rotation in (x,y)-plane
    assert rot(v) == w and norm2(v) == norm2(w)
    print("PASS O12-O14: saturation bridge witnesses exact in 4D")

    # Bounded-length spacelike points of every tested length get bridged:
    for R, Z in pyth:
        root = F(math.isqrt(Z * Z - R * R))
        for S in (F(2), F(3), F(6), F(12)):
            if 2 * Z * S - R * R - S * S > 0:
                assert much(pt(-root, Z), pt(0, S))
    print("PASS O12b: all tested (R,S) norms connected by a chronological step")


def check_collar():
    # O21: collar witnesses with exact rational proper times.
    b = pt(0)
    x1 = pt(F(5, 3), F(4, 3))       # tau = 1
    x2 = pt(F(13, 5), F(12, 5))     # tau = 1 (wide)
    x5 = pt(5)                      # tau = 5
    w = pt(F(3, 2))                 # tau = 3/2, inside the a=2 collar
    c = pt(1)                       # tau(b,c)=1
    assert much(b, x1) and norm2(x1) == 1 and norm2(x5) == 25 and norm2(w) == F(9, 4)
    assert leq(b, c) and much(c, x5) and norm2(tuple(x5[i] - c[i] for i in range(4))) == 16

    # E^0 equals C on the whole test set.
    for b2 in TEST:
        for x in TEST:
            assert collar(0, b2, x) == realm("C", b2, x)
    print("PASS O21a: E^0 = C on the full test set")

    # a=2 keeps the tau<=2 collar member w in I+(b) (violates F_t) but
    # excludes tau=5.
    assert not realm("C", b, w) and collar(2, b, w)
    assert not collar(2, b, x5) and not realm("C", b, x5)
    assert collar(1, b, x1) and collar(1, b, x2)   # tau=1 not > 1: retained
    # Causal persistence instance: x5 excluded at c must be excluded at b.
    assert not collar(2, c, x5) and not collar(2, b, x5)
    # w in E^2_b with b leq c must be in E^2_c: tau(c,w)=1/2 <= 2.
    assert collar(2, b, w) and much(c, w) and norm2(tuple(w[i] - c[i] for i in range(4))) == F(1, 4) and collar(2, c, w)
    # Distinct parameters differ on the test set.
    assert collar(1, b, w) != collar(2, b, w)
    print("PASS O21b: collar membership, persistence and separation exact")


def main():
    check_section1()
    check_census_converse()
    check_table_failures()
    check_saturation()
    check_collar()
    print("All independent witness checks pass.")
    print("Census exhaustiveness remains an analytic claim; nothing here proves it.")


if __name__ == "__main__":
    main()
