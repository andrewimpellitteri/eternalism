"""Records in chance worlds: two parts, S (event) and D (device), one bit each.

A world is (mu0, K) with K a kernel on the four joint states, run on t = 0..T.
For parts X, Y (X != Y) and lag n:
    trace_past(X<-Y)  = I(X_t ; Y_{t-n} | Y_t)   what X holds about Y's past beyond Y's present
    trace_fut(X->Y)   = I(X_t ; Y_{t+n} | Y_t)   the same toward Y's future
Label-free totals sum over both ordered pairs.

R0 delay line: S fresh fair bit each step, D <- previous S.  Stationary.
R1 stationary random kernels: does the label-free total mirror?  per-pair?
R2 stationary reversible kernels: everything mirrors (sanity).
R3 one boundary (fixed mu0), local noisy-copy kernels and random kernels:
   sign of (past total - future total).
"""
import itertools
import math
import random

random.seed(2026_11_18)
STATES = [(s, d) for s in (0, 1) for d in (0, 1)]
IDX = {st: i for i, st in enumerate(STATES)}


def rdist(n):
    w = [random.random() for _ in range(n)]
    s = sum(w)
    return [x / s for x in w]


def stat(K, iters=4000):
    mu = [0.25] * 4
    for _ in range(iters):
        mu = [sum(mu[x] * K[x][y] for x in range(4)) for y in range(4)]
    return mu


def paths(mu0, K, T):
    P = {}
    for p in itertools.product(range(4), repeat=T + 1):
        q = mu0[p[0]]
        for a, b in zip(p, p[1:]):
            q *= K[a][b]
            if q == 0:
                break
        if q > 0:
            P[p] = q
    return P


def H(P, coords):
    # coords: list of (time, part) with part 0 = S, 1 = D
    m = {}
    for p, q in P.items():
        k = tuple(STATES[p[t]][part] for t, part in coords)
        m[k] = m.get(k, 0.0) + q
    return -sum(q * math.log2(q) for q in m.values() if q > 0)


def cmi(P, a, b, c):
    return H(P, a + c) + H(P, b + c) - H(P, a + b + c) - H(P, c)


def traces(P, t, n):
    out = {}
    for X, Y in ((1, 0), (0, 1)):
        out[(X, Y, "past")] = cmi(P, [(t, X)], [(t - n, Y)], [(t, Y)])
        out[(X, Y, "fut")] = cmi(P, [(t, X)], [(t + n, Y)], [(t, Y)])
    past = out[(1, 0, "past")] + out[(0, 1, "past")]
    fut = out[(1, 0, "fut")] + out[(0, 1, "fut")]
    return out, past, fut


def kernel_from(fn):
    K = [[0.0] * 4 for _ in range(4)]
    for (s, d) in STATES:
        for (s2, d2), p in fn(s, d).items():
            K[IDX[(s, d)]][IDX[(s2, d2)]] += p
    return K


def delay_line():
    return kernel_from(lambda s, d: {(0, s): 0.5, (1, s): 0.5})


def noisy_copy(a, c, e):
    """S flips w.p. a.  D takes the old S w.p. c, else flips w.p. e."""
    def f(s, d):
        out = {}
        for s2, ps in ((s, 1 - a), (1 - s, a)):
            for d2, pd in ((s, c), (d, (1 - c) * (1 - e)), (1 - d, (1 - c) * e)):
                out[(s2, d2)] = out.get((s2, d2), 0) + ps * pd
        return out
    return kernel_from(f)


