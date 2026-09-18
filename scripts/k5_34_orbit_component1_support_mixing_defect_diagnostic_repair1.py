#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, itertools, json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CORE=ROOT/'scripts/k5_34_orbit_exact_leading_coefficient_core_repair1.py'
PREPATH=ROOT/'prereg/K5_34_ORBIT_COMPONENT1_SUPPORT_MIXING_DIAGNOSTIC_CONTROL_REPAIR_1.md'
PARENT_PRE='ea49bb0cc67887659bb92c8a68b616f6b7e52513'
REPAIR_PRE='aab70cd2ffbc9bf52fdd83f8caa78bc3d8b220ec'
CRITIC=ROOT/'results/K5_34_ORBIT_COMPONENT1_SUPPORT_MIXING_ADVERSARIAL_REVIEW.md'
COMPONENT=1
FROZEN=((0,1),(2,4),(3,5),(6,8),(7,9))

def load(p,n):
    s=importlib.util.spec_from_file_location(n,p)
    m=importlib.util.module_from_spec(s)
    assert s.loader is not None
    s.loader.exec_module(m)
    return m

c=load(CORE,'c1diag_repair_core')
s5=c.s5
P=s5.C
Pinv=s5.invperm(P)

def clean(d):
    return {k:Fraction(v) for k,v in d.items() if Fraction(v)}

def add_scaled(dst,src,a):
    if not a:return
    for k,v in src.items():
        dst[k]+=a*Fraction(v)

def transform_vec(M,v):
    out=[]
    for row in M:
        z=defaultdict(Fraction)
        for j,a in enumerate(row):
            add_scaled(z,v[j],a)
        out.append(clean(z))
    return out

def transport_one(d,Q):
    g=s5.orientation_character(Q)
    z=defaultdict(Fraction)
    for types,coef in d.items():
        out=[None]*10
        for old in range(10):
            j=s5.ep(Q,old)
            t=types[old]
            if s5.edge_sign(Q,old)==-1:
                t=(t[1],t[0])
            out[j]=t
        z[tuple(out)]+=g*Fraction(coef)
    return clean(z)

def H(d):
    return hashlib.sha256(repr(sorted(d.items(),key=lambda kv:repr(kv[0]))).encode()).hexdigest()

def bit_index(bits):
    x=0
    for b in bits:x=(x<<1)|b
    return x

# Algebraically independent reconstruction from raw source node tensors.
# Deliberately does not call reach.local_action_matrices/global_action_matrix.
def raw_local_tensors(src):
    out=[]
    for k in (0,1):
        v=[Fraction(0)]*16
        for state,coef in src.NODE_OPTIONS[k]:
            v[bit_index(state)]=Fraction(coef)
        out.append(v)
    return out

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),Fraction(0))

def permute_local(v,p):
    out=[Fraction(0)]*16
    for idx,coef in enumerate(v):
        if not coef:continue
        bits=[(idx>>(3-i))&1 for i in range(4)]
        ob=[0]*4
        for i in range(4):ob[p[i]]=bits[i]
        out[bit_index(ob)]=coef
    return out

def direct_local_actions(src):
    tensors=raw_local_tensors(src)
    n0,n1=dot(tensors[0],tensors[0]),dot(tensors[1],tensors[1])
    assert dot(tensors[0],tensors[1])==0
    mats={}
    for p in itertools.permutations(range(4)):
        cols=[]
        for k in (0,1):
            pv=permute_local(tensors[k],p)
            coords=(dot(tensors[0],pv)/n0,dot(tensors[1],pv)/n1)
            recon=[coords[0]*tensors[0][i]+coords[1]*tensors[1][i] for i in range(16)]
            assert recon==pv
            cols.append(coords)
        mats[p]=((cols[0][0],cols[1][0]),(cols[0][1],cols[1][1]))
    return tensors,mats

