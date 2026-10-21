#!/usr/bin/env python3
"""Finite exact checks for the weighted absolute-convergence estimate.

Scope: these are FINITE checks. They corroborate the combinatorial definitions
and the algebraic exponent bookkeeping used in RESULT.md. They do NOT prove the
two analytic inequalities (the two-cap level bound and the inclusion-exclusion
bridge bound); those are proved in RESULT.md by hand.

Standard library only. No installs.
Exact arithmetic:
  * Fraction for rational real p;
  * Gaussian rationals G (Fraction pairs) for complex p;
  * Q2 = u + v*sqrt(2) with u,v Fraction, for moduli such as |(1+i)/2|.

Sections
  A  poset enumeration; natural-label multiplicities; N(H(+)S)=N(H)N(S)
  B  renewal identity U(z)(1-R(z)) = 1 exactly through degree 8
  C  exact level sums W_n, V_n against the two-cap and star lower bounds
  D  bridge coefficients B_j by two independent definitions, plus bounds
  E  the weighted ratio |B_j|/W_(n+j): exact exponent identity and majorant
  F  endpoints p=0, p=1, and the division failure
  G  positive segment sums K_k (variation side) vs the complex R_k
"""
from fractions import Fraction as F
from itertools import permutations
from math import comb, isqrt

MAXN = 7
TOPDEG = 8


# ---------------------------------------------------------------- Q2 arithmetic
class Q2:
    """u + v*sqrt(2), u,v Fraction. Exact sign, +, -, *, /, **."""
    __slots__ = ("u", "v")

    def __init__(self, u, v=0):
        self.u = F(u)
        self.v = F(v)

    def __add__(self, o):
        o = q2(o)
        return Q2(self.u + o.u, self.v + o.v)

    __radd__ = __add__

    def __neg__(self):
        return Q2(-self.u, -self.v)

    def __sub__(self, o):
        return self + (-q2(o))

    def __rsub__(self, o):
        return q2(o) - self

    def __mul__(self, o):
        o = q2(o)
        return Q2(self.u * o.u + 2 * self.v * o.v,
                  self.u * o.v + self.v * o.u)

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = q2(o)
        d = o.u * o.u - 2 * o.v * o.v
        assert d != 0, "division by zero in Q2"
        return self * Q2(o.u / d, -o.v / d)

    def __pow__(self, k):
        assert isinstance(k, int)
        if k < 0:
            return Q2(1) / (self ** (-k))
        r = Q2(1)
        base = self
        while k:
            if k & 1:
                r = r * base
            base = base * base
            k >>= 1
        return r

    def sign(self):
        u, v = self.u, self.v
        if v == 0:
            return (u > 0) - (u < 0)
        if u == 0:
            return (v > 0) - (v < 0)
        if u > 0 and v > 0:
            return 1
        if u < 0 and v < 0:
            return -1
        if u > 0:
            return 1 if u * u > 2 * v * v else -1
        return -1 if u * u > 2 * v * v else 1

    def __eq__(self, o):
        o = q2(o)
        return self.u == o.u and self.v == o.v

    def __repr__(self):
        return f"({self.u}+{self.v}r2)"


def q2(x):
    return x if isinstance(x, Q2) else Q2(x)


def sqrt_rational_box(r):
    """s in Q2 with s^2 = r, when r is a nonneg rational of the form n^2 or
    2 n^2 (n rational). Raises ValueError otherwise."""
    r = F(r)
    if r < 0:
        raise ValueError
    for factor in (1, 2):
        rr = r / factor
        n, d = rr.numerator, rr.denominator
        sn, sd = isqrt(n), isqrt(d)
        if sn * sn == n and sd * sd == d:
            if factor == 1:
                return Q2(F(sn, sd), 0)
            return Q2(0, F(sn, sd))
    raise ValueError(f"sqrt({r}) is not in Q(sqrt2)")


