"""Checks for research/time-direction/consolidation/RESULT.md.

Finite Markov worlds on times 0..T.  Float arithmetic with tolerance 1e-9,
except where noted.  No dependencies.

C1  Stationary chain, any kernel (reversible or not): H(X_A) = H(X_{T-A}) for
    every set of times A.  Amount-type quantities are mirror-symmetric.
C2  Stationary non-reversible chain: the reversed description is homogeneous
    (kernel K*), so homogeneity picks no production direction, although the
    two-time joint law is not symmetric (a value arrow is present).
C3  Bridge (distribution fixed at both ends): no homogeneous description in
    either direction.
C4  One boundary: sign of the openness imbalance
        D_t(n) = H(X_{t+1..t+n} | X_t) - H(X_{t-n..t-1} | X_t)
    (future more open than past when positive).  Doubly stochastic kernels and
    general positive kernels are tested separately; a counterexample is
    reported if found.
"""
import itertools
import math
import random

random.seed(1118)
TOL = 1e-9


def rdist(n, zero_ok=False):
    w = [random.random() if not zero_ok or random.random() > 0.3 else 0.0 for _ in range(n)]
    if sum(w) == 0:
        w[0] = 1.0
    s = sum(w)
    return [x / s for x in w]


def rkernel(n):
    return [rdist(n) for _ in range(n)]


def dskernel(n):
    perms = list(itertools.permutations(range(n)))
    w = rdist(len(perms))
    return [[sum(w[i] for i, p in enumerate(perms) if p[x] == y) for y in range(n)] for x in range(n)]


def stat(K, iters=5000):
    n = len(K)
    mu = [1.0 / n] * n
    for _ in range(iters):
        mu = [sum(mu[x] * K[x][y] for x in range(n)) for y in range(n)]
    return mu


def path_law(mu0, K, T):
    n = len(mu0)
    P = {}
    for path in itertools.product(range(n), repeat=T + 1):
        p = mu0[path[0]]
        for a, b in zip(path, path[1:]):
            p *= K[a][b]
        if p > 0:
            P[path] = p
    return P


def H_marg(P, A):
    m = {}
    for path, p in P.items():
        k = tuple(path[i] for i in A)
        m[k] = m.get(k, 0.0) + p
    return -sum(p * math.log2(p) for p in m.values() if p > 0)


def is_reversible(mu, K):
    n = len(K)
    return all(abs(mu[x] * K[x][y] - mu[y] * K[y][x]) < 1e-12 for x in range(n) for y in range(n))


def c1(trials=40, n=3, T=5):
    worst = 0.0
    for _ in range(trials):
        K = rkernel(n)
        pi = stat(K)
        P = path_law(pi, K, T)
        for r in range(1, T + 2):
            for A in itertools.combinations(range(T + 1), r):
                B = tuple(sorted(T - a for a in A))
                worst = max(worst, abs(H_marg(P, A) - H_marg(P, B)))
    assert worst < 1e-9, worst
    return trials, worst


def c2(trials=200, n=3):
    nonrev = 0
    for _ in range(trials):
        K = rkernel(n)
        pi = stat(K)
        Ks = [[pi[y] * K[y][x] / pi[x] for y in range(n)] for x in range(n)]
        # backward kernels of the stationary forward law equal Ks at every step
        mu = pi
        for _ in range(4):
            nxt = [sum(mu[x] * K[x][y] for x in range(n)) for y in range(n)]
            R = [[mu[x] * K[x][y] / nxt[y] for x in range(n)] for y in range(n)]
            assert all(abs(R[y][x] - Ks[y][x]) < 1e-9 for x in range(n) for y in range(n))
            mu = nxt
        nonrev += not is_reversible(pi, K)
    return trials, nonrev


def c3(trials=200, n=3, T=5):
    for _ in range(trials):
        K = rkernel(n)
        mu0 = rdist(n)
        end = random.randrange(n)
        P = {p: q for p, q in path_law(mu0, K, T).items() if p[-1] == end}
        Z = sum(P.values())
        P = {p: q / Z for p, q in P.items()}

        def kern(t, forward=True):
            pair, single = {}, {}
            for path, p in P.items():
                a, b = (path[t], path[t + 1]) if forward else (path[t + 1], path[t])
                pair[(a, b)] = pair.get((a, b), 0) + p
                single[a] = single.get(a, 0) + p
            return {k: v / single[k[0]] for k, v in pair.items()}

        fw = [kern(t) for t in range(T - 1)]
        bw = [kern(t, False) for t in range(1, T)]
        def same(a, b):
            return a.keys() == b.keys() and all(abs(a[k] - b[k]) < 1e-9 for k in a)
        assert not any(same(fw[t], fw[t + 1]) for t in range(T - 2))
        assert not any(same(bw[t], bw[t + 1]) for t in range(T - 2))
    return trials


def openness(P, t, n):
    fut = H_marg(P, list(range(t, t + n + 1))) - H_marg(P, [t])
    past = H_marg(P, list(range(t - n, t + 1))) - H_marg(P, [t])
    return fut - past


def c4(trials=300, n_states=3, T=6, win=2):
    out = {}
    for name, gen in (("doubly stochastic", dskernel), ("general positive", rkernel)):
        neg, example = 0, None
        for _ in range(trials):
            K = gen(n_states)
            mu0 = rdist(n_states, zero_ok=True)
            P = path_law(mu0, K, T)
            for t in range(win, T - win + 1):
                d = openness(P, t, win)
                if d < -TOL:
                    neg += 1
                    if example is None:
                        example = (K, mu0, t, d)
        out[name] = (neg, example)
    return out


if __name__ == "__main__":
    tr, w = c1()
    print(f"C1 stationary: {tr} random 3-state chains, all {2**6-1} time sets of 0..5; max |H(A)-H(mirror A)| = {w:.1e}: OK")
    tr, nr = c2()
    print(f"C2 stationary: {tr} chains ({nr} non-reversible); reversed description homogeneous with K* every time: OK")
    print(f"C3 bridges: {c3()} chains with fixed endpoint; no homogeneous description either way: OK")
    for name, (neg, ex) in c4().items():
        print(f"C4 one boundary, {name}: windows with past more open than future = {neg}")
        if ex:
            K, mu0, t, d = ex
            print("   example: mu0 =", [round(x, 3) for x in mu0], " t =", t, " D =", round(d, 4))
            print("   K =", [[round(x, 3) for x in row] for row in K])
