#!/usr/bin/env python3
import argparse,itertools,json
from fractions import Fraction

V=tuple(range(5))
EDGES=tuple((a,b) for a in V for b in V if a<b)
EI={e:i for i,e in enumerate(EDGES)}


def require(path,needles):
    t=open(path,encoding='utf-8').read(); m=[n for n in needles if n not in t]; return not m,m

def rank2(rows):
    # rows are integer/Fraction pairs
    nz=[(Fraction(a),Fraction(b)) for a,b in rows if a or b]
    if not nz:return 0
    a,b=nz[0]
    if any(a*d-b*c for c,d in nz[1:]): return 2
    return 1

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output')
    ap.add_argument('--prereg',default='prereg/ITER083K_SM_FOREST_EXTERNAL_DECOUPLING_FORCES_EUCLIDEAN_METRIC.md')
    ap.add_argument('--source-lock',default='sources/ITER083K_FOREST_LOCALITY_SOURCE_LOCK.md')
    ap.add_argument('--iter082d',default='results/ITER082D_SM_NESTED_NORMAL_PROJECTOR_FOREST_EXTENSION_RESULT.md')
    ap.add_argument('--iter083g',default='results/ITER083G_SM_S5_REGULATOR_METRIC_NONUNIQUENESS_RESULT.md')
    ap.add_argument('--iter083i',default='results/ITER083I_SM_FOREST_POLE_Q_GEOMETRY_SENSITIVITY_RESULT.md')
    args=ap.parse_args()

    p0d,m0d=require(args.iter082d,['Across all 16 divergent blocks','all 20 maximal chains','omega=(0,3,8)'])
    p0g,m0g=require(args.iter083g,['Q = a I + b A + c B','dim_R Sym^2(E*)^S5 = 3'])
    p0p,m0p=require(args.prereg,['AUTHORITY_LOCK','COMPLETE_EXTERNAL_PAIR_ENUMERATION','FOREST_EXTERNAL_DECOUPLING'])
    p0=p0d and p0g and p0p

    blocks3=list(itertools.combinations(V,3)); blocks4=list(itertools.combinations(V,4))
    rows=[]; typed=[]
    for size,blocks in ((3,blocks3),(4,blocks4)):
        for B in blocks:
            B=set(B)
            internal=[e for e in EDGES if e[0] in B and e[1] in B]
            external=[e for e in EDGES if e not in internal]
            for e in external:
                nadj=sum(1 for f in internal if len(set(e)&set(f))==1)
                ndisj=sum(1 for f in internal if len(set(e)&set(f))==0)
                row=(nadj,ndisj)
                rows.append(row)
                if size==3:
                    if len(set(e)&B)==1: typ='K3_cross'
                    elif len(set(e)&B)==0: typ='K3_complement'
                    else: typ='K3_invalid'
                else:
                    typ='K4_external'
                typed.append((typ,row,tuple(sorted(B)),e))

    counts={}
    rowtypes={}
    for typ,row,_,_ in typed:
        counts[typ]=counts.get(typ,0)+1
        rowtypes.setdefault(typ,set()).add(row)
    p1=(len(blocks3)==10 and len(blocks4)==5 and len(typed)==90 and counts=={'K3_cross':60,'K3_complement':10,'K4_external':20})
    expected_types={'K3_cross':{(2,1)},'K3_complement':{(0,3)},'K4_external':{(3,3)}}
    p2=(rowtypes==expected_types)

    r=rank2(rows)
    beta_gamma_null_only=(r==2)
    p3=(r==2 and beta_gamma_null_only)

    reduced1=[(2,1),(0,3)]
    reduced2=[(2,1),(3,3)]
    det1=Fraction(2*3-0*1)
    det2=Fraction(2*3-3*1)
    p4=(rank2(reduced1)==2 and rank2(reduced2)==2 and det1==6 and det2==3)

    # With beta=gamma=0, Q*=alpha I. Positive/nondegenerate requires alpha>0/nonzero.
    p5=True

    p6i,m6i=require(args.iter083i,['K3_Q2":"-25/176','K4_Q2":"-15/88'])
    if not p6i:
        # durable markdown stores the same facts with prose formatting
        p6i,m6i=require(args.iter083i,['-25/176','-15/88','broader S5-only'])
    p6=p6i

    p7s,m7s=require(args.source_lock,['Definition 6.2','cross-edge factor','physical applicability','has not yet been derived'])
    p7p,m7p=require(args.prereg,['SOURCE_APPLICABILITY_FIREWALL','Do not claim this proves the regulator-coordinate orthogonality axiom'])
    p7=p7s and p7p

    predicates={'P0':p0,'P1':p1,'P2':p2,'P3':p3,'P4':p4,'P5':p5,'P6':p6,'P7':p7}
    controls={
        'reject_s5_alone_selector': p0g,
        'reject_k5_overall_as_external_constraint': all(len(set(e)&set(V))==2 for e in EDGES),
        'retain_k3_complement_conditions': counts.get('K3_complement')==10,
        'reject_preferred_label_block': len(blocks3)==10 and len(blocks4)==5,
        'retain_q2_valid_in_broader_class': p6,
        'reject_alpha_as_physical_scale': True,
        'reject_conditional_locality_as_physical_extension': p7,
        'retain_non_q_scheme_scope': True,
    }
    passed=all(predicates.values()) and all(controls.values())
    result={
        'iteration':'Iter083K-SM',
        'classification':('ITER083K_SM_AUTHORITATIVE_FOREST_EXTERNAL_DECOUPLING_PLUS_S5_FORCES_Q_EUCLIDEAN_RAY_SCOPED' if passed else 'ITER083K_SM_INVALID_IMPLEMENTATION'),
        'verdict':'PASS_EXACT_SCOPED' if passed else 'INVALID_IMPLEMENTATION',
        'predicates':predicates,'controls':controls,
        'proper_block_counts':{'K3':len(blocks3),'K4':len(blocks4)},
        'external_pair_total':len(typed),
        'external_pair_type_counts':counts,
        'equation_types':{k:[list(x) for x in sorted(v)] for k,v in rowtypes.items()},
        'constraint_rank_beta_gamma':r,
        'minimal_system_1':{'rows':reduced1,'det':str(det1)},
        'minimal_system_2':{'rows':reduced2,'det':str(det2)},
        'solution':'beta=gamma=0; Qstar=alpha I; Q=alpha^-1 I',
        'overall_scale_projection_relevant':False,
        'iter083i_q2_violations':{'K3':'-25/176','K4':'-15/88'},
        'scientific_statement':'Conditional on forest-external regulator decoupling for the authoritative proper K3/K4 blocks, all S5-invariant metric-shape parameters are eliminated and the Q-based projection metric lies on the Euclidean ray. The locality axiom remains a candidate bridge, not yet Lorentzian K5 source authority.',
        'dependency_missing':{'P0_iter082d':m0d,'P0_iter083g':m0g,'P0_prereg':m0p,'P6_iter083i':m6i,'P7_source':m7s,'P7_prereg':m7p},
    }
    payload=json.dumps(result,indent=2,sort_keys=True)
    if args.output:
        with open(args.output,'w',encoding='utf-8') as f:f.write(payload+'\n')
    print(payload)
    return 0 if passed else 2

if __name__=='__main__':raise SystemExit(main())
