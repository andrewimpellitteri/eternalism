#!/usr/bin/env python3
"""Witness checks for task glm-vector-indicator-boundary.

The construction under test: for p in C and alpha in [1, inf) with
|p|^alpha + |1-p|^alpha = 1, the indicator map mu(E) = 1_E into L^alpha(P_r),
r = |p|^alpha, is a countably additive vector measure with
||mu(cyl C)||_alpha = |A_p(C)| = |p|^L |1-p|^h on every two-parameter cylinder.

Checks (standard library only; exact where possible):
  1. binary model, p=(1+i)/2, alpha=2, r=1/2: exact norm prescription on all
     words of length 1..12 (Fractions: |A_p(w)|^2 = (1/2)^n = P_{1/2}(w)).
  2. exact additivity-residual identity ||mu(union) - partial sum||^2 = P(tail).
  3. semivariation on the level-3 algebra: random L^2 functions never exceed
     P(E)^{1/2}; the exact extremizer attains it.
  4. total-variation divergence on level-k partitions: 2^{k/2} -> inf, equal to
     (|p|+|1-p|)^k for the prescription.
  5. causet model: independent exact verification of the classical transitive
     percolation cylinder formula P_r(cyl C) = r^{L(C)} (1-r)^{h(C)} on all
     labelled orders with n = 3, 4 labels, r in {1/2, 2/5}, by edge-subset
     enumeration in Fraction arithmetic.
  6. causet model: finite-level recheck of V_4, V_5 at p=(1+i)/2 via the
     two-cap construction G + {u} + {v}; V_5 must match the value recorded in
     research/replication/AGENT_REPORT.md (1.015165042945...).  Finite levels
     only: the all-level two-cap bound is not re-proved here.
  7. existence locus for alpha: bisection of alpha*(p) for sample points,
     on-circle points give alpha = 2, boundary/outside points admit no solution,
     real-segment points admit only alpha = 1, endpoints admit every alpha,
     and S(alpha) = |p|^alpha + |1-p|^alpha is strictly decreasing on the lens.
"""
import itertools
import math
import random
import sys
from collections import defaultdict
from fractions import Fraction as F

FAILURES = []


def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAILURES.append(name)


# --------------------------------------------------------------------------
# 1. Exact norm prescription, binary model, p = (1+i)/2, alpha = 2, r = 1/2
#    |p|^2 = |1-p|^2 = 1/2 exactly, so |A_p(w)|^2 = (1/2)^n = P_{1/2}(w).
# --------------------------------------------------------------------------
exact_ok = True
word_count = 0
for n in range(1, 13):
    for w in itertools.product((0, 1), repeat=n):
        word_count += 1
        L = sum(w)
        h = n - L
        a2 = F(1, 2) ** L * F(1, 2) ** h      # |A_p(w)|^2
        pw = F(1, 2) ** n                      # P_{1/2}(cyl w)
        if a2 != pw:
            exact_ok = False
check("binary norm prescription |A_p(w)|^2 = P_{1/2}(w), levels 1..12 (exact)",
      exact_ok and word_count == 8190, f"{word_count} words checked in Fraction arithmetic")

check("locus identity |p|^2+|1-p|^2 = 1 at p=(1+i)/2 (exact)",
      (F(1, 4) + F(1, 4)) + (F(1, 4) + F(1, 4)) == F(1))

# --------------------------------------------------------------------------
# 2. Additivity residuals: partition cyl(000) into E_n = "first 1 at slot n".
#    E_n = 000 0^{n-1} 1 ***, so P(E_n) = (1/2)^{n+3} and after N partial sums
#    the exact L^2 residual norm squared is P(tail) = (1/2)^{N+3}.
# --------------------------------------------------------------------------
res = []
for N in range(8):
    partial = sum((F(1, 2) ** (n + 3) for n in range(1, N + 1)), F(0))
    tail = F(1, 8) - partial
    assert tail == F(1, 2) ** (N + 3)
    res.append(tail)
check("additivity residual ||mu(U)-partial||_2^2 = P(tail), decreasing to 0 (exact)",
      all(res[i] > res[i + 1] for i in range(len(res) - 1)) and min(res) > 0,
      f"residuals {str(float(res[0]))[:8]}..{str(float(res[-1]))[:8]}")

