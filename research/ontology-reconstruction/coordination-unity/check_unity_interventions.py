#!/usr/bin/env python3
"""Bounded intervention battery for the carrier-loop unity test.

Apparatus: the finite causal transport/return loop of
coordinator/FEEDBACK_CONSTITUTIVE_TEST.md section 1.  Continuous-time
characteristic equation z(t) = f(t-tau) + g z(t-l), l = tau + sigma.
Sampled on a unit delay grid this is exact for the delay-line model
(no interpolation error because all delays are integer samples).

We compute unit-impulse outputs, explicit dependency-graph edges and
strongly connected components (standard textbook machinery) for five
intervention configurations, plus a graded internal-cohesion measure.
No novelty, ontology or measurement-threshold claim is made.

Runtime target: well under the task limits (hard <= 15 s, actual <= 10 s,
total <= 30 s).  Pure Python standard library only.
"""

import time

T0 = time.perf_counter()

# ---------------------------------------------------------------- model
DT = 0.05          # sample time (s), arbitrary grid unit
TAU_N = 5          # outgoing transit  tau  = 0.25 s
SIGMA_N = 15       # return transit    sigma = 0.75 s
ELL_N = TAU_N + SIGMA_N   # loop delay l = 1.0 s
G = 0.8            # return attenuation, 0 <= g < 1
N = 600            # horizon (samples)

def impulse_response(step_out, loop_n, g):
    """h[k] = f[k - step_out] + g h[k - loop_n], unit impulse input."""
    h = [0.0] * N
    for k in range(N):
        if k == step_out:
            h[k] += 1.0
        if loop_n and k >= loop_n:
            h[k] += g * h[k - loop_n]
    return h

def show(h, label):
    taps = [(k, h[k]) for k in range(N) if abs(h[k]) > 1e-12]
    print(f"  {label}: {len(taps)} taps, first three {taps[:3]}")
    return taps

print("== Unit-impulse outputs (protocol f -> z, g = %.2f) ==" % G)
h_intact = impulse_response(TAU_N, ELL_N, G)
h_cut = impulse_response(TAU_N, 0, 0.0)                 # return severed at junction
h_reroute = impulse_response(TAU_N, ELL_N, G)           # new carrier, same sigma, same g

# External model-following generator: it never receives the outlet signal.
# Physically it is a small device at the junction that knows f and runs the
# same scalar recurrence internally, injecting g*ghat(t-sigma) as a computed
# value.  Its scripted output therefore reproduces the intact loop exactly.
h_gen = impulse_response(TAU_N, ELL_N, G)

same12 = max(abs(a - b) for a, b in zip(h_intact, h_reroute))
same14 = max(abs(a - b) for a, b in zip(h_intact, h_gen))
same13 = max(abs(a - b) for a, b in zip(h_intact, h_cut))
print("  max|h_intact - h_reroute|   = %.2e (equal-delay rerouting)" % same12)
print("  max|h_intact - h_generator| = %.2e (model generator, scripted input)" % same14)
print("  max|h_intact - h_cut|       = %.2e (interruption)" % same13)

# Robustness divergence: change the apparatus (outgoing transit tau -> 6 samples,
# hence l -> 21) while the generator keeps its scripted model (5, 20).
TAU2, ELL2 = 6, 21
h_loop2 = impulse_response(TAU2, ELL2, G)
h_gen2 = impulse_response(TAU_N, ELL_N, G)   # scripted generator keeps its old model
div = max(abs(a - b) for a, b in zip(h_loop2, h_gen2))
kmax = max(range(N), key=lambda k: abs(h_loop2[k] - h_gen2[k]))
print("  after apparatus change (tau: 5 -> 6 samples):")
print("  max|h_loop - h_generator|   = %.4f at sample %d (scripted equivalence breaks)"
      % (div, kmax))
print("  h_loop tracks the physical change: first taps %s"
      % [(k, round(h_loop2[k], 4)) for k in range(N) if abs(h_loop2[k]) > 1e-12][:3])

