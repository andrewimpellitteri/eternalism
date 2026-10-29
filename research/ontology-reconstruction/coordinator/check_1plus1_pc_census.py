"""P_c (causal persistence) census in 1+1 Minkowski without parity.

Companion to check_1plus1_census.py (P_t version, 16 assignments). Here
persistence is causal: b <= c (null steps allowed) implies E_b subset E_c,
and future exclusion is the causal version F_c: E_0 cap J^+(0) = {0}.

Reduction (same as the P_t case): P := E_0 must satisfy
  S:    0 in P,
  P_c:  d <= x in P implies d in P   (causal past closure; null allowed:
        d <= x iff Du_L <= 0 and Du_R <= 0, non-strict),
  F_c:  P cap J^+(0) = {0}.

Consequences (analytic, each witnessed below):
  * J^-(0) = I^- u N-R u N-L u {0} is mandatory (causal past of 0). This
    makes BOTH past-null branches forced, unlike the P_t case.
  * I^+, N+R, N+L are forbidden (they lie in J^+(0) minus 0).
  * Wedge all-or-nothing survives (boost orbits unchanged).
  * Wedge-in drags in nothing new (N-R already mandatory), but the
    implication direction is witnessed: excluding N-R while keeping RW
    breaks closure on the causal pair (-2,0) <= (-1,2).
Hence the only free bits are the two wedges, and the census is exactly
2 x 2 = 4 assignments: J itself (I^- u N^- u {0}), J+RW, J+LW, and
J+RW+LW (= B's region set). Note I = I^- u {0} does NOT satisfy P_c (null
steps force the past nulls), consistent with the coordinator's n>=2
collapse "boundedness and P_c give J only": in 1+1 without parity J is
still the minimum, but wedge freedom survives, so 4 assignments survive.

Correction log: an earlier coordinator conjecture announced 9 (per-side
(wedge, past-null) options (0,0),(0,1),(1,1)); the script refuted it
because the past-null options are never free - J^-(0) is mandatory. The
script caught the slip before any note recorded it as checked; the census
note addendum has been corrected.

Script checks: distinctness, causal-past closure, S, F_c, boost
invariance on the witness grid; the closure-breaking witness; mandatory-
and forbidden-region witnesses. Finite checks are witnesses; the count
rests on the analytic orbit/chain argument above.
"""

from fractions import Fraction as F


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


# bits = (w_R, w_L); past nulls are mandatory, future nulls forbidden.
COMBOS = [(wr, wl) for wr in (0, 1) for wl in (0, 1)]
assert len(COMBOS) == 4


def in_P(bits, uL, uR):
    reg = region(uL, uR)
    if reg in ("0", "Im", "NmR", "NmL"):
        return True
    if reg in ("Ip", "NpR", "NpL"):
        return False
    if reg == "RW":
        return bool(bits[0])
    if reg == "LW":
        return bool(bits[1])
    raise AssertionError(reg)


GRID = [
    (F(0), F(0)),
    (F(-1), F(-2)), (F(-3), F(-1)),
    (F(2), F(1)), (F(1), F(3)),
    (F(-1), F(2)), (F(-2), F(1)), (F(-4), F(1)),
    (F(1), F(-2)), (F(2), F(-1)),
    (F(0), F(2)), (F(0), F(1)),
    (F(2), F(0)),
    (F(-2), F(0)), (F(-1), F(0)),
    (F(0), F(-2)),
]


def causal_future(d, x):
    return d[0] <= x[0] and d[1] <= x[1]


def main():
    sigs = set()
    for bits in COMBOS:
        sig = tuple(in_P(bits, p[0], p[1]) for p in GRID)
        sigs.add(sig)
        assert in_P(bits, F(0), F(0))                       # S
        for p in GRID:                                      # F_c, pointwise
            if p[0] >= 0 and p[1] >= 0 and not (p[0] == 0 and p[1] == 0):
                assert not in_P(bits, p[0], p[1]), (bits, p)
        for p in GRID:                                      # boost invariance
            q = (p[0] / 3, p[1] * 3)
            assert in_P(bits, q[0], q[1]) == in_P(bits, p[0], p[1])
        for d in GRID:                                      # causal closure
            if not in_P(bits, d[0], d[1]):
                continue
            for x in GRID:
                if causal_future(x, d):
                    assert in_P(bits, x[0], x[1]), (bits, x, d)
    assert len(sigs) == 4, len(sigs)
    print("PASS: 4 P_c assignments distinct, causally closed, S and F_c"
          " on the witness grid")

    # Necessity: excluding N-R while keeping RW breaks causal closure
    # (this is why the past-null branches are not free when a wedge is in;
    # they are in fact mandatory regardless, via J^-(0)).
    bits_rw_no_nm = lambda uL, uR: region(uL, uR) in ("0", "Im", "NmL") or \
        region(uL, uR) == "RW"
    assert bits_rw_no_nm(F(-1), F(2))
    assert not bits_rw_no_nm(F(-2), F(0))
    assert causal_future((F(-2), F(0)), (F(-1), F(2)))
    print("PASS: RW-without-N-R breaks causal closure on (-2,0) <= (-1,2)"
          " (direction witnessed)")

    # Mandatory J^-(0) and forbidden J^+(0) pointwise witnesses.
    for bits in COMBOS:
        for p in ((F(-1), F(0)), (F(0), F(-1)), (F(-2), F(-1))):
            assert in_P(bits, p[0], p[1]), (bits, p)        # in J^-(0)
        for p in ((F(0), F(1)), (F(1), F(0))):
            assert not in_P(bits, p[0], p[1]), (bits, p)    # in J^+(0)\{0}
    print("PASS: J^-(0) members always present, J^+(0) members always"
          " absent")

    print("Result: exactly 4 assignments satisfy S, P_c, F_c and"
          " boost+translation covariance in 1+1 without parity:")
    print("        J itself, J+RW, J+LW, J+RW+LW. I does not satisfy P_c."
          " Completeness rests on the analytic argument in the docstring;"
          " the grid provides witnesses only.")


if __name__ == "__main__":
    main()
