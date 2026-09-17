#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DEG_PATH=ROOT/'scripts/k5_projective_normal_polynomial_numerator_degree_ceiling.py'
ANN_SUM=ROOT/'results/raw/k5_order8_s5_deg4_kirchhoff_annihilator_production_summary.json'
PREREG='61d8a72c775d14356695196c50aa2395f9b9afc5'
PASS='K5_PROJECTIVE_NORMAL_32ORBIT_EXACT_CORNER_ORDERS_RESOLVED_SCOPED'
ZERO='K5_PROJECTIVE_NORMAL_32ORBIT_FROZEN_PATH_ZERO_FOUND_EXACT_SCOPED'
NONUNIFORM='K5_PROJECTIVE_NORMAL_32ORBIT_WITNESS_ORDER_NONUNIFORM_EXACT_SCOPED'
S5FAIL='K5_PROJECTIVE_NORMAL_32ORBIT_S5_COEFFICIENT_COVARIANCE_FAIL_EXACT_SCOPED'
INVALID='INVALID_IMPLEMENTATION'
DEG=5
W1=(2,3,5,7,11,13,17,19,23,29)
W2=(31,37,41,43,47,53,59,61,67,71)
CYCLE=(1,2,3,4,0)

spec=importlib.util.spec_from_file_location('deg_support',DEG_PATH)
deg=importlib.util.module_from_spec(spec); assert spec.loader is not None; spec.loader.exec_module(deg)
EDGES=tuple(deg.EDGES); N=len(EDGES); EIDX=dict(deg.EIDX); PERMS=tuple(deg.PERMS)


def fq(q):
    q=Fraction(q); return q.numerator if q.denominator==1 else f'{q.numerator}/{q.denominator}'

def vec_hash(v):
    raw=json.dumps([fq(x) for x in v],separators=(',',':')).encode(); return hashlib.sha256(raw).hexdigest()

def edge_perm(p,eidx):
    a,b=EDGES[eidx]; x,y=p[a],p[b]; return EIDX[(min(x,y),max(x,y))]

def mask_perm(mask,p):
    z=0
    for e in range(N):
        if (mask>>e)&1: z|=1<<edge_perm(p,e)
    return z

def perm_weights(w,p):
    out=[0]*N
    for e,x in enumerate(w): out[edge_perm(p,e)]=x
    return tuple(out)
WP1=perm_weights(W1,CYCLE); WP2=perm_weights(W2,CYCLE)

def subset_orbits():
    unseen=set(range(1<<N)); out=[]
    while unseen:
        rep=min(unseen); orb={mask_perm(rep,p) for p in PERMS}; out.append((rep,len(orb),tuple(sorted(orb)))); unseen-=orb
    return out

def proper_reps(): return [(m,s) for m,s,_ in subset_orbits() if m not in (0,(1<<N)-1)]

def add1(a,b):
    n=max(len(a),len(b)); out=[Fraction(0)]*n
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=x
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def scale1(a,c):
    c=Fraction(c); return [c*x for x in a]

def mul1(a,b):
    out=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def pad6(a):
    assert len(a)<=DEG+1
    return tuple(a+[Fraction(0)]*(DEG+1-len(a)))

def substitute_multivariate(poly,mask,weights):
    out=[Fraction(0)]*(DEG+1)
    for mon,c in poly.items():
        power=sum(mon[e] for e in range(N) if (mask>>e)&1)
        assert power<=DEG
        z=Fraction(c)
        for e,p in enumerate(mon): z*=Fraction(weights[e])**p
        out[power]+=z
    return tuple(out)

def substitute_any(poly,mask,weights,maxdeg):
    out=[Fraction(0)]*(maxdeg+1)
    for mon,c in poly.items():
        power=sum(mon[e] for e in range(N) if (mask>>e)&1)
        assert power<=maxdeg
        z=Fraction(c)
        for e,p in enumerate(mon): z*=Fraction(weights[e])**p
        out[power]+=z
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def state(v):
    o=next((i for i,x in enumerate(v) if x),None); return ('ZERO',None) if o is None else ('ORDER',o)

