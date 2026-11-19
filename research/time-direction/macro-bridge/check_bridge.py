"""Deterministic, exactly time-reversal-symmetric micro world -> macro chance process.

Micro state: event bit S, device bit D, and a ring tape of N bits (N even, m = N/2).
    R1 = rho1 o swap(D, tape[m])     rho1: tape cell i -> -i   (fixes 0 and m)
    R2 = rho2 o swap(S, D)           rho2: tape cell i -> 1-i
    U  = R2 o R1
R1 and R2 are involutions, so U is reversible and R1 U R1 = U^{-1}: the law is
time-reversal symmetric with reversal map eps = R1.  Net effect of one step:
S gets the tape bit arriving at m, D gets the old S, the old D goes onto the tape,
and the tape shifts by one cell.

B0  U is a bijection, R1 and R2 are involutions, R1 U R1 = U^{-1}.
B1  Uniform micro ensemble (stationary; no boundary; maximal entropy at every time).
    The macro process (S, D) over T < N steps is exactly the delay-line chain,
    D records S (1 bit) and never forecasts it; homogeneous in both directions.
B2  eps does not preserve the macro labels: it exchanges D with tape[m].
B3  Macro boundary at the start (S = D = 0, tape uniform): the backward
    description is homogeneous only after the boundary is forgotten; records unchanged.
B4  Macro boundary at the end (uniform ensemble conditioned on S_T = D_T = 0):
    the forward description is inhomogeneous near T, the backward one homogeneous;
    D still records S's earlier state.
"""
from fractions import Fraction as F
import itertools
import math

N, T = 8, 6
M = N // 2


def rho1(tape):
    return tuple(tape[(-i) % N] for i in range(N))


def rho2(tape):
    return tuple(tape[(1 - i) % N] for i in range(N))


def R1(x):
    s, d, tape = x
    tape = list(tape)
    d, tape[M] = tape[M], d
    return (s, d, rho1(tuple(tape)))


def R2(x):
    s, d, tape = x
    return (d, s, rho2(tape))


def U(x):
    return R2(R1(x))


ALL = [(s, d, tape) for s in (0, 1) for d in (0, 1) for tape in itertools.product((0, 1), repeat=N)]


def b0():
    img = {U(x) for x in ALL}
    assert len(img) == len(ALL)
    assert all(R1(R1(x)) == x and R2(R2(x)) == x for x in ALL)
    Uinv = {U(x): x for x in ALL}
    assert all(R1(U(R1(x))) == Uinv[x] for x in ALL)
    return len(ALL)


def macro_law(weights):
    P = {}
    for x, w in weights.items():
        if w == 0:
            continue
        path, y = [], x
        for _ in range(T + 1):
            path.append((y[0], y[1]))
            y = U(y)
        P[tuple(path)] = P.get(tuple(path), 0) + w
    Z = sum(P.values())
    return {k: v / Z for k, v in P.items()}


def kernels(P, forward=True):
    ks = []
    for t in range(T):
        pair, single = {}, {}
        for p, q in P.items():
            a, b = (p[t], p[t + 1]) if forward else (p[t + 1], p[t])
            pair[(a, b)] = pair.get((a, b), 0) + q
            single[a] = single.get(a, 0) + q
        ks.append({k: v / single[k[0]] for k, v in pair.items()})
    return ks


def homog_from(ks):
    """Smallest step index from which all later kernels agree on common rows."""
    def agree(a, b):
        rows = {k[0] for k in a} & {k[0] for k in b}
        return all(a.get((r, y), 0) == b.get((r, y), 0) for r in rows
                   for y in [(0, 0), (0, 1), (1, 0), (1, 1)])
    start = 0
    for i in range(len(ks) - 1):
        if not agree(ks[i], ks[i + 1]):
            start = i + 1
    return start


def H(P, coords):
    m = {}
    for p, q in P.items():
        k = tuple(p[t][part] for t, part in coords)
        m[k] = m.get(k, 0) + q
    return -sum(float(q) * math.log2(float(q)) for q in m.values() if q > 0)


def cmi(P, a, b, c):
    return H(P, a + c) + H(P, b + c) - H(P, a + b + c) - H(P, c)


def rec(P, t):
    return {"D rec S": cmi(P, [(t, 1)], [(t - 1, 0)], [(t, 0)]),
            "D fc S": cmi(P, [(t, 1)], [(t + 1, 0)], [(t, 0)]),
            "S rec D": cmi(P, [(t, 0)], [(t - 1, 1)], [(t, 1)]),
            "S fc D": cmi(P, [(t, 0)], [(t + 1, 1)], [(t, 1)])}


def delay_line_law():
    P = {}
    for s0, d0, *ns in itertools.product((0, 1), repeat=T + 2):
        path, s, d = [(s0, d0)], s0, d0
        for n in ns[:T]:
            s, d = n, s
            path.append((s, d))
        P[tuple(path)] = P.get(tuple(path), 0) + F(1, 2 ** (T + 2))
    return P


def show(name, P, t):
    fw, bw = kernels(P), kernels(P, False)
    r = rec(P, t)
    print(f"{name}: forward homogeneous from step {homog_from(fw)}, backward from step {homog_from(bw)} (of {T});"
          f" at t={t}: " + ", ".join(f"{k} {v:.3f}" for k, v in r.items()))


if __name__ == "__main__":
    print(f"B0 micro: {b0()} states (N={N}); R1, R2 involutions; R1 U R1 = U^-1: OK")
    uni = {x: F(1) for x in ALL}
    P = macro_law(uni)
    assert P == delay_line_law()
    print(f"B1 uniform micro ensemble: macro law over T={T} equals the delay-line chain exactly")
    show("   B1", P, 3)
    x = (0, 1, tuple([0] * N))
    print(f"B2 eps = R1 sends D to tape[m]: R1{(0, 1, 'tape 0...')} has D = {R1(x)[1]}, tape[m] = {R1(x)[2][M]}")
    start = {x: F(1) if (x[0], x[1]) == (0, 0) else F(0) for x in ALL}
    show("B3 macro boundary at start (S=D=0)", macro_law(start), 3)
    end = {}
    for x in ALL:
        y = x
        for _ in range(T):
            y = U(y)
        end[x] = F(1) if (y[0], y[1]) == (0, 0) else F(0)
    show("B4 macro boundary at end (S_T=D_T=0)", macro_law(end), 3)
