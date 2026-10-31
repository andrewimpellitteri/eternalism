"""Exact sign-region certificate for the 1+1 census, 30 October 2026.

Independent coordinator implementation; imports no interrupted worker code.
After the analytic boost/persistence saturation lemma, each candidate is a
union of products of the three atoms (-infinity,0), {0}, (0,infinity).
The operations below are exact operations on those whole intervals, not
sampling or truncation. The reduction to region unions remains a separate
analytic obligation; this certificate checks all 64 reduced candidates.
"""

from itertools import product

NEG, ZERO, POS = -1, 0, 1
SIGNS = (NEG, ZERO, POS)
REGIONS = frozenset(product(SIGNS, repeat=2))
IM, IP, O = (-1, -1), (1, 1), (0, 0)
RW, LW = (-1, 1), (1, -1)
NPR, NPL, NMR, NML = (0, 1), (1, 0), (-1, 0), (0, -1)
MANDATORY = frozenset((IM, O))
FREE = (NPR, RW, NMR, NPL, LW, NML)
J_MINUS = frozenset((IM, NMR, NML, O))
J_PLUS = frozenset((IP, NPR, NPL, O))


def atom_sum(a, b):
    # Opposite open rays sum to the whole real line, including zero.
    if a * b == -1:
        return frozenset(SIGNS)
    if a == ZERO:
        return frozenset((b,))
    return frozenset((a,))  # same nonzero ray, or zero second summand


def region_sum(a, b):
    return frozenset(product(atom_sum(a[0], b[0]), atom_sum(a[1], b[1])))


def add(a, b):
    return frozenset(r for x in a for y in b for r in region_sum(x, y))


def closure(a):
    return frozenset(
        r for x, y in a
        for r in product({x, ZERO}, {y, ZERO})
    )


def reflect(a):
    return frozenset((y, x) for x, y in a)


def bits(a):
    return tuple(tuple(int(r in a) for r in side)
                 for side in ((NPR, RW, NMR), (NPL, LW, NML)))


def main():
    # Exact primitive identities and independent interval-sign witnesses.
    assert atom_sum(NEG, POS) == set(SIGNS)
    assert atom_sum(NEG, NEG) == {NEG}
    assert atom_sum(ZERO, POS) == {POS}
    assert region_sum(RW, LW) == REGIONS
    assert region_sum(NPR, IM) == {IM, NMR, RW}
    assert region_sum(NMR, IM) == {IM}
    for r in REGIONS:
        assert region_sum(r, O) == {r}

    all_candidates = [frozenset(MANDATORY | {
        r for flag, r in zip(flags, FREE) if flag
    }) for flags in product((False, True), repeat=6)]
    valid = [a for a in all_candidates if add(a, {IM}) <= a]
    monotone = [a for a in all_candidates if all(
        nplus <= wedge <= nminus for nplus, wedge, nminus in bits(a)
    )]
    assert valid == monotone and len(valid) == 16

    pc = [a for a in valid if add(a, J_MINUS) <= a]
    fc = [a for a in valid if not a & (J_PLUS - {O})]
    closed = [a for a in valid if closure(a) <= a]
    symmetric = [a for a in valid if reflect(a) == a]
    additive = [a for a in valid if add(a, a) <= a]

    assert len(pc) == 9 and all({NMR, NML} <= a for a in pc)
    assert len(fc) == 9
    assert len([a for a in pc if a in fc]) == 4
    assert len(symmetric) == 4
    # An unordered two-element orbit, or singleton when reflection fixes it.
    assert len({frozenset((a, reflect(a))) for a in valid}) == 10

    left_half = frozenset((x, y) for x, y in REGIONS if x <= 0)
    right_half = reflect(left_half)
    c = REGIONS - {IP}
    assert set(closed) == {J_MINUS, c, left_half, right_half}
    assert [a for a in closed if a in fc] == [J_MINUS]

    # Four and only four failures of additivity: both wedges present.
    assert set(additive) == {a for a in valid if not {RW, LW} <= a}
    assert len(additive) == 12
    assert set(a for a in additive if a in closed) == {
        J_MINUS, left_half, right_half
    }
    assert len([a for a in additive if a in pc]) == 5
    assert len([a for a in additive if a in fc]) == 8
    assert len([a for a in additive if a in fc and a in pc]) == 3

    print("PASS: exact 64-candidate reduction gives 16 chronological past sets")
    print("PASS: P_c 9; F_c 9; both 4; closed 4; closed + F_c 1")
    print("PASS: reflection invariant 4; mirror equivalence classes 10")
    print("PASS: transitive 12; transitive + closed 3; transitive + P_c 5")
    print("PASS: transitive + F_c 8; transitive + P_c + F_c 3")
    print("Scope: exact region operations; continuous-domain orbit reduction remains analytic")


if __name__ == "__main__":
    main()