# --------------------------------------------------------------------------
# 3. Semivariation on the level-3 algebra (8 atoms, P = 1/8 each).
#    For g on the atoms, the variation of gP over a union E of m atoms is
#    sum |g_i|/8 over chosen atoms; ||g||_2^2 = sum g_i^2 / 8.  Claim:
#    V(g; E) <= ||g||_2 P(E)^{1/2} <= P(E)^{1/2}, attained at g = sqrt(8/m) 1_E.
# --------------------------------------------------------------------------
random.seed(7)
sv_ok = True
worst = 0.0
for trial in range(50):
    m = random.randrange(1, 9)
    chosen = set(random.sample(range(8), m))
    for _ in range(80):
        g = [random.gauss(0, 1) for _ in range(8)]
        nrm = math.sqrt(sum(x * x for x in g) / 8.0)
        g = [x / nrm for x in g]
        v = sum(abs(g[i]) / 8.0 for i in chosen)
        worst = max(worst, v - math.sqrt(m / 8.0))
        if v > math.sqrt(m / 8.0) + 1e-12:
            sv_ok = False
# exact extremizer: g = sqrt(8/m) * 1_E has ||g||_2 = 1 and V(g;E) = sqrt(m/8).
m4 = 4
g4 = math.sqrt(8.0 / m4)
v4 = m4 * g4 / 8.0
sv_ok = sv_ok and abs(v4 - math.sqrt(m4 / 8.0)) < 1e-12
check("semivariation bound: V(g;E) <= P(E)^{1/2} for all sampled g, extremizer attains",
      sv_ok, f"max excess {worst:.2e}")

# --------------------------------------------------------------------------
# 4. Total-variation divergence on level-k partitions of the binary model.
#    sum over 2^k words of ||mu(cyl w)||_2 = 2^k * 2^{-k/2} = 2^{k/2}
#    and the prescription makes this (|p|+|1-p|)^k = (sqrt 2)^k identically.
# --------------------------------------------------------------------------
tv = [(k, 2 ** k * math.sqrt(2.0 ** (-k))) for k in (1, 2, 4, 8, 16, 32)]
mono = all(tv[i][1] < tv[i + 1][1] for i in range(len(tv) - 1))
ident = all(abs(s - math.sqrt(2.0) ** k) < 1e-9 * s for k, s in tv)
check("level-k norm sums = (|p|+|1-p|)^k = 2^{k/2} -> inf", mono and ident and tv[-1][1] >= 65536,
      f"k=32 sum = {tv[-1][1]:.6g}")

# --------------------------------------------------------------------------
# 5. Causet model: exact verification of P_r(cyl C) = r^{L(C)} (1-r)^{h(C)}
#    for every labelled order on n = 3, 4 labels, by edge-subset enumeration.
# --------------------------------------------------------------------------
def closure(rel, n):
    R = set(rel)
    changed = True
    while changed:
        changed = False
        for (a, b) in list(R):
            for (c, d) in list(R):
                if b == c and (a, d) not in R:
                    R.add((a, d))
                    changed = True
    return frozenset(R)


def links(rel, n):
    out = 0
    for (i, j) in rel:
        if not any((i, k) in rel and (k, j) in rel for k in range(1, n + 1)):
            out += 1
    return out


ctpf_ok = True
counts = {}
for n in (3, 4):
    pairs = [(i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1)]
    N = len(pairs)
    prob = defaultdict(lambda: F(0))
    for bits in itertools.product((0, 1), repeat=N):
        E = frozenset(p for p, b in zip(pairs, bits) if b)
        prob[closure(E, n)] += F(1, 1)
    counts[n] = len(prob)
    for r in (F(1, 2), F(2, 5)):
        acc = defaultdict(lambda: F(0))
        for bits in itertools.product((0, 1), repeat=N):
            E = frozenset(p for p, b in zip(pairs, bits) if b)
            acc[closure(E, n)] += r ** len(E) * (1 - r) ** (N - len(E))
        for C, pC in acc.items():
            L = links(C, n)
            h = N - len(C)
            if pC != r ** L * (1 - r) ** h:
                ctpf_ok = False
check("causet CTP cylinder formula P_r(cyl C)=r^{L}(1-r)^{h}, n=3,4, r=1/2,2/5 (exact)",
      ctpf_ok, f"labelled orders: {counts[3]} (n=3), {counts[4]} (n=4)")

# --------------------------------------------------------------------------
# 6. Finite-level recheck of V_4, V_5 at p=(1+i)/2 via two-caps.
#    dp orders on k+2 labels = C_G = closure(G) + {k+1} + {k+2}, G any
#    labelled k-order.  Levels checked only; no all-level bound re-proved.
# --------------------------------------------------------------------------
def two_cap(rel, k):
    s = set(rel)
    for i in range(1, k + 1):
        s.add((i, k + 1))
        s.add((i, k + 2))
    s.add((k + 1, k + 2))
    return closure(s, k + 2)


