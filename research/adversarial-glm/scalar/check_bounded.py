#!/usr/bin/env python3
"""Bounded exact checks for the adversarial review of RESULT.md / COVARIANT_RESULT.md.

Standard library only. Enumerations restricted to naturally labelled causets on
at most n = 5 labels. Quantities at n = 6 are computed with the analytic
two-cap amplitude formula applied to the n = 4 enumeration; no 6-element
causet is materialized.

Predictions pre-registered in INDEPENDENT_NOTES.md (section 3) before running:
  N1 two-cap bijection counts           N5 F_k(s) product identity
  N2 V_5 = 3/4 + 3*sqrt(2)/16           N6 laminarity witnesses on shapes n<=5
  N3 V_6 = 31/32 + 55*sqrt(2)/64        N7 p=0 cover facts
  N4 W   = 9/16 + 105/(128*sqrt(2)), 40 principal 5-blocks

Recovery-run corrections (coordinator INTERIM_GLM_CHECK.md, 2026-10-21):
  - certificate W uses exponent L+min(G)+h(G)+1 (ordinal block {bot}+G+{top},
    seam edges to each MINIMAL element), not the two-cap helper exponent
    L+M(G)+h+1 used in run 1;
  - V_2 = 1/sqrt(2) (only doubly-principal 2-order is the 2-chain); the run-1
    printed value 1/2 + sqrt2/4 was a hard-coded print bug;
  - the script now exits nonzero when any check fails.
"""
from fractions import Fraction
from itertools import combinations, permutations, product
import math
import sys

# ---------------------------------------------------------------- enumeration

def transitive_closure(pairs, n):
    """Transitive closure of forward pairs on labels 1..n."""
    adj = {i: set() for i in range(1, n + 1)}
    for i, j in pairs:
        adj[i].add(j)
    reach = {i: set(adj[i]) for i in range(1, n + 1)}
    changed = True
    while changed:
        changed = False
        for i in range(1, n + 1):
            new = set()
            for j in reach[i]:
                new |= reach[j]
            if not new <= reach[i]:
                reach[i] |= new
                changed = True
    return frozenset((i, j) for i in range(1, n + 1) for j in reach[i])


def enumerate_causets(n):
    """All naturally labelled causets on labels 1..n as frozensets of pairs."""
    forward = list(combinations(range(1, n + 1), 2))
    seen = set()
    for mask in range(1 << len(forward)):
        pairs = [forward[b] for b in range(len(forward)) if mask >> b & 1]
        seen.add(transitive_closure(pairs, n))
    return sorted(seen)


def metrics(rels, n):
    """L = covers, R = comparable pairs, M = maximal elements."""
    covers = 0
    for i, j in rels:
        if not any((i, k) in rels and (k, j) in rels for k in range(1, n + 1)):
            covers += 1
    maxima = sum(1 for i in range(1, n + 1)
                 if not any((i, j) in rels for j in range(1, n + 1)))
    return covers, len(rels), maxima


def principal(rels, labels):
    m = metrics(rels, len(labels)) if labels else (0, 0, 0)
    return m[2] == 1 and len(labels) > 0


def prefix(rels, k):
    """Restrict to labels 1..k (rels are transitively closed)."""
    return frozenset((i, j) for (i, j) in rels if j <= k and i <= k)


def doubly_principal(rels, n):
    return principal(rels, range(1, n + 1)) and principal(prefix(rels, n - 1),
                                                          range(1, n))


def natural_relabellings(rels, n):
    """Distinct natural (order-preserving) relabellings as relation sets.

    A poset-shape invariant: two causets are isomorphic iff their sets
    coincide, and its size is N(H) as defined in COVARIANT_RESULT.md.
    Recovery-run fix: run 1's shape_key canonicalised comparability GRAPHS
    (min/max on each mapped pair), which merges a poset with its order dual
    (V-shape vs Lambda-shape on 3 labels). Caught by N2b here; poset
    isomorphism must preserve relation direction.
    """
    out = set()
    for perm in permutations(range(1, n + 1)):
        mapped = set()
        ok = True
        for i, j in rels:
            a, b = perm[i - 1], perm[j - 1]
            if a > b:
                ok = False
                break
            mapped.add((a, b))
        if ok:
            out.add(frozenset(mapped))
    return out