# ------------------------------------------------- graded cohesion measure
# Internal-cohesion fraction: echo energy / total output energy (impulse).
# Exact for positive g: 1/(1-g^2) - 1 over 1/(1-g^2) equals g^2.
tot = sum(x * x for x in h_intact)
ech = sum(x * x for x in h_intact[TAU_N + 1:])
print("== Graded internal-cohesion fraction (echo energy share) ==")
for gg in (0.8, 0.5, 0.1):
    hi = impulse_response(TAU_N, ELL_N, gg)
    t = sum(x * x for x in hi)
    e = sum(x * x for x in hi[TAU_N + 1:])
    print("  g = %.2f : measured echo share = %.6f (exact g^2 = %.6f)"
          % (gg, e / t, gg * gg))

# ------------------------------------------------------- dependency graphs
# Nodes: SRC (external driver), IN (junction), OUT (outgoing channel field),
# RET (return channel field).  Edge A->B means: interventions on A's state
# physically change B's ongoing signal role (physical carriage, not values).
def scc(nodes, edges):
    """Kosaraju SCC on a tiny graph (textbook machinery)."""
    radj = {v: [] for v in nodes}
    for a, b in edges:
        radj[b].append(a)
    order, seen = [], set()
    for s in nodes:
        if s in seen:
            continue
        stack, st = [s], {s}
        while stack:
            v = stack[-1]
            for w in radj[v]:
                if w not in st:
                    st.add(w)
                    stack.append(w)
                    break
            else:
                order.append(v)
                stack.pop()
                seen.add(v)
    comp, assign = [], {}
    for s in reversed(order):
        if s in assign:
            continue
        c = set()
        stack = [s]
        assign[s] = len(comp)
        while stack:
            v = stack.pop()
            c.add(v)
            for w in edges:
                if w[0] == v and w[1] not in assign:
                    assign[w[1]] = len(comp)
                    stack.append(w[1])
        comp.append(c)
    return comp

CONFIGS = {
    "intact loop":            [("SRC", "IN"), ("IN", "OUT"), ("OUT", "RET"), ("RET", "IN")],
    "interruption":           [("SRC", "IN"), ("IN", "OUT"), ("OUT", "RET")],
    "equal-delay rerouting":  [("SRC", "IN"), ("IN", "OUT"), ("OUT", "RET2"), ("RET2", "IN")],
    "external generator":     [("SRC", "IN"), ("IN", "OUT"), ("OUT", "RET")],
    "backreaction (eps>0)":   [("SRC", "IN"), ("IN", "OUT"), ("OUT", "RET"),
                               ("RET", "IN"), ("IN", "SRC")],
}
# The generator case adds no RET->IN edge: the generator is unconnected to OUT.
CONFIGS["external generator"] = [("SRC", "IN"), ("IN", "OUT")]

print("== Dependency-graph verdicts (SCC = textbook machinery) ==")
for name, edges in CONFIGS.items():
    nodes = sorted({v for e in edges for v in e})
    comps = scc(nodes, edges)
    loops = [c for c in comps if len(c) > 1]
    print("  %-24s components: %s   cyclic: %s"
          % (name, [sorted(c) for c in comps],
             [sorted(c) for c in loops] if loops else "none"))

# Backreaction graded measure: source integrator s[k+1] = (1-a) s[k] + eps * w[k].
# Steady DC gain of the loop on the source is eps/a -- continuous in eps, while
# the exact SCC verdict jumps at eps = 0.
ALPHA, EPS = 0.1, 0.01
print("== Backreaction scaling ==")
print("  exact SCC merges the source for every eps > 0 (sharp, fragile)")
print("  graded loop->source steady gain eps/alpha = %.4f at eps = %.3f"
      % (EPS / ALPHA, EPS))
print("  graded gain scales linearly: eps=0.001 -> %.4f" % (0.001 / ALPHA))

elapsed = time.perf_counter() - T0
print("== runtime: %.3f s (limit: hard 15 s, actual 10 s) ==" % elapsed)
assert elapsed < 10.0, "runtime budget exceeded"
