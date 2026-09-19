#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, importlib.util, json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PARENT=ROOT/'scripts/k5_34_orbit_postcollapse_geometry_covariance_s5_transport_diagnostic.py'
PREREG=ROOT/'prereg/K5_34_ORBIT_G8_MATCHING_COVARIANCE_COMPOSITION_DIAGNOSTIC.md'
AUTH=ROOT/'results/raw/k5_34_orbit_postcollapse_geometry_covariance_s5_transport_diagnostic_repair1_authoritative.json'
PREREG_COMMIT='a9781b3c6b61ecaa1940ae796ae0a68b9b29c9b6'
AUTH_COMMIT='3ec5862258da84c25309c8ee091e6b752a246f66'
EXPECTED_PARENT='K5_S5_POSTCOLLAPSE_DEFECT_MATCHING_COVARIANCE_COMPOSITION'
MT=((0,1),(2,3),(4,5),(6,7),(8,9))

CLASSES=[
 'K5_G8_DEFECT_EDGE_PAIR_PERMUTATION',
 'K5_G8_DEFECT_ORIENTATION_COCYCLE_SIGN',
 'K5_G8_DEFECT_COVARIANCE_INDEX_CONVENTION',
 'K5_G8_DEFECT_PER_PAIR_COVARIANCE_FACTOR',
 'K5_G8_DEFECT_ORDERED_PRODUCT_ASSEMBLY',
 'K5_G8_DEFECT_FACTOR_MULTISET_ASSEMBLY',
 'K5_G8_DEFECT_FINAL_MATCHING_CONTRIBUTION',
]
EXACT='K5_G8_FROZEN_MATCHING_COMPOSITION_EXACT'
INVALID='INVALID_IMPLEMENTATION_OR_PROVENANCE'

def load(path,name):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s)
    assert s.loader is not None
    s.loader.exec_module(m)
    return m

p=load(PARENT,'g8_parent')
r1=p.r1
D=p.D

