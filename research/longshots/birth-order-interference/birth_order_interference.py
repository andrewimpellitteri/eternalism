#!/usr/bin/env python3
"""Long shot: interference trace of birth order under norm-only covariance.

Exact computation, Python standard library only (fractions). No floats are
used in any check; floats appear only in optional human-readable comments.

Framework (Srivastava-Surya arXiv:2603.25503v1, Sec. 3 and 3.1, with
H = C, i.e. the commutative/scalar case of [30, 31] there):
  * labelled poscau: naturally labelled causets grown one element at a time;
    child of c_n = c_n plus element n whose past is a down-set P of c_n;
  * vector measure: |c_n> = A_{n-1} ... A_1 |Omega>, here a complex number
    psi(c_n) = product of transition amplitudes along the unique path (Eq. 31);
  * Markov sum rule (Eqs. 32-33): sum of transition amplitudes out of each
    labelled node equals 1;
  * decoherence functional D(a,b) = A*(a) A(b) (Sec. 3.1, product form),
    quantum measure mu(a) = D(a,a) = |A(a)|^2 (Eq. 25);
  * GC (Sec. 3.1): psi(c) = psi(c') for isomorphic c ~ c';
    norm-only GC (Note in Sec. 3.1; Sec. 4): |psi(c)| = |psi(c')|, phases free.

Event types used below (see REPORT.md, Sec. 2):
  * stage-n class event [C]_n: union of all labelled stage-n cylinders whose
    causet is isomorphic to C.  NOT covariant in the sense of Surya-Zalel /
    Srivastava-Surya Sec. 2.4 (it refers to "the first n elements").
  * stage-n stem event stem_n(S): C_n has a down-set isomorphic to S
    (increasing in n; its union over n is the covariant stem event).
  * frozen models: from stage N on, every new element is born above every
    existing element (transitive percolation with p = 1).  Then the infinite
    causet is C_N (+) omega-chain, and {C ~ C_N (+) omega} is a genuinely
    covariant event (a single isomorphism class of infinite causets) whose
    vector measure is exactly the stage-N class vector.  The vector measure
    is a finite atomic complex measure, so it trivially extends.
"""
from fractions import Fraction as Fr
from itertools import permutations, combinations, product
import sys


# ---------------------------------------------------------------- Gaussian rationals
class G:
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = Fr(re)
        self.im = Fr(im)

    @staticmethod
    def c(x):
        return x if isinstance(x, G) else G(x, 0)

    def __add__(s, o):
        o = G.c(o); return G(s.re + o.re, s.im + o.im)
    __radd__ = __add__

    def __sub__(s, o):
        o = G.c(o); return G(s.re - o.re, s.im - o.im)

    def __rsub__(s, o):
        return G.c(o) - s

    def __neg__(s):
        return G(-s.re, -s.im)

    def __mul__(s, o):
        o = G.c(o); return G(s.re * o.re - s.im * o.im, s.re * o.im + s.im * o.re)
    __rmul__ = __mul__

    def conj(s):
        return G(s.re, -s.im)

    def abs2(s):
        return s.re * s.re + s.im * s.im

    def __truediv__(s, o):
        o = G.c(o); d = o.abs2()
        if d == 0:
            raise ZeroDivisionError("G division by zero")
        n = s * o.conj(); return G(n.re / d, n.im / d)

    def __rtruediv__(s, o):
        return G.c(o) / s

    def __pow__(s, k):
        r = G(1)
        for _ in range(k):
            r = r * s
        return r

    def __eq__(s, o):
        o = G.c(o); return s.re == o.re and s.im == o.im

    def __hash__(s):
        return hash((s.re, s.im))

    def iszero(s):
        return s.re == 0 and s.im == 0

    def __repr__(s):
        if s.im == 0:
            return str(s.re)
        if s.re == 0:
            return f"{s.im}i"
        sg = "+" if s.im > 0 else "-"
        return f"({s.re}{sg}{abs(s.im)}i)"


I = G(0, 1)
ONE = G(1)
ZERO = G(0)


def reflect(z, s):
    """Reflection of z across the real line through 0 and s: (s/conj s) conj z.
    Real-linear, fixes s, preserves |z|."""
    return (s / s.conj()) * z.conj()


# ---------------------------------------------------------------- causets
# labelled causet: tuple of frozensets; past[i] = full past of element i (all j<i, j<i in order)

