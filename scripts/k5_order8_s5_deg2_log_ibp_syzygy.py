#!/usr/bin/env python3
from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

VERTICES = tuple(range(5))
EDGES = tuple((a,b) for a in VERTICES for b in VERTICES if a < b)
EDGE_INDEX = {e:i for i,e in enumerate(EDGES)}
N = len(EDGES)
ZERO_MON = (0,)*N

RADIAL1 = (1,4)
RADIAL2 = (1,1,1,4)

CLASS_NONRADIAL = 'K5_S5_FACE_TANGENT_LOG_IBP_DEG2_NONRADIAL_EXISTS_EXACT_SCOPED'
CLASS_RADIAL_ONLY = 'K5_S5_FACE_TANGENT_LOG_IBP_DEG2_RADIAL_ONLY_EXACT_SCOPED'
CLASS_INCONCLUSIVE = 'K5_S5_FACE_TANGENT_LOG_IBP_DEG2_INCONCLUSIVE_SCOPED'
CLASS_INVALID = 'INVALID_IMPLEMENTATION'


def edge_relation(e,f):
    if e == f:
        return 'same'
    return 'adjacent' if len(set(EDGES[e]) & set(EDGES[f])) == 1 else 'disjoint'


def connected_tree(edge_indices):
    adj = {v:set() for v in VERTICES}
    for ei in edge_indices:
        a,b = EDGES[ei]
        adj[a].add(b); adj[b].add(a)
    seen={0}; stack=[0]
    while stack:
        v=stack.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w); stack.append(w)
    return len(edge_indices)==4 and len(seen)==5


def tree_polynomial():
    out={}
    for comb in itertools.combinations(range(N),4):
        if connected_tree(comb):
            m=[0]*N
            for i in comb: m[i]=1
            out[tuple(m)] = Fraction(1)
    return out


def padd(a,b):
    out=dict(a)
    for m,c in b.items():
        out[m]=out.get(m,Fraction(0))+c
        if out[m]==0: del out[m]
    return out


def pscale(a,c):
    if c==0: return {}
    return {m:c*v for m,v in a.items() if c*v}


def pmul(a,b):
    out={}
    for ma,ca in a.items():
        for mb,cb in b.items():
            m=tuple(x+y for x,y in zip(ma,mb))
            out[m]=out.get(m,Fraction(0))+ca*cb
            if out[m]==0: del out[m]
    return out


def monomial_poly(i,power=1,coeff=1):
    m=[0]*N; m[i]=power
    return {tuple(m):Fraction(coeff)}


def pshift(a, shifts, coeff=1):
    s=[0]*N
    for i,p in shifts.items(): s[i]+=p
    out={}
    for m,c in a.items():
        mm=tuple(m[i]+s[i] for i in range(N))
        out[mm]=out.get(mm,Fraction(0))+Fraction(coeff)*c
    return {m:c for m,c in out.items() if c}


def pderiv(a,i):
    out={}
    for m,c in a.items():
        if m[i]:
            mm=list(m); power=mm[i]; mm[i]-=1; mm=tuple(mm)
            out[mm]=out.get(mm,Fraction(0))+c*power
    return {m:c for m,c in out.items() if c}


def incidence_row(edge):
    a,b=edge
    row=[0,0,0,0]
    if a!=0: row[a-1]-=1
    if b!=0: row[b-1]+=1
    return tuple(row)


def laplacian_poly_matrix():
    L=[[{} for _ in range(4)] for _ in range(4)]
    for ei,e in enumerate(EDGES):
        r=incidence_row(e)
        for i in range(4):
            for j in range(4):
                c=r[i]*r[j]
                if c:
                    L[i][j]=padd(L[i][j],monomial_poly(ei,1,c))
    return L


def perm_sign(p):
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inv%2 else 1


def det_poly_4x4(M):
    out={}
    for p in itertools.permutations(range(4)):
        term={ZERO_MON:Fraction(perm_sign(p))}
        for i,j in enumerate(p):
            term=pmul(term,M[i][j])
            if not term: break
        out=padd(out,term)
    return out


def s1_times(poly):
    out={}
    for i in range(N): out=padd(out,pshift(poly,{i:1}))
    return out


def vector_action_basis(poly):
    # A: v_i=alpha_i^2
    # B: v_i=alpha_i sum_{f adjacent i} alpha_f
    # C: v_i=alpha_i sum_{f disjoint i} alpha_f
    A={}; B={}; C={}
    for i in range(N):
        d=pderiv(poly,i)
        A=padd(A,pshift(d,{i:2}))
        for f in range(N):
            rel=edge_relation(i,f)
            if rel=='adjacent': B=padd(B,pshift(d,{i:1,f:1}))
            elif rel=='disjoint': C=padd(C,pshift(d,{i:1,f:1}))
    return A,B,C


