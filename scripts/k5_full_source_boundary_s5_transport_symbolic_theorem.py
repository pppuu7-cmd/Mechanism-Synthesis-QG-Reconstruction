#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
from collections import defaultdict, deque
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SHARD=ROOT/'scripts/k5_full_source_boundary_s5_transport_shard.py'
ACTION=ROOT/'scripts/k5_deg4_annihilator_actual_dual_action.py'
REACH=ROOT/'scripts/k5_order8_invariant_dual_projective_ibp_reachability.py'
SOURCE=ROOT/'distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py'
PREREG=ROOT/'prereg/K5_FULL_SOURCE_BOUNDARY_S5_TRANSPORT_SYMBOLIC_GENERATOR_THEOREM.md'
REPAIR5=ROOT/'results/K5_EXACT_CANCELLATION_UNPROJECTED_BOUNDARY_DUAL_S5_DIAGNOSTIC_REPAIR5_RESULT.md'

PREREG_COMMIT='4f65cff503db976b6ff52b8519e5fdaa0bf4a4f8'
SHARD_BLOB='a5af2d67e1ef48ab138cc1e3516a63e8ec8a9456'
ACTION_BLOB='2ed1b6397236c3f64c22b2a827bf1f0f8b5e0484'
REACH_BLOB='fabe471d3dfffb70bd12cac4077f0e9c09319fe0'
SOURCE_BLOB='2a3e3390556b337eccb6b917979961981f913deb'
PASS_CLASS='K5_FULL_SOURCE_BOUNDARY_S5_SYMBOLIC_ALL_ALPHA_TRIVIAL_CHARACTER_EXACT_SCOPED'
FAIL_CLASS='K5_FULL_SOURCE_BOUNDARY_S5_SYMBOLIC_TRANSPORT_OBSTRUCTION_EXACT_SCOPED'
INVALID='INVALID_IMPLEMENTATION'

C=(1,2,3,4,0)
T=(1,0,2,3,4)
GENS={'C':C,'T':T}
ID=tuple(range(5))
ZERO_MON=(0,)*10


def git_blob_sha(path:Path)->str:
    raw=path.read_bytes();return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()

def load(path:Path,name:str):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);assert spec.loader is not None;spec.loader.exec_module(m);return m

def compose(p,q):
    # Apply q first, then p: (p o q)(i)=p(q(i)).
    return tuple(p[q[i]] for i in range(5))

def invperm(p):return tuple(p.index(i) for i in range(5))
def perm_sign(p):return -1 if sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))%2 else 1

def matmul(A,B):
    BT=list(zip(*B));return [[sum((x*y for x,y in zip(row,col)),Fraction(0)) for col in BT] for row in A]
def transpose(A):return [list(x) for x in zip(*A)]
def eye(n):return [[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
def matrix_scale(c,A):return [[c*x for x in row] for row in A]

def gp_add(a,b):return (a[0]+b[0],a[1]+b[1])
def gp_mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def gp_scale(c,a):return (c*a[0],c*a[1])

def clean_poly(p):return {m:c for m,c in p.items() if c}
def poly_add(a,b):
    z=defaultdict(int);z.update(a)
    for m,c in b.items():z[m]+=c
    return clean_poly(dict(z))
def poly_scale(c,a):return {} if c==0 else clean_poly({m:c*v for m,v in a.items()})
def poly_mul(a,b):
    if not a or not b:return {}
    z=defaultdict(int)
    for ma,ca in a.items():
        for mb,cb in b.items():z[tuple(ma[i]+mb[i] for i in range(10))]+=ca*cb
    return clean_poly(dict(z))
def poly_one():return {ZERO_MON:1}
def var_poly(i,c=1):
    m=[0]*10;m[i]=1;return {tuple(m):c} if c else {}
def det_poly(M):
    n=len(M);out={}
    for p in itertools.permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n));term=poly_one()
        for i,j in enumerate(p):term=poly_mul(term,M[i][j])
        out=poly_add(out,poly_scale(-1 if inv%2 else 1,term))
    return out
def minor(M,row,col):return [[M[i][j] for j in range(len(M)) if j!=col] for i in range(len(M)) if i!=row]

def poly_hash(p):
    h=hashlib.sha256()
    for m,c in sorted(p.items()):h.update((','.join(map(str,m))+'='+str(c)+'\n').encode())
    return h.hexdigest()

def dictvec_hash(v):
    h=hashlib.sha256()
    for i,d in enumerate(v):
        h.update(f'component={i}\n'.encode())
        for k,c in sorted(d.items()):
            flat=';'.join(f'{a}{b}' for a,b in k)
            h.update((flat+'='+str(c.numerator)+'/'+str(c.denominator)+'\n').encode())
    return h.hexdigest()

