"""Cross-lane consistency audit of the finite-world arrow claims.

Each lane checked its own claim on its own models. Here the claims are restated
as predicates, at the scope their prose gives them, and evaluated on one shared
corpus that includes worlds no single lane used: kernels with zero entries,
coarse-grained (hidden-Markov, non-Markov) stationary processes, and macro images
of time-reversal-symmetric permutation dynamics.

A1  Consolidation claim 3, as worded: "A chance law can be described homogeneously
    in exactly one direction, the one leading away from a single boundary."
A2  Consolidation table, deterministic-reversible row: production direction
    "None, even with a boundary".
A3  Consolidation claim 2: "A law arrow on its own leaves every amount of whole
    time slices mirror-symmetric" (C1 checked Markov chains only), read together
    with claim 6 (law arrows are label arrows, i.e. coarse-grained images).
A4  Claim 1 and claim 6: if the reversal map preserves the coarse-graining (up to
    relabelling), every macro arrow vanishes; if not, arrows can appear.
A5  Chance records, "a reversible kernel gives no record arrow of any kind":
    larger parts, lag 2, and coarse-grained images.
A6  Consolidation claim 4: relative entropy to equilibrium never rises away from
    a boundary; tested on kernels with zero entries.

Pure Python, floating point, tolerance 1e-9. Seeds fixed.
"""
import itertools
import math
import random

TOL = 1e-9


# ---------- processes as path distributions ----------

def markov_paths(mu0, K, T):
    n = len(mu0)
    P = {(x,): p for x, p in enumerate(mu0) if p > 0}
    for _ in range(T):
        Q = {}
        for path, p in P.items():
            for y in range(n):
                q = p * K[path[-1]][y]
                if q > 0:
                    Q[path + (y,)] = Q.get(path + (y,), 0.0) + q
        P = Q
    return P


def perm_paths(mu0, U, T):
    P = {}
    for x, p in enumerate(mu0):
        if p > 0:
            path = [x]
            for _ in range(T):
                path.append(U[path[-1]])
            P[tuple(path)] = P.get(tuple(path), 0.0) + p
    return P


def image(P, f):
    Q = {}
    for path, p in P.items():
        k = tuple(f[x] for x in path)
        Q[k] = Q.get(k, 0.0) + p
    return Q


def condition_end(P, ok):
    Q = {k: p for k, p in P.items() if ok(k[-1])}
    Z = sum(Q.values())
    return {k: p / Z for k, p in Q.items()}


def marg(P, idx):
    Q = {}
    for path, p in P.items():
        k = tuple(path[i] for i in idx)
        Q[k] = Q.get(k, 0.0) + p
    return Q


def H(P, idx):
    return -sum(p * math.log2(p) for p in marg(P, idx).values() if p > 0)


def one_step(P, t, forward):
    """Conditional law of X_{t+1} given X_t (forward) or of X_t given X_{t+1}."""
    J = marg(P, (t, t + 1))
    rows = {}
    for (a, b), p in J.items():
        r, c = (a, b) if forward else (b, a)
        rows.setdefault(r, {})
        rows[r][c] = rows[r].get(c, 0.0) + p
    return {r: {c: q / sum(d.values()) for c, q in d.items()} for r, d in rows.items()}


def same_rows(a, b):
    for r in set(a) & set(b):
        for c in set(a[r]) | set(b[r]):
            if abs(a[r].get(c, 0.0) - b[r].get(c, 0.0)) > TOL:
                return False
    return True


def homog_pairs(P, T, forward):
    """For each t, whether the one-step description at t equals that at t+1."""
    ks = [one_step(P, t, forward) for t in range(T)]
    return [same_rows(a, b) for a, b in zip(ks, ks[1:])]


def cmi(P, x, y, z):
    """I(X;Y|Z) for index tuples into the path."""
    return H(P, x + z) + H(P, y + z) - H(P, x + y + z) - H(P, z)


# ---------- random worlds ----------

def rand_kernel(rng, n, pzero=0.0):
    K = []
    for _ in range(n):
        row = [0.0 if rng.random() < pzero else rng.random() + 0.01 for _ in range(n)]
        if sum(row) == 0:
            row[rng.randrange(n)] = 1.0
        s = sum(row)
        K.append([v / s for v in row])
    return K


