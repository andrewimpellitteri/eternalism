"""Minimal check for longshot-bell-for-passage RESULT.md.

Demonstrates the logical structure of the negative result:
  (i)  a chance function with "present-state-alone" (Markov / history-irrelevant)
       structure and PROBABILISTIC-LOCALITY-style nonlocal present chances can
       produce CHSH = 4 statistics (so the pair {history-irrelevance, probabilistic
       locality} cannot both hold -- Horvat's Proposition 3 in numbers);
  (ii) a history-RELEVANT twin theory reproduces exactly the same observable
       statistics, so no inequality on observables separates the two bridge
       premises -- each conjunct is detachable while passage/ontology never is.

Pure stdlib, no dependencies.  Run: python3 toy_check.py
"""
from fractions import Fraction as F

OUT = (1, -1)
SETTINGS = ((0, 0), (0, 1), (1, 0), (1, 1))

def chsh(tab):
    """tab[(x,y)] = E(x,y)."""
    return tab[(0, 0)] + tab[(0, 1)] + tab[(1, 0)] - tab[(1, 1)]

# --- observable target: PR-box statistics (the standard stand-in for the
# --- experimentally violated correlations; quantum reaches 2*sqrt(2) < 4).
PR = {}
for (x, y) in SETTINGS:
    same = (x, y) != (1, 1)
    for a in OUT:
        for b in OUT:
            PR[(x, y, a, b)] = F(1, 2) if ((a == b) if same else (a == -b)) else F(0)
E_pr = {k: sum(a * b * PR[(k[0], k[1], a, b)] for a in OUT for b in OUT) for k in SETTINGS}
assert E_pr[(0, 0)] == E_pr[(0, 1)] == E_pr[(1, 0)] == 1 and E_pr[(1, 1)] == -1
assert chsh(E_pr) == 4, "PR statistics must violate CHSH"

# --- T_M: chances governed by the complete present state e alone (history
# --- irrelevant, Eq. 15-16 of Horvat hold), yet the present-state chances are
# --- nonlocal (e is a two-site state).  Observable statistics = PR.  Because LC
# --- fails while history is irrelevant, Horvat's Prop. 3 says probabilistic
# --- locality fails; in the toy this is visible across the two present states
# --- e_PR and e_antiPR, which agree in distribution on every single-site slice
# --- (each 50/50) but disagree on joint chances.
present_states = ("e_PR", "e_antiPR")
P_given_e = {"e_PR": PR}
anti = {}
for k, p in PR.items():
    x, y, a, b = k
    anti[k] = PR[(x, y, -a, b)]  # flip site a: perfect correlation <-> anti-correlation
P_given_e["e_antiPR"] = anti
# single-site slice distributions agree across the two present states:
for s in (0, 1):
    for site in ("a",):
        for a in OUT:
            ps = {e: sum(P_given_e[e][(s, s, a, b)] for b in OUT) for e in present_states}
            assert ps["e_PR"] == ps["e_antiPR"] == F(1, 2)
# joint chances disagree:
assert P_given_e["e_PR"][(0, 0, 1, 1)] == F(1, 2)
assert P_given_e["e_antiPR"][(0, 0, 1, 1)] == 0

# --- T_H: history-relevant twin.  Present state e is coarse (outcome pair not
# --- yet fixed); histories h1, h2 (prior 1/2 each, independent of settings --
# --- settings independence holds) give different chances conditional on e:
# ---   Ch(.|e,h1): (+,+) whenever a=b, (+,-) when a=-b   (the "all plus" branch)
# ---   Ch(.|e,h2): (-,-) whenever a=b, (-,+) when a=-b   (the "all minus" branch)
# --- so Ch(a=+1|e,x=0,h1)=1 but Ch(a=+1|e,x=0,h2)=0 (Eq. 18 of Horvat holds).
hist_prior = F(1, 2)  # settings-independent
P_hist = {1: {}, 2: {}}
for (x, y) in SETTINGS:
    same = (x, y) != (1, 1)
    for a in OUT:
        for b in OUT:
            P_hist[1][(x, y, a, b)] = F(1) if (a == 1 and ((a == b) if same else (b == -1))) else F(0)
            P_hist[2][(x, y, a, b)] = F(1) if (a == -1 and ((a == b) if same else (b == 1))) else F(0)
# conditional chances at L differ by history, observables match:
assert P_hist[1][(0, 0, 1, 1)] == 1 and P_hist[2][(0, 0, 1, 1)] == 0
avg = {k: hist_prior * P_hist[1][k] + hist_prior * P_hist[2][k] for k in PR}
assert avg == PR, "history-averaged statistics must equal the PR observables exactly"
E_avg = {k: sum(a * b * avg[(k[0], k[1], a, b)] for a in OUT for b in OUT) for k in SETTINGS}
assert E_avg == E_pr and chsh(E_avg) == 4

print("CHSH of PR observable statistics      :", chsh(E_pr))
print("history-averaged stats == PR stats    :", avg == PR)
print("slice-marginals equal across e-states :", True)
print("CHSH unchanged under history mixing   :", chsh(E_avg))
print("ALL CHECKS PASSED")
