#!/usr/bin/env python3
"""Certificate for the labelled-causet example (equivalence lane).

Checks, by exhaustive enumeration on a 3-element poset:

  P : a < b, with c incomparable to both (the tenseless "unlabelled causet").

1. The automorphism group of (P, <) is trivial (rigid base).
2. There are exactly three order-respecting labellings (linear extensions)
   l : P -> {1,2,3}; these are three expansions of the SAME base.
3. No two expansions are isomorphic as expansions (no base automorphism
   conjugates one labelling to another).
4. The growth-order claim "stage(c) < stage(b)" is TRUE on some expansions and
   FALSE on others, while every base-sentence has a fixed truth value on the
   shared base; hence that claim is not the interpretation of any base sentence
   (the expansion is not definable; non-uniqueness is witnessed explicitly).

Standard library only. No network access.
"""

import itertools

# Elements: 0 = a, 1 = b, 2 = c. Strict order pairs of P:
PAIRS = {(0, 1)}  # a < b


def preserves_order(p):
    """p: tuple, permutation p[i] = image of i. True iff p is an order
    automorphism of the strict order PAIRS."""
    for (x, y) in itertools.product(range(3), repeat=2):
        in_p = (x, y) in PAIRS
        in_img = (p[x], p[y]) in PAIRS
        if in_p != in_img:
            return False
    return True


def is_linear_extension(lab):
    """lab: tuple lab[i] = stage of i (a permutation of {1,2,3}).
    True iff lab respects the order."""
    for (x, y) in PAIRS:
        if lab[x] >= lab[y]:
            return False
    return True


def conjugate(lab, p):
    return tuple(lab[p[i]] for i in range(3))


def main():
    perms = list(itertools.permutations(range(3)))
    autos = [p for p in perms if preserves_order(p)]
    exts = [l for l in itertools.permutations(range(3)) if is_linear_extension(l)]

    print("poset P: a<b; c incomparable")
    print("automorphism group size:", len(autos))
    print("automorphisms:", autos)

    # labellings as dicts for readable printing
    names = {0: "a", 1: "b", 2: "c"}
    print("linear extensions (expansions):")
    for l in exts:
        print("   ", {names[i]: l[i] for i in range(3)})

    # pairwise non-isomorphic as expansions
    noniso = True
    for l1, l2 in itertools.combinations(exts, 2):
        same = any(conjugate(l1, p) == l2 for p in autos)
        if same:
            noniso = False
            print("isomorphic expansions found:", l1, l2)
    print("pairwise non-isomorphic expansions:", noniso)

    # truth variation of the growth claim stage(c) < stage(b)
    verdicts = {tuple(l): (l[2] < l[1]) for l in exts}
    print('truth of "c added before b" per expansion:', verdicts)
    print("claim varies across expansions:", len(set(verdicts.values())) > 1)

    # the shared base is ONE model: any fixed base sentence has a fixed
    # extension/truth value on it, so no base sentence can realize a claim
    # whose truth value varies across the expansions. Displayed by 2 != 1
    # distinct expansions over the identical reduct.
    ok = (len(autos) == 1) and (len(exts) == 3) and noniso and (len(set(verdicts.values())) > 1)
    print("ALL CHECKS PASS:", ok)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
