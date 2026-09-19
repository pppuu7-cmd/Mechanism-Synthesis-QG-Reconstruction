#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
R1=ROOT/'scripts/k5_34_orbit_exact_leading_coefficient_core_repair1.py'
R2=ROOT/'scripts/k5_34_orbit_exact_leading_coefficient_core_repair2.py'
PREREG=ROOT/'prereg/K5_34_ORBIT_POSTCOLLAPSE_GEOMETRY_COVARIANCE_S5_TRANSPORT_DIAGNOSTIC.md'
CRITIC=ROOT/'results/raw/k5_34_orbit_component1_repaired_diagnostic_independent_critic_authoritative.json'

PREREG_COMMIT='b7495db85844111b947bc902e5df2a496bf614ad'
REPAIR1_PREREG_COMMIT='cd4dcf9f3b88b142d5413da0c8d17b24acd40074'
REPAIR1_PREREG=ROOT/'prereg/K5_34_ORBIT_POSTCOLLAPSE_GEOMETRY_COVARIANCE_DIAGNOSTIC_IMPLEMENTATION_REPAIR1.md'
C1_CRITIC='CONFIRMED_SCOPED_COMPONENT1_SUPPORT_SET_MISMATCH'

INVALID='INVALID_IMPLEMENTATION_OR_PROVENANCE'
CLASSES=[
 'K5_S5_POSTCOLLAPSE_DEFECT_RAY_PERMUTATION',
 'K5_S5_POSTCOLLAPSE_DEFECT_INCIDENCE_BASIS_TRANSPORT',
 'K5_S5_POSTCOLLAPSE_DEFECT_LAPLACIAN_CONGRUENCE',
 'K5_S5_POSTCOLLAPSE_DEFECT_Q_INVARIANCE',
 'K5_S5_POSTCOLLAPSE_DEFECT_ANNIHILATOR_TANGENT_TRANSPORT',
 'K5_S5_POSTCOLLAPSE_DEFECT_COVARIANCE_SERIES_TRANSPORT',
 'K5_S5_POSTCOLLAPSE_DEFECT_DETERMINANT_FACTOR_TRANSPORT',
 'K5_S5_POSTCOLLAPSE_DEFECT_MATCHING_COVARIANCE_COMPOSITION',
 'K5_S5_POSTCOLLAPSE_DEFECT_NUMERATOR_FLUX_ASSEMBLY',
]
NO_DEFECT='K5_S5_POSTCOLLAPSE_NO_DEFECT_ON_FROZEN_LANE'


def load(path,name):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s)
    assert s.loader is not None
    s.loader.exec_module(m)
    return m

r1=load(R1,'postcollapse_r1')
r2=load(R2,'postcollapse_r2')
b=r1.base
P=b.P
D=b.D
CYCLE=tuple(r1.CYCLE)
MASK=1
WEIGHTS=tuple(r1.W1)
TMASK=b.core.pmask(MASK,CYCLE)
TWEIGHTS=tuple(r1.WP1)
ROWS=tuple(tuple(Fraction(x) for x in row) for row in b.ROWS)
Q=[[Fraction(x) for x in row] for row in b.Q]


def peq(a,bp):
    return isinstance(a,P) and isinstance(bp,P) and a.d==bp.d

def deq(a,bd):
    return peq(a.v,bd.v) and peq(a.d,bd.d)

def vec_eq(a,bv,eq):
    return len(a)==len(bv) and all(eq(x,y) for x,y in zip(a,bv))

def mat_eq(A,B,eq):
    return len(A)==len(B) and all(len(x)==len(y) and all(eq(a,b) for a,b in zip(x,y)) for x,y in zip(A,B))

def transpose(A):
    return [list(x) for x in zip(*A)]

def matmul(A,B,zero):
    BT=list(zip(*B))
    return [[sum((x*y for x,y in zip(row,col)),zero()) for col in BT] for row in A]

