"""Actual-model orbit-descent certificates; shape names independently checked."""
import hashlib
import importlib.util
import json
from itertools import permutations
from pathlib import Path
import sys
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[2]
PINS={
 'research/longshots/bc-matched-diffuse/check.py':'5bf747bd828e48c0b26aba50af5d38643480b4df1a8591f39423a6cd3dfb99d3',
 'research/longshots/bc-matched-norms/check.py':'c1d1ebbf13757001d57b87e8d4f93d3e4956a8c678015f46d03b1364247dc17d'}
for name,digest in PINS.items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
s=importlib.util.spec_from_file_location('growth_intertwiner_model',ROOT/'research/longshots/bc-matched-diffuse/check.py')
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
F=m.F

def signature(c):
    edges=[(i,j) for j,row in enumerate(c) for i in range(j) if row>>i&1]
    return min(tuple(sorted((p[i],p[j]) for i,j in edges)) for p in permutations(range(len(c))))

def certificate(n,first,second,bound):
    source=first[:-1]; other=second[:-1]
    assert signature(first)==signature(second)
    assert signature(source)!=signature(other)
    assert first[-1] in m.ideals(source) and second[-1] in m.ideals(other)
    # Both child orders have exactly one comparable pair: chain2 + isolates.
    assert sum(row.bit_count() for row in first)==sum(row.bit_count() for row in second)==1
    levels=[list(m.enumerate_posets(k)) for k in (n,n+1)]
    src_mult=sum(signature(c)==signature(source) for c in levels[0])
    child_mult=sum(signature(c)==signature(first) for c in levels[1])
    assert src_mult==1
    values={}
    for model in 'AB':
        t=m.transition(source,first[-1],model);mod=t.norm2().sqrt()
        phase=t.scale((mod*bound*src_mult).sqrt().inv())
        positive=(mod/(bound*src_mult)).sqrt()
        assert phase.norm2().lo>0 and positive.lo>0
        if n==2:phase.norm2().tight(F(1,8))
        values[model]={'phase_real':m.decimal(phase.re),'phase_imag':m.decimal(phase.im),
                       'positive':m.decimal(positive),'phase_norm_squared':m.decimal(phase.norm2())}
    # Check actual early row contractions for the newly chosen B2=2.
    if n==2:
        for c in levels[0]:
            for model in 'AB':
                total=m.I.of(0)
                for p in m.ideals(c):total=total+m.transition(c,p,model).norm2().sqrt()
                assert total.hi<m.I.of(2).lo
    return {'depth':f'{n} -> {n+1}','source':'antichain','source_multiplicity':src_mult,
            'child':'one 2-chain plus isolated vertices','child_multiplicity':child_mult,
            'representatives':[first,second],
            'prefix_signatures':[str(signature(source)),str(signature(other))],
            'nonzero_source_component':values,
            'other_component':'exactly zero: unique parent is outside source orbit',
            'normalizer':m.decimal(m.I.of(bound)),'counts':[len(x) for x in levels]}

def run():
    early=certificate(2,(0,0,1),(0,1,0),F(2))
    late=certificate(3,(0,0,0,1),(0,0,1,0),1+m.zeta(3))
    assert early['child_multiplicity']==3 and late['child_multiplicity']==6
    # Up through size two every finite orbit is singleton: no earlier orbit
    # uniformity obstruction is possible for a unique-parent append map.
    for n in (0,1,2):
        level=list(m.enumerate_posets(n))
        assert len(set(signature(c) for c in level))==len(level)
    return {'status':'PASS_OBSTRUCTION','early_with_explicit_B2':early,'late_original_B3':late,
            'predecessor_sha256':PINS,
            'scope':'Actual-model finite counterexamples for both models/maps. B2=2 is an explicit early-step extension; original sequential construction starts at depth3. No completed gauge result.'}

if __name__=='__main__':print(json.dumps(run(),indent=2))
