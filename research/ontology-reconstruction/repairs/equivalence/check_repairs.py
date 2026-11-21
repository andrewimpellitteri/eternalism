#!/usr/bin/env python3
"""Strengthened finite checks for the equivalence-repair lane.

Standard library only. Exact rational arithmetic (fractions.Fraction).
No network access. Runs in well under 10 seconds.

Two kinds of content, kept clearly separate:

  EXACT CHECKS (complete finite proofs, not samples)
    Part A: the repaired three-element poset example
      A1  Aut(P) is trivial (rigid base).
      A2  Exactly three order-respecting labellings (growth orders).
      A3  Each element is parameter-free definable in the base language
          (displayed formulas evaluated exhaustively).
      A4  Each of the three chosen growth-order relations is parameter-free
          definable in the base language (displayed pair formulas, evaluated
          on all 9 ordered pairs)  ->  PER-EXPANSION definability.
      A5  The three growth relations are pairwise distinct, and the
          semantic census of all 2^9 binary relations on P contains exactly
          three strict linear extensions of the base order, namely those
          three  ->  no single relation, hence no single base formula,
          coincides with the growth order of all three expansions
          (UNIFORM RECOVERY fails).  Exact for the fixed base: a formula
          has one extension on it.
      A6  The test sentence "c became real before b" varies across the
          three expansions while the shared reduct is one fixed structure.

  WITNESS CHECKS (explicit finite witnesses with exact arithmetic; the
  corresponding theorems are proved analytically in RESULT.md; this script
  illustrates, it does not prove them)
    Part B: 1+1 Minkowski witnesses
      B1  The chronological-language definition of the causal past,
          J^-(0) = {x : for all y (0 << y -> x << y)}, evaluated on an
          explicit witness list, agrees exactly with the analytic causal
          past on six sampled point kinds (interior / null right / null
          left / spacelike / future / deep interior).
      B2  Sampled origin-stabilizer elements (rational boost, dilation,
          spatial reflection) preserve the chronological relation on an
          explicit list of ordered pairs; the boost is exactly isometric
          on witnesses.
      B3  The sampled nonzero past null cone is one orbit under the sampled
          stabilizer: reflection exchanges the two rays, boost and dilation
          adjust radius (explicit images asserted).
      B4  Both candidate expansions (interior, closed cone) are invariant
          under the sampled reflection on a reflection-closed witness set,
          and candidate membership is preserved by sampled dilation and
          boost images.
    Part C: 0+1 witness
      C1  On a line there is no nonzero null vector: causal past equals
          chronological past plus the point itself, so the two candidates
          coincide (the binary needs at least one spatial dimension).
"""

from fractions import Fraction
import itertools
import time

T0 = time.monotonic()


def fr(t, x):
    """Spacetime point (t, x); components may be int or (num, den)."""

    def f(v):
        return Fraction(v[0], v[1]) if isinstance(v, tuple) else Fraction(v)

    return (f(t), f(x))


# ---------------------------------------------------------------- Part A
# Base poset P = ({a, b, c}, <) with a < b and c incomparable.
# Element encoding: 0 = a, 1 = b, 2 = c.
PAIRS = {(0, 1)}
NAMES = {0: "a", 1: "b", 2: "c"}
ELTS = (0, 1, 2)

print("=== Part A: three-element poset (exact checks) ===")
print("base P: elements a, b, c; strict order pairs: {(a,b)}; c isolated")

# A1 rigidity
perms = list(itertools.permutations(ELTS))
autos = [p for p in perms
         if all(((x, y) in PAIRS) == ((p[x], p[y]) in PAIRS)
                for x in ELTS for y in ELTS)]
assert autos == [(0, 1, 2)], "Aut(P) should be trivial"
print("A1 PASS: Aut(P) is trivial (rigid base)")

# Parameter-free base-language definability of each element:
#   phi_a(x) := exists y. x < y                    (unique strict successor)
#   phi_b(x) := exists y. y < x                    (unique strict predecessor)
#   phi_c(x) := not phi_a(x) and not phi_b(x)      (the isolated element)
def phi_a(x):
    return any((x, y) in PAIRS for y in ELTS)


