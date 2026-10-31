#!/usr/bin/env python3
"""Finite-domain illustration of the modal-category witness bookkeeping.

This is NOT a proof of any general claim. It checks, on small explicit
finite rational time-line models, the case analysis stated in RESULT.md:

  1. Which model categories contain witness pairs for (IND_ex)-style
     failure of the complete worldstate at a later t' with the database
     up to an earlier t held fixed.
  2. Whether the nomological box (DET_ex) holds for all t < t' in each
     single category, and that it fails for some pair in EVERY open cut
     admitted as a complete world (anti-trivialization witness).

Model types (time sets inside [0,1]):
  complete: [0,1] closed            - has a terminal event at 1
  open_cut: [0,c)                   - NO last moment
  terminal: [0,c] closed at c < 1   - complete world with last moment c,
                                      standing for a law class with an
                                      explicit terminal boundary rule
One entity per time point; db(t) is the frozen complete description of
everything existing at or before t plus a totality clause. Times that
do not exist make `At t', db(t')` fail (free-logic reading).

Run: python3 check_modal_witnesses.py  (stdlib only, < 1 s)
"""

from fractions import Fraction as F

N = 20


def line(kind, cut=None):
    pts = [F(i, N) for i in range(N + 1)]
    if kind == "complete":
        return pts
    if kind == "open_cut":
        return [p for p in pts if p < cut]
    if kind == "terminal":
        return [p for p in pts if p <= cut]
    raise ValueError(kind)


def entities(times):
    return {("e_%s" % str(p).replace("/", "_")): p for p in times}


def db_holds(times, actual_desc, t):
    """Does the actual world's description hold at t in this model?

    Checks (i) t exists; (ii) every actual entity located at/before t
    exists here at/before t; (iii) totality: no extra entity exists at
    or before t.
    """
    tset = set(times)
    if t not in tset:
        return False
    model_ents = entities(times)
    for name, loc in actual_desc.items():
        if loc > t:
            continue
        if name not in model_ents or model_ents[name] > t:
            return False
    for name, loc in model_ents.items():
        if loc <= t and (name not in actual_desc or actual_desc[name] > t):
            return False
    return True


def main():
    actual = line("complete")
    desc = entities(actual)
    pairs = [(F(i, N), F(i + 5, N)) for i in range(1, 16)]  # t < t', gap 1/4

    # Cat0 = ALL initial segments, so one cut sits inside every pair
    cat0 = [("complete [0,1]", actual)] + [
        ("open_cut [0,%s)" % c, line("open_cut", cut=c))
        for c in (F(i, N) for i in range(2, N))
    ]
    cat1 = [("complete [0,1]", actual),
            ("terminal [0,1/2]", line("terminal", cut=F(1, 2)))]
    cat2 = [("complete [0,1]", actual)]

    print("== Per-category survey: witness pairs (t<t') with db(t) fixed")
    print("   and At t', db(t') failing ==")
    for label, cats in [("Cat0 all smooth GHDs (incl. open cuts)", cat0),
                        ("Cat1 maximal (complete, or terminal-rule class)", cat1),
                        ("Cat2 selected two-sided complete class", cat2)]:
        print(label)
        for name, times in cats[:1] + cats[1:6:4]:
            wit = [(t, tp) for (t, tp) in pairs
                   if t in set(times) and not db_holds(times, desc, tp)]
            tag = ("BOX HOLDS for all %d pairs" % len(pairs)) if not wit else \
                  ("box FAILS on %d/%d pairs; e.g. t=%s, t'=%s"
                   % (len(wit), len(pairs), wit[0][0], wit[0][1]))
            last = "last time: %s" % times[-1]
            print("   %-18s (%s) -> %s" % (name, last, tag))

    print()
    print("== Anti-trivialization witness under Cat0 admissibility ==")
    full = 0
    for t, tp in pairs:
        hit = any(t in set(times) and not db_holds(times, desc, tp)
                  for _, times in cat0)
        full += hit
    print("(IND_ex)-style witness exists for %d/%d pairs across Cat0" % (full, len(pairs)))

    box1 = all(db_holds(times, desc, tp) for _, times in cat1
               for t, tp in pairs if t in set(times))
    box2 = all(db_holds(times, desc, tp) for _, times in cat2
               for t, tp in pairs)
    print("(DET_ex) holds for all pairs in Cat1: %s" % box1)
    print("(DET_ex) holds for all pairs in Cat2: %s" % box2)

    cut = line("open_cut", cut=F(7, 10))
    print("Open cut [0,7/10) last time: %s (open cuts have no last moment:"
          " the endpoint 7/10 is excluded -> %s)"
          % (cut[-1], F(7, 10) not in set(cut)))

    print()
    print("Illustration only: finite rational time lines, one entity per time.")
    print("Not a proof; see RESULT.md for the exact scope of each claim.")


if __name__ == "__main__":
    main()