def step(mu, K):
    n = len(mu)
    return [sum(mu[x] * K[x][y] for x in range(n)) for y in range(n)]


def stationary(K, iters=5000):
    n = len(K)
    mu = [1.0 / n] * n
    for _ in range(iters):
        mu = [0.5 * a + 0.5 * b for a, b in zip(mu, step(mu, K))]  # lazy, kills periodicity
    return mu


def rand_dist(rng, n):
    v = [rng.random() for _ in range(n)]
    s = sum(v)
    return [x / s for x in v]


def rand_involution(rng, n):
    xs = list(range(n))
    rng.shuffle(xs)
    inv = list(range(n))
    i = 0
    while i + 1 < n:
        if rng.random() < 0.7:
            a, b = xs[i], xs[i + 1]
            inv[a], inv[b] = b, a
        i += 2
    return inv


def symmetric_perm(rng, n):
    """U = R2 R1 from two involutions, so R1 U R1 = U^{-1}: exactly reversal-symmetric."""
    R1, R2 = rand_involution(rng, n), rand_involution(rng, n)
    U = [R2[R1[x]] for x in range(n)]
    Uinv = [0] * n
    for x in range(n):
        Uinv[U[x]] = x
    assert all(R1[U[R1[x]]] == Uinv[x] for x in range(n))
    return U, R1


def preserved_up_to_relabel(f, eps):
    """eps maps each block of f onto a block of f."""
    blocks = {}
    for x, b in enumerate(f):
        blocks.setdefault(b, set()).add(x)
    return all(len({f[eps[x]] for x in xs}) == 1 for xs in blocks.values())


def eps_preserving_partition(rng, eps, k):
    """Random partition whose blocks are unions of eps-orbits."""
    n = len(eps)
    f = [None] * n
    for x in range(n):
        if f[x] is None:
            b = rng.randrange(k)
            f[x] = f[eps[x]] = b
    return f


def mirror_gap(P, T):
    worst = 0.0
    for r in range(1, T + 2):
        for A in itertools.combinations(range(T + 1), r):
            B = tuple(sorted(T - a for a in A))
            worst = max(worst, abs(H(P, A) - H(P, B)))
    return worst


# ---------- audits ----------

def a1(rng, trials=400, T=6):
    """Single start boundary; does backward homogeneity ever occur?"""
    out = {}
    for label, pz in (("positive", 0.0), ("zero entries", 0.45)):
        whole, some, converse_fail = 0, 0, 0
        for _ in range(trials):
            n = rng.choice((3, 4))
            K = rand_kernel(rng, n, pz)
            mu0 = [0.0] * n
            mu0[rng.randrange(n)] = 1.0  # sharp boundary
            P = markov_paths(mu0, K, T)
            hb = homog_pairs(P, T, False)
            whole += all(hb)
            some += any(hb)
            mus = [mu0]
            for _ in range(T):
                mus.append(step(mus[-1], K))
            for t, h in enumerate(hb):
                moving = max(abs(a - b) for a, b in zip(mus[t + 1], mus[t + 2])) > TOL
                if h and moving:
                    converse_fail += 1
                    break
        out[label] = (trials, whole, some, converse_fail)
    return out


def a2(rng, trials=300, T=6):
    """Reversal-symmetric permutations with a macro boundary at the start.
    Micro: does homogeneity pick a direction?  Macro: counts of (both, neither, exactly one)."""
    micro_dir, both, neither, one = 0, 0, 0, 0
    for _ in range(trials):
        n = rng.choice((8, 10, 12))
        U, eps = symmetric_perm(rng, n)
        f = [rng.randrange(2) for _ in range(n)]
        if len(set(f)) < 2:
            continue
        b = f[0]
        mu0 = [1.0 if f[x] == b else 0.0 for x in range(n)]
        s = sum(mu0)
        mu0 = [v / s for v in mu0]
        P = perm_paths(mu0, U, T)
        micro_dir += all(homog_pairs(P, T, True)) != all(homog_pairs(P, T, False))
        Q = image(P, f)
        fw, bw = all(homog_pairs(Q, T, True)), all(homog_pairs(Q, T, False))
        both += fw and bw
        neither += (not fw) and (not bw)
        one += fw != bw
    return micro_dir, both, neither, one


