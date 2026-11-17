"""Exact enumeration checks for the records-asymmetry lane.

Every ensemble is a uniform distribution over a finite list of microstates of
bits. Dynamics are reversible gates (CNOT and Toffoli), so fine-grained
Shannon entropy is conserved. Run with: python3 -I check_records.py
"""

from collections import Counter
from itertools import product
from math import comb, log2


def H(samples):
    """Shannon entropy (bits) of the empirical distribution of samples."""
    c = Counter(samples)
    n = sum(c.values())
    return -sum(v / n * log2(v / n) for v in c.values())


def I(xs, ys):
    return H(xs) + H(ys) - H(list(zip(xs, ys)))


def marginal_sum(states):
    return sum(H([s[i] for s in states]) for i in range(len(states[0])))


def weight_coarse(states):
    """Gibbs entropy coarse-grained by total Hamming weight."""
    n = len(states[0])
    ws = [sum(s) for s in states]
    pw = Counter(ws)
    tot = len(ws)
    return H(ws) + sum(v / tot * log2(comb(n, w)) for w, v in pw.items())


def profile(name, traj):
    print(f"  {name}:")
    for t, states in enumerate(traj):
        print(
            f"    t={t}  joint={H(states):.3f}  marginal-sum={marginal_sum(states):.3f}"
            f"  weight-coarse={weight_coarse(states):.3f}"
        )


# ---------------------------------------------------------------------------
# Part 1. Same dynamics, same entropy profiles, record located differently.
# Gadget bits (S, D, K, E): step 1 D ^= S & K; step 2 S ^= E (event transient).

def gadget_step(g, t):
    S, D, K, E = g
    if t == 0:
        return (S, D ^ (S & K), K, E)
    return (S ^ E, D, K, E)


def evolve(state, steps=2, ngad=2):
    traj = [state]
    for t in range(steps):
        gs = [state[4 * i: 4 * i + 4] for i in range(ngad)]
        state = tuple(b for g in gs for b in gadget_step(g, t))
        traj.append(state)
    return traj


def part1():
    print("Part 1: two gadgets, swap of where the record resides")
    A, B = [], []
    for s1, e1, s2, e2 in product((0, 1), repeat=4):
        A.append((s1, 0, 1, e1, s2, s2, 0, e2))  # G1 blank+coupled, G2 pre-correlated+off
        B.append((s1, s1, 0, e1, s2, 0, 1, e2))  # swapped
    for name, ens in (("A", A), ("B", B)):
        trajs = [evolve(x) for x in ens]
        by_t = [[tr[t] for tr in trajs] for t in range(3)]
        profile(name, by_t)
        s0 = [tr[0][0] for tr in trajs]
        d2 = [tr[2][1] for tr in trajs]
        match = sum(a == b for a, b in zip(s0, d2)) / len(s0)
        # Intervene: flip S1 at t=0, hold every other initial bit fixed.
        robust = 0
        for x in ens:
            y = (1 - x[0],) + x[1:]
            robust += evolve(x)[2][1] != evolve(y)[2][1]
        print(
            f"    device D1 at t=2 vs event S1 at t=0: match={match:.2f}"
            f"  I={I(s0, d2):.3f}  flips-under-intervention={robust / len(ens):.2f}"
            f"  (S1 at t=2 carries I={I(s0, [tr[2][0] for tr in trajs]):.3f})"
        )


# ---------------------------------------------------------------------------
# Part 2. Equal microstate count, different residence of correlation.
# n gadgets (S, D), one step D ^= S.

def part2(n=4):
    print(f"\nPart 2: n={n} gadgets (S,D), step D ^= S; two initial cells of equal size")
    cells = {
        "blank (D=0)": [tuple(b for s in ss for b in (s, 0)) for ss in product((0, 1), repeat=n)],
        "pre-correlated (D=S)": [tuple(b for s in ss for b in (s, s)) for ss in product((0, 1), repeat=n)],
    }
    for name, c0 in cells.items():
        c1 = [tuple(b for i in range(n) for b in (x[2 * i], x[2 * i + 1] ^ x[2 * i])) for x in c0]
        past = sum(I([x[2 * i] for x in c0], [y[2 * i + 1] for y in c1]) for i in range(n)) / n
        fut = sum(I([x[2 * i] for x in c0], [x[2 * i + 1] for x in c0]) for i in range(n)) / n
        print(
            f"  {name}: cell size=2^{log2(len(c0)):.0f}  marginal-sum t0={marginal_sum(c0):.0f}"
            f" t1={marginal_sum(c1):.0f}  per-gadget I(D_after;S)={past:.2f}  I(D_before;S)={fut:.2f}"
        )


