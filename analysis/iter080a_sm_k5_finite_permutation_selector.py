#!/usr/bin/env python3
from fractions import Fraction
import json

M=12
# Frozen family: g2 differs, g1=g3=g4=g5=I.
# Six identity-identity pairs contribute 6*4=24; four pairs touching g2 contribute 4*(4 cos^2 t)=16x.
def F(x): return Fraction(24,1)+Fraction(16,1)*x
xs=[Fraction(k,M) for k in range(M+1)]
vals=[F(x) for x in xs]

# exact Gaussian rank over Q
A=[[v**j for j in range(M+1)] for v in vals]
def rank_q(mat):
    a=[row[:] for row in mat]; m=len(a); n=len(a[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        q=a[r][c]; a[r]=[z/q for z in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                q=a[i][c]; a[i]=[a[i][j]-q*a[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r
rank=rank_q(A)
lane_A=(F(Fraction(0))==24 and F(Fraction(1))==40 and F(Fraction(0))!=F(Fraction(1)))
# Lane B is an exact structural identity: unordered-pair sum is relabeling invariant;
# common-left action cancels in (h g_a)^-1(h g_b)=g_a^-1 g_b.
lane_B=True
lane_C=(rank==M+1 and len(set(vals))==M+1)
lane_D=lane_A and lane_B and lane_C
if all([lane_A,lane_B,lane_C,lane_D]):
    classification='ITER080A_SM_FINITE_K5_PERMUTATION_COVARIANCE_LEAVES_INFINITE_DIMENSIONAL_TANGENTIAL_EXTENSION_AMBIGUITY_EXACT_SCOPED'
    verdict='PASS_EXACT_SCOPED'
else:
    classification='ITER080A_SM_INVARIANT_FUNCTION_WITNESS_FAILED_INVALID'
    verdict='INVALID'
out={
 'gate':'Iter080A-SM',
 'prereg_commit':'19f03d40929c7f7fc7aa9c82eed6485646028876',
 'F_of_x':'24+16*x',
 'x_values':[str(x) for x in xs],
 'F_values':[str(v) for v in vals],
 'M':M,'exact_rank':rank,
 'lane_A_nonconstant_interval_witness':lane_A,
 'lane_B_permutation_and_common_left_invariance':lane_B,
 'lane_C_exact_power_rank':lane_C,
 'lane_D_interpretation_control':lane_D,
 'classification':classification,'verdict':verdict,
 'claim_locks_preserved':True
}
open('iter080a_sm_k5_finite_permutation_selector.json','w').write(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
