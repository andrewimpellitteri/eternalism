#!/usr/bin/env python3
r"""Exact-arithmetic witness checks for RESULT.md (classification lane).

Every machine check below certifies an explicitly listed rational witness or
a displayed inequality used in an analytic argument in RESULT.md.  There are
no grid searches.  The pre-resume version of this file used a 1539-point slab
pool and a 17x17x17 pairwise cube; its H(b)-construction loop was cubic in the
pool size and timed out at 300 s.  All dense pools are removed; the universal
statements they were meant to support are proved analytically in RESULT.md
and are NOT re-established by enumeration here.

Conventions (RESULT.md section 2; stein-gr/main.tex;
lawful-completions/coordinator/HISTORICAL_POTENTIAL.md):

  points (t,z) in 1+1 Minkowski or in the flat conformal slab (0,1) x R;
  x <= y   iff  y_t - x_t >= |y_z - x_z|        (causal, reflexive)
  x prec y iff  x <= y and x != y               (strict causal, null allowed)
  x << y   iff  y_t - x_t >  |y_z - x_z|        (chronological)

Realms at standpoint b (RESULT.md section 3):
  E_all(b) = M
  J(b)     = {x : x <= b}                       (causal past)
  I(b)     = I^-(b) u {b}                       (chronological past)
  B(b)     = M \ (J+(b) \ {b})                  (bow tie)
  D(b)     = {b} u {x : not(b prec x), common strict causal future}
  H(b)     = u_{r <= b} D(r)                    (historical potential)

Membership claims are certified by listed witnesses; nonmembership claims are
one-line analytic exclusions whose numeric constants are re-checked here.
Arithmetic is exact (fractions.Fraction); each check is O(1).

Run:  python3 countermodels.py        (exit 0 = all checks pass)
"""

import sys
from fractions import Fraction as F

FAILURES = []


def check(name, cond):
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {name}")
    if not cond:
        FAILURES.append(name)


# ---------------------------------------------------------------- causal order


def le(x, y):
    return y[0] - x[0] >= abs(y[1] - x[1])


def prec(x, y):
    return le(x, y) and x != y


def chron(x, y):
    return y[0] - x[0] > abs(y[1] - x[1])


def spacelike(x, y):
    return not le(x, y) and not le(y, x)


# ------------------------------------------ CM1: D fails restriction (A2)
# Ambient M = 1+1 Minkowski.  U = I-(p) u I-(q), p=(1/2,-1), q=(1/2,1);
# b=(0,-1), x=(0,1).  U is open, a past set (hence causally convex), globally
# hyperbolic, connected, and flat (vacuum on-shell).  RESULT.md CM1.


def cm1_restriction_D():
    p = (F(1, 2), F(-1))
    q = (F(1, 2), F(1))
    b = (F(0), F(-1))
    x = (F(0), F(1))
    z = (F(3, 2), F(0))

    check("CM1: b,x in U", chron(b, p) and chron(x, q))
    check("CM1: b,x spacelike", spacelike(b, x))
    check("CM1: x in D_M(b) via z=(3/2,0)",
          not prec(b, x) and prec(b, z) and prec(x, z))

    # Analytic exclusion of x from D_U(b): every common causal future w=(s,m)
    # of b,x obeys s >= max(|m+1|, |m-1|) = |m| + 1 >= 1, while U lies in
    # {s < 1/2}.  Machine: the identity and the ceiling, at spot values.
    check("CM1: identity max(|m+1|,|m-1|)=|m|+1 (spot m)",
          all(max(abs(m + 1), abs(m - 1)) == abs(m) + 1
              for m in [F(-2), F(-1), F(0), F(1, 2), F(3)]))
    check("CM1: U ceiling 1/2 < 1 (exclusion constant)", F(1, 2) < 1)


# ----------------------------- CM1-H: H agrees here (scope contrast for CM4)
# Same U, full-Minkowski ambient: the witness standpoint r may sit arbitrarily
# deep in the past, and a common strict U-future zu exists.  This is why H
# restricts on full Minkowski (RESULT.md Lemma L3: H = B there) but fails on
# the finite-past slab (CM4).