def downsets(past):
    n = len(past)
    out = []
    for r in range(n + 1):
        for P in combinations(range(n), r):
            Ps = frozenset(P)
            if all(past[i] <= Ps for i in Ps):
                out.append(Ps)
    return out


def child(past, P):
    return past + (frozenset(P),)


def relations(past):
    return [(j, i) for i in range(len(past)) for j in past[i]]


def canon(past):
    n = len(past)
    rel = relations(past)
    best = None
    for pm in permutations(range(n)):
        k = tuple(sorted((pm[j], pm[i]) for j, i in rel))
        if best is None or k < best:
            best = k
    return (n, best)


def show(past):
    rel = relations(past)
    # report only covering relations for readability
    cov = [(j, i) for (j, i) in rel if not any((j in past[k]) and (k in past[i]) for k in range(len(past)))]
    return "{" + ",".join(f"{j}<{i}" for j, i in cov) + "}" if cov else "{}"


def has_stem(past, S_key):
    """Does the labelled causet have a down-set isomorphic to S (S_key = canon)?"""
    k = S_key[0]
    for D in combinations(range(len(past)), k):
        Ds = frozenset(D)
        if all(past[i] <= Ds for i in Ds):
            idx = {x: t for t, x in enumerate(sorted(D))}
            sub = tuple(frozenset(idx[j] for j in past[i]) for i in sorted(D))
            if canon(sub) == S_key:
                return True
    return False


ROOT = (frozenset(),)


def build_tree(N):
    """levels[n] = list of labelled causets with n elements (n = 1..N)."""
    levels = {1: [ROOT]}
    for n in range(1, N):
        levels[n + 1] = [child(c, P) for c in levels[n] for P in downsets(c)]
    return levels


# names for small classes
NAMES = {}


def name_classes(levels):
    def reg(past, nm):
        NAMES[canon(past)] = nm
    reg(ROOT, "1")
    reg((frozenset(), frozenset({0})), "chain2")
    reg((frozenset(), frozenset()), "anti2")
    reg((frozenset(), frozenset({0}), frozenset({0, 1})), "chain3")
    reg((frozenset(), frozenset({0}), frozenset({0})), "V")         # one below two
    reg((frozenset(), frozenset(), frozenset({0, 1})), "Lambda")     # two below one
    reg((frozenset(), frozenset({0}), frozenset()), "cp")            # 2-chain + isolated point
    reg((frozenset(), frozenset(), frozenset()), "anti3")
    k = 0
    for c in levels.get(4, []):
        key = canon(c)
        if key not in NAMES:
            k += 1
            NAMES[key] = f"C4.{k:02d}" + show(c)


def nm(key):
    return NAMES.get(key, str(key))


# ---------------------------------------------------------------- models
class Model:
    """amp(past, P) -> G : transition amplitude from labelled `past` to child with precursor P.
    frozen_at: if not None, the model is declared frozen from that stage on (p = 1 percolation)."""

    def __init__(self, name, amp, N, frozen_at=None, note=""):
        self.name, self.amp, self.N, self.frozen_at, self.note = name, amp, N, frozen_at, note
        self.levels = build_tree(N)
        self.psi = {ROOT: ONE}
        for n in range(1, N):
            for c in self.levels[n]:
                for P in downsets(c):
                    self.psi[child(c, P)] = self.psi[c] * self.amp(c, P)

    def msr_ok(self):
        bad = []
        for n in range(1, self.N):
            for c in self.levels[n]:
                s = ZERO
                for P in downsets(c):
                    s = s + self.amp(c, P)
                if not s == ONE:
                    bad.append((show(c), s))
        return bad

    def classes(self, n):
        cl = {}
        for c in self.levels[n]:
            cl.setdefault(canon(c), []).append(c)
        return cl

    def norm_gc_ok(self, n):
        bad = []
        for key, cs in self.classes(n).items():
            vals = {self.psi[c].abs2() for c in cs}
            if len(vals) > 1:
                bad.append((nm(key), [self.psi[c].abs2() for c in cs]))
        return bad

    def gc_ok(self, n):
        return all(len({self.psi[c] for c in cs}) == 1 for cs in self.classes(n).values())

    def class_vector(self, n):
        return {key: sum((self.psi[c] for c in cs), ZERO) for key, cs in self.classes(n).items()}


