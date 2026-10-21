#!/usr/bin/env python3
"""Exact stage-4 all-nonzero continuation of the fixed BCPH phase seed."""
from collections import defaultdict
from fractions import Fraction as Fr
from pathlib import Path
import importlib.util


ROOT = Path(__file__).resolve().parents[3]
SEED = ROOT / "research/longshots/birth-order-interference/birth_order_interference.py"
spec = importlib.util.spec_from_file_location("birth_order_interference", SEED)
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)


def induced(causet, subset):
    old = sorted(subset)
    reindex = {x: i for i, x in enumerate(old)}
    return tuple(
        frozenset(reindex[j] for j in causet[i] if j in subset)
        for i in old
    )


def bell_check(model, max_parent_size):
    count, failures = 0, []
    for n in range(1, max_parent_size + 1):
        for C in model.levels[n]:
            down = b.downsets(C)
            for i, P in enumerate(down):
                for Q in down[i + 1 :]:
                    B = induced(C, P | Q)
                    idx = {old: new for new, old in enumerate(sorted(P | Q))}
                    Pbar = frozenset(idx[j] for j in P)
                    Qbar = frozenset(idx[j] for j in Q)
                    lhs = model.amp(C, P) * model.amp(B, Qbar)
                    rhs = model.amp(C, Q) * model.amp(B, Pbar)
                    count += 1
                    if lhs != rhs:
                        failures.append((C, P, Q, B, lhs, rhs))
    return count, failures