def route_b(mask,weights,qs):
    al=[]
    for e,w in enumerate(weights): al.append([Fraction(w),Fraction(0)] if not ((mask>>e)&1) else [Fraction(0),Fraction(w)])
    q1=[substitute_any(q,mask,weights,3) for q in qs]
    v=[mul1(al[e],q1[e]) for e in range(N)]
    s1=[Fraction(0)]; S=[Fraction(0)]; A=[Fraction(0)]; V=[Fraction(0)]
    for e in range(N):
        s1=add1(s1,al[e]); S=add1(S,v[e])
        if (mask>>e)&1: A=add1(A,al[e]); V=add1(V,v[e])
    return pad6(add1(mul1(s1,V),scale1(mul1(S,A),-1)))
def build_objects(ann_coeff):
    stab,horb,qbas,qs=deg.reconstruct_q(ann_coeff)
    alphas=tuple(deg.alpha_linear_poly(i) for i in range(N))
    s1={}; S={}; vs=tuple(deg.pshift(qs[i],i) for i in range(N))
    for a in alphas:s1=deg.padd(s1,a)
    for v in vs:S=deg.padd(S,v)
    return stab,horb,qs,alphas,vs,s1,S

def U_poly(mask,alphas,vs,s1,S,bad_factor=1):
    A={}; V={}
    for e in range(N):
        if (mask>>e)&1:
            A=deg.padd(A,alphas[e]); V=deg.padd(V,vs[e])
    return deg.padd(deg.pmul(s1,V),deg.pscale(deg.pmul(S,A),-bad_factor))
def V_poly(mask,vs):
    V={}
    for e in range(N):
        if (mask>>e)&1: V=deg.padd(V,vs[e])
    return V

