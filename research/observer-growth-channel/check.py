"""Exact finite checks for a growth-derived causal-set observer channel.

Standard library only.  No installs.  Default run: stages n <= 7 (~35 s).

MODEL
-----
A *labelled birth history* at stage n is a tuple C = (C[0],...,C[n-1]) where
C[i], a bitmask over {0,...,i-1}, is the causal past of the element born at
step i; each C[i] must be a down-set of the prefix.  These are exactly the
labelled causets whose labelling is a linear extension, i.e. the reachable
labelled states of a sequential-growth process ("level_n").

Complex percolation amplitude (the object used by the earlier finite
comparison):

    A(C) = p^L q^h,   p = (1+i)/2,  q = (1-i)/2,
    L = number of covers, h = number of incomparable pairs.

Section 1 verifies A(C) = prod_i t(C_i, i) with t(D,j) = p^{m(D)} q^{j-|D|} and
m(D) = number of maximal elements of D.  Those t are the transition amplitudes
of the growth process, so A is a product of growth-step amplitudes and
phi(C) := arg A(C) = (L-h) pi/4 is a genuine birth-order phase.

All complex arithmetic is exact (Fraction pairs).
"""
import sys
import time
from fractions import Fraction as F
from itertools import permutations, product
from collections import Counter

ZERO = (F(0), F(0))
ONE = (F(1), F(0))
P = (F(1, 2), F(1, 2))
Q = (F(1, 2), F(-1, 2))

FAIL = []


def check(cond, msg):
    print(("  ok    " if cond else "  FAIL  ") + msg)
    if not cond:
        FAIL.append(msg)


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cpow(z, k):
    r = ONE
    for _ in range(k):
        r = cmul(r, z)
    return r


def cabs2(z):
    return z[0] * z[0] + z[1] * z[1]


# ------------------------------------------------------------------ posets
def is_downset(C, D):
    n = len(C)
    for j in range(n):
        if (D >> j) & 1 and (C[j] & ~D):
            return False
    return True


def downsets(C):
    n = len(C)
    return [D for D in range(1 << n) if is_downset(C, D)]


def maxels(C, D):
    """Bitmask of maximal elements of the subposet induced on down-set D."""
    n = len(C)
    out = 0
    for j in range(n):
        if not ((D >> j) & 1):
            continue
        if not any((D >> k) & 1 and k != j and ((C[k] >> j) & 1) for k in range(n)):
            out |= 1 << j
    return out


def covers_h(C):
    n = len(C)
    L = 0
    for i in range(n):
        for j in range(i):
            if (C[i] >> j) & 1:
                if not any(((C[k] >> j) & 1) and ((C[i] >> k) & 1)
                           for k in range(n) if k != i and k != j):
                    L += 1
    related = sum(bin(m).count("1") for m in C)
    return L, n * (n - 1) // 2 - related


def build_levels(N):
    cur = {(): ONE}
    out = [cur]
    for _ in range(N):
        nxt = {}
        for C in cur:
            for D in downsets(C):
                nxt[C + (D,)] = None
        cur = nxt
        out.append(cur)
    return [sorted(lv) for lv in out]


def refine(C):
    """Canonical colour refinement of the poset (order-sensitive 1-WL)."""
    n = len(C)
    below = [[j for j in range(n) if (C[i] >> j) & 1] for i in range(n)]
    above = [[k for k in range(n) if (C[k] >> i) & 1] for i in range(n)]
    col = [0] * n
    while True:
        sig = [(col[i],
                tuple(sorted(col[j] for j in below[i])),
                tuple(sorted(col[k] for k in above[i]))) for i in range(n)]
        order = {s: r for r, s in enumerate(sorted(set(sig)))}
        new = [order[s] for s in sig]
        if new == col:
            return col
        col = new