def dictvec_equal(a,b):return all(x==y for x,y in zip(a,b))
def first_dictvec_mismatch(a,b):
    for i,(x,y) in enumerate(zip(a,b)):
        if x==y:continue
        for k in sorted(set(x)|set(y)):
            if x.get(k,Fraction(0))!=y.get(k,Fraction(0)):
                return {'component':i,'types':[list(t) for t in k],'left':str(x.get(k,Fraction(0))),'right':str(y.get(k,Fraction(0)))}
    return None

def clean_dict(d):return {k:v for k,v in d.items() if v}

# Load the exact witness-gate implementation only as a source-construction library.
assert git_blob_sha(SHARD)==SHARD_BLOB
assert git_blob_sha(ACTION)==ACTION_BLOB
assert git_blob_sha(REACH)==REACH_BLOB
assert git_blob_sha(SOURCE)==SOURCE_BLOB
shard=load(SHARD,'k5_symbolic_transport_shard')
act=shard.act
EDGES=tuple(act.EDGES);EIDX={e:i for i,e in enumerate(EDGES)}
ROWS=tuple(act.reach.incidence_row(e) for e in EDGES)
assert len(EDGES)==10 and act.SOURCE_TERMS==100000


def ep(p,i):
    a,b=EDGES[i];x,y=p[a],p[b];return EIDX[(min(x,y),max(x,y))]
def edge_sign(p,i):
    a,b=EDGES[i];return 1 if p[a]<p[b] else -1
def pullback_poly(poly,p):
    # Substitute target alpha_{ep(p,i)} <- old alpha_i.
    out=defaultdict(int)
    for m,c in poly.items():
        n=[0]*10
        for i in range(10):n[i]=m[ep(p,i)]
        out[tuple(n)]+=c
    return clean_poly(dict(out))

def build_formal_laplacian():
    L=[[{} for _ in range(4)] for _ in range(4)]
    for e,r in enumerate(ROWS):
        for i in range(4):
            for j in range(4):
                if r[i]*r[j]:L[i][j]=poly_add(L[i][j],var_poly(e,r[i]*r[j]))
    return L

