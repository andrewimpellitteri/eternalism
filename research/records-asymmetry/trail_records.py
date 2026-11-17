"""A walker that leaves a trail: records, a Janus point, and fake records.

Ring of L sites. State: walker position p, direction bit v (0 = +1, 1 = -1),
rotor bits c[0..L-1], substrate bits s[0..L-1]. One step U:
  1. rotor at p:  v <- v xor c[p];  c[p] <- c[p] xor 1
  2. move:        p <- p + (+1 if v == 0 else -1)
  3. footprint:   s[p] <- s[p] xor 1
Every substep is invertible, so U is a bijection. Rotors and substrate couple
to the walker in the same way (each toggles when visited). They differ only in
how they are prepared.

Exact enumeration over explicit uniform cells; no sampling.
Run: python3 -I trail_records.py   (writes trail_figure.svg next to itself)
"""

import os
from collections import Counter
from itertools import product
from math import log2

L = 12
TMAX = 10
WIN = 4  # event window length


def step(state):
    p, v, c, s = state
    c = list(c)
    s = list(s)
    v ^= c[p]
    c[p] ^= 1
    p = (p + (1 if v == 0 else -1)) % L
    s[p] ^= 1
    return (p, v, tuple(c), tuple(s))


def unstep(state):
    p, v, c, s = state
    c = list(c)
    s = list(s)
    s[p] ^= 1
    p = (p - (1 if v == 0 else -1)) % L
    c[p] ^= 1
    v ^= c[p]
    return (p, v, tuple(c), tuple(s))


def trajectory(x, t0):
    out = {t0: x}
    y = x
    for t in range(t0 + 1, TMAX + 1):
        y = step(y)
        out[t] = y
    y = x
    for t in range(t0 - 1, -TMAX - 1, -1):
        y = unstep(y)
        out[t] = y
    return out


def H(xs):
    c = Counter(xs)
    n = len(xs)
    return -sum(k / n * log2(k / n) for k in c.values())


def I(xs, ys):
    return H(xs) + H(ys) - H(list(zip(xs, ys)))


def arrivals_parity(tr, j, a, b):
    """Parity of walker arrivals at site j over steps a+1..b (a < b)."""
    return sum(tr[t][0] == j for t in range(a + 1, b + 1)) & 1


def main():
    # Boundary cell at t = 0: walker at 0 heading +1, substrate blank, rotors uniform.
    cell0 = [(0, 0, c, (0,) * L) for c in product((0, 1), repeat=L)]
    trajs = [trajectory(x, 0) for x in cell0]
    n = len(trajs)

    print(f"boundary cell: {n} microstates (substrate blank at t=0, rotors uniform)")
    print("   t  H(substrate)/site  H(rotors)/site  rec->past  rec->future")
    rows = {}
    for t in range(-TMAX, TMAX + 1):
        hs = sum(H([tr[t][3][j] for tr in trajs]) for j in range(L)) / L
        hc = sum(H([tr[t][2][j] for tr in trajs]) for j in range(L)) / L
        past = fut = None
        if t - WIN >= -TMAX:
            past = sum(I([tr[t][3][j] for tr in trajs],
                         [arrivals_parity(tr, j, t - WIN, t) for tr in trajs]) for j in range(L)) / L
        if t + WIN <= TMAX:
            fut = sum(I([tr[t][3][j] for tr in trajs],
                        [arrivals_parity(tr, j, t, t + WIN) for tr in trajs]) for j in range(L)) / L
        rows[t] = (hs, hc, past, fut)
        fmt = lambda v: f"{v:.3f}" if v is not None else "  -  "
        print(f"  {t:+3d}   {hs:.3f}             {hc:.3f}           {fmt(past)}      {fmt(fut)}")

    # Rotor bits as would-be records: same coupling, random preparation.
    t = 6
    rot = sum(I([tr[t][2][j] for tr in trajs],
                [arrivals_parity(tr, j, t - WIN, t) for tr in trajs]) for j in range(L)) / L
    print(f"\nrotors at t={t} as records of past visits: mean I = {rot:.3f}")

    # Present-only conditioning at T: condition on an observed (walker position,
    # substrate pattern) alone, with direction and rotors uniform. Report the
    # most common observation and the one with the longest trail.
    T = 6
    obs_counts = Counter((tr[T][0], tr[T][3]) for tr in trajs)
    common = obs_counts.most_common(1)[0][0]
    longest = max(obs_counts, key=lambda o: (sum(o[1]), obs_counts[o]))
    for label, (pT, sT) in (("most common", common), ("longest trail", longest)):
        cellT = [(pT, v, c, sT) for v in (0, 1) for c in product((0, 1), repeat=L)]
        genuine = faithful = 0
        for x in cellT:
            tr = trajectory(x, T)
            genuine += tr[0][3] == (0,) * L
            faithful += all(sT[j] == arrivals_parity(tr, j, 0, T) for j in range(L))
        print(f"\npresent-only cell at T={T}, {label} observation: walker at {pT},"
              f" substrate {''.join(map(str, sT))}, {len(cellT)} microstates")
        print(f"  came from a blank substrate at t=0: {genuine}/{len(cellT)} = {genuine / len(cellT):.4f}")
        print(f"  (equivalently, its trail equals the parity of actual visits over (0,{T}]: {faithful / len(cellT):.4f})")
        print(f"  boundary-cell microstates producing this observation: {obs_counts[(pT, sT)]}")

    # Pick a sample trajectory for the space-time picture: one with a long trail.
    sample = max(trajs, key=lambda tr: (sum(tr[TMAX][3]) + sum(tr[-TMAX][3]), tr[0][2]))
    svg(rows, sample)


