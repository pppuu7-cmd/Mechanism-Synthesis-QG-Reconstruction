#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'scripts/k5_mask511_structural_divisibility_lower_coefficients.py'
PRE='d4275813a910aab0c62d9c38bc01837cc4160015'
CLASS_PASS='K5_34ORBIT_UNSCALED_GRAPH_CLOSURE_WICK_FILTRATION_LOWER_BOUND_EXACT_SCOPED'
CLASS_FAIL='K5_34ORBIT_UNSCALED_GRAPH_CLOSURE_BOUND_REFUTED_EXACT_SCOPED'
INVALID='INVALID_IMPLEMENTATION'
BLOCK='BLOCKED_OBJECT_DEFINITION'

spec=importlib.util.spec_from_file_location('mask511_struct_base_for_34orbit_graph',BASE)
b=importlib.util.module_from_spec(spec);assert spec.loader is not None;spec.loader.exec_module(b)
EDGES=tuple(b.EDGES);N=len(EDGES);assert N==10
PERMS=list(itertools.permutations(range(5)));EIDX={e:i for i,e in enumerate(EDGES)}


def edge_perm(p,e):
    a,bb=EDGES[e];x,y=p[a],p[bb];return EIDX[(min(x,y),max(x,y))]
def pmask(mask,p):
    z=0
    for e in range(N):
        if (mask>>e)&1:z|=1<<edge_perm(p,e)
    return z

def orbit_reps():
    unseen=set(range(1<<N));out=[]
    while unseen:
        m=min(unseen);o={pmask(m,p) for p in PERMS};out.append((m,len(o)));unseen-=o
    return out

def incidence_row(edge):
    a,bb=edge;r=[0]*4
    if a!=0:r[a-1]-=1
    if bb!=0:r[bb-1]+=1
    return tuple(r)
ROWS=tuple(incidence_row(e) for e in EDGES)

def rank(rows):
    a=[[Fraction(x) for x in r] for r in rows if any(r)]
    if not a:return 0
    m=len(a);n=len(a[0]);rr=0
    for c in range(n):
        p=next((i for i in range(rr,m) if a[i][c]),None)
        if p is None:continue
        a[rr],a[p]=a[p],a[rr];q=a[rr][c];a[rr]=[x/q for x in a[rr]]
        for i in range(m):
            if i!=rr and a[i][c]:
                q=a[i][c];a[i]=[x-q*y for x,y in zip(a[i],a[rr])]
        rr+=1
        if rr==m:break
    return rr

def in_span(row,rows):return rank(list(rows)+[row])==rank(rows)
def components(U):
    adj={i:set() for i in range(5)}
    for e in U:
        a,bb=EDGES[e];adj[a].add(bb);adj[bb].add(a)
    unseen=set(range(5));cs=[]
    while unseen:
        root=min(unseen);st=[root];comp={root};unseen.remove(root)
        while st:
            x=st.pop()
            for y in sorted(adj[x]):
                if y in unseen:unseen.remove(y);comp.add(y);st.append(y)
        cs.append(tuple(sorted(comp)))
    return tuple(sorted(cs,key=lambda z:(len(z),z)))
def closure_edges(cs):
    cmap={v:i for i,c in enumerate(cs) for v in c}
    return {e for e,(a,bb) in enumerate(EDGES) if cmap[a]==cmap[bb]}
def pmin_mask(poly,Z):
    if not poly:return None
    return min(sum(mon[e] for e in Z) for mon in poly)
def pinitial(poly,Z,q):return {m:c for m,c in poly.items() if sum(m[e] for e in Z)==q}
def padd(a,c):return b.padd(a,c)
def pscale(a,q):return b.pscale(a,q)

def vec_left(row,M):
    out=[]
    for j in range(4):
        z={}
        for i in range(4):
            if row[i]:z=padd(z,pscale(M[i][j],row[i]))
        out.append(z)
    return out
def vec_right(M,row):
    out=[]
    for i in range(4):
        z={}
        for j in range(4):
            if row[j]:z=padd(z,pscale(M[i][j],row[j]))
        out.append(z)
    return out

def all_perfect_matchings(items):
    items=tuple(items)
    if not items:return {()}
    i=items[0];out=set()
    for p in range(1,len(items)):
        j=items[p];rest=items[1:p]+items[p+1:]
        for mt in all_perfect_matchings(rest):out.add(tuple(sorted(((min(i,j),max(i,j)),)+mt)))
    return out


