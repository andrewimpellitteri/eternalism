"""Exact witnesses for the 30 October corrections to the 1+1 census.

This checks refinements of the 16 analytically classified region unions.
Counts on a witness grid are cross-checks, not completeness proofs on R^2.
In particular it distinguishes strengthening persistence from strengthening
future exclusion, and reflection invariance from quotienting by reflection.
"""

from fractions import Fraction as Q

from check_1plus1_census import BITS, GRID, in_P


def member(bits, point):
    return in_P(bits, *point)


def pc_witnesses_pass(bits):
    return all(
        member(bits, lower)
        for upper in GRID if member(bits, upper)
        for lower in GRID
        if lower[0] <= upper[0] and lower[1] <= upper[1]
    )


def fc_witnesses_pass(bits):
    return all(
        not member(bits, p)
        for p in GRID if p != (0, 0) and p[0] >= 0 and p[1] >= 0
    )


# Region-closure incidences. The sequences below witness every possible
# failure: interior past -> either past null; either wedge -> its two
# null boundaries. The analytic proof justifies this finite list.
BOUNDARIES = [
    (lambda h: (-Q(1), -h), (-Q(1), Q(0))),
    (lambda h: (-h, -Q(1)), (Q(0), -Q(1))),
    (lambda h: (-h, Q(1)), (Q(0), Q(1))),
    (lambda h: (-Q(1), h), (-Q(1), Q(0))),
    (lambda h: (h, -Q(1)), (Q(0), -Q(1))),
    (lambda h: (Q(1), -h), (Q(1), Q(0))),
]


def boundary_witnesses_pass(bits):
    for sequence, limit in BOUNDARIES:
        inside = [member(bits, sequence(Q(1, k))) for k in (2, 3, 10, 100)]
        assert len(set(inside)) == 1  # stays in one boost-saturated region
        if inside[0] and not member(bits, limit):
            return False
    return True


def main():
    pc = [bits for bits in BITS if pc_witnesses_pass(bits)]
    fc = [bits for bits in BITS if fc_witnesses_pass(bits)]
    both = [bits for bits in pc if bits in fc]
    closed = [bits for bits in BITS if boundary_witnesses_pass(bits)]
    invariant = [bits for bits in BITS if all(
        member(bits, (v, u)) == member(bits, (u, v)) for u, v in GRID
    )]
    mirror_classes = {tuple(sorted(bits)) for bits in BITS}
    assert (len(BITS), len(pc), len(fc), len(both)) == (16, 9, 9, 4)
    assert (len(closed), len(invariant), len(mirror_classes)) == (4, 4, 10)

    j = ((0, 0, 1), (0, 0, 1))
    c = ((1, 1, 1), (1, 1, 1))
    h_l = ((1, 1, 1), (0, 0, 1))
    h_r = ((0, 0, 1), (1, 1, 1))
    assert set(closed) == {j, c, h_l, h_r}
    assert [bits for bits in closed if bits in fc] == [j]

    # Independent coordinate formulas for the omitted closed candidates.
    # Each half-space is additive; this tests its exact identification and
    # provides transitivity witnesses without importing the n>=2 table.
    for bits, coordinate in ((h_l, 0), (h_r, 1)):
        assert bits in pc and bits not in fc and bits not in invariant
        for p in GRID:
            assert member(bits, p) == (p[coordinate] <= 0)
        for p in GRID:
            for q in GRID:
                total = (p[0] + q[0], p[1] + q[1])
                assert member(bits, total) == (total[coordinate] <= 0)
                if member(bits, p) and member(bits, q):
                    assert member(bits, total)

    print("PASS: P_c + F_t gives 9; P_t + F_c gives 9; P_c + F_c gives 4")
    print("PASS: reflection invariance gives 4 rules; mirror quotient gives 10 classes")
    print("PASS: closed cases are J, C and the two explicit null half-spaces")
    print("PASS: closedness + F_c leaves J; half-spaces refute the transferred transitivity row")
    print("Scope: exact finite witnesses; completeness uses ONE_PLUS_ONE_CENSUS.md")


if __name__ == "__main__":
    main()
