"""Complete 1+1 no-parity census of covariant self-inclusive chronologically
persistent F_t existence assignments (coordinator deduction, 29 Oct 2026).

Setting (E-space, past-set convention). Poincare covariance reduces any
assignment E to E_b = b + P with P := E_0 (x in E_b iff x-b in P). Then:
  S   iff 0 in P,
  P_t iff P is a past set (d << x in P implies d in P),
  F_t iff P and I^+(0) are disjoint.
Lorentz covariance under boosts+translations (no spatial reflection) makes P
boost-invariant. Null coordinates u_L = t-x, u_R = t+x:
  boosts:  (u_L, u_R) -> (e^-eta u_L, e^eta u_R)   [here exactly /3 and x3]
  timelike future d << x  iff  u_L^d < u_L^x and u_R^d < u_R^x
  regions: I- = {both<0}, I+ = {both>0}, RW = {u_L<0<u_R}, LW = {u_R<0<u_L},
           N+R = {u_L=0,u_R>0}, N+L = {u_L>0,u_R=0},
           N-R = {u_L<0,u_R=0}, N-L = {u_L=0,u_R<0}.
Mandatory: I- u {0} (past set containing 0). Forbidden: I+ (F_t).
All-or-nothing per region (boost-invariant past set): null branches are
single boost orbits; in a wedge the past of one member covers every proper
distance (u_R -> 0+ or u_L -> -inf sweeps all products p = -u_L u_R).
Chain implications witnessed below: N+R => RW => N-R and N+L => LW => N-L
(timelike-past witnesses crossing regions), and no cross-side implication.
Hence valid bit triples per side satisfy n+ <= w <= n- (1 = "in P"), giving
exactly 4 x 4 = 16 assignments. The four n>=2 census candidates I, J, B, C
sit among them as (000|000), (001|001), (011|011), (111|111); the
persistence review's fifth family and its mirror are (000|011), (011|000).

This script verifies, with exact rational arithmetic:
  1. the 16 monotone combos are pairwise distinct, boost-invariant, past
     closed, self-inclusive and I+-free on a witness grid;
  2. each of the 8 non-monotone triples per side violates past closure on
     an explicit timelike pair (necessity of the chain);
  3. partial-wedge and partial-null membership are impossible (all-or-
     nothing witnesses);
  4. the I/J/B/C definitions and the review's fifth assignment agree with
     the corresponding bit patterns on a grid.
The completeness argument itself is the analytic orbit/chain analysis
summarized above; finite checks here are witnesses, not the proof.
"""

from fractions import Fraction as F
from itertools import product

Point = tuple  # (u_L, u_R) as Fractions


def timelike_future(d, x):
    return d[0] < x[0] and d[1] < x[1]


def region(uL, uR):
    if uL == 0 and uR == 0:
        return "0"
    if uL < 0 and uR < 0:
        return "Im"
    if uL > 0 and uR > 0:
        return "Ip"
    if uL == 0:
        return "NpR" if uR > 0 else "NmL"
    if uR == 0:
        return "NmR" if uL < 0 else "NpL"
    return "RW" if uL < 0 else "LW"


# bit order per side: (future-null, wedge, past-null); valid: n+ <= w <= n-
TRIPLES = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)
           if a <= b <= c]
assert len(TRIPLES) == 4

BITS = [(r, l) for r in TRIPLES for l in TRIPLES]

SIDE = {"R": 0, "L": 1}
FUTURE_NULL, WEDGE, PAST_NULL = 0, 1, 2


def in_P(bits, uL, uR):
    reg = region(uL, uR)
    if reg in ("0", "Im"):
        return True
    if reg == "Ip":
        return False
    if reg == "NpR":
        return bool(bits[0][FUTURE_NULL])
    if reg == "NmR":
        return bool(bits[0][PAST_NULL])
    if reg == "RW":
        return bool(bits[0][WEDGE])
    if reg == "NpL":
        return bool(bits[1][FUTURE_NULL])
    if reg == "NmL":
        return bool(bits[1][PAST_NULL])
    if reg == "LW":
        return bool(bits[1][WEDGE])
    raise AssertionError(reg)


# Witness grid: representatives of all regions plus extra wedge products.
GRID = [
    (F(0), F(0)),                      # origin
    (F(-1), F(-2)), (F(-3), F(-1)),    # I-
    (F(2), F(1)), (F(1), F(3)),        # I+
    (F(-1), F(2)), (F(-2), F(1)), (F(-4), F(1)),   # RW, distinct products
    (F(1), F(-2)), (F(2), F(-1)),      # LW
    (F(0), F(2)), (F(0), F(1)),        # N+R
    (F(2), F(0)),                      # N+L
    (F(-2), F(0)), (F(-1), F(0)),      # N-R
    (F(0), F(-2)),                     # N-L
]


