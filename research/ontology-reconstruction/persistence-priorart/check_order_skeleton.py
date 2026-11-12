#!/usr/bin/env python3
"""Order-theoretic skeleton checks for the persistence-census prior-art audit.

Purpose (task ontology-persistence-priorart, 30 October 2026): test the
"immediate corollary of standard order theory" threat against the two
conditional censuses. The script encodes ONLY the outputs of the analytic
reduction (Lorentz-orbit all-or-nothing facts and the E-space saturation
chains) as input axioms, then verifies by exact enumeration that:

  1. the n>=2 four-case census (I, J, B, C) and every row of the
     added-premise table in PERSISTENCE_CONVENTIONS.md section 4, and
  2. the 1+1 no-parity sixteen-case census and every refinement count in
     ONE_PLUS_ONE_CENSUS.md section 4

are elementary combinatorics on those chains.

The geometric reduction itself (orbit transitivity for n>=2, boost-orbit
all-or-nothing, saturation witnesses) is NOT re-proved here; it was verified
analytically by the persistence review (RESULT.md O6-O19). This script is a
combinatorial certificate, not an enumeration proof of any continuous-domain
census.

Input chains, E-space (E_0 region P, past set; family P_t):
  n>=2 orbits beyond the mandatory {I-, 0}: N- (past null), N+ (future null), S (spacelike)
    S  => N-   (spacelike saturation, E-space mirror; witness in PERSISTENCE_CONVENTIONS section 3)
    N+ => S    (past closure: (0, s e) with s/2 < s is in the chronological past of (s, s e))
    N+ => N-   (causal chain, used only for the causal-persistence row)
    F_t forbids I+; S + P_t force I- U {0}.
  1+1 per side (right/left): triple (n_plus, w, n_minus) with chain n_plus <= w <= n_minus.
Transitivity judgments (printed witnesses; not re-derived here):
  I, J additive/transitive; B, C fail on the printed triple b=(0,0), x=(0,2), y=(2,-1).
Runtime: exact integer enumeration, well under 1 s.
"""

# ---------- n >= 2 skeleton ----------

# optional orbits and saturation chains (E-space)
N2_CHAINS = {"N-": set(), "N+": {"S"}, "S": {"N-"}}  # X -> orbits X forces


def n2_valid_subsets(chains, forbidden=(), seed=()):
    """Subsets of optional orbits closed under chains, avoiding forbidden ones.

    `seed` lists orbits forced before enumeration (e.g. causal closure of the
    diagonal under S forces the past null orbit for the P_c row).
    """
    names = list(chains)
    out = []
    for mask in range(1 << len(names)):
        sub = {names[i] for i in range(len(names)) if mask >> i & 1} | set(seed)
        closure = set(sub)
        changed = True
        while changed:
            changed = False
            for x in list(closure):
                for y in chains.get(x, ()):
                    if y not in closure:
                        closure.add(y)
                        changed = True
        if closure == sub and not (sub & set(forbidden)):
            out.append(frozenset(sub))
    return sorted(out, key=sorted)


N2_LABELS = {
    frozenset(): "I = I- U {b}",
    frozenset({"N-"}): "J = J-(b)",
    frozenset({"N-", "S"}): "B = M \\ (J+(b) \\ {b})",
    frozenset({"N-", "N+", "S"}): "C = M \\ I+(b)",
}


def check_n2():
    got = n2_valid_subsets(N2_CHAINS, forbidden=("I+",))
    labels = [N2_LABELS[s] for s in got]
    assert len(got) == 4, got
    assert set(labels) == {
        "I = I- U {b}", "J = J-(b)",
        "B = M \\ (J+(b) \\ {b})", "C = M \\ I+(b)",
    }, labels

    # P_c chains (causal closure adds causal-past orbits); causal closure of
    # the diagonal (S) forces the past null orbit
    pc_chains = {"N-": set(), "N+": {"S", "N-"}, "S": {"N-"}}
    pc = {N2_LABELS[s] for s in n2_valid_subsets(pc_chains, seed=("N-",))}
    assert pc == {"J = J-(b)", "B = M \\ (J+(b) \\ {b})", "C = M \\ I+(b)"}, pc

    # F_c forbids the future null orbit N+ (and I+, already excluded)
    fc = {N2_LABELS[s] for s in n2_valid_subsets(N2_CHAINS, forbidden=("I+", "N+"))}
    assert fc == {"I = I- U {b}", "J = J-(b)", "B = M \\ (J+(b) \\ {b})"}, fc

    # F_c requires P includes b only from J+(b); combined with P_c (seed kept):
    pcf = {N2_LABELS[s] for s in n2_valid_subsets(pc_chains, forbidden=("N+",), seed=("N-",))}
    assert pcf == {"J = J-(b)", "B = M \\ (J+(b) \\ {b})"}, pcf

    # causal boundedness E_b subset J-(b): optional orbits subset of {N-}
    bounded = [N2_LABELS[s] for s in got if s <= {"N-"}]
    assert set(bounded) == {"I = I- U {b}", "J = J-(b)"}
    bounded_pc = [x for x in bounded if x in pc]
    assert bounded_pc == ["J = J-(b)"]

    # transitivity judgments: printed witnesses (I,J additive; B,C fail on
    # b=(0,0), x=(0,2), y=(2,-1)) - audit input, not re-derived
    transitive = {"I = I- U {b}", "J = J-(b)"}
    closed = {"J = J-(b)", "C = M \\ I+(b)"}  # cl(I)=J, cl(B)=C (standard cone facts)
    rows = {
        "none": set(labels),
        "P_c": pc,
        "F_c": fc,
        "P_c and F_c": pcf,
        "closed": closed & set(labels),
        "closed and F_c": closed & fc,
        "transitive": transitive,
        "transitive and closed": transitive & closed,
        "causally bounded": set(bounded),
        "bounded and P_c": set(bounded_pc),
    }
    expected = {
        "none": 4, "P_c": 3, "F_c": 3, "P_c and F_c": 2, "closed": 2,
        "closed and F_c": 1, "transitive": 2, "transitive and closed": 1,
        "causally bounded": 2, "bounded and P_c": 1,
    }
    for row, want in expected.items():
        assert len(rows[row]) == want, (row, rows[row])
    return rows