def main():
    ann=json.loads(ANN_SUM.read_text())
    ann_coeff=tuple(Fraction(x) for x in ann['k5_exact']['annihilator_representative_coefficients'])
    stab,horb,qs,alphas,vs,s1,S=build_objects(ann_coeff)
    psi=deg.spanning_tree_poly(); vp=deg.vpsi(vs,psi)
    reps=proper_reps(); orbits=subset_orbits()
    rows=[]; route_ok=True; degree_ok=True; s5_ok=True; witness_ok=True; zero_found=False; multi_nonzero=True
    wrong_path_detected=False; wrong_perm_detected=False; raw_v_diff=False; bad_sub_diff=False
    for oi,(mask,osize) in enumerate(reps):
        U=U_poly(mask,alphas,vs,s1,S); degree_ok &= bool(U) and deg.degree_set(U)==[5]
        rawV=V_poly(mask,vs); badU=U_poly(mask,alphas,vs,s1,S,bad_factor=2)
        pm=mask_perm(mask,CYCLE)
        lane={}
        for name,w in (('W1',W1),('W2',W2),('S5_W1',WP1),('S5_W2',WP2)):
            mm=pm if name.startswith('S5_') else mask
            UU=U_poly(mm,alphas,vs,s1,S)
            a=substitute_multivariate(UU,mm,w); b=route_b(mm,w,qs)
            route_ok &= a==b
            lane[name]={'coefficients':[fq(x) for x in a],'sha256':vec_hash(a),'state':state(a)[0],'first_nonzero_order':state(a)[1],'exact_zero':state(a)[0]=='ZERO'}
        s5w1=tuple(Fraction(x) for x in lane['S5_W1']['coefficients']); s5w2=tuple(Fraction(x) for x in lane['S5_W2']['coefficients'])
        a1=substitute_multivariate(U,mask,W1); a2=substitute_multivariate(U,mask,W2)
        this_s5=(a1==s5w1 and a2==s5w2); s5_ok &= this_s5
        this_witness=state(a1)==state(a2); witness_ok &= this_witness
        zero_found |= state(a1)[0]=='ZERO' or state(a2)[0]=='ZERO'
        raw_v_diff |= substitute_any(rawV,mask,W1,4)!=list(a1[:5])
        bad_sub_diff |= substitute_multivariate(badU,mask,W1)!=a1
        # Wrong corner path: force the first complement edge to scale with t as well.
        comp=next(e for e in range(N) if not ((mask>>e)&1))
        wrongmask=mask|(1<<comp)
        wrong_path_detected |= substitute_multivariate(U,wrongmask,W1)!=a1
        wrong_perm_detected |= substitute_multivariate(U_poly(pm,alphas,vs,s1,S),pm,W1)!=a1
        rows.append({'orbit_index':oi,'mask':mask,'bits':[e for e in range(N) if (mask>>e)&1],'k':mask.bit_count(),'orbit_size':osize,'multivariate_u_sha256':deg.poly_hash(U),'multivariate_coefficient_count':len(U),'lanes':lane,'w1_w2_state_agreement':this_witness,'s5_full_coefficient_covariance':this_s5})
    bad=list(ann_coeff); bad[4]+=1; _,_,_,_,bad_vs,_,_=build_objects(tuple(bad)); bad_vp=deg.vpsi(bad_vs,psi)
    empty=U_poly(0,alphas,vs,s1,S); full=U_poly((1<<N)-1,alphas,vs,s1,S)
    controls={
      'P1_ten_edges':N==10,
      'P1_stabilizer_order12':len(stab)==12,
      'P1_cubic_orbits33':len(horb)==33,
      'P1_annihilator_coefficients33':len(ann_coeff)==33,
      'P2_all_q_degree3':all(q and deg.degree_set(q)==[3] for q in qs),
      'P2_all_v_degree4':all(v and deg.degree_set(v)==[4] for v in vs),
      'P3_psi_125_trees':len(psi)==125 and all(c==1 for c in psi.values()),
      'P3_vpsi_exact_zero':vp=={},
      'P4_subset_orbits34':len(orbits)==34,
      'P4_proper_reps32':len(reps)==32 and sum(s for _,s in reps)==1022,
      'P5_all_multivariate_proper_u_nonzero_degree5':degree_ok,
      'P6_route_a_b_exact_all_w1_w2_s5':route_ok,
      'P7_empty_full_u_zero':empty=={} and full=={},
      'N1_raw_v_rejected':raw_v_diff,
      'N2_bad_subtraction_rejected':bad_sub_diff,
      'N3_altered_annihilator_breaks_vpsi':bad_vp!={},
      'N4_wrong_corner_path_detected':wrong_path_detected,
      'N5_wrong_cycle_weight_transport_detected':wrong_perm_detected,
      'N6_complete_degree5_vector_used':all(len(r['lanes']['W1']['coefficients'])==6 and len(r['lanes']['W2']['coefficients'])==6 for r in rows),
      'N7_fabricated_order_rejected':state((Fraction(0),Fraction(7),Fraction(0),Fraction(3),Fraction(0),Fraction(0)))==('ORDER',1),
      'N8_no_physical_corner_verdict':True,
    }
    valid=all(controls.values())
    if not valid: classification=INVALID; status=INVALID
    elif not s5_ok: classification=S5FAIL; status='PASS_EXACT_SCOPED'
    elif zero_found: classification=ZERO; status='PASS_EXACT_SCOPED'
    elif not witness_ok: classification=NONUNIFORM; status='PASS_EXACT_SCOPED'
    else: classification=PASS; status='PASS_EXACT_SCOPED'
    hist=defaultdict(int)
    for r in rows:
        o=r['lanes']['W1']['first_nonzero_order']; hist[str(o)]+=1
    out={'gate':'K5_PROJECTIVE_NORMAL_32ORBIT_EXACT_CORNER_ORDER','prereg_commit':PREREG,'status':status,'classification':classification,'weights':{'W1':list(W1),'W2':list(W2),'S5_W1':list(WP1),'S5_W2':list(WP2)},'cycle':list(CYCLE),'degree_ceiling':5,'controls':controls,'summary':{'proper_orbits':32,'route_a_b_exact':route_ok,'s5_full_coefficient_covariance_all':s5_ok,'w1_w2_state_agreement_all':witness_ok,'frozen_path_zero_found':zero_found,'order_histogram_w1':dict(sorted(hist.items(),key=lambda z:int(z[0]))),'distinct_orders_w1':sorted({r['lanes']['W1']['first_nonzero_order'] for r in rows})},'orbit_rows':rows,'physical_corner_finiteness_verdict':None,'global_stokes_ibp_verdict':None,'integrated_period_verdict':None,'finite_part_selector':None,'regulator_independence':None}
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args(); p=Path(args.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print('CLASSIFICATION=',classification); print('SUMMARY=',json.dumps(out['summary'],sort_keys=True)); print('CONTROLS=',json.dumps(controls,sort_keys=True))
    if not valid: raise SystemExit(2)
if __name__=='__main__': main()
