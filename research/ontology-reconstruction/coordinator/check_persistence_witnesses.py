"""Exact finite witnesses for PERSISTENCE_CONVENTIONS.md, not a census proof."""

from fractions import Fraction as F


def point(t, x=0):
    return (F(t), F(x), F(0), F(0))


def le(x, y):
    dt = y[0] - x[0]
    return dt >= 0 and dt * dt >= sum((y[i] - x[i]) ** 2 for i in range(1, 4))


def lt(x, y):
    return x != y and le(x, y)


def chron(x, y):
    dt = y[0] - x[0]
    return dt > 0 and dt * dt > sum((y[i] - x[i]) ** 2 for i in range(1, 4))


def realm(kind, b, x):
    return {
        "I": chron(x, b) or x == b,
        "J": le(x, b),
        "B": not lt(b, x),
        "C": not chron(b, x),
    }[kind]


def main():
    b, null_later = point(0), point(1, 1)
    assert lt(b, null_later) and not chron(b, null_later)
    assert realm("I", b, b) and not realm("I", null_later, b)
    for kind in ("J", "B", "C"):
        assert realm(kind, null_later, b)
    print("PASS: I fails causal persistence on the explicit null step")

    past_null, future_null = point(-1, 1), point(1, 1)
    assert not realm("I", b, past_null)
    assert not realm("B", b, future_null) and realm("C", b, future_null)
    for k in range(1, 6):
        eps = F(1, k)
        assert realm("I", b, point(-1 - eps, 1))
        assert realm("B", b, point(1, 1 + eps))
    print("PASS: explicit sequences expose both omitted null-boundary limits")

    x, y = point(0, 2), point(2, -1)
    for kind in ("B", "C"):
        assert realm(kind, b, x) and realm(kind, x, y) and not realm(kind, b, y)
    print("PASS: B and C fail transitivity on the same exact triple")

    past_null_standpoint = point(-1, -1)
    spacelike_standpoint = point(-F(1, 4), -F(1, 2))
    assert chron(past_null_standpoint, spacelike_standpoint)
    assert not le(b, spacelike_standpoint) and not le(spacelike_standpoint, b)
    for s in (F(2), F(3), F(4), F(6), F(8)):
        # R=3, Z=5 gives q=(-4,5), spacelike length 3.
        assert chron(point(-4, 5), point(0, s))
        assert 2 * 5 * s - 3 ** 2 - s ** 2 > 0
    print("PASS: null-to-spacelike and saturation witnesses match the proof")
    print("All finite witness checks pass; exhaustive classification remains analytic.")


if __name__ == "__main__":
    main()
