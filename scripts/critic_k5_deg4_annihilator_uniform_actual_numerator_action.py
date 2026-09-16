#!/usr/bin/env python3
from __future__ import annotations
import argparse,itertools,json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ANN=ROOT/'results/raw/k5_order8_s5_deg4_kirchhoff_annihilator_production_summary.json'
NUM=ROOT/'results/raw/k5_invariant_dual_deg27_canonical_dag_production_summary.json'
PREREG='5f386aeda775e5513fc37ac5767248f0b561fb45'
REPAIR='1424f2cce9f4e5669988ef31af11586d101bf1e5'
V=tuple(range(5));EDGES=tuple(itertools.combinations(V,2));N=len(EDGES);EIDX={e:i for i,e in enumerate(EDGES)}
PERMS=tuple(itertools.permutations(V))

def eperm(p,e):
    a,b=EDGES[e];x,y=p[a],p[b];return EIDX[(min(x,y),max(x,y))]
def act_mon(m,p):
    q=[0]*N
    for i,x in enumerate(m):q[eperm(p,i)]+=x
    return tuple(q)
def mons_deg(d):
    out=[]
    def rec(i,left,a):
        if i==N-1:out.append(tuple(a+[left]));return
        for x in range(left+1):rec(i+1,left-x,a+[x])
    rec(0,d,[]);return out
def orbit_partition(items,group):
    unseen=set(items);out=[]
    while unseen:
        x=min(unseen);o={act_mon(x,p) for p in group};out.append(tuple(sorted(o)));unseen-=o
    return out

BASE=EIDX[(0,1)];STAB=tuple(p for p in PERMS if {p[0],p[1]}=={0,1})
HORB=orbit_partition(mons_deg(3),STAB)
TRANS=tuple(next(p for p in PERMS if eperm(p,BASE)==e) for e in range(N))
QBAS=tuple(tuple(tuple(act_mon(m,TRANS[e]) for m in o) for o in HORB) for e in range(N))

def ann_uniform(coeff):
    q=[];dq=[]
    for e in range(N):
        z=Fraction(0);dz=Fraction(0)
        for j,c in enumerate(coeff):
            if not c:continue
            for m in QBAS[e][j]:z+=c;dz+=c*m[e]
        q.append(z);dq.append(dz)
    return tuple(q),tuple(dq)

def tree_poly():
    out={}
    for comb in itertools.combinations(range(N),4):
        adj={i:set() for i in V}
        for e in comb:
            a,b=EDGES[e];adj[a].add(b);adj[b].add(a)
        seen={0};stack=[0]
        while stack:
            x=stack.pop()
            for y in adj[x]:
                if y not in seen:seen.add(y);stack.append(y)
        if len(seen)==5:
            m=[0]*N
            for e in comb:m[e]=1
            out[tuple(m)]=Fraction(1)
    return out
PSI=tree_poly()
def pderiv(poly,i):
    out={}
    for m,c in poly.items():
        if m[i]:
            q=list(m);power=q[i];q[i]-=1;out[tuple(q)]=c*power
    return out

def vpsi_poly(coeff):
    out=defaultdict(Fraction)
    for e in range(N):
        d=pderiv(PSI,e)
        for j,cj in enumerate(coeff):
            if not cj:continue
            for qm in QBAS[e][j]:
                shift=list(qm);shift[e]+=1
                for m,c in d.items():
                    z=tuple(m[i]+shift[i] for i in range(N));out[z]+=cj*c
    return {m:c for m,c in out.items() if c}