def phi_b(x):
    return any((y, x) in PAIRS for y in ELTS)


def phi_c(x):
    return (not phi_a(x)) and (not phi_b(x))


# A3 pointwise definability
assert [x for x in ELTS if phi_a(x)] == [0], "phi_a must select a"
assert [x for x in ELTS if phi_b(x)] == [1], "phi_b must select b"
assert [x for x in ELTS if phi_c(x)] == [2], "phi_c must select c"
print("A3 PASS: parameter-free base formulas select each element:")
print("        phi_a = 'x has a strict successor'   -> {a}")
print("        phi_b = 'x has a strict predecessor' -> {b}")
print("        phi_c = 'x is isolated'              -> {c}")

# A2 the three labellings (growth orders)
labellings = [l for l in itertools.permutations((0, 1, 2))
              if all(l[x] < l[y] for (x, y) in PAIRS)]
assert labellings == [(0, 1, 2), (0, 2, 1), (1, 2, 0)], "unexpected extensions"
print("A2 PASS: exactly three order-respecting labellings:")
for i, l in enumerate(labellings, 1):
    print("        expansion %d: stage map %s"
          % (i, {NAMES[e]: l[e] for e in ELTS}))

# Growth-order relation added by expansion i:  R_i(x,y) :<=> l_i(x) < l_i(y)
R = [{(x, y) for x in ELTS for y in ELTS if l[x] < l[y]} for l in labellings]

# A4 per-expansion definability.  For expansion i and stage k let
# rho_{i,k}(x) := 'x is the element whose stage is k', spelled out through
# phi_a / phi_b / phi_c.  Then the growth order of expansion i is the
# displayed pair formula
#     delta_i(x,y) := OR_{k < k'} ( rho_{i,k}(x) AND rho_{i,k'}(y) ),
# a parameter-free formula of the base language {<}.
stage_pred = {}
for i in range(3):
    for k in range(3):
        e = next(t for t in ELTS if labellings[i][t] == k)
        f = {0: phi_a, 1: phi_b, 2: phi_c}[e]
        stage_pred[(i, k)] = f


def delta(i, x, y):
    return any(stage_pred[(i, k)](x) and stage_pred[(i, k2)](y)
               for k in range(3) for k2 in range(3) if k < k2)


for i in range(3):
    ext = {(x, y) for x in ELTS for y in ELTS if delta(i, x, y)}
    assert ext == R[i], "per-expansion definability formula %d failed" % (i + 1)
    who = {k: NAMES[next(t for t in ELTS if labellings[i][t] == k)]
           for k in range(3)}
    print("A4 PASS: expansion %d growth order = OR over stage pairs of "
          "'stage(x)=k and stage(y)=k>', stages %s"
          % (i + 1, {k: who[k] for k in range(3)}))
print("A4 PASS: each of the three chosen growth orders is parameter-free "
      "definable in the base language {<}  (per-expansion definability)")

# A5 distinctness + semantic census
assert R[0] != R[1] and R[0] != R[2] and R[1] != R[2], "growth relations collide"
print("A5 PASS: the three growth-order relations are pairwise distinct:")
for i, Ri in enumerate(R, 1):
    print("        R%d = {%s}" % (i, ", ".join(
        "(%s,%s)" % (NAMES[p], NAMES[q]) for p, q in sorted(Ri))))

census_ext = set()
for mask in range(2 ** 9):
    rel = {(x, y) for x in ELTS for y in ELTS if mask & (1 << (3 * x + y))}
    irrefl = all((x, x) not in rel for x in ELTS)
    total = all(((x, y) in rel) or ((y, x) in rel)
                for x in ELTS for y in ELTS if x != y)
    antisym = not any((x, y) in rel and (y, x) in rel
                      for x in ELTS for y in ELTS if x != y)
    trans = all(((x, y) in rel and (y, z) in rel) <= ((x, z) in rel)
                for x in ELTS for y in ELTS for z in ELTS)
    extends = all(p in rel for p in PAIRS)
    if irrefl and total and antisym and trans and extends:
        census_ext.add(frozenset(rel))
