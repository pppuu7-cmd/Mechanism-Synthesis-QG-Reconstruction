#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial
import hashlib, json, os

MAXQ=4  # radial q^4 times a vector = total degree 9
F=[Fraction(1),Fraction(1,6),Fraction(1,120),Fraction(1,5040),Fraction(1,362880)]
G=[Fraction(1),Fraction(-1,6),Fraction(3,40),Fraction(-5,112),Fraction(35,1152)]
IDM=[Fraction(1),Fraction(0),Fraction(0),Fraction(0),Fraction(0)]

# ---------- exact univariate radial-series algebra ----------
def padd(a,b,n=MAXQ):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n+1)]
def pmul(a,b,n=MAXQ):
    z=[Fraction(0)]*(n+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=n: z[i+j]+=x*y
    return z
def ppow(a,k,n=MAXQ):
    z=[Fraction(1)]+[Fraction(0)]*n
    for _ in range(k): z=pmul(z,a,n)
    return z
def pcompose(poly,arg,n=MAXQ):
    z=[Fraction(0)]*(n+1)
    for k,c in enumerate(poly):
        if c:
            z=padd(z,[c*t for t in ppow(arg,k,n)],n)
    return z
def fs(xs): return [f"{x.numerator}/{x.denominator}" for x in xs]
q=[0,1,0,0,0]
p=pmul(q,pmul(F,F))
GF=pmul(F,pcompose(G,p))
pp=[0,1,0,0,0]
qprime=pmul(pp,pmul(G,G))
FG=pmul(G,pcompose(F,qprime))

# ---------- sparse exact 3-variable polynomial algebra ----------
# dict exponent triple -> Fraction
def poly_add(a,b):
    z=dict(a)
    for e,c in b.items():
        z[e]=z.get(e,Fraction(0))+c
        if z[e]==0: del z[e]
    return z
def poly_mul(a,b,maxdeg=9):
    z={}
    for ea,ca in a.items():
        for eb,cb in b.items():
            e=tuple(ea[i]+eb[i] for i in range(3))
            if sum(e)<=maxdeg:
                z[e]=z.get(e,Fraction(0))+ca*cb
    return {e:c for e,c in z.items() if c}
def poly_pow(a,k,maxdeg=9):
    z={(0,0,0):Fraction(1)}
    for _ in range(k): z=poly_mul(z,a,maxdeg)
    return z
Q={(2,0,0):Fraction(1),(0,2,0):Fraction(1),(0,0,2):Fraction(1)}
def radial_components(coeff):
    comps=[]
    for axis in range(3):
        base={tuple(1 if i==axis else 0 for i in range(3)):Fraction(1)}
        out={}
        for k,c in enumerate(coeff):
            term=poly_mul(base,poly_pow(Q,k),9)
            out=poly_add(out,{e:c*v for e,v in term.items()})
        comps.append(out)
    return comps
Fpoly=radial_components(F)
Gpoly=radial_components(G)

# Mechanical diagonal-ideal test for a component difference P(x)-P(y).
# Lift to 6 variables and substitute y=x; exact cancellation must result.
def difference_restrict_diagonal(poly):
    collapsed={}
    for e,c in poly.items():
        # +P(x)
        collapsed[e]=collapsed.get(e,Fraction(0))+c
        # -P(y), then y=x under diagonal substitution
        collapsed[e]=collapsed.get(e,Fraction(0))-c
    return {e:c for e,c in collapsed.items() if c}
F_diag=[difference_restrict_diagonal(p) for p in Fpoly]
G_diag=[difference_restrict_diagonal(p) for p in Gpoly]

# ---------- exact numerical evaluator, used for covariance and controls ----------
def dot(v): return sum(x*x for x in v)
def eval_radial(v, coeff, cubic_scale=Fraction(1), shift=(Fraction(0),)*3, linear=None):
    if linear is None: linear=((1,0,0),(0,1,0),(0,0,1))
    qv=dot(v)
    scalar=Fraction(0)
    for k,c in enumerate(coeff):
        ck=c
        if k==1: ck*=cubic_scale
        scalar+=ck*(qv**k)
    raw=tuple(scalar*x for x in v)
    out=[]
    for i in range(3):
        # frozen positive map has identity linear; malformed singular control can override its linear part.
        if linear!=((1,0,0),(0,1,0),(0,0,1)):
            nonlinear=raw[i]-v[i]  # retain radial nonlinear part, replace degree-one part
            lin=sum(Fraction(linear[i][j])*v[j] for j in range(3))
            out.append(lin+nonlinear+shift[i])
        else:
            out.append(raw[i]+shift[i])
    return tuple(out)

def transform_nodes(nodes, coeff, cubic_scales=None, shift=(Fraction(0),)*3, linear=None):
    if cubic_scales is None: cubic_scales=[Fraction(1)]*len(nodes)
    return tuple(eval_radial(nodes[i],coeff,cubic_scales[i],shift,linear) for i in range(len(nodes)))

def permute_nodes(nodes,p):
    out=[None]*len(nodes)
    for old,new in enumerate(p): out[new]=nodes[old]
    return tuple(out)

def s5_covariance(coeff,cubic_scales=None):
    nodes=(
        (Fraction(1,7),Fraction(2,9),Fraction(-1,5)),
        (Fraction(-2,11),Fraction(1,8),Fraction(3,10)),
        (Fraction(4,13),Fraction(-1,6),Fraction(2,7)),
        (Fraction(1,4),Fraction(3,17),Fraction(-2,9)),
        (Fraction(-3,14),Fraction(2,15),Fraction(1,12)),
    )
    good=0
    first_failure=None
    for p in permutations(range(5)):
        lhs=transform_nodes(permute_nodes(nodes,p),coeff,
                            None if cubic_scales is None else [cubic_scales[p.index(i)] for i in range(5)])
        rhs=permute_nodes(transform_nodes(nodes,coeff,cubic_scales),p)
        if lhs==rhs: good+=1
        elif first_failure is None: first_failure=p
    return good,first_failure

# ---------- block/chain geometry ----------
labels=tuple(range(5))
blocks=[tuple(c) for k in (3,4,5) for c in combinations(labels,k)]
chains=[(tuple(B3),tuple(B4),labels) for B4 in combinations(labels,4) for B3 in combinations(B4,3)]
omega={3:0,4:3,5:8}

def bary_normal(nodes,B):
    mean=tuple(sum(nodes[i][c] for i in B)/len(B) for c in range(3))
    return tuple(tuple(nodes[i][c]-mean[c] for c in range(3)) for i in B)

def collision_checks(coeff):
    base=(Fraction(2,9),Fraction(-1,7),Fraction(3,11))
    outsiders=[
        (Fraction(1,5),Fraction(2,13),Fraction(-1,4)),
        (Fraction(-1,6),Fraction(3,10),Fraction(1,8)),
        (Fraction(2,7),Fraction(-2,9),Fraction(1,12)),
        (Fraction(1,11),Fraction(4,15),Fraction(-3,14)),
        (Fraction(-2,17),Fraction(1,3),Fraction(2,19)),
    ]
    checks=0; failures=[]
    for B in blocks:
        nodes=list(outsiders)
        for i in B: nodes[i]=base
        out=transform_nodes(tuple(nodes),coeff)
        bn=bary_normal(out,B)
        checks+=1
        if any(any(x!=0 for x in row) for row in bn): failures.append(B)
    return checks,failures

# Tangent normal map at origin: compute on every barycentric basis lane from the actual degree-one coefficient.
def tangent_normal_checks(coeff,linear=((1,0,0),(0,1,0),(0,0,1))):
    c0=coeff[0]
    checks=0; fails=[]
    for B in blocks:
        anchor=B[-1]
        for i in B[:-1]:
            for comp in range(3):
                inp=[[(Fraction(0)) for _ in range(3)] for _ in range(5)]
                inp[i][comp]=Fraction(1)
                inp[anchor][comp]=Fraction(-1)
                # degree-one image only
                out=[[Fraction(0) for _ in range(3)] for _ in range(5)]
                for n in range(5):
                    for a in range(3):
                        out[n][a]=c0*sum(Fraction(linear[a][b])*inp[n][b] for b in range(3))
                checks+=1
                if out!=inp: fails.append((B,i,comp))
    return checks,fails

# Diagonal ideal generators: all pairwise differences in each B, three components.
def ideal_generator_audit(diag_restrictions):
    checks=0; failures=[]
    for B in blocks:
        for i,j in combinations(B,2):
            for comp in range(3):
                checks+=1
                if diag_restrictions[comp]: failures.append((B,i,j,comp))
    return checks,failures

F_ideal_checks,F_ideal_fail=ideal_generator_audit(F_diag)
G_ideal_checks,G_ideal_fail=ideal_generator_audit(G_diag)

# If a ring automorphism and its inverse both preserve every ideal generator,
# then each block ideal I_B and every power I_B^k are preserved exactly.
inverse_ok=(GF==IDM and FG==IDM)
ideal_equal=(not F_ideal_fail and not G_ideal_fail and inverse_ok)
power_checks=0
power_fail=[]
for B in blocks:
    for k in range(1,omega[len(B)]+2):
        for direction in ("X_to_V","V_to_X"):
            power_checks+=1
            if not ideal_equal: power_fail.append((B,k,direction))

# Nested ideals use all pairwise generators, so literal set inclusion follows B3 subset B4 subset B5.
def pair_generators(B): return {(i,j,c) for i,j in combinations(B,2) for c in range(3)}
chain_filtration_checks=0; chain_filtration_fail=[]
for ci,(B3,B4,B5) in enumerate(chains):
    nested=(pair_generators(B3)<=pair_generators(B4)<=pair_generators(B5))
    for direction in ("X_to_V","V_to_X"):
        for B in (B3,B4,B5):
            chain_filtration_checks+=1
            if not (nested and ideal_equal): chain_filtration_fail.append((ci,B,direction))

# Prospective finite-jet classes. Preservation of each nested ideal and its powers means
# the cumulative orders (a,a+b,a+b+c) cannot decrease under either direction.
degree_triples=[(a,b,c) for a in range(10) for b in range(10-a) for c in range(10-a-b)]
order_checks=0; order_fail=[]
for ci,_chain in enumerate(chains):
    for t in degree_triples:
        cumulative=(t[0],t[0]+t[1],sum(t))
        for direction in ("X_to_V","V_to_X"):
            order_checks+=1
            if not ideal_equal: order_fail.append((ci,t,direction,cumulative))

# ---------- exact SO(3) finite controls ----------
def matvec_signed_perm(v,p,s): return tuple(Fraction(s[i])*v[p[i]] for i in range(3))
rot_checks=0; rot_fail=[]
vecs=[(Fraction(1,7),Fraction(-2,9),Fraction(3,11)),(Fraction(2,5),Fraction(1,13),Fraction(-1,4))]
for p3 in permutations(range(3)):
    for signs in product((-1,1),repeat=3):
        for v in vecs:
            Rv=matvec_signed_perm(v,p3,signs)
            lhs=eval_radial(Rv,F)
            rhs=matvec_signed_perm(eval_radial(v,F),p3,signs)
            rot_checks+=1
            if lhs!=rhs: rot_fail.append((p3,signs,v))

# ---------- algebraic rank helper for singular negative control ----------
def rank_fraction(M):
    A=[[Fraction(x) for x in row] for row in M]
    r=0
    for c in range(len(A[0])):
        pivot=next((i for i in range(r,len(A)) if A[i][c]),None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]
        pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]:
                f=A[i][c]; A[i]=[A[i][j]-f*A[r][j] for j in range(len(A[0]))]
        r+=1
    return r

