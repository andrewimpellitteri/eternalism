"""Independent red-team checker for the 1+1 no-parity census and refinements.

Lane: ontology-null-refinements-review, 30 October 2026.

Written from this lane's own re-derivation. It imports nothing from the
coordinator scripts or from the salvaged partial checker. Every region
operation is an exact operation on whole sign atoms of the null coordinates
u_L = t-x, u_R = t+x, so each containment asserted below is a complete
statement about R^2 once the reduction to region unions is granted. The
reduction itself (boost orbits, wedge saturation, chains) is re-proved
analytically in RESULT.md and corroborated here by exact rational witnesses.

Bit convention under audit (ONE_PLUS_ONE_CENSUS.md ss.1-4): bits are a pair
of per-side triples (n+, w, n-) in bit order (future null, wedge, past null)
with sides (right, left); valid triples satisfy n+ <= w <= n-.
"""

from fractions import Fraction as F
from itertools import product

# ----------------------------------------------------------------------
# A. Exact sign-atom algebra.
# ----------------------------------------------------------------------

NEG, ZERO, POS = "neg", "zero", "pos"
SIGNS = (NEG, ZERO, POS)


def atom_add(a, b):
    """Exact sign atoms of the sum of two whole coordinate rays."""
    if a == ZERO:
        return frozenset((b,))
    if b == ZERO:
        return frozenset((a,))
    if a == b:
        return frozenset((a,))
    return frozenset(SIGNS)          # opposite open rays sum to all of R


def region_of(name):
    """Region -> (u_L atom, u_R atom) per the census ss.1 definitions."""
    return {
        "Im": (NEG, NEG), "Ip": (POS, POS),
        "RW": (NEG, POS), "LW": (POS, NEG),
        "NpR": (ZERO, POS), "NpL": (POS, ZERO),
        "NmR": (NEG, ZERO), "NmL": (ZERO, NEG),
        "Z": (ZERO, ZERO),
    }[name]


REGION_NAMES = ("Im", "Ip", "RW", "LW", "NpR", "NpL", "NmR", "NmL", "Z")
ALL = frozenset(REGION_NAMES)


def region_sum(x, y):
    """Exact Minkowski sum of two regions: (A x B) + (C x D) = (A+C) x (B+D)."""
    (xL, xR), (yL, yR) = region_of(x), region_of(y)
    return regions_of_atoms(frozenset(product(atom_add(xL, yL),
                                              atom_add(xR, yR))))


def regions_of_atoms(atoms):
    return frozenset(n for n in REGION_NAMES if region_of(n) in atoms)


def union_add(u, w):
    out = set()
    for x in u:
        for y in w:
            out |= region_sum(x, y)
    return frozenset(out)


def region_closure(x):
    """cl(A x B): each open ray gains its endpoint 0."""
    aL, aR = region_of(x)
    cL = (aL, ZERO) if aL != ZERO else (ZERO,)
    cR = (aR, ZERO) if aR != ZERO else (ZERO,)
    return regions_of_atoms(frozenset(product(cL, cR)))


def union_closure(u):
    out = set()
    for x in u:
        out |= region_closure(x)
    return frozenset(out)


REFLECT_NAME = {n: regions_of_atoms(frozenset({(region_of(n)[1],
                                                region_of(n)[0])}))
                for n in REGION_NAMES}
REFLECT_NAME = {n: next(iter(s)) for n, s in REFLECT_NAME.items()}


def reflect(u):
    return frozenset(REFLECT_NAME[n] for n in u)


IM = frozenset({"Im"})                       # I^-(0), strict timelike past
JM = frozenset({"Im", "NmR", "NmL", "Z"})    # J^-(0)
JP = frozenset({"Ip", "NpR", "NpL", "Z"})    # J^+(0)

# ----------------------------------------------------------------------
# B. Point-level semantics: validate the sign conventions against (t, x).
# ----------------------------------------------------------------------

