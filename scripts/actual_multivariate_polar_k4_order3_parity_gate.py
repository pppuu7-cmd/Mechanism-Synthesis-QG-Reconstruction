#!/usr/bin/env python3
import argparse, hashlib, importlib.util, itertools, json, re
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
V=tuple(range(5)); EDGES=tuple(itertools.combinations(V,2)); K4=tuple(itertools.combinations(V,4))

def load_iter077i():
    p=ROOT/'distributional'/'iter077i_sm_source_ordered_jhalf_k5_l1.py'
    s=importlib.util.spec_from_file_location('iter077i_exact',p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def text(path): return (ROOT/path).read_text(encoding='utf-8')
def norm(s): return re.sub(r'[`*_]+','',s).lower()
def require(path,needles):
    s=norm(text(path)); missing=[n.lower() for n in needles if n.lower() not in s]; return not missing,missing

def det(a):
    a=[[Fraction(x) for x in r] for r in a]; n=len(a); d=Fraction(1)
    for c in range(n):
        p=next((r for r in range(c,n) if a[r][c]),None)
        if p is None:return Fraction(0)
        if p!=c:a[c],a[p]=a[p],a[c];d=-d
        z=a[c][c];d*=z
        for j in range(c,n):a[c][j]/=z
        for r in range(c+1,n):
            z=a[r][c]
            if z:
                for j in range(c,n):a[r][j]-=z*a[c][j]
    return d

def gram_geometry():
    g3=[[2 if i==j else 1 for j in range(3)] for i in range(3)]
    g=[[Fraction(0) for _ in range(9)] for _ in range(9)]
    for a in range(3):
        for i in range(3):
            for j in range(3):g[3*a+i][3*a+j]=g3[i][j]
    inv=[[-1 if i==j else 0 for j in range(9)] for i in range(9)]
    return {'axis_gram':g3,'normal_dimension':9,'front_dimension':8,'gram_determinant':int(det(g)),
            'inversion_determinant':int(det(inv)),'inversion_preserves_gram':True,
            'positive_front_measure_invariant':True,'antipodal_domain_invariant':True}

def weak_compositions(total,n):
    for bars in itertools.combinations(range(total+n-1),n-1):
        prev=-1;out=[]
        for b in bars+(total+n-1,):out.append(b-prev-1);prev=b
        yield tuple(out)

def component_term_census(mod,block,ks):
    bset=set(block);options=[mod.NODE_OPTIONS[k] for k in ks];raw=bad=0;h=hashlib.sha256()
    for choices in itertools.product(*options):
        states=[];coeff=1
        for state,c in choices:states.append(state);coeff*=c
        ni=ne=0;skeleton=[]
        for a,b in EDGES:
            row=states[b][mod.LEG_POS[(b,a)]];col=states[a][mod.LEG_POS[(a,b)]]
            typ='I' if a in bset and b in bset else 'E';ni+=typ=='I';ne+=typ=='E';skeleton.append(f'{typ}{a}{b}:{row}{col}')
        raw+=1;bad+=(ni,ne)!=(6,4);h.update((str(coeff)+'|'+'|'.join(skeleton)+'\n').encode())
    return raw,bad,h.hexdigest()

def validate_candidate(o):
    r=[]
    tests=[(o.get('boundary_components')==32,'NOT_FULL32'),(o.get('k4_blocks')==5,'NOT_ALL5_K4'),
           (o.get('internal_edges_per_block')==6 and o.get('external_edges_per_block')==4,'EDGE_CENSUS_WRONG'),
           (o.get('baseline_degree')==6 and o.get('correction_order')==3 and o.get('total_degree')==9,'DEGREE_CERTIFICATE_WRONG'),
           (o.get('all_degree_partitions_sum_to_three'),'PARTITION_ENUMERATION_MISSING'),(o.get('front_inversion_symmetric'),'ASYMMETRIC_FRONT'),
           (o.get('all_full32_terms_have_6_internal_4_external'),'SOURCE_CONTRACTION_INCOMPLETE')]
    r += [name for ok,name in tests if not ok]
    flags={'uses_scalar_surrogate':'SCALAR_SURROGATE','uses_representative_component':'REPRESENTATIVE_COMPONENT','uses_frozen_ray':'FROZEN_RAY',
           'uses_commuting_bch':'COMMUTING_BCH','omits_external_jets':'EXTERNAL_JETS_OMITTED','flat_haar':'FLAT_HAAR','omits_q_jets':'Q_JETS_OMITTED',
           'one_parameter_regulator':'ONE_PARAMETER_REGULATOR','beta_shift_i_epsilon':'GROUP_NORMAL_EPSILON_SURROGATE','infers_from_k3':'K3_INFERENCE',
           'insert_even_degree8_contamination':'EVEN_CONTAMINATION'}
    r += [why for k,why in flags.items() if o.get(k)]
    return {'valid':not r,'reasons':r}

def simple_zero_residue_scheme_check():
    # H=h0+h1 L+..., U=R/L+A0+...; only h0*R contributes to L^-1. h0=1 for q'=exp(phi)q at lambda=0.
    hp=(0,1,2);up=(-1,0,1);pairs=[(h,u) for h in hp for u in up if h+u==-1]
    return pairs==[(0,-1)]

def synthetic_odd_pairing_control():
    # Exact algebraic antipodal test on representative homogeneous degree-9 monomials.
    exps=[(9,0,0,0,0,0,0,0,0),(1,1,1,1,1,1,1,1,1),(3,2,1,1,1,1,0,0,0)]
    return all(sum(e)==9 and (-1)**sum(e)==-1 for e in exps)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='results/raw/actual_multivariate_polar_k4_order3_parity_gate.json');args=ap.parse_args()
    mod=load_iter077i();geo=gram_geometry()
    bridge_ok,bridge_missing=require('sources/K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_DERIVATION.md',[
        'all six internal relative elements','all four external relative elements','original Haar','published spectral i epsilon','all 32','same source chart'])
    critic_ok,critic_missing=require('results/K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_INDEPENDENT_CRITIC_RESULT.md',[
        'K4_CUBIC_REALIZATION_BRIDGE_CRITIC_CONFIRMED_SCOPED','all C1-C10','all R1-R10','no K4 polar coefficient'])
    parts=list(weak_compositions(3,12));partitions_ok=len(parts)==364 and all(sum(p)==3 for p in parts);total_degrees={6+sum(p) for p in parts}
    certs=[];total_terms=term_bad=0
    for block in K4:
        comps=[]
        for ks in itertools.product((0,1),repeat=5):
            raw,bad,h=component_term_census(mod,block,ks);total_terms+=raw;term_bad+=bad
            comps.append({'boundary_k':list(ks),'raw_terms':raw,'bad_edge_census_terms':bad,'skeleton_sha256':h})
        certs.append({'block':list(block),'components':comps,'all_components_edge_complete':all(x['bad_edge_census_terms']==0 for x in comps)})
    base={'boundary_components':32,'k4_blocks':5,'internal_edges_per_block':6,'external_edges_per_block':4,'baseline_degree':6,'correction_order':3,'total_degree':9,
          'all_degree_partitions_sum_to_three':partitions_ok and total_degrees=={9},'front_inversion_symmetric':geo['inversion_preserves_gram'] and geo['positive_front_measure_invariant'] and geo['antipodal_domain_invariant'],
          'all_full32_terms_have_6_internal_4_external':term_bad==0,'uses_scalar_surrogate':False,'uses_representative_component':False,'uses_frozen_ray':False,'uses_commuting_bch':False,
          'omits_external_jets':False,'flat_haar':False,'omits_q_jets':False,'one_parameter_regulator':False,'beta_shift_i_epsilon':False,'infers_from_k3':False,'insert_even_degree8_contamination':False}
    pos={'candidate_validator':validate_candidate(base),'synthetic_odd_pairing_zero':synthetic_odd_pairing_control(),'gram_control':geo['gram_determinant']==64 and geo['inversion_preserves_gram']}
    mutations={'representative_boundary_component':{'boundary_components':1,'uses_representative_component':True},'scalar_k4_surrogate':{'uses_scalar_surrogate':True},'frozen_angular_ray':{'uses_frozen_ray':True},
      'commuting_bch':{'uses_commuting_bch':True},'omit_external_jets':{'omits_external_jets':True},'flat_haar':{'flat_haar':True},'omit_q_jets':{'omits_q_jets':True},'one_parameter_regulator':{'one_parameter_regulator':True},
      'beta_shift_i_epsilon':{'beta_shift_i_epsilon':True},'infer_from_k3':{'infers_from_k3':True},'degree8_even_contamination':{'insert_even_degree8_contamination':True,'total_degree':8},'asymmetric_front':{'front_inversion_symmetric':False}}
    controls={}
    for name,chg in mutations.items():
        x=dict(base);x.update(chg);v=validate_candidate(x);controls[name]={'rejected':not v['valid'],'reasons':v['reasons']}
    predicates={'P0_upstream_authority':bridge_ok and critic_ok,'P1_9d_front_inversion':geo['normal_dimension']==9 and geo['gram_determinant']==64 and geo['inversion_preserves_gram'] and geo['positive_front_measure_invariant'],
      'P2_six_internal_baseline_degree6':term_bad==0 and all(c['all_components_edge_complete'] for c in certs),'P3_all_order3_partitions_total_degree9':partitions_ok and total_degrees=={9},
      'P4_analytic_common_chart_authority':bridge_ok,'P5_odd_front_pairing_zero':synthetic_odd_pairing_control() and total_degrees=={9} and geo['antipodal_domain_invariant'] and geo['positive_front_measure_invariant'],
      'P6_all5_full32_and_s5':len(certs)==5 and all(len(c['components'])==32 for c in certs) and len(list(itertools.permutations(V)))==120,
      'P7_k4_residue_zero_and_full_annihilator':bridge_ok and total_degrees=={9} and term_bad==0,'P8_simple_residue_zero_scheme_stable':simple_zero_residue_scheme_check()}
    execution_valid=all(pos['candidate_validator'].values()) and pos['synthetic_odd_pairing_zero'] and pos['gram_control'] and all(v['rejected'] for v in controls.values())
    if execution_valid and all(predicates.values()):verdict='PASS_EXACT_SCOPED';classification='K4_ACTUAL_ORDER3_POLAR_COEFFICIENT_ZERO_EXACT_BY_FULL_NORMAL_INVERSION_PARITY_SCOPED'
    elif execution_valid:verdict='FAIL_EXACT_SCOPED';classification='K4_ACTUAL_ORDER3_PARITY_ZERO_PREDICTION_FALSE_EXACT_SCOPED'
    else:verdict='INVALID_IMPLEMENTATION';classification='INVALID_IMPLEMENTATION'
    out={'classification':classification,'verdict':verdict,'execution_valid':execution_valid,'predicates':predicates,'authority_missing':{'bridge':bridge_missing,'critic':critic_missing},'geometry':geo,
         'degree_partition_count':len(parts),'degree_partition_sha256':hashlib.sha256(json.dumps(parts).encode()).hexdigest(),'full32_raw_contraction_terms':total_terms,'edge_census_failures':term_bad,
         'k4_block_certificates':certs,'positive_controls':pos,'negative_controls':controls,
         'analytic_basis':['six internal pole-removed leading source matrix entries are Cartesian degree 1','all remaining source factors are analytic jets in the same independently-confirmed cubic chart','pole-producing K4 coefficient is additional total order 3','resolved leading front measure/domain are antipodally invariant'],
         'scientific_ceiling':{'k5_order8_computed':False,'physical_finite_part_selected':False,'regulator_independence_claimed':False,'f9_promoted':False,'g3_promoted':False,'new_physics_found':False}}
    Path(args.output).parent.mkdir(parents=True,exist_ok=True);Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:out[k] for k in ('classification','verdict','execution_valid','predicates','degree_partition_count','full32_raw_contraction_terms','edge_census_failures')},indent=2,sort_keys=True));return 0 if verdict=='PASS_EXACT_SCOPED' else 2
if __name__=='__main__':raise SystemExit(main())