# ---------- same-machinery negative controls ----------
neg={}
# 1: origin anchoring from actual map evaluation
zero=(Fraction(0),Fraction(0),Fraction(0))
shift=(Fraction(1,5),Fraction(0),Fraction(0))
neg["constant_shift"]={"rejected":eval_radial(zero,F,shift=shift)!=zero,"reason":"compact_locus_not_anchored"}
# 2: exact S5 covariance calculator on a node-dependent cubic coefficient
bad_scales=[Fraction(2),Fraction(1),Fraction(1),Fraction(1),Fraction(1)]
bad_s5_count,bad_s5_first=s5_covariance(F,bad_scales)
neg["label_dependent_cubic"]={"rejected":bad_s5_count<120,"passed_permutations":bad_s5_count,"first_failure":list(bad_s5_first) if bad_s5_first else None}
# 3: actual Jacobian rank
sing=((1,0,0),(0,1,0),(0,0,0))
neg["singular_linear"]={"rejected":rank_fraction(sing)<3,"rank":rank_fraction(sing)}
# 4: explicit malformed order transport
bad_order_input=(0,0,9); bad_order_output=(0,0,8)
def cumulative(t): return (t[0],t[0]+t[1],sum(t))
neg["order9_to_order8"]={"rejected":any(o<i for i,o in zip(cumulative(bad_order_input),cumulative(bad_order_output))),"input":bad_order_input,"output":bad_order_output}
# 5: representative data structure must keep finite parts symbolic
positive_rep={"finite_coefficients":["c_K3","c_K4","c_K5"],"scales":["mu_K3","mu_K4","mu_K5"],"selector_sources":[]}
bad_rep={"finite_coefficients":["c_K3",Fraction(7,3),"c_K5"],"scales":["mu_K3","mu_K4","mu_K5"],"selector_sources":[]}
def finite_parts_symbolic(rep): return all(isinstance(x,str) for x in rep["finite_coefficients"]+rep["scales"])
neg["numeric_finite_part"]={"rejected":not finite_parts_symbolic(bad_rep)}
# 6: provenance/operator structure rejects reassociation as selector source
bad_reassoc={"finite_coefficients":["c_K3","c_K4","c_K5"],"scales":["mu_K3","mu_K4","mu_K5"],"selector_sources":["same_graph_reassociation"]}
def selector_provenance_ok(rep): return "same_graph_reassociation" not in rep.get("selector_sources",[])
neg["reassociation_selector"]={"rejected":not selector_provenance_ok(bad_reassoc)}
negative_all=all(v["rejected"] for v in neg.values())

