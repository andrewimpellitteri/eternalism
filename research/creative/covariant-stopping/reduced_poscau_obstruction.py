"""Exact k=5 certificate for a reduced-poscau variation obstruction.

Standard library only. Enumerates all naturally labelled 5-element posets,
keeps the ones with a unique maximal element, and groups the exponent
E(G)=L(G)+min(G)+C(5,2)-R(G).
"""
from collections import Counter
import csv
from decimal import Decimal, getcontext
from pathlib import Path


def principal_exponents(n=5):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    counts = Counter()
    bivariate = Counter()
    certificate = []
    for mask in range(1 << len(pairs)):
        pred = [0] * n
        succ = [0] * n
        for bit, (i, j) in enumerate(pairs):
            if mask >> bit & 1:
                pred[j] |= 1 << i
                succ[i] |= 1 << j

        # Natural labels force every relation to point forward. Check closure.
        transitive = True
        for i in range(n):
            later = succ[i]
            while later:
                bit = later & -later
                j = bit.bit_length() - 1
                later -= bit
                if succ[j] & ~succ[i]:
                    transitive = False
                    break
            if not transitive:
                break
        if not transitive or sum(row == 0 for row in succ) != 1:
            continue

        links = 0
        for i, j in pairs:
            if not (succ[i] >> j & 1):
                continue
            has_intermediate = any(
                (succ[i] >> z & 1) and (succ[z] >> j & 1)
                for z in range(i + 1, j)
            )
            links += not has_intermediate

        minima = sum(row == 0 for row in pred)
        relations = sum(row.bit_count() for row in succ)
        u = links + minima
        v = n * (n - 1) // 2 - relations
        exponent = u + v
        counts[exponent] += 1
        bivariate[u, v] += 1
        relations_list = [(i, j) for bit, (i, j) in enumerate(pairs) if mask >> bit & 1]
        certificate.append((mask, relations_list, links, minima, relations, u, v))
    return counts, bivariate, certificate


if __name__ == "__main__":
    counts, bivariate, certificate = principal_exponents(5)
    expected = {5: 1, 7: 3, 8: 6, 9: 4, 10: 11, 11: 8, 12: 6, 14: 1}
    expected_bivariate = {
        (5, 0): 1, (6, 1): 3, (6, 2): 6, (6, 3): 4, (6, 4): 3,
        (7, 3): 7, (7, 4): 8, (7, 5): 6, (8, 2): 1, (8, 6): 1,
    }
    assert counts == expected
    assert bivariate == expected_bivariate
    assert sum(counts.values()) == 40
    assert len(certificate) == 40

    certificate_path = Path(__file__).with_name("principal5_certificate.csv")
    with certificate_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(("mask_hex", "relations", "links_L", "minima", "relations_R", "u_L_plus_min", "v_10_minus_R"))
        for mask, relations_list, links, minima, relations, u, v in certificate:
            writer.writerow((f"0x{mask:03x}", ";".join(f"{i}<{j}" for i, j in relations_list),
                             links, minima, relations, u, v))

    # At p=(1+i)/2 and q=(1-i)/2, both moduli are 1/sqrt(2).
    # Thus r_5 = sum_e count[e] * 2^(-e/2).
    getcontext().prec = 30
    sqrt2 = Decimal(2).sqrt()
    r5_decimal = sum(
        Decimal(count) / (Decimal(2) ** (Decimal(exponent) / 2))
        for exponent, count in counts.items()
    )
    # Exact simplification: 105/128 + 9/(8 sqrt(2)) > 1 iff
    # 144/sqrt(2) > 23, which follows by squaring positive sides.
    assert 144 * 144 > 23 * 23 * 2
    assert r5_decimal > 1
    r6_decimal = r5_decimal / sqrt2
    assert sqrt2 < Decimal(3) / 2
    assert r6_decimal > 1
    print("principal 5-order exponent counts:", dict(sorted(counts.items())))
    print("bivariate counts (L+min, 10-R):", dict(sorted(bivariate.items())))
    print("wrote exact 40-row relation certificate:", certificate_path.name)
    print("r5 exact: 105/128 + 9/(8 sqrt(2))")
    print("r5 decimal:", r5_decimal)
    print("r6-double exact: 9/16 + 105/(128 sqrt(2)) > 71/64 > 1")
    print("r6-double decimal:", r6_decimal)
    for k in range(1, 5):
        small_counts, _, _ = principal_exponents(k)
        rk = sum(
            Decimal(count) / (Decimal(2) ** (Decimal(exponent) / 2))
            for exponent, count in small_counts.items()
        )
        print(f"k={k} uniform principal-block sum at |p|=|q|=1/sqrt(2): {rk}")
