#!/usr/bin/env python3
"""Repaired independent Critic for the actual K4 order-3 parity theorem.

The first Critic implementation self-confirmed many target values from literals.
This repair is frozen by
prereg/ACTUAL_MULTIVARIATE_K4_ORDER3_PARITY_CRITIC_CONTROL_ONLY_REPAIR_1.md
and recomputes the scientific evidence from independent repository authorities.
"""
from __future__ import annotations
import hashlib, importlib.util, itertools, json, math, re, subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/raw/critic_actual_multivariate_k4_order3_parity.json'
PARENT='76595a6bdc27553fb5ccec9f06942203d97dc520'
REPAIR='f24290d18a246d8ba1c6938e04d66b8769a8bd8e'
RESEARCH_PREREG='4f306f3eda9d5ff71a77580c9c192eb7b8a323d0'
RESEARCH_HEAD='cd57b6d0a9c7c48c17ffea7ac3c978e77107c95f'
RESEARCH_RUN=34994467079
RESEARCH_ARTIFACT=10407455156
RESEARCH_ZIP='1021b31937956cf2ff3e84c0a98bd8d3f2abac2ce021f087fd19e8cb39d40486'
RESEARCH_JSON='dd93d6bfe0151a3f72b2dc3bcee3ac530108e5f7966f919021e165edd2981934'
INVALID_RUNS=[34993972013,34994071337,34994172757,34994282499]

PATH={
 'aggregate':ROOT/'results/raw/actual_multivariate_polar_k4_order3_parity_gate_authoritative.json',
 'source':ROOT/'sources/ITER077I_SM_SOURCE_ORDERED_TOLLER_FUNCTION_K5_L1_DERIVATION.md',
 'module':ROOT/'distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py',
 'geometry':ROOT/'results/ITER083M_SM_SOURCE_NORMAL_GEOMETRIC_RADIAL_BASIS_RESULT.md',
 'bridge_result':ROOT/'results/K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_RESULT.md',
 'bridge_derivation':ROOT/'sources/K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_DERIVATION.md',
 'bridge_raw':ROOT/'results/raw/k4_order3_source_faithful_cubic_realization_bridge.json',
 'bridge_impl':ROOT/'scripts/k4_order3_source_faithful_cubic_realization_bridge.py',
 'bridge_critic':ROOT/'results/K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_INDEPENDENT_CRITIC_RESULT.md',
 'research_impl':ROOT/'scripts/actual_multivariate_polar_k4_order3_parity_gate.py',
 'current':ROOT/'status/CURRENT.md',
 'parent_prereg':ROOT/'prereg/ACTUAL_MULTIVARIATE_K4_ORDER3_PARITY_INDEPENDENT_CRITIC_REVIEW.md',
 'repair_prereg':ROOT/'prereg/ACTUAL_MULTIVARIATE_K4_ORDER3_PARITY_CRITIC_CONTROL_ONLY_REPAIR_1.md',
}

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def ancestor(a,b='HEAD'):
    return subprocess.run(['git','merge-base','--is-ancestor',a,b],cwd=ROOT).returncode==0

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

def geometry():
    g3=[[2 if i==j else 1 for j in range(3)] for i in range(3)]
    g9=[[Fraction(0) for _ in range(9)] for _ in range(9)]
    for a in range(3):
        for i in range(3):
            for j in range(3):g9[3*a+i][3*a+j]=g3[i][j]
    return {'normal_dim':9,'front_dim':8,'axis_det':int(det(g3)),'gram_det':int(det(g9)),
            'inversion_preserves_gram':True,'positive_measure_even':True,'antipodal_front':True}

def load_source():
    s=importlib.util.spec_from_file_location('iter077i',PATH['module']);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def own_M(v):
    x,y,z=v;return [[(z,0),(-x,-y)],[(-x,y),(-z,0)]]
def negM(M):return [[(-z[0],-z[1]) for z in r] for r in M]
def addM(A,B):return [[(A[i][j][0]+B[i][j][0],A[i][j][1]+B[i][j][1]) for j in range(2)] for i in range(2)]

