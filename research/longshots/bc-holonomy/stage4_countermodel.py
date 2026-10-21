#!/usr/bin/env python3
"""Exact finite audit of a scalar Bell-causal, norm-GC holonomy model.

The birth-order implementation is imported read-only from the longshot seed.
All amplitudes and tests use Gaussian rationals (fractions.Fraction).
"""
from fractions import Fraction as Fr
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/longshots/birth-order-interference/birth_order_interference.py"
spec = importlib.util.spec_from_file_location("birth_order_interference", SOURCE)
boi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(boi)


def induced(past, subset):
    """Relabel an induced subcauset in increasing old-label order."""
    old = sorted(subset)
    new = {i: j for j, i in enumerate(old)}
    return tuple(frozenset(new[j] for j in past[i] if j in subset) for i in old)


def bell_equations(model, through_parent_size):
    """Check exact scalar BC cross-products for every precursor pair.

    For parent C and downsets P,Q, let B=P union Q with its induced order.
    The equation is t(C,P)t(B,Q)=t(C,Q)t(B,P). This is spectator deletion
    from the union of precursors. Products are used even when any factor is 0.
    """
    count = 0
    failures = []
    for n in range(1, through_parent_size + 1):
        for C in model.levels[n]:
            ds = boi.downsets(C)
            for i, P in enumerate(ds):
                for Q in ds[i + 1 :]:
                    B = induced(C, P | Q)
                    idx = {old: new for new, old in enumerate(sorted(P | Q))}
                    Pbar = frozenset(idx[j] for j in P)
                    Qbar = frozenset(idx[j] for j in Q)
                    lhs = model.amp(C, P) * model.amp(B, Qbar)
                    rhs = model.amp(C, Q) * model.amp(B, Pbar)
                    count += 1
                    if lhs != rhs:
                        failures.append((n, C, P, Q, B, lhs, rhs))
    return count, failures


def main():
    # The previously audited Bell-causal norm-GC stage-3 family.
    x = Fr(1, 2)
    y = 1 - x
    alpha1 = boi.G(Fr(1, 4))
    u = boi.G(Fr(3, 5), Fr(4, 5))
    beta0 = alpha1 * u
    alpha = (alpha1, alpha1 * x / y, boi.ONE - alpha1 / y)
    beta = (
        beta0,
        beta0 * x / y,
        beta0 * x / y,
        boi.ONE - beta0 * (1 + x) / y,
    )
    stage3 = boi.stage3_table_amp(x, alpha, beta)

    # At every parent of size >=3, only the full-past child is allowed.
    # This deterministic continuation has amplitudes 1 (timid/full past) and
    # 0 (all other precursors), and is defined at every later stage.
    model = boi.Model("BCPH with full-past continuation", boi.frozen_amp(stage3, 3), 5)

    print("labelled causets:", {n: len(model.levels[n]) for n in range(1, 6)})
    print("MSR failures:", model.msr_ok())
    for n in range(2, 6):
        print(f"norm-GC failures at stage {n}:", model.norm_gc_ok(n))

    for n in range(1, 5):
        count, failures = bell_equations(model, n)
        print(f"BC pair equations, parents through size {n}: {count} checked; failures={len(failures)}")
        if failures:
            print("first BC failure:", failures[0])

    cp = (frozenset(), frozenset({0}), frozenset())
    cp_class = model.classes(3)[boi.canon(cp)]
    cp_amps = [model.psi[c] for c in cp_class]
    cp_holonomies = [z / cp_amps[0] for z in cp_amps]
    cp_sum = sum(cp_amps, boi.ZERO)
    print("stage-3 cp labelled amplitudes:", cp_amps)
    print("stage-3 cp holonomies relative to first:", cp_holonomies)
    print("stage-3 cp amplitude norms-squared:", [z.abs2() for z in cp_amps])
    print("stage-3 cp class sum:", cp_sum)

    # The same nontrivial holonomy survives on the four-element class obtained
    # by adjoining a universal top to cp.
    cp4_paths = []
    for c in cp_class:
        cp4_paths.append(boi.child(c, frozenset(range(3))))
    cp4_key = boi.canon(cp4_paths[0])
    cp4_class = model.classes(4)[cp4_key]
    cp4_amps = [model.psi[c] for c in cp4_class]
    cp4_holonomies = [z / cp4_amps[0] for z in cp4_amps]
    print("stage-4 cp-plus-universal-top class multiplicity:", len(cp4_class))
    print("stage-4 cp-plus-universal-top labelled amplitudes:", cp4_amps)
    print("stage-4 holonomies relative to first:", cp4_holonomies)

    # Hard assertions make this a reproducible certificate, not a sample.
    assert not model.msr_ok()
    assert all(not model.norm_gc_ok(n) for n in range(2, 6))
    assert all(not bell_equations(model, n)[1] for n in range(1, 5))
    # The canonical enumeration chooses an antichain-parent labeling first,
    # so the reported relative phase is u^{-1}; its nontriviality is invariant.
    assert cp_holonomies == [boi.ONE, boi.ONE, u.conj()]
    assert cp4_holonomies == [boi.ONE, boi.ONE, u.conj()]
    assert cp_amps == [boi.G(Fr(3, 40), Fr(1, 10)), boi.G(Fr(3, 40), Fr(1, 10)), boi.G(Fr(1, 8))]
    print("CERTIFICATE: PASS (all assertions exact)")


if __name__ == "__main__":
    main()
