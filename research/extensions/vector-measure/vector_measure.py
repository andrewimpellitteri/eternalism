#!/usr/bin/env python3
"""Norm-prescribed R^2-valued measure on the labelled causet tree.

This is not a vector lift of the complex scalar amplitudes: it prescribes the
NORM of each cylinder vector to be |A_p(C)| and lets the directions vary.  The
scalar complex measure does not exist for p outside [0,1]; at finite level this
construction shows the total-variation argument alone cannot block the finite
data.

[Corrected 2026-10-21, after research/adversarial-review/coordinator/
VECTOR_COUNTERMODEL.md and BOUNDARIES.md:]
- The finite tree is NOT "checked exactly" here: this script is a floating-point
  polygon construction (max errors ~1e-16). Exact finite checks live in
  check_indicator.py.
- A finite norm-matching assignment is not evidence toward an infinite
  extension: mu(C) = (Re A_p(C), Im A_p(C)) already gives an exact finitely
  additive norm-matching assignment on every finite tree. Finite existence is
  not the missing step.
- The infinite norm-prescribed extension is no longer wholly open: on the
  circle |p|^2+|1-p|^2 = 1 the standard L^2(P_r) indicator construction is a
  countably additive infinite-dimensional example (semivariation one, infinite
  total variation off the classical endpoints). What remains open is the
  classification away from that locus; an R^2-valued (finite-dimensional)
  countably additive extension outside [0,1] is impossible. See AGENT_REPORT.md.
"""
import sys
import math
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "experiments" / "baseline"))
import poscau  # noqa: E402

EPS = 1e-10


def add(a, b): return (a[0] + b[0], a[1] + b[1])
def sub(a, b): return (a[0] - b[0], a[1] - b[1])
def scale(a, s): return (a[0] * s, a[1] * s)
def norm(a): return math.hypot(a[0], a[1])


def polygon(V, lengths):
    """Vectors of the given lengths summing to V, in the input order."""
    idx = sorted(range(len(lengths)), key=lambda i: -lengths[i])
    L = norm(V)
    def rec(target, ids):
        if not ids:
            if norm(target) > 1e-8:
                raise ValueError("nonempty target with no vectors")
            return []
        if len(ids) == 1:
            i = ids[0]
            if abs(norm(target) - lengths[i]) > 1e-7:
                raise ValueError(f"single length mismatch {norm(target)} vs {lengths[i]}")
            return [target]
        i0 = ids[0]
        a0 = lengths[i0]
        rest = ids[1:]
        low_r = max(0.0, 2 * max(lengths[j] for j in rest) - sum(lengths[j] for j in rest))
        high_r = sum(lengths[j] for j in rest)
        tl = norm(target)
        lo = max(abs(tl - a0), low_r)
        hi = min(tl + a0, high_r)
        if lo > hi + 1e-8:
            raise ValueError(f"polygon infeasible: lo={lo} hi={hi}")
        t = 0.5 * (lo + hi)
        if tl < 1e-14:
            w = (a0, 0.0)
        else:
            u = scale(target, 1.0 / tl)
            perp = (-u[1], u[0])
            c = (tl * tl + a0 * a0 - t * t) / (2 * tl * a0)
            c = max(-1.0, min(1.0, c))
            ang = math.acos(c)
            w = (a0 * (math.cos(ang) * u[0] + math.sin(ang) * perp[0]),
                 a0 * (math.cos(ang) * u[1] + math.sin(ang) * perp[1]))
        rem = rec(sub(target, w), rest)
        out = [None] * len(ids)
        out[0] = w
        for k, j in enumerate(rest, start=1):
            out[k] = rem[k - 1]
        return out
    result_sorted = rec(V, idx)
    out = [None] * len(lengths)
    for pos, i in enumerate(idx):
        out[i] = result_sorted[pos]
    return out


def build(p, maxlevel):
    vec = {}
    stats = {"norm_err": 0.0, "sum_err": 0.0, "nodes": 0, "failed": 0}
    root = (frozenset(), 1)
    vec[root] = (1.0, 0.0)

    def visit(rel, n, V):
        stats["nodes"] += 1
        A = poscau.amplitude(rel, n, p)
        stats["norm_err"] = max(stats["norm_err"], abs(norm(V) - abs(A)))
        if n == maxlevel:
            return
        kids = poscau.children(rel, n)
        lengths = [abs(poscau.amplitude(child, n + 1, p)) for child, _, _ in kids]
        try:
            ws = polygon(V, lengths)
        except ValueError as exc:
            stats["failed"] += 1
            print(f"  polygon failure at n={n}: {exc}")
            # fallback: put all length on the first child, zero elsewhere
            ws = [(V if i == 0 else (0.0, 0.0)) for i in range(len(kids))]
        total = (0.0, 0.0)
        for (child, _, _), w in zip(kids, ws):
            total = add(total, w)
            vec[(child, n + 1)] = w
        stats["sum_err"] = max(stats["sum_err"], norm(sub(total, V)))
        for child, _, _ in kids:
            visit(child, n + 1, vec[(child, n + 1)])

    visit(*root, vec[root])
    return vec, stats


def level_stats(vec, maxlevel):
    for n in range(1, maxlevel + 1):
        vs = [v for (rel, m), v in vec.items() if m == n]
        total = (0.0, 0.0)
        for v in vs:
            total = add(total, v)
        print(f"level {n}: nodes={len(vs)} "
              f"sum_norm={sum(norm(v) for v in vs):.6g} "
              f"vector_sum=({total[0]:.3g},{total[1]:.3g})")


if __name__ == "__main__":
    p = 0.5 + 0.5j
    maxlevel = 5
    vec, stats = build(p, maxlevel)
    print(f"p={p}, levels 1..{maxlevel}")
    print(f"nodes={stats['nodes']} norm_err={stats['norm_err']:.3e} "
          f"sum_err={stats['sum_err']:.3e} failures={stats['failed']}")
    level_stats(vec, maxlevel)
