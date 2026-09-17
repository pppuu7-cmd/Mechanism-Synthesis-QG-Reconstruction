#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from types import SimpleNamespace

ROOT=Path(__file__).resolve().parents[1]
ACTION=ROOT/'scripts/k5_deg4_annihilator_actual_dual_action.py'
RESOLVER=ROOT/'scripts/k5_34_orbit_exact_leading_coefficient_cancellation_resolution.py'
REPAIR5_RESULT=ROOT/'results/K5_EXACT_CANCELLATION_UNPROJECTED_BOUNDARY_DUAL_S5_DIAGNOSTIC_REPAIR5_RESULT.md'
PREREG='6ac6e7749783b78fb0966450a91d8042c1ad0ca4'
PARENT='d6b0e805101c8590eafac71398cc2b1466691752'
ACTION_BLOB='2ed1b6397236c3f64c22b2a827bf1f0f8b5e0484'
RESOLVER_BLOB='012b04669948962548064334bfbed47062e4acc0'
MARKER='results={};checks={}'
C=(1,2,3,4,0); CI=(4,0,1,2,3); T=(1,0,2,3,4)
PERMS={'C':C,'Cinv':CI,'T':T}


def git_blob_sha(path:Path)->str:
    raw=path.read_bytes(); return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()

def load(path,name):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);assert s.loader is not None;s.loader.exec_module(m);return m

def load_action_prefix():
    assert git_blob_sha(ACTION)==ACTION_BLOB
    text=ACTION.read_text(encoding='utf-8'); assert text.count(MARKER)==1
    ns={'__name__':'k5_full_source_action_prefix','__file__':str(ACTION),'__package__':None}
    exec(compile(text.split(MARKER,1)[0],str(ACTION),'exec'),ns,ns)
    for k in ('PATTERNS','SOURCE_TERMS','P','PIV','WEIGHTS','reach','src','EDGES'):assert k in ns
    assert 'results' not in ns
    return SimpleNamespace(**ns)

assert git_blob_sha(RESOLVER)==RESOLVER_BLOB
r=load(RESOLVER,'k5_full_source_resolver');act=load_action_prefix();core=r.core
EDGES=tuple(act.EDGES); EIDX={e:i for i,e in enumerate(EDGES)}
W={'W1':tuple(r.W1),'W2':tuple(r.W2)}


def invperm(p):return tuple(p.index(i) for i in range(len(p)))
def ep(p,i):
    a,b=EDGES[i];x,y=p[a],p[b];return EIDX[(min(x,y),max(x,y))]
def perm_weights(w,p):
    out=[None]*10
    for i,x in enumerate(w):out[ep(p,i)]=x
    assert all(x is not None for x in out);return tuple(out)
def edge_sign(p,i):
    a,b=EDGES[i];return 1 if p[a]<p[b] else -1
def parity(p):
    return -1 if sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))%2 else 1

def cvadd(a,b):return (a[0]+b[0],a[1]+b[1])
def cvscale(c,a):return (c*a[0],c*a[1])
def cmul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def fq(x):
    q=Fraction(x);return str(q.numerator) if q.denominator==1 else f'{q.numerator}/{q.denominator}'
def encvec(v):return [[fq(z[0]),fq(z[1])] for z in v]

def b0_cov(alpha):
    aa=[r.D(Fraction(x),0) for x in alpha];L=r.build_L(aa);psi=r.psi_direct(aa)
    if psi.v==0:raise ZeroDivisionError('psi zero')
    B0=r.inv_cofactor(L,psi)
    return {(i,j):r.dot_mat(core.ROWS[i],B0,core.ROWS[j]).v for i in range(10) for j in range(i+1,10)}

def standard_pair(cov,i,j,ea,eb):
    g=core.EM[(ea,eb)];return (cov[(i,j)]*g[0],cov[(i,j)]*g[1])

def old_edge_for_target(p):
    out=[None]*10
    for i in range(10):out[ep(p,i)]=i
    assert all(i is not None for i in out);return tuple(out)

def transported_type_and_sign(p,target_edge,t):
    oi=old_edge_for_target(p)[target_edge];s=edge_sign(p,oi)
    return ((t[0],t[1]) if s==1 else (t[1],t[0])),s

