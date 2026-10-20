#!/usr/bin/env python3
"""Reproduce Dowker-Zalel arXiv:2212.01149v2 Fig. 6/7 finite-level values.

Published result being reproduced (explicit scope):
  For Complex Transitive Percolation, on reduced poscau (Fig. 6) and
  doubly-reduced poscau (Fig. 7), the level-n minimum variation is
  zeta_n^min = |p| + |1-p| - 1 (reduced), and for valency>1 nodes
  zeta_bar_n^min = |p| + |1-p| - 1 (doubly reduced), for n = 2, 3, 4 in the
  regions coloured in those figures.

The figures are numerical and show regions, not a theorem for every p; this
script reports equality on a grid and records mismatches rather than asserting
the figures' full range. Standard library only.
"""
from fractions import Fraction
import cmath
import math

import poscau


FORMULA = lambda p: abs(p) + abs(1 - p) - 1


def count_causets():
    print("Naturally labelled causet counts (levels 1-6):")
    for n in range(1, 7):
        print(f"  n={n}: {len(poscau.causets(n))}")
    print()


def check_additivity(max_level=4, p=0.5 + 0.5j, tol=1e-9):
    """The pre-measure is additive: sum over children equals the parent."""
    worst = 0.0
    checks = 0
    for n in range(1, max_level + 1):
        for rel in poscau.causets(n):
            parent = poscau.amplitude(rel, n, p)
            total = sum(poscau.amplitude(c, n + 1, p)
                        for c, _, _ in poscau.children(rel, n))
            worst = max(worst, abs(total - parent))
            checks += 1
    print(f"Additivity over {checks} causets (levels 1-{max_level}): "
          f"max |sum children - parent| = {worst:.3e} "
          f"({'PASS' if worst < tol else 'FAIL'})")
    print()


def check_real_probability(p=0.5, max_level=4, tol=1e-10):
    print(f"Real p={p}: all zeta must vanish (positive probability walk).")
    for doubly in (False, True):
        table = poscau.level_table(max_level, p, doubly)
        worst = max(abs(r["zeta"]) for n in table for r in table[n]["nodes"]
                    if r["zeta"] is not None)
        print(f"  {'doubly-reduced' if doubly else 'reduced'}: "
              f"max |zeta| = {worst:.3e} "
              f"({'PASS' if worst < tol else 'FAIL'})")
    print()


def check_level_two_analytic(p, tol=1e-10):
    """At level 2, the reduced zeta minimum and doubly zeta_bar minimum
    equal |p|+|q|-1. Not every node attains it (the non-principal antichain
    node is higher), which is why the paper compares minima."""
    f = FORMULA(p)
    out = {}
    for doubly in (False, True):
        table = poscau.level_table(2, p, doubly)
        vals = [r["zeta"] for r in table[2]["nodes"]
                if r["zeta"] is not None and (not doubly or r["valency"] > 1)]
        out[doubly] = min(vals)
    print(f"Level-2 analytic check at p={p}: formula={f:.12f}, "
          f"reduced min={out[False]:.12f}, doubly zeta_bar min={out[True]:.12f} "
          f"({'PASS' if all(abs(v - f) < tol for v in out.values()) else 'FAIL'})")
    print()


def reproduce_complex_point():
    p = 0.5 + 0.5j
    f = FORMULA(p)
    print(f"Fig. 6/7 check at p={p} (|p|+|1-p|-1={f:.12f}):")
    print("  level | reduced zeta_min | doubly zeta_bar_min | nodes (red/dbl)")
    for n in (2, 3, 4):
        red = poscau.level_table(n, p, False)[n]
        dbl = poscau.level_table(n, p, True)[n]
        print(f"  {n:5d} | {red['zeta_min']:.12f} | "
              f"{dbl['zeta_bar_min']:.12f} | {red['count']}/{dbl['count']}")
        assert abs(red["zeta_min"] - f) < 1e-9
        assert abs(dbl["zeta_bar_min"] - f) < 1e-9
    print("  PASS: both minima equal the published formula for n=2,3,4.")
    print()