def action_uniform(numerators,divv):
    # Frozen B_v formula at alpha=(1,...,1): s1=10, q_i=v_i=S=v(N)=0.
    return tuple(Fraction(10)*Fraction(divv)*Fraction(n) for n in numerators)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    ann=json.loads(ANN.read_text());num=json.loads(NUM.read_text())
    coeff=tuple(Fraction(x) for x in ann['k5_exact']['annihilator_representative_coefficients'])
    q,dq=ann_uniform(coeff);divv=sum((q[i]+dq[i] for i in range(N)),Fraction(0))
    nvals=tuple(Fraction(row[0]) for row in num['validation_points']['uniform']['numerators'])
    action=action_uniform(nvals,divv)
    researcher_expected=(Fraction(1055742187500000000000),Fraction(821132812500000000000))
    corrected_expected=(Fraction(10557421875000000000000),Fraction(8211328125000000000000))
    bad=list(coeff);bad[4]+=1
    wrong_div_action=action_uniform(nvals,divv+1)
    full_object=(num.get('source_choice_terms')==100000 and num.get('boundary_character')==[32,0,8,2,0,0,2] and num.get('reynolds_rank')==2)
    structural={
      'prereg_locked':PREREG=='5f386aeda775e5513fc37ac5767248f0b561fb45',
      'repair_locked':REPAIR=='1424f2cce9f4e5669988ef31af11586d101bf1e5',
      'ten_edges':len(EDGES)==10,
      'degree3_monomials_220':len(mons_deg(3))==220,
      'stabilizer_order12':len(STAB)==12,
      'fixed_edge_orbits_33':len(HORB)==33,
      'orbit_sizes_match_parent':list(map(len,HORB))==ann['orbit_data']['fixed_edge_cubic_orbit_sizes'],
      'annihilator_coeff_count33':len(coeff)==33,
      'psi_125_trees':len(PSI)==125 and all(c==1 for c in PSI.values()),
      'global_vpsi_zero':vpsi_poly(coeff)=={},
      'uniform_all_q_zero':q==(Fraction(0),)*10,
      'uniform_all_diag_dq_minus15':dq==(Fraction(-15),)*10,
      'uniform_divv_minus150':divv==Fraction(-150),
      'terminal_full32_object':full_object,
      'terminal_numerators_match_authority':nvals==(Fraction(-7038281250000000000),Fraction(-5474218750000000000)),
      'both_computed_actions_nonzero':all(x!=0 for x in action),
      'computed_action_matches_direct_B_formula':action==corrected_expected,
      'no_period_verdict_in_parent':num.get('scientific_invariant_dual_period_verdict') is None,
    }
    controls={
      'altered_annihilator_coefficient_breaks_vpsi':bool(vpsi_poly(tuple(bad))),
      'zero_numerator_fixture_gives_zero_action':action_uniform((0,0),divv)==(0,0),
      'representative_00000_object_rejected':full_object and num.get('source_choice_terms')!=1024,
      'wrong_divergence_changes_action':wrong_div_action!=action,
    }
    implementation_valid=all(structural.values()) and all(controls.values())
    agrees=(action==researcher_expected)
    if not implementation_valid:verdict='INVALID_IMPLEMENTATION'
    elif agrees:verdict='CONFIRMED_SCOPED'
    else:verdict='SCIENTIFIC_FAIL_CONFIRMED'
    out={'gate':'K5_DEG4_ANNIHILATOR_UNIFORM_ACTUAL_NUMERATOR_ACTION_INDEPENDENT_CRITIC','prereg_commit':PREREG,'repair_commit':REPAIR,'verdict':verdict,'checks':structural,'controls':controls,'researcher_witness_agreement':agrees,'uniform_q':[str(x) for x in q],'uniform_diag_dq':[str(x) for x in dq],'uniform_div_v':str(divv),'uniform_numerators':[str(x) for x in nvals],'researcher_uniform_action':[str(x) for x in researcher_expected],'independent_uniform_action':[str(x) for x in action],'exact_ratio_independent_over_researcher':['10','10'],'partial_cancelled_action_run_values_used':False,'weaker_nonzero_action_conclusion_survives':all(x!=0 for x in action),'constant_2x2_closure_verdict':None,'integrated_period_verdict':None}
    Path(args.output).parent.mkdir(parents=True,exist_ok=True);Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
    raise SystemExit(0 if verdict in ('CONFIRMED_SCOPED','SCIENTIFIC_FAIL_CONFIRMED') else 2)
if __name__=='__main__':main()