def cp_amp(p):
    q = ONE - p

    def amp(past, P):
        n = len(past)
        maxP = [i for i in P if not any(i in past[j] for j in P)]
        return (p ** len(maxP)) * (q ** (n - len(P)))
    return amp


def frozen_amp(base, N):
    """Use `base` below stage N; from stage N on, amplitude 1 for the full-past child, else 0."""
    def amp(past, P):
        n = len(past)
        if n < N:
            return base(past, P)
        return ONE if len(P) == n else ZERO
    return amp


def twisted(base, rule):
    """rule(past, P, base) -> G or None (None = keep base amplitude)."""
    def amp(past, P):
        r = rule(past, P, base)
        return base(past, P) if r is None else r
    return amp


A2 = (frozenset(), frozenset())               # labelled 2-antichain
C2 = (frozenset(), frozenset({0}))            # labelled 2-chain


def twist_A_rule(past, P, base):
    """Transition-covariant reflection twist at the 2-antichain node: reflect the
    orbit {P={0},{1}} (total amplitude 2pq) and the Lambda child (P={0,1}) across
    the direction of their sum.  Same twist for both members of the orbit."""
    if past != A2 or len(P) == 0:
        return None
    a = base(A2, frozenset({0}))
    b = base(A2, frozenset({0, 1}))
    s = 2 * a + b
    return reflect(a, s) if len(P) == 1 else reflect(b, s)


def twist_B_rule(past, P, base):
    """Label-dependent (orbit-breaking) twist at the 2-antichain node: reflect only the
    pair (P={0}, P={}) across their sum; P={1} untouched."""
    if past != A2 or P not in (frozenset(), frozenset({0})):
        return None
    a = base(A2, frozenset())
    b = base(A2, frozenset({0}))
    s = a + b
    return reflect(a, s) if len(P) == 0 else reflect(b, s)


CP_KEY = None  # filled after names


def twist_A4_rule(past, P, base):
    """Stage-4 transition-covariant twist at every labelled 'cp' node (2-chain + point):
    reflect the child with P = {} and the child with P = {isolated point} across their sum.
    Aut(cp) is trivial, so these two transition types are well defined label-free."""
    r = twist_A_rule(past, P, base)
    if r is not None:
        return r
    if len(past) != 3 or canon(past) != CP_KEY:
        return None
    iso = [i for i in range(3) if not past[i] and not any(i in past[j] for j in range(3))]
    assert len(iso) == 1
    pt = frozenset({iso[0]})
    if P not in (frozenset(), pt):
        return None
    a = base(past, frozenset())
    b = base(past, pt)
    s = a + b
    return reflect(a, s) if len(P) == 0 else reflect(b, s)


def stage3_table_amp(x, al, be):
    """General stage-3 model given by explicit amplitudes.
    x: amplitude 1 -> chain2 ; 1-x: 1 -> anti2.
    al = (a_cp, a_V, a_chain3): chain2 -> P={}, {0}, {0,1}.
    be = (b_anti3, b_0, b_1, b_Lambda): anti2 -> P={}, {0}, {1}, {0,1}."""
    x = G.c(x)

    def amp(past, P):
        n = len(past)
        if n == 1:
            return x if P else ONE - x
        if n == 2:
            if past == C2:
                return {0: al[0], 1: al[1], 2: al[2]}[len(P)]
            if len(P) == 0:
                return be[0]
            if P == frozenset({0}):
                return be[1]
            if P == frozenset({1}):
                return be[2]
            return be[3]
        raise ValueError
    return amp


# ---------------------------------------------------------------- analysis helpers
OUT = []


def say(*a):
    s = " ".join(str(x) for x in a)
    OUT.append(s)
    print(s)


def class_report(M, n):
    say(f"  stage {n} classes: name | W | labelled psi | |psi|^2 | v(C)=sum psi | mu(C)=|v|^2 | GC value W^2|psi|^2 | coherence |kappa|^2")
    for key, cs in sorted(M.classes(n).items(), key=lambda kv: nm(kv[0])):
        W = len(cs)
        ps = [M.psi[c] for c in cs]
        v = sum(ps, ZERO)
        a2 = ps[0].abs2()
        gcv = W * W * a2
        kap = (v.abs2() / gcv) if gcv != 0 else None
        say(f"   {nm(key):>18} | {W} | {ps} | {a2} | {v} | {v.abs2()} | {gcv} | {kap}")
        if W > 1 and not ps[0].iszero():
            say(f"   {'':>18}   holonomies psi_j/psi_1 = {[pj / ps[0] for pj in ps]}"
                f"  (labellings: {[show(c) for c in cs]})")


