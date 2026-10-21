"""Coordinator independent check of the all-nonzero stage-4 continuation.

From-scratch bit-mask poset enumeration, BCPH level-1/2 amplitudes defined
directly from the birth-order report, and the Bell/MSR continuation rule
re-derived here (no imports from either worker script).  Exact Gaussian
rational arithmetic only.
"""
from fractions import Fraction as F
from itertools import permutations

Z = (F(0), F(0))
ONE = (F(1), F(0))


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def mul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def div(a, b):
    d = b[0] * b[0] + b[1] * b[1]
    return (a[0] * b[0] + a[1] * b[1]) / d, (a[1] * b[0] - a[0] * b[1]) / d


def norm2(a):
    return a[0] ** 2 + a[1] ** 2


def ideals(C):
    return [D for D in range(1 << len(C)) if all(not (D >> i & 1) or C[i] & D == C[i] for i in range(len(C)))]


def canon(C):
    edges = [(j, i) for i, mask in enumerate(C) for j in range(len(C)) if mask >> j & 1]
    return (len(C), min(tuple(sorted((p[j], p[i]) for j, i in edges)) for p in permutations(range(len(C)))))


def induced(C, B):
    old = [i for i in range(len(C)) if B >> i & 1]
    index = {v: i for i, v in enumerate(old)}
    return tuple(sum(1 << index[j] for j in old if C[i] >> j & 1) for i in old)


# BCPH seed, birth-order-interference/REPORT.md: x=1/2, alpha1=1/4, u=(3+4i)/5.
def seed_amp(C, P):
    n = len(C)
    if n == 1:
        return (F(1, 2), F(0))  # x for chain2 child, 1-x for antichain child
    assert n == 2
    if C[1]:  # 2-chain parent
        return {0: (F(1, 4), F(0)), 1: (F(1, 4), F(0)), 3: (F(1, 2), F(0))}[P]
    u = (F(3, 20), F(1, 5))  # (3+4i)/20
    if P == 3:
        return (F(11, 20), F(-3, 5))
    return u


levels = [{(): ONE}]
for n in range(4):
    nxt = {}
    for C in levels[-1]:
        for P in ideals(C):
            nxt[C + (P,)] = None  # psi filled below
    levels.append(nxt)

# psi via the amplitudes: level 1 and 2 from the BCPH table; levels 3-4 from
# the continuation rule defined after r-values are known.
r = {canon(()): ONE, canon((0,)): ONE}
psi = {(): ONE, (0,): ONE}
for n in (1, 2):
    for C in levels[n]:
        for P in ideals(C):
            psi[C + (P,)] = mul(psi[C], seed_amp(C, P))
for C in levels[2]:
    r[canon(C)] = div(seed_amp(C, 3), seed_amp(C, 0))

full_r, sums = {}, {}
for C in levels[3]:
    S = Z
    for P in ideals(C):
        if P != 7:
            S = add(S, r[canon(induced(C, P))])
    sums[canon(C)] = S
    full_r[canon(C)] = add(ONE, (-S[0], -S[1]))
    if canon(C) in r:
        assert r[canon(C)] == full_r[canon(C)]
    r[canon(C)] = full_r[canon(C)]
    for P in ideals(C):
        t = full_r[canon(C)] if P == 7 else r[canon(induced(C, P))]
        psi[C + (P,)] = mul(psi[C], t)


def amp(C, P):
    n = len(C)
    if n <= 2:
        return seed_amp(C, P)
    assert n == 3
    return full_r[canon(C)] if P == 7 else r[canon(induced(C, P))]


# 1. all transitions through the 3-to-4 step nonzero
trans = [amp(C, P) for n in (1, 2, 3) for C in levels[n] for P in ideals(C)]
assert len(trans) == 49 and all(t != Z for t in trans)

# 2. MSR at every parent of size 1-3
for n in (1, 2, 3):
    for C in levels[n]:
        s = Z
        for P in ideals(C):
            s = add(s, amp(C, P))
        assert s == ONE

# 3. product BC at every parent of size 1-3
checks = 0
for n in (1, 2, 3):
    for C in levels[n]:
        ds = ideals(C)
        for i, P in enumerate(ds):
            for Q in ds[i + 1:]:
                Bs = induced(C, P | Q)
                old = [v for v in range(len(C)) if (P | Q) >> v & 1]
                idx = {v: i for i, v in enumerate(old)}
                Pb = sum(1 << idx[j] for j in old if P >> j & 1)
                Qb = sum(1 << idx[j] for j in old if Q >> j & 1)
                lhs = mul(amp(C, P), amp(Bs, Qb))
                rhs = mul(amp(C, Q), amp(Bs, Pb))
                assert lhs == rhs, (n, C, P, Q)
                checks += 1

# 3b. the level-3 psi phase seed is exactly the BCPH values
seed_cp = sorted(psi[C] for C in levels[3] if canon(C) == canon((0, 1, 0)))
assert seed_cp == sorted([(F(3, 40), F(1, 10))] * 2 + [(F(1, 8), F(0))])