# ---------------------------------------------------------------------------
# Part 3. Counterfactual robustness depends on which boundary is held fixed.
# One gadget (S, D, K, E). Event value s = S during step 1.

def run1(x):
    return evolve(x, ngad=1)


def back1(z):
    """Inverse dynamics: undo step 2 then step 1 (both are involutions)."""
    S, D, K, E = z
    S = S ^ E
    D = D ^ (S & K)
    return [(S, D, K, E), (S, D ^ (S & K), K, E), z]


def part3():
    print("\nPart 3: one gadget; robustness relative to the boundary held fixed")
    fwd = [(s, 0, 1, e) for s, e in product((0, 1), repeat=2)]     # blank at t=0
    rev = [back1((s, 0, 1, e)) for s, e in product((0, 1), repeat=2)]  # blank at t=2
    def blank(x):
        return x[1] == 0 and x[2] == 1

    for name, trajs, cell_t in (("blank at t=0", [run1(x) for x in fwd], 0), ("blank at t=2", rev, 2)):
        dep_i = dep_f = keep_i = keep_f = 0
        for tr in trajs:
            s = tr[1][0]
            # Hold (D,K,E) at t=0 fixed and flip the event value.
            S0, D0, K0, E0 = tr[0]
            alt_i = run1((1 - S0, D0, K0, E0))
            dep_i += alt_i[2][1] != tr[2][1]
            keep_i += blank(alt_i[cell_t])
            # Hold (D,K,E) at t=2 fixed and flip the event value.
            S2, D2, K2, E2 = tr[2]
            alt_f = back1((S2 ^ 1, D2, K2, E2))  # with E fixed, flipping s flips S at t=2
            assert alt_f[1][0] == 1 - s
            dep_f += alt_f[0][1] != tr[0][1]
            keep_f += blank(alt_f[cell_t])
        s_vals = [tr[1][0] for tr in trajs]
        print(
            f"  {name}: I(D_t2;s)={I(s_vals, [tr[2][1] for tr in trajs]):.2f}"
            f"  I(D_t0;s)={I(s_vals, [tr[0][1] for tr in trajs]):.2f}\n"
            f"    hold t=0 fixed: late device depends={dep_i / 4:.2f}, intervened world stays in cell={keep_i / 4:.2f}\n"
            f"    hold t=2 fixed: early device depends={dep_f / 4:.2f}, intervened world stays in cell={keep_f / 4:.2f}"
        )


# ---------------------------------------------------------------------------
# Part 4. Typicality under a uniform measure conditioned on a low-weight cell.

def part4(n=5):
    print(f"\nPart 4: n={n} gadgets (S,D), step D ^= S; uniform measure on weight<=k at one time")
    allx = list(product((0, 1), repeat=2 * n))

    def step(x):
        return tuple(b for i in range(n) for b in (x[2 * i], x[2 * i + 1] ^ x[2 * i]))

    pairs = [(x, step(x)) for x in allx]
    for k in range(0, 2 * n + 1, 2):
        for when in (0, 1):
            ens = [p for p in pairs if sum(p[when]) <= k]
            past = sum(I([a[2 * i] for a, _ in ens], [b[2 * i + 1] for _, b in ens]) for i in range(n)) / n
            fut = sum(I([a[2 * i] for a, _ in ens], [a[2 * i + 1] for a, _ in ens]) for i in range(n)) / n
            print(
                f"  k={k:2d} cell at t={when}: states={len(ens):4d}"
                f"  I(D_t1;S)={past:.3f}  I(D_t0;S)={fut:.3f}"
            )


if __name__ == "__main__":
    part1()
    part2()
    part3()
    part4()
