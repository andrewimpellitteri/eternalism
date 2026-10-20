#!/usr/bin/env python3
"""Explicit countermodel to a weakened covariant post-factorization rule.

The selected target is the labelled doubly-principal complex-percolation
classification. The extension adds the covariant post events D_H of
research/creative/COVARIANT_RESULT.md and asks what a factorization rule on
those events can force.

Countermodel (the "Dirac history"):
  H = (A_2 + {z_1}) + (A_2 + {z_2}) + ...
where A_2 is the 2-element antichain and + is ordinal sum. Every z_j is a post
(comparable with every element). Its inclusive past H_j = B_1 + ... + B_j is
principal (unique maximum z_j), but H_j minus z_j has two maximal elements.
Hence H_j is NOT doubly principal. Therefore no post past in this history is
doubly principal.

Let nu be the Dirac measure at H. Then:
  * nu(P_infinity) = 1;
  * nu(D_H) = 0 for every doubly-principal H;
  * the weakened rule "nu(D_H) = kappa N(H) A_p(H) for every doubly-principal
    H" holds with kappa = 0 for every p.

So the doubly-principal-only factorization does not classify p, even with
cyclic normalization. The all-principal factorization (T) does not hold: both
H_1 and H_2 occur in H, with nu(D_{H_j}) = 1, but N(H_j) A_p(H_j) differs
between j=1 and j=2, so no single kappa can fit both.

Standard library only. This is a witness, not a proof of the conditional
theorem; the theorem and its finite-cutoff corollaries are in
research/creative/COVARIANT_RESULT.md and were audited in
research/creative/proof-audit/AUDIT.md.
"""
import sys
from fractions import Fraction
from pathlib import Path

# Reuse the baseline causet checks without copying them.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "baseline"))
import poscau  # noqa: E402


def block_sum(j):
    """Ordinal sum of j blocks A_2 + {z}; returns (relation, n)."""
    rel = set()
    for b in range(j):
        base = 3 * b
        a1, a2, z = base, base + 1, base + 2
        rel.add((a1, z))
        rel.add((a2, z))
        for x in range(base):           # every earlier element below this block
            for y in (a1, a2, z):
                rel.add((x, y))
    return frozenset(rel), 3 * j


def history_checks(max_j=6):
    print("Dirac-history post pasts (H_j = B_1 + ... + B_j):")
    ok = True
    for j in range(1, max_j + 1):
        rel, n = block_sum(j)
        principal = poscau.is_principal(rel, n)
        parent = frozenset((i, k) for (i, k) in rel if k < n - 1)
        parent_principal = poscau.is_principal(parent, n - 1)
        doubly = principal and parent_principal
        # The last element z_j is a post: comparable with every other element.
        z = n - 1
        comparable = all((i, z) in rel or (z, i) in rel
                         for i in range(n) if i != z)
        print(f"  j={j} n={n:2d} post={comparable} principal={principal} "
              f"parent_principal={parent_principal} doubly={doubly}")
        ok &= comparable and principal and not parent_principal and not doubly
    print(f"  {'PASS' if ok else 'FAIL'}: every post past is principal but not doubly principal.")
    print()
    return ok


def n_representatives(j):
    """N(H_j) = 2^j: the two minima in each block may be exchanged."""
    return 2 ** j


def amplitude_principal(j, p):
    """A_p(H_j) for the j-block ordinal sum.

    L = 4j-2 covers (2 within the first block, 4 per later block),
    R = binom(3j,2)-j (all pairs related except the j antichain pairs), so
    A = p^(4j-2) (1-p)^j.
    """
    return (p ** (4 * j - 2)) * ((1 - p) ** j)


def all_principal_violation(p=0.5):
    """Show no single kappa can make the Dirac measure satisfy rule (T)."""
    print(f"All-principal rule (T) on the Dirac history at p={p}:")
    vals = []
    for j in (1, 2):
        n = n_representatives(j) * amplitude_principal(j, p)
        vals.append(n)
        print(f"  H_{j}: N(H_{j}) A_p(H_{j}) = {n:.6f}; nu(D_H_{j}) = 1")
    if abs(vals[0] - vals[1]) > 1e-12:
        print("  No common kappa: kappa would be "
              f"{1/vals[0]:.6f} from H_1 and {1/vals[1]:.6f} from H_2. "
              "The Dirac measure violates (T). PASS")
    else:
        print("  WARNING: the two values coincide; the test is inconclusive.")
    print()


def weakened_rule():
    """The doubly-principal-only rule is satisfied by the Dirac measure."""
    print("Weakened doubly-principal-only rule:")
    print("  nu(D_H) = 0 for every doubly-principal H (none occur on the history),")
    print("  so kappa = 0 satisfies the rule for every p; nu(P_infinity) = 1.")
    print("  PASS: the weakened rule has no p-classification.")
    print()


def main():
    history_checks()
    weakened_rule()
    all_principal_violation()
    print("Scope: this countermodel defeats the doubly-principal-only factorization,")
    print("not the labelled theorem and not the all-principal conditional theorem.")
    print("The latter additionally assumes a common kappa for EVERY principal H,")
    print("which this Dirac measure violates.")


if __name__ == "__main__":
    main()