def stem_report(M, n, stems):
    for S in stems:
        Sk = canon(S)
        v = sum((M.psi[c] for c in M.levels[n] if has_stem(c, Sk)), ZERO)
        say(f"   stem_{n}({nm(Sk)}): v = {v} , mu = {v.abs2()}")
    return


def psd_rank1_check(vec):
    """D_ij = conj(v_i) v_j.  Gram matrix => PSD.  Verify exactly: Hermitian, diag >= 0,
    every 2x2 minor zero (rank <= 1), and v^dag D v = |sum conj(v_i)... |^2 identity on a test vector."""
    keys = list(vec)
    D = {(a, b): vec[a].conj() * vec[b] for a in keys for b in keys}
    herm = all(D[(a, b)] == D[(b, a)].conj() for a in keys for b in keys)
    diag = all(D[(a, a)].im == 0 and D[(a, a)].re >= 0 for a in keys)
    minors = all((D[(a, a)] * D[(b, b)] - D[(a, b)] * D[(b, a)]).iszero() for a in keys for b in keys)
    # test vector w with Gaussian-rational entries: w^dag D w = |sum_i v_i w_i|^2 >= 0
    w = {k: G(t + 1, (-1) ** t * t) for t, k in enumerate(keys)}
    quad = sum((w[a].conj() * D[(a, b)] * w[b] for a in keys for b in keys), ZERO)
    direct = sum((vec[a] * w[a] for a in keys), ZERO).abs2()
    return herm, diag, minors, quad, direct, quad == direct


def gc_reconstruction(M, N):
    """For a model frozen at N, the covariant vector measure is v(C) on stage-N classes.
    Any GC sequential-growth model frozen at N (or at any N' >= N) reproducing it must have
    psi_rec(c) = v([c]) / W([c]) at stage N, and (MSR) ancestors' psi = sums of descendants.
    Markov propagation |c_{n+1}> = A|c_n> forbids psi(ancestor) = 0 with a nonzero descendant.
    Returns (obstructions, reconstructed psi)."""
    v = M.class_vector(N)
    cls = M.classes(N)
    rec = {}
    for key, cs in cls.items():
        for c in cs:
            rec[c] = v[key] / len(cs)
    for n in range(N - 1, 0, -1):
        for c in M.levels[n]:
            rec[c] = sum((rec[child(c, P)] for P in downsets(c)), ZERO)
    obstr = []
    for n in range(1, N):
        for c in M.levels[n]:
            if rec[c].iszero():
                kids = [child(c, P) for P in downsets(c)]
                nz = [k for k in kids if not rec[k].iszero()]
                if nz:
                    obstr.append((show(c), [(show(k), rec[k]) for k in nz]))
    return obstr, rec, v


def verify_reconstruction(M, N, rec):
    """Build the GC model from rec (transition amp = rec(child)/rec(parent)), check MSR, GC,
    and that its frozen covariant vector equals M's."""
    def amp(past, P):
        n = len(past)
        if n >= N:
            return ONE if len(P) == n else ZERO
        return rec[child(past, P)] / rec[past]
    R = Model(M.name + " [GC reconstruction]", amp, N)
    ok_msr = R.msr_ok() == []
    ok_gc = all(R.gc_ok(n) for n in range(2, N + 1))
    same = R.class_vector(N) == M.class_vector(N)
    return R, ok_msr, ok_gc, same


def bc_stage3_check(M):
    """Rideout-Sorkin Bell causality at stage 2 -> 3, product form, scalar amplitudes:
    chain2: t(P={}) * x = t(P={0}) * (1-x);  anti2: t(P={}) * x = t(P={0}) * (1-x) = t(P={1})*(1-x)... (see REPORT)."""
    a = M.amp
    x = a(ROOT, frozenset({0}))
    y = a(ROOT, frozenset())
    c1 = (a(C2, frozenset()) * x - a(C2, frozenset({0})) * y).iszero()
    c2 = (a(A2, frozenset()) * x - a(A2, frozenset({0})) * y).iszero()
    c3 = (a(A2, frozenset()) * x - a(A2, frozenset({1})) * y).iszero()
    return c1 and c2 and c3, (c1, c2, c3)


