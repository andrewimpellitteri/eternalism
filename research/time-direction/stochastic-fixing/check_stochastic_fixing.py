"""Exact finite checks for the stochastic-fixing note. Standard library only.

Probabilities are Fractions; entropies and divergences are floats computed from them.
Every assert is over the stated finite example only. Nothing here is a proof.
Run: python3 check_stochastic_fixing.py
"""
from fractions import Fraction as Fr
from itertools import product, permutations, combinations
from math import log2, inf

F = Fr


# ---------- generic tools ----------
def stationary(K):
    """Exact stationary distribution of an irreducible kernel (Gaussian elimination)."""
    n = len(K)
    A = [[K[j][i] - (1 if i == j else 0) for j in range(n)] + [F(0)] for i in range(n)]
    A[-1] = [F(1)] * n + [F(1)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        A[c] = [v / A[c][c] for v in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                A[r] = [a - A[r][c] * b for a, b in zip(A[r], A[c])]
    pi = [A[i][n] for i in range(n)]
    assert all(sum(pi[i] * K[i][j] for i in range(n)) == pi[j] for j in range(n))
    return pi


def H(ps):
    return -sum(float(p) * log2(float(p)) for p in ps if p > 0)


def paths(mu, K, n):
    """Path measure on times 0..n as {path: prob}, zero-probability paths omitted."""
    out = {}
    for w in product(range(len(K)), repeat=n + 1):
        p = mu[w[0]]
        for a, b in zip(w, w[1:]):
            p *= K[a][b]
        if p:
            out[w] = p
    return out


def marg(P, A):
    """Law of the reading on the set of times A."""
    out = {}
    for w, p in P.items():
        k = tuple(w[t] for t in A)
        out[k] = out.get(k, 0) + p
    return out


def Hset(P, A):
    return H(marg(P, A).values())


def common_part(P, A, C):
    """Exact quantities shared by regions A and C: the connected components of the
    bipartite graph on (values of X_A, values of X_C) whose edges are the possible
    pairs. Returns the partition of X_A values (Gacs-Korner common part)."""
    parent = {}

    def find(x):
        while parent.setdefault(x, x) != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for w in P:
        a, c = ('A',) + tuple(w[t] for t in A), ('C',) + tuple(w[t] for t in C)
        parent[find(a)] = find(c)
    cls = {}
    for x in list(parent):
        if x[0] == 'A':
            cls.setdefault(find(x), []).append(x[1:])
    return sorted(sorted(v) for v in cls.values())


def fixes(P, A, t):
    """Is the reading at time t a probability-one function of the reading on A?"""
    seen = {}
    return all(seen.setdefault(tuple(w[s] for s in A), w[t]) == w[t] for w in P)


def joint2(pi, K):
    n = len(K)
    return [[pi[i] * K[i][j] for j in range(n)] for i in range(n)]


def reversed_kernel(pi, K):
    n = len(K)
    return [[pi[j] * K[j][i] / pi[i] for j in range(n)] for i in range(n)]


def ep_rate(pi, K):
    """Entropy production per step in bits: sum J(x,y) log2(J(x,y)/J(y,x))."""
    J = joint2(pi, K)
    s = 0.0
    for i in range(len(K)):
        for j in range(len(K)):
            if J[i][j]:
                if not J[j][i]:
                    return inf
                s += float(J[i][j]) * log2(float(J[i][j] / J[j][i]))
    return s


def reversing_relabellings(pi, K):
    """All bijections e of the state space with J(e(y), e(x)) = J(x, y):
    the law of (e(X_{-t})) equals the law of (X_t)."""
    J = joint2(pi, K)
    n = len(K)
    return [e for e in permutations(range(n))
            if all(J[e[j]][e[i]] == J[i][j] for i in range(n) for j in range(n))]


def row_classes(pi, K):
    """Probabilities of the classes of states with equal rows. For a chain read in
    full these are the causal states (minimal sufficient statistic of the past for
    the future)."""
    cls = {}
    for i, row in enumerate(K):
        cls[tuple(row)] = cls.get(tuple(row), 0) + pi[i]
    return list(cls.values())


def mirror_entropy_gap(P, n):
    """Largest |H(X_A) - H(X_{n-A})| over all sets of times A in 0..n."""
    g = 0.0
    for k in range(1, n + 2):
        for A in combinations(range(n + 1), k):
            g = max(g, abs(Hset(P, A) - Hset(P, tuple(sorted(n - t for t in A)))))
    return g


def KL_path_reversal(P):
    s = 0.0
    for w, p in P.items():
        q = P.get(w[::-1], 0)
        if not q:
            return inf
        s += float(p) * log2(float(p / q))
    return s


def report(name, K, n=4):
    pi = stationary(K)
    Ks = reversed_kernel(pi, K)
    P = paths(pi, K, n)
    fwd = sum(float(pi[i]) * H(K[i]) for i in range(len(K)))
    bwd = sum(float(pi[i]) * H(Ks[i]) for i in range(len(K)))
    Cp, Cm = H(row_classes(pi, K)), H(row_classes(pi, Ks))
    print(f"\n== {name}")
    print("  stationary law:", [str(p) for p in pi])
    print("  detailed balance:", Ks == K, "| entropy production (bits/step):", round(ep_rate(pi, K), 6))
    print(f"  KL(path || reversed path) on 0..{n}:", round(KL_path_reversal(P), 6))
    print("  reversing relabellings:", reversing_relabellings(pi, K))
    print("  statewise openness (next | x):", [round(H(r), 4) for r in K])
    print("  statewise openness (prev | x):", [round(H(r), 4) for r in Ks])
    print("  averaged: next", round(fwd, 6), "prev", round(bwd, 6))
    print("  C+ =", round(Cp, 6), " C- =", round(Cm, 6), " Xi =", round(Cp - Cm, 6))
    print("  largest mirror gap in region entropies:", f"{mirror_entropy_gap(P, n):.1e}")
    print("  shared exact quantities of X_0 and X_k, k=1..4 (classes of X_0 values):")
    for k in range(1, n + 1):
        print("    k =", k, [[v[0] for v in c] for c in common_part(P, (0,), (k,))])
    assert abs(fwd - bwd) < 1e-12
    assert mirror_entropy_gap(P, n) < 1e-9
    # reciprocity: the two partitions induce the same events
    for k in range(1, n + 1):
        a, c = common_part(P, (0,), (k,)), common_part(P, (k,), (0,))
        assert len(a) == len(c)
    return pi, Ks, P


# ---------- E1: biased 3-cycle (Norris, Example 1.9.4) ----------
E1 = [[F(0), F(2, 3), F(1, 3)], [F(1, 3), F(0), F(2, 3)], [F(2, 3), F(1, 3), F(0)]]
pi, Ks, P = report("E1 biased 3-cycle, stationary, not reversible", E1)
assert Ks != E1 and reversing_relabellings(pi, E1)          # arrow, but mirrored by a reflection
assert abs(ep_rate(pi, E1) - 1 / 3) < 1e-12
assert abs(KL_path_reversal(P) - 4 / 3) < 1e-9              # n * e_p, extensive
print("  P(0,1,2) =", marg(P, (0, 1, 2))[(0, 1, 2)], " P(2,1,0) =", marg(P, (0, 1, 2))[(2, 1, 0)])

# ---------- E2: positive kernel, no reversing relabelling, Xi != 0 ----------
E2 = [[F(1, 2), F(1, 3), F(1, 6)], [F(1, 2), F(1, 4), F(1, 4)], [F(1, 2), F(1, 4), F(1, 4)]]
pi, Ks, P = report("E2 positive kernel, two states with equal rows", E2)
assert Ks != E2 and not reversing_relabellings(pi, E2)
assert H(row_classes(pi, E2)) < H(row_classes(pi, Ks)) - 0.1
assert all(len(common_part(P, (0,), (k,))) == 1 for k in range(1, 5))  # nothing fixed exactly

# ---------- E2b: generic positive kernel, no reversing relabelling, Xi = 0 ----------
E2b = [[F(1, 2), F(1, 3), F(1, 6)], [F(1, 6), F(1, 2), F(1, 3)], [F(1, 4), F(1, 4), F(1, 2)]]
pi, Ks, P = report("E2b generic positive kernel", E2b)
assert Ks != E2b and not reversing_relabellings(pi, E2b)
assert abs(H(row_classes(pi, E2b)) - H(row_classes(pi, Ks))) < 1e-12

# ---------- E3: support-driven statewise asymmetry ----------
E3 = [[F(0), F(1, 2), F(1, 2)], [F(0), F(0), F(1)], [F(1), F(0), F(0)]]
pi, Ks, P = report("E3 0->{1,2}, 1->2, 2->0", E3)
assert H(E3[0]) == 1.0 and H(Ks[0]) == 0.0   # given X=0: past fixed, future open
assert H(E3[2]) == 0.0 and H(Ks[2]) == 1.0   # given X=2: the reverse
assert common_part(P, (0,), (1,)) == [[(0,), (1,)], [(2,)]]  # [X_0=2] = [X_1=0] is shared

# ---------- E4: biased 4-cycle, period 2: the shared quantity is the phase ----------
E4 = [[F(0)] * 4 for _ in range(4)]
for i in range(4):
    E4[i][(i + 1) % 4], E4[i][(i - 1) % 4] = F(2, 3), F(1, 3)
pi, Ks, P = report("E4 biased 4-cycle (period 2)", E4)
assert all(common_part(P, (0,), (k,)) == [[(0,), (2,)], [(1,), (3,)]] for k in range(1, 5))

# ---------- E5: boundary arrow. Reversible kernel, non-stationary start ----------
print("\n== E5 reversible kernel, start (7/8,1/16,1/16): boundary arrow")
E5 = [[F(1, 2), F(1, 4), F(1, 4)], [F(1, 4), F(1, 2), F(1, 4)], [F(1, 4), F(1, 4), F(1, 2)]]
pi5 = stationary(E5)
assert reversed_kernel(pi5, E5) == E5 and ep_rate(pi5, E5) == 0.0
mu = [F(7, 8), F(1, 16), F(1, 16)]
bound = sum(float(m) * log2(float(m / p)) for m, p in zip(mu, pi5)) \
    + sum(float(p) * log2(float(p / m)) for m, p in zip(mu, pi5))
print("  n | KL(path||reversed) | closed form | H(Xn|X0)-H(X0|Xn) | H(mu_n)-H(mu_0)")
for n in range(1, 8):
    P = paths(mu, E5, n)
    mun = marg(P, (n,))
    kl = KL_path_reversal(P)
    closed = sum(float(m) * log2(float(m / p)) for m, p in zip(mu, pi5)) \
        - sum(float(mun[(x,)]) * log2(float(mu[x] / pi5[x])) for x in range(3))
    bal = (Hset(P, (0, n)) - Hset(P, (0,))) - (Hset(P, (0, n)) - Hset(P, (n,)))
    dH = H(mun.values()) - H(mu)
    print(f"  {n} | {kl:.6f} | {closed:.6f} | {bal:.6f} | {dH:.6f}")
    assert abs(kl - closed) < 1e-9 and abs(bal - dH) < 1e-9 and kl < bound and bal > 0
print("  bound D(mu||pi)+D(pi||mu) =", round(bound, 6), "(the path divergence never exceeds it)")
print("  compare E1: divergence grows as n/3 bits and the balance is 0 at every n")

# ---------- E6: coarse readings. X_{t+3} = X_t xor X_{t+1}, uniform, stationary ----------
print("\n== E6 X_{t+3} = X_t xor X_{t+1} on uniform bits (stationary, deterministic, invertible)")
P6 = {}
for a, b, c in product((0, 1), repeat=3):
    w = [a, b, c]
    while len(w) < 7:
        w.append(w[-3] ^ w[-2])
    P6[tuple(w)] = F(1, 8)
for s in (1, 2, 3):   # stationarity of every window that fits
    for L in (1, 2, 3, 4):
        assert marg(P6, tuple(range(L))) == marg(P6, tuple(range(s, s + L)))
print("  {0,1} fixes X_3:", fixes(P6, (0, 1), 3), "| mirror image, {2,3} fixes X_0:", fixes(P6, (2, 3), 0))
print("  H(X0,X1,X3) =", Hset(P6, (0, 1, 3)), " H(X0,X2,X3) =", Hset(P6, (0, 2, 3)))
print("  shared quantities of {0,1} and {3}:", common_part(P6, (0, 1), (3,)), "<->", common_part(P6, (3,), (0, 1)))
assert fixes(P6, (0, 1), 3) and not fixes(P6, (2, 3), 0)
assert len(common_part(P6, (0, 1), (3,))) == len(common_part(P6, (3,), (0, 1))) == 2

# ---------- E7: records of a noisy readout (classical shadow of the collapse claim) ----------
print("\n== E7 records r_1..r_4 of a hidden chain through a noisy readout")
R = [[F(3, 4) if i == j else F(1, 8) for j in range(3)] for i in range(3)]


def record_law(mu, K, n):
    out = {}
    for w, p in paths(mu, K, n).items():
        for r in product(range(3), repeat=n):
            q = p
            for t in range(n):
                q *= R[w[t + 1]][r[t]]
            out[r] = out.get(r, 0) + q
    return out


def asym(L, e=(0, 1, 2)):
    return max(abs(p - L[tuple(e[x] for x in r[::-1])]) for r, p in L.items())


u = [F(1, 3)] * 3
a = asym(record_law(u, E5, 4)); print("  symmetric kernel, uniform start: max |P(r)-P(reversed r)| =", a); assert a == 0
a = asym(record_law(mu, E5, 4)); print("  symmetric kernel, start mu     :", a, "~", round(float(a), 5)); assert a > 0
a = asym(record_law(u, E1, 4)); print("  biased cycle, uniform start    :", a, "~", round(float(a), 5)); assert a > 0
a = asym(record_law(u, E1, 4), e=(0, 2, 1)); print("  biased cycle, reversed and reflected:", a); assert a == 0
a = min(asym(record_law(stationary(E2b), E2b, 4), e=e) for e in permutations(range(3)))
print("  generic kernel E2b, stationary start, best relabelling:", a, "~", round(float(a), 5)); assert a > 0

# ---------- arithmetic of the published RIP example (Crutchfield-Ellison-Mahoney, p.4) ----------
Cp = H([F(2, 5), F(1, 5), F(2, 5)]); Cm = H([F(2, 5), F(3, 10), F(1, 10), F(1, 5)])
print(f"\n== RIP at p=q=1/2 from the published state laws: C+ = {Cp:.4f}, C- = {Cm:.4f}, Xi = {Cp - Cm:.4f}")
assert abs(Cp - 1.5219) < 1e-4 and abs(Cm - 1.8464) < 1e-4
print("\nall checks passed")