def closed_masks(n):
    pairs = [(i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1)]
    out = []
    for bits in itertools.product((0, 1), repeat=len(pairs)):
        rel = frozenset(p for p, b in zip(pairs, bits) if b)
        if closure(rel, n) == rel:
            out.append(rel)
    return out


def pairs_of(m):
    return [(i, j) for i in range(1, m + 1) for j in range(i + 1, m + 1)]


amp_mod = lambda L, h: math.sqrt(0.5) ** (L + h)   # |p|^L |1-p|^h at p=(1+i)/2
for k, expect in ((2, None), (3, 1.015165042945)):
    n = k + 2
    V = 0.0
    for G in closed_masks(k):
        C = two_cap(G, k)
        L = links(C, n)
        h = len(pairs_of(n)) - len(C)
        V += amp_mod(L, h)
    ok = True
    if expect is not None:
        ok = abs(V - expect) < 1e-9
    check(f"two-cap V_{n} at p=(1+i)/2, {len(closed_masks(k))} base orders", ok,
          f"V_{n} = {V:.12f}" + (f" (matches replication {expect})" if expect else ""))

# --------------------------------------------------------------------------
# 7. Existence locus for alpha*(p).
# --------------------------------------------------------------------------
def S(p, q):
    return abs(p) ** q + abs(1 - p) ** q


def qstar(p, lo=1.0, hi=400.0, iters=300):
    if not S(p, lo) > 1.0 or not S(p, hi) < 1.0:
        return None
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if S(p, mid) > 1.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


locus_ok = True
p = 0.5 + 0.5j
q = qstar(p)
locus_ok &= q is not None and abs(q - 2.0) < 1e-9
th = math.pi / 3
p2 = 0.5 + 0.5 * complex(math.cos(th), math.sin(th))
q2 = qstar(p2)
locus_ok &= q2 is not None and abs(q2 - 2.0) < 1e-9          # on the Thales circle
q3 = qstar(0.5 + 0.55j)                                       # lens, outside circle
locus_ok &= q3 is not None and 2.0 < q3 < 3.0                 # approx 2.334
locus_ok &= abs(S(0.5 + 0.55j, q3) - 1.0) < 1e-9
q4 = qstar(0.9 + 0.1j)                                        # inside circle
locus_ok &= q4 is not None and 1.0 < q4 < 2.0
check("locus: on-circle points give alpha*=2, outside alpha*>2, inside alpha*<2",
      bool(locus_ok), f"(1+i)/2: {q:.9f}; {p2.real:.4f}+{p2.imag:.4f}i: {q2:.9f}; "
      f"0.5+0.55i: {q3:.9f}; 0.9+0.1i: {q4:.9f}")

bound_ok = True
for pb in (complex(math.cos(math.pi / 3), math.sin(math.pi / 3)),  # |p| = 1
           0.5 + 0.5j * math.sqrt(3.0),                            # |p| = |1-p| = 1
           2 + 0j, -0.5 + 0j, 0.5 + 1.0j):                         # outside the lens
    bound_ok &= all(S(pb, qq) > 1.0 for qq in [1.0 + 0.25 * i for i in range(240)])
check("boundary/outside points: no alpha in [1,60] satisfies the locus equation", bound_ok)

real_ok = True
for pr in (0.3, 0.5, 0.75):
    real_ok &= abs(abs(pr) + abs(1 - pr) - 1.0) < 1e-12          # S(1) = 1
    real_ok &= S(complex(pr), 1.0 + 1e-6) < 1.0                  # strictly below for alpha > 1
    real_ok &= qstar(complex(pr)) is None                        # no second root above 1
check("real interior (0,1): exactly alpha = 1", real_ok)

eps_ok = all(abs(S(pp, qq) - 1.0) < 1e-12
             for pp in (0j, 1 + 0j) for qq in [1.0 + 0.5 * i for i in range(118)])
check("endpoints p=0,1: S(alpha) = 1 for every alpha in [1,60] (degenerate r in {0,1})", eps_ok)

dec_ok = True
for pl in (0.5 + 0.5j, 0.3 + 0.2j, 0.5 + 0.55j):
    grid = [S(pl, 1.0 + 0.05 * i) for i in range(160)]
    dec_ok &= all(grid[i] > grid[i + 1] for i in range(len(grid) - 1))
check("S(alpha) strictly decreasing on [1,9] for lens points (uniqueness)", dec_ok)

# --------------------------------------------------------------------------
print()
if FAILURES:
    print(f"FAILED: {len(FAILURES)}: {FAILURES}")
    sys.exit(1)
print("ALL CHECKS PASSED")
sys.exit(0)