# ---------- 1+1 no-parity skeleton ----------

def side_triples():
    """Monotone triples (n_plus, w, n_minus) per side: chain n+ <= w <= n-."""
    return [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1) if a <= b <= c]


def check_1plus1():
    triples = side_triples()
    assert len(triples) == 4, triples
    patterns = [(r, l) for r in triples for l in triples]
    assert len(patterns) == 16, patterns
    assert len(set(patterns)) == 16

    def contains_both_wedges(p):
        return p[0][1] == 1 and p[1][1] == 1

    # reflection invariance: mirror swaps the two side triples
    refl = [p for p in patterns if p[0] == p[1]]
    assert len(refl) == 4
    mirror_classes = len({tuple(sorted(p)) for p in patterns})
    assert mirror_classes == 10, mirror_classes

    # refinement counts (ONE_PLUS_ONE_CENSUS.md section 4 and transitivity table)
    pc = [p for p in patterns if p[0][2] == 1 and p[1][2] == 1]
    fc = [p for p in patterns if p[0][0] == 0 and p[1][0] == 0]
    closed = [p for p in patterns
              if (p[0] in {(0, 0, 1), (1, 1, 1)}) and (p[1] in {(0, 0, 1), (1, 1, 1)})]
    trans = [p for p in patterns if not contains_both_wedges(p)]
    counts = {
        "base": len(patterns),
        "reflection": len(refl),
        "P_c": len(pc),
        "F_c": len(fc),
        "P_c and F_c": len([p for p in patterns if p in pc and p in fc]),
        "closed": len(closed),
        "closed and F_c": len([p for p in patterns if p in closed and p in fc]),
        "transitive": len(trans),
        "transitive and closed": len([p for p in patterns if p in closed and p in trans]),
        "transitive and P_c": len([p for p in patterns if p in pc and p in trans]),
        "transitive and F_c": len([p for p in patterns if p in fc and p in trans]),
        "transitive, P_c and F_c": len([p for p in patterns if p in pc and p in fc and p in trans]),
        "mirror classes": mirror_classes,
    }
    expected = {
        "base": 16, "reflection": 4, "P_c": 9, "F_c": 9, "P_c and F_c": 4,
        "closed": 4, "closed and F_c": 1, "transitive": 12,
        "transitive and closed": 3, "transitive and P_c": 5,
        "transitive and F_c": 8, "transitive, P_c and F_c": 3,
        "mirror classes": 10,
    }
    for row, want in expected.items():
        assert counts[row] == want, (row, counts[row], want)

    # named survivors
    I, J, B, C = (0, 0, 0), (0, 0, 1), (0, 1, 1), (1, 1, 1)
    assert (I, I) in patterns and (J, J) in patterns and (B, B) in patterns and (C, C) in patterns
    fifth = (I, B)  # review's fifth family, E-space form (000|011)
    mirror_fifth = (B, I)
    assert fifth in patterns and mirror_fifth in patterns
    # transitive (only the left wedge present), NOT causally persistent
    # (right side lacks its past-null branch)
    assert not contains_both_wedges(fifth)
    assert fifth in trans and fifth not in pc
    return counts


def main():
    n2_rows = check_n2()
    c11 = check_1plus1()
    print("PASS n>=2 skeleton: 4 candidates {I,J,B,C}; all 10 added-premise rows reproduce:")
    for k in ("none", "P_c", "F_c", "P_c and F_c", "closed", "closed and F_c",
              "transitive", "transitive and closed", "causally bounded", "bounded and P_c"):
        print("   %-22s -> %d" % (k, len(n2_rows[k])))
    print("PASS 1+1 skeleton: 16 patterns; all refinement counts reproduce:")
    for k, v in c11.items():
        print("   %-24s -> %d" % (k, v))


if __name__ == "__main__":
    main()