def grid_region(step=0.1, lo=-0.5, hi=1.5, max_level=4):
    """Count grid points where the finite-level minima equal the formula."""
    npts = 0
    stats = {False: {2: 0, 3: 0, 4: 0}, True: {2: 0, 3: 0, 4: 0}}
    mismatches = {False: [], True: []}
    vals = [round(lo + k * step, 10) for k in range(round((hi - lo) / step) + 1)]
    for re in vals:
        for im in vals:
            p = complex(re, im)
            f = FORMULA(p)
            npts += 1
            for doubly in (False, True):
                table = poscau.level_table(max_level, p, doubly)
                for n in (2, 3, 4):
                    row = table[n]
                    v = row["zeta_bar_min"] if doubly else row["zeta_min"]
                    if v is not None and abs(v - f) < 1e-9:
                        stats[doubly][n] += 1
                    elif len(mismatches[doubly]) < 3:
                        mismatches[doubly].append((p, n, v, f))
    print(f"Grid equality over p in [{lo},{hi}]^2, step {step} ({npts} points):")
    for doubly in (False, True):
        name = "doubly-reduced (zeta_bar)" if doubly else "reduced (zeta)"
        print(f"  {name}: " + ", ".join(
            f"n={n}: {stats[doubly][n]}/{npts}" for n in (2, 3, 4)))
    print("  First mismatches (shape: p, level, computed, formula):")
    for doubly in (False, True):
        name = "doubly" if doubly else "reduced"
        for m in mismatches[doubly]:
            print(f"    {name}: {m}")
    print("  NOTE: the paper's figures colour regions, so mismatches outside")
    print("  those regions are expected; this grid is not a proof of the")
    print("  suggested all-level behaviour.")
    print()


def check_improved_criterion(p=0.5 + 0.5j, max_level=4):
    """Print Eq. (30)-(31) inputs; finite levels only, not the limit."""
    print(f"Improved valency>1 criterion inputs at p={p} (Eq. 30-31):")
    for doubly in (False, True):
        table = poscau.level_table(max_level, p, doubly)
        print(f"  {'doubly-reduced' if doubly else 'reduced'}:")
        for n in (2, 3, 4):
            r = table[n]
            print(f"    n={n}: zeta_bar_min={r['zeta_bar_min']:.6f} "
                  f"S_n={r['S']:.6f} S_bar={r['S_bar']:.6f} "
                  f"S_v1={r['S_v1']:.6f} nodes={r['count']}")
        print()
    print("  These are finite-level diagnostics; Eq. (31) is asymptotic.")
    print()


# ---- Candidate finite certificate (separate from the published baseline) ----

def abs_amp_sqrt2(k):
    """(sqrt(2)/2)^k as (a, b) with value a + b*sqrt(2), exact."""
    if k % 2 == 0:
        return Fraction(1, 2 ** (k // 2)), Fraction(0)
    return Fraction(0), Fraction(1, 2 ** ((k + 1) // 2))


def finite_certificate(max_level=6):
    """Sum |A(C)| over doubly-principal causets at levels 5 and 6.

    Expected (research/creative/RESULT.md, verify_small.py):
      V_5 = 3/4 + 3*sqrt(2)/16, V_6 = 31/32 + 55*sqrt(2)/64.
    This is the selected target's certificate, not the published baseline.
    """
    print("Candidate finite certificate at p=(1+i)/2 (exact Q(sqrt2)):")
    expected = {5: (Fraction(3, 4), Fraction(3, 16)),
                6: (Fraction(31, 32), Fraction(55, 64))}
    for n in (5, 6):
        a = Fraction(0)
        b = Fraction(0)
        count = 0
        for rel in poscau.causets(n):
            if not poscau.is_principal(rel, n):
                continue
            parent = frozenset((i, j) for (i, j) in rel if i < n - 1 and j < n - 1)
            if not poscau.is_principal(parent, n - 1):
                continue
            L, R = poscau.stats(rel, n)
            k = L + n * (n - 1) // 2 - R
            da, db = abs_amp_sqrt2(k)
            a += da
            b += db
            count += 1
        ok = (a, b) == expected[n]
        print(f"  n={n}: doubly-principal causets={count}, "
              f"V_{n} = {a} + {b}*sqrt(2) = {float(a + b * math.sqrt(2)):.12f} "
              f"[{'PASS' if ok else 'FAIL'}]")
    print("  Expected: V_5 = 3/4 + 3*sqrt(2)/16,")
    print("            V_6 = 31/32 + 55*sqrt(2)/64.")
    print()


def main():
    count_causets()
    check_additivity()
    check_real_probability()
    check_level_two_analytic(0.5 + 0.5j)
    reproduce_complex_point()
    check_improved_criterion()
    grid_region()
    finite_certificate()


if __name__ == "__main__":
    main()