def degree1_system(poly):
    euler={}
    for i in range(N): euler=padd(euler,pshift(pderiv(poly,i),{i:1}))
    cols=[euler,pscale(poly,-1)]
    return coefficient_rows(cols)


def degree2_system(poly):
    A,B,C=vector_action_basis(poly)
    K=pscale(s1_times(poly),-1)
    return coefficient_rows([A,B,C,K])


def coefficient_rows(cols):
    mons=sorted(set().union(*(set(c) for c in cols)))
    rows=[]
    for m in mons:
        row=[Fraction(c.get(m,0)) for c in cols]
        if any(row): rows.append(row)
    return rows


def rref(rows,ncols):
    a=[list(map(Fraction,row)) for row in rows]
    r=0; piv=[]
    for c in range(ncols):
        p=next((i for i in range(r,len(a)) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        z=a[r][c]; a[r]=[x/z for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                z=a[i][c]; a[i]=[x-z*y for x,y in zip(a[i],a[r])]
        piv.append(c); r+=1
        if r==len(a): break
    return a,piv


def nullspace(rows,ncols):
    a,piv=rref(rows,ncols)
    free=[c for c in range(ncols) if c not in piv]
    basis=[]
    for f in free:
        x=[Fraction(0)]*ncols; x[f]=1
        for rr,p in enumerate(piv): x[p]=-a[rr][f]
        basis.append(tuple(x))
    return basis,piv


def rank_rows(rows,ncols):
    return len(rref(rows,ncols)[1])


def in_span(v,basis):
    if not basis: return all(x==0 for x in v)
    n=len(v)
    r0=rank_rows(basis,n)
    r1=rank_rows(list(basis)+[tuple(map(Fraction,v))],n)
    return r0==r1


def canonical_int_vector(v):
    den=1
    for q in v: den=abs(den*q.denominator)//math.gcd(den,q.denominator)
    ints=[q.numerator*(den//q.denominator) for q in v]
    g=0
    for x in ints: g=math.gcd(g,abs(x))
    if g: ints=[x//g for x in ints]
    first=next((x for x in ints if x),1)
    if first<0: ints=[-x for x in ints]
    return tuple(ints)


def identity_zero(rows,v):
    vv=list(map(Fraction,v))
    return all(sum(row[j]*vv[j] for j in range(len(vv)))==0 for row in rows)


def edge_perm(vertex_perm):
    out={}
    for i,(a,b) in enumerate(EDGES):
        x,y=vertex_perm[a],vertex_perm[b]
        ee=(x,y) if x<y else (y,x)
        out[i]=EDGE_INDEX[ee]
    return out


def stabilizer_orbit_sizes():
    H=[]
    for p in itertools.permutations(VERTICES):
        if {p[0],p[1]}=={0,1}: H.append(p)
    ep=[edge_perm(p) for p in H]
    e_same=EDGE_INDEX[(0,1)]
    e_adj=EDGE_INDEX[(0,2)]
    e_dis=EDGE_INDEX[(2,3)]
    return [len({q[e_same] for q in ep}),len({q[e_adj] for q in ep}),len({q[e_dis] for q in ep})],len(H)


def equivariant_coeff_matrix():
    C=[[0]*N for _ in range(N)]
    for e in range(N):
        for f in range(N):
            C[e][f]={'same':11,'adjacent':13,'disjoint':17}[edge_relation(e,f)]
    return C


def matrix_is_s5_equivariant(C):
    for p in itertools.permutations(VERTICES):
        ep=edge_perm(p)
        for e in range(N):
            for f in range(N):
                if C[ep[e]][ep[f]]!=C[e][f]: return False
    return True


def sample_face_tangent_components():
    comps=[]
    for e in range(N):
        p={}
        p=padd(p,pshift({ZERO_MON:Fraction(2)},{e:2}))
        for f in range(N):
            rel=edge_relation(e,f)
            if rel=='adjacent': p=padd(p,pshift({ZERO_MON:Fraction(3)},{e:1,f:1}))
            elif rel=='disjoint': p=padd(p,pshift({ZERO_MON:Fraction(5)},{e:1,f:1}))
        comps.append(p)
    return comps


def is_face_tangent(comps):
    for i,p in enumerate(comps):
        for m in p:
            if m[i]<1: return False
    return True


def synthetic_product_poly():
    return {(1,)*N:Fraction(1)}


def classify(valid,nonradial_dim):
    if not valid: return CLASS_INVALID
    if nonradial_dim>0: return CLASS_NONRADIAL
    if nonradial_dim==0: return CLASS_RADIAL_ONLY
    return CLASS_INCONCLUSIVE


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args()

    psi_tree=tree_polynomial()
    psi_det=det_poly_4x4(laplacian_poly_matrix())
    orbit_sizes,stab_size=stabilizer_orbit_sizes()

    rows1=degree1_system(psi_tree)
    ns1,piv1=nullspace(rows1,2)
    rows2=degree2_system(psi_tree)
    ns2,piv2=nullspace(rows2,4)

    radial1_in=in_span(RADIAL1,ns1)
    radial2_in=in_span(RADIAL2,ns2)
    nonradial_dim=len(ns2)-(1 if radial2_in else 0)

    basis1=[canonical_int_vector(v) for v in ns1]
    basis2=[canonical_int_vector(v) for v in ns2]

    syn=synthetic_product_poly()
    synrows=degree2_system(syn)
    synns,_=nullspace(synrows,4)
    synrad=in_span((1,1,1,10),synns)
    syn_nonrad=len(synns)-(1 if synrad else 0)

    C=equivariant_coeff_matrix()
    Cbad=[row[:] for row in C]; Cbad[0][1]+=1
    tangent=sample_face_tangent_components()
    bad_tangent=[dict(p) for p in tangent]
    bad_tangent[0]=padd(bad_tangent[0],{ZERO_MON:Fraction(1)})

    checks={
        'ten_edges':N==10,
        'tree_count_125':len(psi_tree)==125,
        'tree_coefficients_one':all(c==1 for c in psi_tree.values()),
        'determinant_equals_tree_polynomial':psi_det==psi_tree,
        'psi_homogeneous_degree_4':all(sum(m)==4 for m in psi_tree),
        'edge_stabilizer_size_12':stab_size==12,
        'edge_stabilizer_orbits_1_6_3':orbit_sizes==[1,6,3],
        'three_parameter_coeff_matrix_s5_equivariant':matrix_is_s5_equivariant(C),
        'degree1_exact_nullspace_complete':len(ns1)==1 and radial1_in,
        'degree1_basis_verified_by_substitution':all(identity_zero(rows1,v) for v in ns1),
        'degree2_radial_anchor_verified':identity_zero(rows2,RADIAL2) and radial2_in,
        'degree2_basis_verified_by_substitution':all(identity_zero(rows2,v) for v in ns2),
        'face_tangent_ansatz_verified':is_face_tangent(tangent),
        'synthetic_fixture_has_nonradial_log_directions':synrad and syn_nonrad>0,
        'no_period_verdict_from_syzygy_classification':True,
    }

    controls={
        'fake_log_vector_rejected':not identity_zero(rows2,(0,0,0,1)),
        'non_face_tangent_field_rejected':not is_face_tangent(bad_tangent),
        'broken_s5_coeff_matrix_rejected':not matrix_is_s5_equivariant(Cbad),
        'synthetic_nonradial_branch_reachable':syn_nonrad>=2,
        'radial_solution_not_hardcoded_as_only_possible':len(synns)>=3,
    }

    valid=all(checks.values()) and all(controls.values())
    classification=classify(valid,nonradial_dim)

    out={
        'gate':'K5_ORDER8_S5_DEG2_FACE_TANGENT_LOG_IBP_SYZYGY',
        'prereg_commit':'01bc02dad5e94873e726fca75ee07f0c8c01946d',
        'status':'PASS_EXACT_SCOPED' if valid else 'INVALID_IMPLEMENTATION',
        'classification':classification,
        'checks':checks,
        'controls':controls,
        'k5':{
            'edge_order':[f'{a}{b}' for a,b in EDGES],
            'spanning_tree_count':len(psi_tree),
            'edge_stabilizer_size':stab_size,
            'edge_stabilizer_orbit_sizes_same_adjacent_disjoint':orbit_sizes,
            'degree1_system_rank':len(piv1),
            'degree1_nullity':len(ns1),
            'degree1_nullspace_basis':basis1,
            'degree2_system_rank':len(piv2),
            'degree2_nullity':len(ns2),
            'degree2_nullspace_basis_a_b_c_k':basis2,
            'radial_degree2_anchor':[1,1,1,4],
            'nonradial_degree2_quotient_dimension':nonradial_dim,
        },
        'synthetic_product_fixture':{
            'polynomial':'prod_e alpha_e',
            'degree':10,
            'degree2_nullity':len(synns),
            'radial_anchor':[1,1,1,10],
            'nonradial_quotient_dimension':syn_nonrad,
            'basis_a_b_c_k':[canonical_int_vector(v) for v in synns],
        },
        'scientific_invariant_dual_period_verdict':None,
        'interpretation':{
            'scope':'S5-equivariant regular face-tangent logarithmic vector fields through component degree two only',
            'if_radial_only_next':'degree>=3 logarithmic derivations, non-equivariant orbit systems, or denominator-shifting IBP with fresh boundary audit',
            'if_nonradial_next':'apply exact nonradial derivation to both actual invariant-dual degree-27 numerators and test whether the induced period relation is nontrivial',
        },
    }
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if valid else 2


if __name__=='__main__':
    raise SystemExit(main())
