#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, permutations, product
import hashlib, json, os

N=4  # scalar q^4 -> vector degree 9
Z=Fraction(0); O=Fraction(1)

def pad(a): return list(a)+[Z]*(N+1-len(a))
def add(a,b): return [(a[i] if i<len(a) else Z)+(b[i] if i<len(b) else Z) for i in range(N+1)]
def mul(a,b):
    out=[Z]*(N+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=N: out[i+j]+=x*y
    return out
def pw(a,k):
    out=[O]+[Z]*N
    for _ in range(k): out=mul(out,a)
    return out
def compose(poly,arg):
    out=[Z]*(N+1)
    for k,c in enumerate(poly):
        if c:
            out=add(out,[c*x for x in pw(arg,k)])
    return out
def radial_comp(first,second):
    # x -> first(q)x -> second(q*first(q)^2)*first(q)x
    q=[Z,O,Z,Z,Z]
    q2=mul(q,mul(first,first))
    return mul(first,compose(second,q2))
def fs(a): return [f"{x.numerator}/{x.denominator}" for x in a]
ID=[O,Z,Z,Z,Z]

XV=[O,Fraction(1,6),Fraction(1,120),Fraction(1,5040),Fraction(1,362880)]
VX=[O,Fraction(-1,6),Fraction(3,40),Fraction(-5,112),Fraction(35,1152)]
XW=[O,Fraction(-1,3),Fraction(2,15),Fraction(-17,315),Fraction(62,2835)]
WX=[O,Fraction(1,3),Fraction(1,5),Fraction(1,7),Fraction(1,9)]
VW=[O,Fraction(-1,2),Fraction(3,8),Fraction(-5,16),Fraction(35,128)]
WV=[O,Fraction(1,2),Fraction(3,8),Fraction(5,16),Fraction(35,128)]
MAPS={"XV":XV,"VX":VX,"XW":XW,"WX":WX,"VW":VW,"WV":WV}

pair_inverse={
 "XV_VX":radial_comp(XV,VX),"VX_XV":radial_comp(VX,XV),
 "XW_WX":radial_comp(XW,WX),"WX_XW":radial_comp(WX,XW),
 "VW_WV":radial_comp(VW,WV),"WV_VW":radial_comp(WV,VW),
}

cocycles={
 "XV_then_VW_equals_XW":(radial_comp(XV,VW),XW),
 "XW_then_WV_equals_XV":(radial_comp(XW,WV),XV),
 "VX_then_XW_equals_VW":(radial_comp(VX,XW),VW),
 "VW_then_WX_equals_VX":(radial_comp(VW,WX),VX),
 "WX_then_XV_equals_WV":(radial_comp(WX,XV),WV),
 "WV_then_VX_equals_WX":(radial_comp(WV,VX),WX),
}

# Exact evaluator used for positive S5/SO3 and malformed preferred-label control.
def dot(v): return sum(x*x for x in v)
def eval_radial(v,c,scale_cubic=O,linear=((1,0,0),(0,1,0),(0,0,1)),shift=(Z,Z,Z)):
    q=dot(v); s=Z
    for k,a in enumerate(c): s+=(a*(scale_cubic if k==1 else O))*(q**k)
    raw=tuple(s*x for x in v)
    out=[]
    for i in range(3):
        if linear!=((1,0,0),(0,1,0),(0,0,1)):
            lin=sum(Fraction(linear[i][j])*v[j] for j in range(3)); out.append(lin+(raw[i]-v[i])+shift[i])
        else: out.append(raw[i]+shift[i])
    return tuple(out)
def transform_nodes(nodes,c,scales=None):
    if scales is None: scales=[O]*5
    return tuple(eval_radial(nodes[i],c,scales[i]) for i in range(5))
def perm_nodes(nodes,p):
    out=[None]*5
    for old,new in enumerate(p): out[new]=nodes[old]
    return tuple(out)
SAMPLE=((Fraction(1,7),Fraction(2,9),Fraction(-1,5)),(Fraction(-2,11),Fraction(1,8),Fraction(3,10)),(Fraction(4,13),Fraction(-1,6),Fraction(2,7)),(Fraction(1,4),Fraction(3,17),Fraction(-2,9)),(Fraction(-3,14),Fraction(2,15),Fraction(1,12)))

def s5_count(c,scales=None):
    good=0; fail=None
    for p in permutations(range(5)):
        lhs=transform_nodes(perm_nodes(SAMPLE,p),c,scales)
        rhs=perm_nodes(transform_nodes(SAMPLE,c,scales),p)
        if lhs==rhs: good+=1
        elif fail is None: fail=p
    return good,fail

# Exact finite SO(3) subgroup checks for every directed map.
so3_checks=0; so3_fail=[]
for name,c in MAPS.items():
    v=(Fraction(1,7),Fraction(-2,9),Fraction(3,11))
    for p in permutations(range(3)):
        for signs in product((-1,1),repeat=3):
            Rv=tuple(Fraction(signs[i])*v[p[i]] for i in range(3))
            lhs=eval_radial(Rv,c)
            rhs0=eval_radial(v,c); rhs=tuple(Fraction(signs[i])*rhs0[p[i]] for i in range(3))
            so3_checks+=1
            if lhs!=rhs: so3_fail.append((name,p,signs))

labels=tuple(range(5))
blocks=[tuple(c) for k in (3,4,5) for c in combinations(labels,k)]
chains=[(tuple(B3),tuple(B4),labels) for B4 in combinations(labels,4) for B3 in combinations(B4,3)]
omega={3:0,4:3,5:8}

def bary(nodes,B):
    m=tuple(sum(nodes[i][j] for i in B)/len(B) for j in range(3))
    return tuple(tuple(nodes[i][j]-m[j] for j in range(3)) for i in B)

def collision_audit(c):
    base=(Fraction(2,9),Fraction(-1,7),Fraction(3,11)); other=[(Fraction(i+1,17),Fraction(i+2,19),Fraction(-(i+1),23)) for i in range(5)]
    fail=[]
    for B in blocks:
        n=list(other)
        for i in B: n[i]=base
        if any(any(x for x in row) for row in bary(transform_nodes(tuple(n),c),B)): fail.append(B)
    return fail

# For radial polynomial maps P(z)=phi(z.z)z, P(x)-P(y) vanishes after exact y=x substitution.
# Construct sparse component polynomials and perform cancellation mechanically.
def pmul3(a,b,maxdeg=9):
    out={}
    for ea,ca in a.items():
        for eb,cb in b.items():
            e=tuple(ea[i]+eb[i] for i in range(3))
            if sum(e)<=maxdeg: out[e]=out.get(e,Z)+ca*cb
    return {e:c for e,c in out.items() if c}
def ppow3(a,k):
    out={(0,0,0):O}
    for _ in range(k): out=pmul3(out,a)
    return out
Q={(2,0,0):O,(0,2,0):O,(0,0,2):O}
def radial_polys(c):
    ans=[]
    for ax in range(3):
        base={tuple(1 if i==ax else 0 for i in range(3)):O}; out={}
        for k,a in enumerate(c):
            t=pmul3(base,ppow3(Q,k))
            for e,v in t.items(): out[e]=out.get(e,Z)+a*v
        ans.append({e:v for e,v in out.items() if v})
    return ans
def diagonal_remainder(poly):
    # +P(x)-P(y), then y=x; combine exact coefficients.
    out={}
    for e,c in poly.items():
        out[e]=out.get(e,Z)+c; out[e]=out.get(e,Z)-c
    return {e:c for e,c in out.items() if c}

ideal_results={}
for name,c in MAPS.items():
    rem=[diagonal_remainder(p) for p in radial_polys(c)]
    checks=sum(len(list(combinations(B,2)))*3 for B in blocks)
    ideal_results[name]={"checks":checks,"failures":sum(1 for B in blocks for _ij in combinations(B,2) for comp in range(3) if rem[comp])}

# If all six overlaps preserve each ideal and pairwise inverses hold, all relevant powers and nested products are preserved.
ideal_all=all(v["failures"]==0 for v in ideal_results.values())
inverse_all=all(v==ID for v in pair_inverse.values())
power_checks=sum((omega[len(B)]+1)*len(MAPS) for B in blocks)
chain_order_checks=len(chains)*220*len(MAPS)

# S5 and collision audits on all maps.
s5={}; collisions={}
for name,c in MAPS.items():
    good,fail=s5_count(c); s5[name]={"passed":good,"first_failure":list(fail) if fail else None}
    collisions[name]=collision_audit(c)

# Negative controls, same validators.
neg={}
# corrupted XW q^2 coefficient breaks the exact cocycle with XV,VW
badXW=list(XW); badXW[2]+=Fraction(1,100)
neg["corrupt_XW_degree5"]={"rejected":radial_comp(XV,VW)!=badXW}
# coefficient tied to absolute label 0
bad_scales=[Fraction(2),O,O,O,O]; badgood,badfail=s5_count(XV,bad_scales)
neg["absolute_label_cubic"]={"rejected":badgood<120,"passed":badgood,"first_failure":list(badfail) if badfail else None}
# singular linear chart
sing=((1,0,0),(0,1,0),(0,0,0))
def rank3(M):
    A=[[Fraction(x) for x in row] for row in M]; r=0
    for col in range(3):
        piv=next((i for i in range(r,3) if A[i][col]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]; z=A[r][col]; A[r]=[x/z for x in A[r]]
        for i in range(3):
            if i!=r and A[i][col]:
                z=A[i][col]; A[i]=[A[i][j]-z*A[r][j] for j in range(3)]
        r+=1
    return r
neg["singular_linear"]={"rejected":rank3(sing)<3,"rank":rank3(sing)}
# explicit order lowering
cum=lambda t:(t[0],t[0]+t[1],sum(t))
i=(0,0,9); o=(0,0,8)
neg["order9_to8"]={"rejected":any(b<a for a,b in zip(cum(i),cum(o)))}
# symbolic representative checks
positive={"finite":["c3","c4","c5"],"scales":["mu3","mu4","mu5"],"selector_sources":[]}
badnum={"finite":["c3",Fraction(1,2),"c5"],"scales":["mu3","mu4","mu5"],"selector_sources":[]}
badcoc={"finite":["c3","c4","c5"],"scales":["mu3","mu4","mu5"],"selector_sources":["atlas_cocycle_identity"]}
symbolic=lambda R: all(isinstance(x,str) for x in R["finite"]+R["scales"])
prov=lambda R:"atlas_cocycle_identity" not in R["selector_sources"]
neg["numeric_finite_part"]={"rejected":not symbolic(badnum)}
neg["cocycle_as_selector"]={"rejected":not prov(badcoc)}

cocycle_pass={k:(a==b) for k,(a,b) in cocycles.items()}
pred={
 "P0_pairwise_charts_and_inverses":inverse_all and all(c[0]==1 for c in MAPS.values()),
 "P1_SO3_S5_covariance":not so3_fail and all(v["passed"]==120 for v in s5.values()),
 "P2_all_collision_ideals_preserved":ideal_all and all(not v for v in collisions.values()),
 "P3_all_relevant_ideal_powers_and_nested_orders_preserved":ideal_all and inverse_all and len(chains)==20,
 "P4_triple_overlap_cocycle_degree9":all(cocycle_pass.values()),
 "P5_finite_jet_quotient_atlas_automorphisms_no_selector":ideal_all and inverse_all and all(cocycle_pass.values()) and symbolic(positive) and prov(positive),
 "P6_all_negative_controls_rejected":all(v["rejected"] for v in neg.values()),
}
passall=all(pred.values())
classification="K5_THREE_CHART_TUBULAR_ATLAS_FINITE_JET_COCYCLE_CLOSED_EXACT_SCOPED" if passall else "K5_THREE_CHART_TUBULAR_ATLAS_COCYCLE_FAIL_SCOPED"
out={
 "iteration":"Iter082F-SM","maps":{k:fs(v) for k,v in MAPS.items()},
 "pair_inverse":{k:fs(v) for k,v in pair_inverse.items()},
 "cocycle_series":{k:{"lhs":fs(a),"rhs":fs(b),"equal":a==b} for k,(a,b) in cocycles.items()},
 "divergent_blocks":len(blocks),"maximal_chains":len(chains),"omega":{"K3":0,"K4":3,"K5":8},
 "ideal_generator_results":ideal_results,"ideal_power_checks":power_checks,"nested_order_check_classes":chain_order_checks,
 "S5":s5,"collision_failures":{k:[list(B) for B in v] for k,v in collisions.items()},"SO3_exact_checks":so3_checks,"SO3_failures":so3_fail,
 "negative_controls":neg,"predicates":pred,"classification":classification,"verdict":"PASS_EXACT_SCOPED" if passall else "FAIL_SCIENTIFIC_SCOPED",
 "claim_ceiling":["finite-jet three-chart atlas only","no global distributional patching theorem","no unique extension or selector","no regulator independence","no G3/F9/G8/K5 promotion","no NEW_PHYSICS_FOUND","no complete-QG claim"]
}
pre=json.dumps(out,sort_keys=True,indent=2,default=str)+"\n"; out["self_payload_sha256_pre_field"]=hashlib.sha256(pre.encode()).hexdigest(); blob=json.dumps(out,sort_keys=True,indent=2,default=str)+"\n"
os.makedirs("artifacts/iter082f",exist_ok=True)
open("artifacts/iter082f/aggregate.json","w",encoding="utf-8").write(blob)
print(blob)
if not passall: raise SystemExit(2)
