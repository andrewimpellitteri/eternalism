"""Exact checks for the partial-record coverage boundary. Standard library only."""
from fractions import Fraction as F
from itertools import combinations


def hidden_blocks(m, B, access):
    """access: set of flat positions 0..mB-1; returns blocks with no access."""
    hidden = 0
    for b in range(m):
        if not any(b * B + j in access for j in range(B)):
            hidden += 1
    return hidden


def targeted(m, B, k):
    best = None
    for access in combinations(range(m * B), k):
        h = hidden_blocks(m, B, set(access))
        best = h if best is None else min(best, h)
    assert best == max(0, m - k), (m, B, k, best)
    return best


def random_expectation_enum(m, B, f, gamma):
    """Enumerate all access sets with their binomial probability."""
    n = m * B
    total = F(0)
    for k in range(n + 1):
        prob = f ** k * (1 - f) ** (n - k)
        for access in combinations(range(n), k):
            total += prob * gamma ** hidden_blocks(m, B, set(access))
    return total


def random_expectation_formula(m, B, f, gamma):
    ph = (1 - f) ** B
    return (1 - ph * (1 - gamma)) ** m


if __name__ == "__main__":
    for m in range(1, 6):
        for B in range(1, 4):
            for k in range(m * B + 1):
                targeted(m, B, k)
    print("targeted minimum H = max(0, m-k) verified for m<=5, B<=3, all k")

    for m, B, f, g in [
        (3, 2, F(1, 3), F(1, 2)),
        (4, 3, F(1, 2), F(1, 4)),
        (5, 2, F(2, 3), F(3, 4)),
        (2, 4, F(1, 5), F(1, 3)),
    ]:
        a = random_expectation_enum(m, B, f, g)
        b = random_expectation_formula(m, B, f, g)
        assert a == b, (m, B, f, g, a, b)
        print(f"random m={m} B={B} f={f} gamma={g}: E[V]={a} exact")

    # Correlated records are easier to erase than independent bits at f near 1.
    m, B, f = 100, 4, F(9, 10)
    block_exp = m * (1 - f) ** B
    indep_exp = m * B * (1 - f)
    assert block_exp < indep_exp
    print(f"exponent at f=9/10, B=4: block={float(block_exp):.4g} "
          f"independent={float(indep_exp):.4g}")
    print("All exact checks passed.")
