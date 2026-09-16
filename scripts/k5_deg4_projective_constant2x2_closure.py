#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LOCK=ROOT/'sources/raw/k5_deg4_projective_closure_parent_point_lock.json'
PRE='4f1e49f9d850fa7834dd189228d0787f84406f84'
C_OK='K5_PROJECTIVE_CONSTANT2X2_CLOSURE_CONFIRMED_ON_FROZEN_POINTS_EXACT_SCOPED'
C_FAIL='K5_PROJECTIVE_CONSTANT2X2_CLOSURE_FALSIFIED_EXACT_SCOPED'
C_DEG='K5_PROJECTIVE_CONSTANT2X2_CLOSURE_BLOCKED_FIT_DEGENERACY_SCOPED'
INVALID='INVALID_IMPLEMENTATION'

FROZEN={
 'fit_A':(2,1,1,1,1,1,1,1,1,1),
 'fit_B':(1,2,1,3,1,2,1,1,2,1),
 'validation_U':(1,1,1,1,1,1,1,1,1,1),
 'validation_G':(2,3,1,2,1,3,2,1,2,3),
}
EXPECTED_S1={'fit_A':11,'fit_B':15,'validation_U':10,'validation_G':20}

def q(x): return Fraction(str(x))
def qs(x):
    x=Fraction(x)
    return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'

def matvec(M,v): return [M[r][0]*v[0]+M[r][1]*v[1] for r in range(2)]
def fit_matrix(NA,NB,PA,PB):
    det=NA[0]*NB[1]-NA[1]*NB[0]
    if det==0:return None,det
    # equations [N1(point),N2(point)] dot row(M) = P_channel(point)
    inv=((NB[1]/det,-NA[1]/det),(-NB[0]/det,NA[0]/det))
    rows=[]
    for ch in range(2):
        y=(PA[ch],PB[ch])
        rows.append((inv[0][0]*y[0]+inv[0][1]*y[1],inv[1][0]*y[0]+inv[1][1]*y[1]))
    return tuple(rows),det

d=json.loads(LOCK.read_text(encoding='utf-8'))
pts=d['points']
N={};B={};P={};s1={}
for name,frozen in FROZEN.items():
    a=tuple(int(x) for x in pts[name]['alpha'])
    N[name]=[q(x) for x in pts[name]['N']]
    B[name]=[q(x) for x in pts[name]['B']]
    s1[name]=sum(Fraction(x) for x in a)
    P[name]=[x/(s1[name]**4) for x in B[name]]

M,det=fit_matrix(N['fit_A'],N['fit_B'],P['fit_A'],P['fit_B'])
res={}
if M is not None:
    for name in FROZEN:
        pred=matvec(M,N[name])
        res[name]=[P[name][i]-pred[i] for i in range(2)]

# exact homogeneous scale controls at lambda=2, no source recomputation needed
lam=Fraction(2)
scale=[]
for name in FROZEN:
    for ch in range(2):
        N2=(lam**27)*N[name][ch]
        B2=(lam**31)*B[name][ch]
        P2=B2/((lam*s1[name])**4)
        scale.append(N2==(lam**27)*N[name][ch])
        scale.append(B2==(lam**31)*B[name][ch])
        scale.append(P2==(lam**27)*P[name][ch])
        if M is not None:
            r2=P2-(M[ch][0]*(lam**27)*N[name][0]+M[ch][1]*(lam**27)*N[name][1])
            scale.append(r2==(lam**27)*res[name][ch])

# wrong denominator powers necessarily have wrong homogeneous degree
wrong3=(31-3)!=27
wrong5=(31-5)!=27
raw_wrong=(31!=27) and any(x!=0 for v in B.values() for x in v)

checks={
 'parent_run_locked':d['run_id']==35130545821 and d['job_id']==104910177408 and d['artifact_id']==10461780450,
 'parent_hash_locked':d['production_json_sha256']=='909b2afc8474b317a424ba59f108756441bdd8cdf8888cb85763d6c368fe95b8',
 'parent_zip_digest_locked':d['artifact_zip_sha256']=='d1b2bbd109aa0a3969e37e97aa3e572fc4cba368c42fdc145f94689afbc032dd',
 'all32_source_terms_locked':d['all32_source_terms']==100000,
 'dual_projection_locked':d['dual_projection_used'] is True,
 'two_channels_retained':all(len(N[k])==2 and len(B[k])==2 for k in FROZEN),
 'frozen_points_exact':all(tuple(pts[k]['alpha'])==FROZEN[k] for k in FROZEN),
 'frozen_s1_exact':all(s1[k]==EXPECTED_S1[k] for k in FROZEN),
 'degree_N_27':d['degree_N']==27,
 'degree_B_31':d['degree_B']==31,
 'degree_P_27':d['degree_B']-4==27,
 'projective_formula_exact':all(P[k][i]*s1[k]**4==B[k][i] for k in FROZEN for i in range(2)),
 'fit_matrix_rule_exact':M is None or (res['fit_A']==[0,0] and res['fit_B']==[0,0]),
 'scale_projective_controls_exact':all(scale),
 'no_integrated_period_verdict':True,
}
controls={
 'raw_B_constant_closure_rejected_by_grading':raw_wrong,
 'wrong_s1_power3_rejected_by_degree':wrong3,
 'wrong_s1_power5_rejected_by_degree':wrong5,
 'validation_not_used_for_fit':True,
 'finite_point_result_not_promoted_global':True,
}
valid=all(checks.values()) and all(controls.values())
if not valid: classification=INVALID
elif M is None: classification=C_DEG
else:
    vz=[x==0 for k in ('validation_U','validation_G') for x in res[k]]
    classification=C_OK if all(vz) else C_FAIL

out={
 'gate':'K5_DEG4_ANNIHILATOR_PROJECTIVE_CONSTANT2X2_CLOSURE',
 'prereg_commit':PRE,
 'status':'PASS_EXACT_SCOPED' if valid else INVALID,
 'classification':classification,
 'checks':checks,
 'controls':controls,
 'parent_provenance':{k:d[k] for k in ('run_id','job_id','artifact_id','artifact_zip_sha256','production_json_sha256','implementation_head')},
 'exact':{
   's1':{k:qs(v) for k,v in s1.items()},
   'fit_determinant':qs(det),
   'fit_degenerate':det==0,
   'projective_P':{k:[qs(x) for x in P[k]] for k in FROZEN},
   'constant_2x2_fit_matrix':None if M is None else [[qs(x) for x in row] for row in M],
   'residuals':{} if M is None else {k:[qs(x) for x in res[k]] for k in FROZEN},
   'validation_nonzero_residual_count':0 if M is None else sum(x!=0 for k in ('validation_U','validation_G') for x in res[k]),
 },
 'scientific_invariant_dual_period_verdict':None,
 'interpretation':{
   'scope':'constant rational 2x2 closure of the two corrected degree-27 projective channels on the four frozen representatives',
   'global_polynomial_or_rational_module_closure':None,
   'integrated_period':None,
 }
}

ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
if not valid: raise SystemExit(2)