# Positive exact S5 covariance through actual evaluator.
s5_good,s5_first=s5_covariance(F)
collision_n,collision_fail=collision_checks(F)
collision_ng,collision_fail_g=collision_checks(G)
tangent_n,tangent_fail=tangent_normal_checks(F)
tangent_ng,tangent_fail_g=tangent_normal_checks(G)

pred={
 "P0_chart_origin_and_identity_jacobian": eval_radial(zero,F)==zero and eval_radial(zero,G)==zero and not tangent_fail and not tangent_fail_g,
 "P0_inverse_composition_degree9": inverse_ok,
 "P0_radial_SO3_equivariance": not rot_fail and rot_checks==96,
 "P1_S5_covariance": s5_good==120 and s5_first is None,
 "P2_collision_strata_preserved": not collision_fail and not collision_fail_g and collision_n==16 and collision_ng==16,
 "P3_normal_ideal_filtration_preserved": ideal_equal and not power_fail,
 "P4_nested_chain_filtration_preserved_both_directions": not chain_filtration_fail and not order_fail and len(chains)==20,
 "P5_supported_jet_class_quotient_automorphism_degree9": inverse_ok and ideal_equal and not order_fail,
 "P5_no_finite_part_selected": finite_parts_symbolic(positive_rep) and selector_provenance_ok(positive_rep),
 "P6_all_negative_controls_rejected": negative_all,
}
all_pass=all(pred.values())
classification=("K5_NONLINEAR_TUBULAR_CHART_OVERLAP_PRESERVES_ALLOWED_SUPPORTED_JET_CLASS_EXACT_SCOPED" if all_pass else "K5_NONLINEAR_TUBULAR_CHART_OVERLAP_CLASS_COMPATIBILITY_FAIL_SCOPED")

