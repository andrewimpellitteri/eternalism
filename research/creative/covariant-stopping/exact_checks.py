"""Small exact checks for the covariant-stopping note. Standard library only."""
from fractions import Fraction as F
from itertools import product


def stopping_index_witness():
    # Position pair of comparable elements in the 3-order (one relation + isolate).
    tau = {(0, 1): 3, (0, 2): 2, (1, 2): 2}
    assert sum(value == 2 for value in tau.values()) == 2
    assert sum(value == 3 for value in tau.values()) == 1
    conditional = {k: F(sum(v == k for v in tau.values()), len(tau)) for k in (2, 3)}
    assert conditional == {2: F(2, 3), 3: F(1, 3)}
    for t0, t1, t2 in ((1, 1, 1), (1, 2, 10)):
        per_path = F(t0 * t1, (t0 + t1) * (t0 + 2 * t1 + t2))
        assert per_path > 0
        print("CSG", (t0, t1, t2), "per-path", per_path,
              "class", 3 * per_path, "conditional tau", conditional)


def hidden_record_nonmarkov():
    flip = F(1, 4)
    emit_one = {0: F(1, 4), 1: F(3, 4)}
    transition = {(s, u): (1 - flip if s == u else flip)
                  for s in (0, 1) for u in (0, 1)}

    def prob(xs):
        total = F(0)
        for states in product((0, 1), repeat=len(xs)):
            weight = F(1, 2)
            for i, x in enumerate(xs):
                weight *= emit_one[states[i]] if x else 1 - emit_one[states[i]]
                if i:
                    weight *= transition[states[i - 1], states[i]]
            total += weight
        return total

    p_0 = prob((0, 1, 1)) / prob((0, 1))
    p_1 = prob((1, 1, 1)) / prob((1, 1))
    p_last = (prob((0, 1, 1)) + prob((1, 1, 1))) / (prob((0, 1)) + prob((1, 1)))
    assert (p_0, p_1, p_last) == (F(15, 28), F(7, 12), F(9, 16))
    print("hidden record:", p_0, p_1, p_last)


if __name__ == "__main__":
    stopping_index_witness()
    hidden_record_nonmarkov()
