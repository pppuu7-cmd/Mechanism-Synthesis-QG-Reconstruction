#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, itertools, json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SRC_PATH=ROOT/'distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py'
REACH_PATH=ROOT/'scripts/k5_order8_invariant_dual_projective_ibp_reachability.py'
PREREG='86438c789eac23eabcb68ff6984ccbcc6fc3853b'
CYCLE=(1,2,3,4,0)


def load(path,name):
    s=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(s); assert s.loader is not None; s.loader.exec_module(m); return m

def matmul(A,B):
    BT=list(zip(*B)); return [[sum((x*y for x,y in zip(r,c)),Fraction(0)) for c in BT] for r in A]
def transpose(A): return [list(x) for x in zip(*A)]
def eye(n): return [[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
def inv(A):
    n=len(A); a=[[Fraction(x) for x in A[i]]+eye(n)[i] for i in range(n)]
    for c in range(n):
        p=next((r for r in range(c,n) if a[r][c]),None)
        if p is None: raise ValueError('singular')
        a[c],a[p]=a[p],a[c]; z=a[c][c]; a[c]=[x/z for x in a[c]]
        for r in range(n):
            if r!=c and a[r][c]:
                z=a[r][c]; a[r]=[x-z*y for x,y in zip(a[r],a[c])]
    return [r[n:] for r in a]
def fq(x):
    x=Fraction(x); return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def eq(A,B): return A==B

def solve_transport(W,Y,piv=(1,4)):
    R=[[W[piv[i]][j] for j in range(2)] for i in range(2)]
    Ri=inv(R)
    Yp=[[Y[piv[i]][j] for j in range(2)] for i in range(2)]
    T=matmul(Ri,Yp)
    ok=matmul(W,T)==Y
    return T,ok

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args()
    src=load(SRC_PATH,'s5diag_src'); reach=load(REACH_PATH,'s5diag_reach')
    tensors=reach.local_tensor_vectors(src); local=reach.local_action_matrices(tensors)
    As=[]; P=[[Fraction(0) for _ in range(32)] for _ in range(32)]
    for sig in itertools.permutations(range(5)):
        A=reach.global_action_matrix(src,sig,local); As.append(A)
        for i in range(32):
            for j in range(32): P[i][j]+=A[i][j]/120
    rank,RR,piv=reach.rref_rank(P)
    A=reach.global_action_matrix(src,CYCLE,local)
    invcycle=tuple(CYCLE.index(i) for i in range(5))
    Ai=reach.global_action_matrix(src,invcycle,local)
    W=[[P[i][piv[c]] for c in range(2)] for i in range(32)]
    targets={
      'vector':matmul(A,W),
      'covector':matmul(transpose(A),W),
      'inverse_covector':matmul(transpose(Ai),W),
    }
    trans={}
    for name,Y in targets.items():
        T,ok=solve_transport(W,Y,tuple(piv))
        trans[name]={'column_space_exact':ok,'matrix':[[fq(x) for x in r] for r in T],'identity':ok and T==eye(2)}
    checks={
      'local_actions_24':len(local)==24,
      'reynolds_rank_two':rank==2,
      'pivots_1_4':piv==[1,4],
      'A_inverse_exact':matmul(A,Ai)==eye(32) and matmul(Ai,A)==eye(32),
      'reynolds_left_invariant':matmul(A,P)==P,
      'reynolds_right_invariant':matmul(P,A)==P,
      'weight_columns_vector_identity':targets['vector']==W,
    }
    if not all(checks.values()): cls='INVALID_IMPLEMENTATION'
    elif trans['vector']['identity']:
        cls='S5_SOURCE_TRANSPORT_IDENTITY_CONFIRMED'
    elif trans['vector']['column_space_exact']:
        cls='S5_SOURCE_TRANSPORT_NONTRIVIAL_2X2_EXACT'
    else:
        cls='S5_SOURCE_TRANSPORT_CURRENT_LANE_INVALID'
    out={'gate':'K5_EXACT_CANCELLATION_S5_SOURCE_TRANSPORT_DIAGNOSTIC','prereg_commit':PREREG,'cycle':list(CYCLE),'inverse_cycle':list(invcycle),'rank':rank,'pivots':piv,'checks':checks,'transports':trans,'classification':cls,'physical_corner_coefficients_used_for_fit':False,'scientific_verdict':None}
    Path(args.output).parent.mkdir(parents=True,exist_ok=True); Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if cls!='INVALID_IMPLEMENTATION' else 2

if __name__=='__main__': raise SystemExit(main())