def stage3_identity(M):
    """GC+BC frozen-at-3 identity: v(cp)^2 = 9 v(V) v(anti3)."""
    v = M.class_vector(3)
    k = {nm(kk): vv for kk, vv in v.items()}
    lhs = k["cp"] * k["cp"]
    rhs = 9 * k["V"] * k["anti3"]
    return lhs, rhs, lhs == rhs, (lhs.abs2(), rhs.abs2())


# ---------------------------------------------------------------- main
def main():
    global CP_KEY
    lv = build_tree(4)
    name_classes(lv)
    CP_KEY = [k for k, v in NAMES.items() if v == "cp"][0]
    say("=" * 100)
    say("Enumeration of the labelled poscau (natural labellings, growth by down-sets)")
    for n in range(1, 5):
        cls = {}
        for c in lv[n]:
            cls.setdefault(canon(c), []).append(c)
        say(f" stage {n}: {len(lv[n])} labelled causets, {len(cls)} unlabelled classes")
        for key, cs in sorted(cls.items(), key=lambda kv: nm(kv[0])):
            if n <= 3 or len(cs) > 1:
                say(f"    {nm(key):>18}: W={len(cs)}  labellings {[show(c) for c in cs]}")
    multi4 = sum(1 for cs in {canon(c): 0 for c in lv[4]})
    say(f" stage-4 classes with W=1 omitted above; total classes {multi4}")

    stems = [C2, A2,
             (frozenset(), frozenset({0}), frozenset({0, 1})),
             (frozenset(), frozenset({0}), frozenset({0})),
             (frozenset(), frozenset(), frozenset({0, 1})),
             (frozenset(), frozenset({0}), frozenset()),
             (frozenset(), frozenset(), frozenset())]

    p = G(Fr(1, 2), Fr(1, 2))   # complex percolation parameter p = (1+i)/2, q = (1-i)/2
    base = cp_amp(p)
    models = []
    models.append(Model("GC0: complex percolation p=(1+i)/2", base, 4,
                        note="GC by construction (label-independent p^L q^(C(n,2)-R))"))
    models.append(Model("PA: CP + transition-covariant reflection twist at anti2", twisted(base, twist_A_rule), 4,
                        note="norm-only GC; same moduli as GC0"))
    models.append(Model("PA4: PA + stage-4 twist at every cp node", twisted(base, twist_A4_rule), 4,
                        note="norm-only GC; same moduli as GC0"))
    models.append(Model("PB: CP + label-dependent twist (P={0} vs P={}) at anti2", twisted(base, twist_B_rule), 4,
                        note="norm-only GC; breaks transition covariance and Bell causality"))

    for M in models:
        say("=" * 100)
        say(f"MODEL {M.name}   ({M.note})")
        bad = M.msr_ok()
        say(f"  Markov sum rule at every labelled node, stages 1-3: {'OK' if not bad else bad}")
        for n in range(2, 5):
            nb = M.norm_gc_ok(n)
            say(f"  stage {n}: norm-only GC {'OK' if not nb else nb};  full GC (psi class function): {M.gc_ok(n)}")
        if M is not models[0]:
            same_mod = all(M.psi[c].abs2() == models[0].psi[c].abs2() for n in range(1, 5) for c in lv[n])
            say(f"  |psi(c)|^2 equal to GC0 for every labelled c, stages 1-4: {same_mod}"
                f"  => every labelled cylinder's quantum measure (Srivastava-Surya's <c_n|c_n>) is unchanged,"
                f" and so is the stage-n total variation sum |psi|")
        for n in (2, 3):
            class_report(M, n)
        say("  stage-4 classes with W>1 (others have a single labelling, hence no labelling phase):")
        for key, cs in sorted(M.classes(4).items(), key=lambda kv: nm(kv[0])):
            if len(cs) > 1:
                ps = [M.psi[c] for c in cs]
                v = sum(ps, ZERO)
                W = len(cs)
                say(f"   {nm(key):>28} W={W} v={v} mu={v.abs2()} GCvalue={W * W * ps[0].abs2()}"
                    f" holonomies={[pj / ps[0] for pj in ps]}")
        say("  stem events (finite-stage approximants of covariant stem events):")
        for n in (2, 3, 4):
            stem_report(M, n, [s for s in stems if len(s) <= n])
        lhs, rhs, eq, mods = stage3_identity(M)
        say(f"  stage-3 identity v(cp)^2 = 9 v(V) v(anti3): lhs={lhs} rhs={rhs} holds={eq}")
        ok, parts = bc_stage3_check(M)
        say(f"  Bell causality (product form) at stage 2->3: {ok} {parts}")

    # ---- Frozen models: genuinely covariant events
    say("=" * 100)
    say("FROZEN MODELS: from stage N on each new element is born above all existing elements.")
    say("Covariant atoms are the classes {C ~ C_N (+) omega}; covariant vector measure v = stage-N class vector.")
    frozen = []
    frozen.append(("GC0 frozen at 3", frozen_amp(base, 3), 3))
    frozen.append(("PA frozen at 3", frozen_amp(twisted(base, twist_A_rule), 3), 3))
    frozen.append(("PB frozen at 3", frozen_amp(twisted(base, twist_B_rule), 3), 3))
    frozen.append(("PA4 frozen at 4", frozen_amp(twisted(base, twist_A4_rule), 4), 4))
    # BC-respecting stage-3 phased family (see REPORT Sec. 5): x, alpha1, beta0 with |alpha1|=|beta0|
    x = Fr(1, 2); y = 1 - x
    a1 = G(Fr(1, 4)); u = G(Fr(3, 5), Fr(4, 5)); b0 = a1 * u
    al = (a1, a1 * x / y, ONE - a1 / y)
    be = (b0, b0 * x / y, b0 * x / y, ONE - b0 * (1 + x) / y)
    frozen.append(("BCPH: Bell-causal phased stage-3 model, x=1/2, a1=1/4, b0=(3+4i)/20, frozen at 3",
                   frozen_amp(stage3_table_amp(x, al, be), 3), 3))
    al0 = (a1, a1 * x / y, ONE - a1 / y)
    be0 = (a1, a1 * x / y, a1 * x / y, ONE - a1 * (1 + x) / y)
    frozen.append(("BCGC: same with b0=a1 (GC+BC), frozen at 3",
                   frozen_amp(stage3_table_amp(x, al0, be0), 3), 3))
    # obstruction example (real signed amplitudes, holonomy pi)
    x = Fr(2, 5); y = 1 - x
    alO = (G(Fr(3, 4)), G(Fr(1, 2)), G(Fr(-1, 4)))
    beO = (G(Fr(-3, 4)), G(Fr(-1, 2)), G(Fr(-1, 2)), G(Fr(11, 4)))
    frozen.append(("OBS: Bell-causal phased model with holonomy pi, x=2/5, frozen at 3",
                   frozen_amp(stage3_table_amp(x, alO, beO), 3), 3))
    # complex point on the obstruction locus: theta_a = 0, theta_b = theta_c = theta with e^{i theta} = (3+4i)/5
    r = Fr(3, 10); e = G(Fr(3, 5), Fr(4, 5))
    xc = (2 * r - 2 * r * e) / 3          # makes v(cp)/3 + v(V) + v(chain3) = 0
    yc = ONE - xc
    alC = (G(r) / xc, G(Fr(1, 8)), ONE - G(r) / xc - G(Fr(1, 8)))
    bC = (r * e) / yc
    beC = (G(Fr(1, 2)), bC, bC, ONE - G(Fr(1, 2)) - 2 * bC)
    frozen.append(("OBSC: complex point on the obstruction locus (not Bell-causal), frozen at 3",
                   frozen_amp(stage3_table_amp(xc, alC, beC), 3), 3))

    for nmF, amp, N in frozen:
        M = Model(nmF, amp, N + 1)  # build one stage past N to confirm freezing is consistent
        say("-" * 100)
        say(f"MODEL {nmF}")
        bad = M.msr_ok()
        say(f"  MSR at all nodes up to stage {N}: {'OK' if not bad else bad}")
        for n in range(2, N + 2):
            nb = M.norm_gc_ok(n)
            say(f"  stage {n}: norm-only GC {'OK' if not nb else nb}; full GC {M.gc_ok(n)}")
        vN = M.class_vector(N)
        vN1 = M.class_vector(N + 1)
        # freezing check: stage N+1 class vectors are the stage-N ones on C_N (+) point
        nz1 = {nm(k): vv for k, vv in vN1.items() if not vv.iszero()}
        say(f"  covariant vector measure v on atoms C_N(+)omega: "
            f"{ {nm(k): vv for k, vv in sorted(vN.items(), key=lambda kv: nm(kv[0]))} }")
        say(f"  sum of v = {sum(vN.values(), ZERO)} (normalisation D(Omega,Omega)=1 requires 1)")
        say(f"  stage {N + 1} nonzero class vectors (should equal the above, one per atom): {sorted(nz1.values(), key=repr) == sorted([vv for vv in vN.values() if not vv.iszero()], key=repr)}")
        herm, diag, minors, quad, direct, same = psd_rank1_check(vN)
        say(f"  decoherence functional on covariant atoms D=conj(v_i)v_j: Hermitian {herm}, diag>=0 {diag},"
            f" all 2x2 minors 0 {minors}, test quadratic form {quad} = |sum v_i w_i|^2 {direct}: {same}")
        if N == 3:
            ks = {nm(k): vv for k, vv in vN.items()}
            say(f"  mu(cp-atom) = {ks['cp'].abs2()} ; mu(V-atom) = {ks['V'].abs2()} ; "
                f"mu(cp or V) = {(ks['cp'] + ks['V']).abs2()} ; D(cp,V) = {ks['cp'].conj() * ks['V']}")
            lhs, rhs, eq, mods = stage3_identity(M)
            say(f"  identity v(cp)^2 = 9 v(V) v(anti3): lhs={lhs} rhs={rhs} holds={eq};"
                f" measure form mu(cp)^2 = 81 mu(V) mu(anti3): {mods[0]} vs {81 * vN[[k for k in vN if nm(k)=='V'][0]].abs2() * vN[[k for k in vN if nm(k)=='anti3'][0]].abs2()}")
            ok, parts = bc_stage3_check(M)
            say(f"  model is Bell-causal (product form) at stage 2->3: {ok}")
        obstr, rec, v = gc_reconstruction(M, N)
        if obstr:
            say(f"  GC RECONSTRUCTION OBSTRUCTED: zero ancestor with nonzero descendants: {obstr}")
            say(f"   => no GC sequential-growth model frozen at any N' >= {N} (nor any GC model that is"
                f" arbitrary up to a finite stage and real percolation p'<1 afterwards) reproduces this covariant vector measure")
        else:
            R, okm, okg, same = verify_reconstruction(M, N, rec)
            say(f"  GC reconstruction exists: MSR {okm}, GC {okg}, reproduces covariant vector measure {same}")
            # show reconstructed transition amplitudes at stages 1-2 (and whether Bell causal)
            if N == 3:
                rx = R.amp(ROOT, frozenset({0}))
                say(f"   reconstructed: x'={rx}, chain2->(cp,V,chain3)={[R.amp(C2, frozenset(s)) for s in [(), (0,), (0, 1)]]},"
                    f" anti2->(anti3,{{0}},{{1}},Lambda)={[R.amp(A2, frozenset(s)) for s in [(), (0,), (1,), (0, 1)]]}")
                ok, parts = bc_stage3_check(R)
                say(f"   reconstructed GC model Bell-causal at stage 2->3: {ok}")
            else:
                big = max((R.amp(c, P).abs2(), show(c), tuple(sorted(P))) for n in range(1, N) for c in M.levels[n] for P in downsets(c))
                say(f"   largest |reconstructed transition amplitude|^2 = {big[0]} at {big[1]} -> P={big[2]}")

    # ---- general stage-3 formulas, checked on a grid of exact holonomies
    say("=" * 100)
    say("STAGE-3 FORMULA CHECK: Bell-causal norm-GC family, x=1/2, |a1|=|b0|=1/4, b0=a1*u, u on a set of exact unit phases")
    units = [G(1), G(-1), I, G(Fr(3, 5), Fr(4, 5)), G(Fr(-3, 5), Fr(4, 5)), G(Fr(5, 13), Fr(12, 13)), G(Fr(-7, 25), Fr(24, 25))]
    x = Fr(1, 2); y = 1 - x
    for u in units:
        a1 = G(Fr(1, 4)); b0 = a1 * u
        al = (a1, a1 * x / y, ONE - a1 / y)
        be = (b0, b0 * x / y, b0 * x / y, ONE - b0 * (1 + x) / y)
        M = Model("grid", frozen_amp(stage3_table_amp(x, al, be), 3), 3)
        v = {nm(k): vv for k, vv in M.class_vector(3).items()}
        # predicted: v(cp) = x a1 + 2 x b0 ; mu(cp) = x^2 |a1|^2 |1 + 2u|^2 = x^2|a1|^2 (5 + 4 cos theta)
        pred = (x * x) * a1.abs2() * (5 + 4 * u.re)
        lhs, rhs, eq, mods = stage3_identity(M)
        say(f"  u={u}: cos theta={u.re}  mu(cp)={v['cp'].abs2()} predicted x^2|a1|^2(5+4cos)={pred}"
            f" GC value={9 * x * x * a1.abs2()}  identity holds={eq}  MSR={'OK' if not M.msr_ok() else 'BAD'}"
            f" normGC={'OK' if not M.norm_gc_ok(3) else 'BAD'}")

    # ---- closure: the obstruction is not robust (limits of GC-reproducible targets)
    say("=" * 100)
    say("CLOSURE CHECK near OBS: target v_eps = v_OBS + eps*(V-atom) - eps*(Lambda-atom).")
    say("A GC frozen-at-3 model reproducing v_eps exists for every eps != 0; the needed amplitudes diverge as eps -> 0.")
    x = Fr(2, 5)
    OBSM = Model("OBS", frozen_amp(stage3_table_amp(x, alO, beO), 3), 3)
    vO = OBSM.class_vector(3)
    kV = [k for k in vO if nm(k) == "V"][0]
    kL = [k for k in vO if nm(k) == "Lambda"][0]
    for eps in (Fr(1, 10), Fr(1, 100), Fr(1, 1000), Fr(-1, 1000)):
        tgt = dict(vO)
        tgt[kV] = tgt[kV] + eps
        tgt[kL] = tgt[kL] - eps

        class Tgt:  # minimal shim exposing the interface gc_reconstruction uses
            pass
        T = Tgt()
        T.levels = OBSM.levels
        T.classes = OBSM.classes
        T.class_vector = (lambda n, _t=tgt: _t)
        T.name = "target"
        obstr, rec, _ = gc_reconstruction(T, 3)
        if obstr:
            say(f"  eps={eps}: obstructed (unexpected)")
            continue
        R, okm, okg, same = verify_reconstruction(T, 3, rec)
        same = R.class_vector(3) == tgt
        a1p = R.amp(C2, frozenset())
        say(f"  eps={eps}: x'={R.amp(ROOT, frozenset({0}))}, MSR {okm}, GC {okg}, reproduces v_eps {same},"
            f" reconstructed chain2->cp amplitude {a1p}, |.|^2={a1p.abs2()}")

    # ---- classical comparison: non-DGC Bell-causal classical models (probabilities, path-dependent)
    say("=" * 100)
    say("CLASSICAL COMPARISON: Bell-causal stage-3 models with nonnegative real amplitudes (probabilities),")
    say("x=1/2, a1 and b0 free (a1 != b0 violates DGC).  Identity and GC reconstruction (frozen at 3).")
    x = Fr(1, 2); y = 1 - x
    for a1v, b0v in [(Fr(1, 4), Fr(1, 4)), (Fr(1, 4), Fr(1, 8)), (Fr(1, 4), Fr(1, 16)), (Fr(1, 8), Fr(1, 4))]:
        a1 = G(a1v); b0 = G(b0v)
        al = (a1, a1 * x / y, ONE - a1 / y)
        be = (b0, b0 * x / y, b0 * x / y, ONE - b0 * (1 + x) / y)
        M = Model("classical", frozen_amp(stage3_table_amp(x, al, be), 3), 3)
        nonneg = all(M.amp(c, P).im == 0 and M.amp(c, P).re >= 0 for n in (1, 2) for c in M.levels[n] for P in downsets(c))
        lhs, rhs, eq, mods = stage3_identity(M)
        obstr, rec, v = gc_reconstruction(M, 3)
        R = None
        if not obstr:
            R, okm, okg, same = verify_reconstruction(M, 3, rec)
        say(f"  a1={a1v}, b0={b0v}: probabilities nonneg {nonneg}; DGC {M.gc_ok(3)}; identity holds {eq} ({lhs} vs {rhs});"
            f" GC reconstruction {'obstructed' if obstr else 'exists'}"
            + ("" if R is None else f", reconstruction Bell-causal {bc_stage3_check(R)[0]}"))

    with open(sys.argv[1] if len(sys.argv) > 1 else "/dev/null", "w") as fh:
        fh.write("\n".join(OUT) + "\n")


if __name__ == "__main__":
    main()