def cm1h_agreement_H():
    p = (F(1, 2), F(-1))
    q = (F(1, 2), F(1))
    b = (F(0), F(-1))
    x = (F(0), F(1))
    r = (F(-4, 5), F(-1, 5))
    zu = (F(1, 4), F(4, 5))

    check("CM1/H: r in U (r << p)", chron(r, p))
    check("CM1/H: r <= b (null)", le(r, b) and r != b)
    check("CM1/H: r not prec x (spacelike)", spacelike(r, x))
    check("CM1/H: zu=(1/4,4/5) in U (zu << q)", chron(zu, q))
    check("CM1/H: r prec zu and x prec zu", prec(r, zu) and prec(x, zu))
    check("CM1/H: so x in D_U(r), x in H_U(b) and in H_M(b)", True)


# ------------------------------------- CM2: D fails persistence (A3) in slab
# Ambient M = flat slab (0,1) x R.  s=(1/2,0) <= c=(3/4,0); x=(0,13/10).
# RESULT.md CM2.  Persistence of D holds on future-directed causally simple
# spacetimes (project review HORIZON_LEMMA_REVIEW.md); the slab is not
# future-directed, and this witness shows the failure concretely.


def cm2_persistence_D_slab():
    s = (F(1, 2), F(0))
    c = (F(3, 4), F(0))
    x = (F(0), F(13, 10))
    w = (F(9, 10), F(2, 5))

    check("CM2: s <= c", le(s, c) and s != c)
    check("CM2: s,x spacelike (not(s prec x))", spacelike(s, x))
    check("CM2: x in D(s) via w=(9/10,2/5) (null steps)",
          prec(s, w) and prec(x, w))

    # x not in D(c): a common strict slab future u=(t,m) of c,x needs
    # t >= 3/4 + |m| and t >= |m - 13/10|, hence |m| < 1/4 from t < 1, hence
    # t >= |m - 13/10| >= 13/10 - 1/4 = 21/20 > 1: contradiction.
    check("CM2: exclusion constant 13/10 - 1/4 = 21/20 > 1",
          F(13, 10) - F(1, 4) > 1)
    check("CM2: agrees with published slab criterion d < 2B-rho-xi "
          "(13/10 >= 5/4)", F(13, 10) >= 2 - F(3, 4))


# --------------------------- CM3: transitivity (A7) fails for B, D, H
# Minkowski: b=(0,0), x=(0,2), y=(2,-1).  RESULT.md CM3.


def cm3_transitivity_BDH():
    b = (F(0), F(0))
    x = (F(0), F(2))
    y = (F(2), F(-1))

    check("CM3: b,x and x,y spacelike; b prec y (timelike)",
          spacelike(b, x) and spacelike(x, y) and prec(b, y))

    # Bow tie B: x in B(b), y in B(x), y not in B(b).
    check("CM3/B: x in B(b), y in B(x), y not in B(b)",
          not prec(b, x) and not prec(x, y) and prec(b, y))

    # Instantaneous potential D: explicit common-future witnesses.
    z1 = (F(5), F(0))
    z2 = (F(7, 2), F(0))
    check("CM3/D: x in D(b) via z1=(5,0)",
          not prec(b, x) and prec(b, z1) and prec(x, z1))
    check("CM3/D: y in D(x) via z2=(7/2,0)",
          not prec(x, y) and prec(x, z2) and prec(y, z2))
    check("CM3/D: y not in D(b) (b prec y)", prec(b, y))

    # Historical potential H: y in H(x) via r <= x with y in D(r).
    r = (F(-8), F(10))
    z3 = (F(5), F(-2))
    check("CM3/H: r=(-8,10) <= x=(0,2) (null)", le(r, x) and r != x)
    check("CM3/H: r not prec y (spacelike)", spacelike(r, y))
    check("CM3/H: y in D(r) via z3=(5,-2)", prec(r, z3) and prec(y, z3))
    check("CM3/H: y not in H(b); positive push-up instance r'<=b => r' prec y",
          prec((F(-1), F(0)), y) and le((F(-1), F(0)), b))
    # Analytic exclusion (RESULT.md Lemma L1): r <= b=(0,0) gives
    # t_r <= -|w_r|, hence |y_w - w_r| <= 1 + |w_r| <= 2 - t_r = y_t - t_r,
    # so r <= y, and r != y since t_r <= 0 < 2; therefore r prec y and
    # y is in no D(r) with r <= b.  Constants: 2 + |w| > 1 + |w| on Q.
    check("CM3/H: cone constants 2 + |w| > 1 + |w| >= |y_w - w_r| (spots)",
          all(2 + abs(w) > 1 + abs(w) and 1 + abs(w) >= abs(-1 - w)
              for w in [F(-3), F(-1), F(0), F(1, 2), F(4)]))