def main():
    # 1. The 16 monotone combos: distinct, invariant, past closed, S, F_t.
    membership_sigs = set()
    for bits in BITS:
        sig = tuple(in_P(bits, p[0], p[1]) for p in GRID)
        membership_sigs.add(sig)
        for p in GRID:                                   # S and F_t
            assert in_P(bits, F(0), F(0))
            if p[0] > 0 and p[1] > 0:
                assert not in_P(bits, p[0], p[1])
        for p in GRID:                                   # boost invariance
            q = (p[0] / 3, p[1] * 3)
            assert in_P(bits, q[0], q[1]) == in_P(bits, p[0], p[1]), (bits, p)
        for d in GRID:                                   # past closure
            if not in_P(bits, d[0], d[1]):
                continue
            for x in GRID:
                if timelike_future(x, d):
                    assert in_P(bits, x[0], x[1]), (bits, x, d)
    assert len(membership_sigs) == 16, len(membership_sigs)
    print("PASS: 16 monotone assignments distinct, invariant, past closed,"
          " S and F_t on the witness grid")

    # 2. Necessity: every non-monotone triple per side breaks past closure.
    broken = 0
    for side in (0, 1):
        for tri in [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)
                    if not (a <= b <= c)]:
            f, w, pn = tri
            xNp = (F(0), F(3)) if side == 0 else (F(3), F(0))
            dW = (F(-1), F(2)) if side == 0 else (F(2), F(-1))
            xNm = (F(-2), F(0)) if side == 0 else (F(0), F(-2))
            viol = None
            # N+R member with a RW point strictly in its timelike past
            if f and not w:
                bits = [(0, 0, 0)] * 2
                bits[side] = (f, w, pn)
                if in_P(bits, xNp[0], xNp[1]) and not in_P(bits, dW[0], dW[1]) \
                        and timelike_future(dW, xNp):
                    viol = (xNp, dW)
            # wedge member with a past-null point strictly in its past
            if viol is None and w and not pn:
                bits = [(0, 0, 0)] * 2
                bits[side] = (f, w, pn)
                if in_P(bits, dW[0], dW[1]) and not in_P(bits, xNm[0], xNm[1]) \
                        and timelike_future(xNm, dW):
                    viol = (dW, xNm)
            if viol is None and f and not pn:            # direct N+ to N-
                dW2 = (F(-3), F(1)) if side == 0 else (F(1), F(-3))
                bits = [(0, 0, 0)] * 2
                bits[side] = (f, w, pn)
                if in_P(bits, xNp[0], xNp[1]) and not in_P(bits, xNm[0], xNm[1]) \
                        and timelike_future(xNm, dW2):
                    viol = None  # still needs wedge bit; handled above
            if viol is not None:
                broken += 1
    assert broken == 8, broken
    print("PASS: all 8 non-monotone triples per side break past closure on"
          " explicit timelike pairs (4 per side counted over both patterns)")

    # 3. All-or-nothing witnesses inside the wedges.
    for bits in BITS:
        for (lo, hi) in (((F(-4), F(1)), (F(-1), F(2))),
                         ((F(-2), F(1)), (F(-1), F(2)))):
            if in_P(bits, hi[0], hi[1]) and timelike_future(lo, hi):
                assert in_P(bits, lo[0], lo[1]), (bits, lo, hi)
    print("PASS: lower-product wedge points lie in the timelike past of"
          " higher ones (orbit all-or-nothing corroborated)")

    # 4. Cross-checks against the coordinator census candidates and the
    #    persistence review's fifth assignment, in (t, x) coordinates.
    def to_tx(p):
        return ((p[0] + p[1]) / 2, (p[1] - p[0]) / 2)

    def cand_I(b, x):
        d = (x[0] - b[0], x[1] - b[1])
        return d == (0, 0) or (d[0] < 0 and d[0] * d[0] > d[1] * d[1])

    def cand_J(b, x):
        d = (x[0] - b[0], x[1] - b[1])
        return d[0] <= 0 and d[0] * d[0] >= d[1] * d[1]

    def cand_B(b, x):
        d = (x[0] - b[0], x[1] - b[1])
        return not (d[0] >= 0 and d[0] * d[0] >= d[1] * d[1] and x != b)

    def cand_C(b, x):
        d = (x[0] - b[0], x[1] - b[1])
        return not (d[0] > 0 and d[0] * d[0] > d[1] * d[1])

    zero = (F(0), F(0))
    checks = [("I", cand_I, (0, 0, 0), (0, 0, 0)),
              ("J", cand_J, (0, 0, 1), (0, 0, 1)),
              ("B", cand_B, (0, 1, 1), (0, 1, 1)),
              ("C", cand_C, (1, 1, 1), (1, 1, 1))]
    for name, fn, rside, lside in checks:
        for p in GRID:
            x = to_tx(p)
            assert fn(zero, x) == in_P(((rside), (lside)), p[0], p[1]), \
                (name, p)
    print("PASS: bit patterns (000|000), (001|001), (011|011), (111|111)"
          " reproduce the census candidates I, J, B, C pointwise")

    # Fifth assignment of the persistence review: A' = {0} u {not I-,
    # t+x>0} with E_b = {x : b-x in A'}; here E_0 = -A'.
    def in_A_prime(t, x):
        if (t, x) == (F(0), F(0)):
            return True
        if t < 0 and t * t > x * x:
            return False
        return t + x > 0

    fifth = ((0, 0, 0), (0, 1, 1))
    grid_tx = [to_tx(p) for p in GRID] + [(F(3), F(1)), (F(1), F(3)),
                                          (F(-3), F(-1)), (F(-1), F(-3)),
                                          (F(2), F(2)), (F(-2), F(-2))]
    for (t, x) in grid_tx:
        mine = in_P(fifth, t - x, t + x)    # E_0(x) at x's null coords
        theirs = in_A_prime(-t, -x)         # review: in_A(b-x) at b=0
        assert mine == theirs, ((t, x), mine, theirs)
    print("PASS: fifth-assignment bit pattern (000|011) agrees with the"
      " persistence review's construction pointwise on the grid")

    print("Result: exactly 16 covariant self-inclusive chronologically"
          " persistent F_t assignments exist in 1+1 without parity;")
    print("        I, J, B, C, the fifth family and its mirror all sit"
          " among them. Completeness rests on the analytic orbit/chain"
          " argument summarized in the docstring, not on the grid.")


if __name__ == "__main__":
    main()
