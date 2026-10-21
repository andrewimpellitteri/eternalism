#!/usr/bin/env python3
"""Independent review computations for growth-completion Props. 5-6 and
regularized-measure Lemma 2 / Theorem 2.  Written from the definitions; does
not import or copy the reviewed scripts.  Standard library only.

Objects
  * naturally labelled causets, element i has full past past[i] (bitmask), grown
    by adding an element whose past is a down-set D of the current causet;
  * complex percolation: transition amplitude p^{|max D|} q^{m-|D|}, so the
    cylinder amplitude is A_p(C) = p^{L} q^{C(n,2)-R};
  * n-stems of C: isomorphism classes of n-element down-sets of C;
  * covtree node N_Gamma (level n): {C : the n-stem set of C is exactly Gamma};
    stage-m approximant: stage-m causets C_m whose n-stem set is Gamma
    (1_{E_m} -> 1_{N_Gamma} pointwise, since the stem set of C_m increases to
    that of C);
  * post-tail event D'_H (H principal, |H| = n, top t): some n-element down-set
    S ~ H whose top is below every element outside S.

Usage: python3 gc_review.py [out_path]
"""
import cmath
import sys
from itertools import permutations

OUT = []


def say(*a):
    s = " ".join(str(x) for x in a)
    OUT.append(s)
    print(s, flush=True)


def popcount(x):
    return bin(x).count("1")


# ------------------------------------------------------------------ enumeration
def downsets(past, n):
    """All down-sets of an n-element naturally labelled causet (bitmasks)."""
    res = [0]
    for i in range(n):
        pi = past[i]
        res = res + [D | (1 << i) for D in res if (D & pi) == pi]
    return res


def max_of(D, past, n):
    """Maximal elements of the down-set D (bitmask)."""
    below = 0
    for i in range(n):
        if D >> i & 1:
            below |= past[i]
    return D & ~below


def grow(levels_upto):
    """levels[n] = list of (past tuple, L, R, maxmask)."""
    levels = {1: [((0,), 0, 0, 1)]}
    for n in range(1, levels_upto):
        nxt = []
        for past, L, R, mx in levels[n]:
            for D in downsets(past, n):
                mD = max_of(D, past, n)
                nxt.append((past + (D,), L + popcount(mD), R + popcount(D), (mx & ~D) | (1 << n)))
        levels[n + 1] = nxt
    return levels