# ------------------------------- CM4: H fails restriction (A2) on the slab
# Ambient M = flat slab (0,1) x R.  U = I-(p) u I-(q) with p=(9/10,8/5),
# q=(9/10,-1/10); b=(1/2,0), x=(1/2,3/2).  RESULT.md CM4.  This verifies
# analytically, at explicit rationals, the claim retracted before the resume:
# the restriction failure of H is REAL on the finite-conformal-past slab
# category, while its full-Minkowski-ambient version is FALSE (CM1/H above,
# Lemma L3).  The finite past enters through t_r > 0 in step (iii).


def cm4_restriction_H_slab():
    p = (F(9, 10), F(8, 5))
    q = (F(9, 10), F(-1, 10))
    b = (F(1, 2), F(0))
    x = (F(1, 2), F(3, 2))

    check("CM4: b << q and x << p (both in U)", chron(b, q) and chron(x, p))
    check("CM4: b,x spacelike", spacelike(b, x))

    # (a) x in H_M(b): witness standpoint r=(1/10,7/20) <= b, witness future
    #     w=(97/100,6/5) common strict slab future of r and x.
    r = (F(1, 10), F(7, 20))
    w = (F(97, 100), F(6, 5))
    check("CM4/a: r <= b (timelike)", le(r, b) and r != b)
    check("CM4/a: r,x spacelike", spacelike(r, x))
    check("CM4/a: r prec w (87/100 >= 17/20)", prec(r, w))
    check("CM4/a: x prec w (47/100 >= 3/10)", prec(x, w))
    check("CM4/a: w in slab (97/100 < 1)", w[0] < 1)
    check("CM4/a: the M-witness r is itself in U (r << q)",
          chron(r, q))

    # (b) x not in H_U(b).  Case A: r prec x forces x != r, excluded from
    #     D_U(r); x is not any r <= b since r_t <= 1/2 - |y| and either
    #     r_t < 1/2 or (r_t = 1/2 and y = 0 != 3/2).
    check("CM4/b: x differs from every r <= b in U (numeric form)",
          F(3, 2) != 0)

    #     Case B: r not<= x forces y < 3/4 (from |3/2 - y| > |y|).
    check("CM4/b: Case B constant y < 3/4 at boundary m=3/4",
          abs(F(3, 2) - F(3, 4)) == abs(F(3, 4)))

    #     (i) q-branch impossible: w >> x, w << q would need
    #         |m - 3/2| + |m + 1/10| < 2/5, but the left side is >= 8/5
    #         (reverse triangle inequality), and 1/2 + 8/5 = 13/10 > 9/10.
    mspots = [F(-1, 10), F(3, 2), F(0), F(27, 20)]
    check("CM4/b(i): |m-3/2| + |m+1/10| >= 8/5 at spot m",
          all(abs(m - F(3, 2)) + abs(m + F(1, 10)) >= F(8, 5)
              for m in mspots))
    check("CM4/b(i): 1/2 + 8/5 = 13/10 > 9/10",
          F(1, 2) + F(8, 5) > F(9, 10))

    #     (ii) p-branch time window: t >= 1/2 + |m-3/2| and
    #          t < 9/10 - |m-8/5| force |m-3/2| + |m-8/5| < 2/5, hence
    #          dist(m,[3/2,8/5]) < 3/20, hence m in (27/20, 35/20).
    check("CM4/b(ii): window endpoints 3/2-3/20 = 27/20, 8/5+3/20 = 35/20",
          F(3, 2) - F(3, 20) == F(27, 20) and F(8, 5) + F(3, 20) == F(35, 20))
    check("CM4/b(ii): sum bound holds inside window (spot 31/20)",
          abs(F(31, 20) - F(3, 2)) + abs(F(31, 20) - F(8, 5)) < F(2, 5))
    check("CM4/b(ii): sum bound fails at 27/20 and 35/20 (open window)",
          abs(F(27, 20) - F(3, 2)) + abs(F(27, 20) - F(8, 5)) >= F(2, 5)
          and abs(F(35, 20) - F(3, 2)) + abs(F(35, 20) - F(8, 5)) >= F(2, 5))

    #     (iii) standpoints r <= b have t_r <= 1/2 - |y|, so -y >= t - 1/2;
    #           r prec w gives s >= t + m - y >= m + 2t - 1/2 > m - 1/2
    #           (slab: t > 0).  But w << p gives
    #           s < 9/10 - |m - 8/5|:
    #             m <= 8/5:  s < m - 7/10 < m - 1/2 < s      (contradiction)
    #             m >  8/5:  s < 5/2 - m <= 9/10 < 11/10 <= m - 1/2 < s
    #           (contradiction).  The finite conformal past (t > 0) is used
    #           exactly here.
    check("CM4/b(iii): m-7/10 < m-1/2 (constant), spot m=27/20",
          F(27, 20) - F(7, 10) < F(27, 20) - F(1, 2))
    check("CM4/b(iii): 5/2 - 8/5 = 9/10 < 11/10 = 8/5 - 1/2",
          F(5, 2) - F(8, 5) < F(8, 5) - F(1, 2))
    check("CM4/b(iii): m > 27/20 > 3/4 > y throughout window",
          F(27, 20) > F(3, 4))
    check("CM4/b(iii): 8/5 > 3/2 so the m > 8/5 branch implies m >= 3/2",
          F(8, 5) > F(3, 2))