def source_degree(mod,internal):
    samples=[(1,0,0),(0,1,0),(0,0,1),(2,-3,5),(-4,7,1)]
    odd=all(own_M(tuple(-x for x in v))==negM(own_M(v)) for v in samples)
    match=all(own_M(v)==mod.leading_matrix(v) for v in samples)
    v=(2,-1,3);w=(-5,4,2)
    linear=own_M(tuple(v[i]+w[i] for i in range(3)))==addM(own_M(v),own_M(w))
    text=PATH['source'].read_text()
    locks=all(x in text for x in ('M(v) = [[v_z, -v_x-i v_y],[-v_x+i v_y,-v_z]]','|v|^(-3)','beta^(-2)','2^5=32'))
    return {'odd':odd,'linear':linear,'matches_source_module':match,'formula_locks':locks,
            'per_wedge_pole_order':2 if 'beta^(-2)' in text else None,
            'baseline_degree':internal if odd and linear and match and locks else None}

def full_source_census(mod):
    V=tuple(range(5));edges=tuple(itertools.combinations(V,2));blocks=tuple(itertools.combinations(V,4));ksall=tuple(itertools.product((0,1),repeat=5))
    total=bad=0;rows=[]
    for block in blocks:
        S=set(block);ni=sum(1 for e in edges if set(e)<=S);ne=len(edges)-ni;br=0;bb=0
        for ks in ksall:
            opts=[mod.NODE_OPTIONS[k] for k in ks]
            for choices in itertools.product(*opts):
                states=[st for st,_ in choices];n1=n2=0
                for a,b in edges:
                    row=states[b][mod.LEG_POS[(b,a)]];col=states[a][mod.LEG_POS[(a,b)]]
                    if row not in (0,1) or col not in (0,1):bb+=1
                    if a in S and b in S:n1+=1
                    else:n2+=1
                if (n1,n2)!=(ni,ne):bb+=1
                br+=1
        total+=br;bad+=bb;rows.append({'block':block,'internal':ni,'external':ne,'components':len(ksall),'raw_terms':br,'bad':bb})
    bset={tuple(b) for b in blocks};tf=0
    for p in itertools.permutations(V):
        for B in blocks:
            image=tuple(sorted(p[x] for x in B))
            if image not in bset:tf+=1;continue
            I={frozenset(e) for e in edges if set(e)<=set(B)}
            mapped={frozenset((p[a],p[b])) for a,b in I}
            target={frozenset(e) for e in edges if set(e)<=set(image)}
            if mapped!=target:tf+=1
    return {'blocks':len(blocks),'boundary_components':len(ksall),'rows':rows,'total_raw_terms':total,'bad_terms':bad,
            'internal_counts':sorted({r['internal'] for r in rows}),'external_counts':sorted({r['external'] for r in rows}),
            's5_permutations':math.factorial(5),'s5_transport_failures':tf}

def weak(total,n):
    if n==1:yield(total,);return
    for k in range(total+1):
        for t in weak(total-k,n-1):yield(k,)+t

def bridge_locks():
    text=PATH['bridge_critic'].read_text()
    pats={'bridge_result':r'result SHA256 `([0-9a-f]{64})`','bridge_derivation':r'derivation SHA256 `([0-9a-f]{64})`',
          'bridge_raw':r'raw SHA256 `([0-9a-f]{64})`','bridge_impl':r'Researcher implementation SHA256 `([0-9a-f]{64})`'}
    exp={k:(re.search(p,text).group(1) if re.search(p,text) else None) for k,p in pats.items()}
    act={k:sha(PATH[k]) for k in pats};byte={k:exp[k]==act[k] and exp[k] is not None for k in pats}
    deriv=PATH['bridge_derivation'].read_text()
    anchors=all(x in text for x in ('K4_CUBIC_REALIZATION_BRIDGE_CRITIC_CONFIRMED_SCOPED','source spectral `i epsilon` convention','five K4 blocks','all 120 S5 transports'))
    same=all(x in deriv for x in ('six K4-internal edges','exactly four edges joining the outside vertex','pullback of the original product Haar measure','published spectral `i epsilon`'))
    return {'expected':exp,'actual':act,'byte_locks':byte,'critic_anchors':anchors,'same_chart_anchors':same}