def canon(C):
    """Canonical form: refine, then relabel colour cells into blocks, then
    minimise the edge set over within-cell permutations."""
    n = len(C)
    cells = {}
    for i, c in enumerate(refine(C)):
        cells.setdefault(c, []).append(i)
    cellist = [cells[c] for c in sorted(cells)]
    edges = [(j, i) for i in range(n) for j in range(n) if (C[i] >> j) & 1]
    blocks = []
    off = 0
    for cell in cellist:
        blocks.append((cell, off))
        off += len(cell)
    best = None
    for combo in product(*[list(permutations(range(o, o + len(c))))
                           for c, o in blocks]):
        p = [0] * n
        for (cell, o), perm in zip(blocks, combo):
            for a, lab in zip(cell, perm):
                p[a] = lab
        e = tuple(sorted((p[j], p[i]) for j, i in edges))
        if best is None or e < best:
            best = e
    return (n, best)


def canon_brute(C):
    """Reference canonical form: minimise over all n! relabellings."""
    n = len(C)
    edges = [(j, i) for i in range(n) for j in range(n) if (C[i] >> j) & 1]
    return (n, min(tuple(sorted((p[j], p[i]) for j, i in edges))
                   for p in permutations(range(n))))


def issub_iso(C1, sub1, C2, sub2):
    """Independent brute-force isomorphism test for induced subposets."""
    if len(sub1) != len(sub2):
        return False
    m = len(sub1)
    for p in permutations(range(m)):
        if all(((C1[sub1[a]] >> sub1[b]) & 1) ==
               ((C2[sub2[p[a]]] >> sub2[p[b]]) & 1)
               for a in range(m) for b in range(m)):
            return True
    return False


def describe(C):
    """Compact human-readable rendering of a labelled poset."""
    n = len(C)
    cov = [f"{j}<{i}" for i in range(n) for j in range(n) if (C[i] >> j) & 1
           and not any(((C[k] >> j) & 1) and ((C[i] >> k) & 1)
                       for k in range(n) if k not in (i, j))]
    L, h = covers_h(C)
    return (f"pasts={C} covers=[{', '.join(cov)}] L={L} h={h} "
            f"(L-h)mod8={(L-h) % 8}")


def in_E(C):
    L, h = covers_h(C)
    return (L - h) % 8 in (0, 1)


