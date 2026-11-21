#!/usr/bin/env python3
"""Finite witnesses for the bridge-premises repair lane (ontology-bridges-repair).

Standard library only. Explicit finite witnesses. Bounded input sizes
(n <= 4 elements; at most 2^(4*4) = 65536 candidate families per reduct).
Runs in well under one second.

NOTHING HERE TREATS A MODEL DOMAIN AS CONCRETE. The elements of every reduct
below are labels in the metalanguage (comparison devices, following the
coordinator's EXPLANATORY_ROLE_TEST section 2 discipline). The program computes
only: which one-place existence predicates on the labels satisfy which premise
sets. A family E maps each marked standpoint b to a subset E(b) of the labels;
membership in E(b) encodes "label x would be concrete from standpoint b" under
that candidate expansion. Admissibility constraints are mathematical properties
of the reduct and the subsets, never ontological assertions.

Witnesses:
  W1  3-point chain: the shared structural constraints admit more than one
      existence family (nonentailment of uniqueness). Adding the universality
      selector leaves exactly one family; adding the down-closed,
      future-excluded selectors leaves exactly one family. Each selector is
      coextensive with its conclusion under the constraints.
  W2  2-point antichain, two marked standpoints: invariance (the finite
      surrogate of "no privileged observers") excludes the privileged
      -standpoint family, but still admits more than one family.
  W3  4-point diamond: down-closure + future-exclusion + invariance + the
      rest of the shared constraints, AND transitivity of the existence
      relation, still admit both the causal-past family and the bow-tie
      analogue (elsewhere included). Transitivity does no filtering here.
  W4  3-element poset {x < z} plus one isolated y: the same constraint set
      admits the causal-past family and a bow-tie analogue, and here the
      bow-tie analogue VIOLATES transitivity. Whether transitivity filters
      the bow-tie reading is category-relative even at 3-4 elements.
  W5  Discrete protocol surrogate for the clipped-Minkowski repair:
      matched records up to a cutoff do not determine lifetime (protocol P1);
      records after the cutoff do distinguish the two models (protocol P2).
"""

from itertools import permutations, product
import time

START = time.time()
T0 = time.perf_counter()


def idty(x):
    return x


class Reduct:
    """A representational reduct: labels, strict order, marked standpoints."""

    def __init__(self, name, elements, order, marks):
        # order: set of pairs (a, b) meaning a < b (strict).
        # Transitive closure is taken so that witnesses can be declared compactly.
        closure = set(order)
        changed = True
        while changed:
            changed = False
            for (a, b) in list(closure):
                for (c, d) in list(closure):
                    if b == c and (a, d) not in closure:
                        closure.add((a, d))
                        changed = True
        self.name = name
        self.elements = tuple(elements)
        self.order = frozenset(closure)
        self.marks = tuple(marks)
        self.autos = self._automorphisms()
        # Precomputed restriction data: initial segments U_k and ordered mark pairs.
        self.segs = {
            k: frozenset({k} | self.strict_past(k)) for k in self.elements
        }
        self.mark_order = [
            (a, c) for (a, c) in self.order if a in self.marks and c in self.marks
        ]

    def _automorphisms(self):
        res = []
        for p in permutations(self.elements):
            f = dict(zip(self.elements, p))
            ok = True
            for (a, b) in self.order:
                if (f[a], f[b]) not in self.order:
                    ok = False
                    break
            if ok:
                # order is reflexive-closed under <-> both directions check
                ok2 = True
                inv = {v: k for k, v in f.items()}
                for (a, b) in self.order:
                    if (inv[a], inv[b]) not in self.order:
                        ok2 = False
                        break
                if ok2:
                    res.append(f)
        return res

    def strict_future(self, x):
        return {b for (a, b) in self.order if a == x}

    def strict_past(self, x):
        return {a for (a, b) in self.order if b == x}

    def weak_past(self, x):
        return {x} | self.strict_past(x)


def all_families(r):
    """Every family: one subset of elements per marked standpoint."""
    for bits in product([0, 1], repeat=len(r.elements) * len(r.marks)):
        fam = {}
        i = 0
        for b in r.marks:
            s = frozenset(
                r.elements[j] for j in range(len(r.elements)) if bits[i + j]
            )
            fam[b] = s
            i += len(r.elements)
        yield fam


# ---------------- constraints (mathematical, not ontological) ----------------


def c_invariance(r):
    """A1: automorphism-invariance of the family (covariance surrogate)."""
    def pred(fam):
        for f in r.autos:
            for b in r.marks:
                img = frozenset(f[x] for x in fam[b])
                if img != fam[f[b]]:
                    return False
        return True
    return pred