def direct_global_action(src,sigma,local_mats):
    A=[[Fraction(0) for _ in range(32)] for _ in range(32)]
    for x in range(32):
        ks=tuple((x>>(4-i))&1 for i in range(5))
        local_by_target={}
        for v in range(5):
            old_neighbors=src.NEIGHBORS[v]
            tv=sigma[v]
            target_pos={w:i for i,w in enumerate(src.NEIGHBORS[tv])}
            leg_perm=tuple(target_pos[sigma[w]] for w in old_neighbors)
            M=local_mats[leg_perm]
            local_by_target[tv]=(M[0][ks[v]],M[1][ks[v]])
        for kout in itertools.product((0,1),repeat=5):
            coef=Fraction(1)
            for tv in range(5):
                coef*=local_by_target[tv][kout[tv]]
                if not coef:break
            if coef:A[bit_index(kout)][x]+=coef
    return A

def transpose(A):
    return [list(x) for x in zip(*A)]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',required=True)
    args=ap.parse_args()

    base=c._BASE_PATTERNS
    src=s5.act.src

    # Parent route 1.
    tensors=s5.act.reach.local_tensor_vectors(src)
    local=s5.act.reach.local_action_matrices(tensors)
    A=s5.boundary_matrix(P,local)
    Ai=s5.boundary_matrix(Pinv,local)
    ATi=s5.transpose(Ai)
    predicted=s5.transform_dictvec(ATi,base)
    pred=clean(predicted[COMPONENT])

    # Repair route 2: transport the full source vector first.
    transported=[transport_one(clean(d),P) for d in base]

    # Independent target projection from raw source tensors.
    dtensors,dlocal=direct_local_actions(src)
    dA=direct_global_action(src,P,dlocal)
    dAi=direct_global_action(src,Pinv,dlocal)
    dATi=transpose(dAi)
    direct_all=transform_vec(dATi,transported)
    direct=clean(direct_all[COMPONENT])

    # Mandatory mixing witness.
    row=dATi[COMPONENT]
    contributors=[(j,a) for j,a in enumerate(row) if a and transported[j]]
    contributor_indices=[j for j,a in contributors]
    contributor_coefficients=[str(a) for j,a in contributors]
    at_least_two=len(contributors)>=2

    dropped=None
    dropped_rejected=False
    if contributors:
        drop_j,drop_a=contributors[0]
        z=defaultdict(Fraction)
        for j,a in contributors[1:]:
            add_scaled(z,transported[j],a)
        dropped=clean(z)
        dropped_rejected=(dropped!=direct)

    ps=set(pred);ds=set(direct)
    missing=sorted(ps-ds,key=repr)
    spurious=sorted(ds-ps,key=repr)
    support_equal=ps==ds
    coeff_bad=next((k for k in sorted(ps&ds,key=repr) if pred[k]!=direct[k]),None)
    coeff_equal=support_equal and coeff_bad is None

    # Endpoint/orientation roundtrip on the entire full source vector.
    roundtrip=all(
        transport_one(transport_one(clean(d),P),Pinv)==clean(d)
        for d in base
    )

    # Wrong-transpose rejection retained.
    wrong=s5.transform_dictvec(Ai,base)
    ctrl=next((i for i in range(32) if clean(wrong[i])!=clean(predicted[i])),None)
    wrong_rejected=ctrl is not None

    # Mutation sensitivity on one contributing transported source coefficient.
    mutation_rejected=False
    if contributors:
        j,a=contributors[0]
        mut=[dict(d) for d in transported]
        if mut[j]:
            k=sorted(mut[j],key=repr)[0]
            mut[j][k]=Fraction(mut[j][k])+1
            mutation_rejected=clean(transform_vec(dATi,mut)[COMPONENT])!=direct

    helper_A=s5.act.reach.global_action_matrix(src,P,local)
    helper_Ai=s5.act.reach.global_action_matrix(src,Pinv,local)

    pretxt=PREPATH.read_text(encoding='utf-8')
    crittxt=CRITIC.read_text(encoding='utf-8')
    validity={
        'parent_prereg_locked':PARENT_PRE=='ea49bb0cc67887659bb92c8a68b616f6b7e52513',
        'repair_prereg_locked':REPAIR_PRE in pretxt,
        'critic_invalid_authority_locked':'Mandatory Critic verdict: **INVALID_IMPLEMENTATION**' in crittxt,
        'component1_frozen':COMPONENT==1,
        'full32':len(base)==len(transported)==len(predicted)==len(direct_all)==32,
        'source100000':c._SOURCE_TERM_COUNT==100000,
        'support945':len(c.MATCH_COEFF)==945,
        'exact_fraction':all(isinstance(Fraction(v),Fraction) for d in base for v in d.values()),
        'endpoint_orientation_roundtrip':roundtrip,
        'independent_local_tensor_vectors_equal':dtensors==tensors,
        'independent_global_A_equals_helper':dA==helper_A==A,
        'independent_global_Ainv_equals_helper':dAi==helper_Ai==Ai,
        'wrong_transpose_distinguishable':wrong_rejected,
        'target_component_has_at_least_two_nonzero_source_contributors':at_least_two,
        'dropped_contributor_rejected':dropped_rejected,
        'coefficient_mutation_detected':mutation_rejected,
    }

    if not all(validity.values()):
        cls='INVALID_IMPLEMENTATION_OR_PROVENANCE'
    elif not support_equal:
        cls='K5_S5_COMPONENT1_DEFECT_SUPPORT_INDEX_MISSING_OR_SPURIOUS'
    elif not coeff_equal:
        cls='K5_S5_COMPONENT1_DEFECT_SUPPORT_COEFFICIENT'
    else:
        cls='K5_S5_COMPONENT1_SUPPORT_MIXING_EXACT'

    out={
        'gate':'K5_34_ORBIT_COMPONENT1_SUPPORT_MIXING_DEFECT_DIAGNOSTIC_CONTROL_REPAIR_1',
        'parent_prereg_commit':PARENT_PRE,
        'repair_prereg_commit':REPAIR_PRE,
        'classification':cls,
        'scientific_verdict':None,
        'frozen':{'mask':1,'ray':'W1','cycle':list(P),'matching':FROZEN,'component':COMPONENT},
        'stage_equalities':{
            'canonical_nonzero_support':bool(base[COMPONENT]),
            'AinvT_target_component_support':bool(pred),
            'full_transported_32vector_nonzero_components':sum(bool(d) for d in transported),
            'direct_projected_target_support':bool(direct),
            'support_index_equality':support_equal,
            'coefficient_equality':coeff_equal,
        },
        'mixing_control':{
            'contributor_count':len(contributors),
            'contributor_indices':contributor_indices,
            'contributor_coefficients':contributor_coefficients,
            'dropped_index':contributors[0][0] if contributors else None,
            'dropped_contributor_rejected':dropped_rejected,
        },
        'first_missing_support_index':repr(missing[0]) if missing else None,
        'first_spurious_support_index':repr(spurious[0]) if spurious else None,
        'first_coefficient_mismatch':repr(coeff_bad) if coeff_bad is not None else None,
        'validity':validity,
        'control_component_wrong_transpose':ctrl,
        'cardinalities':{
            'canonical_component_support':len(base[COMPONENT]),
            'AinvT_target_support':len(pred),
            'direct_target_support':len(direct),
        },
        'hashes':{'AinvT_target':H(pred),'direct_target':H(direct)},
        'no_N_B_orders_or_coefficients_recorded':True,
        'invalid_resolver_values_consumed':False,
        'q18_values_consumed':False,
        'interpretation_ceiling':'implementation diagnosis only; resolver authority remains 0/64 pending separate repair and validation',
    }

    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('CLASSIFICATION='+cls)
    print('MIXING='+json.dumps(out['mixing_control'],sort_keys=True))
    print('STAGES='+json.dumps(out['stage_equalities'],sort_keys=True))
    return 2 if cls=='INVALID_IMPLEMENTATION_OR_PROVENANCE' else 0

if __name__=='__main__':
    raise SystemExit(main())