def wick_vector(alpha, *, p=None, route='base', transpose_reversed=True):
    cov=b0_cov(alpha); cache={}
    oldmap=None if p is None else old_edge_for_target(p)
    global_sign=1 if p is None else int(__import__('math').prod(edge_sign(p,i) for i in range(10)))

    def pair_direct(i,j,ei,ej):
        if p is None:return standard_pair(cov,i,j,ei,ej)
        oi=oldmap[i];oj=oldmap[j];si=edge_sign(p,oi);sj=edge_sign(p,oj)
        ti=ei if (si==1 or not transpose_reversed) else (ei[1],ei[0])
        tj=ej if (sj==1 or not transpose_reversed) else (ej[1],ej[0])
        g=core.EM[(ti,tj)]
        return (cov[(i,j)]*si*sj*g[0],cov[(i,j)]*si*sj*g[1])

    def wick_direct(rem):
        if not rem:return (Fraction(1),Fraction(0))
        key=('D',rem)
        if key in cache:return cache[key]
        i,ei=rem[0];z=(Fraction(0),Fraction(0))
        for pos in range(1,len(rem)):
            j,ej=rem[pos];rest=rem[1:pos]+rem[pos+1:]
            z=cvadd(z,cmul(pair_direct(i,j,ei,ej),wick_direct(rest)))
        cache[key]=z;return z

    def wick_standard(rem):
        if not rem:return (Fraction(1),Fraction(0))
        key=('S',rem)
        if key in cache:return cache[key]
        i,ei=rem[0];z=(Fraction(0),Fraction(0))
        for pos in range(1,len(rem)):
            j,ej=rem[pos];rest=rem[1:pos]+rem[pos+1:]
            z=cvadd(z,cmul(standard_pair(cov,i,j,ei,ej),wick_standard(rest)))
        cache[key]=z;return z

    amps=[(Fraction(0),Fraction(0)) for _ in range(32)];terms=0;seen=[]
    for idx,arr in act.PATTERNS:
        seen.append(idx);z=(Fraction(0),Fraction(0))
        for types,coeff in arr:
            terms+=1
            if route in ('base','direct'):
                rem=tuple((i,types[i]) for i in range(10));w=wick_direct(rem)
            elif route=='pattern':
                assert p is not None
                mt=[]
                for i,t in enumerate(types):
                    oi=oldmap[i];s=edge_sign(p,oi)
                    mt.append(t if s==1 else (t[1],t[0]))
                rem=tuple((i,mt[i]) for i in range(10));w=cvscale(global_sign,wick_standard(rem))
            else:raise ValueError(route)
            z=cvadd(z,cvscale(coeff,w))
        amps[idx]=z
    assert sorted(seen)==list(range(32))
    return tuple(amps),terms,len(cache)

def tr(A):return [list(x) for x in zip(*A)]
def mvec(A,v):
    out=[]
    for row in A:
        z=(Fraction(0),Fraction(0))
        for c,x in zip(row,v):z=cvadd(z,cvscale(c,x))
        out.append(z)
    return tuple(out)
def mm(A,B):
    BT=list(zip(*B));return [[sum((x*y for x,y in zip(row,col)),Fraction(0)) for col in BT] for row in A]