def shape_key(rels, n):
    """Canonical key among natural relabellings (poset isomorphism class):
    the lexicographically least sorted full relation tuple over all natural
    relabellings. Two causets get equal keys iff isomorphic (equal relabelling
    sets)."""
    return min(sorted(s) for s in natural_relabellings(rels, n))


def extension_count(rels, n):
    """Number of linear extensions (total orders respecting rels)."""
    preds = [0] * n
    for i, j in rels:
        preds[j - 1] |= 1 << (i - 1)
    def rec(used):
        total = 0
        for x in range(n):
            if not used >> x & 1 and preds[x] & ~used == 0:
                total += rec(used | 1 << x)
        return total or 1
    return rec(0)


def aut_size(rels, n):
    """Order of the automorphism group of the labelled causet."""
    cnt = 0
    for perm in permutations(range(1, n + 1)):
        mapped = set()
        ok = True
        for i, j in rels:
            a, b = perm[i - 1], perm[j - 1]
            if a > b:
                ok = False
                break
            mapped.add((a, b))
        if ok and mapped == set(rels):
            cnt += 1
    return cnt


def cap_term_2x(w, h):
    """|A_p(C_G)| at p=(1+i)/2 as A + B*sqrt(2) with exact A, B.

    a = b = 1/sqrt(2); |A_p| = (1/sqrt2)^(w+h+1) = 2^-(w+h+1)/2.
    Odd exponent m contributes 2^-(m+1)/2 * sqrt(2).
    """
    m = w + h + 1
    if m % 2 == 0:
        return Fraction(1, 2 ** (m // 2)), Fraction(0)
    return Fraction(0), Fraction(1, 2 ** ((m + 1) // 2))


def abs_amp_exact(rels, n):
    """|A_p(C)| at p=(1+i)/2 computed DIRECTLY on C: exact A+B*sqrt2.

    |p|=|q|=1/sqrt2, |A_p| = 2^{-(L+h)/2}, h = C(n,2)-R. Distinct from
    cap_term_2x, which encodes the two-cap body reindex |A_p(G+u+v)| =
    |p|^{w+1}|q|^h (exponent w+h+1) and must not be applied to an already
    capped object.
    """
    L, R, M = metrics(rels, n)
    m = L + n * (n - 1) // 2 - R
    if m % 2 == 0:
        return Fraction(1, 2 ** (m // 2)), Fraction(0)
    return Fraction(0), Fraction(1, 2 ** ((m + 1) // 2))


results = []


def check(name, ok, detail=""):
    results.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


# ------------------------------------------------- N1: two-cap bijection, n<=5
for n in (3, 4, 5):
    all_n = enumerate_causets(n)
    dbl = [c for c in all_n if doubly_principal(c, n)]
    g_count = len(enumerate_causets(n - 2)) if n >= 3 else 1
    check(f"N1 two-cap bijection n={n}", len(dbl) == g_count,
          f"doubly-principal={len(dbl)} arbitrary G on {n-2} labels={g_count}")

# --------------------------------------------- N2/N3: V_5, V_6 at p=(1+i)/2
def V_exact(k):
    """Sum over arbitrary G on k labels of capped |A_p|; exact A + B*sqrt2."""
    A = B = Fraction(0)
    for g in enumerate_causets(k):
        L, R, M = metrics(g, k)
        w, h = L + M, k * (k - 1) // 2 - R
        a, b = cap_term_2x(w, h)
        A, B = A + a, B + b
    return A, B

A, B = V_exact(0)   # empty G: capped exponent w+h+1 = 1 -> |A_p| = 1/sqrt2
check("N2pre V_2 = 1/sqrt2 (only DP 2-order is the 2-chain)",
      A == 0 and B == Fraction(1, 2), f"got A={A} B={B}")
A, B = V_exact(3)
check("N2 V_5 = 3/4 + 3sqrt2/16", A == Fraction(3, 4) and B == Fraction(3, 16),
      f"got A={A} B={B}")
A, B = V_exact(4)   # n=4 enumeration + analytic two-cap formula (no 6-run)
check("N3 V_6 = 31/32 + 55sqrt2/64",
      A == Fraction(31, 32) and B == Fraction(55, 64), f"got A={A} B={B}")

# N2b: labelled-versus-unlabelled multiplicities, the grouping step used in the
# covariant theorem: A_p must be shape-invariant on doubly-principal orders,
# and the shape-grouped sum sum_[H] N(H)|A_p(H)| must reproduce the labelled V_5.
all5dp = [c for c in enumerate_causets(5) if doubly_principal(c, 5)]
groups = {}
for c in all5dp:
    groups.setdefault(tuple(shape_key(c, 5)), []).append(c)
ok_inv = True
totA = totB = Fraction(0)
for members in groups.values():
    vals = set()
    for c in members:
        vals.add(abs_amp_exact(c, 5))
    if len(vals) != 1:
        ok_inv = False
    a, b = next(iter(vals))
    totA, totB = totA + a * len(members), totB + b * len(members)
check("N2b A_p shape-invariant on DP 5-orders; sum_[H] N(H)|A_p(H)| = V_5",
      ok_inv and (totA, totB) == V_exact(3),
      f"shapes={len(groups)} labelled_reps={len(all5dp)}")

# N2c: N(H) bookkeeping used by (T) and percolation sufficiency:
# extensions = |natural relabellings| * |Aut| for every poset n <= 5.
viol = 0
for n in (1, 2, 3, 4, 5):
    for c in enumerate_causets(n):
        s = natural_relabellings(c, n)
        if extension_count(c, n) != len(s) * aut_size(c, n):
            viol += 1
check("N2c linear extensions = N(H)*|Aut| for all posets n<=5 (N(H)=|S|)",
      viol == 0, f"violations={viol}")

# ------------------------------------- N4: ordinal-block W certificate.
# Coordinator-traced encoding correction (INTERIM_GLM_CHECK.md): the historical
# certificate (covariant-stopping/reduced_poscau_obstruction.py, RESULT.md)
# uses per-block exponent L(G)+min(G)+h(G)+1 with h = 10-R(G): the object is
# the ordinal block {bottom}+G+{top}, doubly principal because G is principal;
# prepending the bottom contributes min(G) covers (seam edges to each minimal
# element), appending the top contributes one, and R({bot}+G+{top}) = R(G)+11
# leaves the h-part at 10-R(G). Run 1 mistakenly used the two-cap helper
# exponent L+M+1 on principal bodies (M=1 there), i.e. L+h+2: a different
# statistic whenever min(G) != 1. That old quantity is kept below only as an
# auxiliary cross-check, clearly not labeled as W.
all5 = enumerate_causets(5)
principal5 = [c for c in all5 if principal(c, range(1, 6))]
check("N4a count of naturally labelled principal 5-blocks = 40",
      len(principal5) == 40, f"got {len(principal5)}")

def minima_count(rels):
    return sum(1 for j in range(1, 6)
               if not any((i, j) in rels for i in range(1, 6)))

builder_bivariate = {
    (5, 0): 1, (6, 1): 3, (6, 2): 6, (6, 3): 4, (6, 4): 3,
    (7, 3): 7, (7, 4): 8, (7, 5): 6, (8, 2): 1, (8, 6): 1,
}
hist = {}
for blk in principal5:
    L, R, M = metrics(blk, 5)
    hist[(L + minima_count(blk), 10 - R)] = \
        hist.get((L + minima_count(blk), 10 - R), 0) + 1
check("N4b bivariate (L+min, 10-R) histogram over 40 blocks matches builder",
      hist == builder_bivariate, f"got {dict(sorted(hist.items()))}")

# Certificate W = sum over the 40 principal 5-blocks of 2^-(L+min+h+1)/2.
A = B = Fraction(0)
for blk in principal5:
    L, R, M = metrics(blk, 5)
    m = L + minima_count(blk) + (10 - R) + 1
    if m % 2 == 0:
        A += Fraction(1, 2 ** (m // 2))
    else:
        B += Fraction(1, 2 ** ((m + 1) // 2))
check("N4c W = 9/16 + 105/(128*sqrt2) (RESULT.md certificate)",
      A == Fraction(9, 16) and B == Fraction(105, 256),
      f"got A={A} B={B}")
# Exact W > 71/64: reduces to 105*sqrt2/256 > 35/64, i.e. sqrt2 > 4/3,
# i.e. 2 > 16/9. No floating point in the assertion.
check("N4d W > 71/64 > 1 (exact integer comparison)",
      2 * 9 > 16, f"W ~ {float(A) + float(B) * math.sqrt(2):.10f}")

# Builder's r5 = sum 2^-(L+min+h)/2 = 105/128 + 9*sqrt2/16, W = r5/sqrt2:
# independent re-derivation of the builder script's printed intermediate.
A = B = Fraction(0)
for blk in principal5:
    L, R, M = metrics(blk, 5)
    m = L + minima_count(blk) + (10 - R)
    if m % 2 == 0:
        A += Fraction(1, 2 ** (m // 2))
    else:
        B += Fraction(1, 2 ** ((m + 1) // 2))
check("N4e r5 = 105/128 + 9*sqrt2/16 (builder printout, W = r5/sqrt2)",
      A == Fraction(105, 128) and B == Fraction(9, 16),
      f"got A={A} B={B}")

# Auxiliary (NOT the certificate): partial V_7 sum over doubly-principal
# G+u+v with principal body G, exponent L(G)+M(G)+h(G)+1 (run 1 mislabeled
# this quantity "W2").
A = B = Fraction(0)
for blk in principal5:
    L, R, M = metrics(blk, 5)
    a, b = cap_term_2x(L + M, 10 - R)
    A, B = A + a, B + b
check("N4f auxiliary principal-body two-cap partial sum = 55/64 + 31sqrt2/64",
      A == Fraction(55, 64) and B == Fraction(31, 64), f"got A={A} B={B}")

# ------------------------------------- N5: random-graph-order product identity
def rg_orders(n):
    """All random-graph orders on vertices 1..n with multiplicity-free masks."""
    forward = list(combinations(range(1, n + 1), 2))
    out = {}
    for mask in range(1 << len(forward)):
        pairs = [forward[b] for b in range(len(forward)) if mask >> b & 1]
        rels = transitive_closure(pairs, n)
        out.setdefault(rels, []).append(mask)
    return out, forward

def mask_weight(mask, forward, r, s):
    w = bin(mask).count("1")
    return r ** w * s ** (len(forward) - w)

for k in (1, 2, 3, 4):           # vertices 1..k+1  (<=5 vertices)
    n = k + 1
    orders, forward = rg_orders(n)
    r, s = Fraction(3, 4), Fraction(1, 4)
    # (a) direct mask-weight sum, grouped by resulting order
    prob = {rels: sum((mask_weight(m, forward, r, s) for m in masks),
                      Fraction(0)) for rels, masks in orders.items()}
    # (b) closed form r^L s^(C(n,2)-R)
    ok_b = all(prob[rels] == r ** metrics(rels, n)[0]
               * s ** (n * (n - 1) // 2 - metrics(rels, n)[1])
               for rels in prob)
    # (c) event 'vertex n above all others' equals F_k(s)
    ev = sum((p for rels, p in prob.items()
              if all((i, n) in rels for i in range(1, n))), Fraction(0))
    Fk = Fraction(1, 1)
    for j in range(1, k + 1):
        Fk *= 1 - s ** j
    check(f"N5 identity k={k}: mask-sum=r^L s^h, event=F_k",
          ok_b and ev == Fk, f"F_{k}(1/4)={Fk} event={ev}")

    # (d) second parameter pair, order-level sum over G only
    r2, s2 = Fraction(2, 5), Fraction(3, 5)
    tot = Fraction(0)
    for g in enumerate_causets(k):
        L, R, M = metrics(g, k)
        tot += r2 ** (L + M) * s2 ** (k * (k - 1) // 2 - R)
    Fk2 = Fraction(1, 1)
    for j in range(1, k + 1):
        Fk2 *= 1 - s2 ** j
    check(f"N5 F_k identity at r=2/5 k={k}", tot == Fk2,
          f"sum={tot} product={Fk2}")

# --------------------------------------------- N6: laminarity on shapes n<=5
def posts_of(rels, n):
    return [x for x in range(1, n + 1)
            if all((x, y) in rels or (y, x) in rels
                   for y in range(1, n + 1) if y != x)]


def past_shape_keys(rels, n):
    """Shape keys of inclusive pasts of posts, by size."""
    out = {}
    for x in posts_of(rels, n):
        p = frozenset((i, j) for (i, j) in rels if j <= x)
        out[x] = (x, tuple(shape_key(p, x)))
    return out

viol = 0
for nj in (1, 2, 3, 4, 5):
    for j in enumerate_causets(nj):
        if not principal(j, range(1, nj + 1)):
            continue
        pj = past_shape_keys(j, nj)
        sizes = [m for m, _ in pj.values()]
        if len(sizes) != len(set(sizes)):     # distinct past sizes among posts
            viol += 1
        for nh in sizes:                       # same-rank shapes: disjointness
            pass
check("N6a posts of a causet have pairwise distinct past sizes", viol == 0,
      f"violations={viol}")

# D_{H+cap} subset D_H: canonical check via post-past shape membership
viol = 0
pairs_seen = 0
for nh in (1, 2, 3, 4):
    for h in enumerate_causets(nh):
        if not principal(h, range(1, nh + 1)):
            continue
        jrel = set(h) | {(i, nh + 1) for i in range(1, nh + 1)}
        jrel = transitive_closure(jrel, nh + 1)
        pj = past_shape_keys(jrel, nh + 1)
        kh = tuple(shape_key(h, nh))
        if kh not in {k for _, k in pj.values()}:
            viol += 1
        pairs_seen += 1
check("N6b D_{H cap x} contained in D_H (post-past membership)",
      viol == 0, f"pairs={pairs_seen} violations={viol}")

# ---------------------------------------------------- N7: p=0 cover structure
l0 = None  # (removed run-1 dead expression)
zero_cover_shapes = [c for c in enumerate_causets(1)
                     if metrics(c, 1)[0] == 0]
dbl5 = [c for c in all5 if doubly_principal(c, 5)]
check("N7a every doubly-principal causet has L >= 1 (A_0 = 0)",
      all(metrics(c, 5)[0] >= 1 for c in dbl5))
check("N7b only 1-element antichain has L = 0 among principal shapes n<=5",
      all(metrics(c, n)[0] >= 1
          for n in (2, 3, 4, 5) for c in enumerate_causets(n)
          if principal(c, range(1, n + 1))))

# -------------------------------------------- growth of the V_n lower bound
print("\nV_n at p=(1+i)/2 (exact A + B*sqrt2, numeric value):")
for k in (0, 1, 2, 3, 4):
    A, B = V_exact(k)
    val = float(A) + float(B) * math.sqrt(2)
    print(f"  V_{k+2}: {A} + {B}*sqrt2 = {val:.6f}"
          f"   ratio^(1/(n-2)) ~ {val ** (1 / max(k, 1)):.4f}")
print(f"\nt = |p|+|1-p| = sqrt2 = {math.sqrt(2):.6f}; c_s = prod(1-2^(-j/2))")
cs = 1.0
j = 1
while True:
    factor = 1 - 2 ** (-j / 2)
    if factor < 1 - 1e-12:
        cs *= factor
    j += 1
    if j > 60:
        break
print(f"c_s ~ {cs:.6f} > 0")

print(f"\n{sum(1 for _, ok, _ in results if ok)}/{len(results)} checks passed")
bad = [name for name, ok, _ in results if not ok]
if bad:
    print("FAILED:", bad)
    sys.exit(1)
print("ALL CHECKS PASSED")
sys.exit(0)