def reversible_kernel():
    # symmetric conductances w on edges, K = w / row sums: reversible w.r.t. row sums
    w = [[0.0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(i, 4):
            w[i][j] = w[j][i] = random.random()
    return [[w[i][j] / sum(w[i]) for j in range(4)] for i in range(4)]


def fmt(x):
    return f"{x:.3f}"


if __name__ == "__main__":
    T, t, n = 4, 2, 1
    K = delay_line()
    P = paths(stat(K), K, T)
    per, past, fut = traces(P, t, n)
    print("R0 delay line (stationary): D<-S past", fmt(per[(1, 0, 'past')]), "fut", fmt(per[(1, 0, 'fut')]),
          "| S<-D past", fmt(per[(0, 1, 'past')]), "fut", fmt(per[(0, 1, 'fut')]),
          "| totals", fmt(past), fmt(fut))

    worst_total, worst_pair = 0.0, 0.0
    for _ in range(300):
        K = [rdist(4) for _ in range(4)]
        P = paths(stat(K), K, T)
        per, past, fut = traces(P, t, n)
        worst_total = max(worst_total, abs(past - fut))
        worst_pair = max(worst_pair, abs(per[(1, 0, 'past')] - per[(1, 0, 'fut')]))
    print(f"R1 stationary random kernels (300): max |total past - total fut| = {worst_total:.2e};"
          f" max per-pair asymmetry = {worst_pair:.3f}")

    worst = 0.0
    for _ in range(200):
        K = reversible_kernel()
        P = paths(stat(K), K, T)
        per, past, fut = traces(P, t, n)
        worst = max(worst, abs(past - fut), max(abs(per[(X, Y, 'past')] - per[(X, Y, 'fut')]) for X, Y in ((1, 0), (0, 1))))
    print(f"R2 stationary reversible kernels (200): max asymmetry, totals and pairs = {worst:.2e}")

    T, t, n = 6, 3, 1
    blank = [0.5, 0.0, 0.5, 0.0]  # S uniform, D = 0
    for label, gen in (("noisy-copy", lambda: noisy_copy(random.uniform(0.05, 0.5), random.uniform(0.05, 0.95), random.uniform(0.0, 0.5))),
                       ("random", lambda: [rdist(4) for _ in range(4)])):
        neg, tot, ex = 0, 0, None
        for _ in range(300):
            K = gen()
            mu0 = blank if label == "noisy-copy" else rdist(4)
            P = paths(mu0, K, T)
            for tt in range(1, T):
                _, past, fut = traces(P, tt, n)
                # remove the stationary (law) part: compare with the same kernel run stationary
                tot += 1
                if past - fut < -1e-9:
                    neg += 1
                    if ex is None:
                        ex = (tt, past, fut)
        print(f"R3 one boundary, {label} kernels: windows with total trace pointing toward the boundary = {neg}/{tot}", ex and f"e.g. t={ex[0]} past={ex[1]:.4f} fut={ex[2]:.4f}")


def kernels_along(P, T, forward=True):
    ks = []
    for t in range(T):
        pair, single = {}, {}
        for p, q in P.items():
            a, b = (p[t], p[t + 1]) if forward else (p[t + 1], p[t])
            pair[(a, b)] = pair.get((a, b), 0) + q
            single[a] = single.get(a, 0) + q
        ks.append({k: v / single[k[0]] for k, v in pair.items()})
    return ks


def homogeneous(ks, tol=1e-9):
    """Rows are compared where both steps define them (the conditioning state has mass)."""
    for a, b in zip(ks, ks[1:]):
        rows = {k[0] for k in a} & {k[0] for k in b}
        for r in rows:
            for y in range(4):
                if abs(a.get((r, y), 0.0) - b.get((r, y), 0.0)) > tol:
                    return False
    return True


def r4(T=7, t=3):
    """End boundary: stationary noisy-copy world conditioned on (S,D) = (0,0) at T.
    Production direction (homogeneity) runs backward from T; does D still record S
    in the forward sense?"""
    K = noisy_copy(0.3, 0.9, 0.0)
    P = paths(stat(K), K, T)
    P = {p: q for p, q in P.items() if p[-1] == IDX[(0, 0)]}
    Z = sum(P.values()); P = {p: q / Z for p, q in P.items()}
    fw, bw = kernels_along(P, T, True), kernels_along(P, T, False)
    per, _, _ = traces(P, t, 1)
    return homogeneous(fw), homogeneous(bw), per


if __name__ == "__main__":
    hf, hb, per = r4()
    print(f"R4 end boundary (noisy copy conditioned at T=7): forward homogeneous={hf}, backward homogeneous={hb};"
          f" at t=3 D rec S {per[(1, 0, 'past')]:.3f}, D fc S {per[(1, 0, 'fut')]:.3f}")