def amp(p, n, L, R):
    q = 1 - p
    return p ** L * q ** (n * (n - 1) // 2 - R)


# ------------------------------------------------------------------ shapes
def canon_sub(past, elems):
    """Canonical form of the induced subposet on the element list `elems`."""
    k = len(elems)
    rel = [(a, b) for a in range(k) for b in range(k) if past[elems[b]] >> elems[a] & 1]
    best = None
    for pm in permutations(range(k)):
        key = tuple(sorted((pm[a], pm[b]) for a, b in rel))
        if best is None or key < best:
            best = key
    return (k, best)


def kdownsets(past, n, k):
    """All k-element down-sets (bitmask)."""
    out = []

    def rec(i, D, size):
        if size == k:
            out.append(D)
            return
        if i == n or size + (n - i) < k:
            return
        rec(i + 1, D, size)
        if (D & past[i]) == past[i]:
            rec(i + 1, D | (1 << i), size + 1)
    rec(0, 0, 0)
    return out


CANON_CACHE = {}


def stemset(past, n, k):
    out = set()
    for D in kdownsets(past, n, k):
        el = [i for i in range(n) if D >> i & 1]
        # canonical form depends only on the relations among el (relabelled 0..k-1)
        sub = tuple(sum(1 << el.index(j) for j in el if past[e] >> j & 1) for e in el)
        if sub not in CANON_CACHE:
            CANON_CACHE[sub] = canon_sub(sub, list(range(k)))
        out.add(CANON_CACHE[sub])
    return frozenset(out)


def shape_of(past, n):
    sub = tuple(past)
    return canon_sub(sub, list(range(n)))


# shapes used below (canonical keys computed from explicit labelled reps)
def key(rep):
    return canon_sub(rep, list(range(len(rep))))


PT = key((0,))
CH2 = key((0, 1))
AN2 = key((0, 0))
CH3 = key((0, 1, 3))
LAM = key((0, 0, 3))      # two minima below one top
VEE = key((0, 1, 1))      # one below two
CP = key((0, 1, 0))       # 2-chain + point
AN3 = key((0, 0, 0))
NAMES = {PT: "pt", CH2: "chain2", AN2: "anti2", CH3: "chain3", LAM: "Lambda", VEE: "V", CP: "cp", AN3: "anti3"}


def nm(k):
    return NAMES.get(k, str(k))


# ------------------------------------------------------------------ events
def is_posttail(past, n, H_key, h):
    """D'_H at the finite stage: an h-element down-set S ~ H (principal) with every
    element outside S above the top of S."""
    for D in kdownsets(past, n, h):
        el = [i for i in range(n) if D >> i & 1]
        top = max(el)  # in a natural labelling the unique maximum of S has the largest label in S
        if any(i != top and not (past[top] >> i & 1) for i in el):
            continue  # S not principal with top `top`
        if any(not (past[j] >> top & 1) for j in range(n) if not D >> j & 1):
            continue
        sub = tuple(sum(1 << el.index(j) for j in el if past[e] >> j & 1) for e in el)
        if canon_sub(sub, list(range(h))) == H_key:
            return True
    return False


def skeleton(past, n, k):
    """K_k(C) = elements with at most k-1 ancestors."""
    return [i for i in range(n) if popcount(past[i]) <= k - 1]


def qpoch(q, N):
    r = 1
    for j in range(1, N + 1):
        r *= 1 - q ** j
    return r


def qpoch_inf(q):
    r, j = 1, 1
    while abs(q) ** j > 1e-18:
        r *= 1 - q ** j
        j += 1
    return r


def num_labellings(H_key, levels):
    n = H_key[0]
    return sum(1 for past, L, R, mx in levels[n] if shape_of(past, n) == H_key)


def amp_of_shape(p, H_key, levels):
    n = H_key[0]
    for past, L, R, mx in levels[n]:
        if shape_of(past, n) == H_key:
            return amp(p, n, L, R)


def nmax_shape(H_key):
    n, rel = H_key
    below = {a for a, b in rel}
    return n - len(below)


def main():
    M = 7
    levels = grow(M)
    say("stage counts:", [len(levels[n]) for n in range(1, M + 1)])
    ps = {"0.8+0.3i": 0.8 + 0.3j, "(1+i)/2": 0.5 + 0.5j, "-0.3+0.4i": -0.3 + 0.4j, "3/2": 1.5}

    say("=" * 90)
    say("A. stage totals sum_C A_p(C) (should be 1)")
    for nmp, p in ps.items():
        say(f"  p={nmp}:", [round(abs(sum(amp(p, n, L, R) for _, L, R, _ in levels[n]) - 1), 14) for n in range(1, M + 1)])

    say("=" * 90)
    say("B. Prop. 5 check: principal singleton covtree nodes N_{H} versus post-tail D'_H")
    say("   claimed: stage-m value of N_{H} = N(H)A_p(H)(q;q)_{m-n}  [growth-completion Prop. 5 / Thm A (C3)]")
    say("   reviewer: N_{H} = {C = S (+) C', S ~ H^-}, value N(H)A_p(H) prod_{j=1}^{m-n} (1 - q^j (1 - p^k)), k = #max(H^-)")
    p = 0.8 + 0.3j
    q = 1 - p
    principal = {1: [PT], 2: [CH2], 3: [CH3, LAM]}
    # level-4 principal shapes: H^- (+) top for every 3-poset H^-
    for rep in [(0, 1, 3, 7), (0, 0, 3, 7), (0, 1, 1, 7), (0, 1, 0, 7), (0, 0, 0, 7)]:
        principal.setdefault(4, []).append(key(rep))
    Hminus_k = {}
    for n, Hs in principal.items():
        for H in Hs:
            # #max of H^- = number of elements covered by the top
            Hm_n, rel = H
            top_candidates = [b for b in range(Hm_n) if all((a, b) in rel for a in range(Hm_n) if a != b)]
            t = top_candidates[0]
            # elements of H^-: all except t; maximal in H^- = not below any other non-top element
            others = [a for a in range(Hm_n) if a != t]
            k = sum(1 for a in others if not any((a, b) in rel for b in others))
            Hminus_k[H] = k
    for n, Hs in principal.items():
        for H in Hs:
            NH = num_labellings(H, levels)
            AH = amp_of_shape(p, H, levels)
            k = Hminus_k[H]
            for m in range(n, M + 1):
                val = sum(amp(p, m, L, R) for past, L, R, mx in levels[m] if stemset(past, m, n) == frozenset([H]))
                claimed = NH * AH * qpoch(q, m - n)
                mine = NH * AH
                for j in range(1, m - n + 1):
                    mine *= 1 - q ** j * (1 - p ** k)
                dpt = sum(amp(p, m, L, R) for past, L, R, mx in levels[m] if is_posttail(past, m, H, n))
                say(f"  H={nm(H)} n={n} k={k} m={m}: N_H stage value {val:.6f} | claimed {claimed:.6f} (err {abs(val-claimed):.1e})"
                    f" | reviewer {mine:.6f} (err {abs(val-mine):.1e}) | D'_H value {dpt:.6f} vs claimed formula err {abs(dpt-claimed):.1e}")

    say("  explicit counterexample to 'n-stem set {H} iff every element outside H lies above t':")
    say("   C = {a<b, a<c} plus an infinite chain above b and c: 2-stems {a,b},{a,c}, both chain2,")
    say("   so C in N_{chain2}; but c is not above b and b is not above c, so C is not in D'_{chain2}.")
    say("   Level 1: N_{pt} = Omega (value 1), but the claimed formula gives (q;q)_inf =", f"{qpoch_inf(q):.6f}")

    say("=" * 90)
    say("C. Level-2 covtree limits via an exact 2-skeleton recursion (state: #minimal a, flag b = some element has exactly 1 ancestor)")
    for nmp, p in [("0.8+0.3i", 0.8 + 0.3j), ("(1+i)/2", 0.5 + 0.5j), ("-0.3+0.4i", -0.3 + 0.4j)]:
        q = 1 - p
        st = {(1, 0): 1 + 0j}
        res = {}
        for m in range(1, 401):
            new = {}
            for (a, b), w in st.items():
                t0 = q ** m                  # new minimal element
                t1 = a * p * q ** (m - 1)    # past = {x}, x minimal
                rest = 1 - t0 - t1           # everything else: does not change (a, b)
                for s, t in (((a + 1, b), t0), ((a, 1), t1), ((a, b), rest)):
                    new[s] = new.get(s, 0) + w * t
            st = new
            if m + 1 in (8, 50, 100, 200, 400):
                ch = sum(w for (a, b), w in st.items() if a == 1 and b == 1)
                an = sum(w for (a, b), w in st.items() if a >= 2 and b == 0)
                bo = sum(w for (a, b), w in st.items() if a >= 2 and b == 1)
                res[m + 1] = (ch, an, bo, abs(ch) + abs(an) + abs(bo))
        for mm, (ch, an, bo, tv) in res.items():
            say(f"  p={nmp} stage {mm}: chain-only {ch:.6f}  antichain-only {an:.6f}  both {bo:.6f}  TV {tv:.6f}")
        if abs(q) < 1:
            say(f"   (q;q)_inf = {qpoch_inf(q):.6f}  [N_chain2 = originary event = D'_pt]; p*(q;q)_inf = {p*qpoch_inf(q):.6f} [= D'_chain2]")

    say("=" * 90)
    say("D. Level-3 covtree total variation at p = 0.8+0.3i, stages m = 3..7 (sum over nodes of |stage value|)")
    p = 0.8 + 0.3j
    for m in range(3, M + 1):
        node = {}
        for past, L, R, mx in levels[m]:
            g = stemset(past, m, 3)
            node[g] = node.get(g, 0) + amp(p, m, L, R)
        say(f"  m={m}: nodes {len(node)}, TV {sum(abs(v) for v in node.values()):.4f}")

    say("=" * 90)
    say("E. Regularized-measure Lemma 2: K_n(C) ~ H  <=>  post-tail D'_H, checked on all labelled causets m <= 6, H principal n <= 4")
    bad = 0
    tot = 0
    for m in range(1, 7):
        for past, L, R, mx in levels[m]:
            for n, Hs in principal.items():
                if n > m:
                    continue
                K = skeleton(past, m, n)
                Kkey = None
                if len(K) == n:
                    sub = tuple(sum(1 << K.index(j) for j in K if past[e] >> j & 1) for e in K)
                    Kkey = canon_sub(sub, list(range(n)))
                for H in Hs:
                    tot += 1
                    if (Kkey == H) != is_posttail(past, m, H, n):
                        bad += 1
    say(f"  cases {tot}, mismatches {bad}")
    say("  NB at a finite stage both sides are stage-m statements; the infinite-causet equivalence is proved in REVIEW.md.")

    say("=" * 90)
    say("F. Theorem 2 / Prop. 6 headline numbers: P_n = sum_{principal |H|=n} N(H)|A_p(H)|, V_n (doubly principal), |kappa| = |(q;q)_inf|")
    # principal n-causet = G (+) top with G any labelled (n-1)-causet: |A| = |A(G)| |p|^{#max G}
    # doubly principal n-causet = G (+) u (+) v with G any labelled (n-2)-causet: |A| = |A(G)| |p|^{#max G + 1}
    levels8_needed = True
    for nmp, p in [("3/2", 1.5), ("(1+i)/2", 0.5 + 0.5j), ("0.8+0.3i", 0.8 + 0.3j)]:
        q = 1 - p
        kap = abs(qpoch_inf(q))
        Pn, Vn = [], []
        for n in range(1, 9):
            g = n - 1
            if g == 0:
                Pn.append(1.0)
            else:
                Pn.append(sum(abs(amp(p, g, L, R)) * abs(p) ** popcount(mx) for _, L, R, mx in levels[g]))
            g2 = n - 2
            if g2 < 0:
                Vn.append(0.0)
            elif g2 == 0:
                Vn.append(abs(p))  # chain2: A = p
            else:
                Vn.append(sum(abs(amp(p, g2, L, R)) * abs(p) ** (popcount(mx) + 1) for _, L, R, mx in levels[g2]))
        # P_9 from labelled 8-causets streamed from stage 7
        P9 = 0.0
        for past, L, R, mx in levels[7]:
            for D in downsets(past, 7):
                mD = max_of(D, past, 7)
                L2, R2 = L + popcount(mD), R + popcount(D)
                mx2 = (mx & ~D) | (1 << 7)
                P9 += abs(p) ** L2 * abs(q) ** (28 - R2) * abs(p) ** popcount(mx2)
        Pn.append(P9)
        V9 = sum(abs(amp(p, 7, L, R)) * abs(p) ** (popcount(mx) + 1) for _, L, R, mx in levels[7])
        Vn.append(V9)
        say(f"  p={nmp}: |(q;q)_inf| = {kap:.6f}")
        say("    |kappa| P_n, n=1..9: " + ", ".join(f"{kap*x:.4g}" for x in Pn))
        say("    V_n,        n=1..9: " + ", ".join(f"{x:.4g}" for x in Vn))
        a, b = abs(p), abs(q)
        t = a + b
        s = b / t
        cs = qpoch_inf(s).real
        say("    two-cap bound |p| t^(n-2) c_s, n=2..9: " + ", ".join(f"{a * t ** (n - 2) * cs:.4g}" for n in range(2, 10)))
        say("    reviewer's covtree-singleton bound |c(q)| V_n/|p| (doubly principal N_{H} = D'_{H^-}), n=2..9: "
            + ", ".join(f"{kap * Vn[n - 1] / a:.4g}" for n in range(2, 10)))

    with open(sys.argv[1] if len(sys.argv) > 1 else "/dev/null", "w") as fh:
        fh.write("\n".join(OUT) + "\n")


if __name__ == "__main__":
    main()