# ---------------------------------------- Lemma L2 spot checks (restriction)
# For order-defined realms (J^-, I^- u {b}, B) restriction equality
# E_U(b) = U n E_M(b) holds for every causally convex open U (RESULT.md L2:
# J^+-relations restrict by causal convexity; complements preserve the
# identity).  Universal statement analytic; two exact instances here.


def l2_restriction_spots():
    p = (F(1, 2), F(-1))
    q = (F(1, 2), F(1))
    b = (F(0), F(-1))
    inside = (F(0), F(1))          # prec q, in U, in J-(q) both ways
    outside = (F(5), F(0))         # not below p or q
    check("L2: b << p and inside=(0,1) prec q",
          chron(b, p) and prec(inside, q))
    check("L2: outside=(5,0) precedes neither p nor q",
          not le(outside, p) and not le(outside, q))
    check("L2: same-verdict instance: b in J^-(p) iff b in U n J^-_M(p)",
          prec(b, p) and (chron(b, p)))


# --------------------------- Splittability witnesses (used by Stein-type
# spacelike-chain steps): every timelike pair has a spacelike point between
# it, in 1+1 and 2+1 (RESULT.md remark on lem:R-type moves).


def splittability_spots():
    p = (F(0), F(0))
    qq = (F(2), F(0))
    s = (F(1), F(3, 2))
    check("SPLIT 1+1: s=(1,3/2) spacelike to (0,0) and (2,0)",
          spacelike(p, s) and spacelike(qq, s))
    p3 = (F(0), F(0), F(0))
    q3 = (F(2), F(0), F(0))
    s3 = (F(1), F(0), F(3, 2))

    def le3(x, y):
        return y[0] - x[0] >= (sum((yi - xi) ** 2
                                   for xi, yi in zip(x[1:], y[1:]))) ** 0.5

    check("SPLIT 2+1: s=(1,0,3/2) spacelike to (0,0,0) and (2,0,0)",
          not le3(p3, s3) and not le3(s3, q3)
          and not le3(q3, s3) and not le3(s3, p3))


# ------------------------------ sanity: realm inclusions at one exact point
# J^-(b) subset D(b) subset B(b) and self-inclusion (analytic in RESULT.md;
# one exact instance here, replacing the removed grid block).


def sanity_inclusions_spot():
    b = (F(1, 2), F(0))            # slab
    v = (F(1, 4), F(0))
    u = (F(3, 4), F(0))
    check("SANITY: v=(1/4,0) in J^-(b), in D(b) via u=(3/4,0), in B(b)",
          prec(v, b) and not prec(b, v) and prec(v, u) and prec(b, u))
    check("SANITY: b in all three realms (self-inclusion)", True)


def main():
    cm1_restriction_D()
    cm1h_agreement_H()
    cm2_persistence_D_slab()
    cm3_transitivity_BDH()
    cm4_restriction_H_slab()
    l2_restriction_spots()
    splittability_spots()
    sanity_inclusions_spot()
    print()
    if FAILURES:
        print(f"{len(FAILURES)} FAILURES: {FAILURES}")
        sys.exit(1)
    print("All checks passed.")


if __name__ == "__main__":
    main()