def mul_series(a,b):
    out=[D(0) for _ in range(p.b.ORDER+1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=p.b.ORDER:
                out[i+j]=out[i+j]+x*y
    return out

def series_eq(a,b):
    return len(a)==len(b) and all(p.deq(x,y) for x,y in zip(a,b))

def factor_series(cov,key):
    return [cov[(key[0],key[1],n)] for n in range(p.b.ORDER+1)]

def scale_series(q,s):
    return [Fraction(q)*x for x in s]

def coeff_hash(c):
    return hashlib.sha256(repr(c).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args()
    prereg=PREREG.read_text(encoding='utf-8')
    auth=json.loads(AUTH.read_text(encoding='utf-8'))

    validity={
      'g8_prereg_locked': PREREG_COMMIT=='a9781b3c6b61ecaa1940ae796ae0a68b9b29c9b6',
      'g8_prereg_present': 'G8 matching-covariance composition diagnostic' in prereg,
      'corrected_parent_authority_commit_locked': AUTH_COMMIT=='3ec5862258da84c25309c8ee091e6b752a246f66',
      'corrected_parent_classification': auth.get('classification')==EXPECTED_PARENT,
      'corrected_parent_run_locked': auth.get('provenance',{}).get('run_id')==35407837027,
      'corrected_parent_G1_G7_pass': all(auth.get('stages',{}).get(k) is True for k in (
          'G1_ray_permutation','G2_incidence_basis_transport','G3_laplacian_congruence',
          'G4_Q_invariance','G5_annihilator_tangent_transport','G6_covariance_series_transport',
          'G7_determinant_factor_transport')),
      'corrected_parent_first_matching_locked': auth.get('subchecks',{}).get('G8_first_failed_matching')==repr(MT),
      'parent_q18_unused': auth.get('q18_values_used') is False,
      'matching_census_945': len(r1.MATCH_COEFF)==945 and len(r1.S5_MATCH_COEFF_CYCLE)==945,
      'source_terms_100000': r1._SOURCE_TERM_COUNT==100000,
    }

    old=p.geometry(p.MASK,p.WEIGHTS)
    target=p.geometry(p.TMASK,p.TWEIGHTS)
    ep=lambda i:r1.s5.ep(p.CYCLE,i)
    es=lambda i:Fraction(r1.s5.edge_sign(p.CYCLE,i))

    mapped=[]
    pair_sign=[]
    for i,j in MT:
        a,b=ep(i),ep(j)
        mapped.append((min(a,b),max(a,b)))
        pair_sign.append(es(i)*es(j))
    TMT=tuple(sorted(mapped))

    # H1: exact forward edge-pair permutation/canonicalization + roundtrip.
    h1=TMT==p.permute_matching(MT)
    inv_edge={ep(i):i for i in range(10)}
    roundtrip=tuple(sorted((min(inv_edge[a],inv_edge[b]),max(inv_edge[a],inv_edge[b])) for a,b in TMT))
    canonical_roundtrip=(roundtrip==MT)
    h1=h1 and canonical_roundtrip

    # H2: orientation cocycle. Edge action followed by inverse action must return +1.
    inv=[0]*5
    for i,j in enumerate(p.CYCLE): inv[j]=i
    edge_cocycle=[es(i)*Fraction(r1.s5.edge_sign(tuple(inv),ep(i)))==1 for i in range(10)]
    h2=all(s in (Fraction(1),Fraction(-1)) for s in pair_sign) and all(edge_cocycle)

    # H3/H4: forward target-index convention and exact per-pair covariance transport.
    forward_keys=[]
    factor_checks=[]
    for (i,j),sgn in zip(MT,pair_sign):
        a,b=ep(i),ep(j); key=(min(a,b),max(a,b)); forward_keys.append(key)
        oldser=factor_series(old['cov'],(i,j))
        tarser=factor_series(target['cov'],key)
        factor_checks.append(series_eq(tarser,scale_series(sgn,oldser)))
    h3=tuple(sorted(forward_keys))==TMT and all(k in [(i,j) for i in range(10) for j in range(i+1,10)] for k in forward_keys)
    h4=all(factor_checks)

    # H5: ordered product of the five predicted transported factors.
    pred_factors=[]; actual_factors=[]
    for (ij,key,sgn) in zip(MT,forward_keys,pair_sign):
        pred_factors.append(scale_series(sgn,factor_series(old['cov'],ij)))
        actual_factors.append(factor_series(target['cov'],key))
    pred_prod=[D(1)]+[D(0) for _ in range(p.b.ORDER)]
    actual_prod=[D(1)]+[D(0) for _ in range(p.b.ORDER)]
    for x,y in zip(pred_factors,actual_factors):
        pred_prod=mul_series(pred_prod,x); actual_prod=mul_series(actual_prod,y)
    h5=series_eq(pred_prod,actual_prod)

    # H6: permutation-insensitive factor multiset equality via exact canonical hashes.
    pred_hashes=sorted(p.seq_hash(x) for x in pred_factors)
    actual_hashes=sorted(p.seq_hash(x) for x in actual_factors)
    h6=(pred_hashes==actual_hashes)

    # H7: final frozen matching contribution, exactly the parent G8 comparison.
    old_coeff=r1.MATCH_COEFF[MT]
    target_coeff=r1.S5_MATCH_COEFF_CYCLE[TMT]
    old_base=p.matching_base(MT,old['cov'],old['F'])
    target_base=p.matching_base(TMT,target['cov'],target['F'])
    old_contrib=p.weighted_contribution(MT,old_coeff,old['cov'],old['F'])
    target_contrib=p.weighted_contribution(TMT,target_coeff,target['cov'],target['F'])
    h7=p.contrib_eq(old_contrib,target_contrib)

    total_pair_sign=Fraction(1)
    for s in pair_sign: total_pair_sign*=s
    geometry_base_expected=p.deq(target_base,total_pair_sign*old_base)
    coeff_direct_equal=(old_coeff==target_coeff)
    coeff_total_sign_equal=(tuple(tuple(total_pair_sign*x for x in ch) for ch in old_coeff)==target_coeff)

    # Frozen malformed controls.
    omitted_sign_rejected=False
    for ij,key,sgn in zip(MT,forward_keys,pair_sign):
        if sgn==-1 and not series_eq(factor_series(target['cov'],key),factor_series(old['cov'],ij)):
            omitted_sign_rejected=True
            break

    # Wrong pullback convention: apply inverse edge map to old edge indices as though they were target indices.
    wrong_keys=[]
    for i,j in MT:
        a=r1.s5.ep(tuple(inv),i); b=r1.s5.ep(tuple(inv),j)
        wrong_keys.append((min(a,b),max(a,b)))
    covariance_index_mutation_rejected=any(w!=c for w,c in zip(wrong_keys,forward_keys))
    if covariance_index_mutation_rejected:
        covariance_index_mutation_rejected=any(
            not series_eq(factor_series(target['cov'],wk),factor_series(target['cov'],ck))
            for wk,ck in zip(wrong_keys,forward_keys)
        )

    # Swap one target endpoint between the first two pairs.
    (a,b),(c,d)=forward_keys[0],forward_keys[1]
    swapped0=(min(a,c),max(a,c)); swapped1=(min(b,d),max(b,d))
    swapped_pair_rejected=(swapped0!=forward_keys[0] or swapped1!=forward_keys[1]) and (
        not series_eq(factor_series(target['cov'],swapped0),factor_series(target['cov'],forward_keys[0]))
        or not series_eq(factor_series(target['cov'],swapped1),factor_series(target['cov'],forward_keys[1]))
    )

    malformed={
      'omitted_orientation_sign_rejected': omitted_sign_rejected,
      'covariance_inverse_pullback_mutation_rejected': covariance_index_mutation_rejected,
      'swapped_edge_pair_rejected': swapped_pair_rejected,
      'canonicalize_pair_roundtrip_all5': canonical_roundtrip,
    }

    stages=[h1,h2,h3,h4,h5,h6,h7]
    if not all(validity.values()) or not all(malformed.values()):
        classification=INVALID
    elif not all(stages):
        classification=CLASSES[next(i for i,x in enumerate(stages) if not x)]
    else:
        classification=EXACT

    out={
      'gate':'K5_34_ORBIT_G8_MATCHING_COVARIANCE_COMPOSITION_DIAGNOSTIC',
      'classification':classification,
      'scientific_verdict':None,
      'prereg_commit':PREREG_COMMIT,
      'corrected_parent_authority_commit':AUTH_COMMIT,
      'frozen':{'mask':1,'ray':'W1','cycle':list(p.CYCLE),'matching':repr(MT)},
      'validity':validity,
      'stages':{
        'H1_edge_pair_permutation':h1,
        'H2_orientation_cocycle_sign':h2,
        'H3_covariance_index_convention':h3,
        'H4_per_pair_covariance_factor':h4,
        'H5_ordered_product_assembly':h5,
        'H6_factor_multiset_assembly':h6,
        'H7_final_matching_contribution':h7,
      },
      'subchecks':{
        'pair_signs':[int(x) for x in pair_sign],
        'total_pair_sign':int(total_pair_sign),
        'per_pair_factor_equalities':factor_checks,
        'geometry_base_transport_exact':geometry_base_expected,
        'source_matching_coeff_direct_equal':coeff_direct_equal,
        'source_matching_coeff_total_pair_sign_equal':coeff_total_sign_equal,
      },
      'malformed_controls':malformed,
      'hashes_only':{
        'old_coeff_sha256':coeff_hash(old_coeff),
        'target_coeff_sha256':coeff_hash(target_coeff),
        'predicted_factor_multiset_sha256':hashlib.sha256(repr(pred_hashes).encode()).hexdigest(),
        'actual_factor_multiset_sha256':hashlib.sha256(repr(actual_hashes).encode()).hexdigest(),
        'old_base_sha256':p.seq_hash(old_base),
        'target_base_sha256':p.seq_hash(target_base),
      },
      'q18_values_used':False,
      'N_B_orders_or_coefficients_used':False,
      'heavy_resolver_authorized':False,
      'global_stokes_authorized':False,
      'interpretation_ceiling':'implementation diagnosis only; resolver authority remains 0/64',
    }
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('CLASSIFICATION='+classification)
    print('STAGES='+json.dumps(out['stages'],sort_keys=True))
    print('SUBCHECKS='+json.dumps(out['subchecks'],sort_keys=True))
    print('MALFORMED='+json.dumps(malformed,sort_keys=True))
    return 0 if classification!=INVALID else 2

if __name__=='__main__':
    raise SystemExit(main())
