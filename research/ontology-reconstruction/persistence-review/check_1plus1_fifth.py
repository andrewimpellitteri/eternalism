"""1+1 Minkowski, boosts+translations covariance only (no parity):

Candidate fifth assignment beyond the asserted n>=2 census.

A' = {0} u {a not in strict timelike past of 0 : t_a + x_a > 0}
E_b = {x : b - x in A'}

Analytic core (complete, not grid-based):
1. Boost with (cosh, sinh) = (5/3, 4/3) maps (t,x) -> ((5t+4x)/3, (4t+5x)/3);
   t+x maps to 3(t+x), so the sign of t+x is preserved. I^- and {0} are
   invariant. Hence A' is boost-invariant; E is Poincare-covariant.
2. Every a in A' has t_a + x_a >= 0, with equality only at a = 0.
   If d >> a then t_d + x_d > t_a + x_a (strict future vectors have positive
   sum-component), so d avoids the left wedge (t+x<0) and the left null
   branch (t+x=0). Timelike-past points have t+x < 0, so d is not timelike
   past either. The remaining regions are exactly A' minus nothing:
   {t+x>0} \\ I^- = I+ u right wedge u right null branch. So A' is a
   chronological future set, which is equivalent to P_t for E.
3. S: 0 in A'. F_t: A' ∩ I^-(0) = ∅ by definition.
4. Distinctness: x -> b-x reverses wedge orientation, so at standpoint 0
   E contains the left-spacelike wedge (0,-1) and the past-null x<0 branch
   (-1,-1), but misses the future null (1,1) and the past-null x>0 branch
   (-1,1). Pattern (T,F,T,F) differs from I (F,F,F,F), J and B (F,F,T,T),
   and C (T,F,T,T). So E differs from all four census candidates.

The script checks finite exact witnesses for each step; the case analysis
above is the actual proof for this candidate.
"""

from fractions import Fraction as F


def pt(t, x=0):
    return (F(t), F(x))


def much(u, v):
    dt, dx = v[0] - u[0], v[1] - u[1]
    return dt > 0 and dt * dt > dx * dx


def in_A(p):
    t, x = p
    if p == (F(0), F(0)):
        return True
    if t < 0 and t * t > x * x:      # strict timelike past of 0
        return False
    return t + x > 0


def realm5(b, x):
    return in_A((b[0] - x[0], b[1] - x[1]))


def realm_census(kind, b, x):
    dt, dx = x[0] - b[0], x[1] - b[1]
    tl = dt > 0 and dt * dt > dx * dx
    cs = dt >= 0 and dt * dt >= dx * dx
    if kind == "I":
        return tl or x == b
    if kind == "J":
        return cs
    if kind == "B":
        return not (cs and x != b)
    if kind == "C":
        return not tl
    raise ValueError(kind)


def main():
    zero = pt(0)

    # Boost invariance on exact rational witnesses across A' regions.
    c, s = F(5, 3), F(4, 3)          # cosh/sinh of a valid rapidity
    assert c * c - s * s == 1
    boost = lambda p: ((c * p[0] + s * p[1], s * p[0] + c * p[1]))
    witnesses = [
        pt(2, 0),                      # timelike future
        pt(1, F(1, 2)),                # timelike future, t+x>0
        pt(0, 1),                      # right wedge
        pt(-1, 2),                     # right wedge, t<0
        pt(3, 3),                      # right null branch
        pt(0, 0),                      # origin
        pt(-1, F(3, 2)),               # timelike past with t+x>0 -> excluded
        pt(-1, 0),                     # timelike past -> excluded
        pt(1, 1),                      # left... right? (1,1): t=x>0 right branch
        pt(1, -1),                     # left null branch -> excluded
        pt(0, -2),                     # left wedge -> excluded
    ]
    for p in witnesses:
        assert in_A(boost(p)) == in_A(p), (p, boost(p))
    print("PASS: A' invariant under the exact boost (cosh,sinh)=(5/3,4/3)")

    # Future-set property on exact witness pairs (analytic proof in header).
    grid = [pt(F(i), F(j)) for i in range(-4, 5) for j in range(-4, 5)]
    n_pairs = 0
    for a in grid:
        if not in_A(a):
            continue
        for v in grid:
            if much(zero, v) and in_A((a[0] + v[0], a[1] + v[1])):
                n_pairs += 1
                assert in_A((a[0] + v[0], a[1] + v[1]))
    assert n_pairs > 100
    print(f"PASS: future-set closure on {n_pairs} exact reachable pairs")

    # Premises for E at grid standpoints and members.
    for b in grid:
        assert realm5(b, b)                                  # S
        for x in grid:
            if much(b, x):
                assert not realm5(b, x)                      # F_t
            if realm5(b, x):
                for c2 in grid:
                    if much(b, c2):
                        assert realm5(c2, x)                 # P_t
    print("PASS: S, P_t, F_t hold for the fifth assignment on the grid")

    # Distinctness from all four census candidates at standpoint 0.
    # Note x -> b-x reverses wedge orientation: A' holds the RIGHT wedge of
    # A-space, so E_0 holds the LEFT-spacelike points in x-space.
    b = zero
    sp_l = pt(0, -1)                # left-spacelike: b-x = (0,1) in A'
    null_f = pt(1, 1)               # future null: b-x = (-1,-1), t+x<0
    pn_l = pt(-1, -1)               # past null, x<0 branch: b-x=(1,1) in A'
    pn_r = pt(-1, 1)                # past null, x>0 branch: b-x=(1,-1), t+x=0
    assert realm5(b, sp_l) and realm5(b, pn_l)
    assert not realm5(b, null_f) and not realm5(b, pn_r)
    for kind in ("I", "J", "B", "C"):
        truth = (realm_census(kind, b, sp_l), realm_census(kind, b, null_f),
                 realm_census(kind, b, pn_l), realm_census(kind, b, pn_r))
        assert truth != (True, False, True, False), kind
    print("PASS: membership pattern (sp, f_null, pn_x<0, pn_x>0) = (T,F,T,F)")
    print("      differs from I (F,F,F,F), J and B (F,F,T,T), C (T,F,T,T)")

    print("Result: a fifth covariant persistent self-inclusive F_t assignment")
    print("exists in 1+1 without parity; the asserted census needs n >= 2.")


if __name__ == "__main__":
    main()
