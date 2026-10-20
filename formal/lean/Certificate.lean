set_option maxRecDepth 100000
/-!
# Light finite kernel for the complex-percolation certificate

This file is self-contained Lean 4 (core only; no mathlib, no dependencies).
It formalizes the finite combinatorial kernel used in the selected proof:

* naturally labelled causets on `{0,...,n-1}` as transitive Boolean relations;
* principal and doubly-principal orders;
* the two-cap map `G ↦ G ⊕ {u} ⊕ {v}`;
* checks, by finite evaluation (`decide`), that:
  - the counts of naturally labelled causets are 1, 2, 7, 40;
  - every doubly-principal order of size 3, 4, 5 is a two-cap of a unique
    order of size 1, 2, 3;
  - covers and incomparable pairs obey the paper's identities under capping;
  - the amplitude factorization `V_{k+2} = p * Σ_G p^{L+M} q^{h}` holds for
    `k=2` at concrete integer `p,q`.

This is a finite kernel, not the all-level analytic theorem. It is deliberately
lightweight: it uses no `sorry`, no axioms, and no imported library.
-/

namespace Cert

/-- `bit m i` is the `i`-th bit of `m`. -/
def bit (m i : Nat) : Bool := (m / 2 ^ i) % 2 == 1

/-- Index of the pair `(i,j)` among the pairs `i < j < n`. -/
def pairIndex (n i j : Nat) : Nat :=
  ((List.range i).map (fun a => n - 1 - a)).sum + (j - i - 1)

/-- Boolean relation `i ≺ j`; false unless `i < j`. -/
def hasRel (n mask i j : Nat) : Bool :=
  if i < j then bit mask (pairIndex n i j) else false

/-- Transitivity of the relation. -/
def isTrans (n mask : Nat) : Bool :=
  (List.range n).all (fun i =>
    (List.range n).all (fun j =>
      (List.range n).all (fun k =>
        !(hasRel n mask i j) || !(hasRel n mask j k) || hasRel n mask i k)))

/-- All naturally labelled causets on `{0,...,n-1}`. -/
def causets (n : Nat) : List Nat :=
  (List.range (2 ^ (n * (n - 1) / 2))).filter (fun m => isTrans n m)

/-- Maximal elements. -/
def maxima (n mask : Nat) : List Nat :=
  (List.range n).filter (fun i =>
    (List.range n).all (fun j => !(hasRel n mask i j)))

/-- Principal: unique maximal element. -/
def principal (n mask : Nat) : Bool := (maxima n mask).length == 1

/-- Restrict to the first `n-1` labels. -/
def restrict (n mask : Nat) : Nat :=
  (List.range (n - 1)).foldl (fun acc i =>
    (List.range (n - 1)).foldl (fun acc' j =>
      if i < j && hasRel n mask i j then
        acc' + 2 ^ pairIndex (n - 1) i j
      else acc') acc) 0

/-- Doubly principal: it and its restriction deleting the last label are principal. -/
def doubly (n mask : Nat) : Bool :=
  principal n mask && principal (n - 1) (restrict n mask)

/-- Pairs `i < j < n`, in the same order as `pairIndex`. -/
def pairs (n : Nat) : List (Nat × Nat) :=
  (List.range n).flatMap (fun i =>
    (List.range n).filterMap (fun j => if i < j then some (i, j) else none))

/-- Adjoin one universal maximum: `G ↦ G ⊕ {u}` (size n+1).
Relations of `G` are re-encoded in the size-(n+1) pair indexing; the new
element `n` is above every old element. -/
def cap (n mask : Nat) : Nat :=
  (pairs (n + 1)).foldl (fun acc p =>
    if p.2 < n then
      (if hasRel n mask p.1 p.2 then acc + 2 ^ pairIndex (n + 1) p.1 p.2 else acc)
    else
      acc + 2 ^ pairIndex (n + 1) p.1 p.2) 0

/-- Adjoin two universal maxima: `G ↦ G ⊕ {u} ⊕ {v}` (size n+2). -/
def cap2 (n mask : Nat) : Nat := cap (n + 1) (cap n mask)

/-- Cover relations. -/
def isCover (n mask i j : Nat) : Bool :=
  hasRel n mask i j &&
    (List.range n).all (fun k =>
      !(hasRel n mask i k && hasRel n mask k j))

def covers (n mask : Nat) : Nat :=
  (List.range n).foldl (fun acc i =>
    (List.range n).foldl (fun acc' j =>
      if isCover n mask i j then acc' + 1 else acc') acc) 0

def relations (n mask : Nat) : Nat :=
  (List.range n).foldl (fun acc i =>
    (List.range n).foldl (fun acc' j =>
      if hasRel n mask i j then acc' + 1 else acc') acc) 0

def incomparable (n mask : Nat) : Nat := n * (n - 1) / 2 - relations n mask

-- Causet counts. These match the Python enumeration (1, 2, 7, 40, 357).
example : (causets 1).length = 1 := by decide
example : (causets 2).length = 2 := by decide
example : (causets 3).length = 7 := by decide
theorem causet_count_four : (causets 4).length = 40 := by decide

-- The two-cap decomposition: the doubly-principal lists are exactly the caps.
example : (causets 3).filter (doubly 3) = (causets 1).map (cap2 1) := by decide
example : (causets 4).filter (doubly 4) = (causets 2).map (cap2 2) := by decide
theorem two_cap_five : (causets 5).filter (doubly 5) = (causets 3).map (cap2 3) := by decide

-- Capping adds `M(G)+1` covers and no incomparable pairs (k=1,2,3).
example : (causets 1).all (fun G =>
    covers 3 (cap2 1 G) == covers 1 G + (maxima 1 G).length + 1) := by decide
example : (causets 2).all (fun G =>
    covers 4 (cap2 2 G) == covers 2 G + (maxima 2 G).length + 1) := by decide
theorem covers_three : (causets 3).all (fun G =>
    covers 5 (cap2 3 G) == covers 3 G + (maxima 3 G).length + 1) := by decide

example : (causets 1).all (fun G =>
    incomparable 3 (cap2 1 G) == incomparable 1 G) := by decide
example : (causets 2).all (fun G =>
    incomparable 4 (cap2 2 G) == incomparable 2 G) := by decide
example : (causets 3).all (fun G =>
    incomparable 5 (cap2 3 G) == incomparable 3 G) := by decide

/-- `|A_p(C)|` at integer `p,q` (a concrete instance of the amplitude). -/
def amp (p q n mask : Nat) : Nat :=
  p ^ covers n mask * q ^ incomparable n mask

def V (p q n : Nat) : Nat :=
  ((causets n).filter (doubly n)).map (amp p q n) |>.sum

def sumG (p q k : Nat) : Nat :=
  (causets k).map (fun G =>
    p ^ (covers k G + (maxima k G).length) * q ^ incomparable k G) |>.sum

-- The amplitude factorization `V_{k+2} = p * Σ_G p^{L+M} q^h`, k=2, p=2, q=3.
theorem amp_factor_two : V 2 3 4 = 2 * sumG 2 3 2 := by decide

-- No axioms: `decide` reduces the finite computation.
#print axioms causet_count_four
#print axioms two_cap_five
#print axioms covers_three
#print axioms amp_factor_two

end Cert