assert len(census_ext) == 3, "semantic census must find exactly 3"
assert census_ext == {frozenset(R[0]), frozenset(R[1]), frozenset(R[2])}
print("A5 PASS: semantic census of all 512 binary relations on P: exactly "
      "3 are strict linear extensions of <, namely R1, R2, R3")
print("        so no single relation - hence no single base formula, whose "
      "extension on the fixed structure is one relation - coincides with")
print("        the growth order of all three expansions: UNIFORM RECOVERY "
      "fails (exact, finite)")

# A6 test sentence variation
truths = [l[2] < l[1] for l in labellings]  # stage(c) < stage(b)
assert truths == [False, True, True]
print("A6 PASS: 'c became real before b' is "
      + ", ".join("%s on expansion %d" % ("TRUE" if t else "FALSE", i + 1)
                  for i, t in enumerate(truths)))
print("        the shared reduct is one fixed structure: every base sentence "
      "has a fixed truth value on it, so no base sentence co-varies with")
print("        this claim across the three expansions.  Scope: ADDED, "
      "not-uniformly-recoverable content - not 'inexpressible language'.")

# ---------------------------------------------------------------- Part B
print()
print("=== Part B: 1+1 Minkowski witnesses (exact Fractions) ===")
# Point = (t, x);  Q(p) = t^2 - x^2.  p << q : d = q - p with d_t > 0 and
# Q(d) < 0 (chronological, timelike future).  p <= q (causal): d_t >= 0 and
# Q(d) <= 0.


def Q(p):
    return p[0] * p[0] - p[1] * p[1]


def chrono(p, q):
    d = (q[0] - p[0], q[1] - p[1])
    return d[0] > 0 and Q(d) > 0


def causal(p, q):
    d = (q[0] - p[0], q[1] - p[1])
    return d[0] >= 0 and Q(d) >= 0


origin = fr(0, 0)

# B1 definability formula against the analytic causal past, on witnesses.
W_test = [fr(1, 0), fr((1, 4), 0), fr((1, 8), (1, 16))]  # y with 0 << y
for y in W_test:
    assert chrono(origin, y), "test witnesses must lie chronological future"

candidates = [
    (fr(-1, 0), "interior past (timelike)"),
    (fr(-1, 1), "nonzero null, right ray"),
    (fr(-1, -1), "nonzero null, left ray"),
    (fr(0, 1), "spacelike"),
    (fr(1, 0), "future timelike"),
    (fr(-2, 0), "deeper interior past"),
]
for x, label in candidates:
    formula = all(chrono(x, y) for y in W_test)  # forall y (0<<y -> x<<y)
    jpast = causal(x, origin)
    assert formula == jpast, "witness mismatch for %s" % label
    print("B1 PASS: %-28s in causal past of 0? %-5s formula %s"
          % (label, jpast, formula))
print("B1 PASS: the chronological-language definition separates exactly the "
      "causal past on all six sampled point kinds")

# B2 sampled stabilizer elements preserve <<; boost exactly isometric.
def boost(p, s=Fraction(2)):
    """Orthochronous boost: null coords u=t+x, w=t-x; u->s*u, w->w/s."""
    u, w = p[0] + p[1], p[0] - p[1]
    return ((s * u + w / s) / 2, (s * u - w / s) / 2)


def dil(p, lam=Fraction(1, 2)):
    return (lam * p[0], lam * p[1])


def refl(p):
    return (p[0], -p[1])


sample = [
    fr(0, 0), fr(1, 0), fr(-1, 0), fr(-1, 1), fr(-1, -1), fr(2, 0),
    fr(0, 2), fr(-2, 2), fr(-2, -2), fr((-1, 2), (1, 2)),
]
for name, s in (("boost s=2", boost), ("dilation 1/2", dil),
                ("reflection", refl)):
    for p in sample:
        for q in sample:
            assert chrono(p, q) == chrono(s(p), s(q)), \
                "%s fails to preserve << on a sampled pair" % name
    print("B2 PASS: %s preserves the chronological relation on all %d "
          "sampled ordered pairs" % (name, len(sample) ** 2))