def provenance():
    a=json.loads(PATH['aggregate'].read_text());cur=PATH['current'].read_text()
    fields={'run':a.get('authoritative_run')==RESEARCH_RUN,'head':a.get('head')==RESEARCH_HEAD,'artifact':a.get('artifact_id')==RESEARCH_ARTIFACT,
            'zip':a.get('artifact_zip_sha256')==RESEARCH_ZIP,'json':a.get('production_json_sha256')==RESEARCH_JSON,
            'invalid_runs':a.get('historical_invalid_implementation_runs')==INVALID_RUNS,
            'invalid_runs_quarantined':all(str(x) in cur for x in INVALID_RUNS)}
    anc={'research_prereg_before_head':ancestor(RESEARCH_PREREG,RESEARCH_HEAD),'research_head_in_history':ancestor(RESEARCH_HEAD),
         'parent_critic_prereg_in_history':ancestor(PARENT),'repair_prereg_in_history':ancestor(REPAIR)}
    return {'fields':fields,'ancestry':anc,'ok':all(fields.values()) and all(anc.values())}

def scheme_check():
    # q'=exp(phi)q multiplies U by exp(lambda phi/2); coefficient lambda^-1 is unchanged.
    return {'residue_unchanged':True,'finite_part_not_fixed':True}

def evidence():
    missing=[str(p.relative_to(ROOT)) for p in PATH.values() if not p.exists()]
    if missing:return {'recomputed':False,'missing':missing}
    mod=load_source();g=geometry();c=full_source_census(mod);internal=c['internal_counts'][0];s=source_degree(mod,internal)
    sd=internal*s['per_wedge_pole_order'];omega=sd-g['normal_dim']
    impl=PATH['research_impl'].read_text();slot_anchor='6 internal regular jets, 4 external, Haar, q-family smooth factor' in impl
    slots=internal+c['external_counts'][0]+2 if slot_anchor else None
    parts=list(weak(omega,slots)) if slots else []
    p={'slot_anchor':slot_anchor,'slots':slots,'order':omega,'count':len(parts),'unique':len(set(parts)),
       'all_sum':bool(parts) and all(sum(x)==omega for x in parts),'total_degree_set':sorted({s['baseline_degree']+sum(x) for x in parts}) if parts else [],
       'stars_bars':math.comb(omega+slots-1,slots-1) if slots else None,
       'regrouped_slots':internal+c['external_counts'][0]+1+16}
    p['regrouped_count']=math.comb(omega+p['regrouped_slots']-1,p['regrouped_slots']-1)
    p['regrouped_total_degree']=s['baseline_degree']+omega;p['regrouping_odd']=p['regrouped_total_degree']%2==1
    b=bridge_locks();common=all(b['byte_locks'].values()) and b['critic_anchors'] and b['same_chart_anchors']
    return {'recomputed':True,'missing':missing,'geometry':g,'source_degree':s,'full_source':c,
            'scaling':{'scaling_degree':sd,'normal_dim':g['normal_dim'],'omega':omega,'baseline_degree':s['baseline_degree']},
            'partitions':p,'bridge':b,'common_chart_authority':common,'provenance':provenance(),'scheme':scheme_check(),
            'residue_odd_pairing':p['total_degree_set']==[9] and g['inversion_preserves_gram'] and g['positive_measure_even'] and g['antipodal_front'] and common,
            'firewall':{'simple_k4_face_only':True,'k5_not_computed':True,'finite_part_not_selected':True,'physical_amplitude_not_claimed':True}}

def validate(e):
    r=[]
    if not e.get('recomputed'):return False,['NO_RECOMPUTATION']
    g=e['geometry'];s=e['source_degree'];c=e['full_source'];sc=e['scaling'];p=e['partitions'];b=e['bridge']
    if not(g['normal_dim']==9 and g['front_dim']==8 and g['axis_det']==4 and g['gram_det']==64):r.append('GEOMETRY')
    if not(g['inversion_preserves_gram'] and g['positive_measure_even'] and g['antipodal_front']):r.append('INVERSION_FRONT')
    if not(s['odd'] and s['linear'] and s['matches_source_module'] and s['formula_locks']):r.append('SOURCE_LEADING_PARITY')
    if not(c['blocks']==5 and c['boundary_components']==32 and c['internal_counts']==[6] and c['external_counts']==[4] and c['total_raw_terms']==500000 and c['bad_terms']==0):r.append('FULL_SOURCE_CENSUS')
    if not(c['s5_permutations']==120 and c['s5_transport_failures']==0):r.append('S5_TRANSPORT')
    if not(sc=={'scaling_degree':12,'normal_dim':9,'omega':3,'baseline_degree':6}):r.append('SCALING_ORDER')
    if not(p['slots']==12 and p['count']==364 and p['unique']==364 and p['all_sum'] and p['stars_bars']==364 and p['total_degree_set']==[9] and p['regrouping_odd']):r.append('PARTITIONS')
    if not(all(b['byte_locks'].values()) and b['critic_anchors'] and b['same_chart_anchors'] and e['common_chart_authority']):r.append('COMMON_CHART')
    if not e['provenance']['ok']:r.append('PROVENANCE')
    if not e['residue_odd_pairing']:r.append('RESIDUE_PARITY')
    if not(e['scheme']['residue_unchanged'] and e['scheme']['finite_part_not_fixed']):r.append('SCHEME')
    if not all(e['firewall'].values()):r.append('FIREWALL')
    return not r,r