def c_self_inclusion(r):
    """A2: b in E(b)."""
    def pred(fam):
        return all(b in fam[b] for b in r.marks)
    return pred


def c_monotone(r):
    """A3: b <= c implies E(b) subset of E(c)."""
    pairs = r.mark_order

    def pred(fam):
        return all(fam[a] <= fam[c] for (a, c) in pairs)
    return pred


def c_restriction(r):
    """A4: restriction compatibility on initial segments U_k = {x : x <= k}.

    For standpoints b in U_k the restricted family must satisfy A2 and A3
    inside U_k, and agree pointwise with the ambient family on U_k.
    """
    segs = r.segs
    pairs = r.mark_order

    def pred(fam):
        for k, U in segs.items():
            for b in r.marks:
                if b in U:
                    rb = fam[b] & U
                    if b not in rb:
                        return False
                    for (a, c) in pairs:
                        if c == b and a in U:
                            if not (fam[a] & U) <= rb:
                                return False
        return True
    return pred


def c_down_closed(r):
    """DOWN: past-inclusion; y <= x in E(b) implies y in E(b)."""
    def pred(fam):
        for b in r.marks:
            for x in fam[b]:
                if not r.weak_past(x) <= fam[b]:
                    return False
        return True
    return pred


def c_future_excluded(r):
    """FUTEX: no strictly-future element of b is in E(b)."""
    def pred(fam):
        for b in r.marks:
            if fam[b] & r.strict_future(b):
                return False
        return True
    return pred


def c_transitive(r):
    """TRANS: the relation R(b,x): x in E(b) is transitive."""
    def pred(fam):
        for b in r.marks:
            for y in fam[b]:
                if y in r.marks:
                    for z in fam[y]:
                        if z not in fam[b]:
                            return False
        return True
    return pred


def c_universal(r):
    """UNIV: E(b) = everything (for marked b)."""
    def pred(fam):
        return all(fam[b] == frozenset(r.elements) for b in r.marks)
    return pred


CONSTRAINTS = {
    "A1": c_invariance,
    "A2": c_self_inclusion,
    "A3": c_monotone,
    "A4": c_restriction,
    "DOWN": c_down_closed,
    "FUTEX": c_future_excluded,
    "TRANS": c_transitive,
    "UNIV": c_universal,
}


_CACHE = {}


def admissible(r, names):
    key = (r.name, tuple(names))
    if key in _CACHE:
        return _CACHE[key]
    preds = [CONSTRAINTS[n](r) for n in names]
    res = [fam for fam in all_families(r) if all(p(fam) for p in preds)]
    _CACHE[key] = res
    return res


def fam_str(r, fam):
    return "; ".join(
        "E(%s)={%s}" % (b, ",".join(sorted(fam[b]))) for b in r.marks
    )


def named(r, fam, kinds):
    tags = []
    for b in r.marks:
        if fam[b] == frozenset(r.elements):
            tags.append("all@%s" % b)
        elif fam[b] == r.weak_past(b):
            tags.append("past@%s" % b)
        elif fam[b] == frozenset([b]):
            tags.append("present@%s" % b)
        elif fam[b] == frozenset(r.elements) - r.strict_future(b):
            tags.append("bowtie@%s" % b)
    return tags


def report_w1():
    r = Reduct("chain3", [0, 1, 2], [(0, 1), (1, 2)], [0, 1, 2])
    shared = admissible(r, ["A1", "A2", "A3", "A4"])
    n = len(shared)
    assert n >= 3, "W1: expected several families, got %d" % n
    kinds = sorted({tuple(sorted(named(r, f, None))) for f in shared})
    univ = admissible(r, ["A1", "A2", "A3", "A4", "UNIV"])
    past = admissible(r, ["A1", "A2", "A3", "A4", "DOWN", "FUTEX"])
    assert len(univ) == 1 and univ[0][0] == frozenset(r.elements)
    assert len(past) == 1 and past[0][1] == frozenset({0, 1})
    both = any(f[0] == frozenset(r.elements) for f in shared) and any(
        f[1] == frozenset({0, 1}) for f in shared
    )
    assert both, "W1: shared class must contain both named candidates"
    print("W1 chain3: shared {A1..A4} families: %d" % n)
    print("   candidates present: %s" % (kinds,))
    print("   +UNIV -> %d family (E_all). +DOWN+FUTEX -> %d family (E_past)." % (len(univ), len(past)))
    return n