GRID_TX = [(F(a), F(b)) for a in (-3, -1, 0, 1, 3) for b in (-3, -1, 0, 1, 3)]
EXTRA_TX = [(F(1), F(2)), (F(2), F(1)), (F(-1), F(-2)), (F(-2), F(-1)),
            (F(1), F(-2)), (F(-1), F(2)), (F(5), F(3)), (F(-5), F(-3))]


def to_null(p):
    t, x = p
    return (t - x, t + x)


def strictly_timelike_future(d, x):
    dt, dx = x[0] - d[0], x[1] - d[1]
    return dt > 0 and dt * dt > dx * dx


def causal_future(d, x):
    dt, dx = x[0] - d[0], x[1] - d[1]
    return dt >= 0 and dt * dt >= dx * dx


def check_conventions():
    # timelike/causal order equals the componentwise null-coordinate order.
    for d in GRID_TX + EXTRA_TX:
        for x in GRID_TX + EXTRA_TX:
            dl, dr = to_null(x)[0] - to_null(d)[0], to_null(x)[1] - to_null(d)[1]
            assert strictly_timelike_future(d, x) == (dl > 0 and dr > 0)
            assert causal_future(d, x) == (dl >= 0 and dr >= 0)
    # Named null regions and wedges match their (t, x) descriptions.
    samples = {"NpR": (F(1), F(1)), "NpL": (F(2), F(-2)),
               "NmR": (F(-1), F(1)), "NmL": (F(-2), F(-2)),
               "RW": (F(0), F(2)), "LW": (F(0), F(-2)),
               "Im": (F(-3), F(0)), "Ip": (F(3), F(0)), "Z": (F(0), F(0))}
    for name, p in samples.items():
        uL, uR = to_null(p)
        t, x = p
        want = {"NpR": uL == 0 and uR > 0, "NpL": uR == 0 and uL > 0,
                "NmR": uR == 0 and uL < 0, "NmL": uL == 0 and uR < 0,
                "RW": uL < 0 < uR, "LW": uR < 0 < uL,
                "Im": uL < 0 and uR < 0, "Ip": uL > 0 and uR > 0,
                "Z": uL == 0 and uR == 0}[name]
        assert want, (name, p)
        if name in ("NpR", "RW"):            # right-going: x > 0 side
            assert x > 0 or (name == "RW" and x > abs(t))
        if name in ("NpL", "LW"):            # left-going: x < 0 side
            assert x < 0 or (name == "LW" and -x > abs(t))
        if name in ("NpR", "NpL"):           # future null: t > 0
            assert t > 0
        if name in ("NmR", "NmL"):           # past null: t < 0
            assert t < 0
    # Partition: every grid point lands in exactly one region, consistently.
    for p in GRID_TX + EXTRA_TX:
        uL, uR = to_null(p)
        hits = [n for n in REGION_NAMES
                if _atom_contains(region_of(n)[0], uL)
                and _atom_contains(region_of(n)[1], uR)]
        assert len(hits) == 1, (p, hits)
    # Boost (cosh, sinh) = (5/3, 4/3): u_L -> u_L/3, u_R -> 3 u_R, regions fixed.
    for p in GRID_TX + EXTRA_TX:
        t, x = p
        bp = ((F(5) * t + F(4) * x) / 3, (F(4) * t + F(5) * x) / 3)
        assert to_null(bp)[0] * 3 == to_null(p)[0]
        assert to_null(bp)[1] == 3 * to_null(p)[1]
    print("PASS B: sign conventions exact - null order = timelike/causal"
          " order; named regions match (t,x) descriptions; boost rescales"
          " (u_L, u_R) -> (u_L/3, 3 u_R); partition holds on exact points")


def _atom_contains(atom, v):
    if atom == NEG:
        return v < 0
    if atom == POS:
        return v > 0
    return v == 0


# ----------------------------------------------------------------------
# C. Reduction witnesses (saturation, chains, cross-side).
# ----------------------------------------------------------------------

