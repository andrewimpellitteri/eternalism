#!/usr/bin/env python3
"""Universal next-post kernel coefficients R_k.

For a post with past H, the next post past is J = H + S (ordinal sum), where S
is a principal order whose only post is its maximum.  Covers from the post to S
are the minimal elements of S.  Therefore

    N(J) A(J) = N(H) A(H) * A(S) p^{min(S)},

and the sum over next posts of size n+k factorizes as N(H)A(H) R_k with

    R_k = sum_{S: principal, only post = max, |S|=k} A_p(S) p^{min(S)}.

This is a proof of the stationarity of the next-post kernel (a finite check is
included against probe.py).  A rank-only measure with kappa_n=lambda^n requires
1 = sum_k R_k lambda^k.
"""
import sys
from fractions import Fraction
from pathlib import Path
import cmath
import math

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "experiments" / "baseline"))
import poscau  # noqa: E402


def posts(rel, n):
    out = []
    for i in range(n):
        if all((j, i) in rel for j in range(i)) and all((i, j) in rel for j in range(i + 1, n)):
            out.append(i)
    return out


def minima(rel, n):
    return [i for i in range(n) if not any((j, i) in rel for j in range(i))]


def R_coeffs(max_k, p):
    out = {}
    for k in range(1, max_k + 1):
        total = 0
        count = 0
        for S in poscau.causets(k):
            if posts(S, k) != [k - 1]:
                continue
            m = len(minima(S, k))
            total += poscau.amplitude(S, k, p) * (p ** m)
            count += 1
        out[k] = (total, count)
    return out


def durand_kerner(coeffs, iterations=200):
    """Roots of c[0] + c[1] z + ... + c[n] z^n, complex coefficients."""
    n = len(coeffs) - 1
    c = [complex(x) for x in coeffs]
    # normalize leading
    lead = c[-1]
    c = [x / lead for x in c]
    roots = [cmath.exp(2j * math.pi * k / n) * (0.4 + 0.9) for k in range(n)]
    for _ in range(iterations):
        new = []
        for i, z in enumerate(roots):
            num = sum(c[j] * z ** j for j in range(n + 1))
            den = 1
            for j, w in enumerate(roots):
                if i != j:
                    den *= (z - w)
            new.append(z - num / den if den != 0 else z)
        roots = new
    return roots


def report(p, max_k=6):
    print(f"p={p}")
    R = R_coeffs(max_k, p)
    for k in range(1, max_k + 1):
        v, c = R[k]
        print(f"  R_{k} = {v!r}  (terms {c})")
    # polynomial 1 - sum R_k z^k, coefficients [1, -R1, ..., -Rmax]
    coeffs = [1.0] + [-R[k][0] for k in range(1, max_k + 1)]
    roots = durand_kerner(coeffs)
    print("  roots of 1 - sum R_k z^k (up to k=%d):" % max_k)
    for z in sorted(roots, key=lambda z: abs(z)):
        print(f"    {z:.6g}  |z|={abs(z):.6g}")
    print()


if __name__ == "__main__":
    report(0.5, 6)
    report(0.5 + 0.5j, 6)
    report(0.2 + 0.7j, 6)