def report_w2():
    r = Reduct("antichain2", ["x", "y"], [], ["x", "y"])
    # privileged family: standpoint y sees x's event too; x sees only itself.
    priv = {"x": frozenset(["x"]), "y": frozenset(["x", "y"])}
    assert c_self_inclusion(r)(priv) and c_monotone(r)(priv)
    assert not c_invariance(r)(priv), "W2: invariance must exclude privilege"
    withA1 = admissible(r, ["A1", "A2"])
    assert len(withA1) >= 2, "W2: symmetric alternatives must remain"
    print("W2 antichain2: privileged family excluded by A1; %d invariant families remain" % len(withA1))
    for f in withA1:
        print("   " + fam_str(r, f))


def bow_family(r):
    """The exact bow-tie analogue: E(b) = everything except b's strict future."""
    return {
        b: frozenset(r.elements) - r.strict_future(b) for b in r.marks
    }


def past_family(r):
    """The exact causal-past family: E(b) = weak causal past of b."""
    return {b: r.weak_past(b) for b in r.marks}


def in_class(r, names, fam):
    return fam in admissible(r, names)


def report_w3():
    r = Reduct(
        "diamond4",
        ["0", "a", "b", "1"],
        [("0", "a"), ("0", "b"), ("a", "1"), ("b", "1")],
        ["0", "a", "b", "1"],
    )
    names = ["A1", "A2", "A3", "A4", "DOWN", "FUTEX", "TRANS"]
    cls = admissible(r, names)
    bf, pf = bow_family(r), past_family(r)
    assert in_class(r, names, pf), "W3: causal-past family must survive TRANS"
    assert in_class(r, names, bf), "W3: bow-tie analogue must survive TRANS here"
    print("W3 diamond4: {A1..A4,DOWN,FUTEX,TRANS} families: %d" % len(cls))
    for f in cls:
        print("   %s  %s" % (fam_str(r, f), named(r, f, None)))
    print("   -> transitivity does NOT separate past from bow-tie analogue here")


def report_w4():
    r = Reduct("chain+isolated", ["x", "z", "y"], [("x", "z")], ["x", "z", "y"])
    base = ["A1", "A2", "A3", "A4", "DOWN", "FUTEX"]
    cls = admissible(r, base)
    bf, pf = bow_family(r), past_family(r)
    assert in_class(r, base, pf), "W4: causal-past family must be admissible"
    assert in_class(r, base, bf), "W4: bow-tie analogue must be admissible before TRANS"
    assert not c_transitive(r)(bf), "W4: bow-tie analogue must violate TRANS here"
    tr = admissible(r, base + ["TRANS"])
    assert in_class(r, base + ["TRANS"], pf), "W4: TRANS must keep causal past"
    assert not in_class(r, base + ["TRANS"], bf), "W4: TRANS must exclude bow-tie here"
    assert len(tr) < len(cls)
    print("W4 chain+isolated: {A1..A4,DOWN,FUTEX}: %d families; with TRANS: %d" % (len(cls), len(tr)))
    for f in cls:
        print("   %s  %s" % (fam_str(r, f), named(r, f, None)))
    print("   -> transitivity filters the bow-tie analogue HERE (category-relative)")


def report_w5():
    """Discrete surrogate for the clipped-Minkowski protocol logic."""
    horizon = 4            # M1 = events 0..4 (clipped); M2 = events 0..6 (full)
    full = 6
    cutoff = 3             # records up to and including t=3 are matched
    rec1 = list(range(0, cutoff + 1))
    rec2 = list(range(0, cutoff + 1))
    assert rec1 == rec2, "P1: matched records"
    life1, life2 = horizon, full
    assert life1 != life2
    late1 = [t for t in range(cutoff + 1, life1 + 1)]
    late2 = [t for t in range(cutoff + 1, life2 + 1)]
    p1_distinguishes = rec1 != rec2
    p2_distinguishes = late1 != late2
    assert not p1_distinguishes and p2_distinguishes
    print("W5 protocol surrogate: M1 lifetime=%d, M2 lifetime=%d" % (life1, life2))
    print("   P1 records <= t=%d: identical (%s) -> matched past records do not fix lifetime" % (cutoff, rec1 == rec2))
    print("   P2 records at t in (%d, lifetime]: %s vs %s -> future records distinguish" % (cutoff, late1, late2))
    print("   -> 'completeness lacks retrodictive content under P1' is NOT 'no protocol distinguishes'")


def main():
    print("Finite witnesses, representational labels only; no concrete-domain assumption.\n")
    report_w1()
    print()
    report_w2()
    print()
    report_w3()
    print()
    report_w4()
    print()
    report_w5()
    dt = time.perf_counter() - T0
    print("\nAll checks passed in %.3f s (bound: 10 s per check / 30 s total)." % dt)
    assert dt < 10.0


if __name__ == "__main__":
    main()