bp = boost(fr(-1, 0))
assert bp == fr((-5, 4), (-3, 4)) and Q(bp) == Q(fr(-1, 0))
print("B2 PASS: boost is exactly isometric on witnesses: "
      "(-1,0) -> (-5/4,-3/4), Q = 1 on both")

# B3 orbit witnesses for the nonzero past null cone.
N_pts = [fr(-1, 1), fr((-1, 2), (1, 2)), fr((-1, 4), (1, 4)),
         fr(-2, 2), fr(-1, -1), fr(-2, -2)]
for p in N_pts:
    assert Q(p) == 0 and p[0] < 0, "orbit samples must be nonzero past-null"
    for name, s in (("boost s=2", boost), ("dilation 1/2", dil),
                    ("reflection", refl)):
        q = s(p)
        assert Q(q) == 0 and q[0] < 0, \
            "%s must keep the sampled null cone null and past" % name
assert boost(N_pts[0]) == N_pts[1] and boost(N_pts[1]) == N_pts[2]
assert refl(N_pts[0]) == N_pts[4] and dil(N_pts[3]) == N_pts[0]
print("B3 PASS: reflection swaps rays; boost s=2 walks (-1,1) -> (-1/2,1/2) "
      "-> (-1/4,1/4); dilation 1/2 sends (-2,2) -> (-1,1)")
print("        (full-orbit transitivity is proved analytically in RESULT.md; "
      "these are exact witnesses, not the proof)")

# B4 candidate expansions invariant on a reflection-closed witness set.
S_inv = [
    fr(0, 0), fr(-1, 0), fr(-2, 0), fr(1, 0),
    fr(-1, 1), fr(-1, -1), fr(-2, 2), fr(-2, -2),
    fr((-1, 2), (1, 2)), fr((-1, 2), (-1, 2)), fr(0, 1), fr(0, -1),
]
assert {refl(p) for p in S_inv} == set(S_inv), "witness set not reflection-closed"
E_int = {p for p in S_inv if chrono(p, origin)} | {origin}
E_cl = {p for p in S_inv if causal(p, origin)}
assert E_int <= E_cl and origin in E_int and len(E_int) < len(E_cl)
assert {refl(p) for p in E_int} == E_int and {refl(p) for p in E_cl} == E_cl
print("B4 PASS: interior and closed-cone candidates are reflection-invariant "
      "on the closed witness set (%d interior, %d causal points sampled)"
      % (len(E_int), len(E_cl)))
for name, s in (("dilation 1/2", dil), ("boost s=2", boost)):
    moved = [(p, s(p)) for p in E_cl if s(p) in set(S_inv)]
    assert all((q in E_cl) == (p in E_cl) for p, q in moved), name
    print("B4 PASS: %s preserves candidate membership on %d sampled images "
          "(witness level)" % (name, len(moved)))

# ---------------------------------------------------------------- Part C
print()
print("=== Part C: 0+1 witness ===")
line = [Fraction(-2), Fraction(-1), Fraction(-1, 2),
        Fraction(0), Fraction(1, 2), Fraction(1), Fraction(2)]
assert not any(t != 0 and Q((t, Fraction(0))) == 0 for t in line), \
    "no nonzero null vector on a line"
for x in line:
    d = -x
    assert (d >= 0) == (d > 0 or x == 0), "causal == chronological on a line"
print("C1 PASS: on 0+1 no nonzero null vector exists (sampled line); causal "
      "past = chronological past + {0}")
print("        the interior and closed-cone candidates coincide there: the "
      "binary needs >= 1 spatial dimension")

dt = time.monotonic() - T0
print()
print("ALL CHECKS PASS. wall time: %.3f s" % dt)
assert dt < 10.0, "checks must complete within 10 seconds"