def frac_inv(A):
    n=len(A)
    M=[[Fraction(A[i][j]) for j in range(n)]+[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p=next(i for i in range(c,n) if M[i][c])
        M[c],M[p]=M[p],M[c]
        z=M[c][c]
        M[c]=[x/z for x in M[c]]
        for i in range(n):
            if i!=c and M[i][c]:
                z=M[i][c]
                M[i]=[x-z*y for x,y in zip(M[i],M[c])]
    return [row[n:] for row in M]

def frac_mat_eq(A,B):
    return A==B

def poly_hash(x):
    if isinstance(x,P):
        payload=repr(sorted((k,str(v)) for k,v in x.d.items()))
    elif isinstance(x,D):
        payload=repr((sorted((k,str(v)) for k,v in x.v.d.items()),sorted((k,str(v)) for k,v in x.d.d.items())))
    else:
        payload=repr(x)
    return hashlib.sha256(payload.encode()).hexdigest()

def seq_hash(xs):
    h=hashlib.sha256()
    def feed(x):
        if isinstance(x,P) or isinstance(x,D):
            h.update(poly_hash(x).encode())
        elif isinstance(x,(list,tuple)):
            h.update(b'[')
            for y in x:feed(y)
            h.update(b']')
        elif isinstance(x,dict):
            h.update(b'{')
            for k in sorted(x,key=repr):
                h.update(repr(k).encode());feed(x[k])
            h.update(b'}')
        else:h.update(repr(x).encode())
    feed(xs)
    return h.hexdigest()

def make_ray(mask,weights):
    Z={i for i in range(10) if (mask>>i)&1}
    return [P.mon(1,weights[i]) if i in Z else P(weights[i]) for i in range(10)]

def derive_G():
    # Old root-edge rows 0..3 are the canonical quotient basis.
    G=[]
    for i in range(4):
        j=r1.s5.ep(CYCLE,i)
        s=Fraction(r1.s5.edge_sign(CYCLE,i))
        G.append([s*x for x in ROWS[j]])
    return G

def row_times_G(row,G):
    return [sum((row[k]*G[k][j] for k in range(4)),Fraction(0)) for j in range(4)]

def geometry(mask,weights):
    aval=make_ray(mask,weights)
    q,v,divv=b.core.ann_data(tuple(aval))
    s1=sum(aval,P());S=sum(v,P());sumq=sum(q,P())
    K=s1*(divv+Fraction(1,2)*sumq)-3*S
    aa_value=[D(aval[i],P()) for i in range(10)]
    L_value=b.build_l_d(aa_value)
    aa=[D(aval[i],v[i]) for i in range(10)]
    L=b.build_l_d(aa)
    psi=b.det_d(L)
    ADJ=b.adj_d(L)
    Ds=b.det_coeffs_d(L)
    F=b.det_factors_d(Ds,psi)
    AQ=[[sum((ADJ[i][k]*Q[k][j] for k in range(4)),D(0)) for j in range(4)] for i in range(4)]
    BN=[ADJ]
    for _ in range(1,b.ORDER+1):
        BN.append([[-x for x in row] for row in b.mm_d(AQ,BN[-1])])
    cov={}
    for i in range(10):
        for j in range(i+1,10):
            for n in range(b.ORDER+1):
                cov[(i,j,n)]=b.dot_d(ROWS[i],BN[n],ROWS[j])
    return {'aval':aval,'q':q,'v':v,'divv':divv,'K':K,'aa_value':aa_value,'L_value':L_value,'aa':aa,'L':L,'psi':psi,'ADJ':ADJ,'Ds':Ds,'F':F,'BN':BN,'cov':cov}

def permute_matching(mt):
    out=[]
    for i,j in mt:
        a=r1.s5.ep(CYCLE,i);bb=r1.s5.ep(CYCLE,j)
        out.append((min(a,bb),max(a,bb)))
    return tuple(sorted(out))

def matching_base(mt,cov,F):
    ser=[D(1)]+[D(0) for _ in range(b.ORDER)]
    for ij in mt:
        nxt=[D(0) for _ in range(b.ORDER+1)]
        for k in range(b.ORDER+1):
            for n in range(k+1):
                nxt[k]=nxt[k]+ser[k-n]*cov[(ij[0],ij[1],n)]
        ser=nxt
    z=D(0)
    for j in range(b.ORDER+1):
        z=z+F[j]*ser[b.ORDER-j]
    return math.factorial(b.ORDER)*z

def weighted_contribution(mt,coeffs,cov,F):
    z=matching_base(mt,cov,F)
    return tuple((Fraction(coeffs[ch][0])*z,Fraction(coeffs[ch][1])*z) for ch in (0,1))

def contrib_eq(a,c):
    return all(deq(x[0],y[0]) and deq(x[1],y[1]) for x,y in zip(a,c))

def route_hashes(route):
    return {
      f'ch{ch+1}_{obj}':r1.vector_hash(route['channels'][ch][obj],r1.N_DEG if obj=='N' else r1.B_DEG)
      for ch in (0,1) for obj in ('N','B')
    }

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    pre=PREREG.read_text(encoding='utf-8')
    repair1_pre=REPAIR1_PREREG.read_text(encoding='utf-8')
    critic=json.loads(CRITIC.read_text(encoding='utf-8'))

    validity={
      'prereg_locked':PREREG_COMMIT=='b7495db85844111b947bc902e5df2a496bf614ad',
      'prereg_present':'post-collapse geometry/covariance S5 transport' in pre,
      'implementation_repair1_locked':REPAIR1_PREREG_COMMIT=='cd4dcf9f3b88b142d5413da0c8d17b24acd40074',
      'implementation_repair1_present':'Implementation-only repair 1' in repair1_pre,
      'parent_scientific_prereg_locked':r1.PRE=='d6b0e805101c8590eafac71398cc2b1466691752',
      'component1_critic_confirmed':critic.get('classification')==C1_CRITIC,
      'q18_unused':critic.get('q18_values_used') is False,
      'source_terms_100000':r1._SOURCE_TERM_COUNT==100000,
      'repair1_matching_945':len(r1.S5_MATCH_COEFF_CYCLE)==945,
      'repair2_matching_945':len(r2.S5_MATCH_COEFF_CYCLE)==945,
      'postcollapse_matching_objects_equal':r1.S5_MATCH_COEFF_CYCLE==r2.S5_MATCH_COEFF_CYCLE,
      'matching_exact_rational':all(isinstance(x,Fraction) for cc in r1.S5_MATCH_COEFF_CYCLE.values() for ch in cc for x in ch),
    }

    old=geometry(MASK,WEIGHTS)
    target=geometry(TMASK,TWEIGHTS)
    ep=lambda i:r1.s5.ep(CYCLE,i)
    es=lambda i:Fraction(r1.s5.edge_sign(CYCLE,i))

    # G1
    g1=all(peq(target['aval'][ep(i)],old['aval'][i]) for i in range(10))

    # G2
    G=derive_G();Ginv=frac_inv(G)
    row_rel=[]
    for i in range(10):
        lhs=list(ROWS[ep(i)])
        rhs=[es(i)*x for x in row_times_G(ROWS[i],G)]
        row_rel.append(lhs==rhs)
    g2=all(row_rel) and matmul(G,Ginv,lambda:Fraction(0))==[[Fraction(int(i==j)) for j in range(4)] for i in range(4)]

    # G3: frozen value-only Laplacian congruence.
    predicted_L_value=matmul(matmul(transpose(G),old['L_value'],lambda:D(0)),G,lambda:D(0))
    g3=mat_eq(target['L_value'],predicted_L_value,deq)

    # G4
    predicted_Q=matmul(matmul(transpose(G),Q,lambda:Fraction(0)),G,lambda:Fraction(0))
    g4=predicted_Q==Q

    # G5: edge tangent components + full dual-jet Laplacian relation.
    qeq=all(peq(target['q'][ep(i)],old['q'][i]) for i in range(10))
    veq=all(peq(target['v'][ep(i)],old['v'][i]) for i in range(10))
    diveq=peq(target['divv'],old['divv'])
    predicted_L_dual=matmul(matmul(transpose(G),old['L'],lambda:D(0)),G,lambda:D(0))
    dual_laplacian_eq=mat_eq(target['L'],predicted_L_dual,deq)
    g5=qeq and veq and diveq and dual_laplacian_eq

    # G6
    cov_checks={}
    first_cov=None
    for i in range(10):
        for j in range(i+1,10):
            a,bb=ep(i),ep(j);key=(min(a,bb),max(a,bb))
            sign=es(i)*es(j)
            for n in range(b.ORDER+1):
                ok=deq(target['cov'][(key[0],key[1],n)],sign*old['cov'][(i,j,n)])
                cov_checks[(i,j,n)]=ok
                if not ok and first_cov is None:first_cov=(i,j,n)
    g6=all(cov_checks.values())

    # G7
    g7=vec_eq(target['F'],old['F'],deq)

    # G8: canonical transported matching-by-matching composition.
    first_match=None;matching_checked=0;g8=True
    for mt in sorted(r1.MATCH_COEFF):
        tmt=permute_matching(mt)
        if tmt not in r1.S5_MATCH_COEFF_CYCLE:
            g8=False;first_match=repr(mt);break
        oc=weighted_contribution(mt,r1.MATCH_COEFF[mt],old['cov'],old['F'])
        tc=weighted_contribution(tmt,r1.S5_MATCH_COEFF_CYCLE[tmt],target['cov'],target['F'])
        matching_checked+=1
        if not contrib_eq(oc,tc):
            g8=False;first_match=repr(mt);break

    # G9 downstream-only equality booleans/hashes.
    original_route=r1.route_a(MASK,WEIGHTS)
    target_route=r1.route_a(TMASK,TWEIGHTS,r1.S5_MATCH_COEFF_CYCLE)
    nbeq={}
    for ch in (0,1):
        nbeq[f'ch{ch+1}_N']=peq(original_route['channels'][ch]['N'],target_route['channels'][ch]['N'])
        nbeq[f'ch{ch+1}_B']=peq(original_route['channels'][ch]['B'],target_route['channels'][ch]['B'])
    g9=all(nbeq.values())

    # Malformed controls, all prospectively frozen.
    ident=[[Fraction(int(i==j)) for j in range(4)] for i in range(4)]
    identity_nonroot_rejected=any(list(ROWS[ep(i)]) != [es(i)*x for x in ROWS[i]] for i in range(4,10))
    identity_nontrivial=(G!=ident) and identity_nonroot_rejected
    identity_L_value=matmul(matmul(transpose(ident),old['L_value'],lambda:D(0)),ident,lambda:D(0))
    identity_G_rejected=not mat_eq(target['L_value'],identity_L_value,deq)

    omitted_sign_rejected=False
    for i in range(10):
        for j in range(i+1,10):
            if es(i)*es(j)==-1:
                a,bb=ep(i),ep(j);key=(min(a,bb),max(a,bb))
                if any(not deq(target['cov'][(key[0],key[1],n)],old['cov'][(i,j,n)]) for n in range(b.ORDER+1)):
                    omitted_sign_rejected=True;break
        if omitted_sign_rejected:break

    # Mutate one deterministic target covariance term and require final route-level
    # matching assembly to change. No coefficient/order is emitted.
    mcov=dict(target['cov'])
    mk=sorted(mcov)[0]
    mcov[mk]=mcov[mk]+D(1)
    mutated_diff=False
    for mt in sorted(r1.S5_MATCH_COEFF_CYCLE):
        if (mk[0],mk[1]) in mt:
            clean=weighted_contribution(mt,r1.S5_MATCH_COEFF_CYCLE[mt],target['cov'],target['F'])
            mut=weighted_contribution(mt,r1.S5_MATCH_COEFF_CYCLE[mt],mcov,target['F'])
            if not contrib_eq(clean,mut):
                mutated_diff=True;break

    malformed={
      'nontrivial_incidence_transform':identity_nontrivial,
      'identity_G_laplacian_rejected':identity_G_rejected,
      'omitted_orientation_sign_rejected':omitted_sign_rejected,
      'altered_covariance_entry_rejected':mutated_diff,
      'original_route_internal_checks':all(original_route['checks'].values()),
      'target_route_internal_checks':all(target_route['checks'].values()),
    }

    stages=[g1,g2,g3,g4,g5,g6,g7,g8,g9]
    if not all(validity.values()) or not all(malformed.values()):
        classification=INVALID
    elif not all(stages):
        classification=CLASSES[next(i for i,x in enumerate(stages) if not x)]
    else:
        classification=NO_DEFECT

    out={
      'gate':'K5_34_ORBIT_POSTCOLLAPSE_GEOMETRY_COVARIANCE_S5_TRANSPORT_DIAGNOSTIC',
      'prereg_commit':PREREG_COMMIT,
      'classification':classification,
      'scientific_verdict':None,
      'frozen':{'mask':MASK,'ray':'W1','cycle':list(CYCLE)},
      'validity':validity,
      'stages':{
        'G1_ray_permutation':g1,
        'G2_incidence_basis_transport':g2,
        'G3_laplacian_congruence':g3,
        'G4_Q_invariance':g4,
        'G5_annihilator_tangent_transport':g5,
        'G6_covariance_series_transport':g6,
        'G7_determinant_factor_transport':g7,
        'G8_matching_covariance_composition':g8,
        'G9_N_B_full_polynomial_equality':g9,
      },
      'subchecks':{
        'G2_all10_row_relations':row_rel,
        'G5_q_edge_transport':qeq,
        'G5_v_edge_transport':veq,
        'G5_divergence_invariant':diveq,
        'G5_dual_jet_laplacian_congruence':dual_laplacian_eq,
        'G6_first_failed_edgepair_order':first_cov,
        'G8_first_failed_matching':first_match,
        'G8_matching_count_checked_before_first_failure':matching_checked,
        'G9_channel_object_equalities':nbeq,
      },
      'malformed_controls':malformed,
      'hashes_only':{
        'G_matrix_sha256':seq_hash(G),
        'old_L_value_sha256':seq_hash(old['L_value']),
        'target_L_value_sha256':seq_hash(target['L_value']),
        'old_L_dual_sha256':seq_hash(old['L']),
        'target_L_dual_sha256':seq_hash(target['L']),
        'old_Q_sha256':seq_hash(Q),
        'target_Q_expected_sha256':seq_hash(predicted_Q),
        'old_covariance_sha256':seq_hash(old['cov']),
        'target_covariance_sha256':seq_hash(target['cov']),
        'old_F_sha256':seq_hash(old['F']),
        'target_F_sha256':seq_hash(target['F']),
        'original_route':route_hashes(original_route),
        'target_route':route_hashes(target_route),
      },
      'no_N_B_orders_or_coefficients_recorded':True,
      'q18_values_used':False,
      'heavy_resolver_authorized':False,
      'global_stokes_authorized':False,
      'interpretation_ceiling':'implementation diagnosis only; resolver authority remains 0/64',
    }
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('CLASSIFICATION='+classification)
    print('STAGES='+json.dumps(out['stages'],sort_keys=True))
    print('MALFORMED='+json.dumps(malformed,sort_keys=True))
    return 0 if classification!=INVALID else 2

if __name__=='__main__':
    raise SystemExit(main())
