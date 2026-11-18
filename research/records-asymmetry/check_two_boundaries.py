"""Exact checks for TWO_BOUNDARIES.md. Run with python3 -B check_two_boundaries.py."""

from collections import Counter, defaultdict
from itertools import product
from math import log2

from push_records import make


def block_path(steps, sign):
    return tuple(
        sign * (2 * block + offset)
        for block in range(steps // 4)
        for offset in (1, 2, 1, 2)
    )


def check_line(limit=24):
    # Reveal a fair rotor only on its first visit. Weights have denominator 2**limit.
    accepted = defaultdict(Counter)

    def visit(position, heading, rotors, lit, path, weight):
        if path and not lit:
            accepted[len(path)][path] += weight
        if len(path) == limit:
            return
        choices = (rotors[position],) if position in rotors else (0, 1)
        for rotor in choices:
            direction = -heading if rotor else heading
            arrival = position + direction
            visit(arrival, direction, {**rotors, position: 1 - rotor},
                  lit ^ {arrival}, path + (arrival,), weight // len(choices))

    visit(0, 1, {}, set(), (), 1 << limit)
    for steps in range(1, limit + 1):
        expected = Counter()
        if steps % 4 == 0:
            for sign in (-1, 1):
                expected[block_path(steps, sign)] = 1 << (limit - steps // 2 - 1)
        assert accepted[steps] == expected, steps


def ring_paths(size, steps):
    step, _, _ = make(size)
    by_final_marks = defaultdict(Counter)
    for rotors in range(1 << size):
        state = (0, 0, rotors, 0)
        path = []
        for _ in range(steps):
            state = step(*state)
            path.append(state[0])
        by_final_marks[state[3]][tuple(path)] += 1
    return by_final_marks


def summary(paths):
    n = sum(paths.values())
    return n, len(paths), -sum((v / n) * log2(v / n) for v in paths.values())


def variable_sites(paths, time, width):
    # Each triple is (current footprint, previous-window parity, next-window parity).
    result = {}
    for site in range(12):
        table = Counter()
        for path, weight in paths.items():
            mark = path[:time].count(site) % 2
            past = path[time-width:time].count(site) % 2
            future = path[time:time+width].count(site) % 2
            table[mark, past, future] += weight
        if len({row[0] for row in table}) > 1:
            result[site] = table
    return result


def check_ring():
    cells = ring_paths(12, 8)
    accepted = cells[0]
    assert accepted == {tuple(x % 12 for x in block_path(8, s)): 128 for s in (-1, 1)}
    assert summary(sum(cells.values(), Counter())) == (4096, 41, 5.0)
    soft = sum((c for mask, c in cells.items() if mask.bit_count() <= 2), Counter())
    assert summary(soft) == (2048, 14, 3.625)
    zero = (0, 0, 0)
    both = {zero: 128, (1, 1, 1): 128}
    past = {zero: 128, (1, 1, 0): 128}
    future = {zero: 128, (1, 0, 1): 128}
    assert variable_sites(accepted, 3, 2) == {2: both, 10: both}
    assert variable_sites(accepted, 2, 1) == {1: future, 2: past, 10: past, 11: future}
    assert len(ring_paths(4, 8)[0]) == 4  # outside the unwrapped regime


def check_tape():
    counts = {}
    for steps in (4, 8, 12, 16):
        accepted = 0
        for directions in product((-1, 1), repeat=steps):
            position = 0
            lit = set()
            for direction in directions:
                position += direction
                lit.symmetric_difference_update((position,))
            accepted += not lit
        counts[steps] = accepted
    assert counts == {4: 4, 8: 32, 12: 304, 16: 3152}
    return counts


def ground_film(path):
    marks = frozenset()
    frames = []
    for site in path:
        marks = marks ^ {site}
        frames.append(marks)
    return tuple(frames)


def check_photographs():
    films = []
    midpoint = Counter()
    with_position = Counter()
    for directions in product((-1, 1), repeat=8):
        path = []
        position = 0
        for sign in directions:
            position += sign
            path.append(position)
        film = ground_film(path)
        films.append(film)
        decoded = [next(iter(old ^ new)) for old, new in zip((frozenset(),) + film, film)]
        assert decoded == path
        if not film[-1]:
            midpoint[tuple(sorted(film[3]))] += 1
            with_position[film[3], path[3]] += 1
    assert midpoint == {(): 16, (-2, 0): 4, (-1, 1): 4, (0, 2): 4,
                        (-3, -1): 2, (1, 3): 2}
    assert summary(midpoint) == (32, 6, 2.125)
    assert summary(with_position) == (32, 10, 3.125)
    rotor_films = [ground_film(block_path(8, sign)) for sign in (-1, 1)]
    assert len({film[1] for film in rotor_films}) == 2
    assert all(not film[3] for film in rotor_films)

    # Verify the largest-atom bound before conditioning, for all 256 schedules.
    for schedule in product((False, True), repeat=8):
        indices = [i for i, observe in enumerate(schedule) if observe]
        counts = Counter(tuple(film[i] for i in indices) for film in films)
        assert max(counts.values()) <= 2 ** (8 - len(indices))


def check_midpoint_construction():
    for n in range(1, 9):
        photographs = set()
        for choices in product((0, 1), repeat=n):
            half = []
            for i, choice in enumerate(choices):
                offsets = (1, 2, 1, 2, 3) if choice else (1, 0, 1, 2, 3)
                half.extend(3 * i + offset for offset in offsets)
            half.extend(range(3 * n - 1, -1, -1))
            path = half + half
            assert len(path) == 16 * n
            assert all(abs(a - b) == 1 for a, b in zip([0] + path, path))
            film = ground_film(path)
            assert not film[-1]
            photographs.add(film[8 * n - 1])
        assert len(photographs) == 2 ** n


if __name__ == "__main__":
    check_line()
    check_ring()
    print("Line paths and cylinder probabilities verified at all durations 1–24.")
    print("Ring counts, local truth tables and wraparound control verified.")
    print("Accepted direction tapes:", check_tape())
    check_photographs()
    check_midpoint_construction()
    print("Photograph partitions, arbitrary eight-step schedules and midpoint codes verified.")