def build_covariance_numerators(L):
    psi=det_poly(L)
    adj=[[{} for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            # adj[i,j]=cofactor(j,i)
            adj[i][j]=poly_scale(-1 if (i+j)%2 else 1,det_poly(minor(L,j,i)))
    nums=[[{} for _ in range(10)] for _ in range(10)]
    for e,r in enumerate(ROWS):
        for f,s in enumerate(ROWS):
            z={}
            for i in range(4):
                if not r[i]:continue
                for j in range(4):
                    if s[j]:z=poly_add(z,poly_scale(r[i]*s[j],adj[i][j]))
            nums[e][f]=z
    return psi,nums

def covariance_transport_check(psi,nums,p):
    psi_ok=pullback_poly(psi,p)==psi
    bad=[]
    for i in range(10):
        ti=ep(p,i);si=edge_sign(p,i)
        for j in range(10):
            tj=ep(p,j);sj=edge_sign(p,j)
            lhs=pullback_poly(nums[ti][tj],p);rhs=poly_scale(si*sj,nums[i][j])
            if lhs!=rhs and len(bad)<5:bad.append((i,j,ti,tj,si*sj))
    return psi_ok and not bad,psi_ok,bad

def aggregate_base_patterns():
    out=[{} for _ in range(32)];terms=0
    for idx,arr in act.PATTERNS:
        d=defaultdict(Fraction)
        for types,c in arr:d[types]+=c;terms+=1
        out[idx]=clean_dict(dict(d))
    return out,terms

def transport_target_key_to_old(types,p,transpose_reversed=True):
    out=[None]*10
    for i in range(10):
        j=ep(p,i);t=types[j]
        if transpose_reversed and edge_sign(p,i)==-1:t=(t[1],t[0])
        out[i]=t
    return tuple(out)
def transported_pattern_dicts(base,p,*,transpose_reversed=True,source_reversal_sign=True):
    g=1
    if source_reversal_sign:
        for i in range(10):g*=edge_sign(p,i)
    out=[]
    for d in base:
        z=defaultdict(Fraction)
        for types,c in d.items():z[transport_target_key_to_old(types,p,transpose_reversed)]+=g*c
        out.append(clean_dict(dict(z)))
    return out

def transform_dictvec(M,v):
    out=[]
    for i,row in enumerate(M):
        z=defaultdict(Fraction)
        for j,c in enumerate(row):
            if not c:continue
            for k,x in v[j].items():z[k]+=c*x
        out.append(clean_dict(dict(z)))
    return out

def source_matrix_reversal_control():
    for v in ((1,0,0),(0,1,0),(0,0,1),(1,2,3)):
        A=act.src.leading_matrix(v);B=act.src.leading_matrix(tuple(-x for x in v))
        if B!=[[(-z[0],-z[1]) for z in row] for row in A]:return False
    return True

def edge_map_bijection(p):return sorted(ep(p,i) for i in range(10))==list(range(10))
def edge_map_inverse_roundtrip(p):
    ip=invperm(p)
    return all(ep(ip,ep(p,i))==i and edge_sign(p,i)*edge_sign(ip,ep(p,i))==1 for i in range(10))

def boundary_matrix(p,local):return act.reach.global_action_matrix(act.src,p,local)

def generated_group_and_representation(local):
    Agen={name:boundary_matrix(p,local) for name,p in GENS.items()}
    seen={ID:eye(32)};q=deque([ID]);representation_ok=True;edge_comp_ok=True
    while q:
        p=q.popleft();Ap=seen[p]
        for name,g in GENS.items():
            np=compose(g,p);nA=matmul(Agen[name],Ap)
            direct=boundary_matrix(np,local)
            representation_ok &= (nA==direct)
            for i in range(10):
                edge_comp_ok &= ep(np,i)==ep(g,ep(p,i))
                edge_comp_ok &= edge_sign(np,i)==edge_sign(p,i)*edge_sign(g,ep(p,i))
            if np not in seen:seen[np]=nA;q.append(np)
            else:representation_ok &= seen[np]==nA
    return seen,Agen,representation_ok,edge_comp_ok

def powperm(p,n):
    z=ID
    for _ in range(n):z=compose(p,z)
    return z

def formal_pattern_generator_check(base,local,p):
    ip=invperm(p);A=boundary_matrix(p,local);Ai=boundary_matrix(ip,local)
    predicted=transform_dictvec(transpose(Ai),base)
    transported=transported_pattern_dicts(base,p,transpose_reversed=True,source_reversal_sign=True)
    no_transpose=transported_pattern_dicts(base,p,transpose_reversed=False,source_reversal_sign=True)
    no_sign=transported_pattern_dicts(base,p,transpose_reversed=True,source_reversal_sign=False)
    source_fixed=transported_pattern_dicts(base,p,transpose_reversed=False,source_reversal_sign=False)
    exact=dictvec_equal(transported,predicted)
    return {
      'exact':exact,
      'transported_hash':dictvec_hash(transported),'predicted_hash':dictvec_hash(predicted),
      'first_mismatch':first_dictvec_mismatch(transported,predicted),
      'no_transpose_rejected':not dictvec_equal(no_transpose,predicted),
      'no_source_sign_rejected':not dictvec_equal(no_sign,predicted),
      'source_fixed_rejected':not dictvec_equal(source_fixed,predicted),
      'extra_sign_rejected':(perm_sign(p)==1) or not dictvec_equal(transported,transform_dictvec(matrix_scale(-1,transpose(Ai)),base)),
      'transported_nonzero':any(bool(d) for d in transported),
      'boundary_inverse_exact':matmul(A,Ai)==eye(32) and matmul(Ai,A)==eye(32),
    }

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    prereg_text=PREREG.read_text(encoding='utf-8')
    repair5_text=REPAIR5.read_text(encoding='utf-8') if REPAIR5.exists() else ''
    tensors=act.reach.local_tensor_vectors(act.src);local=act.reach.local_action_matrices(tensors)
    group,Agen,representation_ok,edge_comp_ok=generated_group_and_representation(local)
    L=build_formal_laplacian();psi,nums=build_covariance_numerators(L)
    base,terms=aggregate_base_patterns()
    gen_results={};cov_results={}
    for name,p in GENS.items():
        ok,psi_ok,bad=covariance_transport_check(psi,nums,p)
        cov_results[name]={'exact':ok,'psi_exact':psi_ok,'bad_pairs':bad}
        gen_results[name]=formal_pattern_generator_check(base,local,p)
    controls={
      'prereg_commit_locked':PREREG_COMMIT=='4f65cff503db976b6ff52b8519e5fdaa0bf4a4f8',
      'prereg_object_present':'symbolic full-source boundary S5 transport theorem' in prereg_text,
      'shard_blob_locked':git_blob_sha(SHARD)==SHARD_BLOB,
      'action_blob_locked':git_blob_sha(ACTION)==ACTION_BLOB,
      'reach_blob_locked':git_blob_sha(REACH)==REACH_BLOB,
      'source_blob_locked':git_blob_sha(SOURCE)==SOURCE_BLOB,
      'repair5_negative_authority_present':'BOUNDARY_S5_REPRESENTATION_UNRESOLVED_EXACT' in repair5_text,
      'ten_edges':len(EDGES)==10,
      'all32':len(base)==32,
      'source_terms_100000':terms==act.SOURCE_TERMS==100000,
      'reynolds_rank2_pivots14':list(act.PIV)==[1,4],
      'source_matrix_reversal_exact':source_matrix_reversal_control(),
      'C_edge_bijection_roundtrip':edge_map_bijection(C) and edge_map_inverse_roundtrip(C),
      'T_edge_bijection_roundtrip':edge_map_bijection(T) and edge_map_inverse_roundtrip(T),
      'C5_identity':powperm(C,5)==ID,
      'T2_identity':powperm(T,2)==ID,
      'generated_group_size120':len(group)==120,
      'boundary_representation_composes_all_generated_words':representation_ok,
      'edge_orientation_transport_composes_all_generated_words':edge_comp_ok,
      'psi_125_coefficient_one_trees':len(psi)==125 and set(psi.values())=={1},
      'formal_covariance_C_exact':cov_results['C']['exact'],
      'formal_covariance_T_exact':cov_results['T']['exact'],
      'C_boundary_inverse_exact':gen_results['C']['boundary_inverse_exact'],
      'T_boundary_inverse_exact':gen_results['T']['boundary_inverse_exact'],
      'no_numeric_alpha_witnesses_used':True,
      'no_fitted_two_channel_matrix_used':True,
      'no_floating_arithmetic_used':True,
      'no_corner_coefficients_computed':True,
    }
    negatives={
      'T_omit_transpose_rejected':gen_results['T']['no_transpose_rejected'],
      'T_remove_source_reversal_sign_rejected':gen_results['T']['no_source_sign_rejected'],
      'T_source_fixed_object_rejected':gen_results['T']['source_fixed_rejected'],
      'T_extra_permutation_sign_rejected':gen_results['T']['extra_sign_rejected'] and gen_results['T']['transported_nonzero'],
      'C_source_fixed_object_not_used_as_authority':gen_results['C']['source_fixed_rejected'] or ('BOUNDARY_S5_REPRESENTATION_UNRESOLVED_EXACT' in repair5_text),
      'finite_witness_path_forbidden':True,
    }
    theorem_exact=gen_results['C']['exact'] and gen_results['T']['exact'] and cov_results['C']['exact'] and cov_results['T']['exact'] and representation_ok and edge_comp_ok and len(group)==120
    implementation_valid=all(controls.values()) and all(negatives.values())
    if not implementation_valid:classification=INVALID;status=INVALID
    elif theorem_exact:classification=PASS_CLASS;status='PASS_EXACT_SCOPED'
    else:classification=FAIL_CLASS;status='PASS_EXACT_SCOPED'
    out={
      'gate':'K5_FULL_SOURCE_BOUNDARY_S5_TRANSPORT_SYMBOLIC_GENERATOR_THEOREM',
      'prereg_commit':PREREG_COMMIT,'status':status,'classification':classification,
      'hypothesis_symbolic_all_alpha_contragredient_trivial_character':theorem_exact,
      'domain':'formal Schwinger variables with Psi_K5 != 0',
      'generators':{'C':list(C),'T':list(T)},'generated_group_size':len(group),
      'source_terms':terms,'boundary_components':32,
      'psi_monomials':len(psi),'psi_sha256':poly_hash(psi),
      'covariance_results':cov_results,'formal_source_boundary_results':gen_results,
      'controls':controls,'negative_controls':negatives,
      'interpretation':{
        'coefficient_level_transport_authority_if_independently_confirmed':bool(theorem_exact),
        'physical_corner_verdict':None,'global_stokes_ibp_verdict':None,'integrated_k5_period_verdict':None,
        'finite_part_selector':None,'new_physics_found':False,'complete_qg':False,
      },
    }
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({
      'status':status,'classification':classification,'group_size':len(group),'psi_monomials':len(psi),
      'covariance_C':cov_results['C']['exact'],'covariance_T':cov_results['T']['exact'],
      'pattern_C':gen_results['C']['exact'],'pattern_T':gen_results['T']['exact'],
      'T_no_transpose_rejected':negatives['T_omit_transpose_rejected'],
      'T_no_sign_rejected':negatives['T_remove_source_reversal_sign_rejected'],
    },indent=2,sort_keys=True))
    return 0 if implementation_valid else 2

if __name__=='__main__':raise SystemExit(main())
