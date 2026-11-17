"""Follow-ups to the walker-trail model (Results 9 and 10 of RESULT.md).

Same dynamics as trail_records.py, written with bitmasks so larger rings run.
Run: python3 -I push_records.py
"""

from collections import Counter
from math import log2


def make(L):
    full = (1 << L) - 1

    def step(p, v, c, s):
        v ^= (c >> p) & 1
        c ^= 1 << p
        p = (p + (1 if v == 0 else -1)) % L
        s ^= 1 << p
        return p, v, c, s

    def unstep(p, v, c, s):
        s ^= 1 << p
        p = (p - (1 if v == 0 else -1)) % L
        c ^= 1 << p
        v ^= (c >> p) & 1
        return p, v, c, s

    return step, unstep, full


def scaling():
    print("Result 9: present-only conditioning, scaling with ring size L and elapsed time T")
    print("   L   T  mean trail  P(blank at 0 | obs)  P(boundary cell | obs)  longest-trail obs: sites, P(blank)")
    for L in (8, 10, 12, 14):
        step, unstep, _ = make(L)
        for T in (2, 4, 6, 8):
            # Boundary ensemble: walker at 0 heading +1, blank substrate, rotors uniform.
            obs = Counter()
            for c in range(1 << L):
                p, v, cc, s = 0, 0, c, 0
                for _ in range(T):
                    p, v, cc, s = step(p, v, cc, s)
                obs[(p, s)] += 1
            # Present cell for (p, s): v and rotors uniform. s does not affect the
            # motion, so s at t=0 is s_T xor (parity pattern of the backward path).
            # Count, for each p, how many (v, c) give each backward parity pattern.
            pat = Counter()
            for p in {o[0] for o in obs}:
                for v in (0, 1):
                    for c in range(1 << L):
                        q, w, cc, s = p, v, c, 0
                        for _ in range(T):
                            q, w, cc, s = unstep(q, w, cc, s)
                        pat[(p, s)] += 1
            cell = 1 << (L + 1)
            tot = 1 << L
            mean_trail = sum(n * bin(s).count("1") for (p, s), n in obs.items()) / tot
            blank = sum(n / tot * pat[o] / cell for o, n in obs.items())
            strict = sum(n / tot * n / cell for o, n in obs.items())
            longest = max(obs, key=lambda o: (bin(o[1]).count("1"), obs[o]))
            print(f"  {L:2d}  {T}    {mean_trail:5.2f}        {blank:.4f}              {strict:.4f}"
                  f"               {bin(longest[1]).count('1'):2d}, {pat[longest] / cell:.5f}")


def H(counter):
    n = sum(counter.values())
    return -sum(k / n * log2(k / n) for k in counter.values() if k)


def two_boundary(L=12, Tf=8, w=2):
    print(f"\nResult 10: blank substrate imposed at t=0 and at t={Tf} (L={L}, window {w})")
    step, unstep, _ = make(L)
    single, double = [], []
    for c in range(1 << L):
        st = [(0, 0, c, 0)]
        for _ in range(Tf):
            st.append(step(*st[-1]))
        single.append(st)
        if st[-1][3] == 0:
            double.append(st)
    print(f"  microstates: one boundary {len(single)}, both boundaries {len(double)}")

    def direction(trajs, t):
        def mi(a, b):
            ca, cb, cab = Counter(a), Counter(b), Counter(zip(a, b))
            return H(ca) + H(cb) - H(cab)

        past = fut = 0.0
        for j in range(L):
            sj = [(tr[t][3] >> j) & 1 for tr in trajs]
            pp = [sum(tr[u][0] == j for u in range(t - w + 1, t + 1)) & 1 for tr in trajs]
            pf = [sum(tr[u][0] == j for u in range(t + 1, t + w + 1)) & 1 for tr in trajs]
            past += mi(sj, pp)
            fut += mi(sj, pf)
        return past / L, fut / L

    print("   t   one boundary: past, future    both boundaries: past, future")
    for t in range(w, Tf - w + 1):
        a = direction(single, t)
        b = direction(double, t)
        print(f"  {t:2d}        {a[0]:.3f}, {a[1]:.3f}                  {b[0]:.3f}, {b[1]:.3f}")


if __name__ == "__main__":
    scaling()
    two_boundary()
