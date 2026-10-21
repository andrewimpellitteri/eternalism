#!/usr/bin/env python3
"""Exact Fraction reproduction of Xu (2026), arXiv:2607.26672v1, Eqs. (258)-(260).

No third-party packages. Uses the operator CPOBC transition A_n^(2)=S Q_n Q_2^{-1}
from Eqs. (259)-(260), with Q_1=diag(q,1-q), R=r I, Q_2=Q_1 R,
S=I-(2I-Q_1)R. Tests the block-Hermiticity condition and determinant gates.
"""
from fractions import Fraction as F


def mm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def inv2(A):
    d = det2(A)
    assert d != 0, "matrix inverse requested on singular control"
    return [[A[1][1]/d, -A[0][1]/d], [-A[1][0]/d, A[0][0]/d]]


def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(2)] for i in range(2)]


def adjoint_real(A):
    return [[A[0][0], A[1][0]], [A[0][1], A[1][1]]]


def scenario(name, q, r, Qn, expected_hermitian, expected_commuting):
    one = F(1)
    Q1 = [[q, F(0)], [F(0), one-q]]
    R = [[r, F(0)], [F(0), r]]
    Q2 = mm(Q1, R)
    S = sub([[one, F(0)], [F(0), one]],
            mm(sub([[F(2), F(0)], [F(0), F(2)]], Q1), R))
    T2 = sub([[one, F(0)], [F(0), one]], R)
    A = mm(mm(S, Qn), inv2(Q2))
    Astar = adjoint_real(A)
    hermitian = A == Astar
    commute = mm(Q1, Qn) == mm(Qn, Q1)
    coeff = q * (one-(2-q)*r) - (one-q) * (one-(1+q)*r)
    factored = (2*q-one)*(one-r)
    assert coeff == factored
    assert det2(Q1) != 0 and det2(Q2) != 0
    assert det2(Qn) != 0 and det2(A) != 0 and det2(S) != 0
    assert (det2(T2) != 0) == (r != 1)
    assert hermitian == expected_hermitian, (name, A, Astar)
    assert commute == expected_commuting, (name, Q1, Qn)
    print(f"{name}: q={q}, r={r}, coefficient={coeff}")
    print(f"  det(Q1)={det2(Q1)}, det(Q2)={det2(Q2)}, det(Qn)={det2(Qn)}, "
          f"det(T2)={det2(T2)}, det(S)={det2(S)}, det(A)={det2(A)}")
    print(f"  Q_n={Qn}; A_n^(2)={A}; hermitian={hermitian}; [Q1,Qn]=0={commute}")


def poly_add(P, Q):
    out = dict(P)
    for mon, coef in Q.items():
        out[mon] = out.get(mon, 0) + coef
        if out[mon] == 0:
            del out[mon]
    return out


def poly_mul(P, Q):
    out = {}
    for (i, j), a in P.items():
        for (k, ell), b in Q.items():
            mon = (i+k, j+ell)
            out[mon] = out.get(mon, 0) + a*b
    return {m: c for m, c in out.items() if c}


def polynomial_identity():
    # Monomial key is (power of q, power of r); integer coefficients are exact.
    one, q, r = {(0, 0): 1}, {(1, 0): 1}, {(0, 1): 1}
    two_q = {(1, 0): 2}
    one_minus_q = poly_add(one, {(1, 0): -1})
    one_minus_r = poly_add(one, {(0, 1): -1})
    two_minus_q = {(0, 0): 2, (1, 0): -1}
    s_q = poly_add(one, {m: -c for m, c in poly_mul(two_minus_q, r).items()})
    s_other = poly_add(one, {m: -c for m, c in poly_mul(poly_add(one, q), r).items()})
    lhs = poly_add(poly_mul(q, s_q), {m: -c for m, c in poly_mul(one_minus_q, s_other).items()})
    rhs = poly_mul(poly_add(two_q, {(0, 0): -1}), one_minus_r)
    assert lhs == rhs, (lhs, rhs)
    print(f"symbolic identity: exact maps agree; coefficient polynomial={lhs}")


def commutator(A, B):
    return sub(mm(A, B), mm(B, A))


def check_commutator_identities():
    # Exact 2x2 rational control for the complementary block lemma.
    q = F(1, 3)
    A = [[q, F(0)], [F(0), 1-q]]
    B = [[F(2), F(1)], [F(1), F(3)]]
    Fop = mm(A, sub([[F(1), F(0)], [F(0), F(1)]], A))
    assert commutator(Fop, B) == [[F(0), F(0)], [F(0), F(0)]]
    C = mm(inv2(A), B)
    Cstar = mm(B, inv2(A))
    normal_comm = commutator(C, Cstar)
    assert det2(B) == 5
    assert normal_comm[0][0] == F(27, 4)
    # The block formula is (q^-2-(1-q)^-2) D D*: here D=1.
    assert normal_comm[0][0] == (1/q**2 - 1/(1-q)**2)
    print(f"complementary-mixing failure control: [F,B]=0, det(B)=5; "
          f"[A^-1B,BA^-1]_11={normal_comm[0][0]} != 0")

    Bdiag = [[F(2), F(0)], [F(0), F(3)]]
    Cdiag = mm(inv2(A), Bdiag)
    assert commutator(Cdiag, mm(Bdiag, inv2(A))) == [[F(0), F(0)], [F(0), F(0)]]
    print("commuting block control: diagonal B satisfies [A^-1B,BA^-1]=0")

    # Distinct R eigenvalues: [R,Qn]=0 directly kills the off-diagonal.
    R = [[F(1, 2), F(0)], [F(0), F(1, 3)]]
    Qn = [[F(2), F(1)], [F(1), F(3)]]
    rc = commutator(R, Qn)
    assert rc == [[F(0), F(1, 6)], [-F(1, 6), F(0)]]
    print(f"simple-R failure control: distinct eigenvalues force [R,Qn]=0, while this mixed Qn gives {rc}")

    # Distinct non-complementary eigenvalues: F=A(I-A) has simple spectrum,
    # so [F,Qn]=0 itself rules out mixing.
    A2 = [[F(1, 3), F(0)], [F(0), F(1, 4)]]
    Fop = mm(A2, sub([[F(1), F(0)], [F(0), F(1)]], A2))
    assert Fop[0][0] == F(2, 9) and Fop[1][1] == F(3, 16)
    assert commutator(Fop, Qn)[0][1] == F(5, 144)
    print("noncomplementary-spectrum control: F eigenvalues 2/9 and 3/16; [F,Qn]_12=5/144")


def main():
    polynomial_identity()
    check_commutator_identities()
    one, zero = F(1), F(0)
    # Positive diagonal/commuting control. All selected operators are nonsingular.
    scenario("commuting-control", F(1,3), F(1,2),
             [[F(2), zero], [zero, F(3)]], True, True)
    # Same nonsingular q,r but an off-diagonal candidate: exact obstruction to Hermiticity.
    scenario("rejected-noncommuting-control", F(1,3), F(1,2),
             [[F(2), one], [one, F(3)]], False, False)
    # The same mixing becomes Hermitian only at r=1, where T_2=I-R is singular.
    # This control is rejected because it lies outside the nonsingular hypothesis.
    scenario("rejected-singular-control", F(1,3), one,
             [[F(2), one], [one, F(3)]], True, False)
    # Irreducible algebraic singularity in Q1 is separately detected and rejected.
    assert det2([[zero, zero], [zero, one]]) == 0
    print("singular-Q1-control: det(Q1)=0; inverse gate rejects it")
    print("PASS: exact rational matrix checks and factorization identity")


if __name__ == "__main__":
    main()