def svg(rows, tr):
    W, Hh = 820, 470
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {Hh}" font-family="Helvetica, Arial, sans-serif" font-size="12">',
           '<rect width="100%" height="100%" fill="#ffffff"/>']
    # Panel A: space-time diagram. Time runs down.
    x0, y0, cw, ch = 40, 52, 22, 17
    out.append(f'<text x="{x0}" y="28" font-weight="600" fill="#111">A. One history: footprints (dark) and walker (ring)</text>')
    for t in range(-TMAX, TMAX + 1):
        y = y0 + (t + TMAX) * ch
        if t % 5 == 0:
            out.append(f'<text x="{x0 - 6}" y="{y + 12}" text-anchor="end" fill="#555">{t:+d}</text>')
        p, v, c, s = tr[t]
        for j in range(L):
            fill = "#1f2937" if s[j] else ("#e0ecff" if t == 0 else "#f3f4f6")
            out.append(f'<rect x="{x0 + j * cw}" y="{y}" width="{cw - 2}" height="{ch - 2}" fill="{fill}"/>')
        out.append(f'<circle cx="{x0 + p * cw + (cw - 2) / 2}" cy="{y + (ch - 2) / 2}" r="5.5" fill="none" stroke="#dc2626" stroke-width="2"/>')
    yb = y0 + (2 * TMAX + 1) * ch
    out.append(f'<text x="{x0}" y="{yb + 16}" fill="#555">site →     time ↓ (blank substrate at t = 0, shaded blue)</text>')

    # Panels B and C: curves.
    px, pw = 360, 430

    def X(t):
        return px + (t + TMAX) / (2 * TMAX) * pw

    def panel(top, h, title, lo, hi, series, zero=False, notes=None):
        out.append(f'<text x="{px}" y="{top - 10}" font-weight="600" fill="#111">{title}</text>')
        out.append(f'<rect x="{px}" y="{top}" width="{pw}" height="{h}" fill="none" stroke="#ccc"/>')
        out.append(f'<line x1="{X(0):.1f}" x2="{X(0):.1f}" y1="{top}" y2="{top + h}" stroke="#2563eb" stroke-dasharray="3 3"/>')
        for v in (lo, hi) + ((0.0,) if zero else ()):
            y = top + h - (v - lo) / (hi - lo) * h
            out.append(f'<text x="{px - 6}" y="{y + 4:.1f}" text-anchor="end" fill="#555">{v:g}</text>')
            if zero and v == 0.0:
                out.append(f'<line x1="{px}" x2="{px + pw}" y1="{y:.1f}" y2="{y:.1f}" stroke="#999"/>')
        for t in range(-TMAX, TMAX + 1, 5):
            out.append(f'<text x="{X(t):.1f}" y="{top + h + 15}" text-anchor="middle" fill="#555">{t:+d}</text>')
        for pts, color, lab, k in series:
            ys = [(t, top + h - (v - lo) / (hi - lo) * h) for t, v in pts]
            out.append(f'<polyline points="{" ".join(f"{X(t):.1f},{y:.1f}" for t, y in ys)}" fill="none" stroke="{color}" stroke-width="2"/>')
            out.append("".join(f'<circle cx="{X(t):.1f}" cy="{y:.1f}" r="2.5" fill="{color}"/>' for t, y in ys))
            if lab:
                out.append(f'<text x="{px + pw - 6}" y="{top + h - 30 + 15 * k}" text-anchor="end" fill="{color}">{lab}</text>')
        for (txt, yy) in notes or []:
            out.append(f'<text x="{px + 8}" y="{yy}" fill="#555">{txt}</text>')

    ts = range(-TMAX, TMAX + 1)
    panel(52, 140, "B. Entropy per site (single-bit marginals)", 0, 1,
          [([(t, rows[t][0]) for t in ts], "#111827", "substrate", 0),
           ([(t, rows[t][1]) for t in ts], "#9ca3af", "rotors", 1)])
    rd = [(t, rows[t][2] - rows[t][3]) for t in ts if rows[t][2] is not None and rows[t][3] is not None]
    lo = min(-0.05, min(v for _, v in rd) * 1.15)
    hi = max(0.05, max(v for _, v in rd) * 1.15)
    lo, hi = -max(-lo, hi), max(-lo, hi)
    panel(260, 150, f"C. Which way do footprints point? (window {WIN} steps)", round(lo, 2), round(hi, 2),
          [(rd, "#dc2626", "", 0)], zero=True,
          notes=[("above 0: footprints tell where it was", 276), ("below 0: where it will be", 404)])
    out.append("</svg>")
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "trail_figure.svg")
    with open(path, "w") as fh:
        fh.write("\n".join(out))
    print(f"\nwrote {path}")


if __name__ == "__main__":
    main()