def rref(matrix, width):
    A = [list(row) for row in matrix if any(row)]
    pivots = []
    r = 0
    for c in range(width):
        pivot = next((i for i in range(r, len(A)) if A[i][c]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        d = A[r][c]
        A[r] = [v / d for v in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c]:
                d = A[i][c]
                A[i] = [v - d * w for v, w in zip(A[i], A[r])]
        pivots.append(c)
        r += 1
        if r == len(A):
            break
    # These are homogeneous equations, so inconsistency is impossible.
    return A, pivots, False


def stage4_norm_linear_system(seed, stage4_tree, r_values):
    """Norm-GC equations linear in x_C=|g_C|^2, y_C=|h_C|^2.

    A stage-4 path has norm |A(C)|^2 |r_P|^2 x_C for proper P, and
    |A(C)|^2 y_C for P=C. Variable order is x_0..x_6,y_0..y_6.
    """
    parents = seed.levels[3]
    parent_index = {C: i for i, C in enumerate(parents)}
    by_class = defaultdict(list)
    for C4 in stage4_tree[4]:
        C = C4[:3]
        P = frozenset(i for i in range(3) if i in C4[3])
        i = parent_index[C]
        coeff = [Fr(0)] * 14
        old_norm = seed.psi[C].abs2()
        if P == frozenset(range(3)):
            coeff[7 + i] = old_norm
        else:
            coeff[i] = old_norm * r_values[induced(C, P)].abs2()
        by_class[b.canon(C4)].append(coeff)

    equations = []
    for rows in by_class.values():
        if rows:
            ref = rows[0]
            equations.extend([[a - z for a, z in zip(row, ref)] for row in rows[1:]])
    reduced, pivots, inconsistent = rref(equations, 14)
    return len(equations), reduced, pivots, inconsistent


def main():
    # Exact stage-3 BCPH seed from the preceding audited longshot.
    x = Fr(1, 2)
    alpha1 = b.G(Fr(1, 4))
    phase = b.G(Fr(3, 5), Fr(4, 5))
    beta0 = alpha1 * phase
    alpha = (alpha1, alpha1, b.ONE - alpha1 / x)
    beta = (beta0, beta0, beta0, b.ONE - 3 * beta0)
    seed_amp = b.stage3_table_amp(x, alpha, beta)

    seed = b.Model("fixed BCPH stage-3 phase seed", seed_amp, 3)
    assert not seed.msr_ok()
    assert not seed.norm_gc_ok(2) and not seed.norm_gc_ok(3)

    # Bell/MSR parametrization: r_empty=1; r_P=h_P/g_P for previous P.
    # For each size-3 parent C choose a common nonzero g_C=q=1. Then MSR
    # uniquely sets r_C=1-sum_{proper P downset C} r_P.
    r = {(): b.ONE, (frozenset(),): b.ONE}
    for P in seed.levels[2]:
        r[P] = seed_amp(P, frozenset(range(2))) / seed_amp(P, frozenset())

    parents3 = seed.levels[3]
    sums, full_r = {}, {}
    for C in parents3:
        proper_sum = sum(
            (r[induced(C, P)] for P in b.downsets(C) if P != frozenset(range(3))),
            b.ZERO,
        )
        sums[C] = proper_sum
        full_r[C] = b.ONE - proper_sum
        r[C] = full_r[C]

    def amp(C, P):
        n = len(C)
        if n < 3:
            return seed_amp(C, P)
        if P == frozenset(range(3)):
            return full_r[C]
        return r[induced(C, P)]

    model = b.Model("fixed BCPH seed with nonzero stage-4 continuation", amp, 4)
    stage4_tree = model.levels

    all_transitions = [amp(C, P) for n in range(1, 4) for C in model.levels[n] for P in b.downsets(C)]
    assert all(not z.iszero() for z in all_transitions)
    assert not model.msr_ok()
    count, failures = bell_check(model, 3)
    assert not failures
    assert all(not model.norm_gc_ok(n) for n in (2, 3, 4))

    eq_count, reduced, pivots, inconsistent = stage4_norm_linear_system(seed, stage4_tree, r)
    assert not inconsistent
    assert pivots == [0, 1, 2, 3, 4, 5, 8, 9]
    # x_0=...=x_6; y_1=y_2=y_4; remaining y's free.
    expected_rows = []
    for i in range(6):
        row = [Fr(0)] * 14
        row[i], row[6] = Fr(1), Fr(-1)
        expected_rows.append(row)
    for i in (1, 2):
        row = [Fr(0)] * 14
        row[7 + i], row[11] = Fr(1), Fr(-1)  # y_i - y_4
        expected_rows.append(row)
    assert reduced[:8] == expected_rows

    cp = (frozenset(), frozenset({0}), frozenset())
    cp_key = b.canon(cp)
    cp3 = seed.classes(3)[cp_key]
    cp4 = [b.child(C, frozenset(range(3))) for C in cp3]
    cp4_key = b.canon(cp4[0])
    cp4_paths = model.classes(4)[cp4_key]
    cp4_amps = [model.psi[C] for C in cp4_paths]
    cp4_hol = [z / cp4_amps[0] for z in cp4_amps]
    assert len(cp4_paths) == 3
    assert len(set(z.abs2() for z in cp4_amps)) == 1
    assert any(z != b.ONE for z in cp4_hol)

    print("r_empty:", r[()])
    print("stage-2 r values:", [(b.canon(C), r[C]) for C in seed.levels[2]])
    print("stage-3 parent order and exact proper sums/full r_C:")
    for i, C in enumerate(parents3):
        print(i, b.canon(C), "S_C=", sums[C], "r_C=", full_r[C], "t(C,empty)=1")
    print("all transition amplitudes nonzero:", len(all_transitions), "checked")
    print("MSR failures:", model.msr_ok())
    print("stage-4 BC product equations:", count, "checked; failures:", len(failures))
    print("norm-GC failures stages 2-4:", [model.norm_gc_ok(n) for n in (2, 3, 4)])
    print("stage-4 norm-GC linear system: equations", eq_count, "rank", len(pivots), "free variables", 14-len(pivots))
    print("norm-GC constraints: x_0=...=x_6; y_1=y_2=y_4; other y_i free")
    print("cp-plus-top amplitudes:", cp4_amps)
    print("cp-plus-top holonomies:", cp4_hol)
    print("CERTIFICATE: PASS (exact Fraction/Gaussian-rational assertions)")


if __name__ == "__main__":
    main()
