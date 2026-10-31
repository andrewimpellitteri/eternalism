"""Finite transition-dilation checks with pinned, inherited outward arithmetic.

The new checks act on actual model transition data through two late growth
steps. They do not re-prove the inherited model or supply physical gate costs.
"""
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path
import sys
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[2]
MODEL=ROOT/'research/longshots/bc-matched-diffuse/check.py'
ARITH=ROOT/'research/longshots/bc-matched-norms/check.py'
# Content pins are recorded alongside the output; predecessor commit ffb48d5.
EXPECTED={'research/longshots/bc-matched-diffuse/check.py': '5bf747bd828e48c0b26aba50af5d38643480b4df1a8591f39423a6cd3dfb99d3', 'research/longshots/bc-matched-norms/check.py': 'c1d1ebbf13757001d57b87e8d4f93d3e4956a8c678015f46d03b1364247dc17d'}

def load():
    for path,digest in EXPECTED.items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest, 'Predecessor changed; re-audit.'
    spec=importlib.util.spec_from_file_location('sequential_checked_model',MODEL)
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def run():
    m=load();I,Z,GRID=m.I,m.Z,m.GRID
    def total(xs):
        out=I.of(0)
        for x in xs:out=out+x
        return out
    def scalar_zero(x):
        assert x.contains(0)
        assert x.hi-x.lo<GRID//2**100
    def conjugate(z):return Z(z.re,-z.im)
    def norm(state):return total(z.norm2() for z in state.values())
    def variation(level,model):return total(m.amplitude(c,model).norm2().sqrt() for c in level)
    def target(level,model):
        v=variation(level,model)
        return {c:m.amplitude(c,model).scale(
            (m.amplitude(c,model).norm2().sqrt()*v).sqrt().inv()) for c in level}
    def positive(level):
        v=variation(level,'A')
        return {c:Z((m.amplitude(c,'A').norm2().sqrt()/v).sqrt(),I.of(0)) for c in level}
    def inner(left,right,selected):
        return m.zsum(conjugate(left[c])*right[c] for c in selected)
    # Direct enumeration is independent of append traversal used below.
    levels={n:tuple(m.enumerate_posets(n)) for n in (3,4,5)}
    assert [len(levels[n]) for n in levels]==[7,40,357]
    v3=variation(levels[3],'A');assert v3.hi<I.of(F(3,2)).lo
    states={j:target(levels[3],j) for j in 'AB'}
    reference=positive(levels[3]);b=F(1)
    rows=columns=0;witness=None;records=[]
    for n in (3,4,5):
        if n>3:
            old=n-1;bound=1+m.zeta(old);b*=bound
            new={j:{} for j in 'AB'};new_ref={};row_values=[]
            for c in levels[old]:
                ps=m.ideals(c)
                mods={j:{p:m.transition(c,p,j).norm2().sqrt() for p in ps} for j in 'AB'}
                sums={j:total(mods[j].values()) for j in 'AB'}
                for j in 'AB':
                    assert sums[j].lo>=GRID and sums[j].hi<I.of(bound).lo
                    success_column=total((mods[j][p]/bound) for p in ps)
                    failure=I.of(1)-sums[j]/bound
                    assert failure.lo>0
                    (success_column+failure).tight(1)
                scalar_zero(sums['A']-sums['B'])
                row_values.append((c,sums['A']))
                for p in ps:
                    child=c+(p,)
                    assert child in levels[n] and child not in new_ref
                    for j in 'AB':
                        t=m.transition(c,p,j)
                        coeff=t.scale((mods[j][p]*bound).sqrt().inv())
                        new[j][child]=states[j][c]*coeff
                    coeff_positive=(mods['A'][p]/bound).sqrt()
                    new_ref[child]=reference[c].scale(coeff_positive)
                    columns+=1
                rows+=1
            assert set(new_ref)==set(levels[n])
            states,reference=new,new_ref
            # An actual row-variation separation certifies the restricted
            # deterministic prefix-isometry obstruction, not a general no-go.
            low=min(row_values,key=lambda x:x[1].hi)
            high=max(row_values,key=lambda x:x[1].lo)
            if high[1].lo>low[1].hi:
                witness={'parent_size':old,'low_parent':low[0],'high_parent':high[0],
                         'low_row':m.decimal(low[1]),'high_row':m.decimal(high[1])}
        v=variation(levels[n],'A');r=I.of(1) if n==3 else v/(v3*b)
        assert r.lo>I.of(F(7,8)).hi and r.hi<=GRID+GRID//2**100
        scalar_zero(norm(reference)-r)
        phi=positive(levels[n])
        for c in levels[n]:m.residual(reference[c]-phi[c].scale(r.sqrt()))
        eta=(v3.square()*(b*b)).inv();assert eta.lo>I.of(F(1,3)).hi
        event=[c for c in levels[n] if c.count(0)==2]
        complement=[c for c in levels[n] if c.count(0)!=2]
        probabilities={};event_probs={}
        for j in 'AB':
            scalar_zero(norm(states[j])-r)
            wanted=target(levels[n],j)
            for c in levels[n]:m.residual(states[j][c]-wanted[c].scale(r.sqrt()))
            # Directly run the positive preparation BRA against the phase
            # preparation KET; both are unnormalized, charging both flags.
            baseline=inner(reference,states[j],levels[n]).norm2()
            scalar_zero(baseline-eta)
            outcome=[I.of(1)-r]
            assert outcome[0].lo>=0
            for subset in (event,complement):
                direct=inner(reference,states[j],subset).norm2()
                raw=m.zsum(m.amplitude(c,j) for c in subset)
                scalar_zero(direct-raw.norm2()*eta)
                sector=total(states[j][c].norm2() for c in subset)
                rejected=sector-direct
                assert rejected.lo>0 and direct.lo>0
                outcome.extend([direct,rejected])
                if subset is event:event_probs[j]=direct
            total(outcome).tight(1)
            probabilities[j]=[m.decimal(x) for x in outcome]
        gap=event_probs['B']-event_probs['A']
        assert gap.lo>I.of(F(399999,30000000)).hi
        records.append({'depth':n,'histories':len(levels[n]),'b_exact':str(b),
                        'variation':m.decimal(v),'forward_success':m.decimal(r),
                        'full_baseline_success':m.decimal(eta),
                        'joint_event_readout_gap':m.decimal(gap),
                        'outcomes_order':'prep_no, E_read_yes, E_read_no, Ec_read_yes, Ec_read_no',
                        'outcomes':probabilities})
    assert witness is not None
    # Exact paired controls with no inherited arithmetic/model dependency.
    # Scalar parent amplitudes (1/2,1/2), hence TV masses (1/2,1/2).
    # MSR rows (1,0) and (2,-1), B=3.
    parent=[F(1,2),F(1,2)];s=[F(1),F(3)]
    vn=sum(x*y for x,y in zip(parent,s));assert vn==2
    naive=parent;desired=[x*y/vn for x,y in zip(parent,s)]
    assert naive==[F(1,2),F(1,2)] and desired==[F(1,4),F(3,4)]
    rtoy=vn/F(3);eta_toy=rtoy*rtoy/(vn*vn)
    assert eta_toy==F(1,9) and rtoy/(vn*vn)==F(1,6)
    # Explicit clean constant-row MSR control: disjoint child columns whose
    # Born probabilities are abs(t)/3, with transition phases retained.
    constant_rows=[[F(2),F(-1)],[F(2),F(-1)]]
    assert all(sum(row)==1 for row in constant_rows)
    rowvars=[sum(abs(t) for t in row) for row in constant_rows]
    assert rowvars==[F(3),F(3)]
    target_masses=[abs(parent[i]*t)/3 for i,row in enumerate(constant_rows) for t in row]
    branch_masses=[parent[i]*abs(t)/rowvars[i] for i,row in enumerate(constant_rows) for t in row]
    assert branch_masses==target_masses==[F(1,3),F(1,6),F(1,3),F(1,6)]
    assert [sum(branch_masses[:2]),sum(branch_masses[2:])]==parent
    # The nonsummable contrast is the analytic sequence 2^-N -> 0,
    # not a limit conclusion certified by a few numerical values.
    s1=lambda x:x/(1-x)**2-x-2*x*x
    s2=lambda x:x*(1+x)/(1-x)**3-x-4*x*x
    z=m.L**2*s2(F(2,m.L))+4*s1(F(4,m.L))+4*s1(F(1,m.L))
    assert z<F(1,8)
    tail=z-m.zeta(3)-m.zeta(4)
    assert 0<tail<1
    # b_5 <= b_infinity <= b_5*exp(tail) <= b_5/(1-tail).
    limit_lower=(v3.square()*(I.of(b)/(1-tail)).square()).inv()
    limit_eta=I(limit_lower.lo,eta.hi)
    return {'status':'PASS','rows':rows,'append_columns':columns,
            'predecessor_commit':'ffb48d5','dependency_sha256':EXPECTED,
            'row_variation_obstruction_witness':witness,'exact_total_zeta':str(z),
            'levels':records,'formal_limiting_baseline_enclosure':m.decimal(limit_eta),
            'remaining_row_sum_after_depth5':str(tail),'controls':{'nonconstant_parent_marginals':'obstructed',
              'constant_row_variation':'explicit two-parent MSR rows and child masses checked',
              'toy_forward_success':'2/3','toy_full_baseline':'1/9',
              'incorrect_free_readout_baseline':'1/6','nonsummable_rejection':'analytic 2^-N contrast; not a finite checker limit result'},
            'limits':'Bounded interval arithmetic; model helpers reused and pinned. All-depth bounds analytic, no physical gate/locality/covariance/complexity result.'}

if __name__=='__main__':print(json.dumps(run(),indent=2))