# 4. norm-GC at stages 2, 3, 4 over the generated psi
for n in (2, 3, 4):
    cls = {}
    for C in levels[n]:
        cls.setdefault(canon(C), []).append(norm2(psi[C]))
    for vals in cls.values():
        assert len(set(vals)) == 1, (n, vals)
classes4 = len({canon(C) for C in levels[4]})

# 5. stage-4 norm system in x_i=|g_C3|^2, y_i=|t(C3,full)|^2
parents = levels[3]
pidx = {C: i for i, C in enumerate(parents)}
rows = []
by_class = {}
for C4 in levels[4]:
    C3 = C4[:3]
    P = C4[3]
    coeff = [F(0)] * 14
    M = norm2(psi[C3])
    if P == 7:
        coeff[7 + pidx[C3]] = M
    else:
        coeff[pidx[C3]] = M * norm2(r[canon(induced(C3, P))])
    by_class.setdefault(canon(C4), []).append(coeff)
for rows_ in by_class.values():
    ref = rows_[0]
    rows.extend([[a - b for a, b in zip(row, ref)] for row in rows_[1:]])
assert len(rows) == 24

# exact rref
A = [row for row in rows if any(row)]
piv = []
rr = 0
for c in range(14):
    p = next((i for i in range(rr, len(A)) if A[i][c]), None)
    if p is None:
        continue
    A[rr], A[p] = A[p], A[rr]
    d = A[rr][c]
    A[rr] = [v / d for v in A[rr]]
    for i in range(len(A)):
        if i != rr and A[i][c]:
            f = A[i][c]
            A[i] = [v - f * w for v, w in zip(A[i], A[rr])]
    piv.append(c)
    rr += 1
assert len(piv) == 8 and piv == [0, 1, 2, 3, 4, 5, 8, 9]

# witness point satisfies the linear system
witness = [F(1)] * 7 + [norm2(full_r[canon(C)]) for C in parents]
assert all(sum(a * b for a, b in zip(row, witness)) == 0 for row in rows)

# 6. cp-plus-top class and holonomy
cp = (0, 1, 0)  # 0<1 plus isolated 2
cp_top = cp + (7,)
vals = [psi[C] for C in levels[4] if canon(C) == canon(cp_top)]
assert len(vals) == 3 and len({norm2(a) for a in vals}) == 1
hol = [div(v, vals[0]) for v in vals]
assert vals[0] != Z and any(h != ONE for h in hol)
assert hol == [ONE, ONE, (F(3, 5), F(-4, 5))]

# 7. residual common-q family: MSR, BC, norm-GC, nonzeros, holonomy
def check_q(q):
    def ampq(C, P):
        if len(C) < 3:
            return amp(C, P)
        if P == 7:
            return div(add(q, (-sums[canon(C)][0], -sums[canon(C)][1])), q)
        return div(r[canon(induced(C, P))], q)

    psiq = dict(psi)
    for C in levels[3]:
        for P in ideals(C):
            psiq[C + (P,)] = mul(psi[C], ampq(C, P))
    for C in levels[3]:
        s = Z
        for P in ideals(C):
            s = add(s, ampq(C, P))
            assert ampq(C, P) != Z
        assert s == ONE
    for C in levels[3]:
        ds = ideals(C)
        for i, P in enumerate(ds):
            for Q in ds[i + 1:]:
                Bs = induced(C, P | Q)
                old = [v for v in range(len(C)) if (P | Q) >> v & 1]
                idx = {v: i for i, v in enumerate(old)}
                Pb = sum(1 << idx[j] for j in old if P >> j & 1)
                Qb = sum(1 << idx[j] for j in old if Q >> j & 1)
                assert mul(ampq(C, P), ampq(Bs, Qb)) == mul(ampq(C, Q), ampq(Bs, Pb))
    cls = {}
    for C in levels[4]:
        cls.setdefault(canon(C), []).append(norm2(psiq[C]))
    for vals_ in cls.values():
        assert len(set(vals_)) == 1
    vals_ = [psiq[C] for C in levels[4] if canon(C) == canon(cp_top)]
    assert len({norm2(v) for v in vals_}) == 1
    assert [div(v, vals_[0]) for v in vals_] == [ONE, ONE, (F(3, 5), F(-4, 5))]
    return True


for q in [(F(2), F(0)), (F(1), F(1)), (F(1, 2), F(0)), (F(-2), F(1))]:
    assert check_q(q)
print("residual q-family: 4 nonzero q values pass MSR/BC/norm-GC/nonzero/holonomy")

print("levels:", [len(levels[n]) for n in range(5)], "unlabelled classes at 4:", classes4)
print("all 49 transitions nonzero; MSR parents 1-3 pass; product-BC checks:", checks)
print("norm-GC stages 2-4 pass")
print("norm system rows 24, rank", len(piv), "pivots", piv)
print("witness x_i=1, y_i=|r_C3|^2 satisfies projected norm system")
print("stage-3 sums S_C:")
for C in parents:
    print(" ", canon(C), "S=", sums[canon(C)], "r_C=", full_r[canon(C)])
print("cp+top amplitudes:", vals)
print("cp+top holonomies:", hol)
print("PASS: independent nonzero continuation check")