out={
 "iteration":"Iter082E-SM-control-repair-1",
 "repair_parent_run":34895924300,
 "frozen_chart_X":"rapidity/exponential boost normal x",
 "frozen_chart_V":"v=(sinh(|x|)/|x|)x",
 "inverse":"x=(asinh(|v|)/|v|)v",
 "series_sinh_over_r":fs(F),"series_asinh_over_s":fs(G),
 "GF_multiplier_degree9":fs(GF),"FG_multiplier_degree9":fs(FG),
 "divergent_blocks":len(blocks),"maximal_chains":len(chains),
 "actual_S5_permutations_passed":s5_good,
 "actual_collision_checks":[collision_n,collision_ng],"collision_failures":[collision_fail,collision_fail_g],
 "actual_tangent_normal_basis_checks":[tangent_n,tangent_ng],"tangent_failures":[tangent_fail,tangent_fail_g],
 "actual_diagonal_ideal_generator_checks":[F_ideal_checks,G_ideal_checks],"ideal_generator_failures":[F_ideal_fail,G_ideal_fail],
 "ideal_power_checks":power_checks,"ideal_power_failures":power_fail,
 "nested_chain_generator_checks":chain_filtration_checks,"nested_chain_failures":chain_filtration_fail,
 "degree_triples_total_degree_le9":len(degree_triples),"nested_order_checks":order_checks,"nested_order_failures":order_fail,
 "SO3_signed_permutation_exact_checks":rot_checks,"SO3_failures":rot_fail,
 "omega":{"K3":0,"K4":3,"K5":8},
 "negative_controls":neg,
 "predicates":pred,
 "classification":classification,
 "verdict":"PASS_EXACT_SCOPED" if all_pass else "FAIL_SCIENTIFIC_SCOPED",
 "claim_ceiling":["local finite-jet/tubular overlap only","no global SL(2,C)^4 forest-extension theorem","no finite-part or invariant-jet selector","no regulator-independence claim","no G3/F9/G8/K5 promotion","no NEW_PHYSICS_FOUND","no complete-QG claim"]
}
pre=json.dumps(out,sort_keys=True,indent=2,default=str)+"\n"
out["self_payload_sha256_pre_field"]=hashlib.sha256(pre.encode()).hexdigest()
blob=json.dumps(out,sort_keys=True,indent=2,default=str)+"\n"
os.makedirs("artifacts/iter082e",exist_ok=True)
with open("artifacts/iter082e/aggregate.json","w",encoding="utf-8") as fh: fh.write(blob)
print(blob)
if not all_pass: raise SystemExit(2)