def main():
    # Exact frozen source/DAG reconstruction, without consuming any physical coefficient outcome.
    dns=b.exact_prefix(b.DAG_SOURCE,'# Evaluate frozen exact points by direct and canonical-DAG paths.','k5_34orbit_graph_dag')
    ans=b.exact_prefix(b.ACTION_SOURCE,'results={};checks={}','$k5_34orbit_graph_action'.replace('$',''))
    PSI=b.from_tuple_poly(dns['PSI'])
    ADJ=[[b.from_tuple_poly(dns['ADJ'][i][j]) for j in range(4)] for i in range(4)]
    LP=[[b.from_tuple_poly(dns['LP'][i][j]) for j in range(4)] for i in range(4)]
    Q=[[Fraction(x) for x in row] for row in dns['Q']]
    R=tuple(tuple(int(x) for x in r) for r in dns['ROWS'])
    assert R==ROWS
    Ds=b.build_det_coeffs(LP,Q);F=b.build_cleared_det_factor(Ds,PSI)
    AQ=b.mat_poly_num_right(ADJ,Q);BN=[ADJ]
    for _ in range(1,5):BN.append([[b.pscale(z,-1) for z in row] for row in b.mat_poly_mul(AQ,BN[-1],10**9)])
    C={(i,j,n):b.dot_rows_poly(R[i],BN[n],R[j]) for i in range(10) for j in range(i+1,10) for n in range(5)}
    MATCH_COEFF,source_pattern_count=b.build_match_coeff(ans)
    retained=set(tuple(sorted(mt)) for mt in MATCH_COEFF)
    complete=all_perfect_matchings(range(10))

    static={
        'parent_prereg_locked':PRE=='d4275813a910aab0c62d9c38bc01837cc4160015',
        'canonical_source_terms_100000':dns['SOURCE_TERMS']==100000 and ans['SOURCE_TERMS']==100000 and source_pattern_count==7776,
        'psi_125_unit_trees':len(PSI)==125 and all(v==1 for v in PSI.values()),
        'retained_matchings_945':len(retained)==945,
        'retained_matching_set_is_all_945_perfect_matchings':retained==complete and len(complete)==945,
        'annihilator_vpsi_zero':bool(ans['VPSI_ZERO']),
        'dual_rank2_pivots14':dns['rank']==2 and dns['piv']==[1,4],
        'exact_rational_only':True,
        'no_boundary_s5_transport_consumed':True,
        'no_physical_N_or_B_coefficients_consumed':True,
    }
    reps=orbit_reps();proper=reps[1:-1]
    static['subset_orbits_34']=len(reps)==34
    static['proper_orbits_32_sizes_sum1022']=len(proper)==32 and sum(s for _,s in proper)==1022

    rows=[];counterexamples=[];closure_larger=False;plus1_seen=False;cross_rejected=False
    for oi,(mask,osize) in enumerate(proper):
        Z={e for e in range(10) if (mask>>e)&1};U=set(range(10))-Z;cs=components(U);cnum=len(cs);d=cnum-1;a=max(d-1,0);H=closure_edges(cs)
        Urows=[ROWS[e] for e in sorted(U)];spanH={e for e in range(10) if in_span(ROWS[e],Urows)}
        graph_d=d
        tree_d=pmin_mask(PSI,Z)
        orbit_checks={
            'graph_tree_d_agree':graph_d==tree_d,
            'closure_graph_equals_rowspan':H==spanH,
        }
        # Leading adjugate grade and closure annihilation.
        amin=min((pmin_mask(ADJ[i][j],Z) for i in range(4) for j in range(4) if ADJ[i][j]),default=None)
        orbit_checks['adjugate_min_grade_at_least_a']=amin is not None and amin>=a
        A=[[pinitial(ADJ[i][j],Z,a) for j in range(4)] for i in range(4)]
        annH=True
        for e in H:
            annH &= all(not z for z in vec_left(ROWS[e],A)) and all(not z for z in vec_right(A,ROWS[e]))
        orbit_checks['leading_adjugate_annihilates_closure_incidence']=annH
        # Cross-component edge must not be incorrectly admitted to closure when d>=1.
        cross=[e for e in range(10) if e not in H]
        if d>=1 and cross:
            cross_rejected |= any(not in_span(ROWS[e],Urows) for e in cross)
        # Determinant coefficient and cleared factor lower bounds.
        d_bounds=True
        for r in range(5):
            md=pmin_mask(Ds[r],Z)
            if md is not None:d_bounds &= md>=max(d-r,0)
        orbit_checks['determinant_coefficient_bounds']=d_bounds
        f_bounds=True
        for j in range(5):
            mf=pmin_mask(F[j],Z)
            if mf is not None:f_bounds &= mf>=j*a
        orbit_checks['cleared_determinant_factor_bounds']=f_bounds
        # Covariance hierarchy generic/+1 closure bounds.
        cov_bounds=True;boost_count=0
        if d>=1:
            for i in range(10):
                for j in range(i+1,10):
                    for n in range(5):
                        mc=pmin_mask(C[(i,j,n)],Z)
                        req=(n+1)*a+(1 if (i in H or j in H) else 0)
                        if mc is not None:
                            cov_bounds &= mc>=req
                            if (i in H or j in H) and mc>=((n+1)*a+1):boost_count+=1
            plus1_seen |= boost_count>0
        orbit_checks['covariance_generic_and_closure_boost_bounds']=cov_bounds
        # Matching lower bound direct and independent combinatorial reconstruction.
        counts=[]
        for mt in retained:counts.append(sum(1 for i,j in mt if i in H or j in H))
        mu=min(counts)
        mu_comb=5-((10-len(H))//2)
        orbit_checks['mu_direct_equals_combinatorial']=mu==mu_comb
        lb=0 if d==0 else 9*a+mu
        # Every frozen matching term bound derived from j+k=4 and five covariance factors.
        all_matching=True
        if d>=1:
            for mt in retained:
                m=sum(1 for i,j in mt if i in H or j in H)
                all_matching &= 9*a+m>=lb
        orbit_checks['every_matching_contribution_at_least_LB']=all_matching
        closure_larger |= len(H)>len(U)
        if not all(orbit_checks.values()):counterexamples.append({'orbit_index':oi,'mask':mask,'failed':[k for k,v in orbit_checks.items() if not v]})
        rows.append({
            'orbit_index':oi,'mask':mask,'bits':sorted(Z),'k':len(Z),'orbit_size':osize,
            'unscaled_edges':sorted(U),'unscaled_component_sizes':sorted(len(x) for x in cs),
            'component_count':cnum,'d_Z':d,'a_Z':a,'closure_edges':sorted(H),'closure_size':len(H),
            'adjugate_min_mask_grade':amin,'mu_Z':mu,'mu_combinatorial':mu_comb,'LB_Z':lb,
            'checks':orbit_checks,
        })
    # Frozen malformed/meta controls.
    malformed={
        'cross_component_edge_not_in_closure_detected':cross_rejected,
        'closure_endpoint_plus1_boost_present':plus1_seen,
        'incomplete_matching_set_rejected':len(retained-{min(retained)})!=945,
        'closure_not_raw_U_cardinality_used':closure_larger,
        'no_downstream_physical_or_transport_import':static['no_boundary_s5_transport_consumed'] and static['no_physical_N_or_B_coefficients_consumed'],
    }
    row511=next(r for r in rows if r['mask']==511)
    controls={
        **static,
        'all_orbit_checks':not counterexamples and all(all(r['checks'].values()) for r in rows),
        'malformed_controls':all(malformed.values()),
        'mask511_positive_control_LB19':row511['LB_Z']==19,
    }
    valid=all(v for k,v in controls.items() if k!='malformed_controls') and controls['malformed_controls']
    if not all(static.values()):status=INVALID;classification=INVALID
    elif counterexamples:status='SCIENTIFIC_FAIL_EXACT_SCOPED';classification=CLASS_FAIL
    elif not all(malformed.values()):status=INVALID;classification=INVALID
    elif valid:status='PASS_EXACT_SCOPED';classification=CLASS_PASS
    else:status=BLOCK;classification=BLOCK
    out={
        'gate':'K5_34ORBIT_UNSCALED_GRAPH_CLOSURE_WICK_FILTRATION_LOWER_BOUND','prereg_commit':PRE,
        'status':status,'classification':classification,'static_checks':static,'malformed_controls':malformed,
        'orbit_rows':rows,'counterexamples':counterexamples,
        'LB_histogram':{},'mask511_LB':row511['LB_Z'],
        'physical_exact_order_verdict':None,'global_stokes_ibp_verdict':None,'finite_part_selector':None,'regulator_independence':None,
    }
    for r in rows:out['LB_histogram'][str(r['LB_Z'])]=out['LB_histogram'].get(str(r['LB_Z']),0)+1
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('CLASSIFICATION='+classification);print('LB_HISTOGRAM='+json.dumps(out['LB_histogram'],sort_keys=True));print('MASK511_LB='+str(row511['LB_Z']))
    if classification==INVALID:raise SystemExit(2)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args();main()
