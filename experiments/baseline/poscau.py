#!/usr/bin/env python3
"""Complex transitive percolation on (doubly-)reduced poscau.

Standard library only. This is an independent implementation of the tree and
variation criterion in Dowker & Zalel, "Observables for cyclic causal set
cosmologies", arXiv:2212.01149v2, Secs. III.3-III.4 and V:

  A_p(C) = p^{L(C)} (1-p)^{binom(n,2) - R(C)}          (Eq. 26)
  zeta(D_n) = sum_i |A(D_n -> D^i_{n+1})| - 1          (Eq. 24)
  zeta_n^min = min over level n                         (Eq. 25)
  improved valency>1 criterion: zeta_bar_n^min, S_n,
  S_bar_n, S_n^{v=1}                                    (Eq. 30-31)

Causets are naturally labelled partial orders on {0,...,n-1}: relation i < j
implies i < j numerically. A causet is principal iff it has a unique maximal
element. It is doubly principal iff it and its restriction deleting the last
label are principal (Dowker-Zalel Sec. V).

The two trees:
  * reduced poscau: children of a node are one singleton node per principal
    child plus one merged node containing all non-principal children;
  * doubly-reduced poscau: the same, with "principal" replaced by "doubly
    principal".

Node amplitudes are sums of causet amplitudes over the causets in the node;
the transition amplitude between adjacent nodes is the ratio of node
amplitudes, so sum-over-children equals one by additivity of the pre-measure.
"""
from itertools import combinations
from functools import lru_cache

_MAX_LEVEL = 6
_CAUSETS = {}
_STATS = {}
_CHILDREN = {}


def causets(n):
    """All naturally labelled transitive orders on {0,...,n-1}."""
    if n in _CAUSETS:
        return _CAUSETS[n]
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    out = []
    for bits in range(1 << len(pairs)):
        rel = frozenset(pairs[k] for k in range(len(pairs)) if (bits >> k) & 1)
        ok = True
        for (i, j) in rel:
            for (k, l) in rel:
                if j == k and (i, l) not in rel:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(rel)
    out.sort(key=lambda r: (len(r), tuple(sorted(r))))
    _CAUSETS[n] = tuple(out)
    return _CAUSETS[n]


def maxima(rel, n):
    return tuple(i for i in range(n)
                 if not any((i, j) in rel for j in range(i + 1, n)))


def is_principal(rel, n):
    return len(maxima(rel, n)) == 1


def stats(rel, n):
    """(L, R): number of covers and number of strict relations."""
    key = (rel, n)
    if key in _STATS:
        return _STATS[key]
    L = sum(1 for (i, j) in rel
            if not any((i, k) in rel and (k, j) in rel for k in range(i + 1, j)))
    R = len(rel)
    _STATS[key] = (L, R)
    return L, R


def amplitude(rel, n, p):
    """A_p(C) = p^L (1-p)^{binom(n,2)-R}."""
    L, R = stats(rel, n)
    q = 1 - p
    return (p ** L) * (q ** (n * (n - 1) // 2 - R))


def down_sets(rel, n):
    """Down-closed subsets of the n-element causet."""
    out = []
    for mask in range(1 << n):
        S = frozenset(i for i in range(n) if (mask >> i) & 1)
        if all((j not in S) or (i in S) for (i, j) in rel):
            out.append(S)
    return out


def children(rel, n):
    """Children in labelled poscau: (child relation, added down-set, principal)."""
    key = (rel, n)
    if key in _CHILDREN:
        return _CHILDREN[key]
    out = []
    for S in down_sets(rel, n):
        child = rel | frozenset((i, n) for i in S)
        out.append((child, S, len(S) == n))
    _CHILDREN[key] = tuple(out)
    return _CHILDREN[key]


def node_children(node, n, p, doubly):
    """Return ([(child node, child amplitude)], parent amplitude).

    A node is a tuple of causets at level n. Its children are grouped by the
    (doubly-)reduced-poscau rule.
    """
    singletons = []
    merged = []
    for rel in node:
        for child, S, principal in children(rel, n):
            if doubly:
                singleton = principal and is_principal(rel, n)
            else:
                singleton = principal
            if singleton:
                singletons.append((child,))
            else:
                merged.append(child)
    kids = list(singletons)
    if merged:
        kids.append(tuple(merged))
    parent_amp = sum(amplitude(r, n, p) for r in node)
    out = [(kid, sum(amplitude(r, n + 1, p) for r in kid)) for kid in kids]
    return out, parent_amp


def zeta(node, n, p, doubly):
    """zeta for one node; None if the node amplitude vanishes."""
    kids, A = node_children(node, n, p, doubly)
    if abs(A) < 1e-12:
        return None, len(kids), 1
    return sum(abs(a) for _, a in kids) / abs(A) - 1, len(kids), A


def level_table(max_level, p, doubly):
    """Walk the tree and return per-level dicts of node diagnostics."""
    nodes = [(frozenset(),)]  # level 1: the one-element causet
    table = {}
    for n in range(1, max_level + 1):
        rows = []
        next_nodes = []
        for node in nodes:
            z, valency, A = zeta(node, n, p, doubly)
            next_nodes.extend(k for k, _ in node_children(node, n, p, doubly)[0])
            rows.append({"node": node, "zeta": z, "valency": valency, "amp": A})
        zs = [r["zeta"] for r in rows if r["zeta"] is not None]
        gt1 = [r["zeta"] for r in rows
               if r["zeta"] is not None and r["valency"] > 1]
        table[n] = {
            "nodes": rows,
            "count": len(rows),
            "zeta_min": min(zs) if zs else None,
            "zeta_bar_min": min(gt1) if gt1 else None,
            "S": sum(abs(r["amp"]) for r in rows),
            "S_bar": sum(abs(r["amp"]) for r in rows if r["valency"] > 1),
            "S_v1": sum(abs(r["amp"]) for r in rows if r["valency"] == 1),
        }
        nodes = next_nodes
    return table