def a3_exact():
    """Smallest example found: a 6-cycle read through the cyclic word 2 0 0 1 1 1, uniform phase.
    Stationary, no boundary, and the rotation is reversal-symmetric (any reflection of the cycle
    conjugates it to its inverse). Returns the patterns of (X0, X1, X3) and of the mirror
    set (X1, X3, X4) for T = 4."""
    word = (2, 0, 0, 1, 1, 1)
    n = len(word)
    fwd = [(word[i], word[(i + 1) % n], word[(i + 3) % n]) for i in range(n)]
    mir = [(word[(i + 1) % n], word[(i + 3) % n], word[(i + 4) % n]) for i in range(n)]
    def ent(xs):
        c = {}
        for x in xs:
            c[x] = c.get(x, 0) + 1
        return -sum(v / n * math.log2(v / n) for v in c.values())
    return len(set(fwd)), len(set(mir)), ent(fwd), ent(mir)


def a3(rng, trials=200, T=5):
    """Stationary coarse-grained processes: are whole-slice entropies mirror-symmetric?"""
    res = {}
    # (i) Markov, any kernel: C1 again, as a control
    worst = 0.0
    for _ in range(trials // 2):
        K = rand_kernel(rng, 3, 0.2)
        worst = max(worst, mirror_gap(markov_paths(stationary(K), K, T), T))
    res["Markov (control)"] = (trials // 2, worst)
    # (ii) hidden Markov: stationary chain on 4 states seen through a 2-block partition
    worst, count, n_viol = 0.0, 0, 0
    for _ in range(trials):
        K = rand_kernel(rng, 4, 0.3)
        f = [0, 0, 1, 1]
        g = mirror_gap(image(markov_paths(stationary(K), K, T), f), T)
        count += 1
        n_viol += g > 1e-6
        worst = max(worst, g)
    res["hidden Markov"] = (count, worst, n_viol)
    # (iii) reversal-symmetric permutation, uniform (stationary, no boundary), coarse-grained
    worst, count, n_viol = 0.0, 0, 0
    for _ in range(trials):
        n = rng.choice((8, 10, 12))
        U, eps = symmetric_perm(rng, n)
        f = [rng.randrange(3) for _ in range(n)]
        g = mirror_gap(image(perm_paths([1.0 / n] * n, U, T), f), T)
        count += 1
        n_viol += g > 1e-6
        worst = max(worst, g)
    res["symmetric permutation, coarse"] = (count, worst, n_viol)
    return res


def two_time_asym(Q, t, lag):
    J = marg(Q, (t, t + lag))
    return max(abs(p - J.get((b, a), 0.0)) for (a, b), p in J.items())


def a4(rng, trials=300, T=5):
    """eps-preserved partition => no macro arrow (entropies and two-time law, up to relabel);
    unpreserved => arrows possible."""
    pres_worst, unpres_worst, unpres_arrows, pres_n, unpres_n = 0.0, 0.0, 0, 0, 0
    for _ in range(trials):
        n = rng.choice((8, 10, 12))
        U, eps = symmetric_perm(rng, n)
        P = perm_paths([1.0 / n] * n, U, T)
        if rng.random() < 0.5:
            f = eps_preserving_partition(rng, eps, 3)
        else:
            f = [rng.randrange(3) for _ in range(n)]
        Q = image(P, f)
        g = mirror_gap(Q, T)
        if preserved_up_to_relabel(f, eps):
            pres_n += 1
            # labels fixed blockwise by construction here, so the two-time law must be symmetric
            fixed = all(f[eps[x]] == f[x] for x in range(n))
            a = two_time_asym(Q, 1, 1) if fixed else 0.0
            pres_worst = max(pres_worst, g, a)
        else:
            unpres_n += 1
            a = max(g, two_time_asym(Q, 1, 1))
            unpres_worst = max(unpres_worst, a)
            unpres_arrows += a > 1e-6
    return pres_n, pres_worst, unpres_n, unpres_arrows, unpres_worst


def reversible_kernel(rng, n):
    """Metropolis kernel for a random target and symmetric proposal."""
    pi = rand_dist(rng, n)
    W = [[0.0] * n for _ in range(n)]
    for x in range(n):
        for y in range(x + 1, n):
            w = rng.random()
            W[x][y] = W[y][x] = w
    K = [[0.0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if x != y:
                K[x][y] = W[x][y] / n * min(1.0, pi[y] / pi[x])
        K[x][x] = 1.0 - sum(K[x])
    return pi, K


def a5(rng, trials=100, T=6):
    """Stationary reversible chains on a 2x3 product (S = x // 3, D = x % 3): record equals
    forecast for both ordered pairs at lags 1 and 2. Then a coarse-graining of the same chains:
    mirror gap and two-time asymmetry."""
    worst = 0.0
    t = 3
    for _ in range(trials):
        pi, K = reversible_kernel(rng, 6)
        P = markov_paths(pi, K, T)
        for xi, yi in ((0, 1), (1, 0)):
            XY = {}
            for path, p in P.items():
                k = tuple(((x // 3, x % 3)[xi], (x // 3, x % 3)[yi]) for x in path)
                XY[k] = XY.get(k, 0.0) + p
            for lag in (1, 2):
                rec = cmi_parts(XY, t, (t - lag,), (t,))
                fc = cmi_parts(XY, t, (t + lag,), (t,))
                worst = max(worst, abs(rec - fc))
    cworst = 0.0
    for _ in range(trials):
        pi, K = reversible_kernel(rng, 6)
        Q = image(markov_paths(pi, K, 5), [0, 0, 1, 2, 2, 1])
        cworst = max(cworst, mirror_gap(Q, 5), two_time_asym(Q, 1, 2))
    return trials, worst, cworst


def Hpair(XY, spec):
    """spec: list of (time, which) with which 0 = X part, 1 = Y part."""
    Q = {}
    for path, p in XY.items():
        k = tuple(path[t][w] for t, w in spec)
        Q[k] = Q.get(k, 0.0) + p
    return -sum(p * math.log2(p) for p in Q.values() if p > 0)


def cmi_parts(XY, xi_t, y_ts, z):
    """I(X_{xi_t}; Y_{y_ts} | Y_z)."""
    x = [(xi_t, 0)]
    y = [(t, 1) for t in y_ts]
    zz = [(t, 1) for t in z]
    return Hpair(XY, x + zz) + Hpair(XY, y + zz) - Hpair(XY, x + y + zz) - Hpair(XY, zz)


def kl(p, q):
    s = 0.0
    for a, b in zip(p, q):
        if a > 0:
            if b <= 0:
                return math.inf
            s += a * math.log2(a / b)
    return s


def a6(rng, trials=400, T=10):
    rises, tested = 0, 0
    for _ in range(trials):
        n = rng.choice((3, 4))
        K = rand_kernel(rng, n, 0.45)
        pi = stationary(K)
        if max(abs(a - b) for a, b in zip(step(pi, K), pi)) > 1e-9:
            continue
        mu = rand_dist(rng, n)
        d = [kl(mu, pi)]
        for _ in range(T):
            mu = step(mu, K)
            d.append(kl(mu, pi))
        tested += 1
        rises += any(b > a + 1e-9 for a, b in zip(d, d[1:]) if a != math.inf)
    return tested, rises


if __name__ == "__main__":
    rng = random.Random(20261119)
    print("A1  single start boundary, backward homogeneity (trials, whole run, some pair, pair while mu moving)")
    for k, v in a1(rng).items():
        print(f"    {k:13s} {v}")
    mi, both, neither, one = a2(rng)
    print(f"A2  symmetric permutations, macro start boundary: micro picks a direction {mi}; "
          f"macro homogeneous both ways {both}, neither {neither}, exactly one {one}")
    print("A3' exact: distinct patterns and entropy, (X0,X1,X3) vs mirror (X1,X3,X4):", a3_exact())
    print("A3  stationary, mirror gap max |H(X_A) - H(X_mirrorA)| over all time sets")
    for k, v in a3(rng).items():
        print(f"    {k:30s} {v}")
    pn, pw, un, ua, uw = a4(rng)
    print(f"A4  eps-preserved partitions: {pn}, worst asymmetry {pw:.2e}; "
          f"unpreserved: {un}, with an arrow {ua}, worst {uw:.3f}")
    t, w, cw = a5(rng)
    print(f"A5  reversible stationary, 2x3 parts, lags 1-2: {t} kernels, worst |record-forecast| {w:.2e}; "
          f"coarse-grained worst asymmetry {cw:.2e}")
    tested, rises = a6(rng)
    print(f"A6  zero-entry kernels: {tested} tested, relative entropy rises in {rises}")
