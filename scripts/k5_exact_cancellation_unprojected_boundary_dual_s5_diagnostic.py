#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
RESOLVER=ROOT/'scripts/k5_34_orbit_exact_leading_coefficient_cancellation_resolution.py'
ACTION=ROOT/'scripts/k5_deg4_annihilator_actual_dual_action.py'
PREREG='41f26f8e314f4ab1213fe6a681b69d2c87e00d68'
CYCLE=(1,2,3,4,0)

def load(path,name):
    s=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(s); assert s.loader is not None; s.loader.exec_module(m); return m
r=load(RESOLVER,'dualdiag_resolver'); act=load(ACTION,'dualdiag_action'); core=r.core; reach=act.reach
WITNESSES={'W1':tuple(r.W1),'W2':tuple(r.W2)}

def invperm(p): return tuple(p.index(i) for i in range(len(p)))
def tr(A): return [list(x) for x in zip(*A)]
def mm(A,B):
    BT=list(zip(*B)); return [[sum((x*y for x,y in zip(row,col)),Fraction(0)) for col in BT] for row in A]
def eye(n): return [[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
def cvadd(a,b): return (a[0]+b[0],a[1]+b[1])
def cvscale(c,a): return (c*a[0],c*a[1])
def cmul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def mvec(A,v):
    out=[]
    for row in A:
        z=(Fraction(0),Fraction(0))
        for c,x in zip(row,v): z=cvadd(z,cvscale(c,x))
        out.append(z)
    return tuple(out)

def b0_cov(alpha):
    aa=[r.D(Fraction(x),0) for x in alpha]; L=r.build_L(aa); psi=r.psi_direct(aa)
    if psi.v==0: raise ZeroDivisionError('psi zero')
    B0=r.inv_cofactor(L,psi)
    return {(i,j):r.dot_mat(core.ROWS[i],B0,core.ROWS[j]).v for i in range(10) for j in range(i+1,10)}

def unprojected(alpha):
    cov=b0_cov(alpha); pair={}
    for i in range(10):
        for j in range(i+1,10):
            for ea in core.ENTRY:
                for eb in core.ENTRY:
                    g=core.EM[(ea,eb)]
                    pair[(i,j,ea,eb)]=(cov[(i,j)]*g[0],cov[(i,j)]*g[1])
    cache={}
    def wick(rem):
        if not rem:return (Fraction(1),Fraction(0))
        if rem in cache:return cache[rem]
        i,ei=rem[0]; total=(Fraction(0),Fraction(0))
        for pos in range(1,len(rem)):
            j,ej=rem[pos]; rest=rem[1:pos]+rem[pos+1:]
            total=cvadd(total,cmul(pair[(i,j,ei,ej)],wick(rest)))
        cache[rem]=total; return total
    amps=[(Fraction(0),Fraction(0)) for _ in range(32)]; terms=0
    for idx,arr in act.PATTERNS:
        z=(Fraction(0),Fraction(0))
        for types,coeff in arr:
            terms+=1; rem=tuple((i,types[i]) for i in range(10)); z=cvadd(z,cvscale(coeff,wick(rem)))
        amps[idx]=z
    return tuple(amps),terms,len(cache)

def coords(a):
    P=act.P; piv=tuple(act.PIV); pt=tr(P); dp=mvec(pt,a)
    auth=tuple(dp[i] for i in piv)
    weighted=[]
    for c in range(2):
        z=(Fraction(0),Fraction(0))
        for j,x in enumerate(a): z=cvadd(z,cvscale(act.WEIGHTS[j][c],x))
        weighted.append(z)
    return auth,tuple(weighted)

def digest_vec(v): return [[str(x[0]),str(x[1])] for x in v]

def lane(alpha,p,A,Ai):
    ap=tuple(core.perm_weights(alpha,p)); a,terms,cache=unprojected(alpha); b,terms2,cache2=unprojected(ap)
    laws={
      'A':mvec(A,a),
      'A_inverse':mvec(Ai,a),
      'A_transpose':mvec(tr(A),a),
      'A_inverse_transpose':mvec(tr(Ai),a),
    }
    exact={k:(v==b) for k,v in laws.items()}
    ca,cw=coords(a); cb,cbw=coords(b)
    return {'permuted_alpha':[str(x) for x in ap],'source_terms':terms,'target_source_terms':terms2,'wick_cache':cache,'target_wick_cache':cache2,
            'laws_exact':exact,'exact_laws':[k for k,v in exact.items() if v],
            'dual_coordinates_base':digest_vec(ca),'dual_coordinates_target':digest_vec(cb),'dual_coordinates_invariant':ca==cb,
            'weighted_coordinates_equal_authoritative_base':cw==ca,'weighted_coordinates_equal_authoritative_target':cbw==cb}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args()
    tensors=reach.local_tensor_vectors(act.src); local=reach.local_action_matrices(tensors)
    A=reach.global_action_matrix(act.src,CYCLE,local); ip=invperm(CYCLE); Ai=reach.global_action_matrix(act.src,ip,local)
    checks={'local_actions_24':len(local)==24,'A_inverse_exact':mm(A,Ai)==eye(32) and mm(Ai,A)==eye(32),'reynolds_rank_two':len(act.PIV)==2 and list(act.PIV)==[1,4],'source_terms_100000':act.SOURCE_TERMS==100000}
    lanes={}
    for name,a in WITNESSES.items():
        lanes[name]={'cycle':lane(a,CYCLE,A,Ai),'inverse':lane(a,ip,Ai,A)}
    allentries=[lanes[n][d] for n in lanes for d in ('cycle','inverse')]
    sourcecoverage=all(x['source_terms']==100000 and x['target_source_terms']==100000 for x in allentries)
    checks['complete_source_coverage']=sourcecoverage
    valid=all(checks.values())
    lawsets=[tuple(x['exact_laws']) for x in allentries]
    unique_consistent=(len(set(lawsets))==1 and len(lawsets[0])==1)
    law=lawsets[0][0] if unique_consistent else None
    coordextract=all(x['weighted_coordinates_equal_authoritative_base'] and x['weighted_coordinates_equal_authoritative_target'] for x in allentries)
    coordinv=all(x['dual_coordinates_invariant'] for x in allentries)
    if not valid:
        cls='INVALID_IMPLEMENTATION'
    elif law=='A_inverse_transpose' and coordinv and coordextract:
        cls='BOUNDARY_DUAL_CONTRAGREDIENT_S5_EXACT'
    elif law=='A_inverse_transpose' and not coordextract:
        cls='DUAL_COORDINATE_EXTRACTION_MISMATCH_EXACT'
    elif unique_consistent:
        cls='BOUNDARY_S5_OTHER_REPRESENTATION_EXACT'
    else:
        cls='BOUNDARY_S5_REPRESENTATION_UNRESOLVED_EXACT'
    out={'gate':'K5_EXACT_CANCELLATION_UNPROJECTED_BOUNDARY_DUAL_S5_DIAGNOSTIC','prereg_commit':PREREG,'cycle':list(CYCLE),'inverse_cycle':list(ip),
         'checks':checks,'lanes':lanes,'unique_consistent_law':law,'dual_coordinates_invariant_all':coordinv,'coordinate_extraction_exact_all':coordextract,
         'classification':cls,'physical_corner_coefficients_used':False,'scientific_verdict':None}
    p=Path(args.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True)); return 2 if cls=='INVALID_IMPLEMENTATION' else 0
if __name__=='__main__': raise SystemExit(main())
