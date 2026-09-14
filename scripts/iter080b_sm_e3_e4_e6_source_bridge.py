#!/usr/bin/env python3
import argparse, json
from pathlib import Path

MATRIX = Path('research/iter080b_sm_e3_e4_e6_source_matrix.json')
BLOCKED = 'ITER080B_SM_PARENT_E3_E4_E6_STRUCTURES_EXIST_LOCAL_CAUSAL_VERTICES_EXIST_BUT_COMPLETE_MULTIVERTEX_INHERITANCE_BRIDGE_NOT_SOURCE_EXPLICIT_BLOCKED_EXACT_SCOPED'
PASS = 'ITER080B_SM_E3_E4_E6_COMPLETE_CAUSAL_MULTIVERTEX_INHERITANCE_BRIDGE_SOURCE_EXPLICIT_EXACT_SCOPED'
INVALID = 'ITER080B_SM_INVALID_SOURCE_OR_IMPLEMENTATION'

def load():
    d=json.loads(MATRIX.read_text())
    if d.get('frozen_prereg')!='d9b4d8a6c489b2c7560cfad538ff62fd1e4f7b07':
        raise RuntimeError('prereg mismatch')
    return d

def src(d, sid):
    return next(x for x in d['sources'] if x['id']==sid)

def lane_a(d):
    k=src(d,'KKL_PARENT')
    ok=all(k[x] for x in ['parent_e3_explicit','parent_e4_explicit','parent_e6_fixing_exists'])
    return {'lane':'A_PARENT','ok':ok,'parent_e3':k['parent_e3_explicit'],'parent_e4':k['parent_e4_explicit'],'parent_e6':k['parent_e6_fixing_exists']}

def lane_b(d):
    b=src(d,'BCG_2601.23162')
    ok=b['causal_toller_local_vertex'] and b['single_vertex_focus_explicit'] and b['many_vertex_described_as_future_construction']
    return {'lane':'B_BCG','ok':ok,'single_vertex_focus':b['single_vertex_focus_explicit'],'many_vertex_future':b['many_vertex_described_as_future_construction'],'p1_p4':[b[f'p{i}_{name}_explicit'] for i,name in [(1,'many_vertex_causal_functional'),(2,'e3_inheritance'),(3,'e4_inheritance'),(4,'e6_inheritance')]]}

def lane_c(d):
    b=src(d,'BELTRAN_2603.22661v2')
    ok=b['arbitrary_2complex_causal_structure_explicit'] and b['generalized_causal_vertex_explicit'] and b['generalized_causal_vertex_finiteness_open']
    return {'lane':'C_BELTRAN','ok':ok,'arbitrary_2complex_causality':b['arbitrary_2complex_causal_structure_explicit'],'local_generalized_vertex':b['generalized_causal_vertex_explicit'],'finiteness_open':b['generalized_causal_vertex_finiteness_open'],'p1_p4':[b[f'p{i}_{name}_explicit'] for i,name in [(1,'many_vertex_causal_functional'),(2,'e3_inheritance'),(3,'e4_inheritance'),(4,'e6_inheritance')]]}

def lane_d(d):
    b=src(d,'BCG_2601.23162'); c=src(d,'BELTRAN_2603.22661v2'); k=src(d,'KKL_PARENT')
    parent=all(k[x] for x in ['parent_e3_explicit','parent_e4_explicit','parent_e6_fixing_exists'])
    local=b['causal_toller_local_vertex'] and c['causal_toller_local_vertex']
    predicates=[]
    for i,name in [(1,'many_vertex_causal_functional'),(2,'e3_inheritance'),(3,'e4_inheritance'),(4,'e6_inheritance')]:
        predicates.append(bool(b[f'p{i}_{name}_explicit'] or c[f'p{i}_{name}_explicit']))
    complete=parent and local and all(predicates)
    classification=PASS if complete else BLOCKED if parent and local else INVALID
    ceilings=d['frozen_claim_ceiling']
    ok=classification!=INVALID and all(ceilings.values())
    return {'lane':'D_AGGREGATE_LOGIC','ok':ok,'parent_structures':parent,'local_causal_vertices':local,'P1_P4_corpus_explicit':predicates,'classification':classification,'claim_ceiling':ceilings}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--lane',choices=['A','B','C','D','aggregate'],required=True); a=p.parse_args()
    d=load(); funcs={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}
    if a.lane=='aggregate':
        rows=[funcs[x](d) for x in 'ABCD']; ok=all(r['ok'] for r in rows); out={'gate':'Iter080B-SM','valid':ok,'lanes':rows,'classification':rows[-1]['classification'] if ok else INVALID}
    else:
        out=funcs[a.lane](d)
    print(json.dumps(out,indent=2,sort_keys=True))
    if not out.get('ok',out.get('valid',False)): raise SystemExit(2)

if __name__=='__main__': main()