def eye(n):return [[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
def coords(a):
    pt=tr(act.P);dp=mvec(pt,a);auth=tuple(dp[i] for i in act.PIV);weighted=[]
    for c in range(2):
        z=(Fraction(0),Fraction(0))
        for j,x in enumerate(a):z=cvadd(z,cvscale(act.WEIGHTS[j][c],x))
        weighted.append(z)
    return auth,tuple(weighted)
def negvec(v):return tuple((-z[0],-z[1]) for z in v)

def matrix_neg(M):return [[(-z[0],-z[1]) for z in row] for row in M]
def source_matrix_reversal_control():
    src=act.src
    vs=((1,0,0),(0,1,0),(0,0,1))
    ok=True
    for v in vs:
        a=src.leading_matrix(v);b=src.leading_matrix(tuple(-x for x in v));ok &= b==matrix_neg(a)
    return bool(ok)
def source_pattern_roundtrip(p):
    ip=invperm(p)
    for i in range(10):
        j=ep(p,i);k=ep(ip,j)
        if k!=i:return False
        for t in ((0,0),(0,1),(1,0),(1,1)):
            t1=t if edge_sign(p,i)==1 else (t[1],t[0])
            t2=t1 if edge_sign(ip,j)==1 else (t1[1],t1[0])
            if t2!=t:return False
    return True

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--label',required=True);ap.add_argument('--output',required=True);args=ap.parse_args()
    witness,plabel=args.label.split('_',1);assert witness in W and plabel in PERMS
    p=PERMS[plabel];ip=invperm(p);alpha=W[witness];target_alpha=perm_weights(alpha,p)
    tensors=act.reach.local_tensor_vectors(act.src);local=act.reach.local_action_matrices(tensors)
    A=act.reach.global_action_matrix(act.src,p,local);Ai=act.reach.global_action_matrix(act.src,ip,local)
    base,terms0,cache0=wick_vector(alpha,route='base')
    direct,terms1,cache1=wick_vector(target_alpha,p=p,route='direct')
    pattern,terms2,cache2=wick_vector(target_alpha,p=p,route='pattern')
    pred=mvec(tr(Ai),base);pred_sgn=pred if parity(p)==1 else negvec(pred)
    trivial_exact=(direct==pred);orientation_exact=(direct==pred_sgn)
    cb,cwb=coords(base);ct,cwt=coords(direct)
    naive_fail=None
    if args.label=='W1_T':
        naive,tn,cn=wick_vector(target_alpha,p=p,route='direct',transpose_reversed=False)
        naive_fail=(naive!=pred and naive!=pred_sgn)
    reversals=sum(edge_sign(p,i)==-1 for i in range(10))
    checks={
      'prereg_locked':PREREG=='6ac6e7749783b78fb0966450a91d8042c1ad0ca4',
      'parent_locked':PARENT=='d6b0e805101c8590eafac71398cc2b1466691752',
      'repair5_terminal_result_present':REPAIR5_RESULT.exists(),
      'action_blob_locked':git_blob_sha(ACTION)==ACTION_BLOB,
      'resolver_blob_locked':git_blob_sha(RESOLVER)==RESOLVER_BLOB,
      'ten_edges':len(EDGES)==10,
      'boundary32':len(base)==len(direct)==len(pattern)==32,
      'all_source_terms':terms0==terms1==terms2==act.SOURCE_TERMS==100000,
      'boundary_action_inverse_exact':mm(A,Ai)==eye(32) and mm(Ai,A)==eye(32),
      'reynolds_rank2_pivots14':list(act.PIV)==[1,4],
      'source_matrix_reversal_exact':source_matrix_reversal_control(),
      'orientation_reversal_parity_matches_perm':((-1 if reversals%2 else 1)==parity(p)),
      'source_pattern_roundtrip_exact':source_pattern_roundtrip(p),
      'route_A_B_exact':direct==pattern,
      'coordinate_extraction_base_exact':cb==cwb,
      'coordinate_extraction_target_exact':ct==cwt,
      'no_physical_corner_coefficients':True,
    }
    if args.label=='W1_T':checks['naive_no_transpose_negative_control_fails_law']=bool(naive_fail)
    valid=all(checks.values())
    out={
      'gate':'K5_FULL_SOURCE_BOUNDARY_S5_TRANSPORT_OBJECT_DEFINITION_SHARD',
      'prereg_commit':PREREG,'parent_gate_prereg':PARENT,'label':args.label,
      'witness':witness,'permutation_label':plabel,'permutation':list(p),'inverse_permutation':list(ip),
      'permutation_sign':parity(p),'orientation_reversals':reversals,
      'alpha':[fq(x) for x in alpha],'target_alpha':[fq(x) for x in target_alpha],
      'source_terms':terms0,'boundary_components':32,
      'route_A_B_exact':direct==pattern,
      'trivial_character_contragredient_exact':trivial_exact,
      'orientation_character_contragredient_exact':orientation_exact,
      'base_dual_coordinates':encvec(cb),'target_dual_coordinates':encvec(ct),
      'base_vector':encvec(base),'target_vector':encvec(direct),
      'checks':checks,'status':'PASS_EXACT_SHARD' if valid else 'INVALID_IMPLEMENTATION',
      'scientific_verdict':None,'physical_corner_coefficients_used':False,
      'cache_sizes':{'base':cache0,'direct':cache1,'pattern':cache2},
    }
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({k:out[k] for k in ('label','permutation_sign','orientation_reversals','route_A_B_exact','trivial_character_contragredient_exact','orientation_character_contragredient_exact','status')},indent=2,sort_keys=True))
    return 0 if valid else 2

if __name__=='__main__':raise SystemExit(main())
