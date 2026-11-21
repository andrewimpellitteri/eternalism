"""Finite checks for research/time-direction/m-arrows/RESULT.md.

Exact rational arithmetic (fractions) throughout, no dependencies.

A Markov world is (mu0, K): an initial distribution and a time-homogeneous kernel
K[x][y] = P(X_{t+1}=y | X_t=x), run on t = 0..T.  Read right to left, the same
path measure has backward kernels R_t[y][x] = mu_t(x) K[x][y] / mu_{t+1}(y).

Checks
  1. Lemma: K strictly positive => R_t == R_{t+1} iff mu_t is stationary.
  2. Deterministic (permutation) K: R_t is the inverse permutation at every t,
     whatever mu0.  Homogeneity picks no direction.
  3. Relative entropy D(mu_t || pi) is non-increasing in the direction the
     kernel is homogeneous; Shannon entropy is non-decreasing when K is doubly
     stochastic.
  4. Janus world: a boundary distribution at t = 0 and the same kernel run
     outward on both sides.  Any single orientation has inhomogeneous kernels on
     one side; the homogeneous direction flips at 0 and agrees with the
     relative-entropy decrease on both sides.
  5. The rank-one corner: a positive kernel can reach stationarity in one step,
     after which the backward kernels are homogeneous.
"""
from fractions import Fraction as F
import itertools
import math
import random

random.seed(20261118)


def step(mu, K):
    n = len(mu)
    return [sum(mu[x] * K[x][y] for x in range(n)) for y in range(n)]


def backward(mu_t, mu_t1, K):
    n = len(mu_t)
    return tuple(
        tuple((mu_t[x] * K[x][y] / mu_t1[y]) if mu_t1[y] != 0 else None for x in range(n))
        for y in range(n)
    )


def rand_dist(n, zero_ok=False):
    w = [F(random.randint(0 if zero_ok else 1, 9)) for _ in range(n)]
    if sum(w) == 0:
        w[0] = F(1)
    s = sum(w)
    return [x / s for x in w]


def rand_pos_kernel(n):
    return [rand_dist(n) for _ in range(n)]


def stationary(K):
    # solve pi K = pi, sum pi = 1, by Gaussian elimination over fractions
    n = len(K)
    A = [[K[x][y] - (1 if x == y else 0) for x in range(n)] for y in range(n)]
    A[-1] = [F(1)] * n
    b = [F(0)] * (n - 1) + [F(1)]
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c] / M[c][c]
                M[r] = [a - f * bb for a, bb in zip(M[r], M[c])]
    return [M[i][n] / M[i][i] for i in range(n)]


def rel_ent(mu, pi):
    return sum(float(m) * math.log2(float(m) / float(p)) for m, p in zip(mu, pi) if m > 0)


def shannon(mu):
    return -sum(float(m) * math.log2(float(m)) for m in mu if m > 0)


def check_lemma(trials=400, n=3, T=4):
    hits = 0
    for _ in range(trials):
        K = rand_pos_kernel(n)
        pi = stationary(K)
        mu0 = pi[:] if random.random() < 0.15 else rand_dist(n, zero_ok=True)
        mus = [mu0]
        for _ in range(T):
            mus.append(step(mus[-1], K))
        Rs = [backward(mus[t], mus[t + 1], K) for t in range(T)]
        for t in range(T - 1):
            homog = Rs[t] == Rs[t + 1]
            stat = mus[t] == mus[t + 1]
            assert homog == stat, (K, mu0, t)
            hits += homog
    return trials, hits


def check_permutation(n=4, T=5):
    for perm in itertools.permutations(range(n)):
        K = [[F(1) if perm[x] == y else F(0) for y in range(n)] for x in range(n)]
        for _ in range(20):
            mu = rand_dist(n)
            mus = [mu]
            for _ in range(T):
                mus.append(step(mus[-1], K))
            Rs = {backward(mus[t], mus[t + 1], K) for t in range(T)}
            assert len(Rs) == 1
    return math.factorial(n)


def check_monotone(trials=300, n=4, T=8):
    for _ in range(trials):
        K = rand_pos_kernel(n)
        pi = stationary(K)
        mu = rand_dist(n, zero_ok=True)
        d_prev = rel_ent(mu, pi)
        for _ in range(T):
            mu = step(mu, K)
            d = rel_ent(mu, pi)
            assert d <= d_prev + 1e-12
            d_prev = d
    # doubly stochastic: convex combination of permutation matrices
    perms = list(itertools.permutations(range(n)))
    for _ in range(trials):
        w = rand_dist(len(perms))
        K = [[sum(w[i] for i, p in enumerate(perms) if p[x] == y) for y in range(n)] for x in range(n)]
        mu = rand_dist(n, zero_ok=True)
        h_prev = shannon(mu)
        for _ in range(T):
            mu = step(mu, K)
            h = shannon(mu)
            assert h >= h_prev - 1e-12
            h_prev = h
    return trials


def check_janus(trials=200, n=3, T=4):
    """Times -T..T. mu at 0; mu_{t} = mu K^{|t|}; the pair law of (X_{t}, X_{t+1})
    is mu_t(x)K(x,y) for t >= 0 and mu_{t+1}(y)K(y,x) for t < 0 (outward production).
    Left-to-right kernels: K for t >= 0, a backward kernel for t < 0."""
    for _ in range(trials):
        K = rand_pos_kernel(n)
        pi = stationary(K)
        mu0 = rand_dist(n)
        if mu0 == pi:
            continue
        out = [mu0]
        for _ in range(T):
            out.append(step(out[-1], K))
        # left-to-right kernel from time -(s+1) to -s, s = 0..T-1: L[x][y] =
        # P(X_{-s}=y | X_{-(s+1)}=x) = out[s][y] K[y][x] / out[s+1][x]
        left = [tuple(tuple(out[s][y] * K[y][x] / out[s + 1][x] for y in range(n)) for x in range(n))
                for s in range(T)]
        right = tuple(tuple(r) for r in K)
        # left side inhomogeneous at every adjacent pair, and differs from K
        assert all(left[s] != left[s + 1] for s in range(T - 1))
        assert all(left[s] != right for s in range(T))
        # relative entropy decreases outward on both sides (symmetric by construction)
        ds = [rel_ent(m, pi) for m in out]
        assert all(ds[i + 1] <= ds[i] + 1e-12 for i in range(T))
    return trials


def check_rank_one():
    pi = [F(1, 2), F(1, 3), F(1, 6)]
    K = [pi[:] for _ in range(3)]
    mu0 = [F(1), F(0), F(0)]
    mus = [mu0]
    for _ in range(4):
        mus.append(step(mus[-1], K))
    Rs = [backward(mus[t], mus[t + 1], K) for t in range(4)]
    assert Rs[0] != Rs[1] and Rs[1] == Rs[2] == Rs[3]
    return True


if __name__ == "__main__":
    tr, hits = check_lemma()
    print(f"1. lemma: {tr} random positive 3x3 worlds, T=4; homogeneous adjacent pairs = {hits}, all stationary: OK")
    print(f"2. permutation kernels: all {check_permutation()} of S_4, 20 initial laws each, backward kernel constant: OK")
    print(f"3. monotone relative entropy (positive) and Shannon entropy (doubly stochastic), {check_monotone()} worlds each: OK")
    print(f"4. Janus worlds, {check_janus()} trials: single orientation inhomogeneous on one side; arrows point outward: OK")
    print(f"5. rank-one positive kernel: homogeneous backward kernels from t=1 on: {check_rank_one()}")
