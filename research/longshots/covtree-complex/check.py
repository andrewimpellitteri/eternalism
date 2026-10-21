"""Boundary and interior checks for covtree complex-percolation amplitudes."""
import cmath
import math


def partial(q, m):
    p = 1 - q
    z = p
    for j in range(1, m):
        z *= 1 - q ** j
    return z


def main():
    # Unit factors never approach 1.
    for q in (cmath.exp(1j), cmath.exp(1j * math.sqrt(2)), -1, 1):
        assert all(abs(abs((1 - q ** j) - 1) - 1) < 1e-12 for j in range(1, 50))
    print("unit-q factor distance |(1-q^j)-1| = 1 checked")

    for q, name in [(cmath.exp(1j), "q=e^i"),
                    (cmath.exp(1j * math.sqrt(2)), "q=e^(i sqrt2)")]:
        vals = []
        for m in (10, 50, 100, 200, 500, 1000, 2000, 5000):
            vals.append((m, abs(partial(q, m))))
        print(name, [(m, round(v, 6)) for m, v in vals])
        assert len({round(v, 6) for _, v in vals}) > 1

    q = 0.5
    vals = [abs(partial(q, m)) for m in (50, 100, 200, 500, 1000, 2000)]
    print("q=1/2:", [round(v, 12) for v in vals])
    assert max(vals) - min(vals) < 1e-12

    for q in (-1, 1):
        z = partial(q, 5)
        assert abs(z) < 1e-12
    print("root-of-unity originary products vanish at the tested stages")
    print("PASS")


if __name__ == "__main__":
    main()