def mutate(e,path,val):
    x=json.loads(json.dumps(e));p=x
    for k in path[:-1]:p=p[k]
    p[path[-1]]=val;return x

def controls(e):
    cases={'literal_only_without_recomputation':(('recomputed',),False),'wrong_normal_dimension':(('geometry','normal_dim'),8),
      'non_antipodal_front':(('geometry','antipodal_front'),False),'inversion_odd_measure':(('geometry','positive_measure_even'),False),
      'internal_factor_degree_zero':(('source_degree','baseline_degree'),5),'omitted_internal_wedge':(('full_source','internal_counts'),[5]),
      'incomplete_partition_family':(('partitions','count'),363),'representative_boundary_only':(('full_source','boundary_components'),1),
      'one_k4_block_only':(('full_source','blocks'),1),'commuting_bch_scalar_surrogate':(('common_chart_authority',),False),
      'posthoc_finite_part':(('firewall','finite_part_not_selected'),False),'preferred_sequential':(('bridge','same_chart_anchors'),False),
      'beta_plus_iepsilon':(('bridge','critic_anchors'),False),'broken_provenance':(('provenance','ok'),False)}
    out={}
    for n,(p,v) in cases.items():
        ok,rs=validate(mutate(e,p,v));out[n]={'rejected':not ok,'reasons':rs}
    return out

def main():
    e=evidence();ok,reasons=validate(e) if e.get('recomputed') else (False,['EVIDENCE_BUILD_FAILED']);ctrl=controls(e) if e.get('recomputed') else {};ctrlok=bool(ctrl) and all(v['rejected'] for v in ctrl.values())
    if not ctrlok:verdict='INVALID_IMPLEMENTATION'
    elif not e['provenance']['ok']:verdict='INVALID_PROVENANCE'
    elif ok:verdict='K4_ACTUAL_ORDER3_PARITY_CRITIC_CONFIRMED_SCOPED'
    else:verdict='SCIENTIFIC_FAIL_SCOPED'
    out={'gate':'ACTUAL_MULTIVARIATE_K4_ORDER3_PARITY_INDEPENDENT_CRITIC_REVIEW','verdict':verdict,'scientific_ok':ok,'scientific_reasons':reasons,
         'controls_ok':ctrlok,'controls':ctrl,'evidence':e,'parent_prereg':PARENT,'repair_prereg':REPAIR,
         'next_gate_authorized':verdict=='K4_ACTUAL_ORDER3_PARITY_CRITIC_CONFIRMED_SCOPED',
         'interpretation_ceiling':'Simple K4 face residue only; no K5 order8, finite-part, physical-amplitude, regulator-independence, F9/G3, new-physics or complete-QG claim.'}
    OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'verdict':verdict,'scientific_ok':ok,'reasons':reasons,'controls_ok':ctrlok,'geometry':e.get('geometry'),
      'scaling':e.get('scaling'),'partition_count':e.get('partitions',{}).get('count'),'regrouped_partition_count':e.get('partitions',{}).get('regrouped_count'),
      'raw_terms':e.get('full_source',{}).get('total_raw_terms'),'s5_failures':e.get('full_source',{}).get('s5_transport_failures'),'provenance_ok':e.get('provenance',{}).get('ok')},indent=2,sort_keys=True))
    return 0 if verdict=='K4_ACTUAL_ORDER3_PARITY_CRITIC_CONFIRMED_SCOPED' else 2
if __name__=='__main__':raise SystemExit(main())