def check_reduction():
    # Wedge saturation: h > max(a/A, B/b) maps (-a, b) above any (-A, B).
    for a, b, A, B in product((F(1), F(2), F(7)), repeat=4):
        h = max(a / A, B / b) + F(1)
        assert -A < -a / h and B < b * h          # (-A,B) << (-a/h, bh)
    # Mirror direction for LW: h < min(a/A, B/b).
    for a, b, A, B in product((F(1), F(2), F(7)), repeat=4):
        h = min(a / A, B / b) / 2
        assert a / h > A and -b * h > -B          # (A,-B) << (a/h, -bh)
    # Exact chains: past of each free region stays on its own side.
    assert region_sum("NpR", "Im") == {"Im", "NmR", "RW"}
    assert region_sum("RW", "Im") == {"Im", "NmR", "RW"}
    assert region_sum("NmR", "Im") == {"Im"}
    assert region_sum("NpL", "Im") == {"Im", "NmL", "LW"}
    assert region_sum("LW", "Im") == {"Im", "NmL", "LW"}
    assert region_sum("NmL", "Im") == {"Im"}
    right = {"NpR", "RW", "NmR"}
    left = {"NpL", "LW", "NmL"}
    for x in right:
        assert not region_sum(x, "Im") & left
        assert not region_sum(x, "Im") & {"NpR"}
    for x in left:
        assert not region_sum(x, "Im") & right
        assert not region_sum(x, "Im") & {"NpL"}
    # Both wedges sum to the whole plane (exact).
    assert region_sum("RW", "LW") == ALL
    print("PASS C: saturation inequalities exact; chains NpR=>RW=>NmR and"
          " NpL=>LW=>NmL with no cross-side past and none to the same future"
          " ray; RW + LW = R^2 exactly")


# ----------------------------------------------------------------------
# D. Census and refinements on the exact region algebra.
# ----------------------------------------------------------------------

TRIPLES = [t for t in product((0, 1), repeat=3) if t[0] <= t[1] <= t[2]]
BITS = [(r, l) for r in TRIPLES for l in TRIPLES]


def bits_to_u(bits):
    u = {"Im", "Z"}
    names = (("NpR", "RW", "NmR"), ("NpL", "LW", "NmL"))
    for side in (0, 1):
        for bit, name in zip(bits[side], names[side]):
            if bit:
                u.add(name)
    return frozenset(u)