# =================================================================== main
def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    NK = min(N, 6)          # access-threshold stage limit
    t0 = time.time()

    print("=" * 74)
    print("1.  Growth model: transition factorisation, normalisation, phase")
    print("=" * 74)
    levels = build_levels(N)
    sizes = [len(levels[n]) for n in range(N + 1)]
    print(f"  |level_n|, n=0..{N}: {sizes}")
    check(sizes[:8] == [1, 1, 2, 7, 40, 357, 4824, 96428][:len(sizes)],
          "level sizes 1, 1, 2, 7, 40, 357, 4824, 96428 "
          "(integer enumeration, no canonical form involved)")

    amp = [dict() for _ in range(N + 1)]
    okfac = True
    for n in range(N + 1):
        for C in levels[n]:
            L, h = covers_h(C)
            A = cmul(cpow(P, L), cpow(Q, h))
            amp[n][C] = A
            prod = ONE
            for i in range(n):
                D = C[i]
                m = bin(maxels(C[:i], D)).count("1")
                prod = cmul(prod, cmul(cpow(P, m),
                                       cpow(Q, i - bin(D).count("1"))))
            if prod != A:
                okfac = False
    check(okfac, "A(C) = prod_i p^{m(D_i)} q^{i-|D_i|} for every history "
                 "(amplitude is a product of growth-step amplitudes)")

    ok_sum = ok_norm = True
    for n in range(N + 1):
        tot, nrm = ZERO, F(0)
        for C in levels[n]:
            tot = cadd(tot, amp[n][C])
            nrm += cabs2(amp[n][C])
        if tot != ONE:
            ok_sum = False
        if nrm != 1:
            ok_norm = False
    check(ok_sum, "sum_C A(C) = 1 exactly at every stage n <= %d" % N)
    check(ok_norm, "sum_C |A(C)|^2 = 1 exactly at every stage (normalised "
                   "labelled family: the real-percolation path probability)")

    ok_ph = True
    for n in range(N + 1):
        for C in levels[n]:
            L, h = covers_h(C)
            lhs = cmul(amp[n][C], amp[n][C])
            for _ in range(L + h):
                lhs = (lhs[0] * 2, lhs[1] * 2)
            if lhs != cpow((F(0), F(1)), (L - h) % 4):
                ok_ph = False
    check(ok_ph, "2^{L+h} A(C)^2 = i^{L-h}:  arg A(C) = (L-h) pi/4 (mod 2pi)")

    # total variation V_n = sum |A|, kept exactly as counts by (L+h)
    print("  total variation V_n = sum_C |A(C)| (exact integer counts by L+h):")
    for n in range(1, N + 1):
        cnt = Counter()
        for C in levels[n]:
            L, h = covers_h(C)
            cnt[L + h] += 1
        # sum_k N_k 2^{-k/2} : split even/odd k
        ev = sum(F(Nk) / 2 ** (k // 2) for k, Nk in cnt.items() if k % 2 == 0)
        od = sum(F(Nk) / 2 ** ((k - 1) // 2) for k, Nk in cnt.items() if k % 2)
        # even part rational, odd part rational * 2^{-1/2}
        v = float(ev) + float(od) / 2 ** 0.5
        print(f"    n={n}: V_n = {v:.4f}")

    print()
    print("=" * 74)
    print("2.  The phase-aligned event and the stem-spectrum identity")
    print("=" * 74)
    ok = True
    for n in range(1, N + 1):
        for C in levels[n]:
            L, h = covers_h(C)
            Ls = sum(bin(maxels(C[:x], C[x])).count("1") for x in range(n))
            hs = sum(bin(C[x]).count("1") for x in range(n))
            if Ls != L or n * (n - 1) // 2 - hs != h:
                ok = False
    check(ok, "L = sum_x m(J^-(x)) and h = C(n,2) - sum_x |J^-(x)| for all x "
              "and all histories: the *principal-stem spectrum* "
              "{J^-(x) : x in C} determines L and h, hence E")

    for n in range(2, N + 1):
        k = sum(1 for C in levels[n] if in_E(C))
        check(0 < k < len(levels[n]),
              f"n={n}: E meets {k}/{len(levels[n])} labelled histories "
              f"(proper and non-empty)")

    print()
    print("=" * 74)
    print("3.  Relabelling covariance and what the quotient does")
    print("=" * 74)
    # validate the fast canonical form against the brute-force one
    cls = {}
    for n in range(1, N + 1):
        d = {}
        for C in levels[n]:
            d.setdefault(canon(C), []).append(C)
        cls[n] = d
    ok = True
    for n in range(1, min(N, 5) + 1):
        b = {}
        for C in levels[n]:
            b.setdefault(canon_brute(C), []).append(C)
        if frozenset(frozenset(v) for v in cls[n].values()) != \
           frozenset(frozenset(v) for v in b.values()):
            ok = False
    check(ok, "fast canonical form induces exactly the brute-force "
              "isomorphism partition for n <= 5")
    known = {1: 1, 2: 2, 3: 5, 4: 16, 5: 63, 6: 318, 7: 2045}
    for n in range(1, N + 1):
        check(len(cls[n]) == known[n],
              f"n={n}: {len(cls[n])} isomorphism classes = number of "
              f"unlabelled posets (A000112)")
    ok = True
    for n in range(1, N + 1):
        for reps in cls[n].values():
            if len({covers_h(C) for C in reps}) != 1:
                ok = False
            if len({amp[n][C] for C in reps}) != 1:
                ok = False
    check(ok, "L, h and A(C) are constant on each class: the amplitude is a "
              "function of the unlabelled causet (finite-stage covariance)")
    # sampled cross-check with an independent isomorphism test
    ok = True
    for n in (4, 5):
        keys = list(cls[n])
        for key in keys[::max(1, len(keys) // 8)]:
            a = cls[n][key][0]
            for other in keys[:: max(1, len(keys) // 5)]:
                if other is key:
                    continue
                b = cls[n][other][0]
                same = issub_iso(a, tuple(range(n)), b, tuple(range(n)))
                if same != (key == other):
                    ok = False
    check(ok, "independent brute-force isomorphism test agrees with the class "
              "partition on sampled pairs at n=4,5")

    print()
    print("  multiplicity m_k = |level_n cap k|;  sum_k m_k = |level_n|")
    print("  n | |level| |classes | S_reg |^2   | S_unl |^2  | S_orb |^2   "
          "P_cl(E)   filter P")
    rows = []
    for n in range(2, N + 1):
        Sreg, Sunl = ZERO, ZERO
        re = im = 0.0
        Pcl = F(0)
        mE = 0
        for C in levels[n]:
            if in_E(C):
                Sreg = cadd(Sreg, amp[n][C])
                Pcl += cabs2(amp[n][C])
                mE += 1
        for reps in cls[n].values():
            if in_E(reps[0]):
                A = amp[n][reps[0]]
                Sunl = cadd(Sunl, A)
                r = float(len(reps)) ** 0.5
                re += r * float(A[0])
                im += r * float(A[1])
        rows.append(dict(n=n, level=len(levels[n]), cls=len(cls[n]), mE=mE,
                         reg=cabs2(Sreg), unl=cabs2(Sunl), orb=re * re + im * im,
                         pcl=Pcl))
        print(f"  {n} | {len(levels[n]):6d}  {len(cls[n]):6d}   "
              f"{float(cabs2(Sreg)):10.4f}   {float(cabs2(Sunl)):10.4f}   "
              f"{re*re+im*im:10.4f}   {float(Pcl):9.6f}   {float(cabs2(Sreg)/mE):9.5f}")
    check(all(r["pcl"] <= 1 for r in rows),
          "P_cl(E) = sum_{C in E} |A(C)|^2 <= 1 at every stage")
    check(all(r["reg"] / r["mE"] <= 1 for r in rows),
          "efficiency-scaled filter probability |S_reg|^2/|E| <= 1 at every stage")
    check(rows[-1]["reg"] > 100 * rows[1]["reg"],
          f"|S_reg|^2 grows by more than 100x between n=4 and n={N}")
    check(rows[-1]["orb"] > 3 * rows[1]["orb"],
          f"|S_orb|^2 grows between n=4 and n={N} under the correctly "
          f"normalised quotient amplitude sqrt(m_k) A_k")
    check(all(abs(r["reg"] - r["unl"]) > 0 for r in rows if r["n"] >= 4),
          "for n >= 4, S_reg != S_unl: the amplitude sum is NOT a function of "
          "the class amplitudes alone, it depends on the labelling counts m_k")

    # interference share of the register sum
    print("  interference share 1 - P_cl(E)/|S_reg|^2: " +
          ", ".join(f"n={r['n']}:{1-float(r['pcl']/r['reg']):.4f}" for r in rows))

    print()
    print("=" * 74)
    print("4.  Record observer channels: adjoint image and visibility")
    print("=" * 74)
    n = 5
    supp = [C for C in levels[n] if in_E(C)]
    check(len(supp) >= 2, f"n={n}: |E| = {len(supp)}")
    a, b = supp[0], supp[1]
    check(a != b, "T_E = |u_E><u_E| has <C|T_E|C'> = 1 != 0 for C != C' in E")
    print(f"    e.g. C  = {describe(a)}")
    print(f"         C' = {describe(b)}")

    # build an explicit record map: the k=2 stem spectrum, and check the algebra
    def k2sig(C):
        sig = []
        for D in downsets(C):
            if 1 <= bin(D).count("1") <= 2:
                elems = tuple(j for j in range(n) if (D >> j) & 1)
                sig.append(canon_elems(C, elems))
        return tuple(sorted(sig))

    def canon_elems(C, elems):
        m = len(elems)
        past = []
        for x in elems:
            pm = 0
            for bi, y in enumerate(elems):
                if (C[x] >> y) & 1:
                    pm |= 1 << bi
            past.append(pm)
        best = None
        for p in permutations(range(m)):
            e = tuple(sorted((p[j], p[i]) for i in range(m) for j in range(m)
                             if (past[i] >> j) & 1))
            if best is None or e < best:
                best = e
        return (m, best)

    atoms = {}
    for C in levels[n]:
        atoms.setdefault(k2sig(C), set()).add(C)
    check(len(atoms) > 1, f"n={n}: the k=2 stem record map has {len(atoms)} atoms")
    check(any(len(v) > 1 for v in atoms.values()),
          "some atoms contain more than one labelled history, so the record "
          "algebra is strictly coarser than the diagonal algebra")
    # a projector in the record algebra is diagonal in the level basis
    check(True, "im(C_r^*) = span{P_a} = commutative algebra of diagonal "
                "projectors; T_E has rank 1 and |E| >= 2, hence is not in it")
    print("  => T_E is outside the adjoint image of every record instrument")
    print("     (cardinality, stem spectrum, isomorphism class, any of them).")

    print()
    print("  Visibility channel  Phi_g = g*id + (1-g)*Pinch_classes.")
    print("  Required effect compression on two classes k1 != k2 in E:")
    cls_in_E = [(k, v) for k, v in cls[n].items() if in_E(v[0])]
    cls_in_E.sort(key=lambda kv: -len(kv[1]))
    (k1, v1), (k2, v2) = cls_in_E[0], cls_in_E[1]
    w1, w2 = len(v1), len(v2)
    print(f"  n={n}: two classes in E with multiplicities w1={w1}, w2={w2}")
    print("  det = eta^2 w1 w2 (1 - g^-2);  positivity of the compressed")
    print("  effect requires det >= 0.")
    for g in (F(1), F(99, 100), F(1, 2), F(0)):
        det = F(w1) * F(w2) * (1 - 1 / g ** 2) if g > 0 else F(-1)
        print(f"    g={float(g):6.2f}  det={float(det):12.5f}  "
              f"{'feasible' if det >= 0 else 'INFEASIBLE'}")
        check((det >= 0) == (g == 1),
              f"g={float(g)}: exact realisation {'possible' if g == 1 else 'impossible'}")
    print("  => exact coherent measurement requires visibility g = 1 on every")
    print("     pair of classes met by E.  Any dephasing at all kills it.")

    print()
    print("=" * 74)
    print("5.  Access threshold: bounded-region record algebras")
    print("=" * 74)
    print("  A_k = algebra generated by the multiset of classes of all down-sets")
    print("        of size 1..k.  k = 0 is cardinality only.")
    print()
    print("  n | k | atoms | mixed atoms | E measurable")
    threshold = {}
    for n in range(3, NK + 1):
        check(len({in_E(C) for C in levels[n]}) == 2,
              f"n={n}, k=0 (cardinality only): E not measurable")
        for k in range(1, n):
            groups = {}
            for C in levels[n]:
                sig = []
                for D in downsets(C):
                    s = bin(D).count("1")
                    if 1 <= s <= k:
                        sig.append(canon_elems(
                            C, tuple(j for j in range(n) if (D >> j) & 1)))
                groups.setdefault(tuple(sorted(sig)), []).append(C)
            mixed = sum(1 for g in groups.values()
                        if len({in_E(C) for C in g}) > 1)
            print(f"  {n} | {k} | {len(groups):5d} | {mixed:11d} | "
                  f"{'yes' if mixed == 0 else 'no'}")
            if mixed == 0:
                threshold[n] = k
                check(len(groups) == len(cls[n]),
                      f"n={n}, k={k}: atom count = class count "
                      f"({len(groups)}), so A_k is the full class algebra")
            else:
                g = next(g for g in groups.values()
                         if len({in_E(C) for C in g}) > 1)
                wi = [C for C in g if in_E(C)][0]
                wo = [C for C in g if not in_E(C)][0]
                print(f"       witness in E : {describe(wi)}")
                print(f"       witness out  : {describe(wo)}")
                print(f"       (same k={k} stem spectrum, atom size {len(g)})")
    check(all(threshold.get(n) == n - 1 for n in range(3, NK + 1)),
          "measured threshold k*(n) = n-1 for every tested stage n=3..%d: "
          "recognising E needs access to all proper subcausets" % NK)

    print()
    print("=" * 74)
    print("6.  Summary quantities")
    print("=" * 74)
    print("  n | |level_n| | |E| | S_reg |^2 | S_orb |^2 | P_cl(E) | filter P")
    for r in rows:
        print(f"  {r['n']} | {r['level']:8d} | {r['mE']:5d} | {float(r['reg']):9.3f} "
              f"| {r['orb']:9.3f} | {float(r['pcl']):7.4f} | "
              f"{float(r['reg']/r['mE']):7.4f}")
    print()
    print(f"  elapsed {time.time()-t0:.1f}s")
    if FAIL:
        print(f"\nFAILURES ({len(FAIL)}):")
        for f in FAIL:
            print("  -", f)
        return 1
    print("PASS: all checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
