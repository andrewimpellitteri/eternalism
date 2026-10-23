"""Exact finite certificates for a named auxiliary instrument, not causal-set physics."""
from fractions import Fraction as F
from math import isqrt
from itertools import permutations
import json

# Q[sqrt(265),sqrt(65)] represented in basis 1,x,y,xy.
def r(a=0,b=0,c=0,d=0):return tuple(F(z) for z in (a,b,c,d))
def ra(a,b):return tuple(x+y for x,y in zip(a,b))
def rn(a):return tuple(-x for x in a)
def rm(a,b):
    out=[F(0)]*4
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i^j]+=x*y*(265 if i&j&1 else 1)*(65 if i&j&2 else 1)
    return tuple(out)
def cs(a,b):return a[0]+b[0],a[1]+b[1]
def cm(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def cc(a):return a[0],-a[1]
def n2(a):return a[0]**2+a[1]**2
def cz(a):return F(a),F(0)
def csum(xs):
    ans=cz(0)
    for x in xs:ans=cs(ans,x)
    return ans

def sqrt_bounds(n):
    scale=10**35
    lower=F(isqrt(n*scale*scale),scale)
    upper=lower+F(1,scale)
    assert lower*lower<=n<upper*upper
    return lower,upper

def bounds(a):
    terms=[(F(1),F(1)),sqrt_bounds(265),sqrt_bounds(65),sqrt_bounds(17225)]
    low=high=F(0)
    for coeff,(lo,hi) in zip(a,terms):
        low+=coeff*(lo if coeff>=0 else hi)
        high+=coeff*(hi if coeff>=0 else lo)
    return low,high

def decimal_interval(lo,hi):
    scale=10**12
    lower=(lo.numerator*scale)//lo.denominator
    upper=-((-hi.numerator*scale)//hi.denominator)
    assert F(lower,scale)<=lo<=hi<=F(upper,scale)
    return [f'{v//scale}.{v%scale:012d}' for v in (lower,upper)]

# Independent seed recurrence, no imports from previous checkers.
ONE=cz(1)
def seed_q(c,model):
    if len(c)==0:return ONE
    if len(c)==1:return cz(F(1,2))
    assert len(c)==2
    return F(3,20),F(-1 if model=='B' and c[1] else 1,5)
def ideals(c):
    return [p for p in range(1<<len(c)) if all(not(p>>j&1) or row&p==row for j,row in enumerate(c))]
def sub(c,p):
    old=[j for j in range(len(c)) if p>>j&1]
    return tuple(sum(1<<k for k,v in enumerate(old) if c[j]>>v&1) for j in old)
def weight(c,model):
    q=seed_q(c,model);d=n2(q)
    value=q[0]/d,-q[1]/d
    proper=csum(weight(sub(c,p),model) for p in ideals(c) if p!=(1<<len(c))-1)
    return value[0]-proper[0],value[1]-proper[1]
def amplitude(c,model):
    a=ONE
    for n,p in enumerate(c):a=cm(a,cm(seed_q(c[:n],model),weight(sub(c[:n],p),model)))
    return a

def main():
    level=[(0,a,b) for a in range(2) for b in range(4) if a!=1 or b!=2]
    assert len(level)==7
    amps={m:[amplitude(c,m) for c in level] for m in 'AB'}
    assert csum(amps['A'])==csum(amps['B'])==ONE
    assert [n2(a) for a in amps['A']]==[n2(a) for a in amps['B']]
    mags=[r(F(1,8)) if c not in [(0,0,3),(0,1,3)] else
          r(0,F(1,40)) if c==(0,0,3) else r(0,0,F(1,20)) for c in level]
    for a,w in zip(amps['A'],mags):assert rm(w,w)==r(n2(a))
    v=r(F(5,8),F(1,40),F(1,20))
    total=r()
    for w in mags:total=ra(total,w)
    assert total==v
    v2=rm(v,v)
    vlo,vhi=bounds(v);v2lo,v2hi=bounds(v2)
    assert 1<vlo<vhi<F(16,7)
    event=[i for i,c in enumerate(level) if c.count(0)==2]
    assert len(event)==4
    a={m:csum(amps[m][i] for i in event) for m in 'AB'}
    b={m:(1-a[m][0],-a[m][1]) for m in 'AB'}
    assert a=={'A':(F(1,2),F(0)),'B':(F(1,2),F(-1,5))}
    le=r()
    for i in event:le=ra(le,mags[i])
    lec=ra(v,rn(le))
    assert le==r(F(3,8),F(1,40))
    joint={}
    for m in 'AB':
        # All probabilities stored multiplied by common V_3^2.
        joint[m]=[r(n2(a[m])),r(n2(b[m])),
                  ra(rm(le,v),r(-n2(a[m]))),ra(rm(lec,v),r(-n2(b[m])))]
        summ=r()
        for num in joint[m]:
            summ=ra(summ,num)
            assert bounds(num)[0]>=0
        assert summ==v2
        # Ignoring final filter returns common membership probabilities.
        assert ra(joint[m][0],joint[m][2])==rm(le,v)
        assert n2(a[m])/(n2(a[m])+n2(b[m]))==F(1,2)
    assert ra(joint['B'][0],rn(joint['A'][0]))==r(F(1,25))
    # Partial pointer vectors: u0=(1,0),u1=(c,s). Compute amplitudes directly.
    for c,s in [(F(0),F(1)),(F(3,5),F(4,5)),(F(1),F(0))]:
        assert c*c+s*s==1
        success={}
        memory={}
        for m in 'AB':
            out0=cs(cm(cz(c),a[m]),b[m]);out1=cm(cz(s),a[m])
            success[m]=n2(out0)+n2(out1)
            expanded=n2(a[m])+n2(b[m])+2*c*cm(cc(a[m]),b[m])[0]
            assert success[m]==expanded
            # Reduced memory state, scaled by V; weights independent of model.
            memory[m]=[ra(rm(le,r(c*c)),lec),rm(le,r(c*s)),rm(le,r(s*s))]
        assert memory['A']==memory['B']
        assert success['B']-success['A']==F(2,25)*(1-c)
    # Auxiliary finite register symmetry: within-isomorphism-class permutations.
    # Equal positive phi coefficients and constant event membership imply both
    # Q_phi and P_E commute, hence so do all four Kraus operators.
    def canonical(c):
        edges=[(i,j) for j,row in enumerate(c) for i in range(j) if row>>i&1]
        return min(tuple(sorted((p[i],p[j]) for i,j in edges)) for p in permutations(range(3)))
    for i,c in enumerate(level):
        for j,d in enumerate(level):
            if canonical(c)==canonical(d):
                assert mags[i]==mags[j]
                assert (i in event)==(j in event)
    assert amps['B'][1]!=amps['B'][4]  # Covariant apparatus != invariant input.
    # Standard actual-pre/post rational states: strict Cauchy-Schwarz bound.
    psi=[F(3,5),F(4,5)];phi=[F(5,13),F(-12,13)]
    assert sum(x*x for x in psi)==sum(x*x for x in phi)==1
    overlap=sum(x*y for x,y in zip(psi,phi))
    weak=[x*y/overlap for x,y in zip(psi,phi)]
    assert weak==[F(-5,11),F(16,11)]
    tv=sum(abs(x) for x in weak)
    assert overlap*overlap<1/(tv*tv)
    # Saturated signed control nu=(2,-1): strong conditional is 4/5, not 4.
    assert F(4,9)/(F(4,9)+F(1,9))==F(4,5)
    assert F(4,9)+F(1,9)!=F(1,9)
    # GNS null vector on two supported histories: annihilated by amplitude
    # map, but intersection with the first singleton has nonzero image.
    x,y=amps['A'][0],amps['A'][1]
    null=cs(cm(y,x),cm((-x[0],-x[1]),y))
    assert null==cz(0) and n2(cm(y,x))>0
    # Rank-one kernel all 2x2 minors vanish (orientation conj(a_i)*a_j).
    gram=[[cm(cc(x),y) for y in amps['A']] for x in amps['A']]
    for i in range(7):
        for j in range(7):
            assert cm(gram[i][i],gram[j][j])==cm(gram[i][j],gram[j][i])
    bound=F(399999,10000000)*F(49,256)
    return {'status':'PASS','domain':'seven-history auxiliary pre/postselected register',
      'variation_exact':'(25+sqrt(265)+2sqrt(65))/40',
      'variation_display_interval':decimal_interval(vlo,vhi),
      'baseline_success_display_interval':decimal_interval(1/v2hi,1/v2lo),
      'joint_E_success_gap_display_interval':decimal_interval(F(1,25)/v2hi,F(1,25)/v2lo),
      'four_outcomes_positive_and_normalized_exactly':True,
      'record_only_statistics_equal':True,
      'finite_within_class_apparatus_covariance':True,
      'conditioned_E_frequency_both':'1/2',
      'partial_pointer_c_values':['0','3/5','1'],
      'total_success_gap_scaled_by_V_squared':'(2/25)(1-c)',
      'strict_bound_and_signed_saturating_controls':True,
      'rank_one_and_event_null_descent_witness':True,
      'completed_ideal_joint_gap_lower_bound':str(bound),
      'display_precision_note':'Decimal intervals rounded outward to 12 places; comparisons and algebra internally exact.',
      'limits':'No all-stage enumeration, physical preparation/cost, completed covariance or novelty certified.'}

if __name__=='__main__':print(json.dumps(main(),indent=2))