def main():
    check_conventions()
    check_reduction()

    # Census: exactly 16 of the 64 unions are past sets; = monotone bits.
    all64 = [bits_to_u((m[0:3], m[3:6])) for m in product((0, 1), repeat=6)]
    assert len(all64) == 64 and len(set(all64)) == 64
    past_closed = [u for u in all64 if union_add(u, IM) <= u]
    monotone = [u for u in all64
                if all(t in TRIPLES for t in
                       [tuple(int(n in u) for n in ("NpR", "RW", "NmR")),
                        tuple(int(n in u) for n in ("NpL", "LW", "NmL"))])]
    assert past_closed == monotone and len(past_closed) == 16
    assert len(set(past_closed)) == 16
    valid = past_closed

    ident = {
        "I": bits_to_u(((0, 0, 0), (0, 0, 0))),
        "J": bits_to_u(((0, 0, 1), (0, 0, 1))),
        "B": bits_to_u(((0, 1, 1), (0, 1, 1))),
        "C": bits_to_u(((1, 1, 1), (1, 1, 1))),
        "fifth": bits_to_u(((0, 0, 0), (0, 1, 1))),
        "sixth": bits_to_u(((0, 1, 1), (0, 0, 0))),
    }
    assert ident["I"] == {"Im", "Z"}
    assert ident["J"] == JM
    assert ident["B"] == ALL - {"Ip", "NpR", "NpL"}
    assert ident["C"] == ALL - {"Ip"}
    assert ident["fifth"] == {"Im", "Z", "LW", "NmL"}   # {u_R<0} u {0}
    assert ident["sixth"] == {"Im", "Z", "RW", "NmR"}   # {u_L<0} u {0}
    half_l = frozenset(n for n in REGION_NAMES if region_of(n)[0] != POS)
    half_r = frozenset(n for n in REGION_NAMES if region_of(n)[1] != POS)
    assert half_l == bits_to_u(((1, 1, 1), (0, 0, 1)))   # {u_L <= 0}
    assert half_r == bits_to_u(((0, 0, 1), (1, 1, 1)))   # {u_R <= 0}
    print("PASS D1: 16/64 unions are past sets, exactly the monotone triples;"
          " I, J, B, C, fifth, sixth and both half-spaces identified exactly")

    # Refinement rows.
    pc = [u for u in valid if union_add(u, JM) <= u]
    fc = [u for u in valid if not (u & (JP - {"Z"}))]
    closed = [u for u in valid if union_closure(u) <= u]
    symmetric = [u for u in valid if reflect(u) == u]
    orbits = {tuple(sorted((tuple(sorted(u)), tuple(sorted(reflect(u))))))
              for u in valid}
    additive = [u for u in valid if union_add(u, u) <= u]

    assert len(pc) == 9 and all({"NmR", "NmL"} <= u for u in pc)
    assert len(fc) == 9 and all("NpR" not in u and "NpL" not in u for u in fc)
    both = [u for u in pc if u in fc]
    assert len(both) == 4 and set(both) == {
        ident["J"], bits_to_u(((0, 1, 1), (0, 0, 1))),
        bits_to_u(((0, 0, 1), (0, 1, 1))), ident["B"]}
    assert len(closed) == 4
    assert set(closed) == {ident["J"], ident["C"], half_l, half_r}
    assert [u for u in closed if u in fc] == [ident["J"]]
    assert len(symmetric) == 4
    assert set(symmetric) == {ident[k] for k in ("I", "J", "B", "C")}
    assert len(set(orbits)) == 10
    print("PASS D2: P_c 9 (iff both past-null bits); F_c 9 (iff no future-null"
          " bit); both 4; closed 4 = {J, C, two null half-spaces}; closed+F_c"
          " 1 = J; reflection invariant 4; mirror quotient 10 classes")

    # Transitivity: additive iff not both wedges; 12 cases, both directions.
    assert len(additive) == 12
    assert set(additive) == {u for u in valid if not {"RW", "LW"} <= u}
    for u in additive:
        assert union_add(u, u) <= u                  # sufficiency, exact
    for u in valid:
        if {"RW", "LW"} <= u:
            assert ALL <= union_add(u, u)            # forces I+ into P
    half_l_closed = union_closure(half_l) == half_l
    half_r_closed = union_closure(half_r) == half_r
    half_l_add = union_add(half_l, half_l) == half_l
    half_r_add = union_add(half_r, half_r) == half_r
    assert half_l_closed and half_r_closed and half_l_add and half_r_add
    print("PASS D3: transitive = 12, exactly the rules without both wedges;"
          " both-wedge rules sum to the whole plane (violating F_t); the two"
          " closed null half-spaces are closed and additive analytic cases")

    # Transitivity combination rows.
    trans = additive
    assert set(trans) & set(closed) == {ident["J"], half_l, half_r}
    tp = [u for u in trans if u in pc]
    tf = [u for u in trans if u in fc]
    tpf = [u for u in trans if u in pc and u in fc]
    assert len(tp) == 5
    assert set(tp) == {ident["J"], bits_to_u(((0, 1, 1), (0, 0, 1))),
                       bits_to_u(((0, 0, 1), (0, 1, 1))), half_l, half_r}
    assert len(tf) == 8
    assert set(tf) == {u for u in fc if u != ident["B"]}
    assert len(tpf) == 3
    assert set(tpf) == {ident["J"], bits_to_u(((0, 1, 1), (0, 0, 1))),
                        bits_to_u(((0, 0, 1), (0, 1, 1)))}
    print("PASS D4: transitive+closed 3; transitive+P_c 5; transitive+F_c 8;"
          " transitive+P_c+F_c 3 - every census ss.4 refinement count exact")

    # Additive-semigroup D-forms for the eight one-wedge transitive rules.
    open_l = frozenset(n for n in REGION_NAMES if region_of(n)[0] == NEG)
    open_r = frozenset(n for n in REGION_NAMES if region_of(n)[1] == NEG)
    assert open_l == {"Im", "RW", "NmR"} and open_r == {"Im", "LW", "NmL"}
    for plus, minus in product((0, 1), repeat=2):
        # RW alone: right (0/1, 1, 1), left (0, 0, minus-bit).
        u = bits_to_u(((1 if plus else 0, 1, 1), (0, 0, minus)))
        assert union_add(u, u) <= u and open_l <= u
        # LW alone: the mirror.
        v = bits_to_u(((0, 0, minus), (1 if plus else 0, 1, 1)))
        assert union_add(v, v) <= v and open_r <= v
    print("PASS D5: all eight one-wedge rules have the exact form"
          " {u_L<0} u ({0} x D) with D in {{0}, [0,inf), (-inf,0], R}, each"
          " D additive - the coordinator's semigroup derivation certifies")

    # Point-level corroboration at the assignment level (all 16 rules):
    # S, F_t, boost invariance, P_t everywhere; P_c for the 9; E-transitivity
    # spot pairs for one asymmetric transitive and one failing rule.
    pts = [to_null(p) for p in GRID_TX + EXTRA_TX]

    def in_u(u, q):
        hits = [n for n in REGION_NAMES
                if _atom_contains(region_of(n)[0], q[0])
                and _atom_contains(region_of(n)[1], q[1])]
        return hits[0] in u

    for u in valid:
        for q in pts:
            assert in_u(u, (F(0), F(0)))
            if q[0] > 0 and q[1] > 0:
                assert not in_u(u, q)
            for h in (F(3), F(1, 3)):
                assert in_u(u, (q[0] / h, q[1] * h)) == in_u(u, q)
        for d in pts:
            if not in_u(u, d):
                continue
            for w in pts:
                if w[0] - d[0] < 0 and w[1] - d[1] < 0:
                    assert in_u(u, w), (sorted(u), w, d)
        if u in pc:
            for d in pts:
                if not in_u(u, d):
                    continue
                for w in pts:
                    if w[0] - d[0] <= 0 and w[1] - d[1] <= 0:
                        assert in_u(u, w)
    # E-level transitivity: x in E_y, y in E_z => x in E_z, i.e. P + P subset P;
    # verified exactly above; spot-check E-form on grid standpoints.
    for u, should in ((bits_to_u(((0, 0, 1), (0, 1, 1))), True),
                      (ident["B"], False)):
        ok = True
        for b in GRID_TX:
            for c in GRID_TX:
                for x in GRID_TX:
                    if (in_u(u, to_null((x[0] - b[0], x[1] - b[1])))
                            and in_u(u, to_null((b[0] - c[0], b[1] - c[1])))
                            and not in_u(u, to_null((x[0] - c[0], x[1] - c[1])))):
                        ok = False
        assert ok == should, (sorted(u), ok, should)
    print("PASS D6: point-level corroboration on exact rationals for all 16"
          " rules (S, F_t, boost invariance, P_t; P_c for the 9); E-level"
          " transitivity holds for J+LW and fails for B on explicit triples")

    print("SUMMARY: census and every refinement row re-verified independently;"
          " no counterexample found. Exactness: all operations are on whole"
          " sign atoms, so each assertion is a statement about R^2 given the"
          " analytically proved region-union reduction.")


if __name__ == "__main__":
    main()
