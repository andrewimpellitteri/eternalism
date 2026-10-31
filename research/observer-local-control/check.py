"""Exact controls and actual-model causal-past access/branch-mass certificates."""
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path
import sys
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[2]
PINS={
 'research/longshots/bc-matched-diffuse/check.py':'5bf747bd828e48c0b26aba50af5d38643480b4df1a8591f39423a6cd3dfb99d3',
 'research/longshots/bc-matched-norms/check.py':'c1d1ebbf13757001d57b87e8d4f93d3e4956a8c678015f46d03b1364247dc17d'}
for path,digest in PINS.items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest
spec=importlib.util.spec_from_file_location('local_checked_model',ROOT/'research/longshots/bc-matched-diffuse/check.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

def total(xs):
    out=m.I.of(0)
    for x in xs:out=out+x
    return out

def zero(x):
    assert x.contains(0) and x.hi-x.lo<m.GRID//2**100

def modulus(z):return z.norm2().sqrt()

def row(c,j,allowed=None):
    ps=m.ideals(c) if allowed is None else allowed
    return total(modulus(m.transition(c,p,j)) for p in ps)

def main():
    # Abstract exact negative/clean pair; overlap squared, no binary float.
    a=(F(1,2),F(1,2));b=(F(1),F(0))
    assert sum(a)==sum(b)==sum(map(abs,a))==sum(map(abs,b))==1
    overlap_squared=F(1,2);assert overlap_squared<1
    local=(F(1,3),F(2,3))
    # Two column states with disjoint parent flags; probabilities sum to one.
    clean_columns=[local,local]
    assert all(sum(c)==1 and all(x>=0 for x in c) for c in clean_columns)
    scaled=tuple(F(3,5)*x for x in local)
    assert tuple(x/sum(scaled) for x in scaled)==local and sum(scaled)==F(3,5)
    # The scaled algebraic row is NOT a second normalized MSR row.
    assert sum(scaled)!=1

    # Actual same-size contexts; observer o=2 has closed causal past {0,2}.
    c,d=(0,0,1),(0,1,1);R=5;O=2;P=2
    assert c[O]==d[O]==1 and m.induce(c,R)==m.induce(d,R)==(0,1)
    assert R==c[O]|(1<<O)==d[O]|(1<<O)
    assert P in m.ideals(c) and P not in m.ideals(d)
    assert set(p for p in m.ideals(c) if p&~R==0)==set(p for p in m.ideals(d) if p&~R==0)
    witness={}
    for j in 'AB':
        t=m.transition(c,P,j);modulus(t).tight(F(1,m.L**3))
        conditional_mass=modulus(t)/row(c,j)
        assert conditional_mass.lo>0
        wr=total(modulus(m.w(m.induce(c,p),j)) for p in m.ideals(c) if p&~R==0)
        for parent in (c,d):
            qs=m.q(parent,j);qphase=qs.scale(modulus(qs).inv())
            allowed=[p for p in m.ideals(parent) if p&~R==0]
            restricted=row(parent,j,allowed)
            zero(restricted-wr/F(m.L**3))
            for p in allowed:
                tr=m.transition(parent,p,j);w=m.w(m.induce(parent,p),j)
                state=tr.scale((modulus(tr)*restricted).sqrt().inv())
                local_state=w.scale((modulus(w)*wr).sqrt().inv())
                m.residual(state-qphase*local_state)
        witness[j]={'available_global_precursors':[list(m.ideals(c)),list(m.ideals(d))],
                    'conditional_mass_at_P2_first_context':m.decimal(conditional_mass),
                    'conditional_mass_at_P2_second_context':'exactly zero: invalid ideal',
                    'restricted_normalized_row_equal_up_to_parent_phase':True}

    # Actual causal past R=(0,0,3) of o=2, with isolated external spectators.
    # k=3 fixed; n=3,4,5. No change to the observer's induced past record.
    past=(0,0,3);k=3;R=(1<<k)-1
    local_mass=[]
    for n in (3,4,5):
        parent=past+(0,)*(n-k)
        assert parent[2]==3 and m.induce(parent,R)==past
        allowed=[p for p in m.ideals(parent) if p&~R==0]
        for j in 'AB':
            lhs=row(parent,j,allowed)
            rhs=row(past,j)*F(m.L**k,m.L**n)
            zero(lhs-rhs)
            probability=lhs/(1+m.zeta(n))
            upper=F(m.L**k,m.L**n)*(1+m.zeta(k))/(1+m.zeta(n))
            assert probability.hi<m.I.of(upper).lo
            if n>k:assert probability.hi<m.I.of(F(9,8)*F(m.L**k,m.L**n)).lo
        local_mass.append({'global_size':n,'past_size':k,'local_step_success':m.decimal(probability)})
    return {'status':'PASS','abstract_overlap_squared':str(overlap_squared),
            'same_observer_record':{'carrier':O,'closed_past_mask':5,'contexts':[c,d]},
            'actual_access_witness':witness,'fixed_past_branch_mass':local_mass,
            'dependency_sha256':PINS,
            'scope':'Actual finite register contexts and analytic mass identity. Restricts which precursor branches of the global instrument are retained; no universal observer locality theorem.'}

if __name__=='__main__':print(json.dumps(main(),indent=2))