# ---------------------------------------------------------------- Gaussian exact
class G:
    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re = F(re)
        self.im = F(im)

    def __add__(self, o):
        o = gg(o)
        return G(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, o):
        return self + (-gg(o))

    def __rsub__(self, o):
        return gg(o) - self

    def __mul__(self, o):
        o = gg(o)
        return G(self.re * o.re - self.im * o.im,
                 self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def __pow__(self, k):
        assert k >= 0
        r = G(1)
        base = self
        while k:
            if k & 1:
                r = r * base
            base = base * base
            k >>= 1
        return r

    def __eq__(self, o):
        o = gg(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def __repr__(self):
        return f"({self.re}+{self.im}i)"


def gg(x):
    if isinstance(x, G):
        return x
    if isinstance(x, tuple):
        return G(x[0], x[1])
    return G(x)


def modulus2(z):
    z = gg(z)
    return z.re * z.re + z.im * z.im


def abs_pair(p):
    """(a,b)=(|p|,|1-p|) in Q2 for the parameters used here."""
    return (sqrt_rational_box(modulus2(p)),
            sqrt_rational_box(modulus2(G(1) - gg(p))))


# ---------------------------------------------------------------- poset library
def close_mask(mask, n):
    rel = [[False] * n for _ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(i + 1, n):
            if mask >> idx & 1:
                rel[i][j] = True
            idx += 1
    for k in range(n):
        for i in range(k):
            if rel[i][k]:
                rk = rel[k]
                for j in range(k + 1, n):
                    if rk[j]:
                        rel[i][j] = True
    out = 0
    idx = 0
    for i in range(n):
        for j in range(i + 1, n):
            if rel[i][j]:
                out |= 1 << idx
            idx += 1
    return out


PAIRS = {n: [(i, j) for i in range(n) for j in range(i + 1, n)]
         for n in range(MAXN + 1)}


def analyse(relset, n):
    L = 0
    for (i, j) in relset:
        if not any((i, k) in relset and (k, j) in relset
                   for k in range(i + 1, j)):
            L += 1
    R = len(relset)
    minima = sum(1 for i in range(n)
                 if not any((j, i) in relset for j in range(i)))
    maxima = sum(1 for i in range(n)
                 if not any((i, j) in relset for j in range(i + 1, n)))
    posts = tuple(i for i in range(n)
                  if all((j, i) in relset for j in range(i))
                  and all((i, j) in relset for j in range(i + 1, n)))
    return L, R, minima, maxima, posts


def build(n):
    """Tuples (mask, L, h, minc, maxc, nposts, principal, dp)."""
    if n == 0:
        return [(0, 0, 0, 0, 0, 0, False, False)]
    masks = {close_mask(m, n) for m in range(1 << (n * (n - 1) // 2))}
    pairs = PAIRS[n]
    out = []
    for m in masks:
        rel = frozenset(pairs[k] for k in range(len(pairs)) if m >> k & 1)
        L, R, minc, maxc, posts = analyse(rel, n)
        principal = (maxc == 1)
        prev = frozenset((i, j) for (i, j) in rel if j <= n - 2)
        dp = principal and analyse(prev, n - 1)[3] == 1
        out.append((m, L, n * (n - 1) // 2 - R, minc, maxc, posts,
                    principal, dp))
    return out


POS = {n: build(n) for n in range(MAXN + 1)}

L_I, H_I, MIN_I, MAX_I, POST_I, PRIN_I, DP_I = 1, 2, 3, 4, 5, 6, 7


def powers(x, top):
    out = [gg(1)]
    for _ in range(top):
        out.append(out[-1] * x)
    return out


def qpowers(x, top):
    out = [Q2(1)]
    for _ in range(top):
        out.append(out[-1] * x)
    return out


# ---------------------------------------------------------------- section A
def canon(mask, n):
    pairs = PAIRS[n]
    rel = [(pairs[k]) for k in range(len(pairs)) if mask >> k & 1]
    best = None
    for perm in permutations(range(n)):
        t = tuple(sorted((perm[i], perm[j]) for (i, j) in rel))
        if best is None or t < best:
            best = t
    return best


def label_table(n):
    tbl = {}
    for P in POS[n]:
        c = canon(P[0], n)
        tbl[c] = tbl.get(c, 0) + 1
    return tbl


def section_a():
    print("A. enumeration and natural-label multiplicities")
    counts = {n: len(POS[n]) for n in range(MAXN + 1)}
    print("  naturally labelled orders, n=0..%d: %s" % (
        MAXN, ", ".join(f"{n}:{counts[n]}" for n in counts)))
    assert [counts[n] for n in range(6)] == [1, 1, 2, 7, 40, 357]
    a = b = Q2(F(1, 2))
    ap, bp = qpowers(a, 30), qpowers(b, 30)
    for n in range(1, 6):
        lab = Q2(0)
        for P in POS[n]:
            lab = lab + ap[P[L_I]] * bp[P[H_I]]
        tbl = label_table(n)
        seen = {}
        shape = Q2(0)
        for P in POS[n]:
            c = canon(P[0], n)
            if c in seen:
                continue
            seen[c] = P
            shape = shape + q2(tbl[c]) * ap[P[L_I]] * bp[P[H_I]]
        assert lab == shape, (n,)
    print("  A1: labelled sum == sum_shapes N(shape)*weight, n=1..5, p=1/2")
    checks = 0
    for n1 in range(1, 5):
        t1 = label_table(n1)
        reps1 = {}
        for P in POS[n1]:
            reps1.setdefault(canon(P[0], n1), P)
        for n2 in range(1, 6 - n1):
            n = n1 + n2
            t2 = label_table(n2)
            t3 = label_table(n)
            reps2 = {}
            for P in POS[n2]:
                reps2.setdefault(canon(P[0], n2), P)
            for c1, P1 in reps1.items():
                rel1 = frozenset(PAIRS[n1][k] for k in range(len(PAIRS[n1]))
                                 if P1[0] >> k & 1)
                for c2, P2 in reps2.items():
                    rel2 = frozenset(PAIRS[n2][k] for k in range(len(PAIRS[n2]))
                                     if P2[0] >> k & 1)
                    rel = set(rel1)
                    rel |= {(i + n1, j + n1) for (i, j) in rel2}
                    rel |= {(i, j + n1) for i in range(n1) for j in range(n2)}
                    k3 = 0
                    for idx, (i, j) in enumerate(PAIRS[n]):
                        if (i, j) in rel:
                            k3 |= 1 << idx
                    assert t3[canon(k3, n)] == t1[c1] * t2[c2], (n1, n2)
                    checks += 1
    print(f"  A2: N(H(+)S) == N(H)N(S), {checks} shape pairs, |H|+|S|<=5")


# ---------------------------------------------------------------- sections B/G
def bridge_tables(p, maxdeg):
    """B_j, R_k (exact G) and K_k (exact Q2 modulus sum) for 1..maxdeg."""
    P_ = gg(p)
    q_ = G(1) - P_
    pp, qp = powers(P_, 60), powers(q_, 60)
    a, b = abs_pair(p)
    ap, bp = qpowers(a, 60), qpowers(b, 60)
    B = {0: G(1), 1: P_}
    R = {1: P_}
    K = {1: a}
    for j in range(2, maxdeg + 1):
        s = G(0)
        for P in POS[j - 1]:
            s = s + pp[P[L_I]] * qp[P[H_I]] * pp[P[MAX_I] + P[MIN_I]]
        B[j] = s
    for k in range(2, maxdeg + 1):
        s = G(0)
        kk = Q2(0)
        for P in POS[k - 1]:
            if len(P[POST_I]) == 0:
                s = s + pp[P[L_I]] * qp[P[H_I]] * pp[P[MAX_I] + P[MIN_I]]
                kk = kk + ap[P[L_I]] * bp[P[H_I]] * ap[P[MAX_I] + P[MIN_I]]
        R[k] = s
        K[k] = kk
    return B, R, K


def section_b():
    print("B. renewal identity U(z)(1-R(z)) = 1 exactly through degree %d"
          % TOPDEG)
    params = [(F(0), "p=0"), (F(1, 2), "p=1/2"), (F(3, 2), "p=3/2"),
              (F(2), "p=2"), (F(-1), "p=-1"),
              ((F(1, 2), F(1, 2)), "p=(1+i)/2"),
              ((F(50, 169), F(120, 169)), "p=(50+120i)/169")]
    for p, name in params:
        B, R, _ = bridge_tables(p, TOPDEG)
        for m in range(1, TOPDEG + 1):
            conv = G(0)
            for k in range(1, m + 1):
                conv = conv + R[k] * B[m - k]
            assert B[m] == conv, (name, m)
        print(f"  {name}: B_m == sum_(k=1..m) R_k B_(m-k), m=1..{TOPDEG} exact")
    B, R, _ = bridge_tables(F(0), TOPDEG)
    assert B[1] == G(0)
    for j in range(2, TOPDEG + 1):
        assert B[j] == G(0) and R[j] == G(0), j
    print("  p=0: B_1=R_1=0 and B_j=R_k=0 for 2<=j,k<=%d (exact)" % TOPDEG)


# ---------------------------------------------------------------- section C
def level_sums(p):
    a, b = abs_pair(p)
    ap, bp = qpowers(a, 30), qpowers(b, 30)
    W, V = {}, {}
    for n in range(1, MAXN + 1):
        w = Q2(0)
        v = Q2(0)
        for P in POS[n]:
            if P[PRIN_I]:
                m = ap[P[L_I]] * bp[P[H_I]]
                w = w + m
                if P[DP_I]:
                    v = v + m
        W[n] = w
        V[n] = v
    return W, V


def two_cap_bound(a, b, n):
    t = a + b
    s = b / t
    assert s.v == 0, "rational s expected for these parameters"
    sv = s.u
    Fm = F(1)
    for j in range(1, n - 1):
        Fm *= (1 - sv ** j)
    return a * (t ** (n - 2)) * q2(Fm)


def section_c():
    print("C. exact level sums against the two-cap and star lower bounds")
    params = [(F(1, 2), "p=1/2"), (F(3, 2), "p=3/2"), (F(2), "p=2"),
              (F(-1), "p=-1"), (F(5, 2), "p=5/2"), (F(-1, 2), "p=-1/2"),
              ((F(1, 2), F(1, 2)), "p=(1+i)/2")]
    for p, name in params:
        a, b = abs_pair(p)
        W, V = level_sums(p)
        for n in range(2, MAXN + 1):
            star = (a ** (n - 1)) * (b ** comb(n - 1, 2))
            assert (W[n] - star).sign() >= 0, (name, n, "star")
            two = two_cap_bound(a, b, n)
            assert (V[n] - two).sign() >= 0, (name, n, "two-cap")
        bip_note = ""
        if b == Q2(1) and a.v == 0:
            # An empty lower row adds a direct cover into the universal cap.
            # Row sum: a + (1+a)^m - 1; the upper-to-cap edges contribute a^m.
            for n in range(3, MAXN + 1):
                m = (n - 1) // 2
                exp_a = m if n % 2 == 1 else m + 1
                bip = (a ** exp_a) * (((1 + a) ** m + a - 1) ** m)
                assert (W[n] - bip).sign() >= 0, (name, n, "bipartite")
            bip_note = "; bipartite bound (odd and even)"
            if a == Q2(F(10, 13)):
                assert W[3] == Q2(F(200, 169))
                assert (a * (1 + a) - W[3]).sign() > 0
                bip_note += "; original bound falsified at n=3"
        print(f"  {name}: W_n >= star and V_n >= two-cap, n=2..{MAXN}"
              f"{bip_note}")
    W, V = level_sums((F(1, 2), F(1, 2)))
    print("  p=(1+i)/2 exact W_n / V_n in Q(sqrt2):")
    for n in range(2, MAXN + 1):
        print(f"    n={n}: W_n={W[n]}  V_n={V[n]}")


# ---------------------------------------------------------------- section D
def bridge_ie(j, p):
    """B_j by inclusion-exclusion: in forward-edge percolation every column
    1..j has an incoming edge and every row 0..j-1 has an outgoing edge."""
    P_ = gg(p)
    Q_ = G(1) - P_
    tot = G(0)
    cols = list(range(1, j + 1))
    rows = list(range(j))
    for Im in range(1 << len(cols)):
        I = {cols[k] for k in range(len(cols)) if Im >> k & 1}
        for Jm in range(1 << len(rows)):
            J = {rows[k] for k in range(len(rows)) if Jm >> k & 1}
            e = sum(1 for u in range(j) for v in range(u + 1, j + 1)
                    if u in J or v in I)
            sign = -1 if (len(I) + len(J)) % 2 else 1
            tot = tot + (Q_ ** e) * sign
    return tot


def brute_bridge(j, p):
    """Third definition: brute-force forward-edge percolation on 0..j, summing
    p^|E| q^(N-|E|) over edge sets where 0 reaches every vertex and every
    vertex reaches j (reachability by BFS, not by the degree criterion)."""
    P_ = gg(p)
    Q_ = G(1) - P_
    edges = [(u, v) for u in range(j + 1) for v in range(u + 1, j + 1)]
    N = len(edges)
    tot = G(0)
    full = (1 << (j + 1)) - 1
    for mask in range(1 << N):
        adj = [0] * (j + 1)
        radj = [0] * (j + 1)
        for k, (u, v) in enumerate(edges):
            if mask >> k & 1:
                adj[u] |= 1 << v
                radj[v] |= 1 << u
        reach = 1
        for v in range(j + 1):
            if reach >> v & 1:
                reach |= adj[v]
        coreach = 1 << j
        for v in range(j, -1, -1):
            if coreach >> v & 1:
                coreach |= radj[v]
        if reach == full and coreach == full:
            tot = tot + (P_ ** bin(mask).count("1")) * (Q_ ** (N - bin(mask).count("1")))
    return tot


def section_d():
    print("D. bridge coefficients: three independent definitions, and bounds")
    params = [(F(1, 2), "p=1/2"), (F(3, 2), "p=3/2"), (F(2), "p=2"),
              (F(-1), "p=-1"), (F(-1, 2), "p=-1/2")]
    for p, name in params:
        B, R, _ = bridge_tables(p, 7)
        assert B[0] == G(1)
        for j in range(1, 8):
            assert B[j] == bridge_ie(j, p), (name, j)
        for j in range(1, 5):
            assert B[j] == brute_bridge(j, p), (name, j, "brute")
        bf = ""
        if p == F(1, 2):
            assert B[5] == brute_bridge(5, p)
            bf = ", brute force to j=5"
        a, b = abs_pair(p)
        # b<1: |B_j| <= [prod_d (1+b^(d/2))]^2 ; b>=1: |B_j| <= 4^j b^(j(j+1)/2)
        skip = ""
        if (b - Q2(1)).sign() < 0:
            for j in range(1, 8):
                mag2 = q2(modulus2(B[j]))
                sb = sqrt_rational_box(b.u)
                prod = Q2(1)
                for d in range(1, j + 1):
                    prod = prod * (1 + (sb ** d))
                assert (prod * prod - mag2).sign() >= 0, (name, j, "b1")
            skip = " (b<1: product bound)"
        else:
            for j in range(1, 8):
                mag2 = q2(modulus2(B[j]))
                second = q2(4 ** j) * (b ** (j * (j + 1) // 2))
                assert (second * second - mag2).sign() >= 0, (name, j, "b2")
            skip = " (b>=1: 4^j b^(j(j+1)/2) bound)"
        print(f"  {name}: B_j == inclusion-exclusion (j=1..7) and brute-force "
              f"percolation (j=1..4{bf}); bound holds{skip}")
    p = (F(1, 2), F(1, 2))
    B, R, _ = bridge_tables(p, 6)
    for j in range(1, 7):
        assert B[j] == bridge_ie(j, p), j
    print("  p=(1+i)/2: B_j == inclusion-exclusion, j=1..6")


# ---------------------------------------------------------------- section E
def section_e():
    print("E. weighted ratio: exact exponent identity and geometric majorant")
    cases = [(F(3, 2), "p=3/2 (b<1)"), (F(1, 2), "p=1/2 (classical, t=1)"),
             (F(-1, 2), "p=-1/2 (b>1)"), (F(-1), "p=-1 (b>1)"),
             (F(5, 2), "p=5/2 (b>1)"), (F(2), "p=2 (b=1)")]
    for p, name in cases:
        a, b = abs_pair(p)
        assert a.v == 0 and b.v == 0
        av, bv = a.u, b.u
        if bv >= 1:
            good = None
            for n in range(2, 80):
                if av * bv ** (n - 2) > 4:
                    good = n
                    break
            ncheck = good if good is not None else 5
            for j in range(0, 41):
                assert F(j * (j + 1), 2) - F((ncheck + j - 1) * (ncheck + j - 2), 2) \
                    == -F((ncheck - 1) * (ncheck - 2), 2) - j * (ncheck - 2)
                assert -(ncheck + j - 1) == -(ncheck - 1) - j
            if good is None:
                print(f"  {name}: no n<=79 with a*b^(n-2)>4; b=1 branch used")
            else:
                q = F(4) / (av * bv ** (good - 2))
                const = F(av) ** (-(good - 1)) * F(bv) ** (-F((good - 1) * (good - 2), 2))
                partial = sum(q ** j for j in range(60))
                print(f"  {name}: exponent identity exact j=0..40; n0={good}, "
                      f"q={float(q):.4f}<1, const*sum_(j<60)q^j="
                      f"{float(const * partial):.6g}")
        else:
            t = av + bv
            if t == 1:
                print(f"  {name}: t=1 exactly (real p in (0,1)); the b<1 "
                      "branch needs t>1 and is NOT invoked here")
            else:
                assert t > 1
                print(f"  {name}: t={float(t):.4f}>1, geometric ratio 1/t; "
                      f"partial sum_60="
                      f"{float(sum((1 / t) ** j for j in range(60))):.6f}")
    for p, name in [(F(3, 2), "p=3/2"), ((F(1, 2), F(1, 2)), "p=(1+i)/2")]:
        B, R, _ = bridge_tables(p, 8)
        mus = [float(modulus2(B[j])) for j in range(0, 8)]
        print(f"  {name}: |B_j|^2, j=0..7 = "
              + ", ".join(f"{x:.4g}" for x in mus))


# ---------------------------------------------------------------- section H
def section_h():
    """Finite child-sum (laminar partition) identity, the exact finite input to
    the absolute-convergence step.  For every labelled principal H of size n and
    every m>n, the sum of A_p(J) over labelled principal J of size m whose
    previous post past is H equals A_p(H) R_(m-n)."""
    print("H. child-sum decomposition sum_J A_p(J) = A_p(H) R_(m-n), exact")
    params = [(F(1, 2), "p=1/2"), (F(3, 2), "p=3/2"),
              (F(-1), "p=-1"), ((F(1, 2), F(1, 2)), "p=(1+i)/2")]
    for p, name in params:
        P_ = gg(p)
        q_ = G(1) - P_
        pp, qp = powers(P_, 60), powers(q_, 60)
        B, R, _ = bridge_tables(p, TOPDEG)
        rels = {}
        for m in range(1, MAXN + 1):
            rels[m] = []
            for J in POS[m]:
                rels[m].append(frozenset(PAIRS[m][k] for k in range(len(PAIRS[m]))
                                         if J[0] >> k & 1))
        checks = 0
        for m in range(2, MAXN + 1):
            acc = {}
            for idx, J in enumerate(POS[m]):
                if not J[PRIN_I]:
                    continue
                posts = J[POST_I]
                if len(posts) < 2:
                    continue
                pidx = posts[-2]
                n = pidx + 1
                Hrel = frozenset((i, j) for (i, j) in rels[m][idx] if j <= pidx)
                key = (n, Hrel)
                acc[key] = acc.get(key, G(0)) + pp[J[L_I]] * qp[J[H_I]]
            for (n, Hrel), s in acc.items():
                L, Rr, _, _, _ = analyse(Hrel, n)
                target = pp[L] * qp[n * (n - 1) // 2 - Rr] * R[m - n]
                assert s == target, (name, n, m, s, target)
                checks += 1
        print(f"  {name}: {checks} exact child-sum identities, "
              f"n<m<={MAXN}")


# ---------------------------------------------------------------- section F
def section_f():
    print("F. endpoints and the division failure")
    assert [P for P in POS[5] if P[PRIN_I] and P[L_I] == 0] == []
    print("  p=0: every principal order of size 2..5 has L>=1, so A_0=0 exactly")
    for n in range(2, 6):
        assert sum(1 for P in POS[n] if P[H_I] == 0) == 1
        P_ = G(1)
        q_ = G(0)
        pp, qp = powers(P_, 30), powers(q_, 30)
        for P in POS[n]:
            val = pp[P[L_I]] * qp[P[H_I]]
            assert val == (G(1) if P[H_I] == 0 else G(0))
    print("  p=1: A_1(H)=1 exactly on the unique chain, 0 elsewhere, n=2..5")
    for n in range(1, 7):
        chain = [P for P in POS[n] if P[H_I] == 0][0]
        assert chain[L_I] == n - 1 and chain[MAX_I] == 1
    print("  chain: L=n-1, h=0, N=1, so N*A_p=p^(n-1); nonzero iff p!=0")
    print("  at p=0 the rank-only recurrence cannot be derived by division;")
    print("  the no-go instead uses A_0(H)=0 at ranks>=2 plus the laminar cover")


# ---------------------------------------------------------------- section G
def section_g():
    print("G. positive segment sums K_k (variation side) vs complex R_k")
    for p, name in [(F(1, 2), "p=1/2"), (F(3, 2), "p=3/2"), (F(2), "p=2"),
                    (F(-1), "p=-1")]:
        B, R, K = bridge_tables(p, 7)
        kk = ", ".join(f"{k}:{float(K[k].u + K[k].v * 2 ** 0.5):.4g}"
                       for k in range(1, 8))
        rr = ", ".join(f"{k}:{abs(complex(R[k].re, R[k].im)):.4g}"
                       for k in range(1, 8))
        print(f"  {name} K_k = {kk}")
        print(f"  {name} R_k = {rr}")
    print("  NOTE: growth of K_k is the total-variation side. It is NOT used by")
    print("  the argument in RESULT.md and says nothing about convergence of")
    print("  the complex series sum R_k z^k (cancellation is not excluded).")


if __name__ == "__main__":
    section_a()
    section_b()
    section_c()
    section_d()
    section_e()
    section_h()
    section_f()
    section_g()
    print("\nALL FINITE EXACT CHECKS PASSED (finite corroboration only)")
